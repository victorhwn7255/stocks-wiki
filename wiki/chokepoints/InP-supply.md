---
type: chokepoint
tickers: [AXTI, LITE, COHR, AAOI, AVGO, VECO]
last_updated: 2026-05-29
---

# InP supply (substrate + epitaxial capacity)

*Tier 3 framework reference: `raw/research/photonics-chokepoint-table.md` Chokepoint 3 (InP substrate supply; Rank 3) + Chokepoint 4 (InP epitaxial capacity; Rank 4) unified treatment per Option C bifurcation handling — single page covering two adjacent Tier 3 ranks with internal subsection structure preserving framework's distinction. Mirrors [[cpo-integration]] Session 32 Option C handling of Scale-up + Scale-out CPO bifurcation per Murphy thesis. Vault canonical Tier 3 Rank numbering preserved.*

## Substrate-tier vs epitaxial-tier scope discipline

*Per Tier 3 framework: substrate-tier (Chokepoint 3) and epitaxial-tier (Chokepoint 4) are structurally distinct chokepoints — substrate alone is not enough; epitaxial process determines whether substrate availability translates into usable laser/EML/photodetector device output. Tier 3 framework: "Substrate alone is not enough. After the InP wafer exists, high-quality epitaxial layers must be grown before the wafer can become a laser, EML, photodiode, or other III-V photonic device. Epi quality affects device efficiency, reliability, output power, wavelength performance, and yield."*

**Covered here (substrate + epitaxial unified InP supply chain framework):**
- **Substrate-tier (Chokepoint 3):** AXTI primary-source vantage; supply concentration (2 vs 3 suppliers dispute); geopolitical dimension (China/Japan concentration); demand drivers; capacity expansion trajectory.
- **Epitaxial-tier (Chokepoint 4):** Equipment-tier (VECO Lumina+ MOCVD; Aixtron primary competitor); device-fabrication-tier epitaxial process (COHR six-inch device-fabrication advantage; LITE three-inch industry-standard; AAOI MBE+MOCVD dual-process vertical integration); wafer-size transition mechanics (4-inch → 6-inch InP).
- **Cross-tier interdependencies:** Substrate→epi→device chain mechanics; vertical integration moat dynamics; geopolitical mirror structure spanning substrate + equipment tiers.

**NOT covered here (other chokepoint page scope):**
- Laser/EML/III-V device-tier dynamics → [[datacenter-laser-supply]] (Chokepoint 1)
- Advanced optical packaging / alignment downstream of laser device fabrication → [[advanced-optical-packaging]] (Chokepoint 5)
- Optical DSP / PHY component dynamics → [[optical-dsp-phy-supply]] (Chokepoint 2)
- CPO integration mechanics → [[cpo-integration]] (Chokepoint 10; ELS architecture cross-references InP epitaxial supply for UHP CW laser supply)

## Overview

InP (indium phosphide) is the foundational compound-semiconductor substrate for datacenter optical components. The supply chain bottleneck operates at two distinct but interdependent tiers — substrate-layer crystal growth (Chokepoint 3) and epitaxial-layer device-fabrication process (Chokepoint 4) — with structurally distinct constraint mechanics but shared geopolitical exposure.

This page synthesizes InP supply chokepoint mechanics across five primary-source vault company vantages:

- **Substrate-tier (Chokepoint 3):** [[AXTI]] (Beijing-based InP substrate manufacturer; one of two-or-three global suppliers; February 2025 Chinese export controls)
- **Epitaxial-tier equipment vantage:** [[VECO]] (Lumina+ MOCVD systems; Aixtron primary competitor; Compound Semiconductor segment $60M FY2025)
- **Epitaxial-tier device-fabrication vantages:** [[COHR]] (six-inch InP device-fabrication advantage at Sherman + Järfälla + Zürich); [[LITE]] (three-inch InP industry-standard manufacturing + 40% capacity expansion); [[AAOI]] (Sugar Land TX MBE + MOCVD dual-process vertical integration)

The supply chain flows:

```
Indium feedstock (JX Advanced Metals dominant — non-vault; ~78% global share per architecture primer)
  → InP substrate (AXTI / Sumitomo / JX Nippon — Chokepoint 3)
    → MOCVD epitaxial growth (VECO Lumina+ / Aixtron equipment — Chokepoint 4 equipment-tier)
      → Epitaxial process at device fabricator (COHR / LITE / AAOI in-house — Chokepoint 4 device-fabrication-tier)
        → Laser / EML / photodetector device fabrication ([[datacenter-laser-supply]] — Chokepoint 1)
          → Transceiver assembly ([[advanced-optical-packaging]] — Chokepoint 5)
```

**Provisional → canonical promotion:** Page promoted from provisional (single-source AXTI primary baseline; Session 13) to canonical multi-source-synthesis chokepoint page at Session 33 via four additional vault primary-source vantages (VECO equipment-tier + COHR/LITE/AAOI device-fabrication-tier epitaxial process). Three-source threshold satisfied multi-fold per Session 25 hybrid architecture; closes Tier 3 framework Chokepoint 3 + Chokepoint 4 dedicated chokepoint page coverage gap.

