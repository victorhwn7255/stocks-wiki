---
type: chokepoint
tickers: [LITE, COHR, NVDA, AAOI, FN]
last_updated: 2026-04-27
---

# Datacenter Laser Supply

## The chokepoint dynamic

Datacenter laser supply for next-generation optical interconnect — particularly co-packaged optics (CPO) and ultra-high-speed transceivers — exhibits chokepoint characteristics at the component layer. This designation is substantiated by independent cross-validation from two competing suppliers ([[LITE]] and [[COHR]]) reporting consistent supply-demand dynamics, capacity constraints, and customer investment patterns across the same quarter (Q2 FY2026, reported February 3-4, 2026).

**Indium phosphide wafer fabrication scarcity.** InP wafer fabs are capital-intensive, technically specialized facilities with multi-year build-out timelines. Both major datacenter laser suppliers report fully allocated InP capacity:
- [[LITE]]: InP wafer fab "fully allocated" with front-loaded 40% capacity expansion on three-inch wafers (LITE Q2 FY2026 call)
- [[COHR]]: Plan to double InP capacity by end of calendar 2026 on six-inch wafers, with wafer starts at 80% of target and "ahead of schedule" — yet Anderson states demand absorbs all new capacity "and then some" (COHR Q2 FY2026 call)

The two companies operate at different manufacturing scales (COHR claims to be "the world's only producer of six-inch indium phosphide," yielding >4x chips at <50% cost vs three-inch; COHR Q2 FY2026 call), yet both report the same fundamental constraint: demand growth exceeds capacity expansion.

**Supply-demand imbalance confirmed industry-wide.** The key analytical question from Session 4 — whether the constraint was LITE-specific or structural — is resolved:
- LITE: under-shipping customer demand by approximately 25-30% (LITE Q2 FY2026 call)
- COHR: "I don't foresee the supply-demand getting back in balance this calendar year. I don't think it happens next calendar year. And if the forecast that we're seeing from customers for indium phosphide laser supply that they need for scale up, I think we could be in a very sustained, long period of supply-demand imbalance on indium phosphide" — Anderson (COHR Q2 FY2026 call)
- COHR: book-to-bill exceeded 4x in datacenter (COHR Q2 FY2026 call)

Thomas O'Malley (Barclays) directly cross-validated on the COHR call: "Your competitor talked about 40% increases [in InP capacity]... Are we still in a position where the industry is short?" Anderson confirmed the industry remains short. This is the first primary-source cross-validation of competing supplier claims in the vault.

**UHP laser technical moat.** Both suppliers describe performance thresholds that narrow the competitive field for CPO-grade lasers:
- LITE: 400mW UHP CW lasers described as "not something that many people can do" — Hurlston (LITE Q2 FY2026 call)
- COHR: "new high-power CW laser" subject to "exceptionally large purchase order" for CPO (COHR Q2 FY2026 call)

**Capacity allocation under constraint.** Both suppliers report demand rationing characteristic of structural chokepoints:
- LITE: all EML capacity spoken for through calendar 2027 via long-term agreements (LITE Q2 FY2026 call)
- COHR: bookings extending into calendar 2027, forecasts to calendar 2028 (COHR Q2 FY2026 call)
- Both companies disclosed customer investment/capital commitment negotiations one month before the March 2, 2026 NVDA $2B investments were announced

**Strategic investment as chokepoint signal.** [[NVDA]]'s $2B equity investment in each of LITE and COHR ($4B total, March 2, 2026) is the strongest evidence that the Layer 1 platform definer perceives laser supply as constrained enough to warrant vertical securing. When the platform definer invests $4B across two suppliers to secure access to a component, the component is functioning as a chokepoint.

**Platform-side demand confirmation (GTC March 16, 2026).** Jensen disclosed CPO products in production — Spectrum-X CPO switch, Spectrum-6 "world's first co-packaged optical" switch — and stated NVDA needs "a lot more capacity for CPO" (NVDA GTC March 16, 2026). This is the first platform-definer production confirmation of CPO demand, advancing the demand signal from investment inference ($4B equity) to disclosed production status. The chokepoint's relevance is reinforced: if the Layer 1 platform definer has CPO products in production and describes capacity as insufficient, the laser supply constraint is not theoretical.

## Evidence from LITE sources

**Capacity constraints (Q2 FY2026 call):**
- InP wafer fab fully allocated, 40% expansion front-loaded (three-inch wafers)
- Supply-demand imbalance ~25-30%
- All EML capacity spoken for through calendar 2027
- "Active negotiations with leading customers to offset our capital requirements in exchange for long-term supply assurances" — Hurlston

