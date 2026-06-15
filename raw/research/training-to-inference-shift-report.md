# Training → Inference Shift — value-capture + chokepoint analysis (Tier-3 deep-research anchor)

**Created:** 2026-06-15
**Provenance:** `/deep-research` harness run `wf_cd306f45-e0d` — 106 agents, 5 search angles, 24 sources fetched, 100 claims extracted, **25 adversarially verified (3-vote): 17 confirmed, 8 killed.**
**Boundary (read first):** This is a **Tier-3 discovery anchor**, not vault canon. Every figure here is a consultancy/analyst **forecast or a secondary-sourced claim**, not a primary filing. It is the evaluation substrate for a theme page; nothing here is citable as vault fact without primary-source confirmation. Quarantined refuted claims are listed explicitly — do NOT carry them forward.

## The question

As AI compute shifts from training to inference (2024-2026 and forward): how big/fast is the shift; where inference actually runs (datacenter vs edge); who captures the value (NVIDIA vs custom ASICs vs inference-specialists vs edge silicon); what it does to the AI-datacenter chokepoints (HBM, optics, power, Jevons); and the investable surface — verified shipping/revenue vs hype.

## Headline verdict (the reason this matters to the vault)

**The training→inference shift SUSTAINS every AI-datacenter chokepoint the vault tracks — it does not relieve them.** Inference is *memory-bandwidth-bound* where training is compute-bound, so as inference comes to dominate, the binding constraint migrates *toward* HBM/memory-bandwidth and power-per-token, not away from the datacenter. Edge/on-device is a **false dawn** for frontier inference (the fails-to-monetize cohort). NVIDIA defends *into* inference (Groq absorption + inference racks). Net: this is a **thesis-reinforcing, worry-closing** result — the datacenter thesis is *more* durable in the inference era, not less.

## Verified findings (confirmed 3-vote)

