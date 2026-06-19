#!/usr/bin/env python3
"""
research_loop.py — the headless-reliable sequential research loop.

The gentle replacement for the bundled /deep-research workflow in the nightly
automation. Instead of ONE `claude -p` that explodes into ~100 simultaneous agents
(which fail-fast on a rate throttle and lose everything — the 2026-06-19 failure),
this runs a PACED loop of small, flat `claude -p` calls:

    scope (topic -> angles)  ->  per-angle research + verify (peak 2 at a time)  ->  synthesis

Properties that make it headless-reliable:
  - LOW CONCURRENCY (max_concurrent, default 2) + pacing  -> never bursts into the throttle.
  - CHECKPOINT + RESUME via a per-run state.json          -> a throttle PAUSES, never wipes.
  - READ-ONLY AGENTS (Read/Grep/Glob/WebSearch/WebFetch)  -> every disk write is done by THIS
    runner, never by an agent; agents only emit text to stdout. No Write/Edit/Agent/Workflow.
  - GRACEFUL DEGRADATION                                   -> synthesis runs on whatever angles
    succeeded; you always get a report if >=1 angle landed.

CONTRACT (automation/README.md): discovery-only. The only files written are under
automation/research-runs/ (state + findings) and the one report at the caller-supplied
report_path under raw/research/self-research/. Never edits canon, never runs git.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

AUTOMATION = Path(__file__).resolve().parent.parent
VAULT_ROOT = AUTOMATION.parent
RESEARCH_SELF = VAULT_ROOT / "raw" / "research" / "self-research"
RUNS_DIR = AUTOMATION / "research-runs"

# Read-only allow-list for every research/verify/synthesis call. NO Write/Edit/Agent/Workflow:
# the agents only emit text; this runner does all disk writes. This is what keeps each call a
# single flat agent that cannot fan out a swarm.
RESEARCH_TOOLS = "Read,Grep,Glob,WebSearch,WebFetch"

# Throttle / rate-limit markers in claude output. On these we checkpoint + stop (resume later)
# rather than burn retries — the 5-hour window resets and the next run continues.
_THROTTLE_MARKERS = ("session limit", "rate limit", "usage limit", "resets ")

# Fallback angle template (the vault's chokepoint-investability lens) if the scope call fails.
_FALLBACK_ANGLES = [
    "Value-chain map: who sits where, upstream to downstream",
    "Chokepoint quality (Framework 12 lens): buyer-defense, supply-response, lockout, substitution tail",
    "Competitors and the substitution tail: who else can supply, how close",
    "Demand durability: is the gated thing actually ramping, structural vs cyclical",
    "Who captures the value: the durable owner(s) vs the commoditizing layer",
    "Risks, falsifiers, and what to verify at primary sources",
]


def _now() -> datetime:
    return datetime.now()


def _stamp() -> str:
    return _now().strftime("%Y-%m-%d")


def _slug(text: str, n: int = 7) -> str:
    words = re.findall(r"[A-Za-z0-9]+", text.lower())[:n]
    return "-".join(words) or "topic"


def _throttled(text: str) -> bool:
    low = (text or "").lower()
    return any(m in low for m in _THROTTLE_MARKERS)


# ---------------------------------------------------------------------------
# One flat, read-only claude -p call
# ---------------------------------------------------------------------------
def _claude(prompt: str, claude_bin: str, timeout: int) -> dict:
    """Run one read-only `claude -p`. Returns {ok, out, err, throttled}. Never raises."""
    cmd = [claude_bin, "-p", prompt, "--allowedTools", RESEARCH_TOOLS,
           "--disallowedTools", "Edit,MultiEdit,NotebookEdit,Write"]
    try:
        p = subprocess.run(cmd, cwd=str(VAULT_ROOT), capture_output=True,
                           text=True, timeout=timeout)
        out, err = p.stdout or "", p.stderr or ""
        return {"ok": p.returncode == 0 and bool(out.strip()),
                "out": out, "err": err, "throttled": _throttled(out + err)}
    except subprocess.TimeoutExpired:
        return {"ok": False, "out": "", "err": f"timeout {timeout}s", "throttled": False}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "out": "", "err": str(e), "throttled": False}


def _call_with_retry(prompt: str, claude_bin: str, timeout: int, max_retries: int) -> dict:
    """Backoff-retry a call on TRANSIENT failure. A hard throttle returns immediately
    (don't waste retries — the caller checkpoints and stops to resume later).
    Returns {ok, text, throttled, calls}."""
    calls = 0
    backoff = 60
    for attempt in range(max_retries + 1):
        r = _claude(prompt, claude_bin, timeout)
        calls += 1
        if r["throttled"]:
            return {"ok": False, "text": "", "throttled": True, "calls": calls}
        if r["ok"]:
            return {"ok": True, "text": r["out"].strip(), "throttled": False, "calls": calls}
        if attempt < max_retries:
            time.sleep(backoff)
            backoff = min(backoff * 3, 300)
    return {"ok": False, "text": "", "throttled": False, "calls": calls}


# ---------------------------------------------------------------------------
# The three step kinds
# ---------------------------------------------------------------------------
def _scope(topic: str, claude_bin: str, timeout: int, max_retries: int) -> tuple[list[str], int]:
    prompt = (
        f"You are scoping a research plan. Topic:\n«{topic}»\n\n"
        "Output ONLY a JSON array of 15-20 focused, DISTINCT, non-overlapping research angles a "
        "stock analyst would investigate to answer it (value chain, chokepoint quality, competitors, "
        "demand, who-captures-value, risks/falsifiers, etc.). Choose the NUMBER by the topic's "
        "breadth — closer to 15 for a focused topic, up to 20 for one spanning a whole value chain. "
        "Never pad with overlapping angles to hit the count; 15 means 15 genuinely distinct facets. "
        "Each angle a short phrase. No prose, no markdown fence — just the JSON array."
    )
    r = _call_with_retry(prompt, claude_bin, timeout, max_retries)
    if not r["ok"]:
        return [], r["calls"]
    m = re.search(r"\[.*\]", r["text"], re.DOTALL)
    if not m:
        return [], r["calls"]
    try:
        angles = [str(a).strip() for a in json.loads(m.group(0)) if str(a).strip()]
        return angles[:20], r["calls"]
    except (json.JSONDecodeError, ValueError):
        return [], r["calls"]


def _angle_work(topic: str, angle: str, claude_bin: str, timeout: int,
                max_retries: int, verify: bool) -> dict:
    """Research one angle, then (optionally) verify it. Returns {ok, text, throttled, calls}."""
    research = (
        f"Research ONLY this angle of the topic «{topic}»:\n«{angle}»\n\n"
        "Do focused web searches (5-8 reputable sources; prefer primary/company/industry over "
        "blogs). Tag each claim Tier 3 (independent analysis) or Tier 4 (news). Write 300-500 "
        "words of findings with inline source links. Output ONLY the findings markdown — no "
        "preamble. Discovery-only: write nothing to disk."
    )
    r = _call_with_retry(research, claude_bin, timeout, max_retries)
    calls = r["calls"]
    if r["throttled"]:
        return {"ok": False, "text": "", "throttled": True, "calls": calls}
    if not r["ok"]:
        return {"ok": False, "text": "", "throttled": False, "calls": calls}
    text = r["text"]
    if verify:
        vprompt = (
            f"Here are research findings on «{angle}» (topic: «{topic}»):\n\n{text}\n\n"
            "Sanity-check each load-bearing claim: is it supported by the cited source, and is "
            "any number/share plausibly correct? Flag unsupported or Tier-5/rumor claims inline "
            "with [unverified]. Output the same findings, lightly corrected/annotated. Markdown only."
        )
        v = _call_with_retry(vprompt, claude_bin, timeout, max_retries)
        calls += v["calls"]
        if v["throttled"]:
            # research succeeded; keep it, but signal the throttle so the loop checkpoints.
            return {"ok": True, "text": text, "throttled": True, "calls": calls}
        if v["ok"] and v["text"].strip():
            text = v["text"]
    return {"ok": True, "text": text, "throttled": False, "calls": calls}


# ---------------------------------------------------------------------------
# CONNECTIONS — 10 grounded agents tie the findings to the existing vault
# (and surface what the vault is MISSING). Each greps its slice; honest-verdict.
# ---------------------------------------------------------------------------
def _connection_specs(vault_root: Path) -> list[dict]:
    """The fixed 10 connection-agent specs. Company/theme corpora are split in half
    deterministically (sorted, halved) so the two agents in each pair cover different pages."""
    comps = sorted(p.stem for p in (vault_root / "wiki" / "companies").glob("*.md"))
    ch = len(comps) // 2
    themes = sorted(p.stem for p in (vault_root / "wiki" / "themes").glob("*.md"))
    th = len(themes) // 2
    return [
        {"label": "companies-A", "dir": "wiki/companies/",
         "scope": "ONLY these company pages: " + ", ".join(comps[:ch]),
         "lens": "which companies/tickers named in the findings ALREADY have a page here, and what "
                 "each finding adds or challenges about them"},
        {"label": "companies-B", "dir": "wiki/companies/",
         "scope": "ONLY these company pages: " + ", ".join(comps[ch:]),
         "lens": "which companies/tickers named in the findings ALREADY have a page here, and what "
                 "each finding adds or challenges about them"},
        {"label": "themes-A", "dir": "wiki/themes/",
         "scope": "ONLY these theme pages: " + ", ".join(themes[:th]),
         "lens": "do the findings CONFIRM / CHALLENGE / EXTEND any of these themes?"},
        {"label": "themes-B", "dir": "wiki/themes/",
         "scope": "ONLY these theme pages: " + ", ".join(themes[th:]),
         "lens": "do the findings CONFIRM / CHALLENGE / EXTEND any of these themes?"},
        {"label": "chokepoints-confirm", "dir": "wiki/chokepoints/",
         "scope": "all chokepoint pages under wiki/chokepoints/",
         "lens": "where do the findings CONFIRM or EXTEND a chokepoint thesis — reinforce the moat, "
                 "durability, or value-capture story?"},
        {"label": "chokepoints-challenge", "dir": "wiki/chokepoints/",
         "scope": "all chokepoint pages under wiki/chokepoints/",
         "lens": "the ADVERSARIAL lens — where do the findings CHALLENGE or THREATEN a chokepoint "
                 "thesis (faster substitution, quicker supply-response, a demand miss, a new entrant)?"},
        {"label": "trackers-relationships", "dir": "wiki/trackers/ + wiki/relationships/",
         "scope": "the tracker pages under wiki/trackers/ and the relationship page(s) under wiki/relationships/",
         "lens": "does any finding FIRE a falsifier/catalyst/tripwire (what-could-go-wrong, "
                 "forward-edge-tracker) or touch hyperscaler-capex / china-exposure / a bilateral relationship?"},
        {"label": "thesis-frameworks", "dir": "wiki/_thesis*.md + raw/notes/frameworks*.md",
         "scope": "the three thesis anchors (wiki/_thesis*.md) and the three frameworks files "
                  "(raw/notes/frameworks*.md)",
         "lens": "does this FIT / EXTEND / CHALLENGE the vault's worldview — the thesis or the "
                 "analytical scaffolding (value-capture layers, chokepoint-quality gradient, tier frameworks)?"},
        {"label": "prior-research", "dir": "raw/research/",
         "scope": "the Tier-3 anchors and self-research reports under raw/research/ (incl. raw/research/self-research/)",
         "lens": "do the findings OVERLAP / EXTEND / CONTRADICT any prior research already saved here?",
         "tag": "Both sides are UNVERIFIED discovery material — tag EVERY link `discovery↔discovery "
                "(unverified)`; it is weaker than a connection to canon."},
        {"label": "coverage-gaps", "dir": "index.md + wiki/",
         "scope": "the whole vault catalog (index.md) and all of wiki/",
         "lens": "the ABSENCE check — which MAJOR entities/claims/sub-sectors in the findings have NO "
                 "vault page anywhere → candidate NEW pages (companies, chokepoints, or themes the vault is missing)"},
    ]


def _connection_prompt(spec: dict, topic: str, angle_findings: str) -> str:
    tag = spec.get("tag", "")
    return (
        "You are finding connections between NEW research findings and an existing investment "
        "research vault (stocks-wiki). Be GROUNDED: use Read/Grep/Glob to check the ACTUAL vault "
        "files — NEVER invent or guess a page that you have not confirmed exists.\n\n"
        f"TOPIC: «{topic}»\n\nRESEARCH FINDINGS:\n{angle_findings}\n\n"
        f"YOUR SLICE: {spec['scope']} (under {spec['dir']}).\n"
        f"YOUR LENS: {spec['lens']}\n\n"
        "For each REAL connection: name the vault page as a [[wikilink]] ONLY after you have "
        "verified the page exists (grep/glob first); say CONFIRM / CHALLENGE / EXTEND and cite the "
        "specific finding + the page claim it touches. "
        + (tag + " " if tag else "")
        + "HONEST-VERDICT: report ONLY meaningful connections. '(no material connection in this "
        "slice)' is a valid, good answer — do NOT manufacture links or list trivial co-mentions. "
        "Output ONLY a short markdown bullet list (or the no-material line). No preamble, no 'here "
        "is'. Discovery-only: write nothing to disk."
    )


def _connection_work(spec: dict, topic: str, angle_findings: str, claude_bin: str,
                     timeout: int, max_retries: int) -> dict:
    """One connection agent: a single grounded pass (no verify step). Returns {ok,text,throttled,calls}."""
    r = _call_with_retry(_connection_prompt(spec, topic, angle_findings),
                         claude_bin, timeout, max_retries)
    return {"ok": r["ok"], "text": r["text"], "throttled": r["throttled"], "calls": r["calls"]}


def _append_connection(findings_path: Path, label: str, text: str) -> None:
    findings_path.parent.mkdir(parents=True, exist_ok=True)
    block = f"\n\n## Vault connection: {label}\n\n{text}\n"
    with findings_path.open("a", encoding="utf-8") as fh:
        fh.write(block)


def _synthesize(topic: str, findings_md: str, claude_bin: str, timeout: int,
                max_retries: int) -> dict:
    prompt = (
        f"You are writing a Tier-3 discovery research anchor for an investment vault. Topic:\n"
        f"«{topic}»\n\nHere are the accumulated per-angle findings AND the vault-connection "
        f"notes (the `## Vault connection:` blocks):\n\n{findings_md}\n\n"
        "Synthesize them into a single cited report in this format:\n"
        "1. One-paragraph verdict (nuanced, CEO-brief style).\n"
        "2. The value chain (downstream -> upstream).\n"
        "3. The analysis by angle (who owns what, where the durable value sits).\n"
        "4. Vault connections — consolidate the `## Vault connection:` blocks into ONE section: "
        "which existing vault pages the findings CONFIRM / CHALLENGE / EXTEND (MERGE duplicates "
        "across lenses — one mention per page, not three), candidate NEW pages (coverage gaps), and "
        "prior-research overlaps (keep the `discovery↔discovery (unverified)` tag). Don't concatenate.\n"
        "5. 'What to verify at primary sources' — concrete, numbered leads.\n"
        "Open with a one-line Tier-3 disclaimer (discovery-only, web-sourced, verify before "
        "treating as canon). Output ONLY the report markdown — no preamble, no 'here is'."
    )
    r = _call_with_retry(prompt, claude_bin, timeout, max_retries)
    return r


# ---------------------------------------------------------------------------
# State + findings persistence (the resumability backbone)
# ---------------------------------------------------------------------------
def _run_dir(topic: str) -> Path:
    return RUNS_DIR / f"{_stamp()}_{_slug(topic)}"


def _load_or_init(state_path: Path, topic: str, report_path: Path) -> dict:
    if state_path.exists():
        try:
            return json.loads(state_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, ValueError):
            pass
    return {
        "topic": topic,
        "slug": _slug(topic),
        "report_path": str(report_path.relative_to(VAULT_ROOT)),
        "started": _now().strftime("%Y-%m-%dT%H%M%S"),
        "angles": [],
        "connections": [],
        "synthesis": {"status": "pending"},
    }


def _save(state: dict, state_path: Path) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def _append_findings(findings_path: Path, angle: dict, text: str) -> None:
    findings_path.parent.mkdir(parents=True, exist_ok=True)
    block = f"\n\n## Angle {angle['id']}: {angle['name']}\n\n{text}\n"
    with findings_path.open("a", encoding="utf-8") as fh:
        fh.write(block)


def _chunks(seq: list, n: int):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


# ---------------------------------------------------------------------------
# The loop
# ---------------------------------------------------------------------------
def run(topic: str, report_path: Path, *, claude_bin: str,
        max_agents: int = 60, max_concurrent: int = 2, pace_seconds: int = 30,
        per_call_timeout: int = 600, max_retries: int = 3, verify_each: bool = True,
        dry_run: bool = False, log=print) -> dict:
    """Run the sequential research loop for one topic. Returns a result dict; writes the
    report to report_path on success. Resumable: re-running continues from state.json."""
    run_dir = _run_dir(topic)
    state_path = run_dir / "state.json"
    findings_path = run_dir / "findings.md"
    state = _load_or_init(state_path, topic, report_path)
    calls = 0

    # --- STEP 0: scope (only if angles not already set) ---
    if not state["angles"]:
        if dry_run:
            angles = _FALLBACK_ANGLES
            log(f"scope: (dry-run) would request angles; using {len(angles)}-item fallback for plan")
        else:
            angles, c = _scope(topic, claude_bin, per_call_timeout, max_retries)
            calls += c
            if not angles:
                angles = _FALLBACK_ANGLES
                log(f"scope: call failed → fixed {len(angles)}-angle template")
        state["angles"] = [{"id": i + 1, "name": a, "status": "pending", "retries": 0}
                           for i, a in enumerate(angles)]
        if not dry_run:  # a dry-run must be side-effect-free — never persist state
            _save(state, state_path)
    log(f"scope ok ({len(state['angles'])} angles)")

    # --- DRY RUN: print the plan, run nothing ---
    if dry_run:
        per = 2 if verify_each else 1
        specs = _connection_specs(VAULT_ROOT)
        planned = 1 + per * len(state["angles"]) + len(specs) + 1
        for a in state["angles"]:
            log(f"  angle {a['id']}/{len(state['angles'])} {a['name']} — research" +
                ("+verify" if verify_each else ""))
        log(f"  — CONNECTIONS ({len(specs)} grounded agents) —")
        for i, s in enumerate(specs, 1):
            log(f"  connection {i}/{len(specs)} {s['label']}")
        log(f"  synthesis → {report_path.relative_to(VAULT_ROOT)}")
        log(f"plan: ~{planned} calls (cap {max_agents}, peak {max_concurrent}, "
            f"pace {pace_seconds}s) — DRY RUN, nothing executed")
        return {"name": "research-loop", "executed": False, "dry_run": True,
                "planned_calls": planned, "angles": len(state["angles"]),
                "connections": len(specs), "report": str(report_path.relative_to(VAULT_ROOT))}

    # --- STEP 1: research loop, batches of max_concurrent, paced + checkpointed ---
    total = len(state["angles"])
    pending = [a for a in state["angles"] if a["status"] != "done"]
    for batch in _chunks(pending, max_concurrent):
        if calls + len(batch) * (2 if verify_each else 1) > max_agents:
            log(f"agent budget {max_agents} reached — stopping; resume next run")
            return {"name": "research-loop", "executed": True, "ok": False,
                    "budget_capped": True, "topic": topic}
        with ThreadPoolExecutor(max_workers=max_concurrent) as ex:
            outcomes = list(ex.map(
                lambda a: _angle_work(topic, a["name"], claude_bin, per_call_timeout,
                                      max_retries, verify_each),
                batch))
        throttled = False
        for a, o in zip(batch, outcomes):
            calls += o["calls"]
            if o["ok"]:
                a["status"] = "done"
                _append_findings(findings_path, a, o["text"])
                log(f"  angle {a['id']}/{total} {a['name'][:40]} ..... ok")
            else:
                a["status"] = "failed"
                a["retries"] += 1
                log(f"  angle {a['id']}/{total} {a['name'][:40]} ..... FAILED (retries {a['retries']})")
            if o["throttled"]:
                throttled = True
        _save(state, state_path)
        if throttled:
            log("throttled — checkpointed; will resume on the next run")
            return {"name": "research-loop", "executed": True, "ok": False,
                    "throttled": True, "topic": topic,
                    "done": sum(1 for a in state["angles"] if a["status"] == "done"), "total": total}
        time.sleep(pace_seconds)

    # --- STEP 1.5: CONNECTIONS — tie the findings to the existing vault (10 grounded agents) ---
    done = [a for a in state["angles"] if a["status"] == "done"]
    if not done:
        log("no angles succeeded — no report written")
        return {"name": "research-loop", "executed": True, "ok": False,
                "note": "no angles succeeded", "topic": topic}

    specs = _connection_specs(VAULT_ROOT)               # deterministic; index aligns with state
    spec_by_id = {i + 1: s for i, s in enumerate(specs)}
    if not state.get("connections"):
        state["connections"] = [{"id": i + 1, "label": s["label"], "status": "pending", "retries": 0}
                                for i, s in enumerate(specs)]
        _save(state, state_path)
    # All connection agents get the SAME fixed input: only the angle findings (strip any
    # connection blocks already appended on a prior resume), so they never see each other's output.
    angle_findings = findings_path.read_text(encoding="utf-8").split("## Vault connection:")[0]
    ncon = len(state["connections"])
    pending_con = [c for c in state["connections"] if c["status"] != "done"]
    for batch in _chunks(pending_con, max_concurrent):
        if calls + len(batch) > max_agents:
            log(f"agent budget {max_agents} reached during connections — stopping; resume next run")
            return {"name": "research-loop", "executed": True, "ok": False,
                    "budget_capped": True, "topic": topic}
        with ThreadPoolExecutor(max_workers=max_concurrent) as ex:
            outcomes = list(ex.map(
                lambda c: _connection_work(spec_by_id[c["id"]], topic, angle_findings,
                                           claude_bin, per_call_timeout, max_retries),
                batch))
        throttled = False
        for c, o in zip(batch, outcomes):
            calls += o["calls"]
            if o["ok"]:
                c["status"] = "done"
                _append_connection(findings_path, c["label"], o["text"])
                log(f"  connection {c['id']}/{ncon} {c['label']:<22} ..... ok")
            else:
                c["status"] = "failed"
                c["retries"] += 1
                log(f"  connection {c['id']}/{ncon} {c['label']:<22} ..... FAILED (retries {c['retries']})")
            if o["throttled"]:
                throttled = True
        _save(state, state_path)
        if throttled:
            log("throttled during connections — checkpointed; will resume on the next run")
            return {"name": "research-loop", "executed": True, "ok": False, "throttled": True,
                    "topic": topic,
                    "connections_done": sum(1 for c in state["connections"] if c["status"] == "done"),
                    "connections_total": ncon}
        time.sleep(pace_seconds)

    # --- STEP 2: synthesis (graceful — uses whatever landed) ---
    if len(done) < total:
        log(f"synthesizing with {len(done)}/{total} angles (rest failed — flagged in report)")
    s = _synthesize(topic, findings_path.read_text(encoding="utf-8"),
                    claude_bin, per_call_timeout, max_retries)
    calls += s["calls"]
    if s["throttled"]:
        log("throttled at synthesis — checkpointed; will resume next run")
        return {"name": "research-loop", "executed": True, "ok": False,
                "throttled": True, "topic": topic, "done": len(done), "total": total}
    if not (s["ok"] and s["text"].strip()):
        log("synthesis failed — no report written")
        return {"name": "research-loop", "executed": True, "ok": False,
                "note": "synthesis failed", "topic": topic}
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(s["text"], encoding="utf-8")
    state["synthesis"]["status"] = "done"
    _save(state, state_path)
    log(f"synthesis ok → {report_path.relative_to(VAULT_ROOT)} "
        f"({len(done)}/{total} angles, {calls} calls)")
    return {"name": "research-loop", "executed": True, "ok": True, "report_saved": True,
            "topic": topic, "report": str(report_path.relative_to(VAULT_ROOT)),
            "angles_done": len(done), "angles_total": total, "calls": calls}


def main():
    ap = argparse.ArgumentParser(description="Sequential research loop (headless-reliable).")
    ap.add_argument("--topic", required=True)
    ap.add_argument("--dry-run", action="store_true", help="print the plan, run nothing")
    ap.add_argument("--max-agents", type=int, default=60)
    ap.add_argument("--max-concurrent", type=int, default=2)
    ap.add_argument("--pace-seconds", type=int, default=30)
    ap.add_argument("--no-verify", action="store_true", help="skip the per-angle verify pass")
    args = ap.parse_args()
    from shutil import which
    import os
    claude_bin = os.environ.get("CLAUDE_BIN") or which("claude") or "claude"
    report_path = RESEARCH_SELF / f"{_stamp()}_{_slug(args.topic)}.md"
    res = run(args.topic, report_path, claude_bin=claude_bin, max_agents=args.max_agents,
              max_concurrent=args.max_concurrent, pace_seconds=args.pace_seconds,
              verify_each=not args.no_verify, dry_run=args.dry_run)
    print(json.dumps(res, indent=2))
    sys.exit(0 if res.get("executed", False) is not False or args.dry_run else 1)


if __name__ == "__main__":
    main()
