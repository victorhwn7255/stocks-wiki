---
type: chokepoint
tickers: [FN, LITE, COHR, AAOI, TSEM, ANET, NOK, MKSI, NVDA]
last_updated: 2026-05-24
---

# Advanced optical packaging / alignment

*Tier 3 framework reference: `raw/research/photonics-chokepoint-table.md` Chokepoint 5 (Advanced optical packaging / alignment) / Ranking Summary Rank 5; high conviction. Framework characterization: "Real chokepoint; FN is clean manufacturing exposure."*

## Overview

Advanced optical packaging / alignment is the manufacturing yield chokepoint in AI photonics. 1.6T modules and CPO optical engines require precise laser attach, lens alignment, fiber coupling, mux/demux integration, thermal control, and calibration. Even when every component works individually, the finished optical assembly can fail if alignment or packaging yield is poor — manufacturing yield can become as important as component design at this layer.

This page synthesizes advanced optical packaging chokepoint dynamics across four primary-source vault companies — [[FN]] (Session 21 ingest baseline; Layer 6 pure contract manufacturing), [[LITE]] (Session 4 ingest baseline; Layer 4 component supplier with internal packaging; three-inch InP industry-standard), [[COHR]] (Session 5 ingest baseline; Layer 4 broadest vertical integration; six-inch InP device-fabrication advantage), and [[AAOI]] (Session 7 ingest baseline; Layer 5 transceiver assembler with Layer 4 in-house laser straddling tension). Three-source threshold satisfied multi-fold per Session 25 hybrid architecture; closes Tier 3 framework Chokepoint 5 dedicated chokepoint page coverage gap.

**Tier 3 framework characterization** (per `raw/research/photonics-chokepoint-table.md`): "Real chokepoint; FN is clean manufacturing exposure. FN is the cleanest listed precision optical manufacturing / contract manufacturing exposure. LITE and COHR have internal photonic packaging know-how. ASE/AMKR are more CPO/advanced-package optionality names. AAOI has vertical module execution leverage but higher customer concentration risk."

**Vault four-company concentration with four distinct vertical integration patterns:** [[FN]] pure contract manufacturing (Layer 6) + [[LITE]] component supplier with internal packaging (Layer 4 / photonics_tier 3) + [[COHR]] broadest vertical integration spanning substrate → epitaxy → chip → module → system (Layer 4 / photonics_tier 2) + [[AAOI]] Layer 5 transceiver assembler with Layer 4 in-house laser fabrication (photonics_tier 5; Layer 4/5 straddling tension preserved per Session 15 codification). Four structurally distinct integration approaches at same chokepoint with different competitive economics.

**Non-vault references** (Tier C future-ingest candidates per `wiki/themes/datacenter-photonics-supply-chain.md`): ASE Technology + Amkor Technology (OSAT-tier photonic packaging — structurally distinct from foundry layer per Session 24 Integration 3); JBL/Jabil + Sanmina + Flex + InnoLight Technology Suzhou + Celestica + Benchmark Electronics + Venture Corporation Limited (additional optical contract manufacturers per FN FY2025 10-K competitive landscape).

## Chokepoint mechanics

### Why advanced optical packaging is a chokepoint

Optical packaging is not like ordinary electronic assembly. Tiny misalignments can create insertion loss, coupling loss, degraded signal quality, and field reliability problems. Volume manufacturing needs repeatability, automation, and process discipline. The "boring but decisive" manufacturing layer determines scale economics — if demand for 1.6T modules explodes, suppliers that can assemble and calibrate at scale capture more value than the market expects.

Specific manufacturing requirements:
- **Laser attach** — precision placement of laser dies onto substrates with sub-micron accuracy
- **Lens alignment** — collimating and focusing optics aligned to laser output for fiber coupling
- **Fiber coupling** — optical fiber attach with low insertion loss and reliable terminations
- **Mux/demux integration** — wavelength-division multiplexing components integrated into module package
- **Thermal control** — hermetic sealing, thermal management, calibration for temperature drift
- **Calibration + qualification** — final-test validation across BER, TDECQ, eye diagrams, FEC, interoperability

### Structural drivers

1. **1.6T module ramp at hyperscaler scale.** Higher lane speeds tighten optical margins; alignment precision and yield requirements rise non-linearly with bandwidth.
2. **CPO architectural transition.** CPO optical engines push packaging requirements further — laser attach, optical coupling, package yield, and serviceability dynamics differ from pluggable architecture.
3. **OCS (Optical Circuit Switch) emerging architecture.** FN Q2 FY2026 call disclosed OCS engagement: "We are working on a couple of projects in that space, and we are quite excited about OCS as a technology" (Grady).
4. **Yield economics matter more at scale.** Volume hyperscaler deployments make yield improvements compound — alignment automation and process discipline become structural differentiators.

### Tier 3 framework key flags

Per Tier 3 source: module yield; assembly capacity; optical alignment automation; capex expansion; customer mix; Malaysia/Asia manufacturing footprint; CPO packaging wins.

## FN positioning

[[FN]] is the cleanest listed precision optical manufacturing / contract manufacturing exposure per Tier 3 framework. Per Session 21 ingest baseline: Layer 6 (scale manufacturing & materials) per `frameworks.md` v8/v9; photonics_tier 4. Second Layer 6 vault page (after [[AXTI]]); pure optical contract manufacturer with no in-house products — Layer 6 is the structurally correct placement; the absence of product design is the feature, not a bug, for customer relationships.

### Pure contract manufacturing model

FN does no in-house product design or material production. Self-described as "advanced optical packaging and precision optical, electro-mechanical and electronic manufacturing services" provider per FY2025 10-K. Customer-neutral assembly model distinguishes from vertically integrated peers: [[LITE]] / [[COHR]] (Layer 4 component suppliers with internal packaging) and [[AAOI]] (Layer 5 transceiver assembler with in-house laser).

### Customer concentration

Per FY2025 10-K customer concentration disclosure (Session 21 ingest):
- **NVIDIA Corporation: 27.6%** of FY2025 revenue (top customer)
- **Cisco Systems: 18.2%** of FY2025 revenue (second-largest)
- Top-2 combined: **45.8%**
- [[LITE]]: 15.4% in FY2023 only; below 10% concentration threshold FY2024-FY2025
- [[COHR]]: not in customer concentration table FY2025
- Emerging AWS HPC ramp ($86M Q2 FY2026)

Customer concentration profile distinct from vault peers: Microsoft 27.6% comparable to AAOI Microsoft ~43% but with broader hyperscaler-tier diversification (NVDA + Cisco + AWS emerging; not single-customer-dominant like AAOI).

### CPO program disclosure (Q2 FY2026 call)

In Q2 FY2026 call Q&A (Samik Chatterjee, JPMorgan), CEO Seamus Grady disclosed:
- **"Three different customers"** CPO programs: "We're working on co-packaged optics programs with three different customers. It's not just one customer, Samik. It's actually three different customers." Customer names not disclosed.
- **Manufacturing positioning ahead** — Grady (rhetorical): "We believe we're far ahead of most of our competitors in the space in making this technology a reality."
- **CPO as evolution from existing capabilities** — Grady: "Co-packaged optics, it's really an evolution from silicon photonics and the precision photonics packaging capabilities we've developed over many years."
- **Some CPO revenue already happening, "amounts are relatively small right now."**

This is more material CPO disclosure than expected from a Layer 6 contract manufacturer. **Enabler-tier perspective comparable to [[GLW]] (Wendell Weeks) Session 20 enabler-tier perspective.** Both flagged as non-contestant CPO ecosystem perspectives — FN and GLW are not platform decision-makers but their manufacturing/material positioning makes them structural beneficiaries of CPO architectural transition regardless of which platform wins.

### OCS engagement

Grady Q2 FY2026 call: "We are working on a couple of projects in that space, and we are quite excited about OCS as a technology. We think it has a significant role to play in the future." OCS engagement is structurally adjacent to CPO advanced packaging; both require precision optical manufacturing capabilities.

