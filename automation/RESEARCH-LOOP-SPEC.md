# Spec — Sequential Research Loop (`research_loop.py`)

The headless-reliable replacement for the bundled `/deep-research` workflow in the nightly automation. Same output contract (a Tier-3 report at `raw/research/self-research/<date>_<slug>.md`); gentle on the rate limit; resumable.

## Why this exists
The 2026-06-19 02:30 run fired the bundled deep-research, which exploded into **104 simultaneous agents / 2.85M tokens in 8 minutes** and was cut off by a **rate/concurrency throttle** (NOT a budget cap — weekly was 38%, the 5-hour window 78%). Headless `claude -p` agents **fail-fast** on a throttle instead of waiting/retrying like interactive mode, so 61 agents died at once and no report was written. This loop fixes both: **low concurrency + pacing** (never bursts) and **checkpoint + resume** (a throttle pauses, never wipes).

## Flow
```
scope (topic → angles)  →  per-angle research + verify (peak 2)  →  CONNECTIONS (10 grounded agents)  →  synthesis
```
The CONNECTIONS step ties the night's findings to the existing vault before synthesis — 10 agents, each grepping its own slice, honest-verdict ("no material connection" is valid), feeding a consolidated "Vault connections" report section.

## Config (the dials)
- `max_agents = 60` — total `claude -p` calls across a run (scope + angles×research/verify + connections + synthesis).
- `max_concurrent = 2` — never more than 2 small agents alive at once. **This is the load-bearing safety setting** — it's what keeps the run under the concurrency throttle, regardless of total size or token budget.
- `pace_seconds = 30` — sleep between waves.
- `per_call_timeout = 600` (10 min) · `run_timeout = 14400` (4 h) — a 60-agent run can take ~2–4 h overnight.
- `max_retries = 3` per call.

## Agent budget — how it's spent (a 15-angle run ≈ 42 calls, cap 60)
| Step | Calls |
|---|---|
| Scope (topic → angles) | 1 |
| Per angle: research + verify | ~15 angles × 2 = 30 |
| **CONNECTIONS** (10 grounded agents — see below) | 10 |
| Synthesis | 1 |
Each call is **one flat agent** restricted to `Read, Grep, Glob, WebSearch, WebFetch` — **no `Agent`/`Workflow`/`Task` tools**, so a call physically cannot fan out a swarm. Peak concurrency stays 2 no matter what.

## CONNECTIONS — the 10 grounded agents
Run between research and synthesis. Each reads the angle findings + greps its slice of the vault; reports only meaningful CONFIRM / CHALLENGE / EXTEND links (wikilink only verified pages); output appended to `findings.md` as a `## Vault connection: <label>` block that synthesis consolidates.
| # | Agent | Slice / lens |
|---|---|---|
| 1–2 | `companies-A/B` | the 81 company pages, split in half — which tickers are already covered + what findings add |
| 3–4 | `themes-A/B` | the 24 theme pages, split in half — CONFIRM/CHALLENGE/EXTEND |
| 5 | `chokepoints-confirm` | all chokepoints — where findings **reinforce** a thesis |
| 6 | `chokepoints-challenge` | all chokepoints — adversarial: where findings **threaten** a thesis |
| 7 | `trackers-relationships` | trackers + relationship — does a finding fire a falsifier/catalyst/tripwire? |
| 8 | `thesis-frameworks` | the 3 thesis anchors + 3 frameworks — FIT/EXTEND/CHALLENGE the worldview |
| 9 | `prior-research` | `raw/research/` anchors + self-research — overlap/extend/contradict (tagged `discovery↔discovery (unverified)`) |
| 10 | `coverage-gaps` | whole vault — the absence check: what entities have **no page** → candidate new pages |

Connections are paced + checkpointed exactly like the angle loop (state `connections[]`); a throttle mid-connections pauses + resumes; graceful degradation (synthesis uses whatever landed).

## Topic source (unchanged pipeline)
Topics come from `raw/research/topics-list.md` via `research_agenda.py`:
- **Pending** (Vic-curated, ranked) → the loop `--pick`s the top item each research night.
- **Researched** → `--mark-done` moves it here when the report lands; the rest shift up.
- **Proposed** → the automation `--propose`s new candidates (connection-finder + open-questions); Vic promotes good ones to Pending.
Vic curates + promotes; he does NOT have to supply a topic every day (8 are queued + it self-replenishes).

## State file (resumability)
`automation/research-runs/<date>_<slug>/state.json` + `findings.md`:
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
- **hard throttle** ("session limit"/"rate limit" in output) surviving retries → **checkpoint state.json + exit gracefully**, log `throttled at angle N — will resume next run`. (The 5-hour window resets; next run/night continues.)
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
