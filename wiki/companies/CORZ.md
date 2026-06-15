---
type: company
tickers: [CORZ]
layer: outside
photonics_tier: outside
memory_tier: outside
energy_power_tier: outside
equipment_tier: outside
materials_tier: outside
last_updated: 2026-06-15
---

# CORZ — Core Scientific, Inc.

## Thesis role

Core Scientific is the vault's **first host / landlord page** — the layer *beneath* the neoclouds. Where [[CRWV]] and [[NBIS]] buy NVIDIA GPUs and rent compute, CORZ builds the **power-secured shells** the GPUs sit in: it sells wholesale colocation (space, grid power, cooling, facility operations) to AI cloud operators on long-term leases, and the customer brings its own hardware. It completes a three-tier picture the vault had only covered from the top down — **demand (hyperscalers) → compute rental ([[CRWV]] / [[NBIS]]) → host infrastructure (CORZ).** It is a former Bitcoin self-miner (it emerged from Chapter 11 in July 2024) now converting every megawatt it owns to high-density colocation over ~3 years.

**Why it matters to the thesis.** CORZ owns the thing the whole build-out is actually short of: **power-secured land + grid interconnection + permits** — the binding 2026 constraint per `_thesis.md` (power, not chips). GPUs depreciate; an energized, interconnected site in a power-constrained grid gets *scarcer*. That makes the host layer, in principle, a more durable position than the GPU-renting layer above it. The forward sharpening of that angle is a pivot toward **behind-the-meter natural-gas generation** (below) to bypass the grid-interconnection queue — which ties CORZ to [[BTM-grid-bypass-workaround]].

**Honest-verdict framing (Section 2.1).** The durability is real but heavily qualified, and the page states the qualifier plainly: **CoreWeave is 100% of CORZ's colocation revenue** (10-K). The thesis and the central risk are the *same fact*. Three more counterweights: the company runs a **stockholders' deficit of $(1.31)B** (negative equity) and a debt-funded build; the headline net losses are large (though mostly non-cash — impairments + warrant remeasurement); and a FY2024-plus-2025-interims **restatement** (a property-accounting error, below) is a controls flag on a young public company. The structural read is "owns the scarce asset, but on one customer's back, with a fragile balance sheet" — not a clean fortress.

**Placement.** `layer: outside` + `outside` on all five per-domain tiers — a capacity/host provider that captures no supply-side chokepoint *rent*, parallel to [[CRWV]] / [[NBIS]]. **`energy_power_tier: outside` is deliberate and honest-verdict-correct:** the FY2025 10-K shows CORZ **buys** grid power from 11 utilities at substations — it does **not** generate. The behind-the-meter gas strategy is forward and in-development (12-14-month lead times, own-vs-PPA undecided, air-quality permits still in study), so assigning an energy/power tier would over-claim a generation position CORZ does not yet hold. The scarce-asset angle lives in prose, not a tier — revisit at a future refresh if BTM generation becomes operational and owned. **Section 2.11 N/A** — calendar-year (December 31) filer; Q1 2026 = calendar Q1 2026.

## Financial snapshot

Two periods kept separate per Section 4.1 (no blending). The shape to read: **the business model crossed over in Q1 2026 — colocation revenue overtook Bitcoin self-mining — while the headline net losses are dominated by non-cash charges (asset impairments + warrant/CVR remeasurement), not operating cash burn.** The load-bearing *operating* trend is the colocation gross margin climbing as billable megawatts come online.

**Restatement flag (Section 4.3).** A 10-K/A + 10-Q/A cluster (filed ~March 2026) restated **FY2024 and all three 2025 interim quarters** for a property-accounting error: CORZ kept capitalizing the carrying value of assets **committed to demolition** during the mining→colocation conversion, which should have been impaired to fair value when the demolition decision was made (10-K Note 3; assessed material). **The FY2025 figures below are the clean, corrected as-filed numbers** from this 10-K; FY2024 comparatives are the restated ones.

**FY2025 (10-K; year ended December 31 2025; vs FY2024):**

| Metric | FY2025 | FY2024 |
|---|---|---|
| Total revenue | $319.0M | $510.7M |
| — Bitcoin self-mining | $229.2M | $408.7M |
| — Colocation (HPC hosting) | $65.4M | — |
| Gross profit | $37.9M | $121.1M |
| Operating loss | $(245.6)M | $(142.1)M |
| Net loss | $(288.6)M | $(1,437.9)M |