### Conspicuous absences (Source audit)

Per FN Session 21 Source audit notes: no mention of "co-packaged" / "CPO" in 10-K body (terminology surfaces only on Q2 FY2026 call). Single mention of "artificial intelligence" — FY2024 narrative attributes data communication products growth "primarily for artificial intelligence applications"; FY2025 narrative does not repeat AI attribution. Layer 5 framing absent from filing self-characterization. Tier 1 / Tier 2 framing gap observation: 10-K corporate framing vs Q2 call commercial CPO disclosure.

## LITE positioning

[[LITE]] occupies Layer 4 (specialized components and differentiated suppliers) per `frameworks.md` v9 with photonics_tier 3 (specialized designers and high-quality differentiated suppliers). Per Session 4 ingest baseline + Session 5 cross-validation: differentiated laser supplier with internal photonic packaging know-how; three-inch InP industry-standard manufacturing; narrower product focus on components and transceivers vs [[COHR]]; capital-offset-for-supply-assurance NVDA relationship framing.

### Three-inch InP industry-standard manufacturing

InP wafer fab fully allocated; ~25-30% supply-demand imbalance; all EML capacity spoken for through calendar 2027 per LITE Q2 FY2026 call. **40% capacity expansion** target front-loaded per Q2 call.

**Three-inch InP in industry context** (per Session 5 + silicon-photonics-primer.md, citing Sumitomo technical reviews and AXT 2020 results). LITE's three-inch InP position reflects the industry baseline, not an inferior capability. InP is brittle, thermally sensitive, and less forgiving than silicon; scaling from three-inch to larger diameters raises stress, bow, warp, dislocation management, and equipment-automation challenges simultaneously. [[COHR]]'s six-inch position is the unusual manufacturing scale, not LITE's three-inch being substandard. AXT's own historical commentary on six-inch InP yield difficulties reinforces this: larger-diameter InP production does not automatically translate to better economics until yields are brought under control.

### NVDA $2B equity-plus-purchase modality (March 2026)

LITE is NVDA-aligned via $2B equity investment + multi-year purchase commitments (March 2026). Capital-offset-for-supply-assurance framing distinguishes LITE relationship from [[COHR]]'s 20-year NVDA relationship + Materials segment intersegment role. Per [[NVDA-platform-integration]] six-modality framework: equity-plus-purchase is the third modality (after Mellanox acquisition + Groq licensing).

### Cross-validation with COHR (resolved at Session 5)

Per Session 5 [[COHR]] cross-validation: datacenter laser supply constraint is industry-wide. COHR independently confirms supply-demand imbalance extending through at least 2027, with book-to-bill >4x in datacenter. Anderson (COHR Q2 FY2026 call): "demand absorbs all of that capacity and then some." See [[datacenter-laser-supply]] for canonical chokepoint analysis. Both LITE and COHR are competing for the same laser supply chokepoint position.

## COHR positioning

[[COHR]] occupies Layer 4 with photonics_tier 2 (irreplaceable infrastructure and chokepoint participants) per Session 5 codification — placed Tier 2 rather than Tier 4 based on primary-source evidence of structural position closer to "chokepoint participant" than "differentiated supplier." Broadest vertical integration in the photonics chokepoint set: substrate → epitaxy → chip → module → system spanning per Q2 FY2026 call.

### Six-inch InP device-fabrication advantage

Anderson (COHR Q2 FY2026 call): "we are the world's only producer of six-inch indium phosphide" — six-inch platform yields >4x chips at <50% cost versus industry-standard three-inch wafer. Three qualified device-fabrication sites: **Sherman, Texas; Järfälla, Sweden; Zürich** (Switzerland).

**Framing refinement (per Session 5 silicon-photonics-primer.md cross-validation, citing Sumitomo 2016 technical paper, AXT 2020 results, IQE 2024 expansion release).** Anderson's "monopoly" framing is not accurate at the substrate level: Sumitomo, AXT, and IQE all have six-inch InP substrate or epitaxial capability, and JX Advanced Metals is a relevant InP supplier at four-inch scale. The defensible claim is narrower but still structurally significant: COHR holds an unusually advanced multi-site six-inch InP **device-fabrication** position — the ability to process six-inch wafers through high-yield epitaxy, lithography, etch, metallization, passivation, facet preparation, device testing, and qualification for specific CPO-grade products. The distinction matters: substrate availability and device-fabrication qualification are different bottleneck layers (see [[datacenter-laser-supply]] decomposed chokepoint map).

### Capacity expansion trajectory

Per COHR Q2 FY2026 call disclosure:
- Quadrupled InP wafer starts from September to December quarter
- Plan to **double** total InP capacity by end of calendar 2026
- Materials segment intersegment role supplies COHR's own Networking segment

### Product portfolio breadth (broadest vertical integration in vault)

Per COHR.md Session 5:
- **EML** (electro-absorption modulated lasers) — record volumes at 100G lane speeds, ramping 200G; both InP-based EMLs internally produced and external EML supply from multiple vendors
- **VCSELs** — 6-inch GaAs VCSEL fabs in US and Europe; both datacom (short-reach) and 3D sensing applications; Apple partnership for 3D sensing using GaAs VCSELs at Sherman, Texas, volume production H2 2026
- **Transceivers** — protocol-agnostic datacenter transceivers supporting Ethernet, InfiniBand, and NVLink (COHR 10-K FY2025); 800G shipping, 1.6T in development
- **CPO purchase orders** — "exceptionally large purchase order from a market-leading AI data center customer for a CPO solution" per Q2 FY2026 call; both InP-based and VCSEL-based CPO/MPO solutions disclosed
- **Materials segment** — substrate-to-system spanning vertical integration; intersegment role unique in vault

COHR spans from laser chips to finished transceiver modules — broader vertical integration than [[LITE]].

### NVDA $2B equity-plus-purchase + 20-year relationship

COHR is NVDA-aligned via $2B equity investment + multi-year purchase commitments (March 2026); 20+ year NVDA relationship per Session 5 codification. Per [[NVDA-platform-integration]] six-modality framework: equity-plus-purchase is the third modality, applied at both LITE and COHR. COHR's 20-year relationship + Materials segment intersegment role differentiates from LITE's newer capital-constrained relationship.

## AAOI positioning

[[AAOI]] occupies Layer 5 (integrated systems) per `frameworks.md` v9 with photonics_tier 5 (integrated systems with CPO displacement long-term risk); **Layer 4/5 straddling tension preserved per Session 15 codification.** Real AI exposure but more commoditized, more customer-concentrated, and more exposed to long-term CPO displacement than the component layer above.

### Layer 4/5 straddling tension

AAOI manufactures its own InP and GaAs laser chips at **Sugar Land, TX** using **MBE (molecular beam epitaxy) and MOCVD (metalorganic chemical vapor deposition)** — a Layer 4 capability. Thompson Lin (CEO; rhetorical claim): "more than 95% of laser will be AI laser by end of year"; AAOI plans to **triple InP laser production by mid-2027** (AAOI Q4 FY2025 call). "Unique in our industry" management framing per AAOI 10-K FY2025.

The straddling is real but does not yet warrant a tier upgrade. Current revenue is ~100% assembled transceivers — the laser capability is vertically integrated into modules, not sold as standalone Layer 4 product. A tier upgrade requires evidence that the laser capability has become commercially material as standalone revenue or merchant customer relationships. Layer 5 classification maintained with this tension noted per Session 15 codification.

### CPO asymmetric exposure (Session 7 codification)

The structural tension: AAOI's revenue comes from pluggable transceivers — the form factor that CPO is designed to replace. If CPO displaces pluggable transceivers in hyperscale datacenters, AAOI's addressable market contracts. Simultaneously, AAOI manufactures InP laser chips internally, and CPO architectures require external laser sources (ELS). CPO therefore threatens AAOI's module business while potentially creating demand for AAOI's laser business. Management chose to highlight only the second dynamic (CPO laser opportunity) per Q4 FY2025 call.

