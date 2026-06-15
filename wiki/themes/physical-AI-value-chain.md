---
type: theme
tickers: [NVDA, MP, HARMONIC, SANHUA, TUOPU, HENGLI, ZHAOWEI, SHUANGHUAN, ZHONGDA, SLING, NOVT, VPG, OUST, TDY, ARM]
last_updated: 2026-06-15
---

# Physical AI — the value chain and its chokepoints

## Thesis role

Physical AI is AI that acts in the physical world — across four embodiment types (humanoid robots, autonomous vehicles / robotaxis, drones / unmanned systems, and industrial / warehouse robots) that sit on top of one shared stack: a "brain" (robot foundation models), perception and sensors, actuation and hardware, an edge-compute layer, and the materials underneath. It is the explicit broadening target of the Humanoid thesis (`_thesis-humanoid-robot.md`: "humanoid-first, broadening to 'physical AI' later").

**This page is the cross-domain umbrella, not a new thesis.** Physical AI is where the vault's three existing supply chains physically meet — AI-datacenter (the training compute + chips), Defense & Drones (unmanned systems), and Humanoid Robots (embodiment). Most of its layers are already mapped on existing pages; the value of this page is *connecting* them and surfacing the few load-bearing facts that hold across all four embodiments. It is the umbrella over [[humanoid-robot-value-chain]] — that page maps the humanoid hardware stack in full; this one places that stack inside the broader Physical AI map and across the other embodiments.

**Construction note (a fusion, not a copy).** The top of the stack (brain / data / compute) is anchored on a Tier-3 research run (`raw/research/physical-AI-value-chain-report.md`, 2026-06-15; deep-research with adversarial verification). The bottom of the stack (actuation / sensing / materials) is anchored on the vault's existing primary-source pages. The two are kept distinct on purpose, because the research round was strong on the top and weak on the bottom (see Source discipline + What this page does not claim).

**The honest headline.** The one *externally verified* durable chokepoint in Physical AI is the **embodiment-data bottleneck** — robots are held back by a shortage of real-world interaction data, not by compute or dexterity — and NVIDIA has built its position directly on top of it. The actuation, sensing, and materials chokepoints are real but rest on the vault's own primary-source pages; and the long-cited "China controls the materials" framing must be sourced from [[rare-earth-magnet-chokepoint]], **not** from the third-party analyst figures that failed verification this round.

## The Physical AI stack (five layers)

Top to bottom. Each layer names what it cites and the vault pages it connects to.

