# Thesis — Humanoid Robots (Embodied-AI Value Chain & Chokepoints)

**Last updated:** 2026-06-05
**Owner:** Vic (human-maintained; never edited by the LLM except by explicit Vic-authorized rework session)
**Status:** **v0.1 DRAFT** — third thesis domain in the stocks-wiki vault, parallel to the AI-datacenter thesis (`wiki/_thesis.md`) and the Defense & Drones thesis (`wiki/_thesis-defense-drones.md`). Drafted via Vic-authorized collaborative drafting (Vic-directed; agent-scaffolded) — **for Vic to shape and finalize.** Shares the vault's methodology, source hierarchy, and disciplines; does not replace or modify the other two anchors. **Scope: humanoid-first; broadens to "physical AI" / embodied AI later** (the same one-domain-at-a-time expansion mechanism the vault used to add Defense).

---

## What I'm trying to figure out

I want to understand where durable value accrues across the **humanoid-robot value chain** as humanoids move from R&D toward volume production over the next 1–2 decades. My operating hypothesis mirrors the other two theses: value concentrates at **structural chokepoints** — scarce, hard-to-replicate inputs the supply chain cannot route around — and **not** at the platform (robot-maker) layer, which is commoditizing exactly the way drone airframes are. The robot you can photograph is becoming the disposable part; the harmonic gear, the roller screw, the rare-earth magnet, the force-torque sensor, and the AI brain are where pricing power lives.

The wiki exists to help me answer five questions with precision:

1. **Where are the durable opportunities in humanoids?** Across the brain (foundation models + compute), actuation (the mechatronic core), manipulation (hands), perception (sensors + vision), power (batteries), and the materials substrate — which positions are structurally durable versus commoditizing? My focus is **US-listed equities accessible via IBKR** — and the central finding up front is that *the strongest chokepoints have the worst US-listed access* (the best pure-plays are Japanese, German, Taiwanese, Chinese, or private).

2. **How big — and how real — is the demand, and how contingent?** Goldman's base case is a **$38bn TAM by 2035** (~1.4M units), blue-sky ~$205bn; Morgan Stanley reaches for ~$5tn by 2050. But realistic 2026 output is **low-thousands of units** — this is an early-innings, long-dated thesis whose viability "hasn't been proven yet" (Goldman). Separating the *direction* (a credible multi-decade automation wave) from the *magnitude and timing* (speculative, slip-prone) is the single most important discipline here.

3. **What are the structural chokepoints?** Rare-earth NdFeB magnets (China ~90% of finished magnets), harmonic/strain-wave reducers (precision grinding + metallurgy), planetary roller screws (precision grinding + alloys; a current supply bottleneck), high-precision six-axis force/torque + tactile sensors, dexterous-hand modules, and the AI "brain." Which are durable on **physics** (magnets, precision grinding) versus which **commoditize** (assembly, basic motors, batteries, cameras)?

4. **How do the layers interact?** From the materials substrate (magnets, bearings) → components (motors, gears, screws, sensors) → subassemblies (actuators, dexterous hands) → robot makers, with the brain (VLA models + compute) running across the top. Where do margins compress (the 40+-maker integration layer) versus expand (the concentrated, capacity-constrained precision parts and the materials substrate)?

5. **What are the inter-connections and cross-thesis overlaps?** OEM supplier relationships (Tesla–Sanhua/Tuopu; Figure; Unitree); the order-vs-capacity gap (Chinese suppliers building 100k–1M-unit capacity *without* binding orders); and the overlap nodes where this thesis touches the existing vault — **[[MP]]** (the rare-earth-magnet chokepoint, now a *triple-thesis* node: defense + AI/materials + humanoid), **[[NVDA]]** (the brain/compute, already owned via the AI-datacenter book), and **[[INOD]]** (physical-AI/robotics training data).

## Core thesis statement

Over the next 1–2 decades, advances in vision-language-action AI ("the variable that surprised us the most," per Goldman) plus a ~40% collapse in component cost will move humanoid robots from lab demos toward volume in **structured, "dirty/dull/dangerous"** settings (EV assembly, logistics, sorting) first, then broader use. **The durable winners control scarce, hard-to-replicate inputs — rare-earth magnets, harmonic reducers, roller screws, high-end force/torque sensors, and the AI brain — rather than the commoditizing robot makers**, of which there are already 40+ (mostly Chinese, many private, several state "Innovation Centers").

