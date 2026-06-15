---
type: company
tickers: [NBIS]
layer: outside
photonics_tier: outside
memory_tier: outside
energy_power_tier: outside
equipment_tier: outside
materials_tier: outside
foreign_issuer: true
last_updated: 2026-06-03
---

# NBIS — Nebius Group N.V.

## Thesis role

Nebius is the hyperscaler PAYER/SPENDER program's **7th payer and 2nd rent-side neocloud** (after [[CRWV]]) — a GPU-renting AI-cloud that buys NVIDIA accelerators, houses them, and rents compute to hyperscalers and labs on multi-year contracts. Its value to the vault is the **neocloud pair**: read alongside [[CRWV]], it turns the rent-side "canary" from a single company into a **pattern** — two debt-and-equity-funded, Microsoft-anchored, NVIDIA-funded GPU clouds, of which Nebius is the **more extreme spender** (FY2026 capex guided at ~7-8× revenue vs CoreWeave's ~3×).

**Honest-verdict framing (Section 2.1).** Like CoreWeave, Nebius holds **no chokepoint** — it is a capacity provider and price-taker buying merchant NVIDIA GPUs. Its inclusion is **not** for thesis centrality; it is the **2nd rent-side data point** (making the neocloud fragility a pattern, not a one-off) and the **most extreme capex-vs-revenue case in the program.** Two honest nuances distinguish it from CoreWeave, though: its **core cloud segment is adjusted-EBITDA-positive** (below), and it carries a large **cash buffer** rather than CoreWeave's heavier net debt — so it is the more aggressive *spender* but, for now, the better-*funded* one.

**Foreign issuer (Section 4.2).** Nebius Group N.V. is a **Netherlands-domiciled** company (the entity left after Yandex N.V. divested its Russian business in 2024, rebranded), listed on NASDAQ. It files **20-F + 6-K** (not 10-K/10-Q) and reports in **USD under IFRS**. **Section 2.11 N/A** — it is a calendar-year (December 31) filer; Q1 2026 = calendar Q1 2026. `foreign_issuer: true`.

**Holding-company structure.** Beyond the core **Nebius** AI-cloud business, the group holds **Avride** (autonomous driving) and **TripleTen** (edtech); **Toloka** (AI data) was deconsolidated mid-2025. The AI-cloud segment must be read separately from these — they materially change the consolidated picture (below). **NOT on the [[software-AI-moat-durability]] scorecard.**

## Financial snapshot

Two periods kept separate per Section 4.1 (no blending); USD millions, IFRS. The shape: **revenue is exploding off a tiny base, the core cloud has just turned adjusted-EBITDA-positive, but the group runs a net loss** — driven below the operating line by heavy depreciation and dragged at the EBITDA line by the non-core businesses.

**FY2025 (20-F; year ended December 31 2025; vs FY2024):**

| Metric | FY2025 | FY2024 |
|---|---|---|
| Total revenue | $529.8M | $91.5M (≈ +480%) |
| — Core **Nebius** segment adjusted EBITDA | **+$59.0M** (turned positive) | $(128.5)M |
| — Avride (autonomous driving) adj. EBITDA | $(82.7)M | $(67.0)M |
| — TripleTen (edtech) adj. EBITDA | $(41.2)M | $(30.8)M |
| Group segment adjusted EBITDA | $(64.9)M | $(226.3)M |
| Property & equipment, net | $5,553M | — |

*The core AI-cloud is adjusted-EBITDA-positive; the group EBITDA loss is entirely the Avride + TripleTen moonshots. "Adjusted EBITDA" excludes the large depreciation of the GPU fleet, so even the core is loss-making on a GAAP basis — see Q1 net loss below.*

**Q1 2026 (6-K; quarter ended March 31 2026; call May 13 2026; vs Q1 2025):**

| Metric | Q1 2026 | Q1 2025 |
|---|---|---|
| Revenue | **$399.0M** | $50.9M (**+684%**; +75% QoQ) |
| — of which AI-cloud revenue | $390M | (**+841%**) |
| Depreciation & amortization | $212.0M | $49.1M |
| Operating loss | ~$(128)M | ~$(120)M |
| Net loss | **$(113.5)M** | $(9.2)M |
| Capex (purchases of P&E + intangibles) | **$2,472.9M** | $543.9M |
| Property & equipment, net | $7,132M | (vs $5,553M at Dec-31-2025) |
| Cash & equivalents | **$9,298M** | (vs $3,678M at Dec-31-2025) |

Q1 revenue ($399M) was ~75% of *all* of FY2025 ($529.8M) — the pace of the ramp. Capex of $2.47B against $399M of revenue is the gap the next section is about. The cash jump to $9.3B reflects the early-2026 financings landing (below).

## CAPEX & the capex-vs-revenue gap

The section this ingest exists to source (cross-ref [[hyperscaler-capex]] + [[CRWV]]) — and Nebius is the most extreme case in the program.

