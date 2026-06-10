---
name: chokepoint-eval
description: "Run the six-question chokepoint-durability test on a vault chokepoint/theme page or a new candidate — buyer-defense, supply-response, generational lockout, substitution tail, demand-ramp, geology/policy overlay — producing an evidence-cited scorecard and a one-line durability verdict (memory-grade / quality-but-cyclical / theme-spike / policy-contingent / conditional-on-demand). Read-only on the vault; flags page contradictions, never edits."
---

# chokepoint-eval — the six-question chokepoint-durability test

This skill answers one question with a fixed rubric: **how durable is this chokepoint, really?** Concentration alone doesn't make a chokepoint — the test probes the things that actually decide whether an oligopoly holds: whether buyers defend it with money, how fast supply can answer, whether technology gates lock out laggards, how close the substitution tail is, whether the gated thing is even ramping, and whether atoms/borders add durability the economics miss.

**Origin + status (say this in every output):** the rubric is **CODIFIED CANONICAL DOCTRINE — `raw/notes/frameworks.md` Framework 12 (v10.2, Vic-authorized 2026-06-10)**. Framework 12 is the authoritative text (six questions, verdict scale incl. the provisional "quality-but-competitive" 6th label, calibration anchors, pre-registered revision triggers); this skill is the operational runner. Cite the verdict as "per Framework 12." Origin: derived from the MLCC-vs-HBM comparison (`raw/research/mlcc-ai-datacenter-bottleneck-report.md` Part 3; `wiki/themes/MLCC-oligopoly.md`), refined on the photonics family (Q5 from [[cpo-integration]], Q6 from [[InP-supply]]). If a run trips one of Framework 12's revision triggers, flag it for Vic — the framework text is human-owned again post-codification.

## The hard boundary

**Read-only on the vault.** This skill MUST NOT edit anything under `wiki/`, or `index.md`, `log.md`, `refresh_log.md`, `conventions-ledger.md`, the three `_thesis*` anchors, or any `frameworks*` file. If a score **contradicts** a page's current framing (e.g., a page calls something canonical-chokepoint-grade and the test says theme-spike), the skill **FLAGS the tension for a human-gated page update** — it never reconciles silently. Output is chat-first; a discovery note to `raw/notes/chokepoint-eval/` only on explicit request (not in `index.md`/`log.md`; doesn't count for accounting).

## When to use

- The user invokes `/chokepoint-eval <page-or-candidate>` or asks "how durable is X as a chokepoint?" / "is X a real chokepoint?"
- At Stop-1 planning for a **new chokepoint page** (informs the Pathway 1 provisional vs Pathway 2 canonical judgment, CLAUDE.md §3.15).
- At a **chokepoint refresh** (has the score moved since the last ingest?).
- When writing or updating a **forward-edge-tracker entry** (the durability-anchor field).

