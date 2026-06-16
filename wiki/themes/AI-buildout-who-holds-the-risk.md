---
type: theme
tickers: [AVGO, NVDA, CRWV, NBIS, ORCL, AMZN, META, MSFT, GOOGL, BE, CSCO, CORZ]
last_updated: 2026-06-16
---

# AI Build-out — Who Holds the Risk

## Thesis role

Mechanism theme. **The question: if AI revenue disappoints, who actually eats the loss?** The AI build-out is increasingly paid for with other people's money and circular promises — vendors investing in their own customers, chipmakers guaranteeing their customers' debt, credit funds lending against GPUs, and frontier labs committing sums they have not raised. This page maps the financing structures, traces each one to its loss-bearer, and keeps the early-warning instruments in one place. It is the falsifier-side twin of [[AI-demand-durability]]: that page tracks whether the demand is real; this page tracks who is exposed if it isn't.

**Sibling page (verdict-ownership rule).** [[neocloud-moat-durability]] asks the adjacent question for the GPU-rental layer specifically — *is the neocloud business model a durable moat or a borrowed one?* — and owns **moat-durability verdicts** (its answer: borrowed-and-temporary, tilting leverage-trap; the neocloud sits at the bottom of the chokepoint gradient, renting every scarce input and owning only the spread). **This page owns loss-distribution verdicts** — where CoreWeave (Structure #4) and Core Scientific (#8) sit in the credit cascade. A name on both carries one verdict of each kind, never two of the same: the durability *why* lives there; the who-eats-the-loss *map* lives here.

**The verdict (from the 2026-06-13 verified research run; anchor: `raw/research/ai-buildout-credit-risk-report.md`): the honest middle, tilted toward load-bearing at the margin.** Three findings carry it:

1. **The funding regime has already flipped.** The big five payers' (Alphabet, Amazon, Meta, Microsoft, Oracle) free cash flow has fallen *below* capex in absolute terms — the BIS bulletin on it is literally titled "from cash flows to debt" (BIS Bulletin 120, January 2026). Of ~$2.9T projected 2025-2028 AI capex, **~$1.5T must come from external capital, ~$800B of it private credit** (Morgan Stanley sizing, relayed by the FSB and Bank of England, May 2026 — Tier 3 origin, official-sector relay). The build-out is no longer self-funded; "marginal wrapper" is no longer the right description.
2. **But it is not telecom-2000 — yet.** The boom is ~1% of US GDP (half the dot-com-era rise in IT investment); only ~20% of private-credit funds participate and AI is ~5% of the average fund's book; the IMF judges stability risks "contained" — *conditional* on AI earnings arriving (IMF GFSR April 2026; BIS). And the strongest point for the benign reading: **as of June 2026, no AI financing structure has failed, been drawn, been impaired, or repriced.**
3. **The warning light that decides between the two readings:** private-credit lenders price AI loans **identically** to non-AI loans (spreads 6.2 vs 6.1pp; insignificant after controls) while S&P models **70-90% loss-given-default** on neocloud unsecured debt. BIS draws the inference itself: "either lenders may be underestimating the risks of AI investments... or equity markets may be overestimating the future cash flows." **One of the two markets is wrong.** The resolution of that disagreement is what this page watches.

## The regime flip — the sizing

| Measure | Figure | Source (tier) |
|---|---|---|
| Projected AI infrastructure capex 2025-2028 | ~$2.9T | Morgan Stanley via FSB Graph 4.1 (Tier 3, official relay) |
| Of which external capital required | **~$1.5T** | same |
| — private credit (asset-based finance largest channel) | ~$800B | same |
| — investment-grade tech bonds | ~$200B | same; IMF: >$100B already raised since Jan 2025 |
| — data-center ABS/CMBS | ~$150B (vs $46B issued since 2018) | MS; IMF GFSR Box 1.3 |
| — plug (sovereign, PE, VC, other) | ~$350B | MS only |
| Big-five FCF vs capex | **FCF now BELOW capex** | BIS Bulletin 120 (Jan 2026) |
| Private credit outstanding to AI-related firms | $200B+ (~8% of all private credit); BIS projects $300-600B by 2030 | BIS |
| AI share of 2025 private-credit deal value | 34% (vs ~17% prior-5yr avg) | FSB/OECD |

Honest caveats baked in: the $2.9T/$1.5T split is ultimately one sell-side estimate (MS itself flags it biased *higher* if hyperscalers cut capex, pushing more onto credit markets); "AI-related" private credit uses broad PitchBook verticals; and total IT investment at ~5% of GDP now *exceeds* the 2000 peak even though the AI-specific slice is smaller.

## The eight structures — the exposure table

Vault-primary (Tier 1/2) unless noted:

| # | Structure | Size | Who books revenue now | Who eats the loss if demand disappoints |
|---|---|---|---|---|
| 1 | **Customer-debt backstop** — [[AVGO]] guarantees a customer's AI-rack lease obligations; Apollo/Blackstone "AI XPU platform," $35B first tranche, >20 GW through 2028; customer inferably Anthropic ("dependent on Anthropic's continued commercial success," 8-K Apr 2026) | **$29B max exposure** (10-Q Q2 FY2026) | AVGO (XPU + rack revenue) | **AVGO — 100% shortfall compensation** |
| 2 | **Vendor equity-for-commitment** — [[NVDA]]'s six instruments: $2B each into [[LITE]] [[COHR]] [[MRVL]] [[CRWV]] [[NBIS]] + $500M [[GLW]] warrant (max ~$3.2B); note CRWV/NBIS are *customers* — NVDA funds the buyers of its own chips | **~$10.5B** ([[nvidia-supply-chain-commitments]]) | NVDA (GPU/component revenue) | NVDA (equity marks + the revenue the equity enabled) |
| 3 | **Landlord-lender-shareholder** — [[AMZN]]→Anthropic: $8B convertible notes + $5B preferred + $20B drawable facility + $5B future-equity option; stake marked **$48.1B** on Amazon's balance sheet (Q1 2026 10-Q) | **~$38B committed** | AMZN (AWS compute revenue from a customer it finances) | AMZN — three exposures to one counterparty (lender + landlord + shareholder) |
| 4 | **GPU-collateralized debt** — [[CRWV]]: $25.1B total debt (+169% YoY); 9.75%-coupon unsecured 2031 notes; PLUS the landmark **$8.5B DDTL rated A3/Moody's — the first investment-grade GPU-backed financing** — non-recourse, secured by a single-purpose subsidiary + ONE customer contract (8-K Mar 31, 2026). The ~340bp secured/unsecured gap means **the A3 rates the contract, not the company** | $25.1B corporate + $8.5B SPV | CRWV (and NVDA upstream) | Bondholders (S&P recovery rating 5 = **70-90% loss-given-default** on unsecured); SPV lenders ride one customer + GPU residual value |
| 5 | **Off-balance-sheet SPV/VIE** — [[META]] Hyperion ~$30B (Blue Owl 80/20) + [[GOOGL]] VIE commitments ~$40.7B; BIS: structures "might mask leverage by moving it off the balance sheet. Yet leverage does not disappear by being out of sight" | **~$70B+** these two alone | The hyperscalers (capacity without reported debt) | Credit funds first; reported leverage understates reality |
| 6 | **Backlog against an unnamed counterparty** — [[ORCL]]: RPO $552.6B (+325%) naming neither OpenAI nor Stargate once; $50B CY2026 financing envelope; CFO: the structures mean "uncoupling of CapEx from Oracle's capital requirements" (Q3 FY2026 call) | $552.6B RPO | ORCL (booked as backlog) | ORCL's lenders — capex is real and current; the offsetting revenue depends on one customer's own unproven funding |
| 7 | **The prepayment wall** — [[CSCO]] purchase commitments $7.6B→$16.0B in 9 months; [[NVDA]] + [[MSFT]] each ~$145B of supply commitments incl. prepaids; [[MU]]/[[SNDK]] customer advances | $300B+ visible across vault filings | Suppliers (cash up front) | The committers, if demand turns before delivery (links to [[memory-shortage-winners-losers]] Channel C) |
| 8 | **Host-layer project bond** — [[CORZ]] (Core Scientific): a **$3.3B CoreWeave-contracted project bond at 7.75%** (net ~$2.9B; a lockbox/cash-waterfall secured by the CoreWeave site assets + the 12-year lease cash flows), plus ~$1.1B of public convertibles — the *inverse* of #4: where CRWV borrows against GPUs, CORZ borrows against the host **real estate + the lease contracts**. CoreWeave is **100% of CORZ's colocation revenue** (and signed to buy CORZ in 2025 — rejected by CORZ's own holders Oct 2025) | $3.3B bond + ~$1.1B converts | CORZ (host rent) | Project-bond holders (lockbox-secured); equity holders (stockholders' deficit $(1.3)B) |

**The end of the chain (verified):** behind the ~$800B private-credit channel sit **insurance companies, pension funds, sovereign wealth funds, endowments, and high-net-worth retail** (Morgan Stanley); private-credit investors are *first*-loss, not sole loss — the top-5 banks hold **63% of committed BDC lending** (FSB). The FSB names the two triggers that would start the loss cascade: **a shortfall in electricity supply** (the vault's own power thesis, read as credit risk) or **data-center overcapacity** — development outpacing AI-services demand.

## The circularity, quantified

This is no longer just a narrative. **IMF staff attribute ~7 of the ~12 percentage points** of equal-weighted return across the seven AI-circle firms (Amazon, AMD, Alphabet, Intel, Microsoft, Nvidia, Oracle) from September to December 2025 **to correlation-reinforcement effects inside the circular-financing circle — roughly $40B of average market cap on a ~$2T base** — warning the circle "may simultaneously report inflated revenues, potentially detached from fundamentals" (GFSR April 2026, fn. 30). The vault's own primary record draws the same loop at deal level: NVDA funds CRWV/NBIS which buy NVDA chips; Amazon finances Anthropic which rents Amazon compute; AVGO guarantees the leases that fund purchases of AVGO racks. Each leg is individually rational; the system property is that **revenue, equity value, and credit support all lean on the same future cash flows arriving.**

## The two stress quantifications worth remembering

1. **The obsolescence scenario (IMF Box 1.4):** hyperscalers depreciate over an implied ~7 years; GPUs "could face obsolescence within two." A stylized 3-year-life scenario: aggregate EBIT margin **−9pp+**, hyperscaler debt **$800B → $1T+**, CDS spreads **+~60bp**. The IMF calls it "essentially a business risk" — but it is the quantified bridge from a chip-cadence question to a credit question, and it prices the collateral under every GPU-backed loan.
2. **The mispricing gap:** AI loans priced like non-AI loans (BIS) against 70-90% modeled loss-given-default (S&P). Whichever market is right, the adjustment lands somewhere — on lenders' books or on equity multiples.

## Honest gaps — stated plainly

- **The frontier-lab funding-gap math (OpenAI/Anthropic committed vs raised) did NOT survive adversarial verification.** The circulating commitment headlines are largely unverifiable at primary. What the vault can say at Tier 1: Amazon's $38B Anthropic stack and AVGO's Anthropic-linked backstop exist; the labs' ability to fund the rest is an open question, not a documented fact in either direction.
- **The telecom-2000 comparison stays a named analogy, not verified history.** The Lucent/Nortel magnitudes and timeline produced no surviving claims; the analogy lives at Tier 3 (the 2026-03-24 video-intel note) until separately researched. Do not cite it as precedent-proven.
- **The reported Blue Owl walk-away from a $10B Oracle financing is unverified** (Tier 4) — kept as a watch item, not a fact.
- **Nothing has broken.** No drawn backstop, no impairment, no failed financing as of June 2026 — the benign reading's best evidence, recorded here with the same weight as the warnings.

## What would prove the load-bearing read wrong

1. **AI earnings arrive on schedule** — hyperscaler AI revenue growth covers the capex curve and FCF climbs back above capex (the BIS regime flip reverses) → the external financing was bridge, not crutch.
2. **Credit keeps pricing tighter, correctly** — AI-linked spreads stay tight *and* no losses materialize through a full GPU depreciation cycle → the lenders were right, the S&P loss models too conservative.
3. **The circle de-levers voluntarily** — backstop ceilings shrink at successive 10-Qs, vendor equity instruments wind down, labs fund commitments with raised equity rather than vendor support.
4. **Stress arrives and is absorbed** — a neocloud or lab stumbles and the structures contain it without cascade (the system test passed).

## Open questions

1. **AVGO backstop ceiling at the Q3 FY2026 10-Q (~September 2026).** Does $29B grow as later tranches deploy? Does any "drawn" or impairment language appear? (Shared trigger with [[what-could-go-wrong]] Entry 5.)
2. **CRWV against S&P's pre-registered thresholds.** FFO/debt 12% and CFO/debt 10% (now upgrade triggers after the April 2026 positive outlook); internal-control remediation by end-2026; the secured-vs-unsecured spread gap as the market's live vote on contract-vs-company quality.
3. **The spread differential.** Does the BIS AI-vs-non-AI loan pricing gap (currently ~zero) open up? A widening = lenders starting to price the risk; the warning light turning from amber to red. **Now tracked operationally at [[AI-credit-spread-watch]]** (four instrument layers + `scripts/spread_watch.py`).
4. **Depreciation-life changes in hyperscaler 10-Ks.** Any extension of useful lives (flattering current earnings while the IMF scenario worsens) or — more honest — shortening.
5. **The frontier-lab funding cadence.** Anthropic/OpenAI raise announcements vs their commitment schedule; AMZN's $20B facility drawdowns appearing in Amazon's 10-Qs (compute-delivery-milestone-linked).
6. **Data-center vacancy/overcapacity data + electricity-supply shortfalls** — the FSB's two named cascade triggers; feeds from [[transformer-supply]] + [[hyperscaler-capex]].
7. **The first crack, if any.** Verification of the Blue Owl/Oracle report; any private-credit fund publicly pulling back from AI; any structure repriced.

## Source audit notes

Created from a two-layer evidence base: (1) vault primary sources already in canon (AVGO Q2 FY2026 10-Q + 8-Ks; AMZN Q1 2026 10-Q; CRWV FY2025 10-K + Q1 2026 10-Q + Mar 2026 8-K; ORCL Q3 FY2026 10-Q + call; META/GOOGL/MSFT filings via [[hyperscaler-capex]]; [[nvidia-supply-chain-commitments]]); (2) a 107-agent deep-research run (2026-06-13) with 3-vote adversarial verification — 24 of 25 claims confirmed, 1 killed — anchored on BIS Bulletin 120 (Jan 2026), IMF GFSR April 2026 (Ch. 1 + Boxes 1.3/1.4), FSB private-credit vulnerabilities report (May 2026), S&P CoreWeave rating actions (May 2025 + April 2026), and the CoreWeave DDTL 8-K. Full verified report + caveats: `raw/research/ai-buildout-credit-risk-report.md`. Tier discipline: Morgan Stanley's $2.9T/$1.5T/$800B sizing is sell-side (Tier 3) even where relayed by official bodies and is labeled so throughout; the killed claim (that the IMF verdict "directly supports the marginal-wrapper reading") is documented in the anchor report as a boundary on how far the benign reading can be pushed. Sourcing observation: the highest-quality warnings come from central-bank/official-sector documents that equity narratives rarely cite — the BIS spread analysis and the IMF circularity quantification have no visible footprint in the Tier-4 coverage of the same deals.

## Change log

- **2026-06-16 (Session 164):** Added the [[neocloud-moat-durability]] sibling-page cross-reference (verdict-ownership rule — loss-distribution verdicts here; moat-durability verdicts there), from the neocloud-business-model deep-research build. No structures or loss-bearer findings changed. last_updated 2026-06-15 → 2026-06-16.
- **2026-06-15 (Session 162):** Added **Structure #8 — host-layer project bond** ([[CORZ]] Core Scientific's $3.3B 7.75% CoreWeave-contracted bond + ~$1.1B convertibles; the *inverse* of #4's GPU-collateralized debt — host real-estate + lease contracts as collateral), from the CORZ first-canonical ingest. The host/landlord tier beneath the neoclouds now appears in the credit map; CORZ added to tickers.
- **2026-06-13 (Session 157):** Page created (mechanism theme; Vic-approved kickoff; the second of the two S155-audit dig-deeper builds after [[memory-shortage-winners-losers]]). Seven-structure exposure table fusing vault primary + verified official-sector research; loss-bearer chain traced to end-holders; IMF circularity quantification + obsolescence scenario; honest gaps recorded (lab funding-gap math and telecom-2000 comparison did not survive verification; nothing has broken yet). Cross-references added at [[AVGO]] + [[nvidia-supply-chain-commitments]] + [[CRWV]] + [[hyperscaler-capex]] + [[AI-demand-durability]]; [[what-could-go-wrong]] Entries 5 + 6 re-pointed here as canonical evidence home; forward-edge-tracker 10th entry added.
