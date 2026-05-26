# 800VHDC Power Semiconductors for AI Data Centers: A Decision-Ready Primer

## TL;DR
- **What it is**: 800VHDC (800-volt high-voltage direct current) is a redesign of how electricity is delivered inside an AI data center. Instead of converting AC voltage many times before it reaches the GPU, a single conversion at the building edge produces an 800-volt DC bus that is piped directly to the racks, where compact silicon-carbide (SiC) and gallium-nitride (GaN) power semiconductors step it down to the sub-1-volt rails the GPUs actually need. NVIDIA is the explicit standard-setter, with full production targeted for 2027 alongside its Kyber/Rubin Ultra racks.
- **Why it matters now**: Per-rack power has gone from ~40 kW (Hopper H100), to 120–132 kW (GB200 NVL72), to ~190 kW (Vera Rubin NVL144) and 600 kW–1 MW for Rubin Ultra / Kyber. At 48 V, a 1 MW rack would need ~20,800 amps and ~200 kg of copper busbar per rack — physically infeasible. At 800 V the same rack draws ~1,250 A and saves about 45% of the copper, while end-to-end efficiency rises ~5 percentage points and TCO drops up to 30% (NVIDIA figures).
- **Is the power semi the bottleneck?**: No — power semiconductors are a *real but transient* constraint (12–18 months of tight SiC/GaN supply for 800V/1200V/1700V classes), but they are not the binding bottleneck for AI data center growth. The harder bottlenecks are **grid interconnect timelines** (multi-year queues), **large power transformer lead times** (128 weeks / up to 4–5 years), and **skilled labor + permitting**. Fourteen named silicon vendors are already racing to supply NVIDIA's 800VDC architecture; competition will resolve the chip-level supply question well before transformers and substations catch up.

---

## Key Findings

1. **NVIDIA has effectively standardized 800VDC.** At OCP Global Summit 2025 (October 2025) NVIDIA published "800 VDC Architecture for Next-Generation AI Infrastructure" and named 14 silicon partners — Analog Devices, AOS, EPC, Infineon, Innoscience, MPS, Navitas, onsemi, Power Integrations, Renesas, Richtek, Rohm, STMicroelectronics, Texas Instruments — plus power-system partners (Delta, Flex, GE Vernova, Lead Wealth, LITEON, Megmeet, BizLink) and facility-power partners (ABB, Eaton, GE Vernova, Heron Power, Hitachi Energy, Mitsubishi Electric, Schneider Electric, Siemens, Vertiv). The OCP "Mt. Diablo" (Diablo 400) specification co-authored by Microsoft, Meta and Google complements this with a ±400 VDC sidecar architecture for 100 kW–1 MW racks; Diablo can output either ±400 VDC or 800 VDC, so the two camps converge at the busbar.
2. **The physics is unambiguous.** Distribution losses scale with current squared (I²R). A 1 MW rack at 48 V needs ~20,833 A; at 800 V it needs ~1,250 A, requiring roughly 45% less copper. NVIDIA quantifies the benefits as "up to 5% improvement in end-to-end power efficiency," "maintenance costs reduced by up to 70%," and "total cost of ownership cut by up to 30%."
3. **Power-per-rack roadmap (verified):** H100/Hopper ~40 kW → GB200 NVL72 ~120–132 kW (HPE/Vertiv data sheets confirm 132 kW: 115 kW liquid-cooled + 17 kW air) → Vera Rubin NVL144 ~190 kW (Vera Rubin NVL144 CPX ~370 kW) → Rubin Ultra in Kyber 600 kW per rack, scaling to 1 MW+. Hyperscalers (Microsoft, Meta, Google) project 500+ kW per rack by 2030 in their Mt. Diablo work.
4. **800V semiconductor content per rack is rising sharply.** onsemi states that its **power-semi content per 1 MW AI rack has doubled from $50,000 to $100,000**; Morgan Stanley estimates that the value of power solutions inside AI racks will grow more than 10x by 2027. According to Yole Group's Power GaN 2025 report (October 2025), data centers and telecom together are expected to generate more than $380 million in GaN revenues by 2030, with the data center segment growing at ~53% CAGR.
5. **Wide bandgap (SiC/GaN) is mandatory above 200 kW racks.** Silicon MOSFETs simply cannot deliver the switching speed and efficiency needed for an 800-V LLC resonant converter operating at 650–850 kHz. Power Integrations has volume 1250 V and 1700 V GaN HEMTs; STMicroelectronics demonstrated 6 kW/12 kW/20 kW 800V-to-low-voltage delivery boards using 700 V GaN with peak efficiency of 97.5%; Navitas integrated GaNFast and GeneSiC SiC across the full chain.
6. **The bigger bottlenecks are upstream, not in the chip.** Wood Mackenzie's Q2 2025 survey put US large power transformer lead times at **128 weeks for standard power transformers and 144 weeks for generator step-up units, with some orders extending to 4 years**; prices are up 77% since 2019. The IEA notes that data center power density rose 11x between 2020 and 2025 and will quadruple again by 2027 — far faster than grid equipment can be built. Sightline Climate reports that of 12 GW of announced 2026 US data center capacity, only ~5 GW is actually under construction, with HV transformers, switchgear and grid-tie batteries as the gating items.

