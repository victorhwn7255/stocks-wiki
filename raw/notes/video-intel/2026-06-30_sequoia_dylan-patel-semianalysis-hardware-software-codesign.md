---
type: video-intel
source_tier: 3
channel: "Sequoia Capital"
guest: "Dylan Patel (founder, SemiAnalysis; ~90 people, ~$100M rev rumored)"
upload_date: 2026-06-30
url: https://youtu.be/f6D_aiy8qyU
entities: [NVDA, GOOGL, AMD, AMZN, MSFT, TSM, AVGO, CRWV, NBIS, CORZ, MRVL, ALAB]
new_names: [DeepSeek, Moonshot-Kimi, Zhipu-GLM, Alibaba-Qwen, Tencent, Xiaomi, Anthropic, OpenAI, Cerebras, Groq, SpaceX, xAI, MediaTek, Crusoe, Thinking-Machines, Naveen-Rao, Huawei, SGLang, vLLM]
trackers_touched: [hyperscaler-capex, what-could-go-wrong, AI-credit-spread-watch, forward-edge-tracker, china-exposure]
headline: "SemiAnalysis's Dylan Patel: the real 100x is hardware-software CO-DESIGN (model+kernel+silicon optimized together), not faster chips — so the 'CUDA moat was never about CUDA'; it's that Chinese open models (DeepSeek/Kimi/Qwen) are co-designed for GPUs → run poorly on TPUs → ecosystem defaults to Nvidia. NVDA=general-purpose (global minimum) vs ASICs risk a 'local minimum' as architectures shift. Neocloud edge = balance-sheet-delivery-now + hyperscaler CPU-cloud expertise HURTS AI perf. Jensen backstops neoclouds/neolabs/Chinese labs to force a multipolar world. Compute crunch: 20GW→30GW/yr; Anthropic Q2 profitable ex-SBC, >80% Opus-token margin"
---

# Sequoia — Dylan Patel (SemiAnalysis): "Why Hardware-Software Co-Design Is AI's Real 100x"

- **Channel:** Sequoia Capital (hosts: Sean, Sonia Huang — Sequoia partners, disclosed **large SpaceX investors**) · **Guest:** Dylan Patel, founder of **SemiAnalysis**
- **Upload:** 2026-06-30 · **Duration:** 1:10:15 · **Views/Likes:** ~23,930 / ~692
- **URL:** https://youtu.be/f6D_aiy8qyU

## Source-tier verdict

**Tier 3 — the gold-standard independent semiconductor analyst** (SemiAnalysis is named in CLAUDE.md §2.2 as a Tier-3 source). Patel reasons from a living benchmark (**InferenceX**, >$50M donated hardware, ~15 chip types) + a data-center-by-data-center tracking model + deep supply-chain contacts — the highest-signal Tier-3 source in the feed. **Incentive lean:** he sells research to institutions and is reportedly exploring a venture fund (so a soft pro-ecosystem tilt); the hosts are Sequoia (large SpaceX holders) — hence the repeated SpaceX detours (flagged, not weighted). Even so, his claims are analytically dense and specific; treat magnitudes as soft (spoken) but the *frameworks* as high-quality. First ~14 min is biography — skipped.

## TL;DR

