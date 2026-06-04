# Frameworks — Defense & Drones (Unmanned Systems Supply Chain & Chokepoint Analysis)

> **Status (v1.0):** Working analytical framework for the vault's second thesis domain (defense unmanned systems), parallel to the AI-datacenter `frameworks.md` (v10.1). Drones-first scope per `_thesis-defense-drones.md`. Created from the Tier-3 anchor report `raw/research/US-defense-and-drones-report.md`.
> **Purpose:** Calibrate the LLM's initial categorization of defense/drone companies before primary sources refine the specifics. Same role the AI `frameworks.md` plays for the AI-datacenter domain.
> **Epistemic note:** These frameworks are *interpretive scaffolding*, not facts extractable from filings. They represent how I think about the defense/drone space. Primary sources should *enrich* them, not override. Company placements will shift as evidence accumulates; the frameworks are the stable part. **The anchor report is Tier-3 — many demand-side figures (FY2027 DAWG $54.6B; magnet capacity targets; micro-cap guidance) are requests/projections, not realized results. Verify against primaries before treating as load-bearing.**

---

## Framework D1: Defense & drones value chain (supply-chain flow)

How an unmanned-systems capability gets physically built and fielded. Read top to bottom — the upstream chokepoints (top) are where structural pricing power concentrates; the platform layer (lower-middle) is being deliberately commoditized.

```
┌─────────────────────────────────────────────┐
│        UPSTREAM CHOKEPOINT INPUTS            │
│  Rare-earth NdFeB magnets (MP, USAR, UUUU)  │
│    — China ~85-90% finished magnets         │
│  Secure/trusted FPGAs (LSCC, MCHP, AMD,     │
│    MRCY) — deeper dependence: TSMC fab       │
│  EO/IR sensors & seekers (TDY/FLIR, DRS)    │
│  High-energy-density batteries (AMPX)        │
│  Edge-AI compute / flight controllers        │
│    (UMAC, NVIDIA Jetson US SKUs)             │
└────────────────────┬────────────────────────┘
                     ▼
┌─────────────────────────────────────────────┐
│        COMPONENTS & PAYLOADS                 │
│  Motors, ESCs, datalinks, gimbals, seekers, │
│  warheads/energetics, propulsion             │
│  (NDAA-compliant "Blue UAS" sourcing —       │
│   policy chokepoint, exemption expires        │
│   Jan 1, 2027)                               │
└────────────────────┬────────────────────────┘
                     ▼
┌─────────────────────────────────────────────┐
│        PLATFORMS (commoditizing)             │
│  Small/tactical/FPV/OWA (Group 1-3):         │
│    Switchblade, Black Widow, Neros Archer    │
│    — driven toward ~$2,000 unit cost          │
│  Large (Group 4-5)/CCA/jet:                   │
│    XQ-58 Valkyrie, YFQ-42A/44A, MQ-9         │
│    — higher barriers, fewer competitors       │
└────────────────────┬────────────────────────┘
                     ▼
┌─────────────────────────────────────────────┐
│        AUTONOMY & AI SOFTWARE                 │
│  Swarming, GPS-denied nav, mission autonomy, │
│  data fusion (Hivemind, Lattice, Maven)      │
│  — DECOUPLED from airframe (CCA precedent);  │
│    best capability is PRIVATE (Anduril,      │
│    Shield AI); US-listed thin (PLTR)         │
└────────────────────┬────────────────────────┘
                     ▼
┌─────────────────────────────────────────────┐
│        COUNTER-UAS                            │
│  Detection / EW / jamming (~90% of fielded   │
│  C-UAS is EW) / kinetic interceptors / C2    │
│  (Coyote, KuRFS, VAMPIRE, MLIDS, Dedrone,    │
│   Iron Drone) — fragmented, under-served      │
└────────────────────┬────────────────────────┘
                     ▼
┌─────────────────────────────────────────────┐
│        PROGRAM INTEGRATION / DEMAND           │
│  Programs of record: Replicator → DAWG →     │
│  JIATF 401; Drone Dominance "Gauntlet"; CCA  │
│  Buyer: DoD (increasingly also a CAPITAL     │
│  provider — MP-DoD deal; OSC equity stakes)  │
└─────────────────────────────────────────────┘
```