**CPO-specific evidence (Q2 FY2026 call):**
- Multi-hundred-million-dollar purchase order for UHP lasers supporting CPO/optical scale-out
- Material UHP chip shipment inflection H2 2026
- First scale-up CPO deployments expected late calendar 2027
- ELS modules providing ~2-2.5x content gain vs. standalone lasers
- 400mW UHP competitive moat

**Capital investment trajectory (10-K + 10-Q):**
- Capex: $128.5M (FY2023) → $133.0M (FY2024) → $231.0M (FY2025) → ~$320M annualized (H1 FY2026)
- Free cash flow approximately $24.8M for H1 FY2026 — capex consuming nearly all operating cash flow

## Evidence from COHR sources

**Capacity constraints (Q2 FY2026 call):**
- InP capacity doubling by end of calendar 2026 (six-inch wafers, Sherman TX and Järfälla Sweden)
- Quadrupled wafer starts September to December quarter, at 80% of target, "ahead of schedule"
- Despite aggressive ramp, demand absorbs all new capacity "and then some"
- Supply-demand imbalance projected through at least calendar 2027, possibly longer
- Book-to-bill >4x in datacenter

**CPO-specific evidence (Q2 FY2026 call):**
- "Exceptionally large purchase order" for CPO solution with new high-power CW laser
- Scale-out CPO arriving first; scale-up CPO "orders of magnitude larger" — Anderson
- Scale-up timeline: "not years out" — potentially more aggressive than LITE's late 2027
- **Scale-up bandwidth multiplier (per /raw/research/silicon-photonics-primer.md, citing OIF Compute Optics Interface white paper):** OIF modeling shows scale-up links in some common AI cluster architectures require approximately 9x the bandwidth capacity of scale-out links and are additionally tail-latency sensitive (corrupted requests can trigger retransmissions that stall new transfers). Anderson's "orders of magnitude" framing is topology-dependent, but the directional claim that scale-up optical content substantially exceeds scale-out is engineering-grounded.
- Both InP-based and VCSEL-based CPO/MPO solutions
- "Very active engagement and design win progress on scale up, on CPO"

**Capital investment trajectory (10-K + 10-Q):**
- Networking capex tripled: $91M (FY2024) → $263M (FY2025)
- Total capex: $441M (FY2025), H1 FY2026 $258M (annualizing ~$516M)
- Inventory build: +$410M (+29%) in six months — building ahead of demand
- "Long-term supply agreements signed or in process," with "financial commitment from customers, like investment for CapEx"

## What the cross-validation shows

The LITE-COHR comparison across the same quarter produces three structural findings:

**1. The constraint is industry-wide, not company-specific.** Both the smaller specialist (LITE, $665M quarterly revenue) and the larger diversified player (COHR, $1,686M quarterly) report the same fundamental dynamic: demand exceeds supply, capacity expansion is being absorbed, and the imbalance extends through at least 2027. This eliminates the hypothesis that LITE's constraint reflected under-investment or integration challenges specific to one company.

**2. Capacity expansion does not resolve the chokepoint.** LITE is expanding InP 40% on three-inch wafers. COHR is doubling capacity on six-inch wafers (>4x chips per wafer, <50% unit cost). Combined, this represents a massive capacity increase — yet both CEOs project continued supply shortage. The demand growth rate from AI datacenter interconnect exceeds even aggressive capacity expansion.

**3. The chokepoint attracted $4B in strategic investment.** [[NVDA]]'s parallel investments in both suppliers ($2B each, March 2, 2026) are a revealed-preference confirmation. Both LITE and COHR disclosed customer investment negotiations one month before the NVDA announcement — LITE emphasizing capital constraint relief, COHR emphasizing demand-side commitment. The platform definer acted on the same supply constraint that both suppliers describe.

## Decomposed chokepoint layers

The "datacenter laser supply" chokepoint is not a single bottleneck but a sequence of four progressively narrower constraints (per /raw/research/silicon-photonics-primer.md, citing OIF Co-Packaging Framework, Lumentum CLEO 2022, and Semiconductor Engineering June 2025):

**Layer 1: InP substrate and epitaxial capability.** Growing single-crystal InP at wafer scale with acceptable defect density, uniformity, and mechanical quality. Both [[LITE]] (three-inch, 40% expansion) and [[COHR]] (six-inch, capacity doubling) report this as fully allocated. The substrate layer is not a single-vendor bottleneck — Sumitomo, AXT, IQE, and JX Advanced Metals all participate in InP substrate supply (per /raw/research/silicon-photonics-primer.md, citing Sumitomo technical reviews, AXT 2020 results, and IQE 2024 expansion release) — but total industry substrate capacity constrains downstream device production. The upstream substrate-level supply dynamics, including [[AXTI]]'s capacity expansion and geopolitical export control risks, are now tracked at [[InP-supply]].