**1. The "brain" — robot foundation models / VLA / world models.** The newest, fastest-moving, most contested layer. The verified structural fact (Tier-3 anchor): the binding constraint here is *real-world interaction data* — there is no internet-scale, action-labeled dataset for robots the way there is text for language models, and the only way to make that data today is human teleoperation, which scales linearly with human time. Synthetic / simulation data only *narrows* the sim-to-real gap; it does not close it. [[NVDA]] sits on this chokepoint with open "brain" models (GR00T) plus the Cosmos world-foundation-models and a synthetic-data pipeline as the workaround — already vault canon, with disclosed "physical AI" revenue >$6B FY2026 rising to >$9B trailing-12-months (NVDA Q1 FY2027). The other named leaders (Figure, Physical Intelligence, Google DeepMind's Gemini Robotics, Skild) are private, **not in the vault, and are demos / research artifacts rather than products shipping at scale** (Tier-3/4; see What this page does not claim).

**2. Compute & edge inference.** The tie-back to the founding AI-datacenter thesis. NVIDIA *frames* Physical AI as a "three-computer" problem — DGX in the datacenter (training) → Omniverse + Cosmos on RTX-PRO servers (simulation) → Jetson Thor on the robot (inference) — so training and simulation demand route straight into the GPU/datacenter supply chain the vault already tracks (cite as NVIDIA framing, [[NVDA]]). [[ARM]] supplies the CPU cores inside the Jetson edge brain. The *edge-inference silicon* layer is genuinely contested — Qualcomm, Tesla, Google, and Huawei all build rival robot-inference chips — but **none of those edge challengers are vault-covered** (a coverage gap to flag, not paper over); [[NVDA]] still leads edge today. Edge power delivery connects to [[power-semis]] (the 800V architecture + power-management chips that feed actuators and embedded compute).

**3. Perception & sensors.** [[OUST]] — LiDAR + cameras, a pure Physical-AI / robotics 3D-sensing play outside the AI-datacenter scope (theme-anchored). [[NOVT]] and [[VPG]] — six-axis force/torque sensing and strain gages; [[VPG]] is the only vault name quantifying a humanoid revenue line. [[TDY]] — electro-optical / infrared sensors, the sensing chokepoint on the defense/drone leg (it also consumes magnets + germanium upstream — the "squeezed-middle" pattern).

**4. Actuation & hardware.** This is the vault's deepest, best-verified layer — and its detail lives in [[humanoid-robot-value-chain]], so this page names the layer and connects, rather than restating it. The cohort: [[HARMONIC]] (harmonic / strain-wave reducers — the highest-value component layer), [[SANHUA]] + [[TUOPU]] (actuator assembly), [[HENGLI]] (planetary roller screws — precision-grinding credibility validated at primary), [[ZHAOWEI]] (dexterous hands), and the reducer field [[SHUANGHUAN]] / [[ZHONGDA]] / [[SLING]]. Actuation is the layer that differs most by morphology — a humanoid's hands and a drone's rotors need different actuators — but the precision-component chokepoints (reducers, roller screws) recur across the mobile platforms.

**5. Materials substrate.** [[MP]] — rare-earth NdFeB permanent magnets, behind every electric motor in every embodiment. The verified chokepoint claim is anchored at [[rare-earth-magnet-chokepoint]] (China controls ~85-90% of finished-magnet output and ~91% of separation/refining; one Chinese producer roughly equals all non-Chinese output combined). [[MP]] is the cleanest US-listed inverse — a domestic magnet chokepoint owner reshoring the constraint.

## The chokepoint-durability gradient (the vault's own framework hypothesis)

The gradient below is **the vault's framework hypothesis, not an externally verified finding** — the deep-research round verified the data bottleneck but did *not* externally substantiate a chokepoint-durability ranking (the analyst taxonomy it tried to use failed verification). It is grounded instead in the vault's primary-source pages. Ranking by how hard each chokepoint is to relieve (physics/geology > precision-grinding/metallurgy > integration/software):

- **Materials / magnets — physics + geology (most durable).** Rare-earth separation is a chemistry + permitting problem measured in years; the chokepoint is grounded at [[rare-earth-magnet-chokepoint]] (primary-source). Durable, China-controlled.
- **Precision actuation — grinding + metallurgy.** Harmonic reducers and roller screws are gated by precision-grinding capacity and process know-how, not raw availability ([[HENGLI]], [[HARMONIC]], [[humanoid-robot-value-chain]]). Durable, but relievable on a longer horizon than software.
- **The embodiment-data bottleneck — the one *verified* chokepoint (brain layer).** Slow to relieve because real-world data scales with human time; only partially relievable via synthetic data (sim-to-real gap). This is the page's load-bearing verified claim.
- **Edge-inference silicon + integration / software — least durable.** Genuinely contested (multiple credible chip challengers) and the fastest-moving / most relievable layer. Value capture here is unsettled.

## Cross-domain convergence (why Physical AI is the umbrella)

The reason Physical AI is one map and not four is that the bottom three layers (materials, actuation, sensing) and the brain/compute are *shared* across embodiments — humanoids, AVs, drones, and industrial robots all need NdFeB motors, precision actuation, sensors, and an edge brain. The vault names that bridge more than one thesis domain are the convergence nodes:

- **[[MP]] — triple-thesis** (AI-datacenter + defense + humanoid). NdFeB magnets feed every embodiment's motors; the single cleanest US-listed chokepoint owner sitting on three demand curves at once.
- **[[HARMONIC]] — triple-thesis** (equipment + defense + humanoid). Harmonic reducers — the highest-value component layer — with a fortress balance sheet; Japan-listed.
- **[[TUOPU]] + [[SANHUA]] — dual-thesis** (AI-datacenter liquid-cooling + humanoid actuators). The concrete bridge between the datacenter thermal chokepoint ([[liquid-cooling]]) and the humanoid actuation layer — both build server cooling *and* robot actuators.
- **[[NVDA]] — dual-thesis** (datacenter GPU + Jetson robot brain). The brain/compute bridge — but Physical AI is ~1-2% of its datacenter book, so it is optionality already owned via the AI-datacenter thesis, **not** a separate position (see below).
- **The defense / drone leg** connects through [[defense-drone-supply-chain]] (autonomy, secure compute, [[TDY]] sensors, [[MP]] magnets) — the same shared stack expressed in unmanned systems.

The plain summary: Physical AI is less a new thesis than the **structural convergence point where three existing vault supply chains intersect** — the chokepoint owners ([[MP]], [[HARMONIC]], [[TDY]]) and the bridge nodes ([[TUOPU]], [[SANHUA]]) already sit in the vault; this page shows the pattern repeating across four embodiments.

## Investor-access lens

Per `_thesis-humanoid-robot.md`, rank these on chokepoint quality and business health, **not** on the listing flag. The strongest hardware chokepoints are the most China-concentrated cohort in the vault — six China-domiciled names ([[SANHUA]], [[TUOPU]], [[SHUANGHUAN]], [[ZHONGDA]], [[ZHAOWEI]], [[HENGLI]]) *are* the chokepoints, mapped at [[china-exposure]]. [[MP]] is the US reshoring inverse; [[HARMONIC]] is Japan-listed; [[NVDA]] is the US brain/compute owner. The "strongest chokepoints sit behind the worst access" tension that dominates the general US-book view largely dissolves for an investor who can reach US, foreign, and China A-share / Hong Kong listings — so the lens leads with chokepoint quality + health, and access is a secondary descriptor.

## What this page does NOT claim (honest-verdict)

- **The "China owns the materials" claim must come from vault primary pages, not analyst figures.** The third-party claim that "China controls 60-65% of lithium refining and 85-90% of rare-earth processing, making materials the *deepest* chokepoint" **failed verification (0-3)** in the research round and is not carried here. The *verified* magnet-concentration figures live at [[rare-earth-magnet-chokepoint]] (primary-grounded) — those are what this page relies on.
- **The brain-layer leaders are demos, not products at scale.** Figure / Gemini Robotics / Physical Intelligence showed impressive results, but they are research artifacts or open-weight releases; Figure's flagship dishwasher demo was independently confirmed curated ("all objects plastic"). The π0.5 "94% out-of-distribution success" claim **failed verification (0-3)**.
- **The near-term market is small.** Industrial-humanoid revenue is on the order of ~$210-270M in 2026 (Deloitte estimate, ~15,000 units) — a useful reality check against the "$5 trillion" / "$40 trillion" headlines. Real, but very early innings.
- **Do not double-count [[NVDA]].** Its Physical AI exposure is already owned via the AI-datacenter thesis (~1-2% of its datacenter book); it is contained optionality, not a separate Physical AI bet. Physical AI does **not** require its own demand thesis ([[AI-demand-durability]]).
- Per vault discipline: no price, valuation, multiples, or position sizing appear here.

## Open questions

1. **Grounding the actuation / sensing / materials durability ranking.** The gradient above rests on vault primary pages, not external verification — what does each component-maker's primary disclosure confirm about durability ([[HENGLI]], [[HARMONIC]], [[ZHAOWEI]], the reducer field, [[rare-earth-magnet-chokepoint]])? Candidate future work: dedicated component-chokepoint pages (harmonic reducers, roller screws, force/torque sensors) that currently live inline.
2. **Does synthetic data actually close the sim-to-real gap at production scale, or only narrow it?** Every verified source scopes NVIDIA's synthetic-data claim to design intent; no independent production-scale benchmark survived.
3. **Which layer captures the durable value as Physical AI scales** — the brain (open models, contested), the edge-inference silicon (contested), or the actuation/materials chokepoints (where the vault's existing thesis sits)?
4. **The order-vs-capacity test (dated).** Chinese suppliers built actuator/reducer capacity ahead of confirmed OEM demand; confirmed H2-2026 orders are the catalyst, and idle capacity through that window is the falsifier (tracked at [[forward-edge-tracker]]; risk at [[what-could-go-wrong]] Entry 14 humanoid timing/magnitude, Entry 13 rare-earth resolution).
5. **Cross-embodiment evidence beyond humanoid.** The AV/robotaxi and drone embodiments were only indirectly connected (via the NVIDIA compute tie-back) — what verified evidence links them to the shared brain/sensing/actuation layers?

## Source discipline

Top-of-stack (brain / data / compute) is Tier-3/4 — one academic data-scaling meta-analysis plus vendor/lab self-disclosures; every "NVIDIA positions it as the fix" line is scoped to NVIDIA's framing, and none verifies that synthetic data *solves* sim-to-real. Bottom-of-stack (actuation / sensing / materials) is anchored on the vault's primary-source company + chokepoint pages. The full verified/refuted detail is in `raw/research/physical-AI-value-chain-report.md`. This is the fastest-moving theme in the vault (brain-layer version numbers date within a quarter) — refresh against [[NVDA]] and the component pages rather than the dated brain-layer specifics.

## Change log

- **2026-06-15 — created.** Cross-domain dynamics theme; the umbrella over [[humanoid-robot-value-chain]] connecting the AI-datacenter, defense/drones, and humanoid theses through the Physical AI stack. Built as a fusion — brain/data/compute from the Tier-3 anchor (`raw/research/physical-AI-value-chain-report.md`), actuation/sensing/materials from vault primary pages; the verified chokepoint is the embodiment-data bottleneck, with the refuted analyst materials/taxonomy figures explicitly excluded.