**Key structural read:** value capture is **inverted relative to visibility.** The platform layer is the most visible (the drone you can photograph) and the least defensible (price-capped, multi-vendor by design). The upstream inputs are the least visible and the most defensible. This is the defense analogue of the AI thesis's "money is not the bottleneck" insight — *airframes are not the bottleneck; magnets, secure chips, seekers, and autonomy are.*

---

## Framework D2: Value-capture / investability tiers (the `defense_tier` field)

A four-tier classification for US-listed defense/drone exposure quality — the first-pass categorization reflected in the **`defense_tier` frontmatter field** (codified in CLAUDE.md Section 3.2, Session 123). Distinct from the value-chain *layer* in Framework D1: a company's tier reflects its investability/structural quality, its layer reflects where it sits in the chain. (Mirrors how the AI vault separates `layer` from `*_tier`.)

**Tier 1 — Primes with real drone-relevant programs of record**
Real contracts, real revenue scale; for the large primes, drones are a slice of a diversified business.
- AVAV (AeroVironment) — tactical UAS + loitering munitions + C-UAS + autonomy (post-BlueHalo: + space/EW/directed energy). The most complete US-listed pure-play.
- KTOS (Kratos) — jet-powered UAS (XQ-58 Valkyrie), target drones, hypersonics, space. Best large-UAS/CCA-adjacent exposure.
- LMT, NOC, RTX, LHX, BA — diversified primes; drones/C-UAS a real but non-needle-moving slice (RTX is the notable C-UAS leader via Raytheon Coyote/KuRFS).
- General Atomics — *private; un-investable* (MQ-9, YFQ-42A CCA, Gambit).

**Tier 2 — Mid-cap pure-plays / specialists with real revenue**
- ONDS (Ondas) — autonomous drones (Optimus) + C-UAS (Iron Drone, Sentrycs) + loitering-munition IDIQ via Mistral. Growth heavily M&A-driven.
- AIRO (AIRO Group) — drones (RQ-35 Heidrun) + avionics + training + eVTOL.
- DRS (Leonardo DRS) — C-UAS (MLIDS, M-SHORAD) + radar + EW + AI processors.
- PLTR (Palantir) — AI/data fusion (Maven, Gotham) for ISR/targeting/C-UAS. Profitable; not drone-specific. **Dual-thesis node** (AI-datacenter demand-side page exists).

**Tier 3 — Speculative micro-caps (FLAGGED — apply Framework D6 financial-quality screen)**
Real revenue inflections, but dilution, losses, and narrative-ahead-of-financials risk are the rule.
- RCAT (Red Cat), UMAC (Unusual Machines), ZENA (ZenaTech), DPRO (Draganfly), UAVS (AgEagle), PDYN (Palladyne AI), PRZO (ParaZero).

**Tier 4 — Supply-chain / materials enablers (highest structural conviction)**
The chokepoint owners — where `_thesis-defense-drones.md` places the strongest structural case.
- MP (MP Materials) — rare-earth magnets. **Multi-thesis node** (AI/materials page exists).
- LSCC (Lattice) — secure FPGAs. **Cross-thesis** (AI-datacenter overlap; [[LSCC]] is now a vault page — dual-thesis from creation, S125).
- TDY (Teledyne) — EO/IR sensors + loitering munition (Rogue 1).
- AMPX (Amprius) — high-energy-density batteries.
- MRCY (Mercury Systems) — trusted/secure microelectronics + C-UAS processing. **Cross-thesis** (not yet a vault page).
- USAR (USA Rare Earth), UUUU (Energy Fuels), AREC (American Resources) — rare-earth feedstock/refining.
- AMD, MCHP (Microchip) — FPGAs. AMD is a **dual-thesis node** (AI page exists).
- AXON (Axon) — C-UAS detection via Dedrone.

**Honest-verdict note:** the report's own net assessment is that the **supply-side / chokepoint framing (Tier 4) is the higher-conviction expression of the thesis** than the platform names (Tier 1) — because platforms are being commoditized by design. The tier numbering is *not* a ranking of conviction (Tier 4 is not "lowest"); it is a taxonomy of where in the structure a company sits. Conviction tracks the chokepoint quality gradient (Framework D5), not the tier number.

