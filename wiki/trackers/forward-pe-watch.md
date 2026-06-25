---
type: tracker
tickers: [NVDA, MSFT, GOOGL, AMZN, META, AVGO]
last_updated: 2026-06-24
---

# Forward P/E Watch — S&P 500

A cross-vault **valuation dial**: the S&P 500 **forward price-to-earnings ratio** on **2026 and 2027 estimated EPS** (plus the next-twelve-month blend), tracked over time — *and*, on every reading, **decomposed** into how much of the move came from **price** vs from **earnings-estimate revisions**. The point isn't the P/E level (FactSet/multpl already show that); it's the two things they don't hand you: *"is the multiple getting cheaper because earnings rose, or because price fell?"* and *"are the earnings revisions speeding up or rolling over?"*

This is the **macro backdrop for the AI-datacenter thesis.** The bulk of the current S&P earnings upgrades are **AI mega-cap-concentrated** ([[NVDA]] / [[MSFT]] / [[GOOGL]] / [[AMZN]] / [[META]] / [[AVGO]]), so a roll-over in forward-EPS revisions *while price holds* is an early read on whether the market's earnings story still backs the AI-capex build-out — a companion dial to [[AI-credit-spread-watch]] (the financing-side dial) and [[hyperscaler-capex]] (the demand-side dial).

## Discipline (binding)
- **Describe, don't recommend.** This is a valuation dial. **No price targets, no buy/sell — ever.**
- **One source across the series.** The time-series stays on **LSEG / I-B-E-S operating EPS** (the source on the Fundstrat exhibit that seeded this page). **Never mix LSEG and FactSet within the series** — the ~3–5% methodology gap would read as a fake move. FactSet is an occasional *cross-check*, not a row.
- **Operating-EPS basis.** Forward operating EPS reads a **lower** P/E than trailing GAAP. At the seed date the S&P was ~**18–22× forward** (operating) vs ~**32× trailing GAAP** (multpl, mean ~16× / median ~15×). Both are true; don't compare across them. This page lives on the forward-operating number and says so on every row.
- **Horizon honesty.** The cleanest "next 12 months" figure is **NTM**, not the 2027 calendar number (which is ~18 months out and reads cheaper). All three (2026 / 2027 / NTM) are shown; **NTM is the honest forward multiple.**
- **Every row carries its source + as-of date.** EPS is never invented — if the weekly LSEG number isn't in hand and the last row is stale, the run flags it rather than guessing.

## Readings (the time-series)

*Source: LSEG / I-B-E-S operating EPS, paired with the contemporaneous S&P 500 close. P/E = level ÷ EPS. NTM = time-weighted blend of CY2026/CY2027 (≈ the next-12-month multiple); tracked from the seed row forward.*

| Date | S&P level | 2026 EPS | 2027 EPS | NTM (F4Q) EPS | 2026 P/E | 2027 P/E | Fwd P/E (LSEG) | Source / as-of |
|---|---|---|---|---|---|---|---|---|
| 2025-12-05 | 6,846 | $309.28 | $351.74 | — | 22.1× | 19.5× | — | LSEG I/B/E/S (Fundstrat Exhibit 24 repro) |
| 2026-05-29 | 7,563.63 | $339.51 | $394.62 | $350.81 | 22.3× | 19.2× | 21.6× | LSEG Scorecard (staged; close 28-May) |
| 2026-06-05 | 7,584.31 | $340.07 | $395.95 | $351.69 | 22.3× | 19.2× | 21.6× | LSEG Scorecard (staged; close 4-Jun) |
| 2026-06-12 | 7,394.30 | $340.39 | $397.87 | $352.16 | 21.7× | 18.6× | 21.0× | LSEG Scorecard (staged; close 11-Jun) |
| 2026-06-18 | 7,420.10 | $340.82 | $399.25 | $352.62 | 21.8× | 18.6× | **21.0×** | LSEG Scorecard TRPR_82201 (staged; close 17-Jun) |

