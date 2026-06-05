---
title: Humanoid Robot Anatomy & Supply Chain Study Guide
source_chart: Goldman Sachs "Mapping the Humanoid Robot Value Chain" (Exhibit 2)
purpose: Understand each robot subsystem + identify best-positioned / most investable companies per part
lens: chokepoint vs commoditizing; US-listed (IBKR) accessibility flagged throughout
date: 2026-06-05
---

# Humanoid Robot Anatomy & Supply Chain Study Guide

## How to read this guide

A humanoid is best understood as **five functional systems layered on a materials substrate**:

| System | Human analogy | Robot subsystems (from GS chart) |
|---|---|---|
| **1. Intelligence** | Brain | Foundation models, GPU/CPU compute |
| **2. Actuation** | Muscles + joints | Rotary actuators (reducers), linear actuators (screws), actuator assembly, motors |
| **3. Manipulation** | Hands | Dexterous hands / end-effectors |
| **4. Perception** | Eyes + skin + inner ear | Vision (camera/LiDAR), force/torque + tactile sensors, IMU |
| **5. Power** | Metabolism | Batteries, power electronics |
| **0. Substrate** | Bones + bloodstream | Rare-earth magnets, precision bearings, structural materials |

**The single most important framing:** value does **not** distribute evenly across these. ~33% of the bill of materials (BOM) sits in actuation (reducers + screws); the brain is where the moat is widest; and the binding physical chokepoint is the materials substrate (rare-earth magnets). Robot *makers* (integrators) are the layer most likely to commoditize — analogous to a Layer-0 hyperscaler that captures the demand but not the durable margin.

**Investability key used below:**
- 🟢 **US-listed / clean IBKR access** (NYSE/Nasdaq or liquid ADR)
- 🟡 **Accessible but awkward** (foreign primary listing, thin ADR, conglomerate dilution)
- 🔴 **Hard to own** (China A-share, HK-only, or private)

---

## SYSTEM 1 — INTELLIGENCE (the brain)

### 1A. Foundation models / "physical AI"
**What it is:** The vision-language-action (VLA) model that turns a camera feed + an instruction ("pick up that bin") into joint commands. This is the layer that made 2024–2026 the inflection — robots went from scripted motion to generalized reasoning. NVIDIA's Isaac GR00T, Cosmos world models, Tesla's FSD-derived stack, and Google DeepMind's robotics models are the reference points.

**Why it's hard:** Requires (a) massive simulation/synthetic data to train without breaking real hardware, (b) sub-100ms inference at the edge (a robot dropping a glass can't wait for a cloud round-trip), and (c) world models that generalize across unseen objects and environments. This is the widest moat in the entire stack — it compounds with data and compute scale.

**Best-positioned companies:**
- 🟢 **NVIDIA (NVDA)** — Isaac platform + Cosmos + GR00T foundation model. The only name spanning brain *and* compute. This is the picks-and-shovels winner; every maker that doesn't build its own stack rents NVIDIA's.
- 🟢 **Alphabet (GOOGL)** — DeepMind robotics models; powers Boston Dynamics' Atlas reasoning.
- 🟢 **Tesla (TSLA)** — vertically integrated FSD→Optimus stack; the only maker with a credible in-house brain.
- 🟢 **Meta (META)** — open research (world models, embodied AI), less commercialized.
- 🔴 OpenAI (private), iFlytek (China), Huawei (private/China).

**Chokepoint verdict:** Structural. But for *you*, this overlaps almost entirely with your existing AI-datacenter NVDA/GOOGL exposure — a robotics allocation here is double-counting, not diversifying.

### 1B. Compute (GPU / CPU / edge SoC)
**What it is:** The physical inference hardware onboard. NVIDIA's Jetson Thor is the de facto humanoid "robot computer." Edge constraints (power budget, thermal, latency) make this distinct from datacenter compute.

**Best-positioned companies:**
- 🟢 **NVIDIA (NVDA)** — Jetson Thor dominates onboard inference.
- 🟢 **Intel (INTC)** — RealSense + some edge compute; weaker position.
- 🟢 **Ambarella (AMBA)** — edge AI vision SoCs; *interesting but moat thinning* as NVIDIA Jetson/Thor absorbs the edge-vision use case. Watch, don't anchor.

**Chokepoint verdict:** Structural but converging on NVIDIA — same caveat as 1A re: double-counting your datacenter book.