*FY2025 net loss includes $21.6M of CoreWeave-merger advisory/legal costs (below). The FY2024 $(1.44)B net loss was driven by a ~$1.45B non-cash warrant/CVR remeasurement following the July 2024 bankruptcy emergence — not operations. Colocation gross margin ran ~30% in FY2025, the first full year of the segment.*

**Q1 2026 (10-Q; quarter ended March 31 2026; call May 6 2026; vs Q1 2025):**

| Metric | Q1 2026 | Q1 2025 |
|---|---|---|
| Total revenue | $115.2M | $79.5M |
| — **Colocation** | **$77.5M** | $8.6M |
| — Bitcoin self-mining | $30.1M | $67.2M |
| — Hosted mining | $7.6M | $3.8M |
| Gross profit | $30.1M | $8.2M |
| Net loss | $(347.2)M | +$576.3M |
| Cash & equivalents | $1,005M | — |
| Stockholders' equity (deficit) | $(1,306)M | — |

**The crossover:** colocation ($77.5M) overtook self-mining ($30.1M) for the first time. **Colocation gross margin jumped to 56.7%** (from ~30%) as billable megawatts ramped. The $(347.2)M net loss vs the prior-year +$576.3M *income* is a ~$923M swing, but it is **non-cash**: a $266.5M PP&E impairment (more conversion write-downs) plus warrant/CVR remeasurement — the inverse of the prior-year warrant *gain*. Read the colocation margin, not the net line. Total debt ~$2.06B (notes payable, current + non-current); warrant liabilities $961.2M; the negative equity is the legacy of the bankruptcy capital structure plus the warrant overhang.

## CAPEX & the build-out

- **Portfolio.** ~**920 MW of leasable customer power capacity** (≈1.43 GW gross utility) across **10 facilities in 7 states** at Dec-31-2025 (10-K). Named sites: Denton TX (394 MW), Pecos TX (300 MW), Muskogee OK (100 MW), Marble NC (82 MW), plus Georgia, Alabama, Kentucky, North Dakota.
- **2026 spend.** ~**$2B of capex guided for 2026** (Q1 call, CFO Nygaard) — including ~$700M for the Hunt County TX site acquisition (closed) and the **Polaris** acquisition at Muskogee, plus long-lead equipment and site pre-seeding for ~1 GW of new billable capacity. The build is being deployed *ahead* of signed contracts (a deliberate "invest-ahead-of-RFS" strategy to compress time-to-power), guard-railed to taking "the first data hall to full RFS."
- **Pipeline (Tier 2, forward).** Two ~1.5 GW campuses lead it: **Pecos** (path from 300 MW → 1.5 GW) and **Muskogee** (~1 GW leasable / ~1.5 GW gross, ~440 MW of it via the Polaris transaction). Additional capacity *outside* the CoreWeave contract is targeted for RFS in 2027, with "five sites with first data halls RFS in 2027" (CEO Sullivan, Q1 call).
- **The execution moat (management framing, Tier 2).** CORZ frames its edge as hands-on experience: it ran the CoreWeave build across five sites and "executed more than 150 design changes" iterating the high-density design — and is shifting from harder brownfield conversions to standardized greenfield builds. Treat as management's own characterization.

## Financing & debt

CORZ funds the build with debt against contracted demand — structurally the *inverse* of [[CRWV]]'s GPU-collateralized debt: CRWV borrows against GPUs and customer contracts; CORZ borrows against the **host site assets + the CoreWeave lease contracts** themselves. This is why CORZ belongs in the cross-vault credit map at [[AI-buildout-who-holds-the-risk]] as a distinct **host-layer financing** structure.

- **The CoreWeave project bond (the centerpiece; Tier 2, disclosed at the May 6 2026 call as a subsequent event).** CORZ closed a **$3.3B CoreWeave project bond at a 7.75% coupon**, with **net proceeds of ~$2.9B** after closing costs + a funded debt-service-reserve account. It carries a **lockbox / cash-waterfall structure**: CoreWeave contract revenues flow into a designated account and are applied first to operating expenses, then debt service, then — crucially — the *majority* of offering proceeds can be distributed up to the corporate level to fund **non-CoreWeave** projects. So it is asset-backed against the CoreWeave-contracted sites but releases capital to diversify. (Confirm the final indenture terms at the next 10-Q.)
- **Public convertibles (Tier 1, 10-K).** $460M **3.00%** Convertible Senior Notes due 2029 + $625M **0.00%** Convertible Senior Notes due 2031 — both publicly traded. These give CORZ a tradeable (if equity-linked) credit footprint; see [[AI-credit-spread-watch]].
- **Balance sheet.** Q1 2026 total debt ~$2.06B (pre-bond); ~$1.0B cash; stockholders' **deficit $(1.31)B**. The bankruptcy-emergence exit debt (2024) was largely repaid the same year.
- **Bitcoin treasury de-risked.** CORZ "monetized a significant portion" of its Bitcoin holdings and retains "only a modest amount" on the balance sheet (Q1 call) — removing most of the crypto-price exposure that defined the old company.

