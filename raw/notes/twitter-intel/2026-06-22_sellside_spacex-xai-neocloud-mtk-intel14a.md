# SpaceX/xAI "from LLMs to Neoclouds" — Anthropic/Google compute leases + first datacenter ASIC on Intel 14A

**Source:** staged screenshot `raw/notes/twitter-notes/spacex-move-to-neocloud.jpg` · **Author/issuer:** unnamed sell-side desk (Taiwan-broker style — references "our earlier MTK report *Likely SpaceX Wins* on May 27"; covers MTK 2454 TT) · **Thread/post date:** undated in image (staged 2026-06-22; use as fallback) · **Engagement:** n/a (research-note crop) · **URL:** unknown

## Tier verdict (gates everything)
**Tier 5 as handled — a cropped, undated screenshot of sell-side research.** Underlying issuer is a broker desk (would be **Tier 3 quality** if fully sourced/dated), but a crop with no date, no analyst name, no full note stays at the **Tier-5 floor** and cannot be cited as vault fact. **Aligned-incentive flag: moderate-high** — the note is *constructive on MTK / INTC / NVDA* and explicitly cross-sells its own prior "Likely SpaceX Wins" call. Every figure is a **forecast/estimate** (`[forward]`), and the headline counterparties (SpaceX, xAI, Anthropic) are **private/uninvestable**. **Major name-fidelity red flag (see below): the note conflates SpaceX with xAI.**

## TL;DR
A sell-side desk argues a Musk AI entity is pivoting "LLMs → neocloud" — **leasing out the Colossus supercomputer's idle training compute** at huge scale: a **May 2026 Anthropic deal (~$1.25bn/month through May 2029, all of Colossus 1, ~220k GPUs / >300MW)** and a **June 2026 Google deal (~$920mn/month, ~110k GPUs)**, together implying **~$26bn ARR**. It projects compute capacity scaling **1GW → 4.5GW/9.5GW by 2027/2028**, **2.2m/2.5m Blackwell-equivalent NVIDIA GPUs**, and — the real sell-side payoff — a **first in-house datacenter ASIC (the "Terafab" project) in 4Q28, designed by MediaTek (MTK) on Intel 14A + EMIB-T packaging, with Intel's 14A Arizona fab as the capacity partner.** The investable hooks are **NVDA (GPU demand), INTC (foundry/packaging win), MTK (ASIC design)** — wrapped around private, unverifiable counterparties and a garbled SpaceX/xAI label.

