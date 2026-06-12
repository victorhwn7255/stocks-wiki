---
type: company
tickers: [CRWV]
layer: outside
photonics_tier: outside
memory_tier: outside
energy_power_tier: outside
equipment_tier: outside
materials_tier: outside
last_updated: 2026-06-03
---

# CRWV — CoreWeave, Inc.

## Thesis role

CoreWeave is the vault's **6th and final hyperscaler PAYER/SPENDER page** and the **first rent-side one** (program scope complete: [[MSFT]] + [[GOOGL]] + [[AMZN]] + [[META]] + [[ORCL]] + CRWV). It is a **"neocloud"** — a GPU-specialized cloud that buys NVIDIA accelerators (mostly with debt), houses them in data centers, and rents AI compute to others on multi-year contracts. Unlike the five hyperscalers, it is *not* a demand source funding its own AI ambitions from a diversified cash-generating business; it is a **capacity provider** sitting between NVIDIA (its supplier) and a small set of large customers, capturing no supply-side chokepoint rent.

**Honest-verdict framing (Section 2.1).** CoreWeave holds **no chokepoint** — it is a structural price-taker, squeezed between merchant-GPU pricing it does not control and customer concentration it cannot easily diversify. Its vault inclusion is **not** for thesis centrality. It is here for two specific reasons: (1) it **completes the rent-side** of the payer picture (the [[hyperscaler-capex]] build-vs-rent dynamic now has a primary-sourced rent-side example), and (2) it is the cohort's **fragility / early-warning vantage — "the canary."** It spends like a hyperscaler (FY2026 capex guided $31-35B) but is funded like a startup (debt, customer concentration, net losses), so it is the layer of the AI-capex chain that would **break first** if demand ever softened — quarters before a cash-funded hyperscaler would feel anything. That early-warning function, not any structural moat, is its thesis relevance.

**Placement.** `layer: outside` + `outside` on all five per-domain tiers — a CAPEX deployer / capacity provider that captures no supply-side value-capture position, per the demand-side hyperscaler precedent. **NOT on the [[software-AI-moat-durability]] scorecard.** **Section 2.11 N/A** — CoreWeave is a calendar-year (December 31) filer; Q1 2026 = calendar Q1 2026. A former crypto-miner (those offerings discontinued) that IPO'd in March 2025; this 10-K is an early annual report, with "limited operating history" of selling AI cloud services flagged in its own risk factors.

## Financial snapshot

Two periods kept separate per Section 4.1 (no blending). The shape to read: **revenue is growing explosively, but the company runs a net loss — and the loss is driven below the operating line by interest on its debt**, not by the operations themselves.

**FY2025 (10-K; year ended December 31 2025; vs FY2024):**

| Metric | FY2025 | FY2024 | YoY |
|---|---|---|---|
| Revenue | $5,131M | $1,915M | **+168%** |
| Operating income (loss) | $(46)M | $324M | swung negative |
| Interest expense, net | $(1,229)M | $(361)M | +240% |
| Net loss | $(1,167)M | $(863)M | wider |
| Capex (cash purchases of P&E + capitalized software) | $10,309M | $8,702M | +18% |
| Total debt (principal) | $21,615M | $8,033M | **+169%** |

*Microsoft was ~67% of FY2025 revenue (10-K-named); no other single customer was >10%; committed contracts were >98% of revenue. Contracted power ~3.1 GW at year-end (850 MW active). Depreciation rose ~$2.0B (+205%) as deployed GPUs began depreciating.*

**Q1 2026 (10-Q; quarter ended March 31 2026; call May 7 2026; vs Q1 2025):**

| Metric | Q1 2026 | Q1 2025 | YoY |
|---|---|---|---|
| Revenue | $2,078M | $982M | **+112%** (+32% sequential) |
| Operating loss | $(144)M | $(27)M | wider |
| Interest expense, net | $(536)M | $(264)M | +103% |
| Net loss | $(740)M | $(315)M | wider |
| Total debt (principal) | $25,149M | — | (vs $21,615M at Dec-31-2025) |
| Revenue backlog | **$99.4B** | — | +~50% QoQ |

Management reports an *adjusted* (non-GAAP) net loss of $(589)M for Q1 2026; the GAAP net loss is $(740)M. The gap between the operating loss ($(144)M) and the net loss ($(740)M) is almost entirely **interest expense** ($(536)M) — the cost of the debt funding the buildout.

## CAPEX & the capex-vs-revenue gap

The section this ingest exists to source (cross-ref [[hyperscaler-capex]] + [[AI-demand-durability]]) — and CoreWeave's capex profile is the most extreme in the program.

