---
type: chokepoint
tickers: [MRVL, AVGO, CRDO]
last_updated: 2026-06-24
---

# Optical DSP / PHY supply

*Tier 3 framework reference: `raw/research/photonics-chokepoint-table.md` Chokepoint 2 (Optical DSPs / PHYs / power-performance) / Ranking Summary Rank 2; very high conviction. Framework characterization: "Top-tier chokepoint; MRVL/AVGO primary."*

## Overview

Optical DSP/PHY is the second-highest-conviction chokepoint in the AI photonics supply chain per Tier 3 framework. The digital electronics determine whether the optical link is practical — PAM4 optical DSPs, PHYs, SerDes, FEC, equalization, clock recovery, and diagnostics determine whether 200G/lane and 1.6T modules can hit performance targets inside strict power and thermal budgets.

This page synthesizes Optical DSP/PHY chokepoint dynamics across three primary-source vault companies — [[MRVL]] (Session 9 ingest baseline; [[NVDA-platform-integration]] Session 22 cross-reference; Celestial AI acquisition codification Session 19; Framework 2.6 codification Session 24), [[AVGO]] (Session 10 ingest baseline), and [[CRDO]] (Session 27 paired ingest with [[ANET]]) — closing the dedicated chokepoint page coverage gap per S27-S30 photonics completion arc plan. Three-source threshold satisfied per Session 25 hybrid architecture.

[[CSCO]] Acacia 3nm Kibo 1.6T PAM4 DSP exists as captive (Cisco-branded pluggables, not merchant) per [[datacenter-photonics-supply-chain]] Section 2.3. [[CSCO]] Acacia DSP is structurally distinct from the merchant DSP/PHY supply chain documented on this page; cross-referenced only. **Q3 FY2026 scale update (S108):** Acacia took **>$1B in Q3 orders, on track for >200% FY2026 growth**, with two named hyperscaler optics design wins (CSCO Q3 FY2026 call). The captive framing still holds (Acacia coherent DSPs ship inside Cisco-branded pluggables, not as merchant DSP) — but the scale is now far larger than the "cross-referenced only" treatment implied; a 4→3 photonics_tier trigger is pre-registered on [[CSCO]] (separate Acacia revenue disclosure + merchant optical sales + sustained >$1B).

**Tier 3 framework characterization** (per `raw/research/photonics-chokepoint-table.md`): Top-tier chokepoint with MRVL and AVGO as primary incumbents and CRDO + MaxLinear as high-beta challengers / adjacent connectivity plays. This is a high-value semiconductor layer with stronger potential value capture than module-level businesses — DSP/PHY suppliers can capture architectural value even when module assembly margins compress.

**Vault three-company concentration:** [[MRVL]] (Layer 3 / photonics_tier 3 / Framework 2.6 bottleneck-tier with control-point aspirations) + [[AVGO]] (Layer 1 with Layer 1/3 straddling tension / photonics_tier 3 / Framework 2.6 control point with bottleneck participation) + [[CRDO]] (Layer 3 / photonics_tier 3 / Framework 2.6 bottleneck-tier with control-point aspirations alongside MRVL at smaller operational scale).

## Chokepoint mechanics

### Why Optical DSP/PHY is a chokepoint

The optical module cannot simply scale bandwidth without increasing signal-processing complexity. Higher lane speeds increase loss, noise, jitter, and error-correction requirements. The DSP must recover the signal while consuming as little power as possible — at 1.6T, the DSP becomes both performance enabler and power problem (per [[datacenter-photonics-supply-chain]] Section 2.3).

DSP/PHY suppliers participate at a high-value semiconductor layer with stronger potential value capture than module-level businesses. The architectural partition between SerDes, retimer, and optical engine remains a core design choice rather than a solved problem; LPO (linear-drive pluggable optics) and LRO can shift equalization burden between module and host but require tighter co-design.

### Structural drivers

1. **Hyperscaler 1.6T transition demand.** All three vault companies position around 1.6T transitions; differentiation occurs at protocol layer (UALink + ESUN + Ethernet vs proprietary scale-up).
2. **Node leadership economics.** Leading-edge node positioning (3nm vs 5nm vs n-1) trades performance and power efficiency against cost and availability. Each company positions node strategy as competitive advantage; honest-verdict synthesis evaluates trade-offs without forcing winner attribution.
3. **Multi-protocol roadmap demand.** UALink + ESUN + Ultra Ethernet Consortium + proprietary scale-up protocols (NVLink) impose multi-protocol roadmaps on DSP/PHY suppliers. Standards-body participation evidence varies per company.
4. **CPO displacement risk asymmetric exposure.** Three distinct CPO strategies surface across the three companies — incumbent + direct competitor + displacement claimant — creating asymmetric exposure profiles within the same chokepoint.

### Tier 3 framework key flags

Per Tier 3 source: watts per 1.6T module; 200G/lane design wins; 3nm/5nm transitions; LPO/LRO displacement risk; hyperscaler qualification; SerDes attach rate; FEC/BER performance.

## MRVL positioning

[[MRVL]] is the primary optical DSP/PHY incumbent per Tier 3 framework, alongside [[AVGO]]. Per Session 9 ingest baseline: Layer 3 specialized designer with Layer 3 → Layer 2 trajectory in progress (per CLAUDE.md Layer straddling tension convention; not upgraded as of FY2026); photonics_tier 3.

### Ara DSP product family

**Ara 3nm 1.6T PAM4 DSP** integrates eight 200G electrical + eight 200G optical lanes; 400G/lane demonstrated; named "Interconnect Product of the Year" February 2026 (per [[datacenter-photonics-supply-chain]] Section 2.3). MRVL's interconnect portfolio per Q4 FY2026 call: "PAM DSPs (first-to-market claim at every PAM generation; 200G per lane productized, 400G demonstrated)."

**Coherent DSPs (1.6T shipping; 2nm next-gen sampling).** Inherited from $10B Inphi acquisition (closed April 2021). Long-haul + metro coherent optics positioning. **Important correction per A6 (g) verification at Phase 0:** MRVL coherent DSP capability is from Inphi acquisition only. Acacia Communications was acquired by [[CSCO]] in 2021 ($4.5B), not by MRVL. The Inphi acquisition included Inphi's coherent DSP capabilities; MRVL's coherent DSP product line traces to Inphi inheritance.

**AEC DSPs.** Design wins at three Tier 1 hyperscalers per MRVL Q4 FY2026 call. Combined AEC + retimer revenue ~$200M FY2027, more than doubling YoY.

