# Thesis — AI Datacenter Supply Chain & Chokepoints

**Last updated:** 2026-06-25
**Owner:** Vic (human-maintained; never edited by the LLM except by explicit Vic-authorized rework session)

---

## What I'm trying to figure out

I want to understand where durable value accrues across the **AI datacenter supply chain** during the multi-year hyperscaler CAPEX expansion cycle. My operating hypothesis is that value concentrates at structural chokepoints — positions the supply chain cannot route around — and that hyperscaler spending flows asymmetrically across these chokepoints rather than uniformly across the supply chain.

The wiki exists to help me answer five questions with precision:

1. **Where are investment opportunities in the AI datacenter boom?** Across photonics, memory, energy, power, equipment, materials, compute (GPU + CPU + custom ASIC), and adjacent infrastructure — which positions are structurally durable vs cyclically dependent? Where do the highest-quality risk-adjusted opportunities concentrate? My focus is on US-listed equities (with selective foreign-issuer coverage where structural positioning is material) accessible via IBKR.

2. **How does hyperscaler CAPEX flow through the supply chain?** Hyperscaler AI infrastructure CAPEX is expanding to ~$640-720B in 2026 (Microsoft FY2026 ~$190B+; Alphabet 2026 $180-190B; Amazon 2026 ~$200B; Meta 2026 $125-145B; plus Oracle Stargate + emerging neoclouds). Which companies capture which share of this CAPEX flow? Where do CAPEX dollars concentrate (compute / networking / power / cooling / storage / facilities) and how does the flow propagate through Tier 1 / Tier 2 / Tier 3+ supply chain layers?

3. **What are the structural chokepoints across the AI datacenter supply chain?** Photonics chokepoints (CPO integration; advanced optical packaging; InP supply; optical DSP/PHY; laser/EML supply) are mapped extensively in this wiki. But the AI datacenter has chokepoints beyond photonics — and as 2026 has revealed, the **most binding chokepoints have shifted from compute supply to power infrastructure**. Power transformers (120-week lead times; 210 weeks for large units), substations, switchgear, HBM oligopoly capacity, and grid interconnection queues are now the gating factors. Half of planned 2026 US datacenter builds are delayed or cancelled due to power infrastructure shortages, not chip availability.

4. **How do the layers of the AI datacenter supply chain interact?** From hyperscaler customer (Layer 0) → platform integrator (Layer 1: NVDA / AVGO) → foundry/packaging (Layer 2: TSM) → specialized designer (Layer 3: MRVL / CRDO / ALAB / ANET) → component supplier (Layer 4: COHR / LITE / VIAV) → integrated systems (Layer 5: AAOI) → scale manufacturing (Layer 6: FN / FLEX). Plus parallel layers across non-photonics domains (memory tier; energy/power tier; equipment tier; materials tier). How does value flow across layers? Where do margins compress vs expand under different scenarios?

5. **What are the inter-connections between AI datacenter companies?** Cross-layer relationships (NVDA $2B equity-plus-purchase modality at LITE + COHR; Mellanox acquisition; Groq licensing; OpenAI ↔ Oracle ↔ AWS Trainium 2GW commitment; Anthropic ↔ AWS 5GW Trainium commitment); customer concentration patterns (AAOI Microsoft 43%; FN NVIDIA 27.6% + Cisco 18.2%; CRDO Customer A 67%→48%; SK Hynix NVDA 90%); architecture co-development (NVDA + TSM COUPE; MRVL Celestial AI acquisition; Amazon + Anthropic Project Rainier 500K Trainium2 cluster). The AI datacenter supply chain is not a stack of independent companies but a network of cross-cutting relationships that determine who captures value at what layer.

## Core framework

The wiki categorizes companies along multiple analytical axes developed across prior analytical work; canonical specifications in `raw/notes/frameworks.md`.

**Value capture layer (six tiers, from highest to lowest structural capture):**

1. **Platform definers** — architecture control (NVDA, AVGO)
2. **Irreplaceable infrastructure** — physical moat (TSM, ASML, HBM oligopoly Samsung/SK Hynix/Micron, datacenter REITs, grid energy)
3. **Specialized designers** — technical expertise (MRVL, ALAB, AMAT/LRCX/KLAC, EDA, silicon photonics startups, custom silicon design)
4. **Differentiated components** — process specialization (COHR, LITE, HyperLight, AI-native storage, high-density power delivery, advanced cooling)
5. **Integrated systems** — commercial integration (AAOI, ANET, DELL, HPE, system OEMs)
6. **Scale manufacturing** — operational efficiency (FN, FLEX, CLS, Foxconn, contract manufacturing)

**Structural vs. cyclical exposure to AI datacenter thesis:**

- **Structural AI exposure** — company's AI datacenter positioning is specific and product-differentiated (e.g., ONTO advanced packaging metrology; AEHR advanced packaging test; LITE datacenter lasers; VRT NVIDIA-aligned thermal infrastructure; SK Hynix HBM3E/HBM4)
- **Broad-cycle exposure** — company has general semi/industrial/infrastructure cycle beta with AI as one of many end markets (e.g., COHU broad semi test handler; PLAB photomask broad semi exposure; FLEX broader EMS exposure with AI datacenter subsegment)

Company pages explicitly track which applies. Owning a position with broad-cycle exposure in an AI datacenter basket is legitimate, but should not be categorized as "AI-specific exposure" when it isn't.

**Domain-specific framework structures:**

- **Framework 5 photonics tier** (Tier 1-5 + Outside Framework 5) — covers photonics-direct exposure assessment per `raw/notes/frameworks.md`
- **Future framework structures** (per CLAUDE.md v9 multi-domain expansion convention; pending Vic-curation):
  - Memory tier framework (HBM oligopoly tier; DRAM scaling tier; logic-memory interface tier)
  - Energy/Power tier framework (grid energy tier; power delivery tier; thermal infrastructure tier; power transformer tier)
  - Equipment tier framework (lithography tier; metrology tier; advanced packaging equipment tier)

**Framework 2.6 control-point gradation (orthogonal to value capture layers):**

Five tiers across the platform/bottleneck axis:
- Full control point (NVDA)
- Control point with bottleneck participation (AVGO)
- Bottleneck-tier with control-point aspirations (MRVL, CRDO)
- Bottleneck participant with platform-tier ambition (CSCO, ANET)
- Pure bottleneck participant

Framework 2.6 operates across all domains (not photonics-specific); applies to compute / memory / power / equipment companies as scope expands.

## Hyperscaler CAPEX flow analysis