- **Current spend.** FY2025 capex **$10.3B** (cash purchases of P&E + capitalized software); **Q1 2026 capex $6.8B** (management figure; $7.7B on the cash-flow line including capitalized software), described as "on schedule."
- **Projected spend.** **Q2 2026 guided to $7-9B**; **full-year 2026 guided to $31-35B** — the low end raised, with management attributing the increase to "increases in **component pricing**" (the same memory/GPU cost-push the hyperscalers cited; cross-ref [[HBM-oligopoly]]).
- **The gap (the canary math).** FY2026 capex of **$31-35B sits against FY2026 revenue guidance of just $12-13B** — capex is roughly **2.6-2.9× revenue**, the most extreme capex-to-revenue ratio of any payer in the cohort. CFO Nitin Agrawal stated it directly: **"CapEx shows up before revenue and cash flow"** — the spending precedes the income it is meant to generate, in the purest form of the capex-ahead-of-revenue timing risk the whole tracker flags.
- **The justification.** Management points to the **$99.4B contracted revenue backlog** (+~50% in one quarter) as forward visibility — "clear visibility into 2026 and beyond" — and notes that capex flows into *construction in progress* (infrastructure not yet in service and not yet depreciated) until the capacity comes online against that contracted demand. The bet: the signed backlog converts to revenue fast enough to service the debt the capex is built on.

## Financing & debt fragility (the canary)

The distinguishing feature versus the five hyperscalers: CoreWeave funds its build with **debt, not operating cash flow**. CRWV is Structure #4 (GPU-collateralized debt) in the cross-vault credit-risk map at [[AI-buildout-who-holds-the-risk]] — including the March 2026 $8.5B non-recourse SPV facility rated A3 (the first investment-grade GPU-backed financing; the rating rides one customer contract plus GPU residual value, not CoreWeave's corporate credit).

- **Total debt principal $25.1B** (Q1 2026), up from $21.6B (Dec-31-2025) and $8.0B (Dec-31-2024) — including a $2.0B 2030 Senior Notes issuance (May 2025) and a $1.75B 2031 Senior Notes issuance (July 2025), plus GPU-backed facilities. FY2025 **interest expense was $1.23B** and rising — the single biggest driver of the net loss.
- **The reflexive financing — NVIDIA invested $2.0B in CoreWeave's Class A common stock in January 2026** (at $87.20/share; 10-K Subsequent Events) — primary confirmation, from CoreWeave's own filing, of the "supplier funding its customer" circularity the tracker flags (see [[nvidia-supply-chain-commitments]]).
- **Tier-3 context** (`ai-capex-map-2025-2027.md`, attributed): a debt-to-equity load around ~4.5×, 2031 bonds yielding ~11.5% (junk-level — the market pricing real credit risk), and >$20B of capital raised in 2026 alone. These are Tier-3 figures, not primary disclosures; the vault's primary debt figures above stand where they differ from the report.
- **Why it is the canary.** A cash-funded hyperscaler can absorb a demand air-pocket; CoreWeave — spending ~3× revenue, carrying $25B of rising-cost debt, and leaning on one customer for most of its income — cannot. A demand wobble would show up here first, in a refinancing or a covenant, well before it dented a Microsoft or an Amazon.

## Customer concentration

- **Microsoft was ~67% of FY2025 revenue** (named explicitly in the 10-K); **no other customer exceeded 10%.** The prior-year comparatives were similarly concentrated (top two customers ~77% in FY2024; top three ~73% in FY2023). **Committed contracts were >98% of revenue** — nearly all income is the backlog converting.
- **Diversification underway but early.** CoreWeave signed a master services agreement with **OpenAI** in May 2025, and names **Meta** as another significant customer — but FY2025 revenue was still overwhelmingly Microsoft.
- **Tier-1/Tier-2 disclosure gap (Section 3.4).** Microsoft's ~67% concentration is disclosed plainly in the 10-K (Tier 1), but **Microsoft is named zero times on the Q1 2026 earnings call** (Tier 2) — a customer-concentration framing gap: the single most important risk to the business is documented where required but not volunteered on the call.
- **Competitors are also customers.** CoreWeave lists Amazon (AWS), Google (Google Cloud), Microsoft (Azure), and Oracle as competitors — several of which are also its customers. Microsoft is simultaneously its largest customer and, via Azure, a direct competitor.

## Business model & capacity