---

## Details

### Question 1 — What are power semiconductors for AI data centers?

**The simple definition.** A *logic chip* (CPU, GPU, TPU) computes — it does math on bits. A *power semiconductor* is a different kind of chip that doesn't compute at all; it acts as an electronic valve that switches electricity on and off thousands or millions of times per second, very efficiently, so engineers can change voltage and current levels with minimal heat loss. Think of a logic chip as the brain and a power semiconductor as the heart, lungs and circulatory system: without continuous, well-shaped flow of "blood" (electrons at the right voltage and current), the brain can't think.

**The main families:**
- **Silicon MOSFETs** — the workhorse since the 1970s. Cheap, mature, but lossy above ~600 V and at high frequencies. Still dominant in low-voltage (≤100 V) point-of-load converters.
- **IGBTs (Insulated Gate Bipolar Transistors)** — silicon devices designed for high current at medium voltages (600–6500 V). Used in EV traction inverters, wind turbines, and traditional UPS systems. Slower switching than MOSFETs; being displaced by SiC at >800 V.
- **Power diodes** — one-way "check valves." Used in rectifiers (AC→DC) and freewheeling roles. Fast-recovery and Schottky variants reduce switching losses.
- **Wide bandgap (WBG) semiconductors — SiC and GaN.** A material's *bandgap* is the energy needed to free an electron; silicon's is 1.12 eV, SiC is 2.26 eV, GaN is 3.4 eV. A wider bandgap means the device can hold off a higher voltage in a thinner layer, switch faster, and run hotter, with lower resistive losses. Practical rule of thumb:
  - **Silicon**: up to ~600 V and ~100 kHz — still the cheapest choice for low-voltage (12 V, 48 V) point-of-load.
  - **GaN**: today best from ~100 V to 1700 V, switching at 500 kHz–MHz, ideal for the 800 V → 50 V or 800 V → 12 V LLC resonant converters inside the rack. Power Integrations has the only volume 1700 V GaN parts; Navitas, EPC, Infineon, Innoscience and STMicro all offer 650 V GaN.
  - **SiC**: today best from 650 V to 3.3 kV (and 6.5 kV–15 kV for solid-state transformer roles), used for the front-end AC-to-DC rectifier and the MV→800 V solid-state transformer (SST).