**Layer 2: High-power CW laser device capability.** Fabricating qualified UHP lasers at 400mW-class output with acceptable linewidth (<500 kHz), RIN (<-145 dB/Hz), thermal stability, and power-conversion efficiency (>10% PCE target). This is a narrower bottleneck than substrate supply: many firms can make InP substrates, fewer can process them into qualified 400mW CW devices. LITE describes this as "not something that many people can do" (LITE Q2 FY2026 call). The recurring engineering challenges are extracting enough optical power without catastrophic thermal rollover, preserving single-mode behavior and linewidth, maintaining conversion efficiency, and surviving qualification at elevated temperature (per /raw/research/silicon-photonics-primer.md, citing Lumentum CLEO 2022 and Coherent 400mW release).

**Layer 3: Laser/ELS packaging and qualification.** Assembling qualified UHP devices into external light source modules (ELSFP or mid-board form factors) that reliably feed multiple silicon photonic engines from a shared source. ELS modules provide ~2-2.5x content gain versus standalone lasers (LITE Q2 FY2026 call), but packaging a shared optical power plant involves fiber coupling, polarization management, thermal interface engineering, and reliability screening at standards more demanding than individual device specs.

**Layer 4: CPO package integration and optical test.** Integrating the optical engine and fiber-attach structures into the same package neighborhood as a hot compute or switch ASIC, with sub-micron alignment tolerances, thermal drift management (~0.1 nm/°C wavelength shift in photonic systems), and test strategies covering both electronic and optical path behaviors. This layer involves advanced packaging foundries and OSATs as much as optics vendors (per /raw/research/silicon-photonics-primer.md, citing Semiconductor Engineering June 2025 and OIF Co-Packaging Framework).

**Why the decomposition matters analytically.** The cross-validated chokepoint evidence from [[LITE]] and [[COHR]] concentrates at layers 1-2 (substrate and device). Layers 3-4 (ELS packaging and CPO integration) are emerging constraints that will tighten as CPO moves from purchase orders to volume deployment. A system is not capacity-ready just because wafers and laser devices exist — the effective supply constraint may migrate downstream as CPO scales.

## Evidence from AAOI sources (integrator-side)

[[AAOI]] provides the first integrator-side (Layer 5) confirmation of the InP laser supply constraint, complementing the supplier-side evidence from [[LITE]] and [[COHR]] above.

**Laser shortage confirmed from customer perspective.** Thompson Lin (CEO): "huge issue of laser shortage... outside suppliers told us, we need to wait at least one year or even longer" to receive external laser supply (AAOI Q4 FY2025 call). This is the demand-side validation of the same constraint LITE and COHR describe from the supply side. When a transceiver assembler independently confirms that its external laser suppliers cannot deliver within a year, the structural nature of the shortage is cross-validated from a different position in the supply chain.

**Adaptive response: vertical integration as chokepoint workaround.** AAOI's decision to triple its own InP laser production by mid-2027 at Sugar Land, TX is a direct response to the chokepoint (AAOI Q4 FY2025 call). AAOI claims its dual MBE + MOCVD capability is "unique in our industry" at the transceiver assembler tier (AAOI 10-K FY2025). Management projects "more than 95% of laser will be AI laser" by end of year (AAOI Q4 FY2025 call). The vertical integration strategy is economically motivated by the chokepoint — when external supply is quoted at 1+ year lead times, building internal capacity becomes a competitive necessity rather than a strategic choice.

**The integrator-side evidence adds a third vantage point** to the chokepoint analysis. The supplier side ([[LITE]], [[COHR]]) reports demand exceeding supply. The platform definer ([[NVDA]]) invested $4B to secure access. Now the integrator side ([[AAOI]]) confirms the shortage from the customer perspective and is investing in self-supply as a workaround. The three-sided confirmation — supplier, platform, integrator — is the strongest form of chokepoint validation available in the vault.

## Evidence from FN sources (Layer 6 contract-manufacturer side)

[[FN]] adds a fourth vantage point to the chokepoint analysis: optical contract manufacturer perspective. Q2 FY2026 call disclosure (Seamus Grady, CEO) confirms EML laser supply constraint at the manufacturing-input level, with resolution path materializing during the quarter:

