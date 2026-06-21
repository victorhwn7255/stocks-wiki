# AAOI — valuation-check (reverse DCF / market-implied expectations) — 2026-06-21

*Tier-3 discovery, reverse-DCF. NOT canon, NOT a fair value, NOT a buy/sell. This says what the market is implicitly assuming and how rare that is — nothing about what to do. Market cap is an auto-fetched APPROXIMATE figure for this run; re-run with the live cap before relying on it. Math by `scripts/reverse_dcf.py` + `scripts/base_rate_score.py`; method anchors in `raw/research/reverse-dcf-*.md` + `mauboussin-base-rate-tables.md`. Two-agent run (extract+compute / adversarial verify), independently re-verified.*

**Inputs:** market cap **$12.99B** · net cash **−$242.9M** (corrected: 10-Q shows 3 debt buckets — revolver $41.2M + bank-acceptance $35.8M + converts $129.5M = $206.5M, vs $449.4M cash) · TTM revenue **$507M** ($325–700M size bucket) · current op margin **−8.6%** · path **revenue** (loss-making) · WACC **12%** (small-cap, top-2 customers ~82%, loss-making, heavy dilution → top of band) · terminal g 3% · horizon 10.

## The headline — a double-bind (priced beyond perfection)

At a **defensible 10% mature operating margin** (already generous for a "minimally differentiated" assembler — the differentiated peers LITE/COHR run ~24–30% best-case), **the ~$13B price is NOT DCF-justifiable at all** — even +100% initial revenue growth fading over 10y produces only **$799M of EV** vs the **$12.75B** the price implies.

The price only *computes* if you assume a **~21%+ mature margin** (roughly 2× a defensible assembler margin, and 2× management's own optimistic non-GAAP) — and even then it requires **~92% initial revenue growth → ~45% 10-year CAGR**, which the base-rate scorer puts at **≈0% historical precedent** for a $325–700M-sales company (the Tesla/OpenAI near-zero tail). **102% of value sits in a terminal business that doesn't yet exist.**

So the price is priced-for-perfection on **two independent axes at once**: a margin re-rate the filings give zero evidence for (CPO/silicon-photonics/LPO go unmentioned), *on top of* growth essentially no company its size has ever delivered.

## Bull / base / bear (engine outputs; net cash −$242.9M, rev $507M, WACC 12%)

| Case | Terminal margin (the whole ballgame) | Verdict | Base-rate |
|---|---|---|---|
| **Bear** — defensible assembler | 8–10% | **Not DCF-justifiable** (even +100% growth → $0.8B EV) | price has no cash-flow justification |
| **Base** — optimistic non-GAAP | 13–15% | **Not DCF-justifiable** ($3.9–6.0B EV; holds at WACC 11–13%) | unjustifiable even at 2× current margin |
| **Bull** — merchant-laser re-rate | 22–25% | solvable → ~45–48% 10y CAGR | **≈0% — no precedent (Tesla/OpenAI tail)** |

Robust to WACC (11–13%) and sales-to-capital (2.0–3.0).

## Agent-2 verification (what was checked / corrected)
- **Net cash corrected** −$324.4M → −$242.9M (Agent 1 counted one debt bucket; the 10-Q has three). Immaterial — nudges EV +0.6%, slightly *sharpens* the double-bind.
- Revenue $507M, the 12% WACC, and the revenue path all **held** against `raw/filings/AAOI/AAOI-10Q-2026-03-31.htm`.
- The 10% terminal margin verified **defensible-to-generous** by benchmarking the differentiated peers (LITE ~30%, COHR ~24% best-case) — AAOI is explicitly *not* differentiated (10-K "minimally differentiated," never a positive operating margin).

## Fit + caveats
- **Reverse DCF is a partial fit** — AAOI is pre-profit + inflecting, so the answer hinges entirely on the (unknowable) normalized margin. The output lands at a "doesn't compute at a defensible margin" wall rather than a clean implied-growth number — and that double-bind *is* the more honest, more useful finding.
- **Per-share erosion not captured:** ~22% annualized dilution (+ a post-snapshot $600M ATM in the unverified Latest-alpha) erodes the equity independent of this firm-level EV math.
- Outputs conditional on the assumption set above. SBC expensed throughout.

**Sources:** `wiki/companies/AAOI.md` (Financial snapshot) · `raw/filings/AAOI/AAOI-10Q-2026-03-31.htm` · market cap auto-fetched (approximate).