**Vault five-vantage concentration with structural diversity:** Substrate-tier vantage (AXTI Layer 6 / Beijing-based) + Equipment-tier vantage (VECO Layer 6 / US-manufactured) + Device-fabrication-tier vantages (COHR Layer 4 / six-inch advantage + LITE Layer 4 / three-inch industry-standard + AAOI Layer 5 / Layer 4/5 straddling per Session 15 codification).

## Substrate-tier (Chokepoint 3 — Tier 3 Rank 3)

### Supply chain position — substrate layer

InP substrates are the foundational input for datacenter optical components. Crystal growth capacity is concentrated among 2-3 commercially significant global suppliers, all in China or Japan; no InP substrate manufacturing exists in the United States or Europe. The substrate-tier constraint is volume capacity + qualification cycles + geopolitical export-control gating.

### Supply concentration — disputed between AXTI's own sources

The number of commercially significant InP substrate suppliers is disputed between AXTI's own primary sources:

- **AXTI 10-K FY2025 (Tier 1):** "There are three primary suppliers of InP substrates worldwide" — AXTI, Sumitomo Electric Industries (Japan), and JX Nippon Mining & Metals (Japan).
- **AXTI Q4 FY2025 earnings call (Tier 2):** CEO Morris Young: "Today there are two InP substrate suppliers in the world, and we're one of them."

**Tier 1/Tier 2 framing gap (per CLAUDE.md v8 convention; risk-framing sub-pattern).** The filing acknowledges three-player competitive landscape; the call asserts duopoly narrative positioning AXTI as more dominant. The framing gap is structurally significant: the filing complies with SEC disclosure obligations on competitive landscape; the call positions AXTI as more dominant than the filing supports.

Whether the supply base is two or three participants, the structural constraint is the same: global InP substrate production is concentrated among a very small number of suppliers, all located in either China (AXTI, 100% of manufacturing) or Japan (Sumitomo, JX Nippon).

**Current capacity:** AXTI's InP substrate revenue was approximately $8M/quarter in Q4 FY2025 (AXTI Q4 FY2025 call), with a $60M+ backlog and plans to double capacity by end 2026 through a $30M brownfield expansion. Sumitomo and JX Nippon capacity figures are not available from AXTI sources.