> "We have been ... supply-constrained in our Datacom, particularly on the leading-edge products, the 200 Gb per lane, both 800 Gb and 1.6 Tb. Demand continues to outstrip supply, and we continue to ship significant volumes to our main customer. But of course, we could ship more if we had more components. We did get approval for a second source for the EML for the laser, which has been the main cause of the supply constraints. So we were able to get a second source. Our customer was able to approve a second source for the laser during the quarter, and that should benefit us this quarter and in future quarters." (FN Q2 FY2026 call, response to Karl Ackerman, BNP Paribas)

Three observations from the contract-manufacturer vantage point:

1. **EML supply constraint at 200 Gb/lane (800G + 1.6T transceivers) was binding.** Datacom -7% YoY in [[FN]] Q2 FY2026 was supply-side, not demand-weak. Demand continued to outstrip supply for leading-edge products.
2. **Second-source qualification path is real.** Customer approved second EML source during Q2 FY2026 — bottleneck resolution path materializing. Supply-demand imbalance trajectory may shift as second-source qualification expands.
3. **Layer 6 contract manufacturer captures the binding-component view.** [[FN]] sees EML laser supply at the assembly-input level (laser components going into transceiver modules); the binding constraint expressed in [[LITE]]/[[COHR]] supplier-side narrative materializes as component-availability gating at the contract-manufacturer assembly stage.

The four-vantage-point chokepoint validation now spans: supplier ([[LITE]], [[COHR]] supply-side narrative), platform ([[NVDA]] $4B equity investment), integrator ([[AAOI]] customer-side shortage + vertical integration workaround), and contract manufacturer ([[FN]] component-availability binding constraint with second-source resolution path). Strongest cross-vantage chokepoint validation in vault.

## Remaining uncertainties

The cross-validation substantiates the chokepoint but does not eliminate all uncertainty:

- **Both suppliers have incentives to emphasize scarcity.** Supply constraints support pricing power, justify customer investment, and signal competitive moats. The convergence of their testimony is strong evidence but is colored by aligned incentives.
- **Hyperscaler in-housing remains a structural threat.** "We may fail to accurately estimate our competitors' or our customers' willingness and capability to backward integrate" (COHR 10-K FY2025). Neither LITE nor COHR can rule out hyperscalers developing internal laser capability.
- **CPO timeline slippage could defer the chokepoint's peak relevance.** If CPO deployment stalls beyond 2028, the UHP laser demand driver weakens. LITE targets late 2027 scale-up; COHR says "not years out" — both are management projections, not confirmed deployments.
- **New entrants or technology disruptions.** On-chip light sources that eliminate external laser supply are technically distant but theoretically possible. New InP wafer fab entrants could dilute structural scarcity, though the capital requirements and multi-year ramp timelines provide a moat.

## Cross-references

- [[LITE]] — first source company; three-inch InP, 40% expansion, $2B NVDA investment
- [[COHR]] — cross-validation source; six-inch InP device-fabrication advantage, capacity doubling, $2B NVDA investment
- [[NVDA]] — $4B combined investment as chokepoint-signaling action
- [[NVDA-platform-integration]] — the LITE and COHR investments as equity+purchase modality
- [[AAOI]] — integrator-side confirmation; laser shortage from customer perspective, vertical integration as adaptive response
- [[FN]] — contract-manufacturer-side confirmation; EML supply constraint binding at 200 Gb/lane; customer-approved second-source qualification path materializing Q2 FY2026
- [[CPO-platform-battle]] — the chokepoint's relevance depends on CPO adoption trajectory
- [[datacenter-photonics-supply-chain]] — Section 2.1 places the laser layer within the cross-cutting supply-chain map; Bucket B in the investability framing covers the optical device stack
- [[chokepoint-investability-priorities]] — Tier 3-anchored vault-canonical reference for 13-chokepoint photonics framework (created Session 25, A2 first canonical application). Chokepoint 1 (Lasers / EMLs / III-V devices) cross-references this page for cross-validated supplier-side scarcity dynamics (LITE + COHR same-quarter testimony; NVDA $4B equity confirmation).

## Change log