---

## SYSTEM 2 — ACTUATION (muscles + joints) — *the ~33%-of-BOM core*

This is the mechanical heart of a humanoid and the part most investors underweight because it's unglamorous. A humanoid needs **40+ actuators**. Two architectures dominate:

### 2A. Rotary actuators (harmonic / strain-wave reducers)
**What it is:** A rotary actuator = motor + gearbox (reducer) that converts a fast, low-torque motor spin into slow, high-torque joint rotation. The reducer is the precision bottleneck. The dominant type is the **harmonic drive (strain-wave gear)** — a flexible toothed cup that meshes to produce huge reduction ratios in a tiny package with near-zero backlash.

**Why it's hard:** Strain-wave gears require micron-level precision grinding and metallurgical know-how. Backlash, durability over millions of cycles, and torque density are the hard tradeoffs. Decades of process IP protect incumbents.

**Best-positioned companies:**
- 🟡 **Harmonic Drive Systems (6324.T, Japan)** — the global gold standard in strain-wave reducers. Genuine chokepoint, but Japan-primary listing; no clean US ADR. The purest expression of this chokepoint is awkward to own.
- 🔴 LeaderDrive, Shuanghuan (002472.SZ), Zhongda Leader (002896.SZ), FORE Intelligent — China domestic-substitution plays, A-share only.
- 🔴 Sling, Reach Machinery, Laiful, Picea Motion — niche/private.

**Chokepoint verdict:** Structural chokepoint, but **Western investors are largely locked out** — the best names are Japanese or Chinese. This is a genuine gap in the US-listed universe.

### 2B. Linear actuators (planetary roller screws / ball screws)
**What it is:** Converts rotary motion into linear push/pull (e.g., the "calf" actuators that extend a leg). **Planetary roller screws (PRS)** are replacing ball screws because they handle far higher loads and last longer — critical for a robot doing millions of duty cycles.

**Why it's hard:** PRS need ~5-micron precision grinding on specialized thread grinders (mostly imported from Japan/Europe), aerospace-grade alloys, and heat treatment. Only a handful of foundries globally can make the raw material. Tesla's Optimus uses four PRS in *each calf*; lead times ballooned to 26 weeks at one point. This is a real, current supply bottleneck.

**Best-positioned companies:**
- 🟡 **Schaeffler (SHA.DE, Germany)** — the leading Western bearings/actuator group moving aggressively into humanoid actuators; preferred actuator supplier to several Western platforms. Best Western expression, but German listing.
- 🟡 **HIWIN (2049.TW, Taiwan)** — major ball-screw / linear-guide maker; reported Boston Dynamics supplier. Taiwan-primary.
- 🔴 **Hengli Hydraulic (601100.SS)** — first-mover on PRS capacity in China; A-share.
- 🔴 **Beite / Shanghai Beite, Wuzhou Spring** — China PRS capacity build-out; A-share.
- 🔴 Nippon Thompson (Japan), Rollvis (Swiss, private) — niche precision, near-capacity.

**Chokepoint verdict:** **Highest-conviction chokepoint on the chart by BOM weight, worst US-listed access.** PRS is "high barriers + domestic-substitution + cost-reduction" — structurally attractive, but China/Taiwan/Germany own it. The investable Western thesis here is mostly Schaeffler or a future US pure-play that doesn't yet exist.

### 2C. Actuator assembly / integrated modules
**What it is:** Companies that package motor + reducer + sensor + controller into a drop-in joint module sold to makers.
- 🔴 **Sanhua (002050.SZ)**, **Tuopu (601689.SS)** — China auto-parts groups pivoting to actuator assembly; A-share only.

**Chokepoint verdict:** Assembly is the part most likely to commoditize (it's integration, not core IP). Lower priority.

### 2D. Motors (the thing the reducer/screw is bolted to)
**What it is:** The electric motor itself — usually frameless torque motors (simpler) or coreless motors (harder, higher performance). Every actuator contains one.
- 🟢 **Regal Rexnord (RRX)** — leading US supplier of motors, gearing, linear actuators. Cleanest US-listed motion play.
- 🟢 **Sensata (ST)** — sensors + electrification components.
- 🟡 **Nidec (6594.T, Japan)** — global motor leader; ADR exists but thin.
- 🔴 Inovance, Leadshine, Moons' Electric — China A-share.

---

## SYSTEM 3 — MANIPULATION (dexterous hands)

**What it is:** The end-effector. A dexterous hand is arguably the *hardest single subsystem* — it packs many tiny actuators, tendons, and tactile sensors into a human-sized envelope with many degrees of freedom. Figure's latest hand reportedly detects forces as small as ~3 grams.

**Why it's hard:** Miniaturization (you're fitting actuators + sensors into a finger), tendon routing, tactile feedback, and cost all fight each other. This is where "the robot can see but can't reliably grasp" failures concentrate. Likely the last subsystem to mature.

