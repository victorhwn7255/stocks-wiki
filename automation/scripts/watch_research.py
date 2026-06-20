#!/usr/bin/env python3
"""
watch_research.py — a READ-ONLY live dashboard for an in-flight research_loop run.

Reads the loop's state.json + findings.md and the process list, prints a progress
dashboard, and refreshes. It NEVER writes to the loop's files, never touches the
runner process, and makes ZERO claude calls — so it cannot affect a running loop
(a partial read mid-write is caught and shown as "refreshing…").

Usage:
  python3 automation/scripts/watch_research.py            # progress dashboard, refresh every 10s
  python3 automation/scripts/watch_research.py --activity  # LIVE per-agent web searches (what each agent is researching)
  python3 automation/scripts/watch_research.py --once      # single snapshot, no loop
  python3 automation/scripts/watch_research.py --interval 5
  python3 automation/scripts/watch_research.py --run <dir-under-research-runs>
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from collections import Counter
from pathlib import Path

AUTOMATION = Path(__file__).resolve().parent.parent
RUNS_DIR = AUTOMATION / "research-runs"
VAULT_ROOT = AUTOMATION.parent

_MARK = {"done": "✅", "failed": "✗", "pending": "·"}

# --- agent-activity tracking (--activity mode) -----------------------------
# Each loop agent is a `claude -p` subprocess that writes a session JSONL under the
# Claude Code project dir. We read those (read-only) to surface each agent's live tool
# calls. Loop agents are identified by their prompt's opening signature.
_PROJECT_SLUG = str(VAULT_ROOT).replace("/", "-").replace("_", "-").replace(".", "-")
_PROJECT_DIR = Path.home() / ".claude" / "projects" / _PROJECT_SLUG
_LOOP_SIG = {           # lowercase prompt-opening marker -> role label
    "research only this angle": "research",
    "here are research findings": "verify",
    "you are scoping a research": "scope",
    "you are writing a tier-3": "synthesis",
}


def _newest_run() -> Path | None:
    if not RUNS_DIR.is_dir():
        return None
    dirs = [d for d in RUNS_DIR.iterdir() if d.is_dir() and (d / "state.json").exists()]
    return max(dirs, key=lambda d: (d / "state.json").stat().st_mtime) if dirs else None


def _read_state(run_dir: Path) -> dict | None:
    sp = run_dir / "state.json"
    try:                                   # tolerate a mid-write partial read
        return json.loads(sp.read_text(encoding="utf-8"))
    except Exception:                      # noqa: BLE001
        return None


def _active_agents() -> list[str]:
    try:
        out = subprocess.run(["ps", "-ax", "-o", "etime,command"],
                             capture_output=True, text=True, timeout=10).stdout
    except Exception:                      # noqa: BLE001
        return []
    rows = []
    for ln in out.splitlines():
        if "claude -p" not in ln:
            continue
        low = ln.lower()
        if "research only" in low:
            kind = "research"
        elif "sanity-check" in low:
            kind = "verify"
        elif "tier-3 discovery" in low or "writing a tier-3" in low:
            kind = "synthesis"
        elif "scoping a research" in low:
            kind = "scope"
        else:
            continue
        rows.append(f"   {ln.split()[0]:>9}  {kind}")
    return rows


def snapshot(run_dir: Path) -> str:
    lines = [f"▶ research_loop — {run_dir.name}", ""]
    st = _read_state(run_dir)
    if st is None:
        return "\n".join(lines + ["  (state.json refreshing — try again in a moment)"])
    angles = st.get("angles", [])
    c = Counter(a["status"] for a in angles)
    syn = st.get("synthesis", {}).get("status", "pending")
    lines.append(f"  topic: {st.get('topic','')[:78]}")
    lines.append(f"  progress: {c.get('done',0)} done · {c.get('pending',0)} pending · "
                 f"{c.get('failed',0)} failed   (of {len(angles)})   synthesis: {syn}")
    lines.append("")
    for a in angles:
        lines.append(f"  {_MARK.get(a['status'],'?')} {a['id']:>2} {a['name'][:64]}")
    fp = run_dir / "findings.md"
    if fp.exists():
        try:
            txt = fp.read_text(encoding="utf-8")
            lines.append("")
            lines.append(f"  findings.md: {len(txt):,} bytes · "
                         f"{txt.count(chr(10)+'## Angle')} angle sections written")
        except Exception:                  # noqa: BLE001
            pass
    agents = _active_agents()
    lines.append("")
    lines.append(f"  active agents (peak should be ≤2): {len(agents)}")
    lines.extend(agents)
    rp = st.get("report_path")
    if rp and (VAULT_ROOT / rp).exists():
        lines.append("")
        lines.append(f"  ✅ REPORT WRITTEN → {rp}")
    return "\n".join(lines)


def _msg_text(msg) -> str:
    """Flatten a JSONL message's content to plain text."""
    if isinstance(msg, str):
        return msg
    if not isinstance(msg, dict):
        return ""
    content = msg.get("content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(c.get("text", "") for c in content
                        if isinstance(c, dict) and c.get("type") == "text")
    return ""


def _classify(first_prompt: str) -> tuple[str | None, str]:
    """Return (role, angle) for a loop-agent prompt, or (None, '') if not a loop agent."""
    low = first_prompt.lower()
    role = next((r for sig, r in _LOOP_SIG.items() if sig in low), None)
    if role is None:
        return None, ""
    spans = re.findall(r"«([^»]+)»", first_prompt)   # «topic» then «angle» (research) / «angle» (verify)
    if role == "research":
        angle = spans[1] if len(spans) > 1 else (spans[0] if spans else "")
    elif role == "verify":
        angle = spans[0] if spans else ""
    else:
        angle = ""
    return role, angle


