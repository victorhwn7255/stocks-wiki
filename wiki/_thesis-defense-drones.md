# Thesis — Defense & Drones (Unmanned Systems Supply Chain & Chokepoints)

**Last updated:** 2026-06-03
**Owner:** Vic (human-maintained; never edited by the LLM except by explicit Vic-authorized rework session)
**Status:** Second thesis domain in the stocks-wiki vault, parallel to the AI-datacenter thesis (`wiki/_thesis.md`). Shares the vault's methodology, source hierarchy, and disciplines; does not replace or modify the AI anchor.

---

## What I'm trying to figure out

I want to understand where durable value accrues across the **defense unmanned-systems supply chain** as the US military shifts toward autonomous mass, attritable drones, and counter-drone defense over the next 1–2 decades. My operating hypothesis mirrors the AI-datacenter thesis: value concentrates at **structural chokepoints** — scarce inputs the supply chain cannot route around — and **not** at the platform layer, which is being deliberately commoditized. The drone airframe is becoming the disposable part; the magnet, the secure chip, the seeker, the autonomy stack, and the compliant supply chain are where pricing power lives.

The wiki exists to help me answer five questions with precision:

1. **Where are the durable opportunities in defense/drones?** Across platforms, payloads/sensors, autonomy software, counter-UAS, and the upstream supply chain — which positions are structurally durable versus politically or cyclically dependent? My focus is US-listed equities accessible via IBKR (the most capable pure-play drone-autonomy companies — Anduril, Shield AI — are private and un-investable, which is itself a central finding).

2. **How does defense spending actually flow — and how contingent is it?** The demand story is loud (FY2027 request ~$1.5T topline; a headline $54.6B for the Defense Autonomous Warfare Group). But how much of that is *enacted law* versus a *request* that depends on a future reconciliation bill surviving the November 2026 midterms? Separating structural budget architecture from contingent surge funding is the single most important discipline of this thesis.

3. **What are the structural chokepoints?** Rare-earth NdFeB magnets (China ~85–90% of finished magnets), secure/trusted microelectronics and FPGAs, EO/IR sensors and seekers, high-energy-density batteries, edge-AI compute, and the NDAA-compliant ("Blue UAS") supply chain. Which of these are durable on geology or physics, and which are durable only while a statute holds?

4. **How do the layers of the value chain interact?** From upstream inputs (magnets, secure chips, sensors, batteries) → components → platforms (Group 1–5 UAS, loitering munitions, CCA) → autonomy/AI software → counter-UAS → program integration. Where do margins compress (commoditizing airframes) versus expand (concentrated inputs, software)?

5. **What are the inter-connections between companies and programs?** Programs of record (Replicator → DAWG → JIATF 401; Drone Dominance "Gauntlet"; Collaborative Combat Aircraft); government equity stakes (the MP Materials–DoD deal; Office of Strategic Capital talks with drone makers); and the overlap nodes where this thesis touches the AI-datacenter vault (MP, AMD, NVDA, PLTR, plus Lattice and Mercury).

## Core thesis statement

Over the next 1–2 decades, persistent great-power competition (US–China), active conflicts (Ukraine; the Middle East/Red Sea, including the 2026 Iran conflict), and a structural shift in warfare toward **mass, attrition, and autonomy** will sustain rising allocations to unmanned aerial systems, counter-UAS, and autonomy/AI — the fastest-growing sub-segments inside a defense budget that is itself growing. **The durable winners control scarce, hard-to-replicate inputs — rare-earth magnets, secure microelectronics, EO/IR seekers, autonomy software, NDAA-compliant supply chains — rather than commoditized airframes.**

The demand thesis is strong and durable on the **direction** of spending. It is weakest on **which public equities capture it** — because the best programs often go to private players (Anduril, Shield AI, Neros, Performance Drone Works), and because the Pentagon's explicit design goal is to drive one-way-attack drones toward a ~$2,000 unit-cost ceiling with deliberately maintained multi-vendor competition. The **supply-side / chokepoint framing is the higher-conviction expression of the thesis** (per the Tier-3 anchor report's net assessment).

## Core framework

The wiki categorizes defense/drone companies along several analytical axes; canonical specifications live in `raw/notes/frameworks-defense-drones.md`.

