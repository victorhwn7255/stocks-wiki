---
type: theme
tickers: [NVDA, AVGO, MRVL, CSCO, AEHR, AXTI, COHR, LITE, AAOI, ALAB, FN, GLW, VRT, ONTO, VECO, TSM, COHU, CRDO, ANET, VIAV]
last_updated: 2026-04-28
---

# Chokepoint Investability Priorities — 13-Chokepoint AI Photonics Framework

*Tier 3-anchored theme page per CLAUDE.md v7 A2 convention. Content sourced from `raw/research/photonics-chokepoint-table.md` (Vic-team-authored chokepoint research framework). Per A2 structural requirement 3: claims included with attribution at construction; deviation-based refinement at future primary-source ingest sessions per A1 three-mode framing. Per A2 structural requirement 2: claims about non-vault companies in over-claim mode annotation pending future primary-source cross-validation. Most chokepoints have not yet undergone primary-source cross-validation cycles; over-claim mode annotation applies pending future ingest sessions.*

## Overview

Vault-canonical reference for the 13-chokepoint AI photonics framework anchored on `raw/research/photonics-chokepoint-table.md`. The framework characterizes the AI datacenter photonics supply chain as 13 chokepoints (with rank ordering and conviction levels) plus 5 portfolio thematic baskets organizing investment exposure.

The framework's analytical lens distinguishes two structural categories: **bottleneck participation** (supply-side scarcity creating capacity constraints) and **control-point participation** (architectural decision authority shaping ecosystem value capture). Per `frameworks.md` v8 Framework 2.6 (Control-point analysis, supplemental to value capture layers): control-point analysis captures *whether* a company at a given layer shapes architectural decisions that determine where ecosystem value accrues; Framework 2 layer placement captures *where* in the value chain a company operates. The two are complementary axes. Chokepoint 7 (Switch ASIC / platform architecture) is the framework's most explicit control-point chokepoint; see [[NVDA-platform-integration]] for the six-modality NVDA control-point framing and Framework 2.6 for canonical analytical text.

**Chokepoint sections below are ordered by Tier 3 Ranking Summary (Rank 1 to Rank 13) for analytical priority.** Per-section depth weighted by rank: Ranks 1-5 receive deeper treatment (~50 lines each); Ranks 6-10 receive medium treatment (~35-40 lines); Ranks 11-13 receive concise treatment (~30 lines).

The 13 chokepoints span six analytical categories (supplemental analytical lens, not section ordering):

- **Optical device manufacturing** (Chokepoints 1, 2, 5: Lasers/EMLs/III-V; Optical DSP/PHY; Advanced optical packaging)
- **Material substrate and equipment** (Chokepoints 3, 4: InP substrate supply; InP epitaxial capacity)
- **Test infrastructure** (Chokepoints 6, 8: Finished-module optical test; Wafer-level SiPh reliability test)
- **Architecture & platform control** (Chokepoint 7: Switch ASIC / platform architecture)
- **Foundry & advanced packaging** (Chokepoints 9, 10: Silicon photonics foundry/PIC capacity; Photonic advanced packaging/CPO integration)
- **Physical attach & infrastructure** (Chokepoints 11, 12, 13: Fiber/connectors; Thermal infrastructure; Board/package power delivery)

Per Session 24 selective integration outputs (carry-overs reflected in chokepoint sections below):
- **Integration 1 (Control-point distinction):** Chokepoint 7 references control-point distinction sections on [[NVDA]], [[AVGO]], [[MRVL]], [[CSCO]] per Session 24, plus `frameworks.md` v8 Framework 2.6 canonical content.
- **Integration 2 (InP substrate two-layer reconciliation):** Chokepoint 3 references two-layer InP supply distinction (indium feedstock layer / JX Advanced Metals dominant; InP wafer production layer / AXTI significant) per [[datacenter-photonics-supply-chain]] Section 2.9.
- **Integration 3 (CPO chokepoint structural split):** Chokepoints 9 and 10 reflect foundry-layer ([[TSM]] COUPE, GFS Fotonix, Tower SiPh) vs OSAT-layer (ASE Technology, Amkor Technology) structural distinction per [[datacenter-photonics-supply-chain]] Sections 2.6 and 2.7.

## Chokepoint 1 — Lasers / EMLs / III-V devices (Tier 3 Rank 1)

**Conviction:** Very high. **Framework characterization:** *"Top-tier photonics chokepoint."* The most direct optical bottleneck for 800G / 1.6T / CPO scaling.

### Why it matters

The light source gates the optical link. 800G / 1.6T modules and future CPO optical engines need lasers and EMLs with high optical power, low noise, tight wavelength control, long-term reliability, and acceptable thermal behavior. A weak light-source supply chain can constrain the entire optical module ramp.

As lane speeds rise toward 200G/lane and beyond, optical margins tighten. The laser/EML must operate reliably inside thermally constrained modules or optical engines while maintaining signal quality. Reliability matters more because failures at scale can be expensive in hyperscale AI clusters. This is one of the cleanest AI datacenter photonics bottlenecks because it maps directly to volume ramps in 800G, 1.6T, LPO/LRO/NPO, and CPO architectures.

### Best listed exposure

- **[[LITE]]** — vault company. Per `frameworks.md` v7 Layer 4, photonics_tier 3. Highest-quality US-listed broad photonics exposure with [[COHR]]. NVDA $2B equity investment March 2026 per [[NVDA-platform-integration]] reciprocal-confirmation modality (sixth modality, Session 22 codification).
- **[[COHR]]** — vault company. Per `frameworks.md` v7 Layer 4, photonics_tier 2. Six-inch InP wafer device-fabrication advantage per Session 5 ingest. NVDA $2B equity investment March 2026.
- **MTSI / MACOM** — non-vault. Tier C future-ingest candidate per [[datacenter-photonics-supply-chain]] Future ingest candidates. Framework characterization: "more specialized and differentiated through analog/RF/optoelectronic components." Over-claim mode annotation pending primary-source verification.
- **[[AAOI]]** — vault company. Per `frameworks.md` v7 Layer 5, photonics_tier 5. Higher-beta with more customer and execution risk per framework. Layer 4/5 straddling tension documented Session 7.

### Editorial assessment (per Tier 3 source)

Top-tier photonics chokepoint. [[LITE]] and [[COHR]] are the highest-quality US-listed broad photonics exposures. MTSI is more specialized and differentiated through analog/RF/optoelectronic components. [[AAOI]] is higher-beta, with more customer and execution risk.

Cross-validated chokepoint substantiation per [[datacenter-laser-supply]]: LITE + COHR same-quarter testimony (Q2 FY2026 calls February 3-4, 2026); InP wafer fab fully allocated; ~25-30% supply-demand imbalance; all EML capacity spoken for through calendar 2027; NVDA $4B combined equity investment as platform-side demand confirmation. The chokepoint is operationally validated, not just framework-asserted.