def _agent_sessions(max_age_sec: int = 600) -> list[dict]:
    """Find recent loop-agent session JSONLs and extract role/angle + their web searches."""
    if not _PROJECT_DIR.is_dir():
        return []
    now = time.time()
    out = []
    for jf in _PROJECT_DIR.glob("*.jsonl"):
        try:
            age = now - jf.stat().st_mtime
        except OSError:
            continue
        if age > max_age_sec:
            continue
        role = angle = None
        searches: list[str] = []
        first_prompt = ""
        try:
            for ln in jf.read_text(encoding="utf-8").splitlines():
                try:
                    o = json.loads(ln)
                except (json.JSONDecodeError, ValueError):
                    continue
                msg = o.get("message", {})
                if role is None and isinstance(msg, dict) and msg.get("role") == "user":
                    first_prompt = _msg_text(msg)
                    role, angle = _classify(first_prompt)
                    if role is None:        # not a loop agent — skip this file
                        break
                for c in (msg.get("content") or []) if isinstance(msg, dict) else []:
                    if isinstance(c, dict) and c.get("type") == "tool_use" \
                            and c.get("name") in ("WebSearch", "WebFetch"):
                        inp = c.get("input", {})
                        q = inp.get("query") or inp.get("url") or ""
                        searches.append(f"{c['name']}: {q}")
        except OSError:
            continue
        if role:
            out.append({"role": role, "angle": angle, "searches": searches,
                        "age": age, "n": len(searches)})
    out.sort(key=lambda s: s["age"])         # most-recently-active first
    return out


def activity_snapshot() -> str:
    sessions = _agent_sessions()
    if not sessions:
        return ("▶ live agent activity — no active loop agents found.\n"
                "  (the run may be between waves, scoping, synthesizing, or already done)")
    lines = [f"▶ live agent activity — {len(sessions)} agent(s) in the last 10 min "
             f"(peak should be ≤2 ACTIVE)", ""]
    for s in sessions[:6]:
        active = "● ACTIVE" if s["age"] < 75 else f"  ({int(s['age'])}s idle)"
        head = f"  [{s['role']}] {active}"
        if s["angle"]:
            head += f" — {s['angle'][:60]}"
        lines.append(head)
        for q in s["searches"][-5:]:
            lines.append(f"      {q[:88]}")
        if not s["searches"]:
            lines.append("      (no web searches yet — reading / reasoning)")
        lines.append("")
    return "\n".join(lines)


def _run_py_alive() -> bool:
    """True if a research run is still going — the overnight run.py OR a manual
    research_loop.py resume (matches both so --until-done is resume-aware)."""
    try:
        r = subprocess.run(["pgrep", "-f", "research_loop|automation/scripts/run.py"],
                           capture_output=True, text=True, timeout=10)
        return bool(r.stdout.strip())
    except Exception:                          # noqa: BLE001
        return False


def _is_complete(run_dir: Path | None) -> bool:
    """True once the run finished: report written, or synthesis marked done."""
    if not run_dir:
        return False
    st = _read_state(run_dir)
    if st is None:
        return False
    if st.get("synthesis", {}).get("status") == "done":
        return True
    rp = st.get("report_path")
    return bool(rp and (VAULT_ROOT / rp).exists())


def _watch(render, run_dir: Path | None, interval: int, until_done: bool) -> None:
    """Shared refresh loop. With until_done, auto-exits when the run completes
    (or flags if run.py ended without producing a report)."""
    try:
        while True:
            print("\033[2J\033[H", end="")     # clear screen
            print(render())
            if until_done:
                if _is_complete(run_dir):       # check complete BEFORE not-alive (avoids the exit race)
                    print("\n  ✅ run complete — report written. Exiting (--until-done).")
                    return
                if not _run_py_alive():
                    print("\n  ⚠️ run process ended WITHOUT a report (throttled / budget-capped / "
                          "error). Check automation/logs/run-*.log. Exiting (--until-done).")
                    return
                tail = " · auto-exits when the report lands"
            else:
                tail = ""
            print(f"\n  (refreshing every {interval}s{tail} — Ctrl-C to stop; the run is unaffected)")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nstopped watching (run continues).")


def main():
    ap = argparse.ArgumentParser(description="Read-only live dashboard for a research_loop run.")
    ap.add_argument("--run", help="run-dir name under automation/research-runs/ (default: newest)")
    ap.add_argument("--activity", action="store_true",
                    help="show each agent's LIVE web searches instead of the progress dashboard")
    ap.add_argument("--once", action="store_true", help="print one snapshot and exit")
    ap.add_argument("--until-done", dest="until_done", action="store_true",
                    help="keep refreshing, then auto-exit when the run completes (or ends)")
    ap.add_argument("--interval", type=int, default=10, help="refresh seconds (default 10)")
    args = ap.parse_args()

    run_dir = (RUNS_DIR / args.run) if args.run else _newest_run()

    if args.activity:
        if args.once:
            print(activity_snapshot())
            return
        _watch(activity_snapshot, run_dir, args.interval, args.until_done)
        return

    if not run_dir or not run_dir.exists():
        print("No research-loop run found under automation/research-runs/.")
        return
    if args.once:
        print(snapshot(run_dir))
        return
    _watch(lambda: snapshot(run_dir), run_dir, args.interval, args.until_done)


if __name__ == "__main__":
    main()
