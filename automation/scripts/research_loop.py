#!/usr/bin/env python3
"""
research_loop.py — the headless-reliable sequential research loop.

The gentle replacement for the bundled /deep-research workflow in the nightly
automation. Instead of ONE `claude -p` that explodes into ~100 simultaneous agents
(which fail-fast on a rate throttle and lose everything — the 2026-06-19 failure),
this runs a PACED loop of small, flat `claude -p` calls:

    scope (topic -> angles)  ->  per-angle research + verify (peak 2 at a time)  ->  synthesis

Properties that make it headless-reliable:
  - LOW CONCURRENCY (max_concurrent, default 2) + pacing  -> never bursts into the concurrency throttle.
  - WAIT-THROUGH the 5-hour Max usage cap (wait_through): on a usage-cap throttle it SLEEPS until
    the cap resets and CONTINUES (the interactive behavior, headless), bounded by a hard deadline
    (e.g. 06:00) -> the run COMPLETES in one go instead of spanning nights. `caffeinate` holds the
    Mac awake for the whole run so a multi-hour wait can't die to sleep.
  - CHECKPOINT + RESUME via a per-run state.json          -> crash-insurance + the deadline fallback
    (if the cap can't clear before the deadline, it checkpoints and the next run resumes).
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
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from pathlib import Path

AUTOMATION = Path(__file__).resolve().parent.parent
VAULT_ROOT = AUTOMATION.parent
RESEARCH_SELF = VAULT_ROOT / "raw" / "research" / "self-research"
RUNS_DIR = AUTOMATION / "research-runs"

# Read-only allow-list for every research/verify/synthesis call. NO Write/Edit/Agent/Workflow:
# the agents only emit text; this runner does all disk writes. This is what keeps each call a
# single flat agent that cannot fan out a swarm.
RESEARCH_TOOLS = "Read,Grep,Glob,WebSearch,WebFetch"

# Throttle / rate-limit markers in claude output. On these we WAIT for the 5-hour Max window to
# reset and CONTINUE (the interactive-mode behavior, headless) — bounded by a hard wall-clock
# deadline (_WAIT_DEADLINE, e.g. 06:00). We only checkpoint + stop if the deadline is reached
# before the cap clears (the fallback) — never as the first move. (Old behavior: bail immediately
# and resume next run; Vic, 2026-06-24: the run must COMPLETE in one go, not span nights.)
_THROTTLE_MARKERS = ("session limit", "rate limit", "usage limit", "resets ")

# --- Wait-through config (set by run(); module-level so every flat call site reads it) ---
_WAIT_THROUGH = False                 # when True, sleep-through a usage cap instead of bailing
_WAIT_DEADLINE: "datetime | None" = None  # hard wall-clock stop; past it we checkpoint + resume
_LOG = (lambda *a, **k: None)         # run() points this at its logger
_POLL_SECONDS = 600                   # if no reset time is parseable, re-probe every 10 min
_RESET_BUFFER = 90                    # wait this many extra seconds past a parsed reset time

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


def _parse_reset_dt(text: str, now: datetime) -> "datetime | None":
    """Best-effort parse of a 'resets at <time>' clock time from a throttle message into the
    NEXT wall-clock datetime that matches it. Returns None if nothing parseable (caller polls)."""
    low = (text or "").lower()
    m = re.search(r"reset[s]?\s*(?:at|by)?\s*(\d{1,2})(?::(\d{2}))?\s*(am|pm)?", low)
    if not m:
        return None
    hh, mm, ap = int(m.group(1)), int(m.group(2) or 0), m.group(3)
    if ap == "pm" and hh != 12:
        hh += 12
    if ap == "am" and hh == 12:
        hh = 0
    if hh > 23 or mm > 59:
        return None
    cand = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
    if cand <= now:
        cand += timedelta(days=1)
    return cand


def _wait_for_reset(throttle_text: str) -> bool:
    """A usage-cap throttle was hit. Sleep until the cap resets, then signal a retry — UNLESS the
    hard deadline (_WAIT_DEADLINE) would be passed first, in which case give up so the caller
    checkpoints and resumes next run. Returns True (slept → retry) or False (deadline forbids)."""
    if not _WAIT_THROUGH or _WAIT_DEADLINE is None:
        return False
    now = _now()
    if now >= _WAIT_DEADLINE:
        _LOG(f"  usage cap hit at/after the {_WAIT_DEADLINE:%H:%M} deadline — checkpointing (resume next run)")
        return False
    reset_dt = _parse_reset_dt(throttle_text, now)
    if reset_dt is not None and reset_dt > _WAIT_DEADLINE:
        _LOG(f"  usage cap will not reset until ~{reset_dt:%H:%M}, past the {_WAIT_DEADLINE:%H:%M} "
             f"deadline — checkpointing (resume next run)")
        return False
    wake = (reset_dt + timedelta(seconds=_RESET_BUFFER)) if reset_dt else (now + timedelta(seconds=_POLL_SECONDS))
    wake = min(wake, _WAIT_DEADLINE)
    secs = max(0, int((wake - now).total_seconds()))
    snippet = " ".join((throttle_text or "").split())[:160]
    _LOG(f"  usage cap hit — waiting {secs // 60}m{secs % 60:02d}s (until ~{wake:%H:%M}), then "
         f"continuing | msg: {snippet}")
    time.sleep(secs)
    return _now() < _WAIT_DEADLINE


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
        ok = p.returncode == 0 and bool(out.strip())
        # A throttle is ONLY a FAILED call. A successful, non-empty result is NEVER a throttle even if
        # its CONTENT mentions "rate limit" / "usage limit" / "reset" — research angles legitimately
        # discuss those words. (2026-06-24: angle 7's findings about share "reset" tripped a bogus
        # 10-min wait-through on its OWN output — the real reason the loop kept looking 'stuck'.)
        return {"ok": ok, "out": out, "err": err,
                "throttled": (not ok) and _throttled(out + err)}
    except subprocess.TimeoutExpired:
        return {"ok": False, "out": "", "err": f"timeout {timeout}s", "throttled": False}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "out": "", "err": str(e), "throttled": False}


def _call_with_retry(prompt: str, claude_bin: str, timeout: int, max_retries: int) -> dict:
    """Run a flat call, riding through throttles and retrying transient failures.
    - USAGE-CAP throttle: sleep until the cap resets, then retry (bounded by _WAIT_DEADLINE).
      Only if the deadline forbids waiting do we return throttled (caller checkpoints + resumes).
    - TRANSIENT failure (empty / timeout / non-zero, not a throttle): backoff-retry up to max_retries.
    Returns {ok, text, throttled, calls, err}. `err` carries the failure reason (live-logged) so a
    failed angle/connection is never a mystery."""
    calls = 0
    backoff = 60
    transient = 0
    last_err = ""
    while True:
        r = _claude(prompt, claude_bin, timeout)
        calls += 1
        if r["throttled"]:
            if _wait_for_reset(r["out"] + r["err"]):
                continue  # cap should be clear now — retry the SAME call, no retry budget spent
            return {"ok": False, "text": "", "throttled": True, "calls": calls, "err": "usage cap (deadline reached)"}
        if r["ok"]:
            return {"ok": True, "text": r["out"].strip(), "throttled": False, "calls": calls, "err": ""}
        last_err = (r["err"] or "empty output / non-zero exit").strip().replace("\n", " ")
        if transient < max_retries:
            transient += 1
            _LOG(f"  · transient fail ({last_err[:100]}) — retry {transient}/{max_retries} in {backoff}s")
            time.sleep(backoff)
            backoff = min(backoff * 3, 300)
            continue
        return {"ok": False, "text": "", "throttled": False, "calls": calls, "err": last_err}


# ---------------------------------------------------------------------------
# The three step kinds
# ---------------------------------------------------------------------------
def _scope(topic: str, claude_bin: str, timeout: int, max_retries: int) -> tuple[list[str], int]:
    prompt = (
        f"You are scoping a research plan. Topic:\n«{topic}»\n\n"
        "Output ONLY a JSON array of EXACTLY 10 focused, DISTINCT, non-overlapping research angles a "
        "stock analyst would investigate to answer it (value chain, chokepoint quality, competitors, "
        "demand, who-captures-value, risks/falsifiers, etc.). "
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
        return angles[:10], r["calls"]
    except (json.JSONDecodeError, ValueError):
        return [], r["calls"]


def _angle_work(topic: str, angle: str, claude_bin: str, timeout: int,
                max_retries: int, verify: bool) -> dict:
    """Research one angle, then (optionally) verify it. Returns {ok, text, throttled, calls}."""
    research = (
        f"Research ONLY this angle of the topic «{topic}»:\n«{angle}»\n\n"
        "Do focused web searches (5-8 reputable sources; prefer primary/company/industry over "
        "blogs). Tag each claim Tier 3 (independent analysis) or Tier 4 (news). Write 300-500 "
        "words of findings with inline source links. Be TWO-SIDED: for every load-bearing claim, "
        "also surface the strongest DISCONFIRMING evidence or counter-case (don't write a one-sided "
        "bull pitch). End with two lines: 'Key number:' (the single most load-bearing figure + its "
        "source + a confidence tag high/med/low) and 'Falsifier:' (the concrete evidence that would "
        "prove this angle's thesis WRONG). Output ONLY the findings markdown — no preamble. "
        "Discovery-only: write nothing to disk."
    )
    r = _call_with_retry(research, claude_bin, timeout, max_retries)
    calls = r["calls"]
    if r["throttled"]:
        return {"ok": False, "text": "", "throttled": True, "calls": calls, "err": r.get("err", "")}
    if not r["ok"]:
        return {"ok": False, "text": "", "throttled": False, "calls": calls, "err": r.get("err", "")}
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
# CONNECTIONS — 8 grounded agents tie the findings to the existing vault canon.
# Each greps its slice; honest-verdict. (Trimmed from 10: dropped prior-research +
# coverage-gaps 2026-06-23 — the two weakest/heaviest agents, which were also the ones
# repeatedly throttling at the end of the run. They cross-reference the research findings,
# they don't produce research, so the report's depth is unaffected — only its breadth of
# vault cross-linking narrows slightly.)
# ---------------------------------------------------------------------------
def _connection_specs(vault_root: Path) -> list[dict]:
    """The fixed 8 connection-agent specs. Company/theme corpora are split in half
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
    return {"ok": r["ok"], "text": r["text"], "throttled": r["throttled"], "calls": r["calls"],
            "err": r.get("err", "")}


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
        "2. Cross-angle insight — 2-3 SECOND-ORDER findings that only emerge when the angles are "
        "read TOGETHER (a constraint in one angle that relieves/worsens another, a value shift one "
        "tier up/down), and explicitly FLAG any CONTRADICTIONS between angles. This is the highest-"
        "value section — do not skip it or pad it with single-angle restatements.\n"
        "3. The value chain (downstream -> upstream).\n"
        "4. The analysis by angle (who owns what, where the durable value sits).\n"
        "5. Vault connections — consolidate the `## Vault connection:` blocks into ONE section: "
        "which existing vault pages the findings CONFIRM / CHALLENGE / EXTEND (MERGE duplicates "
        "across lenses — one mention per page, not three), and any candidate NEW pages the findings "
        "imply the vault is missing. Don't concatenate.\n"
        "6. 'What to verify at primary sources' — concrete, numbered leads.\n"
        "Open with a one-line Tier-3 disclaimer (discovery-only, web-sourced, verify before "
        "treating as canon). Output ONLY the report markdown — no preamble, no 'here is'."
    )
    r = _call_with_retry(prompt, claude_bin, timeout, max_retries)
    return r


