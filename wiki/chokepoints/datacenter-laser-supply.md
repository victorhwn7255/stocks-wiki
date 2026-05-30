---
type: chokepoint
tickers: [LITE, COHR, NVDA, AAOI, FN, SIVE]
last_updated: 2026-05-29
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

**Strategic investment as chokepoint signal.** [[NVDA]]'s $2B equity investment in each of LITE and COHR ($4B total, March 2, 2026) is the strongest evidence that the Layer 1 platform definer perceives laser supply as constrained enough to warrant vertical securing. When the platform definer invests $4B across two suppliers to secure access to a component, the component is functioning as a chokepoint. **Materialization at primary substantiated post-S50 Q3 FY2026 paired refresh (2026-05-10)** — see NVDA $2B equity-plus-purchase materialization at LITE+COHR section below for $2.02B cash injection at LITE + COHR $2B equity + multibillion-dollar multi-year CPO supply through end of decade per CEO Anderson Q3 call.

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

## Evidence from SIVE sources (merchant new-entrant / challenger vantage point)

[[SIVE]] (Sivers Semiconductors; S100) adds a fifth vantage point: the merchant new-entrant trying to enter the CW laser supply layer. It confirms the shortage narrative from the aspirant side, and — by its own pre-revenue fragility — illustrates the entry barrier this page's Remaining-uncertainties section names ("capital requirements and multi-year ramp timelines provide a moat").

**Shortage confirmed from the challenger side.** SIVE expects "a CW laser supply shortage in the next few years as the industry transitions from 800G to 1.6T and eventually to 3.2T" (Sivers Annual Report FY2025). It is sampling CW DFB lasers to "several pluggable transceiver manufacturers worldwide" (scale-out) and CW DFB laser arrays (scale-up), and expects "a subset" to commit to production "in 2027 and beyond." This is a fourth independent angle on the shortage — from a supplier trying to enter, distinct from incumbent ([[LITE]]/[[COHR]]), integrator ([[AAOI]]), and contract-manufacturer ([[FN]]) vantages.

**Entry barrier illustrated.** SIVE's AIDC laser revenue is zero today; production readiness is targeted end-2026, revenue 2027+. It is sub-scale (photonics ~$9M FY2025), carries a going-concern material uncertainty, and depends on an external foundry (WIN Semiconductors) plus its own Glasgow fab for capacity. Its external-light-source push runs through CPO partners POET, O-Net, and Ayar Labs (all SIVE-side disclosed; not bilaterally confirmed). The contrast with NVDA's $4B capital injection into [[LITE]]+[[COHR]] is the point: the platform definer pre-funds incumbent capacity, while a merchant challenger must self-finance a multi-year qualification ramp through serial dilution. Whether SIVE reaches production before incumbent capacity expansion + integrator vertical integration ([[AAOI]]) absorb the shortage is the open test of the new-entrant path.

## NVDA $2B equity-plus-purchase materialization at LITE+COHR (S50 NEW analytical product propagation)

**Single most material change driver since chokepoint creation.** Per [[LITE]] + [[COHR]] paired refresh S50 (2026-05-10) — NVDA $2B equity investment announcements (March 2, 2026) materialized at primary at Q3 FY2026 reporting cycle. Capital-offset-for-supply-assurance modality fully substantiated; investee uses capital to fund capacity expansion that customer requires; investor secures supply access ahead of capacity-binding-constraint dynamics. **First reciprocal-confirmation A1 mode materialization at NVDA architect-customer commitment scope** per [[nvidia-supply-chain-commitments]] S53 cross-vault relationship page.

### LITE — $2.02B cash injection materialization

CFO Wajid Ali Q3 call disclosure: *"cash and short-term investments increased by $2.02 billion to $3.17 billion, with the increase primarily driven by NVIDIA's direct investment in Lumentum."* H1 FY2026 free cash flow ~$24.8M against ~$320M annualized capex pre-injection — **investment effectively pre-funds ~6 years of standalone capex at H1 run-rate**. Capital-binding-constraint relief substantiated at supplier-side.

**Capacity expansion materialization at LITE post-S50:**
- **Greensboro NC 5th InP fab** announced; capacity expansion alignment with NVDA partnership
- **Google explicit named at LITE** at S50 primary — broadens customer-naming pattern beyond NVDA
- LITE three-inch InP industry-standard manufacturing baseline preserved per S5 cross-validation; 40% capacity expansion target front-loaded