Asymmetric CPO exposure profile distinct from FN (enabler-tier; participates in CPO programs without architectural commitment) and from LITE/COHR (CPO laser/EML supply ramp without module-displacement risk).

### Customer concentration profile

Microsoft ~43% top customer per AAOI 10-K FY2025; top 2 = 81.9% (Microsoft + AT&T per recent disclosures). Highest customer concentration risk among 4 vault companies at this chokepoint. Concentration risk magnified by Layer 5 straddling — single-customer dependency at module assembly with smaller in-house laser scale than [[LITE]] / [[COHR]].

### Technology alternatives (Session 7 codification)

Silicon photonics technology landscape includes intermediate architectures between pluggables and full CPO: **LPO** (linear-drive pluggable optics, retaining the pluggable form factor but reducing power); **NPO** (near-packaged optics, moving the optical engine closer to the ASIC without full co-packaging); **CPC** (co-packaged copper, eliminating board-level electrical routing without introducing photonics). Each represents a potential bridge technology that could delay full CPO adoption and extend pluggable relevance (per silicon-photonics-primer.md, OIF COI white paper). AAOI discusses none of these alternatives in any source — observation absence may indicate management does not view technology-transition positioning as discussion topic for investor audience, or that AAOI is not participating in any bridge-technology program.

## Vertical integration pattern distinction (6 distinct patterns post-S68 expansion)

**The structurally most analytically rich cross-source synthesis at this chokepoint — expanded from 4 → 6 patterns post-S68 tickers expansion.** Six vault companies operate at the same chokepoint with six distinct vertical integration approaches, producing different competitive economics:

| Company | Layer | Vertical integration approach | Competitive economics |
|---|---|---|---|
| **FN** | 6 | **Pure contract manufacturing** — no in-house product/material; customer-neutral; **S59 Raytec $32M / 14% stake evolution** to integrated-precision-optical-packaging participation | Margin-stable; volume-driven; less idiosyncratic risk; customer relationships span vault peers (NVIDIA + Cisco + AWS emerging); Taiwan wafer-level packaging access via Raytec |
| **LITE** | 4 | **Component supplier with internal packaging** — three-inch InP fabs + EML/transceiver assembly; **S50 Greensboro NC 5th InP fab + Google explicit named** | Differentiated component pricing; capacity-constrained; supply-allocation negotiating leverage; NVDA $2.02B capital injection at S50 |
| **COHR** | 4 | **Substrate-to-system vertical integration** — six-inch InP device fabrication + EML + VCSEL + transceiver + Materials segment; **S50 Multi-Rail + Thermadite XPU cooling NEW segments + Zürich 3rd 6-inch site** | Highest gross margin potential; broadest moat; structural pricing power if six-inch InP advantage holds; NVDA $2B equity + multibillion-dollar multi-year CPO supply through decade |
| **AAOI** | 5 (with Layer 4/5 straddling) | **Layer 5 transceiver assembly with Layer 4 in-house laser** | Asymmetric CPO exposure (module business displacement risk + laser business opportunity); single-customer concentration risk |
| **TSEM** (S68 NEW) | 2 | **Wafer-tier SiPh PDK foundry reference-design supplier complementarity** — PH18DA SiPh PDK foundry; heterogeneous integration platform; reference-design supplier into TSMC CoWoS at advanced packaging integration scope per S65 [[TSMC-CoWoS]] refresh | Foundry-tier economics; reference-design supplier moat at major integrator scope per CEO Ellwanger S62 disclosure; specialty foundry sub-domain methodology candidate |
| **ANET** (S68 NEW) | 5 | **Finished-module form factor architectural retention** — XPO Extended Pluggable Optics 12.8 TB/module + 204.8 TB/OCP rack unit + 400W cooling via Bechtolsheim OFC keynote per S55 | Pluggable form factor preservation at higher bandwidth/density vs CPO co-packaged displacement; >100 vendor endorsement + 10-year run framing; ANET-architected scale-out networking-tier economics |

Per honest-verdict discipline: no forced winner attribution. Six structurally distinct integration approaches preserve genuine competitive uncertainty across foundry-tier (TSEM) + component-tier (LITE/COHR) + assembly-tier (AAOI) + contract-manufacturing-tier (FN) + module-form-factor-tier (ANET). Each company's competitive economics depends on different externalities:
- FN succeeds if optical contract manufacturing tier captures CPO transition value + Raytec wafer-level packaging integration materializes
- LITE succeeds if three-inch InP industry-standard remains commercially viable through 1.6T transition + Greensboro NC 5th fab capacity ramp
- COHR succeeds if six-inch InP device-fabrication advantage translates to expansion economics + premium pricing + multi-rail/Thermadite segments commercialization
- AAOI succeeds if Layer 4 in-house laser business emerges as merchant supply OR pluggable-displacement timing extends past CPO commercial scale
- **TSEM (S68 NEW) succeeds if SiPh PDK foundry reference-design supplier complementarity to TSMC CoWoS captures wafer-tier value at heterogeneous integration scope; NVDA development partner A1 reciprocal-confirmation-LIMITED at PH18DA platform**
- **ANET (S68 NEW) succeeds if XPO form factor preserves pluggable retention through 2030 per Bechtolsheim 10-year run framing vs CPO displacement timing per Murphy bifurcation thesis**

## NVDA $2B equity-plus-purchase materialization at LITE+COHR (S50 NEW analytical product propagation at packaging scope)

**Single most material change driver since chokepoint creation at packaging-tier scope.** Per [[LITE]] + [[COHR]] S50 Q3 FY2026 paired refresh (2026-05-10) — NVDA $2B equity announcements (March 2, 2026) materialized at primary at Q3 FY2026 reporting cycle. Capital deployment + commercial commitment scope quantified at supplier-tier packaging chokepoint participation. Cross-vault [[datacenter-laser-supply]] S66 + [[cpo-integration]] S67 refresh propagation reciprocal at chokepoint cascade.

**LITE Q3 FY2026:** CFO Ali $2.02B cash injection + Greensboro NC 5th InP fab + Google explicit named (first hyperscaler-naming at LITE primary post-S46).

**COHR Q3 FY2026:** Anderson $2B equity + **multibillion-dollar multi-year CPO supply agreement through end of decade**; Sherman TX 6-inch InP CW laser production explicitly tied to NVDA partnership; Zürich 3rd 6-inch site (production calendar 2027); **Multi-Rail + Thermadite XPU cooling NEW segments**; 6-inch transceiver shipments. Dual-leg equity + supply commitment modality structurally distinct from LITE equity-only.

**Implications for packaging-tier vertical integration patterns:** COHR substrate-to-system vertical integration (pattern 3) becomes most concentrated NVDA architect-customer commitment locus in vault; LITE component supplier with internal packaging (pattern 2) gets capital-binding-constraint relief enabling capacity expansion. **Differential structural commitment substantiation validates Murphy scale-up bifurcation thesis at supplier-tier capacity commitment scale.**

## FN Raytec wafer-level packaging investment (S59 NEW analytical product propagation)

**FN Layer 6 enabler-tier evolution to integrated-precision-optical-packaging participation** per [[FN]] S59 refresh (2026-05-12). **$32M / 14% minority stake in Raytec Semiconductor** (Taiwan wafer-level packaging; CPO ecosystem partner) — substantively elevates FN Layer 6 thesis beyond pure contract manufacturing.

**Cross-vault implications:**
- FN no longer pure-contract-manufacturer at vertical integration pattern distinction; **Raytec investment is FN first vertical integration evolution since canonical creation** (S21 baseline)
- Taiwan wafer-level packaging access via Raytec minority stake = adjacency to TSMC advanced packaging foundry-tier scope per [[TSMC-CoWoS]] S65 refresh
- **Two datacom transceiver programs shipping directly to a hyperscale customer** per S59 — strategic shift from OEM-only to direct hyperscaler engagement
- DCI record $197M (+90% YoY; +38% sequential) at Q3 FY2026 = substantive Datacom acceleration