**Substrate-tier update (AXTI Q1 FY2026, period ended March 31, 2026).** The substrate constraint tightened and AXTI's response escalated:
- **Backlog $60M+ → $100M+** (new high); InP now >50% of AXTI revenue; Q2 FY2026 guided to be AXTI's largest-ever InP quarter (exceeding the prior $17.7M COVID-era high). AXTI also reached a **profitability inflection** (revenue +39% YoY to $26.9M; non-GAAP gross margin rebounding to 29.9%; Q2 guided to GAAP + non-GAAP profitability) — the substrate demand signal converting to results.
- **Capacity roadmap escalated and funded.** From ~$8M/quarter, AXTI now targets ~$35M/quarter by end-2026 (brownfield, ahead of plan), doubling again to ~$65-70M/quarter by end-2027/early-2028 (adjacent Beijing facility), with a 2028 greenfield under planning (possibly outside China). Funded by an **April 2026 $632.5M capital raise**. Management stresses demand "is 10x" the planned doubling — i.e., the constraint persists even after expansion.
- **China-demand leg (new).** AXTI's China InP-laser-market revenue more than doubled QoQ in Q1 and is guided to double again in Q2; China estimated at ~30% of the global InP demand AXTI sees in Q2, rising toward ~40% by Q4, as China builds its own optical/CPO supply chain. In-China shipments require **no export permit** — China demand is unconstrained by the export-control gate.
- **Export-control gate (Section 4.3 update).** Non-US permits continue to flow readily; **US-destined permits remain pending** (reframed from the prior "first denials" — China's Ministry of Commerce has requested additional data on US applications). 6-inch InP qualification is advancing for both iron-doped (laser) and sulfur-doped (photodetector) specs. The geopolitical-chokepoint dimension is unchanged: all AXTI production is in China, gating US-destined supply.

The supply-concentration dispute above is preserved as a prior-instance Tier 1/Tier 2 framing gap; the Q1 FY2026 call did not repeat the "two suppliers" claim (it emphasized "strongest position to grow capacity"), so the framing gap is not re-fired this quarter.

### Substrate-tier demand drivers

InP substrate demand is driven by the downstream proliferation of InP-based lasers for datacenter optical interconnects. The primary demand vectors:

1. **800G/1.6T transceiver deployment:** Each generation of transceiver speed increase requires more InP laser die per module, increasing substrate consumption per unit deployed.
2. **Datacenter build rate:** Hyperscaler AI infrastructure expansion drives raw volume of optical interconnect deployment.
3. **CPO (co-packaged optics) — substrate-tier amplifier dimension:** At the substrate level, CPO is a demand amplifier rather than a displacement threat. CPO architectures integrate more laser die per switch package than pluggable transceivers, potentially increasing InP substrate consumption per unit. AXTI management explicitly framed CPO as "yet another inflection point" for substrate demand beginning "late 2027 and beyond" (Young, AXTI Q4 FY2025 call). This contrasts with higher-layer companies where CPO is viewed as potentially displacing existing pluggable products. See [[CPO-platform-battle]] for the full CPO dynamics including the substrate-tier demand amplifier dimension; see [[cpo-integration]] for ELS architecture preservation of Layer 4 component-tier value through CPO transition.

## Epitaxial-tier (Chokepoint 4 — Tier 3 Rank 4)

### Why epitaxial capacity is structurally distinct from substrate availability

Per Tier 3 framework: substrate alone does not produce a usable photonic device. After the InP wafer exists, high-quality epitaxial layers must be grown before the wafer can become a laser, EML, photodiode, or other III-V photonic device. Epi quality affects device efficiency, reliability, output power, wavelength performance, and yield. MOCVD capacity, process recipes, uniformity, defect density, and operator know-how determine whether the industry can convert substrate availability into usable laser-device output. Poor epi quality can destroy yield even when substrate supply is adequate.

The epitaxial-tier chokepoint operates at two sub-layers:
- **Equipment-tier:** MOCVD reactor manufacturing (VECO Lumina+; Aixtron primary competitor)
- **Device-fabrication-tier:** Epitaxial process at laser-device fabricator (COHR / LITE / AAOI in-house epi)

### Equipment-tier sub-layer — MOCVD reactor supply (VECO + Aixtron)

The MOCVD equipment layer sits between substrate manufacturing and device fabrication.

**[[VECO]] (Lumina+ MOCVD).** VECO's Lumina+ tools grow epitaxial layers on InP and GaAs substrates that become laser devices. Position: one step downstream of [[AXTI]] (substrates) and one step upstream of [[LITE]] / [[COHR]] / [[AAOI]] (device fabrication) in the InP photonics supply chain.

- Compound Semiconductor segment: $60M FY2025 (declined 25.9% from $81M FY2024); guided to $80M FY2026 (VECO 10-K FY2025)
- Segment is VECO's smallest reporting segment (9% of FY2025 revenue); ion beam and laser processing remains the dominant revenue contributor
- Product line: Lumina+ MOCVD for compound semiconductors (GaAs and InP-based materials for photonics, RF, power devices); Aixtron named as primary MOCVD competitor (VECO 10-K FY2025)
- 99.4% of VECO's PP&E is in the United States (VECO 10-K FY2025) — relevant for export control dynamics
- *Epiluvac SiC impairment (FY2025 $28.1M)* analytically irrelevant to photonics thesis but explains operating income decline; SiC epitaxy weakness distinct from InP/GaAs epitaxy positioning

**Aixtron (Germany).** Primary MOCVD competitor per VECO 10-K FY2025. Not in vault; relative market share vs VECO for InP-relevant installations is unknown — Tier B future-ingest candidate per [[chokepoint-investability-priorities]].

**Equipment-tier binding-constraint assessment.** MOCVD tool availability has not been identified as a binding constraint in any ingested vault primary source. The potential chokepoint at equipment-tier operates more through US export controls restricting MOCVD equipment sales to China-based InP growers (secondary constraint on AXTI capacity expansion) than through tool supply scarcity itself.

### Device-fabrication-tier sub-layer — three Layer 4 wafer-size positions

The vault has primary-source coverage at three Layer 4 device-fabrication-tier positions exhibiting structurally distinct InP epitaxial process strategies. Honest-verdict discipline applies — three wafer-size positions preserved without forced winner attribution.

**[[COHR]] — six-inch InP device-fabrication advantage.** Multi-site six-inch InP device-fabrication position at Sherman + Järfälla + Zürich (COHR 10-K FY2025; COHR Q2 FY2026 call). The defensible claim is narrower than substrate-level "monopoly" framing per Session 5 silicon-photonics-primer.md cross-validation: Sumitomo, AXT, and IQE all have six-inch InP substrate or epitaxial capability; JX Advanced Metals is a relevant InP supplier at four-inch scale. COHR's structurally significant advantage sits at device-fabrication — the ability to process six-inch wafers through high-yield epitaxy, lithography, etch, metallization, passivation, facet preparation, device testing, and qualification for specific CPO-grade products.

- **Wafer-size economics (Anderson, COHR Q2 FY2026 call):** ">4x chips at <50% cost vs three-inch" — the ~8x cost-per-chip improvement underpins six-inch device-fabrication moat
- **Capacity ramp trajectory:** Quadrupled InP wafer starts from September to December quarter; wafer starts at 80% of target capacity, "ahead of schedule" (COHR Q2 FY2026 call)
- **Forward capacity plan:** Plans to double total InP capacity by end calendar 2026 (COHR Q2 FY2026 call)
- **Vertical integration scope:** Substrate → epitaxy → chip → module → system (broadest in vault per Session 31 codification)

**[[LITE]] — three-inch InP industry-standard manufacturing.** Three-inch InP is industry standard, not inferior; scaling to six-inch raises brittleness, stress, and yield challenges (per silicon-photonics-primer.md Session 5 codification preserved). LITE's three-inch positioning is the industry baseline.

- **Capacity expansion:** 40% capacity expansion announced (LITE Q2 FY2026 call); demand framing "we cannot keep up with what we're seeing"
- **NVDA $2B equity-plus-purchase modality (March 2026):** Capital-offset-for-supply-assurance framing per Session 22 [[NVDA-platform-integration]] codification; LITE retains Layer 4 component supplier value through CPO transition via UHP CW laser supply for ELS architecture (cross-reference [[cpo-integration]] component-tier value capture subsection)
- **400mW UHP CW laser positioning:** "Not something that many people can do" Sumino LITE Q2 FY2026 call (over-claim mode rhetorical) — competitive moat at the laser-device output of three-inch InP epitaxial process

**[[AAOI]] — Sugar Land TX MBE + MOCVD dual-process vertical integration.** AAOI manufactures InP and GaAs laser chips in-house at Sugar Land, TX using MBE (molecular beam epitaxy) AND MOCVD (metal-organic chemical vapor deposition) dual-process. Thompson Lin (CEO): dual-process capability is "unique in our industry" (AAOI 10-K FY2025; over-claim mode rhetorical attribution).

- **Layer 4/5 straddling tension preserved (Session 15 codification):** AAOI revenue ~100% pluggable transceiver assembly (Layer 5); in-house MBE+MOCVD at Sugar Land (Layer 4 capability) is vertically integrated into modules rather than sold as standalone Layer 4 product. Tier upgrade not warranted absent merchant laser business emergence.
- **Capacity ramp:** Tripling InP laser production by mid-2027 (AAOI Q4 FY2025 call); external laser suppliers quoting "1+ year lead times" framing the rationale for vertical integration acceleration (AAOI Q4 FY2025 call)
- **Sugar Land manufacturing footprint:** ~4% of AAOI manufacturing footprint by location (AAOI 10-K FY2025); subassemblies + laser chip fabrication; structurally distinct from Ningbo China assembly footprint (57.5% of footprint)
- **CPO ELS opportunity asymmetry:** AAOI in-house InP/GaAs laser fabrication creates ELS architecture supply opportunity per [[cpo-integration]] AAOI per-company integration positioning section; module business displacement risk + ELS laser opportunity preserved as asymmetric exposure

### Wafer-size transition mechanics — 4-inch → 6-inch InP

The InP wafer-size transition is a cross-tier mechanism interlocking substrate availability with epitaxial process maturity:

- **4-inch InP:** JX Advanced Metals scale; AXTI baseline scale (most output today)
- **3-inch InP:** Industry-standard device-fabrication size per silicon-photonics-primer.md (LITE position; Sumitomo + IQE substrate availability)
- **6-inch InP:** Sumitomo, AXT, IQE substrate-level capability disclosed; COHR is the only known vault company with multi-site six-inch device-fabrication position

The wafer-size transition affects both substrate-tier AND epitaxial-tier mechanics: substrate-tier supply concentrates at suppliers with six-inch-capable crystal growth; epitaxial-tier device-fabrication-process maturity gates whether substrate scaling translates into device output. COHR's "**>4x chips at <50% cost**" framing (per Q2 FY2026 call) operationalizes the wafer-size transition's cost economics — but the ~8x cost-per-chip improvement requires both substrate-tier scaling AND epi-process qualification at six-inch.

**Industry-baseline preservation (Session 5 silicon-photonics-primer.md cross-validation).** "Six-inch monopoly" framing is not accurate at substrate level. Substrate-level competitors (Sumitomo, AXT, IQE) all have six-inch InP capability. COHR's defensible position is multi-site device-fabrication advantage at six-inch (epitaxial process + downstream qualification) — distinct from substrate-level scarcity claim.

## Geopolitical dimension — substrate + equipment tiers

The InP supply chain exhibits a geopolitical mirror structure spanning both substrate-tier (Chokepoint 3) AND equipment-tier (Chokepoint 4 sub-layer) — compounding vulnerability.

**China side — substrate-tier ([[AXTI]]).** 100% of AXTI's InP manufacturing is located in Beijing, China. On February 4, 2025, China added InP substrates to its export control list, requiring government permits for all exports. As of February 2026, AXTI had received permits for Europe, Japan, UK, and Canada but had received first permit denials for US-destined shipments (AXTI Q4 FY2025 call). AXTI is one of two or three global InP suppliers; its entire output is now gated by Chinese government approval.

**US side — equipment-tier ([[VECO]]).** VECO manufactures the MOCVD equipment (Lumina+) used to grow epitaxial layers on InP substrates. 99.4% of VECO's PP&E is in the United States (VECO 10-K FY2025). US semiconductor equipment export controls restrict VECO's ability to sell advanced MOCVD tools to Chinese customers, including potentially to AXTI's Chinese operations for capacity expansion.

**The fracture risk — both controls simultaneously tightening.** The mirror structure creates a scenario where:
- Chinese export controls could restrict InP substrate supply to Western laser makers ([[LITE]], [[COHR]], [[AVGO]])
- US export controls could restrict MOCVD equipment supply to the largest Western-headquartered InP substrate maker ([[AXTI]], operating in China)
- Both controls simultaneously tightening would leave only Japanese suppliers (Sumitomo, JX Nippon) as unconstrained InP substrate sources for Western customers, using potentially non-US MOCVD equipment (Aixtron, Germany)

This mirror structure makes InP supply uniquely vulnerable to geopolitical escalation. Unlike [[TSMC-CoWoS]], where the chokepoint is concentrated in a single jurisdiction (Taiwan), the InP supply chokepoint spans two adversarial jurisdictions with independently operating control regimes.

**Western device-fabrication-tier alternative path.** AAOI Sugar Land TX MBE+MOCVD dual-process represents the clearest US-domiciled vertical integration alternative for laser-device output independent of China substrate supply (AAOI Q4 FY2025 call); COHR Sherman + Järfälla + Zürich multi-site device-fabrication represents the European-distributed alternative. Both depend on non-China substrate sources (Sumitomo + JX Nippon Japan; potential IQE substrate access).

## Cross-tier interdependencies + vertical integration moat dynamics

The substrate-tier + epitaxial-tier chokepoints exhibit asymmetric dependency mechanics:

**Vertical integration moat structure.** Companies with in-house epitaxial capability (COHR substrate→epi→device; AAOI Sugar Land MBE+MOCVD dual-process) preserve more value through wafer-size transitions than companies dependent on merchant epitaxial process. LITE three-inch industry-standard positioning relies on broader substrate ecosystem (Sumitomo + JX Nippon + AXT + IQE).

**Substrate scarcity vs epi-yield decoupling.** At pluggable-transceiver volumes today, substrate availability is the binding constraint per AXTI Q4 FY2025 call ($60M+ backlog; capacity-doubling expansion). At CPO-volume future per AXTI's "late 2027 and beyond" framing, substrate-tier amplification compounds with epitaxial-process scaling — both tiers tighten simultaneously. Epi-yield matters more at higher volume because qualification delays at six-inch device-fabrication compound substrate-scaling costs.

**Supply-secured-via-equity asymmetry (NVDA $2B March 2026).** NVDA $2B equity-plus-purchase modality (LITE + COHR per Session 22 [[NVDA-platform-integration]] codification) operationalizes vertical securing of laser supply chain at Layer 4 device-fabrication tier. Capital-offset-for-supply-assurance framing distinguishes this modality from acquisition (Mellanox precedent) or licensing (Groq precedent). Three Layer 4 InP device-fabrication positions exhibit different equity-related exposure: COHR + LITE NVDA-aligned; AAOI not NVDA-aligned (vertical integration via in-house Sugar Land MBE+MOCVD instead).

**ELS architecture downstream linkage.** External Laser Source (ELS) architecture preserves Layer 4 component supplier value through CPO transition (cross-reference [[cpo-integration]] CPO integration mechanics + value chain shift dynamics sections). UHP CW laser supply for ELS architecture depends mechanically on InP epitaxial capacity at six-inch (COHR) + three-inch (LITE) + Sugar Land (AAOI) — InP supply chain feeds CPO transition value capture.

## Forward-looking uncertainty

### Substrate-tier (Chokepoint 3) — what would confirm or weaken

**Confirm signals:**
- Sumitomo or JX Nippon sources indicating similar backlog growth and capacity constraints (would confirm industry-wide tightness, not AXTI-specific)
- Downstream customers ([[LITE]], [[COHR]], [[AAOI]]) citing InP substrate availability as a supply constraint in their filings or calls
- Chinese export permit denials extending beyond US to other Western destinations (would confirm escalating geopolitical chokepoint)
- InP substrate lead times lengthening as reported by downstream customers or industry sources

**Weaken signals:**
- Sumitomo or JX Nippon having ample spare capacity that AXTI's backlog growth does not reflect (would suggest AXTI-specific market share gain, not structural tightness)
- Downstream customers qualifying alternative substrate technologies (e.g., InP-on-silicon, GaAs-based alternatives for specific wavelengths) that reduce InP dependency
- Chinese export controls applying broadly but with routine permit approvals, indicating regulatory compliance burden rather than supply restriction
- AXTI's backlog growth driven by pre-ordering and double-ordering rather than genuine end-demand (would deflate the demand signal)

### Epitaxial-tier (Chokepoint 4) — what would confirm or weaken

**Confirm signals:**
- VECO Compound Semiconductor segment growth materially above guided $80M FY2026 (would indicate MOCVD tool demand acceleration tied to epitaxial-tier capacity ramp)
- COHR six-inch InP capacity-doubling milestone delivered on schedule by end calendar 2026 + further capacity-expansion announcements (would confirm device-fabrication-tier scaling viability)
- LITE 40% capacity-expansion milestone delivered + additional expansion announcements (would confirm three-inch industry-standard demand absorption)
- AAOI tripling InP laser production by mid-2027 milestone delivered + merchant laser business emergence (would confirm vertical integration alternative viability + potential Layer 4 tier-upgrade per Session 15 pre-registered trigger)
- Six-inch InP epitaxial-process disclosure from a second vault company beyond COHR (would confirm wafer-size transition broadening across multiple device fabricators)

**Weaken signals:**
- VECO Compound Semiconductor segment further decline below FY2025 $60M baseline (would indicate epitaxial equipment-tier softening)
- COHR six-inch capacity-doubling milestone delayed or scaled-back (would weaken device-fabrication-tier moat framing)
- Industry-wide qualification of InP-on-silicon or alternative substrate technologies displacing InP epitaxial processes
- Aixtron market-share gain vs VECO at InP-relevant installations (would weaken VECO equipment-tier positioning per [[VECO]] Open question pre-registration)
- AAOI in-house InP laser business under-execution + reliance on merchant laser supply emerging (would weaken vertical integration alternative path)

### Cross-tier (substrate + epitaxial) integrated uncertainty

- Whether wafer-size transition (4-inch → 6-inch) accelerates faster at substrate-tier or epitaxial-tier — substrate scaling without epi-process qualification creates capacity-utilization gap; epi-process maturity at six-inch without substrate scaling creates input-constraint gap
- Whether the geopolitical mirror structure escalates symmetrically (both control regimes tightening) or asymmetrically (one regime tightens; counter-regime relaxes)
- Whether NVDA $2B March 2026 equity-plus-purchase modality propagates beyond LITE + COHR to AXTI (substrate-tier vertical securing) or to non-vault InP suppliers (Sumitomo / JX Nippon counterparty exposure)

## Cross-references

- [[chokepoint-investability-priorities]] Chokepoint 3 (InP substrate supply) + Chokepoint 4 (InP epitaxial capacity) — Tier 3-anchored vault-canonical reference; Session 24 Integration 2 two-layer reconciliation framework (indium feedstock layer / JX Advanced Metals dominant; InP wafer production layer / AXTI significant)
- [[datacenter-photonics-supply-chain]] Section 2.9 (Upstream materials and substrates) — places InP layer within cross-cutting supply-chain map; surfaces JX Advanced Metals (~78% global InP substrate share per architecture primer) as Tier A future-ingest candidate
- [[datacenter-laser-supply]] — adjacent Chokepoint 1 (laser/EML/III-V devices); device-tier downstream of substrate + epitaxial supply
- [[advanced-optical-packaging]] — adjacent Chokepoint 5; assembly-tier downstream of laser device fabrication
- [[cpo-integration]] — adjacent Chokepoint 10; ELS architecture preservation of Layer 4 component-tier value through CPO transition depends on UHP CW laser supply per InP epitaxial capacity
- [[CPO-platform-battle]] — substrate-tier demand amplifier dimension at CPO transition (AXTI "yet another inflection point" framing)
- [[NVDA-platform-integration]] — six-modality framework; equity-plus-purchase modality (LITE + COHR $2B March 2026) operationalizes vertical securing of Layer 4 device-fabrication tier
- [[TSMC-CoWoS]] — geopolitical chokepoint comparison; InP supply spans two adversarial jurisdictions vs CoWoS single-jurisdiction concentration
- [[AXTI]] / [[VECO]] / [[COHR]] / [[LITE]] / [[AAOI]] / [[AVGO]] — vault company anchors

## Source attribution

**Tier 3 framework reference:** `raw/research/photonics-chokepoint-table.md` Chokepoint 3 (InP substrate supply; Rank 3) + Chokepoint 4 (InP epitaxial capacity; Rank 4) unified treatment per Option C bifurcation handling (single page covering two adjacent Tier 3 ranks per [[cpo-integration]] Session 32 Option C precedent). Vic-team-authored canonical living document.

**Primary-source vault company anchors (5 vantages):**

- **[[AXTI]]** — Session 13 paired ingest with [[VECO]] baseline (10-K FY2025 Tier 1 + 10-Q Q3 FY2025 Tier 1 + Q4 FY2025 earnings call Tier 2). Substrate-tier core vantage; supply concentration dispute; February 2025 Chinese export controls; capacity-doubling brownfield expansion.
- **[[VECO]]** — Session 13 paired ingest with [[AXTI]] baseline (10-K FY2025 Tier 1). Equipment-tier vantage; Lumina+ MOCVD; Aixtron primary competitor; Compound Semiconductor segment $60M FY2025 → $80M FY2026 guidance.
- **[[COHR]]** — Session 5 ingest baseline + Session 31 [[advanced-optical-packaging]] synthesis. Device-fabrication-tier vantage; six-inch InP at Sherman + Järfälla + Zürich; quadrupled wafer starts Sep→Dec; capacity-doubling by end calendar 2026; Anderson ">4x chips at <50% cost vs three-inch" framing.
- **[[LITE]]** — Session 4 + Session 5 cross-validation + Session 31 [[advanced-optical-packaging]] synthesis. Device-fabrication-tier vantage; three-inch InP industry-standard; 40% capacity expansion; NVDA $2B equity-plus-purchase March 2026; 400mW UHP CW laser positioning.
- **[[AAOI]]** — Session 7 ingest + Session 15 Layer 4/5 straddling codification + Session 31 [[advanced-optical-packaging]] synthesis. Device-fabrication-tier vantage; Sugar Land TX MBE + MOCVD dual-process; tripling InP laser production by mid-2027; "unique in our industry" Thompson Lin rhetorical (over-claim mode).

**Cross-reference vault chokepoint pages:** [[datacenter-laser-supply]] (Session 4) + [[advanced-optical-packaging]] (Session 31) + [[cpo-integration]] (Session 32) + [[optical-dsp-phy-supply]] (Session 30) + [[TSMC-CoWoS]] + [[wafer-level-siph-test]] (Session 25 provisional).

## Source audit notes

### Multi-vantage-point synthesis from existing vault canonical content

Session 33 expansion is multi-source synthesis from existing vault canonical content (5 vault primary-source vantages spanning substrate-tier + equipment-tier + device-fabrication-tier). No new primary-source ingest. Page promoted from provisional (Session 13 single-source AXTI baseline) to canonical multi-source-synthesis chokepoint page; provisional disclaimer replaced with substrate-tier vs epitaxial-tier scope discipline boundary statement.

### Theme-page-overlap-analogous discipline applied within single page (Option C bifurcation handling)

Per Session 32 [[cpo-integration]] Option C precedent: this page covers two adjacent Tier 3 ranks (Chokepoint 3 + Chokepoint 4) within unified InP supply chain framework via internal subsection bifurcation. Subsection structure preserves Tier 3 framework's structural distinction (substrate-tier vs epitaxial-tier as separately-ranked chokepoints per [[chokepoint-investability-priorities]] separate sections) while consolidating shared mechanics (geopolitical mirror structure spanning both tiers; cross-tier interdependencies; wafer-size transition mechanics interlocking substrate + epi). Page-top scope discipline boundary statement explicitly distinguishes covered scope vs other chokepoint page scope ([[datacenter-laser-supply]] Chokepoint 1 device-tier; [[advanced-optical-packaging]] Chokepoint 5 packaging-tier; [[optical-dsp-phy-supply]] Chokepoint 2 DSP/PHY-tier; [[cpo-integration]] Chokepoint 10 CPO architectural transition).

### A6 v8 verification — Phase 0 PASS on product/program names + chokepoint numbering

Per CLAUDE.md v8 A6 application discipline: 8 pattern types verified PASS at Phase 0. (g)/(g)' subtype instance count unchanged at 6 accumulated through Session 32. Session 33 expansion verified canonical product names (VECO Lumina+; AXTI Beijing; COHR Sherman + Järfälla + Zürich; LITE three-inch; AAOI Sugar Land MBE+MOCVD); canonical Tier 3 Rank numbering (Chokepoint 3 + Chokepoint 4 per priorities theme page; not pre-v2 row indexing per Session 32 (g)' lesson). **Zero falsifications surfaced.**