1. **The real 100x is co-design, not faster chips.** Optimizing model + kernels + silicon *together* turns "a 2× here and a 2× there" into 100× (not 8×). Over 3 years the *model layer* gave the biggest gains, then co-design, then hardware. DeepSeek V3's experts were shaped for Hopper; V4 for Blackwell + Huawei.
2. **The "CUDA moat was never about CUDA."** Models write their own kernels now (Claude/Codex), so the *software* moat is partly commoditized. The real moat: Chinese open models (DeepSeek, Kimi, Qwen, Tencent, Xiaomi) are **co-designed for GPUs → run poorly on TPUs → the ecosystem defaults to Nvidia.** If Google open-sourced great models, the same dynamic would favor TPUs.
3. **NVDA vs TPU is not either/or.** Nvidia = general-purpose, always closest to the "global minimum"; ASICs (TPU/Trainium/Cerebras/Groq) risk a **"local minimum"** if model architecture shifts — and labs "don't even know what architecture they'll run in a year." Everyone builds ASICs *and* keeps a general-purpose GPU bucket. Google runs **three** different TPU design programs (Broadcom, MediaTek, + one undisclosed).
4. **Neoclouds exist because hyperscaler CPU-cloud expertise HURTS AI perf** (Nitro NICs, security, custom networks were built for CPU cloud). CoreWeave GPU perf tested *better* than AMZN/GOOGL/MSFT; the durable edge is **balance-sheet ability to deliver compute NOW** + time-to-market, not the tech.
5. **Jensen's strategy = force a multipolar world.** Nvidia backstops neoclouds, funds neolabs, and *loves Chinese labs* — because a world where only OpenAI/Anthropic/Google models exist (and only hyperscalers build compute) is one where "he's screwed."
6. **Compute crunch is demand- AND supply-side:** ~20 GW deployed this year, >30 GW next (net of delays); model TAM (Fable 5/Mythos 5) grew far faster than compute → prices up. **Anthropic Q2 profitable ex-SBC** (maybe incl. SBC by Q3); **>80% per-token margin on Opus** → can pay above-market for every GPU.

## Named entities

| Entity | Speaker | Claim in video | Vault relation | Page? |
|---|---|---|---|---|
| **NVIDIA** | Patel | General-purpose = closest to "global minimum"; ~tens of millions of GPUs, $500B+/yr; CUDA moat is *ecosystem co-design*, not CUDA; Jensen backstops neoclouds/labs for a multipolar world | **refines** the moat thesis | [[NVDA]] |
| **Google (TPU/DeepMind)** | Patel | 10M+ TPUs in ~2yrs (~$100B+/yr); 3 TPU design programs (Broadcom/MediaTek/undisclosed); ICI connects 8,000 chips (no switch) vs NVLink 72; raised capital *despite* huge cash + ~5-10% SpaceX stake | **adds** (TPU scale + capital-need) | [[GOOGL]] |
| **Amazon (Trainium/AWS)** | Patel | Trainium rents <$10B/GW to Anthropic/OpenAI (vs GPU $12-13B/GW); Anthropic made Trainium useful; Nitro/CPU-cloud edge hurts AI perf | **adds** (custom silicon econ) | [[AMZN]] |
| **Broadcom** | Patel | Co-designs one of Google's 3 TPU architectures | confirms (ASIC enabler) | [[AVGO]] |
| **CoreWeave** | Patel | GPU perf/reliability tested *better* than hyperscalers; edge = balance-sheet delivery; NY hedge-fund/crypto origins | **confirms + deepens** neocloud durability | [[CRWV]] |
| **Nebius / Crusoe / Core Sci** | Patel | Neocloud "wild west" — Crusoe (crypto/flared-gas), many started same time & failed; a Crusoe customer just asked to *halt* a buildout | adds (neocloud dispersion + a halt event) | [[NBIS]] [[CORZ]] · Crusoe (no page) |
| **AMD** | Patel | The GPU alternative; "Nvidia margins better" (historical); jack-of-all-trades framing | off-hand | [[AMD]] |
| **TSMC** | Patel | Co-optimizes from consumables/tools upstream to customer chip designs — co-design across the whole stack | confirms (foundry moat) | [[TSM]] |
| **Anthropic** | Patel | Q2 profitable ex-SBC (maybe incl. by Q3); **>80% Opus-token API margin**; trains on TPUs, inferences on Trainium+GPU; bought GPUs above-market | **adds** (monetization datapoint) | Anthropic (no page) |
| **DeepSeek / Kimi / Qwen / Tencent / Xiaomi** | Patel | Chinese open models co-designed for GPUs → run poorly on TPUs → the real "CUDA moat" | **adds** (China open-model ecosystem) | no pages |
| **Cerebras / Groq** | Patel | Great at *fast* inference (SemiAnalysis uses fast mode); but SRAM-based chips can't fit 10T+ param models at long context → risk if models get huge | adds (inference-chip limits) | no pages |
| **Naveen Rao's startup** | Patel | Analog compute + energy-based models; silicon+software+model co-design; long-term bet ("probably won't work quickly") | new name (Sequoia-backed) | no page |

