---
type: company
tickers: [AVGO]
layer: 1
photonics_tier: 3
last_updated: 2026-06-13
---

# Broadcom Inc. (AVGO)

## Thesis role

Layer 1 platform definer alongside [[NVDA]]. AVGO designs custom AI accelerators (XPUs) and networking silicon for hyperscaler data centers, and operates VMware Cloud Foundation (VCF) as enterprise infrastructure software. One of five CPO platform contestants tracked in [[CPO-platform-battle]] via the Bailly platform. Fabless model; 95% of contract-manufactured wafers produced by [[TSM]] (AVGO 10-K FY2025) — the most explicit foundry dependency disclosure in the vault. See [[TSMC-CoWoS]].

**Layer 1 classification with straddling tension.** AVGO's Layer 1 positioning rests on three pillars: (1) networking platform dominance — Tomahawk switching and SerDes leadership at 200G, "the only one out there" (AVGO Q1 FY2026 call); (2) VMware software platform at 93% gross margin, framed as "the essential software layer in data centers... cannot be disintermediated or replaced" (Hock Tan, AVGO Q1 FY2026 call); (3) multi-generation strategic custom ASIC relationships at gigawatt scale with six customers. The straddling tension is real: semiconductor segment GAAP gross margin of ~68.1% is below [[NVDA]]'s 75.2% and closer to [[TSM]]'s 66.2% — Layer 1-2 boundary, not clearly Layer 1. Custom ASIC economics are design-service, not platform-licensing: each XPU is customer-specified, customer-owned tooling is explicitly flagged as a risk in both Tier 1 filings, and AI rack leasing "will likely increase our operating margin but compress or lower future gross margin" (AVGO 10-K FY2025). No CUDA equivalent — AVGO's moat is custom design relationships and SerDes IP, not a developer ecosystem. The Layer 1 classification is maintained per `_thesis.md` and `frameworks.md`; the straddling tension is flagged honestly rather than resolved.

*Control-point distinction (per `raw/research/photonics-chokepoint-table.md`, Tier 3 source).* AVGO is the second strongest strategic control-point name in the vault — Tomahawk switch architecture, custom XPU programs, Bailly CPO platform decisions, and 200G/400G SerDes leadership shape AI networking ecosystem direction. The control-point distinction is complementary to the Layer 1/3 straddling tension already documented above: control-point authority extends beyond layer placement to encompass architectural decision authority. Per the framework: "control point, not just bottleneck." Cross-reference: control-point thread spans [[NVDA]], [[AVGO]], [[MRVL]], [[CSCO]], [[ANET]] within vault per framework five-company set.

## Financial snapshot

### FY2025 annual (10-K, Tier 1)

| Metric | FY2025 | FY2024 | FY2023 |
|--------|--------|--------|--------|
| Revenue | $63,887M | $51,574M | $35,819M |
| Revenue YoY | +24% | +44% | — |
| Semiconductor solutions | $36,858M (58%) | $30,096M (58%) | — |
| Infrastructure software | $27,029M (42%) | $21,478M (42%) | — |
| GAAP gross margin | 68% | 63% | — |
| Semi segment implied GM | 68.1%* | — | — |
| Software segment implied GM | 93.0%* | — | — |
| GAAP operating income | $25,484M (40%) | $13,463M (26%) | — |
| Semi operating income | $21,232M (57.6%) | $16,759M (55.7%) | — |
| Software operating income | $20,765M (76.8%) | $13,977M (65.1%) | — |
| Net income | $23,126M | $5,895M** | $14,082M |
| Diluted EPS | $4.77 | $1.23** | — |
| Operating cash flow | $27,537M | $19,962M | — |
| Capex | $623M (<1%) | $548M | — |
| R&D | $10,977M (17%) | $9,310M | — |

*Segment cost figures exclude $6,031M acquisition-related intangible amortization in COGS. **FY2024 depressed by $3,748M non-recurring tax provision. (AVGO 10-K FY2025)

### Q1 FY2026 quarterly (10-Q, Tier 1)

| Metric | Q1 FY2026 | Q1 FY2025 |
|--------|-----------|-----------|
| Revenue | $19,311M | $14,916M |
| Revenue YoY | +29% | — |
| Semiconductor solutions | $12,515M (65%) | $8,212M (55%) |
| Infrastructure software | $6,796M (35%) | $6,704M (45%) |
| GAAP gross margin | 68.1% | 68.0% |
| Semi operating margin | 60% | 57% |
| Software operating margin | 78.3% | 76.4% |
| Net income | $7,349M | $5,503M |
| Diluted EPS | $1.50 | $1.14 |
| FCF | ~$8,010M (41.5%) | ~$5,963M |

(AVGO 10-Q Q1 FY2026)

### Q2 FY2026 quarterly (10-Q Tier 1, quarter ended May 3, 2026 + earnings call Tier 2, June 3, 2026)

| Metric | Q2 FY2026 | Q2 FY2025 | YoY |
|--------|-----------|-----------|-----|
| Revenue | $22,187M | $15,004M | +48% |
| Semiconductor solutions | $15,009M (68%) | $8,408M (56%) | +79% |
| Infrastructure software | $7,178M (32%) | $6,596M (44%) | +9% |
| GAAP gross margin | 69% | 68% | +100bps |
| GAAP operating income | $10,788M (49% of rev) | $5,829M (39%) | +85% |
| Semi segment operating income | $9,281M (61.8%) | $4,806M (57.2%) | +93% |
| Software segment operating income | $5,647M (78.7%) | $4,987M (75.6%) | +13% |
| Net income | $9,310M | $4,965M | +88% |
| Diluted EPS | $1.91 | $1.03 | +85% |
| Inventory | $4,328M | $2,270M (Nov 2, 2025) | +91% in two quarters |
| Cash | $19,628M | $16,178M (Nov 2, 2025) | — |