The demand thesis is credible on the **direction** of automation. It is weakest on **timing** (realistic near-term volumes are tiny; every Tesla/Figure timeline has slipped) and on **which public equities capture it** — because (a) the strongest mechatronic chokepoints are non-US-listed or private, and (b) the makers are commoditizing by design. **The supply-side / chokepoint framing is the higher-conviction expression of the thesis**, and within it the two cleanest US-listed expressions are the *edges the banks underweight*: **the rare-earth-magnet substrate ([[MP]]) and the six-axis force/torque sensor layer (NOVT / VPG).**

## Core framework

The wiki categorizes humanoid companies along several analytical axes; canonical specifications live in `raw/notes/frameworks-humanoid-robot.md`.

**Value-chain position (the five systems + substrate, highest to lowest structural attractiveness):**

| System | What it is | Structural attractiveness |
|---|---|---|
| **Materials substrate** | Rare-earth NdFeB/NdPr magnets; precision bearings | **Very high** — physics/geology chokepoint; China ~90% of magnets; binding constraint |
| **Actuation core** | Harmonic reducers + planetary roller screws (the ~33–60%-of-BOM mechatronic heart) | **Very high** — precision-grinding + metallurgy barriers; capacity-constrained |
| **Intelligence (brain)** | VLA foundation models + onboard compute | **Very high moat — but already owned via the AI-datacenter book; immaterial *incremental* TAM** |
| **Perception (high-end)** | Six-axis force/torque + tactile sensors | **Medium–high, rising** — high tech barrier; sensor count per robot growing |
| **Manipulation** | Dexterous hands / end-effectors | **High (future) but route-risk** — architecture unsettled (tendon vs linkage vs cable) |
| **Actuation (lower)** | Actuator assembly; frameless/coreless motors | **Low–moderate** — assembly + basic motors commoditize |
| **Perception (vision)** | Cameras / LiDAR / depth | **Low–moderate** — competitive, capital-destructive, vision-vs-LiDAR architectural risk |
| **Power** | Batteries + power electronics | **Low** — shared with EVs; not humanoid-specific |
| **Platform (makers)** | The integrated robot | **Lowest** — 40+ entrants; commoditizing by design |

**Investability / quality tiers (a proposed `humanoid_tier`, deliberately NOT codified yet — held under YAGNI until the domain matures into a physical-AI codification):** rather than a tier field, names land **`outside` the existing per-domain frameworks + theme-anchored** (the [[INOD]] precedent), with the US-listed accessibility flag carried in prose. See `frameworks-humanoid-robot.md` Framework H2.

**Structural vs. cyclical exposure (mirrors the other two theses):**
- **Structural** — the multi-decade labor-automation rationale; the physics chokepoints (magnets, precision grinding) whose scarcity holds regardless of which OEM wins or which year volumes inflect.
- **Cyclical / speculative** — the hype cycle itself; specific-OEM program timing (Optimus Gen-3, Figure BotQ); and the **order-vs-capacity gamble** (suppliers building capacity ahead of binding orders).