*Data home: the weekly LSEG S&P 500 Earnings Scorecards live in `raw/data/forward-earnings/LSEG_reports/`; the extracted machine-readable series (per-report EPS by year + quarter, F4Q/T4Q EPS, forward/trailing P/E, closes) is `raw/data/forward-earnings/forward-earnings-raw-data.csv`. EPS figures are LSEG Exhibit 24 (per-share bottom-up); forward/trailing P/E + F4Q EPS are LSEG Exhibit 23.*

*LSEG's own headline valuation (Ex. 23, .SPX at the 17-Jun close 7,420.10): **forward P/E 21.0×** (on forward-4-quarter EPS 352.62) · **trailing P/E 25.8×** (on trailing-4-quarter operating EPS 287.70). The **forward P/E uses the F4Q/NTM EPS (352.62), not CY2027** — which is why LSEG's "official" forward multiple reads **21.0×** while the Fundstrat slide featured **18.4×** (that's CY2027 EPS, ~18 months out, at a slightly earlier 7,365 close). Same data, different horizon — the cheaper number just looks further out. (Correction: the prior placeholder NTM of $368.83/20.0× was a CY-blend estimate; the primary F4Q figure is $352.62/21.0×, F4Q = Q2'26+Q3'26+Q4'26+Q1'27 incl. the in-progress quarter.)*

## Latest read — decomposition + revision momentum (as of 2026-06-24; 4 weekly LSEG Scorecards staged)

**The 4-week weekly series (May 29 → Jun 18) — estimates grinding steadily up, price flat-to-down, multiple compressing ~0.6 turn.** Forward (F4Q) P/E **21.6× → 21.6× → 21.0× → 21.0×**; CY2027 P/E **19.2× → 19.2× → 18.6× → 18.6×**. The decomposition over the 4 weeks (F4Q forward P/E −0.5) = **price −0.4 + earnings −0.1**: across this *short* window the dip was **mostly the price pullback** (S&P 7,563.63 → 7,420.10, −1.9%), with a small extra tailwind from rising EPS (F4Q +0.5%). The CY2027 multiple's −0.6 split more evenly (price −0.4 / earnings −0.2) because **2027 EPS is being marked up ~3× faster than 2026** — CY2027 +$4.63 (+1.2%) vs CY2026 +$1.31 (+0.4%) over the three weeks. **Revision pace: steady, broad, no roll-over** — the out-year keeps getting upgraded each week.

**Longer-window context (Dec 5 2025 → Jun 18 2026) — the textbook "cheaper for the right reason."** Over ~6 months the S&P rose **+8.4%** (6,846 → 7,420.10) — yet the **2027 forward P/E *fell*** (19.5× → 18.6×). The decomposition:

- **2027 P/E Δ ≈ −0.9** = price **+1.6** (richer) **+ earnings −2.5** (cheaper). The multiple compressed **because the earnings effect outran the price effect** — the healthy kind of de-rating.
- **2026 P/E Δ ≈ −0.4** = price +1.9 + earnings −2.2 (same shape).

**Revision momentum: strongly UP and broad.** CY2026 EPS **+$31.5 (+10.2%)** and CY2027 EPS **+$47.5 (+13.5%)** since the Dec baseline; the dashboard's own growth track confirms the pace — CY2026 blended earnings growth marked from **+15.6% (1 Jan) → +19.0% (1 Apr) → +25.2% (today)** (Ex. 20), CY2027 roughly steady at ~+17% (Ex. 21). This is an **earnings-led** market, not multiple-expansion — and the upgrades are AI-mega-cap-heavy (Technology CY2026 growth +53.5%, the index's single biggest contributor). Momentum **accelerating**, not rolling over.

**Operating-vs-GAAP, quantified from primary:** LSEG's **trailing operating P/E is 25.8×** (Ex. 23) vs multpl's **trailing GAAP ~31.6×** — the ~6-turn gap is the operating-vs-as-reported difference, now sourced on both sides. The forward operating number (21.0×) is lower still on both the forward *and* operating axes; don't read it as "cheap" outright (multpl's GAAP mean is ~16×).

