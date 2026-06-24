# Spec — Sequential Research Loop (`research_loop.py`)

The headless-reliable replacement for the bundled `/deep-research` workflow in the nightly automation. Same output contract (a Tier-3 report at `raw/research/self-research/<date>_<slug>.md`); gentle on the rate limit; resumable.

## Why this exists
The 2026-06-19 02:30 run fired the bundled deep-research, which exploded into **104 simultaneous agents / 2.85M tokens in 8 minutes** and was cut off by a **rate/concurrency throttle** (NOT a budget cap — weekly was 38%, the 5-hour window 78%). Headless `claude -p` agents **fail-fast** on a throttle instead of waiting/retrying like interactive mode, so 61 agents died at once and no report was written. This loop fixes both: **low concurrency + pacing** (never bursts) and **checkpoint + resume** (a throttle pauses, never wipes).

## Flow
```
scope (topic → angles)  →  per-angle research + verify (peak 2)  →  CONNECTIONS (8 grounded agents)  →  synthesis
```
The CONNECTIONS step ties the night's findings to the existing vault before synthesis — 10 agents, each grepping its own slice, honest-verdict ("no material connection" is valid), feeding a consolidated "Vault connections" report section.

## Config (the dials)
- `max_agents = 60` — total `claude -p` calls across a run (scope + angles×research/verify + connections + synthesis). Runaway backstop, not the real limiter.
- `max_concurrent = 2` — never more than 2 small agents alive at once. **This is the load-bearing safety setting** — it's what keeps the run under the *concurrency* throttle, regardless of total size or token budget. (Distinct from the 5-hour *usage cap* below.)
- `pace_seconds = 30` — sleep between waves.
- `per_call_timeout = 600` (10 min).
- `max_retries = 3` per call (transient failures only — NOT usage-cap throttles; see Wait-through).
- **`wait_through = True` + `deadline = 06:00`** (set by `run.py`) — ride through the 5-hour Max usage cap instead of bailing; hard-stop at the deadline. `caffeinate -is` holds the Mac awake for the run.

## Wait-through the 5-hour usage cap (codified 2026-06-24; Vic)
**The run must COMPLETE in one go, not span nights.** The 5-hour Max window is shared with the human's own interactive Claude usage, so the 03:30 job can start with little headroom and hit the cap minutes in (the 2026-06-24 run: capped ~14 min in, 8/10 angles). Old behavior bailed and resumed next night — removed.