**Methodology candidate:** Layer 6 enabler-tier evolution to integrated-precision-optical-packaging participation = first vault canonical Layer 6 enabler-tier vertical integration evolution; Tranche 2C codification candidate.

## ANET XPO finished-module form factor adjacency (S55 NEW analytical product propagation)

**ANET enters advanced-optical-packaging scope at S68 refresh per S55 paired refresh (2026-05-11) substantive content propagation.** **XPO Extended Pluggable Optics 12.8 TB/module** via Andy Bechtolsheim OFC keynote = finished-module form factor adjacency at module-level retention scope (pluggable form factor preservation vs CPO co-packaged displacement).

**XPO specifications at S55 primary:**
- 12.8 TB/module bandwidth at pluggable form factor
- 204.8 TB/OCP rack unit aggregate scale
- 400W cooling per module
- **>100 vendor endorsement + 10-year run framing**
- ANET-architected scale-out networking-tier form factor

**Adjacent at finished-module scope** vs direct packaging-tier manufacturing-yield-chokepoint participation. XPO competes with CPO architecture at scale-out scope per Murphy bifurcation thesis ([[cpo-integration]] S67 cross-reference). Pluggable-retention thesis at higher bandwidth/density preserves Layer 5 networking-tier economics.

**Cross-vault thesis intersection:** ANET XPO + LITE/COHR ELS architecture per [[datacenter-laser-supply]] S66 cross-reference = pluggable retention at multi-tier level (laser supply + module form factor) vs full CPO transition timing per Murphy bifurcation. Three cross-vault data points at pluggable-retention scope: COHR Anderson scale-out vs scale-up phasing + Murphy MRVL bifurcation thesis + ANET Bechtolsheim XPO 10-year run framing.

## NOK Pennsylvania photonics packaging project + OFC March 2026 DSP roadmap adjacency (S73 NEW analytical product propagation)

**NOK enters advanced-optical-packaging scope at S73 first canonical creation per [[NOK]] standalone ingest (2026-05-19).** First foreign-issuer first canonical participant at this chokepoint; **NOK Pennsylvania photonics packaging and testing project** disclosed at NOK 20-F FY2025 Property, plant and equipment Note 4.2 ("potential project in Pennsylvania relating to photonics packaging and testing") + **4 new Digital Signal Processors at OFC March 2026 + 13 new solutions Building Block architecture (4 optical engines per generation vs prior 2 engines)** + 800G ZR/ZR+ coherent pluggables shipping + 1.2T/1.6T coherent transponders current generation + InP manufacturing San Jose Fab 2 ramping later 2026 ("one of a few manufacturers with indium phosphide manufacturing capability at scale" per Hotard Q1 2026 call). Adjacent at photonic packaging chokepoint scope via vertical integration substantive bilateral verification candidate; not directly at module-form-factor scope (Optical Networks integrated systems sub-domain distinct from FN/LITE/COHR/AAOI/TSEM/ANET pre-S73 chokepoint participant scope).

**Cross-vault thesis intersection:** NOK 4 new DSPs OFC March 2026 announcement scope adjacent to ANET XPO Extended Pluggable Optics OFC March 2026 announcement scope (S55 + S71 + S72 cross-references); first cross-vault OFC March 2026 announcement scope methodology candidate at vault chokepoint participant scope.

## Customer concentration patterns (4 distinct profiles)

| Company | Concentration profile |
|---|---|
| **FN** | NVIDIA 27.6% + Cisco 18.2% top-2 = 45.8%; broader hyperscaler-tier customer base; emerging AWS HPC ramp ($86M Q2 FY2026); diverse customer mix relative to vault peers |
| **LITE** | NVDA $2B equity-plus-purchase (March 2026); capital-offset-for-supply-assurance framing; multi-customer hyperscaler base prior to NVDA equity |
| **COHR** | NVDA $2B equity-plus-purchase (March 2026); 20+ year NVDA relationship; protocol-agnostic transceivers (Ethernet + InfiniBand + NVLink) widen customer reach |
| **AAOI** | Microsoft ~43% top-1; top 2 = 81.9% (Microsoft + AT&T); highest customer concentration risk among 4 |

**NVDA equity-plus-purchase modality applied at LITE + COHR (Session 22 codification).** Per [[NVDA-platform-integration]] six-modality framework, NVDA's $2B equity investment in each of LITE and COHR (March 2026) is the third platform integration modality (after Mellanox acquisition + Groq licensing; followed by Ayar Labs equity backing + GLW counterparty-attribution-only + VRT reciprocal-confirmation). This modality vertically secures the photonics laser supply chain at component-tier level. FN benefits indirectly via NVIDIA 27.6% top customer relationship; AAOI is structurally absent from this NVDA-aligned set.

## Six-inch vs three-inch InP device-fabrication asymmetry (cross-COHR/LITE)

**Most analytically substantive cross-source synthesis at this chokepoint.** COHR's six-inch InP device-fabrication position vs LITE's three-inch InP industry-standard creates a manufacturing-economics asymmetry with structural implications.

### COHR claims (Anderson Q2 FY2026 call; per A1 over-claim mode)

- "We are the world's only producer of six-inch indium phosphide" (rhetorical; refined per Session 5 to "device-fabrication position" — substrate-level "monopoly" framing not accurate; Sumitomo, AXT, IQE all have six-inch InP substrate or epitaxial capability)
- Six-inch platform yields **>4x chips at <50% cost** versus industry-standard three-inch wafer
- Three qualified device-fabrication sites (Sherman + Järfälla + Zürich)

### LITE counter-context (Session 5 silicon-photonics-primer.md cross-validation)

- Three-inch InP is industry-standard, not inferior
- Six-inch scaling raises brittleness, stress, yield challenges (InP is more thermally sensitive than silicon)
- AXT 2020 historical commentary on six-inch InP yield difficulties reinforces: larger-diameter InP production does not automatically translate to better economics until yields are brought under control

### Cross-validated supply constraint

- Both LITE and COHR fully allocation-constrained through 2027
- Six-inch advantage manifests in expansion economics rather than current pricing
- Thomas O'Malley (Barclays) cross-validated on COHR call, referencing "your competitor talked about 40% increases" (matching LITE's InP expansion)
- Anderson confirmed: "demand absorbs all of that capacity and then some"

### Structural implication

The six-inch vs three-inch asymmetry is genuine but bounded. COHR captures expansion economics; LITE captures industry-standard scale. Both companies are NVDA-aligned via $2B equity-plus-purchase modality. Honest-verdict framing: outcome depends on whether six-inch InP yield trajectory closes the cost gap claimed by COHR (>4x chips at <50% cost) at scale before three-inch capacity expansion saturates demand.

## CPO advanced packaging implications

CPO architectural transition affects four vault companies asymmetrically:

| Company | CPO exposure profile | Source attribution |
|---|---|---|
| **FN** | **Enabler-tier positive** — 3 CPO customer programs; "amounts relatively small right now"; "evolution from existing capabilities" framing; benefits regardless of platform winner | Grady Q2 FY2026 call (rhetorical claims attributed) |
| **LITE** | **Supply-ramp positive** — CPO laser/EML supply ramping; cross-validated supply constraint extending through 2027 | LITE Q2 FY2026 call + Session 5 cross-validation |
| **COHR** | **Supply-ramp positive + premium pricing** — "exceptionally large CPO purchase order from market-leading AI data center customer"; both InP and VCSEL-based CPO/MPO solutions; six-inch InP advantage applied to CPO-grade products | Anderson Q2 FY2026 call |
| **AAOI** | **Asymmetric — both threat and opportunity** — module business displacement risk if CPO captures pluggable share; in-house laser business opportunity if CPO External Light Source (ELS) demand materializes; management highlights only the second dynamic | Session 7 codification; Q4 FY2025 call |

