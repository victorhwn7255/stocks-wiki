# AI Semiconductor Endgame Projection 2026 (II)

*English translation. Source: Chinese-language analyst note on AI memory/storage cyclicality.*

---

As semiconductor structural evolution moves toward the AI-inference main line, memory and storage have become the largest bottleneck. The market's biggest doubts about memory and storage are:

- Will HBM / DRAM / SSD break free from traditional cyclicality?
- Will the GPU-architecture evolution path that depends on exponential HBM growth stop? When?
- How large is the impact of CXMT's (ChangXin) capacity expansion? Will it drag the market back into the cyclical swamp?

This piece attempts to build a framework to work through these questions.

---

## The framework: how to escape traditional cyclicality

Everything is cyclical, and memory's cyclicality is especially strong. The biggest source is that the capacity-expansion cycle is too long, so it cannot ramp quickly and ends up mismatched against periods of demand shortage.

Several possible ways to escape traditional cyclicality:

1. **Customization** — the product is not interchangeable, capacity cannot be freely re-allocated, and long-term contracts are required.
2. **Structural exponential demand growth** — the demand curve itself is very steep, and supply can never catch up.
3. **Fast technology iteration** — each generation rapidly obsoletes the previous one.

Satisfy any one condition, and you partly escape the traditional cycle; satisfy two or three, and you escape most of it.

By this framework, **HBM satisfies about two-and-a-half of the three.**

### 1. Customization / long contracts (weak — counts as half)

HBM does have a customization and NVIDIA-codesign component, but it isn't very strong. The truly custom part is only in the packaging and the base die. The dozen-plus DRAM dies stacked on top remain fully JEDEC-standardized.

For example, when Samsung's HBM3E failed NVIDIA's qualification and its share fell from roughly 60% all the way to 20%, it did not scrap that capacity. It simply redirected it to Google's TPU and to AMD. Physically, the HBM3E destined for NVIDIA and the HBM3E destined for AMD are the same thing. So capacity is still partly freely transferable.

Customization increases somewhat after HBM4 — including integrating custom logic and/or cache into the base die. A more complex approach puts the HBM4E memory controller and a custom die-to-die interface directly into the logic base die. SemiAnalysis notes that OpenAI, NVIDIA, and AMD are each doing custom-HBM work, but this refers to base-die customization; the DRAM layers above remain standard.

Because of this partial customization, HBM mainly requires collaboration on packaging, which forces customers into long-term contracts — but capacity can indeed be transferred. So HBM barely counts as half a condition here.

### 2. Structural exponential demand growth (satisfied)

The most direct driver is the hardware-upgrade demand for NVIDIA token-factory token throughput, which drives extremely fast generational upgrades in HBM bandwidth and exponential growth in HBM size demand.

This is essentially the conclusion of Part I:

> **token throughput = HBM size × HBM bandwidth, doubling every generation.**

HBM size per GPU grows roughly 40%+ per year. The steepness of this demand curve is very hard for the DRAM supply side — 14% wafer growth × 9% density improvement — to keep up with.

On the hardware side, the attention phase's KV cache requires extremely high bandwidth and extremely high memory size, which gives HBM its unique position. Even if HBM prices rise 3–5×, the marginal token-throughput gain from spending on HBM is still far more economical than spending elsewhere.

The other memory paths — SRAM, HBF, CXL, PIM — currently cannot compete head-on with HBM on its main battleground (KV cache / attention). For at least the next five years, and probably longer, a substitute path is unlikely to emerge.

### 3. Fast technology iteration (satisfied)

The DDR3 era lasted 15 years and we are still only at DDR5. HBM's generational cadence is basically one generation every two years — far, far faster than traditional DDR — and has recently been accelerating. HBM size × HBM bandwidth doubling every generation fits this pattern exactly.

With a new HBM generation every two years, NVIDIA GPU speed climbs roughly exponentially: 2 TB/s → 3.5 TB/s → 4.8 TB/s → 8 TB/s → 22 TB/s. HBM speed is perfectly linearly proportional to inference token throughput. The marginal cost of using a prior-generation HBM becomes uneconomical, so everyone is incentivized to use the newest product — more expensive, but the return (token throughput) is greater.

The logic of the token-factory era: the more you upgrade (HBM bandwidth), the more you earn.

This speed gap creates a situation similar to CPUs: old product depreciates fast, so the value of hoarding falls. HBM3, for instance, depreciates very quickly; today's mainstream products basically no longer use it.

