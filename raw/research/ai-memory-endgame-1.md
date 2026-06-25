# AI Semiconductor Endgame Projection 2026 (I)

## When the new token-economics paradigm shifts from GPU compute to HBM

*English translation. Source: Chinese-language analyst note on HBM demand and inference architecture.*

---

This piece starts from the essence of the GPU-architecture evolution path to explain a question the market has long worried about:

- Why must the HBM-memory demand per GPU grow exponentially? Why won't exponential HBM demand stall?

And it derives the first principle of token economics under the current architecture: **token throughput = HBM size × HBM bandwidth.**

It also discusses why the GPU's ceiling is determined by HBM's two development dimensions.

HBM cyclicality has always been highly contested. Optimists argue AI-driven demand is far larger than before, but the market mainstream still holds that previous up-cycles also had 20%+ annual demand growth — so what's different this time? In this view, AI doesn't change the fact that HBM, like traditional DRAM, has commodity properties; once peak-demand expansion meets a demand downturn, it repeats the old pattern.

We can dismantle and project this question from the perspective of compute-chip architecture, from first principles: why it really is different this time.

---

## History: the CPU-compute era

For a long time we lived in an era where the CPU dominated compute. The CPU's top-level KPI was **performance** — run faster — so each CPU generation used various methods to raise benchmark scores: first frequency, later architectural evolution (superscalar, etc.).

Why didn't DDR need a fast pace of technical progress in this period? (DDR3 to DDR5 took fully 15 years.)

Because DDR's role in this era was purely auxiliary, and a very weak auxiliary at that. By industry experience, even doubling DDR speed typically raised CPU performance by less than ~20%.

Why did raising DDR bandwidth/speed matter so little? Two reasons:

1. **The CPU designed many architectures to hide DDR latency** — superscalar, wider issue width, massive ROBs and register renaming to raise parallelism and hide latency, plus L1 and L2 caches — all weakening the demand for DDR bandwidth/speed.
2. **CPU workloads don't demand much DDR bandwidth.** Most everyday loads (opening a webpage) leave DDR bandwidth massively in surplus — even cloud loads.

That is, in the CPU era DDR bandwidth/speed barely mattered. DDR4 and DDR5 made little difference outside a few games; even JEDEC standards advanced slowly.

Also, the portion of most apps that must stay resident in DDR isn't large — schedule it from disk into DDR when needed. App size didn't grow that fast, so DDR capacity demand also grew slowly. Over the last decade, average DDR per PC went from ~7–8 GB to ~23 GB — only ~3× in ten years.

This slow upgrade directly affected revenue. Capacity (size) pricing is the main way to make money; speed improvements are only a technical upgrade that raises the unit price per unit of size. Demand for both upgrades was weak; demand grew mainly with the number of PCs/phones.

So along both axes — bandwidth/speed and capacity — DRAM was always an "icing on the cake" appendage to the chip industry. The marginal utility of DDR upgrades was low, with almost no direct link to the CPU era's top KPI.

---

## The genAI era: the paradigm shift fundamentally changes the top-level KPI

When GPUs reached the AI-inference era, the top KPI is no longer raw compute (TOPS/FLOPS) but **the cost of tokens** — specifically the overall token throughput per unit cost / per unit power.

Second is token-throughput *speed*, because in the agent era many tasks became serial, and token-throughput speed became a key bottleneck for user experience.

This is why Jensen invented the AI-factory concept: output the most tokens at the lowest cost, while maximizing token-throughput speed as much as possible.

- In the AI-training era, Jensen's economics was **TCO** (total cost of ownership): the more GPUs you buy, the more you save.
- In the inference era, Jensen's token economics is: NVIDIA GPUs are the cheapest-per-token GPUs in the world — **the more you buy, the more you earn** (inference gross margins are substantial).

The top KPI becomes a **Pareto frontier** curve, optimizing along two dimensions: raising token throughput and raising token speed (see Figure 1). NVIDIA's token-factory generational progress is essentially pushing the entire Pareto frontier toward the upper-right — the single most important KPI of the AI-inference era.

---

## The core logic chain: from exponential token throughput to the HBM size × HBM bandwidth ceiling

Now the most important logic chain of this piece: starting from the essence of exponential token-throughput growth, derive that the ceiling bottleneck lies in the exponential growth of HBM size and HBM bandwidth.

In the single-GPU, single-thread, batch-size = 1 inference era, token throughput had only one dimension — HBM bandwidth/speed. Higher bandwidth → higher throughput.

But in the NVL72 era, inference is no longer single-GPU; it's a system-level token factory of 72 GPUs + 36 CPUs, maxing out HBM bandwidth and compute to extract the utmost token throughput.

Token-throughput growth depends on two things: the number of simultaneously batched requests × the average token speed per user request. That is:

> **batch size × per-user token speed**