**Auto-caption garble line (all soft):** "Navian Ral / Deaveen" = **Naveen Rao** (MosaicML founder); "trrenium / cranium" = **Trainium**; "Zippui" = **Zhipu (GLM)**; "Neotron" = **Nemotron** (NVIDIA open model); "GPTOSS" = **GPT-OSS**; "SG lang / VLM" = **SGLang / vLLM**; "RadixArc / InRact" = Radix / Inferact (inference-opt startups, hedged); "Cerebrus" = **Cerebras**; "Whimo" = **Waymo**; "ICI" = Google Inter-Chip Interconnect; "Mythos 5 / Fable 5" = the day's new frontier models; "dark GDP" = SemiAnalysis's economic-value framework; "Tinker / Thinking Machines" = Thinking Machines Lab's product. All spoken numbers soft.

## Key claims + numbers (grouped; all soft)

**Co-design = the 100x (~28:00–38:00):**
- > "Instead of being multiplicative to 8×, it's actually 100× because you've optimized across all three layers." Model layer gave the most gains over 3yrs, then co-design, then hardware. `[opinion]`
- **DeepSeek V3 experts shaped for Hopper; V4 for Blackwell + Huawei.** "TPUs suck at running DeepSeek but are really great at running other kinds of models that don't run well on Nvidia." OpenAI models **sparser**; Anthropic **denser** — pulling them toward different hardware. `[verifiable-ish/opinion — architecture]`
- **CUDA moat:** "the CUDA moat is at least partially disentangled because models are great at coding... what people call the CUDA moat has nothing to do with CUDA — it's that the downstream models are co-designed for GPUs." Big labs fork PyTorch / build their own stack; they pick the best hardware and co-design through-and-through. `[opinion — the moat REFINEMENT]`
- Cost/efficiency: model cost for equivalent quality **−60×/yr**; intelligence-per-watt **~40×/yr**; Hopper→Blackwell ~30× on DeepSeek. `[verifiable — InferenceX]`