Per honest-verdict discipline: AAOI exposure asymmetry is genuine. CPO timing and architectural outcomes determine whether AAOI laser business evolves into merchant supply (Layer 4 tier upgrade) or remains internal-use-only (Layer 5 module assembly with high customer concentration risk).

**NVDA Q1 FY2027 venue-specific pattern at advanced packaging scope (S85b cross-vault propagation post-S81 + S82 + S84).** NVDA Q1 FY2027 earnings call (May 20, 2026) preserved silence on advanced optical packaging across 16 pages — consistent with the broader venue-specific CPO disclosure pattern documented at [[cpo-integration]] S84 + [[CPO-platform-battle]] S84. GTC venue (March 2026) remains the chosen venue for advanced packaging + COUP disclosure; earnings calls preserve silence. **Cross-venue disclosure gap convention 3rd instance MET per CLAUDE.md v9.1 Section 3.6 codification threshold** (Tranche 2C-ii formal codification at S86). Vera Rubin Q3 2026 production commencement (per Colette Q1 FY2027) drives advanced packaging demand through 2027+ — cross-reference [[TSMC-CoWoS]] S84 for CoWoS allocation demand framing + [[NVDA-platform-integration]] S82 for COUP co-development modality scope (NVDA + TSM joint co-development; 7th platform integration modality framework).

## Cross-references

- [[chokepoint-investability-priorities]] Chokepoint 5 (Advanced optical packaging / alignment) — Tier 3-anchored vault-canonical reference; this chokepoint page provides multi-source synthesis depth complementing theme page breadth
- [[datacenter-photonics-supply-chain]] Section 2.7 (Assembly / packaging / testing) — supply-chain-layer breadth; this chokepoint page provides chokepoint-specific synthesis vs supply-chain-layer breadth
- [[InP-supply]] — adjacent Chokepoint 1 (substrate supply); upstream of advanced optical packaging in supply chain flow
- [[datacenter-laser-supply]] — adjacent Chokepoint 1 (laser/EML supply); structurally parallel — laser supply + advanced packaging both feed into module integration
- [[optical-dsp-phy-supply]] — adjacent Chokepoint 2 (Optical DSP/PHY); structurally parallel at component-tier
- [[CPO-platform-battle]] — five-way executive comparison + Layer 1 adoption-vs-dismissal divergence; CPO transition affecting this chokepoint asymmetrically across 4 vault companies
- [[NVDA-platform-integration]] — six-modality framework; equity-plus-purchase modality applied at LITE + COHR (third modality) operationalizing NVDA vertical securing of photonics supply chain
- [[FN]] — vault company anchor; Session 21 ingest baseline (Layer 6 contract manufacturing)
- [[LITE]] — vault company anchor; Session 4 ingest baseline + Session 5 cross-validation (Layer 4 component supplier with internal packaging; three-inch InP industry-standard)
- [[COHR]] — vault company anchor; Session 5 ingest baseline (Layer 4 broadest vertical integration; six-inch InP device-fabrication advantage)
- [[AAOI]] — vault company anchor; Session 7 ingest baseline (Layer 5 transceiver assembler with Layer 4 in-house laser; straddling tension preserved per Session 15)
- [[GLW]] — adjacent enabler-tier perspective; Session 20 ingest; FN and GLW both flagged as non-contestant CPO ecosystem perspectives

## Open questions

1. **FN CPO program revenue ramp timing.** "Amounts relatively small right now" per Grady Q2 FY2026 call; trajectory ambiguous between (a) gradual ramp consistent with Murphy bifurcation thesis (scale-out CPO limited; scale-up CPO inflecting FY2028) and (b) faster ramp consistent with NVDA Spectrum-X CPO production timeline.
2. **COHR doubling InP capacity by end calendar 2026 — execution risk.** Quadrupled InP wafer starts September to December quarter is aggressive trajectory; six-inch InP yield management at expanding scale is non-trivial per silicon-photonics-primer.md commentary.
3. **LITE 40% capacity expansion completion timing.** Front-loaded expansion target per Q2 FY2026 call; whether expansion closes supply-demand imbalance before 1.6T demand inflection is open.
4. **AAOI Layer 4 laser business merchant emergence.** Tripling InP laser production by mid-2027 — does this evolve into standalone merchant Layer 4 revenue or remain captive for Layer 5 module assembly? Tier upgrade trigger pre-registered per Session 15 codification.
5. **Six-inch InP yield trajectory at scale.** COHR claim of >4x chips at <50% cost vs three-inch is a steady-state assertion; whether yield holds at expansion-scale volumes (doubling InP capacity by end calendar 2026) is open.
6. **FN OCS engagement — analytical product distinct from CPO.** OCS market structurally adjacent to CPO; whether FN OCS engagement generates separate analytical thread or remains subsumed in CPO advanced packaging framing depends on future FN disclosures.
7. **ASE/AMKR OSAT-tier photonic packaging vault entry.** Per Session 24 Integration 3: ASE/AMKR are OSAT-layer photonic packaging participants structurally distinct from foundry layer. Future ASE or AMKR primary-source ingest would test multi-source threshold at OSAT layer specifically.
8. **AAOI alternative-architecture (LPO/NPO/CPC) silence.** AAOI discusses none of these alternatives — observation absence is meta-signal; whether AAOI participates in bridge-technology programs is open.

## What would confirm or weaken this framing

### Confirm signals

- **FN CPO program revenue ramp** — disclosed revenue from any of three customer programs at material scale would confirm enabler-tier framing
- **COHR doubling InP capacity execution** — capacity build-out to plan with yield maintenance would confirm six-inch InP device-fabrication advantage at expansion scale
- **LITE 40% capacity expansion completion** — three-inch InP industry-standard scaling continues to absorb demand inflection
- **AAOI laser merchant business emergence** — standalone Layer 4 revenue or named merchant customer relationship would warrant tier upgrade per Session 15 codification
- **Multi-customer NVDA-aligned ramp** — both LITE and COHR delivering on $2B equity-plus-purchase commitments confirms equity-plus-purchase modality structural integration

### Weaken signals

- **CPO timing pull-forward** — earlier-than-expected scale-out CPO displacement of pluggable optics would weaken AAOI module business and bound LITE/COHR/FN revenue trajectories before scale-up CPO ramp
- **Six-inch InP yield reversal** — if COHR doubling InP capacity introduces yield problems, six-inch device-fabrication advantage could narrow vs three-inch industry-standard
- **AAOI customer concentration crisis** — Microsoft ~43% concentration creates single-customer dependency risk; loss of Microsoft business would destabilize Layer 5 assembly without Layer 4 merchant offset
- **Asian transceiver assembler share gain** — InnoLight + Eoptolink + Accelink + Source Photonics structurally analogous to AAOI Layer 5 positioning; share gain would weaken AAOI competitive moat
- **ASE/AMKR OSAT-tier photonic packaging emergence at scale** — could compress contract-manufacturing tier (FN) margin if OSAT-layer photonic packaging becomes commodity
- **NVDA platform integration retreat** — material change to LITE/COHR equity-plus-purchase commitments would weaken NVDA-aligned ramp thesis

## Source attribution

**Tier 3 framework reference:** `raw/research/photonics-chokepoint-table.md` Chokepoint 5 (Advanced optical packaging / alignment) / Ranking Summary Rank 5; high conviction. Vic-team-authored canonical living document. Per A2 fourth canonical application structural requirements: Tier 3 source attribution at page-top + per-section + Source attribution + Source audit notes; counterparty-attribution-only annotation continues for non-vault company references (ASE Technology, Amkor Technology, JBL/Jabil, Sanmina, Flex, InnoLight Technology Suzhou, Celestica, Benchmark Electronics, Venture Corporation Limited, Sumitomo Electric, Furukawa Electric, Fujikura).

**Primary-source vault company anchors (4 companies):**