### COHR — $2B equity + multibillion-dollar multi-year CPO supply through end of decade

CEO Anderson Q3 call disclosure: *"$2 billion equity investment in Coherent and a multi-year supply agreement extending through the end of the decade"* + *"a multibillion-dollar agreement that extends out through the end of the decade. Importantly, it's multiple different CPO solutions"* — covers high-power CW laser + ELS module + Fiber Array Unit + polarization-maintaining fiber + isolators + thermoelectric coolers; **Sherman TX 6-inch InP CW laser production explicitly tied to NVDA partnership**. Cash $1.5B → $3.0B sequential (+$1.5B net of $290M Q3 CapEx + $162M debt repayment). Anderson framing: *"an expansion of a more than 20-year relationship."*

**Capacity expansion materialization at COHR post-S50:**
- **6-inch InP Zürich 3rd site** added (beyond Sherman TX + Järfälla Sweden baseline per S5)
- **First 6-inch transceiver shipments** at S50 primary baseline
- **Multi-Rail + Thermadite XPU cooling NEW segments** at COHR adjacent-scope
- COHR claims "world's only producer of six-inch indium phosphide" preserved per S5 cross-validation

### Differential structural commitment substantiation per Section 3.3 rhetorical-vs-factual

**Equity-only confirmation at LITE; dual-leg equity + supply commitment at COHR.** Differential structural commitment between the two photonics laser suppliers despite identical $2B equity headline. COHR commercial commitment scope (multibillion-dollar multi-year CPO supply through end of decade) extends beyond LITE equity-only scope per S50 primary verification. Cross-vault [[NVDA-platform-integration]] six-modality framework: equity-plus-purchase modality at LITE; equity + multi-year supply agreement modality at COHR — distinct sub-modality classification.

### Chokepoint validation reinforcement post-S50

The chokepoint dynamic strengthens post-S50: NVDA's investment is no longer announcement-only but materialized at primary with capital deployment + commercial commitment scope quantified. **CPO supercycle thesis substantive validation** at supplier-tier vault canonical. Capacity expansion alignment (LITE Greensboro + COHR Zürich + Sherman TX 6-inch tied to NVDA partnership) demonstrates the platform definer is actively pre-funding chokepoint capacity expansion rather than merely securing equity stake passively. **The chokepoint is functioning as architected dependency** — NVDA recognizes supply constraint, materializes capital to relieve constraint, secures supply access via commercial commitment.

## VECO equipment-tier substrate rerating (S58 NEW analytical product propagation)

**Equipment-tier leading-indicator for InP substrate capacity expansion trajectory** per [[VECO]] S58 refresh (2026-05-12) — adjacent to Layer 1 + Layer 2 of decomposed chokepoint layers (substrate + epitaxial process equipment feeds laser device fabrication).

### Substantive S58 refresh content

- **$250M+ multi-customer indium phosphide laser orders** at VECO primary — Lumina MOCVD + WaferStorm wet processing + Spector IBD; delivery 2026-2027 acceleration
- **Spector IBD capacity expansion 10X from base** per S58 baseline
- **InP laser SAM $700M by 2030 + $2B growth opportunity framing** per S58 baseline
- **Tier 1 logic LSA + HBM supplier production tool of record substantiation** per S58 baseline
- **First explicit NVIDIA reference at VECO primary** at S58 — counterparty-attribution-only A1 mode at **downstream-ecosystem-reference scope** (distinct from architect-customer modality at LITE/COHR S50)
- **Compound Semi FY2026 RAISED to ~50% growth** (vs prior +33% baseline)
- **Axcelis merger close H2 2026 pending** (China antitrust approval; all other approvals received + shareholders of both companies approved)

### Implication for laser supply chokepoint

VECO MOCVD equipment + WaferStorm wet processing + Spector IBD = upstream equipment for InP substrate epitaxial process → laser device fabrication. **Equipment-tier substrate rerating substantiates upstream Layer 1 of decomposed chokepoint** — InP substrate capacity expansion trajectory at supplier-side (LITE + COHR) is downstream of VECO equipment delivery cycle. $250M+ multi-customer orders + 10X Spector IBD expansion = **leading indicator for 2026-2027 InP substrate capacity expansion materialization**.

**Cross-vault [[InP-supply]] S33 chokepoint refresh propagation candidate** flagged per Open questions section below. VECO equipment-tier substrate rerating is more substantively elevated at [[InP-supply]] scope (substrate-tier + epitaxial-tier unified Option C bifurcation) than at this chokepoint (laser device-tier scope); cross-reference framing preserved.