**LPO chipsets + PCIe retimers.** Adjacent component segments; cross-reference [[CRDO]] AEC franchise as adjacent competitor.

### Photonic Fabric (Celestial AI acquisition)

**Acquisition terms (per MRVL.md Session 9 + Session 19 codification):** Closed February 2, 2026 (subsequent to FY2026 fiscal year end). Cash consideration ~$1.3B ($1.0B net of ~$300M cash acquired); stock ~24.5M MRVL shares; contingent earn-outs through FY2029 — total consideration up to ~$5.5B including earn-outs. Earn-out's ~$2.2B incremental value ($5.5B minus ~$3.3B at close) is MRVL's implicit bet that Celestial revenue will materialize at scale.

**Photonic Fabric technology.** First-generation product is a chiplet "integrating all required electrical and optical components, including drivers, TIAs, equalizers, SerDes, microcontrollers, modulators, photodiodes, and waveguides, into a compact form factor" (MRVL 10-K FY2026). Purpose-built for scale-up networking — chiplets co-packaged into both custom XPUs and scale-up switches, on both sides of the link.

**CPO revenue projections.** $500M annualized run rate Q4 FY2028; $1B annualized Q4 FY2029. Celestial + Xconn combined ~$250M aggregate revenue FY2028 (full-year, not run rate). First-gen chiplet in high-volume manufacturing. "Large-scale commercial deployment of CPO for scale-up connectivity starting next year" — FY2028 (MRVL Q4 FY2026 call). Scale-up interconnect TAM: >$10B by 2030.

**Tier 1/Tier 2 framing gap (widest in vault).** The 10-K's treatment of Celestial AI is corporate and procedural ("not practicable to disclose" preliminary purchase price allocation; subsequent event framing). The earnings call's treatment is commercially aggressive ($500M/$1B run rate targets stated as operating forecasts; "fully engaged in bringing Celestial's first-generation chiplet into high-volume manufacturing"). A wiki reader relying on only one tier would reach substantially different conclusions about Celestial's commercial maturity. Both factually accurate within respective disclosure conventions.

### Vertical integration pattern

Layer 3 component (Ara DSP, coherent DSPs from Inphi) + Layer 2-tier ambition via Photonic Fabric (Celestial AI). Aggressive XPU control-point ambition through chiplet integration into custom XPUs and scale-up switches. **Layer 3 → Layer 2 trajectory in-progress, not upgraded** per CLAUDE.md Layer straddling tension convention. Upgrade trigger: GAAP margins approaching 60%+ (52.1% as of Q1 FY2027; non-GAAP 58.9%), Celestial/CPO revenue exceeding $500M annual, custom ASIC mix demonstrably improving rather than diluting margins.

### Custom ASIC franchise

Hyperscaler co-design: Microsoft + AWS + Google + Meta (multiple programs over time). Two customer warrants (FY2025 + FY2026 instruments) — revenue-milestone-vesting structures recognized as revenue reductions; FY2025 warrant 4.2M shares at $87.77 ($227.6M fair value); FY2026 warrant 1.0M shares at $87.00 ($55.4M fair value; associated with Celestial acquisition). Two separate warrants confirm at least two major custom programs with equity-participation structures.

### Networking switch products (adjacent to DSP)

Teralynx scale-out switches: 12.8T sustained, 51.2T ramping, 100T sampling H1 FY2027. Scale-up: UALink 115T solutions sampling H2 FY2027, volume production FY2028. Switch revenue exceeded $300M FY2026, guided to >$600M FY2027 (MRVL Q4 FY2026 call). Switch products integrate Photonic Fabric chiplets for CPO scale-up positioning.

### Murphy combative positioning (CEO combativeness convention monitoring)

CEO Matt Murphy on custom silicon competitive noise per Q4 FY2026 call: "Do you see me blinking? You don't... I'm very fired up on this topic" — referencing "analysts retracting notes" and "articles that weren't even accurate at all." Most combative management passage in vault. CEO combativeness convention currently at 2 instances (MRVL.md + AVGO.md); monitoring continues per CLAUDE.md. **Q1 FY2027 update:** Murphy's tone was confident but measured — no comparable combative passage on the May 27, 2026 call; the convention count is unchanged at 2 (this quarter does not add an instance).

### Q1 FY2027 update (MRVL 10-Q + May 27, 2026 call)

