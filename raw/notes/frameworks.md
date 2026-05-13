# Frameworks — AI Datacenter Supply Chain & Chokepoint Analysis

> **Status (v10.1):** Working analytical framework expanded from photonics-primary to AI datacenter supply chain scope; v10.1 refinement applies full structural alignment with _thesis.md (3 critical fixes + 4 significant gaps + 3 lesser refinements per Option C alignment).
> **Purpose:** Calibrate the LLM's initial categorization of companies before primary sources refine the specifics.
> **Epistemic note:** The frameworks here are *interpretive scaffolding*, not facts extractable from filings. They represent how I think about this space. Primary sources should *enrich* these frameworks, not override them. Specific company placements may shift as evidence accumulates — the frameworks themselves are the stable part.

---

## Framework 1: Supply chain flow

How the AI datacenter gets physically built. Multi-domain view across photonics, memory, compute, energy/power, equipment, and materials.

### 1.1 Photonics supply chain (canonical from Sessions 1-32)

How an AI photonic system gets physically built. Read top to bottom — each layer depends on the layer above.

```
┌─────────────────────────────────────────┐
│         RAW MATERIALS & INPUTS          │
│  Silicon wafers (Shin-Etsu, SUMCO)      │
│  III-V substrates (InP, GaAs)           │
│  Specialty gases (Air Liquide, Linde)   │
│  Exotic materials (TFLN, lithium niobate)│
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         MANUFACTURING EQUIPMENT         │
│  Lithography: ASML (EUV monopoly)       │
│  Deposition/etch: AMAT, LRCX            │
│  Metrology: KLAC, ONTO                  │
│  Test: AEHR, COHU                       │
│  Epi reactors: VECO, Aixtron            │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│      FOUNDRIES & ADVANCED PACKAGING     │
│  Leading-edge logic: TSMC, Samsung      │
│  Specialty / photonics: GlobalFoundries │
│  Advanced packaging — TSMC platforms    │
│    at different maturity stages:        │
│    • CoWoS — exists today, HBM stacking │
│    • CoPoS — next-gen packaging format  │
│      (larger substrates, pilot line)    │
│    • COUPE — silicon photonics engine   │
│      (NVDA in production; TSMC silent)  │
│  Secondary packaging: ASE, Amkor        │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         PIC COMPONENT DESIGNERS         │
│  Silicon photonics PICs: in-house       │
│    (NVDA, AVGO, MRVL), Ayar Labs,       │
│    Lightmatter                          │
│  Specialty modulators: HyperLight (TFLN)│
│  Lasers (III-V): COHR, LITE, Scintil    │
│  Optical DSPs: MRVL, AVGO, CRDO         │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│      OPTICAL ENGINE INTEGRATION         │
│  Co-packaged optics: NVDA, AVGO         │
│    (advanced photonic engines)          │
│  Pluggable optical modules:             │
│    AAOI, Innolight, Eoptolink           │
│  Contract manufacturing: FN, FLEX       │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         SYSTEM INTEGRATION              │
│  Switch systems: ANET, CSCO, NVDA       │
│  AI servers: DELL, HPE, Foxconn         │
└─────────────────────────────────────────┘
```

**Timeline validation status (canonical post-Session-5):** CPO can proceed at component layer (LITE/COHR scaling now) on non-COUPE packaging approaches. COUPE-specific packaging timing is uncertain; TSMC remains silent in primary sources. Distinguish two CPO tracks when reasoning about timelines: component-layer deployment (validated 2026-2028 window) from COUPE-specific packaging timing (uncertain).

### 1.2 Memory supply chain

How HBM and DRAM are produced for AI accelerators. Same layered structure but distinct chokepoints.

```
┌─────────────────────────────────────────┐
│         RAW MATERIALS & INPUTS          │
│  Silicon wafers (Shin-Etsu, SUMCO)      │
│  Specialty substrates (Ibiden HBM)      │
│  Specialty gases                        │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         MANUFACTURING EQUIPMENT         │
│  Lithography: ASML (EUV)                │
│  HBM-specific tooling: AMAT, LRCX       │
│  TSV equipment: Disco, Lasertec         │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│      MEMORY OLIGOPOLY (THREE-SUPPLIER)  │
│  SK Hynix (50-62% HBM share;            │
│    NVDA primary supplier ~90%)          │
│  Samsung Electronics                    │
│    (17-35% share recovering)            │
│  Micron Technology                      │
│    (11-21% share; only US-listed)       │
│                                         │
│  HBM3E shipping (~$300/stack)           │
│  HBM4 mass production 2026 (~$500)      │
│  HBM consumed 23% DRAM wafers Q4 2025   │
│  "3-to-1 rule": each AI chip destroys   │
│  capacity to make 3 normal PC chips     │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│      HBM-LOGIC INTEGRATION (TSMC)       │
│  CoWoS HBM stacking (canonical today)   │
│  HBM4 16-Hi stack integration           │
│  (technical challenge "formidable")     │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         AI ACCELERATOR INTEGRATION      │
│  NVDA (Blackwell, Rubin)                │
│  AMD (MI series)                        │
│  Custom ASIC (Trainium, TPU, Maia)      │
└─────────────────────────────────────────┘
```

**Memory chokepoint observation:** HBM oligopoly cannibalizes commodity DRAM (Samsung HBM4 ramp depleting commodity DDR5 capacity). Each HBM generation transition concentrates more wafer capacity in lower-bit-yield processes. AI compute scaling structurally tightens broader memory market — affects every server class, not just AI.

### 1.3 Energy/Power supply chain

How datacenter power infrastructure flows from grid to rack. **Now the binding constraint in 2026.**

```
┌─────────────────────────────────────────┐
│         RAW MATERIALS & INPUTS          │
│  GOES steel (Cleveland-Cliffs sole US)  │
│  Copper (FCX, SCCO)                     │
│  Rare earths + magnets (MP, Chinese)    │
│  SiC + GaN substrates                   │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         POWER GENERATION                │
│  Grid utilities (regulated)             │
│  Natural gas turbines (GE Vernova, MHI) │
│  Nuclear restart (CEG, VST, NRG)        │
│  Renewable + storage                    │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         GRID INFRASTRUCTURE             │
│  Transformers: ABB, ETN, Schneider,     │
│    HD Hyundai Electric, Hyosung         │
│    Heavy Industries                     │
│  HV cables: Prysmian, Nexans, NKT       │
│  Switchgear: ABB, ETN, Schneider, POWL  │
│  120-week lead times standard;          │
│  210 weeks for large units (4 years)    │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         DATACENTER POWER DELIVERY       │
│  Substations + transformers             │
│  UPS + backup: VRT, CAT, CMI, GNRC      │
│  800V DC architecture transition        │
│    (VRT canonical H2 2026 program)      │
│  High-density power management:         │
│    MPWR, VICR, IFNNY (GaN/SiC)          │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         RACK + AI ACCELERATOR POWER     │
│  Rack densities 100-240kW               │
│  (vs traditional 5-15kW)                │
│  Liquid cooling required at scale:      │
│    VRT, MOD, FLEX (JetCool), Schneider  │
└─────────────────────────────────────────┘
```

**Energy/Power chokepoint observation:** ~50% of planned 2026 US datacenter builds delayed/cancelled per Bloomberg/Sightline Climate due to power infrastructure shortages — not chip availability. Money is not the bottleneck — $650B+ committed CAPEX exceeds deployable infrastructure. Transformer 4-year lead times mean compute CAPEX cannot deploy faster than power infrastructure expansion.

### 1.4 Compute supply chain (GPU + CPU + custom ASIC)

How AI accelerators reach hyperscaler datacenters.

```
┌─────────────────────────────────────────┐
│         INPUTS (cross-domain)           │
│  Memory: HBM oligopoly (see 1.2)        │
│  Photonics: lasers, DSPs (see 1.1)      │
│  Power: package-level delivery (see 1.3)│
│  Substrates: silicon wafers, advanced   │
│    packaging substrates                 │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         SEMI EQUIPMENT                  │
│  Lithography: ASML (EUV monopoly)       │
│  Deposition/etch: AMAT, LRCX            │
│  Metrology: KLAC, ONTO                  │
│  Test/burn-in: AEHR, FormFactor, TER    │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         FOUNDRY (TSMC dominant)         │
│  Leading-edge logic (3nm, 2nm, A14)     │
│  Advanced packaging (CoWoS, COUPE)      │
│  Custom silicon manufacturing           │
│  (Trainium, TPU, Maia all at TSMC)      │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         AI ACCELERATOR DESIGN           │
│  Merchant GPU: NVDA (~70%+ share),      │
│    AMD (challenger, MI300/400)          │
│  Custom ASIC partners:                  │
│    AVGO (Google TPU), MRVL (Microsoft)  │
│  Hyperscaler custom (in-house design):  │
│    Amazon Trainium, Google TPU,         │
│    Microsoft Maia                       │
│  CPU: Intel datacenter, AMD EPYC,       │
│    ARM-based (Graviton, Cobalt, Axion)  │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         SYSTEM INTEGRATION              │
│  Hyperscaler-built clusters (Project    │
│    Rainier 500K Trainium2; Microsoft    │
│    Fairwater 2GW; Stargate)             │
│  AI server OEMs: DELL, HPE, Supermicro  │
│  Networking integration (see 1.1)       │
└─────────────────────────────────────────┘
```

**Compute chokepoint observation:** Custom silicon programs shifting compute CAPEX flow away from merchant Layer 1 (NVDA) toward Layer 3 designers (AVGO custom; MRVL custom) + Layer 2 manufacturing (TSM benefits regardless). Trainium $225B revenue commitments + OpenAI 2GW + Anthropic 5GW commitments are early signals of custom silicon share gain. NVDA share defense via platform integration (Mellanox + ecosystem). The cleanest hedge against NVDA custom-silicon erosion risk is **TSM exposure** — captures manufacturing share regardless of merchant vs custom outcome.

### 1.5 Equipment supply chain (semi capex driving AI manufacturing)

Same equipment supplies all four domains above. Listed separately for clarity.

```
┌─────────────────────────────────────────┐
│         LITHOGRAPHY (chokepoint)        │
│  ASML EUV monopoly + High-NA EUV        │
│  ramp; secondary monopoly cycle         │
│  Each node transition (3nm→2nm→A14)     │
│  requires more EUV layers               │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         METROLOGY + INSPECTION          │
│  KLAC (KLA Corp; broader semi)          │
│  ONTO (advanced packaging metrology;    │
│  CoWoS/COUPE-adjacent revenue)          │
│  Advanced packaging-specific exposure   │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         WAFER TEST + BURN-IN            │
│  AEHR (single-public-pure-play          │
│  wafer-level burn-in)                   │
│  TER (Teradyne; broader semi test)      │
│  FORM (FormFactor; wafer prober)        │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         OPTICAL + ELECTRICAL TEST       │
│  KEYS (Keysight; 1.6T validation)       │
│  VIAV (Spirent acquisition)             │
│  Anritsu (foreign-listed Japanese)      │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         ETCH + DEPOSITION               │
│  AMAT (Applied Materials)               │
│  LRCX (Lam Research)                    │
│  Cyclical with AI tailwind              │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│         EPITAXIAL REACTORS              │
│  VECO (MOCVD/MBE; canonical at          │
│  InP-supply.md photonics)               │
│  Aixtron (German MOCVD competitor)      │
└─────────────────────────────────────────┘
```

---

## Framework 2: Value capture layers (six tiers)

Not all positions in the supply chain capture equal value. Higher layers extract more economic rent per dollar of revenue. Tier indicates structural margin capture potential, not company quality.