**Value-chain position (the layers, highest to lowest structural attractiveness):**

| Layer | What it is | Structural attractiveness |
|---|---|---|
| **Supply-chain / chokepoint inputs** | NdFeB magnets, secure FPGAs, EO/IR seekers, high-energy batteries, edge-AI compute | **High–very high** — scarce, concentrated, capacity-constrained |
| **Autonomy & AI software** | swarming, GPS-denied nav, mission autonomy, data fusion | **Very high** — software margins, platform-agnostic, decoupled from hardware |
| **Counter-UAS** | detection, EW/jamming, kinetic interceptors, C2 | **High** — persistent, growing, under-served, hard discrimination problem |
| **Payloads / sensors** | EO/IR, gimbals, seekers | **High** — concentrated, export-controlled IP |
| **Platforms — large (Group 4–5 / CCA)** | jet-powered UAS, loyal wingman | **Moderate–high** — higher barriers, programs of record |
| **Platforms — small/tactical/FPV/OWA** | Group 1–3, one-way-attack | **Low–moderate** — commoditizing fast; price ceilings by design |

**Investability / quality tiers (the `defense_tier` field, proposed):**

1. **Primes** with real drone-relevant programs of record (large, diversified; drones a slice).
2. **Mid-cap pure-plays / specialists** with real revenue.
3. **Speculative micro-caps** — real revenue inflections but dilution, losses, narrative-ahead-of-financials risk (apply the financial-quality screen, below).
4. **Supply-chain / materials enablers** — where the report places the highest structural conviction (the chokepoint owners).

**Structural vs. cyclical exposure** (mirrors the AI thesis axis):
- **Structural** — budget architecture (reconciliation mechanics, OSC loans, the DAWG line), bipartisan China-pacing rationale, NDAA component bans, acquisition reform. Durable across administrations.
- **Cyclical / contingent** — conflict-driven supplementals (Ukraine, Red Sea) and the FY2027 "one-year surge." Officials themselves call FY2027 a possible surge.