## TSEM SiPh PDK foundry InP modulator integration adjacency (S62 NEW analytical product propagation)

**SiPh PDK foundry adjacency at laser-device-tier scope** per [[TSEM]] S62 canonical placement (2026-05-14). TSEM PH18DA (200mm) silicon photonics platform enables heterogeneous integration of InP modulators + InP lasers into SiPho chips at wafer-tier foundry scope.

### Substantive TSEM-side InP integration disclosures (Q1 2026 call prepared remarks)

- **Coherent 400 Gb per lane all-silicon Mach-Zehnder modulator long-term contract** at TSEM PH18DA — Ellwanger: *"one of our customers having signed a high volume long-term contract"* — **bilateral verification candidate at COHR-side** per next COHR refresh (Q4 FY2026 + FY2026 full-year release); pre-registered in Open questions section
- **OpenLight 400G InP electro-absorption modulator (EAM)** heterogeneously integrated on PH18DA platform
- **Scintil Photonics heterogeneous DWDM laser sources** designed for near package optics + CPO-based AI infrastructures
- **Salience Labs + Oriole Networks** silicon photonics optical circuit switches on PH18DA + heterogeneous InP optical amplifiers for AI data center scaling
- **TSEM 20-F FY2025 explicit:** "wafer-to-wafer bonding, lasers (including DWDM lasers), III-V modulators and TSVs, all embedded in the SiPho chip"; "a platform that embeds InP lasers in the SiPho chip"

### Implication for laser supply chokepoint

TSEM SiPh PDK foundry InP modulator integration adjacency is **distinct from supplier-tier laser device fabrication** (LITE + COHR scope) — TSEM operates at wafer-tier SiPh PDK foundry scope per S62 photonics_tier 2 placement; InP modulator + heterogeneously-integrated InP laser scope is downstream of InP substrate but **adjacent to standalone InP CW laser device fabrication** at chokepoint scope. Cross-reference for foundry-tier integration pathway; TSEM-side reference-design supplier complementarity into TSMC CoWoS per [[TSEM]] S62 + [[TSMC-CoWoS]] S65 refresh.

**Coherent partnership bilateral verification candidate** at COHR-side is most material new finding per S62 propagation — TSEM-side discloses Coherent as long-term contract partner at PH18DA all-silicon MZ modulator scope; COHR-side baseline (S5 + S50) does not explicitly cross-reference TSEM partnership. Pre-registered for next COHR refresh.

## MRVL coherent-DSP + scale-across demand vector (S102 propagation; S110)

[[MRVL]]'s Q1 FY2027 refresh added a **coherent / DCI demand vector** that amplifies laser-supply demand from a new direction — distinct from the supplier-tier (LITE/COHR), integrator (AAOI), and contract-manufacturer (FN) vantages above:

- **First 1.6T ZR/ZR+ DCI modules on a new 2nm coherent DSP**, plus coherent-light products for 2–20 km reach at 200G/lane (MRVL Q1 FY2027 call, per [[optical-dsp-phy-supply]]). Coherent DCI optics pull on the same InP CW-laser / EML supply base that 800G/1.6T datacom transceivers do.
- **"Scale-across" as a new demand axis.** MRVL formalized a scale-out / scale-up / **scale-across** trifurcation; scale-across (multi-datacenter AI clusters with >10× front-end DCI bandwidth) is a structurally new coherent-optics demand driver, with DCI on a line of sight to **~$1B annualized by FY2028** (MRVL Q1 FY2027 call). This is incremental demand on top of the intra-datacenter 800G/1.6T ramp the chokepoint already tracks.
- **Polariton modulator (cross-ref, lighter fit).** MRVL's Polariton acquisition (plasmonic modulator >1 THz, ~10× SiPh/TFLN bandwidth, 3.2T roadmap) is modulator-tier, adjacent to — not part of — the laser-device supply base; see [[advanced-optical-packaging]] + [[cpo-integration]] for the packaging/modulator-tier treatment. Noted here for device-tier adjacency only.

**Scope discipline:** MRVL is a coherent-DSP / DCI demand-side adjacency (it consumes and amplifies demand for coherent lasers), NOT a laser-device-tier supplier — following the VECO + TSEM precedent, MRVL is documented here but **not added to tickers** (Section 3.2(b) provenance; tickers preserve laser-device-tier substantiating sources). The scale-across vector reinforces the chokepoint's demand-side durability.