1. **Size + pace — real, but slower and more datacenter-bound than the hype (HIGH).** McKinsey (confirmed 3-0): inference **surpasses training as the dominant AI workload by ~2030**, reaching **>half of all AI compute** and **30-40% of total datacenter demand**, on a ~35% CAGR to **>90 GW**. These are Tier-3 *forecasts*, not shipped data. The more aggressive consultancy numbers did NOT survive (see refuted).
2. **Where it runs — edge is a false dawn for frontier work (HIGH).** Most 2026 inference stays in **metro hyperscale datacenters** because of a **30-50x memory-bandwidth gap** vs edge silicon + phone-RAM ceilings (Deloitte: "most inference will still take place in new data centers rather than at the edge"). Latency sets the split: training tolerates ~100ms → remote/power-rich sites; real-time inference needs **metro low-round-trip**. On-device economics work only for a narrow niche; the **AI-PC / AI-phone "supercycle" is "dead on arrival"** (Tom's Hardware/Micron). Edge AI = the **fails-to-monetize cohort**.
3. **Value capture — NVIDIA defends into inference (HIGH).** NVIDIA **absorbed Groq** for ~$20B as a **non-exclusive license + team-hire** structured to avoid antitrust (Jensen: "we are not acquiring Groq"; CNBC secondary), shipping a hybrid **GPU+LPU** inference system in ~4 months; and is building **dedicated inference-optimized racks** (confirmed 3-0). Hyperscaler ASICs **do ship for inference** — **Microsoft Maia 200 is in production serving GPT-5.2** (confirmed 3-0). BUT the headline aggregate "inference ASICs = $20B+ 2025 / $50B+ 2026 revenue" **failed verification** (see refuted).
4. **Chokepoints — memory bandwidth is the binding constraint (HIGH).** **LLM inference is memory-bandwidth-bound, not compute-bound** (confirmed 3-0): token decode is bandwidth-limited, and **reasoning / test-time-scaling explodes the KV cache** (confirmed 3-0), so the shift **sustains, not relieves**, memory + power + optical chokepoints. **HBM demand surging >130% YoY 2025, >70% 2026** (TrendForce); **HBM4 ~2-3.3 TB/s** (Samsung 13 Gb/s/pin, confirmed 3-0); **inference racks ~370 kW (~3x training density)** (Deloitte); per-query energy **+13x** for reasoning; optics converging on **CPO** (DWDM scale-up + DR-optics scale-out, confirmed 3-0). "HBM demand is surging, NOT relieved by the inference shift" — confirmed 3-0.

## Live variable (partial / nuanced)

- **KV-cache compression (~5-6x) flattens but does not reverse the memory-demand slope** — Jevons (more, cheaper inference) keeps the aggregate climbing. This is the single biggest swing factor on the power/memory thesis; watch it.
- "Test-time scaling / reasoning models materially raise [memory + compute] demand" — confirmed 2-1 (held, but not unanimous).

## Quarantined — REFUTED claims (do NOT carry as fact)

The 8 killed claims are the floating narratives that did NOT survive verification — useful precisely because they are widely repeated:

| Refuted claim | Vote | Why it matters |
|---|---|---|
| Inference = **67% of compute by 2026** (33→50→67 progression) | 0-3 | The aggressive consultancy hockey-stick; use McKinsey-2030 instead |
| Inference becomes **primary AI-server driver by 2028/2029** (TrendForce) | 0-3 | Too fast; the durable read is ~2030 |
| Custom inference ASICs = **>$20B 2025 / $50B+ 2026** revenue | 1-2 | ASICs ship (Maia), but this aggregate-revenue threat is unverified |
| **8-20x efficiency offset** keeps inference power "manageable" | 1-2 | The power-RELIEF bear case died — efficiency does not offset Jevons |
| **~0.31 Wh/query**, headlines overstate energy 4-20x | 1-2 | The low-energy framing did not hold |
| **Edge is the durable home** for latency-critical inference (two-stage hybrid) | 0-3 | The edge-BULL case died — edge is a false dawn for frontier |
| Edge-vs-cloud split set by a **single dominant factor** per workload | 0-3 | Oversimplified |
| Structural **"memory wall" = compute growing 3x faster than bandwidth** | 1-2 | The *specific* 3x framing failed; the broader "memory-bandwidth-bound + HBM surging" DID hold (finding 4) |

## What this means for the vault (integration map)

- **Reinforces (the inference era is more memory/power-bound, not less):** [[HBM-oligopoly]] (the mechanism — inference is memory-bandwidth-bound + KV-cache explosion = why HBM demand keeps surging), [[AI-demand-durability]] (inference *sustains* the demand curve), [[liquid-cooling]] (~370 kW inference racks), [[cpo-integration]] / [[advanced-optical-packaging]] (CPO convergence), [[transformer-supply]] (power-per-token).
- **Closes a worry:** the "edge disrupts the datacenter" thesis is a false dawn → a [[QCOM]] / edge-silicon ingest would be a **weak-fit counterpoint** page (the INOD/PLAB pattern), not a strong-thesis one.
- **Value-capture:** consistent with [[hyperscaler-custom-ASIC]] — ASICs ship but NVIDIA's grip extends into inference (Groq); the aggregate-ASIC-revenue threat is unverified.
- **Forward-edge variant view:** the market frets that edge + efficiency gains will *relieve* the datacenter; the vault view (now research-backed) is that inference **sustains** the chokepoints → a [[forward-edge-tracker]] entry.

## Caveats

- Share / GW / capex numbers are **Tier-3 consultancy forecasts** (McKinsey, Deloitte, TrendForce, Morgan Stanley), not facts.
- Mechanism claims lean on **SemiAnalysis (Tier 3)**, corroborated by NVIDIA / Samsung / Microsoft / JEDEC primary docs.
- The Groq ~$20B figure is **secondary (CNBC)**, not a primary disclosure.
- Qualcomm's edge-economics framing is **its own position** and was rebutted on substance.

## Key sources (quality-tagged)

- McKinsey — "The next big shifts in AI workloads and hyperscaler strategies" (secondary) — the 2030 / >50% / 30-40% / 90 GW figures.
- Deloitte 2026 TMT Predictions — "compute power AI" (secondary) — datacenter-hosted inference, 370 kW racks.
- SemiAnalysis — "NVIDIA: The Inference Kingdom Expands" + "Scaling the Memory Wall: HBM" + "ISSCC 2026: NVIDIA and Broadcom CPO" (secondary) — the memory-bandwidth-bound mechanism + Groq + CPO.
- TrendForce — memory-wall / HBM (secondary) — HBM >130% YoY.
- Tom's Hardware — "AI PC revolution dead on arrival … supercycle is a bust" (secondary) — the edge false-dawn evidence.
- Morgan Stanley AI Market Trends 2026 (secondary).
- ScienceDirect S2542435126001145 (primary, energy-per-query) — the source of the refuted 0.31 Wh / 8-20x-offset claims.