- **Current spend.** Q1 2026 capex **$2.47B** (purchases of property & equipment + intangibles) — PP&E net grew $5.55B → $7.13B in the quarter, with D&A of $212M.
- **Projected spend.** **FY2026 capex guidance RAISED to $20-25B** (up from a prior $16-20B range), per CEO Volozh and CFO Boyido Alonso. The raise funds **2027 capacity** coming online early next year, which management expects to contribute to revenue in H1 2027, against customer commitments already in place.
- **The gap (the canary math).** FY2026 capex of **$20-25B sits against roughly ~$3B of revenue** — capex of **~7-8× revenue**, more than double CoreWeave's ~3× and the most extreme capex-to-revenue ratio of any payer in the program. The spend is being deployed years ahead of the revenue it is meant to generate.
- **How it is funded.** Nebius pre-funded the plan with a large liquidity buffer — **cash of ~$9.3B** at March 31 2026 (up from $3.7B), built from early-2026 financings (a NVIDIA equity investment + debt). The CFO said the incremental capacity in the raised guidance "will be funded through additional financing," specifically flagging **asset-backed financing against the Microsoft contract**. So the model is the same as CoreWeave's — debt against contracted demand — but Nebius currently sits on a larger cash cushion.

## Financing & debt fragility (the canary)

- **The cash buffer.** Unlike [[CRWV]] (heavily net-debt), Nebius entered the build with **~$9.3B of cash** (Mar-31-2026), reducing near-term refinancing risk — the more aggressive spender, but for now the better-funded one. This is the key honest distinction between the two neoclouds.
- **The NVIDIA investment (the circularity).** Nebius received **~$2B in proceeds plus a pre-funded Class A purchase warrant (~21M shares)** from **NVIDIA** (per the 20-F) — primary confirmation, from Nebius's own filing, of the "supplier funds its customer" circularity the tracker flags (see [[nvidia-supply-chain-commitments]]); the 2nd vault-canonical instance after CoreWeave.
- **Tier-3 context** (`ai-capex-map-2025-2027.md`, attributed): a ~$4.34B debt issuance in March 2026. Vault primaries (the cash + capex figures above) stand where they differ from the report.
- **Management's own framing.** The 20-F states plainly that **"our core business is capital-intensive and currently not profitable"** — the honest version of the canary thesis. The bet: the $20-25B build, funded ahead of revenue, converts (via the Microsoft/Meta contracts) fast enough to justify the spend before the cash buffer and financing capacity run down.

## Customer concentration

- **Microsoft and Meta** are the anchor customers — "multi-year, multi-billion dollar agreements" with "attractive economics and financing terms" (20-F).
- **Meta** committed to buy **up to $15B of capacity** across these clusters, at Nebius's option, over a five-year contract (CRO Boroditsky). A separate customer agreement referenced on the call could generate **$27B+ in revenue** (consistent with the Microsoft relationship).
- Concentration is the fragility — as with [[CRWV]] (Microsoft ~67%), Nebius's contracted demand is narrow, even as the dollar commitments are large. Exact >10%-customer disclosure to be confirmed against the 20-F at next refresh.

## Business model & structure

Nebius's core model mirrors CoreWeave's: **buy NVIDIA GPUs → house them → rent AI compute on multi-year contracts**, with capacity repeatedly "sold out." It markets **ARR** (annualized run-rate revenue) as its headline forward metric (Q1 group revenue $399M, +75% QoQ). The group is a **holding company**: the core Nebius cloud (adjusted-EBITDA-positive +$59.0M FY2025) plus **Avride** (autonomous driving; $(82.7)M FY2025 adj. EBITDA) and **TripleTen** (edtech; $(41.2)M) — the moonshots that pull the consolidated EBITDA negative — with **Toloka** (AI data) deconsolidated mid-2025. It also retains minority stakes from the Yandex heritage. The non-core businesses are the analytical complication: the AI-cloud story is stronger than the consolidated numbers, but the group's losses are real.

**Where Nebius sits in the stack.** Unlike a pure GPU-renter, Nebius builds and operates its *own* datacenters — so it spans both the compute-rental tier and the host tier. That contrasts with the vault's host/landlord page [[CORZ]] (Core Scientific), which owns power-secured capacity and leases it *to* neoclouds rather than renting compute. The three-tier picture the vault now covers end to end: **demand (hyperscalers) → compute rental ([[CRWV]] / NBIS) → host infrastructure ([[CORZ]]).**

## The CoreWeave comparison (the analytical product)

Reading the two neoclouds together is the point — the rent-side canary as a *pattern*, not a single point:

| | NBIS (Nebius) | [[CRWV]] (CoreWeave) |
|---|---|---|
| FY2026 capex guidance | **$20-25B** | $31-35B |
| ~Revenue base | ~$3B | $12-13B |
| **Capex ÷ revenue** | **~7-8×** (most extreme) | ~3× |
| Funding posture | large cash buffer (~$9.3B) | heavier net debt ($25B) |
| Core profitability | core cloud adj-EBITDA **positive** | net loss |
| Anchor customer | Microsoft + Meta ($15B option) | Microsoft (~67%) |
| NVIDIA stake | $2B + warrant | $2B |
| Filing | foreign (20-F/6-K, IFRS) | domestic (10-K/10-Q) |

