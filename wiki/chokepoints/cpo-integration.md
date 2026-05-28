---
type: chokepoint
tickers: [NVDA, AVGO, MRVL, CRDO, LITE, COHR, AAOI, TSM, FN, ALAB, ANET, TSEM, SIVE, SOI]
last_updated: 2026-05-28
---

# CPO integration

*Tier 3 framework reference: `raw/research/photonics-chokepoint-table.md` Photonic advanced packaging / CPO integration (Ranking Summary Rank 10a Scale-up + Rank 10b Scale-out post-v2 bifurcation per Murphy bifurcation thesis) / [[chokepoint-investability-priorities]] Chokepoint 10 (vault canonical Tier 3 Rank numbering). Framework characterization: "Important, but adoption timing still uncertain. This is a strategic architecture-transition row rather than a guaranteed near-term revenue row."*

## Theme-page-overlap differentiation boundary

*This chokepoint page covers CPO **integration mechanics + value chain shift dynamics**; complementary to [[CPO-platform-battle]] (theme page covering platform-strategy archetype breadth across 14-16 companies). Per CLAUDE.md theme-page-vs-chokepoint-page differentiation discipline, this page does **NOT** replicate platform-strategy-archetype framing or tier-silence-pattern data point enumeration; those belong in the theme page.*

**Covered here (mechanics + value chain shift depth):** Six core CPO integration mechanics (thermal isolation; laser reliability; optical coupling; serviceability; package yield; field repair); external laser architecture (ELS); value chain shift dynamics (where value accrues across CPO transition); Scale-up + Scale-out bifurcation mechanics (Option C single-page handling per Murphy bifurcation thesis); adoption timing uncertainty mechanics (reliability data thresholds; serviceability concerns; deployment timeline drivers); per-company integration positioning across 9 vault primary-source companies; cross-chokepoint dependencies.

**NOT covered here (theme-page scope):** Platform-strategy archetype framing (incumbent dismissive / direct competitor / acknowledged-deferral / tier-silence / displacement claimant — see [[CPO-platform-battle]]); tier-silence-pattern data point enumeration (39-44 data points across 14-16 companies — see [[CPO-platform-battle]]); five-way executive comparison (Jensen / Murphy / Hock Tan / Mohan / Robbins — see [[CPO-platform-battle]]); reciprocal claim verification across full company set per Tier 3 disclosure (theme-page A1 mode classification — see [[CPO-platform-battle]]).

**NOT covered here (other chokepoint page scope):** Laser supply chokepoint dynamics ([[datacenter-laser-supply]]); optical DSP/PHY supply chokepoint dynamics ([[optical-dsp-phy-supply]]); advanced optical packaging mechanics general ([[advanced-optical-packaging]]); InP substrate supply ([[InP-supply]]); TSMC CoWoS advanced packaging general ([[TSMC-CoWoS]] — COUPE evolution cross-referenced; not duplicated).

## Overview

CPO (co-packaged optics) integration is the architectural transition chokepoint where optics move from front-panel pluggable into the switch ASIC or compute package. This shift creates harder integration problems — thermal isolation, laser reliability, optical coupling, serviceability, package yield, field repair — but can reduce electrical reach and power if integration mechanics are mastered at scale. Adoption timing remains uncertain; the chokepoint is a strategic architecture-transition rather than guaranteed near-term revenue.

This page synthesizes CPO integration chokepoint mechanics across **twelve primary-source vault companies post-S67 refresh tickers expansion** — [[NVDA]] (Spectrum-X CPO production + COUPE packaging + Kyber scale-up); [[MRVL]] (Photonic Fabric direct CPO platform competitor via Celestial AI); [[AVGO]] (Bailly platform optionality + copper DAC scale-up alternative); [[CRDO]] (OmniConnect MicroLED near-package optics displacement architecture); [[LITE]] + [[COHR]] (UHP CW laser supply for ELS architecture + S50 NVDA $2B equity-plus-purchase materialization); [[AAOI]] (asymmetric module displacement risk + ELS laser opportunity); [[TSM]] (COUPE foundry-tier integration + S65 refresh with TSEM reference-design supplier complementarity); [[FN]] (3 CPO customer programs enabler-tier positioning); **NEW S67 expansion:** [[ALAB]] (Photonic Fabric / Celestial AI direct CPO scale-up competitor via S55); [[ANET]] (XPO Extended Pluggable Optics 12.8 TB/module direct CPO competitor per S55 Bechtolsheim OFC keynote); [[TSEM]] (PH18DA SiPh PDK foundry CPO ecosystem participant per S62 NVDA development partner). Three-source threshold satisfied multi-fold per Session 25 hybrid architecture; closes Tier 3 framework Chokepoint 10 dedicated chokepoint page coverage gap.

**Vault twelve-company concentration with structural diversity (broadest cross-vault concentration in vault history at chokepoint scope):** Layer 1 platform-tier ([[NVDA]] full control point + [[AVGO]] control point with bottleneck participation); Layer 2 foundry-tier ([[TSM]] COUPE platform + **[[TSEM]] SiPh PDK foundry CPO ecosystem participant**); Layer 3 specialized designer-tier ([[MRVL]] + [[CRDO]] bottleneck-tier with control-point aspirations + **[[ALAB]] scale-up CPO competitor with Photonic Fabric**); Layer 4 component-tier ([[LITE]] + [[COHR]] with NVDA $2B equity-plus-purchase **materialized at Q3 FY2026 per S50** + [[AAOI]] Layer 4/5 straddling); Layer 5 networking-tier (**[[ANET]] XPO direct CPO competitor scope per S55**); Layer 6 contract-manufacturing-tier ([[FN]] enabler-tier).

**Murphy bifurcation thesis durability validation post-S50/S55 substantiation** (MRVL Q4 FY2026 call): "Scale-out CPO would be relatively limited" vs "scale-up CPO inflecting in a pretty big way" — bifurcation as analytical structure preserved throughout this page per Option C handling. **Post-S67 substantiation reinforcement:** (1) LITE+COHR S50 NVDA $2B equity-plus-purchase materialization + COHR multibillion-dollar multi-year CPO supply through end of decade = supplier-tier capacity commitment scale validates scale-up CPO inflection thesis; (2) ALAB S55 Photonic Fabric (Celestial AI Feb 2026 acquisition) multi-customer NVLink Fusion engagement = third direct scale-up CPO competitor (alongside MRVL Photonic Fabric + NVDA Kyber); (3) ANET S55 XPO Extended Pluggable Optics + Bechtolsheim OFC keynote = ANET-architected pluggable optics form factor at scale-up scope; (4) TSEM S62 SiPh PDK foundry NVDA development partner = wafer-tier ecosystem participation in CPO transition. **Four substantive post-S32 substantiation drivers reinforce Murphy scale-up bifurcation framing without falsification.**

## CPO integration mechanics

Six core integration challenges differentiate CPO from pluggable architecture:

### Thermal isolation

CPO co-packages laser dies with switch ASICs or compute packages — high heat-generating components in close proximity to temperature-sensitive optical elements. Laser efficiency and lifetime degrade with junction temperature rise; modulator wavelength drift (~0.1 nm/°C in photonic systems) creates link instability; thermal cycling fatigues solder joints and package interfaces. Pluggable architectures isolate optics from ASIC heat via front-panel placement; CPO requires package-level thermal management. External Laser Source (ELS) architecture partially relieves this — moving heat-generating laser into a managed thermal zone outside the CPO package.

### Laser reliability

Laser MTBF (mean time between failures) at CPO scale becomes a structural bottleneck. Hyperscale deployments expose laser populations to harsh thermal cycling and high-availability requirements; pluggable architecture allows front-panel-replaceable failure modes whereas CPO failure cascades into package-level rework. ELS architecture concentrates laser reliability risk at fewer external CW sources rather than distributed integrated lasers — analytically distinct exposure profile.

### Optical coupling

Sub-micron alignment between laser output, lens optics, fiber attach, and waveguide entry determines insertion loss and coupling efficiency. CPO compresses alignment tolerances relative to pluggable assembly; misalignment creates non-recoverable link loss. Manufacturing yield economics become non-linear at higher integration density.

### Serviceability

Front-panel-replaceable pluggable optics enable field repair without package disassembly; CPO failures can require ASIC-level rework. Hyperscale operators value MTBF + serviceability tradeoffs differently per workload — training clusters tolerate higher repair downtime than inference fleets. ELS architecture preserves laser serviceability while integrating modulators/PHYs at package level.

### Package yield

Cost-of-failed-die rises non-linearly with CPO integration density. A failed laser in a packaged CPO module destroys not just the laser but the entire package value (ASIC + photonic engine + integration). Known-Good-Die (KGD) economics matter more — wafer-level burn-in screening becomes more valuable (cross-reference [[wafer-level-siph-test]] provisional chokepoint page).

### Field repair

Hyperscale deployment serviceability requires module replacement procedures distinct from pluggable architecture. CPO field repair economics depend on module-level vs package-level failure isolation — currently underspecified across vault primary-source disclosures.

### External Laser Source (ELS) architectural relief

ELS architecture concentrates lasers as external CW sources connected to CPO packages via fiber. Mechanically distinct from integrated laser approach: ELS reduces CPO thermal load; preserves laser serviceability; concentrates laser reliability risk at fewer external sources (which can be NVDA-aligned via [[LITE]]/[[COHR]] $2B equity-plus-purchase modality per Session 22 codification). LITE characterizes ELS modules as ~2-2.5x content gain vs pluggable laser supply per Q2 FY2026 call (rhetorical attribution; LITE-side over-claim mode). ELS architecture is the structural mechanism by which Layer 4 component suppliers retain value through CPO transition.

### Strict architecture definitions (per CPO-for-AIDC-Infrastructure.md 2026-05-26 + CPO-in-AIDC.md 2026-05-27)

Tier 3 source frames category confusion as "single most common analyst error." Strict definitions, tightest integration to loosest:

| Category | Definition | Vault primary-source representative |
|---|---|---|
| **Optical I/O (chiplet-class)** | Optical engine integrated *in-package* with compute/switch die via 2.5D/3D advanced packaging (CoWoS, SoIC). Light enters/exits the package. Used for chip-to-chip in scale-up. | Ayar Labs TeraPHY UCIe chiplet (8 Tbps; GFS 45nm photonics; Series E March 2026 $500M at $3.75B post-money; NVIDIA + AMD-backed); future AVGO XPU CPO |
| **CPO (strict, switch-class)** | Switch ASIC and multiple silicon-photonic optical engines share common substrate. No electrical SerDes leave the package toward front panel. Lasers external (ELS / ELSFP). | AVGO TH5-Bailly (51.2T; 8× 6.4T engines; 5.5W/800G port ~6.9 pJ/bit); TH6-Davisson (102.4T; 16× 6.4T engines; ~3.5W/800G port ~4.4 pJ/bit; TSMC COUPE; shipping Oct 8 2025); AVGO 4th-gen 400G/lane in development |
| **NPO (Near-Packaged Optics)** | Optical engines placed centimeters from ASIC on PCB/substrate. Shorter electrical traces than front-panel pluggables but not on package. Transitional. | [[ALAB]] NPO 2027 roadmap per S55 paired refresh |
| **NVIDIA Quantum-X / Spectrum-X** | **HYBRID implementation.** TSMC SoIC-X 3D hybrid bonding stacks 65nm EIC on PIC (COUPE), then optical sub-assemblies integrated on switch-package interposer. Detachable optical sub-assemblies + external CW lasers. Closer to strict CPO than NPO but emphasizes "4× fewer lasers, detachable subassemblies." | [[NVDA]] Spectrum-X CPO production scope per GTC March 2026 |
| **LRO (Linear Receive Optics)** | Removes DSP on receive side only; transmit retains DSP. Pragmatic intermediate at 1.6T. | Non-vault primarily |
| **LPO (Linear Pluggable Optics)** | Removes DSP entirely; analog TIAs + drivers. Current commercial 800G LPO at 7-8.5W/module (~9-11 pJ/bit per Vitex). LPO MSA published March 25, 2025. | [[ANET]] XPO + LPO strategy per Q1 2026 call |
| **Conventional pluggables** | Full DSP. 800G DR8 at ~17.5 pJ/bit. 1.6T via OSFP-XD (92% of 2025 hyperscaler 1.6T procurement per OCP). 3.2T expected ~2027-2028 on 16× 200G. | [[LITE]] + [[COHR]] + [[AAOI]] + [[FN]] (assembly) |