**NVDA vs TPU / end-state (~44:00–50:00; ~1:05:00):**
- Nvidia general-purpose = closest to the "global minimum"; ASICs risk a **"local minimum"** if architecture shifts. "Labs literally don't know what architecture they'll be doing in a year." → durable market for general-purpose compute. `[opinion]`
- Everyone builds ASICs (Google **hundreds of $B/yr**, others tens of $B) *and* keeps GPU buckets (Google's non-Gemini bets — drug discovery, Waymo — often use GPUs). Google pays **xAI ~$11/GPU/hour**; Google runs **3 different TPU architectures**. `[verifiable-ish]`
- **Jensen's play:** "A world where OpenAI/Anthropic/Google models are the only models is one he's screwed in... a world where hyperscalers are the only ones building compute is one he's screwed in. So he points the allocation gun at neoclouds, backstops their clusters, funds neolabs, and loves Chinese labs — he wants a multipolar world." `[opinion — the strongest strategic frame; feeds the relationship page]`

**Memory + power bottlenecks (~40:00–42:00):**
- **Memory is the tech bottleneck** (not just supply): NAND cell ~25yrs old, DRAM cell ~40yrs old, no cell-level breakthrough; HBM is "just more stacks, faster." **NEW: stacking memory *directly on* the compute chip (not beside it) → "bandwidth explodes"** — "interesting companies and PoCs in that space." `[forward — feeds memory-wall + CXL]`
- **Power/silicon:** ~1 watt/mm² held for 2 decades; Nvidia now ~1,400W, next-gen (Rubin) **2,000W**, Rubin Ultra **~4,000W**. **NEW: pumping >1 W/mm² into silicon → need *less* silicon** (thermal/interference hurdles). `[forward]`
- **CPO:** "everyone knows co-packaged optics happens by end of decade — the debate is 2027/28/29/30." `[forward — CPO timing]`

**Compute crunch + neocloud economics (~50:00–1:10:00):**
- ~**20 GW deployed this year, >30 GW next** (net of delays); every quarter deploys "vastly more" than the prior. Model TAM grew far faster than compute in the last 6-8mo (Opus 45 → Fable/Mythos step-function) → prices up. `[verifiable-ish — SemiAnalysis DC model]`
- **Anthropic Q2 profitable excluding SBC** (maybe incl. SBC by Q3); **Opus-48 per-token API margin >80%** (corp gross margin clawed by Bedrock/Vertex deals). → can pay above-market for every GPU/TPU/Trainium and still run 50%+ GM. `[verifiable at Anthropic — strong monetization signal]`
- **Rental economics:** Trainium <$10B/GW; GPU ~$12-13B/GW (Amazon ~$13B); the **SpaceX–Google GPU deal ~$25M/MW/yr (~$25B/GW)** — "crazy divergence" from the compute shortage + balance-sheet ability to deliver *now*. Colocation power: **$60/kW/mo → $120-160**, up to **$200** (poor-credit tenant / good DC), as low as $80 (India, unreliable grid). `[verifiable-ish]`
- **A gigawatt to Anthropic is worth more revenue than one to OpenAI** (both can sell every GW they have). Google puts **1.5 GW of hardware in a 1 GW DC** (power-sloshing) + utility deals ("2 GW except 3 days/yr"). Google's GW worth more (optical switches, power smoothing, delivery). `[opinion]`
- **Why neoclouds exist:** hyperscaler CPU-cloud expertise (Nitro NICs, security, custom nets) *hurts* AI perf; GPU rental = whole racks on long-term contracts, so the hyperscaler edge fell away. CoreWeave GPU perf tested *better* than hyperscalers; the durable edge = balance-sheet + time-to-market. `[opinion — deepens neocloud-moat-durability]`

**ROI / model progress (his "trigger topics") (~42:00–44:00):**
- "**AI has no ROI** infuriates me... the line has been up-and-to-the-right on capabilities the entire time; benchmarks saturate at 90% then the new ones skyrocket." Pseudo-recursive self-improvement (models help write the next model → faster releases). `[opinion — firmly bull on ROI + progress]`
- **Falsifier he concedes:** "if the work these models can do does NOT expand faster than compute capacity, the tide turns" — over the last 6mo it's levered the *other* way. `[forward — the honest tripwire]`

## Cross-video corpus check

- **Primary source for the "Dylan Patel / SemiAnalysis NVDA-too-big" relay** in the Basis Points note (06-19) — this is the direct, unfiltered version.
- **NVDA moat:** *refines* the Dwarkesh/Jensen note (04-15, "will NVIDIA's moat persist") — Patel's "CUDA moat was never about CUDA, it's ecosystem co-design + the multipolar-world backstop strategy" is a sharper, more skeptical framing than Jensen's own. A **Consensus-vs-Consensus** tension worth holding: the moat is real but *relocated* (from CUDA to model-ecosystem gravity).
- **Memory bandwidth bottleneck** → confirms the [[memory-wall]] / All-In-Baker (06-27) / Tensormesh (06-30) thread; *adds* the memory-on-chip-stacking bandwidth-explosion angle.
- **Neocloud economics** → the deepest external data yet on [[neocloud-moat-durability]] (S177): Trainium-vs-GPU $/GW, balance-sheet-delivery edge, hyperscaler-expertise-doesn't-transfer. Confirms the theme's "borrowed/temporary moat, balance-sheet-not-diversification" verdict from a top source.
- **Anthropic profitability** → a strong data point *against* the monetization-gap bear (feeds [[AI-demand-durability]] + the `ai-monetization-gap` research topic).
- **Chinese open models** → confirms the All-In/Baker GLM + Tensormesh "Chinese open-weights are best" thread; *adds* the co-designed-for-GPU wrinkle.

## Vault cross-reference (company → chokepoint → theme → tracker → relationship)

- **Company:** [[NVDA]] **refines** (moat = ecosystem co-design + multipolar backstop, not CUDA); [[GOOGL]] **adds** (3 TPU programs, ICI-vs-NVLink, capital raise despite cash); [[AMZN]] **adds** (Trainium econ, Nitro hurts AI); [[AVGO]] confirms (Google TPU); [[CRWV]]/[[NBIS]]/[[CORZ]] **confirms + deepens** neocloud durability; [[TSM]] confirms (whole-stack co-optimization).
- **Chokepoint:** [[HBM-oligopoly]] adds (memory-on-chip stacking as the next bandwidth lever); no new chokepoint. Memory-bandwidth as the durable technology bottleneck.
- **Theme:** [[neocloud-moat-durability]] **confirms + deepens** (the single richest external corroboration); [[memory-wall]] confirms + adds; [[CXL-memory-disaggregation]] adds (memory-on-chip / bandwidth); [[CPO-platform-battle]] confirms (CPO end-of-decade timing); [[foundry-competition]] confirms (TSMC co-design); [[AI-demand-durability]] confirms (Anthropic profit + ROI); [[training-to-inference-shift]] adds (inference = biggest market, sparse/dense HW split).
- **Tracker:** see below.
- **Relationship:** [[nvidia-supply-chain-commitments]] — **the strongest external articulation of the "allocation gun" / neocloud-backstop / multipolar-world strategy** yet. Directly confirms + enriches the relationship page's circular-commitment analysis.

## Tracker signals (discovery-only — never edited here)

- **[[hyperscaler-capex]]** — ~20 GW this year → >30 GW next (SemiAnalysis DC model, net of delays); Google + Meta raising *capital despite* huge cash → "tells you how much they think they need to spend." `[verify vs Q2 guidance]`
- **[[what-could-go-wrong]]** — **the clean falsifier, stated by a bull:** *"if the work these models can do stops expanding faster than compute capacity, the tide turns / prices reverse."* Observable mechanism = model-progress stall + $/compute-hour rolling over. Plus a near-event: **a Crusoe customer asked to halt a data-center buildout** — a tripwire-*candidate* worth watching (single anecdote, not fired). NOT fired (crunch still tightening). `[verify: $/GPU-hour trend + any buildout-halt cluster]`
- **[[AI-credit-spread-watch]]** — neocloud model = "hyperlevered equity owners"; the durable edge is *balance-sheet delivery* → the leverage/financing structure is exactly this dial's concern. Anthropic's >80% token margin = a strong credit-positive for the AI-cash-flow side. `[verify vs spread readings]`
- **[[forward-edge-tracker]]** — Consensus-vs-Vault pairs: (a) **NVDA moat relocated** (CUDA → model-ecosystem gravity + multipolar backstop) — sharpen the NVDA-durability entry; (b) **ASIC "local minimum" risk** — TPU/Trainium/Cerebras win niches but general-purpose GPU persists because architectures shift; (c) **neocloud durability = balance-sheet, not tech**. `[sharpens existing entries]`
- **[[china-exposure]]** — Chinese open models (DeepSeek/Kimi/Qwen/Tencent/Xiaomi) co-designed for GPUs = the real Nvidia ecosystem moat; Nvidia *wants* Chinese labs strong (multipolar). Huawei chip named for DeepSeek V4. Soft confirm + a nuance (China open-weights *help* Nvidia's moat).

## Framework & chokepoint placement

No new investable chokepoint, but two **technology-bottleneck** refinements for existing chokepoints: **memory bandwidth** (memory-on-chip stacking as the next lever — a [[memory-wall]]/HBM deepening) and **power density** (>1 W/mm² silicon). On the chokepoint-quality gradient, both sit at the physics/precision-manufacturing tier. **Thesis verdict: refines the AI-datacenter thesis** across compute (NVDA moat), memory (bandwidth), neoclouds (balance-sheet moat), and demand (Anthropic monetization). Off-thesis for Defense/Humanoid.

## Ingest leads (primary-source-verifiable)

1. **Anthropic Q2 profitable ex-SBC + >80% Opus-token margin** → a landmark monetization datapoint (private, so no filing) — monitor for any disclosed figure; feeds [[AI-demand-durability]] + the `ai-monetization-gap` research topic (the vault's key demand falsifier).
2. **Trainium <$10B/GW vs GPU $12-13B/GW; SpaceX–Google ~$25M/MW/yr** → verify the custom-silicon-vs-GPU rental economics at the next [[AMZN]]/[[GOOGL]] disclosures + neocloud filings → refreshes [[neocloud-moat-durability]] + [[nvidia-supply-chain-commitments]].
3. **Google 3 TPU design programs (Broadcom/MediaTek/undisclosed)** → verify AVGO's TPU role + any MediaTek tie at [[AVGO]]/[[GOOGL]] → the custom-silicon competitive map.
4. **Memory-on-chip stacking ("bandwidth explodes")** → identify the "interesting companies" and verify at memory primaries ([[MU]]/SK Hynix) → [[memory-wall]] technology-bottleneck refresh.
5. **Crusoe buildout-halt request** → watch for a cluster (single anecdote now) → [[what-could-go-wrong]] compute-demand tripwire.

**New-name candidates:** none threshold-crossing — the Chinese labs (DeepSeek/Kimi/Qwen), Cerebras, Groq, Crusoe, Thinking Machines, Naveen Rao's startup are private/foreign infra; recurring across the feed but not vault-page candidates yet.

## Vault blind spots / coverage gaps

- **Inference-optimization software layer** (SGLang, vLLM, Radix, Inferact) named repeatedly across notes (here + Tensormesh) with no vault coverage — consistent with the "software layer is where durable value may accrue" thread; a `/connection-finder` lead if the layer ever produces an investable name.
- **The Chinese open-model ecosystem as an Nvidia-moat *support*** (not just a China risk) is a nuance the vault's china-exposure framing doesn't yet capture.

## Contradictions / red flags

- **Soft pro-ecosystem lean** (research-seller, possible VC fund) + Sequoia hosts (SpaceX holders) → the SpaceX detours are promotional; flagged, not weighted.
- **Spoken numbers are soft** — the $/GW, GW-deployment, and margin figures are Patel's estimates/model outputs, not filings; treat as leads.
- **Anthropic profitability** is his characterization of a private company — high-value but unverifiable at primary; hold as Tier-3.
- His ROI-bull framing is a genuine view, but he *concedes* the falsifier (work-expands-faster-than-compute) — the honest tension is preserved, not hidden.

## Self-learning hand-offs

- NVDA-moat-relocation + ASIC-local-minimum + neocloud-balance-sheet-moat → **[[forward-edge-tracker]]** + **[[neocloud-moat-durability]]** (human-gated propagation, not here).
- Anthropic monetization datapoint → feeds the `ai-monetization-gap` research topic + [[AI-demand-durability]].
- Crusoe buildout-halt → **[[what-could-go-wrong]]** tripwire-candidate watch.
- Inference-software layer (SGLang/vLLM/Radix) blind spot → **`/connection-finder`** if an investable name emerges.
- **Tier verdict (restated):** Tier 3 (top-quality), soft pro-ecosystem lean — **do not cite as vault fact; verify against primary sources before any page edit.** This skill touched no wiki/index/log/tracker page.

## Transcript (Tier 3/5 — not a primary source)

> Auto-captions (YouTube `en`), cleaned. ~70-min interview; analysis above extracts signal with approximate timestamps (chapters: bio → InferenceX/benchmarking → sparse-vs-dense → interconnect → CUDA moat → co-design → Cerebras → ROI → 10-yr bets → compute-crunch/neoclouds). Names/numbers soft — see garble line (Naveen Rao, Trainium, Zhipu, SGLang/vLLM, Cerebras, Waymo). First ~14 min (biography: motel/Xbox/forums/quant/homeless-roadtrip) omitted from this excerpt; full text retained below from the InferenceX section.

[Inference = biggest market] "Use of tokens is going to be the biggest market... inference of AI will be many percentage points of GDP, much bigger than oil." InferenceX: a living benchmark — CoreWeave, Crusoe, Nebius, Oracle, Microsoft, Amazon, Google, OpenAI contribute compute; SGLang, vLLM, Radix, Inferact collaborate; Nvidia, AMD, Google (TPUs), Amazon (Trainium) — >$50M donated hardware (>$100M once TPU/Trainium land), ~15 chip types running every model daily (Moonshot, Alibaba, ~5 Chinese models, GPT-OSS, Nemotron). Produces the pareto-optimal throughput-vs-interactivity curve, all public. "Model cost for equivalent quality has dropped ~60× a year."

[The throughput-interactivity curve] "Everything downstream of that curve." Low-latency (low batch, speculative decoding / multi-token prediction) vs batch (pack many users, don't care about time). Anthropic's Claude Code fast mode costs way more than regular; OpenAI's priority queue similar. Some workloads want the 4× cost decrease; some pay 4× more because the person/feedback-loop using the tokens is expensive.

[Space compute] "Space data centers won't matter in the next 3-5 years, but in ~20 years the vast majority of compute will be in space. By 2030, OpenAI + Anthropic alone will have over 100 GW combined for inference; by 2040, terawatts. More than half of *incremental* compute goes to space by 2040; sub-1% by 2030." (Not investment advice — repeated re: SpaceX.)

[Intelligence per watt] "−60× cost / ~40× intelligence-per-watt per year. We're many orders of magnitude from the human brain, but it doesn't matter — much easier to power computers than brains." Three input levels: hardware efficiency, low-level systems (kernels/matmul libs), high-level model/algorithmic. "Most gains came from the *model* layer, then co-design, then hardware — but the real breakthrough is co-designing all three: 2×·2×·2× becomes 100×, not 8×."

[DeepSeek / co-design] "DeepSeek V3's experts were all optimized for Hopper; V4 for Blackwell and Huawei's chip. TPUs are an amazing chip and run all of DeepMind + Anthropic pre-training, but they *suck* at running DeepSeek — and are great at models that don't run well on Nvidia. Deep optimization — expert shapes, network IO, collectives, attention arithmetic intensity — is co-optimized between model, hardware, and infra-software; you can't disentangle the gains." OpenAI models sparser; Anthropic denser. "It's not that China does it better — the West just doesn't tell people what they do."

[CUDA moat] "The CUDA moat is at least partially disentangled because models are great at coding, so software gets commoditized. What people call the CUDA moat has nothing to do with CUDA — it's that DeepSeek, Kimi, Zhipu, Alibaba, Tencent, Xiaomi models are co-designed for GPUs, so they don't run well on TPUs. The ecosystem downstream (inference API providers, RL companies customizing open models) uses Nvidia because the *models* are optimized for Nvidia — not because they care about writing CUDA kernels. If Google open-sourced really good models, people would say 'these don't run well on Nvidia, I should rent TPUs.' Big labs fork PyTorch / build their own stack and just pick the best hardware and co-design through-and-through."

[Cerebras] "Really innovative — very fast inference, a big market; we use fast mode almost exclusively. But running really large models at long context is hard on SRAM-based chips like Cerebras and Groq. If OpenAI's model is 10T+ params at million-context, it won't fit. And the bulk of revenue/usage at the labs is on their *best* model, even when the price goes up (Fable/Mythos)." "Who cares about volume by tokens? It's about the dollars" (F-150 vs Camry analogy).

[Bottlenecks] "Memory: the NAND cell is ~25 years old, the DRAM cell ~40, no cell-level breakthrough — HBM is just more stacks. But new innovations are coming: stack memory *directly on* the compute chip and bandwidth explodes. Power: ~1 W/mm² has held for two decades — Nvidia's at ~1,400W, next-gen 2,000W, Rubin Ultra ~4,000W — but we're finally learning to pump >1 W/mm², which means *less* silicon (thermal/interference challenges)."

[Hot takes] "'AI has no ROI' infuriates me — the capability line has been up-and-to-the-right the whole time; benchmarks saturate at 90%, then new ones skyrocket. The funniest thing is when people have all the facts and get the conclusion completely wrong."

[10-yr bets] Space; co-packaged optics (end of decade, 2027-2030 debate); Naveen Rao's startup (analog compute + energy-based models, silicon+software+model co-design — "probably won't work quickly, but exciting"). "The first really important person I talked to in the semiconductor industry — I baited him on the internet in 2019."

[End-state] "Everyone builds their own ASIC — Google hundreds of $B/yr, others tens of $B — but keeps general-purpose GPU buckets, because ASICs can hit a 'local minimum' and labs don't know their architecture a year out. Google has three different TPU design programs (Broadcom, MediaTek, one I won't disclose). Nvidia stays closest to the global minimum. Niches get carved out — companies make money even if most of the pie goes to Nvidia/TPU/Trainium."

[Compute crunch] "Every quarter we deploy vastly more than the prior — ~20 GW this year, >30 GW next, net of delays. The model TAM (Fable/Mythos vs Opus) grew far faster than compute in 6-8 months, so prices go up. Anthropic is Q2 net-income profitable excluding SBC, maybe including SBC by Q3; Opus-48 per-token margin is north of 80% API price. So they can pay above-market for every GPU and still run 50% GM. If model progress stops, the tide turns — but everyone at the labs says progress keeps going, and models are improving *faster* (pseudo-recursive self-improvement)."

[Neocloud economics] "Trainium rents <$10B/GW to Anthropic/OpenAI; GPUs ~$12-13B/GW; the SpaceX–Google deal was ~$25M/MW/yr — a crazy divergence, driven by shortage + balance-sheet ability to deliver *now*. Colocation power went from $60/kW/mo to $120-160, up to $200 for poor-credit tenants at good data centers. A gigawatt to Anthropic is worth more revenue than to OpenAI. Google puts 1.5 GW of hardware in a 1 GW site and slosh power; does utility deals for 2 GW 'except 3 days a year.'"

[Why neoclouds exist] "In 2023 I wrote 'Amazon's Cloud Crisis' — Nitro NICs, custom SSDs, Graviton were great for *CPU* cloud but *hurt* AI performance. GPU rental = whole racks on long-term contracts, so the hyperscaler edge fell away. Microsoft's data-center teams fell on their face when they had to double their forecast and had to go rent neocloud capacity. CoreWeave's GPU perf tested *better* than the hyperscalers; the edge is balance-sheet + time-to-market — Google sells six months before it has the compute (needs the signed paper for debt), SpaceX says 'it's running now, buy it.'"

[Jensen's strategy] "Jensen hates a world where hyperscalers have all the power. He's blowing money pumping up random AI labs and telling everyone to invest — he wants a multipolar world. That's why he loves Chinese labs. A world where OpenAI/Anthropic/Google are the only models, or hyperscalers the only compute-builders, is one he's screwed in. So he points the allocation gun at neoclouds, backstops clusters, funds neolabs. Throw bait in the water, the best fish survive — Crusoe (crypto/flared-gas guys), CoreWeave (NY hedge-fund/crypto guys); many started the same time and failed. Thinking Machines' Tinker is doing a few hundred million ARR, <6 months old."