Both are debt-and-equity-funded, Microsoft-anchored, NVIDIA-funded GPU clouds selling out capacity and spending years ahead of revenue. Nebius is the **more aggressive spender** (the wider gap) but the **better-funded** today (the cash cushion + the adjusted-EBITDA-positive core). The shared structural risk is the same: a demand wobble or a financing-market tightening hits the rent-side layer first — which is why the pair is the program's early-warning vantage (see [[hyperscaler-capex]] disconfirming signal #5).

## Open questions

1. **Does ARR/contracted demand convert before the financing runs down?** The $20-25B build is funded ahead of revenue; the cash buffer + asset-backed financing must bridge to the 2027 capacity monetizing.
2. **Can it actually fund $20-25B?** Even with $9.3B cash, the guidance implies large additional financing — how much, on what terms, and how does the cash cushion deplete through 2026?
3. **Microsoft/Meta concentration durability** — how exposed is the contracted demand to its two anchor customers?
4. **Path to group profitability** — the core cloud is adjusted-EBITDA-positive, but GAAP net losses persist (D&A) and Avride/TripleTen drag; when (if) does the group turn net-income-positive?
5. **Do the non-core businesses distract or fund?** Avride + TripleTen consume EBITDA; do they get divested (like Toloka) to focus on the cloud?

## Source audit notes

Per-source entries, ordered by recency + tier.

- **NBIS Q1 2026 earnings call (Tier 2; May 13, 2026; quarter ended Mar 31, 2026).** Source of the **$20-25B FY2026 capex guidance** (raised from $16-20B), the asset-backed-financing-against-Microsoft framing, the Meta $15B capacity option, and the "sold out capacity" demand framing. Management (Volozh / Boyido Alonso / Boroditsky) answered analyst questions on the capex-vs-revenue gap and Meta backstop directly — no defensive or dismissive markers; **CEO-combativeness count UNCHANGED**.
- **NBIS Q1 2026 6-K (Tier 1; quarter ended Mar 31, 2026; cover + EX-99.1 MD&A + EX-99.2 financial statements).** Source of the verified Q1 financials ($399M revenue, $(113.5)M net loss, $2.47B capex, $7.13B PP&E, $9.3B cash). **6-K-exhibit diligence:** the 6-K cover is a wrapper; the actual financials sit in the exhibits (EX-99.2 statements + EX-99.1 MD&A) — a foreign-issuer pattern handled per Section 4.2.
- **NBIS FY2025 20-F (Tier 1; year ended Dec 31, 2025; USD/IFRS).** Source of the $529.8M revenue, the **segment split** (core Nebius adj-EBITDA +$59.0M; Avride $(82.7)M; TripleTen $(41.2)M; group $(64.9)M), the $5.55B PP&E, the NVIDIA **$2B + pre-funded warrant**, the Microsoft/Meta multi-year agreements, and the "capital-intensive and currently not profitable" admission. **Foreign-issuer + holding-company complexity:** the Toloka mid-2025 deconsolidation + the Avride/TripleTen segments require separating the AI-cloud story from the consolidated numbers; a 20-F/A amendment (filed May 22, 2026) was noted at Phase 0 (original 20-F is the annual report).

## Change log

- **2026-06-03 (S122 — creation):** First-canonical ingest from FY2025 20-F + Q1 2026 6-K (cover + EX-99.1 MD&A + EX-99.2 financials) + Q1 2026 call. The hyperscaler PAYER/SPENDER program's **7th payer and 2nd rent-side neocloud** (after [[CRWV]]) — making the rent-side canary a *pattern*. Foreign issuer (Netherlands, ex-Yandex; Section 4.2; 20-F/6-K; USD/IFRS); `layer: outside` + all five `*_tier: outside` + `foreign_issuer: true`; Section 2.11 N/A (Dec-31). Honest-verdict: no chokepoint — the most extreme capex-vs-revenue case (~7-8×) but better-funded than CoreWeave (cash buffer + adj-EBITDA-positive core). Centerpiece: the **CAPEX gap** — FY2026 capex guidance **$20-25B (raised from $16-20B) vs ~$3B revenue**, $2.47B Q1, funded by a ~$9.3B cash buffer + asset-backed financing vs the Microsoft contract + the NVIDIA $2B+warrant (the circularity, primary-confirmed). Verified financials direct off the statements (FY2025 revenue $529.8M / core Nebius adj-EBITDA +$59.0M / group adj-EBITDA $(64.9)M; Q1 2026 revenue $399.0M (+684%) / net loss $(113.5)M / capex $2,472.9M / PP&E $7.13B / cash $9.3B). Holding-company structure (core cloud + Avride + TripleTen; Toloka deconsolidated mid-2025). Customers: Microsoft + Meta ($15B 5-year capacity option; a $27B+ agreement referenced). Cross-vault propagation: [[hyperscaler-capex]] (7th / 2nd-neocloud row + the CoreWeave comparison), [[AI-demand-durability]] (rent-side demand subsection), [[nvidia-supply-chain-commitments]] (2nd circularity instance). Companies 61 → 62.