New behavior, in `_call_with_retry` → `_wait_for_reset`:
- On a usage-cap throttle (`session limit` / `usage limit` / `resets …`), **parse the reset time, sleep until it (+90s), then retry the same call** — no retry budget spent, the loop just continues. If no reset time is parseable, poll every 10 min.
- **Bounded by a hard `deadline` (06:00 local).** If the cap will not reset before the deadline (or the deadline is reached mid-wait), it stops, checkpoints, and the next run resumes (the only fallback — used when the human's 06:00 ceiling forbids waiting longer).
- `caffeinate -is -w <pid>` is spawned for the run so a multi-hour wait can't die to Mac sleep (laptop must be lid-open / on AC; it self-terminates when the run exits).
- `state.json` is kept purely as crash-insurance now, not as the throttle response.

## Agent budget — how it's spent (a 15-angle run ≈ 42 calls, cap 60)
| Step | Calls |
|---|---|
| Scope (topic → angles) | 1 |
| Per angle: research + verify | ~10 angles × 2 = 20 |
| **CONNECTIONS** (8 grounded agents — see below) | 8 |
| Synthesis | 1 |
Each call is **one flat agent** restricted to `Read, Grep, Glob, WebSearch, WebFetch` — **no `Agent`/`Workflow`/`Task` tools**, so a call physically cannot fan out a swarm. Peak concurrency stays 2 no matter what.

## CONNECTIONS — the 8 grounded agents
Run between research and synthesis. Each reads the angle findings + greps its slice of the vault; reports only meaningful CONFIRM / CHALLENGE / EXTEND links (wikilink only verified pages); output appended to `findings.md` as a `## Vault connection: <label>` block that synthesis consolidates.
| # | Agent | Slice / lens |
|---|---|---|
| 1–2 | `companies-A/B` | the company pages, split in half — which tickers are already covered + what findings add |
| 3–4 | `themes-A/B` | the theme pages, split in half — CONFIRM/CHALLENGE/EXTEND |
| 5 | `chokepoints-confirm` | all chokepoints — where findings **reinforce** a thesis |
| 6 | `chokepoints-challenge` | all chokepoints — adversarial: where findings **threaten** a thesis |
| 7 | `trackers-relationships` | trackers + relationship — does a finding fire a falsifier/catalyst/tripwire? |
| 8 | `thesis-frameworks` | the 3 thesis anchors + 3 frameworks — FIT/EXTEND/CHALLENGE the worldview |

*(Trimmed from 10 on 2026-06-23 — dropped `prior-research` and `coverage-gaps`, the two weakest + heaviest agents that repeatedly throttled the run at the end. They cross-referenced findings rather than producing research, so report depth is unaffected; only the breadth of vault cross-linking narrows slightly.)*

Connections are paced + checkpointed exactly like the angle loop (state `connections[]`); a throttle mid-connections pauses + resumes; graceful degradation (synthesis uses whatever landed).

## Topic source (unchanged pipeline)
Topics come from `raw/research/topics-list.md` via `research_agenda.py`:
- **Pending** (Vic-curated, ranked) → the loop `--pick`s the top item each research night.
- **Researched** → `--mark-done` moves it here when the report lands; the rest shift up.
- **Proposed** → the automation `--propose`s new candidates (connection-finder + open-questions); Vic promotes good ones to Pending.
Vic curates + promotes; he does NOT have to supply a topic every day (8 are queued + it self-replenishes).

## State file (resumability)
The run-dir is **topic-keyed** — `automation/research-runs/<slug>/` (NOT date-prefixed). This is load-bearing for cross-night resume: an unfinished topic must land in the SAME dir the next night so it continues instead of restarting. (A date-prefixed dir defeated this — fixed 2026-06-24.)

`automation/research-runs/<slug>/state.json` + `findings.md`:
```json
{
  "topic": "...", "slug": "...", "report_path": "raw/research/self-research/<date>_<slug>.md",
  "started": "<iso>",
  "angles": [
    {"id":1,"name":"value-chain map","status":"done","retries":0},
    {"id":2,"name":"chokepoint quality (Framework 12)","status":"pending","retries":1}
  ],
  "synthesis": {"status":"pending"}
}
```
`findings.md` accumulates each angle under `## Angle N: <name>`. A killed/throttled run re-reads `state.json`, **skips `done`, retries `pending`/`failed`** — no lost work.

## The calls (concrete)
- **Scope:** "Given «{topic}», output a JSON list of ~12 focused, non-overlapping research angles a stock analyst would investigate. No prose." (fallback: a fixed vault template — value-chain / chokepoint-quality / competitors-&-tail / demand / risks-&-falsifiers / …)
- **Per angle (research):** "Research ONLY «{angle}» of «{topic}». 5–8 reputable web sources. Tag each claim Tier 3/4. 300–500 words + inline source links. Output ONLY the findings markdown. Discovery-only — write nothing to disk."
- **Per angle (verify):** "Here are findings on «{angle}»: {text}. Check each load-bearing claim against a second source; flag any unsupported/Tier-5 ones. Output a short corrected/annotated version."
- **Synthesis:** "Read {findings.md}. Synthesize a Tier-3 discovery anchor in the vault format (one-paragraph verdict · value-chain map · analysis · what-to-verify leads). Discovery-only. Save to EXACTLY {report_path}."

## Resilience
After each call, inspect result:
- **transient** (empty / exit≠0) → backoff 60→180s, retry inline up to 3×.
- **usage-cap throttle** ("session limit"/"usage limit"/"resets …") → **wait until the cap resets, then continue** (see Wait-through), bounded by the 06:00 deadline. Only at the deadline does it checkpoint + stop and resume next run.
- **graceful degradation** — synthesis runs on whatever angles succeeded; flags the gaps. Always a report if ≥1 angle landed.

## Observability (fixes the silent-failure gap)
Every step → `run-<date>.log` + the digest:
```
deep-research (loop): scope ok (12 angles)
  angle 1/12 value-chain ........ ok
  angle 2/12 chokepoint-quality . rate-limited → retry 1 → ok
  angle 7/12 ................... FAILED after 3 retries (skipped)
  synthesis .................... ok → raw/research/self-research/<date>_<slug>.md
```

## Code changes
- **New:** `automation/scripts/research_loop.py` — the engine (scope / loop / verify / synthesize / retry / checkpoint / resume).
- **Modified:** `automation/scripts/run.py` — `deep_research_step()` calls `research_loop.run(question, report_path, log)` instead of the heavy `build_deepresearch_cmd`; raise its timeout; emit per-step log lines. `--pick`/`--mark-done`/`--propose` integration unchanged.
- **New (transient, gitignored):** `automation/research-runs/`.
- **Contract unchanged:** report still lands at `raw/research/self-research/`; topics-list lifecycle identical; discovery-only allow-list preserved.

## Operational requirements (60-agent overnight run)
- Mac **awake 02:30–~06:00** (launchd won't wake it; if it sleeps mid-run the loop pauses, resumes next wake/run).
- `run_timeout` raised to ~4 h.

## Honest tradeoffs vs `/deep-research`
- Per-angle single/double-pass research + one verify call ≠ deep-research's 3-vote adversarial per claim. Rigorous, but a notch less. Acceptable for a human-gated Tier-3 anchor.
- Slower (paced) — that's the point overnight.
- Resilience makes a throttle a *pause*, not a *failure* — the core win.

## Verification (post-build)
- `python3 automation/scripts/research_loop.py --topic "test" --dry-run` → prints the planned calls, runs none.
- one live angle → `findings.md` gets a section.
- kill mid-loop, re-run → skips `done`, finishes.
- full run → report at `raw/research/self-research/`, per-step log present, peak concurrency = 2.