## Named entities
| Entity | Claim in note | Vault page | Confidence |
|---|---|---|---|
| **SpaceX** | The "neocloud" leasing Colossus compute; building Terafab ASIC | no page (private) | **GARBLED — Colossus/Grok are xAI assets, not SpaceX (see red flags)** |
| xAI / Grok / Colossus | Grok tops Arena leaderboard; Colossus 1/2 = 1GW freed compute | no page (private) | inferable (the note's *real* subject) |
| Anthropic | ~$1.25bn/month through May 2029 for all Colossus-1 compute (~220k GPUs, >300MW) | no page (private) | claimed (note) |
| Google / Alphabet | ~$920mn/month for ~110k GPUs | [[GOOGL]] | claimed (note) |
| NVIDIA | Primary GPU; ~2.2m/2.5m Blackwell-equiv GPUs 2027/2028 | [[NVDA]] | claimed (note) |
| MediaTek (MTK, 2454 TT) | Designs the first SpaceX datacenter ASIC (Terafab), 4Q28; full design services | no page (Taiwan-listed) | claimed (note) — **new-name candidate** |
| Intel | 14A Arizona = key capacity partner; EMIB-T advanced packaging | [[INTC]] | claimed (note) |
| Terafab project | The custom-ASIC program; first silicon 4Q28 | no page | claimed (note) |

## Key claims + numbers (all sell-side forecasts/estimates)
- **Anthropic: ~$1.25bn/month → ~$15bn/yr, through May 2029, for all of Colossus 1 (~220k GPUs, >300MW).** `[forward]` `[opinion]`
- **Google: ~$920mn/month (~$11bn/yr) for ~110k GPUs.** `[forward]`
- **Combined ~$26bn ARR** vs. the entity's "2025 AI segment revenue $3.2bn / corporate revenue $18.7bn." `[forward]` — implies a ~8x AI-revenue step-up.
- **Capacity 1GW today → 4.5GW (2027) → 9.5GW (2028).** `[forward]`
- **GPU demand ~2.2m (2027) / ~2.5m (2028) Blackwell-equivalents.** `[forward]`
- **Build speed/cost: Colossus 1 in 122/91 days vs ~2-yr norm; ~$3mn/MW vs ~$10mn/MW industry avg.** `[opinion]` — striking if true; a cost/speed claim worth skepticism.
- **First datacenter ASIC ("Terafab") 4Q28, MTK-designed, Intel 14A + EMIB-T, fab in Arizona.** `[forward]` — the note's core monetizable call.

## Vault cross-reference
- **[[hyperscaler-custom-ASIC]] — ADDS a new entrant.** A Musk AI entity commissioning its own datacenter ASIC (MTK-designed, Intel-fabbed) extends the custom-silicon proliferation thesis *beyond* the MSFT/GOOG/AMZN/META set — and notably routes around the Broadcom/Marvell + TSMC default stack (MTK + Intel instead). If real, it's a datapoint that custom-ASIC ambition is now table stakes even for neocloud-scale buyers. Confirms the theme's direction; introduces a non-hyperscaler ASIC buyer.
- **[[neocloud-moat-durability]] — CONFIRMS the commoditization read.** "Lease your idle training cluster as a neocloud" is exactly the borrowed/temporary-edge dynamic the page argues — compute as a fungible rental, not a moat. A new mega-entrant renting out Colossus pressures CRWV/NBIS-style economics (more supply of rentable GPUs).
- **[[AI-buildout-who-holds-the-risk]] — ADDS a circular-financing datapoint.** **Anthropic committing ~$15bn/yr to a Musk compute entity** is precisely the frontier-lab-funding / who-holds-the-risk question the page tracks (Anthropic's own funding must support that run-rate). Tier-5 only, but it's a vivid "who's actually paying, and with what money" flag.
- **[[INTC]] — bullish Foundry datapoint (verify hard).** Intel **14A Arizona + EMIB-T** as the capacity/packaging partner for a marquee AI ASIC would be a real external-validation signal for Intel Foundry's 14A node — directly relevant to the INTC thesis (foundry turnaround). This is the **highest-value investable hook** in the crop.
- **[[NVDA]] / [[AI-demand-durability]] — demand datapoint.** 2.2–2.5m Blackwell-equiv GPUs + $26bn ARR is incremental AI-compute demand; supports demand-durability, but it's a single sell-side estimate on a private buyer — weight accordingly.
- **[[GOOGL]] — tangential.** Google as a *compute lessee* of a rival Musk cluster is an odd cross-buy; if real, a capacity-tightness signal (even Google renting third-party GPUs). Verify — could be garbled.
- **[[advanced-optical-packaging]] / packaging — context.** EMIB-T is Intel's advanced-packaging answer (vs TSMC CoWoS) — a non-TSMC packaging datapoint for the packaging-chokepoint pages.

## Ingest leads (verify at primary / higher tier)
1. **INTC 14A external customer** — does Intel confirm a major AI-ASIC foundry/packaging win on 14A (Arizona) + EMIB-T at its next earnings call / Foundry update? This is the one genuinely checkable, thesis-moving item for a *listed* vault name. → [[INTC]] next 10-Q/call.
2. **NVDA GPU-demand corroboration** — any NVIDIA commentary on a large neocloud/Musk-entity Blackwell allocation. → [[NVDA]].
3. **MediaTek (2454 TT) as a custom-ASIC designer** — **new-page candidate**: MTK keeps surfacing as an ASIC-design alternative to Broadcom/Marvell. If a 2nd–3rd independent source names MTK in AI datacenter ASICs, it may cross the page-creation threshold for [[hyperscaler-custom-ASIC]] coverage (Vic curates).
4. **The Anthropic/Google compute-lease dollar figures** — private counterparties; unverifiable at primary. Treat $1.25bn/mo & $920mn/mo as Tier-5 rumor until a filing/press confirms. Feeds [[AI-buildout-who-holds-the-risk]] only as a *question*.

## Contradictions / red flags
- **★ SpaceX vs xAI conflation (load-bearing).** **Colossus and Grok are xAI's assets, not SpaceX's.** The note repeatedly says "SpaceX" while describing xAI's supercomputer and model. Either the author is using "SpaceX" as loose shorthand for Musk's AI entity, or there's an assumed corporate consolidation not stated here. **Do not propagate "SpaceX builds AI datacenters" as fact** — verify which legal entity before any of this touches a vault page.
- **Cropped, undated, self-promotional.** References "our earlier MTK report *Likely SpaceX Wins*" — the desk is talking its own book on MTK/INTC. Constructive-call incentive; weight as confirmation-seeking.
- **Extraordinary numbers.** ~$26bn ARR from ~$3.2bn, $1.25bn/month single-customer commitments, ~$3mn/MW build cost (⅓ of industry) — all are remarkable claims on a private entity; none are disclosures. High burden of proof.
- **Private all the way down.** SpaceX, xAI, Anthropic are unlisted — there is no direct investable expression of the headline; only the *suppliers* (NVDA, INTC, MTK) are reachable, which is conveniently where the sell-side note points.

## Source-tier verdict (restated)
**Tier 5 — do not cite as vault fact.** A cropped, undated, book-talking sell-side note with a SpaceX/xAI entity error. Use it to generate questions only: the single worthwhile lead is **whether Intel confirms a 14A/EMIB-T AI-ASIC foundry win** (checkable at INTC primary). Verify entity identity + all figures before any page edit.

## Thread (Tier 5 — not a primary source)
> **SpaceX from LLMs to Neoclouds**
> According to Arena AI (LLM Leaderboard), Grok now outperforms major LLMs. The Colossus 1/2 has freed compute capacity, [and] we believe this has accelerated SpaceX' shift toward infrastructure monetization by leasing compute capacity at Colossus which originally built for Grok training, to generate higher revenue streams. By its transition toward Neocloud business model, 1) In May 2026, SpaceX signed cloud service agreements with Anthropic, with Anthropic committing to pay $1.25bn per month through May 2029 to use all of the compute capacity at Colossus 1, including ~220k GPUs that can provide over 300MW. 2) In June 2026, Google entered into agreements with SpaceX, paying $920mn per month for access to compute capacity of ~110k GPUs. Together, the Anthropic and Google deals imply ~$26bn of ARR vs. SpaceX's 2025 AI segment revenue of $3.2bn and corporate revenue of $18.7bn.
>
> **SpaceX compute capacity to increase substantially.** According to the company, the Colossus 1/2 has 1GW compute capacity. Driven by the transformation to Neocloud, we expect the total compute capacity to be 4.5GW/9.5GW by 2027/2028. We expect SpaceX to primarily adopt Nvidia GPU, with demand of ~2.2m/~2.5m Blackwell-equivalent GPUs in 2027/2028. We note that SpaceX constructed datacenters within extremely short time, including Colossus 1 in 122/91 days vs. industry benchmark of ~2 years, with low build cost of ~$3mn/MW vs. industry average of ~$10mn/MW. Additionally, as said in our earlier MTK report of *Likely SpaceX Wins* on May 27, SpaceX is expected to start its first datacenter ASIC, being a part of the Terafab project, in 4Q28. We believe it is designed by MTK based on Intel 14A and EMIB-T.
>
> **Recommendations**
> GPU and datacenter ASICs – Nvidia (NVDA), MTK (2454 TT), Intel (INTC): We expect SpaceX to primarily adopt Nvidia's GPU, with demand of ~2.2m/~2.5m GPUs in 2027/2028. Additionally, SpaceX is expected to start its first datacenter ASIC in 4Q28. We expect MTK to obtain the project, backed by its experience with Intel's process, and are likely to benefit from providing the full design services. Capacity wise, we expect Intel's 14A in Arizona to be the key capacity partner.
