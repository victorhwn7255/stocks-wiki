---
name: calibration-check
description: The self-evaluation loop for the stocks-wiki vault — sweep the vault's pre-registered falsifiers, dated catalysts, and tripwires (forward-edge-tracker + what-could-go-wrong + Open-questions), then score the ones that have resolved against current primary state, writing dated scored records to automation/calibration/. This is the vault's "private evals" fitness function — did our structural calls turn out right? Use when the user asks to score the vault's calls, check whether catalysts fired or falsifiers tripped, run a calibration sweep, grade past verdicts, or build the accuracy scorecard. Trigger on "calibration", "did our calls hold", "score the forward edge", "which falsifiers fired", "check the tripwires", "how accurate were we". Discovery-only — it writes scored records to automation/calibration/, never edits canon.
---

# calibration-check — the self-evaluation loop (private evals)

This skill closes the vault's learning loop: it scores whether the vault's pre-registered structural calls turned out right. It generalizes the §4.6 falsification streak from *process*-accuracy ("did our kickoff match the filing?") to *analytical*-accuracy ("did our chokepoint verdict / forward-edge view hold?"). It is the missing "private evals" pillar.

## The boundary (discovery-only)

Writes ONLY inside `automation/calibration/`. MUST NOT edit any `wiki/` page (including the trackers it reads), `index.md`, `log.md`, `_thesis*`, `frameworks*`, or `CLAUDE.md`, and never runs git. When a score implies a tracker should change (a catalyst fired → a forward-edge entry should move; a tripwire fired → `what-could-go-wrong` should mark it), it **FLAGS that for a separate human-gated update** — it never cascades into canon. (When run headlessly by the automation runner, the locked tool allow-list enforces this.)

## When to invoke

Any ask about scoring the vault's calls, whether catalysts fired / falsifiers tripped, grading past verdicts, or building the accuracy scorecard. Also: the weekly automation runner surfaces the candidate list; this skill (interactive or via `claude -p`) does the scoring.

## Steps

1. **Get the candidate list (deterministic):**
   ```bash
   python3 scripts/calibration_sweep.py            # human-readable
   python3 scripts/calibration_sweep.py --json      # machine-readable
   python3 scripts/calibration_sweep.py --due-days 30
   ```
   It parses `forward-edge-tracker.md` (Catalyst / Falsifier / Last moved) and `what-could-go-wrong.md` (Tripwire / Status / Last checked), extracts dated/temporal markers, and ranks by FIRED → review-due → oldest. It surfaces WHAT to score; it does not score.

2. **Score each due / dated candidate against CURRENT PRIMARY STATE.** For each entry flagged review-due or carrying a watch date that has arrived:
   - read the entry's catalyst/falsifier/tripwire and its canonical home page;
   - check the most recent primary evidence (the company page's latest snapshot, a tracker reading, a recent filing/8-K in `raw/`) — Tier 1/2 only decides a verdict; Tier 3/4 may *name* a mechanism but never *fires* a tripwire (CLAUDE.md §2.2);
   - assign a verdict: **RIGHT** (call held / falsifier correctly stayed un-tripped) · **WRONG** (falsifier tripped / catalyst fired against us) · **PARTIAL** · **STILL-OPEN** (not yet testable).

3. **Write the scored record** to `automation/calibration/<YYYY-MM-DD>_scored.md`, one block per scored entry:
   `date · entry (source + title) · the pre-registered call · current primary evidence (cited) · verdict {RIGHT/WRONG/PARTIAL/STILL-OPEN} · one-line lesson · [flag: tracker update needed?]`.
   Append/refresh a running `automation/calibration/scorecard.md` roll-up (counts by verdict → the accuracy %).

4. **Flag, don't cascade.** List any canon updates the scores imply (a forward-edge entry to move, a tripwire to mark FIRED) as human-gated follow-ups. Do not edit the trackers.

## Disciplines

- **Honest-verdict** — a WRONG call is recorded plainly; the point is calibration, not a flattering record.
- **Tier discipline** — only primary sources fire a verdict; flag Tier-3-only signals as STILL-OPEN-pending-primary.
- **Describe-don't-recommend; no price/valuation** — score structural calls, never buy/sell or price targets.

## What this skill is NOT

- Not a canon/ tracker editor — it scores and flags; the human moves the trackers.
- Not the hygiene scan (that's `vault-hygiene`).
- Not a forecaster — it grades *resolved* calls against what actually happened.