**Best-positioned companies:**
- 🟡 **Maxon (Swiss, private)** — premium micro-motors for hands; not directly investable.
- 🔴 **Moons' Electric (603728.SS)**, **Inovance (300124.SZ)**, **Zhaowei (003021.SZ)**, **Leadshine (002979.SZ)**, **Leili**, **Veichi**, **RoboSense (HK)**, **FORE Intelligent**, **Paxini** — overwhelmingly China A-share / HK.

**Chokepoint verdict:** Technically the highest-value future subsystem, but the listed pure-plays are almost entirely Chinese. Hard to own cleanly; watch for a Western entrant.

---

## SYSTEM 4 — PERCEPTION (eyes + skin + balance)

### 4A. Force / torque + tactile sensors (the "skin" and proprioception)
**What it is:** Six-axis force/torque sensors in the wrists/ankles let the robot feel how hard it's pushing; tactile sensors in the fingers enable delicate grasping; IMUs (accelerometer + gyro) provide balance. A single Optimus prototype reportedly used ~28 discrete sensors. Sensor density is the fastest-growing part of the BOM as robots leave cages.

**Why it's hard:** Six-axis force sensing requires precise calibration and drift compensation; tactile sensing at gram-level resolution across a whole hand is an unsolved cost problem.

**Best-positioned companies:**
- 🟢 **Novanta (NOVT)** — owns **ATI Industrial Automation**, a leading six-axis force/torque sensor maker. *This is one of the cleanest US-listed picks on the entire chart and it isn't even highlighted by Goldman.*
- 🟢 **Vishay Precision Group (VPG)** — precision force/strain sensing; US-listed.
- 🟡 **Murata (6981.T)**, **TDK (6762.T)** — Japanese passives/sensor giants (IMUs, MLCCs); ADRs exist.
- 🔴 Kunwei — China.

**Chokepoint verdict:** **Underappreciated US-listed sweet spot.** NOVT and VPG give you force/torque exposure without the China access problem. Structural as sensor count per robot rises.

### 4B. Vision (cameras / LiDAR / depth)
**What it is:** The robot's eyes — RGB cameras, depth cameras, and sometimes LiDAR for spatial mapping. There's an active architectural debate (vision-only à la Tesla vs. LiDAR-assisted), which matters for who wins.

**Why it's hard:** Cost vs. resolution vs. power. LiDAR has been a brutal industry (many bankruptcies/mergers). Tesla's vision-only bet, if it wins, *shrinks* the LiDAR TAM for humanoids.

**Best-positioned companies:**
- 🟢 **Ouster (OUST)** — merged with Velodyne; leading US-listed industrial LiDAR.
- 🟢 **Hesai (HSAI)** — Chinese LiDAR leader but US-listed ADR (liquid).
- 🟢 **Innoviz (INVZ)**, **Luminar (LAZR)** — US-listed LiDAR; both speculative / execution-dependent.
- 🟡 **Sunny Optical (2382.HK)** — dominant camera-module maker; HK-listed.
- 🔴 **DJI / Livox** (private China), **Orbbec**, **RoboSense (HK)** — depth/LiDAR, hard to own.

**Chokepoint verdict:** Several US-listed options, but LiDAR is *not* a clean chokepoint — it's competitive, capital-destructive, and at architectural risk if vision-only wins. Treat as higher-beta optionality, not structural.

---

## SYSTEM 5 — POWER (batteries)

**What it is:** Energy storage + power electronics. Humanoids are power-hungry; runtime and hot-swap architectures are active constraints.

**Best-positioned companies:**
- 🔴 **CATL (300750.SZ / also HK)** — global battery leader; A-share primary, HK access improving.
- 🟡 **Samsung SDI (Korea)**, **Panasonic (6752.T, Japan)** — foreign-listed.

**Chokepoint verdict:** Battery tech is shared with EVs (not humanoid-specific), so it's a diluted way to play robotics. Lower priority; no clean US-listed pure-play.