Interconnect demand accelerated — FY2027 interconnect growth raised to **>70% YoY** (from >50%). PAM: 200G/lane 1.6T ramping after its H2 FY2026 launch; 400G/lane demonstrated at OFC April 2025; a further 1.6T step-up expected FY2028. Coherent: first secure **1.6T ZR/ZR+ DCI modules on a new 2nm coherent DSP** sampling this year; coherent-light products (2-20km, low power) shipping at 200G/lane; DCI has line-of-sight to ~$1B annualized in FY2028 (~2× FY2026's ~$500M), driven by the emerging scale-across category. **TIAs and drivers** to exceed a $1B annualized run rate within a few quarters. **AEC ("Golden Cable") + retimers:** design wins at 3 Tier 1 US hyperscalers; combined revenue to "more than double" YoY FY2027.

**NVIDIA optics collaboration.** MRVL's long-standing DSP / TIA / driver supply relationship with NVIDIA expands into a silicon-photonics collaboration for scale-up networking, alongside NVLink Fusion and a $2.0B NVIDIA convertible-preferred investment (MRVL 10-Q Q1 FY2027); see [[NVDA-platform-integration]] Mode 4. New **Polariton** acquisition (plasmonics; >1 THz modulator bandwidth) extends the coherent / DCI roadmap to 3.2T (call-only). **Celestial PPA finalized** at $3.5B and consolidated from Feb 2, 2026 — the framing gap above is narrowing as the 10-Q now discloses the purchase consideration and runs the $331.8M earn-out remeasurement through GAAP earnings.

## AVGO positioning

[[AVGO]] is the second primary optical DSP/PHY incumbent per Tier 3 framework. Per Session 10 ingest baseline: Layer 1 platform definer with Layer 1/3 straddling tension; photonics_tier 3.

### Taurus DSP product family

**Taurus 400G/lane optical DSP** — first 400G/lane optical DSP per [[datacenter-photonics-supply-chain]] Section 2.3. Hock Tan AVGO Q1 FY2026 call: "we are the only one out there at 1.6T DSP." 200G SerDes leadership claim integrates Taurus DSP positioning with Tomahawk switch ASIC platform.

### Tomahawk switch ASIC integration

**Tomahawk 6** (100 Tbps with 200G SerDes; "first to market"; introduced ~9 months prior to Q1 FY2026 call). **Tomahawk 7** next generation, "double the performance," launching 2027 (AVGO Q1 FY2026 call). **Davisson 102.4T** switch ASIC variant per [[datacenter-photonics-supply-chain]] Section 2.3. Vertical integration pattern: Layer 1 platform definition via Tomahawk + Layer 3 component supply via Taurus. SerDes IP at 200G + 400G is the structural moat.

### Custom ASIC franchise

Six named hyperscaler customers per Q1 FY2026 call:
- **Google** — 7th-gen Ironwood TPU; continued 2026 growth; stronger demand from next-gen TPUs in 2027+
- **Anthropic** — "1 GW of TPU compute" in 2026; demand surging to >3 GW in 2027
- **Meta** — MTIA "alive and well... we're shipping now"; next-gen XPUs to "multiple gigawatts in 2027 and beyond"
- **Apple** — multi-program XPU exposure
- Plus two additional un-named customers per call disclosure

**"Anthropic TPU compute" Freudian-slip observation** (per AVGO.md Session 10): Hock Tan called Anthropic deployment "TPU compute" using Google's TPU architecture terminology, then later: "You can tweak your TPUs — sorry, Freudian slip" when referring to all XPUs generically. If Anthropic's program is architecturally derived from Google TPU, six customer names may overstate the number of independent design-in programs. Framed as franchise concentration observation, not definitive proof.

### CPO positioning — silence + dismissal

**Bailly platform never named.** AVGO.md Session 10: "Bailly — AVGO's named CPO platform — is **never mentioned** in any of the three sources. Both Tier 1 filings contain zero mentions of CPO, co-packaged optics, silicon photonics, or any photonics-forward language."

**Active dismissal + claimed leadership.** AVGO simultaneously claims CPO leadership ("we are the lead in CPOs") and pushes the timeline ("bright, shiny objects"). Per [[CPO-platform-battle]] tiered silence pattern: Layer 1 active dismissal variant.

**Scale-up: copper DAC via SerDes, not CPO.** Hock Tan core argument per AVGO Q1 FY2026 call: "You really want to connect XPUs to XPUs directly where you can. The best way to do that is use Direct Attach Copper. That's the lowest latency, lowest power, and lowest cost... We can do it with copper, we can push the envelope from 100G to 200G to even 400G." Scale-up uses copper (SerDes advantage); scale-out uses Ethernet optical (Tomahawk advantage). CPO is deferred.

### Vertical integration pattern

Layer 1 platform (Tomahawk switch ASIC) + Layer 3 component (Taurus DSP) vertical integration. Custom ASIC franchise (Google TPU + Anthropic 1GW + Meta MTIA + Apple) operates orthogonally — design-service rather than platform-licensing. The Layer 1 classification rests on networking platform dominance + VMware software platform (93% gross margin) + multi-generation strategic custom ASIC relationships.

### Foundry concentration

95% of contract-manufactured wafers produced by [[TSM]] (AVGO 10-K FY2025) — most explicit foundry dependency disclosure in vault. See [[TSMC-CoWoS]].

### Hock Tan combative positioning (CEO combativeness convention monitoring)

AVGO.md Session 10 documented: Hock Tan "you must be a bit hallucinating" defensive response. Plus AVGO Q1 FY2026 call CPO dismissal as "bright shiny objects." Second instance for CEO combativeness convention monitoring (alongside MRVL Murphy "Do you see me blinking?").

## CRDO positioning

[[CRDO]] is the third primary-source vault company at Optical DSP/PHY chokepoint per Session 27 paired ingest. Per Tier 3 framework: high-beta challenger / adjacent connectivity play (alongside MaxLinear). Per Session 27 framework verification: Layer 3 / photonics_tier 3 / Framework 2.6 bottleneck-tier with control-point aspirations alongside [[MRVL]] at smaller operational scale.

**FY2026 refresh (S171).** CRDO posted a blow-out FY2026 — revenue **$1,335.1M (+206%)**, non-GAAP NI $662M — and the growth engine is **shifting copper→optical**: ~half of the guided FY2027 >80% growth is optical, anchored by a **~$600M optical ramp** with three >$100M legs — discrete optical DSPs (Robin 100G + Cardinal 200G, 7nm), silicon-photonics PICs, and ZeroFlap Optics (the largest). So the DSP is no longer a side line but a named growth leg. The **DustPhotonics** acquisition (SiPho PIC; closed late-May 2026) adds in-house silicon photonics — a step up the optical stack (CPO/NPO path, FY2028; see [[cpo-integration]]). Placement HELD at Layer 3 / photonics_tier 3 (optical ramp is forward-guided; upgrade trigger pre-registered). See [[CRDO]].

### Cardinal Optical PAM4 DSP product family

**Cardinal Optical PAM4 DSPs** with mature node n-1 cost advantage (per CRDO.md Session 27). CEO Bill Brennan Q3 FY2026 call: "100 gig per lane deployments with increasing traction at 200 gig as customers prepare for 1.6T transitions." Fifth-generation 50G/100G PAM4 DSPs for optical transceivers and AOCs. Connectivity ranges 5m to 10km+ at 50Gb/s to 800Gb/s.

CRDO competitive positioning vs MRVL Ara + AVGO Taurus per Tier 3 framework: "More high-beta challenger or adjacent connectivity play." n-1 fabrication node strategy trades leading-edge performance against cost and availability. CRDO claim per Brennan Q3 call: "Our proprietary SerDes and DSP technologies enable us to achieve similar performance to leading competitors' products but at a lower cost and more highly available legacy node (n-1 advantage)" (rhetorical claim attributed to Brennan).

### HiWire AECs (adjacent component family)

**HiWire AEC product line** is structurally distinct from optical DSP business; CRDO HiWire AECs target server-to-ToR connectivity at 100G/200G/400G/800G/1.6T data speeds. Per Brennan Q3 FY2026 call: "AECs are now the de facto standard for intra-rack and rack-to-rack connectivity up to seven meters, increasingly displacing laser-based optical modules" (rhetorical claim). "Fifth hyperscaler" AEC win per Q3 call. Microsoft HiWire Switch AEC partnership for dual-Top-of-Rack architecture (CRDO 10-K FY2025).

### Blue Heron 200G/lane retimer

Brennan Q3 FY2026 call: "Blue Heron, our 200 gig per lane retimer that is purpose-built for scale of AI. It leverages our SerDes expertise to deliver long reach, energy efficiency, and advanced telemetry with support for UALink, Ethernet, and ESUN protocols." Protocol-spanning positioning (UALink + Ethernet + ESUN) — distinguishes from MRVL UALink-focused switching and AVGO Ethernet-focused Tomahawk.

### 1.6T leadership positioning + protocol-spanning

CRDO Q3 FY2026 call: "Our 1.6T AECs will support Ethernet, UALink, and ESUN protocols. Additionally, our PCIe 6.0 AECs are sampling now and will be released to mass production in first half fiscal 2027." Cross-validates against MRVL UALink switching products and AVGO Ethernet/copper-DAC scale-up advocacy — three distinct protocol-tier positions.

### Three new TAM expansions

**ZeroFlap optics** — production ramp pulled forward to Q1 FY2027; TensorWave first production neocloud customer; 3 additional in qualification (hyperscalers + neoclouds). Brennan Q3 call: "1,000x better reliability than commodity laser-based optics, while consuming roughly half the power" (rhetorical claim). Direct CPO displacement framing per Brennan: ZeroFlap is "the first time anybody has taken an optical transceiver up the stack to deliver real-time telemetry data... so you can make real-time decisions identifying and mitigating potential link flaps before they happen."

**Active LED Cables (ALCs) via Hyperlume acquisition.** MicroLED technology integrated for mid-reach optical (up to 30m). First sample/qualification fiscal 2027; production ramp fiscal 2028. ALCs "extend our system-level AEC philosophy into mid-reach optical" combining connectivity architecture with MicroLED expertise.

**OmniConnect / Weaver gearbox** — XPU connectivity via purpose-built VSR SerDes. Weaver "enables up to a 10x improvement in memory beachfront IO density with reach up to 10 inches." First customer Positron (inference XPU 2TB memory). Future OmniConnect gearboxes targeting "near package optics with MicroLED that will address the reliability, serviceability, and availability pitfalls of current CPO solutions" — **direct CPO displacement framing** (per Brennan Q3 call). Production ramp fiscal 2028.

### Vertical integration pattern

Vertically integrated system-level model at smaller operational scale than MRVL Photonic Fabric. Brennan Q3 call: "Our purpose-built SerDes and ICs, vertically integrated system model, and deep hyperscaler partnerships win at scale. We established leadership in high reliability copper connectivity and built strong position in optical DSPs and retimers." System-level integration without Layer 1 platform — distinguishes from AVGO Tomahawk + Taurus pattern.

### Customer concentration broadening

Customer A (contracting entity) declining: 67% FY2025 → 48% Q3 FY2026 (revenue); 86% AR → 57% AR. Customer B emerged at 39% Q3 FY2026 revenue. Customer C emerged at 11% AR by January 31, 2026. Top 10 customers = 90% of FY2025 revenue. Three to four customers expected >10% in coming quarters per CFO Dan Fleming Q3 call.

Customer A inferable as Microsoft per HiWire AEC Top-of-Rack architecture context (CRDO.md Session 27 per Disclosed/inferable/unknown convention).

### Financial trajectory

FY2025 revenue $436.8M (+126% YoY from $193.0M FY2024). Q3 FY2026 standalone $407M (+52% sequential, >+200% YoY). FY2027 outlook ">50% year-over-year growth" (Brennan Q3 call rhetorical projection). Non-GAAP gross margin Q3 FY2026 68.6% (above guidance high end); non-GAAP net income $208.8M (record; +63% sequential).

## Competitive dynamics across three companies

### Node leadership trade-offs

| Company | DSP product | Node strategy | Positioning |
|---|---|---|---|
| MRVL | Ara | 3nm leading-edge | Eight 200G electrical + eight 200G optical lanes; 400G/lane demonstrated; Interconnect Product of the Year Feb 2026 |
| AVGO | Taurus | leading-edge | Hock Tan: "we are the only one out there at 1.6T DSP" (rhetorical claim); 200G SerDes leadership; first 400G/lane optical DSP |
| CRDO | Cardinal | n-1 mature node | Brennan: "similar performance to leading competitors' products but at a lower cost and more highly available legacy node (n-1 advantage)" (rhetorical claim) |

Per honest-verdict discipline: no forced winner attribution. Each company positions node strategy as competitive advantage at different angle. MRVL leverages technical demonstration + industry award; AVGO leverages 1.6T DSP "only one out there" rhetorical claim; CRDO leverages n-1 cost-availability advantage. Trade-off: leading-edge node performance vs cost vs availability.

### Vertical integration pattern distinction (three patterns)

1. **AVGO** — Layer 1 platform (Tomahawk switch ASIC) + Layer 3 component (Taurus DSP) vertical integration; 200G SerDes IP as structural moat; copper DAC scale-up advocacy
2. **MRVL** — Layer 3 component (Ara DSP, Inphi-inherited coherent DSPs) + Layer 2-tier ambition via Photonic Fabric (Celestial AI $1.3B-$5.5B); aggressive XPU control-point ambition through chiplet integration; Layer 3 → Layer 2 trajectory in-progress
3. **CRDO** — Vertically integrated system-level model at smaller operational scale; HiWire AECs + Cardinal Optical DSPs + PCIe retimers + ZeroFlap + ALCs + OmniConnect; system integration without Layer 1 platform

### CPO strategy distinction (three strategies)

| Company | CPO strategy | Status |
|---|---|---|
| AVGO | Bailly platform never named in vault sources; "we are the lead in CPOs" + "bright shiny objects" dismissal; copper DAC scale-up advocacy | CPO incumbent in rhetorical claim; deferred timeline; symmetric exposure (Taurus DSP demand profile changes with CPO architecture) |
| MRVL | Photonic Fabric direct CPO platform competitor; $500M FY2028 / $1B FY2029 annualized run rate projections; chiplet integration into XPUs and scale-up switches | Direct CPO competitor; aggressive commercial trajectory framing; asymmetric exposure (gain via Photonic Fabric ramp) |
| CRDO | ZeroFlap + OmniConnect direct CPO displacement framing ("near package optics with MicroLED that will address the reliability, serviceability, and availability pitfalls of current CPO solutions" — Brennan) | CPO displacement claimant; asymmetric exposure (gain if displacement occurs; loss if CPO wins) |

Three distinct CPO strategies preserve genuine competitive uncertainty per honest-verdict discipline. No forced winner attribution.

### Reciprocal non-naming pattern

[[NVDA]] was never named in MRVL's Q4 FY2026 call (reciprocal non-naming pattern at Layers 1, 2, and 3 per MRVL.md Session 9). **This reciprocal-non-naming pattern is BROKEN for MRVL↔NVDA as of Q1 FY2027 (S102; see the "Q1 FY2027 update" subsection above)** — MRVL now names NVIDIA throughout (optics/silicon-photonics collaboration + NVLink Fusion + a $2.0B NVIDIA convertible-preferred investment; [[NVDA-platform-integration]] **Mode 4**, equity + partnership + merchant-silicon competitor overlap, FIRST INSTANCE). The Q4 FY2026 non-naming observation is preserved as the prior-quarter record; the *current* relationship is named-partner-AND-competitor, and the vault's reciprocal-non-naming convention is flagged for reconciliation (codification candidate). [[AVGO]] never named in MRVL Q4 FY2026 call but is "competition from another supplier" at lead XPU customer per multiple analyst references. [[ALAB]] is named as direct competitor in ALAB's 10-K FY2025; both companies compete in scale-up fabric switching market — MRVL via UALink switches + Photonic Fabric; ALAB via Scorpio X-Series + NVLink Fusion.

CRDO Q3 FY2026 call: ZERO direct mention of MRVL or AVGO by name. Reciprocal non-naming extends to merchant DSP/PHY chokepoint participants.

## Customer concentration patterns

### Hyperscaler customer overlap (inferable per Disclosed/inferable/unknown convention)

**Disclosed:**
- MRVL — Microsoft + AWS + Google + Meta hyperscaler co-design (multiple programs over time per MRVL.md); FY2025 + FY2026 customer warrants confirm at least two major custom programs with equity-participation structures
- AVGO — 6 named hyperscaler customers per Q1 FY2026 call: Google TPU, Anthropic 1GW TPU compute (potentially Google TPU derivative per Hock Tan Freudian slip), Meta MTIA, Apple, plus two unnamed
- CRDO — Customer A 48% Q3 FY2026 (likely Microsoft per HiWire context); Customer B emerged 39% (anonymized; possibly fifth-hyperscaler win); top 10 = 90% of FY2025 revenue

**Inferable:** All three companies serve hyperscaler customer base with significant overlap. Specific customer-by-customer matrix not constructible from disclosures.

**Unknown:** Customer-program-specific component sourcing relationships. Whether MRVL Ara DSP + AVGO Taurus DSP + CRDO Cardinal DSPs are deployed in same hyperscaler programs (multi-vendor strategy) or different programs (sole-source strategy) not disclosed.

### Customer concentration trajectory differences

| Company | Profile |
|---|---|
| MRVL | Multi-year hyperscaler co-design + customer warrants; data center grew from 40% to 74% of revenue in two years; custom silicon doubled YoY |
| AVGO | 6 named customers with multi-program multi-generation relationships; Google TPU concentration via Anthropic potential derivative; gigawatt-scale custom ASIC programs |
| CRDO | Single-customer-dominance broadening — Customer A 67% FY2025 → **49% FY2026** (10-K); a 2nd ≥10% customer emerged (32%); Q4 end-customer split **34/27/16/10** (four ≥10%); neoclouds → possibly ~20% (FY2026 refresh, S171) |

Three distinct customer concentration profiles. CRDO trajectory most distinct — broadening pattern (high concentration narrowing) vs MRVL/AVGO multi-customer mature concentration.

## CPO displacement implications

CPO displacement risk profiles asymmetric across three companies per Phase 1 synthesis:

- **AVGO Taurus + Tomahawk** — symmetric CPO exposure. CPO architecture changes Sian DSP demand profile; Tomahawk switch ASIC integrates with both pluggable optics (current architecture) and CPO-integrated optics (future architecture). AVGO copper DAC scale-up advocacy positions away from CPO scale-up specifically; scale-out optical transitions to CPO would impact Taurus DSP merchant demand.
- **MRVL Ara + Photonic Fabric** — asymmetric exposure favoring CPO transition. Photonic Fabric is direct CPO platform competitor; Photonic Fabric chiplet integration into XPUs and scale-up switches captures CPO architectural value; Ara DSP merchant demand at risk if CPO scale-out displaces pluggable optics; net exposure depends on Photonic Fabric revenue ramp ($500M FY2028 / $1B FY2029 targets) vs Ara DSP merchant demand erosion.
- **CRDO Cardinal + ZeroFlap + OmniConnect** — asymmetric exposure favoring CRDO if CPO displacement occurs. CRDO ZeroFlap explicit displacement claimant ("near package optics with MicroLED that will address the reliability, serviceability, and availability pitfalls of current CPO solutions" — Brennan). Cardinal DSP merchant demand at risk if CPO captures pluggable share, but CRDO ZeroFlap + ALCs + OmniConnect Weaver positioned to capture displacement value via MicroLED technology stack. **FY2026 refresh (S171):** the exposure is no longer purely displacement — the **DustPhotonics** acquisition (SiPho PIC, closed late-May 2026) gives CRDO a *direct path into* CPO/NPO architectures (initial revenue FY2028), so CRDO now straddles both sides of the CPO question (displacement via OmniConnect/MicroLED AND participation via SiPho). See [[cpo-integration]].

Per honest-verdict discipline: no forced winner attribution. CPO displacement timing and architectural outcomes remain genuinely uncertain. All three companies have credible competitive positions across different CPO scenarios.

## Cross-references

- [[chokepoint-investability-priorities]] Chokepoint 2 (Optical DSP / PHY power-performance) — Tier 3-anchored vault-canonical reference; this chokepoint page provides multi-source synthesis depth complementing theme page breadth
- [[datacenter-photonics-supply-chain]] Section 2.3 (Optical DSPs / PHYs / SerDes) — supply-chain map context; this chokepoint page provides chokepoint-specific synthesis vs supply-chain-layer breadth
- [[InP-supply]] — adjacent Chokepoint 1 (substrate supply for laser/EML production); upstream of optical DSP/PHY in supply chain flow
- [[datacenter-laser-supply]] — adjacent Chokepoint 1 (laser/EML supply); structurally parallel to optical DSP/PHY layer (lasers + DSPs are both in optical module integration)
- [[CPO-platform-battle]] — five-way executive comparison context for CPO strategy distinction; Layer 1 divergence (NVDA adoption vs AVGO active dismissal) framework
- [[NVDA-platform-integration]] — Layer 1 platform context; six-modality integration framework for NVDA platform-tier control point
- [[MRVL]] — vault company anchor; Session 9 ingest baseline + Session 19 Celestial codification + Session 24 Framework 2.6 codification
- [[AVGO]] — vault company anchor; Session 10 ingest baseline + Session 24 Framework 2.6 codification
- [[CRDO]] — vault company anchor; Session 27 paired ingest with [[ANET]]
- [[CSCO]] — captive Acacia 3nm Kibo 1.6T PAM4 DSP cross-reference (captive in Cisco-branded pluggables, not merchant) per [[datacenter-photonics-supply-chain]] Section 2.3

## Open questions

1. **Node leadership trajectory.** Will MRVL Ara 3nm leading-edge advantage hold against AVGO Taurus + CRDO Cardinal n-1 cost-availability advantage as 1.6T transition progresses? Hyperscaler qualification cycles may favor different node strategies in different deployment scenarios.
2. **CPO winner determination timing.** Will CPO architecturally displace pluggable optics, and on what timeline? AVGO 2027+ deferred; MRVL FY2028 commercial deployment; CRDO ZeroFlap Q1 FY2027 production ramp + MicroLED-based "near package optics" framing. Three distinct CPO timelines.
3. **Customer concentration evolution.** Will CRDO continue broadening (Customer A 48% Q3 FY2026 → further dilution as 5+ customers emerge >10%)? Will MRVL custom warrants vest at scale across multiple hyperscaler programs? Will AVGO Anthropic-as-Google-TPU-derivative observation hold or resolve as Anthropic scales?
4. **Protocol fragmentation outcomes.** UALink + ESUN + Ultra Ethernet + proprietary scale-up — which protocols survive at scale? CRDO protocol-spanning positioning (UALink + Ethernet + ESUN) hedges; MRVL UALink-focused switching + AVGO Ethernet/copper-DAC scale-up advocacy concentrate.
5. **LPO/LRO displacement risk.** Per Tier 3 key flag — LPO (linear-drive pluggable optics) and LRO can shift equalization burden between module and host; would displace DSP/PHY value capture if widely adopted. None of three vault companies report LPO/LRO as displacement risk in primary sources; warrants monitoring.
6. **Standards body participation outcomes.** UALink Consortium + Ultra Ethernet Consortium + ESUN — which company's standards-body participation translates to design-win outcomes? CRDO explicit protocol participation; MRVL UALink switching products; AVGO Tomahawk SerDes-tier IEEE participation.
7. **CSCO Acacia captive-DSP demand evolution.** Will CSCO Acacia 3nm Kibo 1.6T PAM4 DSP transition from captive to merchant if CSCO competitive positioning shifts? Currently captive in Cisco-branded pluggables; not merchant DSP supplier.
8. **MaxLinear (MXL) Tier C high-beta challenger.** Per Tier 3 framework, MaxLinear Rushmore 1.6T PAM4 DSP is challenger candidate. MXL ingest pending future session per [[datacenter-photonics-supply-chain]] Future ingest candidates Tier C; would test CRDO-vs-MXL high-beta-challenger competitive dynamics.

## What would confirm or weaken this framing

### Confirm signals

- **1.6T design win count** at hyperscaler-tier customers across all three companies — multi-vendor 1.6T deployments confirm chokepoint multi-supplier concentration per Tier 3 framework
- **CPO production deployments** at scale (NVDA Quantum-X CPO production confirmed at GTC March 2026; AVGO Bailly platform confirmed in production; MRVL Photonic Fabric chiplet high-volume manufacturing per FY2028 commercial deployment target) — confirms three distinct CPO strategies playing out
- **CRDO customer broadening continuation** — fifth hyperscaler win + 5+ customers >10% of revenue confirms Customer A concentration narrowing
- **Photonic Fabric revenue ramp** — $500M FY2028 / $1B FY2029 MRVL targets — confirms direct CPO competitor commercial trajectory
- **AVGO Tomahawk + Taurus 1.6T DSP design wins** — confirms vertical integration pattern delivers ecosystem lock-in
- **Standards body convergence** — UALink + ESUN + Ultra Ethernet adoption at hyperscaler scale confirms protocol-spanning positioning thesis (CRDO Blue Heron 200G/lane retimer)

### Weaken signals

- **CPO displacement timing pull-forward** — earlier-than-expected CPO scale-up displacement of pluggable optics would weaken MRVL/AVGO/CRDO Cardinal merchant DSP demand
- **Node leadership reversal** — n-1 cost-availability advantage outpacing leading-edge node performance at 1.6T scale would weaken MRVL Ara + AVGO Taurus rhetorical positioning vs CRDO Cardinal cost-availability framing
- **Customer concentration narrowing** at MRVL or AVGO — single-hyperscaler-program dependency at scale would weaken multi-customer franchise framing
- **LPO/LRO captures pluggable share** — equalization burden shift between module and host would weaken DSP value capture (per Tier 3 framework key flag)
- **MaxLinear (MXL) Rushmore captures meaningful 1.6T share** — challenger displacement would weaken MRVL/AVGO incumbent dominance per Tier 3 framework "MRVL/AVGO primary" characterization
- **CRDO ZeroFlap + OmniConnect commercial ramp disappointment** — failure to capture CPO displacement value would weaken CRDO 1.6T leadership claim and protocol-spanning positioning thesis

## Source attribution

**Tier 3 framework reference:** `raw/research/photonics-chokepoint-table.md` Chokepoint 2 (Optical DSPs / PHYs / power-performance) / Ranking Summary Rank 2; very high conviction. Vic-team-authored canonical living document. Per A2 structural requirements: Tier 3 source attribution at page-top + per-section + Source attribution + Source audit notes; counterparty-attribution-only annotation continues for non-vault company references (MaxLinear, MTSI, Alphawave Semi, Synopsys, Cadence, Semtech).

**Primary-source vault company anchors (3 companies):**

- **[[MRVL]]** — Session 9 ingest baseline (10-K FY2025 + 10-Q Q3 FY2026 + Q3 FY2026 call); Session 19 Celestial AI codification (acquisition closed February 2, 2026); Session 24 Framework 2.6 control-point distinction integration; Session 25 [[chokepoint-investability-priorities]] Chokepoint 2 vault-status.
- **[[AVGO]]** — Session 10 ingest baseline (10-K FY2025 + 10-Q Q1 FY2026 + Q1 FY2026 call); Session 24 Framework 2.6 control-point distinction integration; Session 25 [[chokepoint-investability-priorities]] Chokepoint 2 vault-status.
- **[[CRDO]]** — Session 27 paired ingest with [[ANET]] (10-K FY2025 + 10-Q Q3 FY2026 + Q3 FY2026 call dated March 2, 2026); first vault Chokepoint 2 third-source threshold satisfaction per Session 25 hybrid architecture.

**Cross-reference vault chokepoint pages:** [[InP-supply]] (Session 13 first canonical chokepoint page); [[datacenter-laser-supply]] (Session 4 chokepoint page); [[wafer-level-siph-test]] (Session 25 provisional chokepoint page).

## Source audit notes

### MRVL Session 9 ingest reference

Session 9 baseline (MRVL 10-K FY2025 + 10-Q Q3 FY2026 + Q3 FY2026 call). Subsequent updates: Session 19 Celestial AI codification ($1.3B cash + $5.5B max with earn-outs; closed February 2, 2026; $500M FY2028 / $1B FY2029 annualized run rate projections per Murphy Q4 FY2026 call). Session 24 Framework 2.6 control-point distinction integration (bottleneck-tier with control-point aspirations alongside [[CRDO]] post-Session 27 codification). Session 25 [[chokepoint-investability-priorities]] vault-status promotion.

**Tier 1/Tier 2 framing gap (widest in vault).** 10-K corporate/procedural treatment of Celestial vs earnings call commercially aggressive treatment — preserved as canonical observation per CLAUDE.md Tier 1/Tier 2 framing gap convention (sub-pattern: technology-content gap).

**Murphy CEO combativeness instance** — "Do you see me blinking?" defensive Q4 FY2026 call passage. CEO combativeness convention monitoring (currently 2 instances vault-wide).

### AVGO Session 10 ingest reference

Session 10 baseline (AVGO 10-K FY2025 + 10-Q Q1 FY2026 + Q1 FY2026 call). Subsequent updates: Session 24 Framework 2.6 control-point distinction integration (control point with bottleneck participation alongside Tomahawk + Taurus + custom ASIC franchise + Bailly CPO platform decisions). Session 25 [[chokepoint-investability-priorities]] vault-status promotion.

**Bailly CPO platform never named** in any of three primary sources — most explicit CPO-silence-with-rhetorical-claim variant in vault. Layer 1 active dismissal variant per [[CPO-platform-battle]].

**Hock Tan CEO combativeness instance** — "you must be a bit hallucinating" defensive response. CEO combativeness convention monitoring (second instance at Session 10).

**95% TSMC dependency** — most explicit foundry dependency disclosure in vault per AVGO 10-K FY2025.

### CRDO Session 27 ingest reference

Session 27 paired ingest with [[ANET]] (CRDO 10-K FY2025 + 10-Q Q3 FY2026 + Q3 FY2026 call dated March 2, 2026). First Layer 3 specialized designer DSP/PHY component company added since [[MRVL]] (Session 9) and [[AVGO]] (Session 10). Closed Chokepoint 2 (Optical DSP/PHY) third primary-source threshold per Session 25 hybrid architecture.

**Hyperlume vs Comira kickoff hypothesis falsification** (Session 27 Phase 0) — kickoff cited "Comira acquisition" for MicroLED tech; CRDO Q3 FY2026 call cites Hyperlume acquisition. Documented on [[CRDO]] page; A6 (g) factual error scope sub-pattern.

**Customer concentration broadening** — Customer A (contracting entity) 67% FY2025 → 48% Q3 FY2026; Customer B emerged 39% Q3 FY2026; trajectory most distinct profile across three vault companies at Optical DSP/PHY chokepoint.

### A6 v8 (g) Phase 0 verification — Session 30 kickoff hypothesis falsifications (3 instances)

Per CLAUDE.md v8 A6 application discipline + kickoff hypothesis falsification convention, three Session 30 kickoff hypothesis falsifications surfaced at Phase 0 verification:

1. **"AVGO Sian3 3nm DSP"** — kickoff prompt cited Sian3 product name multiple times. Vault canonical content (AVGO.md + [[datacenter-photonics-supply-chain]] Section 2.3) shows AVGO product naming as **Taurus 400G/lane optical DSP** (no "Sian3" product exists). Synthesis uses canonical Taurus product name throughout.
2. **"MRVL Spica DSP"** — kickoff prompt cited Spica product name multiple times. Vault canonical content (MRVL.md + Section 2.3) shows MRVL product naming as **Ara 3nm 1.6T PAM4 DSP** (no "Spica" product exists). Synthesis uses canonical Ara product name throughout.
3. **"MRVL Coherent DSP — Acacia acquisition"** — kickoff prompt attributed MRVL coherent DSP capability to "$1.1B Acacia acquisition (closed December 2021)." Acacia Communications was acquired by [[CSCO]], not by MRVL. MRVL coherent DSP capability is from Inphi acquisition (April 2021, $10B). Synthesis attributes MRVL coherent DSPs to Inphi inheritance only.

Plus 1 frontmatter discrepancy: kickoff "AVGO Layer 1+3 / photonics_tier 2" — actual canonical AVGO.md frontmatter is `layer: 1, photonics_tier: 3` with Layer 1/3 straddling tension documented in Thesis role only. Synthesis uses canonical Layer 1 / photonics_tier 3 placement.

Pattern follows Session 27 Hyperlume vs Comira precedent. A6 v8 (g) factual error scope sub-pattern instance count post-Session 30: Session 26 addendum (1) + Session 27 (1 Hyperlume) + Session 30 (3) = **5 instances accumulated**. Codification refinement to (g)/(g)' subtypes triggerable at next codification session per Session 29 codification cadence reset (next trigger Session 34+ or 5+ accumulated items).

## Change log

- **2026-06-24 (S171 — [[CRDO]] FY2026 refresh propagation):** Added a FY2026 refresh note to the CRDO positioning section (blow-out year +206%; the copper→optical pivot with a ~$600M FY2027 optical ramp — DSPs the named >$100M leg; DustPhotonics SiPho PIC adds a direct CPO/NPO path, FY2028). Updated the customer-concentration row (A 67%→49%; Q4 end-customer 34/27/16/10) + the CPO-displacement profile (CRDO now straddles displacement AND SiPho participation). Placement HELD (Layer 3 / photonics_tier 3). last_updated 2026-05-29 → 2026-06-24.
- **2026-05-29 (S110 cross-vault re-evaluation propagation — A8 + B2 fix):** Fixed the internal self-contradiction in the "Reciprocal non-naming pattern" section — the standing "NVDA never named in MRVL" statement was contradicted by the page's own Q1 FY2027 subsection (which names the NVIDIA partnership + $2.0B stake). Added an inline note that the MRVL↔NVDA reciprocal-non-naming pattern is **BROKEN as of Q1 FY2027** ([[NVDA-platform-integration]] Mode 4); Q4 FY2026 observation preserved as prior-quarter record; convention flagged for reconciliation (codification candidate). Refreshed the CSCO Acacia captive cross-ref with the Q3 FY2026 (S108) scale (>$1B orders / >200% FY2026 / 2 named hyperscaler optics wins) while preserving the captive framing. No tier/participant changes.
- **2026-05-29 (MRVL Q1 FY2027 refresh propagation):** Added "Q1 FY2027 update" subsection to MRVL positioning — interconnect growth raised to >70% FY2027; 200G/lane 1.6T ramping + 400G/lane (OFC Apr 2025); first secure 1.6T ZR/ZR+ DCI on new 2nm coherent DSP; coherent light 2-20km; DCI line-of-sight ~$1B FY2028; TIAs/drivers >$1B run rate; AEC "Golden Cable" + retimers >2× FY2027 (3 Tier 1 hyperscalers). NVIDIA optics/silicon-photonics collaboration + $2.0B convertible-preferred + NVLink Fusion ([[NVDA-platform-integration]] Mode 4); Polariton plasmonics (3.2T; call-only); Celestial PPA $3.5B finalized. Margin trigger note updated to 52.1% / non-GAAP 58.9%. CEO-combativeness convention count unchanged at 2 (Q1 FY2027 tone measured). last_updated 2026-04-28 → 2026-05-29.
- **2026-04-28 (Session 30 multi-source synthesis — closes S27-S30 photonics completion arc):** Created from three vault primary-source company anchors per Session 25 hybrid architecture three-source threshold satisfaction: [[MRVL]] Session 9 ingest baseline + Session 19 Celestial AI codification + Session 24 Framework 2.6 codification; [[AVGO]] Session 10 ingest baseline + Session 24 Framework 2.6 codification; [[CRDO]] Session 27 paired ingest with [[ANET]]. **Second canonical multi-source-synthesis chokepoint page in vault history** (after [[InP-supply]] Session 13). **First dedicated chokepoint page operating under canonical CLAUDE.md v8** including A6 v8 (8 pattern types) + A2 second canonical application (Tier 3-anchored convention) + Outside Framework 5 codification (N/A; all three companies are Tier 3 photonics_tier) + parallel-but-independent paired-ingest variant codification (N/A; single chokepoint page creation) + foreign-issuer ingest convention (N/A; all three US-domiciled) + vault scope codification (operates within photonics primary scope). A6 v8 (g) Phase 0 verification surfaced 3 kickoff hypothesis falsifications (AVGO Sian3 → Taurus; MRVL Spica → Ara; MRVL Acacia attribution wrong-company; MRVL coherent DSPs from Inphi only) + 1 frontmatter discrepancy (AVGO Layer 1+3/photonics_tier 2 vs canonical Layer 1/photonics_tier 3); synthesis uses canonical vault content per A6 application discipline. Per-company depth allocation: MRVL ~115 lines + AVGO ~95 lines + CRDO ~115 lines + competitive dynamics ~50 lines + customer concentration ~30 lines + CPO displacement implications ~25 lines + cross-references / open questions / what would confirm or weaken / source attribution / source audit notes. Forward-wikilink discipline preserved: 16-session vault wikilink-clean streak post-Session 30 (extended from 15 post-Session 29). Per A2 structural requirements: Tier 3 source attribution at page-top + per-section + Source attribution + Source audit notes; counterparty-attribution-only annotation for non-vault company references (MaxLinear, MTSI/MACOM, Alphawave Semi, Synopsys, Cadence, Semtech). S27-S30 photonics completion arc closed: Sessions 27 (CRDO + ANET) + 28 (VIAV + PLAB) + 29 (CLAUDE.md v7 → v8 codification) + 30 (this chokepoint page).
- **2026-04-30 (Session 32 cross-reference — [[cpo-integration]] chokepoint page creation):** Cross-referenced from new chokepoint page [[cpo-integration]] (fourth canonical multi-source-synthesis chokepoint page in vault history; closes Tier 3 framework Chokepoint 10 dedicated chokepoint page coverage gap). MRVL Photonic Fabric scale-up CPO platform-tier ambition + AVGO Bailly never-named pattern + CRDO OmniConnect MicroLED CPO displacement positioning cross-referenced from [[cpo-integration]] per-company integration positioning sections (Tier A: MRVL/AVGO/CRDO ~65-70 lines each; alongside NVDA Tier A) + Layer 3 four-variant CPO profile preserved per [[CPO-platform-battle]] codification. Adjacent chokepoint dependency documented in [[cpo-integration]] Cross-chokepoint dependencies section: MRVL Ara + AVGO Taurus + CRDO Cardinal DSPs feed CPO modules; node leadership trade-offs (3nm vs 5nm vs n-1). **A6 v8 (g)/(g)' subtype instance count: 6 accumulated through Session 32** (incremented from 5 post-Session-30 by Session 32 (g)' subtype Phase 6 numbering-convention falsification documented in [[cpo-integration]] Source audit notes). **S27-S32 photonics chokepoint completion arc closed** (3 dedicated chokepoint pages: Chokepoint 2 Session 30 + Chokepoint 5 Session 31 + Chokepoint 10 Session 32). No content edits to this chokepoint page.
- **2026-04-30 (Session 33 cross-reference — [[InP-supply]] provisional → canonical promotion):** Adjacent chokepoint page [[InP-supply]] promoted from provisional to canonical multi-source-synthesis chokepoint page via Option C bifurcation handling — single page covers Tier 3 framework Chokepoint 3 (InP substrate supply) + Chokepoint 4 (InP epitaxial capacity) with internal subsection structure. **Fifth canonical multi-source-synthesis chokepoint page in vault history**. Cross-chokepoint relationship: optical DSP/PHY chokepoint (this page; Chokepoint 2) is electrically downstream of laser device output but architecturally adjacent to InP supply chain via signal-conditioning of laser-driven optical links. Light cross-reference only — DSP/PHY-tier and InP-tier are structurally distinct chokepoints; vault canonical Tier 3 Rank 2 vs Rank 3+4 separation preserved. No content edits to this chokepoint page.
