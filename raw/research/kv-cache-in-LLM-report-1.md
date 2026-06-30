# KV Cache in Large Language Models: Mechanism, Frontier, and the Memory-Centric Reshaping of AI Infrastructure

*A deep-research report for a technical, investment-oriented reader. Current as of June 30, 2026. Claims tagged [established], [vendor claim], or [speculative]; source disagreements surfaced rather than smoothed. Not investment advice — structural-positioning and durability-of-value analysis only.*

---

## Executive Summary

The KV (key-value) cache is the working memory of a transformer during text generation: the stored key and value vectors for every token already processed, kept so the model never recomputes them. It is simultaneously the single most important enabler of fast LLM inference and the dominant variable cost and architectural bottleneck of serving models at scale. Understand the KV cache and the next several years of AI hardware roadmaps, inference margins, and infrastructure investment become legible.

**The core mechanism and why it matters.** Inference has two phases: *prefill* (process the whole prompt in parallel — compute-bound) and *decode* (generate tokens one at a time, re-reading the entire cache each step — memory-bandwidth-bound) [established]. The cache grows linearly with context length × batch size and, at long context and high concurrency, exceeds the model weights themselves — for Llama-3.1-70B at 128K context with 8 concurrent users the KV cache is ~2.4× the size of the model weights [established]. This is the "memory wall": GPUs are fast calculators starved for memory bandwidth and capacity.

