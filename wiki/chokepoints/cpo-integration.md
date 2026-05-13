---
type: chokepoint
tickers: [NVDA, AVGO, MRVL, CRDO, LITE, COHR, AAOI, TSM, FN]
last_updated: 2026-04-30
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

This page synthesizes CPO integration chokepoint mechanics across nine primary-source vault companies — [[NVDA]] (Spectrum-X CPO production + COUPE packaging + Kyber scale-up); [[MRVL]] (Photonic Fabric direct CPO platform competitor via Celestial AI); [[AVGO]] (Bailly platform optionality + copper DAC scale-up alternative); [[CRDO]] (OmniConnect MicroLED near-package optics displacement architecture); [[LITE]] + [[COHR]] (UHP CW laser supply for ELS architecture); [[AAOI]] (asymmetric module displacement risk + ELS laser opportunity); [[TSM]] (COUPE foundry-tier integration); [[FN]] (3 CPO customer programs enabler-tier positioning). Three-source threshold satisfied multi-fold per Session 25 hybrid architecture; closes Tier 3 framework Chokepoint 10 (vault canonical Tier 3 Rank numbering) dedicated chokepoint page coverage gap.

**Vault nine-company concentration with structural diversity:** Layer 1 platform-tier ([[NVDA]] full control point + [[AVGO]] control point with bottleneck participation); Layer 3 specialized designer-tier ([[MRVL]] + [[CRDO]] bottleneck-tier with control-point aspirations); Layer 4 component-tier ([[LITE]] + [[COHR]] with NVDA $2B equity-plus-purchase + [[AAOI]] Layer 4/5 straddling); Layer 2 foundry-tier ([[TSM]] COUPE platform); Layer 6 contract-manufacturing-tier ([[FN]] enabler-tier).

**Murphy bifurcation thesis** (MRVL Q4 FY2026 call): "Scale-out CPO would be relatively limited" vs "scale-up CPO inflecting in a pretty big way" — bifurcation as analytical structure preserved throughout this page per Option C handling.

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

## Value chain shift dynamics

CPO transition shifts value across the supply chain in three asymmetric directions:

**Component-tier value capture (Layer 4):** ELS architecture preserves Layer 4 component supplier value through CPO transition. [[LITE]] + [[COHR]] retain laser supply position via UHP CW laser supply for ELS architecture. NVDA $2B equity-plus-purchase modality (March 2026) operationalizes vertical securing of laser supply chain at Layer 4 (per [[NVDA-platform-integration]] six-modality framework). [[AAOI]] asymmetric exposure: module business displacement risk vs ELS laser opportunity for in-house InP/GaAs laser fabrication.

**Platform-tier value capture (Layer 1):** CPO transition shifts architectural decision authority to platform-tier (NVDA/AVGO control points per Framework 2.6 v9). Three Layer 1 positions exhibit structurally opposed CPO timing per [[CPO-platform-battle]] Layer 1 timing divergence callout: NVDA production adoption (Spectrum-X CPO + Kyber scale-up); AVGO active dismissal ("bright shiny objects" rhetorical Hock Tan; Bailly platform never named in vault primary sources); MRVL quantified projection ($500M FY2028 / $1B FY2029 annualized run rate per Murphy Q4 FY2026 call).

**Foundry/packaging-tier value capture (Layer 2/4):** CPO advanced packaging concentrates foundry-tier value at TSMC COUPE platform (cross-reference [[TSMC-CoWoS]] for COUPE evolution). [[FN]] enabler-tier positioning captures contract-manufacturing-tier value parallel to [[GLW]] Session 20 enabler-tier perspective (3 CPO customer programs disclosed; "amounts relatively small right now" but trajectory positive).

**Net value capture implication:** CPO transition shifts component-tier value (lasers + DSP + optical assembly) toward platform-tier (architecture decisions) + foundry-tier (advanced packaging integration). Component-tier suppliers retain value through ELS architecture for high-power CW laser supply. Layer 4 displacement risk concentrates at integrated-laser-only suppliers without ELS pivot capability.

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

## Per-company integration positioning

### NVDA — Layer 1 full control point; Spectrum-X production + Kyber scale-up

[[NVDA]] is the only vault company with **CPO production-confirmed adoption** per Session 17 GTC ingest. Spectrum-X CPO switch "in full production" (Jensen GTC March 16, 2026; rhetorical attribution); Spectrum-6 "world's first co-packaged optical" switch; Kyber CPO scale-up architecture; Quantum-X networking platform.

**COUPE packaging integration.** Per Session 18 naming convention: "COUPE" in body text; "COUP" in NVDA-attributed quotes. Jensen GTC: "We invented the process technology with TSMC. We're the only one in production with it today" (rhetorical attribution). NVDA + TSM COUPE co-development modality represents joint technology creation rather than pure equity or acquisition (per [[NVDA-platform-integration]] six-modality framework).