**The structural fact:** Hyperscaler AI infrastructure CAPEX is now the largest corporate investment cycle in history. Combined 2026 CAPEX guidance from Microsoft + Alphabet + Amazon + Meta is **~$640-720B**, roughly double 2025's $381B — a figure now **primary-sourced across all four payers** (it previously rested on NVDA's analyst-estimate framing). Including Oracle, the cohort extends toward **~$700-770B**; current analyst/web aggregation commonly cites ~$725B for the US hyperscalers, and TrendForce puts the top-nine *global* cloud providers at ~$830B in 2026 (+79% YoY) — both Tier-3 context, not vault-verified. The canonical primary-by-payer breakdown (per-quarter updates, Oracle's financing-envelope extension, the financing/global layers) lives in the `wiki/trackers/hyperscaler-capex.md` tracker. The trajectory continues — Alphabet has explicitly guided 2027 CAPEX to "significantly increase" from 2026 levels.

**2026 hyperscaler CAPEX guidance:**

| Hyperscaler | 2025 CAPEX (actual) | 2026 CAPEX (guidance) | YoY Δ |
|---|---|---|---|
| Microsoft (FY2026) | ~$88B (FY2025) | $190B+ (raised April 2026) | +116% |
| Alphabet (Google) | $91B | $180-190B | +98-109% |
| Amazon (AWS) | $131B | ~$200B | +53% |
| Meta | $72B | $125-145B | +73-101% |
| Oracle | ~$15B | Stargate $100B initial / $500B by 2029 | Multi-year commitment |
| **Combined Big 4** | **~$381B** | **~$640-720B** | **~+70-90%** |

*Status note (refreshed 2026-06-25, Vic-authorized): the Big-4 per-company figures in the table below are the April-2026 guidance and remain consistent with the current primary-sourced figures on the demand-side hyperscaler pages (MSFT / GOOGL / AMZN / META / ORCL) and the `wiki/trackers/hyperscaler-capex.md` tracker — which is the canonical home for the live payer-by-payer breakdown. The aggregate paragraph above was refreshed (primary-sourced; Oracle extension; analyst/global context); the per-row table below is left at its April-2026 values as a dated snapshot. Read the tracker for the current per-quarter detail.*

**Microsoft FY2026 trajectory:** Q1 FY2026 CAPEX $34.9B; Q2 $37.5B; Q3 $31.9B; full-year guidance raised to $190B+ as of April 2026 (originally $110-120B). Roughly two-thirds of Q3 spend on short-lived assets (GPUs/CPUs); one-third on long-lived assets (datacenters/land/power infrastructure for 15+ year lifespans). Azure backlog $80B; capacity constrained through 2026.

**Alphabet 2026 trajectory:** Original guidance $175-185B; raised to $180-190B in Q1 2026 earnings (April 2026). 60% allocation to servers; 40% to datacenters and networking equipment. Google Cloud backlog $460B (nearly doubled QoQ). 2027 CAPEX guided to "significantly increase."

**Amazon 2026 trajectory:** $200B guidance (vs $131B 2025; +53%). Trainium2 fully subscribed at 1.4M chips; 2.1M total AI chips landed past 12 months (>50% Trainium); 1M+ NVIDIA GPUs to deploy starting 2026. Trainium revenue commitments at $225B (per Jassy Q1 2026). OpenAI 2GW Trainium commitment ramping 2027; Anthropic 5GW Trainium commitment.

**Meta 2026 trajectory:** Original guidance $115-135B; raised to $125-145B in Q1 2026 (April 2026). Cited "higher component costs" and "additional data center costs." Meta raising $20-25B in bonds to fund AI infrastructure spending. Memory chip shortage extending server lifespans per WSJ.

**CAPEX flow categories (rough estimates of allocation; not all hyperscaler disclosures break this down):**

1. **Compute (GPU + CPU + custom ASIC) — largest single category, ~50-65% of hyperscaler CAPEX**
   - NVDA: dominant merchant GPU (~70%+ AI accelerator share); Blackwell B200/B300 ramping; Vera Rubin 2026; Kyber CPO scale-up
   - AMD: MI300/MI350/MI400 series; share growth uncertain
   - Custom ASIC: AVGO Google TPU partnership; Marvell Microsoft custom; Amazon Trainium2/3/4 (TSMC manufactured)
   - CPU: Intel datacenter; AMD EPYC; ARM-based hyperscaler custom (Amazon Graviton; Microsoft Cobalt; Google Axion)

2. **Networking (switching + interconnect + optical) — ~10-15%**
   - Switch ASIC: AVGO Tomahawk; MRVL Photonic Fabric; CSCO Silicon One; ANET 7xxx series
   - Optical: LITE / COHR / AAOI (transceivers + lasers); CRDO / MRVL / AVGO (DSPs); FN (contract manufacturing)
   - InfiniBand/NVLink: NVIDIA proprietary; Ethernet adoption competing

3. **Memory (HBM + DRAM) — ~10-15%, structurally constrained**
   - HBM oligopoly: SK Hynix 50-62% share (NVDA primary supplier; ~90% NVDA HBM); Samsung 17-35% share recovering; Micron 11-21% share; HBM4 entering mass production 2026; "3-to-1 rule" (every AI chip destroys capacity to make 3 normal PC chips); HBM consumed 23% of DRAM wafers Q4 2025
   - DRAM/NAND: tightening due to HBM cannibalization; commodity DRAM supply shock from Samsung HBM4 ramp

4. **Power infrastructure — ~10-15%, NOW THE BINDING CONSTRAINT**
   - **Transformers:** 120-week lead times (210 weeks for large units; 4 years); GOES steel constraint (Cleveland-Cliffs sole US supplier); 80% historically imported from Mexico/China/Thailand
   - Power semiconductors: MPWR / VICR / IFNNY (high-density power delivery); 800V DC architecture transition (VRT canonical H2 2026 program)
   - Switchgear / cables / busways: ABB / ETN / Schneider / HD Hyundai Electric / Hyosung Heavy Industries / Prysmian / Nexans / NKT / Powell Industries
   - Backup power / UPS / gensets: VRT / CAT / CMI / GNRC
   - **~50% of planned 2026 US datacenter builds delayed or cancelled due to power infrastructure shortages** per Bloomberg/Sightline Climate

5. **Thermal infrastructure / cooling — ~5-10%, transition to liquid cooling**
   - Direct-to-chip liquid cooling adoption (rack densities 100-240kW exceed air cooling capacity)
   - VRT (canonical thermal); MOD; FLEX (JetCool acquisition); Schneider; emerging Chinese suppliers

6. **Datacenter facilities + REITs — ~10-15%**
   - Hyperscaler-built (Microsoft Fairwater 2GW Wisconsin; Amazon Project Rainier; Stargate Texas/New Mexico/Ohio)
   - Datacenter REITs (DLR / EQIX / VRT-adjacent)
   - Specialty facilities builders

7. **Equipment — semiconductor capex flowing through TSMC/foundries**
   - Lithography: ASML EUV monopoly + High-NA ramp
   - Metrology: ONTO / KLAC / KLA
   - Advanced packaging: AEHR (test); ASE / AMKR (OSAT); TSM CoWoS internal
   - Test: KEYS / VIAV / Anritsu / FormFactor

8. **Materials — specialty constraints**
   - Specialty gases (semi manufacturing; Air Products/Linde)
   - Rare earths (power semi magnets; Chinese export concentration)
   - Substrate supply (InP/AXTI; silicon wafers; HBM substrates)
   - GOES steel for transformers (Cleveland-Cliffs)
   - Copper (cabling at scale)

**Cross-cutting CAPEX flow patterns:**

- **NVDA platform integration vertical securing.** NVDA captures Tier 1 CAPEX flow at compute layer; through six-modality platform integration framework (Mellanox / Groq / COHR-LITE equity / Ayar Labs / GLW / VRT), NVDA secures cross-layer access to component-tier CAPEX. NVDA exposure provides indirect access to all NVDA-aligned component layers.

- **Custom silicon programs as CAPEX flow redirection.** Amazon Trainium ($225B revenue commitments; OpenAI 2GW + Anthropic 5GW commitments); Google TPU (AVGO partnership); Microsoft Maia (now live in Iowa/Arizona; "30% improved tokens per dollar"). Custom silicon shifts CAPEX flow away from merchant Layer 1 (NVDA) toward Layer 2 (TSM manufacturing) + Layer 3 designers (AVGO custom; MRVL custom). Hyperscaler-captive silicon could save "tens of billions annually in capex" per Jassy.

- **Hyperscaler customer concentration as CAPEX flow concentration risk.** AAOI Microsoft 43%; LITE+COHR NVDA $2B equity each; CRDO Customer A 67%→48%; SK Hynix NVDA ~90%; FN NVIDIA 27.6% + Cisco 18.2%. Position sizing should account for shared hyperscaler exposure across multiple holdings — CAPEX flow concentration is structural risk.

- **Power constraint as binding ceiling on CAPEX deployment.** Money is not the bottleneck — $650B+ CAPEX commitments exceed deployable infrastructure. Transformer 4-year lead times mean compute CAPEX cannot deploy faster than power infrastructure expansion. This creates persistent constraint on Tier 1 (NVDA / AMD) revenue trajectory while power infrastructure suppliers (ETN / VRT / ABB / Schneider / HD Hyundai / Hyosung) capture pricing power.

- **HBM cannibalization of commodity DRAM.** HBM3E to HBM4 transition increases dies-per-stack from 12 to 16 (33% more DRAM dies per AI accelerator); Samsung HBM4 ramp depleting commodity DDR5 capacity. AI compute scaling structurally tightens broader memory market — affects every server class, not just AI.

## Demand-side metrics — how the buildout's output is judged

The CAPEX flow analysis above is the **input** side (money in, by domain). This thesis is built almost entirely supply-side — where value accrues across the chain — but the supply-side map carries no object for **how the factory's output is measured**: whether a given gigawatt or dollar of capex is actually producing monetized intelligence. The Stanford CS153 "AI factory" lens supplies that demand-side / unit-economics metric set — a Tier-3 outside-view (the speakers are talking their books; the speaker-attributed detail and the agree/diverge cross-walk against vault canon live at `wiki/themes/ai-frontier-systems.md`). It is a measurement frame, not a vault fact — every figure on the source page is rendered soft and pre-registered for primary-source verification.

The discriminating dials judge the buildout on output per scarce input, not on headline capex or announced megawatts:

- **Value-per-gigawatt** (revenue-per-GW; daily-active-users-per-GW) — the cleanest cross-stack return measure. A poorly-balanced gigawatt delivers a fraction of a balanced one's output, so raw GW and raw spend are weak metrics. This is the same distinction between capex and return-on-invested-capital a public-market investor has to draw.
- **Tokens-per-watt / energy-per-token** — the efficiency the buildout is judged on; with power the binding constraint, output-per-watt is the unit that matters.
- **Tokens-per-dollar / cost-per-token** — the factory's unit cost (accelerator depreciation + HBM/package + power + networking + storage + financing, divided by tokens delivered at target quality/latency × utilization). Microsoft's Maia "~30% improved tokens per dollar" is the one place the supply-side map already touches this.
- **Memory-bandwidth-per-flop / system balance** — the real gate is memory bandwidth, not flops (the infra-side statement of the memory-wall / HBM thesis already in this file); low measured utilization (MFU) is the symptom of an unbalanced system.
- **The MW funnel** — requested → studied → contracted → permitted → under-construction → energized → utilized megawatts; only the last two are real capacity. The discipline-keeper behind the "announced ≠ energized / money is not the bottleneck" reframing already central to this thesis.

Why it matters here: these dials adjudicate the **capex-vs-return** question the whole buildout rests on — the timing risk the hyperscalers all acknowledge (per the `wiki/trackers/hyperscaler-capex.md` tracker). If value-per-GW and cost-per-token keep improving and the revenue conversion shows up, the supply-side chokepoint thesis holds; if output-per-input stalls while capex keeps climbing, that is the bubble / cycle-turn case (the `wiki/themes/ai-frontier-systems.md` centerpiece + the `wiki/trackers/what-could-go-wrong.md` register).

## The portfolio positions

Each holding is present for a reason rooted in this framework. What I want the wiki to track for each:

**Photonics-anchored positions (vault baseline; current holdings):**

- **NVDA** — Layer 1 platform definer, most central to thesis. Wiki tracks: photonics strategy evolution (Spectrum-X production; Quantum-X; Kyber CPO scale-up; COUPE), TSMC allocation, competitive positioning vs AVGO, ecosystem lock-in signals, NVDA platform integration six-modality framework, CAPEX flow concentration as primary compute CAPEX recipient.

- **TSM** — Layer 2 structural chokepoint. Wiki tracks: CoWoS and COUPE capacity commentary, capex trajectory, N2 and A14 ramp, geopolitical risk commentary, pricing power signals, custom silicon ASIC manufacturing for hyperscalers (Trainium / Google TPU / Microsoft Maia all manufactured at TSMC).

- **AEHR** — Layer 3-4 specialized test equipment, advanced packaging exposure. Wiki tracks: design wins at advanced packaging customers, customer concentration, revenue visibility, differentiation vs broader semi test, wafer-level burn-in adoption trajectory.

- **ONTO** — Layer 3-4 advanced packaging metrology. Wiki tracks: CoWoS/COUPE-adjacent revenue, metrology share, memory and logic cyclicality offset, HBM4 ramp benefit (16-Hi stack metrology requirements).

- **LITE** — Layer 4 differentiated components, datacenter laser exposure. Wiki tracks: datacenter transceiver laser share, CPO laser positioning, NVDA $2B equity-plus-purchase relationship, three-inch InP industry-standard manufacturing, ELS architecture exposure.

- **AAOI** — Layer 5 integrated systems, datacenter transceiver assembler. Wiki tracks: Microsoft customer concentration (~43%), LPO positioning vs CPO displacement risk, Layer 4/5 straddling tension (Sugar Land MBE+MOCVD InP/GaAs laser fabrication; tier upgrade trigger pre-registered), margin progression.

- **COHU** — Layer 3 semi test handler; **Outside Framework 5 placement** per honest-verdict discipline (broad-cycle semi exposure with AI as minority subsegment). Most analytically uncertain holding.

**Adjacent infrastructure positions (vault baseline):**

- **VRT** — Layer 5 / photonics_tier 4 thermal infrastructure with NVIDIA reciprocal-confirmation; 800V DC programs H2 2026; EcoDataCenter Sweden Vera Rubin deployment. Wiki tracks: thermal/power infrastructure positioning under 2026 power constraint binding; VRT vs FLEX (JetCool) competitive dynamics; structural reclassification under AI datacenter scope (was adjacent infrastructure under photonics-primary scope; now primary chokepoint exposure under power-binding-constraint observation).

**Candidate additions per AI datacenter scope expansion (sequenced per vault planning):**

*Status note (2026-06-04): FLEX, ETN, MU, MPWR, VICR, VECO, and TSEM are now ingested vault pages (see `index.md`); the per-name notes below reflect the original pre-ingest framing and are retained as written.*

- **FLEX** (Session 36+): Layer 6 contract manufacturing + JetCool liquid cooling acquisition. Liquid cooling AI datacenter exposure thesis verification at primary sources. Possible Outside Framework 5 placement if EMS exposure dominates.
- **ETN** (Session 37+): Layer 4-5 power infrastructure; canonical Tier B Energy/Power per Tier 3 source. Power transformer + electrical equipment exposure — most directly investible US-listed exposure to the binding 2026 power constraint.
- **MU** (Session 38+): Layer 2 memory oligopoly participant; only US-listed HBM oligopoly exposure; 11-21% market share; HBM3E shipping 12-stack; HBM4 ramping 2026.
- **MPWR / VICR** (Session 39+): Layer 4 high-density power delivery; 800V DC architecture transition beneficiaries.
- **VECO** (already vault-canonical at InP-supply.md): Layer 4 MOCVD epitaxial reactor equipment; future elevated focus per epitaxial chokepoint coverage.
- **TSEM / GFS** (foreign-issuer ingest pending FY2025 20-F): Layer 2 photonic foundry tier merchant alternatives to TSM dominant position.
- **Foreign-listed candidates (require IBKR foreign access decision):** Samsung Electronics (KRX 005930) + SK Hynix (KRX 000660) — HBM oligopoly direct exposure; ASE Technology (Taiwanese ADR) — OSAT-tier photonic packaging; Aixtron (German; XETRA AIXA) — MOCVD equipment competitor to VECO; ABB (Swiss; ABB) + Schneider Electric (French; SBGSF) — European power infrastructure incumbents; HD Hyundai Electric + Hyosung Heavy Industries (Korean) — Korean transformer manufacturers expanding US capacity at structural pricing power point.

The portfolio should evolve toward **dual-anchor exposure across compute (NVDA / TSM as canonical) + power infrastructure (ETN / VRT as canonical)** as the binding constraint observation matures. Photonics positions remain core to thesis but should be sized considering the broader AI datacenter exposure rather than photonics-pure exposure.

## What would prove this thesis wrong

The wiki should watch for evidence that would challenge or disprove the thesis, not just support it.

**Photonics-thesis falsification candidates (preserved from prior _thesis.md):**

- **CPO adoption stalls or reverses.** If hyperscalers signal they're sticking with pluggable transceivers into 2028+, the displacement thesis weakens and AAOI's position looks stronger rather than weaker.
- **TSMC's packaging advantage narrows.** If Intel Foundry, Samsung, or ASE meaningfully close the gap on advanced packaging, TSMC's chokepoint status becomes less durable.
- **NVDA loses CPO ecosystem momentum to AVGO.** If design wins and partner announcements concentrate around Bailly rather than Quantum-X/COUPE, the NVDA platform thesis weakens.
- **Silicon photonics startups get acquired into hyperscalers rather than merchant platform players.** If Ayar Labs goes to Microsoft or Lightmatter goes to Google, the "open CPO platform" thesis breaks down in favor of hyperscaler-captive implementations.
- **Advanced packaging test/metrology opportunity smaller than expected.** Faster CoWoS yield improvements weaken AEHR/ONTO leverage.

**AI datacenter scope-expanded falsification candidates:**

- **Hyperscaler CAPEX deceleration.** If hyperscaler AI infrastructure CAPEX expansion materially decelerates (sustained QoQ deceleration; full-year guidance cuts; cloud backlog growth slowing materially), the AI datacenter buildout thesis weakens broadly. Track quarterly CAPEX guidance changes — particularly Microsoft, Alphabet, Amazon, Meta. Currently all four raised guidance in Q1 2026 earnings.

- **HBM supply catches up to demand.** If HBM4 ramps on time across all three vendors (Samsung / SK Hynix / Micron) and oligopoly pricing normalizes, the structural HBM chokepoint proves more cyclical than assumed. Track HBM4 capacity trajectory + pricing dynamics; HBM3E spot prices currently ~$300/stack with HBM4 estimated ~$500/stack.

- **Power infrastructure constraint resolves faster than expected.** If transformer manufacturing capacity expands materially (Cleveland-Cliffs steel expansion; Korean/Chinese supplier US capacity additions; modular substation adoption), grid interconnection queues accelerate, regulatory expedition succeeds — thermal/power infrastructure thesis weakens. Currently lead times stretching not compressing (120-week transformer; 210 weeks for large units; 4-year delivery for some).

- **Custom silicon disrupts merchant compute materially.** If hyperscaler custom silicon (Google TPU; Microsoft Maia; Amazon Trainium2/3) captures meaningful share from NVDA merchant GPU at faster pace than expected, Layer 1 compute concentration thesis weakens. Trainium $225B revenue commitments + OpenAI 2GW + Anthropic 5GW commitments are early signals — track NVDA share in hyperscaler new deployments.

- **Liquid cooling adoption stalls.** If hyperscaler datacenter cooling adoption stays predominantly air-cooled into 2028+, thermal infrastructure thesis (VRT + adjacent) bounded near-term. Currently rack densities 100-240kW exceed air cooling; transition appears structurally forced.

- **AI inference compute requirements compress materially.** Algorithmic efficiency gains (Mixture-of-Experts; quantization; sparse models; smaller specialized models) may reduce per-query compute demand faster than total query growth, decelerating compute CAPEX. Watch for trend lines in tokens/dollar metrics (Microsoft Maia "30% improved tokens per dollar" framing already shows efficiency focus).

- **Macro or geopolitics dominate structural analysis.** Taiwan crisis (TSM dependency); broad semi downturn; export control escalation (China rare earths; Korean memory; Chinese transformer supply); energy crisis; AI regulation overhang. Could make structural positioning irrelevant for 12-24 months.

- **Demand-side softening from end customers.** If enterprise AI adoption disappoints (consumer AI revenue trajectory; B2B SaaS AI monetization slower than expected), hyperscaler ROI on AI CAPEX spending becomes negative, triggering CAPEX guidance reversal. Track hyperscaler AI revenue run rates: AWS AI revenue $15B+ run rate Q1 2026; Microsoft Copilot/Azure AI revenue trajectory; Google Cloud AI revenue + backlog growth.

- **Datacenter overbuilding correction (2027-2030).** S&P Global flags risk of overbuilding in some locations medium-term. If 2027-2030 sees efficiency gains (liquid cooling; model specialization; AI optimization) reducing infrastructure requirements simultaneously with overbuilt capacity coming online, regional asset-stranding risk surfaces.

The wiki should flag evidence of any of these, not ignore or minimize it.

## What the wiki is for — and what it isn't

**The wiki is for:**
- Synthesizing what I actually believe about AI datacenter supply chain dynamics as evidence accumulates
- Stress-testing each position's structural fit with the thesis (across all domains, not just photonics)
- Surfacing chokepoints and cross-company relationships across compute / photonics / memory / energy / power / equipment / materials
- Tracking how specific companies' strategic positioning evolves quarter over quarter
- Mapping hyperscaler CAPEX flow patterns and concentration dynamics
- Generating uncomfortable conclusions when my positions don't fit the thesis

**The wiki is not for:**
- Tracking P&L, cost basis, or position sizing (that lives in IBKR + trading journal)
- Recommending whether to buy, sell, or hold specific names
- Covering the AI datacenter sector comprehensively — companies that don't inform the thesis don't need pages
- Producing confirmation of views I already hold; the honest verdict matters more than the comfortable one

## Scope discipline

Companies earn pages by showing up in primary sources relevant to the thesis — not by being on a predefined list. Portfolio holdings are starting points, but as filings and calls surface other names across compute / photonics / memory / energy / power / equipment / materials, they should get pages when they cross the multi-source threshold (per CLAUDE.md v9 vault scope codification).

**Vault scope expansion mechanism (per CLAUDE.md v9):** AI datacenter supply chain — compute, photonics, memory, energy, power, equipment, and more. Vault under ongoing expansion; sequencing per opportunity (source availability, thesis development, time-bounded events) rather than rigid pre-codification. Domain-specific Tier 3 framework sources to be Vic-curated as expansion proceeds.

## Chokepoint-by-chokepoint investment thesis

*This section captures investment thesis content per chokepoint across AI datacenter supply chain domains. Photonics chokepoint baseline preserved from prior _thesis.md (Sessions 1-32 vault canonical content); multi-domain chokepoint expansion adds Energy/Power, Memory, Equipment, Materials, Compute domains.*

### Photonics chokepoint baseline (Sessions 1-32 canonical)

**InP substrate (Rank 3):** AXTI is a high-beta upstream scarcity play with structural-cyclical hybrid profile; structural Western-HQ InP supplier position offset by China manufacturing footprint and small revenue base. COHR is a broader, higher-quality photonics exposure with partial vertical integration — substrate exposure via six-inch InP wafer position, not as a pure substrate stock. Two-layer InP supply distinction (indium feedstock JX Advanced Metals ~78% upstream of InP wafer production AXTI ~60-70%) means substrate-supply thesis decomposes into feedstock concentration + wafer-production capacity.

**Lasers / EMLs / III-V devices (Rank 1):** LITE and COHR are the highest-quality US-listed broad photonics exposures and are now NVDA-aligned via $2B equity-plus-purchase modality (March 2026). COHR sits at photonics_tier 2 (six-inch InP device-fabrication position + 20-year NVDA relationship); LITE at photonics_tier 3 (three-inch InP industry-standard + newer capital-offset relationship). MTSI is a differentiated component play (analog/RF/optoelectronic). AAOI is a high-beta transceiver/laser execution play with Microsoft customer concentration ~43% — Layer 5 transceiver assembler with Layer 4 in-house InP/GaAs laser capability flagged as straddling tension.

**Optical DSP / PHY power-performance (Rank 2):** MRVL Ara 3nm 1.6T PAM4 DSP and AVGO Taurus 400G/lane optical DSP are core architecture-enabling names. CRDO Cardinal Optical PAM4 DSPs (mature node n-1 cost advantage) is the third primary-source vault company at this chokepoint. CRDO and MXL offer more upside if they gain share or benefit from LPO/LRO/AEC/SerDes transitions — but CRDO uniquely positions AGAINST CPO via OmniConnect MicroLED + ZeroFlap optics CPO displacement framing. Layer 3 four-variant CPO profile per vault Session 28 codification: MRVL escalating disclosure / ALAB phased coexistence / CSCO acknowledged-deferral / CRDO displacement positioning.

**Advanced optical packaging / alignment (Rank 5):** FN is the neutral manufacturing bottleneck play (NVIDIA 27.6% + Cisco 18.2% top-2 customer concentration per FY2025 10-K). LITE and COHR combine components with process know-how (vertically integrated photonic packaging). ASE/AMKR benefit if photonic packaging moves closer to mainstream advanced packaging. AAOI has vertical module execution leverage but high customer concentration risk. Vault canonical chokepoint page `wiki/chokepoints/advanced-optical-packaging.md` (Session 31) — four distinct vertical integration patterns synthesized.

**Silicon photonics foundry / PIC capacity (Rank 9):** TSM is the high-quality platform bet (CoWoS today + COUPE roadmap). GFS and TSEM are more direct merchant foundry optionality plays. TSEM is foreign private issuer (20-F + 6-K filings); vault ingest pending FY2025 20-F filing. Future bottleneck rather than tightest current one.

**Scale-up CPO integration (Rank 10a, v2 bifurcation):** This is the real CPO platform battle per Murphy bifurcation thesis. MRVL Photonic Fabric is the most quantified scale-up CPO bet ($1.3B-$5.5B Celestial AI; $500M FY2028 / $1B FY2029 run rate projections — over-claim mode rhetorical). NVDA Kyber CPO scale-up disclosed at GTC March 2026 alongside copper-scale-up Vera Rubin path ("we're gonna do both" — Jensen). AVGO Bailly platform never named in vault primary sources but AVGO custom XPU + scale-up SerDes positioning provides optionality. Three Layer 1 control-point names with three structurally distinct CPO positions — outcome genuinely uncertain. Bet on scale-up CPO via MRVL is the most quantified path; NVDA is platform diversified across both copper and optical scale-up; AVGO is the dismissal-proven-right scenario. Vault canonical chokepoint page `wiki/chokepoints/cpo-integration.md` (Session 32) — multi-vantage-point synthesis across 9 vault companies.

**Scale-out CPO integration (Rank 10b, v2 bifurcation):** Bounded near-term thesis if Murphy "scale-out CPO relatively limited" framing holds. Pluggable transceiver suppliers (LITE/COHR/AAOI) likely retain scale-out share into 2028+. NVDA Spectrum-X CPO production is falsification candidate for "scale-out limited" framing — production deployment volume vs pluggable retention is the resolving signal. Bet on continued pluggable share via LITE/COHR is the consensus-default scenario.

**Fiber / connectors / high-density attach (Rank 11):** Good second-order infrastructure exposure, especially if CPO increases high-density attach requirements. GLW (Corning Optical Communications $6,274M FY2025 revenue + Meta $6B agreement) is the cleanest US-listed; APH datacenter interconnect exposure adds complementary positioning. AI photonics may not dominate consolidated earnings — diversified business mix limits thesis-pure exposure.

**Finished-module optical test (Rank 6):** Less glamorous but durable test-equipment exposure to every speed transition. KEYS / VIAV / Anritsu benefit from 1.6T validation cycle. VIAV (vault Session 28) extends NSE data center mix to 45% Q2 FY2026; Spirent acquisition $425M from Keysight (closed October 16, 2025); multi-quarter visibility extension (1-1.5 → 3 quarters) per Khaykin. Equipment-refresh logic is credible but TAM is bounded relative to component layers.

**Wafer-level SiPh reliability test (Rank 8):** High-upside narrow exposure if wafer-level burn-in becomes standard in SiPh / optical I/O production flows. AEHR is single-public-pure-play; provisional chokepoint per vault Session 25 single-company-exposure designation. Promotion to canonical pending FormFactor vault entry / ASE-AMKR primary-source ingestion / new public entrants in wafer-level photonic reliability test ecosystem.

**Switch ASIC / platform architecture (Rank 7):** Own the decision-makers rather than only the component suppliers — but five-tier control-point gradation matters per Framework 2.6 orthogonal axis. NVDA full control point ≠ ANET bottleneck participant with platform-tier ambition. Risk that valuation already reflects strategic control varies sharply by tier:
- NVDA (full control point): strongest strategic position; valuation likely reflects most of it
- AVGO (control point with bottleneck participation): Layer 1/3 straddling tension; semi margins at Layer 1-2 boundary
- MRVL (bottleneck-tier with control-point aspirations): Photonic Fabric is genuine platform-tier ambition; aspiration not yet realized; Layer 3→2 trajectory in progress with no triggers met
- CSCO (bottleneck participant with platform-tier ambition): Silicon One + Acacia capability is real; acknowledged-deferral CPO position is weakest commitment of five contestants
- ANET (bottleneck participant with platform-tier ambition): EOS + NetDL software platform + ESUN founding member; bounded by single merchant silicon vendor dependency on AVGO Tomahawk; Layer 5 with Layer 5 photonics_tier — long-term CPO displacement risk most exposed

**Thermal infrastructure (Rank 12):** Originally framed as "more AI datacenter infrastructure trade than photonics trade." Under AI datacenter scope expansion, this is a primary chokepoint, not adjacent infrastructure. VRT clearest pure-play (NVIDIA partnership reciprocally confirmed at Tier 1 per vault Session 22; EcoDataCenter Sweden Vera Rubin deployment; 800V DC programs H2 2026). MOD + Schneider broaden infrastructure exposure but with less photonics-specific positioning. FLEX (JetCool acquisition) as Session 36+ ingest candidate.

**Board/package power delivery (Rank 13):** System-density bottleneck rather than optical-component bottleneck. MPWR is a high-quality power-management exposure; VICR is more direct to high-density power architecture but more volatile; IFNNY adds broad power-semiconductor exposure including GaN/SiC.

### Energy/Power chokepoints (AI datacenter scope expansion)

**Grid energy capacity + interconnection queues (Rank 1 Energy/Power):** US data center IT load projected to double from 80GW (2025) to 150GW (2028) per Bloom Energy 2026 Data Center Power Report. Northern Virginia interconnection queues stretch multi-year; Texas emerging as largest US datacenter market with 40GW+ by 2028. Power availability is now the primary bottleneck for new datacenter construction. Investment exposure is genuinely difficult here — most direct beneficiaries are utility companies with regulated rate structures (limited upside even when load grows). The cleaner exposure is via the equipment suppliers that utilities must buy from to expand capacity. Nuclear restart beneficiaries (CEG / VST / NRG) offer adjacent exposure but with significant regulatory and execution risk.

**Power transformers + GOES steel (Rank 2 Energy/Power — TIGHTEST CURRENT BOTTLENECK):** Transformer lead times 120 weeks (2.3 years) standard; large units 210 weeks (4 years). 80% historically imported (Mexico/China/Thailand); Cleveland-Cliffs sole US grain-oriented electrical steel (GOES) producer. ~50% of planned 2026 US datacenter builds delayed/cancelled per Bloomberg/Sightline Climate. China controls ~60% global production capacity (TBEA, China XD Group); US export restrictions on Chinese transformers escalating. **The cleanest US-listed exposure is ETN** — diversified electrical equipment platform with direct transformer exposure and US manufacturing footprint; positioned to benefit from "made-here" policy tailwinds. **ABB** (Swiss; ABB ADR) and **Schneider Electric** (French; SBGSF ADR) are the European incumbents with broader product portfolios including transformers, switchgear, and grid automation. **Korean expansion plays** (HD Hyundai Electric; Hyosung Heavy Industries) offer high-beta exposure to US datacenter transformer demand — Hyosung Memphis plant doubling capacity to 250+ units by 2027; HD Hyundai Alabama expansion ~$270M+ targeting ultra-high-capacity datacenter units; both have order books filled through 2027. **Cleveland-Cliffs (CLF)** offers narrow GOES steel exposure but the broader steel business muddies the thesis. **Prysmian (PRYMF) / Nexans / NKT** add HV cable adjacency. **Powell Industries (POWL)** offers smaller-cap medium-voltage switchgear exposure with structural pricing power.

This is the chokepoint where the binding constraint observation is most directly investible. The 4-year transformer lead time means pricing power persists structurally — orders placed today don't deliver until 2030 in some cases; suppliers can extract premium pricing on the existing order book without expanding capacity faster than demand.

**High-density power delivery (Rank 3 Energy/Power):** Rack densities transitioning from 5-15kW (traditional) to 100-240kW (AI training clusters); 800V DC architecture transition (VRT canonical H2 2026 program). VRT remains the canonical thermal + power infrastructure pure-play with NVIDIA reciprocal-confirmation; MPWR offers high-quality power-management semiconductor exposure with stable end-market diversification; VICR offers more direct exposure to high-density power architecture but trades with higher volatility and execution risk; IFNNY (Infineon ADR) offers broad power-semi exposure including GaN/SiC for the underlying semiconductor transition. The 800V DC transition is structurally significant — every new AI cluster deployment increasingly defaults to 800V DC, displacing legacy 480V architectures.

**Backup power + UPS + on-site generation (Rank 4 Energy/Power):** Hyperscaler shift toward on-site generation due to grid constraints (Microsoft UAE $15.2B power-rich expansion; nuclear restart commitments). VRT captures UPS dominance; CAT (Caterpillar) and CMI (Cummins) capture diesel and gas genset demand at hyperscale; GNRC (Generac) is smaller-scale exposure. The on-site generation theme intersects with grid constraint observation — hyperscalers are increasingly self-generating to bypass grid interconnection queues. This benefits genset suppliers + the natural gas turbine supply chain (GE Vernova; Mitsubishi Heavy Industries).

**Switchgear + cables + busways (Rank 5 Energy/Power):** Long lead times + qualification cycles create pricing power, though less concentrated than transformers. ABB / ETN / Schneider already cited above; Prysmian (PRYMF) is Italian-listed with US ADR — direct HV cable exposure; Nexans + NKT are smaller European cable plays; Powell Industries (POWL) is US-listed medium-voltage switchgear with structural pricing power and AI datacenter tailwind. Less concentrated chokepoint than transformers but with similar pricing dynamics.

### Memory chokepoints (AI datacenter scope expansion)

**HBM oligopoly capacity (Rank 1 Memory):** Three-supplier oligopoly: SK Hynix 50-62% share, Samsung 17-35% share recovering, Micron 11-21% share. SK Hynix dominates as NVDA primary supplier (~90% NVDA HBM). HBM3E shipping (~$300/stack); HBM4 entering mass production 2026 (~$500/stack estimated). 16-Hi HBM stacks (HBM4 advanced) requested by NVDA Q4 2026 — technical challenge "formidable" per industry. **HBM consumed 23% of DRAM wafers Q4 2025; "3-to-1 rule" — every AI chip destroys capacity to make 3 normal PC chips.** Capacity sold out through 2026 across all three suppliers. HBM TAM projected $35B (2025) → $100B (2028) per Introl.

**MU (Micron) is the only US-listed direct exposure** to HBM oligopoly — captures 11-21% market share with capacity expansion ramp; benefits from broader DRAM pricing power from HBM cannibalization (HBM consumes wafer capacity disproportionately to bits produced); HBM4 ramp positioning improving. The investment case for MU rests on three legs: (1) HBM share defense + expansion via HBM4 generation; (2) commodity DRAM pricing power from HBM cannibalization; (3) AI memory revenue mix shift improving margin profile from commodity DRAM exposure.

**Foreign-listed direct exposure** offers cleaner oligopoly access: Samsung Electronics (KRX 005930 or US OTC SSNLF) — 35%+ share rebuilding with HBM4 ramp; SK Hynix (KRX 000660 or US OTC HXSCL) — 50-62% share leader with NVDA primary supplier position. Both require IBKR foreign access — Vic to determine portfolio fit. Note that SSNLF + HXSCL OTC trading is thin with limited liquidity; KRX direct is the cleaner exposure but operationally heavier.

**DRAM scaling + commodity DRAM supply shock (Rank 2 Memory):** Samsung HBM4 ramp depleting commodity DDR5 capacity; memory prices rising; Meta extending server lifespans due to memory shortage per WSJ. Each HBM generation transition concentrates more wafer capacity in lower-bit-yield processes. The investment exposure overlaps with HBM oligopoly (same three suppliers); shorter-cycle DRAM ASP appreciation benefits MU + foreign-listed names disproportionately to longer-cycle HBM contract pricing. This is a 2026-2027 thesis specifically — by 2028, HBM5 generational transition may extend supply tightness even further per Samsung HBM4 dynamic.

**NAND + SSD storage (Rank 3 Memory):** AI training/inference creates persistent storage demand; NAND oligopoly has more participants than HBM. Investment exposure: WDC (Western Digital) — SanDisk separation creates clean NAND exposure; STX (Seagate) — primarily HDD with NAND adjacency; MU NAND business adds to memory thesis; foreign-listed Samsung/SK Hynix/Kioxia. Less concentrated chokepoint than HBM with weaker pricing power dynamics; AI tailwind is real but secondary to HBM thesis.

### Equipment chokepoints (semi capex driving AI datacenter manufacturing)

**EUV lithography (Rank 1 Equipment; cross-domain anchor):** ASML EUV monopoly canonical; High-NA EUV emergence creates secondary monopoly cycle. AI compute scaling drives advanced node demand at TSMC/Samsung/Intel — each node transition (3nm → 2nm → A14) requires more EUV layers, more advanced tooling. **ASML (foreign-listed; ADR available)** is the only public exposure. Limited US-listed alternatives — the closest US-listed competitors (AMAT, LRCX, KLAC) operate in adjacent semi equipment markets but don't directly compete on lithography. ASML is structurally the cleanest single-name AI datacenter equipment thesis play.

**Advanced packaging metrology (Rank 2 Equipment):** ONTO is canonical holding with AI advanced packaging exposure (CoWoS/COUPE-adjacent revenue). KLAC (KLA Corp) offers broader semi metrology + inspection exposure — not a pure-play on advanced packaging but with structural AI tailwind. KLA's positioning is broader than ONTO's; ONTO captures more pure-play exposure to advanced packaging-specific revenue but with smaller diversification.

**Wafer test + burn-in (Rank 3 Equipment):** AEHR is canonical holding; single-public-pure-play in wafer-level burn-in. Adjacent test equipment exposure via TER (Teradyne) — broader semi test platform with AI tailwind but diluted exposure; FormFactor (FORM) — wafer prober exposure adjacent to AEHR's burn-in positioning.

**Optical + electrical test equipment (Rank 4 Equipment):** KEYS (Keysight) is the largest US-listed optical/electrical test equipment platform — captures 1.6T validation cycle exposure with broader portfolio diversification reducing AI-pure exposure; VIAV is canonical holding (Session 28); Spirent acquisition extending KEYS positioning. Anritsu (foreign-listed Japanese; Tokyo: 6754) offers parallel exposure but with foreign access friction.

**Etch + deposition (broader semi capex; Rank 5 Equipment):** AMAT (Applied Materials) and LRCX (Lam Research) are the canonical broad-cycle semi equipment plays. Cyclical exposure with AI tailwind but not chokepoint plays in the structural sense — meaningful AI datacenter exposure but with significant non-AI cyclical risk. Lower priority than concentrated chokepoint exposures but worth tracking for cyclical positioning.

### Materials chokepoints (provisional)

**GOES steel for transformers (Rank 1 Materials):** Cleveland-Cliffs sole US producer; 80% transformer imports historically; Cleveland-Cliffs received $500M Biden-era grant for electrical steel plant upgrade (subsequently partially cancelled by Trump administration). **CLF (Cleveland-Cliffs)** offers narrow exposure but broader steel business muddies the thesis — not a clean chokepoint play in the equity sense. The structural insight is that GOES steel is the binding upstream constraint on transformer manufacturing; the investment translation is via transformer suppliers (ETN / ABB / Schneider) rather than direct CLF exposure.

**Specialty gases (semi manufacturing; Rank 2 Materials):** Air Products (APD) and Linde (LIN) are the diversified specialty gas leaders with semiconductor exposure as one of multiple end markets. Cyclical-with-secular-AI-tailwind framing; not chokepoint pure-play. Smaller specialty plays exist (Versum acquired by Merck KGaA; Mitsubishi Chemical) but require foreign access.

**Rare earths + magnets (Rank 3 Materials):** Chinese export concentration is severe (China controls ~85-90% rare earth processing). MP Materials (MP) is the US-listed reshoring play — Mountain Pass mine + downstream processing buildout. Critical for power semiconductor magnets, motors, and many datacenter components. The investment case is structurally compelling but execution risk significant — MP has thin operating history and is funding capacity expansion through dilution and government grants. Geopolitical tail risk both upside (export restrictions favor MP) and downside (Chinese supply normalization weakens thesis).

**Copper (Rank 4 Materials):** Long-cycle supply constraint affecting datacenter cabling at scale. FCX (Freeport-McMoRan) is the largest US-listed copper miner; SCCO (Southern Copper) adds Latin American exposure. Copper is broad-cycle with AI tailwind but not a chokepoint play in the structural sense — diversified end-market exposure (EVs; grid; construction) means AI datacenter is one driver among many.

**Substrate supply (canonical at InP-supply.md photonics; Rank 5 Materials):** Silicon wafers via SUMCO (Japanese; 3436.T) and Shin-Etsu Chemical (Japanese; 4063.T); HBM substrates via Ibiden (Japanese; 4062.T); InP substrates via AXTI (canonical InP-supply chokepoint) + Sumitomo + JX Advanced Metals. Substrate supply is foreign-listed dominant — limited US-listed exposure beyond AXTI's narrow InP positioning.

### Compute chokepoints

**AI accelerator architecture (Rank 1 Compute):** NVDA Blackwell B200/B300 ramping; Vera Rubin 2026; Kyber CPO scale-up. AMD MI300/MI350/MI400 series with uncertain share trajectory. Custom ASIC programs reshaping landscape: Amazon Trainium2/3/4 ($225B revenue commitments); Google TPU (AVGO partnership); Microsoft Maia ("30% improved tokens per dollar" framing). **NVDA remains the canonical full control point** with platform integration vertical securing across component layers; share defense via ecosystem lock-in (CUDA; NVLink; Mellanox; equity stakes at LITE/COHR/Ayar Labs/CoreWeave/etc.). **AMD is the merchant alternative** but execution gap to NVDA remains material — MI300 generation underperformed expectations; MI400 generation positioning improving but enterprise adoption lagging. **AVGO captures custom ASIC tailwind** as the dominant Google TPU partner and emerging custom silicon platform; MRVL captures Microsoft custom ASIC partnership. Custom silicon trajectory is the key falsification candidate for NVDA share defense thesis — track NVDA share in hyperscaler new deployments quarterly.

**CPU architecture for AI workloads (Rank 2 Compute):** AI workloads are increasingly GPU-centric, but CPU architecture remains relevant for orchestration, data preparation, and inference at scale. AMD EPYC has gained meaningful share from Intel in datacenter CPU; Intel datacenter recovery uncertain; ARM-based hyperscaler custom (Amazon Graviton; Microsoft Cobalt; Google Axion) shifting volume away from x86. **AMD remains the merchant CPU growth play** with structural share-take story; **INTC offers turnaround optionality** but execution credibility weak; **ARM Holdings (ARM)** captures royalty exposure to ARM-based hyperscaler custom but with high valuation and uncertain royalty rate trajectory.

**Switch ASIC / platform architecture (Rank 7 photonics framework; preserved):** Per Framework 2.6 control-point gradation. Detailed analysis in photonics chokepoint baseline above.

**Networking ASIC (broader than switch):** AVGO Tomahawk dominance + Photonic Fabric extension; MRVL Photonic Fabric; emerging custom ASIC programs at hyperscalers. Investment positioning overlaps with Switch ASIC but extends to interconnect (NVLink; UALink; Ethernet evolution). NVDA platform integration via NVLink / Mellanox InfiniBand acquisition captures merchant networking share asymmetrically.

### Cross-chokepoint themes

**Existing photonics-anchored themes (preserved from prior _thesis.md):**

- **Hyperscaler customer concentration as structural risk.** AAOI Microsoft ~43%; LITE+COHR NVDA $2B equity each (March 2026); CRDO Customer A 67%→48% broadening; MRVL custom warrants for two major hyperscaler programs; AVGO Anthropic-as-Google-TPU-derivative observation per Hock Tan Freudian slip; SK Hynix NVDA ~90%. Concentration is cross-chokepoint pattern, not per-row risk. Position sizing should account for shared hyperscaler exposure across multiple holdings.

- **NVDA platform integration vertical securing.** Six modalities (Mellanox acquisition, Groq licensing, COHR/LITE equity-plus-purchase, Ayar Labs equity backing, GLW counterparty-attribution-only, VRT reciprocal-confirmation) operationalize NVDA's full control point across component chokepoints. Affects laser supply (Rank 1), advanced packaging (Rank 5), fiber/connectors (Rank 11), thermal (Rank 12), and Switch ASIC chokepoint (Rank 7) directly. NVDA exposure provides indirect exposure to all NVDA-aligned component layers.

- **Layer 3 four-variant CPO profile (vault Session 28 codification).** MRVL escalating disclosure / ALAB phased coexistence / CSCO acknowledged deferral / CRDO displacement positioning — four structurally distinct positions at same Framework 2 layer. CRDO uniquely positions AGAINST CPO via Hyperlume MicroLED + OmniConnect MicroLED-based "near package optics" — alternative architecture bet. Position sizing should consider whether thesis bets on CPO adoption (MRVL/NVDA path) or CPO displacement (CRDO path) — exposure pattern is asymmetric across these scenarios.

- **Outside Framework 5 placements (CLAUDE.md v8.1 codification).** COHU + PLAB are placed Outside Framework 5 per honest-verdict discipline canonical examples — broad-cycle semi exposure with AI as minority subsegment driver, not photonics-thesis-direct. These holdings serve as analytical reference / counterpoint role rather than thesis centrality.

**Multi-domain expanded themes (NEW):**

- **Hyperscaler CAPEX flow asymmetry across domains.** Compute captures ~50-65% CAPEX share; networking + memory + power follow at ~10-15% each; equipment + materials + thermal cooling at ~5-10% each. Investment positioning across domains per CAPEX flow + concentration interaction. Compute exposure (NVDA + custom ASIC plays) captures dollar volume; chokepoint exposure (HBM + transformers + COUPE) captures pricing power. The dollar-volume-vs-pricing-power asymmetry matters for risk-adjusted positioning — NVDA captures the largest CAPEX flow share but at increasingly competitive pricing dynamics; HBM and transformer suppliers capture smaller absolute flow but with structural pricing power that's less reflected in market valuations.

- **Power constraint as binding ceiling on CAPEX deployment.** Money is not the bottleneck — $650B+ committed CAPEX exceeds deployable infrastructure. Transformer 4-year lead times mean compute CAPEX cannot deploy faster than power infrastructure expansion. This creates persistent constraint on Tier 1 (NVDA / AMD) revenue trajectory while power infrastructure suppliers (ETN / VRT / ABB / Schneider / HD Hyundai / Hyosung) capture pricing power. Under-allocating to power infrastructure exposure may understate structural pricing power as constraint binds. Power chokepoint exposure may outperform compute exposure on risk-adjusted basis 2026-2028 if constraint persists.

- **Cross-domain chokepoint dependencies.** Photonics chokepoints depend on power chokepoints (laser thermal management); compute chokepoints depend on memory chokepoints (HBM-compute interface); power chokepoints depend on materials chokepoints (rare earths; SiC; GaN; GOES steel). Cross-domain dependency maps as analytical lens — single-chokepoint thesis bets miss dependency-chain exposure. Dual-chokepoint exposure (compute + memory; or compute + power) captures dependency dynamics that single-chokepoint exposure cannot.

- **Custom silicon vs merchant compute disruption.** Hyperscaler custom silicon programs shifting compute CAPEX flow away from merchant Layer 1 (NVDA) toward Layer 3 designers (AVGO custom; MRVL custom) + Layer 2 manufacturing (TSM benefits regardless of merchant vs custom share). NVDA share defense via platform integration (Mellanox + ecosystem); custom silicon share gain via Trainium ($225B commitments); Google TPU (AVGO); Microsoft Maia (now production). Trajectory + share dynamics matter for NVDA position thesis. The cleanest hedge against NVDA custom-silicon erosion risk is **TSM exposure** — captures manufacturing share regardless of merchant vs custom outcome.

- **HBM cannibalization of commodity DRAM.** HBM3E to HBM4 transition increases dies-per-stack from 12 to 16 (33% more DRAM dies per AI accelerator); Samsung HBM4 ramp depleting commodity DDR5 capacity. AI compute scaling structurally tightens broader memory market — affects every server class, not just AI. Investment implication: memory exposure (MU + Samsung + SK Hynix) captures broader pricing power than HBM-specific revenue would suggest. The "3-to-1 rule" makes memory exposure structurally more attractive than headline HBM TAM growth would imply.

- **Energy/Power constraint as compute scaling ceiling.** Grid + power infrastructure may bound AI compute scaling at hyperscaler scale before compute-tier supply constraints bind. Energy/Power chokepoint as macro-thesis-level constraint vs micro-thesis component. Strategic implication: if CAPEX deployment trajectory diverges from CAPEX commitment trajectory due to power constraints, Tier 1 (NVDA) revenue may underperform commitment-implied trajectory while power infrastructure suppliers outperform. This is the most structurally significant observation in this rework — it reframes the entire investment thesis from "ride the AI compute boom via NVDA + photonics" to "ride the AI datacenter buildout via dual-anchor compute + power infrastructure exposure."

- **Geopolitical risk concentration at multiple chokepoints.** Taiwan (TSM dependency); China (rare earths; transformers; substrates); Korea (memory; transformers). Single-jurisdiction chokepoint concentration risk across multiple critical supply chain layers. Diversification challenge: alternative geographies often have parallel concentration risks rather than diversification benefits. The structural reality is that the AI datacenter supply chain is geographically concentrated at multiple critical points; portfolio construction should account for correlated geopolitical risk across photonics (Taiwan TSM), memory (Korea Samsung/SK Hynix), and power infrastructure (China transformers/rare earths) exposures.

## Evolution

This thesis will evolve as evidence accumulates and vault scope expands across AI datacenter supply chain domains. When I revise this file, I will note the change here. The LLM should treat whatever is in this file at read-time as the current anchor and flag when ingested sources suggest this file itself needs updating.

The most likely directions for thesis evolution:

- **Power infrastructure thesis maturation** — as ETN ingest (Session 37) and adjacent power infrastructure ingests proceed, the power chokepoint thesis will mature from research-backed scaffolding to vault-canonical analytical depth. Likely refinements to position sizing recommendations as primary-source evidence accumulates.

- **Memory expansion** — MU ingest (Session 38+) and potential foreign-issuer Samsung/SK Hynix consideration will mature memory chokepoint thesis. HBM4 ramp trajectory through 2026-2027 will resolve oligopoly pricing power durability question.

- **Custom silicon disruption** — quarterly tracking of NVDA share in hyperscaler new deployments vs custom ASIC programs (Trainium / TPU / Maia) will resolve the merchant vs custom share trajectory question. If custom silicon captures meaningful share faster than expected, NVDA thesis weakens; if NVDA share defends via platform integration, thesis strengthens.

- **CPO timing resolution** — Murphy bifurcation thesis (scale-up real / scale-out limited) vs NVDA Spectrum-X CPO production volume vs AVGO copper-scale-up persistence — three Layer 1 timing scenarios will resolve through 2026-2028. Photonics chokepoint thesis sensitivity to CPO timing remains material.

- **Geopolitical event-driven repositioning** — Taiwan crisis; China export controls; Korean memory disruption; energy crisis. Tail risks that could trigger material thesis revision rather than gradual evolution.

---

**Note on this rework (2026-04-30):** Comprehensive rework executed via collaborative chat drafting (Vic-directed; agent-scaffolded with research backing) per CLAUDE.md v8.1 _thesis.md ownership convention exception (one-time Vic-authorized rework session; resumed default for future sessions). Scope expanded from "AI compute supply chain — photonics primary" framing to "AI datacenter supply chain — compute, photonics, memory, energy, power, equipment, materials, and more." Hyperscaler CAPEX flow analysis section added with research-backed 2026 figures (Microsoft FY2026 $190B+; Alphabet 2026 $180-190B; Amazon 2026 ~$200B; Meta 2026 $125-145B). Multi-domain chokepoint expansion delivered (Energy/Power; Memory; Equipment; Materials; Compute) with full analytical positioning per chokepoint. Photonics chokepoint baseline preserved verbatim. Key structural observation: power infrastructure has displaced compute as the binding 2026 constraint (50% of planned 2026 US datacenter builds delayed/cancelled per Bloomberg/Sightline Climate; transformer lead times 120-210 weeks). Investment thesis reframed from photonics-thesis-anchored to dual-anchor (compute + power infrastructure) AI datacenter supply chain exposure with multi-domain diversification.

**Note on the 2026-06-25 targeted edit (Vic-authorized, S175):** Two scoped changes — authorized by Vic, not a full rework; default human-ownership otherwise resumes. (1) **Added** the *Demand-side metrics — how the buildout's output is judged* section (value-per-GW / tokens-per-watt / tokens-per-dollar / memory-bandwidth-per-flop / the MW funnel) — the CS153 "AI factory" Tier-3 lens, the clearest demand/output-side gap in this otherwise supply-side thesis; speaker-attributed detail + cross-walk at `wiki/themes/ai-frontier-systems.md`. (2) **Refreshed** the 2026 hyperscaler-capex figure: the Big-4 ~$640-720B is unchanged but is now primary-sourced (was NVDA's analyst estimate), extends toward ~$700-770B with Oracle, reconciles with the ~$725B analyst/web aggregation and TrendForce's ~$830B top-nine global figure (Tier-3), and now points to the canonical `wiki/trackers/hyperscaler-capex.md` tracker; the per-row table is left as a dated April-2026 snapshot. No other content changed.