CoreWeave's model is simple and capital-intensive: **buy NVIDIA GPUs → install them in data centers with power and cooling → rent the compute on multi-year contracts.** It is a specialist ("neocloud") — narrow where AWS/Azure/Google Cloud are broad — competing on speed of deployment of NVIDIA's newest accelerators and AI-optimized infrastructure, which is why even Microsoft (which builds its own capacity) rents from it. As of Dec 31 2025 it had ~**3.1 GW of contracted power** (850 MW active) to deploy over future periods, and NVIDIA has committed CoreWeave to building large-scale AI capacity over the coming years (alongside the $2B equity investment). It maintains direct relationships with semiconductor manufacturers and OEMs to secure supply.

## Open questions

1. **Backlog-vs-debt race.** Does the $99.4B contracted backlog convert to revenue and cash flow fast enough to service $25B+ of rising-cost debt before maturities come due?
2. **Microsoft-concentration durability.** Does the OpenAI/Meta diversification meaningfully reduce the ~67% Microsoft dependence, or does concentration persist?
3. **Path to free cash flow.** With capex ~3× revenue and "capex shows up first," when (if) does CoreWeave turn FCF-positive, and what does the interest burden look like by then?
4. **Refinancing risk.** At ~11.5% bond yields (Tier-3), how exposed is CoreWeave to a tightening in private credit / capital markets — the disconfirming-signal the tracker watches?
5. **Component-pricing pass-through.** Does memory/GPU cost inflation keep lifting capex, and how much of it passes through to customers vs compresses CoreWeave's margins?

## Source audit notes

Per-source entries, ordered by recency + tier.

- **CRWV Q1 2026 earnings call (Tier 2; May 7, 2026; quarter ended Mar 31, 2026).** Source of the capex guidance (Q2 $7-9B; FY2026 $31-35B, component-pricing-driven) and the **"CapEx shows up before revenue and cash flow"** framing (Agrawal). Management discloses an *adjusted* net loss ($(589)M) more prominently than the GAAP figure ($(740)M). **Microsoft named zero times** despite being ~67% of revenue (the Tier-1/Tier-2 gap, above). CEO Intrator + CFO Agrawal answered an analyst's after-hours-stock / component-pricing question directly and in detail (purchase-orders-in-hand pricing; "good at supply chain") — **not** defensive or dismissive; **CEO-combativeness count UNCHANGED**.
- **CRWV Q1 2026 10-Q (Tier 1; quarter ended Mar 31, 2026).** Source of the verified Q1 financials, the $25.1B total debt, and the $99.4B backlog. Operating loss $(144)M vs net loss $(740)M shows the interest-expense weight directly.
- **CRWV FY2025 10-K (Tier 1; year ended Dec 31, 2025).** Source of the +168% revenue, the $(46)M operating loss / $(1,167)M net loss / $1.23B interest expense, the $10.3B capex, the $21.6B debt, the **Microsoft ~67%** concentration, the ~3.1 GW contracted power, the crypto-mining-history / IPO context, and the **NVIDIA $2B equity investment** (Jan 2026 subsequent event). "Committed contracts >98% of revenue" frames the backlog-conversion model.

## Change log

- **2026-06-03 (S121 — creation):** First-canonical ingest from FY2025 10-K + Q1 2026 10-Q + Q1 2026 call. The hyperscaler PAYER/SPENDER program's **6th and final payer — the first rent-side / neocloud** (the program is now complete: 5 hyperscalers + 1 neocloud). `layer: outside` + all five `*_tier: outside` (CAPEX deployer / capacity provider; no chokepoint rent). Section 2.11 N/A (Dec-31 filer). Honest-verdict: included for rent-side completion + the fragility/early-warning ("canary") vantage, not thesis centrality. Centerpiece: the **capex-vs-revenue gap** — FY2026 capex $31-35B vs $12-13B revenue (~2.6-2.9×); "CapEx shows up before revenue"; funded by $25.1B of rising-cost debt ($1.23B FY2025 interest), the NVIDIA $2B equity investment (the circularity, primary-confirmed), and Microsoft ~67% concentration (Tier-1/Tier-2 disclosure gap — 10-K-named, zero call mentions). Verified financials direct from the statements (FY2025 revenue $5,131M / op loss $(46)M / net loss $(1,167)M / capex $10.3B / debt $21.6B; Q1 2026 revenue $2,078M / net loss $(740)M / debt $25.1B / backlog $99.4B). Cross-vault propagation: [[hyperscaler-capex]] (6th / first rent-side row + dynamics #7/#8/#9 + disconfirming #5), [[AI-demand-durability]] (rent-side demand subsection), [[nvidia-supply-chain-commitments]] (the NVIDIA→CRWV circularity). Companies 60 → 61.
