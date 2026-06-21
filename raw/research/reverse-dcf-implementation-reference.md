*Methodology / tooling reference — NOT a vault thesis anchor. Tier-3 discovery material. Assembled by the main agent from a `/deep-research` run whose Synthesize step was cut off by session limits: the workflow produced 20 adversarially-verified claims (vote tallies shown as `[✓ 3-0]` etc.) + 5 primary-source claims whose verification votes were interrupted (flagged `[primary, verification incomplete]`). Connective tissue, standard valuation conventions, ranges, and the worked pre-profit example are the main agent's synthesis from established practice (Damodaran / Rappaport-Mauboussin / Koller-McKinsey) — use for building a tool, confirm any single figure before relying on it.*

# Reverse DCF / Market-Implied Expectations — Implementation Reference

## 0. Mental model (the whole thing in a paragraph)

Reverse DCF **takes price as given and solves for the embedded expectation** instead of forecasting cash flows to derive a price. `[✓ 3-0; Expectations Investing]` There are two equivalent outputs the tool should produce: **(a) a market-implied growth rate** (Damodaran: solve a DCF algebraically for `g`), and **(b) a market-implied forecast / value-creation period** (Rappaport–Mauboussin "PIE": how many years of value-creating performance the price requires before the modeled value reaches the market price). The analytical payoff is the **gap** between that implied expectation and an independent, base-rate-anchored view — that gap is the buy/sell edge. `[✓ 3-0]`

---

## 1. THE CORE MECHANIC

### 1a. Closed-form implied perpetuity growth (mature names)
Single-stage Gordon model, price given, solve for `g`:

```
V = FCFF·(1+g) / (WACC − g)
⇒  g = (V·WACC − FCFF) / (V + FCFF)
```

