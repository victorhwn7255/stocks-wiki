# MU (Micron) — valuation-check (reverse DCF / market-implied expectations) — 2026-06-21

*Tier-3 discovery, reverse-DCF. NOT canon, NOT a fair value, NOT a buy/sell. Market cap is an auto-fetched APPROXIMATE figure for this run. Math by `scripts/reverse_dcf.py` + `scripts/base_rate_score.py`; method anchors in `raw/research/reverse-dcf-*.md` + `mauboussin-base-rate-tables.md`. Two-agent run (extract+compute / adversarial verify), independently re-verified.*

**Inputs:** market cap **$1.28T** · net cash **−$6.5B** (debt $10.1B − cash $16.7B) · TTM revenue **$58B** (mega >$50B size bucket) · path **fcff** · WACC **9.5%** · terminal g 3% · horizon 10.

## The headline — reverse DCF is the WRONG primary tool here (cyclical at peak)

MU is a deeply cyclical memory (DRAM/NAND) business sitting at a **textbook cyclical peak** (Q2 FY2026 gross margin ~75%, one-quarter net income $13.8B) — the same snapshot shows the trough two years earlier (FY2023 net loss **−$5.8B**). That swing *is* the cycle.

A reverse DCF **systematically misreads a cyclical at peak.** The market doesn't pay a high multiple here — it pays a **low ~15× multiple on PEAK earnings** (verified: ~14.8× on the guided run-rate), the classic "cheap at the top" cyclical signature, *because* everyone expects mean reversion. A growth-DCF can't see that: fed a low normalized base, it must manufacture a huge growth rate to bridge up to a price set against *peak* cash flow. So the "implied growth" is an artifact of the base you feed it, not a real market expectation.

**The proof is the fragility:** the implied growth swings **20% → 45%** purely on whether you feed peak vs normalized FCFF — while a ±1% WACC move shifts it only ~3 points. The model's verdict is hostage to the one input it can't pin down. **That fragility is the finding.**

## What each base implies (engine outputs; EV $1.27T, WACC 9.5%, 10y)

| Case | FCFF base | Story | Implied FCFF growth | Base-rate |
|---|---|---|---|---|
| **Bear** — deep-cycle reversion | ~$3.5B | trailing FY25 FCF was only $1.67B | **~47%/yr** | ≈0% — no precedent |
| **Base** — AI-era higher mid-cycle | ~$7B | LTAs/HBM lift the trough | **~36%/yr** | ≈0% — no precedent |
| **Bull** — durable supercycle | ~$18B | near-peak FCF persists | **~23%/yr** | ≈0% — no precedent (least extreme) |
| *(peak ref)* | $21.6B | annualized H1 FY26 | ~20.5%/yr | ≈0% |

Every cell scores ≈0% base rate (18–47% real sales growth for a mega-cap is historically unprecedented), and TV% (70–81%) / PVGO (82–97%) are all in the engine's "very assumption-heavy" zone.

## Agent-2 verification (what was checked / corrected)
- **Normalization stress-tested + sharpened.** Pulled the actual 10-K cash flow: FY23 FCF **−$6.1B** / FY24 **+$0.1B** / FY25 **+$1.7B** → **3-yr cumulative FCF is NEGATIVE (−$4.3B)**. So Agent 1's $4.0B normalized FCFF is *generous*, not low. Capex ($15.9B FY25, >$25B FY26 guide) structurally suppresses trailing FCF while peak ASPs inflate OCF — neither peak nor normalized is "clean."
- Net cash −$6.5B and the peak-FCFF arithmetic ($10.79B H1 ×2 = $21.6B) **held** against the snapshot.

## Fit + the real question
- **Reverse DCF is a WEAK fit for MU** — it misreads a cyclical-at-peak as "priced for high growth." Use **normalized mid-cycle earnings power × a through-cycle multiple**, or an explicit cyclical/scenario framework.
- The question that actually matters is **MU Open Question #8**: has the AI/HBM era *structurally* raised mid-cycle profitability (the "memory is no longer cyclical" PBR→PER re-rating), or does it mean-revert? That cyclical-vs-structural debate — not a single implied-growth number — is the decision. The same $1.27T can be told as ~$21B growing 20%, ~$7B growing 36%, or ~$70–90B durable at no-growth — same price, different stories.
- Outputs conditional on the assumption set. SBC expensed (FCF is post-SBC cash FCF).

**Sources:** `wiki/companies/MU.md` (Financial snapshot) · `raw/filings/MU/` (FY2023–25 10-K cash flow) · market cap auto-fetched (approximate).
