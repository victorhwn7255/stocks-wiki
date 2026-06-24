# CRDO — valuation-check (reverse DCF / market-implied expectations)

- **Run date:** 2026-06-24
- **Ticker:** CRDO (Credo Technology Group Holding; Nasdaq)
- **Market cap used:** **$50.7B** (user-provided live figure) · net cash $1.4B, no debt → EV ≈ **$49.3B**
- **Mode:** `deep` (3-agent run: extract+compute → adversarial verify → red-team)

> **What this is (the boundary).** This is a **reverse DCF**: it takes the market cap as *given* and solves for **what the market must believe** to justify it — implied growth, the explicit-vs-terminal cash-flow split, and how rare that bet is against history. It is **Tier-3 discovery material** (`/valuation-check`), not vault canon: nothing here is written to any `wiki/` page, and it is **not a fair-value estimate, a price target, or a buy/sell call.** It says what the price is *betting on* and how unusual that bet is — not whether to own it. CRDO is in the holder's portfolio; the discipline here stays describe-don't-recommend. All numbers trace to `scripts/reverse_dcf.py` runs; the agents picked the inputs, the script did the arithmetic.

---

## ★ For the price to make sense, CRDO must become ___

At $50.7B, **all of the following must hold together** — each demanding on its own; jointly near-unprecedented:

1. **Compound free cash flow ~34–35%/yr for a full decade** (defended base case; the trailing-base read is ~40%/yr). No semiconductor company at CRDO's ~$1.3B revenue size has sustained ~32% *real* growth for 10 years — the historical base rate is **≈0% of firms ever**. This is Tesla-from-$6B / Oracle-Cloud / OpenAI company.
2. **Land a brand-new ~$600M optical ramp cleanly and on schedule.** The FY2027 >80% guide already *leans on* optical (three legs each >$100M — discrete DSPs / SiPho PICs / ZeroFlap — plus DustPhotonics → CPO/NPO in FY2028). This is a **single-vector dependency the company has not yet proven at scale** — the growth case is a bet on a ramp, not an extrapolation of a track record.
3. **HOLD peak margins, not reach them.** Non-GAAP net margin is already ~50% and non-GAAP GM ~68% — there is no margin-expansion tailwind left to harvest. The model needs CRDO to *defend* fortress margins for a decade while scaling ~10×, on a single-foundry (TSMC) cost base it does not control.
4. **Broaden the customer base without the whales leaving.** Customer A is **49%** and Customer B **32%** of FY2026 revenue (top-10 ≈ 90%; Customer A is 53% of receivables). A decade of growth requires winning many new ≥10% customers *while* retaining the two that are ~80% of the book.
5. **Survive Pillar Two.** ~92% of pretax income is offshore at a 0% Cayman rate today, but CRDO's own 10-K flags a **15% OECD global-minimum-tax exposure from FY2028**. The cash-flow base the bulls quote is partly a tax artifact scheduled to erode (~$68–97M/yr vs GAAP NI at a 15–21% rate).
6. **Justify a price that is ~76% terminal value / ~95% growth premium.** Only ~$2.2–3.4B of the $49.3B EV is "assets in place" (no-growth value); the other **93–95% is PVGO** — a bet almost entirely on cash flows that do not yet exist.

**The answer hinges most on WACC** (±1pt moves implied growth ~2.7pt) and the **FCFF base / competitive-advantage period**. Terminal growth is capped (g ≤ R_f) and is *not* a back door. This is a **conditional read, not a fact** — change the inputs and the number moves (see scenarios).

---

## The two headlines

- **"The market is pricing in ~34–41% FCFF growth per year for 10 years"** — ~40.6%/yr on the trailing FCFF base ($224M), ~34.5%/yr on the defended steady-state base ($340M), then ~3% forever. (At a generous 15-year horizon, ~24–29%/yr.)
- **"Of $49.3B enterprise value, ≈$11B is explicit 10-year cash flow + ≈$38B is a terminal business"** — **~76–78% of the value sits in the terminal**, the most assumption-sensitive piece.