*(Investment idea per Tier 3 source: LITE/COHR are quality bottleneck exposures; MTSI is a differentiated component play; AAOI is a high-beta transceiver/laser execution play. Investment-idea content positioning deferred to Vic-side decision per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

Hyperscaler purchase agreements; Nvidia-related commitments; 800G/1.6T revenue mix; laser gross margins; customer concentration; yield ramp; pricing pressure from Asian suppliers.

### Cross-references

- [[datacenter-laser-supply]] — vault chokepoint page documenting cross-validated supplier-side scarcity
- [[NVDA-platform-integration]] — six-modality framing including March 2026 LITE/COHR equity-plus-purchase-commitment modality
- [[CPO-platform-battle]] — five-way executive comparison includes scale-up CPO laser demand framing
- [[LITE]], [[COHR]], [[AAOI]] — vault company pages

## Chokepoint 2 — Optical DSP / PHY power-performance (Tier 3 Rank 2)

**Conviction:** Very high. **Framework characterization:** *"Top-tier chokepoint; MRVL/AVGO primary."* High-value semiconductor layer where power/performance defines module feasibility.

### Why it matters

The digital electronics determine whether the optical link is practical. PAM4 optical DSPs, PHYs, SerDes, FEC, equalization, clock recovery, and diagnostics determine whether 200G/lane and 1.6T modules can hit performance targets inside strict power and thermal budgets.

The optical module cannot simply scale bandwidth without increasing signal-processing complexity. Higher lane speeds increase loss, noise, jitter, and error-correction requirements. The DSP has to recover the signal while consuming as little power as possible. This is a high-value semiconductor layer with stronger potential value capture than many module-level businesses — DSP/PHY suppliers can capture architectural value even when module assembly margins compress.

### Best listed exposure

- **[[MRVL]]** — vault company. Per `frameworks.md` v7 Layer 3 (Layer 3→2 trajectory in progress), photonics_tier 3. Primary optical DSP/PHY incumbent per framework. Custom ASIC + DSP/PHY participation; control-point aspirations via Celestial Photonic Fabric per Session 24 Integration 1.
- **[[AVGO]]** — vault company. Per `frameworks.md` v7 Layer 1 with Layer 1/3 straddling tension, photonics_tier 3. Primary optical DSP/PHY incumbent per framework. "We are the only one out there at 1.6T DSP" (Hock Tan, AVGO Q1 FY2026 call). Control-point with bottleneck participation per Session 24 Integration 1.
- **[[CRDO]]** — vault company (Session 27 paired ingest with [[ANET]]). Per `frameworks.md` v8 Framework 2.6: bottleneck-tier with control-point aspirations (alongside [[MRVL]] at smaller operational scale). 1.6T AEC franchise + Optical PAM4 DSPs + PCIe Gen6 retimers + SerDes Chiplets + three new TAM expansions (ZeroFlap optics with embedded telemetry; ALCs via Hyperlume MicroLED acquisition; OmniConnect/Weaver gearboxes). FY2025 revenue $436.8M (+126% YoY); Q3 FY2026 standalone $407M (+>200% YoY). Customer concentration broadening (Customer A 67% FY2025 → 48% Q3 FY2026 contracting; Customer B emerged 39% Q3). UALink/ESUN/Ethernet protocol participation across product lines. Confidence MEDIUM-HIGH per Session 27 framework verification.
- **MXL / MaxLinear** — non-vault. Tier C future-ingest candidate. Smaller-cap DSP with execution risk. Over-claim mode annotation pending primary-source verification.

### Editorial assessment (per Tier 3 source)

Top-tier chokepoint; [[MRVL]] / [[AVGO]] primary. [[CRDO]] (vault post-Session 27) and MXL are more high-beta challengers or adjacent connectivity plays. This layer is both a technical bottleneck and an economic value-capture point.

Per [[NVDA-platform-integration]] control-point thread (Session 22 sixth modality): MRVL/AVGO are the second strongest strategic control-point names in vault per `frameworks.md` v8 Framework 2.6. Bottleneck participation in optical DSP/PHY is operationally distinct from control-point authority — Chokepoint 7 (Switch ASIC / platform architecture) covers control-point analytical thread directly.

**Three primary-source vault coverage post-Session 27.** CRDO joins MRVL (Session 9) and AVGO (Session 10) as third primary-source vault company at this chokepoint. Triangulation of Optical DSP/PHY positioning across three vault sources now possible: AVGO 1.6T DSP leadership claim ("we are the only one out there at 1.6T DSP" — Hock Tan); MRVL Spica 1.6T DSP from Inphi acquisition with Celestial Photonic Fabric platform-tier ambition; CRDO 1.6T AEC + Optical DSPs with mature node n-1 advantage and AEC franchise differentiation. Three-source threshold satisfied per Session 25 hybrid architecture; dedicated `optical-dsp-phy-supply.md` chokepoint page candidacy assessment scheduled per S27-S30 photonics completion arc plan.

*(Investment idea per Tier 3 source: MRVL/AVGO are core architecture-enabling names; CRDO/MXL offer more upside if they gain share or benefit from LPO/LRO/AEC/SerDes transitions. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

Watts per 1.6T module; 200G/lane design wins; 3nm/5nm transitions; LPO/LRO displacement risk; hyperscaler qualification; SerDes attach rate; FEC/BER performance.

### Cross-references

- **[[optical-dsp-phy-supply]]** — second canonical multi-source-synthesis chokepoint page (Session 30; closes Chokepoint 2 dedicated chokepoint page coverage gap per S27-S30 photonics completion arc). Provides chokepoint-specific synthesis depth complementing this theme page's 13-chokepoint breadth. Multi-source synthesis across [[MRVL]] + [[AVGO]] + [[CRDO]] per Session 25 hybrid architecture three-source threshold satisfaction.
- [[NVDA-platform-integration]] — six-modality framing; control-point thread spans NVDA, AVGO, MRVL, CSCO, [[ANET]] in-vault complete (Session 27)
- [[CPO-platform-battle]] — five-way executive comparison including Murphy ↔ Hock Tan scale-up technology disagreement
- [[MRVL]], [[AVGO]], [[CRDO]] — vault company pages with control-point distinction sections (Session 24 Integration 1 + Session 27 paired ingest)

## Chokepoint 3 — InP substrate supply (Tier 3 Rank 3)

**Conviction:** High. **Framework characterization:** *"Real chokepoint; highest geopolitical risk. Qualify 60-70% claim."*

### Why it matters

Foundational upstream material for III-V photonics. Indium phosphide (InP) substrates are used to build high-performance photonic devices including lasers, EMLs, photodiodes, and compound-semiconductor optical components. Substrate availability constrains downstream laser and optical-device output regardless of 800G / 1.6T / CPO demand.

InP is a specialized substrate market with fewer qualified suppliers than mainstream silicon wafers. AI datacenter optical demand pulls demand upstream into substrates. Qualification cycles are long because customers need consistency, defect control, and reliability across wafers.

### Best listed exposure

- **[[AXTI]]** — vault company. Per `frameworks.md` v7 Layer 6 (substrate manufacturing), photonics_tier 3. Closest US-listed InP substrate exposure but not a clean "low-risk bottleneck" because operational footprint and customer base carry China-related risk. AXTI 60-70% claim per Tier 3 source over-claim mode pending future primary-source verification — see [[AXTI]] Open question #7 for two-layer reconciliation framework with JX Advanced Metals 78% claim.
- **[[COHR]]** — vault company. Per `frameworks.md` v7 Layer 4, photonics_tier 2. Broader vertical photonics exposure with partial integration; not a pure substrate stock. Vault canonical six-inch InP wafer device-fabrication advantage per Session 5 ingest.
- **JX Advanced Metals** — non-vault. Tier A future-ingest candidate per [[datacenter-photonics-supply-chain]] Future ingest candidates section. Indium feedstock dominance (~78% global share per Session 19 architecture primer) — over-claim mode annotation pending primary-source verification. Japan-headquartered without US listing; ingest mechanics challenging.
- **Sumitomo Electric** — non-vault. Framework-named with over-claim mode annotation pending future primary-source verification.

### Editorial assessment (per Tier 3 source)

Real chokepoint with highest geopolitical risk in the framework's chokepoint set. Two-layer InP supply distinction documented per Session 24 Integration 2: indium feedstock layer (JX Advanced Metals dominant) vs. InP wafer production layer (AXTI significant). The two claims address different layers and are not contradictory at face value. Both treated as over-claim mode per A1 three-mode framing convention pending future primary-source cross-validation.

*(Investment idea per Tier 3 source: AXTI as high-beta upstream scarcity play; COHR as broader photonics exposure with partial vertical integration. Investment-idea content positioning deferred to Vic-side decision per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

China export controls; InP wafer pricing; AXTI backlog; customer concentration; qualification delays; capacity-expansion timing; gross margin sensitivity.

### Cross-references

- **[[InP-supply]]** — fifth canonical multi-source-synthesis chokepoint page (Session 33 promotion from provisional; Option C bifurcation handling — single page covers Chokepoint 3 substrate-tier + Chokepoint 4 epitaxial-tier with internal subsection structure preserving framework distinction; mirrors Session 32 [[cpo-integration]] Scale-up + Scale-out CPO precedent). Multi-source synthesis across [[AXTI]] (substrate-tier core) + [[VECO]] (epitaxial-tier equipment) + [[COHR]] + [[LITE]] + [[AAOI]] (epitaxial-tier device-fabrication). Substrate-tier subsection preserves Session 13 AXTI canonical content.
- [[AXTI]] — vault company page; Open question #7 documents two-claim reconciliation per Session 24 Integration 2
- [[datacenter-photonics-supply-chain]] Section 2.9 — vault canonical framing for two-layer distinction
- [[COHR]] — vault company page; six-inch InP wafer device-fabrication position per Session 5

## Chokepoint 4 — InP epitaxial capacity (Tier 3 Rank 4)

**Conviction:** High. **Framework characterization:** *"Real chokepoint; should sit immediately after substrate."* The bridge between substrate and device.

### Why it matters

Substrate alone is not enough. After the InP wafer exists, high-quality epitaxial layers must be grown before the wafer can become a laser, EML, photodiode, or other III-V photonic device. Epi quality affects device efficiency, reliability, output power, wavelength performance, and yield.

MOCVD capacity, process recipes, uniformity, defect density, and operator know-how determine whether the industry can convert substrate availability into usable laser-device output. Poor epi quality can destroy yield even when substrate supply is adequate. This layer creates both equipment upside and vertically integrated device-manufacturer advantage.

### Best listed exposure

- **[[VECO]]** — vault company. Per `frameworks.md` v7 Layer 3-4, photonics_tier 4. MOCVD process-tool exposure (Lumina+ for arsenide and phosphide epitaxial growth). Per Session 13 ingest: Compound Semiconductor segment $60M FY2025 (~9% of revenue); photonics fit weak relative to broader semi equipment exposure.
- **AIXTRON** — non-vault. Tier C future-ingest candidate. Primary VECO competitor in MOCVD per Session 13 framing. Over-claim mode annotation pending primary-source verification.
- **[[LITE]]** — vault company. Vertically integrated device-manufacturer benefit if epi/device know-how becomes harder to replicate.
- **[[COHR]]** — vault company. Same vertical-integration framing as LITE.
- **MTSI / MACOM** — non-vault. Tier C future-ingest candidate. Over-claim mode annotation pending primary-source verification.

### Editorial assessment (per Tier 3 source)

Real chokepoint; should sit immediately after substrate. This is one of the most underappreciated layers because investors often jump from "substrate" directly to "laser," but epi is the bridge between the two.

Per Session 13 [[VECO]] ingest: VECO's photonics fit is structurally weak relative to broader semiconductor equipment (advanced packaging) exposure. The framework Rank 4 positioning emphasizes the chokepoint dynamic; vault canonical framing emphasizes VECO's broader exposure mix. Both framings are consistent — VECO participates in InP epi via Compound Semiconductor segment but the segment is small relative to total VECO revenue.

*(Investment idea per Tier 3 source: VECO/AIXTRON are picks-and-shovels process-equipment exposures; LITE/COHR/MTSI are device-level beneficiaries if they can convert epi expertise into higher laser yield and reliability. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

MOCVD order momentum; optical communications tool demand; 4-inch vs 6-inch InP transition; epi yield commentary; laser-fab capacity expansion; tool lead times.

### Cross-references

- **[[InP-supply]]** — fifth canonical multi-source-synthesis chokepoint page (Session 33 promotion from provisional; Option C bifurcation handling — Chokepoint 4 epitaxial-tier covered in dedicated subsection within unified InP supply chain framework alongside Chokepoint 3 substrate-tier). Equipment-tier sub-layer (VECO Lumina+ MOCVD; Aixtron primary competitor) + device-fabrication-tier sub-layer (COHR six-inch advantage at Sherman/Järfälla/Zürich; LITE three-inch industry-standard + 40% capacity expansion; AAOI Sugar Land MBE+MOCVD dual-process). Wafer-size transition mechanics (4-inch → 6-inch InP) documented as cross-tier interlocking subsection.
- [[VECO]] — vault company page with Compound Semiconductor segment positioning
- [[LITE]], [[COHR]] — vault company pages with vertical integration framing
- [[AAOI]] — vault company page; Sugar Land TX MBE + MOCVD dual-process vertical integration per Session 7 + Session 15 Layer 4/5 straddling codification

## Chokepoint 5 — Advanced optical packaging / alignment (Tier 3 Rank 5)

**Conviction:** High. **Framework characterization:** *"Real chokepoint; FN is clean manufacturing exposure."* Yield, optical alignment, and process control determine scale economics.

### Why it matters

Manufacturing yield can become as important as component design. 1.6T modules and CPO optical engines require precise laser attach, lens alignment, fiber coupling, mux/demux integration, thermal control, and calibration. Even if every component works individually, the finished optical assembly can fail if alignment or packaging yield is poor.

Optical packaging is not like ordinary electronic assembly. Tiny misalignments can create insertion loss, coupling loss, degraded signal quality, and field reliability problems. Volume manufacturing needs repeatability, automation, and process discipline. This row captures the "boring but decisive" manufacturing layer.

### Best listed exposure

- **[[FN]]** — vault company. Per `frameworks.md` v7 Layer 6 (scale manufacturing), photonics_tier 4. Cleanest listed precision optical manufacturing / contract manufacturing exposure per framework. Per Session 21 ingest: NVIDIA Corporation 27.6% + Cisco Systems 18.2% top-2 customer concentration; three CPO customer programs disclosed; "far ahead of competitors" in CPO manufacturing positioning per Q2 FY2026 call.
- **[[LITE]]** — vault company. Internal photonic packaging know-how.
- **[[COHR]]** — vault company. Internal photonic packaging know-how.
- **JBL / Jabil** — non-vault. Tier B future-ingest candidate per [[datacenter-photonics-supply-chain]] Future ingest candidates. Over-claim mode annotation pending primary-source verification.
- **ASE Technology** — non-vault. Tier C future-ingest candidate. CPO/advanced-package optionality. Per Session 24 Integration 3: OSAT-layer photonic packaging structurally distinct from foundry layer.
- **Amkor Technology** — non-vault. Tier C future-ingest candidate. CPO/advanced-package optionality. Same Session 24 Integration 3 framing.
- **[[AAOI]]** — vault company. Vertical module execution leverage but higher customer concentration risk per framework.

### Editorial assessment (per Tier 3 source)

Real chokepoint; [[FN]] is clean manufacturing exposure. [[FN]] is the cleanest listed precision optical manufacturing / contract manufacturing exposure. [[LITE]] and [[COHR]] have internal photonic packaging know-how. ASE/AMKR are more CPO/advanced-package optionality names. [[AAOI]] has vertical module execution leverage but higher customer concentration risk.

Per Session 24 Integration 3: framework groups foundry-layer photonic integration ([[TSM]] COUPE, GFS Fotonix, Tower SiPh) with OSAT-level photonic packaging (ASE, AMKR) into single "Photonic advanced packaging / CPO integration" chokepoint (Chokepoint 10 below). Vault structural organization correctly separates these into two layers via [[datacenter-photonics-supply-chain]] Section 2.6 (foundry) vs Section 2.7 (OSAT/assembly).

*(Investment idea per Tier 3 source: FN is the neutral manufacturing bottleneck play; LITE/COHR combine components with process know-how; ASE/AMKR benefit if photonic packaging moves closer to mainstream advanced packaging. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

Module yield; assembly capacity; optical alignment automation; capex expansion; customer mix; Malaysia/Asia manufacturing footprint; CPO packaging wins.

### Cross-references

- [[datacenter-photonics-supply-chain]] Section 2.7 (Assembly / packaging / testing) — vault canonical framing
- **[[advanced-optical-packaging]]** — third canonical multi-source-synthesis chokepoint page (Session 31; closes Chokepoint 5 dedicated chokepoint page coverage gap). Provides chokepoint-specific synthesis depth complementing this theme page's 13-chokepoint breadth. Multi-source synthesis across [[FN]] + [[LITE]] + [[COHR]] + [[AAOI]] per Session 25 hybrid architecture three-source threshold satisfaction (multi-fold).
- [[FN]] — vault company page; Session 21 ingest with NVIDIA/Cisco top customer concentration
- [[LITE]], [[COHR]] — vault company pages with internal photonic packaging know-how
- [[AAOI]] — vault company page with Layer 4/5 straddling tension

## Chokepoint 6 — Finished-module optical test (Tier 3 Rank 6)

**Conviction:** Medium-high. **Framework characterization:** *"Real equipment refresh cycle."* Speed transition creates equipment refresh cycle.

### Why it matters

1.6T creates a test-equipment refresh cycle. Higher-speed modules need validation for BER, TDECQ, eye diagrams, FEC, interoperability, thermal behavior, and compliance. More complex modules require more sophisticated test flows and higher throughput.

Testing can become a manufacturing bottleneck if equipment throughput cannot keep up with module production. At higher speeds, validation complexity rises, and false passes / false failures become more expensive.

### Best listed exposure

- **Keysight (KEYS)** — non-vault. Tier C future-ingest candidate (per Session 24 Integration 4 promotion). Most prominent test name across all three Session 19 reports per [[datacenter-photonics-supply-chain]] Section 2.7. Over-claim mode annotation pending primary-source verification.
- **[[VIAV]]** — vault company (Session 28 paired ingest with [[PLAB]]). Per `frameworks.md` v8 Layer 4 / photonics_tier 4 / Framework 2.6 pure bottleneck participant. **First vault Chokepoint 6 baseline** post-Session 28. Spirent acquisition (HSE + network security + channel emulation testing businesses, closed October 16, 2025; $425M from Keysight Technologies) extended NSE data center ecosystem positioning to ~45% of NSE Q2 FY2026 mix (up from ~40% prior quarter). Multi-quarter visibility extension (one-and-a-half quarters historical → up-to-three quarters ahead) tied to hyperscaler vertical integration patterns. Inertial Labs PNT acquisition (January 2025; $121.7M) extended aerospace/defense exposure to ~15% NSE mix. Confidence MEDIUM-HIGH per Session 28 framework verification.
- **Anritsu** — non-vault. Tier C future-ingest candidate (Session 24 addition). 1.6T module evaluation; 200G/lane sampling oscilloscope. Over-claim mode annotation.

### Editorial assessment (per Tier 3 source)

Real equipment refresh cycle. Keysight, [[VIAV]] (vault post-Session 28), and Anritsu benefit from higher-speed validation needs. TAM may be smaller than components, but the equipment-refresh logic is credible.

**First vault Chokepoint 6 baseline post-Session 28** via [[VIAV]] paired ingest. Vault now holds direct primary-source exposure to finished-module optical test layer; Keysight + Anritsu remain Tier C future-ingest candidates per Session 24 Integration 4 sequencing. Vault learning extends test-equipment ecosystem coverage and complements [[AEHR]]'s structurally distinct wafer-level test positioning per [[wafer-level-siph-test]] — finished-module test is downstream of wafer-level test in the production flow, with different equipment classes and customer profiles. VIAV multi-quarter visibility extension (1-1.5 → 3 quarters per Khaykin Q2 FY2026 call) signals hyperscaler-vertical-integration-driven AI ecosystem demand durability — analytically distinct from AEHR FOX system order acceleration ($14M follow-on AI accelerator order; new hyperscaler customer win on Sonoma platform per [[wafer-level-siph-test]] evidence).

*(Investment idea per Tier 3 source: less glamorous but durable test-equipment exposure to every speed transition. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

1.6T test product launches; optical test orders; module vendor capex; test-throughput bottlenecks; manufacturing test attach rate.

### Cross-references

- [[datacenter-photonics-supply-chain]] Section 2.7 — non-vault test equipment vendors documented
- [[wafer-level-siph-test]] — adjacent test ecosystem framing distinguishing wafer-level from finished-module test

## Chokepoint 7 — Switch ASIC / platform architecture (Tier 3 Rank 7)

**Conviction:** Very high strategic importance. **Framework characterization:** *"Control point, not just bottleneck."* Determines architecture adoption and value-chain allocation.

This chokepoint is the framework's most explicit control-point chokepoint. **See `frameworks.md` v8 Framework 2.6 (Control-point analysis, supplemental to value capture layers) for canonical analytical text** — Vic-side codification per action between Sessions 24 and 25 establishes Framework 2.6 as supplemental analytical axis to layer placement (Framework 2). Per Framework 2.6 five-tier gradation: full control point (NVDA); control point with bottleneck participation (AVGO); bottleneck-tier with control-point aspirations (MRVL); bottleneck participant with platform-tier ambition (CSCO + non-vault ANET); pure bottleneck participant (all other vault companies).

### Why it matters

The platform owner decides the optical architecture. Switch ASIC and networking platform vendors influence whether AI networks use pluggables, LPO, NPO, CPO, optical I/O, Ethernet, or InfiniBand. This determines where value accrues across the supply chain.

Component suppliers do not decide architecture alone. NVDA, AVGO, ANET, CSCO, and MRVL shape roadmaps, reference designs, customer qualifications, and ecosystem standards. Their choices can redirect value from modules toward CPO, from DSPs toward linear optics, or from merchant optics toward proprietary ecosystems.

### Best listed exposure

- **[[NVDA]]** — vault company. Per `frameworks.md` v8 Framework 2.6: full control point. Strongest in vault. CUDA, NVLink, Spectrum-X, Quantum-X define ecosystem direction; CPO/LPO/NPO transitions move on NVDA's roadmap. See [[NVDA-platform-integration]] for six platform integration modalities (Mellanox acquisition; Groq licensing; COHR/LITE equity-plus-purchase; Ayar Labs equity backing; GLW counterparty-attribution-only; VRT reciprocal-confirmation).
- **[[AVGO]]** — vault company. Per `frameworks.md` v8 Framework 2.6: control point with bottleneck participation. Tomahawk switch architecture, custom ASIC programs, Bailly CPO platform decisions; complementary to Layer 1/3 straddling tension flagged in `frameworks.md` Framework 2 Caveat #2.
- **[[ANET]]** — vault company (Session 27 paired ingest with [[CRDO]]). Per `frameworks.md` v8 Framework 2.6: bottleneck participant with platform-tier ambition (alongside [[CSCO]]; framework Tier 3 prior framing confirmed by Session 27 source evidence). Etherlink portfolio (20+ products spanning Scale Up / Scale Out / Scale Across); 7800R AI Spine + 7060 AI Leaf + 7700R4 DES; EOS + NetDL software platform; ESUN founding member + Ultra Ethernet Consortium 1.0 contributor. FY2025 revenue $9.0B (+28.6% YoY); FY2026 guidance $11.25B with $3.25B AI center revenue (raised from $2.75B). Top 2 customer concentration 42% (Customer A 16% + Customer B 26%); 10-15 year top-customer partnerships. Single merchant silicon vendor dependency (likely [[AVGO]] Tomahawk per ecosystem context) explicit in Risk Factors. ZERO CPO mentions in 10-K + Q4 2025 call sample — distinct from [[CSCO]] acknowledged-deferral framing.
- **[[CSCO]]** — vault company. Per `frameworks.md` v8 Framework 2.6: bottleneck participant with platform-tier ambition (same Framework 2.6 tier as [[ANET]] post-Session 27). Silicon One + Acacia capability is real, but acknowledged-deferral CPO position reflects ambivalent platform-tier commitment. CPO acknowledged-deferral distinct from ANET tighter silence pattern.
- **[[MRVL]]** — vault company. Per `frameworks.md` v8 Framework 2.6: bottleneck-tier with control-point aspirations. Photonic Fabric (via Celestial $3.25-5.5B) is genuine platform-tier ambition, but Layer 3→2 trajectory triggers (`frameworks.md` Section 2.5) remain unmet. Aspiration is real, not yet realized.

### Editorial assessment (per Tier 3 source)

Control point, not just bottleneck. [[NVDA]] and [[AVGO]] are the strongest strategic control names. [[ANET]] is the cleanest Ethernet AI networking platform exposure (vault post-Session 27). [[CSCO]] and [[MRVL]] are important secondary architecture names.

Per Session 24 Integration 1 + Session 27: control-point distinction integrated into [[NVDA]], [[AVGO]], [[MRVL]], [[CSCO]], [[ANET]] Thesis role sections. **Five-company analytical thread now in-vault complete** (Session 27 fifth-member completion via [[ANET]] paired ingest). Cross-reference structure on each company page wikilinks to all five members per framework five-company set.

*(Investment idea per Tier 3 source: own the decision-makers rather than only the component suppliers. The risk is that valuation already reflects this strategic control. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

NVDA Spectrum-X / Quantum roadmap; AVGO Tomahawk/CPO roadmap; ANET 800G/1.6T adoption; Ethernet vs InfiniBand share; LPO/NPO/CPO adoption signals.

### Cross-references

- `frameworks.md` v8 Framework 2.6 — canonical control-point analysis text (five-tier gradation; supplemental to Framework 2 layer placement; line 289 plain-text reference candidate for Vic-side wikilink update post-Session 27)
- [[NVDA-platform-integration]] — six-modality framing operationalizing NVDA's full control-point authority
- [[CPO-platform-battle]] — five-way executive comparison (Jensen "both by platform design"; Murphy "CPO wins"; Hock Tan "copper wins"; Mohan "phased coexistence"; Robbins "acknowledged deferral"); ANET joins as fourth tier-silence-pattern data point at Layer 5 systems integrator level (Session 27)
- [[NVDA]], [[AVGO]], [[MRVL]], [[CSCO]], [[ANET]] — vault company pages with control-point distinction sections (Session 24 Integration 1 + Session 27 paired ingest)

## Chokepoint 8 — Wafer-level SiPh reliability test (Tier 3 Rank 8)

**Conviction:** Medium-high, narrow. **Framework characterization:** *"Narrow but clean photonics-specific test exposure."* Clean niche exposure to SiPh / optical I/O reliability screening.

### Why it matters

Catch weak photonic dies before expensive packaging. Silicon photonics and optical I/O devices become more expensive after packaging and integration. Wafer-level burn-in / reliability screening improves known-good-die economics and reduces downstream failure cost.

As optical engines become more integrated and expensive, the cost of packaging a bad die rises. Earlier reliability screening becomes more valuable if SiPh / optical I/O moves into high-volume AI infrastructure.

### Best listed exposure

- **[[AEHR]]** — vault company. Per `frameworks.md` v7 Layer 3-4, photonics_tier 4. Currently the only public pure-play exposure in vault and in framework Tier 3 source. FOX wafer-level burn-in system family is the primary product line. Per Session 6 ingest: FOX system order acceleration documented Q3 FY2026 call; single-company-customer concentration risk flagged.

### Editorial assessment (per Tier 3 source)

Narrow but clean photonics-specific test exposure. [[AEHR]] should be treated as a specialized photonics test-infrastructure name, not a broad optical transceiver company.

**See [[wafer-level-siph-test]] vault chokepoint page for full chokepoint analysis** including single-company-exposure disclaimer per Option A, expansion triggers (FormFactor entering vault; ASE/AMKR ingestion; Onto Innovation expanding metrology into reliability test; Advantest/Teradyne entering segment), adjacent test ecosystem framing, and "What would confirm or weaken" pre-registration per provisional chokepoint convention.

*(Investment idea per Tier 3 source: high-upside narrow exposure if wafer-level burn-in becomes standard in SiPh / optical I/O production flows. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

SiPh customer wins; FOX system orders; repeat orders; customer concentration; wafer-level burn-in attach rate; OSAT/foundry adoption.

### Cross-references

- [[wafer-level-siph-test]] — vault chokepoint page with full chokepoint analysis (provisional, single-company-exposure disclaimer)
- [[AEHR]] — vault company page with primary-source canonical framing per Session 6
- [[ONTO]] — adjacent metrology positioning (structurally distinct supply chain layer)

## Chokepoint 9 — Silicon photonics foundry / PIC capacity (Tier 3 Rank 9)

**Conviction:** Medium today; high later. **Framework characterization:** *"Future bottleneck; not the tightest current one."* (honest-verdict hedge preserved per Tier 3 source)

### Why it matters

Integrated photonics shifts value from discrete optics to wafer-scale photonic circuits. Silicon photonics PICs can integrate waveguides, modulators, couplers, splitters, photodetectors, and other optical functions. They are important for CPO, optical I/O, and higher-density optical engines.

If the industry shifts from pluggable discrete optics toward integrated PIC-based architectures, qualified silicon photonics foundry capacity becomes more strategically important. The key issue is not just wafer capacity; it is qualified process design kits, packaging compatibility, yield, and customer tape-outs.

### Best listed exposure

- **[[TSM]]** — vault company. Per `frameworks.md` v7 Layer 2 (irreplaceable infrastructure), photonics_tier 1. Strongest if silicon photonics becomes tightly integrated with advanced packaging. COUPE silicon photonics packaging position documented per Session 17 NVDA GTC reciprocal-confirmation (vault Session 17 findings remain canonical: NVDA named technology as "COUP" with TSMC co-development attribution; TSMC primary sources silent on COUPE).
- **GFS / GlobalFoundries** — non-vault. Tier B-leading future-ingest candidate per Session 24 Integration 4 reordering. Verified largest pure-play silicon photonics foundry by revenue post-AMF acquisition (November 17, 2025). Complements [[TSM]] COUPE position with merchant SiPh foundry alternative.
- **[[TSEM]] / Tower Semiconductor** — *Ingested in Session 62 (first specialty foundry canonical at Layer 2 placement; photonics_tier 2).* PH18 + PH45 SiPh PDK foundry platform. NVIDIA partnership bilaterally confirmed at Tier 2 per Session 62 (A1 reciprocal-confirmation-LIMITED); "1.6T modules" specific framing analyst-introduced not management-confirmed at primary. Preserves both partial substantiation (NVIDIA partnership EXISTS at CEO acknowledgment scope) + Tier 3 source over-claim (1.6T specific framing).

### Editorial assessment (per Tier 3 source)

**Future bottleneck; not the tightest current one.** *(honest-verdict hedge preserved)* [[TSM]] is the high-quality platform bet; GFS/[[TSEM]] are more direct merchant foundry optionality plays.

Per Session 24 Integration 3: Chokepoint 9 (foundry layer) is structurally distinct from Chokepoint 10 (photonic advanced packaging / CPO integration) per [[datacenter-photonics-supply-chain]] Section 2.6 vs Section 2.7 organization. Framework grouping conflates the layers; vault structural organization preserves the distinction.

*(Investment idea per Tier 3 source: TSM is the high-quality platform bet; GFS/[[TSEM]] are more direct merchant foundry optionality plays. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

GF Fotonix traction; TSM photonics roadmap; customer tape-outs; CPO volume ramps; optical I/O adoption; yield disclosure; PDK maturity.

### Cross-references

- [[datacenter-photonics-supply-chain]] Section 2.6 (Photonic foundries) — vault canonical framing per Session 24 Integration 3
- [[TSM]] — vault company page with COUPE positioning per Session 17 GTC ingest
- [[foundry-competition]] — vault theme page with ASML EUV foundry dependency framing
- [[CPO-platform-battle]] — five-way executive comparison context

## Chokepoint 10 — Photonic advanced packaging / CPO integration (Tier 3 Rank 10)

**Conviction:** Medium-high, timing uncertain. **Framework characterization:** *"Important, but adoption timing still uncertain."* (honest-verdict hedge preserved per Tier 3 source)

### Why it matters

CPO moves optics close to the switch ASIC or compute package. This can reduce electrical reach and power, but it creates harder integration problems: thermal isolation, laser reliability, optical coupling, serviceability, package yield, and field repair.

In a pluggable architecture, failed optics can be replaced at the front panel. In CPO, optics become more tightly coupled to expensive switch ASICs or compute packages. That raises the cost of failure and increases the importance of packaging yield and reliability screening.

### Best listed exposure

- **[[TSM]]** — vault company. CoWoS leading + COUPE silicon photonics packaging participation.
- **[[AVGO]]** — vault company. Bailly CPO platform decisions per Session 10 ingest. Per Framework 2.6 control point with bottleneck participation framing.
- **[[NVDA]]** — vault company. Per Session 24 Integration 3 NVDA exclusion correction: NVDA is platform decision-maker / control-point per Chokepoint 7, **not foundry-layer participant**. NVDA specifies COUP packaging from [[TSM]] rather than participating at foundry layer directly. The framework groups NVDA with TSM/ASE/AMKR in CPO chokepoint; vault structural organization correctly distinguishes platform-decision-maker (NVDA) from foundry-layer participant (TSM) from OSAT-layer participant (ASE/AMKR).
- **ASE Technology** — non-vault. Tier C future-ingest candidate. CPO-for-AI demonstrations.
- **Amkor Technology** — non-vault. Tier C future-ingest candidate. Silicon photonics + CPO in advanced packaging portfolio.

### Editorial assessment (per Tier 3 source)

**Important, but adoption timing still uncertain.** *(honest-verdict hedge preserved)* This is a strategic architecture-transition row rather than a guaranteed near-term revenue row. [[AVGO]] / [[NVDA]] control platform direction; [[TSM]] / ASE / AMKR benefit if advanced packaging becomes central to optical integration.

Per Session 24 Integration 3 structural split: Chokepoint 9 (Photonic foundries) covers foundry-layer photonic integration ([[TSM]] COUPE, GFS Fotonix, Tower SiPh) per [[datacenter-photonics-supply-chain]] Section 2.6; this Chokepoint 10 covers OSAT-layer photonic packaging (ASE Technology, Amkor Technology) per [[datacenter-photonics-supply-chain]] Section 2.7. Framework groups foundry and OSAT layers; vault correctly separates them.

*(Investment idea per Tier 3 source: AVGO/NVDA are control-point names; TSM is the advanced-packaging platform name; ASE/AMKR are secondary packaging optionality names. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

AVGO/NVDA CPO roadmap; OIF ecosystem progress; field reliability data; serviceability concerns; external laser architecture; hyperscaler deployment timelines.

### Cross-references

- **[[cpo-integration]]** — fourth canonical multi-source-synthesis chokepoint page (Session 32; closes Chokepoint 10 dedicated chokepoint page coverage gap per S27-S32 photonics chokepoint completion arc). Provides chokepoint-specific synthesis depth complementing this theme page's 13-chokepoint breadth. Multi-source synthesis across 9 vault primary-source companies ([[NVDA]] + [[AVGO]] + [[MRVL]] + [[CRDO]] + [[LITE]] + [[COHR]] + [[AAOI]] + [[TSM]] + [[FN]]) per Session 25 hybrid architecture three-source threshold satisfaction (multi-fold). Page-top theme-page-overlap differentiation boundary explicitly distinguishes scope vs [[CPO-platform-battle]] theme page (mechanics + value chain shift depth here; platform-strategy archetype framing breadth there). Scale-up + Scale-out bifurcation per Murphy thesis preserved as analytical structure throughout via Option C single-page handling.
- [[datacenter-photonics-supply-chain]] Sections 2.6 + 2.7 — vault canonical framing for foundry vs OSAT structural split per Session 24 Integration 3
- [[CPO-platform-battle]] — five-way executive comparison; CPO platform contestants and tiered silence pattern
- [[NVDA-platform-integration]] — six-modality framing including COUP/COUPE TSMC co-development modality
- [[TSMC-CoWoS]] — vault chokepoint page with advanced packaging positioning
- [[TSM]], [[AVGO]], [[NVDA]] — vault company pages

## Chokepoint 11 — Fiber / connectors / high-density attach (Tier 3 Rank 11)

**Conviction:** Medium. **Framework characterization:** *"Underappreciated but lower-purity."* (honest-verdict hedge preserved per Tier 3 source)

### Why it matters

The physical optical layer becomes harder as cluster scale rises. AI clusters require huge numbers of fiber links, dense connectors, low insertion loss, reliable terminations, and manageable cabling. CPO may increase the importance of fiber attach and field-service design.

Bad connectors, cable-management failures, or fiber-density limits can create reliability and operational bottlenecks even if the optical modules are technically capable.

### Best listed exposure

- **[[GLW]] / Corning** — vault company. Per `frameworks.md` v7 Layer 4, photonics_tier 3. Cleanest US-listed name per framework. Per Session 20 ingest: Optical Communications segment $6,274M FY2025 (+35% YoY); Meta $6B agreement; customer-prepayment + long-term-commitment moat-deepening pattern.
- **SENKO Advanced Components** — non-vault (private). Tier B future-ingest candidate. NVDA Spectrum-X / Quantum-X ecosystem partner; CPO detachable FAU; ELSFP host-connector products. Over-claim mode annotation.
- **Furukawa Electric** — non-vault. Tier B future-ingest candidate. Commercialized 100mW × 16-channel blind-mate ELS connector for CPO. Over-claim mode annotation.
- **APH / Amphenol** — non-vault. Tier C future-ingest candidate. Over-claim mode annotation.
- **TEL / TE Connectivity** — non-vault. Tier C future-ingest candidate. Over-claim mode annotation.
- **Sumitomo Electric** — non-vault. Multicore fiber adjacent.
- **Fujikura** — non-vault. Japanese fiber/cable supplier.

### Editorial assessment (per Tier 3 source)

**Underappreciated but lower-purity.** *(honest-verdict hedge preserved)* [[GLW]] and APH are the cleanest US-listed names; TEL and Japanese fiber/cable suppliers broaden the global map. The issue is not whether the layer matters technically; it is whether it is big enough to drive the stock.

Per Session 20 cross-validation: framework's Tier 3-derived ecosystem-partner narrative for Corning relied primarily on NVDA-side March 2025 announcement attribution rather than reciprocal Corning primary-source confirmation. Multicore fiber framing materially refined to Contour single-core architecture per GLW FY2025 10-K. Counterparty-attribution-only annotation discipline (over-claim mode) applied per [[datacenter-photonics-supply-chain]] Section 2.4 per Session 20 cross-validation finding.

*(Investment idea per Tier 3 source: good second-order infrastructure exposure, especially if CPO increases high-density attach requirements. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

Fiber density; connector loss budgets; hyperscaler cable-management issues; CPO fiber attach; GLW optical communications growth; APH datacenter interconnect exposure.

### Cross-references

- [[datacenter-photonics-supply-chain]] Section 2.4 (Fiber attach / connectors) — vault canonical framing
- [[GLW]] — vault company page; Session 20 cross-validation finding (over-claim mode for NVDA-named ecosystem-partner claims)

## Chokepoint 12 — Thermal infrastructure (Tier 3 Rank 12)

**Conviction:** High for AI infrastructure; adjacent to photonics. **Framework characterization:** *"AI infrastructure bottleneck; adjacent to photonics."* (honest-verdict hedge preserved per Tier 3 source)

### Why it matters

AI racks are becoming thermally constrained. High-density AI racks and CPO architectures concentrate heat near temperature-sensitive optical and electronic components. Better liquid cooling and thermal-management infrastructure become necessary as rack density rises.

Optics are sensitive to temperature drift, while GPUs, switch ASICs, and high-speed DSPs generate intense heat. Thermal design becomes a system-level constraint, especially at high rack densities.

### Best listed exposure

- **[[VRT]] / Vertiv** — vault company. Per `frameworks.md` v7 Layer 5, photonics_tier 4. Clearest listed pure-play per framework. Per Session 22 ingest: NVIDIA partnership reciprocally confirmed at Tier 1 level (10-K Item 7 Outlook and Trends Strategic Partnerships); EcoDataCenter Sweden Vera Rubin deployment; 800V DC programs H2 2026 portfolio launches. First reciprocal-confirmation modality per [[NVDA-platform-integration]] (sixth integration modality).
- **Eaton (ETN)** — non-vault. Tier B future-ingest candidate. Boyd Thermal acquisition (~$9.5B, November 3, 2025 per industry reporting) creates grid-to-chip cooling stack. Over-claim mode annotation.
- **Modine (MOD)** — non-vault. Tier C future-ingest candidate (Session 24 addition). Datacenter thermal management and liquid cooling. Over-claim mode annotation.
- **Schneider Electric** — non-vault. Tier C future-ingest candidate. 800V DC architecture; AI datacenter modernization. Over-claim mode annotation.

### Editorial assessment (per Tier 3 source)

**AI infrastructure bottleneck; adjacent to photonics.** *(honest-verdict hedge preserved)* [[VRT]] is the clearest listed pure-play; MOD and Schneider add broader infrastructure exposure.

Per Session 22 [[VRT]] ingest: reciprocal-confirmation modality — NVIDIA-aligned framing reciprocally confirmed at Tier 1 level (10-K Item 7 Outlook and Trends Strategic Partnerships disclosure plus Q1 2026 call EcoDataCenter Sweden Vera Rubin deployment specificity). First vault primary-source confirmation of NVIDIA Vera Rubin commercial deployment timing.

*(Investment idea per Tier 3 source: more of an AI datacenter infrastructure trade than a photonics trade, but still relevant because photonics must function inside the thermal envelope. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

Liquid cooling adoption; rack power density; hyperscaler thermal design wins; coolant distribution unit demand; GPU/CPO thermal limits.

### Cross-references

- [[datacenter-photonics-supply-chain]] Section 2.8 (Thermal / liquid cooling) — vault canonical framing
- [[VRT]] — vault company page with NVIDIA reciprocal-confirmation positioning per Session 22
- [[NVDA-platform-integration]] — sixth integration modality (reciprocal-confirmation)

## Chokepoint 13 — Board/package power delivery (Tier 3 Rank 13)

**Conviction:** High for AI infrastructure; adjacent to photonics. **Framework characterization:** *"AI infrastructure bottleneck; adjacent to photonics."* (honest-verdict hedge preserved per Tier 3 source)

### Why it matters

Power density limits system scaling. AI compute, switch ASICs, DSPs, and optical I/O packages require efficient power conversion close to the load. Losses create heat, and heat reduces reliability.

As rack and package power density rise, power conversion efficiency and proximity matter. 48V distribution, DC-DC conversion, GaN/SiC power devices, and near-chip power architectures become more important.

### Best listed exposure

- **Monolithic Power (MPWR)** — non-vault. Tier C future-ingest candidate (Session 24 addition). High-quality power-management exposure. Over-claim mode annotation.
- **Vicor (VICR)** — non-vault. Tier C future-ingest candidate (Session 24 addition). More direct to high-density power architecture but more volatile. Over-claim mode annotation.
- **Infineon (IFNNY)** — non-vault. Tier C future-ingest candidate (Session 24 addition). Broad power-semiconductor exposure including GaN/SiC. Over-claim mode annotation.

### Editorial assessment (per Tier 3 source)

**AI infrastructure bottleneck; adjacent to photonics.** *(honest-verdict hedge preserved)* MPWR is a high-quality power-management exposure; VICR is more direct to high-density power architecture but more volatile; IFNNY adds broad power-semiconductor exposure.

Vault gap: no current vault company exposure to board/package power delivery. Tier C future-ingest candidates per Session 24 Integration 4 surface MPWR/VICR/IFNNY for future ingest sequencing. Adjacent to photonics rather than photonics-direct — photonics must fit into the same power/thermal budget as compute and switching stack.

*(Investment idea per Tier 3 source: system-density bottleneck rather than optical-component bottleneck. Useful as a parallel AI infrastructure basket. Vic-side `_thesis.md` integration deferred per Session 24 Phase 4 recommendation.)*

### Key flags (per Tier 3 source)

48V adoption; near-chip power conversion; AI power-management revenue; GaN/SiC traction; customer concentration; margin sustainability.

### Cross-references

- [[datacenter-photonics-supply-chain]] Section 2.8 (Thermal / liquid cooling — adjacent layer) for broader AI infrastructure framing
- [[VRT]] — vault company page; thermal/power infrastructure adjacent positioning

## Ranking Summary

Mirror of Tier 3 source Ranking Summary table, with vault status annotations per company:

| Rank | Chokepoint | Conviction | Best exposure set | Reason |
|---:|---|---|---|---|
| 1 | Lasers / EMLs / III-V devices | Very high | [[LITE]], [[COHR]], MTSI (non-vault Tier C), [[AAOI]] | Most direct optical bottleneck for 800G / 1.6T / CPO scaling |
| 2 | Optical DSP / PHY power-performance | Very high | [[MRVL]], [[AVGO]], [[CRDO]], MXL (Tier C) | High-value semiconductor layer; power/performance defines module feasibility |
| 3 | InP substrate supply | High | [[AXTI]], [[COHR]], JX Advanced Metals (Tier A) | Earliest material scarcity layer; highest geopolitical leverage |
| 4 | InP epitaxial capacity | High | [[VECO]], AIXTRON (Tier C), [[LITE]], [[COHR]] | Converts substrate into usable laser/EML device potential |
| 5 | Advanced optical packaging / alignment | High | [[FN]], [[LITE]], [[COHR]], ASE (Tier C), AMKR (Tier C) | Yield, optical alignment, and process control determine scale economics |
| 6 | Finished-module optical test | Medium-high | [[VIAV]], KEYS (Tier C), Anritsu (Tier C) | Speed transition creates equipment refresh cycle; first vault baseline via [[VIAV]] post-Session 28 |
| 7 | Switch ASIC / platform architecture | Very high strategic importance | [[NVDA]], [[AVGO]], [[ANET]], [[CSCO]], [[MRVL]] | Determines architecture adoption and value-chain allocation; control point per `frameworks.md` v8 Framework 2.6; five-company in-vault complete post-Session 27 |
| 8 | Wafer-level SiPh reliability test | Medium-high, narrow | [[AEHR]] | Clean niche exposure to SiPh / optical I/O reliability screening; see [[wafer-level-siph-test]] |
| 9 | Silicon photonics foundry / PIC capacity | Medium today; high later | [[TSM]], GFS (Tier B-leading), [[TSEM]] (in-vault post-Session 62) | Future bottleneck if CPO and optical I/O move to volume |
| 10 | Photonic advanced packaging / CPO integration | Medium-high, timing uncertain | [[TSM]], [[AVGO]], [[NVDA]], ASE (Tier C), AMKR (Tier C) | Strategic transition, but adoption path remains uncertain |
| 11 | Fiber / connectors / high-density attach | Medium | [[GLW]], APH (Tier C), TEL (Tier C) | Real physical-layer constraint but less pure equity exposure |
| 12 | Thermal infrastructure | High for AI infrastructure; adjacent to photonics | [[VRT]], MOD (Tier C), Schneider (Tier C) | Critical AI datacenter constraint but not pure photonics |
| 13 | Board/package power delivery | High for AI infrastructure; adjacent to photonics | MPWR (Tier C), VICR (Tier C), IFNNY (Tier C) | Critical to system density but broader than photonics |

## Editorial assessment positioning

The Tier 3 source includes editorial content beyond the per-chokepoint analytical structure:

1. **Portfolio Watchlist Grouping** — 5 thematic baskets (Pure AI photonics bottlenecks / High-beta photonics smaller-cap / Photonics process equipment & test / CPO platform-control / Adjacent AI infrastructure).
2. **Conviction levels per chokepoint** (Very high / High / Medium-high / Medium) — preserved in this page's Ranking Summary table above.
3. **"Investment idea" sub-sections** within Core Chokepoint Table providing portfolio-level positioning recommendations — referenced in this page's per-chokepoint editorial assessment paragraphs via parenthetical attribution but not migrated.

Per Session 24 Phase 4 recommendation:

- **Portfolio Watchlist Grouping integration into `_thesis.md`** is Vic-side action between Sessions 24 and 25 (status check at Session 25 close).
- **Conviction levels integration into `_thesis.md`** is Vic-side action with same status check.
- **"Investment idea" sub-sections are deferred entirely to Vic-side decision** per "_thesis.md never edited by LLM" convention. This theme page references investment-idea content via parenthetical attribution within editorial assessment paragraphs but does not migrate or restate.

The theme page surfaces editorial-assessment content via Tier 3 source citation; Vic-side execution determines whether and how this content migrates to `_thesis.md` for portfolio-level reading.

## Source attribution

Tier 3 source: `raw/research/photonics-chokepoint-table.md` — Vic-team-authored chokepoint research framework. Single canonical source per Vic direction at Session 24. Canonical living document model (no date stamp; updates replace in-place).

Source structure: 13-chokepoint Core Table (Why it matters / Best listed exposure / My assessment per chokepoint); Ranking Summary table; Portfolio Watchlist Grouping (5 thematic baskets); Source Pointers section.

A2 structural requirement 1 compliance: Tier 3 source named in page-top disclaimer, per-chokepoint section editorial-assessment citations, and this Source attribution body section.

## Open questions

Session 24 carry-overs:

1. **Chokepoint 3 InP substrate two-claim reconciliation** — JX Advanced Metals 78% (Session 19) vs AXTI 60-70% (Tier 3 framework); both over-claim mode pending future primary-source verification. Two-layer distinction (indium feedstock vs InP wafer production) preserved per [[datacenter-photonics-supply-chain]] Section 2.9.
2. **Chokepoint 10 CPO chokepoint structural distinction** — framework groups foundry-layer (TSM, GFS, Tower) with OSAT-layer (ASE, AMKR); vault correctly separates per Session 24 Integration 3. Chokepoint 9 covers foundry layer; Chokepoint 10 covers OSAT layer.
3. **Chokepoint 7 Switch ASIC / platform architecture** — Framework 2.6 codification at `frameworks.md` v8 establishes canonical control-point analysis; per-company application documented at Session 24 Integration 1.

New Session 25 questions:

4. Whether Tier 3 framework's "Future bottleneck; not the tightest current one" hedge for Chokepoint 9 (Silicon photonics foundry / PIC capacity) holds against future GFS or Tower Semiconductor primary-source ingest.
5. Whether Tier 3 framework's "Important, but adoption timing still uncertain" hedge for Chokepoint 10 (Photonic advanced packaging / CPO integration) tightens or loosens with NVDA Q1 FY2027 cross-venue gap third-instance test (Session 26+ deferred per Vic direction).
6. Whether Tier 3 framework's "Underappreciated but lower-purity" hedge for Chokepoint 11 (Fiber / connectors) holds against future SENKO or Furukawa primary-source ingest given GLW Session 20 reciprocal-confirmation reframing of fiber-attach Tier 3 ecosystem-partner claims.

## Future-ingest verification triggers

Per-chokepoint future-ingest opportunities that would refine Tier 3 claims to inversion or reciprocal-confirmation mode per A1:

| Chokepoint | Current vault status | Future-ingest verification trigger |
|---|---|---|
| 1 Lasers / EMLs | [[LITE]] + [[COHR]] + [[AAOI]] vault | MTSI / MACOM primary-source ingest (Tier C) |
| 2 Optical DSP / PHY | [[MRVL]] + [[AVGO]] vault | Credo (CRDO Tier B); MaxLinear (MXL Tier C) |
| 3 InP substrate | [[AXTI]] + [[COHR]] vault; JX Tier A | JX Advanced Metals primary-source ingest (challenging) |
| 4 InP epitaxial | [[VECO]] + [[LITE]] + [[COHR]] vault | AIXTRON primary-source ingest (Tier C) |
| 5 Advanced optical packaging | [[FN]] + [[LITE]] + [[COHR]] + [[AAOI]] vault | Jabil (JBL Tier B); ASE/AMKR primary-source |
| 6 Finished-module optical test | None vault | KEYS / VIAVI / Anritsu (Tier C per Session 24) |
| 7 Switch ASIC / platform | [[NVDA]] + [[AVGO]] + [[MRVL]] + [[CSCO]] vault | NVDA Q1 FY2027 (deferred Session 26+); ANET if ingested |
| 8 Wafer-level SiPh test | [[AEHR]] vault → [[wafer-level-siph-test]] new | FormFactor expansion trigger; ASE/AMKR OSAT |
| 9 Silicon photonics foundry | [[TSM]] vault | GFS (Tier B-leading per Session 24); Tower (Tier C) |
| 10 Photonic advanced packaging / CPO | [[TSM]] + [[AVGO]] + [[NVDA]] vault | ASE/AMKR primary-source for OSAT layer |
| 11 Fiber / connectors | [[GLW]] vault | SENKO (Tier B); Furukawa (Tier B); APH/TEL Tier C |
| 12 Thermal infrastructure | [[VRT]] vault | Eaton (ETN Tier B); Modine (MOD Tier C) |
| 13 Board/package power | None vault | MPWR / VICR / IFNNY (Tier C per Session 24) |

## Source audit notes

### `raw/research/photonics-chokepoint-table.md` (Tier 3, Vic-team-authored chokepoint research framework)

Vic-team-authored synthesis. Canonical living document model — no date stamp; updates replace in-place per Vic direction at Session 24. Three discrete sections: 13-chokepoint Core Table (primary content for chokepoint sections above); Ranking Summary table (preserved as Section 3 above); Portfolio Watchlist Grouping (5 thematic baskets — investment thesis content; Vic-side `_thesis.md` integration per Session 24 Phase 4 recommendation).

A2 no-verification convention application: claims included with attribution at construction time; deviation-based refinement at primary-source ingest cycles per A1. Most chokepoints have not yet undergone primary-source cross-validation. Specific claims warranting future-ingest verification documented in Open questions and Future-ingest verification triggers sections.

Vault-conflict reconciliations applied (per Session 24 selective integration):

- **Integration 2:** AXTI 60-70% vs JX 78% reconciled via two-layer distinction (preserved at Chokepoint 3)
- **Integration 3:** CPO chokepoint structural split (foundry vs OSAT layers; preserved at Chokepoints 9 and 10)
- **Integration 1:** Five-company control-point thread (NVDA + AVGO + MRVL + CSCO + ANET non-vault; preserved at Chokepoint 7 with Framework 2.6 canonical reference)

Honest-verdict framing preserved per Tier 3 source. Hedges retained: "Future bottleneck; not the tightest current one" (Chokepoint 9); "Important, but adoption timing still uncertain" (Chokepoint 10); "Underappreciated but lower-purity" (Chokepoint 11); "AI infrastructure bottleneck; adjacent to photonics" (Chokepoints 12, 13).

## Change log

- **2026-04-27 (Session 25 dual-page creation — A2 first canonical application):** Theme page created as Tier 3-anchored vault-canonical reference for 13-chokepoint photonics framework. Per A2 structural requirement 1: Tier 3 source attribution at page-top disclaimer, per-chokepoint editorial assessment citations, and Source attribution body section. Per A2 structural requirement 2: counterparty-attribution-only annotation at construction time for non-vault company references (over-claim mode pending future primary-source verification). Per A2 structural requirement 3: no-verification at construction; future-ingest verification triggers documented per chokepoint. Cross-references to vault companies (17), vault chokepoint pages (3 — [[InP-supply]], [[datacenter-laser-supply]], [[wafer-level-siph-test]]), vault theme pages (3 — [[datacenter-photonics-supply-chain]], [[CPO-platform-battle]], [[NVDA-platform-integration]]), `frameworks.md` v8 Framework 2.6 (Control-point analysis canonical text). Three Session 24 carry-overs (Integration 1 control-point distinction at Chokepoint 7; Integration 2 InP two-layer reconciliation at Chokepoint 3; Integration 3 CPO chokepoint structural split at Chokepoints 9 and 10) reflected in respective sections. Chokepoint sections ordered per Tier 3 Ranking Summary (Rank 1 to Rank 13) for analytical priority. Forward-wikilink discipline preserved: ~25+ non-vault companies (AIXTRON, Sumitomo Electric, Furukawa Electric, Fujikura, Schneider Electric, Anritsu, TSEM, ASE Technology, Amkor Technology, Modine, MPWR, VICR, IFNNY, KEYS, VIAVI, APH, TEL, GFS, CRDO, MXL, ANET, JX Advanced Metals, MTSI/MACOM, plus Eaton, Jabil, SENKO, FormFactor, Tower Semiconductor) referenced as plain text.
- **2026-04-28 (Session 26 addendum — factual error correction):** Chokepoint 8 (Wafer-level SiPh reliability test) AEHR ingest attribution corrected from "Session 4" to "Session 6" (2 instances at body line 297 + Cross-references line 314) and "Q4 FY2025 call" to "Q3 FY2026 call" (1 instance at line 297). Original Session 25 page creation propagated kickoff-drafting error: AEHR was ingested at Session 6 (2026-04-20, paired with [[ONTO]]) using AEHR Q3 FY2026 earnings call dated April 7, 2026 — per `log.md` line 280 and `wiki/companies/AEHR.md` Change log line 164. No content edits beyond mechanical text replacement; substantive analytical content unchanged.
- **2026-04-28 (Session 27 paired ingest — [[CRDO]] + [[ANET]] vault-status promotion):** Chokepoint 2 (Optical DSP / PHY power-performance) updated: CRDO promoted from Tier B non-vault to in-vault wikilink with full Framework 2.6 placement (bottleneck-tier with control-point aspirations alongside [[MRVL]] at smaller operational scale); three primary-source vault coverage post-Session 27 (MRVL Session 9 + AVGO Session 10 + CRDO Session 27); editorial assessment expanded to note three-source threshold satisfaction per Session 25 hybrid architecture and `optical-dsp-phy-supply.md` chokepoint page candidacy assessment per S27-S30 photonics completion arc plan. Chokepoint 7 (Switch ASIC / platform architecture) updated: ANET promoted from non-vault plain-text to in-vault wikilink with Framework 2.6 placement (bottleneck participant with platform-tier ambition alongside [[CSCO]]; framework Tier 3 prior framing confirmed by Session 27 source evidence); five-company analytical thread now in-vault complete via Session 27 fifth-member completion. Ranking Summary table updated for Chokepoint 2 ([[CRDO]] in-vault) and Chokepoint 7 ([[ANET]] in-vault). Cross-references sections updated. Frontmatter `tickers` extended to add CRDO + ANET (19 tickers total). Forward-wikilink discipline preserved: 13-session streak post-Session 27.
- **2026-04-28 (Session 28 paired ingest — [[VIAV]] vault-status promotion; [[PLAB]] excluded per Outside Framework 5 placement):** Chokepoint 6 (Finished-module optical test) updated: VIAV promoted from non-vault Tier C plain-text to in-vault wikilink with Framework 2.6 placement (pure bottleneck participant; Layer 4 / photonics_tier 4); first vault Chokepoint 6 baseline post-Session 28; editorial assessment expanded with cross-reference to [[wafer-level-siph-test]] documenting structural distinction between finished-module test (downstream) and wafer-level test (upstream); VIAV multi-quarter visibility extension framing per Khaykin Q2 FY2026 call; AEHR FOX system order acceleration cross-reference. Ranking Summary table updated for Chokepoint 6 ([[VIAV]] in-vault; KEYS + Anritsu remain Tier C). [[PLAB]] excluded from theme page per Outside Framework 5 placement (Session 28 honest-verdict discipline application; PLAB ZERO photonic foundry customer disclosure; analogous to [[COHU]] broad-cycle exposure pattern; second vault Outside Framework 5 placement after COHU). Frontmatter `tickers` extended to add VIAV (20 tickers total; PLAB excluded). Forward-wikilink discipline preserved: 14-session streak post-Session 28.
- **2026-04-28 (Session 30 multi-source chokepoint synthesis — closes S27-S30 photonics completion arc):** Chokepoint 2 (Optical DSP / PHY power-performance) Cross-references section updated with `[[optical-dsp-phy-supply]]` cross-reference to new dedicated chokepoint page. Second canonical multi-source-synthesis chokepoint page in vault history (after [[InP-supply]] Session 13). Closes Chokepoint 2 dedicated chokepoint page coverage gap per S27-S30 photonics completion arc plan. Multi-source synthesis across [[MRVL]] + [[AVGO]] + [[CRDO]] per Session 25 hybrid architecture three-source threshold satisfaction. Theme page Chokepoint 2 section content unchanged (theme page maintains 13-chokepoint breadth; chokepoint page provides depth). No `tickers` frontmatter changes; `last_updated` 2026-04-28 unchanged. Forward-wikilink discipline preserved: 16-session streak post-Session 30.
- **2026-04-30 (Session 31 multi-source chokepoint synthesis — Tier 3 framework Chokepoint 5 dedicated chokepoint page):** Chokepoint 5 (Advanced optical packaging / alignment) Cross-references section updated with `[[advanced-optical-packaging]]` cross-reference to new dedicated chokepoint page. **Third canonical multi-source-synthesis chokepoint page in vault history** (after [[InP-supply]] Session 13 and [[optical-dsp-phy-supply]] Session 30). Multi-source synthesis across [[FN]] + [[LITE]] + [[COHR]] + [[AAOI]] per Session 25 hybrid architecture three-source threshold satisfaction (multi-fold; 4 vault primary-source companies). Theme page Chokepoint 5 section content unchanged (theme page maintains 13-chokepoint breadth; chokepoint page provides depth). No `tickers` frontmatter changes; `last_updated` 2026-04-28 unchanged. Forward-wikilink discipline preserved: 17-session streak post-Session 31.
- **2026-04-30 (Session 32 multi-source chokepoint synthesis — Tier 3 framework Chokepoint 10 dedicated chokepoint page; closes S27-S32 photonics chokepoint completion arc):** Chokepoint 10 (Photonic advanced packaging / CPO integration) Cross-references section updated with `[[cpo-integration]]` cross-reference to new dedicated chokepoint page placed at top of section (per S27-S30 + S31 ordering convention). **Fourth canonical multi-source-synthesis chokepoint page in vault history** (after [[InP-supply]] Session 13, [[optical-dsp-phy-supply]] Session 30, [[advanced-optical-packaging]] Session 31). Multi-source synthesis across 9 vault primary-source companies ([[NVDA]] + [[AVGO]] + [[MRVL]] + [[CRDO]] + [[LITE]] + [[COHR]] + [[AAOI]] + [[TSM]] + [[FN]]) per Session 25 hybrid architecture three-source threshold satisfaction (multi-fold). **Largest multi-vantage-point synthesis at chokepoint page scope yet** (vs 3 companies Session 30; 4 companies Session 31). Page-top theme-page-overlap differentiation boundary explicitly distinguishes scope vs [[CPO-platform-battle]] theme page (mechanics + value chain shift depth here; platform-strategy archetype framing breadth there). Scale-up + Scale-out bifurcation per Murphy thesis preserved as analytical structure throughout via Option C single-page handling. Theme page Chokepoint 10 section content unchanged (theme page maintains 13-chokepoint breadth; chokepoint page provides depth). **A6 v8 (g)' subtype Phase 6 verification finding:** Session 32 kickoff used "Chokepoint 7" matching source file's pre-v2 row index; vault canonical numbering (this priorities theme page Tier 3 Rank ordering, used at Sessions 25, 30, 31) places this chokepoint at Chokepoint 10. Chokepoint 7/Chokepoint 10 numbering corrected at Phase 6 cross-reference fan-out (4 occurrences in cpo-integration.md + 9 occurrences in company page Change log entries). A6 (g)/(g)' subtype instance count: 6 accumulated through Session 32. No `tickers` frontmatter changes; `last_updated` 2026-04-28 unchanged. Forward-wikilink discipline preserved: 18-session streak post-Session 32. **Closes S27-S32 photonics chokepoint completion arc** (3 dedicated chokepoint pages: Chokepoint 2 + Chokepoint 5 + Chokepoint 10; 6 sessions; 4 paired ingests + 3 chokepoint pages + 1 codification + 1 framework synthesis).
- **2026-04-30 (Session 33 multi-source chokepoint synthesis — Tier 3 framework Chokepoint 3 + Chokepoint 4 unified dedicated chokepoint page; provisional → canonical promotion via Option C bifurcation handling):** Chokepoint 3 (InP substrate supply) + Chokepoint 4 (InP epitaxial capacity) Cross-references sections updated with reinforced `[[InP-supply]]` cross-reference reflecting promotion from provisional Session 13 to canonical multi-source-synthesis chokepoint page placement. **Fifth canonical multi-source-synthesis chokepoint page in vault history** (after [[optical-dsp-phy-supply]] Session 30, [[advanced-optical-packaging]] Session 31, [[cpo-integration]] Session 32). **Second chokepoint page applying Option C bifurcation handling** (single page covers two adjacent Tier 3 ranks via internal subsection structure; mirrors Session 32 Scale-up + Scale-out CPO precedent). Multi-source synthesis across 5 vault primary-source vantages — [[AXTI]] (substrate-tier core; preserved Session 13 content) + [[VECO]] (epitaxial-tier equipment; Lumina+ MOCVD + Aixtron primary competitor + Compound Semi $60M FY2025 → $80M FY2026 guidance) + [[COHR]] (epitaxial-tier device-fabrication; six-inch InP at Sherman + Järfälla + Zürich) + [[LITE]] (epitaxial-tier device-fabrication; three-inch InP industry-standard + 40% capacity expansion) + [[AAOI]] (epitaxial-tier device-fabrication; Sugar Land MBE + MOCVD dual-process). Page filename preserved per Vic Stop 1 decision (avoids wikilink-cascade across 6+ vault pages); page title expanded "InP substrate supply" → "InP supply (substrate + epitaxial capacity)". Theme page Chokepoint 3 + Chokepoint 4 section content unchanged (theme page maintains 13-chokepoint breadth; chokepoint page provides depth). Three Layer 4 InP wafer-size positions preserved without forced winner attribution (COHR six-inch advantage / LITE three-inch industry-standard / AAOI dual-process); Tier 1/Tier 2 framing gap (2 vs 3 suppliers dispute at AXTI) preserved without silent adjudication; geopolitical mirror structure preserved as conditional risk. **A6 v8 verification PASS** — vault canonical Tier 3 Rank numbering preserved (Chokepoint 3 + Chokepoint 4) per Session 32 (g)' lesson; zero falsifications surfaced; A6 (g)/(g)' subtype instance count unchanged at 6 accumulated through Session 32. No `tickers` frontmatter changes; `last_updated` 2026-04-28 unchanged. Forward-wikilink discipline preserved: 19-session streak post-Session 33. Vault now holds dedicated chokepoint pages for **7 of 13 Tier 3 framework chokepoints** (Chokepoints 1 + 2 + 3 + 4 + 5 + 8 provisional + 10).