**The chokepoint quality gradient (the core analytical insight, parallel to the AI thesis's "binding constraint"):** Not all chokepoints are equal. **Chokepoints durable on geology or physics rank above chokepoints durable only on policy.** Rare-earth magnet concentration and EO/IR seeker IP are geology/physics chokepoints — years to replicate regardless of statute. The NDAA-compliant "Blue UAS" supply chain is a *policy-created* chokepoint — powerful while it lasts, but the DoD Blue UAS exemption expires **January 1, 2027** with no guaranteed renewal. A policy chokepoint with a known expiry date is a weaker structural position than a geology one, even if today's revenue looks identical.

## Demand drivers & budget map

**The honest caveat up front (the discipline that defines this thesis):** The **direction** of defense/drone spending is structural and well-supported; the **magnitude** of the headline figures is a political bet, not a fact. Only the FY2025 reconciliation package is **enacted law**. The FY2027 numbers are a **request**. Treat the two differently everywhere in the wiki.

**Enacted (structural, ground truth):**
- **FY2025 reconciliation ("One Big Beautiful Bill," P.L. 119-21, signed July 4, 2025):** provided **$156.2B in mandatory defense funding** in FY2025 against a $150B headline target (CBO scored ~$149.5B net over 2025–2034) — per CRS IN12580. Drone-relevant pots: ~$16B for "low-cost enablers" (drones, counter-drone, cheap munitions, AI); $1B+ to expand the one-way-attack drone industrial base; $1.1B for the small-drone industrial base; $500M to prevent attritable-drone delivery delays; $500M for counter-UAS. This put total FY2025 defense above $1 trillion while keeping the base budget roughly flat — a deliberate structure.
- **FY2026:** first year of a separately tracked **~$13.4B DoD AI-and-autonomy budget line.**

**Requested (contingent — verify before treating as load-bearing):**
- **FY2027 request (released April 3, 2026):** ~$1.5T topline (largest in US history). Headline: **$54.6B for the Defense Autonomous Warfare Group (DAWG)** — up from $225.9M in FY2026 — **but only $1B sits in the base budget; $53.6B (≈98%) sits in a future reconciliation pot** with up to 5 years to obligate. That second reconciliation bill is contingent on the November 2026 midterms. Office of Strategic Capital loan program: ~$20.2B requested ($216M base + $20B reconciliation).

**Programs of record / the demand map:**
- **Replicator → DAWG → JIATF 401.** Replicator 1 (attritable autonomous systems to counter China's mass) selected AeroVironment's Switchblade 600, Anduril's Altius-600/Ghost-X, Performance Drone Works' C-100, Fortem's DroneHunter F700. Replicator dissolved into DAWG in late 2025; Replicator 2 (counter-small-UAS) folded into **JIATF 401**, the new Joint Interagency Task Force (reporting to Deputy Secretary Feinberg; director has acquisition authority up to $50M per C-UAS effort). The legacy Joint C-sUAS Office is being disestablished. **Execution-vs-announcement caveat (CRS IF12611):** Replicator aimed to field thousands of systems by summer 2025 but "had fielded only hundreds by that time." The history of this theme is announcements outrunning delivery.
- **Drone Dominance Program (DDP):** ~$1.1B, four-phase, targeting hundreds of thousands (~300,000) of weaponized one-way-attack drones by end-2027. Gauntlet I (Fort Benning, results March 2026): 25 vendors; winners Skycutter, Neros, Napatree; ~$150M initial delivery orders. Unit-cost ceilings ~$5,500/$4,500 tightening toward a **$2,000 Phase IV target.** Gauntlet 2 qualified 48–49 companies (including AeroVironment and Kratos); harder test with GPS denial, jamming, EW.
- **Counter-UAS:** Army requested ≥$858M for C-UAS in FY2026; >350 drone detections at ~100 US installations in the prior year; JIATF 401 selected five installations for an FY2026 directed-energy C-UAS pilot.
- **Collaborative Combat Aircraft (CCA):** Increment 1 down-selected to Anduril (YFQ-44A) and General Atomics (YFQ-42A); 100–150 aircraft over five years (~$30M/unit); program est. ~$8.9B; Shield AI Hivemind + RTX autonomy selected (decoupled from airframe). Increment 2 opened to nine+ vendors. Kratos' XQ-58 Valkyrie positioned for adjacent loyal-wingman efforts.
- **Government equity stakes:** the Office of Strategic Capital is reported (WSJ ~May 28, 2026) to be in talks to take debt-and-equity positions in domestic drone makers — Performance Drone Works, Unusual Machines, Neros named — attacking the supply side directly. (Compare the MP Materials–DoD deal in the chokepoint section: the government is increasingly a capital provider, not just a customer.)

**Conflict-driven demand (cyclical):** Ukraine (drones drive most casualties; FPV/fiber-optic drones; lessons absorbed into US programs); Middle East / Red Sea / the 2026 Iran conflict (Operation Epic Fury; the cost-exchange problem of expensive interceptors vs. cheap drones; a May 2026 ceasefire could moderate urgency, partly offset by inventory restocking).

## Chokepoint-by-chokepoint thesis

*Ordered by structural conviction. Geology/physics chokepoints first; policy chokepoint last. Full durability scoring in `frameworks-defense-drones.md` Framework D5.*

**Rare-earth NdFeB magnets (highest conviction):** The most concentrated, most durable, best-funded chokepoint. China holds ~85–90% of finished magnets, ~91% of separation/refining, ~69% of mining, and ~100% of production equipment (IEA, Nov 2025); one Chinese firm (JL MAG) ≈ all non-Chinese output combined. The Pentagon needs ~3,000–4,000 tons of specialized magnets annually, rising toward ~10,000 tons by 2030, against minimal current US output (meaningful finished-magnet capacity is 2027–2028+). Drones are a small-volume (<3% of global NdFeB demand) but high-criticality consumer — skewed toward the most China-controlled heavy rare earths (Dy/Tb) for high-temp motors. **[[MP]] is the US-listed leader** (also a multi-thesis node — spans defense + EV/wind + AI/robotics; already a vault page on the AI side). The **MP–DoD deal (July 9, 2025)** is the template for government-as-capital-provider: DoD bought $400M of convertible preferred + a warrant for up to ~11.2M shares (conversion/exercise $30.03), giving DoD a ~15% as-converted stake as largest shareholder; plus a 10-year $110/kg NdPr price floor, a 10-year magnet offtake, the "10X" facility (~10,000 MT, Northlake TX, commissioning 2028), and $500M from Apple. First commercial NdFeB at Independence in December 2025. US-listed adjacents: USA Rare Earth (pre-revenue, well-funded), Energy Fuels (oxides, not magnets), American Resources (ReElement minority stake).

**Secure microelectronics / FPGAs (high conviction, with a geographic asterisk):** NDAA-compliant secure-control FPGAs, hardware root-of-trust, rad-tolerant parts. Lattice (LSCC) in low-power secure FPGAs; Microchip (PolarFire); AMD/Xilinx high-end; Mercury Systems (trusted/secure microelectronics). Design/IP is a defensible Western position — but the **deeper chokepoint is TSMC fabrication in Taiwan, a geographic risk NDAA rules do not solve.** Note also Lattice's ~64% Greater China revenue (a two-edged exposure if China weaponizes supply). This is the cleanest **cross-thesis overlap** with the AI-datacenter vault.

**EO/IR sensors & seekers (high conviction):** Cooled/uncooled thermal imagers, gimbals, seekers, automatic target recognition. Teledyne (TDY, via FLIR) is dominant in Western EO/IR — decades of export-controlled IP, hard to replicate; also makes the Black Hornet nano-drone and the Rogue 1 loitering munition (selected for Army LASSO). Leonardo DRS and RTX adjacent. Concentrated and durable on IP/physics.

**Autonomy & AI software (very high structural value, mostly private):** Swarming, GPS-denied navigation, mission autonomy, data fusion. The CCA precedent — autonomy decoupled from airframe — proves the software earns separate value. But the best autonomy is **private and un-investable**: Anduril (Lattice; revenue doubled to ~$2.2B in 2025; $5B Series H at $61B post-money, May 2026; $20B Army Lattice contract) and Shield AI (Hivemind; $12.7B valuation; selected for CCA). US-listed exposure is thin: Palantir (Maven data fusion; profitable but not drone-specific) and small/speculative names (Palladyne).

**High-energy-density batteries (moderate–high conviction):** Silicon-anode cells (450–500 Wh/kg) for endurance UAS/eVTOL; NDAA-compliant. Amprius (AMPX) is the silicon-anode play (customers incl. Teledyne FLIR; FY2026 NDAA phases in battery-origin restrictions). China dominates conventional Li-ion; energy density is the moat.

**Counter-UAS detection / EW (high conviction, fragmented):** Discrimination of drones in clutter/swarms; spectrum; non-kinetic defeat (~90% of fielded C-UAS is EW). Fragmented across RTX (Coyote, KuRFS), L3Harris (VAMPIRE), Leonardo DRS (MLIDS), Axon (Dedrone, drone detection), Ondas (Iron Drone). A hard technical problem against a persistent, growing threat.

**Edge-AI compute / flight controllers (moderate conviction):** NDAA-compliant, Blue UAS-listed, US-assembled modules. Thin ecosystem (ARK Electronics, ModalAI [private], Unusual Machines; NVIDIA Jetson US-made SKUs). Replicable, so moderate durability.

**NDAA-compliant supply chain / "Blue UAS" (policy chokepoint — weakest structural quality despite real current revenue):** Whole-system China-free sourcing via the DCMA Blue UAS list. Powerful while the statute holds — but it is a *policy-created* chokepoint, and the **DoD Blue UAS exemption expires January 1, 2027** with no guaranteed renewal. Beneficiaries (UMAC, RCAT, AVAV, ONDS, AIRO) earn premium positioning today on a regulatory cliff. Per the quality gradient, this ranks below the geology/physics chokepoints.

## The company universe — what to track

The investable universe is thin; the tiered map below is the starting point (lifted from the Tier-3 anchor report; full table with figures and risk flags in `frameworks-defense-drones.md`). **Speculative micro-caps carry the financial-quality screen (Framework D6) — narrative-ahead-of-financials risk is the rule, not the exception, in this tier.**

- **Tier 1 — Primes with real programs of record:** AeroVironment (AVAV), Kratos (KTOS), plus diversified primes where drones are a slice (LMT, NOC, RTX, LHX, BA). General Atomics is private.
- **Tier 2 — Mid-cap pure-plays / specialists:** Ondas (ONDS), AIRO Group (AIRO), Leonardo DRS (DRS), Palantir (PLTR).
- **Tier 3 — Speculative micro-caps (FLAGGED):** Red Cat (RCAT), Unusual Machines (UMAC), ZenaTech (ZENA), Draganfly (DPRO), AgEagle (UAVS), Palladyne AI (PDYN), ParaZero (PRZO).
- **Tier 4 — Supply-chain / materials enablers (highest structural conviction):** MP Materials (MP), Lattice (LSCC), Teledyne (TDY), Amprius (AMPX), Mercury Systems (MRCY), USA Rare Earth (USAR), Energy Fuels (UUUU), American Resources (AREC), AMD, Microchip (MCHP), Axon (AXON).
- **Private / un-investable (mark and monitor):** Anduril, Shield AI, General Atomics, Skydio, Saronic, Neros, Performance Drone Works, Vulcan Elements. **The best pure drone-autonomy capability is not publicly investable — a structural feature of this thesis, not a temporary gap.**

**Prioritized first deep-dives** (per the report's research agenda): MP (purest play on the most durable chokepoint), AVAV (most complete US-listed pure-play), KTOS (large-UAS/CCA exposure), LSCC (secure-FPGA chokepoint + AI overlap), TDY (EO/IR sensor chokepoint), then ONDS / AMPX / RCAT / UMAC with the financial-quality screen applied.

## Cross-thesis overlap with the AI-datacenter vault

Several names sit at the intersection of this thesis and the AI-datacenter supply chain — these are **dual-thesis pages** (add defense framing + a `defense_tier` to the existing AI page rather than duplicating):

- **[[MP]]** — rare-earth magnets: a multi-thesis chokepoint (defense motors + EV/wind + AI/robotics + power-semiconductor magnets). Already a vault page on the AI/materials side.
- **[[AMD]]** — Xilinx FPGAs (avionics/EW/radar) on the defense side; AI accelerators + datacenter CPU on the AI side. Already a vault page.
- **[[NVDA]]** — Jetson edge-AI modules (indirect) on the defense side; the AI platform definer on the AI side. Already a vault page.
- **[[PLTR]]** — Maven/Gotham data fusion for ISR/targeting on the defense side; an AI demand-side / software page on the AI side. Already a vault page.
- **Mercury (MRCY)** — secure microelectronics spanning both theses; not yet a vault page. ([[LSCC]] is now a vault page — dual-thesis from creation, S125.)

**Rare-earth magnets are the cleanest multi-thesis chokepoint** — the same NdFeB concentration that constrains drone motors also constrains AI-datacenter power-semiconductor magnets and robotics. A single chokepoint, two demand drivers.

## What would prove this thesis wrong

The wiki should watch for evidence that challenges the thesis, not just supports it.

- **Budget reversal / reconciliation failure.** The FY2027 DAWG surge is ~98% reconciliation-funded; a Democratic chamber after November 2026 could block a second reconciliation bill. Watch: does FY2027 funding land in the *base* budget, or vanish? This is the single biggest falsifier.
- **Airframe commoditization destroys platform margins.** Sub-$2,000 unit-cost targets + deliberate multi-vendor competition compress platform margins. If drones become disposable commodities, value accrues only to chokepoint owners and software — and the platform-tier names (even AVAV/KTOS) earn thin, cyclical margins.
- **De-escalation.** A durable Ukraine ceasefire + Middle East calm reduces urgency (partly offset by restocking depleted inventories).
- **China supply normalization.** If China relaxes rare-earth export controls, the MP/USAR reshoring thesis weakens (the mirror risk: further weaponization helps US magnet names but hurts anyone still dependent on Chinese inputs — note Lattice's 64% Greater China revenue).
- **Tech obsolescence / EW.** Gauntlet 2's GPS-denial and jamming tests show platforms can be made obsolete fast; if autonomy/EW-resilience doesn't become the moat, today's winners are tomorrow's legacy.
- **Valuation already priced in.** Several pure-plays trade at premium multiples that embed years of flawless execution; the bull case may already be in the price (descriptive risk — the wiki does not issue buy/sell calls).
- **Policy chokepoint expiry.** The Blue UAS exemption expires Jan 1, 2027 with no guaranteed renewal — a regulatory cliff for NDAA-compliant names.
- **The capability stays private.** If the best programs keep flowing to Anduril, Shield AI, Neros, and PDW, the public-equity universe may never capture the thesis's best economics regardless of how right the demand call is.
- **Narrative ahead of financials.** Several micro-caps (ZENA, DPRO, RCAT's internal-control weakness, UAVS warrant-driven "income") show promotion outrunning fundamentals — see the LASE financial-quality screen (Framework D6).

## What the wiki is for — and what it isn't

Same four disciplines as the AI-datacenter thesis (per CLAUDE.md Section 2.1):

**The wiki is for:** synthesizing what I actually believe about defense/drone supply-chain dynamics; stress-testing each name's structural fit; surfacing chokepoints and cross-company/cross-program relationships; tracking how positioning evolves; and generating uncomfortable conclusions when a name doesn't fit (especially the speculative micro-caps).

**The wiki is not for:** tracking P&L, cost basis, or position sizing; recommending buy/sell/hold; covering the defense sector comprehensively (names that don't inform the thesis don't get pages); or producing confirmation of views I already hold. The honest verdict matters more than the comfortable one — "Should I buy RCAT" gets reframed to "what would have to be true for RCAT's thesis to hold given the ~13% gross margin and the internal-control weakness."

## Scope discipline

Companies earn pages by showing up in primary sources (10-K, 10-Q, earnings calls, 8-K material events) relevant to the thesis — not by being on a list. The tiered map is a starting point; names get pages when they cross the multi-source threshold per CLAUDE.md conventions.

**Initial scope: drones-first.** Unmanned platforms, counter-UAS, autonomy/AI, and the supply-chain chokepoints (rare-earth magnets, secure microelectronics, EO/IR, batteries, edge-AI compute, NDAA compliance).

**Deliberately out of initial scope** (future expansion, sequenced per opportunity — the same mechanism the AI vault used to add domains one at a time):
- Broad munitions / energetics / solid-rocket-motors / magazine-depth (a distinct supply chain).
- European / foreign-listed rearmament names (Rheinmetall and peers) — a separate geography and access question.
- Dedicated directed-energy (laser/HPM weapons) as a standalone domain — touched only where it intersects counter-UAS.

Scope expansion follows source availability, thesis development, and time-bounded events rather than rigid pre-codification — identical to the AI vault's mechanism.

## Evolution

This thesis will evolve as primary-source evidence accumulates and the Tier-3 anchor report's figures are verified against filings. When I revise this file, I will note the change here. The LLM treats whatever is in this file at read-time as the current anchor and flags when ingested sources suggest the file itself needs updating.

Most likely directions:
- **Budget resolution** — the FY2027 reconciliation outcome (post-midterms) will resolve the biggest structural-vs-contingent question. Until then, hold the magnitude figures as requests.
- **Chokepoint maturation** — MP / LSCC / TDY / AMPX primary-source ingests will mature the supply-side thesis from Tier-3 scaffolding to vault-canonical depth.
- **Micro-cap shakeout** — the speculative tier will likely bifurcate (real inflections vs. promotional fades) as SRR/Drone Dominance orders convert or don't, OSC equity outcomes land, and dilution/internal-control issues resolve.
- **Private-to-public transitions** — if Anduril, Shield AI, or others IPO, the investable universe changes materially.

---

**Note on this creation (2026-06-03):** Drafted via Vic-authorized collaborative drafting (Vic-directed; agent-scaffolded) as the second thesis domain in the stocks-wiki vault, parallel to the AI-datacenter `_thesis.md` (which is untouched). Sourced from the Tier-3 research report `raw/research/US-defense-and-drones-report.md` (assessed research-grade) plus prior chat synthesis. **All figures are Tier-3 and several forward numbers (FY2027 DAWG $54.6B, magnet capacity targets, micro-cap guidance) are requests/projections, not realized results — verify against primary filings (CRS reports; SEC 10-K/10-Q/8-K; company IR) before treating as load-bearing.** Scope is drones-first; broad munitions, European rearmament, and standalone directed-energy are sequenced for future expansion. Companion frameworks file: `raw/notes/frameworks-defense-drones.md`. Subsequently codified (Session 123, CLAUDE.md v9.4): the CLAUDE.md Section 1.2 two-domain scope note and the `defense_tier` frontmatter field.
