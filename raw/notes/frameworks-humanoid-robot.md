# Frameworks — Humanoid Robots (Embodied-AI Value Chain & Chokepoint Analysis)

> **Status (v0.1 DRAFT):** Working analytical framework for the vault's **third** thesis domain (humanoid robots), parallel to the AI-datacenter `frameworks.md` (v10.1) and the Defense & Drones `frameworks-defense-drones.md` (v1.0). Humanoid-first scope per `wiki/_thesis-humanoid-robot.md`. Drafted via Vic-authorized collaborative drafting — **for Vic to shape and finalize.** Created from two Tier-3 anchor reports (`raw/research/humanoid-robot-primer-report.md` + `humanoid-robot-high-value-subsystems-research.md`), anchored on Goldman Sachs' humanoid value-chain work.
> **Purpose:** Calibrate the LLM's initial categorization of humanoid companies before primary sources refine the specifics. Same role the other two frameworks files play for their domains.
> **Epistemic note:** These frameworks are *interpretive scaffolding*, not facts extractable from filings. Primary sources should *enrich* them, not override. **The anchor reports are Tier-3 — TAM/unit/cost figures, BOM splits, magnet-per-robot estimates, and China-concentration %s are projections/estimates, not realized results. Verify against primaries before treating as load-bearing. Multi-bank figures are attributed (the 40–60% BOM is McKinsey's, the 33% reducers+screws is JPM's, the $38bn 2035 TAM is Goldman's — do not misattribute.)**

---

## Framework H1: Humanoid value chain (value-capture flow)

How a humanoid capability gets physically built — note this is a **value-capture / BOM map, not a logistics flow.** Read bottom-to-top for the build (substrate → makers); the *value* is inverted relative to visibility — the robot at the top is the commodity, the magnets and precision parts at the bottom are the chokepoints.

```
┌─────────────────────────────────────────────┐
│   PLATFORM / ROBOT MAKERS (commoditizing)    │
│   40+ integrators: Tesla, Figure, 1X,        │
│   Agility, Apptronik + a wall of Chinese     │
│   (Unitree, UBTech, AGIBOT, Xiaomi, XPeng)   │
│   — racing to a sub-$20k cost floor           │
└───────────────────▲─────────────────────────┘
                    │  (integrates)
┌───────────────────┴─────────────────────────┐
│   SUBASSEMBLIES                              │
│   Actuator modules (motor+reducer/screw+     │
│   encoder+control); dexterous hands          │
│   (route-risk: tendon vs linkage vs cable)   │
└───────────────────▲─────────────────────────┘
                    │
┌───────────────────┴─────────────────────────┐
│   COMPONENTS (the ~33–60%-of-BOM core)        │
│   Harmonic reducers (rotary joints) ........ │ ◄ CHOKEPOINT (Japan/China)
│   Planetary roller screws (linear joints) .. │ ◄ CHOKEPOINT (Germany/China)
│   Frameless/coreless motors ................ │   commoditizing
│   6-axis force/torque + tactile sensors .... │ ◄ rising (US: NOVT, VPG)
│   Cameras / LiDAR / depth .................. │   competitive, route-risk
│   Batteries ................................ │   EV-shared, commoditizing
└───────────────────▲─────────────────────────┘
                    │
┌───────────────────┴─────────────────────────┐
│   MATERIALS SUBSTRATE (the binding chokepoint)│
│   Rare-earth NdFeB/NdPr magnets ............ │ ◄◄ BINDING CHOKEPOINT
│     China ~90% finished magnets             │     (US: MP — triple-thesis)
│   Precision bearings / encoders (China ~40%) │
└─────────────────────────────────────────────┘

   ┌─────────────────────────────────────────┐
   │  THE BRAIN (runs across the whole stack) │
   │  VLA foundation models + onboard compute │
   │  (NVDA Isaac/GR00T + Jetson Thor; Tesla; │
   │  GOOGL DeepMind) — widest moat, but       │
   │  already owned via the AI-datacenter book │
   │  + immaterial *incremental* humanoid TAM  │
   └─────────────────────────────────────────┘
```

**Key structural read:** value capture is **inverted relative to visibility** — identical to the Defense thesis. The robot maker is the most visible and least defensible (40+ entrants, cost-floored). The magnet substrate and the precision actuator core are the least visible and most defensible. *The robot is not the bottleneck; the magnet, the reducer, the roller screw, and the brain are.*

---

## Framework H2: Value-capture / investability tiers (the proposed-but-HELD `humanoid_tier`)

A value-capture gradient for US-listed humanoid exposure quality. **Deliberately NOT codified as a frontmatter field yet (YAGNI):** at n≈3 US-listed pure-ish-plays, a `humanoid_tier` field is premature. Names land **`outside` the existing per-domain frameworks + theme-anchored** (the [[INOD]] precedent), with the US-listed accessibility flag carried in prose. A `humanoid_tier` (or, more likely, a broader `physical_ai_tier`) is a **human-owned codification** to revisit only when the name count and the physical-AI broadening justify it.

The gradient (highest to lowest durable value capture), with the **central tension — strongest chokepoints, worst US access — baked in**:

| Tier | Position | Durability | US-listed access | Names |
|---|---|---|---|---|
| **A — Materials substrate** | Rare-earth magnets | **Very high (physics/geology)** | 🟢 **MP** | MP; Lynas (🟡 AUS) |
| **B — Actuation core** | Harmonic reducers; roller screws | **High (precision grinding/metallurgy)** — *commoditization clock* | 🔴/🟡 — Japan/Germany/China | Harmonic Drive (6324.T), Schaeffler (SHA.DE), HIWIN (2049.TW); LeaderDrive, Hengli (🔴 China) |
| **C — High-end sensing** | 6-axis force/torque + tactile | **Medium–high, rising (tech barrier)** | 🟢 **NOVT, VPG** | NOVT (ATI), VPG; Murata/TDK (🟡 Japan) |
| **D — Manipulation** | Dexterous hands | **High (future), route-risk** | 🔴 China/private | Zhaowei, Inovance (🔴); Maxon (private) |
| **E — Brain** | VLA models + compute | **Very high moat — but already owned; immaterial incremental** | 🟢 NVDA, GOOGL, TSLA | NVDA, GOOGL, TSLA (don't double-count) |
| **F — Commoditizing** | Assembly; motors; vision; battery | **Low–moderate** | 🟢 (mixed) RRX, OUST/HSAI; 🔴 China | RRX, OUST, HSAI, INVZ, LAZR; Sanhua/Tuopu (🔴); CATL (🔴) |

🟢 US-listed clean / 🟡 awkward-foreign / 🔴 China-A-share / HK / private.

**Honest-verdict note:** the tier *letter* is not a ranking of conviction — Tier A (materials) carries the *highest* structural conviction. Conviction tracks the **chokepoint quality gradient (H5)** and the **US-listed accessibility tension**, not the position in the build. The vault's edge here is surfacing what the banks' component-rankings underweight: the materials substrate (MP) and the high-end sensor layer (NOVT/VPG).

---

## Framework H3: Demand map / adoption timeline (how big, how real, how contingent)

The humanoid analogue of the AI vault's Framework 10 (CAPEX flow) and the Defense D3 (budget map). **The discipline: lead with "early-innings optionality," separate direction from timing, and never present a TAM projection as a fact.**

**Sizing (Tier-3; attribute):**
- **Goldman:** TAM **$38bn by 2035** (base; raised 6× from $6bn), blue-sky **$205bn**; units **~76k (2027E) → >250k (2030) → ~502k (2032E) → ~1.4M (2035).** Goldman is *more conservative than the market.*
- **Morgan Stanley ("Humanoid 100"):** ~$5tn by 2050; ~1bn units by 2050; China ~63% of value chain. More bullish long-run.
- **Reality check:** Omdia estimates Tesla / Figure / Agility each shipped **~150 units in 2025**; realistic 2026 output is low-thousands. This is early-innings.

**BOM / value distribution (attribute by bank):**
| Source | Actuators | Sensing | Compute | Notes |
|---|---|---|---|---|
| **JPM** | reducers+screws ≈ **33%** | — | — | PRS $1,350–2,700 each, ~40+/robot |
| **McKinsey** | **40–60%** (gearbox 30–50%) | 10–20% | 10–15% | 5 domains = 85–90% of cost; screws/reducers = choke points |
| **BofA** | dominant | depth cam + LiDAR | AI chip | BOM ≈ $35k (2025) → $13–17k (2030–35) |
| **Goldman (only public per-part figure)** | roller-screw linear joint = **20–30% of high-spec component cost** | — | — | Prefers harmonic gear + actuator assembly |

**Cost decline (the key TAM-upgrade driver):** ~40% drop ($50–250k → $30–150k); *"AI progress surprised us the most"* (Goldman) — end-to-end VLA models replacing hand-coded behavior.

**The central demand-side risk — the order-vs-capacity gap:** Goldman's supplier survey (nine Chinese companies, Nov 2025) found suppliers planning **100k–1M robot-equivalent units of capacity each, with no confirmed binding orders** — a "capacity-first" gamble. *Benchmark to watch:* the first sizable confirmed OEM order (Tesla Optimus Gen-3 production order; Figure BotQ; XPeng IRON) validates it; continued absence into 2H2026 signals overcapacity/margin risk.

**Maker landscape (the commoditizing platform layer):** Tesla Optimus (Gen-3, Fremont summer 2026; ~$685M Sanhua linear-actuator order + ~RMB1.2bn rotary order); Figure ($39bn val, Helix VLA, BMW pilot); Boston Dynamics/Hyundai (electric Atlas, Gemini brain); Unitree (world leader >5,500 units 2025 / 32.4% share / STAR IPO), UBTech (HK), AGIBOT, Xiaomi, XPeng.

---

## Framework H4: Structural vs. cyclical exposure

Mirrors the AI Framework 4 and Defense D4.

**Structural (durable):**
- The multi-decade labor-automation rationale (aging demographics, labor shortages in dirty/dull/dangerous work).
- The physics chokepoints (rare-earth magnets; precision grinding) — scarce regardless of which OEM wins or which year volumes inflect.
- The brain's moat (compounds with data/compute scale) — though its humanoid *increment* is immaterial vs datacenter AI.

**Cyclical / speculative:**
- The hype cycle itself (valuations embedding flawless scaling; "ChatGPT moment for manipulation" not yet arrived).
- Specific-OEM program timing (Optimus Gen-3, Figure BotQ, XPeng IRON) — slip-prone.
- The order-vs-capacity gamble — capacity built ahead of binding orders.

**Per-name read:** materials/sensor enablers (MP, NOVT, VPG) skew structural *but humanoid is optionality on a legacy base* (apply H6). Robot makers and pure-narrative names are the most cyclical/speculative. The brain (NVDA) is structural at the company level but its humanoid slice is immaterial.

---

## Framework H5: Chokepoint framework + quality gradient (the core)

The highest-conviction lens, and the humanoid analogue of the Defense D5 (geology-over-policy) rule. **The central rule: rank chokepoints by what makes them durable. Physics/geology > precision-manufacturing know-how > assembly/integration. And cross-reference durability against US-listed accessibility — the defining tension of this thesis is that the strongest chokepoints have the worst access.**

| Chokepoint | What's scarce | Who controls it | Durability basis | Quality | US-listed access |
|---|---|---|---|---|---|
| **Rare-earth NdFeB magnets** | High-perf sintered NdFeB; heavy rare earths (Dy/Tb) for high-temp motors; **~0.9–4 kg/robot (~2× EV)** | China ~90% finished magnets, ~88% refined RE, ~40% precision bearings/encoders | **Geology + capacity** (years to replicate) | **Very high** | 🟢 **MP** (triple-thesis); Lynas (🟡) |
| **Harmonic / strain-wave reducers** | Micron-precision grinding + flexspline metallurgy; limited grinding machines | Top-5 (Harmonic Drive/Nabtesco/HDS/Wittenstein/Schaeffler) ~55–60%; China localizing | **Precision grinding/metallurgy** — *commoditization clock as China closes* | **High** (GS top pick, score 16) | 🔴/🟡 Japan (6324.T)/China |
| **Planetary roller screws** | ~5-micron thread grinding; aerospace alloys; heat treatment; ~26-wk lead times | Schaeffler (Ewellix), HIWIN, THK/NSK/SKF; China (Hengli, Beite) scaling | **Precision grinding/alloys** (low capacity-flexibility = pricing power) | **High** (score 14) | 🟡 Germany (SHA.DE)/Taiwan; 🔴 China |
| **6-axis force/torque + tactile sensors** | High-precision F/T calibration; gram-level tactile across a hand | ATI + HBM dominate 6-axis F/T | **Tech barrier (calibration/IP)** | **Medium–high, rising** (score 13) | 🟢 **NOVT (ATI), VPG** |
| **Dexterous hands** | Miniaturized actuators+tendons+tactile in a finger envelope | Zhaowei, Inovance (China); Maxon (private) | **Capability barrier, but architecture UNSETTLED (route-risk)** | **High future, low certainty** (score 15, certainty 1) | 🔴 China/private |
| **The brain (VLA + compute)** | Sub-100ms edge inference; world models; sim/synthetic data | NVDA (Isaac/GR00T + Jetson Thor); GOOGL; Tesla | **Data/compute scale (widest moat)** | **Very high — but already owned; immaterial *incremental*** | 🟢 NVDA/GOOGL/TSLA (don't double-count) |
| **Actuator assembly** | Motor+reducer+encoder+control integration | Sanhua, Tuopu (China) | **Integration, not core IP** | **Low–moderate (commoditizing)** | 🔴 China |
| **Motors (frameless/coreless)** | PM motors; coreless cup motors for hands | Kinco, Haozhi, Moons', Leadshine (China); AMETEK; Nidec | **Low tech barrier** | **Low–moderate** | 🟡 Nidec; 🟢 RRX (adjacent); 🔴 China |
| **Vision (camera/LiDAR)** | Depth/LiDAR; image sensors | Intel RealSense; Orbbec, RoboSense, Hesai, DJI (China); OUST/INVZ/LAZR (US) | **Competitive + vision-vs-LiDAR route risk** | **Low–moderate (commoditizing)** | 🟢 OUST/HSAI/INVZ/LAZR (higher-beta) |
| **Battery** | ~2–3 kWh Li-ion packs | CATL, Samsung SDI, Panasonic | **EV-shared; not humanoid-specific** | **Low** | 🔴 no clean US pure-play |

**The MP node as chokepoint template:** MP is the only US-listed integrated rare-earth miner + magnet producer scaling domestic capacity (Pentagon equity + $110/kg NdPr price floor + the "10X" facility 2028; first commercial NdFeB Dec 2025). The *same* NdFeB concentration that constrains drone motors (Defense) and AI-datacenter power-semiconductor magnets also constrains humanoid actuators — **one chokepoint, three demand drivers.** This is the cleanest multi-thesis node in the entire vault.

**Honest counter-signals to preserve (don't let the magnet thesis become a foregone conclusion):** (a) BofA's contrarian view that **machine tools, not magnets, are the near-term bottleneck**; (b) **magnet-free-motor R&D** (induction / electrically-excited synchronous / FeN) that would de-risk *and undercut* MP; (c) the **harmonic/roller-screw commoditization clock** as Chinese challengers close the precision gap.

**LLM application:** score each chokepoint on its **durability basis** (geology/physics > precision-manufacturing > integration) *and* its **US-listed accessibility** — both matter for this thesis. Flag evidence that moves a chokepoint up or down the gradient (China relaxing export controls weakens the magnet chokepoint; grinding-capacity scaling weakens the reducer/screw chokepoint; a Western dexterous-hand or precision-actuator pure-play emerging fills the biggest access gap).

---

## Framework H6: The "optionality-vs-pure-play / needle-mover" screen (the early-innings discipline)

The humanoid analogue of the Defense D6 financial-quality screen — but the dominant risk here isn't micro-cap distress, it's **mistaking a legacy-industrial business with humanoid *optionality* for a humanoid *pure-play*.** Apply at first-mention and at every ingest.

**The needle-mover test (mandatory for every cross-over name):**
1. **What % of revenue is actually humanoid today?** For MP (defense + EV + humanoid), NVDA (datacenter + humanoid), NOVT/VPG (legacy industrial automation + humanoid), the honest answer is *"small / mostly optionality."* Quote the revenue-mix evidence; never call a name a "humanoid play" without it. (Same discipline as the AI vault's AAOI/MRVL layer-straddling rule.)
2. **Is the humanoid exposure incremental or transformational?** Goldman's "% incremental opportunity from humanoids" column is the tell: low (1) for the giants (NVDA, Intel, CATL — humanoids are a rounding error) and high (3) for the small-base pure-plays (gears, hands, motors).
3. **Pure-play vs cross-over vs beneficiary:** distinguish a true humanoid pure-play (rare in US listings) from a cross-over (humanoid optionality on a real business — MP/NOVT/VPG) from a beneficiary where it's immaterial (NVDA/INTC).

**The early-innings / hype discipline:**
4. **Order book vs capacity vs narrative.** A press-release "design win," "evaluation," or "reported supplier" relationship is *not* a booked order (and many Optimus-supplier claims come from Chinese-language trade press — reported, not OEM-confirmed; Section 3.3 disclosed/inferable/unknown). Distinguish booked orders from capacity announcements from narrative.
5. **Timing realism.** Lead every read with realistic near-term volumes (low-thousands in 2026), not the 2035 TAM. Treat all forward TAM/unit/cost figures as Tier-3 projections.

**Honest framing (per CLAUDE.md Section 2.1):** when a name's humanoid fit is weak — humanoid revenue tiny, exposure immaterial, relationship merely "reported" — the page states it plainly. Inclusion is for the chokepoint/optionality angle, not thesis centrality. The honest verdict (e.g., "this is a force/torque sensor business that *could* ride humanoids, not a humanoid company") matters more than the comfortable one.

---

## Framework H7: Cross-thesis overlap

Several names sit at the intersection of this thesis and the existing vault. **Convention: these are dual/triple-thesis pages** — add humanoid framing to the *existing* page rather than duplicating; note the overlap on all sides.

| Company | Humanoid role | Other-thesis role(s) | Vault status |
|---|---|---|---|
| **[[MP]]** | Rare-earth magnets — the binding actuator chokepoint (Tier A) | Defense (`defense_tier 4` magnets) + AI/materials (rare earths) | **Existing vault page** — add humanoid framing → **triple-thesis** |
| **[[NVDA]]** | The robot brain/compute (Isaac/GR00T + Jetson Thor) — immaterial incremental | AI-datacenter platform definer + defense Jetson edge | **Existing vault page** — add a light humanoid-optionality note |
| **[[INTC]]** | RealSense depth + edge compute | AI-datacenter (CPU/foundry) | **Existing vault page** — light humanoid note |
| **[[INOD]]** | Physical-AI / robotics *training data* (the feedstock for the brain) | [[AI-data-supply-chain]] anchor | **Existing vault page** — cross-ref (the data layer for embodied AI) |
| **NOVT** | 6-axis force/torque via ATI (Tier C — clean US pick) | Industrial precision-motion/photonics | **Not yet a vault page** — humanoid-first new ingest candidate |
| **VPG** | Force/strain sensing (Tier C) | Industrial precision sensing | **Not yet a vault page** — new ingest candidate |
| **RRX** | Motors / motion (commoditizing core) | Industrial motion | **Not yet a vault page** — watch |

**The cleanest multi-thesis chokepoint: rare-earth NdFeB magnets ([[MP]]).** The same China concentration that constrains drone motors and AI-datacenter power-semiconductor magnets constrains humanoid actuators — **one chokepoint, three demand drivers.** **[[china-exposure]] overlay:** the humanoid value chain is the *most* China-concentrated in the entire vault (~63% of the chain, ~90% of magnets).

---

## Positioning judgments for the tracked universe

Calibrated reference points for how each US-listed name fits the frameworks. **Current views; primary-source evidence should refine, not overwrite them. All figures Tier-3 — verify at ingest. No `humanoid_tier` field is codified (H2); placements are prose. Apply the H6 needle-mover screen to every cross-over name.**

| Ticker | Chokepoint position (H1 tier) | Durability (H5) | US access | Humanoid-revenue reality | Current thesis fit |
|---|---|---|---|---|---|
| **[[MP]]** | Materials substrate — magnets (A) | **Very high (geology)** | 🟢 | *Optionality* — humanoid is incremental on a defense+EV magnet business | **Strongest enabler** — the cleanest US chokepoint; triple-thesis; already a vault page (add humanoid framing) |
| **NOVT** | High-end sensing — 6-axis F/T via ATI (C) | Medium–high, rising | 🟢 | *Optionality on legacy industrial automation* — verify mix at ingest | **Cleanest new US pick the banks miss** — force/torque the rising layer |
| **VPG** | High-end sensing — force/strain (C) | Medium–high | 🟢 | *Optionality on legacy precision sensing* | Real US sensor exposure; smaller/awkward; verify humanoid mix |
| **RRX** | Motors / motion (F) | Low–moderate | 🟢 | Diffuse; motion is commoditizing | Cleanest US motion play, but commoditizing layer — watch |
| **[[NVDA]]** | The brain (E) | Very high moat | 🟢 | *Immaterial incremental* (GS scores humanoid opportunity 1) | Already owned via datacenter — **don't double-count**; light humanoid note only |
| **[[INTC]]** | Vision (RealSense) + edge (E/F) | Low–moderate | 🟢 | Immaterial | Light note; primarily an AI-datacenter/foundry story |
| **TSLA** | Maker w/ in-house brain | Software-moat bet | 🟢 | The maker — Optimus is one leg of a huge auto/energy co. | Maker-with-a-brain (not a hardware chokepoint); not currently a vault page |
| **OUST / HSAI / INVZ / LAZR** | Vision/LiDAR (F) | Low–moderate (route-risk) | 🟢 (HSAI = China ADR) | Speculative; vision-vs-LiDAR risk | Higher-beta optionality, not structural — watch only |
| **Harmonic Drive (6324.T)** | Reducers (B) | High (precision) | 🔴 Japan | The purest reducer chokepoint | Best pure-play, *awkward to own* — map, don't ingest (no clean US ADR) |
| **Schaeffler (SHA.DE)** | Roller screws (B) | High (precision) | 🟡 Germany | Best Western screw exposure | Foreign — map; possible 🟡 ingest if access acceptable |
| **HIWIN (2049.TW); Nidec (6594.T); Lynas (LYC.AX)** | Screws / motors / magnets | High–moderate | 🟡 foreign | Foreign pure-plays | Map; awkward access |
| **LeaderDrive / Sanhua / Tuopu / Inovance / Zhaowei / Hengli / CATL / Sunny / RoboSense / Hesai** | Reducers / assembly / hands / motors / vision / battery | mixed | 🔴 China A/HK | China-dominated layers | **Map, don't pretend investable** — the China-concentration evidence base |

**Private / un-investable (mark and monitor):** Figure AI ($39bn), 1X, Agility, Apptronik, Sanctuary, Maxon, DJI/Livox, Unitree (pre-STAR-IPO), UBTech (HK-listed). **As with Defense, the best pure-play capability is often not publicly investable — a structural feature, not a temporary gap.**

**Prioritized first deep-dives:** **MP** (graduate the humanoid-magnet angle on the existing page + [[rare-earth-magnet-chokepoint]]), then **NOVT** (the clean US sensor pick), then **VPG** / **RRX**; **NVDA** carries a light humanoid-optionality note only.

---

## How the LLM should use these frameworks

1. **For first-pass categorization:** place each humanoid company in its value-chain position (H1), its value-capture tier letter (H2), and its chokepoint position + durability (H5). **No `humanoid_tier` frontmatter field** — names land `outside` the existing frameworks + theme-anchored ([[INOD]] precedent); the US-listed accessibility flag lives in prose.

2. **Lead with the central tension (H2/H5):** the strongest chokepoints have the worst US-listed access. Always pair a chokepoint's durability with its accessibility. The vault's edge is surfacing the *edges the banks underweight* — the materials substrate (MP) and high-end sensors (NOVT/VPG).

3. **Apply the needle-mover screen to every cross-over name (H6).** Quote the humanoid-revenue mix; distinguish pure-play vs cross-over (optionality) vs immaterial beneficiary. Never call a name a "humanoid play" without revenue-mix evidence. Distinguish booked orders from capacity announcements from narrative (many Optimus-supplier claims are Chinese trade-press — reported, not OEM-confirmed).

4. **Separate direction from timing (H3).** The automation direction is credible; near-term volumes are tiny (low-thousands 2026). Lead with "early-innings optionality," treat all TAM/unit/cost figures as Tier-3 projections, and attribute BOM figures to the right bank.

5. **Score chokepoints on durability basis, not order book (H5).** Physics/geology > precision-manufacturing > integration. Flag the magnet counter-signals (BofA machine-tools view; magnet-free-motor R&D) and the reducer/screw commoditization clock so the chokepoint thesis stays falsifiable.

6. **Handle dual/triple-thesis nodes per H7.** For MP/NVDA/INTC (existing vault pages), add humanoid framing to the existing page rather than duplicating; MP becomes a triple-thesis node. NOVT/VPG/RRX, if created, are humanoid-first new pages (`outside` + theme-anchored).

7. **Treat the anchor reports as Tier 3.** `raw/research/humanoid-robot-primer-report.md` + `humanoid-robot-high-value-subsystems-research.md` are Vic-commissioned synthesis on the Goldman value-chain work — attribute, paraphrase in wiki voice, and verify quantitative claims against primaries at ingest. Vault primary-source findings win on conflict.

8. **The frameworks evolve, and the domain is scoped to broaden.** Humanoid-first now; the physical-AI superset (quadrupeds, AMRs, cobots) is the planned next broadening — the chokepoints are general-robotics, so it's additive. If evidence across ingests consistently challenges a placement, raise it as a proposal for Vic — these frameworks are **human-owned scaffolding** (same convention as the other two frameworks files).

9. **Cross-reference `wiki/_thesis-humanoid-robot.md` as the anchor.** When framework and thesis diverge, raise it to Vic — don't silently reconcile. The AI-datacenter and Defense anchors remain untouched by this file.

---

**Note on this creation (2026-06-05):** **v0.1 DRAFT** drafted via Vic-authorized collaborative drafting as the companion frameworks file to `wiki/_thesis-humanoid-robot.md` (the vault's third thesis domain). **For Vic to shape, finalize, and commit; after that, default human-ownership resumes.** Sourced from two Tier-3 reports (`raw/research/humanoid-robot-primer-report.md` + `humanoid-robot-high-value-subsystems-research.md`) on Goldman's humanoid value-chain work, plus cross-bank corroboration (MS, JPM, BofA, McKinsey, Jefferies). Mirrors the other two frameworks files' structure (value-chain flow → value-capture tiers → demand map → structural-vs-cyclical → chokepoint quality gradient → quality/needle-mover screen → cross-thesis overlap → positioning judgments → LLM application). Humanoid-first scope; the physical-AI broadening is sequenced for future expansion. The AI `frameworks.md` (v10.1) and Defense `frameworks-defense-drones.md` (v1.0) are untouched. **No `humanoid_tier` frontmatter field is codified** (held under YAGNI; revisit at the physical-AI broadening). The first theme under this anchor is `humanoid-robot-value-chain`.