**Pattern observation reinforcement.** Session 33 follows refined kickoff-drafting-discipline observation: detail level is not the failure mode; canonical anchoring is the success mode. Vic's prior-session direct alignment on canonical content (via prior exchanges confirming product/program details + chokepoint numbering reference + Option C bifurcation handling decision) anchors the expansion on vault canonical content; zero (g)/(g)' instances regardless of detail level.

### A1 three-mode framing applied throughout

- *Anderson COHR rhetorical claims* ("six-inch monopoly" framing per Q2 FY2026 call) — refined per Session 5 silicon-photonics-primer.md cross-validation; substrate-level monopoly framing not accurate; device-fabrication position confirmed (over-claim mode → reciprocal-confirmation mode after refinement)
- *Sumino LITE rhetorical claims* ("400mW UHP not something that many people can do") — over-claim mode
- *Thompson Lin AAOI rhetorical claims* ("unique in our industry" dual-process MBE+MOCVD; "more than 95% of laser will be AI laser by end of year") — over-claim mode
- *Young AXTI rhetorical claims* ("Today there are two InP substrate suppliers" call vs "three primary suppliers" filing) — Tier 1/Tier 2 framing gap (risk-framing sub-pattern); preserved as canonical Session 13 observation
- *Non-vault references* (Sumitomo, JX Nippon, Aixtron, AXT, IQE, JX Advanced Metals) — counterparty-attribution-only mode pending future primary-source verification

