#!/usr/bin/env python3
"""
run.py — the stocks-wiki automation runner (the self-X loop conductor).

Lives in automation/ (operational, not canon). Orchestrates the deterministic scans,
writes a ranked digest + an audit log + the calibration/discovery queues, and (opt-in)
invokes the agentic `claude -p` steps behind the locked tool allow-list.

CONTRACT (automation/README.md): DISCOVERY-ONLY + PROPOSE-ONLY. Writes ONLY inside
automation/. Never edits canon, never runs git, never bumps last_updated. The agentic
steps are launched with a restricted --allowedTools list (read + Write-to-automation),
never Edit on wiki/.

Modes:
  python3 automation/scripts/run.py --scan        # deterministic weekly scan (default, FREE)
  python3 automation/scripts/run.py --calibrate    # + agentic calibration scoring (PAID; needs --run-llm)
  python3 automation/scripts/run.py --brief        # + agentic ranked briefing  (PAID; needs --run-llm)
  python3 automation/scripts/run.py --scan --with-freshness   # also hit SEC EDGAR (slow/network)

The default --scan is what the weekly schedule runs: zero LLM, zero canon-risk.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

AUTOMATION = Path(__file__).resolve().parent.parent
VAULT_ROOT = AUTOMATION.parent
SCRIPTS = VAULT_ROOT / "scripts"
LOGS = AUTOMATION / "logs"
DIGESTS = AUTOMATION / "digests"
CALIBRATION = AUTOMATION / "calibration"
DISCOVERY = AUTOMATION / "discovery"
PROMPTS = AUTOMATION / "prompts"
RESEARCH_SELF = VAULT_ROOT / "raw" / "research" / "self-research"   # daily deep-research reports

# The locked tool allow-list for any headless claude -p the runner launches.
# Read/scan + Write-scoped-to-automation only. NEVER Edit on wiki/.
ALLOWED_TOOLS = "Read,Grep,Glob,Bash(python3 scripts/*),Write"
DISALLOWED_TOOLS = "Edit,MultiEdit,NotebookEdit"

# Resolve the `claude` CLI robustly — launchd has a minimal PATH with no `claude` on it.
# Order: explicit CLAUDE_BIN env (set by the launchd plist) > PATH lookup > known nvm path.
# The claude CLI authenticates with the user's logged-in account (the Claude Max subscription),
# so the headless agentic steps run on Max, not API billing.
CLAUDE_BIN = (
    os.environ.get("CLAUDE_BIN")
    or shutil.which("claude")
    or "/Users/victor_he/.nvm/versions/node/v22.22.0/bin/claude"
)


def _now() -> datetime:
    return datetime.now()


def _stamp() -> str:
    return _now().strftime("%Y-%m-%d")


def _runid() -> str:
    return _now().strftime("%Y-%m-%dT%H%M%S")


def _ensure_dirs():
    for d in (LOGS, DIGESTS, CALIBRATION, DISCOVERY, RESEARCH_SELF):
        d.mkdir(parents=True, exist_ok=True)


def _run(cmd: list[str], timeout: int = 120) -> dict:
    """Run a subprocess; capture stdout/stderr/rc. Never raises."""
    try:
        p = subprocess.run(cmd, cwd=str(VAULT_ROOT), capture_output=True,
                           text=True, timeout=timeout)
        return {"ok": p.returncode == 0, "rc": p.returncode,
                "out": p.stdout, "err": p.stderr}
    except subprocess.TimeoutExpired:
        return {"ok": False, "rc": -1, "out": "", "err": f"timeout after {timeout}s"}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "rc": -1, "out": "", "err": str(e)}


def _json_or_none(res: dict):
    if not res["ok"]:
        return None
    try:
        return json.loads(res["out"])
    except (json.JSONDecodeError, ValueError):
        return None


# ---------------------------------------------------------------------------
# Deterministic scans
# ---------------------------------------------------------------------------
def scan_deterministic(with_freshness: bool) -> dict:
    results = {}
    # hygiene (JSON)
    res = _run(["python3", "scripts/vault_hygiene.py", "--json"], timeout=120)
    results["hygiene"] = {"meta": res, "data": _json_or_none(res)}
    # calibration (JSON)
    res = _run(["python3", "scripts/calibration_sweep.py", "--json"], timeout=120)
    results["calibration"] = {"meta": res, "data": _json_or_none(res)}
    # connection-finder (text)
    res = _run(["python3", "scripts/find_connections.py"], timeout=180)
    results["connections"] = {"meta": res, "text": res["out"] if res["ok"] else ""}
    # pattern accumulation (text)
    res = _run(["python3", "scripts/monitor_patterns.py"], timeout=120)
    results["patterns"] = {"meta": res, "text": res["out"] if res["ok"] else ""}
    # freshness (network; opt-in)
    if with_freshness:
        res = _run(["python3", "scripts/fetch_filings.py", "--freshness"], timeout=300)
        results["freshness"] = {"meta": res, "text": res["out"] if res["ok"] else ""}
    return results


def _text_head(text: str, n: int) -> str:
    lines = [ln for ln in (text or "").splitlines() if ln.strip()]
    return "\n".join(lines[:n])


# ---------------------------------------------------------------------------
# Digest composition (the ranked briefing)
# ---------------------------------------------------------------------------
def compose_digest(results: dict, runid: str) -> tuple[str, list[str]]:
    actions: list[str] = []
    hy = results["hygiene"]["data"]
    cal = results["calibration"]["data"]

    # --- derive action items (ruthless prioritization) ---
    if hy:
        if hy["overall"] == "FAIL":
            actions.append("🔴 HYGIENE FAIL — a hard defect (index-sync / frontmatter). See Hygiene.")
        for c in hy["checks"]:
            if c["check"] == "link-integrity" and c["unresolved"]:
                uniq = sorted({u["link"] for u in c["unresolved"]})
                bad = ", ".join(f"[[{x}]]" for x in uniq[:6])
                actions.append(f"⚠️ unresolved wikilinks: {bad} — forward-link or typo (check).")
            if c["check"] == "index-sync" and c["status"] == "FAIL":
                actions.append("🔴 index out of sync with disk — run build_index.py (human-gated).")
            if c["check"] == "tracker-freshness":
                overdue = [r["tracker"] for r in c["rows"] if r["overdue"]]
                if overdue:
                    actions.append(f"⚠️ stale trackers (>30d): {', '.join(overdue)}.")
    if cal:
        if cal["counts"]["fired"]:
            fired = [e["title"] for e in cal["candidates"] if e.get("fired")]
            actions.append(f"🔴 FIRED tripwire(s): {'; '.join(fired)} — verify + propagate.")
        if cal["counts"]["review_due"]:
            actions.append(f"⏳ {cal['counts']['review_due']} tracker entries review-due "
                           f"(>30d) — run --calibrate to score.")
    fr = results.get("freshness", {}).get("text", "")
    if fr and "New filings available" in fr:
        actions.append("📥 new filings available to ingest — see Discovery › Freshness.")

    if not actions:
        actions.append("✅ Nothing actionable — vault clean, trackers fresh, no FIRED tripwires.")

    # --- compose markdown ---
    out = []
    out.append(f"# Vault automation digest — {_stamp()}")
    out.append(f"*run `{runid}` · deterministic scan · discovery-only (nothing in canon touched)*\n")

    out.append("## ⚡ Action items\n")
    for a in actions[:8]:
        out.append(f"- {a}")
    out.append("")

    # Hygiene
    out.append("## 🧹 Hygiene (self-maintaining)\n")
    if hy:
        icon = {"PASS": "✅", "WARN": "⚠️", "FAIL": "❌"}
        out.append(f"overall **{icon[hy['overall']]} {hy['overall']}**\n")
        for c in hy["checks"]:
            out.append(f"- {icon[c['status']]} **{c['check']}** — {c['summary']}")
    else:
        out.append("_hygiene scan failed — see run log_")
    out.append("")

    # Calibration
    out.append("## 🎯 Calibration queue (self-evaluation)\n")
    if cal:
        c = cal["counts"]
        out.append(f"forward-edge {c['forward_edge']} · risk-register {c['risk_register']} · "
                   f"review-due {c['review_due']} · FIRED {c['fired']}\n")
        flagged = [e for e in cal["candidates"] if e.get("fired") or e.get("review_due")]
        if flagged:
            for e in flagged[:12]:
                tag = "🔴 FIRED" if e.get("fired") else "⏳ review-due"
                out.append(f"- [{tag}] ({e['source']}) {e['title']} "
                           f"— last touched {e.get('last_moved') or e.get('last_checked')}")
        else:
            out.append("_all entries fresh (≤30d) and no tripwire fired — nothing to score this run._")
        # surface entries carrying near-term watch dates regardless of staleness
        dated = [e for e in cal["candidates"] if e.get("temporal_markers")]
        if dated:
            out.append("\n**Entries carrying explicit watch dates** (agent judges if reached):")
            for e in dated[:8]:
                out.append(f"- {e['title']} → {', '.join(e['temporal_markers'][:6])}")
    else:
        out.append("_calibration sweep failed — see run log_")
    out.append("")

    # Discovery
    out.append("## 🔭 Discovery (self-discovering)\n")
    if fr:
        out.append("### Freshness / new filings")
        out.append("```\n" + _text_head(fr, 30) + "\n```")
    out.append("### Connection candidates (top of `find_connections.py`)")
    out.append("```\n" + _text_head(results["connections"]["text"], 24) + "\n```")
    out.append("### Pattern accumulation (`monitor_patterns.py`)")
    out.append("```\n" + _text_head(results["patterns"]["text"], 18) + "\n```")
    out.append("")

    # Run log
    out.append("## 📋 Run log\n")
    for name, r in results.items():
        m = r["meta"]
        status = "ok" if m["ok"] else f"FAILED (rc={m['rc']})"
        out.append(f"- `{name}`: {status}" + (f" — {m['err'][:120]}" if not m["ok"] else ""))
    out.append("")
    out.append(f"*Next: `--calibrate` to score the queue (paid), `--brief` for a ranked briefing (paid). "
               f"Contract: discovery-only, writes only to `automation/`.*")
    return "\n".join(out), actions


def write_calibration_queue(results: dict, runid: str) -> Path | None:
    cal = results["calibration"]["data"]
    if not cal:
        return None
    path = CALIBRATION / f"{_stamp()}_candidates.json"
    path.write_text(json.dumps(cal, indent=2), encoding="utf-8")
    return path


def append_log(runid: str, actions: list[str], results: dict):
    LOGS.mkdir(parents=True, exist_ok=True)
    logpath = LOGS / f"run-{_stamp()}.log"
    lines = [f"\n=== run {runid} ==="]
    for name, r in results.items():
        m = r["meta"]
        lines.append(f"  {name}: {'ok' if m['ok'] else 'FAILED ' + str(m['rc'])}")
    lines.append(f"  actions: {len(actions)}")
    for a in actions:
        lines.append(f"    - {a}")
    with logpath.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return logpath


# ---------------------------------------------------------------------------
# Agentic steps (opt-in, paid) — built behind the locked allow-list
# ---------------------------------------------------------------------------
def build_claude_cmd(prompt_file: Path, extra: str = "") -> list[str]:
    """Construct a locked-down `claude -p` invocation. Never loosens the allow-list."""
    instruction = (
        f"Read the instructions in {prompt_file.relative_to(VAULT_ROOT)} and execute them. "
        "CONTRACT: discovery-only + propose-only. Write ONLY inside automation/. "
        "Never edit wiki/, _thesis*, frameworks*, CLAUDE.md, index.md, log.md. Never run git. "
        + extra
    )
    return [
        CLAUDE_BIN, "-p", instruction,
        "--allowedTools", ALLOWED_TOOLS,
        "--disallowedTools", DISALLOWED_TOOLS,
    ]


def agentic_step(name: str, prompt_file: Path, run_llm: bool) -> dict:
    cmd = build_claude_cmd(prompt_file)
    if not run_llm:
        return {"name": name, "executed": False,
                "cmd": " ".join(f'"{c}"' if " " in c else c for c in cmd),
                "note": "DRY-RUN — pass --run-llm to actually invoke (incurs token cost)"}
    res = _run(cmd, timeout=900)
    return {"name": name, "executed": True, "ok": res["ok"],
            "out_tail": (res["out"] or "")[-1500:], "err": res["err"][:500]}


def _slug(text: str, n: int = 7) -> str:
    words = re.findall(r"[A-Za-z0-9]+", text.lower())[:n]
    return "-".join(words) or "topic"


def build_deepresearch_cmd(question: str, report_path: Path) -> list[str]:
    """A `claude -p` that runs the deep-research workflow and saves the report.
    Broad tools (deep-research needs web + workflow); only canon EDITS are hard-blocked."""
    instruction = (
        "Run a thorough multi-source DEEP-RESEARCH investigation (use the deep-research workflow: "
        "fan out search angles, fetch sources, adversarially verify claims, synthesize) on:\n\n"
        f"{question}\n\n"
        f"When complete, save the final CITED, VERIFIED report as a Tier-3 anchor to EXACTLY: "
        f"{report_path.relative_to(VAULT_ROOT)} (create the folder if needed). "
        "CONTRACT: discovery-only. Write ONLY that report file under raw/research/self-research/. "
        "NEVER edit any wiki/ page, _thesis*, frameworks*, CLAUDE.md, index.md, or log.md. Never run git."
    )
    return [CLAUDE_BIN, "-p", instruction, "--disallowedTools", "Edit,MultiEdit,NotebookEdit"]


def deep_research_step(run_llm: bool) -> dict:
    """Research the top Pending topic via the headless-reliable SEQUENTIAL RESEARCH LOOP
    (automation/scripts/research_loop.py) — paced, low-concurrency (peak 2), checkpointed,
    resumable. Replaces the bundled deep-research workflow, whose ~100-agent burst fail-fasts
    on a rate throttle (the 2026-06-19 failure). See automation/RESEARCH-LOOP-SPEC.md."""
    res = _run(["python3", "scripts/research_agenda.py", "--pick"], timeout=30)
    question = (res["out"] or "").strip()
    if not question:
        return {"name": "deep-research", "executed": False,
                "note": "no Pending topic in raw/research/topics-list.md"}
    report_path = RESEARCH_SELF / f"{_stamp()}_{_slug(question)}.md"
    if not run_llm:
        return {"name": "deep-research", "executed": False, "topic": question,
                "note": "DRY-RUN — pass --run-llm to actually run the research loop"}
    RESEARCH_SELF.mkdir(parents=True, exist_ok=True)
    # Local import so a research_loop issue can never break the (free) deterministic scan.
    import research_loop  # noqa: E402

    loglines: list[str] = []
    result = research_loop.run(
        question, report_path, claude_bin=CLAUDE_BIN,
        max_agents=60, max_concurrent=2, pace_seconds=30,
        per_call_timeout=600, max_retries=3, verify_each=True,
        log=lambda m: loglines.append(str(m)),
    )
    # Observability — write the loop's per-step outcome into the day's run log so a failure
    # (throttle, budget cap, synthesis miss) is VISIBLE in the morning, not buried in a JSONL.
    try:
        with (LOGS / f"run-{_stamp()}.log").open("a", encoding="utf-8") as f:
            f.write("\n  deep-research (loop):\n")
            for ln in loglines:
                f.write(f"    {ln}\n")
    except Exception:  # noqa: BLE001
        pass

    saved = report_path.exists()
    if saved:  # mark the topic researched only if the report actually landed
        _run(["python3", "scripts/research_agenda.py", "--mark-done", str(report_path)], timeout=30)
    result["report_saved"] = saved
    result["log"] = loglines
    return result


def main():
    ap = argparse.ArgumentParser(description="stocks-wiki automation runner (self-X loop).")
    ap.add_argument("--scan", action="store_true", help="deterministic scan (default)")
    ap.add_argument("--calibrate", action="store_true", help="+ agentic calibration scoring (Max subscription)")
    ap.add_argument("--brief", action="store_true", help="+ agentic ranked briefing (Max subscription)")
    ap.add_argument("--full", action="store_true",
                    help="the autonomous loop: scan + calibration scoring + briefing (Max subscription)")
    ap.add_argument("--auto", action="store_true",
                    help="daily heartbeat: scan every day; deep-research Tue-Sat; full agentic review Mon")
    ap.add_argument("--deep-research", dest="deep_research", action="store_true",
                    help="run /deep-research on the top topics-list.md item -> raw/research/self-research/")
    ap.add_argument("--with-freshness", action="store_true", help="also run SEC EDGAR freshness (network)")
    ap.add_argument("--run-llm", action="store_true", help="actually invoke claude -p (default: dry-run)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    # --auto = the daily heartbeat. Free deterministic scan every day; the full agentic
    # loop (calibration scoring + briefing, on the Max subscription) ONLY on Mondays —
    # so Max usage stays ~1 run/week while hygiene/discovery/freshness run daily.
    if args.auto:
        args.with_freshness = True
        wd = _now().weekday()       # Mon=0 ... Sun=6
        if wd == 0:                 # Monday → weekly agentic review (calibration + briefing)
            args.full = True
            args.run_llm = True
        elif 1 <= wd <= 5:          # Tue–Sat → deep-research day (one topic)
            args.deep_research = True
            args.run_llm = True
        # Sunday → free deterministic scan only

    _ensure_dirs()
    runid = _runid()

    # Deterministic scan always runs (it's the filter the agentic steps ride on).
    results = scan_deterministic(with_freshness=args.with_freshness)
    digest, actions = compose_digest(results, runid)
    digest_path = DIGESTS / f"{_stamp()}_digest.md"
    digest_path.write_text(digest, encoding="utf-8")
    cal_path = write_calibration_queue(results, runid)
    log_path = append_log(runid, actions, results)

    # Which agentic steps to run. --full = the autonomous loop (calibration scoring → briefing).
    steps: list[tuple[str, str]] = []
    if args.full:
        steps = [("calibrate", "calibration-score.md"), ("brief", "brief.md")]
    else:
        if args.calibrate:
            steps.append(("calibrate", "calibration-score.md"))
        if args.brief:
            steps.append(("brief", "brief.md"))
    agentic = [agentic_step(name, PROMPTS / pf, args.run_llm) for name, pf in steps]

    # Deep-research day (Tue–Sat via --auto, or explicit --deep-research):
    # keep the agenda fresh (free), then research the top Pending topic.
    if args.deep_research:
        _run(["python3", "scripts/research_agenda.py", "--propose"], timeout=200)
        agentic.append(deep_research_step(args.run_llm))

    if not args.quiet:
        print(f"✅ scan complete — run {runid}")
        print(f"   digest:      {digest_path.relative_to(VAULT_ROOT)}")
        if cal_path:
            print(f"   calibration: {cal_path.relative_to(VAULT_ROOT)}")
        print(f"   log:         {log_path.relative_to(VAULT_ROOT)}")
        print(f"\n   {len(actions)} action item(s):")
        for a in actions:
            print(f"     - {a}")
        for step in agentic:
            if step.get("executed"):
                extra = f" — {step['topic'][:60]}" if step.get("topic") else ""
                print(f"\n   {step['name']}: {'ok' if step.get('ok') else 'check log'}{extra}")
                if step.get("report"):
                    print(f"     report: {step['report']} (saved={step.get('report_saved')})")
            else:
                print(f"\n   {step['name']} (not run): {step.get('note', '')}")
                if step.get("cmd"):
                    print(f"     cmd: {step['cmd']}")
    sys.exit(0)


if __name__ == "__main__":
    main()
