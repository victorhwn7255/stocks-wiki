---
type: valuation-check
ticker: META
run_date: 2026-07-10
market_cap_used: 1.71T
method: reverse-DCF (FCFF path) + Mauboussin base rates
depth: deep (3-agent, red-team)
tier: 3 (discovery-only — NOT canon)
---

# META — reverse-DCF / market-implied-expectations check ($1.71T)

**What this is.** A reverse DCF: it takes the **$1.71T market cap as given** (user-supplied, 2026-07-10) and solves for the free-cash-flow growth the market must be assuming, then scores how rare that growth is historically. It is **Tier-3 discovery material — not canon, not a fair value, not a buy/sell.** It says *what the market is betting on and how rare that is*, not whether the bet is right. Math from `scripts/reverse_dcf.py` (+ `base_rate_score.py`); every number traces to a run. Net debt −$22.43B (net **cash**), so enterprise value ≈ **$1.69T**.

**The one-sentence result.** There is **no honest point answer** — the read swings from "cheap" to "priced for perfection" across a defensible ~2× range for one unknowable input (normalized owner earnings), and the single judgment that decides it is **whether today's ~$135B AI-capex super-cycle is temporary growth investment that reverts toward maintenance (→ reasonable) or a permanent ~40–50%-of-revenue operating cost (→ expensive).** On *honest* inputs (stock comp expensed, a textbook ~9% discount rate) the center of gravity is **"aggressive — top-quartile-to-priced-for-perfection,"** not "cheap."

---

## ★ For the price to make sense, META must become ___

On the **honest central estimate** — normalized owner earnings of **~$55–60B** (free cash flow *after* expensing ~$22B/yr of stock-based comp), discounted at a defensible **~9%** — the $1.71T price requires META to:

1. **Turn free cash flow from *flat-and-collapsing* into *low-double-digit compounding* — ~10%/yr for a decade.** Reported free cash flow went *sideways* the last three years ($43B → $52B → $44B, 2023–25) and is guided toward **roughly zero in 2026** as capex nearly doubles. The price needs a **V-shaped inflection**, not a continuation. *A ~10% real-adjusted FCFF compounding for a >$50B-revenue company was managed by only ~17% of firms historically — top-quartile, and the bar rises fast from here.*

2. **See the AI-capex spike come back down — or pay off hard.** Today's ~$135B guide is **~60% of revenue**; Meta's pre-AI norm was **~24%**. The whole "reasonable" case rests on capex drifting back toward that old normal (so more of the cash it throws off is *free*). *If instead ~$135B is the new floor (AI-server depreciation is a permanent operating cost), normalized owner earnings sit near ~$45B and the required growth jumps to ~14% — a near-no-precedent (~1% of mega-caps) bar.*

3. **Stop the Reality Labs bleed.** The metaverse segment loses **~$19B/yr and the loss is *widening*** (FY24 $17.7B → FY25 $19.2B). That is a ~$16B-after-tax hole in cash flow every year; capping or spinning it out is the **single cleanest lever** back toward "reasonable" — but management is *doubling down*, not retreating.

4. **Earn its cost of capital on the build while margins face a depreciation wave.** As $125B+/yr of capex depreciates (servers ~5–6 yr) plus the memory-price cost-push Zuckerberg flagged, operating margins face downward pressure — so free cash flow likely grows *slower* than revenue, making the true bar *harder* than the headline number.

**↳ The lever the answer hinges on most: the normalized-owner-earnings judgment (the capex value-vs-burn call).** It alone swings the implied growth from ~2% ("common") to ~15% ("extreme outlier"). The discount rate is the second-order lever (±1pt of WACC ≈ ±2.3pt of implied growth). **This is a conditional read, not a fact.**

---

## The two headlines (anchored on the honest central estimate; range shown)

- **"The market is pricing in ~10%/yr FCFF growth for 10 years"** — off ~$55–60B of normalized owner earnings at a ~9% discount rate (then 3% forever). *Range across the defensible fork:* **~2%/yr (bull corner) to ~14%/yr (bear corner)** — see the ladder below.
- **"Of the ~$1.69T enterprise value, ≈$0.60T is explicit 10-year cash flow + ≈$1.08T is a terminal business (~64% of the value sits in the terminal)."** The value is overwhelmingly a bet on the *far* future — which is exactly what you'd expect when *near-term* free cash flow is guided toward zero.

---

## Price decomposition (honest central estimate, $57B @ 9.0%)