**Critical analytical refinement per Tier 3 source.** "Adoption is already happening" depends entirely on which definition is invoked. NVIDIA Spectrum-X Photonics availability is 2H 2026 (Ethernet) but it is NOT strict Broadcom-class CPO. Genuine strict-CPO production deployment to date is Meta's Bailly characterization cohort of 15 switches — not a 100k-port production fleet. Per CPO-for-AIDC-Infrastructure.md (2026-05-26).

## Value chain shift dynamics

CPO transition shifts value across the supply chain in three asymmetric directions:

**Component-tier value capture (Layer 4):** ELS architecture preserves Layer 4 component supplier value through CPO transition. [[LITE]] + [[COHR]] retain laser supply position via UHP CW laser supply for ELS architecture. NVDA $2B equity-plus-purchase modality (March 2026) operationalizes vertical securing of laser supply chain at Layer 4 (per [[NVDA-platform-integration]] six-modality framework). [[AAOI]] asymmetric exposure: module business displacement risk vs ELS laser opportunity for in-house InP/GaAs laser fabrication.

**Platform-tier value capture (Layer 1):** CPO transition shifts architectural decision authority to platform-tier (NVDA/AVGO control points per Framework 2.6 v9). Three Layer 1 positions exhibit structurally opposed CPO timing per [[CPO-platform-battle]] Layer 1 timing divergence callout: NVDA production adoption (Spectrum-X CPO + Kyber scale-up); AVGO active dismissal ("bright shiny objects" rhetorical Hock Tan; Bailly platform never named in vault primary sources); MRVL quantified projection ($500M FY2028 / $1B FY2029 annualized run rate per Murphy Q4 FY2026 call).

**Foundry/packaging-tier value capture (Layer 2/4):** CPO advanced packaging concentrates foundry-tier value at TSMC COUPE platform (cross-reference [[TSMC-CoWoS]] for COUPE evolution). [[FN]] enabler-tier positioning captures contract-manufacturing-tier value parallel to [[GLW]] Session 20 enabler-tier perspective (3 CPO customer programs disclosed; "amounts relatively small right now" but trajectory positive).

**Net value capture implication:** CPO transition shifts component-tier value (lasers + DSP + optical assembly) toward platform-tier (architecture decisions) + foundry-tier (advanced packaging integration). Component-tier suppliers retain value through ELS architecture for high-power CW laser supply. Layer 4 displacement risk concentrates at integrated-laser-only suppliers without ELS pivot capability.

### Value-chain 6-layer mapping with margin capture (per CPO-for-AIDC-Infrastructure.md 2026-05-26 + CPO-in-AIDC.md 2026-05-27)

Tier 3 dual-source framework documents 6 distinct value-chain layers with margin capture (High / Medium / Low) + commoditization risk + IP defensibility. Productive analytical tension between reports: Report 1 argues margin concentrates in Layer C (lasers) + Layer D (packaging); Report 2 argues margin concentrates in Layer B (switch silicon + SerDes 40-50% of CPO revenue). Both defensible — Report 1 answers "where does INCREMENTAL margin from CPO accrue?" + Report 2 answers "where does STRUCTURAL profit pool sit in any networking architecture?"

| Layer | Description | Vault canonical participants | Margin capture | Commoditization risk |
|---|---|---|---|---|
| **A: Photonic Die / Optical Engine** | Silicon photonics integration; micro-ring modulator (MRM); hybrid bonding; fiber-to-PIC coupling | [[AVGO]] + [[MRVL]] (incl. Celestial AI Dec 2 2025; non-vault: Ayar Labs $3.75B post-money) + [[COHR]] + [[LITE]] + [[INTC]] + GlobalFoundries (GFS) | HIGH | LOW next 24mo (Samsung/UMC/Tower enter 2027-2029) |
| **B: DSP / SerDes / Switch Silicon** | Optical DSP + SerDes IP + switch ASIC integration | [[AVGO]] + [[MRVL]] + [[CRDO]] + [[ALAB]] + [[NVDA]] + [[CSCO]] + [[ANET]] | MEDIUM-HIGH today, MEDIUM in CPO end-state | LOW-MEDIUM (high-speed SerDes club: NVDA/AVGO/MRVL/Alphawave) |
| **C: Lasers / Light Source (CW chokepoint)** | InP EML + CW DFB; ELS modules; BH DFB IP | [[LITE]] (50-60% global share 200G/lane EML) + [[COHR]] (Sherman TX 6-inch InP fab >5×) + [[AAOI]] | **HIGHEST** per Report 1 framing | LOW for next 3-5 years (InP epi multi-year to build) |
| **D: Packaging / Substrate / Fiber Attach / Test** | TSMC COUPE + SoIC + CoWoS; OSAT services | [[TSM]] (COUPE volume production 2026; SoIC 30-40K wpm end-2026; CoWoS 5.5-reticle >98% yield; ~50 SiPh patents 2024 vs Intel 26) + Amkor + ASE (NVIDIA CPO partner) + [[AEHR]] (InP wafer-level burn-in) | HIGH (TSM) / MEDIUM (OSATs) | LOW (TSM) / MEDIUM (OSATs) |
| **E: ODM / System Integration / Module Assembly** | Contract photonic manufacturing; fiber alignment; wafer-level packaging | [[FN]] (3 active CPO programs; Raytec $32M stake Q3 FY26) + [[FLEX]] + Celestica + Jabil (Intel SiPh transceivers Oct 2023) + Sanmina | LOW-MEDIUM (revenue HIGH; gross margin structurally ~12-13% per FN baseline) | MEDIUM-HIGH |
| **F: Hyperscaler Pull (demand control)** | Architecture standardization; reference design ownership; capex deployment | Meta (Bailly 15-switch + 15M port-device-hours) + Google (TPU v4 Apollo OCS; <5% cost + <3% power) + [[NVDA]] (Spectrum-X/Quantum-X HYBRID) + AWS (Marvell/Celestial Photonic Fabric) + Microsoft (Maia quiet) | NOT component margin pool; sets standards + timing | N/A |

**CoWoS capacity contention observation per Report 1.** CPO competes with GPU/HBM for CoWoS capacity at TSMC — "most overlooked supply gating factor" per source. Cross-reference [[TSMC-CoWoS]] chokepoint for COUPE-on-CoWoS milestone 2026-2027 monitoring. Per CPO-for-AIDC-Infrastructure.md (2026-05-26).

## Scale-up CPO mechanics + positioning

Per Murphy bifurcation thesis: scale-up CPO is "the real CPO platform battle" inflecting "in a pretty big way." Scale-up = within-rack / intra-domain interconnect (NVLink-style; tightly coupled compute fabric).

**Mechanics:** Scale-up bandwidth demands exceed copper electrical reach at 200G/400G per lane; CPO chiplets bypass package-edge bandwidth limits. Architectural fragmentation: NVLink (NVDA proprietary) + UALink (open standard alternative) + ESUN + proprietary scale-up fabrics. CPO chiplet positioning at package level enables higher per-link bandwidth than copper DAC alternatives.

**Vault positioning at Scale-up CPO:**
- **NVDA Kyber CPO scale-up** disclosed at GTC March 2026 alongside copper-scale-up Vera Rubin path. Jensen rhetorical: "copper scale-up or optical scale-up? We're gonna do both." NVLink 144 via copper (Kyber) + NVLink 576 via optical (Oberon).
- **MRVL Photonic Fabric** chiplets co-packaged into both custom XPUs and scale-up switches; on both sides of the link. Commercial deployment FY2028 (calendar 2027); $500M annualized run rate Q4 FY2028; $1B Q4 FY2029. Scale-up interconnect TAM: >$10B by 2030.
- **AVGO** custom XPU + scale-up SerDes (200G/400G copper DAC advocacy). Hock Tan: "You really want to connect XPUs to XPUs directly where you can. The best way to do that is use Direct Attach Copper" (rhetorical; AVGO Q1 FY2026 call). Scale-up via copper rather than CPO is AVGO position.

**Scale-up CPO outcome scenarios:**
1. Murphy bifurcation correct + MRVL Photonic Fabric captures scale-up — MRVL platform-tier ambition realized
2. NVDA Kyber + Oberon optical scale-up captures market — NVDA full control point extends into scale-up CPO
3. AVGO copper DAC scale-up persists — CPO scale-up timeline extends beyond FY2028

## Scale-out CPO mechanics + positioning

Per Murphy bifurcation thesis: scale-out CPO is "relatively limited" — pluggable transceivers retain share into 2028+. Scale-out = between-rack / inter-domain interconnect (Ethernet / InfiniBand fabric; switch-attached CPO).

**Mechanics:** Scale-out CPO replaces pluggable transceivers at switch package level. Bandwidth demands less extreme than scale-up; pluggable serviceability advantage persists at scale-out scale; LPO (linear-drive pluggable optics) + LRO architectures provide intermediate efficiency improvements without full CPO commitment.

**Vault positioning at Scale-out CPO:**
- **NVDA Spectrum-X CPO** "in full production" per GTC March 2026; Spectrum-6 "world's first co-packaged optical" switch. Production-confirmed adoption at platform-tier — falsification candidate for "scale-out limited" Murphy framing.
- **AVGO Bailly platform** never named in vault primary sources (canonical observation per [[CPO-platform-battle]]). Hock Tan: "We are the lead in CPOs" (rhetorical) coexists with "bright shiny objects" dismissal. Without bifurcation, framing is incoherent; with bifurcation, AVGO copper-scale-up advocacy + scale-out CPO optionality is internally consistent.
- **TSM COUPE platform** foundry-tier integration; supports both scale-up and scale-out CPO via foundry packaging (cross-reference [[TSMC-CoWoS]] for COUPE evolution). NVDA-attributed "COUP" naming convention preserved per Session 18 codification.

**Scale-out CPO outcome scenarios:**
1. Murphy bifurcation correct — pluggables retain scale-out share; LITE/COHR/AAOI module business preserved into 2028+
2. NVDA Spectrum-X CPO production capture exceeds Murphy's "limited" framing — pluggable share erosion accelerates
3. AVGO Bailly emerges in Tier 1 disclosures — scale-out CPO Layer 1 contestant set widens

## NVDA $2B equity-plus-purchase materialization at LITE+COHR (S50 NEW analytical product propagation at CPO scope)

