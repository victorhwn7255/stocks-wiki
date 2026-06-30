---
type: theme
tickers: [NVDA, AMD, MU, SNDK, MRVL, ALAB, CRWV, NBIS]
last_updated: 2026-06-30
---

# KV cache — the inference-memory bottleneck

*Tier-3-anchored dynamics/mechanism theme (per CLAUDE.md Section 3.13 / A2). Anchored on two Vic-curated research rounds — `raw/research/kv-cache-in-LLM-report-1.md` + `kv-cache-in-LLM-report-2.md` (both ~2026-06-30) — plus the adjacent `raw/research/interactive/2026-06-20_ai-memory-hierarchy-kv-cache-disaggregation.md` and the 2026-06-30 Tensormesh video-intel note. The two rounds were independent and converge, which strengthens the anchor; even so, every figure here is a Tier-3 claim, `[verify: …]`-flagged for primary cross-validation, never asserted as vault fact. Describe-don't-recommend; no price targets.*

## Thesis role — what this page is, and the honest verdict

This is the **connective mechanism page** that explains *why* the memory chokepoint the vault already rates highest is durable. It sits beside [[memory-wall]] (the "why memory is the bottleneck" cycle layer), [[HBM-oligopoly]] (supply structure), and [[memory-shortage-winners-losers]] (cycle scoreboard), and it owns the piece those don't: the **KV-cache causal chain** — prefill/decode → bandwidth-bound decode → the context-memory hierarchy — plus the **agentic demand driver** and the **KV-storage-tier infrastructure**.