**Cross-venue disclosure pattern.** NVDA Q4 FY2026 earnings call (February 25, 2026) contained ZERO CPO mentions across 19 pages; GTC (March 16, 2026) contains extensive CPO production disclosure. Venue-specific information control hypothesis per Session 2 + Session 17 canonical observation. NVDA reserves technology roadmaps for dedicated venues (GTC) rather than earnings calls.

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
- [[NVDA]] / [[AVGO]] / [[MRVL]] / [[CRDO]] / [[LITE]] / [[COHR]] / [[AAOI]] / [[TSM]] / [[FN]] — vault company anchors

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

## Change log

- **2026-04-30 (Session 32 multi-vantage-point synthesis — closes S27-S32 photonics chokepoint completion arc):** Created from nine vault primary-source company anchors per Session 25 hybrid architecture three-source threshold satisfaction (multi-fold; 9 vault primary-source companies + Tier 3 framework anchor). **Fourth canonical multi-source-synthesis chokepoint page in vault history** (after [[InP-supply]] Session 13 [provisional baseline; promoted to canonical at Session 33 per Option C bifurcation handling], [[optical-dsp-phy-supply]] Session 30, [[advanced-optical-packaging]] Session 31). **First chokepoint page with explicit theme-page-overlap differentiation boundary** as page-top scope discipline statement (cpo-platform-battle.md theme page covers platform-strategy archetype breadth; this page covers integration mechanics + value chain shift depth). **First chokepoint page with Scale-up + Scale-out bifurcation handling per Option C** (single page with Scale-up + Scale-out subsections within mechanics + value chain shift sections; Murphy bifurcation thesis preserved as analytical structure). **A2 fifth canonical application** (after Session 25 theme page + Session 30/31 chokepoint pages). **Largest multi-vantage-point synthesis at chokepoint page scope yet** — 9 vault primary-source companies vs Sessions 30 (3 companies) + 31 (4 companies). Per-company depth allocation per CPO-disclosure-density: Tier A (NVDA/MRVL/AVGO/CRDO ~65-70 each) + Tier B (LITE/COHR/AAOI ~35-40 each) + Tier C (TSM/FN ~25-30 each) + cross-cutting context (GLW + non-vault). A6 v8 (g)/(g)' subtype instance count unchanged at 5 accumulated through Session 30; **zero new falsifications** reinforces refined kickoff-drafting-discipline observation: failure mode is fabrication, not detail level; canonical anchoring is success mode. Forward-wikilink discipline preserved: 18-session vault wikilink-clean streak post-Session 32 (extended from 17 post-Session 31). Per A2 structural requirements: Tier 3 source attribution at page-top + theme-page-overlap differentiation boundary + per-section + Source attribution + Source audit notes; counterparty-attribution-only annotation for non-vault company references (Acacia pre-CSCO; Inphi pre-MRVL; Celestial AI pre-MRVL; ASE Technology; Amkor Technology; Sumitomo Electric; Furukawa Electric; Fujikura). Honest-verdict discipline applied to: three Layer 1 CPO timing scenarios (no forced winner); Murphy bifurcation thesis with explicit falsification candidates; Layer 4 component supplier value retention via ELS as conditional thesis; CRDO displacement positioning per Layer 3 four-variant CPO profile.
- **2026-04-30 (Session 33 cross-reference — [[InP-supply]] provisional → canonical promotion):** Adjacent chokepoint page [[InP-supply]] promoted from provisional to canonical multi-source-synthesis chokepoint page via Option C bifurcation handling — single page covers Tier 3 framework Chokepoint 3 (InP substrate supply) + Chokepoint 4 (InP epitaxial capacity) with internal subsection structure. **Fifth canonical multi-source-synthesis chokepoint page in vault history** (after [[optical-dsp-phy-supply]] Session 30, [[advanced-optical-packaging]] Session 31, this chokepoint page Session 32). **Second chokepoint page applying Option C bifurcation handling** (mirrors this page's Scale-up + Scale-out CPO precedent). InP supply chain feeds ELS architecture (UHP CW laser supply for CPO transition) — substrate-tier (AXTI) + epitaxial-tier device-fabrication (COHR six-inch / LITE three-inch / AAOI Sugar Land MBE+MOCVD) feed Layer 4 component-tier value retention through CPO transition documented at this chokepoint page Value chain shift dynamics + per-company integration positioning sections. Cross-chokepoint dependency reference at this page already documents InP substrate constraint extension through 2027 + UHP CW lasers for ELS architecture; promotion of [[InP-supply]] reinforces the cross-tier dependency framing. No content edits to this chokepoint page.