# ---------------------------------------------------------------------------
# State + findings persistence (the resumability backbone)
# ---------------------------------------------------------------------------
def _run_dir(topic: str) -> Path:
    # TOPIC-keyed (NOT date-keyed) so an unfinished topic RESUMES across nights instead of
    # restarting from scratch. The old `{date}_{slug}` defeated cross-night resume — a throttled
    # 3:30am run left a 2026-06-24_<slug> checkpoint that the next night's 2026-06-25_<slug> dir
    # never found, so every night started over. (Fixed 2026-06-24; the report file keeps its date.)
    return RUNS_DIR / _slug(topic)


# --- Per-run lock: keeps the 5:30 watchdog from colliding with a still-running 3:30 job ---
def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True          # exists, owned by another user
    except Exception:        # noqa: BLE001
        return True
    return True


def _acquire_lock(run_dir: Path, log) -> bool:
    """Best-effort exclusive lock per run-dir. A lock whose pid is DEAD is stale (the holder exited
    by any path — no explicit release needed) and is taken over. Returns False only if a LIVE
    process already holds it (e.g. a 3:30 run still sleeping in wait-through)."""
    run_dir.mkdir(parents=True, exist_ok=True)
    lock = run_dir / ".lock"
    if lock.exists():
        try:
            pid = int(lock.read_text().split()[0])
        except Exception:    # noqa: BLE001
            pid = 0
        if pid and _pid_alive(pid):
            log(f"another run (pid {pid}) is active on this topic — not starting a second")
            return False
    lock.write_text(f"{os.getpid()} {_now().isoformat()}\n")
    return True


