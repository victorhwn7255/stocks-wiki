---
type: company
tickers: [CEG]
layer: 2
energy_power_tier: outside
photonics_tier: outside
equipment_tier: outside
materials_tier: outside
last_updated: 2026-05-29
---

# CEG — Constellation Energy Corporation

## Thesis role

Constellation Energy is the largest US producer of clean, carbon-free energy and operator of the largest US nuclear fleet (12 operated nuclear stations plus a South Texas Project interest), with a combined ~55 GW fleet across nuclear, natural gas, geothermal, hydro, wind, and solar following the January 2026 Calpine acquisition. It is the **supply side** of the marquee hyperscaler nuclear PPAs the vault has tracked from the uranium/reactor side ([[CCJ]]) and the equipment side ([[GEV]]) — most prominently the Microsoft PPA for the Crane Clean Energy Center (the Three Mile Island Unit 1 restart). CEG had been referenced across the vault for over a session arc as a non-vault counterparty; it is promoted to a canonical page per Section 3.1 (referenced by 5+ vault sources) now that its own primary sources are in hand.

**Placement framing (honest-verdict, Section 2.1).** Per `frameworks.md` v10.1, CEG sits in the **"Adjacent — Power Generation"** category — *"structurally adjacent to the Energy/Power infrastructure thesis but operating in a different framework (energy generation rather than datacenter power infrastructure)… not Tier 1 of Framework 7."* The Framework 7 tiers cover datacenter-power *infrastructure* (equipment and delivery — transformers, switchgear, UPS, power semis: [[ETN]], [[VRT]]), whereas CEG *generates* the electricity. Its frontmatter therefore carries `energy_power_tier: outside` (Adjacent — Power Generation), not a Framework 7 tier — mirroring [[CCJ]] (`energy_power_tier outside`; "not energy/power infrastructure direct"). See the placement-substantiation section; this is the first primary power *generator* in the vault and surfaces a `frameworks.md` revision question (a dedicated Power Generation tier) flagged for a future codification session.