```
┌──────────────────────────────────────────────────┐
│  LAYER 1: PLATFORM DEFINERS                      │
│  Architecture control                            │
│  NVDA — Spectrum-X / Quantum-X / Kyber           │
│         (TSMC advanced packaging;                │
│          COUPE in production GTC Mar 2026)       │
│  AVGO — Bailly CPO + Tomahawk + custom ASIC      │
│                                                  │
│  Moat: Ecosystem lock-in, software platform,     │
│        standards ownership                       │
│  Risk: Platform shifts, vertical integration,    │
│        antitrust, custom silicon disruption      │
└──────────────────────────────────────────────────┘
                       │
┌──────────────────────────────────────────────────┐
│  LAYER 2: IRREPLACEABLE INFRASTRUCTURE           │
│  Physical moat                                   │
│  TSM — foundry + CoWoS + COUPE                   │
│  ASML — EUV lithography monopoly                 │
│  SK Hynix / Samsung / MU — HBM oligopoly         │
│  DLR / EQIX — datacenter real estate             │
│  Grid utilities — regulated power infrastructure │
│                                                  │
│  Moat: Manufacturing scale, process complexity,  │
│        decade+ of accumulated expertise          │
│  Risk: Geopolitical, technological disruption,   │
│        capital intensity                         │
└──────────────────────────────────────────────────┘
                       │
┌──────────────────────────────────────────────────┐
│  LAYER 3: SPECIALIZED DESIGNERS                  │
│  Technical expertise                             │
│  MRVL — optical DSPs + Celestial Photonic Fabric │
│  ALAB — CXL + retimers + aiXscale photonics      │
│  CRDO — Cardinal DSPs + ZeroFlap + OmniConnect   │
│  AMAT / LRCX / KLAC — semi equipment             │
│  SNPS / CDNS — EDA software                      │
│  CSCO — Silicon One + Acacia                     │
│  Ayar Labs, Lightmatter (private)                │
│                                                  │
│  Moat: Technical expertise, customer integration,│
│        patent portfolios                         │
│  Risk: Platform definers going in-house,         │
│        commoditization, customer concentration   │
└──────────────────────────────────────────────────┘
                       │
┌──────────────────────────────────────────────────┐
│  LAYER 4: DIFFERENTIATED COMPONENTS              │
│  Process specialization                          │
│  COHR — lasers + transceivers + substrate        │
│  LITE — lasers + photonic components             │
│  HyperLight — TFLN modulators (private)          │
│  ETN — power infrastructure + electrical equip   │
│    (Layer 4-5 straddling — see Caveat #8)        │
│  MPWR — high-density power management            │
│  VICR — high-density power architecture          │
│  ABB / Schneider — electrical equipment (foreign)│
│  HD Hyundai / Hyosung — transformers (Korean)    │
│  PSTG / NTAP — AI-integrated storage             │
│                                                  │
│  Moat: Process expertise, qualification          │
│        barriers, specialty materials             │
│  Risk: Commoditization over time, volume         │
│        competition, cyclicality                  │
└──────────────────────────────────────────────────┘
                       │
┌──────────────────────────────────────────────────┐
│  LAYER 5: INTEGRATED SYSTEMS                     │
│  Commercial integration                          │
│  AAOI — datacenter transceivers                  │
│  ANET — switch systems                           │
│  VRT — UPS + thermal + power infrastructure      │
│         integrated datacenter solutions          │
│         (NVIDIA reciprocal-confirmation;         │
│          800V DC programs H2 2026)               │
│  DELL / HPE — AI servers                         │
│                                                  │
│  Moat: Customer relationships, integration       │
│        expertise, distribution                   │
│  Risk: Commoditization, customer concentration,  │
│        CPO displacement (for transceivers)       │
└──────────────────────────────────────────────────┘
                       │
┌──────────────────────────────────────────────────┐
│  LAYER 6: SCALE MANUFACTURING & MATERIALS        │
│  Operational efficiency / specialty production   │
│  Scale manufacturing:                            │
│    FN — optical contract manufacturing           │
│    FLEX — EMS + JetCool liquid cooling           │
│    CLS / Foxconn — AI server assembly            │
│  Substrate & materials manufacturing:            │
│    AXTI — InP/GaAs/Ge substrates (100% China     │
│    mfg, capacity-constrained, geographic         │
│    concentration)                                │
│    CLF — GOES steel (Cleveland-Cliffs;           │
│    sole US producer; transformer constraint)     │
│    MP — rare earths reshoring                    │
│                                                  │
│  Moat: Operational efficiency, scale advantages  │
│        (scale mfg); high barriers to entry,      │
│        capacity-constrained specialty production,│
│        geographic concentration (materials)      │
│  Risk: Pure cycle exposure, low differentiation  │
│        (scale mfg); geopolitical, export         │
│        controls, few competitors (materials)     │
└──────────────────────────────────────────────────┘
```

**Important caveats:**

1. Layer assignments reflect *current* positioning. Companies can move between layers (see "Active layer transitions" section below).