---

## Framework D3: Demand map / programs of record (how the money flows)

The defense analogue of the AI vault's Framework 10 (hyperscaler CAPEX flow). Where does drone/autonomy money originate, and how contingent is each pot? **The discipline: separate enacted law from requests everywhere.**

**Enacted (structural, ground truth):**
- **FY2025 reconciliation (P.L. 119-21, signed July 4, 2025):** $156.2B mandatory defense funding (CRS IN12580). Drone pots: ~$16B low-cost enablers; $1B+ OWA drone industrial base; $1.1B small-drone industrial base; $500M attritable-drone delivery; $500M counter-UAS. Total FY2025 defense >$1T; base budget roughly flat (deliberate).
- **FY2026:** first separately tracked ~$13.4B DoD AI-and-autonomy budget line; Army ≥$858M C-UAS request.

**Requested (contingent — flag as requests):**
- **FY2027 request (April 3, 2026):** ~$1.5T topline. **DAWG $54.6B** (from $225.9M FY2026) — **but only $1B base; $53.6B (≈98%) in a future reconciliation pot** (up to 5 yrs to obligate), contingent on a second reconciliation bill surviving the Nov 2026 midterms. OSC loan program ~$20.2B ($216M base + $20B reconciliation).

**Programs of record (the demand structure):**
- **Replicator → DAWG → JIATF 401.** Replicator dissolved into DAWG (late 2025); Replicator 2 → JIATF 401 (acquisition authority up to $50M/C-UAS effort; legacy JCO disestablished). **CRS IF12611 execution caveat:** Replicator fielded "only hundreds" by summer 2025 vs. a "thousands" target — announcements outrun delivery.
- **Drone Dominance Program (DDP):** ~$1.1B, four-phase, ~300,000 OWA drones by end-2027. Gauntlet I (March 2026): 25 vendors; winners Skycutter/Neros/Napatree; ~$150M initial orders; unit-cost ceiling tightening toward $2,000. Gauntlet 2: 48–49 companies (incl. AVAV, KTOS); GPS-denial/jamming/EW.
- **CCA:** Increment 1 → Anduril (YFQ-44A) + General Atomics (YFQ-42A); 100–150 aircraft/5 yrs (~$30M/unit); ~$8.9B; Shield AI Hivemind + RTX autonomy (decoupled from airframe). Increment 2 → nine+ vendors. KTOS XQ-58 adjacent.
- **Counter-UAS:** >350 detections at ~100 US installations; JIATF 401 five-installation directed-energy pilot.

**Government as capital provider (a structural shift to track):** the DoD is increasingly taking *equity/debt*, not just buying product — the MP–DoD deal (convertible preferred + warrant + price floor + offtake; see Framework D5) and reported OSC talks with PDW/UMAC/Neros (WSJ ~May 28, 2026). This concentrates government backing in chosen suppliers and can distort the competitive field for public-equity holders.

---

## Framework D4: Structural vs. cyclical exposure

Mirrors the AI `frameworks.md` Framework 4. Classifies whether a name's drone exposure is durable across administrations or dependent on a contingent surge / active conflict.

**Structural (durable):**
- Budget architecture itself — reconciliation mechanics, OSC loans, the standing DAWG line, NDAA component bans, acquisition reform.
- Bipartisan China-pacing rationale.
- The chokepoint owners (rare-earth magnets, secure microelectronics, EO/IR) — demand is durable on geology/physics regardless of which year's budget passes.

**Cyclical / contingent:**
- The FY2027 "one-year surge" (~98% reconciliation-funded; officials call it a possible surge).
- Conflict-driven supplementals (Ukraine; Red Sea / 2026 Iran conflict) — a durable ceasefire reduces urgency (partly offset by restocking).
- Platform-tier volume tied to specific program cycles (Gauntlet phases, Replicator successors).

**Per-name read:** Tier 4 enablers skew structural (chokepoint durability). Tier 1 primes are structural at the company level but their *drone* slice is partly cyclical. Tier 3 micro-caps are the most cyclical/contingent — their revenue inflections often depend on a single program award converting.

---

## Framework D5: Chokepoint framework + quality gradient (the core)