So the rational choice for HBM makers shifts from competing on current capacity to grab market share (quantity competition) to competing on stability and HBM speed — competing for next-generation qualification share on NVIDIA's platform (quality competition). This avoids the prisoner's-dilemma of the traditional down-cycle, where nobody is willing to cut production and lose share.

---

## Can HBM escape traditional cyclicality?

With two-and-a-half of three conditions met versus traditional DRAM — can HBM escape cyclicality?

The mainstream narrative on the source of memory cyclicality is: DRAM has commodity properties (undifferentiated → price wars → inventory can be hoarded), so it is cyclical. But the commodity property itself does not *create* the cycle — it is only an **amplitude amplifier.**

In DRAM specifically, a prisoner's-dilemma has occurred before: in a down-cycle Samsung once expanded to grab share, and whoever cut first lost, so nobody dared cut — and everyone took brutal losses.

The main *structural* source of cyclicality is that the supply cycle is too long and easily falls out of phase with the demand cycle. Building a fab takes 3 years and tens of billions of dollars; once decided it is irreversible. Demand growth is unstable: each new paradigm (cloud services, mobile internet/smartphones, pandemic online demand) brings an explosive surge, then growth slows after two years, supply exceeds demand, prices drop too hard, and it turns into a money-losing cycle.

Everything is cyclical; HBM cannot avoid this either. But as long as token demand keeps growing exponentially, structural exponential growth weakens the cycle, because demand is more predictable, and once prices fall, customers want larger HBM size (to raise token throughput). Combined with HBM's slight customization forcing long contracts, this converts cyclicality into **growth-cyclicality** — and this round of cycle will be unusually long.

- **Cyclicality:** earn a lot in the up-cycle, lose a lot in the down-cycle.
- **Growth-cyclicality:** earn a lot in the up-cycle, earn a little in the down-cycle.

### A fourth advantage on top of the three conditions

**4. Because DRAM density scaling is slowing, and HBM upgrades increase the DRAM stacking multiplier, the difficulty of expanding supply keeps rising.**

Around 2000, per-wafer DRAM bit density grew ~45% per year — meaning even with no wafer expansion, supply-side DRAM bits could still grow 45% annually. Ten years ago this fell to ~20%. Now, DRAM bit density grows only ~9% per year. Previously DRAM could get 20–30% annual bit growth without even building new cleanrooms; now expansion relies more on wafer-count growth — i.e., new buildings and cleanrooms.

Another HBM rapid-expansion difficulty: HBM3E needs roughly 3× the DRAM wafers, and HBM4 — due to higher stacking density — needs roughly 4× the DRAM wafers. HBM bits are getting progressively harder to manufacture relative to DRAM bits; each DRAM wafer yields fewer and fewer HBM bits. It is effectively deflationary on the bit-supply side.

---

## Will the HBM-dependent GPU architecture path ever stop?

Will HBM revert from growth-cyclicality back to traditional cyclicality? The most important factor is structural exponential growth. So: in the AI-inference era, will the GPU-architecture evolution path that depends on exponential HBM growth stop, and when?

In `token throughput = HBM size × HBM bandwidth`, the HBM-size growth in this first-principles relation is driven precisely by KV-cache growth. The properties of KV cache and of attention fit HBM extremely well — they even put HBM ahead of other technology paths, maximizing utilization in the KV-cache and attention phases.

In other words, **if KV cache structurally ceased to exist, the HBM-size exponential-growth logic would be challenged.** So the essence of the question is: will the attention mechanism (Transformer) and its derived KV-cache mechanism disappear? After the tide recedes, will they be replaced?

From historical patterns: in every AI model-architecture revolution, what truly survives are the primitive operations that have some mathematical universality.

Example: FFN (the feed-forward / MLP layers) was a product of the 2012 deep-learning era, but it survived all the way into today's LLMs and still occupies a large share of parameters. Why did it survive? Because it is a form of the universal approximation theorem — any sufficiently wide MLP can approximate any continuous function.

Attention is most likely another such retained primitive, because it solves an equally fundamental problem: dynamic routing between any two positions in a sequence, letting any two positions form an on-demand connection. Once this capability is validated as effective, it is very hard to discard.

So even as future architectures evolve from pure Transformer toward hybrid architectures, or toward world models, the attention layer will still exist, KV cache (or its latent-compression equivalent) will still be needed, and HBM will still be one of the cores of inference. The HBM-dependent GPU / KV-cache architecture path will not stop.

---

## What about DRAM? Can it escape traditional cyclicality?

There is some market consensus that HBM escapes cyclicality, but for DRAM there is basically no consensus today.