### Honest-verdict discipline applied throughout

Three Layer 4 InP wafer-size positions preserved without forced winner attribution: COHR six-inch device-fabrication advantage; LITE three-inch industry-standard manufacturing; AAOI Sugar Land MBE+MOCVD dual-process. Vertical integration moat dynamics preserved as conditional (depends on wafer-size transition pacing + ELS architecture viability + NVDA equity modality propagation). Substrate-tier supply concentration dispute (2 vs 3 suppliers) preserved per Tier 1/Tier 2 framing gap convention; no silent adjudication. Geopolitical mirror structure preserved as conditional risk (both control regimes simultaneously tightening) without forced escalation prediction.

## Change log

- **2026-04-23:** Page created. Session 13 paired ingest ([[AXTI]] + [[VECO]]). Provisional chokepoint page — sourced primarily from AXTI filings and call, with VECO context for equipment tier. Geopolitical mirror structure documented as primary structural risk.
- **2026-04-27:** Session 19 cross-reference. Added Cross-references section linking [[datacenter-photonics-supply-chain]].
- **2026-04-27 (Session 25):** Added Cross-reference to [[chokepoint-investability-priorities]] new theme page (A2 first canonical application). Page content unchanged.
- **2026-04-30 (Session 33 multi-source chokepoint synthesis — Option C bifurcation handling; provisional → canonical promotion; closes Tier 3 framework Chokepoint 3 + Chokepoint 4 unified coverage gap):** Page promoted from provisional (Session 13 single-source AXTI baseline) to canonical multi-source-synthesis chokepoint page via four additional vault primary-source vantages added at Chokepoint 4 (InP epitaxial capacity): VECO equipment-tier (Lumina+ MOCVD; Aixtron competitor; Compound Semi $60M FY2025 → $80M FY2026 guidance) + COHR device-fabrication-tier (six-inch InP at Sherman + Järfälla + Zürich; quadrupled wafer starts; doubling capacity by end calendar 2026; ">4x chips at <50% cost" Anderson) + LITE device-fabrication-tier (three-inch InP industry-standard; 40% capacity expansion; NVDA $2B equity-plus-purchase March 2026) + AAOI device-fabrication-tier (Sugar Land MBE+MOCVD dual-process; tripling InP laser production by mid-2027; Layer 4/5 straddling preserved per Session 15 codification). **Fifth canonical multi-source-synthesis chokepoint page in vault history** (after [[InP-supply]] originating Session 13, [[optical-dsp-phy-supply]] Session 30, [[advanced-optical-packaging]] Session 31, [[cpo-integration]] Session 32). **Second chokepoint page applying Option C bifurcation handling** (single page covers two adjacent Tier 3 ranks via internal subsection structure; mirrors Session 32 Scale-up + Scale-out CPO precedent). Page title expanded from "InP substrate supply" → "InP supply (substrate + epitaxial capacity)"; filename preserved per Vic Stop 1 decision (avoids wikilink-cascade across 6+ vault pages referencing [[InP-supply]]). Provisional disclaimer replaced with substrate-tier vs epitaxial-tier scope discipline boundary statement (Session 32 theme-page-overlap discipline pattern adapted within-page). Section structure: Substrate-tier (Chokepoint 3) preserves Session 13 content (Supply concentration + Demand drivers + capacity dynamics); Epitaxial-tier (Chokepoint 4) adds Equipment-tier sub-layer + Device-fabrication-tier sub-layer + Wafer-size transition mechanics; Geopolitical dimension preserved + extended (substrate + equipment tiers); Cross-tier interdependencies + vertical integration moat dynamics (NEW); Forward-looking uncertainty rewritten with substrate-tier + epitaxial-tier + cross-tier subsections. Per A2 fifth canonical application + structural requirements: Tier 3 source attribution at page-top + per-section + Source attribution + Source audit notes; counterparty-attribution-only annotation for non-vault company references (Sumitomo Electric, JX Nippon Mining & Metals, Aixtron Germany, AXT, IQE, JX Advanced Metals). Per Session 32 (g)' lesson: vault canonical Tier 3 Rank numbering preserved (Chokepoint 3 + Chokepoint 4; not pre-v2 row indexing). A6 v8 (g)/(g)' subtype instance count unchanged at 6 accumulated through Session 32 — **zero new falsifications**. Honest-verdict discipline applied to: three Layer 4 InP wafer-size positions (no forced winner); Tier 1/Tier 2 framing gap (2 vs 3 suppliers dispute) preserved without silent adjudication; geopolitical mirror structure preserved as conditional risk; NVDA $2B equity-plus-purchase modality propagation framed as forward-looking uncertainty. Forward-wikilink discipline preserved: 19-session vault wikilink-clean streak post-Session 33 (extended from 18 post-Session 32). Frontmatter `tickers` unchanged ([AXTI, LITE, COHR, AAOI, AVGO, VECO] already complete from Session 13); `last_updated` 2026-04-27 → 2026-04-30.
- **2026-05-29 (Session 105 — [[AXTI]] Q1 FY2026 refresh propagation):** Added substrate-tier update subsection reflecting AXTI Q1 FY2026 (10-Q + call): backlog $60M+ → $100M+; profitability inflection (Q2 guided GAAP + non-GAAP profitable); capacity roadmap escalated and funded ($35M/qtr end-2026 → $65-70M/qtr end-2027; April 2026 $632.5M raise); new China-demand leg (~30%→40% of global InP demand AXTI sees; in-China shipments permit-exempt); export-control gate Section 4.3 update (US permits "still pending," reframed from prior "first denials"); 6-inch advancing. Supply-concentration "two vs three suppliers" framing gap preserved as prior-instance, not re-fired (Q1 call did not repeat the "two suppliers" claim). `last_updated` 2026-04-30 → 2026-05-29.
