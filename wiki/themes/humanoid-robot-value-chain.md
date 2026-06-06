---
type: theme
tickers: [MP, NVDA, INTC, INOD, NOVT, VPG]
last_updated: 2026-06-06
---

# Humanoid Robot Value Chain — where the durable value sits

*Tier 3-anchored theme (per CLAUDE.md Section 3.13). The **first vault page of the third thesis domain — Humanoid Robots** (anchors: `wiki/_thesis-humanoid-robot.md` + `raw/notes/frameworks-humanoid-robot.md`, both v0.1 drafts). Anchored on Goldman Sachs' humanoid value-chain work (Exhibit 2 = the enabler map; Exhibit 5 = the component exposure ranking) + two commissioned research reports (`raw/research/humanoid-robot-primer-report.md` + `humanoid-robot-high-value-subsystems-research.md`), with cross-bank corroboration (Morgan Stanley, JPM, BofA, McKinsey, Jefferies). All figures are Tier-3 — verify against primaries before treating as load-bearing; BOM splits are attributed to the originating bank. Structural framing only (value-capture / what-would-have-to-be-true), not buy/sell.*

## Scope & forward path

This is a **value-capture / bill-of-materials map** of the humanoid robot — which subsystems are durable chokepoints versus commoditizing — *not* a logistics flow. Scope is **humanoid-first**; the chokepoints (magnets, gears, screws, sensors, motors) are general-robotics parts, so the planned broadening to **"physical AI"** (quadrupeds, autonomous mobile robots, cobots) is additive, not a re-scope. The only name ingested at primary to date is [[MP]] (the magnet chokepoint, already a vault page); the rest are referenced by name pending ingest.

## Thesis relevance

The humanoid thesis mirrors the vault's other two: value concentrates at **structural chokepoints**, not at the platform (robot-maker) layer, which is commoditizing the way drone airframes did. The robot you can photograph is the disposable part; the harmonic gear, the roller screw, the rare-earth magnet, the force-torque sensor, and the AI brain are where pricing power lives. The honest, uncomfortable finding up front: **the strongest chokepoints have the worst US-listed access** — the best pure-plays are Japanese, German, Taiwanese, Chinese, or private — so a US book can only cleanly own the *edges* the banks underweight.

## The value-capture gradient

A humanoid is five functional systems on a materials substrate, with the AI brain running across the top. Value does **not** distribute evenly — actuators are **~33–60% of the bill of materials** (JPM: reducers + screws ≈ 33%; McKinsey: full actuators 40–60%), and the binding physical bottleneck is the magnet substrate.

Goldman's Exhibit 5 scores each component 1–3 on six criteria (content value in BOM, certainty of tech choice, technology barrier, manufacturing barrier, capacity flexibility, % incremental opportunity from humanoids), summed out of 18:

Goldman's ranking groups into **three tiers** — and its two headline picks sit at the top:

| Tier | Component | GS score | Read |
|---|---|---|---|
| **High-value mechatronic core** | **Harmonic reduction gear** ★ | **16** | GS **top pick** ("growth") — high content value + high tech *and* manufacturing barriers + high humanoid demand |
| | **Dexterous hand module** | **15** | High value + high barriers, but **lowest certainty-of-tech-choice** (architecture unsettled) — route-risk, so *not* a headline pick |
| | **Actuator assembly** ★ | **14** | GS's other **headline pick** ("adoption certainty") — highest certainty-of-tech-choice, but low tech barrier (integration, not core IP) |
| | **Planetary roller screw** | **14** | High content value + high mfg barrier; knock is **low capacity-flexibility** (precision-grinding constraint) = pricing power |
| **Middle (solid, a notch below)** | **Sensors (6-axis force/torque, tactile)** | **13** | Highest *tech barrier* in this tier; the high-precision end is a chokepoint |
| | **GPU/CPU** | **13** | Top barriers but **lowest incremental-humanoid opportunity (1)** — humanoids tiny vs its data-center business; strategic, not a pure-play |
| | **Coreless motor** | **13** | High volume, low tech moat — commoditizing |
| | **Frameless torque motor** | **13** | High volume, low tech moat — commoditizing |
| **Bottom (commoditized / "ready")** | **Battery** | **12** | Lowest content value + lowest incremental humanoid opportunity — EV-shared |
| | **Camera / LiDAR** | **12** | Lowest content value; parts "mostly ready" — commoditized |