**Worked (profitable name — Damodaran's Boeing):** V = $40,789M, FCFF = $1,176M, WACC = 9.17% → **implied g = 6.11%**. `[✓ 3-0; Damodaran fcff.pdf]`
*Limitation:* only valid for stable, mature firms. For growth names this overstates/understates — use the multi-stage solve.

### 1b. Two-stage / explicit-horizon solve (the "X% for Y years" output)
Model an explicit high-growth window of **N years** (FCF or the value-drivers grow), then a terminal value at a stable rate `g_T`. Set:

```
EV  =  Σ_{t=1..N} FCF_t/(1+WACC)^t   +   TV_N/(1+WACC)^N
```

Then solve **numerically** (bisection or Newton) for the unknown:
- **"market is pricing ~X% growth for Y years"** → fix N, solve for the growth rate `g`.
- **market-implied forecast period (Rappaport–Mauboussin)** → fix the value-driver assumptions, solve for **N** (the year the modeled value first reaches the market price). `[✓ 3-0]`

**Worked (the PIE duration form — Domino's Pizza, Sept 2020):** modeled value $285/share at end-2020 grows each year until it reaches the **$418 market price in 2027 → an 8-year market-implied forecast period.** `[✓ 3-0; expectationsinvesting.com]`

### 1c. The "$Z cumulative cash flow + $W terminal business" decomposition
Report the two PV pieces separately:

```
EV  =  PV(explicit-period FCFs)  [= $Z]   +   PV(terminal value)  [= $W]
```

This is the "price bakes in ≈$Z of near-term cash flow plus a terminal business worth $W" framing. `$W` is usually the majority of EV (see §4).

### 1d. The value-driver engine (so growth maps to cash, not hand-waved)
**Do not grow FCF directly — grow the drivers** (this is the McKinsey/PIE discipline and what you implement):

```
NOPAT            = pre-tax operating profit × (1 − cash tax rate)            [✓ 3-0]
Incremental inv. = ΔSales × (incremental WC rate + incremental fixed-cap rate)  [✓ 3-0]
FCF              = NOPAT − Incremental investment
```

Equivalent Damodaran identity (ties growth to reinvestment and returns — the backbone of a disciplined engine):

```
Expected growth  = Reinvestment Rate × ROIC
Reinvestment Rate = g / ROIC
FCFF             = EBIT(1−t) × (1 − g/ROIC)                                  [✓ 3-0]
```

**Implementation:** a driver model (revenue-growth path, operating-margin path, capital intensity, tax) emits per-year FCF; wrap it in a solver. The reinvestment identity is what stops a user from assuming high growth with zero reinvestment (an impossible free lunch).

---

## 2. DISCOUNT RATE

**The cardinal rule — match the rate to the cash-flow definition** (the #1 implementation bug):
- **FCFF → WACC** (firm/operating-asset value; then + cash − debt = equity). `[✓ 3-0]`
- **FCFE → cost of equity Kₑ** (equity value directly). `[✓ 3-0]`

```
WACC = (E/(D+E))·Kₑ  +  (D/(D+E))·K_d·(1−t)                                  [✓ 3-0]
Kₑ (CAPM) = R_f + β·ERP
```

**Worked (Boeing):** Kₑ = 5.00% + 1.01×5.5% = **10.58%**; WACC = 10.58%·(32,595/40,789) + 3.58%·(8,194/40,789) = **9.17%**. `[✓ 3-0]`

**Conventions & realistic ranges** *(standard practice — verify the live numbers):*
- **R_f** = current 10-yr Treasury (use the live yield, not a textbook constant).
- **ERP** ≈ 4.5–5.5% typical; Damodaran publishes a monthly *implied* ERP (often ~4.3–5.0%). Use one consistent source.
- **β**: regression beta or, better, **bottom-up** (unlever peer betas, relever at the firm's D/E) — more stable for single names.
- **WACC ranges:** large-cap mature ≈ **7–9%**; higher-beta / high-growth / more-levered ≈ **9–12%+**. Capital-light high-growth software often lands ~9–11% on a ~1.1–1.4 beta.
- **Disagreement:** *constant* WACC (majority, for simplicity) vs *fading* WACC (lower as a firm de-risks/de-levers — Koller/Damodaran allow it for firms whose risk profile clearly changes). Majority convention: hold WACC constant unless you have a specific reason.

---

## 3. CASH FLOW — FCFF vs FCFE, and the SBC / buyback traps

```
FCFF = EBIT(1−t) − Reinvestment            (Reinvestment = net capex + ΔNWC)
       → pre-debt; discount at WACC; firm value → +cash −debt → equity        [✓ 3-0]

FCFE = FCFF − after-tax interest − (debt principal repaid − new debt issued)
     = "cash flow after taxes, reinvestment AND debt payments"
       → discount at Kₑ; equity value directly                                [✓ 3-0]
```
FCFE and FCFF **share the same after-tax/after-reinvestment base**; FCFE just adds the debt-flow layer. `[✓ 3-0; Damodaran]`

### Stock-based compensation — the dominant tech-FCF error
**Do NOT add SBC back to reach free cash flow.** `[✓ 3-0; Damodaran]` SBC is a real, in-kind expense (paying people in equity instead of cash); adding it back implicitly assumes either employees work for nothing or that dilution is costless to per-share value. *"None of the numerous variants of adjusted EBITDA that add it back holds up to scrutiny."*

**Two internally-consistent treatments that give the same per-share value** — pick ONE: `[primary, verification incomplete — Morgan Stanley]`
1. **Expense method** — subtract SBC from FCF (treat as cash), hold share count fixed.
2. **Dilution method** — leave FCF unadjusted, but **grow projected share count** for ongoing issuance.

The error is **mixing them** (add SBC back to FCF *and* ignore dilution) → overstates value, the classic tech-bull mistake. **Majority convention:** treat SBC as a cash operating cost (expense method) — cleanest for a tool.

### Buybacks
Buybacks are a **use of FCFE** (a financing/return-of-capital decision), **not a source of cash** and **not a value driver**. Per-share value comes from the FCFE the business generates; buybacks only change the share count. **Common error:** adding a "buyback yield" on top of unadjusted FCF (double-counting). In a reverse DCF, model the cash generation; let share-count changes flow through the per-share bridge, not through FCF.

---

## 4. TERMINAL VALUE

### Method & the growth cap
- **Perpetuity-growth (Gordon)** vs **exit-multiple.** Damodaran calls perpetuity-growth the **"technically soundest"**; the multiple approach is easiest but **"makes the valuation a relative valuation"** (you've imported the market's multiple, defeating an intrinsic reverse-DCF). `[✓ 3-0]` **Majority convention for reverse DCF: perpetuity-growth.**

```
TV_N = FCF_{N+1} / (WACC − g_T)                                              [✓ 3-0]
```

- **Terminal-growth cap:** `g_T ≤` the nominal growth rate of the economy `≤` the **risk-free rate** (a clean practical ceiling: R_f ≈ expected inflation + real growth). `[✓ 3-0, confirmed twice]` Typical convention: **2–3%** (or ≈ R_f).

### The non-obvious truth: TV is about EXCESS RETURNS, not growth
```
TV_N = EBIT_{N+1}(1−t)·(1 − g_T/ROIC) / (WACC − g_T)                          [✓ 3-0]
```
Terminal value depends **far more on the assumed ROIC vs WACC spread than on `g_T`.** `[✓ 3-0]` **If ROIC = WACC in perpetuity, TV does not change with `g_T` at all** — growth creates zero value once excess returns fade. `[✓ 3-0]`
**Implementation guard:** don't let users dial up terminal `g` without a coherent terminal **ROIC**. The disciplined default is **ROIC → WACC convergence** (competition erodes excess returns), which makes terminal growth value-neutral and prevents the most common abuse.

### How much value sits in TV (and why it's fine)
- TV is **always a large share of total value** (commonly **60–80%+**), **rises with growth**, and **PV(TV) can exceed 100% of the current stock value.** `[✓ 3-0]` It is the **most assumption-sensitive input** — sensitize it explicitly.
- But a high TV% is **NOT a flaw of DCF:** the earnings base on which TV is computed is itself shaped by the high-growth assumptions, and most equity return *is* price appreciation. `[✓ 3-0]` (Don't let a tool reviewer "reject" a model just because TV is 75% of value.)

### Fade / CAP (Competitive Advantage Period / GAP)
The **CAP** (Mauboussin/McKinsey) — also "growth appreciation period" — is the window over which the firm earns **excess returns / above-stable growth** before fading to economic equilibrium (ROIC → WACC, g → GDP). The **market-implied forecast period** (Domino's 8 years, §1b) is essentially the **market-implied CAP**. **Implementation:** model an explicit window with margin/ROIC **fading** to a stable terminal state; solving for the CAP length is the Rappaport–Mauboussin "how long must they stay special?" question. *(The formal MICAP/MEROI machinery — Market-Expected Return on Investment, solving for the breakeven return that equates PV of capitalized NOPAT changes to PV of investments — is `[primary, verification incomplete — Morgan Stanley]`; useful but confirm before coding.)*

---

## 5. EDGE CASES & JUDGMENT

### 5a. Pre-profit / hyper-growth names (revenue × normalized margin)
You can't grow today's negative FCF. **Method (Damodaran "narrative→numbers"):** project **revenue × a normalized mature operating/FCF margin**, then back-solve. The reverse version: **solve for the revenue CAGR (or terminal revenue / market share) the price requires**, given assumed mature margin, capital intensity, and tax.

**Worked (illustrative pre-profit example — main agent's construction):**
> "NewCo" SaaS: EV = $20B, current revenue $1B, currently FCF-negative. Assume terminal FCF margin **25%**, WACC **11%**, terminal growth **3%**, 10-yr horizon. Terminal multiple = (1.03)/(0.11−0.03) = **12.875×**. Discount factor to yr-10 = 1.11¹⁰ ≈ 2.839. Ignoring interim cash for a first cut: PV(TV) = EV ⇒ TV = 20×2.839 = $56.8B ⇒ FCF₁₀ = 56.8/12.875 = $4.41B ⇒ **Revenue₁₀ = 4.41/0.25 = $17.65B** ⇒ required **revenue CAGR ≈ 33%/yr for a decade** (1 → 17.65). *(Interim cash-burn years would push the required terminal scale higher.)*
> **Base-rate check (§5c): a sustained ~33% 10-yr revenue CAGR sits in the top <1% of all firms historically — the price is pricing a far-outlier. That is the output that matters.**

### 5b. No-growth value vs growth premium (decompose the price)
```
No-growth (steady-state) value = current NOPAT / WACC      (capitalize current cash, zero growth)
Growth premium (PVGO)          = EV − steady-state value
```
Tells you what fraction of price is "the business as it is" vs "growth the market expects." *(Miller–Modigliani identity; MS worked case: value $2,230.8 = steady-state $1,428.6 + PVGO $802.2; Microsoft $248.7B = $61.0B steady-state + $187.7B PVGO — `[primary, verification incomplete]`.)*

### 5c. Base-rate plausibility (Mauboussin — the killer feature of the tool)
After solving for implied growth, **score it against historical base rates conditioned on the company's SIZE decile, not the full universe.** `[✓ 3-0]` Embed these tables:
- **Full universe** (top-1,000 global firms, 1950–2015, real): median 3-yr sales CAGR **5.4%** (mean 8.1%, SD 18.7%); 10-yr median **4.9%.** `[✓ 2-0]`
- **Sustained high growth is rare:** 15–20% CAGR achieved by **6.0%** of firms over 5 yr / **4.5%** over 10 yr; 20–25% → **3.1% / 2.0%**; **>45% over 10 yr → 0.3%.** `[✓ 3-0]`
- **Size conditioning is huge:** mega-cap (>$50B sales) 5-yr base rate for 15–20% is just **2.3%**, for 20–25% only **0.6%** `[✓ 2-1]`; the Tesla **$4.5–7B decile** had **ZERO** firms >45% over 10 yr, only **~0.2%** at 30–35%. `[✓ 3-0]`
- **Weight the median** (outside view) for horizons ≥3 yr — growth autocorrelation decays fast (year-to-year r = 0.30 → ~0.17–0.19 over 3–5 yr). `[✓ 3-0]` The **inside view alone is systematically too optimistic; blend, weighting the outside view more where luck dominates.** `[✓ 3-0]`

### 5d. Bull / base / bear scenarios
Vary the **2–3 highest-sensitivity drivers** — usually **revenue CAGR, terminal/mature margin, CAP length** (occasionally WACC). Keep TV disciplined (ROIC→WACC convergence) so scenarios don't diverge through the terminal back door. Report, per scenario: implied growth, the **$Z/$W split**, the **no-growth/PVGO split**, and the **base-rate percentile** of the implied growth.

### 5e. Where reverse DCF FAILS (flag these in the tool) *(standard cautions)*
- **Cyclicals** — current/normalized FCF is garbage at trough or peak; use **mid-cycle normalized** earnings/margins or the implied growth is meaningless.
- **Banks / financials / insurers** — FCFF is undefined (debt is raw material; "reinvestment ≠ capex + ΔNWC"). Use **FCFE / dividend-discount / excess-return (residual income)** models, **equity-only, discount at Kₑ.**
- **Holdcos / conglomerates** — consolidated FCF misleads; do **sum-of-the-parts**, reverse-DCF the operating subs separately, apply a holdco discount.
- **Negative/erratic reinvestment, big one-offs, distress** — normalize first or the solver returns nonsense.

---

## 6. Build spec (condensed)

- **Inputs:** market cap (→ EV via +debt −cash), revenue, EBIT/NOPAT, cash tax rate, current ROIC, net debt, cash, share count, SBC; WACC inputs (R_f, β, ERP, K_d, D/E).
- **Engine:** driver model (rev-growth path, margin path, capital intensity, tax) → per-year **FCFF** (+ optional FCFE) over N years + terminal.
- **Solver:** bisection/Newton on `EV = ΣPV(FCF) + PV(TV)` to back out **(i) g given N**, **(ii) N given g**, or **(iii) implied revenue CAGR** (pre-profit).
- **Discipline guards:** `g_T ≤ R_f`; **ROIC→WACC convergence** toggle; **SBC not added back**; **CF matched to rate**; surface **TV %**.
- **Outputs:** implied growth %, implied CAP/forecast-period (yrs), **$Z explicit vs $W terminal split**, **no-growth-value vs growth-premium split**, and the **size-conditioned base-rate percentile** of the implied growth.
- **Reference data to embed:** Mauboussin base-rate tables by size decile (the plausibility scorer).

---

## 7. The 5 points of genuine professional disagreement (with the majority convention)

| # | Disagreement | Majority / recommended convention |
|---|---|---|
| 1 | **SBC**: add-back (common in "adjusted" metrics) vs expense vs dilution | **Don't add back.** Expense it (cleanest for a tool) OR model dilution — never both/neither. `[✓ Damodaran]` |
| 2 | **Terminal value**: perpetuity-growth vs exit-multiple | **Perpetuity-growth** ("technically soundest"); exit-multiple smuggles in relative valuation. `[✓]` |
| 3 | **WACC**: constant vs fading over time | **Constant**, unless the firm's risk/leverage demonstrably changes. |
| 4 | **Terminal-growth cap**: R_f vs long-run GDP vs inflation-only | **≤ nominal GDP ≈ R_f** (commonly 2–3%). `[✓]` |
| 5 | **CAP length**: assume a fixed window (10–15 yr) vs solve for the market-implied period | **Solve for it** — the market-implied CAP/forecast period *is* the reverse-DCF insight (Mauboussin). `[✓]` |

---

## Sources (verified primary, from the research run)
- Rappaport & Mauboussin, *Expectations Investing* — expectationsinvesting.com (PIE method, Domino's 8-yr example, NOPAT/incremental-capital FCF). `primary`
- Damodaran — Stern: `fcff.pdf` (Boeing reverse-DCF 6.11%, FCFF/WACC/CAPM, reinvestment=g/ROIC), `valonlineslides/session9.pdf` + `growthandtermvalue.pdf` (terminal value, excess-return driver, growth cap, TV%), `aswathdamodaran.substack.com` (FCFF vs FCFE, SBC add-back error). `primary`
- Mauboussin, *The Base Rate Book* (2016) — sorfis.com PDF (size-conditioned sales-growth base rates, Tesla example, inside/outside view, correlation decay). `primary`
- Morgan Stanley Counterpoint Global — SBC dilution-vs-expense methods, MEROI, MM/PVGO decomposition. `primary` *(verification votes interrupted — confirm before coding)*
- Koller/McKinsey, *Valuation* — CAP/fade, key value-driver formula (referenced; corroborates the ROIC-spread terminal logic).

*Provenance recap: `[✓ x-y]` = adversarially verified (refute-votes for–against); `[primary, verification incomplete]` = from a primary source but the run's verification was cut off by a session limit; unflagged ranges/cautions/the pre-profit example = main-agent synthesis from standard practice. Confirm any single load-bearing figure at the cited source before it drives a real decision.*