**Where power semis sit in an AI data center power chain (grid → GPU):**
1. **Utility medium voltage** (e.g. 13.8 kV AC) enters the campus through a substation.
2. **Substation transformer or solid-state transformer (SST)** steps it down. In the legacy path: 13.8 kV → 480/415 V AC inside the building, then AC-to-DC rectifier, then UPS, then PDU, then 54 V DC at the rack. In NVIDIA's 800VDC path: 13.8 kV → 800 V DC in one stage using an SST built around SiC devices (Delta claims 98.5% efficiency, SolarEdge/Infineon target 99%).
3. **AC-DC rectifiers (PSUs)** in the legacy path do the heavy lifting of AC→DC conversion. Infineon's 8 kW reference PSU uses SiC for the front-end totem-pole PFC and GaN for the secondary-side LLC, hitting 97.4% efficiency.
4. **DC distribution busbar**: today 48 V/54 V; future 400 V or 800 V. The busbar is essentially a giant copper rail running vertically up the rack.
5. **Rack-level DC-DC converters (intermediate bus converters or "power shelves").** In a GB200 NVL72 today, six 33-kW power shelves bolt into the rack.
6. **Board-level DC-DC converters** drop 48 V → 12 V → sub-1 V.
7. **Point-of-load (PoL) converters** sit right next to the GPU and deliver 0.6–0.8 V at 2,000–5,000+ amps. ADI, Infineon, Vicor, MPS, Renesas and uPI are the key suppliers.
8. **Vertical Power Delivery (VPD)** is the bleeding edge: place the PoL *underneath* the GPU package instead of beside it, so current flows up vertically through the PCB rather than sideways. Vicor (Factorized Power Architecture), Empower Semiconductor (Crescendo), Infineon, ADI, TDK and Flex all sell VPD modules. The motivation: at 2,000+ A and 0.65 V, even 1 milli-ohm of trace resistance dissipates a kilowatt of waste heat.

**Key concepts the reader should hold:**
- *Efficiency*: at 1 MW per rack, every 1% saved is 10 kW that never has to be cooled.
- *Current-voltage trade-off*: power = volts × amps. Raise the voltage and you can carry the same power with less current, less copper, less heat (I²R).
- *Switching frequency*: faster switching = smaller capacitors and inductors = denser power supplies. WBG enables 5–10x higher frequency than silicon.
- *Power density*: STMicro's 12-kW PSU board now hits **138 W/in³**.
- *Thermal dissipation*: every watt of conversion loss must be removed by liquid or air cooling, so power semi efficiency directly determines cooling capex/opex.

**Bill of materials in a single GB200 NVL72 rack (best public estimates):** 18 compute trays × 2 Bianca boards (each with 1 Grace CPU + 2 Blackwell GPUs and a 16-to-24-phase VRM) + 9 NVSwitch trays + 6 power shelves. Each GPU and CPU socket draws ~675 A through dedicated cables. Triangulating from Infineon's 12-kW PSU reference design (30–50 wide-bandgap switches per shelf) and Bianca board VRM counts, a single NVL72 plausibly contains **several thousand discrete power FETs, controllers and PoL modules**, of which hundreds are SiC/GaN devices in the PSUs alone. **onsemi pegs the power-semi BOM dollar value at roughly $50,000 per 1 MW AI rack today, rising to $100,000 in next-generation 1 MW racks** — i.e. roughly $5,000–$13,000 of power semiconductors per 132-kW GB200 rack on a kW-pro-rata basis. Morgan Stanley separately projects that the *power solution* dollar content of AI racks will grow more than 10x by 2027.

### Question 2 — What is 800VHDC and why does it matter for AI?

**Definition in one sentence.** 800VHDC is direct-current power distribution at a nominal 800 V (either monopolar 0–800 V à la NVIDIA, or bipolar ±400 V à la OCP Mt. Diablo — both produce 800 V between conductors) running from a single AC-to-DC conversion at the facility edge all the way to the rack, where on-board converters step it down to whatever the chips need.

**Evolution of data center power architecture:**
- **1990s–2010s "Traditional"**: 480 V AC distributed across the data hall; each rack's PSU converts AC → 12 V DC. Multiple lossy conversions; end-to-end efficiency ~83% in legacy designs.
- **2016–2024 "48 V era"**: Google led the industry to 48 V DC inside the rack (Open Rack v2.2). 48 V cut copper use roughly 4x vs 12 V and enabled 10–100 kW racks.
- **2025–2026 "Sidecar transitional"**: ±400 V DC sidecars (Mt. Diablo) supply AI compute racks of 100–500 kW; ecosystem prototypes from Eaton, Schneider, Vertiv, Delta showcased at OCP 2025.
- **2027+ "Full 800VDC"**: Kyber/Rubin Ultra racks at 600 kW–1 MW are 800-V-native; medium-voltage AC is converted only once via SST.