(AVGO 10-Q Q2 FY2026)

Revenue landed slightly above the ~$22B guide; the semiconductor segment (+79% YoY) is now 68% of revenue and its operating margin expanded ~460bps YoY. Inventory nearly doubled in two quarters ($2,270M → $2,962M → $4,328M) — the production-ramp signal first flagged at Q1 is accelerating. 1H capital returns: $8,450M buybacks + $6,178M dividends.

**NEW — the $29B AI-rack lease backstop, and the structure behind it (the rack-leasing risk, now quantified AND identified).** The 10-Q discloses that AVGO "arranged for an investor partner to take on certain agreements to purchase AI racks based on custom AI accelerators designed by us and the related lease agreements with a customer," and entered a backstop for that customer's lease obligations over 5-year terms — **maximum exposure $29 billion**, growing as racks deploy and shrinking as the customer pays; remedies on default include assuming the lease or selling the racks (AVGO 10-Q Q2 FY2026). The Q2 call names the structure: Hock Tan is "creating the **AI XPU platform with Apollo and Blackstone** and other leading investors to deploy **more than 20 GW of compute capacity through 2028**," with "the first tranche of this platform, valued at **$35 billion**, currently being launched by Apollo" — built for "the leading AI frontier labs, including Anthropic and OpenAI" (AVGO Q2 FY2026 call). Tom O'Malley framed the recent Anthropic deal as "backstopped by Broadcom chips"; Hock Tan corrected the mechanics but confirmed the deal ("we use our TPU chips… to provide the compute capacity to Anthropic… disclosed in our 8-K recently") — making **Anthropic the inferable (not disclosed) customer behind the $29B backstop**. The structure keeps rack economics off AVGO's P&L ("No rack. It's all chips. We're in the chip business only" — Hock Tan, with Spears echoing) while concentrating frontier-lab credit risk on the balance sheet as a contingent exposure ~1.3× a quarter's revenue.

