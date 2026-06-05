---
type: theme
tickers: [MP, NVDA, INTC, INOD]
last_updated: 2026-06-05
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

| Component | GS score | Read |
|---|---|---|
| **Harmonic reduction gear** | **16** | GS top pick ("growth") — high content value + high barriers + high humanoid demand |
| **Dexterous hand module** | **15** | High value, but lowest certainty-of-tech-choice (architecture unsettled) — route-risk |
| **Actuator assembly** | **14** | GS "adoption certainty" pick — highest certainty, but low tech barrier (integration, not core IP) |
| **Planetary roller screw** | **14** | Acute chokepoint — high mfg barrier, low capacity-flexibility = pricing power |
| **Sensors (6-axis force/torque, tactile)** | **13** | Highest *tech barrier* in its tier; the high-precision end is a chokepoint |
| **GPU/CPU** | **13** | Top barriers but **lowest incremental-humanoid opportunity (1)** — strategic, not a pure-play |
| **Coreless / frameless motors** | **13** | High demand, low tech barrier — commoditizing |
| **Battery** | **12** | Lowest content value + lowest incremental humanoid opportunity — EV-shared |
| **Camera / LiDAR** | **12** | Lowest content value; "mostly ready" — commoditizing |

**The chokepoint quality gradient:** physics/geology (magnets) > precision-grinding/metallurgy (harmonic gears, roller screws) > integration (actuator assembly) > commodity (basic motors, vision, battery). Score a name on *what makes its position durable*, not on today's order book.

## The central tension — strongest chokepoints, worst US-listed access

This is the defining feature of investing in humanoids from a US brokerage:

- **The strongest mechatronic chokepoints are non-US-listed.** The best harmonic-gear pure-play is Japanese (Harmonic Drive Systems, 6324.T, no clean US ADR); the best roller-screw exposure is German (Schaeffler, via Ewellix) or Taiwanese (HIWIN); the rest of the actuator complex is overwhelmingly Chinese A-share (LeaderDrive, Sanhua, Tuopu, Inovance, Hengli) or private (Maxon).
- **The brain you already own.** Foundation models + compute (NVDA Isaac/GR00T + Jetson Thor; GOOGL; Tesla) are the widest moat — but for this vault that overlaps almost entirely with the existing AI-datacenter [[NVDA]]/[[INTC]] book, and GS scores its *incremental* humanoid opportunity at 1 (a rounding error vs datacenter AI). A robotics allocation here is double-counting, not diversifying.

## Goldman's preference + our refinement

**Goldman's "deserves investment"** = the high-content-value mechatronic parts: **harmonic reduction gears** (growth), **actuator assembly** (adoption certainty), and **planetary roller screws** (chokepoint), with dexterous hands the high-upside/high-route-risk wildcard.

**Our refinement** adds the two cleanest *US-listed* expressions GS's component-ranking underweights:
- **The materials substrate — rare-earth magnets.** GS folds magnets *inside* "actuators," but every motor needs NdFeB permanent magnets (~0.9–4 kg/robot, ~2× an EV; ~40+ motors per humanoid), and China controls ~90% of finished magnets. **[[MP]] is the one clean US-listed play** — and a **triple-thesis node** (defense + EV/wind + humanoid). See [[rare-earth-magnet-chokepoint]].
- **The high-end sensor layer (6-axis force/torque).** GS ranks it mid-tier (13), but it's the rising, US-investable sweet spot via **Novanta (NOVT, owns ATI Industrial Automation)** and **Vishay Precision (VPG)** — the exact names in GS's sensor row, just not flagged as a top pick.

## The investable surface

- **🟢 Cleanest US-listed expressions (the edges the banks underweight):** **[[MP]]** (magnets — already in vault), **NOVT** (force/torque via ATI), **VPG** (force/strain).
- **🟢 US-listed, already-owned or commoditizing:** [[NVDA]] (brain/compute — *don't double-count*), [[INTC]] (RealSense/edge), TSLA (the maker with an in-house brain), Regal Rexnord (RRX — cleanest US motion/motor), Ouster/Hesai/Innoviz/Luminar (LiDAR — higher-beta optionality, vision-vs-LiDAR route risk).
- **🟡 Foreign-listed chokepoint pure-plays (awkward to own):** Harmonic Drive Systems (6324.T, Japan), Schaeffler (Germany), HIWIN (Taiwan), Nidec (Japan), Lynas (Australia).
- **🔴 China A-share / HK or private (map, don't pretend investable):** LeaderDrive, Sanhua, Tuopu, Inovance, Zhaowei, Hengli, CATL, RoboSense, Sunny Optical; Unitree (pre-IPO), UBTech; Figure AI, 1X, Maxon, DJI. *As with Defense, the best pure-play capability is often not publicly investable — a structural feature, not a temporary gap.*

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

1. **Needle-mover (the key one):** how much of NOVT / VPG / MP revenue is actually humanoid vs. legacy industrial automation / defense / EV? Humanoid is *optionality on a legacy business*, not a base case — verify the revenue mix at each ingest before calling any name a "humanoid play."
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

## Change log

- **2026-06-05 (S136 — creation):** First vault page of the third thesis domain (Humanoid Robots), built on the v0.1 domain anchors (`_thesis-humanoid-robot.md` + `frameworks-humanoid-robot.md`). Tier-3-anchored on Goldman's humanoid value-chain work + two commissioned reports. Centerpiece: the value-capture gradient (GS Exhibit 5) + **the central tension — strongest chokepoints, worst US-listed access** + the two GS-misses ([[MP]] magnets, NOVT/VPG sensors). Attached to [[MP]] as the day-one anchor (humanoid-magnet graduation → triple-thesis); cross-refs [[rare-earth-magnet-chokepoint]], [[china-exposure]], [[drone-platform-commoditization]], [[INOD]]. No `humanoid_tier` codified (held under YAGNI). `tickers: [MP, NVDA, INTC, INOD]` (the in-vault names referenced; the rest plain text pending ingest). Describe-don't-recommend applied; all figures Tier-3, verify-at-primary.