## Cross-vault NVIDIA partnership pattern at laser supply scope

**LITE + COHR are 2 of 4 Tier 1 reciprocal-confirmation participants** per [[nvidia-supply-chain-commitments]] S53 cross-vault relationship page (first relationship page in vault history). Cross-vault NVIDIA partnership pattern post-S64 = **4 Tier 1 + 7 Tier 2 substantiating sources**:

**Tier 1 reciprocal-confirmation at laser supply scope:**
- **[[LITE]]** — Equity injection modality ($2.02B cash; capital-offset-for-supply-assurance per CFO Wajid Ali Q3 call)
- **[[COHR]]** — Equity + multiyear CPO supply modality ($2B equity + multibillion-dollar multi-year supply through end of decade per CEO Anderson Q3 call)

**Tier 1 reciprocal-confirmation at adjacent scope (power infrastructure + thermal):**
- **[[ETN]]** — Beam Rubin DSX platform partnership (Energy/Power Tier 1)
- **[[VRT]]** — Strategic Partnership + EcoDataCenter Sweden Vera Rubin deployment (Energy/Power Tier 1)

**Modality distinction at laser supply scope vs broader pattern.** LITE + COHR equity-plus-purchase modality (NVDA capital deployment) is **structurally distinct** from:
- [[TSMC-CoWoS]] Tier 2 counterparty-attribution-only foundry-customer modality (per [[TSM]] S3 + S65 refresh)
- [[ALAB]] / [[CSCO]] / [[ANET]] Tier 2 ecosystem-partner counterparty-attribution-only modality
- [[FN]] Tier 2 contract-manufacturer customer-concentration modality (NVIDIA 27.6% top customer)

The laser supply chokepoint is **the strongest Tier 1 reciprocal-confirmation scope in vault** — both LITE + COHR vault canonical participants directly substantiate NVDA architect-customer commercial commitment at supplier-tier. First downstream propagation cycle test of [[nvidia-supply-chain-commitments]] S53 living document scaffolding at chokepoint scope.

## Remaining uncertainties

The cross-validation substantiates the chokepoint but does not eliminate all uncertainty:

- **Both suppliers have incentives to emphasize scarcity.** Supply constraints support pricing power, justify customer investment, and signal competitive moats. The convergence of their testimony is strong evidence but is colored by aligned incentives.
- **Hyperscaler in-housing remains a structural threat.** "We may fail to accurately estimate our competitors' or our customers' willingness and capability to backward integrate" (COHR 10-K FY2025). Neither LITE nor COHR can rule out hyperscalers developing internal laser capability.
- **CPO timeline slippage could defer the chokepoint's peak relevance.** If CPO deployment stalls beyond 2028, the UHP laser demand driver weakens. LITE targets late 2027 scale-up; COHR says "not years out" — both are management projections, not confirmed deployments.
- **New entrants or technology disruptions.** On-chip light sources that eliminate external laser supply are technically distant but theoretically possible. New InP wafer fab entrants could dilute structural scarcity, though the capital requirements and multi-year ramp timelines provide a moat.
- **VECO MOCVD equipment-tier rerating timeline durability.** S58 $250M+ multi-customer InP laser orders + InP laser SAM $700M by 2030 framing is forward-looking; equipment-tier capacity expansion translation to substrate-tier output materialization spans 2026-2027 cycle; rerating durability pending future VECO refresh + downstream InP-supply chokepoint refresh propagation.
- **TSEM SiPh PDK foundry capacity expansion trajectory.** S62 $1.3B 2027 contracted SiPh-only revenue + 5x SiPh capacity growth target by end-2026 is forward-looking; capacity materialization at TSEM PH18DA platform + InP modulator heterogeneous integration commercial scale dynamics pending future TSEM refresh.
- **Cross-vault [[nvidia-supply-chain-commitments]] living document scaffolding refresh propagation cadence.** S53 relationship page first downstream propagation cycle test at S66 chokepoint refresh; cadence durability + relationship-page-vs-chokepoint-page refresh propagation sequencing methodology pending future cross-vault refresh cycles.

## Open questions