**Why now? Concrete physics.** With per-rack power rising from 132 kW (GB200) to 600 kW (Rubin Ultra) to 1 MW+ (Kyber/Rubin Ultra Ultra), the constraints become:
- **Copper**: At 48 V, 1 MW = 20,833 A → ~200 kg of copper busbar per rack. A 1-GW data center with 1,000 such racks would need ~200,000 kg of copper just in busbar — both expensive and physically impossible to fit. At 800 V the same rack draws ~1,250 A and uses ~45% less copper.
- **Space**: NVIDIA notes that retaining 54 VDC into a 1-MW rack would consume **up to 64 U of rack space for power shelves alone**, leaving no room for compute. The 800 V architecture moves the power-shelf bulk into a separate sidecar (Schneider, Delta, Vertiv designs) or eliminates it entirely with a centralized SST.
- **Conversion stages**: Traditional AC distribution has 4–5 stages (MV→480 V→UPS→PDU→rack PSU→PoL). 800VDC compresses this to **2 stages** (MV→800 V via SST; 800 V→sub-1 V via on-board converters). End-to-end efficiency rises from ~83% to >92%.

**NVIDIA's roadmap (publicly confirmed):**
- May 2025: NVIDIA's Mathias Blake publishes the technical blog "NVIDIA 800 VDC Architecture Will Power the Next Generation of AI Factories."
- October 2025 (OCP Global Summit): 14 silicon partners, 7 power-system component partners and 9 data center power partners announced. ABB, Eaton, Hitachi Energy, Schneider, Siemens, Vertiv all publish reference designs.
- 2026 H2: Vertiv ships full 800VDC product line; Vera Rubin NVL144 (~190 kW per rack on existing 415/480 VAC ± 400 VDC infrastructure).
- **2027: Full-scale 800VDC production coincident with Kyber/Rubin Ultra at 576 GPUs and 600 kW per rack.**

**Hyperscaler adoption.** Microsoft, Meta and Google co-authored the OCP Mt. Diablo (Diablo 400) spec at ±400 VDC. Foxconn's 40 MW Kaohsiung-1 data center in Taiwan is being built natively for 800 VDC. CoreWeave, Lambda, Nebius, Oracle Cloud Infrastructure and Together AI are publicly designing for 800-volt data centers. Microsoft notes the disaggregated power rack allows "up to 35% more AI accelerators per server rack."

**The OCP specifications.** Mt. Diablo v0.5.2 (May 2025) defines ±400 VDC distribution with ±410 VDC at no-load, 800 V across +/- rails, up to 1.1 MW per rack across three AC-input options (480/415/400 VAC) and standardizes connector and protection schemes. The newer OCP "Data Center Facility – Low-Voltage Direct Current Power Distribution" whitepaper v1.0 (Q1 2026) extends the envelope to ≤1500 VDC and evaluates "700V or 800V device compatible, 1400V or 1500V compatible" voltage classes. Practical engineering rule (AOS, ST): a 10% margin over 800 V plus turn-off spikes pushes designers to **1200 V SiC** or **1250–1700 V GaN** for the primary-side switches.

**Why DC, not AC?** A modern data hall has on-site batteries (BBUs), solar arrays and possibly fuel cells — all of which are DC-native. Every AC-DC-AC conversion costs 1–3% in losses and adds failure points. DC distribution removes those stages and makes battery integration trivially clean. The downside: DC arcs do not self-extinguish at zero crossings the way AC arcs do, so 800 V DC requires new fuses, breakers (often solid-state) and grounding schemes — and a workforce trained on HVDC safety.

**Automotive precedent.** The Porsche Taycan (2019) was the first mass-production 800-V EV, with a Delphi-built SiC inverter. Hyundai E-GMP, Kia EV6, Audi e-tron GT (PPE/J1 platforms), Lucid Air (900+ V), BYD and Xiaomi SU7 followed. By 2025–2026 every premium 800-V EV uses SiC inverters. **Google has explicitly said it is leveraging the EV-derived 400 V/800 V supply chain (drivers, connectors, SiC modules) to accelerate data center deployment** — the data center industry inherits a manufacturing curve that automotive has already paid to develop.

### Question 3 — Are 800VHDC power semiconductors a key bottleneck for AI data center power supply?