Back to the framework. Of the three escape conditions, DRAM has no customization, so it depends on iteration speed and — most critically — on whether there is structural exponential growth. The answer is yes.

Within the AI token-factory concept, the structural exponential growth is mainly HBM. But things changed after late 2025: as agentic CPUs began to release their potential, the DRAM demand attached to CPUs is becoming DRAM's new source of structural exponential growth.

### The growth logic has two layers

**Layer 1: rapid growth of the CPU-server TAM. Layer 2: rapid growth of the DRAM provisioned per CPU core, driven by agentic flow.**

The four reasons for rapid server-CPU TAM growth (detailed in the April CPU note), briefly:

1. The CPU:GPU ratio in AI-accelerator clusters shifts from the traditional 1:4 toward 1:2, possibly toward 1:1.
2. In agentic flow, the latency share handled by CPUs is high — 50–90% becomes a major bottleneck — requiring synchronized expansion.
3. AI coding massively boosts software-engineer efficiency; code volume grows by orders of magnitude, software API calls grow exponentially, directly translating into exponential growth in this slice of CPU-hours.
4. Sandboxing for data security and isolation (e.g., an Analytical Agent must replicate large databases and user context for each task) causes severe waste of memory (DRAM) and CPU cores — and this waste problem won't be solved for five years or more. CPU-hours are also technically very hard to deflate via optimization.

This is why: a couple of quarters ago AMD's results said CPU TAM reaches $60B by 2030; two months ago AMD/ARM doubled the 2030 forecast to $120B; a month ago NVIDIA again doubled the 2030 forecast to $200B. And last week Bernstein again raised the 2030 CPU TAM guide to $223B. In my view, a 2031 CPU TAM upward revision to $400B is not in much doubt — the only suspense is when the giants will announce it.

Now Layer 2: why does the DRAM provisioned per CPU core grow rapidly in the agentic era?

1. **Agents are stateful, long-resident processes, not stateless request-response.** Traditional web/SaaS is stateless: a request comes in, memory is allocated, and reclaimed immediately after. An agent task can run from a minute to an hour, and throughout that time its message history, system prompt, working memory, long-term memory, and tool-result buffers all reside in DRAM. Like CPU-hours, each task's memory footprint is technically hard to compress, given stateful and sandbox-isolation requirements.
2. **Context windows are growing exponentially; each session's working set swells. Concurrency × per-session memory footprint is a multiplicative amplifier.** Context windows go 32K → 256K → 1M; reasoning / test-time-compute sequence lengths explode and will keep growing. The resident messages per active session grow linearly with context length.

Now multiply the two layers:

- **Layer 1**, server-CPU TAM toward 2030–2031: roughly 5–7× ($60B → $120B → $200B → $223B; I think it reaches $400B).
- **Layer 2**, DRAM per CPU: roughly 3–4× (4–8 GB → 16–32 GB/core), though much of this is likely a one-time dividend.

Two independent variables multiplied → server-side DRAM demand grows by orders of magnitude.

In 2030, even on a conservative $300B CPU TAM, $50/CPU-core, and a conservative 16 GB/core in the agent era, the new increment is at least 96 EB — whereas this year's total DRAM output is only 47 EB, and next year barely 60 EB. A staggering increment.

Although this agentic-CPU-driven exponential DRAM growth is largely a one-time dividend at Layer 2, it will last for a very long time, because the shortfall gap is simply too large.

### Back to the framework, for DRAM

- **Condition 1 (customization):** basically negligible.
- **Condition 2 (structural exponential, hard-to-reverse demand source):** holds. Commodity DRAM now also has partial qualification to escape traditional cyclicality — not as completely as HBM (two-and-a-half), but a real change.
- **Condition 3 (iteration speed):** DRAM's cadence is also different from before.

Previously DRAM iteration speed depended heavily on consumer electronics, and DDR progress mattered little for performance. But for the foreseeable future, carbon-based consumption (traditional consumer DRAM) will be far smaller than silicon-based consumption (CPU servers) in DRAM usage.

Previously the marginal utility of DRAM speed upgrades was low; now, because CPU servers' memory demand has grown — and edge-AI demand for DDR speed has grown too (e.g., Apple raising LPDDR speed to run local large models) — the marginal utility of speed upgrades is much higher. So the iteration-demand for DDR6 and LPDDR6 has risen enormously versus before; the charts show LPDDR6/DDR6 iteration time shortening and the speed slope turning back up.