## Customer concentration (CoreWeave) + the rejected acquisition

- **CoreWeave = 100% of Colocation segment revenue** (10-K, exact wording: *"One customer, CoreWeave, currently accounts for 100% of our Colocation segment revenue"*). Reciprocally confirmed (Section 3.5) — it is a public contract, and [[CRWV]]'s own 10-K discloses the relationship. Contracted capacity ramped via options from 16 → 216 → **~590 MW** on **12-year leases** (the 12-year term confirmed on the Q1 call via the straight-line GAAP revenue disclosure; the 10-K states only "10 years or more" generically).
- **The delivery curve.** **243 MW billable to CoreWeave** at Q1 2026 (≈ **>$350M annualized colocation GAAP run-rate**, per CFO) — Marble NC (65 MW) + Dalton GA phase I (30 MW) fully turned over — stepping to **>450 MW by end of summer 2026** and the **full 590 MW by early 2027** (COO Brown).
- **The margin target (Tier 2, non-GAAP).** Management *raised* its **cash-gross-profit target for the CoreWeave contract to 80-85%** (from an original 75-80%), citing greater cost visibility now that a meaningful share of the megawatts is billing. Keep this distinct from the **GAAP** colocation gross margin (56.7% in Q1) — it is a non-GAAP management target, not a realized figure.
- **The rejected acquisition (the defining counterparty event).** CoreWeave signed an **all-stock Agreement and Plan of Merger to acquire Core Scientific on July 7 2025**; it was **terminated on October 30 2025 after CORZ stockholders rejected it** at a special meeting. **No termination fee**; ~$21.6M of advisory/legal costs hit FY2025. The standalone path the page describes exists *because* CORZ's own holders refused to be absorbed by their 100%-of-colocation customer — a genuinely unusual host-tenant dynamic (a candidate for a dedicated CRWV↔CORZ relationship page).
- **Diversification catalyst (Tier 2, in progress).** A hyperscaler exclusivity over Pecos + Muskogee **expired**; CORZ says **three hyperscalers immediately re-engaged** on those sites, and it is replacing blanket exclusivity with a "milestone arrangement" approach. Chip makers, AI labs, and neocloud providers are also named as engaging. A signed second large customer would be the single biggest de-risking event for the concentration thesis — and is the key thing to watch.

## Capacity & power strategy (grid today, behind-the-meter tomorrow)

- **Today: a grid-power buyer.** The 10-K is explicit — bilateral firm/interruptible supply agreements with **11 utilities** (TVA, Duke, Denton Municipal, Texas New-Mexico Power, OG&E, Austin Energy, Alabama Power, and others) delivered to **dedicated substations**. No on-site generation in the FY2025 picture. This is what keeps `energy_power_tier: outside`.
- **The pivot: behind-the-meter gas (Tier 2, forward; the [[BTM-grid-bypass-workaround]] connection).** The Q1 call reveals a power strategy moving *beyond existing grid capacity* — securing natural-gas infrastructure to enable expansion where the grid queue would otherwise bind. Concretely: a **linear gas pipeline to the Pecos campus** ("low-emission generation"), and Muskogee combining BTM infrastructure with utility supply (incl. the ~440 MW Polaris acquisition), helped by Oklahoma's behind-the-meter legislation. Management frames BTM lead times at ~12-14 months and is explicit that the ownership model is **undecided** — some generation it might own, some via third-party PPAs; air-quality permits are still in study. This is exactly the grid-bypass workaround the vault tracks at [[BTM-grid-bypass-workaround]] — CORZ is an **emerging, not-yet-operational** participant there; the durable-asset thesis strengthens *if* BTM generation comes online and is owned, weakens if it stays a third-party PPA pass-through (where CORZ captures no generation economics).
- **Consumer of two vault chokepoints.** Each high-density deployment pulls on distribution-tier grid gear ([[transformer-supply]] — transformers, switchgear, interconnection) and on [[liquid-cooling]] (high-density AI colocation). CORZ's buildout pace is a demand signal on both.

