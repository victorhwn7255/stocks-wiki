---
name: extract-learnings
description: The self-improving loop for the stocks-wiki vault — mine recent session traces (log.md tail, refresh_log.md, conventions-ledger.md) and the monitor_patterns.py accumulation state for promotable codification candidates and MEMORY.md drift, then DRAFT codification proposals into automation/codification/ for human review. Use when the user asks what we've learned recently, which patterns are ready to codify, to draft codification proposals, to surface convention updates, or to shorten the learn→codify lag. Trigger on "extract learnings", "what should we codify", "draft codification", "what patterns are ready", "mine recent sessions". Propose-only — it drafts to automation/codification/, never edits CLAUDE.md / frameworks / the anchors (those are human-owned).
---

# extract-learnings — the self-improving loop (RL-from-traces, drafted)

This skill is the agentic draft layer on top of `learning-monitor`. Where `learning-monitor` *counts* pattern instances and flags threshold crossings, this skill *reads the traces* — including the `calibration-check` loop's scored **WRONG / PARTIAL** calls — and *drafts the codification proposal*, shortening the lag between noticing a pattern and promoting it to a convention. Mining the calibration output is what **closes the self-X loop**: self-maintenance (`vault-hygiene`) → self-evaluation (`calibration-check`) → self-improvement (this skill) *compound* instead of running as three separate scans.

## The boundary (propose-only — human-owned anchors)

Writes ONLY inside `automation/codification/`. MUST NOT edit `CLAUDE.md`, `raw/notes/frameworks*.md`, the three `_thesis*` anchors (all human-owned), or any `wiki/` page / `index.md` / `log.md`. It DRAFTS proposals; Vic makes the actual codification edit at a codification session. Never runs git.

## When to invoke

Any ask about recent learnings, codification readiness, drafting convention proposals, or shortening the learn→codify lag. Also: a Phase-3 step of the automation runner.

## Steps

1. **Get the accumulation state (deterministic):**
   ```bash
   python3 scripts/monitor_patterns.py
   ```
   Note patterns AT threshold (codification candidates) and MEMORY.md drift.

2. **Mine the traces** for what changed and what was learned:
   - `log.md` tail (recent sessions' Phase-4 reflections + backlog items),
   - `raw/notes/refresh_log.md` (per-company refresh deltas),
   - `raw/notes/conventions-ledger.md` (codification history + per-instance evidence),
   - **`automation/calibration/*_scored.md` + `scorecard.md`** (the self-evaluation output — the **WRONG / PARTIAL** verdicts and their one-line lessons; this is the loop-closing source).
   Look for: a pattern that crossed its threshold; a convention that proved wrong / was retired; a recurring methodology that isn't codified yet; MEMORY drift vs the live counts; **a scored call that came out WRONG/PARTIAL — its lesson is an inverse-RL signal for the "negative signal / retire" section.**

3. **Draft proposals** to `automation/codification/<YYYY-MM-DD>_proposals.md`, one block each:
   `date · pattern/convention · instance count + where (cite the ledger / pages) · the proposed convention text (a paste-ready draft) · which human-owned file it would touch (CLAUDE.md §X / frameworks / anchor) · the case for codifying now`.
   Include a "negative signal" section: anything the vault got wrong or a belief that should be retired.

4. **Flag, don't edit.** Every proposal is for Vic to gate. Surface the top 1–3 highest-readiness candidates; do not touch the human-owned files.

## Disciplines

- **Human-owned anchors are sacrosanct** — propose, never silently edit (CLAUDE.md §1.1 / §5.3).
- **Honest-verdict** — include what was *wrong* / retired, not just new patterns (two-sided RL signal).
- **Brevity** — proposals follow the §3.8 brevity discipline; a draft convention is paste-ready, not an essay.

## What this skill is NOT

- Not a codifier — it drafts; Vic codifies (the human gate is the point).
- Not `learning-monitor` — that counts; this drafts on top of it.
- Not a canon editor.