Previously, when a new DDR/LPDDR generation came out, everyone reacted coolly and waited for prices to fall before adopting. Now, when LPDDR6 arrives, everyone is scrambling to adopt as early as possible, because the performance gain from higher speed is within reach.

### The HBM "bit tax" on DDR

DDR supply is also taxed by HBM. HBM's annual expansion is so fast that every year a batch of wafers that could have made commodity DDR is pulled into HBM — and HBM's conversion ratio is extremely poor (HBM3E needs ~3 DDR wafers' worth of capacity for the same bits; HBM4 needs ~4). So each year roughly 3–5% of DDR bit growth is eaten directly by this HBM bit tax.

So although DRAM bit volume can grow ~24% per year (14% from wafer growth, 9% from per-wafer density), after the HBM bit tax, traditional non-HBM commodity DDR grows only ~20% per year (~10% wafer growth × ~9% node density).

---

## How large is CXMT's (ChangXin) expansion impact? Could reckless expansion drag the market back into the cyclical swamp?

CXMT's expansion pace has been fast. In 2025 it was ~200k wafers/month; in 2026 the Beijing fab and added lines bring it to 320k–350k. The Shanghai fab Phase 1 and Phase 2 under construction add ~100k/month each by 2027 and 2028 respectively — i.e., ~420k/month in 2027 and ~500k/month in 2028.

But note: CXMT's DRAM bit density is only about half of the Big Three's. So 500k wafers/month yields only half the DRAM bit volume of the others. Computing wafers-per-month on an equivalent-half basis:

After applying this discount, CXMT's shock to the whole DRAM industry is much smaller. From end-2025 to end-2028, CXMT's impact on DRAM-bit capacity CAGR is only ~1.5%; industry-wide DRAM capacity CAGR rises from ~12.7% to ~14.2%.

**DRAM monthly capacity (kwspm), 2025E → 2028E, CAGR**

| Supplier | 2025E | 2028E | CAGR |
|---|---|---|---|
| Samsung | 685K | 920K | 10.3% |
| SK Hynix | 519K | 725K | 11.8% |
| Micron | 340K | 560K | 18.1% |
| Non-China other | 150K | 218K | 13.3% |
| China (density halved) | 117K | 274K | 32.8% |
| **Total incl. China** | **1,811K** | **2,697K** | **14.2%** |
| **Total excl. China** | **1,694K** | **2,423K** | **12.7%** |

Even if CXMT sustains its expansion pace, its impact on industry-wide equivalent annual DRAM-bit-volume capacity CAGR by 2030 is under ~3% — from a 20% CAGR to a 23% CAGR. That's all.

Additionally, CXMT is constrained by lithography. DDR6 requires higher data rates (starting at 14,400 MT/s) and higher density; the Big Three will likely make DDR6 on 1c or more advanced nodes (~sub-12nm), already fully using EUV. CXMT may be rate-limited on DDR6, with only half the density.

---

## Even as a growth-cycle, why will this DRAM super-cycle last very long — at least five years with no end in sight?

**First reason: the structural exponential DRAM demand from the massive growth in CPU-server demand.** Combining this with a steady ~20% supply-side bit-volume CAGR shows clearly why the DRAM gap widens in the coming years:

Non-HBM traditional DRAM supply grows ~20% per year. On the demand side, at a 2026 $60B CPU TAM, 8 GB/core average, $30–35/core, demand is ~16 EB. By 2030, at $400B CPU TAM, 16 GB/core average, $80/core (CPU price more than doubling), demand is ~80 EB — a demand CAGR of roughly 50%, far above current estimates.

Unlike HBM, which is tied directly to token throughput (and thus directly to GPU earning efficiency), insufficient DRAM mainly affects speed for agent flow. For example, 8 GB/core vs 16 GB/core might slow some workloads ~30%, and some low-value tasks can tolerate waiting. The structural-exponential motivation is strong, but demand is not as rigid as GPU demand.

SemiAnalysis says this year's DRAM gap is a single-digit percentage; next year it exceeds 10%. From the structural growth driven by surging agent-CPU counts, this gap keeps widening every year, with no chance of narrowing before 2030.

**Second reason: when prices rise, the demand killed off isn't truly gone — only delayed. The demand reservoirs are vast.**

A "reservoir" is latent demand that gets released the moment memory prices fall. Their existence means that even if supply temporarily catches up, prices struggle to collapse, because new demand keeps pouring out of the reservoirs to absorb it:

- **Memory-for-compute/speed is a reservoir.** Lots of demand that would normally use extra memory to optimize speed/compute is suppressed when memory is too expensive, and released once memory cheapens. For example, NVIDIA's CPX prefill accelerator was originally designed to use extra low-cost GDDR7 for a dedicated prefill accelerator — but LPDDR/GDDR became so expensive (more expensive than pre-hike HBM) that the ROI no longer worked. When ordinary memory cheapens, CPX-like optimizations will return.
- **Low-value tasks are a reservoir.** When memory price keeps token prices high, high-value tasks are prioritized and low-value ones deferred; once memory cheapens, the deferred demand returns.
- **Edge AI is a reservoir.** AI-PC memory config may climb from 24 GB to 128 GB. Apple has already required its latest full-strength on-device AI to go from 8 GB to 12 GB.
- General consumer electronics, Agent PCs, and low-end phones — demand reduced by memory price hikes — are all reservoirs.

So many reservoirs stacked together form an extremely thick demand buffer. That's why DDR's structural growth this round has more staying power than the market imagines.

**Third reason DRAM prices struggle to fall much: HBM and DRAM capacity are mutually convertible, so the whole DRAM complex re-rates together.**

In the up-cycle, DRAM margins far exceed HBM's — so much that HBM price hikes are driven by DRAM. The newly signed HBM4 price this year is current DRAM price × 4 — i.e., the price corresponding to the normal stacking multiplier for HBM4. Once DRAM cheapens and gross margins decline, because of HBM's long-contract transparency, HBM margins are protected — so HBM indirectly pulls away more DRAM capacity. HBM price drops also give GPU makers more incentive to upgrade HBM size as much as possible, which indirectly defends the DRAM price floor.

Structural exponential demand is present; density scaling is slowing and expansion difficulty rising; makers' expansion plans are cautious; CXMT's impact over these years is limited; and the demand reservoirs are huge. These four reasons mean DRAM will struggle to enter a cyclical trough for at least the next five years, probably longer.

---

## Can NAND SSD escape traditional cyclicality?

NAND's structural growth driver is not as strong as DDR's. This year's shortage is mainly because the major players maintained good production discipline and did not expand aggressively; annual capacity additions come mainly from technical improvement (more NAND stacking layers).

**First structural growth comes from AI**, mainly from KV-cache offloading — offloading the warm/cold KV cache that overflows HBM onto NAND SSD. Strangely, this KV-cache offloading growth hasn't even happened at scale yet, and SSD is already shorter than DRAM, with bigger price increases. When Rubin CMX ramps next year, plus large-scale KV-cache offloading, SSD shortage will also grow on this structural driver.

**Second**, the AI-video structural increment mentioned in last year's annual summary is already going mainstream this year. Seedance's volume is growing 10× to 40× per year. It's still stuck in the GPU-shortage / insufficient-compute stage, with demand suppressed by compute. But once the GPU-shortage stage passes, AI video's structural demand for NAND storage will grow for quite a long time.

**Third**, structural growth also comes from the exponential growth in sandbox usage driven by agent flow. Sandboxing for data security/isolation (e.g., an Analytical Agent replicating large databases and user context per task) wastes memory (DRAM) and CPU cores — and likewise generates large SSD waste (demand).

**Fourth**, perhaps active after 2030: structural growth from the HBF path, which needs SSD. It is highly anticipated in many bank analyses, but this technology path is still somewhat distant. Its main role can only be storing large-model weights — written once, then read-only — and it must be packaged together with GPU/HBM (48 TBps / 96 TBps); otherwise PCIe 7/8 speeds are too slow to use at all. Promising for the future; Part III will analyze this in more detail.

In short, NAND SSD's structural growth isn't as strong as HBM's, but its advantage is being cheap: by 2027, $0.8/GB, only 1/40th of DRAM at the time. So it's the all-purpose layer of the multi-tier cache, with extremely broad structural-growth sources.

That is, there's no scenario where DRAM/HBM alone boom and rise in price while SSD doesn't, because if that happened, people would find ways to use SSD to carry part of DRAM/HBM's function at lower cost. HBM, DRAM, and NAND are not three independent stories, but the same AI memory hierarchy growing structurally at different temperature layers.

Structural exponential demand is present — has NAND SSD escaped the cycle? That depends on NAND makers' production discipline. The only one that might break discipline is YMTC (ChangCun). This is a prisoner's-dilemma: if one player expands recklessly, the difficulty of expanding NAND capacity is much lower than DRAM's. But at minimum, this round of NAND is also a super-cycle; the several structural exponential demand drivers should comfortably push any down-cycle out past 2030.