Not for: company-level analysis (that's the company page), broad theme sweeps, or anything requiring a page edit (flag instead).

## Inputs

One of:
- **A vault page name** — e.g. `/chokepoint-eval InP-supply` or `/chokepoint-eval MLCC-oligopoly`. Read the page from `wiki/chokepoints/` or `wiki/themes/` (check both); evidence comes primarily from the page itself + directly cited vault pages.
- **A new candidate name** — e.g. `/chokepoint-eval ABF-substrates`. No page exists: do **light web research** first (a few searches; primary/company sources preferred), tag every datapoint Tier 3/4, and say plainly that the run is research-grade, not vault-grade.

## The six questions (every cell needs cited evidence — never vibes)

| # | Question | What passes / what fails |
|---|---|---|
| **Q1 — BUYER-DEFENSE** | Is anyone *paying* to defend the supplier? Equity stakes, prepayments, capacity bookings, binding LTAs. | **Gold standard:** [[NVDA]]'s $2B each into [[LITE]] + [[COHR]] (buyers defending laser supply with money). **Fail mode (the MLCC lesson):** a tiny %-of-BOM component nobody writes checks for — criticality without defense. |
| **Q2 — SUPPLY-RESPONSE** | How fast can capacity answer demand? | **<24 months = weak** (buildings + known process, e.g. MLCC kilns). **3+ years = strong** (leading-edge fabs, crystal growth, TSMC-grade packaging). Cite actual announced expansions + their dates. |
| **Q3 — GENERATIONAL LOCKOUT** | Do hard technology gates exclude laggards each generation (HBM4-style), or is progress continuous (always partially substitutable)? | Hard gates = strong. Continuous improvement = weak — the tail always absorbs the less-extreme parts of demand. |
| **Q4 — SUBSTITUTION TAIL** | How many credible second-tier / regional makers exist, and how close are they? | ~3 makers on Earth = strong (HBM). A second tier + a fast regional tier (China) already shipping adjacent grades = weak. Name the tail members. |
| **Q5 — DEMAND-RAMP** *(blind spot #1, from CPO)* | Is the thing this chokepoint gates actually ramping — or is ownership perfect for a market that may not arrive? | A 4/4 economic score is conditional if adoption is unresolved (CPO: maximal ownership, open adoption question). Cite the demand evidence + the route risks. |
| **Q6 — GEOLOGY/POLICY OVERLAY** *(blind spot #2, from InP)* | Do atoms/borders add durability the economics miss — or does policy expiry add fragility? | Geology/geographic concentration (indium, rare earths) can rescue a failed Q1. Policy-created chokepoints (Blue-UAS-style, expiry-dated) are fragile regardless of score. Cross-check the chokepoint-quality gradient: **geology/physics > precision-manufacturing > policy.** |

Scoring per cell: **pass / weak / fail** (or **split** when a page contains two different-quality sub-chokepoints — e.g. advanced-optical-packaging = wafer-level ~4/4 vs precision-assembly ~2/4; say so rather than averaging).

## Output (chat-first)

1. **Scorecard table** — Q1–Q6 × evidence (cited to page section or source) × pass/weak/fail.
2. **One-line verdict** using the standard five-label scale:
   - **memory-grade** — durable structural chokepoint (passes the economics AND the demand/overlay checks)
   - **quality-but-cyclical** — real moat at a top bin, but the cycle/tail caps durability (the MLCC verdict)
   - **theme-spike** — narrative without structural ownership
   - **policy-contingent** — durability rests on statute/subsidy with an expiry or political gate
   - **conditional-on-demand** — ownership maximal, adoption unresolved (the CPO verdict)
3. **"What would change the score"** — 2–3 pre-registered triggers (dated where possible) that would upgrade or downgrade the verdict.
4. **Contradiction flag (if any):** if the verdict conflicts with the page's current framing or tier placement, state the tension plainly and recommend a human-gated page update — do not edit.
5. The one-line methodology status note (agent-side rubric, pending frameworks codification).

On explicit request only, save the full scorecard as `raw/notes/chokepoint-eval/<RUN_DATE>_<name>.md`.

## Disciplines

- **Honest-verdict** — no manufactured passes; if the evidence says theme-spike, say theme-spike. A run that flatters every chokepoint is a failed run.
- **Evidence per cell** — each Q cites the page section, vault page, or (for candidates) the researched source + tier tag. "Everyone knows" is not evidence.
- **Describe-don't-recommend** — durability verdicts, never buy/sell; no price targets, valuation, or position language.
- **Plain language**, short sentences.
- **Splits over averages** — when a page holds two sub-chokepoints of different quality, score them separately.

## Reference results (calibration anchors — do not re-derive, verify against)

From the 2026-06-10 derivation runs:
- [[datacenter-laser-supply]] (UHP/ELS bin): 4/4 economics + Q1 *proven* ($2B×2) → strongest in vault.
- [[cpo-integration]]: 4/4 economics, Q5 open → **conditional-on-demand**.
- [[advanced-optical-packaging]]: **split** — wafer-level (TSM COUPE) ~4/4; precision assembly (FN) ~2/4.
- [[InP-supply]]: fails Q1 (like MLCC), Q6 rescue (indium geology + China domicile) → quality chokepoint whose crisis mode is geopolitical, not economic.
- [[MLCC-oligopoly]]: 1/4 except the top bin → **quality-but-cyclical** (the founding run).

## What this skill is NOT

- Not a page writer or editor — read-only; contradictions get flagged, not fixed.
- Not a replacement for the chokepoint-quality gradient or the theses — it complements them (Q6 cross-checks the gradient explicitly).
- Not a buy/sell or sizing tool.
- Not canonical doctrine until Vic codifies the rubric into `frameworks.md`.