## Price decomposition

- **No-growth value (assets in place):** ~$2.24B (trailing base) to ~$3.4B (defended base) — i.e. the current cash-flow stream, frozen, is worth ~5–7% of the price.
- **Growth premium (PVGO):** ~$47B = **~93–95% of EV.** Across every scenario (including the bull cases), PVGO stays 81–95% of EV. CRDO at this price is, mathematically, almost entirely a growth bet.

## Plausibility (the base-rate read)

- Implied ~38% *real* FCFF growth for a $1.25–2B-revenue company → achieved by **≈0.0% of firms in the historical base-rate tables** (Mauboussin/Credit Suisse persistence data). Reference tail comparables: Tesla (~50%/10y), OpenAI (~108%/5y), Oracle Cloud (~75%). Median for the size bucket is ~5.6% real.
- **Killer line:** *Priced for perfection with no historical precedent* — the price requires ~34%/yr free-cash-flow growth for a decade, an outcome ≈0% of companies its size have ever delivered, all riding on an unproven ~$600M optical ramp, two customers that are ~80% of revenue, a single TSMC foundry, and a 0% tax shield the company says expires in FY2028.

**Sensitivity — implied FCFF growth (defended-base region), WACC × terminal g:**

| WACC ＼ g_T | 2% | 3% | 4% |
|---|---|---|---|
| 9% | 37.5% | 38.4% | 39.4% |
| 10% | 38.7% | 40.6% | 42.2% |
| 11% | 41.7% | 43.2% | 44.9% |

*(grid shown for the trailing $224M base; raising the base to the defended $340M shifts the whole grid down ~6pt.)*

---

## Bull / Base / Bear

| Scenario | FCFF base | WACC | Horizon | Implied growth | Terminal % EV | Base-rate verdict |
|---|---|---|---|---|---|---|
| **Bear** (priced-for-perfection most exposed) | $200M | 11% | 10y | **~45%/yr** | 76% | ≈0% — no precedent |
| **Base** (defended steady-state) | $340M | 10% | 10y | **~34.5%/yr** | 76% | ≈0% — no precedent |
| **Bull** (most generous defensible, *trailing* base) | $343M | 9.5% | 15y | **~23.7%/yr** | 68% | ≈0.5% — extreme outlier |

### Red-team (`deep`) — the verdict HOLDS

The strongest *fair* attack is to set the price against **forward** cash flow (the >80% growth is company guidance), not trailing. Two independent builds put a defensible **FY2027E SBC-expensed, Pillar-Two-taxed FCFF at ~$650M (central) to ~$800M (bull-max)**.

| Red-team run | Fwd FCFF base | WACC | Horizon | Implied growth | Base-rate verdict |
|---|---|---|---|---|---|
| Forward base, 10y | $650M | 9.5% | 10y | ~24.0% | ≈0.1% — no precedent |
| Forward base, low WACC | $650M | 9.0% | 10y | ~22.6% | ≈0.2% — no precedent |
| High fwd base, 12y | $650M | 9.0% | 12y | ~19.7% | ≈0.9% — extreme outlier |
| **Stacked steelman** | **$800M** | **8.5%** | **15y** | **~13.4%** | **≈12.5% — aggressive, ~top quartile** |
| FY2028E base (double-double-count) | $1,200M | 8.5% | 15y | ~10.3% | ≈24.7% — ordinary |

**Verdict: "priced for perfection / no precedent" SURVIVES.** Even crediting the full guided +80% year into the base ($650M) at a 10-year horizon, the market still needs **~23–24%/yr FCFF growth** — a ≈0.1–0.2% base-rate event. The implied growth only exits the no-precedent tail into "aggressive but achievable" (~13.4%, ~top quartile) when **all four** most-generous levers are stacked at once: the $800M forward base (which already credits a +190% FCFF year), an 8.5% WACC, a 15-year moat, *and* 3.5% terminal growth. Drop any one — WACC back to 9%, or a 12-year CAP — and it snaps back to priced-for-perfection. It only flips to "ordinary" by using an FY2028E base that double-counts *two* hyper-growth years, which is no longer an honest frame for what the market must assume *from here*.