Take Rubin NVL72: at an average token speed of 100 token/s, batching 1,920 requests simultaneously yields a throughput of 192,000 token/s. A Rubin NVL72 is roughly 120 kW (0.12 MW), giving 1.6M token/s per MW. (See Figure 1.)

So we must raise both parameters — batch size and average per-user token speed; their product is our top KPI, token throughput.

### Parameter 1: batch-size growth — bottleneck is HBM size

Every request in the batch carries its own KV cache, which must live in HBM, roughly several GB to tens of GB each. Because the hot KV cache needs constant high-frequency, high-speed reads, it must sit in HBM. For example, if a model has 80 layers, then each token-generation step requires 80 reads of the KV cache in HBM.

As batch size grows, hot KV cache grows linearly. And because all requests' hot KV caches in the batch must sit in HBM, **HBM size must grow linearly with batch size.**

Like an airport shuttle bus: the gate gets passengers to the plane as fast as possible. If HBM size is small, the bus is small, so it must make extra trips.

Conclusion: batch size is bottlenecked by HBM size growth.

### Parameter 2: average per-user token speed — bottleneck is HBM bandwidth

The speed of an LLM's decode phase is bottlenecked by HBM bandwidth, because generating each token requires reading the activated weights and KV cache many times.

The LPU's emergence moved the activated-weights portion onto SRAM when the batch isn't very large — but generating each token still requires many KV-cache reads from HBM. The higher the HBM bandwidth, the faster each token is generated — essentially a linear relationship.

Like the shuttle bus again: HBM bandwidth is how wide the bus door is — the wider the door, the faster passengers board.

The GPU's other configurations all adapt to batch growth and balance token-compute speed against HBM growth — even using surplus compute to recover some bandwidth (e.g., bandwidth-compression techniques).

### The shuttle-bus analogy, summarized

- **Shuttle cabin size = HBM size (capacity):** how many passengers (how many requests' KV cache) fit at once. Bigger cabin → larger batch. Too small, and 100 people take two trips, capping overall throughput.
- **Shuttle door width = HBM bandwidth:** how fast passengers board/alight. Wider door → everyone piles in fast (fast decode/token generation). Narrow door → even a 200-seat cabin loads single-file, wasting all the time at the doors.
- **Passenger throughput = cabin size × boarding speed (door width).**

---

## The first principle of token economics

We have logically derived the hardware-demand first principle of token economics:

> **Token throughput = HBM size × HBM bandwidth**

The top KPI of the AI-inference era is in fact highly dependent on progress in HBM's two dimensions.

To sustain 2× token-throughput growth per generation actually means: each generation, per single GPU, the *product* of HBM size × HBM bandwidth must grow 2×. This is also the first time in history that HBM *size* can affect the top KPI, token throughput.

To validate the theory, plot NVIDIA's token throughput from A100 to Rubin Ultra against HBM size × HBM bandwidth on the same chart (see Figure 2). The two curves track astonishingly closely on a log axis.

HBM size × HBM bandwidth actually grows even faster than token throughput, since HBM determines the *ceiling*, and ceiling utilization is hard to push to 100%. Even if HBM size × HBM bandwidth grows 1,000×, it's hard for the rest of compute and architecture to fully extract that 1,000× ceiling potential.

This curve isn't coincidence — it's the inevitable solution to system optimization. throughput = batch × bandwidth is the unavoidable first principle of token-factory economics.

### What about software? Won't optimization lower bandwidth/HBM demand?

This is an independent dimension from hardware. It's like asking: if the software on a CPU is optimized to run faster, does the CPU not need to develop for ten years (since software runs faster anyway)? If so, would the CPU vendor still make money? For a CPU to survive, there's only one path: on standard benchmarks (ignoring software optimization), each CPU generation must score higher, or it won't sell.

GPUs are the same: how software is optimized and whether one's own token-throughput KPI must improve substantially every year are two different matters.

As long as token demand keeps growing, the pursuit of token throughput will never stop — so the pursuit of HBM size × HBM bandwidth will never stop. If HBM size and bandwidth develop too slowly, Jensen will personally go to the Big Three and pressure them to upgrade, because this is the ceiling of his GPU. If the ceiling is nailed shut with no progress, can his GPU still sell?

Of course, NVIDIA must rack its brains to extract the part beyond the HBM ceiling from a heterogeneous-computing architecture angle — e.g., the LPU is a fine attempt, improving the Pareto frontier from another angle (the right-hand, high-token-speed part).

---

## Conclusion

HBM has bid farewell to the old era of drifting with the tide. On this one-way street paved by exponential demand, it has walked, in an almost fated way, to the center of the industry's epic main stage.

As the inference-paradigm first principle evolves to this point, as long as Jensen still sells GPUs, HBM must double — and must double generation after generation. This is the **supply side's endogenous pressure** — unrelated to AI demand, unrelated to the macro cycle, unrelated to hyperscalers' mood.

The only remaining question: when demand is physically locked into exponential growth, will the three supply-side players, as they have for the past thirty years, drag themselves back into the cyclical swamp once again?