**Stability checks at Q2 (Tier 1):** single-distributor concentration **42%** (stable vs Q1's 42%; vs 29% prior year); top-5 end customers ~45% (vs 40%); ~95% TSMC wafer dependency restated verbatim, with new explicit language that TSMC "has raised, and may in the future raise" prices; **zero CPO / silicon-photonics mentions** — the Tier-1 silence pattern persists through Q2.

**Q2 FY2026 call (Tier 2, June 3, 2026) — the AI numbers and the program map, one quarter on:**

| Item | Q2 FY2026 call disclosure |
|---|---|
| AI semiconductor revenue | **$10.8B, +143% YoY** (record; 49% of total revenue); networking ~40% of AI revenue ("stars align" peak — expected to settle ~30%) |
| AI bookings | **>$30B booked in the quarter** vs $10.8B shipped; visibility now extends **to 2028** ("three months ago… 2027") |
| FY2026 AI guide | **$56B (+~180% YoY)** — H2 to roughly double the ~$19B H1 |
| Q3 FY2026 guide | Total revenue **$29.4B +84%**; semi $20.5B +124%; **AI semi $16B, +200% YoY**; software $8.9B +31%; GM ~74% (mix, "not structural"); op margin ~67% flat |
| FY2027 | **">$100B" AI revenue REITERATED** ("easily exceed"); 10 GW 2027 shipment intact, back-half loaded; 2028 "a lot more gigawatts," "substantial growth" |
| Margins | Non-GAAP GM 77.1% (−230bps, mix); record op margin 67.3% (+200bps); FCF record $10.3B (46% of revenue); TPU/ASIC margins lower, AI networking "very rich" offsetting (Spears) |

**Customer-program updates vs the Q1 baseline (all Tier 2, named):** **Google** — April long-term agreement for *multiple generations* of TPUs + AI networking, "very substantial dollars," with Hock Tan explicitly accepting "some diversity of sources" at Google (the share question, answered with a hedge). **Anthropic** — >1 GW TPU compute in 2026 + a NEW April agreement for **another 5 GW of next-generation TPU compute beginning 2027** (up from ">3 GW in 2027" at Q1). **OpenAI** — silicon delivered, production on track late 2026, **contractual 1.3 GW in 2027** within the 10-GW-by-2029 deal. **Meta** — April partnership for multiple generations of MTIA XPUs, **3 GW through end-2028**, initial 1 GW order received (delivery 2H 2027). Other two customers: shipments late 2026, **$6B of purchase orders received**. Supply: secured 2026–2027, "working on 2028 and 2029 right now." Demand framing: "insatiable," "sustainable and steepening" — with enterprise token consumption routed through the same few frontier labs ("Opus 4.7, ChatGPT 5.5 or Gemini 3.5"), concentrating end-demand on AVGO's six customers.

**CFO transition:** Kirsten Spears retires June 12, 2026 after 12 years; **Amie Thuener incoming CFO** — guidance-methodology continuity is a watch item for the next two quarters.

### Forward outlook (Tier 2 — management guidance, AVGO Q1 FY2026 call)

| Metric | Q2 FY2026 guidance | 2027 outlook |
|--------|-------------------|--------------|
| Total revenue | ~$22B (+47% YoY) | — |
| Semiconductor | ~$14.8B (+76% YoY) | — |
| AI semiconductor | ~$10.7B (+140% YoY) | "$100B+" (chips only) |
| Non-AI semiconductor | ~$4.1B (+4% YoY) | — |
| Infrastructure software | ~$7.2B (+9% YoY) | — |
| Non-GAAP GM | 77% (flat) | — |
| Adjusted EBITDA | ~68% of revenue | — |
| Compute capacity | — | ~10 GW |

**Hock Tan's "$100B+" AI chip revenue claim — three formulations with escalating qualifier:**

1. "Today, in fact, we have line of sight to achieve AI revenue from chips, just chips in excess of $100 billion in 2027. We have also secured the supply chain required to achieve this" (Hock Tan, AVGO Q1 FY2026 call, prepared remarks).

2. "When I say we forecast, we have a line of sight that our revenue in 2027 will be significantly in excess of $100 billion, I'm focusing on the fact that these are pretty much all based on chips. Whether they are XPUs, whether they are switch chips, DSPs, these are silicon content we're talking about" (Hock Tan, AVGO Q1 FY2026 call, Blayne Curtis clarification).

3. On gigawatt math — Stacy Rasgon placed content at roughly "$20 billion per gigawatt." Hock Tan: "It's not far from the dollars you're talking about. If you look at it by gigawatt in 2027, we are seeing it getting close to 10 GW" (AVGO Q1 FY2026 call). The GW math is directional — "not far" is a qualifier, not a confirmation; $/GW "varies, sometimes quite dramatically" across customers.

The claim is scoped to silicon content only (XPUs, switch chips, DSPs), explicitly excluding racks and non-silicon. Supply chain "fully secured for 2026 through 2028." The qualifier escalation from "in excess of" to "significantly in excess of" over the same call is itself a signal — the initial framing was conservative relative to Hock Tan's actual confidence level.

## Custom AI accelerator franchise

Six custom AI accelerator customers as of Q1 FY2026, corrected from five during the call — "Sorry, not five, six. Six" (Hock Tan, AVGO Q1 FY2026 call):

| Customer | Detail | Source |
|----------|--------|--------|
| [[GOOGL]] | 7th-gen Ironwood TPU; continued 2026 growth; stronger demand from next-gen TPUs in 2027+ | AVGO Q1 FY2026 call |
| Anthropic | "1 GW of TPU compute" in 2026; demand surging to >3 GW in 2027 | AVGO Q1 FY2026 call |
| Meta | MTIA "alive and well... we're shipping now"; next-gen XPUs to "multiple gigawatts in 2027 and beyond" | AVGO Q1 FY2026 call |
| OpenAI | 6th customer; 1st-gen XPU 2027 at >1 GW; 10 GW deal through 2029 (analyst-sourced, not denied) | AVGO Q1 FY2026 call |
| Customer 4 | Unnamed; "strong shipments this year," expected to more than double in 2027 | AVGO Q1 FY2026 call |
| Customer 5 | Unnamed; same trajectory as Customer 4 | AVGO Q1 FY2026 call |

No XPU customers are named in either Tier 1 filing. The 10-K and 10-Q refer only to "hyperscalers, companies with AI frontier models and system integrators" (AVGO 10-K FY2025). Hock Tan's naming specificity — Google, Anthropic, Meta, OpenAI by name with GW figures — is the most customer-specific AI disclosure in the vault, contrasting sharply with [[NVDA]] (names no customers) and [[MRVL]] (names no XPU customers).

**Anthropic "TPU compute" observation.** Hock Tan's exact wording: "For Anthropic, we are off to a very good start in 2026 for 1 GW of TPU compute" (AVGO Q1 FY2026 call). The use of "TPU compute" — Google's TPU architecture terminology — for an Anthropic deployment raises a thesis-relevant question: is Anthropic running on Google TPU architecture designed by Broadcom, making it a derivative of the Google relationship rather than a fully independent XPU program? This observation is reinforced by Hock Tan's self-described "Freudian slip" later on the call: "You can tweak your TPUs — sorry, Freudian slip" when referring to all XPUs generically (AVGO Q1 FY2026 call). Google TPU is reflexive vocabulary for Hock Tan, suggesting its dominance within AVGO's custom silicon franchise. If Anthropic's program is architecturally derived from Google TPU, six customer names may overstate the number of independent design-in programs. This is framed as a thesis-relevant observation about franchise concentration, not definitive proof of program consolidation.

**AI semiconductor revenue.** Q1: $8.4B (+106% YoY), "way above our outlook" (Hock Tan). Custom accelerators +140% YoY. AI networking: ~$2.8B (+60% YoY, one-third of AI total). Non-AI semiconductor: $4.1B, flat YoY. Q2 guidance: AI semi ~$10.7B (+140% YoY), networking growing to ~40% of AI total (AVGO Q1 FY2026 call). AI semiconductor revenue is disclosed only on the call (Tier 2); neither Tier 1 filing breaks out AI-specific figures. See [[AI-demand-durability]] for AVGO's contribution to six-position demand convergence.

**XPU vs. GPU competitive framing.** Hock Tan positioned custom XPUs as the trajectory: "The one-size-fits-all with general purpose GPU gets you only that far... XPUs will eventually be more the choice" (AVGO Q1 FY2026 call). He named [[NVDA]] as the competitive benchmark: "you're also competing against NVIDIA, who is by no means letting down their guard" (AVGO Q1 FY2026 call). [[ALAB]]'s 10-K FY2025 names Broadcom as a direct competitor in the connectivity and fabric switching market. Both companies serve scale-up cluster interconnect — AVGO via SerDes/copper DAC, ALAB via Scorpio switches and NVLink Fusion. See [[hyperscaler-custom-ASIC]] for the cross-company custom ASIC competitive landscape and warrant structure comparison.

## Networking and interconnect platform

AVGO's networking silicon provides the platform layer that distinguishes it from pure custom ASIC designers like [[MRVL]]:

- **Tomahawk 6:** "First to market" at 100 Tbps with 200G SerDes — "we're the only one out there" (Hock Tan, AVGO Q1 FY2026 call). Introduced 9 months prior.
- **Tomahawk 7:** Next generation, "double the performance," launching 2027 (AVGO Q1 FY2026 call).
- **1.6 Tb optical transceivers:** "The only player out there doing DSP at 1.6 Tb" (Hock Tan, AVGO Q1 FY2026 call).
- **SerDes roadmap:** 200G SerDes in production, 400G in development. Central to AVGO's CPO deferral argument — copper DAC extends as SerDes speed increases.
- **AI networking mix:** 33-40% of total AI semiconductor revenue, growing from one-third in Q1 to guided ~40% in Q2 (AVGO Q1 FY2026 call).

Charlie Kawwas on Ethernet for scale-up: "What we're hearing consistently and what we're seeing is the right answer is Ethernet" — positioning Ethernet for both scale-out and scale-up, announced with "multiple hyperscalers and many of our peers" (AVGO Q1 FY2026 call).

## CPO positioning

**"Bright, shiny objects."** Hock Tan's CPO framing is the most dismissive in the vault:

> "All I'm trying to say is you don't need to go run into some bright, shiny objects called CPO, even as we are the lead in CPOs. CPOs will come in its time, not this year, maybe not next year, but in its time" (Hock Tan, AVGO Q1 FY2026 call).

AVGO simultaneously claims CPO leadership ("we are the lead in CPOs") and pushes the timeline. "Bailly" — AVGO's named CPO platform — is **never mentioned** in any of the three sources. Both Tier 1 filings contain zero mentions of CPO, co-packaged optics, silicon photonics, or any photonics-forward language. See [[CPO-platform-battle]] for the tiered silence pattern and the Layer 1 active dismissal variant.

**Scale-up: copper DAC via SerDes, not CPO.** Hock Tan's core argument: "You really want to connect XPUs to XPUs directly where you can. The best way to do that is use Direct Attach Copper. That's the lowest latency, lowest power, and lowest cost... We can do it with copper, we can push the envelope from 100G to 200G to even 400G" (AVGO Q1 FY2026 call). Scale-up uses copper (Broadcom's SerDes advantage); scale-out uses Ethernet optical (Broadcom's Tomahawk advantage). CPO is deferred.

**Murphy ↔ Hock Tan disagreement.** This framing directly contradicts [[MRVL]] CEO Murphy's positioning: Murphy says scale-up CPO is "inflecting in a pretty big way" (MRVL Q4 FY2026 call); Hock Tan says scale-up uses copper and CPO is "bright, shiny objects." Both agree on the scale-out/scale-up bifurcation structure — they disagree on what technology wins scale-up: optical (CPO, MRVL's Photonic Fabric) or electrical (copper DAC, AVGO's SerDes). Both positions are self-serving: Murphy acquired Celestial AI for up to ~$5.5B to pursue scale-up CPO; Hock Tan's current competitive advantage is SerDes (200G, only one on market). See [[CPO-platform-battle]] for the full comparative analysis and resolution signals.

**Tier 3 substrate addition (per `raw/research/CPO-for-AIDC-Infrastructure.md` 2026-05-26 + `raw/research/CPO-in-AIDC.md` 2026-05-27; in-place refresh per Vic instruction; not counted as separate session).** Tier 3 dual-source observable refines AVGO CPO positioning substantively beyond vault current scope (vault last_updated 2026-04-27):

- **TH6-Davisson 102.4T CPO switch shipping Oct 8, 2025** per Tier 3 sources — 16× 6.4T silicon-photonic optical engines + ~3.5W per 800G port (~4.4 pJ/bit) + uses TSMC COUPE + field-replaceable ELSFP laser modules (resolves prior serviceability objection); 4th-gen 400G/lane in development per Broadcom disclosures.
- **Meta Bailly production validation** (Amiralizadeh et al. paper at ECOC 2025): initially 1,049k 400G port-device-hours across 15 Bailly 51.2T CPO switches; extended at the ECOC talk to 15M 400G port-device-hours; "no failures or uncorrectable codewords (UCWs)"; one FEC bin >10 event in the initial 1,049k-hour run traced to a faulty fiber. Paper conclusion: *"The demonstrated lower bound mean time between failures (MTBFs) of optical links can readily support a 24K GPU AI cluster with >90 percent training efficiency without interconnect failures being the bottleneck."* 65% optics power savings vs pluggables (5.4W per 800G CPO vs 15W per 800G DSP pluggable).
- **NVIDIA Spectrum-X vs Broadcom TH6-Davisson power gap observation** — NVIDIA Spectrum-X Photonics 9W per 800G port (~11.3 pJ/bit) vs TH6-Davisson 3.5W per 800G port (~4.4 pJ/bit) per Tier 3 source = meaningful under-discussed gap at switch-CPO scope per NVIDIA Developer Blog + Broadcom disclosures.

Substantive observable trajectory shift since vault baseline 2026-04-27: prior vault Hock Tan "bright shiny objects" framing + AVGO Bailly silence at Tier 1 documented per [[CPO-platform-battle]] tier-silence pattern; Tier 3 sources document TH6-Davisson shipping with Meta production validation = substantive competitive trajectory advancement at AVGO CPO scope. Per CPO-for-AIDC-Infrastructure.md (2026-05-26) + CPO-in-AIDC.md (2026-05-27). *(The refresh this paragraph recommended was executed at S151.)*

**Q2 FY2026 call — the dismissal flips to ownership (Tier 2, June 3, 2026).** One quarter after "bright, shiny objects," Hock Tan's prepared remarks claim the category outright: "In **CPOs, which is co-packaged optics, 1.6Tb DSPs, CW and EML lasers, we are the de facto standard in the industry**" (AVGO Q2 FY2026 call). The scale-up position is unchanged — direct-attach copper on 200G/400G SerDes, now with "co-packaged copper" named alongside Ethernet/PCIe switches — but the scale-out optics stance moved from deferral rhetoric to an outright leadership claim, consistent with the Tier-3 TH6-Davisson shipping record above and with [[CPO-platform-battle]]'s "ships scale-out CPO while dismissing scale-up" reframe. Also disclosed: Tomahawk 6 shipping "for over a year"; **next-generation 200-terabit switch taping out this quarter**; Jericho 3/4 for scale-across. The Murphy ↔ Hock Tan scale-up disagreement stands (copper vs optical), but the "CPO is premature" half of AVGO's old framing has now been retired by AVGO itself. The Q2 10-Q still contains zero CPO mentions — the Tier-1/Tier-2 gap persists, with the call now on the *leading* side of it.

## Infrastructure software (VMware)

VMware Cloud Foundation (VCF) provides the second basis for AVGO's Layer 1 classification:

- Q1 FY2026: $6,796M revenue (+1% YoY), 93% gross margin, 78.3% operating margin (AVGO 10-Q Q1 FY2026)
- FY2025: $27,029M (42% of total), 93.0% implied GM, 76.8% operating margin (AVGO 10-K FY2025)
- VMware-specific revenue: +13% YoY; ARR sustaining 19% YoY growth; total contract value >$9.2B in Q1 (AVGO Q1 FY2026 call)
- Q2 guidance: ~$7.2B (+9% YoY) (AVGO Q1 FY2026 call)
- VMware acquisition: $86,290M total consideration; goodwill $54,206M allocated to software segment (AVGO 10-K FY2025)

Hock Tan frames VCF as thesis-relevant AI infrastructure: "VMware Cloud Foundation, VCF, is the essential software layer in data centers... As the permanent abstraction layer between AI software and physical chips, silicon, VCF cannot be disintermediated or replaced" and "the growth in generative and agentic AI will create the need for more VMware, not less" (AVGO Q1 FY2026 call).

The software segment provides Layer 1 economic ballast (93% GM) and platform stickiness but is not the thesis-relevant growth driver. The semiconductor business (+52% YoY) is AVGO's thesis-central segment; VMware (+1% YoY total, +13% VMware-specific) is a cost optimization story with expanding margins.

## Supply chain dependencies

**95% TSMC wafer dependency** — the most explicit foundry disclosure in the vault. Both the 10-K and 10-Q state: "approximately 95% of the wafers manufactured by our CMs were produced by TSMC" (AVGO 10-K FY2025; AVGO 10-Q Q1 FY2026). AVGO's wafer requirements "represent a meaningful portion of TSMC's total production capacity." No long-term capacity commitments; "substantially all of our manufacturing services are on a purchase order basis with no minimum quantities" (AVGO 10-K FY2025).

**Reciprocal non-naming on call.** AVGO never names [[TSM]] on the earnings call despite 95% dependency in filings. References are oblique: "leading-edge wafers" and "T-glass" (TSMC's advanced packaging substrate) referenced by name without attribution to TSMC (AVGO Q1 FY2026 call). The reciprocal non-naming pattern is now observed at Layer 1 ([[NVDA]], AVGO), Layer 2 ([[TSM]]), and Layer 3 ([[MRVL]]).

**Supply secured 2026-2028.** Hock Tan: "we have fully secured capacity of these components for 2026 through 2028" — leading-edge wafers, HBM, substrates, T-glass (AVGO Q1 FY2026 call). Charlie Kawwas: "We're probably the first one to secure that up to 2028 or beyond" (AVGO Q1 FY2026 call). The most aggressive supply security claim in the vault.

**InP wafer fabrication.** Breinigsville, Pennsylvania is "the sole source for the InP-based wafers used in our fibre optics products" (AVGO 10-K FY2025). AVGO fabricates VCSELs and InP lasers internally — a self-supply capability for fiber optic components. See [[InP-supply]] for the broader InP substrate supply chain dynamics.

**Taiwan revenue.** Crossed 10% for the first time at $6,451M in FY2025, up from "less than 10%" in both FY2024 and FY2023 (AVGO 10-K FY2025). Consistent with increased TSMC wafer purchases. The filing caveats that ship-to location is not necessarily end-customer location.

## Customer concentration

| Metric | Q1 FY2026 | FY2025 | FY2024 | FY2023 | Trend |
|--------|-----------|--------|--------|--------|-------|
| Single distributor | **42%** | 32% | 28% | 21% | Fastest acceleration in vault |
| Top 5 end customers | ~50% | ~40% | ~40% | — | Concentrating |
| Distributor share | 55% | 48% | 48% | — | Growing |

(AVGO 10-K FY2025; AVGO 10-Q Q1 FY2026)

The 42% single-distributor concentration is the highest in the vault, surpassing [[MRVL]]'s Distributor A at 37%. The distributor is unnamed; identified only as "one semiconductor solutions customer, which is a distributor" (AVGO 10-K FY2025). This is the traditional semiconductor business channel, not the AI/XPU franchise — the six XPU customers (named on the call) flow through different channels.

**Customer-owned tooling (COT).** Both Tier 1 filings flag COT as a risk: customers may "proceed with customer-owned tooling" and "develop these products themselves" (AVGO 10-K FY2025; AVGO 10-Q Q1 FY2026). On the call, Hock Tan dismissed: "Very modestly, I would say we are by far way out there, and we will not see competition in COT for many years to come" (AVGO Q1 FY2026 call). The 10-K also flags a new risk vector: "AI-driven design tools may lower traditional barriers to entry in the semiconductor industry" (AVGO 10-K FY2025). This is a Tier 1/Tier 2 framing gap — filings acknowledge the risk; the call dismisses it.

**AI rack leasing margin gap.** Both filings flag that leasing AI racks "will likely increase our operating margin but compress or lower future gross margin" and create "credit or customer default risks" (AVGO 10-K FY2025; AVGO 10-Q Q1 FY2026). On the call, when Tim Arcuri asked about rack margins, Hock Tan responded: "I hate to tell you that you must be a bit hallucinating" (AVGO Q1 FY2026 call). A second Tier 1/Tier 2 framing gap — filings flag margin compression, call dismisses it. See Source audit notes for pattern observation.

## Open questions

1. **Layer 1 straddling resolution.** Watch semiconductor segment margin trajectory, custom ASIC margin mix (rack leasing compresses gross margin per Tier 1 filings), and whether networking platform revenue becomes separable from custom ASIC revenue.
2. **$100B+ claim verification — tracking AHEAD at Q2.** Q2 AI semi revenue $10.8B +143% (beat outlook); FY2026 guided to $56B (+~180%); Q3 guided to $16B (+200%); >$30B of AI bookings in one quarter with visibility extended to 2028; FY2027 ">$100B" reiterated ("easily exceed… if anything, stronger"). Live remainder: whether the H2-doubles-H1 shape lands ($37B in two quarters), and whether the new CFO (Thuener) keeps the same guidance constructs.
3. **Anthropic independence — the derivative question SHARPENED at Q2.** The new April agreement gives Anthropic another **5 GW of "next-generation TPU-based compute" from 2027** — still TPU-architecture terminology, now in a formal multi-GW agreement, reinforcing the Google-derivative hypothesis rather than resolving it. Watch for any Anthropic-specific (non-TPU) silicon language.
4. **OpenAI execution risk.** First-gen XPU deploying 2027 at >1 GW, with 10 GW through 2029 (analyst-sourced). Sharp ramp from zero to gigawatt scale with no track record.
5. **COT timeline.** Hock Tan says "many years." AI design tools are lowering barriers (10-K). Watch for hyperscaler in-house silicon announcements.
6. **CPO timing — RESOLVED on the scale-out side at Q2 (the dismissal flipped).** Q1: "bright, shiny objects… not this year, maybe not next year." Q2: "in CPOs… we are the de facto standard in the industry." Live remainder is now only the **scale-up** question — copper DAC + co-packaged copper (AVGO) vs scale-up CPO (MRVL Photonic Fabric, commercial FY2028) — and when (if ever) CPO language reaches AVGO's Tier-1 filings.
7. **The $29B backstop / Apollo-Blackstone XPU platform (structure identified at Q2 call).** The investor-partner structure = the "AI XPU platform" with Apollo + Blackstone (>20 GW through 2028; $35B first tranche launching via Apollo) for frontier labs incl. Anthropic + OpenAI; the backstopped customer is **inferably Anthropic** (8-K-referenced TPU-compute deal; not disclosed in the 10-Q). Live remainder: confirmation of the customer identity; whether the $29B ceiling grows with later tranches; and the credit quality of pre-profit frontier labs as multi-billion-dollar lessees — the chips-only P&L claim ("No rack. It's all chips") holds only as long as the backstop is never called.

## Source audit notes

**10-K FY2025 (Tier 1, filed December 18, 2025).** Complete CPO/Bailly/silicon photonics absence. 95% TSMC dependency — most explicit foundry disclosure in the vault. 32% single-distributor concentration (21%→28%→32% three-year acceleration). XPU business described extensively in Item 1 but no AI semiconductor revenue breakout — AI figures exist only on the call (Tier 2). AI rack leasing appears repeatedly in Risk Factors as a new business model with explicit margin compression disclosure. Taiwan revenue crossed 10% for the first time ($6,451M). InP wafer fab at Breinigsville identified as sole source. No competitors named anywhere. VMware goodwill ($54,206M) and total goodwill ($97,801M) dominate the balance sheet. Key person risk flagged for Hock Tan specifically. Capex remarkably low at $623M (<1% of revenue) — capital-light model dependent on outsourced manufacturing.

**10-Q Q1 FY2026 (Tier 1, filed March 2026).** 42% single-distributor concentration — dramatic acceleration from 29% in Q1 FY2025, representing ~$8.1B of quarterly revenue through a single channel. 95% TSMC confirmed. Zero CPO mentions. Inventory +30% to $2,962M (WIP $1,544M) — production ramp signal. Customer-owned tooling explicitly flagged as risk. $45B remaining performance obligations (33% within 12 months, but 67% of contract liabilities have termination for convenience). $7,850M share repurchases in a single quarter — most aggressive quarterly buyback in the vault. New $10B authorization in March 2026. Revenue recognition: majority of products revenue recognized in Penang, Malaysia.

**Q1 FY2026 earnings call (Tier 2, March 4, 2026).** Most customer-specific AI call in the vault — four customers named (Google, Anthropic, Meta, OpenAI) with GW-scale figures, two unnamed, corrected from five to six during the call. $100B+ AI chip revenue claim with three formulations and escalating qualifier — most extreme forward-looking AI revenue statement in the industry. CPO dismissed as "bright, shiny objects" — most dismissive CPO commentary in the vault. Hock Tan's tone: combative and confident. Called Arcuri's margin question "hallucinating" — paralleling [[MRVL]]'s Murphy "Do you see me blinking?" response to competitive pressure questions. Both are CEO combativeness on structurally reasonable margin/competition questions; whether this reflects genuine confidence or defensive deflection is itself analytically significant. "Freudian slip" — said TPUs generically for all XPUs. [[TSM]] never named; "T-glass" and "leading-edge wafers" referenced. 11 analysts; zero questions about CPO/photonics, TSMC by name, VMware integration, or tariffs/China. Complete analyst disinterest in the software business despite VMware representing 35% of revenue.

**10-Q Q2 FY2026 (Tier 1, quarter ended May 3, 2026).** The headline disclosure is the $29B maximum-exposure backstop on a single customer's AI-rack lease obligations via an investor-partner structure — the most concrete quantification yet of the rack-leasing risk both prior filings flagged generically. Inventory nearly doubled in two quarters ($2,270M → $4,328M), the strongest production-ramp signal in the filing. Distributor concentration held at 42% (no further acceleration); ~95% TSMC dependency restated with new "TSMC has raised, and may in the future raise, their prices" language; zero CPO/silicon-photonics mentions — the Tier-1 silence pattern persists while the Tier-3 record shows TH6-Davisson CPO shipping since October 2025 (the cross-venue gap at its widest).

**Q2 FY2026 earnings call (Tier 2, June 3, 2026; full Quartr transcript).** The most consequential single sentence is the CPO reversal — "we are the de facto standard in the industry" — retiring the Q1 "bright, shiny objects" framing without acknowledgment; no analyst pressed the contradiction. The Apollo/Blackstone XPU-platform disclosure (>20 GW through 2028, $35B first tranche) supplies the structure behind the 10-Q's $29B backstop, and Hock Tan's correction of O'Malley's "backstopped by Broadcom chips" framing — while citing the Anthropic 8-K — is the closest the call comes to naming the backstopped customer. Tone: Hock Tan confident, expansive, no combativeness this quarter (no "hallucinating" moment); a smooth, scripted CFO handoff (Spears → Thuener); 11 analysts, and once again zero questions on the VMware integration or the 42% distributor concentration — the analyst-silence pattern holding at both spots. Hock Tan's enterprise-demand framing ("they are buying from the same source, these same few guys") is an unusually direct primary-source statement of frontier-lab demand concentration — both the bull case and the systemic-risk case for the whole AI supply chain in one quote.

<!-- LATEST-ALPHA:START -->
## ⚠️ Latest alpha — unverified, between-filings (as of 2026-06-13)

*Tier 3/4 discovery — NOT canonical. Recent 8-K / news to verify at the next primary source (Q3 FY2026: call Sept 2, 10-Q ~mid-Sept). Full detail + sources: [discovery note](../../raw/notes/latest-alpha/2026-06-13_AVGO_recent-developments.md). Items graduate into canon (or are pruned) at the next 10-Q/10-K ingest.*

- **Google Supply Assurance Agreement through up to 2031** — networking + components for Google's next-gen AI racks, a second agreement alongside the TPU LTA (8-K Apr 6) — Tier 1 · multi-year networking annuity not yet in canon. `[verify: revenue/RPO treatment at Q3 10-Q]`
- **Anthropic GW discrepancy** — 8-K (Apr 6): "~3.5 GW from 2027"; Q2 call (Jun 3): "another five gigawatts" — Tier 1 vs Tier 2 conflict · expansion or loose rounding? `[verify: restatement at Q3 venue / any 8-K amendment]`
- **The credit-risk sentence at primary** — Anthropic consumption "dependent on Anthropic's continued commercial success" + "financial partners" in discussion (8-K Apr 6) — Tier 1 · AVGO's own words for the vendor-financing risk the market repriced -12.6% on Jun 4. `[verify: $29B backstop ceiling movement at Q3 10-Q]`
- **Apollo/Blackstone tranche mechanics** (reports): $6B A1 + $24B A2, AVGO credit endorsement + residual-value guarantee + 100% shortfall compensation; SPV sells chips on default — Tier 4 · ≈ the 10-Q's $29B max exposure. `[verify: guarantee terms at any future filing]`
- **Google four-partner diversification** (reports): MediaTek inference TPU at 20–30% lower cost; Marvell/Intel in chain — Tier 4 · the mix risk behind Hock Tan's "diversity of sources" hedge. `[verify: customer language at Q3 call; MediaTek/MRVL announcements]`
- **Debt tender offers launched Jun 11** (8-K) + **say-on-pay ~33% against** (8-K Apr 21) — Tier 1 · balance-sheet management days after taking the backstop; comp dissent footnote. `[verify: tender size at next 10-Q debt footnote]`
- Related: [[GOOGL]] (LTA counterparty) · [[MRVL]] [[INTC]] (reported Google co-designers) · [[CPO-platform-battle]] (de-facto-standard claim still absent from Tier-1)

*Signal only (not weighted): -12.6% post-earnings (~$280B), a megacap-record single-day loss; Q3 AI guide $16B vs street $17.2B framing drove the headline reaction.*
<!-- LATEST-ALPHA:END -->

## Change log

- **2026-06-13 (S151 addendum — call ingested same day, completing the full Q2 FY2026 refresh):** Added the Q2 call layer: FY2026 AI guide $56B / Q3 AI $16B +200% / >$30B quarterly AI bookings with visibility to 2028; customer-program updates (Anthropic +5 GW next-gen TPU from 2027, Meta MTIA 3 GW, OpenAI 1.3 GW 2027, Google multi-generation LTA); the Apollo/Blackstone XPU platform identified as the structure behind the $29B backstop (customer inferably Anthropic); and the CPO stance reversal ("bright, shiny objects" → "de facto standard"). Open questions 2/3/6/7 updated to live remainders; CFO transition (Spears → Thuener) noted as a guidance-continuity watch item.
- **2026-06-13 (S151 — Q2 FY2026 partial refresh, Tier-1-only; first refresh executed under CLAUDE.md v9.9 page conventions):** Added Q2 FY2026 snapshot ($22.2B revenue +48%, semi segment +79%, EPS $1.91) + the NEW $29B AI-rack lease backstop disclosure; sharpened Open question 7 to its live remainder and updated Open question 2. Q2 earnings-call (June 3) transcript not yet staged at execution time — escalation trigger 5 noted; completed by the same-day addendum above. The 2026-05-27 "AVGO refresh recommended" flag is resolved by this refresh.
- **2026-05-27 (in-place refresh per Vic instruction; not counted as separate session — Tier 3 substrate addition per `CPO-for-AIDC-Infrastructure.md` 2026-05-26 + `CPO-in-AIDC.md` 2026-05-27):** Added Tier 3 dual-source substrate paragraph at CPO positioning subsection: TH6-Davisson 102.4T CPO switch shipping Oct 8 2025 + 16× 6.4T optical engines + ~3.5W/800G + field-replaceable ELSFP modules + 4th-gen 400G/lane in development; Meta Bailly production validation (15M 400G port-device-hours; "no failures or uncorrectable codewords"; supports 24K GPU cluster at >90% training efficiency per ECOC 2025); NVIDIA Spectrum-X 9W vs TH6-Davisson 3.5W per 800G power gap observation. **AVGO refresh recommended at next dedicated session candidate** — vault baseline (2026-04-27) substantively stale relative to TH6-Davisson commercial trajectory. last_updated 2026-04-27 → 2026-05-27.
- **2026-04-23:** Created from AVGO 10-K FY2025 (Tier 1), AVGO 10-Q Q1 FY2026 (Tier 1), AVGO Q1 FY2026 earnings call (Tier 2). Second Layer 1 company page (alongside [[NVDA]]). Three-source coverage from inception. Layer 1 with straddling tension flagged. Six XPU customers documented with GW-scale figures. $100B+ claim preserved with three escalating formulations. CPO dismissal ("bright, shiny objects") and Murphy ↔ Hock Tan scale-up interconnect disagreement documented. Two Tier 1/Tier 2 framing gaps identified (COT risk, rack leasing margins).
- **2026-04-23:** Session 12 audit execution (non-ingest). Added [[AI-demand-durability]] cross-reference.
- **2026-04-23:** Session 13 cross-reference. Added [[InP-supply]] link in InP wafer fabrication section.
- **2026-04-23:** Session 14 cross-reference. Added [[ALAB]] competitive context and [[hyperscaler-custom-ASIC]] cross-reference in XPU section.
- **2026-04-27 (Session 24 chokepoint research framework integration — Integration 1):** Added control-point distinction paragraph to Thesis role section per Tier 3 source `raw/research/photonics-chokepoint-table.md`. AVGO framed as second strongest strategic control-point name in vault. Control-point distinction is complementary to existing Layer 1/3 straddling tension documentation. Cross-reference structure includes four-company control-point thread + ANET plain-text reference. A6 framework-placement verification confirmed Layer 1 with Layer 1/3 straddling tension per `frameworks.md` v7. Confidence: HIGH.
- **2026-04-27 (Session 25):** Cross-referenced from new theme page [[chokepoint-investability-priorities]] Chokepoint 2 (Optical DSP / PHY power-performance), Chokepoint 7 (Switch ASIC / platform architecture), and Chokepoint 10 (Photonic advanced packaging / CPO integration) per A2 first canonical application. Per `frameworks.md` v8 Framework 2.6 codification: AVGO control point with bottleneck participation. No content edits.
- **2026-04-28 (Session 27 ANET wikilink completion):** Control-point thread cross-reference plain-text "Arista Networks (ANET — not currently a vault company page)" replaced with `[[ANET]]` wikilink. Five-company control-point thread now in-vault complete. AVGO single-merchant-silicon-vendor positioning relevant: [[ANET]] 10-K Risk Factors Summary disclosed "primarily reliant upon a predominant merchant silicon vendor" — almost certainly AVGO Tomahawk per ecosystem context (reciprocal-confirmation candidate pending future cross-validation). No content edits beyond wikilink completion.
- **2026-04-28 (Session 30 multi-source chokepoint synthesis):** Cross-referenced from new chokepoint page [[optical-dsp-phy-supply]] (second canonical multi-source-synthesis chokepoint page in vault history after [[InP-supply]] Session 13). AVGO Taurus 400G/lane optical DSP + Tomahawk switch ASIC integration + custom ASIC franchise + 95% TSMC dependency + Bailly CPO platform never-named pattern synthesized into chokepoint page per Session 10 ingest baseline + Session 24 Framework 2.6 codification. **A6 v8 (g) Phase 0 verification finding** documented on chokepoint page Source audit notes: kickoff "AVGO Sian3 3nm DSP" → canonical "AVGO Taurus" product naming used in synthesis; kickoff "AVGO Layer 1+3 / photonics_tier 2" → canonical Layer 1 / photonics_tier 3 frontmatter placement preserved. No content edits beyond cross-reference fan-out.
- **2026-04-30 (Session 32 multi-source chokepoint synthesis):** Cross-referenced from new chokepoint page [[cpo-integration]] (fourth canonical multi-source-synthesis chokepoint page in vault history; closes Tier 3 framework Chokepoint 10 (vault canonical Tier 3 Rank numbering) dedicated chokepoint page coverage gap). AVGO control-point with bottleneck-participation positioning at CPO chokepoint — Bailly platform never-named pattern + Hock Tan "We are the lead in CPOs" rhetorical + "bright shiny objects" dismissal + copper DAC scale-up advocacy via Tomahawk SerDes + scale-up vs scale-out architectural framing synthesized into chokepoint page per Session 10 ingest baseline + Session 24 Framework 2.6 codification. Murphy bifurcation thesis (MRVL Q4 FY2026 call) provides analytical framework rendering AVGO simultaneous CPO leadership claim + active dismissal internally consistent (scale-up copper advocacy + scale-out CPO optionality). Per Layer 1 timing divergence callout in [[chokepoint-investability-priorities]]: AVGO active dismissal preserved as one of three Layer 1 CPO timing scenarios without forced winner attribution. No content edits.