- **No-growth ("assets in place") value ≈ $0.63T** — what the current owner-earnings stream is worth with zero growth.
- **Growth premium (PVGO) ≈ $1.05T — 62% of enterprise value.** Nearly two-thirds of the price is paying for growth that hasn't happened yet.
- **The vivid anchor:** the market pays ~$1.69T EV while **FY2026 free cash flow is guided toward ~$0** (capex ~$135B ≈ operating cash flow). So on a *forward* basis ~100% of the price is future-normalization-plus-growth — the reverse DCF literally **blocks** on the forward number (free cash flow ≤ 0), which is itself the finding.

---

## Plausibility — the killer line

**On honest inputs (stock comp expensed as the real ~$22B/yr dilution it is, and a CAPM-consistent ~9–9.5% discount rate), the $1.71T price implies ~10–13% FCFF growth every year for a decade off a $200B revenue base. Historically only ~2–17% of >$50B-revenue companies compounded real cash flow that fast, and ~0% did so above ~15% real. The comfortable "above-median, ordinary" read exists *only* at the optimistic corner — full capex reversion to maintenance **and** a sub-CAPM 8.5% discount rate. It does not survive textbook inputs.**

Supporting facts: reported free cash flow has gone sideways ($43B→$52B→$44B) and is guided to ~$0 in 2026; on a stock-comp-expensed basis Meta's free cash flow *peaked* at ~$35B (2024) and is ~$23B trailing — so even the ~$50–57B "normalized" base is already *above anything Meta has produced net of stock comp*. **Base-rate caveat (cuts against Meta):** the score maps *FCFF*-growth onto *sales*-growth history — valid only at stable margins; the coming D&A wave + memory cost-push likely compress margins, so the true bar is *harder* than the raw percentile. (Counter-caveat, honestly: base rates are an outside view, not destiny — dominant high-margin platforms do occasionally fill the tail; they just rarely do.)