**The chokepoint quality gradient (the core analytical insight, parallel to the Defense thesis's geology-over-policy rule):** Not all chokepoints are equal. **Chokepoints durable on physics/geology rank above those durable on precision-manufacturing know-how, which rank above assembly/integration.** Rare-earth magnet processing (China ~90%) is a geology/capacity chokepoint — years to replicate. Harmonic-gear and roller-screw manufacturing is a precision-grinding/metallurgy chokepoint — high, but Chinese challengers (LeaderDrive, Hengli) are closing the gap and compressing price, so it has a *commoditization clock* the magnet substrate lacks. Actuator assembly and basic motors are integration — the weakest. Score every name on *what makes its position durable*, not on today's order book.

## Demand drivers & market map

**The honest caveat up front (the discipline that defines this thesis):** The **direction** of humanoid automation is credible; the **magnitude and timing** of the headline figures are a long-dated bet, not a fact. Realistic 2026 shipments are in the **low thousands** (Omdia estimates Tesla / Figure / Agility shipped ~150 units *each* in 2025). Treat all TAM/unit projections as forward estimates, and lead every company read with "early-innings optionality," not "current revenue" — except for the cross-over names (MP, NVDA, NOVT, VPG) where humanoid is *incremental* on a real existing business.

**Sizing (Tier-3; attribute + verify):**
- **Goldman:** TAM **$38bn by 2035** (base, raised 6× from $6bn), blue-sky **$205bn**; units **~76k (2027E) → ~502k (2032E) → ~1.4M (2035)**. Goldman is *more conservative than the market* on near-term shipments.
- **Morgan Stanley ("Humanoid 100"):** ~$5tn TAM by 2050; ~1 billion units by 2050; China ~63% of the value chain.
- **Cost (the key upgrade driver):** manufacturing cost fell ~40% ($50–250k → $30–150k); BofA puts the China-made BOM at ~$35k in 2025 → $13–17k by 2030–35; Tesla targets ~$20k at scale. *"AI progress surprised us the most"* (Goldman) — end-to-end VLA models, not hand-coded behavior.

**Use cases / adoption path:** near-term demand concentrates in **structured environments** (EV/auto assembly, logistics, component sorting) and **dirty/dull/dangerous** jobs (mining, disaster rescue, nuclear/chemical maintenance). Manipulation (reliable grasping) and unstructured human interaction remain the bottlenecks.

**The maker landscape (the commoditizing platform layer):** Tesla Optimus (Gen-3 at Fremont, summer 2026; 1M-unit/yr *line capacity* target by end-2026 — realistic output far lower); Figure AI ($39bn private valuation; in-house Helix VLA; an 11-month BMW Spartanburg pilot); Boston Dynamics/Hyundai (electric Atlas; Gemini Robotics brain); and the Chinese leaders — **Unitree** (world unit-shipment leader, >5,500 humanoids in 2025, 32.4% share, G1 from ~$16k, STAR Market IPO filed Mar 2026), UBTech (first listed pure-play, HK), AGIBOT (10,000th unit by Mar 2026), Xiaomi, XPeng. **The single most important demand-side risk: the order-vs-capacity gap** — Goldman's own supplier survey found Chinese suppliers planning 100k–1M robot-equivalent units of capacity *without confirmed binding orders.*

## Chokepoint-by-chokepoint thesis

*Ordered by structural conviction. Physics/geology chokepoints first; commoditizing layers last. Full durability scoring in `frameworks-humanoid-robot.md` Framework H5. All figures Tier-3 — verify at primary ingest.*

**Rare-earth NdFeB magnets (highest conviction — the binding physical chokepoint):** Every motor in every joint uses NdFeB permanent magnets (Nd/Pr; Dy/Tb for high-temp grades) — no viable substitute at the required power density. A humanoid needs **~0.9–4 kg** of magnet (~2× an EV); a Tesla Optimus has ~28–42 motors. The binding constraint is **midstream processing, not mining**: China makes **~90% of the world's permanent magnets** (McKinsey), ~88% of refined rare earths (Morgan Stanley), and ~40% of precision bearings/encoders. Goldman *folds this into "actuators" and does not call it out* — but it is the hardest physical bottleneck in the stack; China's 2025 export controls already disrupted robotics/auto supply chains. Adamas projects robotics becomes the *largest* NdFeB demand driver by ~2040. **[[MP]] is the only US-listed integrated miner + magnet producer scaling domestic capacity** (Pentagon equity backing + price floor; first commercial NdFeB Dec 2025; the "10X" facility 2028) — **the single cleanest US-listed chokepoint expression on this entire topic, and a triple-thesis node** (defense + EV/wind + humanoid/robotics). *Honest counter-signal (preserve it): BofA's contrarian view that magnets are NOT the near-term bottleneck (high-end machine tools are), and ongoing magnet-free-motor R&D — both would de-risk and undercut the MP thesis.*

**Harmonic / strain-wave reducers (high conviction; worst US access):** The precision gearbox at rotary joints (shoulder, elbow, wrist, neck) — flexspline + circular spline + wave generator giving huge reduction with near-zero backlash. Requires micron-precision grinding, specialized metallurgy, and limited high-precision grinding machines (a key Goldman bottleneck). Top-5 players (Harmonic Drive, Nabtesco, HDS, Wittenstein, Schaeffler) ~55–60% global share. Goldman's *top pick* (Exhibit 5 score 16). **But the cleanest pure-play is Japanese (Harmonic Drive Systems, 6324.T) with no clean US ADR**; the challengers are Chinese A-shares (LeaderDrive, Shuanghuan). A genuine gap in the US-listed universe — with a commoditization clock as China localizes.

**Planetary roller screws (high conviction; the acute current bottleneck):** Converts rotary to linear motion at linear joints (knee, ankle); rollers (vs balls) handle the shock loads of walking. Needs ~5-micron grinding on specialized thread grinders, aerospace-grade alloys, heat treatment. Tesla's Optimus uses ~14; each costs $1,350–$2,700; lead times reportedly ballooned to ~26 weeks. **Best Western expression is German (Schaeffler, via Ewellix)**; also Taiwanese (HIWIN); the capacity build-out is heavily Chinese (Hengli Hydraulic, Shanghai Beite). High barrier, low capacity-flexibility = pricing power if humanoids scale — but, again, the best names are foreign.

**Six-axis force/torque + tactile sensors (medium-high, rising — the underappreciated US sweet spot):** Wrist/ankle six-axis force sensing + fingertip tactile + IMUs — sensor count per robot is rising fast as robots leave cages. Highest tech barrier in its tier (Goldman score 13); the six-axis F/T market is dominated by a few players (**ATI and HBM**). **This is one of the cleanest US-listed picks on the whole chart, and Goldman doesn't highlight it: [[NVDA]]'s sensor peers NOVT (Novanta, owns ATI Industrial Automation) and VPG (Vishay Precision).** Apply the needle-mover discipline — humanoid is *optionality on a legacy industrial-automation sensing business*, not yet the base case (verify the revenue mix at ingest).

**Dexterous hands (high future value, high route-risk):** The hardest single subsystem — many tiny actuators + tendons + tactile sensors in a human-sized envelope. Goldman score 15, but with the **lowest "certainty of technology choice" (1)** — the architecture is unsettled. A capability chokepoint with real route risk; the listed pure-plays are almost entirely Chinese (Zhaowei, Inovance) or private (Maxon micro-motors). Watch for a Western entrant.

**The brain — VLA foundation models + compute (very high moat; already owned):** The vision-language-action model + onboard inference (NVIDIA Jetson Thor is the de facto robot computer; Isaac/GR00T/Cosmos the platform). Highest moat in the stack, and where the West leads. **But for this vault it overlaps almost entirely with the existing AI-datacenter [[NVDA]]/[[GOOGL]] exposure — a robotics allocation here is double-counting, not diversifying** — and Goldman scores its *incremental humanoid opportunity* at 1 (a rounding error vs datacenter AI). Tesla is the one maker with a credible in-house brain (a software-moat bet, not a hardware-chokepoint bet).

**Commoditizing layers (participate via cost leaders, not chokepoint economics):** actuator assembly (China — Sanhua, Tuopu; integration, not core IP); frameless/coreless motors (low tech barrier; some US via Regal Rexnord); vision/LiDAR (competitive, capital-destructive, vision-vs-LiDAR architectural risk — US-listed OUST/HSAI/INVZ/LAZR are higher-beta optionality, not structural); batteries (EV-shared; CATL/Samsung SDI/Panasonic; no clean US pure-play).

## The company universe — what to track

The US-listed investable universe is thin; the tiered map below is the starting point (full table with figures and US-access flags in `frameworks-humanoid-robot.md`). **Apply the needle-mover / layer-straddling discipline to every cross-over name: how much revenue is actually humanoid vs. legacy? Humanoid is optionality, not the base case, for MP / NVDA / NOVT / VPG.**

- **Cleanest US-listed chokepoint expressions (the edges the banks underweight):** **[[MP]]** (rare-earth magnets — triple-thesis; already a vault page), **NOVT** (Novanta — six-axis force/torque via ATI), **VPG** (Vishay Precision — force/strain sensing).
- **US-listed, but already-owned or commoditizing:** **[[NVDA]]** (brain/compute — don't double-count; already a vault page), **TSLA** (the maker-with-a-brain), **RRX** (Regal Rexnord — cleanest US motion/motor), **INTC** (RealSense/edge — already a vault page), **OUST / HSAI / INVZ / LAZR** (LiDAR — higher-beta optionality), AMBA / ST (watch).
- **Foreign-listed chokepoint pure-plays (awkward to own):** Harmonic Drive Systems (6324.T, Japan — the purest reducer chokepoint), Schaeffler (SHA.DE, Germany — roller screws), HIWIN (2049.TW, Taiwan), Nidec (6594.T, Japan — motors), Lynas (LYC.AX, Australia — rare earths).
- **China A-share / HK (map, don't pretend investable):** LeaderDrive, Shuanghuan, Sanhua, Tuopu, Inovance, Zhaowei, Hengli Hydraulic, Leadshine, Moons' Electric, CATL, Sunny Optical, RoboSense, Hesai, Unitree (pre-IPO), UBTech.
- **Private / un-investable (mark and monitor):** Figure AI, 1X, Agility, Apptronik, Sanctuary, Maxon, DJI/Livox, Boston Dynamics (Hyundai sub). **As with Defense, the best pure-play capability is often not publicly investable — a structural feature, not a temporary gap.**

**Prioritized first deep-dives:** **MP** (purest play on the most durable chokepoint; already in vault — graduate the humanoid-magnet angle), then **NOVT** (the clean US sensor pick the banks miss), then **VPG** / **RRX**, with **NVDA** carrying a light humanoid-optionality note (don't double-count).

## Cross-thesis overlap with the AI-datacenter & Defense vaults

Several names sit at the intersection of this thesis and the existing vault — **dual/triple-thesis pages** (add humanoid framing to the existing page rather than duplicating):

- **[[MP]]** — rare-earth magnets: now a **triple-thesis chokepoint** (defense motors + EV/wind + humanoid/robotics actuators). The single cleanest multi-thesis node — one chokepoint, three demand drivers. Already a vault page (AI/materials + `defense_tier 4`).
- **[[NVDA]]** — the robot brain/compute (Isaac/GR00T + Jetson Thor) on the humanoid side; the AI platform definer on the datacenter side; Jetson edge modules on the defense side. Already a vault page.
- **[[INTC]]** — RealSense depth cameras + edge compute (humanoid) on top of its datacenter role. Already a vault page.
- **[[INOD]]** — physical-AI / robotics training-data (its disclosed growth vector) — the *data feedstock* for embodied AI; ties the humanoid brain back to [[AI-data-supply-chain]].
- **[[china-exposure]]** — the humanoid value chain is the *most* China-concentrated in the vault (~63% of the chain, ~90% of magnets). A heavy geopolitical overlay.

## What would prove this thesis wrong

- **Viability never arrives.** Mass-produced general-purpose humanoids stay lab demos; manipulation/generalization stays unsolved; the shipment curve slips right indefinitely. The single biggest falsifier — Goldman itself stresses viability "hasn't been proven yet."
- **The order-vs-capacity gamble busts.** Chinese suppliers built 100k–1M-unit capacity without binding orders; if confirmed OEM orders don't materialize into 2H2026, the supply side faces overcapacity and margin collapse — the inverse of a chokepoint.
- **Maker commoditization is total.** 40+ integrators racing to a sub-$20k cost floor means platform value evaporates; value accrues *only* to chokepoint owners and the brain (Tesla the exception via its in-house stack).
- **The magnet chokepoint de-risks.** China relaxes rare-earth export controls (weakening the MP reshoring thesis), OR magnet-free motors (induction / electrically-excited synchronous / FeN) advance — directly undercutting MP. Note BofA's contrarian view that machine tools, not magnets, are the near-term bottleneck.
- **Precision-grinding capacity scales fast.** If grinding-machine capacity for harmonic gears / roller screws scales quickly (compressing lead times and margins), the actuator chokepoint erodes and value shifts downstream.
- **Vision-only wins.** If Tesla's vision-only approach prevails, the LiDAR TAM leg (OUST/HSAI/INVZ/LAZR) shrinks materially.
- **The value stays in China / private.** If the chokepoints remain Chinese-or-private, the US-listed universe may never capture the thesis's best economics regardless of how right the automation call is (the MP/NOVT edges are the partial answer).
- **Valuation already priced in.** Several names already embed years of flawless humanoid scaling (descriptive risk — the wiki issues no buy/sell calls).
- **Humanoid is immaterial to the cross-over names.** If MP/NVDA/NOVT/VPG humanoid revenue stays a rounding error, the "humanoid play" framing fails the needle-mover test and these revert to their primary theses.

## What the wiki is for — and what it isn't

Same four disciplines as the other two theses (per CLAUDE.md Section 2.1).

**The wiki is for:** synthesizing what I actually believe about humanoid value-chain dynamics; stress-testing each name's structural fit *and* its US-listed accessibility; surfacing chokepoints and cross-thesis nodes; tracking how positioning evolves; and generating uncomfortable conclusions (especially that the best chokepoints aren't cleanly investable, and that "humanoid plays" are mostly optionality on legacy businesses).

**The wiki is not for:** P&L, cost basis, or position sizing; buy/sell/hold calls; covering the robotics sector comprehensively (names that don't inform the thesis don't get pages); or confirming views I already hold. "Should I buy MP for humanoids" gets reframed to "what share of MP's value is actually humanoid-driven vs defense/EV, and what would have to be true for the humanoid leg to matter."

## Scope discipline

Companies earn pages by showing up in primary sources (10-K, 10-Q, earnings calls) relevant to the thesis — not by being on Goldman's slide. The tiered map is a starting point; names get pages at the multi-source threshold per CLAUDE.md conventions.

**Initial scope: humanoid-first.** The bipedal-humanoid value chain — actuation, manipulation, perception, the brain, power, and the materials substrate.

**Deliberately out of initial scope** (future expansion, sequenced per opportunity — the same mechanism the vault used to add domains one at a time):
- **The broader "physical AI" / embodied-AI superset** — quadrupeds, autonomous mobile robots (AMRs), industrial cobots, and autonomous machines. *This is the planned next broadening* (the domain name would generalize from humanoid-robot to physical-AI). The chokepoints (magnets, gears, screws, sensors) are general-robotics, so the broadening is additive, not a re-scope.
- **Autonomous vehicles / ADAS** — a distinct, huge supply chain; explicitly excluded to prevent scope creep.

## Evolution

This thesis will evolve as primary-source evidence accumulates and the Tier-3 report figures are verified against filings. Most likely directions:
- **Demand resolution** — the first sizable, *confirmed* OEM orders (a Tesla Optimus Gen-3 production order; Figure BotQ scale-up) would validate the capacity bet; continued absence into 2H2026 signals overcapacity.
- **Chokepoint maturation** — MP / NOVT / VPG primary-source ingests will mature the supply-side thesis from Tier-3 scaffolding to vault-canonical depth, and resolve the needle-mover (humanoid-revenue-mix) question.
- **Architecture resolution** — dexterous-hand design, vision-only-vs-LiDAR, and magnet-free-motor R&D will each resolve route risks that currently cap conviction on specific legs.
- **Private-to-public transitions** — Unitree's STAR IPO, and any Figure / Apptronik / 1X listing, would materially change the investable universe.
- **The physical-AI broadening** — when a quadruped/AMR/cobot name crosses the threshold, the domain generalizes per the scope note above.

---

**Note on this creation (2026-06-05):** **v0.1 DRAFT** drafted via Vic-authorized collaborative drafting (Vic-directed; agent-scaffolded) as the vault's third thesis domain, parallel to the AI-datacenter `_thesis.md` and the Defense & Drones `_thesis-defense-drones.md` (both untouched). **For Vic to shape, finalize, and commit; after that, default human-ownership resumes.** Sourced from two Tier-3 research reports (`raw/research/humanoid-robot-primer-report.md` + `humanoid-robot-high-value-subsystems-research.md`) anchored on Goldman Sachs' humanoid value-chain work (Exhibits 2 & 5), plus cross-bank corroboration (Morgan Stanley, JPM, BofA, McKinsey, Jefferies). **All figures are Tier-3 and forward TAM/unit/cost numbers ($38bn 2035 TAM, ~1.4M units, BOM splits, magnet kg/robot, China-concentration %s) are projections/estimates, not realized results — verify against primary filings (SEC 10-K/10-Q; company IR) before treating as load-bearing.** Scope is humanoid-first; the physical-AI broadening is sequenced for future expansion. Companion frameworks file: `raw/notes/frameworks-humanoid-robot.md`. No `humanoid_tier` frontmatter field is codified (held under YAGNI; names land `outside` + theme-anchored per the [[INOD]] precedent). The first theme under this anchor is `humanoid-robot-value-chain`.