- **[[FN]]** — Session 21 paired ingest baseline (FN 10-K FY2025 + 10-Q Q2 FY2026 + Q2 FY2026 call). Three CPO customer programs disclosed; "far ahead of competitors" Grady rhetorical; OCS engagement; NVIDIA 27.6% + Cisco 18.2% customer concentration.
- **[[LITE]]** — Session 4 ingest baseline (LITE 10-K FY2025 + 10-Q Q2 FY2026 + Q2 FY2026 call). Three-inch InP industry-standard manufacturing; 40% capacity expansion; NVDA $2B equity-plus-purchase March 2026.
- **[[COHR]]** — Session 5 ingest baseline (COHR 10-K FY2025 + 10-Q Q2 FY2026 + Q2 FY2026 call). Six-inch InP device-fabrication advantage at Sherman + Järfälla + Zürich; substrate-to-system vertical integration; Materials segment intersegment role; NVDA $2B equity-plus-purchase + 20-year relationship.
- **[[AAOI]]** — Session 7 ingest baseline (AAOI 10-Q Q3 FY2025 + 10-K FY2025 + Q4 FY2025 call). Sugar Land TX MBE+MOCVD InP/GaAs laser fabrication; tripling InP laser production by mid-2027; Microsoft ~43% customer concentration; Layer 4/5 straddling tension preserved per Session 15.

**Cross-reference vault chokepoint pages:** [[InP-supply]] (Session 13 first canonical chokepoint page); [[datacenter-laser-supply]] (Session 4 chokepoint page); [[optical-dsp-phy-supply]] (Session 30 second canonical multi-source-synthesis chokepoint page); [[wafer-level-siph-test]] (Session 25 provisional chokepoint page).

## Source audit notes

### FN Session 21 ingest reference

Session 21 paired ingest baseline (FN 10-K FY2025 + 10-Q Q2 FY2026 + Q2 FY2026 call). Layer 6 contract manufacturing per `frameworks.md` v9. Customer concentration disclosed: NVIDIA 27.6% + Cisco 18.2% top-2; emerging AWS HPC ramp ($86M Q2 FY2026); LITE 15.4% in FY2023 only (below 10% threshold FY2024-FY2025); COHR not in customer concentration table.

**CPO 3-customer programs Q2 FY2026 call disclosure** — material disclosure from Layer 6 contract manufacturer; enabler-tier perspective parallel to GLW Session 20.

**OCS engagement disclosed** — structurally adjacent to CPO advanced packaging.

**Tier 1/Tier 2 framing gap.** 10-K corporate framing with single mention of "artificial intelligence" (FY2024 narrative; not repeated FY2025) vs Q2 FY2026 call commercial CPO disclosure. Pattern: Layer 6 contract manufacturer breaks CPO silence at Tier 2 venue while Tier 1 filings remain commercially conservative.

**A1 three-mode framing.** FN-side framing of "far ahead of competitors" is over-claim mode (CRDO-style rhetorical claim attributed to Grady); CPO 3-customer programs with names not disclosed is counterparty-attribution-only mode (FN-side disclosure without bilateral customer-side primary-source confirmation in this Session 31 scope).

### LITE Session 4 ingest reference

Session 4 ingest baseline (LITE 10-K FY2025 + 10-Q Q2 FY2026 + Q2 FY2026 call). Layer 4 specialized component supplier; photonics_tier 3 per Session 5 cross-validation. Three-inch InP industry-standard manufacturing per silicon-photonics-primer.md cross-validation; 40% capacity expansion target per Q2 FY2026 call. NVDA $2B equity-plus-purchase + capital-offset-for-supply-assurance relationship framing March 2026.

**[[datacenter-laser-supply]] chokepoint provisional creation at Session 4** anchored on LITE sources; substantiated by COHR Session 5 cross-validation. This chokepoint page (Session 31) is structurally adjacent — laser supply (datacenter-laser-supply.md) and advanced optical packaging (this page) feed into different stages of optical module integration.

### COHR Session 5 ingest reference

Session 5 ingest baseline (COHR 10-K FY2025 + 10-Q Q2 FY2026 + Q2 FY2026 call). Layer 4 with photonics_tier 2 placement per Session 5 codification (placed Tier 2 rather than Tier 4 based on primary-source evidence of structural position closer to "chokepoint participant" than "differentiated supplier"). Six-inch InP device-fabrication advantage at Sherman + Järfälla + Zürich; >4x chips at <50% cost vs three-inch. Substrate-to-system vertical integration spanning + Materials segment intersegment role unique in vault. NVDA $2B equity-plus-purchase + 20-year relationship March 2026.

**Six-inch InP "monopoly" framing refined per silicon-photonics-primer.md cross-validation** — substrate-level monopoly framing not accurate (Sumitomo, AXT, IQE all have six-inch InP substrate or epitaxial capability); device-fabrication position confirmed as structurally significant. Refinement preserved per Session 5 codification + this Session 31 chokepoint page.

**Anderson "demand absorbs all of that capacity and then some" cross-validation** — supply constraint extending through at least 2027 confirmed across LITE + COHR primary sources.

### AAOI Session 7 ingest reference

Session 7 ingest baseline (AAOI 10-Q Q3 FY2025 + 10-K FY2025 + Q4 FY2025 call). Layer 5 transceiver assembler with Layer 4/5 straddling tension preserved per Session 15 codification. Sugar Land TX MBE+MOCVD InP/GaAs laser fabrication; tripling InP laser production by mid-2027; "more than 95% of laser will be AI laser by end of year" Thompson Lin Q4 FY2025 call (rhetorical). Microsoft ~43% top customer concentration; top 2 = 81.9%.

**CPO displacement analysis section codified at Session 7** — asymmetric exposure framing preserved (module business displacement risk + laser business opportunity); management highlights only the second dynamic.

**Technology alternatives silence (LPO/NPO/CPC)** observation preserved per Session 7 Source audit notes — AAOI discusses none of these alternatives in any source; absence is meta-signal.

**Prysm silicon photonics hypothesis falsified per Session 7** — kickoff hypothesis not confirmed by primary sources.

### A6 v8 Phase 0 verification — no new gap pattern instances

Per CLAUDE.md v8 A6 application discipline: 8 pattern types verified PASS at Phase 0. (g)/(g)' subtype instance count unchanged at 5 accumulated through Session 30 (Session 26 addendum + Session 27 + 3 Session 30 instances). Codification refinement to (g)/(g)' subtypes remains triggerable per Session 30 reflection but no Vic-side decision yet to canonicalize.