1. **[[LITE]] Q4 FY2026 + FY2026 full-year refresh propagation (highest priority).** S50 Q3 FY2026 baseline (May 5, 2026 call) is ~10 sessions stale at S66 refresh. LITE Q4 FY2026 + FY2026 full-year release would: (a) verify Greensboro NC 5th InP fab capacity ramp trajectory; (b) verify NVDA $2.02B capital deployment trajectory; (c) verify 400mW UHP commercial scale ramp; (d) potentially surface additional hyperscaler engagement disclosures beyond NVDA + Google; (e) cross-vault refresh propagation trigger to this chokepoint per S51 [[HALEU-fuel-chokepoint]] precedent cadence.

2. **[[COHR]] Q4 FY2026 + FY2026 full-year refresh propagation.** S50 Q3 FY2026 baseline (May 6, 2026 call) is ~10 sessions stale. COHR refresh would: (a) verify Sherman TX 6-inch InP CW laser production capacity ramp tied to NVDA partnership; (b) **bilateral verification candidate at COHR-side for TSEM PH18DA Mach-Zehnder modulator long-term contract** per S62 [[TSEM]] disclosure; (c) verify Zürich 3rd 6-inch InP site capacity ramp trajectory; (d) verify multi-rail + Thermadite XPU cooling segment commercial scale.

3. **[[NVDA]] Q1 fiscal 2027 refresh bilateral verification.** Post-May 20, 2026 release. NVDA-side bilateral verification candidates accumulated: (a) LITE + COHR Tier 1 reciprocal-confirmation at NVDA architect-side primary; (b) Spectrum-X CPO production + Kyber CPO scale-up commercial scale trajectory; (c) Vera Rubin HBM4 16-die stack deployment trajectory; (d) potentially first explicit Google/Microsoft/Anthropic naming at NVDA primary scope.

4. **VECO Compound Semi FY2026 +50% growth trajectory validation.** S58 raised guidance to ~50% growth (vs prior +33% baseline); Spector IBD capacity expansion 10X from base materialization; Axcelis merger close H2 2026 pending China antitrust approval. Future VECO refresh cycle propagation to [[InP-supply]] S33 chokepoint primary; secondary propagation to this chokepoint at substrate-tier upstream scope.

5. **Sherman TX 6-inch InP capacity ramp trajectory + Greensboro NC 5th InP fab capacity ramp.** COHR Sherman TX 6-inch InP CW laser production explicitly tied to NVDA $2B partnership; LITE Greensboro NC 5th InP fab capacity expansion alignment with NVDA $2.02B capital deployment. Materialization trajectory at supplier-side capacity expansion cycle is single most important leading indicator for chokepoint moderation candidate; future LITE + COHR refresh propagation candidates.

6. **TSEM-COHR Mach-Zehnder modulator bilateral verification at COHR-side.** S62 TSEM PH18DA Ellwanger disclosure: Coherent 400 Gb per lane all-silicon Mach-Zehnder modulator long-term contract. COHR-side baseline (S5 + S50) does NOT explicitly cross-reference TSEM partnership at primary. Bilateral verification candidate at next COHR refresh.

7. **Hyperscaler in-housing risk monitoring per `_thesis.md` disconfirming signal.** Per current "Remaining uncertainties" section: "Silicon photonics startups get acquired into hyperscalers rather than merchant platform players." NVDA $2B equity-plus-purchase at LITE + COHR is **counter-evidence to vertical integration disconfirming signal** (NVDA secures merchant supplier access via capital injection rather than acquisition); future hyperscaler (Microsoft / Google / Amazon / Meta) potential vertical integration of laser supplier as falsification candidate. Track at next major NVDA refresh + hyperscaler 10-K filings.

8. **CPO timeline slippage candidates per cross-vault [[cpo-integration]] S32 refresh propagation.** [[cpo-integration]] S32 baseline ~17 sessions stale at S66; refresh propagation candidate per S51 + S65 cadence. NVDA GTC March 2026 Spectrum-X CPO production status + Murphy thesis validation candidates at next [[cpo-integration]] refresh. **Update (S110):** MRVL Q1 FY2027 evolved the scale-up/scale-out bifurcation into a **scale-out / scale-up / scale-across trifurcation** (DCI scale-across ~$1B FY2028); the scale-up CPO inflection remains the contested frontier (see MRVL coherent-DSP demand-vector section above).

9. **Adjacent chokepoint refresh propagation triggers** post-S65 [[TSMC-CoWoS]] + S66 this chokepoint refresh. [[InP-supply]] S33 (substrate-tier upstream; VECO equipment-tier rerating cross-reference) + [[cpo-integration]] S32 (CPO integration mechanics; LITE/COHR ELS architecture cross-reference) + [[advanced-optical-packaging]] S31 (packaging-tier; FN Raytec + TSEM SiPh PDK foundry adjacency) — all candidates for refresh propagation per S51 sequential cadence.