The highest-conviction lens, and the defense analogue of the AI thesis's "binding constraint" framing. **The central rule: rank chokepoints by what makes them durable. Geology/physics chokepoints rank above policy chokepoints — even when today's revenue looks identical — because a policy chokepoint can expire on a known date.**

| Chokepoint | What's scarce | Who controls it | Durability basis | Quality | US-listed beneficiaries |
|---|---|---|---|---|---|
| **Rare-earth NdFeB magnets** | High-perf sintered NdFeB, esp. heavy rare earths (Dy/Tb) for high-temp motors | China ~85-90% finished magnets, ~91% separation/refining, ~69% mining, ~100% production equipment (IEA Nov 2025); JL MAG ≈ all non-Chinese output combined | **Geology + capacity** (years to replicate; meaningful US finished-magnet capacity 2027-2028+) | **Very high** | MP, USAR, UUUU, AREC |
| **Secure microelectronics / FPGAs** | NDAA-compliant secure-control FPGAs, hardware root-of-trust, rad-tolerant parts | LSCC (low-power secure), MCHP (PolarFire), AMD/Xilinx (high-end), MRCY (trusted). Deeper chokepoint: TSMC fab (Taiwan) | **IP + fab physics** (design defensible; fab dependence is a geographic risk NDAA rules don't solve) | **High** (asterisk: Taiwan fab; LSCC ~64% China revenue) | LSCC, MCHP, AMD, MRCY |
| **EO/IR sensors & seekers** | Cooled/uncooled thermal imagers, gimbals, seekers, AiTR | TDY (FLIR) dominant in Western EO/IR; concentrated | **Decades of export-controlled IP** | **High** | TDY, DRS, RTX |
| **Autonomy & AI software** | Swarming, GPS-denied nav, mission autonomy | Best capability PRIVATE (Anduril Lattice, Shield AI Hivemind); US-listed thin | **Software margins + decoupled value (CCA precedent)** | **Very high structurally, but mostly un-investable** | PLTR (adjacent); PDYN (speculative) |
| **High-energy-density batteries** | Silicon-anode cells (450-500 Wh/kg), NDAA-compliant | AMPX silicon-anode; China dominates conventional Li-ion | **Energy-density physics + NDAA battery-origin rules phasing in** | **Moderate-high** | AMPX, KULR |
| **Counter-UAS detection / EW** | Drone discrimination in clutter/swarms; spectrum; non-kinetic defeat | Fragmented: RTX, LHX, DRS, AXON, ONDS | **Hard technical problem + persistent threat** | **High (fragmented)** | RTX, LHX, DRS, AXON, ONDS |
| **Edge-AI compute / flight controllers** | NDAA-compliant, Blue UAS-listed, US-assembled modules | Thin ecosystem: ARK, ModalAI (private), UMAC; NVIDIA Jetson US SKUs | **Replicable ecosystem** | **Moderate** | UMAC; NVDA (indirect) |
| **NDAA-compliant supply chain ("Blue UAS")** | Whole-system China-free sourcing | DCMA Blue UAS list; small compliant-vendor set | **POLICY** — durable only while statute holds; **DoD exemption expires Jan 1, 2027** | **High but policy-dependent (weakest quality)** | UMAC, RCAT, AVAV, ONDS, AIRO |

**The MP–DoD deal as chokepoint template (July 9, 2025):** DoD bought $400M convertible preferred + a warrant for up to ~11.2M shares (conversion/exercise $30.03) → ~15% as-converted stake, largest shareholder; plus a 10-year $110/kg NdPr price floor, a 10-year magnet offtake, the "10X" facility (~10,000 MT, Northlake TX, commissioning 2028), Independence expansion to 3,000 MT, $1B JPMorgan/Goldman financing, and $500M from Apple. First commercial NdFeB at Independence December 2025. This is the clearest case of government converting a chokepoint into a backstopped commercial position — watch whether the model repeats (OSC equity talks suggest it will).

**Rare-earth detail:** China ~69% mining but ~91% separation/refining and ~85-90% finished magnets (IEA Nov 2025). Pentagon needs ~3,000-4,000 tons specialized magnets/yr → ~10,000 tons by 2030; domestic capacity years away. Drones are <3% of global NdFeB demand but high-criticality (skewed to the most China-controlled heavy rare earths).

**LLM application:** when a primary source surfaces a new chokepoint or a shift in an existing one, score it on the **durability basis** (geology / physics / IP / capacity / policy), not just on current revenue. A policy chokepoint with a known expiry (Blue UAS, Jan 1 2027) is structurally weaker than a geology one even at identical revenue. Flag any evidence that moves a chokepoint up or down the gradient (e.g., China relaxing export controls weakens the magnet chokepoint; a Blue UAS exemption renewal strengthens the policy chokepoint).

---

## Framework D6: Booked-contract-vs-narrative / financial-quality screen (the "LASE discipline")

Formalized from the LASE investigation: a distressed/promotional micro-cap can ride a thematic narrative (defense, drones, lasers) while its filings show going-concern doubt, cash burn, and constant dilution. **This screen is mandatory for every Tier 3 speculative micro-cap and applied to any name where narrative appears to outrun fundamentals.** Apply at first-mention and at every ingest.

**Red flags to check in primaries (10-K / 10-Q / 8-K), in priority order:**
1. **Going-concern language** — explicit "substantial doubt about the Company's ability to continue as a going concern."
2. **Cash burn vs. runway** — operating cash burn against cash on hand; how many quarters of runway? (e.g., a name with ~2.8yr runway is healthier than one burning faster than it can raise.)
3. **Dilution history** — share-count growth; number of offerings; warrant overhang. (UMAC's >320% share growth / $157.8M raised in 2025; DPRO's 9+ offerings since 2023 are cautionary archetypes.)
4. **Earnings quality** — is "net income" real operating profit or a fair-value gain on warrants/derivatives? (UAVS "income" from warrant gains; UMAC's $10.3M Q1 net income likely warrant/one-off-driven; ZENA's $25M derivative revaluation.)
5. **Internal-control weakness** — disclosed material weakness (RCAT) is a direct quality flag.
6. **Listing-compliance history** — Nasdaq bid-price/listing deficiencies (PRZO May 2026; UAVS/DPRO histories).
7. **Filing delinquency** — overdue/late filings are themselves a signal (the difficulty of *finding* a name's latest earnings is information).

**The contract-vs-narrative distinction:** a press-release "selection," "evaluation," "pilot," "LOI," or "framework agreement" is **not** a booked contract. Distinguish:
- **Booked / funded** — a definitive contract or funded delivery order with a dollar value and a period of performance (cite the 8-K/10-Q).
- **IDIQ / ceiling** — a maximum-value vehicle, not guaranteed revenue (e.g., a "$982M IDIQ" is a ceiling, not booked).
- **Backlog** — distinguish funded vs. unfunded; pro-forma (acquisition-inclusive) vs. organic.
- **Narrative** — selection/pilot/evaluation/MOU; track but do not treat as revenue.

**Honest framing (per CLAUDE.md Section 2.1):** when a micro-cap's thesis fit is weak — revenue tiny, losses large, dilution heavy, "income" warrant-driven — the page states it plainly and may be short and verdict-like. Inclusion is for trajectory/counterpoint, not thesis centrality. This is the defense analogue of the AI vault's Outside-Framework / honest-verdict discipline.

---

## Framework D7: Cross-thesis overlap with the AI-datacenter frameworks

Several names sit at the intersection of this thesis and the AI-datacenter supply chain. **Convention: these are dual-thesis pages** — add defense framing + a `defense_tier` to the *existing* AI page rather than creating a duplicate. Note the overlap on both sides.

| Company | Defense role (`defense_tier`) | AI-datacenter role | Vault status |
|---|---|---|---|
| **MP** | Rare-earth magnets — Tier 4 chokepoint | Materials (rare earths/magnets); Framework 9 | **Existing AI page** — add defense framing |
| **AMD** | Xilinx FPGAs (avionics/EW/radar) — Tier 4 | AI accelerators + datacenter CPU; compute | **Existing AI page** — add defense framing |
| **NVDA** | Jetson edge-AI modules (indirect) — Tier 4 | Platform definer; Layer 1 | **Existing AI page** — add defense framing |
| **PLTR** | Maven/Gotham data fusion — Tier 2 | AI demand-side / software | **Existing AI page** — add defense framing |
| **[[LSCC]] (Lattice)** | Secure FPGAs — Tier 4 chokepoint | Secure-control FPGAs; AI server FPGA +86% YoY | **Vault page (S125)** — dual-thesis from creation |
| **MRCY (Mercury)** | Trusted microelectronics — Tier 4 | Secure microelectronics | **Not yet a vault page** — would be dual-thesis from creation |

**The cleanest multi-thesis chokepoint: rare-earth NdFeB magnets.** The same China concentration that constrains drone motors constrains AI-datacenter power-semiconductor magnets and robotics — one chokepoint, two demand drivers. MP is the shared node.

**Secure microelectronics is the second overlap node:** Lattice's secure FPGAs serve both defense (NDAA root-of-trust) and AI-datacenter (server FPGA) demand; the TSMC-fab dependence and China-revenue exposure are shared risks across both theses.

---

## Positioning judgments for the tracked universe

Calibrated reference points for how each US-listed name fits the frameworks. Current views; primary-source evidence should refine rather than overwrite them. **Figures are Tier-3 (mostly Q1 2026 / FY2025) — verify at ingest; the four INGESTED names ([[MP]], [[AVAV]], [[LSCC]], [[KTOS]]) now carry primary-source-verified figures, marked "INGESTED".** `defense_tier` is the codified field per Framework D2 (CLAUDE.md Section 3.2).

| Ticker | defense_tier | Value-chain layer | Chokepoint position | Structural/cyclical | Tier-3 scale & flags | Current thesis fit |
|---|---|---|---|---|---|---|
| [[AVAV]] | 1 | Platforms + C-UAS + autonomy | Platforms; chokepoint consumer | Structural (co.) / cyclical (program) | INGESTED S124: Q3 FY2026 rev $408M (+143%); FY2026 guide CUT to $1.85–1.95B; $151.3M goodwill impairment (SCAR termination-for-convenience); funded backlog $1.12B; US Gov ~75% / Ukraine ~18% | Strong — most complete US-listed pure-play; chokepoint *consumer* (not owner); margin + integration the watch item |
| [[KTOS]] | 1 | Large UAS + hypersonics + propulsion | Large UAS; propulsion/SRM (chokepoint builder) | Structural/cyclical | INGESTED S127: Q1 FY2026 rev $371M (+15.8% org); record backlog $2.011B; book-to-bill 1.6x; FY2026 guide RAISED to $1.70–1.76B; $1.35B Feb-2026 equity raise (net) | Good — beat-and-raise; honest-verdict = serial dilution + negative FCF + pre-PoR timing; vertically integrated (builds engines + SRMs) |
| RTX | 1 | C-UAS + autonomy + sensors | C-UAS leader | Structural | ~$80B+; diversified | C-UAS leader but drone/C-UAS a slice |
| LHX | 1 | C-UAS + EW + datalinks | C-UAS/EW | Structural | ~$21B; diversified | Real but diluted |
| LMT / NOC / BA | 1 | Platforms + integration | Large UAS / sensing | Structural | Large; drones a slice (BA loss-making co.-wide) | Diversified; drone exposure not needle-moving |
| ONDS | 2 | Platforms + C-UAS + autonomy | C-UAS + autonomy | Structural with M&A risk | FY2025 ~$50.7M; FY2026 guide ≥$390M (acq-fueled); backlog $457M pro forma; $982M Army IDIQ via Mistral; FY2025 loss ~$137M | Mixed — verify organic vs. acquired; backlog quality |
| AIRO | 2 | Platforms + avionics | Platforms | Structural | FY2025 $90.9M; net loss $4.1M; ~$150M drone backlog | Real revenue, larger than most micro-caps; unprofitable |
| DRS | 2 | C-UAS + sensing | C-UAS | Structural | ~$3.5B | Real C-UAS portfolio; diversified |
| PLTR | 2 | Autonomy/AI software | Autonomy/AI software | Structural | ~$3B+, profitable; Maven | Real; not drone-specific; **dual-thesis** |
| RCAT | 3 | Tactical drones | Platform (Blue UAS) | Cyclical | FY2025 $40.7M (+161%); Q1 2026 $15.5M (+849%); GM ~13%; Q1 net loss $26.6M; **material weakness in internal controls** | FLAG — Army SRR anchor real; financial-quality screen critical |
| UMAC | 3 | NDAA-compliant components / edge | Edge-AI + Blue UAS | Cyclical | FY2025 ~$11.2M; Q1 2026 $8.1M (+296%); $10.3M net income (likely warrant-driven); OSC equity talks; **>320% share growth, $157.8M raised 2025** | FLAG — improving, but massive dilution; >half of Gauntlet awardees are customers |
| ZENA | 3 | Drone-as-a-service | — | Cyclical | FY2025 C$12.9M (+558%, roll-up); $25M derivative revaluation | FLAG — promotional (quantum claims, Mar-a-Lago events); heavy losses |
| DPRO | 3 | NDAA-compliant drones | Blue UAS | Cyclical | FY2025 ~$7.7M; loss ~$23M; ~$90M cash; **9+ offerings since 2023** | FLAG — severe dilution; defense pivot |
| UAVS | 3 | Small UAS + sensors | — | Cyclical | Tiny (~$2M-scale quarters); "income" from warrant fair-value gains | FLAG — tiny revenue; warrant-driven earnings |
| PDYN | 3 | Autonomy software | Autonomy (speculative) | Cyclical | Q1 2026 $3.5M; loss $12.6M; ~$43.7M cash (~2.8yr runway) | FLAG — minimal revenue; narrative-driven |
| PRZO | 3 | C-UAS interceptor | C-UAS (micro) | Cyclical | FY2025 ~$1.05M; negative GM; **May 2026 Nasdaq bid-price deficiency** | FLAG — micro revenue; partners with ONDS |
| [[MP]] | 4 | Supply-chain (magnets) | **Rare-earth magnets (core)** | Structural | INGESTED S90 (dual-thesis S123): Q1 FY2026 rev $90.6M (+49%); +$42.3M PPA income; Materials adj EBITDA $36.7M; $400M DoW convertible preferred (DPA Title III); 10X facility 2028 | Strongest enabler — purest play on the most durable chokepoint; **dual-thesis**; owner-side anchor of [[rare-earth-magnet-chokepoint]] |
| [[LSCC]] | 4 | Supply-chain (secure FPGAs) | **Secure microelectronics (core)** | Structural | INGESTED S125: Q1 FY2026 rev $170.9M (+42%); GM 68.8%; net income $21.8M; **64% Greater China revenue**; fabless on TSMC/Samsung/UMC; AMI acq ($1.65B, ~Q3 close) | Strong on secure-FPGA *capability* (defense revenue thin/undisclosed); currently an AI-datacenter story; China + Taiwan-fab the counter-signal; **cross-thesis** |
| TDY | 4 | Payloads/sensors | **EO/IR sensors (core)** | Structural | ~$6.23B TTM; Rogue 1/LASSO; Black Hornet | Strong — diversified, profitable way to own the sensor layer |
| AMPX | 4 | Supply-chain (batteries) | **High-energy batteries** | Structural | FY2025 $73M (+202%); Q4 positive adj EBITDA; customers incl. Teledyne FLIR | Good — energy-density moat; EBITDA inflection |
| MRCY | 4 | Supply-chain (microelectronics) | Secure microelectronics + C-UAS processing | Structural (turnaround) | FY2025 $912M; GAAP loss; "BuiltSECURE" | Turnaround; **cross-thesis** |
| USAR | 4 | Supply-chain (magnets) | Rare-earth magnets | Structural (pre-revenue) | FY2025 $1.64M (pre-revenue); ~$1.75B cash post-PIPE; Stillwater OK 2026 | Well-funded but pre-revenue; meaningful volume 2027+ |
| UUUU | 4 | Supply-chain (oxides) | Rare-earth feedstock | Structural | Uranium-revenue base; first US Tb/Dy oxide 2026 | Oxides, not magnets — one step upstream |
| AREC | 4 | Supply-chain (refining) | Rare-earth refining | Speculative | Small; $1.4B Pentagon-backed ReElement/Vulcan deal | Speculative refining-stake play |
| AMD | 4 | Supply-chain (FPGAs) | Secure microelectronics | Structural | Large-cap, profitable; Xilinx high-end FPGA | **Dual-thesis**; Xilinx the defense angle |
| MCHP | 4 | Supply-chain (FPGAs) | Secure microelectronics | Structural | ~$4-5B; PolarFire rad-tolerant | Aerospace-grade FPGAs/MCUs |
| AXON | 4 | C-UAS detection | C-UAS detection | Structural | ~$2B+, profitable; Dedrone | C-UAS via Dedrone acquisition |

**Private / un-investable (mark and monitor):** Anduril (Lattice; ~$2.2B 2025 revenue; $61B post-money May 2026; $20B Army Lattice contract), Shield AI (Hivemind; $12.7B; CCA-selected), General Atomics, Skydio, Saronic, Neros, Performance Drone Works, Vulcan Elements. **The single most important structural fact for public-equity exposure: the best pure drone-autonomy capability is not investable.**

---

## How the LLM should use these frameworks

1. **For first-pass categorization:** place each defense/drone company in its value-chain layer (D1), its `defense_tier` (D2), and its chokepoint position (D5). Company pages carry the `defense_tier` field (codified CLAUDE.md Section 3.2).

2. **Separate enacted from requested everywhere (D3).** When a primary or Tier-3 source cites a budget figure, classify it: enacted law (FY2025 reconciliation $156.2B) vs. a request (FY2027 DAWG $54.6B, ~98% reconciliation-contingent). Never present a request as a fact. This is the defense thesis's single most important discipline.

3. **Score chokepoints on durability basis, not revenue (D5).** Rank geology/physics/IP chokepoints above policy chokepoints. Flag the Blue UAS exemption expiry (Jan 1, 2027) on every NDAA-compliance-dependent name. When evidence moves a chokepoint up or down the gradient, raise it.

4. **Apply the financial-quality screen to every Tier 3 micro-cap (D6).** Check going-concern, burn/runway, dilution, earnings quality (warrant gains ≠ operating profit), internal-control weakness, listing compliance, filing delinquency. Distinguish booked/funded contracts from IDIQ ceilings, backlog (funded vs. unfunded; organic vs. pro-forma), and narrative (selection/pilot/MOU). State weak fit plainly (honest-verdict discipline).

5. **Treat the anchor report as Tier 3.** `raw/research/US-defense-and-drones-report.md` is Vic-curated synthesis — attribute it, paraphrase in wiki voice, and verify its quantitative claims against primaries at ingest (CRS reports for budget; SEC filings for company figures; company IR for program/contract claims). Vault primary-source findings win on conflict.

6. **Handle dual-thesis nodes per D7.** For MP, AMD, NVDA, PLTR (existing AI pages), add defense framing + `defense_tier` to the existing page rather than duplicating; note the overlap on both sides. LSCC and MRCY, if created, are dual-thesis from first creation. Rare-earth magnets and secure microelectronics are the shared chokepoints.

7. **The frameworks evolve.** If evidence across multiple ingests consistently challenges a placement, raise it as a proposal for Vic to revise — not an automatic re-categorization. These frameworks are human-owned scaffolding (same convention as the AI `frameworks.md`).

8. **Cross-reference `_thesis-defense-drones.md` as the anchor.** Frameworks support thesis articulation; when framework and thesis diverge, raise it to Vic — don't silently reconcile. The AI-datacenter `_thesis.md` / `frameworks.md` remain the anchors for that domain and are untouched by this file.

---

**Note on this creation (2026-06-03):** Drafted via Vic-authorized collaborative drafting as the companion frameworks file to `wiki/_thesis-defense-drones.md` (the vault's second thesis domain). Sourced from the Tier-3 report `raw/research/US-defense-and-drones-report.md` plus prior chat synthesis. Mirrors the AI `frameworks.md` structure (supply-chain flow → value-capture tiers → demand/CAPEX map → structural-vs-cyclical → chokepoint framework → financial-quality screen → cross-thesis overlap → positioning judgments → LLM application). Drones-first scope; broad munitions, European rearmament, and standalone directed-energy sequenced for future expansion. The AI `frameworks.md` (v10.1) is untouched. Both subsequently codified (Session 123, CLAUDE.md v9.4): the `defense_tier` frontmatter field (Framework D2) and the CLAUDE.md Section 1.2 two-domain scope note.