**The one number a fair bull would cite:** with a defensible ~$800M FY2027E forward FCFF, a 15-year moat, and an 8.5% WACC, the price implies **~13.4% FCFF growth for 15 years** — genuinely achievable. That is the real bull case; it requires believing the optical pivot delivers, the moat lasts 15 years, *and* you grant CRDO its blow-out guided year for free.

---

## Assumptions + Agent-2 verification (outputs are conditional on these)

**Verified exactly against the FY2026 10-K (year ended May 2, 2026):** OCF $464.292M · capex $57.296M · **SBC $182.638M** (expensed, never added back) · ΔNWC cash drag −$242.3M (inventory $90.0M→$250.8M, AR $162.1M→$233.4M) · net cash $1.44B, zero debt · Customer A 49% / B 32% of revenue (top-10 ≈90%) · "exclusively used TSMC" for wafers (single-foundry, verbatim).

**What Agent 2 corrected (the load-bearing judgment):**
- **FCFF base.** Agent 1's primary trailing base was $224M (OCF−capex−SBC), but that figure embeds two large offsetting distortions — an abnormal −$242M hyper-growth working-capital build (too harsh) and a ~0.66% cash tax rate (too generous). Agent 2's **defended steady-state base ≈ $340M** = GAAP EBIT $445M × (1 − 15% Pillar-Two) + D&A $35M − capex $57M − modest normalized NWC. Two independent routes (Agent 1's 18%/zero-NWC and Agent 2's 15%/small-NWC) converge on ~$340–343M — that convergence is the confidence signal. The **$224M trailing base is retained as the bear anchor**, $340M as the base case.
- **Tax.** GAAP NI ($472.3M) was **not** flattered by a one-time deferred-tax release (the valuation-allowance line was a +$93.4M *expense*, not a release). The ~0.66% effective rate is structural (92% of pretax income offshore at the Cayman 0% rate). But CRDO's 10-K itself flags a **15% Pillar-Two rate from FY2028**, so a ~15% forward normalized rate is the honest base — the near-zero cash tax does not survive a 10-year DCF.

**Input set (base case):** path `fcff`; market_cap $50.7B; net_debt −$1.4B; FCFF $340M (defended; $224M trailing bear anchor); revenue $1.3351B (base-rate size bucket); WACC 10.0% (Damodaran semi band, high beta >1.5, net cash; sensitivity flexes 9–11%); terminal g 3.0% (≤ R_f 4.5%); horizon 10y (12–15y as CAP-sensitivity).

**Weak-fit caveat (honest about the tool).** Reverse DCF is **borderline-fit** for CRDO as a *precise* read — the base FCFF is one fiscal year old in a name that grew +206% and guides FY2027 >80%, and PVGO is 95% of EV. The point *estimate* is fragile; the *conclusion* is robust — every cut (trailing base, defended base, forward base, every WACC/horizon) puts the implied growth in the same near-zero-precedent tail until you maximally stack the steelman. Use this as a plausibility stress-test of "how heroic is the story," not as a fair-value anchor. A revenue-path cross-check (revenue × 40–50% mature operating margin) agrees independently: the price needs a ~28–31% revenue CAGR for a decade.

## Sources

- Canon: `wiki/companies/CRDO.md` (Financial snapshot, refreshed S171 — FY2026 10-K + Q4/FY2026 call).
- Primary: CRDO FY2026 10-K (fiscal year ended May 2, 2026; filed 2026-06-15) — Consolidated Statements of Cash Flows + Operations, Note 13 (income taxes), customer-concentration + foundry disclosures. CRDO Q4/FY2026 earnings call (June 1, 2026) — FY2027 guidance, optical-ramp framing.
- Engine: `scripts/reverse_dcf.py` + `scripts/base_rate_score.py` (Damodaran / Rappaport-Mauboussin / Koller-McKinsey methodology per `raw/research/reverse-dcf-*.md` + `raw/research/mauboussin-base-rate-tables.md`).