10. **Second-source EML qualification path expansion per FN Q2 FY2026 + future ingest validation.** Current page Section "Evidence from FN sources" documents customer-approved second EML source during Q2 FY2026 (resolution path materializing). Future FN refresh + cross-vault second-source qualification expansion would test whether supplier diversification beyond LITE + COHR is materializing at commercial scale.

11. **On-chip light source technology disruption monitoring.** Per current "Remaining uncertainties" section: on-chip light sources that eliminate external laser supply are technically distant but theoretically possible. New entrants (e.g., Lightmatter / Ayar Labs heterogeneous integration approaches) at SiPh PDK foundry scope (TSEM PH18DA platform per S62) could shift competitive landscape; monitor at future TSEM + cross-vault [[CPO-platform-battle]] refresh propagation.

12. **Cross-vault [[HBM-oligopoly]] paired chokepoint adjacency.** S64 [[HBM-oligopoly]] canonical creation + S65 [[TSMC-CoWoS]] paired chokepoint formalization (upstream-vs-integration tier pair). InP laser supply at this chokepoint feeds CPO integration → optical interconnect for AI accelerator packaging; HBM-CoWoS paired chokepoint serves same AI accelerator packaging dependency at distinct memory-tier scope. Cross-domain dependency chain monitoring per future cross-vault refresh cycles.

## Cross-references

- [[LITE]] — first source company; three-inch InP, 40% expansion, $2B NVDA investment
- [[COHR]] — cross-validation source; six-inch InP device-fabrication advantage, capacity doubling, $2B NVDA investment
- [[NVDA]] — $4B combined investment as chokepoint-signaling action
- [[NVDA-platform-integration]] — the LITE and COHR investments as equity+purchase modality
- [[AAOI]] — integrator-side confirmation; laser shortage from customer perspective, vertical integration as adaptive response
- [[FN]] — contract-manufacturer-side confirmation; EML supply constraint binding at 200 Gb/lane; customer-approved second-source qualification path materializing Q2 FY2026
- [[SIVE]] (S100) — merchant new-entrant / challenger vantage; confirms the CW laser shortage (800G→1.6T→3.2T) from the aspirant side; pre-revenue (2027+), sub-scale, going-concern-flagged — illustrates the entry-barrier moat
- [[MRVL]] (S102) — coherent-DSP / DCI demand-side adjacency; 1.6T ZR/ZR+ DCI on a 2nm coherent DSP + the new **scale-across** demand axis (DCI ~$1B FY2028) amplify coherent-laser demand; Polariton modulator adjacency. Not a laser-device-tier source (not in tickers per Section 3.2(b))
- [[CPO-platform-battle]] — the chokepoint's relevance depends on CPO adoption trajectory
- [[datacenter-photonics-supply-chain]] — Section 2.1 places the laser layer within the cross-cutting supply-chain map; Bucket B in the investability framing covers the optical device stack
- [[chokepoint-investability-priorities]] — Tier 3-anchored vault-canonical reference for 13-chokepoint photonics framework (created Session 25, A2 first canonical application). Chokepoint 1 (Lasers / EMLs / III-V devices) cross-references this page for cross-validated supplier-side scarcity dynamics (LITE + COHR same-quarter testimony; NVDA $4B equity confirmation).
- **[[nvidia-supply-chain-commitments]]** (S53) — First relationship page in vault history; LITE + COHR are 2 of 4 Tier 1 reciprocal-confirmation participants; cross-vault NVIDIA partnership pattern 4 T1 + 7 T2 post-S64; first downstream propagation cycle test of living document scaffolding at chokepoint scope per S66 refresh.
- **[[TSMC-CoWoS]]** (S65 refresh) — Integration-tier chokepoint for advanced packaging; HBM-CoWoS paired chokepoint formalization at S65 refresh; TSEM SiPh PDK foundry reference-design supplier complementarity finding cross-reference; NVDA $2B equity-plus-purchase at LITE+COHR documented per S50 propagation at integration-tier scope.
- **[[HBM-oligopoly]]** (S64) — Memory framework F6 chokepoint; HBM-CoWoS paired chokepoint with TSMC-CoWoS at upstream-vs-integration tier scope; cross-domain dependency chain (laser supply at this page ↔ memory at HBM-oligopoly via CPO integration ↔ advanced packaging at TSMC-CoWoS).
- **[[VECO]]** (S58 refresh) — Equipment-tier substrate rerating substantive substantiating source per S66 refresh propagation; $250M+ multi-customer InP laser orders + Spector IBD 10X capacity expansion + InP laser SAM $700M by 2030 framing; upstream of laser device fabrication at Layer 1 + Layer 2 of decomposed chokepoint layers.
- **[[TSEM]]** (S62) — SiPh PDK foundry InP modulator heterogeneous integration adjacency per S66 refresh propagation; PH18DA platform; Coherent Mach-Zehnder modulator long-term contract bilateral verification candidate at COHR-side; reference-design supplier complementarity into TSMC CoWoS.
- **[[transformer-supply]]** (S63) — Energy/Power chokepoint pair complement; distinct domain at distribution-side power infrastructure constraint; cross-vault Energy/Power chokepoint pair (constraint-source-vs-workaround) precedent for cross-domain analytical product methodology.