**The `_thesis.md` skepticism, hosted directly.** `_thesis.md` names CEG explicitly but is cautious: *"most direct beneficiaries are utility companies with regulated rate structures (limited upside even when load grows)… Nuclear restart beneficiaries (CEG / VST / NRG) offer adjacent exposure but with significant regulatory and execution risk."* Two honest refinements from primary sources: (1) CEG is a **competitive merchant generator** operating in PJM / MISO / NYISO / ERCOT — explicitly **not a regulated rate-base utility** (CEO Dominguez, on a Pennsylvania governor's letter to utilities: *"even that letter… pertained to regulated utilities and not to entities like Constellation"*). So the "limited upside" critique of regulated utilities partially misapplies — CEG carries merchant price upside plus premium firm-clean PPAs. (2) But the "regulatory and execution risk" is real and confirmed by the sources: PJM/FERC large-load market-design uncertainty dominates the Q1 2026 call, the Crane restart timeline depends on FERC capacity-credit and interconnection decisions, and merchant power-price exposure (weak ERCOT forwards) is a live analyst concern. CEG's vault inclusion is for the power-generation adjacency to the binding 2026 power-infrastructure constraint and for bilateral confirmation of the nuclear-datacenter PPAs — not as a Framework 7 infrastructure chokepoint participant.

## Financial snapshot

### FY2025 annual (CEG 10-K, period-end December 31, 2025; pre-Calpine)

| Metric | FY2025 | FY2024 | Δ |
|---|---|---|---|
| Operating revenues | $25,533M | $23,568M | +8.3% |
| Net generation capacity (proportionate, owned) | 31,676 MW | — | — |

Calpine closed January 7, 2026 and is a **subsequent event** in the FY2025 10-K — so FY2025 figures are pre-Calpine. The 10-K business overview describes the ~55 GW combined fleet reflecting the Calpine addition.

### Q1 2026 quarterly (CEG 10-Q, period-end March 31, 2026; Calpine consolidated) + guidance (Q1 2026 call)

| Metric | Q1 2026 | Q1 2025 | Δ |
|---|---|---|---|
| Operating revenues | $11,122M | $6,788M | +64% (Calpine consolidation) |
| GAAP diluted EPS | $4.49 | — | — |
| Adjusted operating EPS | $2.74 | — | +$0.60 YoY |

- **FY2026 adjusted-operating-EPS guidance reaffirmed at $11-$12** (Q1 2026 call); long-term base EPS growth >20% through 2029, anchored by the nuclear production tax credit (inflation-indexed) + long-term contracts.
- Nuclear: 40M MWh generated Q1 at a **92.3% capacity factor** (incl. more planned outage days than typical). CCGT + cogeneration: 23M MWh at 47.1% capacity factor (5.1% forced outage factor — delivered when called ~95% of the time).
- **Free cash flow before growth:** ~$8.4B (2026-2027) → **$11.5-13B (2028-2029)** (~+45% at midpoint).
- Capital allocation: $5B buyback authorization ($335M / ~1.2M shares at ~$285 in Q1 2026); dividend growing ~10%/year.
- Commercial platform serves ~275M MWh of electricity + 800 BCF of natural gas annually across 40 states; >80% of the Fortune 100.

The Q1 2026 revenue step-up ($6.8B → $11.1B) is driven primarily by Calpine consolidation — a mid-stream M&A boundary; pre- and post-Calpine periods are kept distinct per Section 4.1, and cross-period comparisons should annotate the consolidation date.

## Generation fleet + five geographic segments

CEG reports **five geographic segments** (by region of owned generating resources + customer-facing activity); FY2025 net generation capacity (proportionate ownership, December 31, 2025, pre-Calpine):

| Segment | Net capacity | % | Region |
|---|---|---|---|
| Mid-Atlantic | 10,386 MW | 33% | Eastern half of PJM (NJ, MD, VA, WV, DE, DC, parts of PA + NC) |
| Midwest | 11,606 MW | 37% | Western half of PJM + US MISO (ex-Southern) |
| New York | 3,093 MW | 10% | NYISO |
| ERCOT | 4,742 MW | 15% | Texas |
| Other Power Regions | 1,849 MW | 5% | New England, South, West, Canada |
| **Total** | **31,676 MW** | 100% | — |

Nuclear is the dominant share of the pre-Calpine fleet (12 operated stations — including Calvert Cliffs, FitzPatrick, and others — plus a South Texas Project interest). Calpine adds natural gas (the largest US merchant gas fleet), geothermal (the Geysers), and retail — raising the combined fleet to ~55 GW and shifting the generation mix materially toward gas.

## Datacenter power exposure (thesis-central)

CEG is the generation-side counterparty to several headline AI-datacenter power arrangements:

- **Crane Clean Energy Center (TMI Unit 1 restart) — Microsoft PPA, ~835 MW** of emissions-free capacity dedicated to powering Microsoft's PJM data centers (CEG FY2025 10-K). On the Q1 2026 call, management said the plant "won't start sooner" than planned but is pursuing **full capacity credit**: it has filed at FERC to transfer Capacity Interconnection Rights (CIRs) from the retired Eddystone units to Crane (targeting a 2027-deadline capacity credit), with a FERC response expected June-July 2026 and ongoing work to shorten the transmission-interconnection timeline.
- **Texas (ERCOT) — three data-center projects.** Customers address reliability either by bringing firm backup generation or by accepting full curtailability during grid stress. The **CyrusOne powered-land deal at the Freestone Energy Center** received PUCT approval of its net-metering agreement (a market signal for co-located projects); the enabling substation is expected energized in Q4 2026.
- **New generation delivered / in queue:** Pin Oak Creek 460 MW natural-gas peaker (Texas, commercial ops Q1 2026); Pastoria 105 MW solar (California); ~5,000 MW of new capacity submitted into PJM's interconnection queue (nuclear uprates + new gas + battery storage).
- **Demand signal:** management states hyperscaler demand has "not slowed" — projected 2026 spending ~75% higher than 2025 — and cites 400,000+ MW of large loads in the ERCOT queue (vs a forward market the CEO argues prices only ~10-15k MW of incremental load, implying upside if realized load exceeds ~30k MW).

These confirm, from CEG's own primary sources, the nuclear-datacenter PPAs the vault previously tracked counterparty-side via [[CCJ]] (see Cross-vault adjacency).

## Calpine acquisition

Constellation completed its acquisition of Calpine Corporation on **January 7, 2026** (announced ~January 2025; a subsequent event in the FY2025 10-K, consolidated from Q1 2026). Management guides **~$2/share of full-year adjusted-operating-EPS accretion**. In consideration, CEG issued **50 million Constellation shares** to Calpine owners — **25M subject to a lockup expiring June 30, 2026; 25M expiring June 30, 2027** — a dilution overhang to monitor (management noted the $5B buyback authorization gives flexibility "to the extent there could be a transaction of note around the lockup"). Calpine brings an industry-leading natural-gas fleet, geothermal (the Geysers), a large retail platform, and battery-storage/solar development capability — supplementing Constellation's nuclear base with firm gas generation relevant to ERCOT/PJM co-location and natural-gas data-center transactions.

## PJM / ERCOT regulatory landscape

The Q1 2026 call centered on large-load market-design clarity. PJM has put forward a market-based "backstop" solution plus a co-location framework for large-load customers, with a stated timeline to vote and submit to **FERC in June 2026** ("faster than we had hoped," per Dominguez). PJM had indicated a co-location implementation date of 2029; CEG is pushing for that to be moved up and expects clarity "by the end of the year." Management frames the ERCOT precedent (Texas SB6 concerns resolved once co-location-with-generation requirements were set, after which transactions resumed) as the likely PJM trajectory. Some hyperscaler customers paused agreement negotiations pending regulatory clarity while others continued — a "pause, then quick resumption," not a "full stop," per management.

## Energy/Power placement substantiation (Adjacent — Power Generation)

CEG's frontmatter is `energy_power_tier: outside`, with the placement rationale per `frameworks.md` v10.1's **"Adjacent — Power Generation (cross-domain bridge)"** category, which lists CEG (with VST, NRG) as *"structurally adjacent… but operating in a different framework (energy generation rather than datacenter power infrastructure)… not Tier 1 of Framework 7."* The Framework 7 chokepoint scope is datacenter-power *infrastructure* — transformers (GOES-steel-bound, 4-year lead times), switchgear, UPS/thermal, high-density power delivery — where pricing power accrues to equipment suppliers ([[ETN]], [[VRT]]). CEG generates electricity; it is a buyer, not a supplier, of that infrastructure. Placing it in a Framework 7 tier would contradict the human-owned framework, so `outside` (Adjacent) is the honest-verdict-correct designation.

**Layer 2** is the closest Framework 2 analog: `frameworks.md` maps grid utilities to Layer 2 (irreplaceable infrastructure). CEG owns the scarce, irreplaceable nuclear fleet — but is a **competitive merchant generator, not a regulated rate-base utility**, so the Layer 2 placement carries a competitive-not-regulated nuance (merchant price exposure + premium PPAs rather than a regulated return).

**`frameworks.md` revision flag (for a future codification session, not this session):** CEG is the first primary power *generator* ingested. The current framework only lists it as "Adjacent," with no dedicated tier and an imperfect Layer-2 mapping (regulated-utility analog applied to a merchant generator). Whether to add an explicit "Power Generation" tier / sub-framework — and how to treat competitive vs regulated generators — is raised here per Section 1.1 (framework-divergence raised on the page, not silently reconciled). `frameworks.md` + `_thesis.md` are human-owned and were not edited.

## Cross-vault adjacency

| Vault entity | Adjacency | Substantiation |
|---|---|---|
| [[CCJ]] (Cameco) | Upstream uranium + reactor-design (Westinghouse) → CEG downstream nuclear-fleet operator | CCJ tracked Microsoft-Constellation TMI/Crane + Meta-Constellation Clinton PPAs counterparty-side (A1 reciprocal-confirmation); **now bilaterally confirmed at CEG primary** (Crane 835 MW Microsoft). CEG is a Westinghouse AP1000-licensee-adjacent operator. |
| [[GEV]] (GE Vernova) | Gas-turbine / grid-equipment supplier; nuclear-deal non-participant | GEV primary sources note Microsoft-Constellation / Meta nuclear PPAs as deals GEV does NOT participate in; CEG is the operator in those deals. Partial overlap: CEG's gas peakers + Calpine gas fleet are turbine demand. |
| [[HALEU-fuel-chokepoint]] | Downstream reactor-licensee demand for nuclear fuel | CEG operates the TMI/Crane + Clinton reactors named in the hyperscaler-PPA reactor-licensee list. |
| [[BTM-grid-bypass-workaround]] | Firm clean baseload + powered-land / co-location as grid-bypass-adjacent | CEG's Crane firm-clean PPA + Texas powered-land (CyrusOne Freestone) + curtailable co-location are the generation-side of the behind-the-meter / grid-bypass dynamic. |
| [[ETN]] / [[VRT]] (Framework 7 Tier 1) | Infrastructure vs generation distinction | ETN/VRT supply the datacenter-power infrastructure CEG's load customers need; CEG generates the power — the Adjacent vs Tier 1 boundary. |
| [[AI-demand-durability]] | Generation-side demand signal | Hyperscaler demand "not slowed"; 2026 spending +75% YoY; 400k+ MW ERCOT queue. |

## Open questions

1. **Crane (TMI Unit 1) restart + FERC capacity credit.** The restart timeline depends on FERC approving the Eddystone→Crane CIR transfer (response expected June-July 2026) and on shortening the transmission-interconnection timeline. Track full-capacity-credit outcome + restart date (vs the prior 2031 connection reference management wants moved up).
2. **Calpine integration + 50M-share lockup dilution.** 25M shares unlock June 30, 2026; 25M June 30, 2027. Track whether owners sell (dilution) and whether CEG executes a buyback "around the lockup." Also track realized ~$2/share accretion + gas-fleet integration.
3. **PJM/FERC large-load co-location outcome.** PJM targets a FERC submission June 2026; implementation date 2029 (CEG pushing earlier). The market-design outcome gates how quickly hyperscaler co-location/PPA transactions convert. Track the FERC order + co-location implementation date.
4. **Merchant power-price exposure.** Analysts flagged weak ERCOT/PJM forwards despite strong pipeline demand (load "isn't yet on the system"). CEG argues forwards undervalue 2028-2029+ but is hedged near-term. Track forward-curve realization vs the >20% base EPS growth guide.
5. **Energy/Power framework placement resolution.** Whether `frameworks.md` should add an explicit "Power Generation" tier (and how to treat competitive vs regulated generators) now that a primary generator is in-vault — a human-owned codification decision. Revisit if a second primary generator (VST / NRG) is ingested.
6. **Nuclear PTC durability + fleet capacity factor.** Base EPS growth is anchored on the inflation-indexed nuclear production tax credit; track PTC policy durability + the fleet capacity factor (92.3% Q1 2026, incl. heavier planned outages).

## Source audit notes

### CEG Q1 FY2026 earnings call (Tier 2; May 11, 2026)

CEO Joseph Dominguez + CFO Shane Smith; relatively brief prepared remarks (an investor business update had been held ~a month prior). Tone confident; heavily focused on PJM/FERC large-load regulatory clarity (Dominguez has "[done] this 20-plus years with PJM" and sees "unprecedented" speed). Notable honest framing: management declined to project a new-vs-existing capacity ratio ("a fool's errand"), and addressed the Crane timeline candidly (plant "won't start sooner"; the question is full capacity credit). The competitive-vs-regulated distinction was made explicitly. No combative exchange surfaced (CEO combativeness convention count unchanged). Merchant-price weakness in forwards was acknowledged, not deflected.

### CEG Q1 FY2026 10-Q (Tier 1; period-end March 31, 2026)

First Calpine-consolidated quarter — operating revenues $11,122M (vs $6,788M Q1 2025); the step-up is largely Calpine. Crane Clean Energy Center defined (formerly TMI Unit 1); Geysers Power Co (geothermal) appears via Calpine. Five geographic segments retained.

### CEG FY2025 10-K (Tier 1; period-end December 31, 2025)

Pre-Calpine annual (Calpine = subsequent event, closed January 7, 2026). Operating revenues $25,533M (+8.3% YoY). Five geographic segments totaling 31,676 MW proportionate net capacity; ~55 GW combined fleet described in the business overview (incl. Calpine). Crane (Microsoft, 835 MW) datacenter PPA disclosed. No Tier 1/Tier 2 framing gap surfaced at first-canonical sampling scope.

## Change log

- **2026-05-29 (Session 107 — first-canonical creation):** Created from CEG FY2025 10-K (Tier 1; period-end December 31, 2025) + Q1 2026 10-Q (Tier 1; period-end March 31, 2026; first Calpine-consolidated quarter) + Q1 2026 earnings call (Tier 2; May 11, 2026). **First primary power *generator* in the vault.** Placement: `layer 2` (closest Framework 2 analog — irreplaceable infrastructure operator; competitive-merchant-not-regulated nuance) + `energy_power_tier outside` (**Adjacent — Power Generation** per `frameworks.md` v10.1; NOT a Framework 7 tier — generation ≠ datacenter-power-infrastructure) + photonics/equipment/materials outside (`memory_tier` omitted per Section 3.2(c)). Honest-verdict framing hosts the `_thesis.md` utility-skepticism (regulatory + execution risk confirmed by primary; "limited upside" critique partially refined by competitive-merchant status). **A1 reciprocal-confirmation:** the Microsoft-Constellation TMI/Crane (835 MW) + Meta-Constellation Clinton PPAs — previously tracked counterparty-side via [[CCJ]] — are now bilaterally confirmed at CEG primary. Key facts: FY2025 revenue $25.5B; Q1 2026 revenue $11.1B (Calpine-consolidated); adj-op EPS $2.74, FY2026 guide $11-12; Calpine closed Jan 7 2026 (~$2/share accretion; 50M shares issued, lockups June 2026/2027; ~55 GW combined fleet); FCF $8.4B (2026-2027) → $11.5-13B (2028-2029); $5B buyback + 10% dividend growth. **`frameworks.md` Power-Generation-tier revision flagged** (human-owned; not edited this session). Cross-vault inbound links from [[CCJ]] / [[GEV]] / [[HALEU-fuel-chokepoint]] / [[BTM-grid-bypass-workaround]] + [[AI-demand-durability]] data point.