def is_locked(run_dir: Path) -> bool:
    """True iff a LIVE process holds the run-dir lock — the watchdog uses this to defer to a 3:30 run."""
    lock = run_dir / ".lock"
    if not lock.exists():
        return False
    try:
        pid = int(lock.read_text().split()[0])
    except Exception:        # noqa: BLE001
        return False
    return bool(pid and _pid_alive(pid))


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
        wait_through: bool = False, deadline: "datetime | None" = None,
        dry_run: bool = False, log=print) -> dict:
    """Run the sequential research loop for one topic. Returns a result dict; writes the
    report to report_path on success.

    wait_through + deadline: when wait_through is True, a 5-hour Max usage-cap throttle makes the
    loop SLEEP until the cap resets and then CONTINUE (so the run completes in one go), bounded by
    `deadline` (a hard wall-clock stop, e.g. 06:00). Only if the deadline is reached before the cap
    clears does it checkpoint + stop. state.json still makes any run resumable (crash-insurance)."""
    # Publish the wait-through config + logger for the flat call sites to read.
    global _WAIT_THROUGH, _WAIT_DEADLINE, _LOG
    _LOG = log
    _WAIT_THROUGH = bool(wait_through) and not dry_run
    _WAIT_DEADLINE = deadline if _WAIT_THROUGH else None

    # Hold the Mac awake for the whole run so a multi-hour wait-for-reset can't die to sleep.
    # `caffeinate -w <pid>` self-terminates when this process exits — no manual cleanup needed.
    if _WAIT_THROUGH:
        try:
            subprocess.Popen(["caffeinate", "-is", "-w", str(os.getpid())])
            log(f"caffeinate: holding the Mac awake until process exit"
                + (f" (deadline ~{deadline:%H:%M})" if deadline else ""))
        except Exception as e:  # noqa: BLE001  (macOS-only; degrade gracefully)
            log(f"caffeinate unavailable ({e}) — relying on the Mac staying awake")

    run_dir = _run_dir(topic)
    state_path = run_dir / "state.json"
    findings_path = run_dir / "findings.md"

    # Refuse to start if a live process already holds this topic's lock (the 5:30 watchdog must
    # never run a second loop over a 3:30 run that is still alive). Stale locks are taken over.
    if not dry_run and not _acquire_lock(run_dir, log):
        return {"name": "research-loop", "executed": False, "ok": False, "locked": True,
                "topic": topic, "note": "another run is active on this topic"}

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
                a["error"] = (o.get("err") or "unknown").replace("\n", " ")[:200]
                log(f"  angle {a['id']}/{total} {a['name'][:40]} ..... FAILED — {a['error'][:90]} (retries {a['retries']})")
            if o["throttled"]:
                throttled = True
        _save(state, state_path)
        if throttled:
            log("usage cap could not clear before the deadline — checkpointed; resumes next run")
            return {"name": "research-loop", "executed": True, "ok": False,
                    "throttled": True, "topic": topic,
                    "done": sum(1 for a in state["angles"] if a["status"] == "done"), "total": total}
        time.sleep(pace_seconds)

    # --- STEP 1.5: CONNECTIONS — tie the findings to the existing vault (8 grounded agents) ---
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
    # Resume-safety: if the spec list shrank between runs (e.g. an agent was dropped) a stored
    # connection id may no longer map to a spec — skip those orphans instead of KeyError-crashing,
    # so an in-flight run started under the old spec list still completes to synthesis.
    pending_con = [c for c in state["connections"] if c["status"] != "done" and c["id"] in spec_by_id]
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
                c["error"] = (o.get("err") or "unknown").replace("\n", " ")[:200]
                log(f"  connection {c['id']}/{ncon} {c['label']:<22} ..... FAILED — {c['error'][:90]} (retries {c['retries']})")
            if o["throttled"]:
                throttled = True
        _save(state, state_path)
        if throttled:
            log("usage cap could not clear before the deadline (connections) — checkpointed; resumes next run")
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
        log("usage cap could not clear before the deadline (synthesis) — checkpointed; resumes next run")
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
    # Stream logs LIVE even when stdout is a pipe (a backgrounded run, `| tee`, etc.). Without this
    # Python block-buffers stdout to a non-TTY, so a long run looks dead until it exits — the trap
    # that made the 2026-06-24 manual resume appear hung. Line-buffering flushes on every newline.
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description="Sequential research loop (headless-reliable).")
    ap.add_argument("--topic", required=True)
    ap.add_argument("--dry-run", action="store_true", help="print the plan, run nothing")
    ap.add_argument("--max-agents", type=int, default=60)
    ap.add_argument("--max-concurrent", type=int, default=2)
    ap.add_argument("--pace-seconds", type=int, default=30)
    ap.add_argument("--no-verify", action="store_true", help="skip the per-angle verify pass")
    ap.add_argument("--wait-through", action="store_true",
                    help="ride through 5-hour usage caps (sleep until reset + continue), "
                         "bounded by --deadline-hour")
    ap.add_argument("--deadline-hour", type=float, default=6.0,
                    help="hard wall-clock stop (local 24h, e.g. 6 = 06:00) for --wait-through")
    args = ap.parse_args()
    from shutil import which
    claude_bin = os.environ.get("CLAUDE_BIN") or which("claude") or "claude"
    report_path = RESEARCH_SELF / f"{_stamp()}_{_slug(args.topic)}.md"
    deadline = None
    if args.wait_through:
        now = _now()
        hh = int(args.deadline_hour)
        mm = int(round((args.deadline_hour - hh) * 60))
        deadline = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
        if deadline <= now:  # already past today's deadline (e.g. a manual daytime run)
            deadline = now + timedelta(hours=2)
    res = run(args.topic, report_path, claude_bin=claude_bin, max_agents=args.max_agents,
              max_concurrent=args.max_concurrent, pace_seconds=args.pace_seconds,
              verify_each=not args.no_verify, wait_through=args.wait_through,
              deadline=deadline, dry_run=args.dry_run)
    print(json.dumps(res, indent=2))
    sys.exit(0 if res.get("executed", False) is not False or args.dry_run else 1)


if __name__ == "__main__":
    main()