**Short answer: No, power semiconductors are not the binding bottleneck. They are a 12–18-month tightness issue in a market with 14 competing suppliers and rapid capacity additions, sitting downstream of much harder constraints.**

**Ranking of bottlenecks for AI data center power supply (highest severity first):**

| # | Bottleneck | Severity | Timeline | Evidence |
|---|------------|----------|----------|----------|
| 1 | **Utility power / grid interconnect** | Severe | Multi-year, structural | Bloom Energy 2026 Data Center Power Report: "the biggest obstacle is no longer capital, land, or connectivity — it's electricity." Sightline Climate: of 12 GW announced 2026 US capacity only ~5 GW is under construction. |
| 2 | **Large power transformers** | Severe | 2.5–5 years | Wood Mac Q2 2025: 128 weeks standard power transformers, 144 weeks generator step-ups, some up to 4 years. Prices up 77% since 2019. IEA: prices up to 2.6x pre-pandemic in real terms. |
| 3 | **Skilled labor + permitting** | High | Multi-year | EPC firms reordering project sequences; Dept of Energy October 2025 directive proposing federal jurisdiction over >20 MW loads to speed approvals. |
| 4 | **Switchgear and busbar manufacturing** | High | 1–2 years | Hyperscalers and EPCs report this as a sub-bottleneck of #2; ABB, Eaton, Schneider expanding capacity. |
| 5 | **On-site generation (gas turbines, SMRs)** | High | 2–7 years | Gas turbine backlogs through 2028+; per IEA's "Key Questions on Energy and AI" (April 2026), the pipeline of conditional offtake agreements between data center operators and SMR projects has grown from 25 GW at the end of 2024 to 45 GW as of April 2026; commercial SMRs are still 2030+. |
| 6 | **Cooling (liquid, immersion, CDUs)** | Moderate | 12–24 months | New 1–3 MW CDU designs (Google Deschutes) emerging; supply chain ramping. |
| 7 | **800V power semiconductors (SiC/GaN)** | **Moderate, transient** | 12–18 months | 14 named suppliers; aggressive 200 mm SiC capacity additions; GaN capacity ramping at GlobalFoundries, Innoscience, Power Integrations. |
| 8 | **Backup power (BBUs)** | Moderate | 12 months | Lithium supply manageable; integration complexity rising. |

**Why power semiconductors are not the binding constraint:**

*Supply side is racing forward.*
- **SiC**: Wolfspeed completed shutdown of its 150 mm Durham fab in early FY26 and consolidated all production into the 200 mm Mohawk Valley fab; it also demonstrated a 300 mm SiC wafer. Infineon's Module 3 of its Kulim, Malaysia 200 mm SiC fab — described by Infineon as "the world's largest 200-mm SiC fab" — is in ramp-up, targeting 30% global SiC share by 2030. STMicroelectronics' integrated Catania SiC Campus begins production in 2026, scaling to 15,000 wafers/week by 2033. The STMicro/San'an JV in China is in risk production with ~480,000 8-inch SiC wafers/year of capacity. McKinsey estimates total announced SiC wafer capacity will grow from ~2.8 million 150-mm-equivalent wafers in 2023 to ~10.9 million in 2027 — roughly 4x.
- **GaN**: Yole projects power GaN to grow at ~42% CAGR to ~$3 B by 2030, with data center/telecom combined contributing more than $380 million in GaN revenues by 2030 and data center the fastest-growing segment at ~53% CAGR. Power Integrations is in volume production with 1250 V and 1700 V PowiGaN (the only vendor above 1200 V GaN). onsemi signed a December 2025 agreement with GlobalFoundries to manufacture 200 mm GaN-on-silicon, starting at 650 V. Navitas, Innoscience, EPC, Infineon and STMicro are all in production with 650 V GaN.
- **Demand-side ironically helpful**: the BEV slowdown in 2024–2025 has freed SiC capacity. Yole sees the upstream SiC supply running ~50% utilized; device lines ~70%. Net result: there is *headroom* in SiC capacity, not a shortage, for the data center ramp.