★ = Goldman's two explicit headline picks. The **high-value layers are the mechatronic core** (the four top rows); reduce it to Goldman's stated preference and it's **harmonic reduction gears (growth) + actuator assembly (adoption certainty)**.

**The chokepoint quality gradient (the vault's overlay):** physics/geology (magnets) > precision-grinding/metallurgy (harmonic gears, roller screws) > integration (actuator assembly) > commodity (basic motors, vision, battery). Score a name on *what makes its position durable*, not on today's order book.

## The central tension — strongest chokepoints, worst US-listed access

This is the defining feature of investing in humanoids from a US brokerage:

- **The strongest mechatronic chokepoints are non-US-listed.** The best harmonic-gear pure-play is Japanese (Harmonic Drive Systems, 6324.T, no clean US ADR); the best roller-screw exposure is German (Schaeffler, via Ewellix) or Taiwanese (HIWIN); the rest of the actuator complex is overwhelmingly Chinese A-share (LeaderDrive, Sanhua, Tuopu, Inovance, Hengli) or private (Maxon).
- **The brain you already own.** Foundation models + compute (NVDA Isaac/GR00T + Jetson Thor; GOOGL; Tesla) are the widest moat — but for this vault that overlaps almost entirely with the existing AI-datacenter [[NVDA]]/[[INTC]] book, and GS scores its *incremental* humanoid opportunity at 1 (a rounding error vs datacenter AI). A robotics allocation here is double-counting, not diversifying.

## Goldman's preference + our refinement

**Goldman's "deserves investment"** = the high-value **mechatronic core** — the four top-ranked layers (harmonic gears 16, dexterous hands 15, actuator assembly 14, roller screws 14). Goldman's slide narrows it to **two explicit headline picks: harmonic reduction gears** (highest growth potential + barriers) **and actuator assembly** (highest adoption certainty). Dexterous hands (high value, but unsettled architecture) and roller screws (capacity-constrained) round out the core but aren't the two it most prefers.

**Our refinement** adds the two cleanest *US-listed* expressions GS's component-ranking underweights:
- **The materials substrate — rare-earth magnets.** GS folds magnets *inside* "actuators," but every motor needs NdFeB permanent magnets (~0.9–4 kg/robot, ~2× an EV; ~40+ motors per humanoid), and China controls ~90% of finished magnets. **[[MP]] is the one clean US-listed play** — and a **triple-thesis node** (defense + EV/wind + humanoid). See [[rare-earth-magnet-chokepoint]].
- **The high-end sensor layer (6-axis force/torque).** GS ranks it mid-tier (13), but it's the rising, US-investable sweet spot via **[[NOVT]]** (owns ATI Industrial Automation) and **[[VPG]]** (Vishay Precision Group) — the exact names in GS's sensor row, just not flagged as a top pick. *Caveat from both ingests (S138/S139): each is a clean US name, but force/torque/strain sensing is a small slice of a diversified precision-tech business — the real vault exposure is AI-datacenter equipment, not humanoid sensing. VPG is the one name that actually **quantifies** humanoid revenue (~$600K Q1 2026, ~$5M 2026 target, ~50% CAGR); NOVT never sized it.*

## Value-layer map (stock → value layer → investability)

Every company on Goldman's two exhibits, organized by value layer (rank-ordered by the Exhibit 5 exposure score), tagged by investability. **🟢 US-listed** (incl. foreign ADRs like HSAI/INVZ) · **🟡 foreign-listed** (Japan/Germany/Korea/Taiwan/Australia) · **🔴 China A-share / HK or private** (map, don't pretend investable). The materials substrate + the brain are appended (Exhibit 2 layers GS doesn't score in Exhibit 5).

| Value layer | GS rank | Companies (by investability) | Cleanest US-investable |
|---|---|---|---|
| **Harmonic reduction gear** | 16 | 🟡 Harmonic Drive (Japan) · 🔴 LeaderDrive, **Shuanghuan**, **Zhongda Leader**, Sling, Reach Machinery, FORE Intelligent, Laiful, Picea Motion | — none clean |
| **Dexterous hand module** | 15 | 🟡 Maxon (Swiss, private) · 🔴 Zhaowei, Inovance, Moons' Electric, LeaderDrive, Fortior, RoboSense, Leadshine, Leili, Veichi, FORE Intelligent, Paxini | — none clean |
| **Actuator assembly** | 14 | 🔴 **Sanhua**, **Tuopu** | — none clean |
| **Planetary roller screw** | 14 | 🟡 Schaeffler (Germany), HIWIN (Taiwan) · 🔴 Sanhua, LeaderDrive, Beite, XCC, Seenpin, Best, Hengli Hydraulic, Zhenyu, CSB, Shuanglin | — none clean |
| **Sensors (force/torque/tactile)** | 13 | 🟢 **[[NOVT]]** (via ATI), **[[VPG]]** (Vishay Precision) · 🟡 Murata, TDK (Japan) · 🔴 Kunwei | **[[NOVT]], [[VPG]]** |
| **GPU / CPU** | 13 | 🟢 [[NVDA]], [[INTC]] — *already owned via the AI book* | NVDA, INTC (don't double-count) |
| **Coreless motor** | 13 | 🟢 Regal Rexnord (RRX, adjacent) · 🔴 Moons' Electric, Zhaowei, Leadshine, Leili, Veichi | RRX (adjacent) |
| **Frameless torque motor** | 13 | 🟡 Nidec (Japan) · 🟢 RRX (adjacent) · 🔴 Kinco, Haozhi, Veichi | RRX (adjacent) |
| **Battery** | 12 | 🟡 Samsung SDI (Korea), Panasonic (Japan) · 🔴 CATL | — none clean |
| **Camera / LiDAR** | 12 | 🟢 Ouster (OUST), Hesai (HSAI, ADR), Innoviz (INVZ, ADR), Luminar (LAZR), [[INTC]] · 🔴 DJI/Livox, Orbbec, RoboSense, Sunny Optical | OUST / HSAI / INVZ / LAZR (higher-beta) |
| **Foundation models / brain** | *(Exh. 2; not scored in 5)* | 🟢 [[NVDA]], TSLA, GOOGL, META, OpenAI (private) · 🔴 iFlytek, Huawei | already owned (NVDA/GOOGL/META) |
| **Materials substrate (magnets)** | *(GS folds into "actuators")* | 🟢 **[[MP]]** · 🟡 Lynas (Australia) | **[[MP]]** — the GS-miss; already in vault |

*Investability flags are this vault's classification (the GS slide's color key is the authority for nationality); a few obscure names (Picea Motion; Sanhua/Tuopu HK-listing status) carry a verify-at-source caveat.*

**What the map shows — the inversion, made concrete.** The four **highest-value layers** (harmonic gear 16, dexterous hands 15, actuator assembly 14, roller screw 14) have **no clean US-investable name** — they're China A-share or Japanese/German. The **US-investable** names cluster in the **lower** layers (sensors 13, camera/LiDAR 12), plus the materials substrate (**MP**, which GS hides) and the already-owned brain. The value-layer ranking and the investability ranking run in opposite directions.

**Ingest priority that follows from the map:**
1. **[[MP]]** — the one US-investable *high-value* chokepoint (materials substrate); already in vault ✓ (humanoid-magnet graduation).
2. **[[NOVT]]** ✓ (S138), **[[VPG]]** ✓ (S139) — the US sensors layer, both ingested. Both are clean US names where the needle-mover screen fired: each carries the sensor/strain exposure as a small slice of a diversified precision-tech business, and both landed `equipment_tier 4` + theme-anchored humanoid (the real vault exposure is AI-datacenter equipment). NOVT never sized humanoid ("prototype phase," 2027); **VPG quantifies it** (~$600K Q1 2026, ~$5M 2026 target, ~50% CAGR) — disclosed but ~1.5% of revenue. See the NOVT-vs-VPG comparison on [[VPG]].
3. **OUST** (+ HSAI / INVZ / LAZR) — camera/LiDAR, higher-beta optionality with vision-vs-LiDAR route risk.
4. **The top-layer China chokepoints** (Sanhua / Tuopu / Shuanghuan / Zhongda + Harmonic Drive / Schaeffler) → covered via a consolidated **`humanoid-actuator-chokepoint`** page (un-investable structural coverage), **not** company-page ingests — the same "un-investable names live in chokepoint/theme pages" precedent the vault uses for Anduril/Figure.

## How real, how big (the early-innings discipline)

Lead with realistic near-term volumes, not the 2035 TAM: Omdia estimates Tesla / Figure / Agility shipped **~150 units *each* in 2025**; realistic 2026 output is low-thousands. Goldman's base case is a **$38bn TAM by 2035** (~1.4M units; blue-sky ~$205bn); Morgan Stanley reaches for ~$5tn by 2050. The single biggest TAM-upgrade driver was a **~40% cost decline** plus *"AI progress surprised us the most"* (Goldman) — end-to-end vision-language-action models replacing hand-coded behavior.

**The central demand-side risk — the order-vs-capacity gap:** Goldman's own supplier survey found Chinese suppliers building 100k–1M-unit capacity *without confirmed binding orders* — a capacity-first gamble. The first sizable confirmed OEM order (Tesla Optimus Gen-3; Figure BotQ) would validate it; continued absence into 2H2026 signals overcapacity.

**Counter-signals to keep the chokepoint thesis falsifiable:** BofA's contrarian view that **machine tools, not magnets, are the near-term bottleneck**; **magnet-free-motor R&D** (induction / electrically-excited synchronous / FeN) that would de-risk *and undercut* the MP thesis; and the **harmonic/roller-screw commoditization clock** as Chinese challengers close the precision gap.

## China concentration

The humanoid value chain is the **most China-concentrated supply chain in the entire vault** — ~63% of the value chain (Morgan Stanley "Humanoid 100"), ~90% of finished magnets, ~88% of refined rare earths, ~40% of precision bearings/encoders. Building a Tesla Optimus without Chinese suppliers reportedly costs ~3× more. A heavy geopolitical overlay — see [[china-exposure]].

## Makers = the commoditization trap

The left side of Goldman's map is 40+ robot makers (Tesla, Figure, Boston Dynamics, Agility + a wall of Chinese names and state "Innovation Centers"). Forty integrators racing to a sub-$20k cost floor is the same signal as forty drone airframes — none is a durable moat; value migrates upstream to the chokepoints. This is the vault's [[drone-platform-commoditization]] pattern, a third time. The exception is the maker that owns its own brain (Tesla) — a software-moat bet, not a hardware-chokepoint bet.

## Cross-vault nodes

- **[[MP]]** — rare-earth magnets: now a **triple-thesis node** (defense motors + AI-datacenter cooling/power magnets + humanoid actuators). One chokepoint, three demand drivers — the cleanest multi-thesis node in the vault. See [[rare-earth-magnet-chokepoint]].
- **[[NVDA]]** — the robot brain/compute (Isaac/GR00T + Jetson Thor); already owned via the AI-datacenter book; humanoid is immaterial *incremental* upside (don't double-count).
- **[[INOD]]** — its disclosed physical-AI / robotics training-data growth vector is the *data feedstock* for the humanoid brain — the link from [[AI-data-supply-chain]] to embodied AI.

## Open questions (primary-source verification triggers)

1. **Needle-mover (the key one):** how much of NOVT / VPG / MP revenue is actually humanoid vs. legacy industrial automation / defense / EV? Humanoid is *optionality on a legacy business*, not a base case — verify the revenue mix at each ingest before calling any name a "humanoid play." **[[NOVT]] S138 + [[VPG]] S139 = two confirmations:** NOVT left humanoid unsized ("prototype phase," 2027); VPG sized it at ~$600K Q1 2026 / ~$5M 2026 target (~1.5% of revenue). Both real, both small, both AI-datacenter-equipment names first. The screen works.
2. **Vision-only vs LiDAR** — if Tesla's vision-only approach wins, the LiDAR TAM leg (OUST/HSAI/INVZ/LAZR) shrinks.
3. **The missing US precision-actuator pure-play** — does a US-listed harmonic-gear / roller-screw name emerge to fill the biggest access gap?
4. **Magnet-free motors** — does the R&D advance enough to de-risk (and undercut) the magnet chokepoint?
5. **Order-vs-capacity** — do confirmed OEM orders materialize into 2H2026, or does the capacity-first gamble bust?

## Source audit notes

- **Provenance + attribution.** Tier-3 synthesis anchored on Goldman's humanoid value-chain work (Exhibits 2 & 5) + two commissioned research reports (`raw/research/`), with cross-bank corroboration. The structural framework is scaffolding paraphrased in wiki voice — not human-owned canon. Per Section 2.2, report figures are Tier 3 with **verify-at-primary** status; only [[MP]]'s figures are primary-verified.
- **Attribution discipline.** BOM splits attributed to the originating bank (33% reducers+screws = JPM; 40–60% actuators = McKinsey; $38bn-2035 TAM = Goldman; ~63% China value chain = Morgan Stanley). Magnet-per-robot (~0.9–4 kg) and China-concentration %s are Tier-3 — verify against IEA / USGS / company filings.
- **Reported-not-confirmed.** Several OEM supplier-relationship claims (e.g., "exclusive Optimus supplier") come from Chinese-language trade press — reported, not OEM-confirmed (Section 3.3 disclosed/inferable/unknown).
- **Describe-don't-recommend.** The underlying reports carried 🟢/🔴 investability calls; stripped here to structural value-capture + accessibility framing per Section 2.1.

## Cross-references

- [[MP]] — the rare-earth-magnet chokepoint owner; the one US-listed, already-in-vault triple-thesis node (the day-one anchor).
- [[rare-earth-magnet-chokepoint]] — the owner-side chokepoint depth; humanoid actuators are the third major NdFeB demand driver.
- [[china-exposure]] — the geopolitical overlay; the humanoid chain is the most China-concentrated in the vault.
- [[drone-platform-commoditization]] — the "value migrates from makers to enablers" parallel (drones → AI-data → humanoids, a third time).
- [[AI-data-supply-chain]] / [[INOD]] — the physical-AI/robotics data feedstock for the humanoid brain.
- [[NOVT]] — the US sensor / precision-motion layer; ingested S138 as an AI-datacenter equipment name (`equipment_tier 4`) with humanoid as theme-anchored optionality — the needle-mover screen in action.
- [[VPG]] — the paired US sensor-layer name (Vishay Precision Group); ingested S139, also `equipment_tier 4` + theme-anchored humanoid. The one vault name that *quantifies* humanoid revenue; carries the NOVT-vs-VPG comparison.

## Change log

- **2026-06-06 (S139 — second humanoid name ingested):** [[VPG]] (Vishay Precision Group) ingested — the paired US sensor-layer name (#2 on the map, with NOVT). VPG bracketed at its mentions; added to `tickers`; ingest-priority #2 marked complete. VPG is the **first vault name to *quantify* humanoid revenue** (~$600K Q1 2026, ~$5M 2026 target, ~50% CAGR) — the disclosed-magnitude contrast vs NOVT (which never sized it); both landed `equipment_tier 4` + theme-anchored humanoid (~1.5% optionality). The needle-mover screen now has two confirmations.

- **2026-06-06 (S138 — first humanoid name ingested):** [[NOVT]] ingested as the first company off the value-layer map (sensor layer, ingest-priority #2). NOVT bracketed at its mentions; added to `tickers`. The ingest **confirmed Open Question #1 (the needle-mover screen)**: NOVT is a clean US name but humanoid is its *smallest* AI leg (unsized at filing level, "prototype phase," 2027) — its real vault exposure is the ~15% AI-datacenter semiconductor-equipment collective, so it landed `equipment_tier 4` + theme-anchored humanoid (no `humanoid_tier`). Also split the value-capture gradient's "Coreless / frameless motors" into two rows (both GS-13) to match Exhibit 5 + the value-layer map.

- **2026-06-06 (S137 — value-layer map):** Superseded the lighter "investable surface" bullets with a comprehensive **Value-layer map** — every company on Goldman's Exhibits 2 & 5, organized by value layer (rank-ordered), tagged by investability (🟢 US-listed / 🟡 foreign / 🔴 China-A·HK·private), with a "cleanest US-investable" column + the ingest-priority order. Makes the inversion concrete (top-value layers = un-investable China/Japan; US names cluster in lower layers + the MP magnet substrate). Tier-3 mapping, describe-don't-recommend; no `tickers` change (in-vault names unchanged; the rest plain text). Also (per a Goldman-value-layer note relayed by Vic) re-grouped the value-capture gradient table into Goldman's explicit **three tiers** (high-value mechatronic core / middle 13 / bottom 12) and marked the **two headline picks (★ harmonic gears + actuator assembly)** precisely. `last_updated` → 2026-06-06.

- **2026-06-05 (S136 — creation):** First vault page of the third thesis domain (Humanoid Robots), built on the v0.1 domain anchors (`_thesis-humanoid-robot.md` + `frameworks-humanoid-robot.md`). Tier-3-anchored on Goldman's humanoid value-chain work + two commissioned reports. Centerpiece: the value-capture gradient (GS Exhibit 5) + **the central tension — strongest chokepoints, worst US-listed access** + the two GS-misses ([[MP]] magnets, NOVT/VPG sensors). Attached to [[MP]] as the day-one anchor (humanoid-magnet graduation → triple-thesis); cross-refs [[rare-earth-magnet-chokepoint]], [[china-exposure]], [[drone-platform-commoditization]], [[INOD]]. No `humanoid_tier` codified (held under YAGNI). `tickers: [MP, NVDA, INTC, INOD]` (the in-vault names referenced; the rest plain text pending ingest). Describe-don't-recommend applied; all figures Tier-3, verify-at-primary.