## Business model & the Bitcoin wind-down

CORZ's model: **secure power + land → build standardized high-density shells → lease them to AI operators on long-term contracts** (fixed capacity payments + variable usage), with the tenant deploying its own GPUs. The legacy Bitcoin self-mining business (~151,400 miners at Dec-31-2025, down ~12% YoY) is being wound down to fund the transition — running only to consume committed power during conversion. Management now dates the wind-down: by **end-2026, only one or potentially two sites** will still mine (CEO Sullivan, Q1 call), with a meaningful step-down in the second half. The endgame is an all-colocation operator within ~3 years.

## Open questions

1. **Does a second large customer sign?** The expired Pecos/Muskogee exclusivity and three re-engaged hyperscalers are the path off 100%-CoreWeave-colocation concentration. Watch for a signed non-CoreWeave lease (targeted RFS 2027) — the biggest single de-risking event.
2. **BTM generation — owned or passed-through?** The durable-asset thesis hinges on whether CORZ *owns* the behind-the-meter gas generation (captures the economics) or merely contracts it via PPA (pass-through). Watch Pecos/Muskogee for an ownership decision + air-quality permit progress.
3. **The project-bond structure.** What are the final indenture terms of the $3.3B 7.75% CoreWeave bond — covenants, the cash-waterfall release mechanics, how much actually frees up to fund non-CoreWeave growth? Confirm at the next 10-Q.
4. **Billable-MW disclosure cadence.** Does the 590 MW deliver on schedule (450 MW by end-summer 2026 → 590 MW early 2027), and does management keep disclosing billable MW so the colocation run-rate stays trackable?
5. **Impairment trajectory + controls.** Do the conversion-driven PP&E impairments keep recurring as more mining sites convert, and does the restatement remediation hold (no further property-accounting corrections)?
6. **Negative equity.** Does the colocation cash flow + the $2.9B net bond proceeds repair the $(1.31)B stockholders' deficit over time, or does the warrant overhang keep equity negative?

## Source audit notes

Per-source entries, ordered by recency + tier.

- **CORZ Q1 FY2026 earnings call (Tier 2; May 6 2026; quarter ended Mar 31 2026).** The richest source for the forward story: confirms the **12-year** CoreWeave term, the **243 MW billing ≈ >$350M annualized** colocation run-rate, the **80-85% cash-gross-profit target** (raised from 75-80%, non-GAAP), the **$3.3B 7.75% CoreWeave project bond** (net ~$2.9B, lockbox structure), the **behind-the-meter gas pivot** (Pecos pipeline, Polaris/Muskogee, Oklahoma BTM legislation), the **Hunt County (~$700M) + Polaris** acquisitions, ~$2B 2026 capex, the expired-exclusivity diversification path, and the **end-2026 mining wind-down to 1-2 sites**. Management (Sullivan / Brown / Nygaard) answered analyst questions on exclusivity, BTM lead times/cost, and the margin-target raise directly and at length — no defensive markers; **CEO-combativeness count UNCHANGED**.
- **CORZ Q1 FY2026 10-Q (Tier 1; quarter ended Mar 31 2026).** Source of the verified Q1 financials — the **colocation-over-mining crossover** ($77.5M vs $30.1M), the 56.7% colocation gross margin, the $(347.2)M net loss (with the $266.5M PP&E impairment driving it), ~$1.0B cash, ~$2.06B debt, and the **$(1.31)B stockholders' deficit**.
- **CORZ FY2025 10-K (Tier 1; year ended Dec 31 2025).** Source of FY2025 revenue $319.0M / gross profit $37.9M / operating loss $(245.6)M / net loss $(288.6)M; the **CoreWeave = 100% of colocation revenue** disclosure; the **920 MW / 1.43 GW** portfolio + 11-utility grid-power sourcing; the two **public convertibles** ($460M 3.00% 2029 + $625M 0.00% 2031); the **restatement** (Note 3, PP&E demolition-capitalization error, FY2024 + 2025 interims, $21.6M merger costs); and the **terminated CoreWeave merger** (signed Jul 7 2025, rejected by stockholders Oct 30 2025, no fee).
- **CORZ Q4 FY2025 earnings call (Mar 2 2026) — SOURCE UNAVAILABLE (Section 2.2 observation).** The PDF in the source set is a paywalled Quartr/Yahoo export: only the header + an AI-generated summary are readable, with the call body behind an "upgrade" wall. The AI summary is Tier-3/4 and was **not** used as primary. The prior-baseline call is therefore not available at primary; the Q1 FY2026 call + the two filings carry this first-canonical ingest. Re-fetch a full transcript to recover the Q4 baseline.