**Single most material change driver since chokepoint creation.** Per [[LITE]] + [[COHR]] S50 Q3 FY2026 paired refresh (2026-05-10) — NVDA $2B equity announcements (March 2, 2026) materialized at primary at Q3 FY2026 reporting cycle. **First reciprocal-confirmation A1 mode materialization at NVDA architect-customer commitment scope at CPO supply tier** per [[nvidia-supply-chain-commitments]] S53.

**LITE Q3 FY2026 materialization:** CFO Ali $2.02B cash injection (cash + ST $1.155B → $3.17B); Greensboro NC 5th InP fab + Google explicit named at LITE primary; capital-offset-for-supply-assurance equity-only modality.

**COHR Q3 FY2026 materialization:** Anderson $2B equity + **multibillion-dollar multi-year CPO supply agreement extending through end of decade** ("an expansion of a more than 20-year relationship"); Sherman TX 6-inch InP CW laser production explicitly tied to NVDA partnership; Zürich 3rd 6-inch InP site (production calendar 2027); multi-rail + Thermadite XPU cooling NEW segments; **dual-leg equity + supply commitment modality** structurally distinct from LITE equity-only.

**Differential structural commitment validates Murphy scale-up bifurcation thesis.** COHR multibillion-dollar multi-year CPO supply commitment through end of decade = supplier-tier capacity commitment scale that validates scale-up CPO inflection thesis at primary. NVDA architect-customer commercial commitment scope materially exceeds prior March 2, 2026 announcement framing. Cross-vault [[datacenter-laser-supply]] S66 refresh propagates same materialization at supplier-tier scope.

**NVIDIA Spectrum-X vs Broadcom TH6-Davisson power gap observation (per CPO-for-AIDC-Infrastructure.md 2026-05-26).** Tier 3 source flags under-discussed analytical refinement: NVIDIA Spectrum-X Photonics 9W per 800G port (~11.3 pJ/bit) vs Broadcom TH6-Davisson 3.5W per 800G port (~4.4 pJ/bit) per NVIDIA Developer Blog + Broadcom disclosures — meaningful gap at switch-CPO scope. NVIDIA Spectrum-X is HYBRID (TSMC SoIC-X 3D hybrid bonding + detachable optical sub-assemblies + external CW lasers) per strict architecture definitions above, NOT strict Broadcom-class CPO. Observational analytical refinement at NVDA-vs-AVGO competitive positioning scope per Section 5.2 — gap may narrow with future revisions per Tier 3 caveat; does NOT prescribe competitive verdict.

**$4B NVDA injection March 2, 2026 quantification refinement (per CPO-for-AIDC-Infrastructure.md 2026-05-26).** $2B LITE at $695.31/share + $2B COHR per SEC 8-Ks (March 2, 2026) — substantive share-price + 8-K filing specificity beyond prior vault [[NVDA-platform-integration]] S82 + S50 paired refresh substantively-documented scope.

## Per-company integration positioning

### NVDA — Layer 1 full control point; Spectrum-X production + Kyber scale-up

[[NVDA]] is the only vault company with **CPO production-confirmed adoption** per Session 17 GTC ingest. Spectrum-X CPO switch "in full production" (Jensen GTC March 16, 2026; rhetorical attribution); Spectrum-6 "world's first co-packaged optical" switch; Kyber CPO scale-up architecture; Quantum-X networking platform.

**COUPE packaging integration.** Per Session 18 naming convention: "COUPE" in body text; "COUP" in NVDA-attributed quotes. Jensen GTC: "We invented the process technology with TSMC. We're the only one in production with it today" (rhetorical attribution). NVDA + TSM COUPE co-development modality represents joint technology creation rather than pure equity or acquisition (per [[NVDA-platform-integration]] six-modality framework).

**Cross-venue disclosure pattern (verdict durable per S84 propagation).** NVDA Q4 FY2026 earnings call (February 25, 2026) contained ZERO CPO mentions across 19 pages; GTC (March 16, 2026) contains extensive CPO production disclosure; **NVDA Q1 FY2027 earnings call (May 20, 2026) preserves CPO silence — ZERO CPO mentions across 16 pages**. Venue-specific information control verdict CONFIRMED durable per S84 cross-vault propagation post-S81 NVDA refresh. NVDA reserves technology roadmaps for dedicated venues (GTC + product launches); earnings calls preserve silence at CPO scope. **Cross-venue disclosure gap convention 3rd instance MET** per CLAUDE.md v9.1 Section 3.6 codification threshold (flagged for Tranche 2C-ii formal codification per S81 Vic Decision #5). Resolves NVDA.md S81 Open Question #3 (venue-specific CPO disclosure persistence) at durable-pattern verdict.

**Vera Rubin Q3 2026 production trajectory + CPO-integrated rack platforms (S84 propagation).** Per Colette Kress NVDA Q1 FY2027 call: "on track to commence production shipments of Vera Rubin in the second half of this year, starting in Q3" + "35x higher inference throughput and up to 10x greater AI factory revenue compared with Blackwell." CPO-integrated rack platforms — Spectrum-X CPO switch + Spectrum-6 + Kyber CPO scale-up + Oberon optical scale-up to NVLink 576 — tie to Vera Rubin commencement. Per Jensen GTC March 2026: "We need a lot more capacity for copper. We need a lot more capacity for optics. We need a lot more capacity for CPO" — demand pull through Vera Rubin ramp Q3 → Q4 → Q1 FY2028 ("very big" per Colette Q&A). COUP packaging Q1 FY2027 silence preserved consistent with venue-specific pattern.

**Both copper + optical scale-up.** Jensen GTC: "copper scale-up or optical scale-up? We're gonna do both." NVLink 144 via copper (Kyber) + NVLink 576 via optical (Oberon). NVDA platform straddles both architectures rather than betting on single approach.

### MRVL — Layer 3 bottleneck-tier with control-point aspirations; Photonic Fabric direct CPO competitor

[[MRVL]] is the most quantified scale-up CPO bet via Photonic Fabric (Celestial AI acquisition closed February 2, 2026; ~$1.3B cash + up to $5.5B with earn-outs). Cross-reference [[optical-dsp-phy-supply]] MRVL positioning section for full Photonic Fabric mechanics.

**Photonic Fabric chiplet integration.** First-generation product is a chiplet "integrating all required electrical and optical components, including drivers, TIAs, equalizers, SerDes, microcontrollers, modulators, photodiodes, and waveguides, into a compact form factor" (MRVL 10-K FY2026). Purpose-built for scale-up networking; chiplets co-packaged into both custom XPUs and scale-up switches, on both sides of the link.

**CPO revenue projections (over-claim mode rhetorical).** $500M annualized run rate Q4 FY2028; $1B annualized Q4 FY2029. Celestial + Xconn combined ~$250M aggregate FY2028 (full-year). First-gen chiplet in high-volume manufacturing now. Murphy: "Large-scale commercial deployment of CPO for scale-up connectivity starting next year" (FY2028).

**Tier 1/Tier 2 framing gap (widest in vault).** 10-K corporate/procedural treatment of Celestial AI vs earnings call commercially aggressive treatment ($500M/$1B run rate targets stated as operating forecasts). Preserved per [[optical-dsp-phy-supply]] canonical observation.

### AVGO — Layer 1 control point with bottleneck participation; Bailly optionality + copper DAC alternative

[[AVGO]] simultaneously claims CPO leadership and dismisses CPO timing — incoherent without Murphy bifurcation thesis; with bifurcation, AVGO copper-scale-up advocacy is internally consistent at scale-up tier with scale-out CPO optionality preserved.

**Bailly platform never named.** Per [[CPO-platform-battle]] canonical observation: AVGO Bailly platform is **never mentioned** in any of three primary sources (10-K FY2025 + 10-Q Q1 FY2026 + Q1 FY2026 call). Bailly named in industry framework + ecosystem context only. Both Tier 1 filings contain ZERO mentions of CPO, co-packaged optics, silicon photonics, or any photonics-forward language.

**Active dismissal + claimed leadership.** Hock Tan AVGO Q1 FY2026 call: "We are the lead in CPOs" (rhetorical attribution); "bright, shiny objects" dismissal; copper DAC scale-up advocacy via Tomahawk SerDes leadership. Per [[CPO-platform-battle]] tiered silence pattern: Layer 1 active dismissal variant.

**Scale-up: copper DAC via SerDes, not CPO.** Hock Tan core argument: "You really want to connect XPUs to XPUs directly where you can. The best way to do that is use Direct Attach Copper. That's the lowest latency, lowest power, and lowest cost... We can do it with copper, we can push the envelope from 100G to 200G to even 400G" (AVGO Q1 FY2026 call). Scale-up uses copper (Tomahawk SerDes advantage); scale-out optical (Tomahawk + Bailly future optionality). CPO deferred at scale-up tier.

### CRDO — Layer 3 bottleneck-tier with control-point aspirations; OmniConnect MicroLED near-package optics displacement architecture

[[CRDO]] is the only vault Layer 3 company positioning AGAINST CPO via alternative architecture. Cross-reference [[optical-dsp-phy-supply]] CRDO positioning section for full Cardinal DSP + ZeroFlap + OmniConnect mechanics.

**OmniConnect / Weaver gearbox displacement framing.** Brennan Q3 FY2026 call: future OmniConnect gearboxes targeting "near package optics with MicroLED that will address the reliability, serviceability, and availability pitfalls of current CPO solutions" (rhetorical; over-claim mode CRDO-side displacement framing). Direct architectural challenge to CPO integration approach.

**ZeroFlap optics + Hyperlume MicroLED acquisition.** Production ramp Q1 FY2027; TensorWave first production neocloud customer; 3 additional in qualification (hyperscalers + neoclouds). MicroLED technology via Hyperlume acquisition (NOT Comira per Session 27 A6 (g) factual error scope correction). MicroLED-based "near package optics" architecture positions against integrated laser CPO approach.

**Asymmetric CPO exposure (positive direction).** If CPO displacement materializes, CRDO ZeroFlap + OmniConnect MicroLED captures value asymmetrically. If CPO adoption wins (MRVL Photonic Fabric / NVDA Kyber path), CRDO Cardinal DSP merchant demand at risk. Layer 3 four-variant CPO profile per [[CPO-platform-battle]] codification.

### LITE — Layer 4 component supplier; UHP CW lasers for ELS architecture

[[LITE]] retains Layer 4 component supplier value through CPO transition via UHP CW laser supply for ELS architecture. Cross-reference [[datacenter-laser-supply]] for full laser supply chokepoint dynamics.

**400mW UHP CW laser positioning.** LITE Q2 FY2026 call: 400mW UHP laser competitive moat ("not something that many people can do"); ELS modules providing ~2-2.5x content gain (rhetorical; LITE-side over-claim mode); CPO reliability "gaining real customer confidence," "much more broad-based than people think." Multi-hundred-million-dollar UHP purchase order. First scale-up CPO deployments expected late calendar 2027.

**NVDA $2B equity-plus-purchase modality (March 2026).** LITE NVDA-aligned via $2B equity investment + multi-year purchase commitments. Capital-offset-for-supply-assurance framing distinguishes LITE relationship from COHR's 20-year NVDA relationship. Per [[NVDA-platform-integration]] six-modality framework: equity-plus-purchase is the third modality.

### COHR — Layer 4 broadest vertical integration; CPO purchase order ramp

[[COHR]] is the most aggressive Layer 4 CPO supply ramp via "exceptionally large CPO purchase order from a market-leading AI data center customer" (Anderson COHR Q2 FY2026 call). Cross-reference [[advanced-optical-packaging]] COHR positioning section for full vertical integration mechanics.

**CPO laser/EML supply ramping.** Both InP-based and VCSEL-based CPO/MPO solutions disclosed; new high-power CW laser subject to "exceptionally large purchase order"; book-to-bill >4x in datacenter; "demand absorbs all of that capacity and then some" (Anderson). Six-inch InP device-fabrication advantage at Sherman + Järfälla + Zürich applied to CPO-grade products.

**Scale-out + scale-up phasing.** Anderson Q2 FY2026 call introduces scale-out vs scale-up phasing: scale-out CPO arriving first; scale-up "orders of magnitude larger" and "not years out" (rhetorical). Directionally consistent with Murphy bifurcation but doesn't argue scale-out is *limited* (vs Murphy's stronger framing).