**Kickoff hypothesis falsification status: zero falsifications surfaced.** Session 31 kickoff was less prescriptive (didn't pre-commit specific product/acquisition names); agent-driven Phase 0 vault exploration verified canonical content directly. Pattern: high-level prompts that defer product/acquisition naming to Phase 0 verification produce zero (g) subtype instances vs detailed prompts that pre-commit names (Session 27 Hyperlume vs Comira; Session 30 Sian3/Spica/Acacia). Worth tracking as kickoff-drafting discipline observation.

## MKSI MSD chemistry + PSD photonics electronics & packaging participant (S75 NEW analytical product propagation)

**[[MKSI]] enters advanced-optical-packaging chokepoint scope at S75 first canonical creation per [[MKSI]] standalone ingest (2026-05-21).** 8th canonical participant at this chokepoint scope post-S68 6-canonical baseline + S73 NOK 7-canonical expansion. **First-vault-scope-decision candidate** per Section 1.2 ongoing scope expansion mechanism. **FIRST multi-domain F5 + F8 + F9 simultaneous placement vault canonical** (Layer 4 + photonics_tier 3 + equipment_tier 2 + materials_tier 3) — participant scope at this chokepoint via BOTH MSD chemistry (F9 materials_tier 3 UPWARD reframing) AND PSD photonics (F5 photonics_tier 3 lithography subsystem) cross-Division participation.

**MSD chemistry "market leader bonding chemistry" substantive participation evidence:**

Lee Q1 2026 earnings call (May 7, 2026) explicit (verified at primary; analyst Melissa Weathers Q&A on warpage + glass cores topic): *"every time there's a technical problem, it's also an opportunity, and we at MKS certainly love those opportunities... we are one of the market leaders in the chemistry needed to bond layers to each other. We don't talk about that too much. We usually talk about plating and putting the copper lines in, but obviously bonding the layers together is also something difficult and also a big contributor to yield."*

MKSI 10-K Item 1 Business explicit: MSD **"chemistry, equipment and services for innovative and high-technology applications in our electronics and packaging and specialty industrial markets"** + **"advanced surface modification, electroless and electrolytic plating, surface finishing, functional coating and corrosion resistance applications"** + **"flexible interconnect PCB processing systems and high-density interconnect (HDI) solutions for the creation of blind micro-vias necessary for the manufacturing of PCBs"** — substantive PCB + substrate chemistry chokepoint participant scope at electronics & packaging chemistry sub-domain.

**Q1 2026 E&P substantiation:** $321M (+27% YoY); chemistry sales +22% YoY constant currency (ex-FX + palladium passthrough); AI = 15% of chemistry revenue (Lee Q1 2026 call quantified disclosure). MSD HIGHEST gross margin Division (54.1% FY2025) — substantive moat depth at electronics & packaging chemistry scope. Atotech-origination (closed August 17, 2022); mixed-outcome honest framing per S75 (market position SUCCESS + acquisition cost FAILURE per 2023 $1.9B impairment + capital structure overhang per 3.5x EBITDA net leverage).

**PSD photonics packaging adjacency:** Newport-branded photonics applications at lithography + metrology + inspection scope; Newport ULTRAlign fiber alignment stage at datacom optical-to-electronic conversion test scope; ultrafast lasers for back-end semi applications; "Optimize the Interconnect®" combined laser drilling + chemistry cross-Division offering (Surround the Workpiece extension).

**Cross-vault advanced optical packaging chokepoint participant scope expansion (8-canonical post-S75):**

| Vault entity | Layer | photonics_tier / materials_tier | Sub-variant scope at chokepoint |
|---|---|---|---|
| [[FN]] | 6 | photonics 4 (cross-domain) | Pure contract manufacturing; NVIDIA 27.6% + Cisco 18.2% top-2 |
| [[LITE]] | 4 | photonics 3 | 3-inch InP industry-standard manufacturing; NVDA $2B equity |
| [[COHR]] | 4 | photonics 2 | 6-inch InP device-fabrication advantage; broadest vertical integration |
| [[AAOI]] | 5 | photonics 5 | Layer 5 transceiver assembler with Layer 4 in-house laser straddling |
| [[TSEM]] | 2 | photonics 2 | Specialty foundry SiPh PDK (Israeli FPI) |
| [[ANET]] | 5 | photonics 5 | XPO Extended Pluggable Optics module-form-factor adjacency |
| [[NOK]] | 4 | photonics 2 | Pennsylvania photonics packaging project + 4 new DSPs OFC March 2026 |
| **[[MKSI]] S75** | **4** | **photonics 3 + materials 3** | **MSD chemistry market leader bonding chemistry + PSD photonics packaging applications; FIRST canonical with TWO substantive `*_tier` fields at this chokepoint** |

**Honest framing:** MKSI brings a NEW dimension to the chokepoint scope — chemistry-layer participation (PCB/substrate bonding chemistry; Atotech-origination) complementing prior 7-canonical photonics-layer + packaging-layer participation. Cross-Division integrated participation methodology candidate per Tranche 2C.

## Change log

- **2026-05-21 (Session 75 minimal cross-reference — [[MKSI]] standalone first canonical ingest propagation):** Frontmatter tickers expansion 7 → 8 ([FN, LITE, COHR, AAOI, TSEM, ANET, NOK, **MKSI**]) per Section 3.2 (b) multi-ticker provenance discipline. NEW substantive subsection "MKSI MSD chemistry + PSD photonics electronics & packaging participant (S75 NEW analytical product propagation)" added per S55/S59/S68 propagation pattern + S75 reserve scope. MKSI 8th canonical at chokepoint scope post-S73 NOK 7-canonical baseline; FIRST multi-domain F5 + F8 + F9 simultaneous placement vault canonical; FIRST canonical with TWO substantive `*_tier` fields at this chokepoint scope (photonics_tier 3 PSD + materials_tier 3 MSD); MSD chemistry "market leader in chemistry needed to bond layers" verified at primary (Lee Q1 2026 call explicit on bonding chemistry adjacency to advanced packaging warpage + glass cores topic); E&P Q1 2026 +27% YoY substantive AI advanced PCB manufacturing demand; Atotech-origination chemistry scope (mixed-outcome honest framing per Vic refinement #2 at S75: market position success + acquisition cost failure + capital structure overhang). last_updated 2026-05-19 → 2026-05-21. No other content edits per scope discipline.
- **2026-05-19 (Session 73 minimal cross-reference — [[NOK]] standalone first canonical ingest propagation):** Frontmatter tickers expansion 6 → 7 ([FN, LITE, COHR, AAOI, TSEM, ANET, **NOK**]) per Section 3.2 (b) multi-ticker provenance discipline. NEW substantive subsection "NOK Pennsylvania photonics packaging project + OFC March 2026 DSP roadmap adjacency (S73 NEW analytical product propagation)" added per Vic adjustment #2 cross-reference scope expansion at S73 reserve scope. NOK adjacent at photonic packaging chokepoint scope via Pennsylvania photonics packaging and testing project disclosure (NOK 20-F FY2025 Property, plant and equipment Note 4.2) + 4 new DSPs OFC March 2026 + Building Block architecture (4 optical engines vs prior 2 engines) + 800G ZR/ZR+ coherent pluggables shipping + InP manufacturing San Jose Fab 2 ramping later 2026; first foreign-issuer first canonical participant at this chokepoint; substantive bilateral verification candidate at Optical Networks integrated systems sub-domain (structurally distinct from FN/LITE/COHR/AAOI/TSEM/ANET pre-S73 chokepoint participant scope). Cross-vault OFC March 2026 announcement scope methodology candidate strengthens at NOK + ANET 2-canonical OFC March 2026 announcement scope at vault chokepoint participant scope. last_updated 2026-05-15 → 2026-05-19. No other content edits to this chokepoint page (substantive bilateral analytical product completion deferred to future dedicated NOK refresh OR chokepoint refresh).
- **2026-05-15 (Session 68 1-stop chokepoint refresh — FIFTH 1-stop chokepoint refresh in vault history post-S51+S65+S66+S67 precedents; FOURTH consecutive major-chokepoint full refresh; SECOND refresh with substantive tickers expansion post-S67 precedent (4 → 6 participants); HISTORIC same-day refresh-heavy day at 5 chokepoint sessions; 1-stop refresh protocol durability VALIDATED at 5-instance threshold):** 5 escalation triggers: 4 NEGATIVE + 1 POSITIVE (new canonical participant addition — Vic approval gate; **Option (a) tickers expansion approved**). Substantive additions ~115 lines (334 baseline → ~449 final). **Tickers expansion 4 → 6 participants** — added [[TSEM]] (Layer 2 SiPh PDK foundry wafer-tier vertical integration reference-design supplier complementarity 5th pattern per S62) + [[ANET]] (Layer 5 XPO Extended Pluggable Optics finished-module form factor adjacency 6th pattern per S55 Bechtolsheim OFC keynote). **FOUR NEW substantive sections delivered:** (1) **Vertical integration pattern distinction (4 → 6 patterns post-S68)** — updated structural anchor table with TSEM foundry-tier + ANET module-form-factor patterns; (2) **NVDA $2B equity-plus-purchase materialization at LITE+COHR (S50 NEW propagation at packaging scope)** — LITE $2.02B + COHR $2B equity + multibillion-dollar multi-year CPO supply + Sherman TX 6-inch InP tied to NVDA + Multi-Rail + Thermadite XPU cooling NEW segments + Zürich 3rd 6-inch site + Greensboro NC 5th InP fab + Google explicit named; differential structural commitment substantiation validates Murphy scale-up bifurcation thesis at supplier-tier capacity commitment scale; (3) **FN Raytec wafer-level packaging investment (S59 NEW elevation)** — $32M / 14% stake at Taiwan wafer-level packaging; FN Layer 6 enabler-tier evolution to integrated-precision-optical-packaging participation; FIRST FN vertical integration evolution since canonical creation; two datacom transceiver programs shipping directly to hyperscale customer at S59; DCI record $197M (+90% YoY); methodology candidate Tranche 2C; (4) **ANET XPO finished-module form factor adjacency (S55 NEW)** — 12.8 TB/module + 204.8 TB/OCP rack unit + 400W cooling + >100 vendor endorsement + 10-year run via Bechtolsheim OFC; pluggable-retention thesis at higher bandwidth/density vs CPO co-packaged displacement; cross-vault three pluggable-retention data points (COHR Anderson scale-out/scale-up + Murphy MRVL bifurcation + ANET XPO 10-year run). **Section 4.6 ROI VALIDATED at 0 falsifications (23-instance zero-falsification streak post-S46).** A6 (g)/(g') UNCHANGED at 8+2=10. Cross-vault NVIDIA partnership pattern UNCHANGED at 4 T1 + 7 T2 (LITE + COHR + ANET + TSEM reinforced via S68 propagation; no new T1 verification). **1-stop refresh protocol durability VALIDATED at 5-instance threshold + second-substantive-tickers-expansion scope** — Tranche 2C codification candidate. **Fourth downstream propagation cycle test of [[nvidia-supply-chain-commitments]] S53 at chokepoint scope** — methodology durability VALIDATED at 4-instance threshold (S65+S66+S67+S68). Wikilink-clean streak: **51 sessions** post-S68. Files updated: 6 files (advanced-optical-packaging.md substantive refresh + TSEM.md cross-ref + ANET.md cross-ref + FN.md cross-ref + index.md + log.md; under hard cap 7). LITE+COHR cross-refs deferred per S66+S67 same-day propagation already covered. **Same-day refresh-heavy session count: 5** (S64 + S65 + S66 + S67 + S68 today) — HISTORIC vault refresh-heavy day; vault canonical photonics chokepoint refresh trio (datacenter-laser-supply + cpo-integration + advanced-optical-packaging) COMPLETED post-S68.
- **2026-04-30 (Session 31 multi-source synthesis — closes Tier 3 framework Chokepoint 5 dedicated chokepoint page coverage gap):** Created from four vault primary-source company anchors per Session 25 hybrid architecture three-source threshold satisfaction (multi-fold): [[FN]] Session 21 ingest baseline (Layer 6 contract manufacturing); [[LITE]] Session 4 ingest baseline + Session 5 cross-validation (Layer 4 / photonics_tier 3 component supplier with internal packaging); [[COHR]] Session 5 ingest baseline (Layer 4 / photonics_tier 2 broadest vertical integration); [[AAOI]] Session 7 ingest baseline (Layer 5 transceiver assembler with Layer 4/5 straddling tension preserved per Session 15 codification). **Third canonical multi-source-synthesis chokepoint page in vault history** (after [[InP-supply]] Session 13 and [[optical-dsp-phy-supply]] Session 30). **First chokepoint page operating under canonical CLAUDE.md v8 + frameworks.md v9 + chokepoint-table v2** post-Session-30 framework synthesis refinement. **A2 fourth canonical application** (after Session 25 theme page; Session 30 chokepoint page; Session 28 adjacent application). Per-company depth allocation: FN ~85 lines + LITE ~80 lines + COHR ~85 lines + AAOI ~75 lines + cross-company synthesis sections (~120 lines). A6 v8 (g)/(g)' subtype instance count unchanged at 5 accumulated through Session 30 — kickoff was less prescriptive (no product/acquisition pre-commitment); zero new falsifications. Forward-wikilink discipline preserved: 17-session vault wikilink-clean streak post-Session 31 (extended from 16 post-Session 30). Per A2 structural requirements: Tier 3 source attribution at page-top + per-section + Source attribution + Source audit notes; counterparty-attribution-only annotation for non-vault company references (ASE Technology, Amkor Technology, JBL/Jabil, Sanmina, Flex, InnoLight Technology Suzhou, Celestica, Benchmark Electronics, Venture Corporation Limited, Sumitomo Electric, Furukawa Electric, Fujikura). Honest-verdict discipline applied to: 4 vertical integration patterns (no forced winner); six-inch vs three-inch InP asymmetry (refined "monopoly" framing per Session 5); AAOI Layer 4/5 straddling preserved (no silent tier upgrade per Session 15); FN enabler-tier framing parallel to GLW (Session 20 precedent).
- **2026-04-30 (Session 32 cross-reference — [[cpo-integration]] chokepoint page creation):** Cross-referenced from new chokepoint page [[cpo-integration]] (fourth canonical multi-source-synthesis chokepoint page in vault history; closes Tier 3 framework Chokepoint 10 dedicated chokepoint page coverage gap). FN + LITE + COHR + AAOI advanced optical packaging mechanics + 4 vertical integration patterns + ELS architecture + Layer 4/5 straddling at AAOI cross-referenced from [[cpo-integration]] per-company integration positioning sections (Tier B: LITE/COHR/AAOI ~35-40 lines each) + Value chain shift dynamics component-tier value capture subsection. Adjacent chokepoint dependency documented in [[cpo-integration]] Cross-chokepoint dependencies section: yield + alignment + thermal control mechanics common to all CPO assembly. **S27-S32 photonics chokepoint completion arc closed** (3 dedicated chokepoint pages: Chokepoint 2 Session 30 + Chokepoint 5 Session 31 + Chokepoint 10 Session 32). No content edits to this chokepoint page.
- **2026-05-24 (Session 85b 1-file completion post-S85 deferral per context budget escape valve):** Added NVDA Q1 FY2027 venue-specific pattern observation at CPO advanced packaging implications section. Q1 FY2027 zero advanced packaging mentions reinforces GTC-vs-earnings-call venue-specific disclosure pattern. Cross-venue gap convention 3rd instance MET per Section 3.6 codification threshold (Tranche 2C-ii flag at S86). Vera Rubin Q3 2026 demand pull cross-references to [[TSMC-CoWoS]] S84 + [[NVDA-platform-integration]] S82 COUP modality. Frontmatter NVDA added per Section 3.2(b) provenance. Closes S85 4-file MEDIUM-tier propagation batch (S85 = 3 of 4; S85b = 4th).
- **2026-04-30 (Session 33 cross-reference — [[InP-supply]] provisional → canonical promotion):** Adjacent chokepoint page [[InP-supply]] promoted from provisional to canonical multi-source-synthesis chokepoint page via Option C bifurcation handling — single page covers Tier 3 framework Chokepoint 3 (InP substrate supply) + Chokepoint 4 (InP epitaxial capacity) with internal subsection structure. **Fifth canonical multi-source-synthesis chokepoint page in vault history** (after [[optical-dsp-phy-supply]] Session 30, [[advanced-optical-packaging]] Session 31, [[cpo-integration]] Session 32). InP supply chain (substrate-tier AXTI + epitaxial-tier equipment VECO + epitaxial-tier device-fabrication COHR/LITE/AAOI) feeds laser device fabrication upstream of advanced optical packaging documented at this chokepoint page. Three Layer 4 InP wafer-size positions (COHR six-inch device-fabrication advantage / LITE three-inch industry-standard / AAOI Sugar Land MBE+MOCVD dual-process) preserved without forced winner attribution per honest-verdict discipline at both [[InP-supply]] and this chokepoint page. No content edits to this chokepoint page.