*Lead times for power semis are normalizing.*
- Aehr Test Systems (a key burn-in equipment supplier) reports growing AI/data center test orders, indicating supplier ramps are happening on schedule.
- AEC-Q101 automotive SiC MOSFET lead times remained at 52+ weeks in early 2026, but spot premiums of 40–80% are concentrated in automotive grades, not data-center grades.

*Competition is brutal — that is good for buyers.*
With 14 named NVIDIA silicon partners plus the OCP/Mt. Diablo ecosystem and Chinese champions (Innoscience, Silan), no single supplier can hold up the ramp. NVIDIA explicitly stated at OCP 2025 that the multi-vendor reference design strategy is intended to "minimize bottlenecks in constructing next-generation AI factories."

**Historical analogue.** EV-grade SiC went from severe shortage in 2021–2023 (lead times of 52+ weeks, double-digit price premiums) to manageable supply by mid-2024 once Wolfspeed, ST, onsemi and Infineon ramped 150 mm and then 200 mm fabs. The 800 V data center transition will follow a similar 18–24-month curve, with the difference that fabs are already largely built — the marginal capex is qualification and packaging, not greenfield wafer lines.

**Three scenarios for power semiconductors specifically:**

| Scenario | Probability (author estimate) | Description |
|----------|------------------------------|-------------|
| **Bull**: not a bottleneck | 35% | 14+ qualified vendors flood the market; SiC and GaN both move to 200 mm at scale; prices fall through 2027. The 800 V transition is gated only by Kyber rack readiness and grid power. |
| **Base**: transient 12–18 months | 55% | Spot tightness in 1200 V SiC and 1250–1700 V GaN through 2026 as everyone qualifies 800 V designs simultaneously. Lead times stretch to 30–40 weeks for specialty parts but multi-sourcing and OCP standardization smooth procurement by 2H 2027 when Kyber ships in volume. |
| **Bear**: structural multi-year shortage | 10% | A single failure mode (e.g., 1700 V GaN yield issues, SiC substrate quality at 200 mm) plus simultaneous EV recovery in 2027 strains capacity through 2028. Even then, the binding constraint remains the transformer/grid stack. |

**Which other bottlenecks are more binding?** Three are clearly worse than power semis:

1. **Grid power availability.** Per the IEA's "Key Questions on Energy and AI" (April 24, 2026), "electricity consumption from data centres roughly doubling from 485 TWh in 2025 to 950 TWh in 2030, accounting for around 3% of global electricity demand by that date. Electricity consumption from AI-focused data centres grows much faster than overall data centre electricity consumption, tripling in this period." McKinsey ("The next big shifts in AI workloads and hyperscaler strategies," December 17, 2025) projects global data center capacity demand to rise from 82.3 GW in 2025 to 219.0 GW in 2030 at a 22% CAGR, with AI inference (93.3 GW) and AI training (62.2 GW) together accounting for 71% of demand. McKinsey ("How data centers and the energy sector can sate AI's hunger for power," September 17, 2024) projects US data center electricity demand at 606 TWh — 11.7% of total US power demand — by 2030. Sightline Climate's project-level tracking shows the gap between announced and under-construction capacity widening.
2. **Large power transformers.** 128–144-week lead times, prices up 77%, and a US grid where >50% of distribution transformers are past expected life. Per Utility Dive (September 4, 2025), Hitachi Energy's $457 million South Boston, Virginia transformer plant is part of a broader $1 B+ US investment program but is not operational until 2028; Siemens' $421 M Charlotte expansion is still ramping. EnkiAI describes high-voltage transformers and switchgear as "100% of the bottleneck" while accounting for <10% of total data center cost.
3. **Skilled labor + permitting.** Less quantifiable but pervasive; HVDC safety training, liquid-cooling commissioning, MV-DC interconnection are all specialty skills with thin labor pools.

**Bottom line.** 800VHDC power semiconductors are an exciting, fast-growing market and a genuine engineering enabler for 1-MW AI racks, but they are *not* the gating factor for AI data center deployment. The gating factor is the boring, slow-moving stuff: utility grid capacity, large transformers, switchgear and permitting. Operators who are not putting equal urgency on grid interconnection and transformer pre-ordering will find that having abundant 1200 V SiC FETs is small comfort when the substation isn't energized.

---

## Recommendations