## Change log

- **2026-05-29 (S110 cross-vault re-evaluation propagation — A4):** Added a "MRVL coherent-DSP + scale-across demand vector" section (deferred at the S102 MRVL refresh) — MRVL's first 1.6T ZR/ZR+ DCI on a 2nm coherent DSP + 200G/lane coherent + the new **scale-across** demand axis (DCI ~$1B FY2028) amplify coherent-laser demand from a new direction; Polariton modulator noted as device-tier adjacency (lighter fit). Updated Open Q#8 (bifurcation → trifurcation) + added [[MRVL]] to Cross-references. MRVL NOT added to tickers (coherent-DSP/DCI demand adjacency, not laser-device-tier supplier — per the VECO/TSEM Section 3.2(b) precedent). No change to the core supplier-tier constraint substantiation.
- **2026-05-28 (Session 100 cross-reference — [[SIVE]] canonical creation):** Added "Evidence from SIVE sources (merchant new-entrant / challenger vantage point)" section — fifth vantage on the chokepoint, from a sub-scale merchant trying to enter the CW laser layer. SIVE confirms the 800G→1.6T→3.2T shortage from the aspirant side and illustrates the entry-barrier moat (pre-revenue 2027+, going-concern-flagged, external-foundry-dependent). SIVE added to tickers + Cross-references. No edits to existing evidence sections.
- **2026-05-15 (Session 66 1-stop chokepoint refresh — third 1-stop chokepoint refresh in vault history post-S51 [[HALEU-fuel-chokepoint]] + S65 [[TSMC-CoWoS]] precedents; second consecutive major-chokepoint full refresh; largest single-session refresh additions in vault history):** 5 escalation triggers per S51 + S65 1-stop refresh protocol all NEGATIVE (no new primary-source ingest; vault participants stable; no new structural type; no new chokepoint creation; cross-vault analytical product established at S50 + S53 + S58 + S62 + S65 — propagation only). Substantive refresh additions ~135 lines (162 baseline → 297 final; largest single-session refresh additions in vault history vs S65 TSMC-CoWoS ~90 lines + S52 ETN refresh ~50 lines). **FOUR NEW substantive sections delivered:** (1) **NVDA $2B equity-plus-purchase materialization at LITE+COHR (S50 NEW analytical product propagation)** — **single most material change driver since chokepoint creation**; LITE $2.02B cash injection per CFO Wajid Ali Q3 call + COHR $2B equity + multibillion-dollar multi-year CPO supply through end of decade per CEO Anderson Q3 call; Sherman TX 6-inch InP CW laser production explicitly tied to NVDA partnership; Greensboro NC 5th InP fab + Google explicit named at LITE; 6-inch InP Zürich 3rd site + multi-rail + Thermadite XPU cooling NEW segments at COHR; **first reciprocal-confirmation A1 mode materialization at NVDA architect-customer commitment scope**; differential structural commitment substantiation (equity-only at LITE; dual-leg equity + supply commitment at COHR); (2) **VECO equipment-tier substrate rerating (S58 NEW analytical product propagation)** — $250M+ multi-customer InP laser orders + Spector IBD 10X capacity expansion + InP laser SAM $700M by 2030 + first explicit NVIDIA reference at VECO primary (counterparty-attribution-only at downstream-ecosystem-reference scope); Compound Semi FY2026 RAISED to ~50% growth; equipment-tier leading-indicator for InP substrate capacity expansion trajectory; cross-vault [[InP-supply]] S33 refresh propagation candidate flagged; (3) **TSEM SiPh PDK foundry InP modulator integration adjacency (S62 NEW analytical product propagation)** — PH18DA InP modulator heterogeneous integration; **Coherent 400 Gb per lane all-silicon Mach-Zehnder modulator long-term contract bilateral verification candidate at COHR-side**; OpenLight 400G InP EAM + Scintil Photonics DWDM laser + Salience Labs + Oriole Networks heterogeneous integration; adjacency at laser-device-tier scope vs distinct from supplier-tier vault canonical; (4) **Cross-vault NVIDIA partnership pattern at laser supply scope** — LITE + COHR are 2 of 4 Tier 1 reciprocal-confirmation participants per [[nvidia-supply-chain-commitments]] S53; 4 T1 + 7 T2 cross-vault pattern post-S64; modality distinction (equity-plus-purchase at LITE; equity + multiyear CPO supply at COHR); first downstream propagation cycle test of relationship page living document scaffolding at chokepoint scope. **EXPANSIONS to existing sections:** "Strategic investment as chokepoint signal" subsection (forward-reference to NEW NVDA $2B materialization section); "Decomposed chokepoint layers" Layer 1 InP substrate (VECO MOCVD equipment-tier feed cross-reference); "Remaining uncertainties" (added 3 uncertainties: VECO equipment-tier rerating timeline durability; TSEM SiPh PDK foundry capacity expansion trajectory; cross-vault relationship page living document scaffolding refresh propagation cadence). **NEW Open questions section** (12 items pre-registered; closes structural gap — only provisional [[wafer-level-siph-test]] remains without Open questions section per single-company exposure provisional convention; 11 of 11 canonical chokepoint pages now with Open questions section). Highest-priority Open questions: LITE Q4 FY2026 + FY2026 full-year refresh propagation; COHR Q4 FY2026 + FY2026 full-year refresh propagation with TSEM-COHR Mach-Zehnder modulator bilateral verification candidate; NVDA Q1 fiscal 2027 refresh; Sherman TX 6-inch InP capacity ramp trajectory; VECO Compound Semi FY2026 +50% growth trajectory validation. **NEW Cross-references expansion** with [[nvidia-supply-chain-commitments]] + [[TSMC-CoWoS]] + [[HBM-oligopoly]] + [[VECO]] + [[TSEM]] + [[transformer-supply]] (6 new cross-references; total 14 cross-references vs prior 8). VECO + TSEM NOT added to tickers field per Section 3.2(b) provenance discipline (tickers preserve laser-device-tier substantiating sources only: LITE + COHR + NVDA + AAOI + FN). **Section 4.6 ROI VALIDATED at 0 falsifications (21-instance zero-falsification streak post-S46 codification baseline; refresh propagation only; no kickoff hypothesis falsification candidates per Section 4.4).** A6 (g)/(g') count UNCHANGED at 8+2=10. Cross-vault NVIDIA partnership pattern UNCHANGED at 4 T1 + 7 T2 (no new NVIDIA verification at S66 refresh scope; LITE + COHR Tier 1 reciprocal-confirmation reinforced via S50 materialization documented). Cross-vault Aschenbrenner thesis pattern UNCHANGED at 22+ participants (refresh propagation only). **1-stop refresh protocol durability VALIDATED at 3-instance threshold + largest-single-session-refresh-additions scope** — S51 HALEU smaller scope + S65 TSMC-CoWoS ~90 lines + S66 datacenter-laser-supply ~135 lines = 3-instance protocol durability + scaling validation; Tranche 2C codification candidate methodology formalization. Wikilink-clean streak: **49 sessions** post-S66. Files updated: 7 files (datacenter-laser-supply.md substantive refresh + LITE.md cross-reference + COHR.md cross-reference + nvidia-supply-chain-commitments.md cross-reference + VECO.md cross-reference + index.md + log.md; at hard cap 7 per S57 BTM precedent). TSEM.md cross-reference deferred per scope discipline (TSEM SiPh PDK foundry InP modulator content INCLUDED in this chokepoint page substantive section; TSEM-side cross-reference addressed at next TSEM refresh propagation). **Adjacent chokepoint refresh propagation triggers strengthened:** [[cpo-integration]] S32 + [[advanced-optical-packaging]] S31 + [[InP-supply]] S33 all flagged for refresh propagation per S51 sequential cadence + S65 + S66 accumulated cross-vault analytical product additions; per Vic sequencing direction "CPO-integration and packaging later."
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