**The technique frontier is maturing and consolidating.** Architectural fixes (GQA, and DeepSeek's Multi-head Latent Attention / MLA) are now baked into frontier models; PagedAttention (vLLM) and RadixAttention (SGLang) made cache reuse a production default; prefill/decode disaggregation and tiered KV offload (Mooncake, NVIDIA Dynamo, LMCache) are now production infrastructure, not research [established]. State-space and hybrid models (Mamba) eliminate the KV cache entirely but have not displaced transformers for frontier quality [established].

**The industry impact splits three ways:**
- **Memory/storage is the clearest beneficiary.** Growing KV demand pulls HBM (bandwidth + capacity), CPU DRAM, and now a dedicated NVMe/SSD "KV tier" (NVIDIA CMX, WEKA, VAST). The bull case is data-gravity and tiered offload; the bear case is that compression (FP8/FP4, MLA, eviction) cuts bits-per-unit-of-work — Google's TurboQuant reportedly moved memory stocks on exactly this fear [established/contested].
- **Agentic workloads are the structural demand driver.** Agents have ~100:1 input-to-output token ratios and repeated, shared context, making prefix/prompt caching the highest-leverage cost lever in AI; cached tokens are billed up to 90% cheaper [established].
- **Durable value is contested.** Hardware (NVIDIA, memory oligopoly) captures the most defensible value; serving software is commoditizing toward open-source (vLLM/SGLang) with thin commercial wrappers; model labs capture value through architecture (MLA) that is model-version-bound and recomputable — the key disanalogy with "KV cache is the next Big Data."

**Bottom line:** KV cache management has shifted from an inference micro-optimization to a first-class architectural layer that is reshaping the memory and storage hierarchy of the AI datacenter. The most durable value accrues to the memory/HBM oligopoly and to NVIDIA's full-stack control of the KV movement fabric; the serving-software layer is strategically critical but structurally commoditized; efficiency gains are real but, on current evidence, are being outrun by usage growth (a Jevons dynamic) rather than shrinking aggregate demand.

---

## PART A — Foundations: How the Mechanism Works

### A.1 What the KV cache is

A transformer generates text autoregressively — one token at a time, each new token conditioned on all previous ones. The attention mechanism works by projecting each token into three vectors: a **Query (Q)** ("what am I looking for"), a **Key (K)** ("what do I offer"), and a **Value (V)** ("what I contribute if attended to"). To generate token *t*, the model takes *t*'s query and compares it against the keys of all prior tokens, then takes a weighted sum of their values [established].

The crucial observation: the keys and values of past tokens do not change as new tokens are generated. Without caching, generating each new token would require recomputing K and V for the entire sequence from scratch — turning generation into an O(n²) repeated-work disaster [established]. The KV cache stores those already-computed K and V vectors so each new step computes only the single new token's K/V and appends it. This converts the per-step cost from "recompute everything" to "compute one token and read the cache," the difference between quadratic and linear cumulative work [established]. The trade is memory for compute: the cache must live in fast memory and grows with every token. (Note: the KV cache is an *inference-only* construct — it is not used during training, where all positions are processed in parallel with full backprop.)

### A.2 Prefill vs decode — and why "the input is the expensive part"

Inference has two distinct phases with opposite hardware profiles [established]:

- **Prefill** processes the entire input prompt in one parallel forward pass, computing K/V for every prompt token at once. Because all tokens are processed together, this is a dense matrix-matrix multiplication (GEMM) that saturates the GPU's arithmetic units — it is **compute-bound** (limited by FLOPs). Prefill draws 70–100% of peak GPU power (Patel et al., *Splitwise*, ISCA 2024) [established].
- **Decode** generates output tokens one at a time. Each step is a matrix-vector multiplication (GEMV) that must read the entire model weights *and* the entire KV cache from memory to produce a single token. Arithmetic intensity collapses to ~60–80 operations per byte and GPU utilization falls to 20–40% — it is **memory-bandwidth-bound** [established].

This explains the counterintuitive economics: even though API providers price input ("prompt") tokens far cheaper than output tokens, the prefill of a long input is often the genuinely expensive computational event, because prefill cost grows super-linearly with input length and the resulting KV cache then burdens every subsequent decode step. In agentic workloads where the input-to-output ratio is ~100:1 (Manus) [established], prefill and cache management dominate the cost structure — which is exactly why cached input tokens are discounted so heavily (see Part D.5).

Per-token cost intuition: decode latency is governed by how many bytes must be read per token. If decoding reads ~140 GB of weights + tens of GB of cache per token at ~3–8 TB/s of HBM bandwidth, the floor on inter-token latency is set by bandwidth, not math. This is why memory-dense GPUs (H200, with more HBM3e capacity and bandwidth) are better decode engines than compute-dense ones, and why disaggregation pairs different silicon to each phase (Towards Data Science) [established]. A nuance worth flagging: these bottlenecks *shift* — very long prefills become memory-bound (attention's quadratic term dominates), and large-batch decode can become compute-bound (SPAD, arXiv 2510.08544; arXiv 2601.19910) [research].

### A.3 The KV-cache size problem (with worked math)

The standard formula for the KV cache size (multi-head attention) is:

**KV bytes = 2 × layers × kv_heads × head_dim × seq_len × batch × bytes_per_element**

The factor of 2 is for K and V. "kv_heads" (not query heads) is what matters — the central insight behind GQA/MQA [established].

**Worked examples:**
- **Per-token, generic 32-layer/32-head/128-dim model at FP16:** 2 × 32 × 32 × 128 × 2 bytes ≈ 0.5 MB per token across all layers [established]. A 4,096-token request then needs ~2 GB for one user.
- **Llama-3.1-70B with GQA (80 layers, 8 KV heads, 128 head-dim, FP16):** each token's KV state is 2 × 80 × 8 × 128 × 2 = 327,680 bytes ≈ 0.33 MB/token. A 4,096-token prompt produces ~1.34 GB of cache; a comparable MHA model (64 KV heads) would need ~2.6 MB/token — the 8× reduction from GQA (Towards Data Science / Spheron) [established].
- **128K context, Llama-3.1-70B:** ~40 GB of KV cache for a *single* user (multiple independent sources converge on ~40 GB) [established]. At 32K context with 8 concurrent users, the KV cache already exceeds the 140 GB of model weights; at 128K with 8 users it is ~2.4× the weights (Spheron) [established].
- **Llama 4 (10M-token context support):** can require a ~5.4 TB cache — "requiring dozens of GPUs just to store these values" (SK Hynix H³ paper) [vendor/research claim].
- **Video (VLM) at 30 fps with ViT-style encoding:** cache grows ~5.6 GB per minute of video, OOM-ing a 24 GB GPU in under four minutes (arXiv 2602.14236) [research claim].

The crossover point — where cache memory equals weight memory — is the key deployment threshold: below it, hardware choice is driven by model size; above it, cache management strategy dominates (Brenndoerfer) [established]. Long context + high concurrency drives you firmly above it, and that is where "the memory wall bites."

### A.4 "Lost in the middle" and attention patterns relevant to cache reuse

Two empirical phenomena shape what can be safely compressed or evicted:

1. **"Lost in the middle"** (Nelson F. Liu et al., Stanford, TACL 2024, arXiv 2307.03172): LLM accuracy follows a U-shaped curve over input position — highest when relevant information is at the beginning or end of the context, significantly degraded in the middle, even for explicitly long-context models [established]. This is both a limitation (long contexts are not used uniformly) and an opportunity (middle-context tokens are candidates for eviction).

2. **Attention sinks** (StreamingLLM, Xiao et al.): the first few tokens absorb a disproportionate share of attention mass regardless of semantic content — one pilot found the position-0 sink holds ~75% of prefix attention mass (arXiv 2605.18053) [established/research]. Retaining sink tokens is essential for coherent generation under aggressive cache compression; naively evicting them collapses output quality (F1 ≤ 0.064) [research claim]. This insight underpins nearly every eviction and streaming method.

The strategic upshot: attention is sparse and non-uniform, which is *why* eviction, sparsity, and compression methods can work at all — but the same patterns mean naive compression destroys quality, so the frontier is about *which* tokens to keep.

---

## PART B — The Research & Technique Frontier

### B.1 Architectural KV reduction (deployed, frontier-default)

- **Multi-Query Attention (MQA)** — Noam Shazeer, Google, 2019 ("Fast Transformer Decoding: One Write-Head Is All You Need," arXiv 1911.02150). All query heads share a *single* K/V head, shrinking the cache to single-head size. Maximum memory savings, but quality degradation vs MHA [established].
- **Grouped-Query Attention (GQA)** — Ainslie, Lee-Thorp, de Jong, Zemlyanskiy, Lebrón, Sanghai, Google Research, 2023 ("GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints," arXiv 2305.13245, EMNLP 2023). Uses an intermediate number of KV heads (more than 1, fewer than query heads), giving a tunable quality/memory trade-off; the abstract notes "uptrained GQA achieves quality close to multi-head attention with comparable speed to MQA," and that existing MHA checkpoints can be uptrained to GQA using ~5% of original pretraining compute. GQA is now the workhorse default — Llama 2/3, Mistral 7B all use it [established].
- **Multi-head Latent Attention (MLA)** — DeepSeek, introduced in DeepSeek-V2 (2024), extended in V3/R1. Instead of reducing head count, MLA compresses K/V into a shared low-rank latent vector that is cached; head-specific K/V are reconstructed on the fly via up-projection. DeepSeek claims MLA *both* shrinks the cache dramatically *and* improves quality over MHA — a rare Pareto improvement [vendor claim, with independent corroboration]. The TransMLA paper (arXiv 2502.07864) proves GQA can always be represented by MLA at the same cache overhead (but not vice versa), and offers a post-training conversion of GQA models (Llama, Qwen) to MLA [research claim]. **Disagreement to flag:** despite MLA's demonstrated efficiency in DeepSeek V2/V3/R1, most major Western labs continue to use GQA with no public plans to adopt MLA — TransMLA's authors note this explicitly [established]. MLA is more invasive to the serving stack (extra projection logic, RoPE-handling complications), which is the likely reason.

### B.2 Compression & quantization (deployed to research-stage)

- **FP8 KV cache** — natively supported on NVIDIA Hopper (H100) and Blackwell; dropping bytes_per_element from 2 (BF16) to 1 (FP8) halves cache size, doubling batch or context within the same VRAM. Widely deployed; generally near-lossless [established].
- **KIVI** (Liu et al., ICML 2024) — tuning-free asymmetric 2-bit quantization; key insight: quantize the **key cache per-channel** and the **value cache per-token**. Achieves ~2.4× less peak memory and up to 2.05× throughput; INT4 maintains accuracy but 2-bit shows meaningful degradation on hard reasoning tasks [established/research].
- **KVQuant** (Hooper et al., Berkeley, NeurIPS 2024) — non-uniform, outlier-aware, per-channel key quantization with custom CUDA kernels; enables up to 10M-token context on a multi-GPU system; ~14% better than KIVI at similar bit-width. Caveat: KVQuant's sparse-dense handling can be hardware-unfriendly/slow on GPUs; and at 2-bit on reasoning models accuracy can collapse (MixKVQ table shows KVQuant KV2 dropping to near-zero on AIME/MATH for distilled R1 models) [research claim].
- **TurboQuant** (Google DeepMind, 2026) — post-training KV quantization reported to cut KV memory 5–6× with minimal perplexity loss; notable for its *market* impact (see Part D.1) [vendor/research claim].
- **PatternKV, RotateKV, Ada-KV, SQuat, InnerQ** — active 2025–26 research frontier pushing robust 2-bit quantization; not yet standard in production [research-stage].

The trajectory: **FP8 is the deployed default; 4-bit is increasingly safe; 2-bit remains research-stage** because reasoning/long-generation tasks are sensitive to cumulative quantization error across the sequence [established/research].

### B.3 Eviction & sparsity (research-stage, partial deployment)

- **StreamingLLM** (Xiao et al., 2023) — retains a few "attention sink" tokens plus a sliding window of recent tokens, enabling effectively infinite streaming. Fast and hardware-friendly, but a fixed positional rule that discards middle context [established].
- **H2O (Heavy-Hitter Oracle)** (Zhang et al., 2023) — dynamically keeps "heavy hitter" tokens (high cumulative attention) plus recent tokens; up to 29× throughput over HuggingFace Accelerate on OPT models at 20% budget. A decode-phase method — does not reduce prefill cost [established/research].
- **SnapKV** (Li et al., 2024) — compresses the prompt KV during prefill using an "observation window" at the prompt's end to vote (via pooled attention) for important positions [research].
- **Scissorhands, PyramidKV/PyramidInfer, FastGen, CAKE, Ada-KV** — variants on hierarchical/per-head budget allocation [research].

**Critical caveat surfaced by recent work** (arXiv 2605.18053): under a shared global cache budget, seven popular eviction policies (incl. H2O, SnapKV, StreamingLLM) collapse to near-zero quality (F1 ≤ 0.064) *unless* structurally critical boundary tokens (delimiters, sinks) are explicitly protected; reserving 10% of cache at each boundary recovers 69–90% of reference quality. Eviction is more fragile than vendor framing suggests, and is much less deployed at frontier scale than quantization or reuse [research claim — important falsifier for aggressive eviction theses].

### B.4 Reuse & sharing (deployed, foundational)

- **PagedAttention / vLLM** (Kwon et al., UC Berkeley, SOSP 2023) — manages the KV cache in fixed-size pages like OS virtual memory, cutting fragmentation waste (historically 60–80% of allocated KV memory was wasted) to <4% and enabling flexible sharing across requests. The single biggest leap in serving efficiency; every major framework now uses it. vLLM adds Automatic Prefix Caching (APC) [established].
- **RadixAttention / SGLang** (Zheng et al.) — stores KV in a radix tree keyed by token sequence, enabling automatic, zero-config prefix discovery and reuse across requests; excels on multi-turn and multi-agent workloads sharing system prompts, with reported 75–95% cache hit rates on shared-prefix workloads [established/vendor]. At unique-prompt workloads it performs similarly to vLLM; the advantage opens up only with shared prefixes [established].
- **Prompt/prefix caching** (production at OpenAI, Anthropic, Google, DeepSeek) — see Part D.5.
- **Non-prefix reuse — CacheBlend** (Yao et al., LMCache team, EuroSys 2025 best paper, arXiv 2405.16444) — the key advance beyond prefix caching. In RAG, retrieved chunks are rarely the exact prefix, so standard prefix caching barely helps. CacheBlend reuses precomputed KV of *any* chunk and selectively recomputes only a small subset (~15%) of cross-attention-critical tokens, achieving near-100% hit rate and 2.2–3.3× lower TTFT with negligible quality loss (F1 degradation ~0.02) [research, peer-reviewed]. Successors: CacheClip, RAGCache, Cache-Craft [research].

### B.5 Offload & disaggregation (production infrastructure as of 2025–26)

- **Prefill/decode disaggregation** — Splitwise (Patel et al., Microsoft/Azure, ISCA 2024) and DistServe (Zhong et al., 2024) split the two phases onto separate GPU pools, each tuned to its bottleneck (compute-dense for prefill, memory-dense for decode). Splitwise reports 1.4× throughput / 20% lower cost; DistServe reports 2×+ P99 latency improvements. **Now production** in NVIDIA Dynamo, vLLM, SGLang, Ray Serve — Meta, LinkedIn, Mistral, HuggingFace run it [established]. **Falsifier to flag:** disaggregation is *not* always beneficial — the KV transfer overhead between pools can exceed the benefit for short-prompt/low-concurrency workloads, and when context becomes very long, prefill itself shifts toward memory-bound, undermining the hardware-specialization rationale (arXiv 2601.19910, 2603.21354) [research]. Chunked prefill is the lower-cost first step for most deployments.
- **KV offload to CPU DRAM / SSD / NVMe** — the hot→cold hierarchy: HBM (active) → CPU DRAM → local SSD/NVMe → networked/object storage. NVIDIA Dynamo's KV Block Manager and LMCache both implement this, scaling cache to "petabyte levels" [vendor claim]. Perplexity's production stack transfers KV layer-by-layer over RDMA/libfabric so decode can start on early layers while later layers are still in transit [established].
- **Mooncake** (Moonshot AI / Kimi, FAST '25, arXiv 2407.00079) — the canonical KVCache-centric disaggregated architecture. Pools underused CPU/DRAM/SSD/NIC across the GPU cluster into a disaggregated KV cache with a global scheduler. Reported 59–498% higher effective request capacity on real traces; in production it lets Kimi handle 115%/107% more requests on A800/H800 clusters; runs across thousands of nodes processing 100B+ tokens/day [vendor/peer-reviewed]. Transfer Engine and Mooncake Store are open-sourced and integrate with vLLM/SGLang.
- **LMCache** — open-source KV cache layer (UChicago origin) that offloads/persists KV across CPU DRAM and remote storage and implements CacheBlend; integrates with vLLM, SGLang, NVIDIA Dynamo, TensorRT, KServe. Commercialized by Tensormesh (Part C) [established].
- **GPUDirect Storage / NIXL / cuObject** — NVIDIA's data-movement plumbing (NIXL = NVIDIA Inference Xfer Library) for low-latency RDMA streaming of KV between GPU memory and storage tiers; cuObject streams S3 payloads directly into GPU VRAM [vendor].

### B.6 Architecture-shift risk: SSMs, linear attention, hybrids

- **Mamba** (Gu & Dao, 2023, arXiv 2312.00752) — a selective state-space model with O(1) constant memory per step during inference: **no KV cache at all**. The recurrent state is fixed-size regardless of sequence length. Reported 4–5× higher inference throughput than a similar-size transformer (no cache → much larger batches) [established/research]. Mamba-3 (2026, arXiv 2603.15569) continues the line.
- **Linear attention** — replaces softmax with a dot-product kernel, viewable as an RNN with constant-memory recurrent inference; Mamba-2 is a special case (Structured State Space Duality, Dao & Gu 2024) [established].
- **Hybrids** — Bamba (IBM, Mamba2-based, 2× throughput vs comparable transformer), Hunyuan-TurboS (Transformer-Mamba2-MoE, 560B params), Jamba, and others interleave a few full-attention layers (for precise recall) with many SSM/linear layers (for cheap memory). This is the pragmatic middle path [established].

**Where the consensus is heading:** SSMs/linear attention solve the KV problem by eliminating it, but pure SSMs have **limited state capacity and irreversible context compression** that hurt fine-grained recall and complex reasoning — the very capabilities frontier labs sell [established]. The industry consensus as of mid-2026 is **hybrid**, not pure-SSM: keep some attention for recall, replace the rest to bound memory. Serving frameworks (SGLang, vLLM/Jenga) are racing to handle the resulting heterogeneous KV shapes (full-attention layers + SSM state + sliding-window), which is now a leading systems challenge [established]. Transformers with optimized KV caches remain the frontier-quality default; the KV cache is not going away on a 2–3 year horizon.

**Winning approaches / open problems.** Winning and deployed: GQA/MLA, PagedAttention/RadixAttention, prefix+non-prefix reuse, FP8 cache, prefill/decode disaggregation, tiered offload. Promising but research-stage: robust 2-bit quantization, aggressive eviction, hybrid-model serving. Open problems: composability (speculative decoding + hybrid VLM + disaggregation + unified prefix cache simultaneously); eviction robustness; quantization for reasoning models; and KV-cache management for million-token and multimodal contexts.

---

## PART C — Companies & Ecosystem (durable vs commoditized)

### C.1 Inference-optimization / KV-cache startups

- **Tensormesh** (San Francisco) — commercializes the open-source **LMCache** (8,000+ GitHub stars). Founded by UChicago/Berkeley/CMU researchers; CEO Junchen Jiang (UChicago faculty), LMCache co-creator Yihua Cheng. Raised $4.5M seed (Oct 2025, Laude Ventures) + $20M extension (May 2026) → $24.5M total. **The investor list is the story:** AMD Ventures, CoreWeave, and NVIDIA's NVentures all backed a company whose product *reduces the GPU cycles their hardware consumes* — a strong signal of industry consensus that the KV layer is strategically central. Samsung's NAND division is a collaborator. Pricing: cached input tokens billed at **$0 permanently** on serverless. Claims up to 10× lower latency/GPU spend [vendor claim]. **Durability read:** the moat is open-source mindshare + enterprise usability/observability, not proprietary algorithms (the core is open). Commoditization risk is real, but the strategic-investor syndicate and storage-vendor partnerships suggest a credible "control point" position in the emerging KV-data stack.

### C.2 Open-source serving stacks (commoditizing core, monetized at the edges)

- **vLLM** — UC Berkeley origin (PagedAttention); the de facto open standard; broad commercial adoption (Red Hat/IBM ship and support it; Meta, Mistral, HuggingFace run it). Monetized indirectly via vendors who support/host it.
- **SGLang** — RadixAttention; strong in multi-turn/agentic; backed by an active community, used in DeepSeek/Kimi-scale deployments.
- **NVIDIA Dynamo + TensorRT-LLM** — NVIDIA's open inference framework (Dynamo, GA at GTC 2026) for distributed/disaggregated serving with KV-aware routing and KV offload; TensorRT-LLM is the optimized engine. **The point of Dynamo is to make NVIDIA hardware the best place to run any framework** — it backends vLLM, SGLang, TensorRT-LLM. Monetized via hardware pull-through + NVIDIA AI Enterprise.
- **Hugging Face TGI** — production serving with PagedAttention-style features; monetized via HF platform.
- **llm-d** — vLLM-based disaggregated platform; KV-state-aware scheduling; inherits one-model-per-node constraints from vLLM [research/early-production].
- **Mooncake** — open-sourced by Moonshot AI; functions as a KV-store/transfer layer beneath vLLM/SGLang.

**Durability read:** serving software is structurally **commoditized** — the best ideas are published and open-sourced within months. Value capture is thin at the framework layer and accrues instead to (a) the hardware vendor that controls the movement fabric (NVIDIA), and (b) enterprise-support/managed-service wrappers (Red Hat, Baseten, neoclouds).

### C.3 Model labs driving KV innovation

- **DeepSeek** — MLA (the most important architectural KV innovation); demonstrates frontier quality at low inference cost; automatic context caching priced at ~98% discount on cache hits (V4 Flash: $0.0028 vs $0.14 per MTok miss) [established].
- **Moonshot AI / Kimi** — Mooncake; KVCache-centric serving at scale.
- **Google** — GQA (origin), TurboQuant, Gemini context caching.
- **Meta** — GQA adoption across Llama; vLLM in production.
- **Anthropic, OpenAI** — prompt caching productization at 90%/50–90% discounts (Part D.5).

**Durability read:** labs capture value through architecture (MLA) and through *owning the cache-hit discount economics* of their APIs. But architectural advantages are model-version-bound and replicable (TransMLA converts GQA→MLA post-hoc).

### C.4 Hardware: GPU and inference-ASIC

- **NVIDIA** — owns the full stack: HBM-rich GPUs (H200/B200/GB200, Rubin ramping), the NVLink/NVSwitch scale-up fabric, Dynamo/NIXL/CMX KV movement software. **The most durable position in the entire KV value chain.** Blackwell B200: native FP4 (boosts prefill), ~8 TB/s HBM3e (accelerates decode) [established/vendor].
- **AMD** — MI300X/MI350 with large HBM; AMD Ventures backs Tensormesh; positioned as the credible #2.
- **SRAM-centric inference ASICs** — **Groq** (LPU, ~230 MB on-die SRAM, no HBM → needs hundreds/thousands of chips for large models; pivoted to selling inference; won the ~$1.5B Saudi Sovereign AI Infrastructure deal per Forbes, Oct 2025, and raised $750M at a $6.9B valuation, Sept 2025), **Cerebras** (WSE-3 wafer-scale, ~40–44 GB on-chip SRAM, ~21 PB/s on-chip bandwidth, fastest single-stream latency; raised a $1.1B Series G at an $8.1B post-money valuation, Sept 2025, led by Fidelity and Atreides), **d-Matrix** (Corsair, digital in-memory compute, 512 MB SRAM/chiplet). These bet on keeping weights/state in ultra-fast SRAM to beat the memory wall on latency — but SRAM is far less dense and far more expensive per GB, so large KV caches and long context are an architectural challenge. Their sweet spot is low-latency, smaller-model, lower-concurrency serving [established].
- **Three-tier memory ASICs** — **SambaNova** (SN40L: SRAM + HBM + DDR, can hold KV across the hierarchy without external appliances; 16 chips serve DeepSeek-R1 671B) [vendor].
- **Etched** (Sohu) — transformer-only ASIC, hard-wires the architecture; high risk if architectures shift to SSMs/hybrids [speculative].

**Durability read:** the memory/KV problem is precisely where SRAM-only ASICs are most exposed (long context, high concurrency, agentic). HBM-based architectures (NVIDIA, AMD, SambaNova) are better positioned for the KV-heavy future; NVIDIA's software control of KV movement compounds its hardware lead.

### C.5 Memory & storage layer (the clearest beneficiary)

- **HBM oligopoly** — **SK Hynix** (~50–62% share, leads HBM3E, reportedly ~70% of NVIDIA Rubin HBM4), **Samsung** (~17–35%, HBM4 qualifying with NVIDIA), **Micron** (~11–22%, only US-domiciled, sold out CY26 capacity, exited consumer to focus on AI). HBM is the tightest chokepoint in AI; "no relief until 2028" (Intel's Lip-Bu Tan) [established]. **Sources disagree on exact shares** (Counterpoint vs TrendForce vs others, and bit-share vs revenue); directionally SK Hynix leads, Micron is tightest-supplied.
- **HBF (High-Bandwidth Flash)** — SK Hynix's proposed HBM+NAND hybrid (H³) to store read-only shared KV caches in flash adjacent to the GPU [research/vendor].
- **NAND/SSD for the KV tier** — **Micron, SanDisk, Kioxia, Samsung, Solidigm** (Solidigm's "Inference Context Memory Storage" tier). NVIDIA's **CMX** (formerly ICMS, announced CES 2026) formalizes a new "G3.5" Ethernet-attached flash tier dedicated to KV cache as "agentic long-term memory," persistent across inference runs [vendor].
- **KV-storage software vendors** — **WEKA** (Augmented Memory Grid, demonstrated 270 GB/s KV streaming across 8 H100s via a NIXL plugin), **VAST Data** ("context memory," frames KV as "Really Big Data"), **DDN**, **NetApp** (ONTAP + LMCache), **Pure Storage** (Everpure). These sell the persistent KV tier.
- **CXL / memory-pooling** — **Astera Labs** (Leo CXL Smart Memory Controllers, up to 2TB/controller; with Penguin Solutions demonstrated 75% higher GPU utilization / 2× inference throughput on KV offload; in Azure M-series preview), **Marvell** (Structera controllers + CXL switch; in-line hardware memory compression at a cited 2–3.6× — field reporting is more conservative at 1.8–2×; reported 4.8× inference throughput and 82.7% lower TTFT on a 16TB pooled-memory config) [vendor claims]. CXL is complementary to NVLink (CPU-to-memory pooling vs GPU-to-GPU scale-up). Academic work shows offloading KV to CXL memory can cut GPU usage up to 87% while maintaining latency (arXiv 2511.00321) [research].

**Durability read:** this is where KV-cache growth most directly and durably pulls demand — and where the bull/bear debate (Part D.1) actually matters for the numbers.

### C.6 Cloud & neocloud

- **Hyperscalers** (Azure, AWS, Google) — productize prompt caching and KV offload; Azure runs Splitwise/Dynamo; control long-term agreements (LTAs) that lock up memory supply. **TrendForce projected combined capex of the top-8 CSPs (Google, AWS, Meta, Microsoft, Oracle, Tencent, Alibaba, Baidu) to exceed $710B in 2026 (~61% YoY growth)** in its Feb 2026 release, then **revised it up to ~$830B for the top nine (adding ByteDance), ~79% YoY**, in May 2026 — a large share flowing into memory procurement [analyst].
- **Neoclouds** (CoreWeave, Together, Baseten, Fireworks, GMI Cloud, Spheron, Lambda) — inference-serving exposed; CoreWeave both invests in Tensormesh and would benefit from selling more efficient inference. Baseten reports 2× faster inference via Dynamo KV-aware routing [vendor].

---

## PART D — Industry Impact

### D.1 Memory — does KV demand pull more HBM/DRAM/NAND?

**Yes, net — but the split across the hierarchy is the nuance, and the bear case is real.**

The hot→cold KV hierarchy is now explicit: **HBM** (active decode, highest bandwidth) → **CPU DRAM** (staging, hot reuse) → **local SSD/NVMe** (warm, persistent) → **networked/object storage / CXL pools** (cold/shared). NVIDIA's CMX inserting a dedicated "G3.5" flash tier and SK Hynix proposing HBF both ratify that KV cache has become a distinct, sizeable storage workload — VAST estimates 100,000 users × 30GB avg × 15-conversation retention ≈ **45 PB** of KV cache [vendor illustrative math].

- **Bull case:** every user, every turn, every agent step generates more KV state; long context, multimodal, and persistent agent memory all multiply it; data gravity favors keeping it (recompute is expensive); tiered offload monetizes DRAM and NAND below HBM. This pulls **capacity** demand down the hierarchy (DRAM, NAND, CXL pools) while **bandwidth** demand keeps HBM scarce.
- **Bear case:** compression and reuse cut *bits per unit of work*. MLA shrinks the cache an order of magnitude; FP8/FP4 halve/quarter it; eviction and TurboQuant claim 5–6× reductions. When **Google published TurboQuant (5–6× KV reduction)**, Micron's stock fell several percent in a session and SK Hynix/Samsung saw similar pressure — the market priced the fear that AI buildouts might need *less* memory per unit of output [the move is established; the causal magnitude is contested].

**Net assessment:** the bull case dominates on current evidence because (a) usage growth (agents, long context, multimodal) is outrunning efficiency gains — a Jevons dynamic (Part E.1); (b) compression mostly shifts *where* KV lives (HBM → DRAM/NAND) rather than eliminating it, which *expands* the addressable memory/storage market downward; and (c) bandwidth (HBM) demand is structurally tight regardless of capacity-side compression because decode is bandwidth-bound. The most durable demand is for **HBM bandwidth** and for the **DRAM/NAND/CXL capacity tiers** that absorb offloaded KV. The genuine risk to the *capacity* thesis is a step-change in compression (a robust 2-bit or MLA-everywhere world) combined with hybrid/SSM adoption that bounds state — worth monitoring as the key falsifier.

### D.2 Semiconductors — GPU vs ASIC, memory-centric design, the prefill/decode split

The prefill/decode dichotomy is becoming a **hardware design axis**. Disaggregation lets operators put compute-dense silicon (FP4-heavy, e.g. B200) on prefill and memory-dense silicon (HBM-heavy, e.g. H200) on decode — and academic work (SPAD, arXiv 2510.08544) proposes *specialized* prefill and decode chips. The KV cache is the reason decode is bandwidth-bound, so memory-centric architectures (more HBM, near-memory/in-memory compute, processing-near-memory over CXL) are favored for the decode/serving future. SRAM-only ASICs (Groq, Cerebras) win latency but struggle with large KV/long context; HBM+tiered designs (NVIDIA, SambaNova) are better matched to KV-heavy agentic workloads. **The KV cache thus tilts silicon design toward memory bandwidth and capacity over raw FLOPs** — exactly the opposite of the training-era FLOPs race.

### D.3 Model training — where KV/architecture choices touch training

- **Architecture decisions are training-time commitments:** GQA/MLA must be designed in (or uptrained — GQA at ~5% of pretraining compute; TransMLA converts GQA→MLA post-hoc). MLA is a training-time bet that pays off in inference economics [established].
- **Long-context training** directly inflates training-time activation/KV memory and is itself memory-bound; techniques like Ring/Striped Attention distribute the attention computation across devices.
- **RL post-training** (RLHF/reasoning RL) runs massive generation (rollout) phases that are inference-bound — KV-cache FP8 quantization during rollouts is being used and shown to track BF16 baselines closely (FP8-RL, arXiv 2601.18150), tying KV efficiency directly into the training loop for reasoning models [research].

### D.4 Inference economics — cost, latency, throughput, margins

KV optimization is the dominant lever on inference unit economics:
- PagedAttention took memory utilization from 20–38% to 96%+, multiplying throughput per GPU [established].
- The same H100 serving the same model supports ~190 concurrent users at 8K context but only ~1–2 at 128K — identical nominal price, radically different provider cost (Data Gravity illustrative) [vendor illustrative].
- Disaggregation: ~1.4× throughput / 20% lower cost (Splitwise); KV-aware routing: ~2× (Baseten/Dynamo).
- HBM capacity sets concurrency: a 192 GB card supports ~20 concurrent users at 70B/32K (~8 GB KV each) [illustrative].

**Margin implication:** providers that master KV reuse, disaggregation, and tiered offload can serve far more users per GPU, which is why cached-token pricing (D.5) is simultaneously a customer discount and a confession about the underlying cost curve. As frontier model quality converges, **inference efficiency becomes a primary axis of margin competition** — and it is largely a KV-cache engineering contest.

### D.5 Agentic workflows — the structural demand driver (emphasis)

Agents are the reason KV cache moved from optimization to strategic layer. Three structural features:

1. **Long, growing, repeated context.** An agent loop re-sends its system prompt, tool definitions, and accumulating action/observation history every step. Manus (Monica AI) reports an **average input-to-output token ratio of ~100:1** — overwhelmingly prefill-dominated, the opposite of a chatbot. In the words of the Manus engineering team (Yichao "Peak" Ji, *Context Engineering for AI Agents*): *"If I had to choose just one metric, I'd argue that the KV-cache hit rate is the single most important metric for a production-stage AI agent. It directly affects both latency and cost."* [practitioner].

2. **The cached-vs-uncached cost cliff.** Manus quantifies it directly: *"with Claude Sonnet, for instance, cached input tokens cost $0.30/MTok, while uncached ones cost $3/MTok—a 10x difference."* [established]. Anthropic's own claim ("Prompt caching with Claude," Dec 2024): customers can *"[reduce] costs by up to 90% and latency by up to 85% for long prompts"* [vendor claim, scoped to "long prompts," "up to"]. DeepSeek's cache hits run ~98% cheaper than misses. Well-implemented caching achieves 80–95% hit rates on static content in production [vendor/practitioner].

3. **Cache fragility under context management.** The natural move of capping context (drop oldest messages) is *fatal* to cache hit rate — dropping message 1 to add message 12 invalidates every cached byte after message 1 (autoregressive prefix invalidation). Even a single-token change (a timestamp in a system prompt) invalidates the cache from that token on. Manus's engineering rules — stable prompt prefix, append-only context, explicit cache breakpoints — are now standard agentic practice [established/practitioner].

Beyond prefix reuse, **shared-knowledge caching** (CacheBlend for RAG/tools, RadixAttention for shared system prompts across agent swarms) and KV-aware routing (Dynamo) extend the savings to non-prefix and cross-request reuse. As agentic workloads go mainstream, they convert KV cache from per-request scratch into a **persistent, reused, cross-session asset** — directly motivating the storage/data thesis in Part E.2. **This is the single strongest structural driver of KV-cache pressure and the strongest bull argument for the memory/storage layer.** (Falsifier: standard LRU eviction is reportedly pathological for agentic workloads — context-aware retention with session-affinity routing is needed, arXiv 2603.21354 — so the savings are real but require non-trivial engineering, not automatic.)

### D.6 Multimodal — images/video reshape the problem

Multimodal massively inflates token counts: a single video frame generates hundreds of visual tokens (576/frame in LLaVA-1.6) vs ~20 for a sentence; video at 30 fps grows the cache ~5.6 GB/minute, OOM-ing a 24 GB GPU in <4 minutes [research]. This makes KV compression *more* essential and *different*: VLM attention patterns differ from text (text-salient early layers → pivot-token-salient later layers), so text-tuned methods underperform. A purpose-built sub-field has emerged — VL-Cache, AKVQ-VL, AirCache, DyCoke, LightVLM — many showing ~10% cache retention matches full-cache accuracy with up to 7× decode speedups and ~90% memory cuts [research claims]. **Net:** multimodal both intensifies KV pressure (more tokens, more memory/storage demand — reinforcing D.1 bull case) and creates a large, distinct compression-research opportunity.

---

## PART E — Outlook & Debates

### E.1 Central tension: demand explosion (Jevons) vs efficiency optimization

- **Explosion (Jevons) case:** cheaper, faster inference → more usage. Agents, long context, multimodal, and persistent memory each multiply KV demand faster than compression shrinks it. Empirically, frontier providers keep adding context length and agentic features, and capex keeps rising (top-CSP capex revised *up* to ~$830B for 2026) — consistent with demand outrunning efficiency. The hot→cold tiering and dedicated KV storage tiers (CMX, HBF, WEKA, VAST) are infrastructure bets that *aggregate* KV demand grows.
- **Optimization case:** MLA (~order-of-magnitude), FP8/FP4 (2–4×), TurboQuant (5–6×), eviction, and especially **architecture shift to hybrids/SSMs** (which bound or eliminate KV) could flatten per-unit demand. The TurboQuant market reaction shows investors take this seriously.

**What would settle it:** the observable test is whether **aggregate HBM/DRAM/NAND consumed by inference** keeps rising despite per-token efficiency gains. On current evidence (HBM sold out to 2028, memory the tightest chokepoint, capex rising, agentic adoption accelerating), **the Jevons dynamic is winning** — efficiency is being reinvested into longer contexts, more agents, and multimodal rather than banked as lower aggregate demand. The decisive falsifier would be simultaneous (a) mass adoption of hybrid/SSM architectures that bound state and (b) a robust 2-bit-everywhere compression standard — neither has happened at frontier scale as of mid-2026.

### E.2 "KV cache is the next Big Data" — for and against

**For:** KV cache is increasingly persistent (GPU→DRAM→SSD→S3), reused across sessions, cross-tier-managed like a data pipeline, and even semantically *mutable* (Stanford Cartridges, UChicago LLMSteer, Georgia Tech PASTA show editing KV steers behavior). A storage stack (WEKA, VAST, DDN, NetApp, Pure), a movement fabric (NIXL, cuObject, CMX), and a commercial layer (Tensormesh/LMCache) are forming around it — the hallmarks of a new platform layer. VAST calls it "Really Big Data"; LMCache argues the name "cache" is now misleading [vendor framing].

**Against — the disanalogies that matter:**
1. **Recomputable.** Unlike Big Data (irreplaceable records), KV cache can always be regenerated from the source tokens + model weights. It is a *cost-optimization cache*, not irreplaceable data — storing it is only worthwhile when recompute cost > storage+retrieval cost.
2. **Model-version-bound.** KV tensors are specific to a model's weights; a model update invalidates the entire stored corpus. Big Data outlives application versions; KV cache does not.
3. **Opaque and ephemeral by SLA.** Anthropic holds KV representations in memory only, deleted after 5 min–1 hr — the opposite of a durable asset.

**Verdict:** "next Big Data" is **overstated as an asset thesis** but **directionally right as a platform/software-layer thesis.** The durable opportunity is the *infrastructure layer* that manages KV movement and reuse (storage + fabric + caching software), not the KV data itself as a mineable asset. The recomputability and model-version-binding are the load-bearing disanalogies an investor should weight heavily against the "data asset" framing.

### E.3 Distributed/edge inference and "CDN for KV cache"

The idea: a geographically distributed KV cache, served from the nearest node like a content-delivery network. Partially real today — global/shared KV stores (Mooncake's global cache, LMCache→S3, Everpure's global KV store, RadixAttention across fleets, Dynamo KV-aware routing across clusters) implement cross-node reuse. A true edge "CDN for KV" (caching at the network edge near users) is **mostly speculative** as of mid-2026: KV is large, model-version-bound, and latency-sensitive to retrieve, and most reuse value is captured intra-datacenter. Expect datacenter- and region-scale KV sharing to mature first; genuine edge-CDN KV is a 5+-year, model-stability-dependent prospect [speculative].

### E.4 Where durable value accrues

- **Hardware / memory (most durable):** the HBM oligopoly (SK Hynix, Samsung, Micron) sits on the tightest chokepoint; NVIDIA's control of GPU + scale-up fabric + KV-movement software (Dynamo/NIXL/CMX) is the most defensible full-stack position. The DRAM/NAND/CXL capacity tiers (Astera, Marvell, Solidigm) are durable secondary beneficiaries *if* the offload thesis holds.
- **Serving software (least durable):** commoditized by open source; value leaks to hardware and managed-service wrappers.
- **Model labs (conditionally durable):** capture value via architecture (MLA) and API cache-discount economics, but advantages are replicable and version-bound.

### E.5 Scenario sketches

**2–3 years (2026–2028):** Transformers + optimized KV remain frontier-dominant. Prefill/decode disaggregation and tiered KV offload become standard; a dedicated KV storage tier (NVMe/flash) is a normal line item; FP8 cache is universal and 4-bit common. Agentic workloads dominate token volume and make prefix/shared caching table stakes. HBM stays the binding constraint (no relief until ~2028); DRAM/NAND/CXL capacity demand rises as offload matures. Hybrid (Mamba-transformer) models gain real production share but do not displace transformers at the frontier. Memory/HBM and NVIDIA remain the durable value capturers; serving-software startups consolidate or get absorbed.

**5+ years (2028+):** Two divergent paths. *KV-persistent world:* hybrids bound state but transformers persist for top-quality reasoning; the KV-data/storage platform matures into a real layer (persistent agent memory, region-scale KV sharing, possibly early edge-CDN KV); memory/storage demand compounds. *Architecture-shift world:* robust hybrids/SSMs + aggressive compression meaningfully flatten per-unit KV demand, partially relieving the memory chokepoint and devaluing KV-specific software — the principal bear scenario for the memory thesis. Current evidence favors the persistent path on a 5-year horizon, but the architecture-shift risk is the single most important variable to monitor.

---

## Caveats & Methodological Notes

- **Vendor vs verified.** "Up to 10×," "up to 90%," 5–6× compression, and throughput multipliers are largely **vendor/marketing claims** scoped to favorable conditions; treat as upper bounds, not expected values. Peer-reviewed numbers (PagedAttention utilization, CacheBlend TTFT, Splitwise/Mooncake throughput) are higher-confidence.
- **Source disagreements surfaced:** HBM market shares differ by analyst (SK Hynix ~50–62%; Samsung ~17–35%; Micron ~11–22%) depending on source/quarter/metric (bit-share vs revenue). MLA-vs-GQA adoption is genuinely contested (DeepSeek/efficiency case vs Western labs' GQA inertia). Disaggregation's benefit is workload-dependent and can be negative. Marvell's CXL compression ratio is cited at 2–3.6× by the vendor but 1.8–2× in field reporting. CSP capex figures were revised upward within Q1–Q2 2026.
- **Fast-moving area.** Model names, prices, and funding reflect mid-2026 snapshots and will drift. Some cited sources are secondary/commercial blogs; primary papers (arXiv) and engineering docs (vLLM, NVIDIA, Mooncake, LMCache, Anthropic, Manus) were prioritized where available.
- **No investment advice.** This is structural-positioning and durability-of-value analysis, not buy/sell/hold guidance or price targets.

---

### Reference List (selected)

- Liu, N. F. et al., "Lost in the Middle: How Language Models Use Long Contexts," TACL 2024, arXiv 2307.03172
- Shazeer, N., "Fast Transformer Decoding: One Write-Head Is All You Need," 2019, arXiv 1911.02150 (MQA)
- Ainslie, J. et al. (Google), "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints," EMNLP 2023, arXiv 2305.13245
- DeepSeek-V2/V3 technical reports (MLA); "TransMLA: Multi-head Latent Attention Is All You Need," arXiv 2502.07864
- Liu, Z. et al., "KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache," ICML 2024; Hooper et al., "KVQuant," NeurIPS 2024 (Berkeley)
- Xiao, G. et al., "Efficient Streaming Language Models with Attention Sinks" (StreamingLLM); Zhang, Z. et al., "H2O"; Li, Y. et al., "SnapKV"; "Protection Is (Nearly) All You Need," arXiv 2605.18053
- Kwon, W. et al., "Efficient Memory Management for LLM Serving with PagedAttention" (vLLM), SOSP 2023; Zheng, L. et al., SGLang/RadixAttention
- Yao, J. et al., "CacheBlend: Fast LLM Serving for RAG with Cached Knowledge Fusion," EuroSys 2025, arXiv 2405.16444; "CacheClip," arXiv 2510.10129
- Patel, P. et al., "Splitwise," ISCA 2024; Zhong, Y. et al., "DistServe," 2024; SPAD, arXiv 2510.08544
- Qin, R. et al., "Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving," FAST 2025, arXiv 2407.00079
- Gu, A. & Dao, T., "Mamba," arXiv 2312.00752; "Mamba-3," arXiv 2603.15569; Dao & Gu, "Transformers are SSMs" (SSD), 2024
- NVIDIA Dynamo technical blogs (NIXL, KV offload, KV-aware routing); LMCache blog (CacheBlend; "Stop Calling It KV Cache"); Ji, Y. ("Peak"), "Context Engineering for AI Agents: Lessons from Building Manus" (manus.im)
- Anthropic, "Prompt caching with Claude" (Dec 2024); Astera Labs and Marvell CXL technical blogs; SK Hynix H³ (HBF) IEEE paper; VAST Data "context memory / Really Big Data"; FP8-RL, arXiv 2601.18150; "CXL-Enabled KV-Cache Management Beyond GPU Limits," arXiv 2511.00321
- VLM KV: VL-Cache (arXiv 2410.23317), AKVQ-VL (2501.15021), AirCache (2503.23956), DyCoke (CVPR 2025)
- Market/industry: TrendForce CSP capex releases (Feb & May 2026); Forbes (Groq/Cerebras/SambaNova, Oct 2025); Tensormesh funding (TechCrunch, Business Wire, May 2026); PatSnap/Counterpoint HBM share data