- **2026-04-19:** Created from LITE sources (10-K FY2025, 10-Q Q2 FY2026, Q2 FY2026 call). Provisional single-source chokepoint page.
- **2026-04-19:** Promoted from provisional to substantiated. COHR sources (10-K FY2025, 10-Q Q2 FY2026, Q2 FY2026 call) independently confirm industry-wide supply-demand imbalance through at least 2027. Provisional disclaimer removed. COHR evidence section added. Cross-validation analysis section added. "Confirm/weaken" section replaced with "Remaining uncertainties" reflecting substantiated status.
- **2026-04-20:** Updated from Tier 3 research (/raw/research/silicon-photonics-primer.md). Added decomposed chokepoint layers section (four sequential bottlenecks: InP substrate/epi → CW laser device → ELS packaging → CPO integration). Added OIF-grounded scale-up bandwidth multiplier (~9x scale-out in some architectures). Substrate layer competition (Sumitomo, AXT, IQE, JX Advanced Metals) noted — bottleneck narrows at each layer.
- **2026-04-20:** Updated from AAOI (10-K FY2025, Q4 FY2025 call). Added integrator-side evidence section — first Layer 5 confirmation of laser shortage from customer perspective. Thompson Lin: "huge issue of laser shortage," external suppliers quoting 1+ year. AAOI tripling internal InP laser production as adaptive response. Three-sided chokepoint validation now complete: supplier (LITE, COHR), platform (NVDA $4B investment), integrator (AAOI shortage confirmation).
- **2026-04-23:** Session 13 cross-reference. Added [[InP-supply]] boundary clarification in decomposed chokepoint Layer 1 (substrate). Substrate-level dynamics now tracked separately from device-level chokepoint.
- **2026-04-26:** Updated from NVDA GTC March 16, 2026 keynote (Tier 2). Platform-side demand confirmation added: Jensen disclosed CPO in production with capacity demand signal ("a lot more capacity for CPO"). Chokepoint relevance reinforced from platform-definer production status.
- **2026-04-27:** Session 19 cross-reference. Added [[datacenter-photonics-supply-chain]] link in Cross-references.
- **2026-04-27 (Session 21):** Added FN sources section — fourth vantage point on chokepoint validation (Layer 6 contract-manufacturer perspective). EML supply constraint at 200 Gb/lane (800G + 1.6T transceivers) confirmed from FN assembly-input view; customer-approved second-source qualification path materializing Q2 FY2026. Four-vantage-point validation now spans supplier ([[LITE]], [[COHR]]), platform ([[NVDA]]), integrator ([[AAOI]]), and contract manufacturer ([[FN]]). [[FN]] added to tickers and Cross-references.
- **2026-04-27 (Session 25):** Added Cross-reference to [[chokepoint-investability-priorities]] new theme page (A2 first canonical application). Page content unchanged.
- **2026-04-30 (Session 32 cross-reference — [[cpo-integration]] chokepoint page creation):** Cross-referenced from new chokepoint page [[cpo-integration]] (fourth canonical multi-source-synthesis chokepoint page in vault history; closes Tier 3 framework Chokepoint 10 dedicated chokepoint page coverage gap). External Laser Source (ELS) architecture documented in [[cpo-integration]] CPO integration mechanics section as the structural mechanism by which Layer 4 component suppliers retain value through CPO transition. UHP CW laser supply for ELS architecture cross-referenced from LITE 400mW UHP positioning + COHR new high-power CW laser purchase order + AAOI in-house InP/GaAs laser fabrication subsections in [[cpo-integration]]. NVDA $2B equity-plus-purchase modality (March 2026 LITE+COHR; capital-offset-for-supply-assurance framing per Session 22 [[NVDA-platform-integration]] codification) documented in [[cpo-integration]] Value chain shift dynamics + per-company integration positioning sections. Adjacent chokepoint dependency documented in [[cpo-integration]] Cross-chokepoint dependencies section: UHP CW lasers for ELS architecture; InP substrate constraint extends through 2027 per Session 5 cross-validation. No content edits to this chokepoint page.
- **2026-04-30 (Session 33 cross-reference — [[InP-supply]] provisional → canonical promotion):** Adjacent chokepoint page [[InP-supply]] promoted from provisional to canonical multi-source-synthesis chokepoint page via Option C bifurcation handling — single page covers Tier 3 framework Chokepoint 3 (InP substrate supply) + Chokepoint 4 (InP epitaxial capacity) with internal subsection structure. **Fifth canonical multi-source-synthesis chokepoint page in vault history** (after [[optical-dsp-phy-supply]] Session 30, [[advanced-optical-packaging]] Session 31, [[cpo-integration]] Session 32). InP supply chain feeds laser-device fabrication directly: substrate-tier (AXTI Beijing) + epitaxial-tier equipment (VECO Lumina+ MOCVD; Aixtron) + epitaxial-tier device-fabrication (COHR six-inch advantage; LITE three-inch industry-standard; AAOI Sugar Land MBE+MOCVD) all feed laser supply documented at this chokepoint page. EML laser supply constraint at 200 Gb/lane (Session 21 cross-validation) interlocked with InP substrate + epitaxial capacity scaling. No content edits to this chokepoint page.