---

## SYSTEM 0 — THE MATERIALS SUBSTRATE (the real binding chokepoint)

**Goldman's chart underplays this** — it's folded inside "actuators" — but it's the hardest physical bottleneck in the whole stack.

### Rare-earth permanent magnets (NdFeB / NdPr)
**What it is:** High-torque actuators need rare-earth permanent magnets for power density. Each humanoid needs roughly **1.3–4 kg** of NdFeB/NdPr magnets.

**Why it's the chokepoint:** China controls ~69% of rare-earth mining and **~90% of magnet processing/refining**. China's 2025 export restrictions *directly delayed Optimus production*. Musk's framing — production "moves as fast as the slowest, least lucky component" — is a tacit admission that this, not AI, is the binding constraint.

**Best-positioned companies:**
- 🟢 **MP Materials (MP)** — the only US-listed integrated rare-earth miner + magnet producer scaling domestic capacity; Pentagon equity backing + price-floor support. **The single cleanest US-listed chokepoint expression on this entire topic.** Cross-cuts EVs + defense + humanoids.
- 🟡 **Lynas (LYC.AX, Australia)** — largest non-China rare-earth producer; foreign-listed.
- 🔴 JL Mag (6680.HK) — Chinese magnet maker.

**Chokepoint verdict:** **Structural, binding, and uniquely investable via MP.** If you own one thing off this chart through a US listing, the materials chokepoint is the most defensible.

---

## Synthesis — where the durable, *ownable* value actually sits

Mapping the chart against IBKR/US-listed accessibility produces a sharp asymmetry:

| Subsystem | Value durability | US-listed access | Net for you |
|---|---|---|---|
| Foundation models / compute | Highest moat | 🟢 NVDA, GOOGL, TSLA | **Already own via datacenter book — don't double-count** |
| Rotary actuators (reducers) | High (BOM core) | 🔴 Japan/China only | Chokepoint you can't cleanly own |
| Linear actuators (screws) | High (BOM core) | 🟡 Schaeffler only | Best Western proxy is German |
| Dexterous hands | High (future) | 🔴 China/private | Watch for a Western entrant |
| **Force/torque + tactile sensors** | Medium-high, rising | 🟢 **NOVT, VPG** | **Underappreciated clean US pick** |
| Vision / LiDAR | Low-medium, competitive | 🟢 OUST, HSAI, INVZ, LAZR | Higher-beta optionality, architectural risk |
| Batteries | Low (EV-shared) | 🔴 none clean | Diluted play, skip |
| **Rare-earth magnets** | **Structural / binding** | 🟢 **MP** | **Cleanest US chokepoint expression** |

**The three takeaways:**

1. **The mechatronic core (actuators = ~33% of BOM) is the strongest chokepoint and the worst US-listed access.** This is the central tension of investing in humanoids from a US brokerage. The best pure-plays are Japanese (Harmonic Drive), Taiwanese (HIWIN), German (Schaeffler), or Chinese A-shares. There is a real gap in the market for a US-listed precision-actuator pure-play.

2. **The two cleanest US-listed picks aren't even highlighted on Goldman's slide:** **NOVT** (force/torque sensors via ATI) and **MP** (rare-earth magnet chokepoint). Both let you own a genuine bottleneck without the China-access problem.

3. **The makers list (left column) is the commoditization trap** — 40+ integrators, mostly Chinese, racing to the same cost-down. The exception is the maker that owns its own brain (Tesla) — that's a software-moat bet, not a hardware-chokepoint bet.

---

## Open questions to pressure-test next

- Does **vision-only win over LiDAR** for humanoids? If yes, the LiDAR names (OUST/HSAI/INVZ/LAZR) lose a major TAM leg.
- Is there a **near-term US/Western listed precision-actuator or PRS pure-play** emerging? This is the highest-value gap. (Parallels your glass-substrate "no clean US pure-play" problem.)
- How fast does **magnet-free motor R&D** (induction / electrically-excited synchronous, FeN magnets) advance? It would partially de-risk the rare-earth chokepoint — and undercut the MP thesis.
- **NOVT/VPG concentration:** how much of force/torque sensor revenue is humanoid vs. legacy industrial automation? Need revenue-mix evidence before treating either as a "humanoid play" (same discipline as your AAOI/MRVL layer-straddling rule).