2. A company may sit at different layers in different domains. Example: Broadcom is Layer 1 in CPO platforms (Bailly) but also Layer 3 in switch silicon and Layer 2 in custom ASICs for hyperscalers. Don't force a single layer if the company genuinely spans multiple. **AVGO Layer 1 straddling tension (codified Session 15):** AVGO's Layer 1 classification rests on franchise breadth (networking platform dominance + VMware software platform at 93% GM), but semiconductor segment ~68% GAAP gross margin sits at the Layer 1-2 boundary (below NVDA's 75%). Custom ASIC economics carry Layer 3 characteristics — design-service, customer-owned tooling risk, no CUDA equivalent. Layer 1 maintained; tension flagged.

3. **Layer notation flexibility (Caveat #3; extended Session 46).** Companies that structurally operate at multiple layers may be notated with flexible layer scope rather than forced to single-value placement. Two notation patterns codified:

   **(a) Hyphenated dual-layer notation (existing pattern).** Adjacent layers; placement spans two sequential value-capture positions. Canonical example: AEHR + ONTO Layer 3-4 (advanced packaging metrology + test). They appear in Framework 1 at the Manufacturing Equipment tier (alongside AMAT, LRCX, KLAC) — that's supply chain position, which is a different axis than value capture layer. On the value capture axis, their advanced packaging metrology and test exposure places them at Layer 3-4: higher differentiation than Layer 6 scale manufacturing, specific AI-adjacent positioning, and margin profiles inconsistent with the Layer 6 characterization. Layer 6 is reserved for pure-cycle manufacturing with low differentiation (FN, CLS, Foxconn, FLEX).

   **(b) Comma-separated hybrid layer notation (codified Session 46 per Session 43 CCJ precedent).** Non-adjacent layers; company holds material exposure at structurally distinct value-capture positions. Frontmatter notation: `layer: 4` primary + dedicated subsection treatment for hybrid scope on company page (e.g., CCJ Layer 4 primary + Layer 2 hybrid via 49% Westinghouse equity in Brookfield JV; hybrid documented in dedicated Caveat #7 designated-IP moat subsection on company page).

   **Hybrid layer notation criteria:**
   (i) Company structurally operates at multiple layers (not just product-line breadth)
   (ii) Revenue mix supports hybrid framing (material revenue / equity carrying value at non-primary layer)
   (iii) Caveat #7 (designated-IP moat) or analogous structural framework supports non-primary layer placement
   (iv) Frontmatter `layer:` field retains primary-layer numerical value; subsection treatment carries hybrid scope on company page

   **Empirical motivation.** Session 43 CCJ established Layer 4 (uranium mining + Port Hope conversion) + Layer 2 hybrid (Westinghouse 49% equity → AP1000 + AP300 reactor design house designated-IP moat per Caveat #7) precedent. CCJ frontmatter `layer: 4`; Westinghouse Layer 2 hybrid documented in dedicated subsection.

4. **NVDA is "platform-integrated," not fully vertically integrated.** NVDA owns the platform layer (Spectrum-X, Quantum-X, CUDA software stack, ecosystem) but depends on TSMC's advanced packaging (CoWoS today, potentially COUPE for CPO) at the physical manufacturing layer. The same is true for AVGO's Bailly. The TSMC dependency is what makes TSM a Layer 2 chokepoint — even the Layer 1 platform definers can't route around it.

5. **COHR and LITE occupy the same Layer 4 tier but at different photonics_tier placements.** Both are Layer 4 in value capture framework terms (differentiated components). Their photonics-tier differentiation (COHR at photonics_tier 2, LITE at photonics_tier 3) reflects manufacturing and structural asymmetries that value-capture-layer assignment alone does not capture. See Framework 5 and the positioning judgments table.

6. **Energy/Power participants span Layer 4 through Layer 6.** Power infrastructure suppliers with differentiated component process expertise (transformer manufacturing, electrical equipment, high-density power semiconductors) sit at Layer 4 (ETN, MPWR, VICR, ABB, Schneider, HD Hyundai, Hyosung). Integrated datacenter solutions providers (UPS + thermal + power into commercial integration) sit at Layer 5 (VRT). Materials suppliers feeding upstream (GOES steel for transformers via CLF; rare earths for power magnets via MP) sit at Layer 6 with structural geographic concentration risk. Grid utilities (regulated rate structures) sit at Layer 2 — irreplaceable infrastructure but with regulated upside.

7. **Layer 2 designated-IP moat (Caveat #7; generalized Session 46).** HBM oligopoly participants sit at Layer 2 (irreplaceable infrastructure) due to three-supplier oligopoly with structural pricing power, capital intensity, and process complexity. SK Hynix / Samsung / Micron operate as canonical examples. The HBM tier framework refines further — see Framework 6. Caveat #7 generalizes from HBM oligopoly precedent to designated-IP moat scope at Layer 2.

   **Generalized Layer 2 designated-IP moat criteria:**

   (a) **Designated-IP scope.** Company holds licensed or owned IP that is structurally irreplaceable in its domain — reactor design house licensing (AP1000/AP300 designs); HBM process IP (oligopoly-locked); analogous patent + process know-how scope.

   (b) **Structural irreplaceability.** Customers cannot route around the IP without multi-year development + capital deployment + regulatory licensing barriers. NRC reactor type licensing (Westinghouse AP1000 4-year+ NRC review) is canonical example.

   (c) **Multi-decade asset-life framing.** Designed for 60-100 year operating lifecycles (reactor lifecycle); 20-30 year capital deployment cycles (HBM fab process). Long-duration IP moat distinct from short-cycle product moats.

   (d) **Reactor design house OR analogous IP-licensing structure.** Westinghouse-style designated-IP licensing (CCJ 49% equity holder) extends Caveat #7 from HBM oligopoly to broader designated-IP moat scope.

   **Canonical applications:**

   | # | Session | Company / Entity | Designated-IP scope |
   |---|---|---|---|
   | 1 | S1-2 | TSM | HBM advanced-packaging process IP (CoWoS); oligopoly-locked |
   | 2 | S43 | CCJ-Westinghouse | AP1000 + AP300 reactor design house; NRC licensing barrier; 60-100 year reactor lifecycle |

   **Application discipline.** Layer 2 generalization warrants confirmation that all four criteria met. Pure-component participation alone (e.g., merchant battery cell supplier; merchant DRAM producer) does not qualify for Layer 2 designated-IP moat generalization absent structural irreplaceability + designated-IP scope.

8. **NVDA Layer 1 share dynamics under custom silicon disruption.** NVDA Layer 1 classification is not at risk (CUDA + ecosystem lock-in remains structurally durable), but Layer 1 *share* faces structural pressure from hyperscaler custom silicon programs — Amazon Trainium ($225B revenue commitments; OpenAI 2GW + Anthropic 5GW commitments); Google TPU (AVGO partnership); Microsoft Maia (now in production). Custom silicon shifts compute CAPEX flow from merchant Layer 1 (NVDA) toward Layer 3 designers (AVGO custom; MRVL Microsoft custom) + Layer 2 manufacturing (TSM benefits regardless of merchant vs custom outcome). Track NVDA share in hyperscaler new deployments quarterly; trajectory is the resolving signal — falsifiable transition tracked in Framework 2.5 (NVDA Layer 1 share dynamics) below.

9. **Layer 4-5 straddling tension (Caveat #9; reinforced Session 46 with 7 canonical applications).** Companies operating at Layer 4 (differentiated components) with integrated-systems characteristics flag Layer 5 candidate framing but require revenue-mix evidence for upgrade. Layer 4 maintained as primary placement; Layer 5 capability flagged as upgrade trigger candidate pending primary-source ingest evidence on integrated solutions revenue mix vs component mix.

   **Seven canonical applications:**

   | # | Session | Company | Outcome |
   |---|---|---|---|
   | 1 | S9 | MRVL | Layer 3 maintained per revenue-mix-required upgrade discipline |
   | 2 | S14 | AAOI | Layer 5 maintained (component-supplier scope insufficient for Layer 6 demotion) |
   | 3 | S14 | ALAB | Layer 3 maintained pending aiXscale integrated-platform revenue mix evidence |
   | 4 | S37 | ETN | Layer 4 maintained per integrated solutions revenue mix evidence |
   | 5 | S40 | BE | Layer 4 maintained (Q1 2026 revenue mix 87% product / 12.3% non-product) |
   | 6 | S42 | BWXT | Layer 4 maintained (Q4/FY2025 backlog mix 77% government / 23% commercial) |
   | 7 | S45 | ENS | Layer 4 maintained (Q3 FY2026 segment mix Energy Systems 44.4% / Motive Power 38.4% / Specialty 17.1% / New Ventures <0.5%) |

   **Future Layer 5 upgrade triggers (pre-registered at Session 45 ENS):**

   1. Integrated-systems sub-segment within domain operating segment separately disclosed >30% of consolidated revenue
   2. Service revenue >30% of total consolidated revenue (or analogous integrated-deployment revenue stream)
   3. "Power-as-a-service" / equivalent go-to-market framing shift in management commentary
   4. Named end-customer integrated turnkey deployments cited as primary commercial structure
   5. Multi-year service / PPA / integrated-deployment revenue stream growth >50% YoY

   **Revenue-mix-required upgrade discipline.** Positioning evidence (M&A momentum; integrated-solutions framing in 10-K Item 1; segment-level integration scope) is insufficient for tier upgrade absent revenue-mix evidence meeting one or more triggers above.

---

## Framework 2.5: Active layer transitions to watch

Thesis evolution tracks movement between layers. Companies don't stay fixed — they try to move upward through acquisitions, product expansion, and ecosystem plays. Multiple active transitions worth watching:

**MRVL: Layer 3 → Layer 2 (via Celestial AI)**

Marvell completed the acquisition of Celestial AI on February 2, 2026 for approximately $3.25 billion. Pre-acquisition MRVL was a Layer 3 specialized designer (optical DSPs, networking silicon). Celestial's Photonic Fabric is a scale-up optical interconnect platform purpose-built for multi-rack AI deployments. Combined, MRVL is positioning itself as a connectivity platform player rather than a component supplier.

Whether this transition succeeds depends on: (1) whether the Photonic Fabric achieves hyperscaler design wins in 2026-2027, (2) whether MRVL can monetize the scale-up interconnect opportunity without being squeezed by NVDA/AVGO platforms, (3) integration execution.

**Falsifiable upgrade triggers (defined Session 9, codified Session 15).** Three conditions, all required for Layer 2 reclassification: (a) GAAP gross margins approaching 60%+ (currently 51.0%, FY2026); (b) Celestial/CPO revenue exceeding $500M annual (management targets $500M annualized run rate by Q4 FY2028); (c) custom ASIC mix shift demonstrably improving rather than diluting margins. None met as of FY2026. The trajectory is real — data center revenue 40% → 74% in two years, custom silicon doubled YoY, Celestial adds infrastructure-tier capability — but the classification remains Layer 3 until the triggers are met.

Watch for: design-win announcements, scale-up interconnect revenue disclosure, margin trajectory through FY2027-FY2028, commentary on NVLink Fusion participation.

**ALAB: Layer 3 → Layer 2 (via aiXscale Photonics)**

Astera Labs completed the acquisition of aiXscale Photonics on November 10, 2025. Pre-acquisition ALAB was a Layer 3 specialist in PCIe/CXL retimers and fabric switches. aiXscale brings fiber-chip coupling technology for optical interconnects. ALAB is explicitly positioning as a rack-scale connectivity platform rather than a retimer specialist.

Whether this transition succeeds depends on: (1) whether Scorpio X-Series achieves volume production with hyperscaler customers, (2) whether optical engine delivery in 2027-2028 is timely and cost-competitive, (3) whether copper-to-optical timing plays out in ALAB's favor (too fast risks retimer headwinds; too slow risks optics investment sitting idle).

Watch for: Scorpio X design-wins, optical engine roadmap specifics, commentary on LPO/NPO/CPO timing.

**AAOI: Layer 5 → Layer 4/5 straddling (in-house InP/GaAs laser fabrication)**

AAOI revenue is ~100% Layer 5 transceiver assembly, but in-house InP/GaAs laser manufacturing at Sugar Land, TX (MBE + MOCVD epitaxial growth) is a Layer 4 capability. The straddling is real — management plans to triple InP laser production by mid-2027 — but does not yet warrant a tier upgrade. Current laser production serves internal module integration, not merchant Layer 4 sales.

**Falsifiable upgrade triggers (codified Session 15):** Tier upgrade requires evidence laser capability has become commercially material — standalone Layer 4 merchant revenue OR named non-AAOI Layer 5 customer for Sugar Land laser supply. Layer 5 classification maintained with this tension noted.

**NVDA: Layer 1 share dynamics under custom silicon disruption (NEW; codified 2026-04-30 with thesis rework)**

NVDA Layer 1 classification is not at risk under any current evidence — CUDA software platform + NVLink + Spectrum-X / Quantum-X ecosystem lock-in remains structurally durable. But NVDA Layer 1 *share* faces structural pressure from hyperscaler custom silicon programs that redirect compute CAPEX flow:

- **Amazon Trainium:** $225B revenue commitments per Jassy Q1 2026; Trainium2 fully subscribed at 1.4M chips landed; 2.1M total AI chips landed past 12 months (>50% Trainium); OpenAI 2GW Trainium commitment ramping 2027; Anthropic 5GW Trainium commitment; Project Rainier 500K+ Trainium2 cluster
- **Google TPU:** AVGO custom partnership; multi-generation TPU roadmap; Hock Tan "Anthropic-as-Google-TPU-derivative" Freudian slip observation
- **Microsoft Maia:** Now in production at Iowa + Arizona datacenters per Q3 FY2026; MRVL custom partnership; "30% improved tokens per dollar" framing

**The transition framing:** Custom silicon shifts compute CAPEX flow from merchant Layer 1 (NVDA) toward Layer 3 designers (AVGO custom for Google; MRVL custom for Microsoft) + Layer 2 manufacturing (TSM benefits regardless of merchant vs custom share). Hyperscaler-captive silicon could save "tens of billions annually in capex" per Jassy.

**Falsifiable share-erosion triggers (NEW; defined 2026-04-30):** NVDA Layer 1 *share* meaningfully erodes if any of:
- (a) Custom silicon captures >30% of hyperscaler new AI accelerator deployments through 2027
- (b) Merchant GPU share at Big 4 hyperscalers (combined) drops below 60% in any quarter
- (c) Trainium / TPU / Maia volume run rate exceeds combined NVDA Big 4 unit shipments in any reporting period

If any trigger met, NVDA Layer 1 placement remains unchanged but **NVDA share defense thesis weakens materially**; AVGO + MRVL Layer 3 custom-ASIC trajectory strengthens; TSM Layer 2 thesis strengthens (custom silicon manufactured at TSMC regardless). Update relevant company pages + chokepoint analysis if triggers met.

Watch for: Quarterly NVDA share data in hyperscaler new deployments; AVGO + MRVL custom ASIC revenue disclosure; Trainium / TPU / Maia volume run rate; custom silicon performance benchmarks vs NVDA Blackwell B200/B300 + Vera Rubin.

**The thesis question:** Multiple Layer 3-5 companies are betting they can move up a layer through specialized capability investments. Historically, layer transitions of this kind succeed roughly half the time. Plus a layer-1 share dynamic — NVDA defending Layer 1 share against hyperscaler custom silicon. The wiki should track evidence for and against each transition and avoid assuming success.

---

## Framework 2.6: Control-point analysis (supplemental to value capture layers)

Layer placement (Framework 2 above) captures *where* in the value chain a company operates. Control-point analysis captures *whether* a company at a given layer shapes architectural decisions that determine where ecosystem value accrues. The two are complementary axes on the same value-capture question, not separate frameworks — but the distinction matters because some Layer 1 platform definers exhibit architectural authority well beyond their layer placement, while some Layer 3/5 specialized designers exhibit partial control-point characteristics that complicate pure-bottleneck positioning.

**Five-tier gradation, not binary classification:**

- **Full control point.** [[NVDA]] — CUDA, NVLink, Spectrum-X, Quantum-X define ecosystem direction; CPO/LPO/NPO transitions move on NVDA's roadmap. Strongest in vault.

- **Control point with bottleneck participation.** [[AVGO]] — Tomahawk switch architecture, custom ASIC programs, Bailly CPO platform decisions; complementary to Layer 1/3 straddling tension flagged in Caveat #2 above.

- **Bottleneck-tier with control-point aspirations.** [[MRVL]] + [[CRDO]] — MRVL: Photonic Fabric (via Celestial $3.25-5.5B) is genuine platform-tier ambition, but Layer 3→2 trajectory triggers (Framework 2.5) remain unmet. Aspiration is real, not yet realized. CRDO: vertically integrated system-level model + CPO displacement positioning via OmniConnect MicroLED + ZeroFlap optics; smaller operational scale than MRVL Photonic Fabric / Celestial; aspirations real (UALink/ESUN/Ethernet protocol participation; Blue Heron 200G/lane retimer purpose-built for scale-AI) at smaller realization scale.

- **Bottleneck participant with platform-tier ambition.** [[CSCO]] + [[ANET]] — CSCO: Silicon One + Acacia capability is real, but acknowledged-deferral CPO position reflects ambivalent platform-tier commitment. ANET: EOS + NetDL software platform + ESUN founding member + Ultra Ethernet Consortium 1.0 contributor; bounded by single merchant silicon vendor dependency (likely AVGO Tomahawk per ANET 10-K Risk Factors Summary disclosure); ZERO CPO mentions in 10-K + Q4 2025 call sample (distinct silence pattern from CSCO acknowledged-deferral).

- **Pure bottleneck participant.** All other vault companies — supply-side scarcity is real, architectural authority is not.

**Five-company analytical thread (six post-Session-27 with CRDO at MRVL tier).** [[NVDA]], [[AVGO]], [[MRVL]], [[CRDO]], [[CSCO]], [[ANET]] within vault — five-company control-point thread now in-vault complete via Session 27 ANET fifth-member completion + CRDO addition at MRVL tier (Session 27 codification). Per-company application documented in vault company page Thesis role sections.

**Cross-domain extension under AI datacenter scope.** Framework 2.6 control-point gradation applies across all domains, not photonics-specific. Power infrastructure participants (ETN, VRT) operate as bottleneck participants without architectural authority — the binding 2026 power constraint creates supply-side scarcity but not platform-shaping power. HBM oligopoly participants (SK Hynix, Samsung, MU) operate as bottleneck participants with limited architectural authority (oligopoly pricing power) but not full control-point characteristics. Custom silicon designers (AVGO Google TPU; MRVL Microsoft custom) capture partial control-point characteristics — designs are customer-owned but architecture decisions are co-developed.

**Empirical evidence base.** Analytical concept anchored on `raw/research/photonics-chokepoint-table.md` (Vic-team-authored chokepoint research framework, Tier 3 source; v2 refinement applied 2026-04-30 with Framework 2.6 control-point gradation as orthogonal axis section explicitly cross-referencing this framework subsection). Per-company application documented in [[NVDA]], [[AVGO]], [[MRVL]], [[CSCO]], [[ANET]], [[CRDO]] Thesis role sections. Control-point analysis is supplemental to layer placement, not a replacement — strategic positioning is best read by combining both axes.

---

## Framework 3: Dependency / relationship map

How dependencies flow among the key players across all AI datacenter supply chain domains. Multi-domain view emphasizing cross-cutting chokepoints.

```
                ┌─────────────────────────┐
                │   HYPERSCALERS          │
                │  MSFT (FY26 $190B+)     │
                │  AMZN (2026 ~$200B)     │
                │  GOOGL (2026 $180-190B) │
                │  META (2026 $125-145B)  │
                │  ORCL (Stargate $500B)  │
                │  Combined ~$640-720B    │
                └────────┬────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
  ┌──────────┐   ┌──────────────┐   ┌──────────────┐
  │ COMPUTE  │   │  POWER INFRA │   │  NETWORKING  │
  │ ~50-65%  │   │  ~10-15%     │   │  ~10-15%     │
  │ CAPEX    │   │  CAPEX       │   │  CAPEX       │
  └────┬─────┘   └──────┬───────┘   └──────┬───────┘
       │                │                  │
       ▼                ▼                  ▼
  ┌──────────┐   ┌──────────────┐   ┌──────────────┐
  │ NVDA     │   │ ETN / ABB    │   │ AVGO         │
  │ AMD      │   │ Schneider    │   │ MRVL         │
  │ Custom:  │   │ Korean trans │   │ ANET / CSCO  │
  │ Trainium │   │ POWL (gear)  │   │ + LITE/COHR  │
  │ TPU/Maia │   │ CAT (gen)    │   │ optics tier  │
  └────┬─────┘   │ VRT (UPS+    │   └──────┬───────┘
       │         │  thermal)    │          │
       │         └──────────────┘          │
       │    (commissions custom silicon)   │
       │    (allocates capacity from)      │
       ▼                                   │
  ┌─────────────────────────────────┐     │
  │   TSMC (foundry + packaging)    │     │
  │   CoWoS (existing) + COUPE      │◄────┘
  │   (NVDA in production today)    │
  │   ◄── ASML (EUV)                │
  │   ◄── AMAT / LRCX / KLAC        │
  │   ◄── Shin-Etsu / SUMCO (wafers)│
  │   ◄── Air Liquide (gases)       │
  └────────┬────────────────────────┘
           │
           ▼
  ┌─────────────────────────────────┐
  │ HBM OLIGOPOLY (3-supplier)      │
  │ SK Hynix (NVDA primary ~90%)    │
  │ Samsung Electronics             │
  │ Micron Technology               │
  │ HBM4 mass production 2026       │
  │ Capacity sold out through 2026  │
  └─────────────────────────────────┘

  COMPUTE DEPENDS ON: TSM packaging + HBM memory + LITE/COHR
                      lasers + ASML lithography
  POWER INFRA DEPENDS ON: Cleveland-Cliffs GOES steel +
                          Chinese transformers (60% global)
                          + rare earths (Chinese ~85-90%)
  NETWORKING DEPENDS ON: TSM packaging + NVDA platform
                          ecosystem + CRDO/MRVL DSPs

  COMPONENT-LAYER PHOTONICS:
  ┌─────────────────────────────────┐
  │   COHR (lasers) ◄─── NVDA $2B   │
  │   LITE (lasers) ◄─── NVDA $2B   │
  │   AAOI (transceivers + in-house │
  │   InP laser at Sugar Land)      │
  │   FN / FLEX (contract mfg)      │
  └─────────────────────────────────┘

  UPSTREAM — InP substrate supply:
  AXTI — sole Western-HQ InP substrate supplier
  (100% China mfg). InP substrates feed COHR,
  LITE, AAOI laser fabrication.

  PARALLEL — MRVL position (post-Celestial):
  MRVL supplies optical DSPs to essentially
  ALL transceiver makers (AAOI, Innolight, etc.)
  AND now owns Celestial's Photonic Fabric for
  scale-up XPU interconnect. Custom ASIC
  partnership with Microsoft.

  PARALLEL — ALAB position (post-aiXscale):
  ALAB pivoting from retimer specialist toward
  rack-scale connectivity platform.

  PARALLEL — CRDO position:
  CRDO Cardinal DSPs + ZeroFlap optics +
  OmniConnect MicroLED (via Hyperlume); CPO
  displacement architecture rather than CPO
  adoption.

  CROSS-DOMAIN DEPENDENCIES:
  — Photonics depends on Power (laser thermal)
  — Compute depends on Memory (HBM-compute interface)
  — Power depends on Materials (rare earths, GOES, SiC)
  — All depend on Geopolitics (Taiwan TSM; China
    transformers/rare earths; Korea memory)
```

**The structural reality:** TSMC sits at the center of the photonics + compute + memory dependency graph as the gating chokepoint. Power infrastructure is a parallel chokepoint that constrains CAPEX deployment regardless of TSMC capacity. Materials chokepoints (GOES steel; rare earths; InP substrates) are upstream constraints affecting multiple downstream layers. Geopolitical concentration at Taiwan / China / Korea creates correlated risk across multiple critical chokepoints simultaneously — diversification across geographies often produces parallel concentration risks rather than diversification benefits.

---

## Framework 4: Structural vs. cyclical AI exposure

Distinguishing companies whose AI datacenter exposure is product-specific and structurally durable vs companies with broad-cycle exposure where AI is one driver among many. Multi-domain assessment captures domain-specific structural durability vs cyclical risk.

### 4.1 Cross-domain summary classification

**Structural AI exposure (product-differentiated AI datacenter positioning):**
- NVDA, AVGO, TSM (Layer 1-2 platform/foundry definers)
- COHR, LITE (Layer 4 component suppliers; NVDA equity-aligned)
- ONTO, AEHR (Layer 3-4 advanced packaging metrology + test)
- VRT (Layer 5 thermal/power infrastructure; NVIDIA reciprocal-confirmation)
- MRVL, CRDO, ALAB (Layer 3 specialized designers with platform aspirations)
- SK Hynix, MU, Samsung (Layer 2 HBM oligopoly)
- ETN (Layer 4 power infrastructure; binding 2026 constraint exposure)

**Broad-cycle exposure (AI as one driver among many):**
- COHU (Layer 3 semi test handler; Outside Framework 5; broad semi cycle with automotive/analog drag)
- PLAB (Layer 4 photomask supplier; Outside Framework 5; broad semi infrastructure exposure with AI advanced packaging as sub-segment)
- AMAT, LRCX (Layer 3 broad semi equipment; cyclical with AI tailwind)
- FCX, SCCO (Layer 6 copper miners; long-cycle commodity)
- KLAC (Layer 3 broad semi metrology with AI exposure)

**Mixed (structurally tilted but with cyclical exposure):**
- AXTI (Layer 6 InP substrate; structural Western-HQ position + cyclical revenue)
- VECO (Layer 3-4 epi equipment; AI tailwind via InP-supply but Compound Semi 9% revenue)
- VIAV (Layer 4 optical test; structural data center mix + broader test cyclicality)
- FLEX (Layer 6 EMS; broad EMS exposure + JetCool liquid cooling AI datacenter tailwind)

### 4.2 Per-domain structural vs cyclical assessment

Different domains have different structural-cyclical character. Same company can be structural in one domain and cyclical in another.

**Photonics domain — structural for now, CPO timing risk.**
Structural durability rests on CPO adoption trajectory; component-layer (LITE/COHR) deployment validated 2026-2028; scale-up CPO platform battle (MRVL/NVDA/AVGO) genuinely uncertain. CPO displacement positioning (CRDO via OmniConnect MicroLED) creates asymmetric exposure. Cyclical risk: optical transceiver cycle dependent on hyperscaler refresh timing.

**Memory domain — structural oligopoly, cyclical pricing.**
HBM oligopoly (SK Hynix / Samsung / Micron) is structurally durable — three-supplier capital intensity creates pricing power. But memory pricing has cyclical character — DRAM/NAND historical cycles persist. AI-specific HBM is structural; broader DRAM/NAND is cyclical with AI tailwind. Memory exposure structurally strengthens via HBM cannibalization of commodity DRAM (HBM consumed 23% DRAM wafers Q4 2025; "3-to-1 rule").

**Energy/Power domain — structural binding constraint.**
Power infrastructure as the binding 2026 constraint is the most structurally durable thesis in the rework — transformer 4-year lead times mean structural pricing power persists for years regardless of CAPEX deceleration. ETN, ABB, Schneider, VRT, HD Hyundai, Hyosung capture this directly. Materials upstream (CLF GOES steel; MP rare earths) carry geopolitical exposure that's structural (Chinese concentration won't normalize quickly). Cyclical risk: power infrastructure spend has historically been long-cycle; AI may not match this pattern.

**Compute domain — structural platform + cyclical share dynamics.**
NVDA Layer 1 + TSM Layer 2 structurally durable for compute capture. AMD merchant alternative cyclically dependent on share trajectory. Custom silicon programs (Trainium / TPU / Maia) introduce structural share-redirection dynamic — see Framework 2.5 NVDA share dynamics transition. CPU domain (Intel / AMD / ARM-based hyperscaler custom) more cyclically sensitive than GPU.

**Equipment domain — ASML structural; broader equipment cyclical.**
ASML EUV monopoly is structural — secondary monopoly cycle as nodes transition (3nm → 2nm → A14). Advanced packaging metrology (ONTO) and test (AEHR) carry structural AI-specific exposure. Broader semi equipment (AMAT / LRCX / KLAC) is cyclical with AI tailwind. AI tailwind doesn't fully insulate from broader semi cycle.

**Materials domain — structural concentration, cyclical commodities.**
GOES steel (CLF), rare earths (MP), InP substrates (AXTI) carry structural concentration risk. Specialty gases (APD / LIN), copper (FCX / SCCO), silicon wafers (Shin-Etsu / SUMCO) are cyclical commodities with AI tailwind as one driver among many.

Company pages should be clear about which structural-cyclical assessment applies per domain. Multi-domain companies may carry different classifications across domains (e.g., TSM structural across photonics + memory + compute + equipment; KLAC structural for AI advanced packaging metrology but broader semi cyclical for general semiconductor end markets). Owning a position with broad-cycle exposure in an AI datacenter basket is legitimate, but it should not be categorized as "AI-specific exposure" when it isn't.

---

## Framework 5: Photonics exposure tier framework

A simpler five-tier view specifically for AI photonics exposure quality — useful for first-pass categorization of companies claiming photonics tailwind. This is the classification reflected in the `photonics_tier` frontmatter field on company pages. **Photonics-specific framework; complementary to Framework 6 (Memory tier), Framework 7 (Energy/Power tier), Framework 8 (Equipment tier) for non-photonics domain assessments.**

**Tier 1 — Structural chokepoints (highest quality exposure)**
Positions every CPO implementation must pass through, regardless of which platform wins.
- TSM (CoWoS + COUPE packaging chokepoint + leading-edge logic foundry)
- NVDA (broad AI platform owner, aggressively extending into photonics)

**Tier 2 — Irreplaceable infrastructure and chokepoint participants**
- ASML (EUV lithography monopoly)
- COHR (six-inch InP wafer monopoly claim, broader vertical integration spanning substrate → epitaxy → chip → module → system, 20+ year NVDA relationship, Materials segment intersegment role supplying COHR's own Networking segment). Session 5 placed COHR here rather than Tier 4 based on primary-source evidence of structural position closer to "chokepoint participant" than "differentiated supplier."
- Memory oligopoly (SK Hynix, Samsung, Micron) for HBM
- Specific datacenter real estate positions (DLR, EQIX)

**Tier 3 — Specialized designers and high-quality differentiated suppliers**
Real technical moats but more substitutable than Tier 2.
- LITE (three-inch InP industry-standard manufacturing, narrower product focus on components and transceivers, newer NVDA relationship framed as capital-offset-for-supply-assurance, coherent DSP exit confirming commitment to Layer 4 component focus). Session 5 confirmed Tier 3 placement rather than promoting to Tier 2; the differentiation from COHR reflects real structural asymmetry, not calibration.
- MRVL (post-Celestial, transitioning toward Layer 2)
- AXTI (sole Western-headquartered InP substrate supplier; photonics exposure through structural position in InP supply chain rather than product design)
- CRDO — Cardinal Optical PAM4 DSPs + HiWire AECs + PCIe retimers + 1.6T leadership positioning + ZeroFlap optics + ALCs (via Hyperlume MicroLED acquisition) + OmniConnect/Weaver gearbox; n-1 mature node cost advantage; vertically integrated system-level model claim; Layer 3 specialized designer at smaller operational scale than MRVL
- Semi equipment incumbents (AMAT, LRCX, KLAC)

**Tier 4 — Differentiated components and good indirect exposure**
Real but indirect — benefits from overall buildout, not a specific platform bet.
- ONTO (advanced packaging metrology)
- AEHR (advanced packaging test)
- ALAB (post-aiXscale, transitioning toward Layer 2; revised from Tier 3 — aiXscale $31.1M is a technology tuck-in with zero current optical revenue, not a platform-scale investment. Tier 4 reflects current state; trajectory toward Layer 2 tracked separately in Framework 2.5)
- VRT (thermal/power infrastructure with NVIDIA reciprocal-confirmation; first vault adjacent infrastructure placement Session 22)
- HyperLight (TFLN modulators, private)
- VECO — MOCVD/MBE deposition equipment; photonics fit weak (Compound Semiconductor 9% of revenue; InP-relevant MOCVD tools but CPO/photonics silent across all three sources)
- CSCO — Silicon One + Acacia coherent (1.6T OSFP, 800G LPO with Cisco silicon photonics technology); Acacia captive in Cisco products; CPO explicitly deferred ("not imminent")
- VIAV — finished-module optical test (Tier 3 framework Rank 6; medium-high conviction); first vault Chokepoint 6 baseline; Spirent acquisition $425M from Keysight; NSE data center mix 45% Q2 FY2026; multi-quarter visibility extension framing

**Tier 5 — Integrated systems**
AAOI, ANET. Real AI exposure but more commoditized, more customer-concentrated, and more exposed to long-term CPO displacement than the component layer above. ANET specifically: EOS + NetDL software platform + ESUN founding member + UEC 1.0 contributor; single merchant silicon vendor dependency (likely AVGO Tomahawk); ZERO CPO mentions in 10-K + Q4 2025 call sample (distinct silence pattern from CSCO acknowledged-deferral).

**Outside the framework**
- COHU — semi test handler, but broad cycle exposure not AI-specific. Legitimate semi equipment company, inefficient vehicle for an AI/photonics thesis specifically.
- PLAB — photomask supplier with broad semi infrastructure exposure; AI advanced packaging cited as growth driver but as broad signal not photonics-specific; ZERO photonic foundry customer disclosure across 3 primary sources; photomask demand is upstream of all advanced packaging including but not limited to photonic foundry production. Counterpoint role for honest-verdict canonical example pair (COHU + PLAB).

---

## Framework 6: Memory exposure tier framework

A complementary five-tier view for AI memory exposure quality. Operates parallel to Framework 5 (photonics tier) — applies the same Tier 1-5 + Outside structural assessment to memory-specific exposure. The classification reflected in the `memory_tier` frontmatter field on company pages (when applicable). **Pending Tier 3 framework source curation for canonical chokepoint analysis at multi-source threshold.**

**Memory chokepoint identification (preamble):** Three structural chokepoints define AI datacenter memory exposure: (1) HBM oligopoly capacity (three-supplier — SK Hynix 50-62% / Samsung 17-35% / Micron 11-21%) creating sustained pricing power; (2) HBM-logic integration via TSM CoWoS HBM stacking (HBM4 16-Hi technical challenge "formidable" per industry); (3) EUV lithography for HBM logic die manufacturing (ASML monopoly). HBM consumed 23% of DRAM wafers Q4 2025 ("3-to-1 rule" — every AI chip destroys capacity to make 3 normal PC chips); HBM TAM projected $35B (2025) → $100B (2028) per Introl. HBM4 entering mass production 2026 (~$500/stack estimated); capacity sold out through 2026 across all three suppliers.

**Tier 1 — Structural chokepoints (highest quality exposure)**
The companies that capture chokepoint pricing power directly.
- SK Hynix (HBM oligopoly leader; 50-62% market share; NVDA primary supplier ~90%; KRX-listed; HBM3E shipping with 12-stack production; HBM4 mass production preparation complete)
- Samsung Electronics (HBM oligopoly recovering; 17-35% share with HBM4 ramp; KRX-listed; broad memory + foundry diversification; "Samsung is back" customer signaling per CEO Jun Young-hyun)
- TSM (CoWoS HBM stacking; HBM4 16-Hi integration "formidable" technical challenge; canonical Memory tier 1 placement reflecting HBM-logic integration chokepoint)
- ASML (EUV lithography for HBM logic die manufacturing; cross-domain anchor)

**Tier 2 — Irreplaceable infrastructure and chokepoint participants**
- MU — only US-listed direct HBM oligopoly participant; 11-21% market share; HBM3E shipping 12-stack; HBM4 ramping 2026; commodity DRAM exit announced December 2025 (in favor of AI datacenter customers); broader DRAM pricing power benefit from HBM cannibalization

**Tier 3 — Specialized designers and high-quality differentiated suppliers**
- Ibiden (HBM substrate supplier; foreign-listed Japanese; Tokyo: 4062.T; specialty substrate process expertise)
- HBM-specific tooling vendors (Disco; Lasertec; foreign-listed; TSV / hybrid bonding equipment)

**Tier 4 — Differentiated components and indirect exposure**
- WDC (Western Digital; SanDisk separation creates clean NAND exposure)
- STX (Seagate; primarily HDD with NAND adjacency)
- Kioxia (foreign-listed NAND)

**Tier 5 — Integrated systems**
- Storage OEMs (PSTG, NTAP) — AI-integrated storage but at integrated systems layer, not memory chokepoint exposure

**Outside the framework**
- Companies with memory exposure as minor end market or unrelated to AI datacenter thesis

---

## Framework 7: Energy/Power exposure tier framework

A complementary five-tier view for AI datacenter Energy/Power exposure quality. **Cross-domain framing critical:** Per _thesis.md AI datacenter scope rework, **power infrastructure has displaced compute as the binding 2026 constraint** — ~50% of planned 2026 US datacenter builds delayed/cancelled per Bloomberg/Sightline Climate. This is not a parallel framework alongside Frameworks 5/6/8; Energy/Power constraint **bounds CAPEX deployment across all other domains**. When reasoning about deployment trajectory in Frameworks 5 (photonics), 6 (memory), and 1.4 (compute), account for Energy/Power as ceiling, not parallel — money is not the bottleneck; transformer 4-year lead times mean compute CAPEX cannot deploy faster than power infrastructure expansion. The classification reflected in the `energy_power_tier` frontmatter field on company pages (when applicable). **Pending Tier 3 framework source curation for canonical chokepoint analysis at multi-source threshold.**

**Energy/Power chokepoint identification (preamble):** The binding 2026 constraints are: (1) Power transformers (120-week lead times standard; 210 weeks / 4 years for large units) constrained by GOES steel supply (Cleveland-Cliffs sole US producer; 80% transformer imports historically from Mexico/China/Thailand; China controls ~60% global production capacity); (2) Grid energy capacity + interconnection queues (US datacenter IT load 80GW 2025 → 150GW 2028 projected; Northern Virginia multi-year interconnection delays; Texas emerging as largest US datacenter market 40GW+ by 2028); (3) High-density power delivery transition (rack densities 100-240kW vs traditional 5-15kW; 800V DC architecture transition); (4) On-site generation as grid-bypass (nuclear restart commitments; natural gas turbines; Microsoft UAE $15.2B power-rich expansion). The 4-year transformer lead time means pricing power persists structurally — orders placed today don't deliver until 2030 in some cases; suppliers extract premium pricing on existing order books without expanding capacity faster than demand.

**Tier 1 — Structural chokepoints (highest quality exposure)**
The companies that capture pricing power most directly under the binding 2026 constraint.
- ETN (Eaton; cleanest US-listed transformer + electrical equipment exposure; "made-here" policy tailwinds; canonical Tier B Energy/Power per Tier 3 source; Layer 4-5 straddling tension flagged in Framework 2 Caveat #9)
- VRT (Vertiv; UPS dominance + thermal infrastructure; NVIDIA reciprocal-confirmation; 800V DC programs H2 2026; first vault adjacent-infrastructure-now-primary placement under AI datacenter scope rework)
- ABB (Swiss; transformers + switchgear + grid automation; ADR available)
- Schneider Electric (French; transformers + electrical equipment + datacenter infrastructure; SBGSF ADR)

**Tier 2 — Irreplaceable infrastructure and chokepoint participants**
- HD Hyundai Electric (Korean transformer manufacturer expanding US capacity; Alabama expansion ~$270M+ targeting ultra-high-capacity datacenter units; foreign-listed; US large transformer orders grew 4x between 2021 and 2023)
- Hyosung Heavy Industries (Korean; doubling Memphis plant capacity to 250+ units by 2027; foreign-listed; order book filled through 2027)
- Grid utilities serving major datacenter markets (regulated rate structures with limited upside despite load growth; Layer 2 placement per Framework 2)

**Tier 3 — Specialized designers and high-quality differentiated suppliers**
- MPWR (Monolithic Power Systems; high-density power management semiconductor; broad end-market diversification limits AI-pure exposure)
- VICR (Vicor; high-density power architecture; more volatile execution; closer to 800V DC architecture transition)
- IFNNY (Infineon ADR; broad power-semi GaN/SiC for underlying semiconductor transition)
- Powell Industries (POWL; medium-voltage switchgear; smaller-cap with structural pricing power; US-listed)
- GE Vernova (gas turbines for on-site generation; renewable generation portfolio)

**Tier 4 — Differentiated components and indirect exposure**
- Prysmian (PRYMF ADR; HV cable exposure)
- Nexans (foreign-listed; HV cables)
- NKT (foreign-listed; HV cables)
- CAT (Caterpillar; gensets for backup power; broad construction equipment exposure)
- CMI (Cummins; backup gensets at hyperscale; broad commercial/industrial exposure)
- GNRC (Generac; smaller-scale on-site generation)

**Tier 5 — Integrated systems / cross-domain participants**
- FLEX (Layer 6 EMS + JetCool liquid cooling acquisition; broader EMS exposure with AI datacenter subsegment driver; possible Outside Framework 7 placement pending ingest evidence on liquid cooling revenue mix)
- MOD (Modine; thermal management; broader HVAC exposure)

**Adjacent — Power Generation (cross-domain bridge to energy thesis)**
Power generation is structurally adjacent to Energy/Power infrastructure thesis but operates in a different framework (energy generation rather than datacenter power infrastructure). Listed for cross-reference; not Tier 1 of Framework 7.
- CEG (Constellation Energy; nuclear restart beneficiary; significant regulatory and execution risk)
- VST (Vistra; nuclear + natural gas)
- NRG (NRG Energy; mixed generation)

**Outside the framework**
- Diversified industrials (broad exposure with AI datacenter as minor segment; structural fit weaker than concentrated Energy/Power exposure)

**Important note on the binding 2026 constraint as cross-framework principle:** This framework's Tier 1 placements may understate near-term opportunity vs framework structure suggests — the binding constraint observation makes Tier 1 Energy/Power exposure (ETN/VRT/ABB/Schneider) materially more attractive on risk-adjusted basis 2026-2028 than parallel-framework comparison would imply. Power infrastructure exposure may outperform compute exposure on risk-adjusted basis if constraint persists. See Framework 11 cross-chokepoint themes for the full thesis-level structural framing.

**Energy/Power Tier 4 first canonical methodology (codified Session 46 per Session 45 ENS precedent).**

Tier 4 = specialized fit, narrower exposure within Energy/Power chokepoint domain. First canonical placement: ENS (Session 45; Layer 4 component-supplier with Energy/Power Tier 4 specialty fit).

**Substantiation methodology (Section 3.10 inverse four-criterion test):**

| Criterion | Tier 4 application |
|---|---|
| 1. Multiple datacenter customer disclosure | Generic plural framing acceptable ("data center customers" without named hyperscalers); industry-standard non-disclosure pattern |
| 2. Datacenter as named served segment in 10-K Item 1 | Required — datacenter must appear as explicitly named served segment within domain operating segment |
| 3. AI datacenter exposure structural | Required — primary-source explicit AI datacenter framing or AI-driven growth cycle commentary |
| 4. Customer concentration includes named hyperscaler exposure | OPTIONAL at Tier 4 — diversified-broad-customer-base archetype (no >10% single customer) compatible with Tier 4 placement |

Tier 4 placement substantiated at ~70% medium-high confidence when 3-of-4 criteria met (criterion 4 absent due to diversified customer base archetype is honest-verdict-correct).

**Layer placement default:** Layer 4 (component supplier scope). Multi-segment companies tested per Caveat #9 Layer 4-5 straddling discipline.

**Customer concentration archetype compatibility:** Tier 4 compatible with diversified-broad-customer-base archetype (no >10% single customer). Distinguished from Tier 1-3 placements where named hyperscaler concentration may be present (e.g., VRT canonical text energy_power_tier 1; ETN energy_power_tier 1).

**Specialty technology platform proprietary moat (where applicable):** Capital-investment-barrier moat framing per ENS TPPL precedent. Honest-verdict scope — primary technology applications may not be primarily AI datacenter (per ENS TPPL primary applications = Specialty AGM aerospace/defense + Motive Power maintenance-free).

---

## Framework 8: Equipment exposure tier framework

A complementary five-tier view for AI datacenter Equipment exposure quality. Subset already canonical at Framework 5 photonics tier; multi-domain expansion captures broader semi equipment + AI test equipment exposure. The classification reflected in the `equipment_tier` frontmatter field on company pages (when applicable).

**Tier 1 — Structural chokepoints (highest quality exposure)**
- ASML (EUV lithography monopoly + High-NA EUV ramp; secondary monopoly cycle as nodes transition 3nm → 2nm → A14)

**Tier 2 — Irreplaceable infrastructure and chokepoint participants**
- AMAT (Applied Materials; broad semi capex with AI tailwind)
- LRCX (Lam Research; broad semi capex)
- KLAC (KLA Corp; broad semi metrology + inspection with AI exposure)

**Tier 3 — Specialized designers and high-quality differentiated suppliers**
- ONTO (canonical photonics tier 4 with advanced packaging metrology focus; CoWoS/COUPE-adjacent revenue)
- AEHR (canonical photonics tier 4 with wafer-level burn-in single-public-pure-play positioning)
- KEYS (Keysight; largest US-listed optical/electrical test equipment platform; 1.6T validation cycle)
- TER (Teradyne; broader semi test platform with AI tailwind; diluted exposure)

**Tier 4 — Differentiated components and indirect exposure**
- VIAV (canonical photonics tier 4; finished-module optical test; Spirent acquisition extending portfolio)
- FORM (FormFactor; wafer prober adjacent to AEHR burn-in)
- VECO (canonical photonics tier 4; MOCVD/MBE epi equipment with InP-supply chokepoint adjacency)
- Anritsu (foreign-listed Japanese; parallel to KEYS but with foreign access friction)
- Aixtron (German MOCVD competitor to VECO)

**Tier 5 — Integrated systems**
- Less applicable at equipment tier; equipment doesn't typically operate at Layer 5 commercial integration

**Outside the framework**
- COHU (canonical Outside Framework 5; same Outside Framework 8 placement; broad-cycle semi test handler with automotive/analog drag rather than AI-specific)
- Diversified industrial test/measurement (broad exposure with semi as minor segment)

---

## Framework 9: Materials exposure tier framework (provisional)

A complementary five-tier view for AI datacenter materials chokepoint exposure. Provisional structure — many materials chokepoints are difficult to access via clean equity exposure. **Pending Tier 3 framework source curation for canonical chokepoint analysis at multi-source threshold.**

**Materials chokepoint identification (preamble):** Three structural materials chokepoints feed AI datacenter supply chain: (1) GOES steel for transformers (Cleveland-Cliffs sole US producer; binding upstream constraint on transformer manufacturing — see Framework 7); (2) Rare earths processing (China controls ~85-90%; geopolitical chokepoint risk affecting power semiconductors, motors, magnets); (3) InP substrates (canonical at InP-supply.md photonics chokepoint page; AXTI ~60-70% Western-HQ supplier with 100% China manufacturing; JX Advanced Metals ~78% indium feedstock concentration upstream). Additional chokepoints: silicon wafers (foreign-listed Japanese duopoly Shin-Etsu/SUMCO); HBM substrates (Ibiden); specialty gases; copper. Investability often lies two layers downstream — GOES steel exposure best accessed via transformer suppliers (ETN/ABB/Schneider) rather than direct CLF exposure.

**Tier 1 — Structural chokepoints (highest quality exposure)**
The companies that capture chokepoint pricing power most directly under structural concentration.
- AXTI (sole Western-HQ InP substrate supplier; canonical photonics tier 3; 100% China manufacturing creating geographic concentration risk; $60M+ backlog as of Q4 FY2025; structural Western-HQ position offset by small revenue base)
- CLF (Cleveland-Cliffs; sole US GOES steel producer; broader steel business creates exposure dilution; received $500M Biden-era grant for electrical steel plant upgrade subsequently partially cancelled; narrow structural chokepoint exposure with broader steel cyclicality drag)
- MP Materials (MP; US-listed rare earths reshoring play; thin operating history; execution risk significant; geopolitical tail risk both upside and downside; Mountain Pass mine + downstream processing buildout)

**Tier 2 — Irreplaceable infrastructure and chokepoint participants (foreign-listed dominant)**
- Sumitomo Electric (Japanese; foreign-listed; InP wafer supplier; competitive positioning vs AXTI)
- JX Advanced Metals (Japanese; foreign-listed; ~78% indium feedstock concentration creating upstream substrate-supply chokepoint)
- SUMCO (Japanese silicon wafer supplier; foreign-listed; duopoly with Shin-Etsu)
- Shin-Etsu Chemical (Japanese silicon wafer supplier; foreign-listed; broader chemicals exposure; silicon wafer duopoly leader)
- Ibiden (HBM substrate; foreign-listed Japanese; specialty substrate process expertise)

**Tier 3 — Specialized designers and high-quality differentiated suppliers**
- APD (Air Products; specialty gases; cyclical-with-secular-AI-tailwind framing)
- LIN (Linde; specialty gases; broader industrial gas exposure)

**Tier 4 — Differentiated components and indirect exposure**
- FCX (Freeport-McMoRan; copper; broad-cycle with AI tailwind; diversified end-market exposure means AI datacenter is one driver among many)
- SCCO (Southern Copper; Latin American copper exposure)
- Versum Materials (acquired by Merck KGaA; specialty semiconductor materials)
- Mitsubishi Chemical (broader chemicals with semi exposure; foreign-listed)

**Tier 5 — Integrated systems**
- Less applicable at materials tier; materials don't typically operate at Layer 5 commercial integration

**Outside the framework**
- Diversified miners + chemicals companies with AI datacenter as minor end market

**Important note on materials investability:** Many materials chokepoints are structurally significant but difficult to invest in via clean equity exposure. GOES steel chokepoint is best accessed via transformer suppliers (ETN/ABB/Schneider/HD Hyundai/Hyosung — Framework 7) rather than direct CLF exposure. Rare earths chokepoint exposure via MP carries significant execution and geopolitical risk. InP substrate chokepoint exposure via AXTI is the cleanest direct chokepoint exposure but bounded by small revenue base ($88M FY2025) and 100% China manufacturing risk. The structural insight often translates to investment exposure two layers downstream rather than at the materials tier directly.

**Materials Tier 1 first canonical methodology (codified Session 46 per Session 42 LEU + BWXT paired precedent).**

Tier 1 = pure chokepoint / monopoly position within Materials domain (commodity-materials feedstock supply layer feeding AI datacenter infrastructure). First canonical placements: LEU (Centrus Energy; HALEU enrichment 5/5 Acute and Binding monopoly; sole NRC-licensed Western producer) + BWXT (BWX Technologies; HALEU deconversion 4/5 + TRISO fabrication 3/5 + naval defense ballast triple-stack moat).

**Substantiation methodology:**

(a) **Western monopoly scope.** Sole or near-sole Western/non-state producer at chokepoint layer. LEU sole NRC-licensed Western HALEU enricher (AC100M Piketon).

(b) **DOE intermediary-customer pattern.** Government counterparty as primary commercial structure when commercial-customer enumeration absent. LEU DOE HALEU Operations Contract; BWXT DOE deconversion program ($2.7B ceiling).

(c) **Sequential fuel/material chain dependency.** Multi-layer chain where chokepoint position propagates demand backward + supply-constrained capacity propagates forward.

(d) **Defense industrial cross-cut (where applicable).** Multi-domain triple-stack moat per BWXT precedent (HALEU + TRISO + naval defense).

**Layer placement default:** Layer 4 (differentiated component / specialized designer scope at materials-feedstock supply).

**Customer concentration archetype compatibility:** Concentrated-government-counterparty (BWXT 68% U.S. Government); diversified-government-intermediary (LEU DOE methodology). Both archetypes consistent with Materials Tier 1 placement.

**Honest-verdict criterion 4 modification.** Section 3.10 inverse four-criterion test criterion 4 (named hyperscaler concentration) modified at Materials Tier 1 — substituted with named end-customer (reactor developer or government counterparty) concentration where applicable; reactor developer enumeration gap (e.g., LEU TerraPower / X-energy / Oklo enumeration) flagged as honest-verdict-correct industry-standard non-disclosure rather than substantiation gap.

**Materials Tier 2 first canonical methodology (codified Session 46 per Session 43 CCJ precedent).**

Tier 2 = strong chokepoint participant within Materials domain. First canonical placement: CCJ (Cameco Corporation; uranium mining 3/5 + Port Hope conversion 4/5; Westinghouse 49% Layer 2 hybrid via Brookfield JV).

**Substantiation methodology:**

(a) **Upstream materials chain participation.** Mining + conversion + (sometimes downstream extension via equity stakes); structural participation across multiple materials layers within sequential chain.

(b) **Layer 4 + Layer 2 hybrid scope (per Caveat #3 layer notation flexibility extension).** Company structurally operates at multiple layers; revenue mix supports hybrid framing. CCJ Layer 4 primary (mining + conversion) + Layer 2 hybrid via 49% Westinghouse equity (reactor design house designated-IP moat per Caveat #7).

(c) **Foreign-issuer protocol application.** Section 4.2 MJDS Canadian sub-protocol where applicable.

(d) **Distributed long-term contract customer concentration archetype.** Long-term contract portfolio (e.g., CCJ 230 Mlb committed); structural diversification via multi-decade contract structure.

**Layer placement default:** Layer 4 + Layer 2 hybrid (per Caveat #3 hybrid notation extension).

**Customer concentration archetype compatibility:** Distributed-long-term-contract archetype (CCJ 230 Mlb committed). Structurally distinct from concentrated-related-party (BE) / concentrated-government-counterparty (BWXT) / diversified-broad-customer-base (ETN/VRT/GEV/FLEX/ENS) / diversified-government-intermediary (LEU).

**Hyperscaler PPA framing context.** Materials Tier 2 placement permits explicit hyperscaler-utility PPA disclosure context at MD&A level despite upstream position — CCJ S43 5 named hyperscaler-utility PPAs documented (Microsoft-Constellation TMI; Meta-Constellation Clinton; Amazon-Talen Susquehanna; Google-NextEra Duane Arnold; Meta-Vistra/TerraPower/Oklo Prometheus).

---

## Framework 10: Hyperscaler CAPEX flow allocation framework

A structural framework for understanding how hyperscaler AI infrastructure CAPEX flows through the supply chain by allocation category. Reflects the central thesis observation that hyperscaler spending flows asymmetrically across chokepoints rather than uniformly. The classification informs how primary-source CAPEX commentary should be calibrated against vault structural framing.

**The structural fact:** Hyperscaler AI infrastructure CAPEX is now the largest corporate investment cycle in history. Combined 2026 CAPEX guidance from Microsoft + Alphabet + Amazon + Meta is **~$640-720B**, roughly double 2025's $381B. Alphabet has explicitly guided 2027 CAPEX to "significantly increase" from 2026 levels. Currently all four raised guidance in Q1 2026 earnings — sustained acceleration rather than deceleration.

**2026 hyperscaler CAPEX guidance (research-backed):**

| Hyperscaler | 2025 CAPEX (actual) | 2026 CAPEX (guidance) | YoY Δ |
|---|---|---|---|
| Microsoft (FY2026) | ~$88B (FY2025) | $190B+ (raised April 2026) | +116% |
| Alphabet (Google) | $91B | $180-190B (raised April 2026) | +98-109% |
| Amazon (AWS) | $131B | ~$200B | +53% |
| Meta | $72B | $125-145B (raised April 2026) | +73-101% |
| Oracle | ~$15B | Stargate $100B initial / $500B by 2029 | Multi-year commitment |
| **Combined Big 4** | **~$381B** | **~$640-720B** | **~+70-90%** |

**CAPEX allocation by category (allocation estimates; not all hyperscaler disclosures break this down precisely):**

**Category 1 — Compute (GPU + CPU + custom ASIC): ~50-65% of hyperscaler CAPEX**
The largest single CAPEX flow category. Recipients:
- **Merchant GPU (Layer 1):** NVDA dominant (~70%+ AI accelerator share); Blackwell B200/B300 ramping; Vera Rubin 2026; Kyber CPO scale-up. AMD challenger position with MI300/MI350/MI400 series.
- **Custom ASIC (Layer 1-3 cross-cutting):** Amazon Trainium ($225B revenue commitments; OpenAI 2GW + Anthropic 5GW commitments); Google TPU (AVGO partnership); Microsoft Maia (now in production at Iowa + Arizona); MRVL Microsoft custom partnership.
- **CPU:** Intel datacenter (declining share); AMD EPYC (gaining share); ARM-based hyperscaler custom (Amazon Graviton; Microsoft Cobalt; Google Axion).
- **Foundry-tier capture (Layer 2):** TSM benefits regardless of merchant vs custom outcome — all custom ASIC programs (Trainium / TPU / Maia) manufactured at TSMC.

**Category 2 — Networking (switching + interconnect + optical): ~10-15%**
- **Switch ASIC (Layer 1-3):** AVGO Tomahawk (dominant); MRVL Photonic Fabric (post-Celestial); CSCO Silicon One; ANET 7xxx series.
- **Optical components (Layer 4-5):** LITE / COHR / AAOI (transceivers + lasers); CRDO / MRVL / AVGO (DSPs); FN / FLEX (contract manufacturing).
- **Interconnect protocols:** InfiniBand/NVLink (NVIDIA proprietary via Mellanox); Ethernet (UEC/UALink ecosystem; AVGO Tomahawk-anchored).

**Category 3 — Memory (HBM + DRAM + NAND): ~10-15%, structurally constrained**
- **HBM oligopoly (Layer 2):** SK Hynix 50-62% share (NVDA primary supplier ~90%); Samsung 17-35% share recovering; Micron 11-21% share; HBM4 entering mass production 2026; capacity sold out through 2026.
- **DRAM/NAND broader exposure:** Tightening due to HBM cannibalization; commodity DRAM supply shock from Samsung HBM4 ramp; "3-to-1 rule" (every AI chip destroys capacity to make 3 normal PC chips); HBM consumed 23% DRAM wafers Q4 2025.

**Category 4 — Power infrastructure: ~10-15%, NOW THE BINDING CONSTRAINT**
- **Transformers (Tier 1 chokepoint):** 120-week lead times standard; 210 weeks (4 years) for large units; GOES steel constraint (Cleveland-Cliffs sole US supplier); 80% historically imported from Mexico/China/Thailand.
- **Power semiconductors (Layer 4):** MPWR / VICR / IFNNY (high-density power delivery); 800V DC architecture transition (VRT canonical H2 2026 program).
- **Switchgear / cables / busways (Tier 1-4):** ABB / ETN / Schneider / HD Hyundai Electric / Hyosung Heavy Industries / Prysmian / Nexans / NKT / Powell Industries.
- **Backup power / UPS / gensets (Tier 1-4):** VRT (UPS dominance); CAT / CMI / GNRC.
- **~50% of planned 2026 US datacenter builds delayed or cancelled due to power infrastructure shortages** per Bloomberg/Sightline Climate.

**Category 5 — Thermal infrastructure / cooling: ~5-10%, transition to liquid cooling**
- Direct-to-chip liquid cooling adoption (rack densities 100-240kW exceed air cooling capacity)
- VRT (canonical thermal — first vault adjacent-infrastructure-now-primary placement); MOD; FLEX (JetCool acquisition); Schneider; emerging Chinese suppliers

**Category 6 — Datacenter facilities + REITs: ~10-15%**
- Hyperscaler-built (Microsoft Fairwater 2GW Wisconsin; Amazon Project Rainier 500K+ Trainium2 cluster; Stargate Texas/New Mexico/Ohio)
- Datacenter REITs (DLR / EQIX) — Layer 2 irreplaceable infrastructure
- Specialty facilities builders

**Category 7 — Equipment (semi capex flowing through TSMC/foundries)**
- Lithography (Tier 1 chokepoint): ASML EUV monopoly + High-NA ramp
- Metrology: ONTO (advanced packaging) / KLAC / KLA
- Advanced packaging: AEHR (test); ASE / AMKR (OSAT); TSM CoWoS internal
- Test: KEYS / VIAV / Anritsu / FormFactor

**Category 8 — Materials (specialty constraints)**
- Specialty gases: Air Products / Linde
- Rare earths: Chinese export concentration; MP Materials reshoring play
- Substrate supply: InP/AXTI; silicon wafers Shin-Etsu/SUMCO; HBM substrates Ibiden
- GOES steel for transformers: Cleveland-Cliffs
- Copper: FCX / SCCO

**Cross-cutting CAPEX flow patterns (analytical implications):**

**Pattern A — Dollar volume vs pricing power asymmetry.** Compute captures the largest absolute CAPEX flow (~50-65%) but at increasingly competitive pricing dynamics under custom silicon disruption. Power infrastructure + memory chokepoint exposure capture smaller absolute flow (~10-15% each) but with structural pricing power that's less reflected in market valuations. Risk-adjusted positioning may favor chokepoint exposure over dollar-volume exposure.

**Pattern B — Custom silicon as CAPEX flow redirection.** Custom silicon programs shift CAPEX flow away from merchant Layer 1 (NVDA) toward Layer 3 designers (AVGO custom; MRVL custom) + Layer 2 manufacturing (TSM benefits regardless). Hyperscaler-captive silicon could save "tens of billions annually in capex" per Jassy.

**Pattern C — Hyperscaler customer concentration as CAPEX flow concentration risk.** AAOI Microsoft 43%; LITE+COHR NVDA $2B equity each; CRDO Customer A 67%→48%; SK Hynix NVDA ~90%; FN NVIDIA 27.6% + Cisco 18.2%. Position sizing should account for shared hyperscaler exposure across multiple holdings — CAPEX flow concentration is structural risk.

**Pattern D — Power constraint as binding ceiling on CAPEX deployment.** Money is not the bottleneck — $650B+ committed CAPEX exceeds deployable infrastructure. Transformer 4-year lead times mean compute CAPEX cannot deploy faster than power infrastructure expansion. This creates persistent constraint on Tier 1 (NVDA / AMD) revenue trajectory while power infrastructure suppliers (ETN / VRT / ABB / Schneider / HD Hyundai / Hyosung) capture pricing power.

**Pattern E — HBM cannibalization of commodity DRAM.** HBM3E to HBM4 transition increases dies-per-stack from 12 to 16 (33% more DRAM dies per AI accelerator); Samsung HBM4 ramp depleting commodity DDR5 capacity. AI compute scaling structurally tightens broader memory market — affects every server class, not just AI.

**LLM application:** When primary sources mention hyperscaler CAPEX commentary, calibrate against this allocation framework. Specific company exposure can be cross-referenced via category recipient lists. Material divergences from this allocation pattern (e.g., a primary source claims hyperscaler power infrastructure CAPEX is much smaller than ~10-15%) should surface as falsification candidates per Framework 11.

---

## Framework 11: Cross-chokepoint themes framework

Structural patterns operating across multiple AI datacenter supply chain domains rather than confined to single chokepoints. These themes are analytically distinct from per-domain framework structures (Frameworks 5-9) — they capture cross-cutting dynamics that single-domain framing obscures.

### 11.1 Hyperscaler customer concentration as structural risk

Cross-chokepoint pattern, not per-row risk. Concentration:
- AAOI Microsoft ~43% (Layer 5 transceiver assembly customer concentration)
- LITE + COHR NVDA $2B equity each (March 2026; Layer 4 component supplier vertical securing)
- CRDO Customer A 67%→48% broadening (Layer 3 specialized designer customer concentration improvement)
- MRVL custom warrants for two major hyperscaler programs (Layer 3 custom ASIC partnership)
- AVGO Anthropic-as-Google-TPU-derivative observation per Hock Tan Freudian slip (Layer 1 custom ASIC platform exposure)
- SK Hynix NVDA ~90% (Layer 2 HBM oligopoly customer concentration)
- FN NVIDIA 27.6% + Cisco 18.2% (Layer 6 contract manufacturing customer concentration)

**Position sizing implication:** Shared hyperscaler exposure across multiple holdings creates correlated risk — multiple wiki holdings may share customer concentration via NVDA (which itself has hyperscaler customer concentration). Position sizing should account for shared hyperscaler exposure rather than treating each holding as independent.

### 11.2 NVDA platform integration vertical securing

Six modalities operationalize NVDA's full control point across component chokepoints (canonical Sessions 22-32 documentation):

1. **Acquisition modality:** Mellanox (InfiniBand / Ethernet networking; capture switching + interconnect chokepoint)
2. **Licensing modality:** Groq (LPU IP licensing observation)
3. **Equity-plus-purchase modality:** COHR + LITE $2B each (March 2026; capture laser supply chokepoint)
4. **Equity backing modality:** Ayar Labs (silicon photonics startup; capture CPO scale-up optionality)
5. **Counterparty-attribution-only modality:** GLW (Corning Optical Communications; capture fiber/connector chokepoint via $6B Meta agreement)
6. **Reciprocal-confirmation modality:** VRT (capture thermal/power infrastructure chokepoint; NVIDIA reciprocal partnership confirmed at Tier 1)

NVDA exposure provides indirect exposure to all NVDA-aligned component layers. Affects laser supply (photonics Rank 1), advanced packaging (photonics Rank 5), fiber/connectors (photonics Rank 11), thermal infrastructure (Energy/Power Tier 1), and Switch ASIC chokepoint (photonics Rank 7) directly.

### 11.3 Layer 3 four-variant CPO profile

Four structurally distinct positions at same Framework 2 layer 3 (vault Session 28 codification):

- **MRVL: escalating disclosure** — Photonic Fabric scale-up via Celestial AI ($3.25-5.5B); $500M FY2028 / $1B FY2029 run rate projections
- **ALAB: phased coexistence** — retimer specialist with nascent CPO via aiXscale ($31.1M tuck-in)
- **CSCO: acknowledged-deferral** — "not imminent" CPO position; weakest commitment of five contestants
- **CRDO: displacement positioning** — uniquely against CPO via Hyperlume MicroLED + OmniConnect MicroLED-based "near package optics" alternative architecture

**Position sizing implication:** Whether thesis bets on CPO adoption (MRVL/NVDA path) or CPO displacement (CRDO path) determines exposure pattern asymmetry across these scenarios. Owning both CPO-adoption and CPO-displacement names captures bidirectional exposure but may underperform pure-direction exposure if outcome resolves clearly.

### 11.4 Outside Framework 5 placements as honest-verdict canonical examples

Two-company canonical pair (CLAUDE.md v8.1 codification):

- **COHU** — Layer 3 broad-cycle semi test handler; AI as minority subsegment (heavy automotive/analog/general consumer drag)
- **PLAB** — Layer 4 photomask supplier; broad semi infrastructure exposure with AI advanced packaging cited as growth driver but as broad signal not photonics-specific; ZERO photonic foundry customer disclosure across 3 primary sources

These holdings serve as analytical reference / counterpoint role rather than thesis centrality. The Outside Framework placement is itself the analytical signal — when a company's AI exposure is broad-cycle rather than structural, frameworks should declare that explicitly rather than rationalize photonics fit.

### 11.5 Power constraint as binding ceiling on CAPEX deployment

Money is not the bottleneck — $650B+ committed CAPEX exceeds deployable infrastructure. Transformer 4-year lead times mean compute CAPEX cannot deploy faster than power infrastructure expansion. This is the most structurally significant cross-chokepoint observation in the v10 rework — it reframes the entire investment thesis:

- Compute-tier names (NVDA / AMD) face deployment ceiling regardless of demand
- Power infrastructure suppliers (ETN / VRT / ABB / Schneider / HD Hyundai / Hyosung) capture structural pricing power
- Power chokepoint exposure may outperform compute exposure on risk-adjusted basis 2026-2028 if constraint persists
- Dual-anchor portfolio reframing: compute (NVDA / TSM) + power infrastructure (ETN / VRT) captures cross-domain dynamics

### 11.6 Cross-domain chokepoint dependencies

Single-chokepoint thesis bets miss dependency-chain exposure:

- Photonics chokepoints depend on power chokepoints (laser thermal management)
- Compute chokepoints depend on memory chokepoints (HBM-compute interface)
- Power chokepoints depend on materials chokepoints (rare earths; SiC; GaN; GOES steel)
- Memory chokepoints depend on equipment chokepoints (EUV for HBM logic dies)

**Position sizing implication:** Dual-chokepoint exposure (compute + memory; or compute + power; or photonics + power) captures dependency dynamics that single-chokepoint exposure cannot. Cross-domain dependency maps as analytical lens.

### 11.7 Custom silicon vs merchant compute disruption

Hyperscaler custom silicon programs shifting compute CAPEX flow:

- **Away from:** Merchant Layer 1 (NVDA)
- **Toward:** Layer 3 designers (AVGO custom for Google TPU; MRVL custom for Microsoft Maia) + Layer 2 manufacturing (TSM benefits regardless of merchant vs custom share)

NVDA share defense via platform integration (Mellanox + ecosystem); custom silicon share gain via Trainium ($225B commitments); Google TPU; Microsoft Maia (now production). Trajectory + share dynamics matter for NVDA position thesis. **The cleanest hedge against NVDA custom-silicon erosion risk is TSM exposure** — captures manufacturing share regardless of merchant vs custom outcome. See Framework 2.5 NVDA Layer 1 share dynamics transition for falsifiable share-erosion triggers.

### 11.8 HBM cannibalization of commodity DRAM

HBM3E to HBM4 transition increases dies-per-stack from 12 to 16 (33% more DRAM dies per AI accelerator); Samsung HBM4 ramp depleting commodity DDR5 capacity. AI compute scaling structurally tightens broader memory market — affects every server class, not just AI.

**Investment implication:** Memory exposure (MU + Samsung + SK Hynix) captures broader pricing power than HBM-specific revenue would suggest. The "3-to-1 rule" makes memory exposure structurally more attractive than headline HBM TAM growth would imply. Each HBM generation transition (HBM4 → HBM4E → HBM5) likely produces similar commodity-DRAM supply shocks rather than relief.

### 11.9 Energy/Power constraint as compute scaling ceiling

Grid + power infrastructure may bound AI compute scaling at hyperscaler scale before compute-tier supply constraints bind. Energy/Power chokepoint as macro-thesis-level constraint vs micro-thesis component.

**Strategic implication:** If CAPEX deployment trajectory diverges from CAPEX commitment trajectory due to power constraints, Tier 1 (NVDA) revenue may underperform commitment-implied trajectory while power infrastructure suppliers outperform. This reframes the entire investment thesis from "ride the AI compute boom via NVDA + photonics" to "ride the AI datacenter buildout via dual-anchor compute + power infrastructure exposure."

### 11.10 Geopolitical risk concentration at multiple chokepoints

Single-jurisdiction chokepoint concentration risk across multiple critical supply chain layers:

- **Taiwan:** TSM dependency (canonical Layer 2 chokepoint across photonics + memory + compute)
- **China:** Rare earths (~85-90% processing); transformers (~60% global production capacity); InP substrate manufacturing (100% AXTI manufacturing footprint)
- **Korea:** Memory (Samsung + SK Hynix HBM oligopoly ~70-95% combined); transformers (HD Hyundai + Hyosung emerging US capacity)

Diversification challenge: alternative geographies often have parallel concentration risks rather than diversification benefits. Portfolio construction should account for correlated geopolitical risk across photonics (Taiwan TSM), memory (Korea Samsung/SK Hynix), and power infrastructure (China transformers/rare earths) exposures simultaneously.

### LLM application: cross-chokepoint theme prioritization

When reasoning about portfolio construction or position sizing implications across the wiki, apply Framework 11 themes as analytical lens beyond single-chokepoint placement. Multiple Framework 11 themes may apply simultaneously to any holding — e.g., NVDA carries themes 11.2 (platform integration), 11.5 (binding constraint exposure), 11.7 (custom silicon disruption), 11.10 (Taiwan TSM dependency); ETN carries themes 11.5 (binding constraint participant), 11.10 (geopolitical risk via Chinese transformer competition). Cross-chokepoint themes capture analytical patterns that per-chokepoint frameworks cannot.

---

## Specific positioning judgments for the tracked holdings

Calibrated reference points for how each tracked company fits the frameworks. These are current views; evidence from filings should refine rather than overwrite them.

| Ticker | Layer | Photonics tier | Memory tier | Energy/Power tier | Equipment tier | Structural/cyclical | Current thesis fit |
|--------|-------|----------------|-------------|-------------------|-----------------|---------------------|-------------------|
| NVDA | 1 | 1 | — | — | — | Structural | Strongest — central platform definer; CAPEX flow primary recipient |
| TSM | 2 | 1 | 1 | — | 2 | Structural | Very strong — keystone chokepoint across photonics + memory + compute (CoWoS today; COUPE roadmap-dependent) |
| COHR | 4 | 2 | — | — | — | Structural | Strong — laser supply chokepoint participant, NVDA-backed, six-inch InP monopoly + 20-year NVDA relationship + Materials segment intersegment role |
| LITE | 4 | 3 | — | — | — | Structural | Good — differentiated laser supplier, NVDA-backed, three-inch InP industry-standard manufacturing |
| AEHR | 3–4 | 4 | — | — | 3 | Structural | Good — advanced packaging test specific |
| ONTO | 3–4 | 4 | — | — | 3 | Structural | Good — advanced packaging metrology |
| AAOI | 5 | 5 | — | — | — | Structural but weaker | Mixed — real AI exposure, weaker structural position, CPO displacement risk + Layer 4/5 straddling |
| COHU | 3 (broad-cycle 3–6) | Outside | — | — | Outside | Broad-cycle | Weakest — Outside Framework 5 + Framework 8; not AI-specific |
| MRVL | 3 | 3 | — | — | — | Structural | Good — specialized designer + CPO platform trajectory via Celestial; Layer 3→2 in progress, no triggers met |
| AVGO | 1 (straddling) | 3 | — | — | — | Structural | Strong — dual-pillar platform definer; straddling tension; custom ASIC partner for Google TPU |
| AXTI | 6 | 3 | — | — | — | Structural-cyclical hybrid | Niche — sole Western-HQ InP substrate supplier; vault value as upstream demand signal |
| ALAB | 3 | 4 | — | — | — | Structural | Moderate — retimer specialist with nascent CPO; Layer 3→2 trajectory tracked |
| VECO | 3-4 | 4 | — | — | 4 | Cyclical with structural tilt | Weak photonics fit; vault value as InP supply chain cross-reference |
| CSCO | 3 (3/5 straddling) | 4 | — | — | — | Mixed | Moderate — real silicon photonics capability but CPO explicitly deferred; weakest commitment of five CPO contestants |
| CRDO | 3 | 3 | — | — | — | Structural | Good — Cardinal DSPs + ZeroFlap optics + OmniConnect/Weaver gearbox; n-1 mature node cost advantage; CPO displacement positioning |
| ANET | 5 | 5 | — | — | — | Structural with CPO displacement long-term risk | Moderate — Etherlink portfolio + EOS + NetDL software + ESUN founding member; bounded by single merchant silicon vendor dependency |
| VIAV | 4 | 4 | — | — | 4 | Structural with broader test-equipment cyclicality | Good — first vault Chokepoint 6 baseline; Spirent acquisition; multi-quarter visibility extension |
| PLAB | 4 | Outside | — | — | Outside | Predominantly cyclical with structural AI advanced packaging exposure as sub-segment | Outside Framework 5 placement (second canonical case after COHU); counterpoint role |
| VRT | 5 | 4 | — | 1 | — | Structural | Strong under AI datacenter scope — first canonical adjacent-infrastructure-now-primary placement; thermal + UPS leadership; NVIDIA reciprocal-confirmation; 800V DC programs |

**Candidate additions per AI datacenter scope expansion (sequenced; ingest pending):**

| Ticker | Layer | Photonics tier | Memory tier | Energy/Power tier | Equipment tier | Structural/cyclical | Notes |
|--------|-------|----------------|-------------|-------------------|-----------------|---------------------|-------|
| FLEX | 6 | Outside | — | 5 | — | Mixed (broad EMS + AI tailwind) | Session 36+ ingest; liquid cooling thesis verification; possible Outside Framework 5 + Outside Framework 7 |
| ETN | 4 | — | — | 1 | — | Structural | Session 37+ ingest; canonical Tier 1 Energy/Power participant per binding 2026 constraint observation; cleanest US-listed transformer chokepoint exposure; Layer 4-5 straddling tension flagged in Framework 2 Caveat #9 |
| MU | 2 | — | 2 | — | — | Structural | Session 38+ ingest; only US-listed HBM oligopoly direct exposure; 11-21% market share + HBM4 ramping 2026 |
| MPWR | 4 | — | — | 3 | — | Structural with broad-cycle exposure | Session 39+ ingest; high-density power management semiconductor |
| VICR | 4 | — | — | 3 | — | Structural with execution risk | Session 39+ ingest; high-density power architecture; more volatile |

### Honest-verdict positioning observations

**The COHU honesty:** COHU is the one position where the wiki's analysis needs to be clear-eyed. It's a real semiconductor test handler company with a real business. But for an AI datacenter supply chain thesis specifically, its exposure is broad semi cycle (heavy automotive, analog, general consumer) rather than AI-differentiated. The wiki should state this plainly rather than softening it. The COHU page should articulate what would have to be true for COHU to fit the thesis better — that's more useful than rationalizing its inclusion.

**The AAOI straddling (codified Session 15):** AAOI's revenue is ~100% Layer 5 transceiver assembly, but in-house InP/GaAs laser manufacturing at Sugar Land, TX (MBE + MOCVD epitaxial growth) is a Layer 4 capability. The straddling is real — management characterizes it as strategically critical and plans to triple InP laser production by mid-2027 — but does not yet warrant a tier upgrade. Current laser production serves internal module integration, not merchant Layer 4 sales. Tier upgrade requires evidence laser capability has become commercially material — standalone Layer 4 merchant revenue OR named non-AAOI Layer 5 customer for Sugar Land laser supply.

**The LITE/COHR March 2026 differentiation:** The $2B NVDA investment in each, combined with multi-year purchase commitments and capacity access rights, is a material strengthening event for both laser supplier theses. Session 5 cross-validation established that LITE and COHR are not structurally equivalent. COHR sits at photonics_tier 2 (chokepoint participant, six-inch InP monopoly, 20+ year NVDA relationship) while LITE sits at photonics_tier 3 (differentiated supplier, three-inch InP, newer capital-constrained relationship). The tier gap could narrow if LITE demonstrates a proprietary three-inch process moat in future sources, or if COHR's six-inch monopoly claim proves overstated. On current evidence, the differentiation is earned.

**The VRT structural reclassification under AI datacenter scope:** VRT was originally placed Tier 4 photonics with explicit "adjacent infrastructure" framing (Session 22 codification). Under AI datacenter scope expansion (CLAUDE.md v9 / _thesis.md rework 2026-04-30), VRT becomes a primary chokepoint participant at Energy/Power Tier 2. The structural reclassification reflects the binding 2026 power constraint observation — thermal/power infrastructure is now structural to AI datacenter buildout, not adjacent. Photonics_tier 4 placement preserved per existing Sessions 22-32 canonical content; energy_power_tier 2 placement adds canonical Energy/Power framework positioning.

**The dual-anchor portfolio reframing:** Under AI datacenter scope expansion, the portfolio should evolve toward dual-anchor exposure — compute (NVDA / TSM as canonical) + power infrastructure (ETN / VRT as canonical) — capturing the binding-constraint observation. Photonics positions remain core to thesis but should be sized considering broader AI datacenter exposure rather than photonics-pure exposure.

---

## How the LLM should use these frameworks

1. **For first-pass categorization:** Place each company in the relevant layers and tiers based on these frameworks. Company pages should reference `layer` and applicable `*_tier` fields in YAML frontmatter (per CLAUDE.md conventions). Multi-domain companies may carry multiple tier classifications (e.g., TSM with photonics_tier 1 + memory_tier 1 + equipment_tier 2).

2. **As a stable reference point:** When a filing or transcript surfaces something that contradicts these frameworks, don't silently override — flag the tension on the relevant page and keep the framework as the baseline. Vic will revise the frameworks if evidence warrants it.

3. **Not as a complete ontology:** Many companies in the AI datacenter supply chain don't appear here. When they appear in primary sources, place them using the same analytical approach — ask what layer, what moat, what end-market exposure — rather than forcing them into an existing category. Domain assignment may require combining multiple framework structures.

4. **The frameworks evolve:** If evidence across multiple ingests consistently challenges a specific placement (e.g., "three sources now suggest MRVL has fully graduated to Layer 2"), raise this as a proposal for Vic to revise the framework, not as an automatic re-categorization. The Active Layer Transitions section (Framework 2.5) is where such evidence should accumulate.

5. **Track layer transitions actively:** Multiple Layer 3-5 companies are attempting layer transitions, plus a Layer 1 share dynamic (NVDA defending share against custom silicon). The wiki should maintain explicit pages for each transition and accumulate evidence for/against success as filings and calls surface new data.

6. **Distinguish the two CPO tracks.** When reasoning about CPO timelines, distinguish component-layer deployment (validated 2026-2028 window, grounded in LITE and COHR primary sources) from COUPE-specific packaging timing (uncertain, silent in TSMC primary sources). CPO can proceed on non-COUPE packaging approaches; treating the two as a single coupled timeline is analytically incorrect.

7. **Combine layer placement with control-point analysis.** When reasoning about strategic positioning of NVDA, AVGO, MRVL, CSCO, ANET, CRDO, read both Framework 2 layer placement AND Framework 2.6 control-point analysis. The two axes capture complementary aspects of value capture. Pure-bottleneck framing alone obscures the architectural authority that some Layer 1 platform definers exhibit and the partial control-point characteristics that some specialized designers exhibit.

8. **Combine multi-domain framework structures for cross-domain companies.** Companies operating across photonics + memory + compute + energy/power + equipment + materials may carry multiple tier classifications. TSM (photonics_tier 1 + memory_tier 1 + equipment_tier 2). VRT (photonics_tier 4 + energy_power_tier 1; Layer 5 not Layer 4 per Framework 2 box update). MU (memory_tier 2). ETN (energy_power_tier 1; Layer 4-5 straddling per Caveat #9). Multi-domain classification captures cross-cutting exposure that single-domain framing obscures.

9. **Honor the binding constraint observation.** Per _thesis.md AI datacenter supply chain scope, power infrastructure has displaced compute as the binding 2026 constraint (~50% of planned 2026 US datacenter builds delayed/cancelled). When reasoning about CAPEX flow trajectory and investment positioning, account for this constraint asymmetry — compute-tier names face deployment ceiling; power-tier names face structural pricing power. Framework 7 has cross-domain status — Energy/Power constraint binds AI compute scaling at hyperscaler scale before compute-tier supply constraints bind. Dual-anchor exposure (compute + power infrastructure) captures cross-domain dynamics that single-domain exposure cannot.

10. **Calibrate hyperscaler CAPEX commentary against Framework 10.** When primary sources mention hyperscaler CAPEX trajectory, allocation, or guidance changes, calibrate against Framework 10's 8-category allocation framework. Specific company exposure cross-references via category recipient lists. Material divergences from this allocation pattern (e.g., a primary source claims hyperscaler power infrastructure CAPEX is much smaller than ~10-15%) should surface as falsification candidates.

11. **Apply Framework 11 cross-chokepoint themes for portfolio construction analysis.** When reasoning about portfolio construction, position sizing, or correlated risk across the wiki, apply Framework 11's 10 cross-chokepoint themes as analytical lens. Multiple themes may apply simultaneously to any holding. Cross-chokepoint themes capture analytical patterns (hyperscaler customer concentration; NVDA platform integration; power constraint binding ceiling; HBM cannibalization; geopolitical concentration; etc.) that per-chokepoint frameworks cannot.

12. **Cross-reference _thesis.md as anchor.** Per CLAUDE.md "_thesis.md is the evaluation point for everything." Frameworks support thesis articulation; thesis evolution may surface framework refinements. When framework structures and thesis content diverge, raise the divergence to Vic — don't silently reconcile.

---

**Note on this rework (2026-04-30 → 2026-05-01 v10.1 refinement):** Comprehensive rework executed via collaborative chat drafting (Vic-directed; agent-scaffolded with research backing) per CLAUDE.md v8.1 frameworks.md ownership convention exception (one-time Vic-authorized rework session aligning frameworks with reworked _thesis.md AI datacenter supply chain scope; resumed default for future sessions).

**v10.0 scope (2026-04-30):** Scope expanded from photonics-primary framework structure to multi-domain framework structures: Framework 1 (Supply chain flow) extended with 5 sub-domain diagrams (1.1 photonics canonical + 1.2 memory + 1.3 energy/power + 1.4 compute + 1.5 equipment); Framework 5 photonics tier preserved as canonical; new parallel framework structures added — Framework 6 (memory tier), Framework 7 (energy/power tier), Framework 8 (equipment tier), Framework 9 (materials tier provisional). Frameworks 2 + 2.5 + 2.6 + 3 + 4 preserved with multi-domain extensions where applicable. Specific positioning judgments table extended with multi-domain tier columns (memory_tier; energy_power_tier; equipment_tier). Honest-verdict observations preserved + added (VRT structural reclassification under AI datacenter scope; dual-anchor portfolio reframing).

**v10.1 refinement (2026-05-01) — full structural alignment with thesis:**
- **Critical fix 1 — VRT layer:** Moved from Layer 4 box to Layer 5 box (corrects internal inconsistency; Framework 2 box now matches positioning judgments table + thesis line 166)
- **Critical fix 2 — Framework 7 duplicate Tier 1:** Renamed second "Tier 1 (Energy / Generation)" to "Adjacent — Power Generation" sub-section
- **Critical fix 3 — Tier 1 design consistency:** Frameworks 6 / 7 / 9 restructured to match Framework 5 design pattern (Tier 1 = named companies as chokepoint participants; chokepoint identification moved to lead preamble paragraphs)
- **Significant gap fix 4 — Framework 10 added:** Hyperscaler CAPEX flow allocation framework with 8 categories (Compute / Networking / Memory / Power / Thermal / Facilities / Equipment / Materials) + 5 cross-cutting CAPEX flow patterns
- **Significant gap fix 5 — Power constraint elevation:** Framework 7 framing rewritten to elevate Energy/Power as cross-domain binding constraint; framework now bounds CAPEX deployment across all other domains rather than parallel framework
- **Significant gap fix 6 — Custom silicon disruption codification:** Framework 2.5 expanded with NVDA Layer 1 share dynamics under custom silicon disruption transition; falsifiable share-erosion triggers defined; Framework 2 Caveat #8 added
- **Significant gap fix 7 — Framework 11 added:** Cross-chokepoint themes framework with 10 themes (hyperscaler customer concentration; NVDA platform integration; Layer 3 four-variant CPO profile; Outside Framework 5 placements; power constraint binding ceiling; cross-domain chokepoint dependencies; custom silicon disruption; HBM cannibalization; energy/power as compute scaling ceiling; geopolitical risk concentration)
- **Lesser refinement 8 — ETN Layer 4-5 straddling:** Framework 2 Caveat #9 added explicitly flagging straddling tension parallel to AAOI Layer 4/5 + AVGO Layer 1 patterns
- **Lesser refinement 9 — Hyperscaler customer concentration:** Codified as Framework 11.1 component
- **Lesser refinement 10 — Framework 4 expansion:** Added Section 4.2 per-domain structural vs cyclical assessment subsections (photonics / memory / energy/power / compute / equipment / materials)

Key structural observation captured throughout: power infrastructure has displaced compute as binding 2026 constraint per _thesis.md rework. Framework 7 elevated to cross-domain status (bounds Frameworks 5/6/8/10 deployment trajectory rather than parallel framework). Custom silicon disruption codified as structural force redirecting compute CAPEX flow. Cross-chokepoint themes captured as Framework 11 (parallel structural framework to per-domain Frameworks 5/6/7/8/9). CAPEX flow allocation captured as Framework 10 with research-backed 2026 hyperscaler guidance figures.