**For an AI infrastructure decision-maker (you), staged actions:**

1. **Within 0–6 months (planning):**
   - Treat power-semi-supply risk as Tier-2; treat utility-grid + transformer risk as Tier-1. Lock multi-year transformer slots *now* if you're planning a 2027–2028 facility — that is what determines whether you can deploy Kyber on schedule.
   - When evaluating a colo/hyperscaler for an AI tenancy, ask explicitly: (a) "What is your interconnection queue position and energization date?" (b) "Have you pre-ordered transformers?" and (c) "Is the facility designed for ±400 VDC or 800 VDC, or only retrofit-capable?"
   - **Trigger to escalate concern**: if your operator can't show transformer purchase orders dated before mid-2026 for 2027 occupancy, your project is at material risk regardless of GPU allocation.

2. **Within 6–18 months (procurement & design):**
   - For new builds >100 kW/rack, design for the ±400 VDC sidecar (Mt. Diablo) path as the production case and the 800 VDC monopolar (NVIDIA) path as the upgrade case — they share connectors and busbar at the rack interface.
   - Multi-source power semiconductors across at least three of {Infineon, STMicro, TI, onsemi, Navitas, Power Integrations, EPC, Innoscience}. Treat single-source 1700 V GaN as a yellow flag.
   - **Trigger**: if 1200 V SiC lead times pierce 40 weeks or spot pricing rises >30% by mid-2026, accelerate inventory by one quarter; otherwise standard JIT is fine.

3. **Within 18–36 months (deployment):**
   - Target Vera Rubin NVL144 (190 kW, late 2026, drop-in to existing 132-kW Oberon-class facilities) for any 2026–2027 capacity.
   - For 2027+ capacity, plan natively for Kyber 800 VDC and budget for in-row SSTs (Delta, SolarEdge/Infineon, Amperesand) and 1.2-MW-class sidecars (Schneider, Vertiv).
   - **Trigger**: if Wolfspeed/ST/Infineon 200 mm SiC yields disappoint in 2026 (look for quarterly utilization disclosures), defer aggressive 800 V buildouts and stay on ±400 VDC sidecar architecture.

---

## Caveats

- **Roadmap dates are vendor-published projections.** Kyber, Rubin Ultra and 800VDC production are confirmed by NVIDIA but actual ship volumes for 2027 are not yet locked, and the chip industry has a history of slipping 3–6 months on major transitions.
- **The "$50K → $100K per 1 MW AI rack" power-semi BOM figure is onsemi's own statement (via William Blair).** It is directionally consistent with Morgan Stanley's "10x by 2027" qualitative claim but no audited third-party teardown of an NVL72 has been published. Triangulated device counts (several thousand discrete FETs/controllers) are author estimates derived from Infineon, ST and Bianca-board references.
- **Efficiency improvements of "up to 5%" and TCO reductions of "up to 30%" are NVIDIA marketing figures.** Real-world facility efficiency gains depend heavily on cooling design, baseline architecture and load profile. Independent peer-reviewed validation is not yet available.
- **OCP 800VDC standardization is still maturing.** Mt. Diablo v0.5.2 is a base specification, not a ratified standard; the OCP LVDC v1.0 whitepaper (Q1 2026) is explicitly "directional" and does not yet specify voltage tolerance bands or final connector/protection schemes. IEEE/IEC formal standards are not yet finalized.
- **Bottleneck severity differs by region.** Singapore (where the user is based) and most of APAC face different constraints than the US: less acute transformer shortage, more acute land/water constraints, and stricter regulatory caps on data center power (Singapore's 2019–2022 moratorium). 800VDC adoption in APAC will likely be paced by Chinese SST players (Delta, Hopewind, Megmeet, Zhongheng) rather than US/EU vendors.
- **Author probabilities for bull/base/bear scenarios are subjective**, derived from a synthesis of cited evidence rather than a formal market model.
- **The GaN-on-QST, GaN-on-SiC and GaN-on-Si distinctions** the user asked about are relevant for cost/quality trade-offs (QST and SiC substrates give better thermal performance, Si is cheaper) but no single supplier dominates and the choice is not on the critical path for 800 VDC deployment in 2027.