*Scorer note (don't over-read the exact percentile):* the base-rate verdict jumps sharply at the 10%-real boundary (the published mega-cap anchor covers 5–10%; above it the score falls to a thin modeled tail). Read the *bands* — "aggressive → outlier" — not the decimal.

---

## Bull / base / bear (every row a `reverse_dcf.py` run; g_T = 3%, EV target $1.69T)

| Scenario | Normalized FCFF | The capex/RL premise | WACC | Horizon | Implied FCFF growth | Real | Base-rate verdict |
|---|---|---|---|---|---|---|---|
| **Bull** (steelman) | **$89B** (FoA-only NOPAT) | RL exited **and** capex fully reverts to maintenance (≈ D&A) | 8.0% | 15y | **2.2%/yr** | ~0% | **base-rate plausible (common / cheap)** |
| Optimistic | $70B | capex fully reverts; RL stays | 8.5% | 10y | 6.2%/yr | 4% | above median, still ordinary |
| **★ Honest central** | **$55–60B** | capex partly reverts (~25% of rev, still > D&A); SBC expensed | 9.0% | 10y | **~10%/yr** | ~8% | **aggressive (top quartile)** |
| Honest base (Agent 2) | $50B | ~25%-of-rev capex; full-CAPM rate | 9.5% | 10y | 13.0%/yr | 11% | priced for perfection (~top 2%) |
| **Bear** (steelman) | **$45.6B** (TTM actual) | AI capex is a **permanent** step-up; trailing IS normal | 9.5% | 10y | **14.3%/yr** | 12% | **extreme outlier (~top 1%)** |
| *Memo: hard bear* | ≈$0 (FY2026 guide) | forward reality | 9.0% | 10y | *engine blocks (FCFF≤0)* | — | *~100% of EV is PVGO* |

**Red-team verdict (deep pass — does the central read survive the strongest fair attack?).** **No — not as a point; only as a midpoint.** Both *individually defensible* extremes flip it: the bull corner ($89B FoA-only NOPAT + RL exit + 8% WACC + 15y CAP) makes META look **cheap (~2%, common)**; the bear corner ($45.6B trailing-actual + textbook 9.5–10% WACC) makes it **priced-for-perfection-to-outlier (~14–15%)**. The normalized-FCFF axis *alone* spans **$45.6B → $89B** — a ~2× range that straddles *every* base-rate boundary. So the honest deliverable is **the range, conditional on the capex call**, and "~10%/aggressive" is the *midpoint of the fork, not a robust standalone answer.* The one place the red-team could not rescue the price: on a *stock-comp-expensed* base META has never produced more than ~$35B of free cash flow, so the ~$70–89B bases require *believing in the normalization*, not observing it.

---

## Assumptions + verification (the outputs are conditional on this input set)

**Verified against the primary filings (10-K FY2025 + 10-Q Q1 2026):**
- **Net debt −$22.43B (net cash):** cash $23.43B + marketable securities $57.75B = $81.18B, minus long-term debt $58.75B. (Memo: excludes ~$103.8B leases-not-yet-commenced + ~$131B purchase commitments — correctly kept out of the net-debt bridge since they flow through future reinvestment the DCF already discounts; but they mean the AI capex is *contractually committed*, i.e. sticky and hard to cut — which supports the *permanent-step-up* bear, not a "net-cash cushion" comfort.)
- **Revenue $200.97B** (FY2025; the base-rate size bucket = ">$50B mega").
- **EBIT $83.28B (41% margin); reported net income $60.46B is tax-*depressed*** by a one-time OBBB deferred-tax valuation-allowance charge (30% effective vs ~13% clean rate; the 10-K states it explicitly) → **normalized net income ~$74.8B**, which matches the Q1-normalized run-rate ($18.7B × 4). *Reported net income is NOT a clean owner-earnings anchor here.*
- **Reality Labs operating loss ~$19B/yr and widening** (kept inside the base; FoA-only would be ~$89B NOPAT — the bull lever).
- **TTM:** operating cash flow $124.0B; capex incl. finance leases $78.36B; D&A ~$20.7B; **stock-based comp ~$22.3B**; reported (SBC-added-back) free cash flow $45.6B.
- **FY2026 capex guide $125–145B (~$135B mid, ~+87% YoY)** → forward free cash flow ≈ 0-to-negative.

**What Agent 2 corrected in Agent 1's first pass (both push the same way — the price is *more* demanding than the first cut said):**
1. **Stock comp must be expensed, not added back.** Agent 1's $70B base leaned partly on an "operating-cash-flow minus capex" route, but operating cash flow *adds SBC back* (it's non-cash), leaving ~$22B of real dilution un-expensed — the exact error the methodology reference forbids. The clean, SBC-expensed normalized figure at ~25%-of-revenue capex is **~$45–52B**, ~$20B below Agent 1's $70B. (The normalized-*net-income* leg to $74.8B *does* expense SBC — but that leg is only a valid FCFF proxy if capex reverts all the way to *maintenance* ≈ D&A, i.e. the most optimistic capex assumption. The two legs agreed near $72B by coincidence, giving false robustness.)
2. **8.5% WACC is below the honest floor.** Bottom-up CAPM (Rf 4.5% + β~1.25 × ERP ~4.75% ≈ 10.4% cost of equity; ~97% equity-financed) supports **~9.5–10%**. The central case uses ~9%; the "ordinary" read requires the generous 8.5%.

**Weak-fit / honest flags.** (a) **Capex-trough distortion is the whole story** — reported and forward free cash flow are unusable, so a *normalization judgment* is unavoidable and it is where all the subjectivity lives (this is the intended use of the "at a cyclical/capex trough, normalize" discipline, but it means the answer is a range). (b) The **base-rate proxy** (FCFF-growth vs sales-growth history) loosens if margins compress under the depreciation wave — biasing the true bar *harder*. (c) Terminal value is 60–72% of EV across the ladder — assumption-heavy by construction; the sensitivity table flexes WACC ±1pt and terminal-g ±1pt.

---

## Sources

- **Vault canon:** `wiki/companies/META.md` (human-verified Financial snapshot; last_updated 2026-06-02, S117 first-canonical).
- **Primary filings:** `raw/filings/META/META-10K-2025-12-31.htm` (FY2025) + `META-10Q-2026-03-31.htm` (Q1 2026) — income statement, cash-flow statement, balance sheet, OBBB tax note.
- **Method:** `scripts/reverse_dcf.py` + `scripts/base_rate_score.py`; conventions from `raw/research/reverse-dcf-implementation-reference.md`, `reverse-dcf-research.md`, `mauboussin-base-rate-tables.md`.
- **Market cap:** user-supplied ($1.71T, 2026-07-10) — reverse DCF needs a live price, which is not auto-fetched.

*Discovery-only. This note computes what the market is *implying* and how rare that is — never a fair value, price target, or buy/sell. Nothing here reaches a canon page.*