**Honest verdict (load-bearing).** KV cache is **not itself a chokepoint.** It is a **workload / demand amplifier** that flows downstream and concentrates value at **HBM bandwidth** — a physics/precision-grade, three-player oligopoly chokepoint. The layers built *around* KV (serving software, offload middleware, even much of the compression work) are fast-moving and commoditizing. So the durable money is in the substrate (HBM, secondarily the CXL fabric and NVIDIA's KV-movement stack), **not** in "KV cache" as an asset. Both research rounds explicitly reject the "KV cache is the next Big Data" asset framing — KV state is model-, precision-, tokenizer-, and prompt-order-specific, and often short-lived. This page treats KV cache as the *mechanism that makes the memory chokepoint legible*, with a built-in falsifier — consistent with the vault's gradient (value accrues to geology/physics-grade memory, not to the software racing to shrink the bytes).

## The mechanism (plain language)

A transformer writes one token at a time, and each new token "looks back" at every earlier token through attention. For that lookback, every past token is turned into a **Key** ("what I offer") and a **Value** ("what I contribute"). Those K/V vectors never change once computed — so the model stores them instead of recomputing them every step. That store is the **KV cache**: the model's working memory for the sequence so far. Without it, generating token 1,000 would re-process all 999 prior tokens through every layer, every step — quadratic repeated work that "destroys throughput and latency." (KV cache is an **inference-only** construct; training processes all positions in parallel and uses none.)

**The prefill/decode split is the hinge of the whole story** — two phases with opposite hardware profiles:
- **Prefill** — ingest the whole prompt at once. Dense parallel matrix math → **compute-bound**; draws ~70–100% of peak GPU power `[verify: Splitwise/ISCA]`. Sets time-to-first-token.
- **Decode** — generate output one token at a time, re-reading all model weights *plus the whole growing cache* every step → **memory-bandwidth-bound**; GPU utilization falls to ~20–40% `[verify: report claim]`.

Because decode must re-read the KV cache for every token it emits, **decode is a bandwidth problem by construction** — which is exactly why this routes into HBM and the memory hierarchy rather than into more FLOPs.

## Why it grows — context, concurrency, and the agentic driver

Cache size scales linearly with `2 × layers × kv_heads × head_dim × seq_len × batch × bytes` (the "2" = K and V; **kv_heads**, not query heads, is the lever GQA/MQA pull). Concrete sizing both rounds converge on, for Llama-3.1-70B (80 layers, 8 KV heads, BF16): **~0.32 MB per token → ~40 GB for a single 128K-context user** `[verify: report/SK Hynix]`. At 32K context × 8 users the cache already exceeds the ~140 GB of model weights; long video/VLM streams grow it ~5.6 GB/minute.

The structural demand driver is **agentic inference**: agent loops run input:output token ratios as high as **~100:1** `[verify: practitioner claim]` (prefill-dominated, opposite of a chatbot), and keep persistent context across steps. More users, longer context, multimodal input, and persistent agent memory all multiply KV state. The cleanest real-world proof that this is economically real: hosted **prompt-caching** is now a priced API primitive — OpenAI cuts input cost up to ~90% / latency up to ~80% on cache hits; Anthropic prices cache reads at ~0.1× base input `[verify: vendor pricing pages]`.

## Impact — Memory (the heart of it)

- **HBM bandwidth is the hottest, most durable bottleneck.** Decode is bandwidth-bound, so HBM bandwidth demand stays structurally tight *regardless of capacity-side compression*. This amplifies the existing [[HBM-oligopoly]] / [[memory-wall]] thesis rather than naming a new one — "no relief until 2028" (attributed to Intel's Lip-Bu Tan) `[verify: primary]`.
- **Capacity and bandwidth are two separate failures.** Capacity fails first (long context + concurrency exhaust HBM); bandwidth fails continuously during decode.
- **The context-memory hierarchy** — the structural infra story: **HBM** (active decode) → **DRAM, incl. CXL-pooled** (warm reuse) → **NAND/SSD** (persistence + spill — a "warm context tier" moving up from cold storage) → **remote/networked tiers** (cluster-wide sharing). Compression doesn't delete KV — it **relocates** it down this hierarchy, which *widens* the addressable DRAM/NAND/CXL market even as it shrinks bytes-per-token. Read-through to [[MU]] (HBM + DRAM), [[SNDK]] (NAND-as-warm-context), and the broader [[memory-shortage-winners-losers]] scoreboard.
- **The capacity tier is the contingent bet:** its size depends on the offload thesis holding *vs* compression hollowing out the bytes (see falsifiers below). Bandwidth, by contrast, stays tight either way.

## Impact — Semiconductors / compute

- KV pressure shifts inference-silicon design from **"FLOPs" to "bytes moved per useful token."** The training-era FLOPs race inverts toward memory bandwidth and capacity.
- The prefill/decode split is becoming a **hardware design axis** — compute-dense parts for prefill vs memory-dense parts for decode, and prefill/decode **disaggregation** (separate pools/SKUs; NVIDIA Dynamo, Mooncake) is now in production.
- **SRAM-only inference ASICs are the most exposed** to KV-heavy / long-context / agentic workloads — SRAM is fast but far less dense per GB (Groq ~230 MB on-die, Cerebras ~40–44 GB; both private). Their sweet spot is low-latency, smaller-model, lower-concurrency. **HBM-rich + tiered designs ([[NVDA]], [[AMD]]) are better matched** to the KV future; NVIDIA's software control of KV movement compounds its hardware lead.

## Impact — Infrastructure

- **The serving-software layer is commoditizing.** The breakthroughs — PagedAttention (vLLM, cut KV waste from 60–80% to <4%), RadixAttention (SGLang, prefix reuse), CacheBlend (non-prefix RAG reuse) — are published and open-sourced within months; value leaks to hardware and managed wrappers. Where value *holds* is the **cluster-scale control plane** (routing, offload, reuse, observability): NVIDIA Dynamo/NIXL, Mooncake (Moonshot/Kimi), LMCache, llm-d.
- **CXL memory pooling** is the natural DRAM middle tier and the freshest vault-relevant node: **[[ALAB]]** (Leo controllers; vendor-claimed +75% GPU utilization / 2× inference throughput on KV offload) and **[[MRVL]]** (Structera + in-line memory compression) — both already in [[CXL-memory-disaggregation]]. This page adds the *KV-offload* use-case framing.
- **A dedicated KV storage tier is being formalized** — the least-covered nodes in the vault: NVIDIA **CMX** (CES 2026; an Ethernet-attached flash tier for KV as "agentic long-term memory," persistent across runs) and SK Hynix **HBF** (HBM+NAND hybrid for read-only shared KV); plus Kioxia / Samsung / Western Digital KV-cache SSDs and KV-storage software (WEKA, VAST, DDN) — all private or non-vault, plain-text until a page is warranted.

## Durability / chokepoint read (honest both sides)

- **Durable:** HBM bandwidth (physics/precision-grade oligopoly) + NVIDIA's full-stack KV-movement control (an integration-tier chokepoint — softer than HBM physics, but real, because it owns the fabric that moves KV between tiers).
- **Commoditizing:** the single-node serving-software layer (open-source core; best ideas leak in months).
- **Contingent:** the capacity tiers (DRAM/NAND/CXL) — real, but their size rides on offload winning vs compression.

## What would prove this wrong (pre-registered falsifiers)

The honest "what breaks the read." Each plugs into [[what-could-go-wrong]] / [[forward-edge-tracker]]:
1. **2-bit-everywhere compression at frontier scale** — robust 2-bit KV (e.g. Google **TurboQuant**, vendor-claimed ~5–6× reduction) deployed as default would flatten KV bytes-per-token. Compression announcements have visibly moved memory-sector sentiment (Tier-3 observation; no price claim) — the market already prices this fear.
2. **MLA / hybrid adoption that bounds state** — DeepSeek **MLA** (vendor-claimed ~93% KV reduction, ~5.8× throughput) spreading to Western frontier labs (most still use GQA, no public MLA plans) would shrink the capacity tier.
3. **Architecture shift (the deep falsifier)** — SSM/hybrid models (Mamba/Jamba) use ~O(1) state and can sidestep KV cache entirely. Industry consensus is **hybrid, not pure-SSM**, on a 2–3-year horizon (keep a few attention layers for recall) — so KV cache is not going away near-term, but a frontier-scale hybrid shift would de-value KV-specific software and bound per-unit memory demand.

*Note the asymmetry: every falsifier attacks the **capacity** tier (bytes-per-token). None of them break **bandwidth-bound decode** — which is why HBM bandwidth is the durable read and the capacity tiers are the contingent one.*

## Vault cross-references (dashboard-not-duplicate)

This page owns the KV mechanism + agentic driver + KV-storage tier; it links rather than restates:
- [[memory-wall]] — the bandwidth-not-compute connective layer this sits beside (this page supplies the KV-specific causal chain memory-wall's mechanism section was missing).
- [[HBM-oligopoly]] — the supply structure behind the bandwidth chokepoint.
- [[memory-shortage-winners-losers]] — the cycle scoreboard ([[MU]] vs [[SNDK]] etc.).
- [[CXL-memory-disaggregation]] — the CXL pooling layer ([[ALAB]] / [[MRVL]]); this page adds the KV-offload use case.
- [[training-to-inference-shift]] — KV cache is an inference-only construct; the shift is what makes it matter.
- [[AI-demand-durability]] — the Jevons "efficiency reinvested into more usage" dynamic (cheaper KV → more inference).
- [[hyperscaler-capex]] — the demand the buildout has to keep funding.

## Named entities

| Entity | Role in the KV story | Domain(s) | Vault page |
|---|---|---|---|
| NVIDIA | HBM-rich GPUs + NVLink + Dynamo/NIXL/CMX KV-movement stack — most durable position in the chain | Semis, Infra, Memory | [[NVDA]] |
| AMD | MI300X/MI350 large-HBM inference parts; backs Tensormesh | Semis, Memory | [[AMD]] |
| Micron | HBM (sold out CY26) + DRAM; the capacity+bandwidth read-through | Memory | [[MU]] |
| SanDisk | NAND-as-warm-context KV tier | Memory | [[SNDK]] |
| Marvell | CXL pooling (Structera) + in-line memory compression | Semis, Infra | [[MRVL]] |
| Astera Labs | CXL memory pooling (Leo) — KV-offload mitigation | Infra, Memory | [[ALAB]] |
| CoreWeave / Nebius | inference-serving neoclouds exposed to KV economics | Infra/demand | [[CRWV]] / [[NBIS]] |
| SK Hynix / Samsung / Kioxia / Western Digital | HBM leaders + NAND KV-SSDs + HBF | Memory | — (non-vault) |
| Groq / Cerebras / SambaNova / Etched / d-Matrix | inference ASICs; SRAM-only most KV-exposed; Etched = SSM-shift risk | Semis | — (private) |
| Tensormesh / WEKA / VAST / LMCache / Mooncake | KV middleware / context-memory software | Infra | — (private) |
| DeepSeek / Moonshot / Google / Meta | model labs driving KV innovation (MLA / Mooncake / TurboQuant / GQA) | model arch | mixed |

## Open questions (primary-source verification triggers)

1. **HBM bandwidth tightness "to 2028"** — verify the supply-relief timeline at [[MU]] / SK Hynix / Samsung primary sources, not the Tier-3 attribution.
2. **CXL KV-offload claims** — verify Astera ([[ALAB]]) and Marvell ([[MRVL]]) GPU-utilization / throughput figures at their next 10-Q / call (vendor benchmarks today).
3. **The KV storage tier** — does NVIDIA CMX / SK Hynix HBF show up in primary product revenue or hyperscaler deployment, or stay roadmap? Pre-register for the next NVDA / memory-maker refresh.
4. **Compression adoption telemetry** — track whether 2-bit KV / MLA move from papers to frontier-default (falsifier #1/#2). A confirmed shift upgrades the capacity-tier risk in [[what-could-go-wrong]].
5. **Agentic ~100:1 ratio** — a practitioner claim; watch for a primary-source-grade figure on agentic input:output token mix.

## Source audit notes

- **Two independent Tier-3 research rounds (report-1 + report-2, ~2026-06-30)** plus two adjacent notes (2026-06-20 interactive research + 2026-06-30 Tensormesh video-intel). The two rounds were commissioned separately and **converge** on the mechanism, the four-tier hierarchy, and the honest "not the next Big Data" verdict — which is why the anchor is treated as reasonably firm despite being Tier-3. Both rounds flag the same weak spot: **no energy/power read-through** (the reason Power was dropped from this page's scope). All numbers are vendor/paper/practitioner claims; none are primary.

## Change log

- **2026-06-30** — Page created (Tier-3-anchored dynamics/mechanism theme; Option A standalone, Vic-approved). Scoped to Memory / Semiconductors / Infrastructure; **Power dropped** (reports carry no energy read-through). Owns the prefill/decode → bandwidth-bound-decode mechanism, the agentic demand driver, and the KV-storage-tier infrastructure; links out to the six adjacent memory pages (dashboard-not-duplicate). Honest verdict: KV cache is a demand amplifier, not a chokepoint — durable value sits at HBM bandwidth; capacity tiers contingent on offload-vs-compression; serving software commoditizing. Falsifier set (2-bit-everywhere / MLA / hybrid-SSM) pre-registered for [[what-could-go-wrong]] / [[forward-edge-tracker]].
