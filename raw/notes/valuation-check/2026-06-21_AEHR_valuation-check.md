# AEHR (Aehr Test Systems) — valuation-check (reverse DCF) — 2026-06-21 · DEEP (red-teamed)

*Tier-3 discovery, reverse-DCF. NOT canon, NOT a fair value, NOT a buy/sell. Says what the market is implicitly assuming and how rare that is — nothing about what to do. Market cap user-provided. Math by `scripts/reverse_dcf.py` + `scripts/base_rate_score.py`; method anchors in `raw/research/reverse-dcf-*.md` + `mauboussin-base-rate-tables.md`. Three-agent DEEP run (extract+compute / adversarial verify / red-team), independently re-verified.*

**Inputs (base):** market cap **$3.62B** (~61× FY2025 sales) · net cash **−$37.1M** (no debt) · revenue **$59M** (FY2025; $0–325M size bucket) · current op margin **−9.7%** · path **revenue** (loss-making FY2025; profitable FY2023–24) · terminal margin **18%** (AEHR's own FY2023 20.6% / FY2024 15.2%) · WACC **12%** · sales-to-capital 2.5 · terminal g 3% · horizon 10.

## ★ For the price to make sense, AEHR has to BECOME:

1. **Grow revenue ~48% a year for a decade** — from $59M to **~$3 billion** (a ~50× revenue ramp).
2. **AND reach a ~38% operating margin at maturity** — *nearly 2× its all-time best (20.6%, FY2023)*, and above where the best test-equipment franchises ever operate (the scaled peer [[ONTO]] runs 13–19% through-cycle, ~25–28% only at peak).
3. **Clear the history bar:** ~46% real growth for a $0–325M-sales company was done by only **≈2.1% of firms ever → priced for perfection.**

And the binding wall: a ~$3B AEHR would have to **capture essentially its entire stated burn-in TAM as a near-monopolist** (its own disclosure: package-level burn-in "multi-hundreds of millions," only ~5–20% of ASICs / ~50% of AI accelerators burned in today) — *while* that market expands several-fold.

**The lever the answer hinges on:** the terminal margin (the engine ranks it the top driver). **It's a conditional read, not a fact.**

## The headline — priced beyond perfection, and it's an inversion

At any margin **AEHR has ever earned** (≤~22%), **the $3.62B price is NOT DCF-justifiable at all** — even +100% revenue growth for 10 years tops out at ~$1.25B of EV (≈35% of the price). The price only *computes* at a **~37–38% terminal margin** — and even then it still needs **~48% revenue CAGR** (top ~2%). This is the inversion: the **bear and base cases can't even be priced** (the price exceeds what the math allows); only the bull case produces a number, and it's an outlier on two axes at once, with **85% of value in a terminal business that doesn't yet exist** (FY2025 was an operating *loss*).

## Bull / base / bear (engine outputs; revenue path, the dominant lever = terminal margin)

| Case | Terminal margin | Result | Implied | Base-rate |
|---|---|---|---|---|
| **Bear** — AEHR's own history | 18–22% | **Not DCF-justifiable** (max EV $1.25–1.73B) | impossible at any growth | — |
| **Base** — optimistic scale (Teradyne/ONTO-peak) | 25% | **Not DCF-justifiable** (max EV $2.10B; fails even at 10% WACC) | impossible | — |
| **Bull** — differentiated-AI-test re-rate | 38–40% | solves | ~47–48% CAGR | **≈top 2% — priced for perfection** |

## Red-team (the `deep` pass) — does the verdict survive the strongest fair attack?

**Verdict: SURVIVES (bends, doesn't break).** Agent 3 built the most *defensible* bull — a near-doubled revenue base ($100M, on order momentum), 25% margin (ONTO-best), 9% WACC (de-risked), and a **15-year** horizon — and only then does the required growth fall to "above-median ordinary" (~26–28% CAGR). But that reads better than it is: it requires **stacking four stretches at once**, and the "ordinary" label is partly an **artifact** — the base-rate scorer snaps a 15-year horizon to its 10-year table, *understating* how rare 15 straight years of ~26% growth is for a sub-$325M company. Knock out **any one** stretch — use AEHR's actual $59M base, or the standard 10-year horizon, or a margin it has actually sustained — and it **lands right back in the ≈3–8% base-rate "priced for perfection" zone.** The conclusion holds.

## Agent-2 verification (what was checked / corrected)
- Every Agent-1 input **held** against the FY2025 10-K + Q3 FY2026 10-Q (net cash $36.9M raw vs $37.1M rounded — immaterial; current margin −9.6% vs −9.7%; revenue $58,968K confirmed).
- **The terminal margin is, if anything, generous** — the AI mix shifts revenue toward *lower*-margin package-level Sonoma (vs high-margin wafer-level FOX); Q3 FY26 non-GAAP GM already compressed to 36.5%.
- **Right peer benchmark established:** not the broad "Semiconductor" sector (~35% — chip designers, wrong comp) but **semi test/capital equipment** — [[ONTO]] (the scaled version of AEHR's niche) at 13–19% op / ~25–28% peak. So 18–25% is the realistic mature band; 35–40% has no peer precedent.
- The record-backlog bull argument doesn't rescue the base (effective backlog $50.9M < $59M trailing; Q3 revenue −44% YoY, FY26 guide cut to $45–50M).

## Fit + caveats
- **Reverse DCF is a genuinely WEAK fit** — AEHR is tiny ($59M), lumpy (book-to-bill >3.5×), single-customer-concentrated (~42%), and mid-inflection (SiC/EV collapsing, AI/HBM burn-in ramping but unconverted). 85% of value sits in an un-modelable terminal. The honest output is **not** a point estimate but the **falsification result**: the price can't be reconciled with AEHR's own demonstrated economics.
- **A real (minor) scorer limitation surfaced:** the base-rate percentile snaps multi-year horizons (>10y) to the 10-year table, understating rarity for long-CAP cases — flagged for a future scorer refinement.
- Outputs conditional on the assumption set. SBC expensed; FY2024 one-off ($20.7M valuation-allowance release) stripped.

**Sources:** `wiki/companies/AEHR.md` (Financial snapshot, Thesis-role) · `raw/filings/AEHR/` (FY2025 10-K, Q3 FY2026 10-Q) · market cap user-provided.