### AAOI — Layer 5 with Layer 4/5 straddling; asymmetric CPO exposure

[[AAOI]] has the most asymmetric CPO exposure profile — both threat and opportunity simultaneously. Cross-reference [[advanced-optical-packaging]] AAOI positioning section for full straddling mechanics.

**Asymmetric exposure structure.** AAOI revenue ~100% pluggable transceiver assembly — the form factor CPO is designed to replace. Module business displacement risk if CPO captures pluggable share. Simultaneously, AAOI manufactures InP/GaAs laser chips internally at Sugar Land, TX (MBE+MOCVD) — Layer 4 capability creating ELS supply opportunity. Tripling InP laser production by mid-2027.

**Management framing emphasizes opportunity, not threat.** Q4 FY2025 call: "more than 95% of laser will be AI laser by end of year" (Thompson Lin rhetorical). Per Session 7 codification: management chose to highlight only the second dynamic (laser opportunity) rather than first dynamic (module displacement risk). Honest-verdict framing per fourth discipline preserves both dynamics.

### TSM — Layer 2 foundry-tier; COUPE platform integration

[[TSM]] is the foundry-tier integration anchor for CPO advanced packaging. COUPE platform supports both scale-up and scale-out CPO via foundry-level photonic integration. Cross-reference [[TSMC-CoWoS]] for full COUPE evolution mechanics.

**Tier 1 silence preserved.** Per Session 17/19 canonical observation: TSM 20-F FY2025 contains zero mentions of COUPE/CPO/co-packaged optics across 244 pages. COUPE conspicuously absent from formal technology listing where CoWoS and SoIC are named. TSM Q1 2026 earnings call zero COUPE mentions; CoPoS referenced as distinct future packaging technology.

**NVDA + TSM co-development modality.** Per Session 18 codification + Session 22 [[NVDA-platform-integration]] update: NVDA-attributed "COUP" naming via Jensen GTC March 16, 2026 ("We invented the process technology with TSMC. We're the only one in production with it today" — rhetorical). Joint technology creation modality distinct from equity/acquisition modalities.

### FN — Layer 6 enabler-tier; 3 CPO customer programs

[[FN]] enabler-tier positioning parallel to [[GLW]] Session 20 enabler-tier perspective. Cross-reference [[advanced-optical-packaging]] FN positioning section for full enabler-tier mechanics.

**3 CPO customer programs.** Grady Q2 FY2026 call: "We're working on co-packaged optics programs with three different customers. It's not just one customer, Samik. It's actually three different customers." Customer names not disclosed; counterparty-attribution-only mode pending bilateral confirmation. "Far ahead of competitors" rhetorical (Grady over-claim mode). "Some CPO revenue already happening, amounts are relatively small right now."

**OCS engagement (adjacent).** Grady Q2 FY2026 call: "We are quite excited about OCS as a technology. We think it has a significant role to play in the future." OCS structurally adjacent to CPO advanced packaging; both require precision optical manufacturing capabilities.

### ALAB — Layer 3 with scale-up CPO ambition; Photonic Fabric (Celestial AI) direct competitor (S55 NEW)

[[ALAB]] enters cpo-integration scope at S67 refresh per S55 paired refresh (2026-05-11) substantive content propagation. **Photonic Fabric (Celestial AI Feb 2026 acquisition $31.1M)** = direct CPO scale-up platform competitor scope; chiplets co-packaged into both custom XPUs and scale-up switches; revenue 2027+ forward-looking per Mohan Q1 FY2026 call.

**Multi-customer NVLink Fusion engagement at Q1 FY2026 (S55):** Gajendra: *"we are engaging with multiple customers to enable NVIDIA Fusion scale-up architecture for hybrid racks"* + *"this is an ecosystem that NVIDIA is creating with NVLink Fusion"* (explicit NVIDIA-as-ecosystem-creator framing); *"We're very deep in engagement for an initial design win in collaboration with NVIDIA and then the hyperscaler. That project is going well... we do expect that this will start providing some meaningful revenue in 2027"* (Gajendra; revenue 2027+).

**A1 counterparty-attribution-only mode preserved** at S55 (NVDA-side bilateral verification deferred per NVDA Q1 fiscal 2027 refresh). Microsoft Azure separately named at Leo CXL scope = first non-Amazon hyperscaler naming at ALAB.

**Cross-vault [[NVDA-platform-integration]] six-modality framework:** ALAB ecosystem-partner counterparty-attribution-only modality distinct from LITE/COHR equity-plus-purchase modality.

**Murphy bifurcation thesis alignment:** ALAB Photonic Fabric scale-up CPO scope alongside MRVL Photonic Fabric scale-up CPO scope + NVDA Kyber scale-up = **three scale-up CPO competitor scopes substantiated at primary post-S55**; reinforces Murphy "scale-up CPO inflecting" framing.

### ANET — Layer 5 with XPO direct CPO competitor scope (S55 NEW)

[[ANET]] enters cpo-integration scope at S67 refresh per S55 paired refresh (2026-05-11) substantive content propagation. **XPO Extended Pluggable Optics** via Andy Bechtolsheim OFC keynote = direct CPO platform competitor scope at ANET-architected pluggable optics form factor.

**XPO specifications at S55 primary:** 12.8 TB/module; 204.8 TB/OCP rack unit; 400W cooling; **>100 vendor endorsement + 10-year run framing**. ANET positioning as scale-out networking-tier with explicit CPO alternative architecture (pluggable optics form factor retained at higher bandwidth + density vs CPO co-packaged form factor displacement).

**Multi-year supply constraint** (Ullal S55): *"one or two year phenomena"* with 52-week lead times + $8.9B purchase commitments; cross-vault Aschenbrenner thesis pattern strengthening at Layer 5 networking-tier first canonical instance.

**ANET CPO tiered silence pattern partial closes (S55):** Layer 5 tiered-silence data point evolves to acknowledged-and-explicitly-dismissed framing. Ullal Q1 2026: *"today's scale-up is mostly limited to NVLink from Nvidia and maybe some PCIe switching. Majority of the Ethernet scale-up will only really happen in 2027 and 2028"* — subordination framing preserved (NVIDIA-as-platform-leader; ANET-as-networking-layer-alongside).

**Caveat #9 vertical integration trigger NOT met preserved per S55** — ANET XPO is networking-tier form factor extension; not Layer 4 component vertical integration.

### TSEM — Layer 2 SiPh PDK foundry CPO ecosystem participant (S62 NEW)

[[TSEM]] enters cpo-integration scope at S67 refresh per S62 first canonical placement (2026-05-14) substantive content propagation. **PH18DA (200mm) SiPh PDK foundry** = direct CPO ecosystem participant scope at wafer-tier foundry layer; Layer 2 specialty foundry / photonics_tier 2 placement.

**NVDA development partner A1 reciprocal-confirmation-LIMITED at S62 Q1 2026 call** — CEO Ellwanger: *"the PR that we did with NVIDIA. It was fairly clear that he talked about us as a development partner."* Bilateral confirmation at Tier 2 via NVDA PR + CEO acknowledgment; "1.6T modules" framing analyst-introduced (Cody Acree Benchmark) not management-confirmed.

**Named SiPh partners at S62 Q1 2026 call prepared remarks (substantive CPO ecosystem partnerships):**
- **Coherent** — 400G all-silicon Mach-Zehnder modulator long-term contract (bilateral verification candidate at COHR-side preserved per S66 datacenter-laser-supply refresh propagation)
- **OpenLight** — 400G InP electro-absorption modulator (EAM) heterogeneously integrated on PH18DA
- **Scintil Photonics** — heterogeneous DWDM laser sources *"designed for near package optics and CPO-based AI infrastructures"*
- **Salience Labs + Oriole Networks** — silicon photonics optical circuit switches on PH18DA + heterogeneous InP optical amplifiers for AI data center scaling
- **Arista (via Bechtolsheim OFC presentation)** — XPO leadership scope cross-references TSEM SiPh PDK foundry positioning

**NPO-to-CPO ramp sequence per CEO Ellwanger (S62 NEW analytical product):** *"NPO is likely to ramp over the next several years and precede a significant ramp in CPO for our primary customers."* Validates Anderson (COHR) + Murphy (MRVL) scale-out/scale-up CPO bifurcation per Murphy bifurcation thesis. First SiPh foundry CEO confirmation of NPO-CPO sequence.

**Reference-design supplier complementarity into TSMC CoWoS per S65 cross-reference** — TSEM provides PIC content into TSMC CoWoS at advanced packaging integration scope. Cross-vault Layer 2 foundry-tier reference-design supplier complementarity pattern first explicit primary-source documentation per S65 + S66 propagation.

### SIVE — merchant external-light-source entrant (pre-revenue; S100 NEW)

[[SIVE]] (Sivers Semiconductors; S100) enters cpo-integration scope as a sub-scale merchant supplier at the External Laser Source (ELS) layer — it makes the CW/DFB laser light source; partners supply the interposer/optical engine. Layer 4 / photonics_tier 4 with explicit pre-revenue framing (AIDC laser revenue zero today; production readiness end-2026, revenue 2027+).

**ELS partnerships — all A1 over-claim (SIVE-side disclosed; not bilaterally confirmed in vault primary sources):** POET Technologies (Sivers DFB laser arrays + POET Optical Interposer → external light engine; prototypes H1 2026, production readiness year-end 2026); O-Net (external laser sources for CPO; OFC March 2026 demos expected); Ayar Labs (named alongside POET/O-Net as a CPO engagement); LIGHTIUM / EU INGENIOUS (TFLN transceiver engines with Sivers CW lasers + photodetectors). A "big household name brand" cited as in roadmap discussions on the Q4 FY2025 call is over-claim (unnamed, "discussions," no design-win).

SIVE's CW-laser positioning is architecture-neutral — it feeds both pluggables (scale-out) and laser arrays (scale-up) — so it is insulated from the pluggable-vs-CPO outcome but exposed to overall optics demand. It is a sub-scale challenger to incumbents [[LITE]]/[[COHR]] (whom NVDA backed with $4B); the open test is whether a self-financing merchant reaches production before incumbent capacity expansion + integrator vertical integration absorb the shortage. See [[datacenter-laser-supply]] merchant-new-entrant vantage + [[SIVE]].

### SOI — silicon-photonics substrate (upstream of the photonic die; S101 NEW)

