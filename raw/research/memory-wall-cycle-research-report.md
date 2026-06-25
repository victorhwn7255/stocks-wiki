# The Memory Wall: Why Memory Is AI's Binding Bottleneck, and Whether the Cycle Is Structurally Different

## TL;DR

- **Memory bandwidth — not compute — is the binding wall for AI**, and the gap is structural: server compute scales ~3.0x every two years while DRAM bandwidth scales only ~1.6x (Gholami et al.). At the inference/decode stage that now dominates AI, accelerators sit idle waiting on data. This mechanism, plus a three-firm oligopoly (~90%+ of DRAM, effectively 100% of HBM) and hard wafer cannibalization (HBM uses ~3x the wafer area per bit of DDR5, rising toward 4x for HBM4), has produced the most extreme memory upcycle on record.
- **The cycle is genuinely different in *amplitude* and *demand source* — but not yet proven *non-cyclical*.** Demand is now machine/token-driven (compounding) rather than bounded human-device demand; long-term contracts ("sold out" HBM for 2026) and stated supply discipline dampen volatility. But every prior "structural" claim (1995, 2010, 2017–18) ended in a supply-driven glut, and a real, coordinated 2027–28 fab wave (SK Hynix M15X, Micron Idaho, Samsung P5) is the classic glut setup. A *partial* re-rating is justified; "permanent TSMC-ification" is not yet proven.
- **The single clearest falsifier:** **HBM** (not merely commodity DRAM) contract prices decline QoQ **AND** maker book-to-bill falls below 1.0 for two consecutive quarters, while supplier inventories rebuild above ~8 weeks (from today's 2–4). A commodity-only roll is ambiguous; an HBM-tier roll means oligopoly pricing power has broken and the cycle is reverting to type.

---

## Key Findings

1. **The wall is real and widening.** LLM decode reads the entire weight set per token; at batch size 1, arithmetic intensity is ~1–2 FLOPs/byte — 200–600x below the compute-bound knee. An H100's 989 FP16 TFLOPS are throttled to ~24 tokens/s for a 70B FP16 model by its 3.35 TB/s of HBM3. Adding FLOPS does nothing.
2. **Efficiency techniques mostly don't relieve bandwidth** (quantization is the partial exception), and a "memory-Parkinson" dynamic re-saturates any headroom they create.
3. **HBM content per GPU rose ~3.6x (80→288GB, H100→B300) and ~18x across P100→B300, while FP compute rose ~500x** — the quantitative root of bandwidth starvation. A GB200 NVL72 rack holds ~13.4–13.5 TB of HBM3e.
4. **Memory has inverted from a server cost minority to ~65–70% of server BOM** in under two years; on a B300, HBM is >50% of the GPU bill of materials.
5. **Micron's FQ3 2026 (reported June 24, 2026) was a record**: $41.46B revenue, 84.9% non-GAAP gross margin, $50B Q4 guidance, HBM sold out for 2026, and 16 Strategic Customer Agreements worth ~$100B in minimum contracted revenue. Its data-center segments are now *larger* than consumer/edge — a re-dating of the old framing.
6. **The wafer-cannibalization mechanism is company-disclosed, not just analyst opinion**, and is the key reason commodity DRAM prices stay elevated even when consumer demand is weak.
7. **A formal valuation re-rating is underway** (SK Securities switched memory from P/B to P/E in Nov 2025), but single-digit forward multiples show the market has not accepted a permanent non-cyclical thesis.

---

## Details

### A — The mechanism: why bandwidth, not compute, is the wall

**Plain-English.** Every chip has two ceilings: compute (FLOPS) and the rate it can move data from memory to compute units (bandwidth, TB/s). Whichever you hit first caps throughput. The deciding ratio is *arithmetic intensity* — math operations per byte fetched. High intensity → compute-bound; low intensity → memory-bandwidth-bound, with expensive compute idle. This is the roofline model (Williams, Waterman, Patterson, 2009).

**Why LLM inference is memory-bound.** In the *decode* phase (one token at a time), the GPU must read the entire model-weight set for every token. At batch size 1, decode arithmetic intensity is ~1–2 FLOPs/byte — 200–600x below the roofline knee. An H100 has 989 FP16 TFLOPS but 3.35 TB/s HBM3; a 70B FP16 model needs ~140 GB read per token, capping output at ~24 tokens/s and leaving most TFLOPS idle. Doubling FLOPS changes nothing. (Training differs: large batches reuse weights, raising intensity into compute-bound territory. The wall is specifically an *inference/decode* phenomenon — and inference is the dominant, growing share of deployed AI.)

**The scaling gap (verified).** Gholami et al., "AI and Memory Wall" (arXiv:2403.14123): "peak server hardware FLOPS [has been] scaling at a rate of 3x/2yrs, while both the DRAM and interconnect bandwidth have been increasingly falling behind, with a scaling rate of 1.6x/2yrs and 1.4x/2yrs, respectively." Over 20 years FLOPS rose ~60,000x vs ~100x/30x for DRAM/interconnect bandwidth. The d-Matrix CTO and Google's Amin Vahdat independently echo it. **Confidence: high.**

**Where efficiency helps and where it doesn't.**
- *Quantization (FP16→FP8→FP4, INT8/4):* cuts bytes moved per weight, raising arithmetic intensity — genuinely eases bandwidth for a given model (honest exception). But models expand to fill freed memory.
- *MoE/sparsity:* cuts active-parameter compute, but full experts must still reside in memory and be fetchable; at low batch sizes MoE stays bandwidth-bound (GB200's compute-bound threshold ~1,250 FLOPs/byte, far above decode intensity).
- *Speculative decoding:* helps latency but only at low batch sizes — the most bandwidth-bound regime.

Net: efficiency cuts compute/capacity more than bandwidth, and bigger models/more users/longer context/KV-cache re-saturate any headroom.

### B — The memory hierarchy and content per GPU/server/rack

**Three tiers:** (1) **HBM** — stacked DRAM on-package; provides bandwidth; holds active weights + live KV-cache; the binding tier; ~100% three-player. (2) **DDR5/LPDDR5X** — capacity tier; server RDIMMs, KV-cache spillover, CPU/edge. (3) **NAND/SSD** — storage, checkpointing, fast caching, emerging near-memory (HBF).

**HBM per leading-edge GPU (verified, tightened):**

| GPU (year) | HBM capacity | Type | Bandwidth |
|---|---|---|---|
| P100 (2016) | 16 GB | HBM2 | ~0.72 TB/s |
| V100 (2017) | 16→32 GB | HBM2 | ~0.9 TB/s |
| A100 (2020) | 40→80 GB | HBM2e | 1.55→2.0 TB/s |
| H100 (2022) | 80 GB | HBM3 | 3.35 TB/s |
| H200 (2023) | 141 GB | HBM3e | 4.8 TB/s |
| B200 (2024) | 192 GB | HBM3e | 8.0 TB/s |
| GB300/B300 (2025) | 288 GB | HBM3e | ~8 TB/s |
| Vera Rubin (2026E) | 288 GB | HBM4 | ~13 TB/s |

"80→288GB ≈ 3.6x" (H100→B300) is correct; full P100→B300 arc ≈ 18x capacity vs ~500x compute. **Confidence: high.**

**Per server/rack:** GB200 NVL72 = 72 B200 GPUs → ~13.4–13.5 TB HBM3e at 576 TB/s aggregate. An AI server uses ~8x the memory of a traditional server. Server memory BOM share rose from ~30% to ~65–70% in under two years ("server has become a memory appliance"). HBM is >50% of a B300 GPU's BOM; ~50%+ of H100 manufacturing cost, ~60%+ on Blackwell. **Confidence: medium-high.**

**Share of output absorbed by AI:** Per TrendForce, "AI workloads will absorb about 20 percent of global DRAM wafer capacity in 2026," with "one gigabyte of HBM equating to four gigabytes of standard DRAM in wafer area." HBM specifically consumes ~23% of total DRAM wafers in 2026 (up from ~19% in 2025). For NAND, data center became the largest single end-market for the first time in 2026, overtaking mobile. **Confidence: high.**

### C — Company positioning

**Maker map:** HBM/DRAM — SK Hynix (leader), Samsung, Micron (~100% HBM, ~90%+ DRAM). NAND — Samsung, SK Hynix (incl. Solidigm), Micron, Sandisk/Kioxia (JV), China's YMTC.

**Micron (MU) — the HBM-bandwidth bet.** FQ3 2026 (ended May 28, 2026; reported June 24, 2026): revenue **$41.46B** (+74% QoQ, +346% YoY), GAAP GM **84.6%** (non-GAAP 84.9%), net income **$28.24B**; FQ4 guidance **$50B ± $1B** at ~86% GM. Segments: Cloud Memory $13.77B (83% GM); Core Data Center $11.52B (87% GM); Mobile & Client $11.52B; Auto & Embedded $4.63B. HBM share ~21–22% (now #2 by some allocations); **HBM sold out for 2026**; 16 Strategic Customer Agreements ≈ **$100B** minimum contracted revenue. **Re-dated:** the old "datacenter still smaller than consumer/edge" framing is *outdated* — combined data-center BUs ($25.3B) now exceed mobile/client/auto ($16.2B). **Confidence: high (8-K).**

**Sandisk (SNDK) — the NAND-storage bet.** Different vector: enterprise-SSD/storage exposure, not HBM bandwidth. Spun from Western Digital Feb 2025. FQ2 2026: revenue $3.03B (+61% YoY), non-GAAP GM 51.1%, EPS $6.20; data center $440M (+76% YoY); FQ3 guide $4.4–4.8B. Co-developing High Bandwidth Flash (HBF) with SK Hynix. Stock up sharply (>1,200% over prior 12 months at points); high multiples price hyper-growth. **Confidence: high.**

**Crucial distinction — edge/physical-AI uses LPDDR + NAND, not HBM.** Humanoid robots, robotaxis, AI PCs/phones run on-device LPDDR5X and NAND. So the *datacenter HBM leg* benefits SK Hynix/Samsung/Micron (HBM); the *edge/physical-AI leg* benefits LPDDR + NAND suppliers (Micron's LP5X SOCAMM2, automotive LPDDR5, robotaxi DDR5; Samsung; SK Hynix; and on NAND the Sandisk/Kioxia/Micron/Samsung/SK Hynix group). An investor "betting on robots" is betting on LPDDR/NAND, not the HBM margin engine.

### D — Oligopoly structure and pricing power

**Concentration (Q1 2026):** DRAM three makers ≈ 90%+ (90–96%); TrendForce Q1 2026 revenue share: Samsung led, SK Hynix #2 at 28.8%, Micron #3 at 22.4%; Counterpoint Q1 2026: Samsung 38%, SK Hynix 29%. HBM ≈ 100% three-player. The working 62/21/17 split (SK Hynix/Micron/Samsung) is **mid-2025 vintage**; re-dated, SK Hynix ~57% (Counterpoint Q3'25) rising toward ~62–70% (TrendForce Q1'26), with 2026 *bit-output* projected SK Hynix ~50% (from 59% in 2025), Samsung ~20→28%, Micron ~20–24%. Present as a range — it shifts with HBM4 allocation. **Confidence: medium (single-source-per-quarter).**

**Wafer cannibalization (verified, company-disclosed).** Micron's FY2024 call: "HBM3E consumes approximately three times the wafer supply as DDR5 to produce a given number of bits in the same technology node," with the HBM4 trade ratio expected higher. CBO Sumit Sadana: "As we increase HBM supply, it leaves less memory left over for the non-HBM portion of the market, because of this three-to-one basis." (TrendForce's equivalent-GB framing puts it at ~4x for HBM4.) HBM absorbs ~23% of DRAM wafers in 2026; AI ~20% of global DRAM output. This is *why* commodity DDR5/DDR4 prices stay high even with weak consumer demand. **Confidence: high (primary maker + multiple independents).**

**Price trajectory by tier (TrendForce contract prices, re-dated):**

| Quarter | Conventional DRAM QoQ | NAND Flash QoQ |
|---|---|---|
| Q4 2025 | +18–23% (up from +8–13%) | +5–10% |
| Q1 2026 | **+90–95%** (actual ~93–98%; record) | +55–60% |
| Q2 2026 | **+58–63%** | **+70–75%** |

DRAM growth is *decelerating* (95%→~60%) while NAND *accelerated* (60%→75%), outpacing DRAM QoQ for the first time this cycle in Q2 2026. Q1'26 DRAM industry revenue rose 81% QoQ to ~$97B. Per Gartner's April 8, 2026 release: "DRAM and NAND flash annual prices in 2026 will increase by 125% and 234%, respectively, and any meaningful pricing relief is not expected until late 2027"; analyst Rajeev Rajput: "Memflation will destroy, or at least delay, non-AI demand into 2028." **Confidence: high.**

### E — Is the cycle structurally different?

**History — every prior "structural" claim ended in glut:**
- **1995 (Windows PC):** ~20 suppliers, >50% margins, ~50 fab plans 1995–96, flip to oversupply by 1996 — generational crash.
- **2010 (cloud/mobile):** LPDDR muted the uplift; DDR3 2Gb fell ~46% from 1H10 peak by Nov 2010.
- **2017–18 (cloud/NAND):** ~90% price rise, then steep crash within ~2 years.

SemiAnalysis pattern: boom 4–7 quarters → bust 4–8 quarters; revenue −25–40%; margins >50%→low-20s/negative; stocks −50–60%, leading fundamentals by 1–2 quarters. TechInsights' Jim Handy: "supercycle" is overdone — "a classic shortage that usually lasts a year or two."

**What may genuinely differ:** (1) *Demand source* — machine/token demand compounds rather than saturating like human-device counts. (2) *LTAs* — Micron's ~$100B contracted, Sandisk multi-year deals, HBM "sold out" for 2026 reduce uncommitted-capacity risk; honest counter: LTAs are themselves a peak-of-cycle feature with reset clauses, historically renegotiated when the cycle turns. (3) *Supply discipline* — bit-supply growth ~16% (DRAM) vs prior-peak 40–60%; capex skews to packaging/infrastructure over wafer output.

**The 2027–28 supply wave (dated to disclosure):**

| Fab | Maker | Meaningful output |
|---|---|---|
| M15X (Cheongju) | SK Hynix | Wafer-in Feb 2026 (4 mo early); volume mid-2027; HBM4-dedicated |
| Yongin Y1 | SK Hynix | Completion early 2027; ops ~May 2027 |
| Idaho Fab 1 | Micron | First output mid-2027 |
| Tongluo (acq. PSMC) | Micron | Shipments mid-2027 |
| Singapore (HBM packaging) | Micron | H1 2027 |
| New York (Clay) | Micron | ~2028 (full ~2030) |
| P5 (Pyeongtaek) | Samsung | Construction H1 2027; mass production late 2028 |
| Hiroshima | Micron | AI memory ~2028 |

Consensus relief: **late 2027–2028 at earliest** ("no relief until 2028" — Intel's Lip-Bu Tan). The wave adds ~20–30% capacity in a concentrated window — the classic glut setup. Whether it crushes the cycle depends on whether AI/HBM demand (modeled 35–40%+ CAGR) is still outrunning supply when it lands.

### F — The value-migration / re-rating question

**The thesis (now formally articulated).** SK Securities analyst Han Dong-hee, "New paradigm, New multiple" (Nov 3, 2025) — the first time a Korean broker switched memory valuation from P/B to P/E. Logic: memory was P/B-valued because boom/bust made long-term earnings untrustworthy ("build-first, order-later," macro-driven). TSMC — "same cycle, same end-markets, same capital-intensive industry" — earned a P/E because "order-first, build-later" gave trustworthy growth. Han's claim: AI is shifting memory toward TSMC's model (LTAs, discipline, demand breadth), so "if the industry has changed, the methodology for valuing companies must change too." He raised Samsung to ₩170,000 (from ₩110,000; 15x 2026E EPS) and SK Hynix to ₩1,000,000 (from ₩480,000; 11x, a ~15% discount to Micron's 13x), conceding that applying P/E to Korean memory is "an unprecedented…situation [where] a phase of doubt over the reasonableness of the Target P/E level is…inevitable." (Note: 2026 won-denominated targets imply a subsequent share renominalization/split; methodology and percentage moves are consistent but absolute won figures should not be compared across that break.)

The thesis spread: Hanwha (Park Jun-young, June 22, 2026) raised SK Hynix to ₩4,300,000 from ₩1,630,000 on 10x forward P/E — "the Korean memory industry no longer has reason to be valued solely on P/B." KB and Hyundai Motor Securities (blended P/B+P/E) followed; Nomura argued convergence toward TSMC multiples. **Counterpoint:** Kyobo Securities (June 11, 2026) argued P/E *distorts* signals when AI earnings are abnormally inflated (low P/E at peak, spiking at trough), so P/B remains the better benchmark and the cycle is not eliminated.

**Testing it honestly.** The working "<6x forward" figure holds: Samsung ~5.8–6.0x, SK Hynix ~5.2–6.2x, vs Micron ~10x, TSMC ~20x+, Nvidia ~22x (spring 2026). Two defensible reads:
- **Re-rating justified (bull):** Samsung memory and SK Hynix Q4'25 gross margins ~63–67% topped TSMC's ~60% guidance (first time since Q4 2018). Per SK hynix's own 1Q26 release (Apr 22, 2026): revenue ₩52.5763T, operating profit ₩37.6103T (operating margin **72%**), net margin 77% — "operating profit and operating margin reached record highs." Stocks already re-rated (SK Hynix ~4x, Samsung ~3x since Aug 2025; SK Hynix briefly passed Samsung as Korea's most valuable company June 22, 2026). A <6x multiple on quadrupled earnings may under-price durability.
- **Market correctly pricing cyclicality (bear):** <6x is exactly what the market assigns near a cyclical *peak* — discounting normalization. Insider behavior fits: every recent Micron insider transaction is a sale; bear-capitulation upgrades (Morgan Stanley flipping from "DRAM winter") are a mid/late-cycle tell.

**Structural read:** the re-rating is *partly* real (margins, demand source, contract structure genuinely differ), but persistent single-digit multiples show the market has *not* accepted permanent "TSMC-ification." The cycle is being re-rated for higher amplitude and a better demand source — not yet as non-cyclical.

### G — Demand legs beyond the datacenter

**Edge/on-device AI.** AI PCs: Copilot+ requires ≥16GB; 32GB is becoming the practical minimum, with high-end at 32GB+. AMD "Gorgon Halo" supports up to 192GB unified memory (runs a 300B model locally); Nvidia RTX Spark targets the same niche. **But the unit upgrade wave is not materializing — arguably the reverse.** Per Gartner (Feb 26, 2026): "worldwide PC shipments to decline 10.4% and smartphone shipments to drop by 8.4% in 2026," driven by a "130% surge in combined DRAM and SSD prices by the end of 2026," lifting PC prices 17% and smartphone prices 13% — "the steepest contraction in device shipments witnessed in over a decade" (Ranjit Atwal). IDC's downside scenarios: PC −5 to −9%, phones ~−5%. Per HP's Q1 FY2026 call (Feb 25, 2026), memory "now accounts for 35 percent of the cost of materials it needs to build a PC, up from between 15 and 18 percent last quarter." Apple removed the 512GB M3 Ultra Mac Studio upgrade (was $4,000) and raised the 256GB upgrade to $2,000, with Tim Cook acknowledging Mac mini/Studio "may be hard to get for months." **So the edge leg is real in bits-per-device and ASP, but is currently net-suppressing units — an important honest caveat.**

**Physical AI / humanoid robots (Micron CEO claim, stress-tested).** On the June 24, 2026 call, CEO Sanjay Mehrotra said a humanoid robot carries ~10x the memory of an L2+ vehicle and a "sustainable, decades-long memory demand cycle" begins 2026–2030; he separately projected L4-vehicle memory rising from ~16GB to over 300GB, with robots needing "a compute platform comparable to a high-end L4-capable vehicle." *Memory type:* LPDDR + NAND, **not HBM** — so this benefits capacity/storage makers, not the HBM margin engine. *Realism:* these are forward-looking CEO projections, not current revenue. Magnitude check: one GB200 NVL72 rack holds ~13,500 GB of *premium HBM*; even at 300GB/robot of *cheaper LPDDR/NAND*, humanoid robots would need to ship in the *tens of millions of units* to rival 2026 datacenter memory demand (millions of GPUs × 192–288GB HBM) — not in sight this decade. **Verdict: real long-term LPDDR/NAND optionality, immaterial to the 2026–28 thesis; single-source CEO projection, low confidence on timing/magnitude.**

### H — Long-term substitution / disruption risk (5–10 years)

1. **High-Bandwidth Flash (HBF):** Sandisk + SK Hynix OCP standardization (Feb 25, 2026); 8–16x HBM capacity at similar cost, comparable read bandwidth (256GB/die, 512GB per 16-high stack, 1.6 TB/s), but NAND limits (latency, write endurance, write power). A *complement* (capacity tier, SK Hynix "H3" hybrid), not an HBM replacement. Samples H2 2026; inference devices early 2027; scale ~2030. Micron's CEO is cautious. **Likely *expands* memory-maker TAM rather than erodes it. Credibility medium; horizon 2027–2030.**
2. **CXL memory pooling/disaggregation:** CXL 4.0 released Nov 18, 2025 (128 GT/s via PCIe 7.0); 100TB+ shared pools; all three makers supply modules. Eases *capacity* economics (KV-cache offload), not the *bandwidth* wall; adds latency/software complexity. Commercial adoption ~2027 (ABI). **Medium-high for capacity tiering; low as an HBM substitute.**
3. **Processing-in-Memory (PIM):** Samsung HBM-PIM/FIMDRAM, SK Hynix AiM; published PIM-HBM gains ~53% performance/~10% energy. Pre-volume, programming-model-immature. **If it succeeds it *increases* memory's value capture (compute migrates into memory). High as research, low as near-term disruptor; 5–10 yr.**
4. **Advanced packaging (CoWoS evolution, panel-level fan-out, optical):** CoWoS-L sold out through 2027 despite ~3x expansion; packaging is itself a bottleneck. **Mostly *reinforces* the logic+memory moat coupling.**

**Synthesis:** none credibly erodes the memory-maker thesis within ~5 years; most expand value capture or add capacity tiers. The genuine long-term risk is the classic one — **new wafer supply (2027–28 fabs + China's CXMT/YMTC) arriving faster than demand.**

---

## The structural debate, distilled

**Bull (re-rated / dampened cycle):** mechanism durable (3.0x vs 1.6x widens every generation); demand source changed to compounding machine/token demand; oligopoly + capital discipline + HBM cannibalization = higher price floor; LTAs reduce uncommitted-capacity risk; margins now exceed TSMC's (SK Hynix 72% operating margin record; Micron 84.9% GM); <6x multiples may under-price durability.

**Bear (commodity cycle intact, glut risk):** every prior "structural" claim ended in glut within ~2 years; the 2027–28 fab wave is real, coordinated, concentrated; LTAs are a peak-of-cycle feature with reset clauses; <6x is the market correctly pricing peak earnings; insider selling and bear-capitulation upgrades are late-cycle tells; China (CXMT/YMTC) is a supply wildcard prior cycles lacked; efficiency gains + Jevons ambiguity make demand forecasts fragile.

---

## Recommendations (for the explainer's framing and monitoring; no buy/sell/price targets)

**Stage 1 — Frame the page around the mechanism, not the narrative.** Lead with the roofline/arithmetic-intensity explanation (Workstream A) and the 3.0x-vs-1.6x scaling gap. This is the most durable, least-contestable claim and the honest core of "AI runs on memory." Benchmark that would *strengthen* it: each new GPU generation continuing to add HBM faster than it relieves bandwidth-per-FLOP (it has through Rubin).

**Stage 2 — Present the cycle as "structurally different in amplitude, not yet proven non-cyclical."** Use the two-column bull/bear table verbatim. Avoid asserting a permanent re-rating; the data supports "partial re-rating, burden of proof on bulls." Threshold that would shift toward the bull verdict: HBM staying sold-out through 2027 *with* 2027 allocations pricing flat-to-up, *and* inventories staying at 2–4 weeks through the first tranche of the 2027 fab ramp.

**Stage 3 — Instrument the falsifier and secondary signals (below) as a live dashboard.** The cleanest decision-relevant content is the monitoring list. Threshold that would shift toward the bear verdict: the primary falsifier triggering, or any *two* secondary signals turning simultaneously (especially inventory rebuild + 2027 HBM pricing weakness).

**Stage 4 — Keep the demand legs honestly weighted.** Datacenter HBM is the thesis; edge is currently a *content/ASP* story that is *suppressing units*; robotics is *optionality*, not thesis support. Do not let the robot/edge headlines carry weight the unit data doesn't support.

---

## The single clearest falsifier + secondary signals

**Primary falsifier (kills the bullish structural thesis):**
> **HBM contract prices decline QoQ AND aggregate maker book-to-bill falls below 1.0 for two consecutive quarters, while supplier inventories rebuild above ~8 weeks (from current 2–4).**
The HBM-specific condition is essential: a commodity-DRAM-only roll is consistent with the structural thesis (cannibalization easing); an HBM-tier roll means binding-tier pricing power has broken.

**Secondary signals (rough lead-time order):**
1. Supplier inventory rising 2–4 → >8 weeks (earliest classic tell).
2. OEM/hyperscaler double-ordering or buffer-building (none currently).
3. 2027 HBM allocation negotiations settling at *weaker* pricing than 2026.
4. Micron gross margin declining sequentially two quarters (mirrors 2018 peak).
5. Industry DRAM bit-supply growth exceeding ~25% YoY (now ~16%); watch M15X/Idaho/P5 ramp acceleration.
6. CXMT/YMTC HBM-grade qualification progress (China breakout).
7. Any oligopoly "defection" — one maker breaking capital discipline for share.
8. Spot prices rolling over ahead of contract (spot leads contract).

---

## Caveats

- **Several "share" figures are single-source-per-quarter and in flux.** The HBM split (SK Hynix ~57–62%+, Micron ~21–24%, Samsung ~17→28%) shifts with HBM4 allocation; treat as a range. Primary maker disclosure lags independent estimates by a quarter.
- **Working figures re-dated:** (1) the 62/21/17 HBM split is mid-2025; (2) Micron's "datacenter smaller than consumer/edge" is *outdated* — data center is now larger (FQ3'26: $25.3B vs $16.2B); (3) DRAM "~+58–63%" describes Q2'26 and NAND "~+55–60%" describes Q1'26 — different quarters; the record DRAM print was Q1'26 at +90–95%.
- **Robotics and L4-vehicle memory figures are CEO forward-looking projections**, not realized demand — optionality, not thesis support.
- **Wafer-cannibalization multiplier:** ~3x per bit (Micron, company-disclosed) vs TrendForce's ~4x equivalent-GB framing for HBM4 — both are cited correctly; they measure slightly different things (area-per-bit vs equivalent-GB).
- **The SK Securities won targets span a likely share renominalization/split** between Nov 2025 and 2026; methodology and percentage moves are consistent, but absolute won figures should not be compared across that break.
- **Capex magnitudes vary by source/scope:** TrendForce (May 6, 2026) put combined 2026 capex of the top *nine* CSPs (Google, AWS, Meta, Microsoft, Oracle, ByteDance, Tencent, Alibaba, Baidu) at ~US$830B (growth revised "from 61% to 79%"); the US big-four figure is ~$725B (Microsoft ~$190B/~130% YoY; Google $180–190B; Meta $125–145B). Use scope-appropriate figures.
- **Forward statements flagged:** Vera Rubin specs, fab ramp dates, HBF timelines, and all price-trajectory forecasts beyond Q2 2026 are projections subject to revision.