<!-- LATEST-ALPHA:START -->
## ⚠️ Latest alpha — unverified, between-filings (as of 2026-06-15)

*Tier 3/4 discovery — NOT canonical. Recent 8-K / news, to verify at the next primary source. Full detail + sources: [discovery note](../../raw/notes/latest-alpha/2026-06-15_CORZ_recent-developments.md). Items graduate into canon (or are pruned) at the next 10-Q/10-K ingest.*

- **Steve M. Smith appointed to the Board** (8-K, May 26 2026) — Tier 1 · the **former Equinix CEO** (2007-2018) + current **Zayo CEO** + NextDC director joins as an independent director — heavyweight datacenter-industry governance for the host pivot, and exactly the operator profile that could help land a **second hyperscaler customer** beyond CoreWeave. `[verify: next proxy/10-Q for committees + comp; watch whether it precedes a non-CoreWeave lease — the Open Question #1 concentration-break trigger]`
- **2026 Annual Meeting results** (8-K Item 5.07, May 12 2026) — Tier 1 · five directors re-elected; routine, but **Jeff Booth + Eric Weiss each drew ~51M withhold votes** (vs ~2-7M for the other three) — a mild governance-dissent signal, not a failure. `[verify: 2026 proxy; track at the 2027 meeting]`
- **$1B JPMorgan + Morgan Stanley strategic financing facility** (announced Mar 23 2026 — pre-dates the May 6 call) — Tier 1 · a separate instrument from the $3.3B CoreWeave bond ($500M JPMorgan added to $500M Morgan Stanley); the canon Financing section does not yet name it. `[verify: confirm in the Q1 2026 10-Q debt note — likely already disclosed; fold into canon at next refresh]`
- **Counterweight (unchanged):** nothing post-call alters the core risk — the **$3.3B 7.75% bond + CoreWeave = 100% of colocation revenue** are already in canon; the honest-verdict concentration story stands.
- Related: [[CRWV]] [[AI-credit-spread-watch]] [[BTM-grid-bypass-workaround]] (host-tenant; the bond as a host-layer credit instrument; the BTM-gas pivot)

*Signal only (not weighted): stock cooled ~9% on the week into early June off a ~67% 90-day run; a sell-side target raise circulated (Jun 3) — price/sentiment only, never a vault input.*
<!-- LATEST-ALPHA:END -->

## Change log

- **2026-06-15 (S162 — creation):** First-canonical ingest from FY2025 10-K + Q1 2026 10-Q + Q1 FY2026 call (Q4 call paywalled/unavailable). The vault's **first host/landlord page** — the infrastructure tier beneath the neoclouds ([[CRWV]] / [[NBIS]]): demand → compute rental → host. `layer: outside` + all five `*_tier: outside` (incl. `energy_power_tier: outside` — a grid-power buyer, not a generator; the BTM-gas pivot is forward/in-development). Section 2.11 N/A (Dec-31 filer). Honest-verdict centerpiece: **CoreWeave = 100% of colocation revenue** (the thesis and the risk are one fact) — and the customer's all-stock acquisition of CORZ was **rejected by CORZ stockholders (Oct 2025)**. Verified financials off the statements (FY2025 rev $319.0M / net loss $(288.6)M; Q1 2026 rev $115.2M with **colocation $77.5M overtaking self-mining $30.1M**, colo GM 56.7%, net loss $(347.2)M impairment-driven, **stockholders' deficit $(1.31)B**). Financing: the **$3.3B 7.75% CoreWeave project bond** (net ~$2.9B, lockbox) + two public convertibles. **Restatement flagged** (PP&E demolition-capitalization error; FY2024 + 2025 interims; FY2025 figures clean). New connection surfaced from the call: the **behind-the-meter gas pivot → [[BTM-grid-bypass-workaround]]**. Cross-vault propagation: [[CRWV]] (host-tenant back-link + the rejected merger), [[AI-buildout-who-holds-the-risk]] (host-layer financing structure), [[hyperscaler-capex]] (host-supply note), [[AI-credit-spread-watch]] (public-convertible + project-bond instrument note), [[transformer-supply]] + [[liquid-cooling]] + [[BTM-grid-bypass-workaround]] (consumer/participant), [[NBIS]] (three-tier-stack cross-ref).