[[SOI]] (Soitec; S101) sits one layer below the photonic die: every silicon-photonics PIC is fabricated on an SOI wafer, and Soitec is the dominant merchant supplier via its near-monopoly Smart Cut™ process. Layer 6 / photonics_tier 3 — a real-revenue substrate (the SOI analog to [[AXTI]]'s InP), distinct from the pre-revenue [[SIVE]] laser entrant above.

**CPO is a substrate-content uplift, and it is pulling forward.** Because CPO inserts the optical interconnect "at the substrate level," it pulls more Photonics-SOI content per unit than today's pluggables (Soitec Q3 FY2026 call). The CPO timeline has accelerated — Soitec reports "first designs commercially available by end of [calendar] 2026" — and Photonics-SOI (>$100M FY2026) is supply-constrained ("the demand for AI is higher than what the industry today can provide"). Soitec is the architecture-agnostic substrate beneath both pluggables and CPO, so the CPO transition is a positive mix shift; LNOI (lithium-niobate-on-insulator) is the next-gen substrate it is accelerating beyond 1.6T. See [[CPO-platform-battle]] substrate-tier demand-amplifier (SOI alongside [[AXTI]] InP) + [[SOI]].

## Cross-cutting context — non-vault enabler tier + GLW

[[GLW]] fiber/connector enabler-tier positioning. Per Session 20 cross-validation: NVDA-named partnership claims initially over-claim mode; Contour single-core fiber framing refined per GLW FY2025 10-K. CPO fiber attach implications cross-reference [[advanced-optical-packaging]].

**Non-vault enabler tier:** ASE Technology + Amkor Technology OSAT-tier photonic packaging structurally distinct from foundry layer per Session 24 Integration 3. Future ASE/AMKR primary-source ingest would test multi-source threshold at OSAT tier specifically; cross-reference [[advanced-optical-packaging]] for non-vault Tier C future-ingest candidate framing.

## Adoption timing uncertainty mechanics

Per Tier 3 framework: "Important, but adoption timing still uncertain. This is a strategic architecture-transition row rather than a guaranteed near-term revenue row."

**Three Layer 1 timing scenarios** (per Layer 1 timing divergence callout in [[chokepoint-investability-priorities]] post-v2):

1. **Murphy bifurcation thesis correct.** Scale-up CPO inflects FY2028 (MRVL Photonic Fabric commercial deployment); scale-out CPO remains "relatively limited" with pluggable retention into 2028+. AVGO copper-scale-up advocacy proves internally consistent. Component-tier (LITE/COHR/AAOI) module business preserved through bifurcated transition.

2. **AVGO dismissal directionally right.** CPO timing extends beyond FY2028; copper DAC scale-up persists; pluggable scale-out share retained. Murphy framing proves over-aggressive. Layer 1 active dismissal vindicated; component-tier suppliers retain pluggable revenue base longer.

3. **NVDA production lead captures architectural control.** Spectrum-X CPO production + Kyber scale-up + COUPE foundry co-development creates first-mover lock-in before competitors converge. NVDA full control point extends into both scale-up and scale-out CPO architecture; AVGO/MRVL scenarios become reactive.

**Mechanical timing drivers:**
- Reliability data emergence — MTBF data at hyperscale-deployed CPO scale; failure mode analysis
- Serviceability concerns resolution — field repair economics; module replacement procedures
- Deployment timeline drivers — hyperscaler design-cycle commitments; volume ramp pacing

Honest-verdict framing per fourth discipline: no forced winner attribution across three scenarios. CPO timing remains genuinely falsifiable.

### Adoption trigger framework (per CPO-for-AIDC-Infrastructure.md 2026-05-26)

Tier 3 source ranks 10 adoption triggers by importance × falsifiability. Top 5:

| Rank | Trigger | Importance | Status (May 2026) |
|---|---|---|---|
| 1 | Switch radix at 102.4T / 204.8T | HIGH | TH6-Davisson 102.4T shipping Oct 8 2025; 204.8T projected ~2028 |
| 2 | TSMC COUPE / CoWoS capacity | HIGH | COUPE volume production 2026; SoIC 30-40K wpm end-2026 |
| 3 | GPU cluster scale (>100K → >1M XPU) | HIGH | NVIDIA Rubin 2H 2026; Anthropic >1M TPU commitment |
| 4 | 224G SerDes reach/power at 1.6T+ | HIGH | NVIDIA Blackwell ships 224G; Broadcom 224G sampling late 2024 |
| 5 | Yield maturity for SiPh-electronic integration | HIGH | Meta Bailly: 1M+ port-device-hours flap-free; 15M extended at ECOC 2025 |

Per source: 2025-2026 catalyst sequence checks essentially all triggers except #7 (hyperscaler scale-up architecture choice — heterogeneous: Meta committed; Google on OCS+ICI; AWS on Marvell/Celestial; Microsoft quiet). **Heterogeneity = no single-vendor "CPO wave"** — laser + packaging layers (architecture-agnostic) capture margin. Per CPO-for-AIDC-Infrastructure.md (2026-05-26).

### Bull / Base / Bear scenario mechanics (per CPO-for-AIDC-Infrastructure.md 2026-05-26 + CPO-in-AIDC.md 2026-05-27)

Tier 3 dual-source convergent scenario framework with Report 1 probabilities (25/55/20). Section 5.2 enforcement: scenario MECHANICS extracted observationally; "Actionable" investment recommendation rows EXCLUDED per Section 5.2 + Section 2.1 disciplines.

| Scenario | Probability (Report 1) | Adoption timeline | Core assumption |
|---|---|---|---|
| Bull | ~25% | 2026-2027 broad ramp | TH6-Davisson + NVIDIA Spectrum-X Photonics drive >20% CPO attach in 51.2T+ switches starting 2H 2026; 1.6T pluggables peak earlier as Rubin Ultra forces scale-up over fiber |
| Base | ~55% | 2027-2029 gradual ramp | TH6 + Spectrum-X adoption concentrated in 1-2 hyperscalers (Meta + 1) through 2027; broader adoption awaits 4th-gen CPO (400G/lane ~2028+); 1.6T/3.2T pluggables default for scale-out; CPO confined to highest-density TOR + scale-up trials |
| Bear | ~20% | 2030+ only | 1.6T/3.2T pluggables (incl. LPO/LRO) + Arista XPO/AEC extend conventional roadmap through 2029-2030; CPO niche for scale-up |

**Coexistence-vs-displacement framework (both reports converge).** Pluggable 800G+ shipments 24M (2025) → 63M (2026) per TrendForce; McKinsey: 1.6T transceiver shortfall 30-40% through 2029. LightCounting + Cignal AI explicitly state CPO will not materially affect pluggable shipments in next 3 years. Per CPO-for-AIDC-Infrastructure.md (2026-05-26) + CPO-in-AIDC.md (2026-05-27).

### OCI MSA 2026 standardization observation (per CPO-in-AIDC.md 2026-05-27)

Optical Compute Interconnect (OCI) MSA founded 2026 by AMD + Broadcom + NVIDIA + Meta + Microsoft + OpenAI — protocol-agnostic optical physical layer for scale-up AI systems with 3.2T-class link roadmap. Substantive cross-vendor industry standardization signal at scale-up CPO scope. Standardization moving but "around a staged future, not a completed present" per Tier 3 framing. Monitor 12-18 month OCI MSA interop milestones per Open Question #16 below. Per CPO-in-AIDC.md (2026-05-27).

## Cross-chokepoint dependencies

CPO integration depends mechanically on adjacent chokepoints:

- **Laser supply** ([[datacenter-laser-supply]] + [[InP-supply]]) — UHP CW lasers for ELS architecture; InP substrate constraint extends through 2027 per Session 5 cross-validation
- **Optical DSP/PHY supply** ([[optical-dsp-phy-supply]]) — MRVL Ara + AVGO Taurus + CRDO Cardinal DSPs feed CPO modules; node leadership trade-offs (3nm vs 5nm vs n-1)
- **Advanced optical packaging** ([[advanced-optical-packaging]]) — yield + alignment + thermal control mechanics common to all CPO assembly
- **Wafer-level SiPh test** ([[wafer-level-siph-test]] provisional) — KGD economics rise non-linearly with CPO integration density; reliability screening becomes more valuable
- **TSMC CoWoS + COUPE** ([[TSMC-CoWoS]]) — foundry-tier advanced packaging integration; COUPE evolution

CPO transition concentrates dependency risk at adjacent chokepoints. Component-tier suppliers ([[LITE]] / [[COHR]] / [[AAOI]]) retain value through ELS architecture; Layer 1 platform-tier ([[NVDA]] / [[AVGO]]) and Layer 2 foundry-tier ([[TSM]]) capture architectural decision authority + advanced packaging integration value.

## Cross-references

- [[CPO-platform-battle]] — theme page covering platform-strategy archetype framing breadth across 14-16 companies (DIFFERENT scope from this page; complementary)
- [[NVDA-platform-integration]] — Layer 1 platform integration context; six-modality framework operationalizing NVDA CPO control point
- [[chokepoint-investability-priorities]] Chokepoint 10 (post-v2 bifurcation: 10a Scale-up + 10b Scale-out per Tier 3 Rank Ranking Summary) — Tier 3-anchored vault-canonical reference
- [[datacenter-photonics-supply-chain]] Section 2.6 (Photonic foundries) + Section 2.7 (Assembly / packaging / testing) — supply-chain-layer breadth
- [[InP-supply]] — adjacent Chokepoint 3 (substrate supply for laser/EML production)
- [[datacenter-laser-supply]] — adjacent Chokepoint 1 (laser/EML supply); ELS architecture depends on UHP CW laser supply
- [[optical-dsp-phy-supply]] — adjacent Chokepoint 2 (Optical DSP/PHY); MRVL Ara + AVGO Taurus + CRDO Cardinal DSPs feed CPO modules
- [[advanced-optical-packaging]] — adjacent Chokepoint 5 (Advanced optical packaging / alignment); yield + alignment + thermal control mechanics
- [[wafer-level-siph-test]] — adjacent Chokepoint 8 (provisional; wafer-level SiPh reliability test); KGD economics
- [[TSMC-CoWoS]] — TSMC advanced packaging chokepoint; COUPE evolution context
- [[NVDA]] / [[AVGO]] / [[MRVL]] / [[CRDO]] / [[LITE]] / [[COHR]] / [[AAOI]] / [[TSM]] / [[FN]] / **[[ALAB]] / [[ANET]] / [[TSEM]]** — vault company anchors (12 participants post-S67 refresh)
- **[[nvidia-supply-chain-commitments]]** (S53) — Cross-vault NVIDIA partnership pattern relationship page; LITE + COHR Tier 1 reciprocal-confirmation participants; ALAB Tier 2 counterparty-attribution-only ecosystem partner; TSEM Tier 2 reciprocal-confirmation-LIMITED development partner
- **[[HBM-oligopoly]]** (S64) — HBM upstream-vs-CoWoS integration tier pair adjacency; cross-domain 4-framework bridge at AI accelerator packaging scope
- **[[transformer-supply]]** (S63) — Energy/Power chokepoint pair complement; cross-vault paired-chokepoint methodology precedent

## Cross-vault NVIDIA partnership pattern at CPO scope (S67 NEW analytical product propagation)

**Cross-vault NVIDIA partnership pattern 4 T1 + 7 T2 at CPO scope substantiation** per [[nvidia-supply-chain-commitments]] S53 + S64 + S65 + S66 cumulative propagation:

**Tier 1 reciprocal-confirmation at supplier-tier (CPO scope):**
- [[LITE]] — Equity injection modality ($2.02B cash; capital-offset-for-supply-assurance per CFO Wajid Ali Q3 call)
- [[COHR]] — Equity + multiyear CPO supply through decade modality ($2B equity + multibillion-dollar multi-year supply per CEO Anderson Q3 call)

**Tier 2 counterparty-attribution-only at CPO ecosystem scope (S67 NEW propagation):**
- [[ALAB]] — NVLink Fusion ecosystem partner per S55 (Mohan + Gajendra Q1 FY2026 call); revenue 2027+ forward-looking
- [[TSEM]] — A1 reciprocal-confirmation-LIMITED development partner per S62 (CEO Ellwanger Q1 2026 call); first sub-mode codification candidate

**Tier 2 counterparty-attribution-only at integration-tier (existing):**
- [[TSM]] — Foundry-customer modality + NVDA-attributed COUP at GTC March 2026

**Third downstream propagation cycle test of [[nvidia-supply-chain-commitments]] S53 living document scaffolding** at chokepoint scope (S65 TSMC-CoWoS first; S66 datacenter-laser-supply second; S67 cpo-integration third). Methodology durability validation at 3-instance threshold.

**Cross-vault NVIDIA partnership pattern at CPO scope is the BROADEST chokepoint participation scope in vault** — 5 of 11 cross-vault NVIDIA partnership pattern substantiating sources (4 T1 LITE+COHR + 4 T2 ALAB+TSM+TSEM) participate directly at CPO chokepoint scope. CPO chokepoint is the primary cross-vault locus for NVIDIA architect-customer commercial commitment substantiation.

## Open questions

1. **Layer 1 CPO timing divergence resolution.** Three structurally opposed scenarios (Murphy bifurcation correct / AVGO dismissal directionally right / NVDA production captures control) — which converges first? Falsification candidates: NVDA Spectrum-X CPO production volume disclosure; AVGO Bailly emergence in Tier 1 sources; MRVL Photonic Fabric design wins beyond lead customer.
2. **Murphy bifurcation thesis falsification.** Scale-out CPO "relatively limited" — does NVDA Spectrum-X CPO production exceed Murphy framing, or does pluggable retention validate? Pluggable share retention into 2028+ is the testable claim.
3. **ELS architecture commitment.** Does Layer 4 component-tier value capture via ELS architecture materialize at hyperscaler scale? LITE/COHR UHP CW laser supply ramp + AAOI laser merchant business emergence are testable signals.
4. **Reliability data emergence at hyperscale CPO deployment.** MTBF + failure mode analysis at NVDA Spectrum-X production scale; serviceability concerns resolution timeline.
5. **AVGO Bailly emergence in Tier 1 disclosures.** Currently never named in vault primary sources; Tier 1 emergence would shift CPO Layer 1 contestant set materially.
6. **CRDO OmniConnect commercial scale.** ZeroFlap production ramp Q1 FY2027 + OmniConnect/Weaver gearbox production fiscal 2028 — does displacement architecture capture meaningful CPO-displacement value, or remain niche?
7. **TSM COUPE Tier 1 disclosure timing.** Currently zero mentions in 20-F FY2025 + Q1 2026 call; Tier 1 emergence would validate NVDA-attributed "only in production" rhetorical.
8. **Scale-up vs scale-out structural split durability.** Bifurcation analytically useful at vault canonical scope; durability across future ingest cycles remains testable.
9. **Layer 4 component supplier displacement risk asymmetry.** ELS architecture relief depends on integrated-laser-only suppliers having pivot capability; pure-play integrated laser exposure without ELS pivot is structurally vulnerable.
10. **OSAT-tier (ASE/AMKR) photonic packaging scale emergence.** Future primary-source ingest would test OSAT-tier multi-source threshold at advanced packaging chokepoint specifically.
11. **Venue-specific CPO disclosure persistence at NVDA primary — RESOLVED at durable verdict (added S84).** NVDA.md S81 Open Question #3 falsifiable forward observation tested: Q1 FY2027 earnings call (May 20, 2026) preserved CPO silence (zero mentions across 16 pages). Pattern is durable; cross-venue disclosure gap convention 3rd instance MET per Section 3.6 codification threshold. Resolution forwarded to Tranche 2C-ii codification (S86). Forward-tracking: whether durable pattern holds at NVDA Q2 FY2027 (~August 26, 2026 expected) + future earnings cycles.
12. **Marvell-Celestial AI integration trajectory + AWS Photonic Fabric** (NEW per CPO-for-AIDC-Infrastructure.md 2026-05-26 + CPO-in-AIDC.md 2026-05-27) — Celestial AI Dec 2 2025 acquisition ($6B total deal value per Marvell 8-K: ~$3.25B upfront [$1B cash + ~$2.25B in ~27.2M shares] + up to ~27.2M earnout shares tied to revenue milestones); AWS endorsement per Dave Brown VP Compute & ML Services; Photonic Fabric for scale-up architecture; vault MRVL canonical S9 baseline substantively stale at 1-month last_updated — refresh candidate at next dedicated MRVL session.
13. **CoWoS capacity contention between CPO + GPU/HBM** (NEW per CPO-for-AIDC-Infrastructure.md 2026-05-26) — "most overlooked supply gating factor" per Report 1; vault [[TSMC-CoWoS]] chokepoint cross-reference monitoring candidate at COUPE-on-CoWoS milestone 2026-2027; SoIC monthly capacity 30-40K wpm by end-2026 + CoWoS 5.5-reticle >98% yield 2026 substantiation.
14. **OCI MSA 2026 interop milestone tracking** (NEW per CPO-in-AIDC.md 2026-05-27) — Optical Compute Interconnect MSA founded by AMD + Broadcom + NVIDIA + Meta + Microsoft + OpenAI; protocol-agnostic optical PHY for scale-up; 3.2T-class link roadmap; monitor 12-18 month interop milestones as standardization-trajectory observable signal.

## What would confirm or weaken this framing

### Confirm signals

- **NVDA Spectrum-X CPO design wins** at hyperscaler-tier customers beyond lead deployment — confirms Layer 1 production adoption framing
- **MRVL Photonic Fabric revenue ramp** to $500M FY2028 / $1B FY2029 targets — confirms quantified projection thesis
- **AVGO Bailly emergence in Tier 1 disclosures** — confirms scale-out CPO contestant emergence
- **CRDO ZeroFlap production scale** at multiple hyperscaler-tier customers — confirms displacement architecture viability
- **LITE/COHR ELS module revenue ramp** at multi-hundred-million-dollar scale — confirms component-tier value retention via ELS
- **TSM COUPE Tier 1 disclosure** — confirms NVDA-attributed production framing

### Weaken signals

- **CPO timing pull-forward beyond Murphy framing** — earlier-than-expected scale-out CPO displacement of pluggable optics weakens Murphy bifurcation thesis
- **Pluggable retention beyond 2028+** — extended pluggable share preservation weakens NVDA production lead framing
- **Layer 4 component supplier displacement at integrated-laser-only suppliers** — failure of ELS pivot capability weakens component-tier value retention
- **CRDO OmniConnect commercial disappointment** — failure to capture CPO displacement value weakens Layer 3 four-variant CPO profile fourth variant (CRDO displacement claimant)
- **Reliability data emergence below hyperscale-deployment thresholds** — sub-spec MTBF or serviceability concerns weaken CPO production adoption framing
- **AVGO copper DAC scale-up persistence** — copper scale-up adequacy at 200G/400G per lane weakens scale-up CPO inflection thesis (Murphy bifurcation thesis Scale-up = real CPO platform battle)

## Source attribution

**Tier 3 framework reference:** `raw/research/photonics-chokepoint-table.md` Photonic advanced packaging / CPO integration (Ranking Summary Rank 10a Scale-up + Rank 10b Scale-out post-v2 bifurcation per Murphy bifurcation thesis) / [[chokepoint-investability-priorities]] Chokepoint 10 (vault canonical Tier 3 Rank numbering). Vic-team-authored canonical living document. Per A2 fifth canonical application structural requirements: Tier 3 source attribution at page-top + theme-page-overlap differentiation boundary + per-section + Source attribution + Source audit notes; counterparty-attribution-only annotation continues for non-vault company references (Acacia Communications [pre-CSCO acquisition entity]; Inphi [pre-MRVL acquisition entity]; Celestial AI [pre-MRVL acquisition entity]; ASE Technology; Amkor Technology; Sumitomo Electric; Furukawa Electric; Fujikura).

**Primary-source vault company anchors (9 companies):**

- **[[NVDA]]** — Session 17 GTC ingest baseline (NVDA GTC March 16, 2026 keynote) + Session 22 NVDA-platform-integration codification + Session 24 Framework 2.6 codification.
- **[[MRVL]]** — Session 9 ingest baseline + Session 19 Celestial AI codification (acquisition closed February 2, 2026) + Session 24 Framework 2.6 codification + Session 30 optical-dsp-phy-supply.md synthesis.
- **[[AVGO]]** — Session 10 ingest baseline + Session 24 Framework 2.6 codification + Session 30 optical-dsp-phy-supply.md synthesis.
- **[[CRDO]]** — Session 27 paired ingest with [[ANET]] + Session 30 optical-dsp-phy-supply.md synthesis.
- **[[LITE]]** — Session 4 ingest baseline + Session 5 cross-validation + Session 31 advanced-optical-packaging.md synthesis.
- **[[COHR]]** — Session 5 ingest baseline + Session 31 advanced-optical-packaging.md synthesis.
- **[[AAOI]]** — Session 7 ingest baseline + Session 15 Layer 4/5 straddling codification + Session 31 advanced-optical-packaging.md synthesis.
- **[[TSM]]** — Sessions 1-2 ingest baseline + Session 17 NVDA GTC refresh + Session 18 COUPE/COUP naming codification.
- **[[FN]]** — Session 21 ingest baseline + Session 31 advanced-optical-packaging.md synthesis.

**Cross-reference vault chokepoint pages:** [[InP-supply]] (Session 13) + [[datacenter-laser-supply]] (Session 4) + [[optical-dsp-phy-supply]] (Session 30) + [[advanced-optical-packaging]] (Session 31) + [[wafer-level-siph-test]] (Session 25 provisional) + [[TSMC-CoWoS]].

## Source audit notes

### Multi-vantage-point synthesis from existing vault canonical content

Session 32 is multi-source synthesis from existing vault canonical content (9 vault primary-source companies + Tier 3 framework anchor). No new primary-source ingest. Per A2 fifth canonical application: Tier 3 source attribution at page-top + theme-page-overlap differentiation boundary + per-section + Source attribution + Source audit notes; deviation-based refinement at primary-source ingest cycles.

### Theme-page-overlap discipline

Per CLAUDE.md theme-page-vs-chokepoint-page differentiation discipline + page-top boundary statement: this page covers CPO integration **mechanics** + **value chain shift** depth; complementary to [[CPO-platform-battle]] theme page covering platform-strategy archetype **breadth**. No replication of platform-strategy-archetype framing or tier-silence-pattern data point enumeration; cross-references to [[CPO-platform-battle]] for full archetype + tier-silence pattern coverage.

### A6 v8 verification — Phase 0 PASS on product/program names; one Phase 6 (g)' numbering-convention falsification surfaced and corrected

Per CLAUDE.md v8 A6 application discipline: 8 pattern types verified at Phase 0 + Phase 6 cross-reference verification.

**Phase 0 PASS on product/program names.** Session 32 kickoff pre-committed specific product/program names (NVDA Spectrum-X CPO + COUPE/COUP + Kyber; AVGO Bailly + Tomahawk; MRVL Photonic Fabric + Celestial AI; CRDO ZeroFlap + OmniConnect/Weaver + Hyperlume; TSM COUPE; LITE 400mW UHP CW; COHR new high-power CW laser; AAOI Sugar Land MBE+MOCVD; FN OCS engagement + 3 CPO customer programs) — all verified consistent with vault canonical content; zero product/program-name falsifications.

**Phase 6 (g)' numbering-convention falsification — surfaced and corrected.** Kickoff and Stop 1 plan referenced "Tier 3 framework Chokepoint 7" matching the source file's pre-v2 row index (and the v2 refinement note's "Row 7 bifurcated" framing). Vault canonical numbering convention (per [[chokepoint-investability-priorities]] theme page Tier 3 Rank ordering used at Sessions 25, 30, 31) places this chokepoint at **Chokepoint 10** (post-v2 bifurcation: 10a Scale-up + 10b Scale-out per Ranking Summary). Sessions 30 ([[optical-dsp-phy-supply]] = Chokepoint 2) and 31 ([[advanced-optical-packaging]] = Chokepoint 5) used Tier 3 Rank numbering matching priorities theme page. Session 32 page-top reference + Overview + Cross-references + Source attribution + 9 company page Change log entries corrected from "Chokepoint 7" → "Chokepoint 10" at Phase 6 cross-reference fan-out verification. **A6 (g)/(g)' subtype instance count: 6 accumulated through Session 32** (prior 5: Session 26 addendum + Session 27 Hyperlume + Session 30 Sian3/Spica/Acacia 3 instances).

**Pattern observation refinement (per Vic Stop 2 instruction):** Session 32 zero product/program-name falsification result with detail level pre-committed reinforces Session 31 kickoff-drafting-discipline observation. **Failure mode is fabrication (product/program names) and numbering-convention divergence (g' subtype); not detail level.** Session 27 Hyperlume vs Comira; Session 30 Sian3/Spica/Acacia falsifications were product/acquisition NAMES that did not match vault canonical content (fabricated). Session 32 numbering-convention divergence is a (g') subtype where source data is real but the numbering convention is inconsistent with vault canonical (kickoff used pre-v2 row index numbering; vault canonical uses Tier 3 Rank). Refined pattern: **canonical anchoring is the success mode for both fabrication risk and numbering-convention risk.** Detailed kickoffs that anchor product/program names AND chokepoint numbering on vault canonical content (rather than source-file pre-v2 row indexing) produce zero (g)/(g)' instances regardless of detail level.

### A1 three-mode framing applied throughout

- *NVDA Jensen rhetorical claims* ("only one in production"; "we're gonna do both copper and optical scale-up") — over-claim mode
- *AVGO Hock Tan rhetorical claims* ("we are the lead in CPOs"; "bright shiny objects"; copper DAC advocacy) — over-claim mode
- *MRVL Murphy projections* ($500M FY2028 / $1B FY2029 run rate) — over-claim mode (rhetorical projections vs operational forecasts)
- *CRDO Brennan displacement framing* ("near package optics with MicroLED that will address pitfalls of current CPO solutions") — over-claim mode
- *LITE 400mW UHP laser "not something that many people can do"* — over-claim mode
- *COHR Anderson "exceptionally large CPO purchase order"* — over-claim mode
- *AAOI Thompson Lin "more than 95% of laser will be AI laser"* — over-claim mode
- *FN Grady "far ahead of competitors" + 3 CPO customer programs (names not disclosed)* — over-claim + counterparty-attribution-only modes
- *Non-vault references* (Acacia pre-CSCO; Inphi pre-MRVL; Celestial AI pre-MRVL; ASE; AMKR; Sumitomo; Furukawa; Fujikura) — counterparty-attribution-only mode

### Honest-verdict discipline applied throughout

Three Layer 1 CPO timing scenarios preserved without forced winner attribution. Four CPO strategy positions cross-referenced to [[CPO-platform-battle]] (theme-page scope). Murphy bifurcation thesis preserved with explicit falsification candidates. AVGO copper-scale-up advocacy + Bailly silence preserved per existing canonical observation. Layer 4 component supplier value retention via ELS architecture preserved as conditional thesis (depends on pivot capability). CRDO displacement positioning preserved per Layer 3 four-variant CPO profile.

### Tier 3 dual-source addition (in-place refresh 2026-05-27 per Vic instruction; not counted as separate session)

- `raw/research/CPO-for-AIDC-Infrastructure.md` (231 lines; Vic-team-authored 2026-05-26; "Variant Perception Memo" buy-side thematic research) — sources Broadcom PR (Oct 1 2025; Bailly 1M+ flap-free 400G port-device-hours) + TH6-Davisson Oct 8 2025 shipment + NVIDIA SEC 8-Ks March 2 2026 (LITE + COHR $2B + $2B) + TSMC SEMICON Taiwan disclosures + TrendForce 800G+ shipments + McKinsey "Optical Networking: Capturing the Next Wave of Value" + ECOC 2025 Amiralizadeh et al. Meta Bailly paper + Marvell 8-K Dec 2 2025 + LightCounting + Cignal AI commentary. Strict 6-category architecture definitions framework; value-chain 6-layer mapping (A: photonic die + B: DSP/SerDes/switch silicon + C: lasers/CW chokepoint + D: packaging/test + E: ODM/assembly + F: hyperscaler pull); 10-trigger adoption framework; Bull/Base/Bear scenarios (25/55/20); NVIDIA Spectrum-X 9W vs Broadcom TH6 3.5W power gap observation.
- `raw/research/CPO-in-AIDC.md` (260 lines; Vic-team-authored 2026-05-27; analytical memo; structurally complementary) — sources Broadcom PR + NVIDIA disclosures + TSMC COUPE ecosystem + Ayar Labs + Alchip TSMC European OIP Forum demonstrator + AWS-STMicroelectronics transceiver partnership + Meta collective communication papers (>100K GPUs) + Google TPU v4 OCS data + Marvell 8-K + Coherent networking segment Q3 + AMD/Broadcom/NVIDIA/Meta/Microsoft/OpenAI OCI MSA 2026 announcement. Hyperscaler architecture heterogeneity 5-way matrix; coexistence-vs-displacement framework; staged deployment timeline (switch-side first + compute-package later).
- **CRITICAL Section 5.2 + Section 2.1 prescriptive-content non-integration documentation** per LC Pass 2 precedent established 2026-05-26: both sources carry substantive prescriptive content unique among Tier 3 sources at `raw/research/`. **EXCLUDED from vault integration:** Report 1 "HIGHEST CONVICTION LONG: Lumentum (LITE) and Coherent (COHR)" + "HIGH CONVICTION LONG: Fabrinet (FN)" + "HIGH CONVICTION LONG: TSMC (TSM ADR)" + "MEDIUM CONVICTION LONG: Broadcom (AVGO)" + "PAIR: Long COHR/LITE vs short richly-valued pure pluggable transceiver names" + "AVOID shorts on CRDO and MRVL" + "NEUTRAL / monitor: ANET, CSCO" + "AVOID as 'CPO play': INTC and AAOI" + portfolio Add/Trim thresholds per stock + Bull/Base/Bear "Actionable" rows. Report 2 "favors Broadcom most clearly" + "keeps Marvell and Nvidia highly relevant" + "makes Credo unusually attractive as a hedge" + "barbell: own the integrated silicon and packaging bottlenecks" + Best/Most-at-risk scenario tables favoring specific tickers. **All prescriptive content EXCLUDED per CLAUDE.md Section 5.2 "no P&L, no position sizes, no cost basis, ever" + "pages do not prescribe buying, selling, or holding" + Section 2.1 "Describe, don't recommend" disciplines.** Vault integration extracts STRUCTURAL ANALYTICAL CONTENT only — architecture definitions + value-chain layer mapping + adoption trigger framework + Bull/Base/Bear scenario MECHANICS (probabilities + core assumptions; NOT actionable recommendations) + hyperscaler architecture heterogeneity + supply chain bottleneck mapping.
- **3-instance Tier 3 investment-research-style source precedent observation:** LC Pass 2 (1st instance; 2026-05-26 `liquid-cooling-for-AIDC-invest-report.md`) + CPO refresh dual-report (2nd + 3rd instance; 2026-05-27 `CPO-for-AIDC-Infrastructure.md` + `CPO-in-AIDC.md`) = 3-instance precedent. **Tranche 2C-iii codification candidate** at Section 4.6 sub-protocol scope: formalize Section 5.2 enforcement discipline for investment-research-style Tier 3 sources. Vic decision required at future codification cycle.

## Change log

- **2026-05-28 (Session 101 cross-reference — [[SOI]]/Soitec canonical creation):** Added per-company section "SOI — silicon-photonics substrate (upstream of the photonic die)" — Soitec SOI wafer sits one layer below the photonic die; near-monopoly Smart Cut; CPO is a substrate-content uplift + pulling forward to end-CY2026; Photonics-SOI >$100M FY2026, supply-constrained; the SOI analog to [[AXTI]] InP. SOI added to tickers (13 → 14 participants). No edits to existing per-company sections.
- **2026-05-28 (Session 100 cross-reference — [[SIVE]] canonical creation):** Added per-company section "SIVE — merchant external-light-source entrant (pre-revenue)" — sub-scale CW/DFB laser maker at the ELS layer via POET/O-Net/Ayar Labs/LIGHTIUM partnerships (all A1 over-claim). Architecture-neutral light-source positioning; pre-revenue (2027+); challenger to [[LITE]]/[[COHR]]. SIVE added to tickers (12 → 13 participants). No edits to existing per-company sections.
- **2026-05-27 (in-place refresh per Vic instruction; not counted as separate session — Tier 3 dual-source substrate enrichment per `CPO-for-AIDC-Infrastructure.md` 2026-05-26 + `CPO-in-AIDC.md` 2026-05-27):** Same-day dual-Tier-3-source delivery integrated per Vic mini in-place refresh decision. Added NEW strict architecture definitions subsection at CPO integration mechanics scope (6-category framework: Optical I/O chiplet-class + strict CPO switch-class + NPO + NVIDIA Quantum-X/Spectrum-X HYBRID + LRO + LPO + conventional pluggables). NEW value-chain 6-layer mapping subsection at Value chain shift dynamics scope (Layer A photonic die + Layer B DSP/SerDes/switch silicon + Layer C lasers CW chokepoint + Layer D packaging/test + Layer E ODM/assembly + Layer F hyperscaler pull) with margin capture H/M/L + commoditization risk + IP defensibility per Report 1 framework. NEW NVIDIA Spectrum-X 9W vs Broadcom TH6-Davisson 3.5W per 800G power gap observation at NVDA $2B subsection. NEW adoption trigger framework subsection (top 5 of 10 triggers ranked by importance × falsifiability). NEW Bull/Base/Bear scenario mechanics subsection (probabilities 25/55/20 + core assumptions; "Actionable" rows EXCLUDED per Section 5.2). NEW OCI MSA 2026 standardization observation (AMD + Broadcom + NVIDIA + Meta + Microsoft + OpenAI; 3.2T-class link roadmap). 3 NEW Open questions (#12-14: Marvell-Celestial AI integration + AWS Photonic Fabric + CoWoS capacity contention CPO+GPU/HBM + OCI MSA 2026 interop milestone tracking). Source audit notes Tier 3 dual-source addition entry with EXPLICIT Section 5.2 + Section 2.1 prescriptive-content non-integration documentation — both sources' conviction rankings + portfolio Add/Trim thresholds + pair-trade language + Long/Hold/Neutral/Avoid labels EXCLUDED per vault discipline. **3-instance Tier 3 investment-research-style source precedent observation** (LC Pass 2 + CPO dual-report) flagged as Tranche 2C-iii codification candidate. Section 4.6 ROI streak: +1 to 47 instances post-mini-refresh.
- **2026-05-15 (Session 67 1-stop chokepoint refresh — FOURTH 1-stop chokepoint refresh in vault history post-S51 [[HALEU-fuel-chokepoint]] + S65 [[TSMC-CoWoS]] + S66 [[datacenter-laser-supply]] precedents; THIRD consecutive major-chokepoint full refresh; FIRST refresh with substantive tickers expansion (9 → 12 participants); LARGEST chokepoint page in vault history post-refresh):** 5 escalation triggers per 1-stop refresh protocol: 4 NEGATIVE + 1 POSITIVE (new canonical participant addition — substantive scope decision warranted explicit Vic approval at Stop 1; approved Option (a) tickers expansion). Substantive refresh additions ~115 lines (330 baseline → ~445 final; **largest chokepoint page in vault history**). **Tickers expansion 9 → 12 participants** — added [[ALAB]] (Photonic Fabric / Celestial AI direct CPO scale-up competitor per S55) + [[ANET]] (XPO Extended Pluggable Optics 12.8 TB/module direct CPO competitor per S55 Bechtolsheim OFC keynote) + [[TSEM]] (PH18DA SiPh PDK foundry CPO ecosystem participant per S62 NVDA development partner). **Broadest cross-vault concentration in vault history at chokepoint scope.** **FOUR NEW substantive sections delivered:** (1) **NVDA $2B equity-plus-purchase materialization at LITE+COHR (S50 NEW propagation at CPO scope)** — single most material change driver since chokepoint creation; LITE $2.02B cash injection + COHR $2B equity + multibillion-dollar multi-year CPO supply through end of decade; Sherman TX 6-inch InP CW laser production tied to NVDA partnership; differential structural commitment substantiation validates Murphy scale-up bifurcation thesis at supplier-tier capacity commitment scale; (2) **NEW per-company section: ALAB (Layer 3 with scale-up CPO ambition)** — Photonic Fabric (Celestial AI Feb 2026 acquisition $31.1M) + multi-customer NVLink Fusion engagement per S55; revenue 2027+ forward-looking; Microsoft Azure named at Leo CXL; A1 counterparty-attribution-only mode preserved; Murphy bifurcation thesis alignment with MRVL + NVDA Kyber = three scale-up CPO competitor scopes substantiated at primary post-S55; (3) **NEW per-company section: ANET (Layer 5 with XPO direct CPO competitor scope)** — XPO Extended Pluggable Optics 12.8 TB/module via Bechtolsheim OFC keynote per S55; 204.8 TB/OCP rack unit + 400W cooling; >100 vendor endorsement; ANET-architected pluggable optics form factor direct competitor scope; Caveat #9 vertical integration trigger NOT met preserved; (4) **NEW per-company section: TSEM (Layer 2 SiPh PDK foundry CPO ecosystem participant)** — PH18DA NVDA development partner A1 reciprocal-confirmation-LIMITED per S62; named SiPh partners (Coherent 400G MZ modulator + OpenLight 400G InP EAM + Scintil Photonics DWDM laser for CPO + Salience Labs + Oriole Networks + Arista via Bechtolsheim); NPO-to-CPO ramp sequence per CEO Ellwanger NEW analytical product validates Anderson + Murphy bifurcation; reference-design supplier complementarity into TSMC CoWoS per S65; (5) **NEW Cross-vault NVIDIA partnership pattern at CPO scope** — third downstream propagation cycle test of [[nvidia-supply-chain-commitments]] S53 living document scaffolding at chokepoint scope; CPO chokepoint = **BROADEST chokepoint participation scope in vault** at 5 of 11 cross-vault NVIDIA partnership pattern substantiating sources. **EXPANSIONS to existing sections:** Overview (12-participant scope framing + Murphy bifurcation thesis durability validation post-S50/S55 substantiation with 4 substantive substantiation drivers); Cross-references (added [[nvidia-supply-chain-commitments]] + [[HBM-oligopoly]] + [[transformer-supply]]). **Section 4.6 ROI VALIDATED at 0 falsifications (22-instance zero-falsification streak post-S46 codification baseline).** A6 (g)/(g') count UNCHANGED at 8+2=10. Cross-vault NVIDIA partnership pattern UNCHANGED at 4 T1 + 7 T2 (ALAB + TSEM Tier 2 reinforced via S67 propagation; no new T1 verification). Cross-vault Aschenbrenner thesis pattern UNCHANGED at 22+ participants. **1-stop refresh protocol durability VALIDATED at 4-instance threshold + substantive-tickers-expansion scope** — S51 + S65 + S66 + S67 = 4-instance protocol validation; Tranche 2C codification candidate methodology formalization. **Third downstream propagation cycle test of [[nvidia-supply-chain-commitments]] S53 at chokepoint scope** — methodology durability VALIDATED at 3-instance threshold (S65 + S66 + S67). Wikilink-clean streak: **50 sessions** post-S67. Files updated: 6 files (cpo-integration.md substantive refresh + ALAB.md cross-reference + ANET.md cross-reference + TSEM.md cross-reference + index.md + log.md; under hard cap 7). LITE.md + COHR.md cross-reference deferred per scope discipline (S50 propagation already substantively covered at S66 change log entries earlier today; S66 datacenter-laser-supply refresh propagation reciprocal). **Same-day refresh-heavy session count: 4** (S64 HBM-oligopoly creation + S65 TSMC-CoWoS refresh + S66 datacenter-laser-supply refresh + S67 cpo-integration refresh) — historic vault refresh-heavy day. Per Vic sequencing direction "CPO-integration and packaging later" — S67 CPO-integration refresh delivered; **S68 advanced-optical-packaging refresh next** per accumulated cross-vault analytical product additions.
- **2026-04-30 (Session 32 multi-vantage-point synthesis — closes S27-S32 photonics chokepoint completion arc):** Created from nine vault primary-source company anchors per Session 25 hybrid architecture three-source threshold satisfaction (multi-fold; 9 vault primary-source companies + Tier 3 framework anchor). **Fourth canonical multi-source-synthesis chokepoint page in vault history** (after [[InP-supply]] Session 13 [provisional baseline; promoted to canonical at Session 33 per Option C bifurcation handling], [[optical-dsp-phy-supply]] Session 30, [[advanced-optical-packaging]] Session 31). **First chokepoint page with explicit theme-page-overlap differentiation boundary** as page-top scope discipline statement (cpo-platform-battle.md theme page covers platform-strategy archetype breadth; this page covers integration mechanics + value chain shift depth). **First chokepoint page with Scale-up + Scale-out bifurcation handling per Option C** (single page with Scale-up + Scale-out subsections within mechanics + value chain shift sections; Murphy bifurcation thesis preserved as analytical structure). **A2 fifth canonical application** (after Session 25 theme page + Session 30/31 chokepoint pages). **Largest multi-vantage-point synthesis at chokepoint page scope yet** — 9 vault primary-source companies vs Sessions 30 (3 companies) + 31 (4 companies). Per-company depth allocation per CPO-disclosure-density: Tier A (NVDA/MRVL/AVGO/CRDO ~65-70 each) + Tier B (LITE/COHR/AAOI ~35-40 each) + Tier C (TSM/FN ~25-30 each) + cross-cutting context (GLW + non-vault). A6 v8 (g)/(g)' subtype instance count unchanged at 5 accumulated through Session 30; **zero new falsifications** reinforces refined kickoff-drafting-discipline observation: failure mode is fabrication, not detail level; canonical anchoring is success mode. Forward-wikilink discipline preserved: 18-session vault wikilink-clean streak post-Session 32 (extended from 17 post-Session 31). Per A2 structural requirements: Tier 3 source attribution at page-top + theme-page-overlap differentiation boundary + per-section + Source attribution + Source audit notes; counterparty-attribution-only annotation for non-vault company references (Acacia pre-CSCO; Inphi pre-MRVL; Celestial AI pre-MRVL; ASE Technology; Amkor Technology; Sumitomo Electric; Furukawa Electric; Fujikura). Honest-verdict discipline applied to: three Layer 1 CPO timing scenarios (no forced winner); Murphy bifurcation thesis with explicit falsification candidates; Layer 4 component supplier value retention via ELS as conditional thesis; CRDO displacement positioning per Layer 3 four-variant CPO profile.
- **2026-04-30 (Session 33 cross-reference — [[InP-supply]] provisional → canonical promotion):** Adjacent chokepoint page [[InP-supply]] promoted from provisional to canonical multi-source-synthesis chokepoint page via Option C bifurcation handling — single page covers Tier 3 framework Chokepoint 3 (InP substrate supply) + Chokepoint 4 (InP epitaxial capacity) with internal subsection structure. **Fifth canonical multi-source-synthesis chokepoint page in vault history** (after [[optical-dsp-phy-supply]] Session 30, [[advanced-optical-packaging]] Session 31, this chokepoint page Session 32). **Second chokepoint page applying Option C bifurcation handling** (mirrors this page's Scale-up + Scale-out CPO precedent). InP supply chain feeds ELS architecture (UHP CW laser supply for CPO transition) — substrate-tier (AXTI) + epitaxial-tier device-fabrication (COHR six-inch / LITE three-inch / AAOI Sugar Land MBE+MOCVD) feed Layer 4 component-tier value retention through CPO transition documented at this chokepoint page Value chain shift dynamics + per-company integration positioning sections. Cross-chokepoint dependency reference at this page already documents InP substrate constraint extension through 2027 + UHP CW lasers for ELS architecture; promotion of [[InP-supply]] reinforces the cross-tier dependency framing. No content edits to this chokepoint page.
- **2026-05-24 (Session 84 cross-vault propagation post-S81 NVDA + S82 NVDA-platform-integration):** Refreshed "NVDA — Layer 1 full control point" subsection with venue-specific CPO disclosure persistence verdict durable per NVDA Q1 FY2027 zero CPO mentions across 16 pages. Added Vera Rubin Q3 2026 production trajectory + CPO-integrated rack platform demand pull (Spectrum-X CPO + Kyber + Oberon optical scale-up to NVLink 576). Cross-venue disclosure gap convention 3rd instance MET per Section 3.6 codification threshold (flagged for Tranche 2C-ii at S86). Added Open Question #11 documenting RESOLVED status of NVDA.md S81 Open Question #3 + forward-tracking at NVDA Q2 FY2027. Resolves Murphy/AVGO/NVDA Layer 1 timing scenario at production-confirmed trajectory preserved without forced winner attribution. No new chokepoint participant additions.