**Where the dials sit now:** **2026 21.8× · 2027 18.6× · forward/F4Q 21.0×** (LSEG close 7,420.10, 17-Jun). The live FRED close (7,365, 23-Jun) is a touch lower; with EPS unchanged since the dashboard, the multiples are ~flat — steady is a valid reading.

## What would be notable (watch-lines, not tripwires — no price levels)
- **Revision roll-over while price holds** — 2026/2027 EPS estimates revised *down* for 2+ consecutive readings while the index is flat/up → an early flag that the AI-concentrated earnings story is stalling. Cross-check [[AI-demand-durability]] (disconfirming signals) + [[what-could-go-wrong]] (Entry 1, hyperscaler-capex turn) + [[hyperscaler-capex]].
- **De-rating that flips to the *wrong* reason** — forward P/E falling driven by the **price** effect (price down) rather than the **earnings** effect → risk-off, not value creation. The decomposition is exactly what separates the two.
- **NTM forward P/E pushing toward the upper end of its recent range on price** (multiple expansion outrunning revisions) → the opposite risk: paying up ahead of earnings. Pair with the reverse-DCF "what's priced in" reference (`raw/research/2026-06-21_reverse-dcf-implementation-reference.md`).

*Tier note: LSEG/I-B-E-S consensus is a primary estimate feed (usable for the series); any strategist framing layered on top (e.g. the Fundstrat exhibit's "cheaper" narrative) is Tier 3 — cite, don't treat as fact. These are estimates: forward EPS starts optimistic and is often trimmed as the year nears, so weight the **direction of revisions** over the level.*

## Change log
- **2026-06-24 (4-week series + folder restructure):** Vic staged 4 weekly LSEG Scorecards (May 29 / Jun 5 / Jun 12 / Jun 18) under `raw/data/forward-earnings/LSEG_reports/` and the extracted series is now in `raw/data/forward-earnings/forward-earnings-raw-data.csv`. Added the three earlier weekly rows (05-29 / 06-05 / 06-12) → a proper 4-week series + the Dec anchor. 4-week read: EPS grinding up weekly (CY2027 ~3× faster than CY2026), price flat-to-down, forward P/E 21.6×→21.0× — over the short window the dip was mostly price, not earnings (the longer Dec→Jun move was earnings-led). No roll-over.
- **2026-06-24 (first primary run — LSEG dashboard staged):** Vic staged the LSEG S&P 500 Earnings Scorecard (TRPR_82201, 18-Jun) at `raw/data/forward-earnings/LSEG-2026-06-18.pdf`. Confirmed the CY EPS (2026 $340.82 / 2027 $399.25, Ex. 24) and **upgraded the row to primary**: LSEG close 7,420.10, F4Q/NTM EPS **$352.62**, **LSEG forward P/E 21.0× / trailing operating 25.8× (Ex. 23)**. **Corrected the placeholder NTM** ($368.83/20.0× blend → primary $352.62/21.0× F4Q) and pinned down the "21.0 vs 18.4" gap as a horizon choice (F4Q vs CY2027). Operating-vs-GAAP gap quantified (25.8× LSEG operating vs ~31.6× multpl GAAP). Revisions accelerating (CY2026 growth 15.6%→19.0%→25.2%).
- **2026-06-24 (created):** Standalone valuation-dial tracker (6th tracker), modeled on [[AI-credit-spread-watch]] + the `forward-pe-watch` skill / `scripts/forward_pe_watch.py` helper (FRED `SP500` auto-fetch + price-vs-earnings decomposition). Seeded with two LSEG I/B/E/S rows from the Fundstrat Exhibit 24 (2025-12-05 + 2026-06-18); launch decomposition shows the 2027 forward P/E compressing 19.5×→18.4× on rising earnings (price +1.48 / earnings −2.49), with 2026/2027 EPS revised up +10.2% / +13.5% — an earnings-led move. Dials at 2026 21.6× / 2027 18.4× / NTM 20.0×. Subsequent runs update this page's readings table + latest-read block only (not log.md).
