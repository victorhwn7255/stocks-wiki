---
type: chokepoint
tickers: [TSM, NVDA, AEHR, ONTO, AVGO, MRVL]
last_updated: 2026-05-29
---

# TSMC CoWoS — Advanced Packaging Chokepoint

## What CoWoS is

CoWoS (Chip-on-Wafer-on-Substrate) is [[TSM]]'s advanced packaging platform used today for integrating high-bandwidth memory (HBM) stacking with leading-edge logic dies. It is the primary packaging technology for AI accelerators, enabling the multi-die configurations that GPUs, custom ASICs, and AI training/inference chips require.

CoWoS is a *current* bottleneck — well-documented allocation constraints exist today. This distinguishes it from TSMC's COUPE (silicon photonics engine), which is a *forward-looking* chokepoint still ramping to volume production. The wiki treats them as distinct chokepoints with different time horizons per the analytical framework.

## Current capacity status

Advanced packaging capacity is "very tight" as of Q1 2026 (TSM Q1 2026 call). TSMC is currently producing the largest reticle size CoWoS available in the market. The main supply approach for AI chip packaging today remains large-sized CoWoS combined with system-level and wafer-level integration (TSM Q1 2026 call).

Supply constraints in advanced packaging are expected to persist through at least 2027, paralleling front-end wafer capacity tightness (TSM Q1 2026 call). C.C. Wei confirmed that demand continues to increase and supply remains insufficient, with TSMC working to "speed it up" by pulling forward construction and equipment schedules.

**AVGO 2026-2028 HBM+CoWoS dual-chokepoint securing (Q1 FY2026):** Per Hock Tan + Charlie Kawwas Q1 FY2026 call, AVGO has secured both leading-edge wafers AND HBM through 2028 — *"We're probably the first one to secure that up to 2028 or beyond"* (Kawwas) — establishing AVGO 95% TSMC wafer + HBM dependency as the **single most concentrated cross-chokepoint dependency in vault** (per [[HBM-oligopoly]] S64 paired chokepoint analysis). [[TSEM]] S62 Q1 2026 call CEO Ellwanger separately disclosed TSMC purchases TSEM PIC content for CoWoS — see TSEM SiPh PDK foundry reference-design supplier complementarity section below.

### Quantification from Tier 1 filing

The TSM 20-F FY2025 provides the first quantitative context for advanced packaging, though no CoWoS-specific breakout exists:

- **Non-wafer revenue:** Packaging, testing, mask making, and other services = 14% of net revenue = NT$536,501M in FY2025 (TSM 20-F FY2025, Note 22a). This is the broadest available proxy for advanced packaging revenue; it includes testing and mask making alongside packaging and is not CoWoS-specific.
- **Backend fabs:** 7 advanced backend fabs as of the filing date (TSM 20-F FY2025).
- **Capex allocation:** FY2025 capex was allocated in part to "expanding capacity for specialty technologies and advanced packaging, including building/facility expansion for Fab 23 and Fab 24" (TSM 20-F FY2025, p.33). This confirms advanced packaging has its own identified capex category, not merely embedded in front-end wafer spending.
- **No material contracts:** "TSMC is not currently a party to any material contract, other than contracts entered into in the ordinary course of business" (TSM 20-F FY2025, p.61). Even the largest advanced packaging customer relationships are classified as ordinary course — no single customer supply agreement rises to SEC materiality.
- **Temporary receipts from customers:** NT$189,858M as of December 2025, down 35% from NT$291,102M in December 2024 (TSM 20-F FY2025, Note 22c). These are advance capacity reservation payments. The decline could reflect increased capacity availability, changing reservation terms, or balance sheet reclassification — flagged as an open question in [[TSM]].

## TSEM SiPh PDK foundry reference-design supplier complementarity (S62 NEW analytical product)

**First explicit primary-source documentation of cross-vault Layer 2 foundry-tier reference-design supplier complementarity pattern at CoWoS scope** per [[TSEM]] S62 canonical placement (2026-05-14). CEO Russell Ellwanger Q1 2026 call response to Krish Sankar (TD Cowen) on TSMC COUPE competitive positioning — exact CEO wording preserved per Section 3.3 rhetorical claims convention:

> *"I think there's nobody that can compete with TSMC with what they're doing on the extreme deep digital content...TSMC wouldn't be buying our PIC for their CoWoS if our PIC was much superior to everything else"* — followed by clarification: *"we become the reference design for the major integrators, and that would be part of what they'd be using with TSMC."*

**Cross-vault analytical implication.** TSEM occupies wafer-tier SiPh PDK foundry position (Layer 2 / photonics_tier 2 per S62; PH18 200mm + PH45 300mm SiPho platforms; 1.6Tb/s + 3.2Tb/s development; CPO investment scope); provides PIC content into TSMC CoWoS at advanced packaging integration scope. **Complementarity, not pure competition.** Refines cross-vault chokepoint analysis at [[advanced-optical-packaging]] S31 + [[cpo-integration]] S32 baseline framing — TSEM is reference-design supplier across "major integrators" including TSMC at wafer-tier SiPh PDK scope. **First explicit primary-source documentation of cross-vault Layer 2 foundry-tier reference-design supplier complementarity pattern in vault history.**

**Bilateral verification candidate at TSM-side pending Q2 2026 refresh.** Does TSM 20-F FY2026 (expected ~April 2027) or Q2 FY2026 earnings call (mid-July 2026 reporting timeline expected) reference TSEM PIC content at CoWoS scope? Pre-registered in Open questions section below.

**Methodology codification candidate (Tranche 2C):** Cross-vault Layer 2 foundry-tier reference-design supplier complementarity methodology formalization at frameworks.md.

## Demand drivers

CoWoS demand is driven by the same forces driving TSMC's overall leading-edge business, concentrated in HPC/AI applications (TSM Q1 2026 call):

- AI accelerator packaging (GPU, custom ASIC, HBM integration)
- HBM base die stacking
- Larger die sizes from AI customers pushing reticle size limits
- The shift from generative AI to agentic AI driving more computation and more chips per system (see [[AI-demand-durability]])

AI customers are developing "much larger reticle size chips" and some are considering substrate-based packaging (EMIB) as an alternative for circular larger chip designs (TSM Q1 2026 call, Morgan Stanley analyst question). This demand for ever-larger packages reinforces CoWoS's chokepoint status — the technical difficulty scales with die size.

### Customer-side demand pressure (NVDA perspective)

The [[NVDA]] Q4 FY2026 call provides customer-side evidence that directly reinforces CoWoS demand intensity:

**Dielet avoidance philosophy:** Jensen Huang stated that NVIDIA uses dielets "only when we absolutely have no choice" because each dielet crossing adds interfaces, latency, and power (NVDA Q4 FY2026 call). The Grace Blackwell and Rubin architectures use "two giant reticle limited dies" abutted together to minimize interface crossings. This architectural preference for monolithic or near-monolithic designs means each GPU generation pushes toward reticle limits, requiring correspondingly larger CoWoS interposers.

**Supply tightness confirmed from customer side:** Colette Kress confirmed NVDA expects "tightness in the supply for our advanced architectures to persist" and that purchase commitments have been extended "further out in time than usual" into calendar 2027 (NVDA Q4 FY2026 call). This corroborates TSM's supply-side constraint commentary from the same period.

**Blackwell deployment scale:** Nearly 9 gigawatts of Grace Blackwell NVL72 infrastructure are deployed (NVDA Q4 FY2026 call), and Blackwell systems accounted for roughly two-thirds of Q4 data center revenue. With Vera Rubin production beginning H2 2026 alongside continued Blackwell and Blackwell Ultra sales, total advanced packaging demand will compound rather than substitute.

The combination of NVDA's architecture choices (reticle-limited dies → larger CoWoS packages) and deployment scale (9 GW and growing) means CoWoS demand pressure is structural and intensifying, not merely a near-term supply-demand imbalance.

**NVDA GTC March 16, 2026 expanded context — Spectrum-X CPO production + Kyber CPO scale-up.** Jensen disclosed at GTC: Spectrum-X CPO switch *"in full production"*; COUP/COUPE packaging co-developed with TSMC (*"We invented the process technology with TSMC. We're the only one in production with it today"* — Jensen, attributed per rhetorical claims convention); Spectrum-6 as *"world's first co-packaged optical"* switch; Kyber CPO scale-up. NVDA platform integration absorbs photonics + power infrastructure layers simultaneously through Vera Rubin chip generation — see [[nvidia-supply-chain-commitments]] S53. **CPO production status broke previous tier-silence pattern at NVDA primary** per [[CPO-platform-battle]] theme observation; production-confirmed adoption shifts CPO chokepoint analysis from forward-looking to current-bottleneck-adjacent.

**NVDA $2B equity-plus-purchase materialization at LITE+COHR (S50 Q3 FY2026; 2026-05-10 refresh).** Per [[LITE]] + [[COHR]] paired refresh — NVDA $2.02B cash injection at LITE (CFO Wajid Ali Q3 call) + NVDA $2B equity stake + **multibillion-dollar multi-year CPO supply agreement extending through end of decade** at COHR (CEO Anderson Q3 call). **Sherman TX 6-inch InP CW laser production explicitly tied to NVDA partnership** per S50. Capital-offset-for-supply-assurance modality — NVDA pre-funding photonics laser supplier capacity expansion alignment with CoWoS demand trajectory. Cross-vault [[datacenter-laser-supply]] chokepoint refresh propagation candidate post-S50. **First reciprocal-confirmation A1 mode materialization at NVDA architect-customer commitment scope** per [[nvidia-supply-chain-commitments]] S53.

**NVDA Q1 FY2027 customer-side demand expansion (S84 cross-vault propagation post-S81 refresh).** Single-customer GPU count milestones disclosed at scale not previously substantiated at NVDA primary — all advanced-packaging-dependent:
- **Microsoft Fairwater** — "world's most powerful AI data center, now live, ahead of schedule, powered by hundreds of thousands of Blackwell GPUs" (Colette Kress Q1 FY2027)
- **AWS** — "Starting this year, AWS will add over 1 million Blackwell and Rubin GPUs" (Colette)
- **Google A5X bare-metal instances** — "can support up to 960,000 Rubin GPUs across multiple sites" (Colette)

**Vera Rubin Q3 2026 production trajectory + 7-chip/5-rack-scale platform CoWoS demand pull.** Per Colette: "on track to commence production shipments of Vera Rubin in the second half of this year, starting in Q3. By integrating seven purpose-built chips across five accelerated racks, Vera Rubin will deliver up to 35x higher inference throughput and up to 10x greater AI factory revenue compared with Blackwell." Each Vera Rubin platform requires advanced packaging at scale — Vera CPU + Rubin GPU + NVLink switches + ConnectX-9 + SuperNIC + BlueField-4 + Spectrum-6 = 7 purpose-built chips per platform. Multi-customer GPU count milestones translate directly to CoWoS allocation demand at the multi-year scale (Vera Rubin ramp Q3 → Q4 → Q1 FY2028 "very big" per Colette Q&A).

**$145B total supply commitment (Q1 FY2027).** Per Colette: "we increased total supply, inclusive of inventory, purchase commitments, and prepaids to $145 billion." Material expansion from Q4 FY2026 baseline. Purchase commitments extend into calendar 2027 and beyond per Q4 FY2026 baseline preserved at Q1 FY2027.

**TSMC reciprocal non-naming reverted at Q1 FY2027 earnings call.** NVDA Q1 FY2027 (May 20, 2026) preserved non-naming of TSMC across 16 pages despite Vera Rubin Q3 2026 production trajectory being directly TSMC-dependent for advanced packaging. The GTC March 2026 venue-specific break — where Jensen explicitly named TSMC for COUP packaging — did NOT propagate to the earnings call venue. Pattern verdict: venue-specific naming, with GTC + product launches as the chosen venue for TSMC reciprocal naming; earnings calls preserve silence at supply chain scope. Consistent with broader NVDA-side reciprocal non-naming asymmetry per [[NVDA-platform-integration]] S82 (hyperscaler-side naming substantively broken at Q1 FY2027; supply chain + CPU competitor sides preserved). COUP co-development modality preserved per [[NVDA-platform-integration]] S82 7-modality framework documentation — cross-reference rather than re-document here.

### Equipment-tier demand signals

Two equipment-tier companies provide upstream confirmation of CoWoS demand intensity:

**[[AEHR]]** explicitly names "CoWoS" as an application for its FOX-NP burn-in systems, positioning Known-Good Die (KGD) testing as economically critical for multi-die advanced packaging — a defective die in a CoWoS package wastes the entire package (AEHR Q3 FY2026 call). AEHR's bookings surged 6x QoQ to $50.9M in Q3 FY2026, with advanced packaging test driving the semiconductor segment's growth from 3% to 25% of revenue (AEHR 10-K FY2025; AEHR 10-Q Q3 FY2026).

**[[ONTO]]** derives substantial revenue from TSMC — its largest named customer at 21% of Q3 FY2025 revenue (ONTO 10-Q Q3 FY2025). ONTO's advanced packaging and HBM metrology revenue grew >30% YoY (ONTO Q4 FY2025 call), and its $240M+ VPA pipeline is concentrated in HBM measurement. As the metrology supplier to the CoWoS chokepoint holder, ONTO's demand trajectory is a leading indicator: metrology tool orders precede wafer starts.

**ONTO S54 Q1 2026 refresh propagation (2026-05-11):** Record $292M revenue (+9.6% sequential); FY2026 RAISED outlook >30% revenue growth / >$1.3B; **advanced packaging +50% growth** (raised from prior >30%); **advanced nodes +25% growth** (ahead of WFE low-20%s). **Dragonfly G5 commercial ramp at HBM 2D + 3D metrology wins** — Q1 handful → Q2/Q3/Q4 doubling each quarter; qualified at leading 2.5D logic customer; 15-application pipeline across 10 customers. **Atlas G6 OCD metrology head-to-head competitive wins at multiple key accounts for next-gen logic nodes** + GAA transistor + HBM DRAM scope. **Rigaku 27% strategic stake $710M H2 2026 close from Carlyle Group** — 75-year X-ray technology partnership; hybrid metrology solutions roadmap; X-ray adds penetration + precision for exotic materials + 3D structures at transistor + chiplet scale relevant to HBM 16-die stack metrology requirements. **TSMC + Samsung + SK Hynix all named customers via XBRL** (anonymous Customer A/B/C in body) — first explicit named-customer disclosure of TSMC AND HBM oligopoly suppliers at vault Tier 1 filing scope. ONTO is the **strongest cross-vault leading-indicator** for CoWoS + HBM dual-chokepoint capacity trajectory.

Equipment orders are a structural leading indicator for packaging capacity deployment. Both companies' demand signals are consistent with the CoWoS constraint intensifying rather than easing.

### Custom ASIC designer demand pressure (AVGO and MRVL perspectives)

Two custom ASIC designers provide demand-side corroboration for the CoWoS chokepoint from the perspective of TSMC's largest fabless customers:

**[[AVGO]] — 95% explicit TSMC dependency.** "Approximately 95% of the wafers manufactured by our CMs were produced by TSMC" (AVGO 10-K FY2025) — the most explicit foundry dependency disclosure in the vault. AVGO's wafer requirements "represent a meaningful portion of TSMC's total production capacity" (AVGO 10-K FY2025). Supply chain "fully secured for 2026 through 2028" per Hock Tan, including leading-edge wafers, HBM, substrates, and "T-glass" — TSMC's advanced packaging substrate referenced by name without attribution to TSMC (AVGO Q1 FY2026 call). Charlie Kawwas: "We're probably the first one to secure that up to 2028 or beyond" (AVGO Q1 FY2026 call). With AI semiconductor revenue at $8.4B in Q1 FY2026 (+106% YoY) and six custom XPU customers approaching ~10 GW aggregate deployment in 2027, AVGO represents a substantial and accelerating demand driver for CoWoS capacity. Taiwan ship-to revenue crossed 10% for the first time at $6,451M in FY2025 (AVGO 10-K FY2025).

**[[MRVL]] — Taiwan surge as geographic proxy.** Taiwan ship-to revenue surged from $161.9M (3%) in FY2024 to $1,657.3M (20%) in FY2026 — 10x in two years — strongly suggesting TSMC advanced packaging dependency as custom ASICs ship to Taiwan for CoWoS/InFo integration (MRVL 10-K FY2026). COO Koopmans named supply binding constraints explicitly: "advanced wave fabrication, advanced packaging, large body substrates" (MRVL Q4 FY2026 call).

**MRVL Q1 FY2027 — CoWoS named as the scale-up integration substrate (NEW; S102 propagation, S110).** Beyond the geographic proxy, MRVL's Q1 FY2027 call named CoWoS explicitly: its Celestial **MRM-based (micro-ring-modulator) scale-up is "progressing in close collaboration with TSMC on CoWoS"** (MRVL Q1 FY2027 call). This is a new *qualitative, CoWoS-specific* demand vector — MRVL's photonic-fabric scale-up architecture is being co-developed on CoWoS as the integration substrate, not just inferred from Taiwan ship-to. Demand-side reinforcement (not a capacity-constraint change).

Both companies corroborate the CoWoS chokepoint from the demand side: AVGO explicitly, MRVL through geographic and supply language. Together with the NVDA customer-side evidence (dielet avoidance driving larger CoWoS packages) and the equipment-tier signals ([[AEHR]], [[ONTO]]), the demand case for CoWoS constraint intensification is now supported from four distinct vantage points in the supply chain.

**HBM-CoWoS dual-chokepoint securing pattern post-S64 [[HBM-oligopoly]] canonical creation.** AVGO 95% TSMC + HBM secured through 2028 = **single most concentrated cross-chokepoint dependency in vault** (HBM oligopoly supplier-tier per [[HBM-oligopoly]] S64 + CoWoS integration-tier this chokepoint). AVGO Bailly CPO + Tomahawk custom ASIC product line HBM bandwidth integration dynamics drive simultaneous demand on both upstream HBM oligopoly capacity AND CoWoS advanced packaging integration capacity. Six AVGO custom XPU customers approaching ~10 GW aggregate deployment 2027 = substantial dual-chokepoint allocation footprint.

## HBM integration tier paired chokepoint (S64 NEW analytical product)

**HBM-CoWoS upstream-vs-integration tier pair formalized per [[HBM-oligopoly]] S64 canonical creation.** Sequential chokepoint pairing — **HBM oligopoly chokepoint = upstream supplier-tier (SK Hynix 50-62% + Samsung 17-35% + Micron 11-21%; all non-vault); TSMC CoWoS chokepoint (this page) = integration-tier for HBM base die stacking** at AI accelerator packaging.

**New chokepoint pair structural type — upstream-vs-integration tier pair** — distinct from [[transformer-supply]] + [[BTM-grid-bypass-workaround]] constraint-source-vs-workaround pair (S63 paired-chokepoint methodology). Tranche 2C methodology codification candidate.

**Sequential causation pattern at primary-source verification:**

```
HBM oligopoly chokepoint (upstream supplier-tier)
  → 3-supplier global concentration (SK Hynix 50-62% + Samsung 17-35% + Micron 11-21%)
    → HBM3E → HBM4 generation transition (12 → 16 dies-per-stack; 33% more DRAM per AI accelerator)
      → SK Hynix ~90% NVDA HBM primary supplier concentration (consumer-side)
        → TSMC CoWoS integration-tier (this chokepoint) = HBM base die stacking advanced packaging
          → AVGO 95% TSMC + HBM secured 2026-2028 (dual-chokepoint securing pattern)
            → NVDA Vera Rubin HBM4 16-die stack requirements drive CoWoS allocation tension
```

**Cross-domain 4-framework bridge substantiated.** HBM-CoWoS paired chokepoint dynamics span F2 Layer (cross-Layer 1-4 vault canonical substantiation) + F5 Photonics adjacent (at HBM optical I/O future integration scope) + **F6 Memory PRIMARY** (HBM oligopoly) + F8 Equipment adjacent (metrology/inspection/burn-in subscale at ONTO + COHU + AEHR). First explicit 4-framework cross-domain bridge in vault canonical scope.

**HBM4 ramp dynamics + "3-to-1 rule" capacity displacement at CoWoS scope.** Per `_thesis.md` Rank 1 Memory: HBM consumed 23% DRAM wafers Q4 2025; HBM3E ~$300/stack → HBM4 ~$500/stack pricing; 16-Hi HBM stacks requested by NVDA Q4 2026 — *"formidable"* technical challenge. Higher HBM density → higher thermal load at CoWoS package + tighter base die stacking precision requirements; reinforces TSMC mechanical stress + warpage + thermal limitation challenges per Technical challenges section above.

## Expansion plans

TSMC is expanding CoWoS capacity through two channels (TSM Q1 2026 call):

1. **Internal capacity expansion:** Building additional advanced packaging capacity alongside front-end fab expansions. The $52-56B 2026 capex budget includes advanced packaging investment (not broken out separately).

2. **OSAT partnerships:** Working with outsourced semiconductor assembly and test (OSAT) partners to increase total available advanced packaging capacity. C.C. Wei: "we certainly have to work with our OSAT partners. We hope that we can increase the capacity to support our customers" (TSM Q1 2026 call).

The willingness to expand through OSAT partners suggests that demand is sufficiently beyond TSMC's internal capacity that maintaining full vertical control is less important than meeting customer needs. This is a capacity signal — when the chokepoint holder opens to partners, the constraint is genuine.

## Technical challenges and evolution

C.C. Wei identified the primary technical challenges in advanced packaging (TSM Q1 2026 call):

- **Mechanical stress** — the dominant challenge as die sizes increase
- **Warpage** — related to mechanical stress at larger reticle sizes
- **Thermal limitations** — heat dissipation in tightly integrated multi-die packages
- **Electrical engineering challenges (impedance matching)** — described as "a very tough challenge"

Management framed technical difficulty as competitive advantage: "A good challenge, and we like it, the harder the better, because of TSMC's strength in technical engineering" (TSM Q1 2026 call). This framing is consistent with a deepening moat — the harder the problems, the fewer competitors can solve them, and TSMC has accumulated "a lot of experience already today because we have supply most of the leading edge and in packaging area" (TSM Q1 2026 call).

**Evolution beyond current CoWoS:**

- **CoPoS** (Chip-on-Panel-on-Substrate): Pilot line under construction, production expected "a couple of years later" (TSM Q1 2026 call). Positioned as a next-generation approach for addressing larger reticle demands. CoPoS is distinct from both current CoWoS and from TSMC's COUPE silicon photonics engine.
- **SoIC** (System-on-Integrated-Chips): Also mentioned as part of TSMC's advanced packaging technology roadmap alongside CoPoS (TSM Q1 2026 call). No timeline specifics provided in this call.
- **COUP/COUPE** (compact universal photonic engine): Jensen disclosed at GTC March 16, 2026 that NVDA and TSMC co-developed this packaging technology for silicon photonics integration: "We invented the process technology with TSMC. We're the only one in production with it today" (Jensen, NVDA GTC March 16, 2026 — attributed per rhetorical claims convention). COUP is the first primary-source COUP/COUPE reference from any vault company; TSMC's own sources (Q1 2026 call, 20-F FY2025) contain zero COUPE mentions. Whether COUP and COUPE are the same technology or naming variants is an open question — Jensen used "COUP"; frameworks.md uses "COUPE." See [[CPO-platform-battle]] for the full CPO platform analysis.

## Competitive alternatives

The primary competitive alternative raised in this call was Intel's **EMIB** (Embedded Multi-die Interconnect Bridge), noted by a Morgan Stanley analyst as substrate-based and potentially "more suitable for circular larger size chip design" (TSM Q1 2026 call).

C.C. Wei's response acknowledged the competition: "we understand that our competitors also offer very attractive technology. But we work on that. So our customers can have more choices and then we can do more business with our customers" (TSM Q1 2026 call). This is notably non-dismissive — TSMC acknowledges EMIB as a real alternative while expressing confidence in its own roadmap.

See [[foundry-competition]] for broader competitive dynamics.

## Cross-vault NVIDIA partnership pattern at CoWoS scope

**NVDA-TSM A1 counterparty-attribution-only foundry-customer modality per [[nvidia-supply-chain-commitments]] S53.** NVDA is implicitly TSMC's most significant HPC/AI customer per [[TSM]] customer concentration disclosure (Customer A 19% FY2025 per 20-F Note 38 — anonymized per SEC convention). Reciprocal non-naming pattern preserved at earnings call scope but **broken at GTC venue** — NVDA named TSMC explicitly at GTC March 16, 2026 per COUP/COUPE co-development disclosure (*"We invented the process technology with TSMC"* — Jensen).

**Cross-vault NVIDIA partnership pattern post-S110 = 5 Tier 1 + 7 Tier 2 substantiating sources** per [[nvidia-supply-chain-commitments]] S53 living document scaffolding (roster refreshed S110 for the MRVL equity stake):
- **Tier 1 reciprocal-confirmation:** [[LITE]] $2B equity + [[COHR]] $2B equity + multibillion-dollar multiyear CPO supply + [[ETN]] Beam Rubin DSX platform + [[VRT]] Strategic Partnership + EcoDataCenter Sweden Vera Rubin deployment + **[[MRVL]] $2.0B NVIDIA convertible-preferred (Mar 31 2026; [[NVDA-platform-integration]] Mode 4 — equity + NVLink-Fusion partnership + merchant-silicon competitor overlap; equity Tier-1-confirmed, partnership scope MRVL-side pending NVDA bilateral)** — directly relevant here because MRVL's MRM scale-up co-develops on TSMC CoWoS (see Custom ASIC designer demand subsection)
- **Tier 2 cross-vault context:** [[FN]] NVIDIA 27.6% top customer + [[ALAB]] NVLink Fusion ecosystem partner + [[CSCO]] enterprise networking partnership + [[ANET]] networking interoperation + **[[TSM]] foundry-customer (this chokepoint)** + [[AVGO]] peer-competitor framing + [[TSEM]] reciprocal-confirmation-LIMITED at NVIDIA development partner scope

**TSM-side bilateral verification deferred per TSM Q2 2026 release pending** (mid-July 2026 reporting timeline expected). Future TSM refresh would surface: Vera Rubin deployment trajectory at TSM customer concentration scope; COUP/COUPE commercialization timeline + capacity allocation; HBM-CoWoS dual-chokepoint customer allocation patterns. Pre-registered in Open questions section below.

## Thesis implications

CoWoS capacity tightness directly supports the thesis that value concentrates at structural chokepoints. Evidence from this call:

1. **The chokepoint is active and intensifying.** Capacity is "very tight," demand continues to increase, and supply-demand balance is not expected before 2027 at the earliest. This is not a theoretical future constraint — it is a present reality affecting every AI chip customer.

2. **Technical difficulty reinforces the moat.** Mechanical stress, warpage, and thermal challenges at larger die sizes are getting harder, not easier, as AI chips grow. TSMC's accumulated experience in solving these problems is a durable competitive advantage. Competitors face a moving target.

3. **The OSAT expansion signal.** TSMC opening advanced packaging to OSAT partners is evidence of genuine constraint severity. It also implies the chokepoint may gradually widen if OSAT capacity scales — a dynamic to monitor.

4. **No evidence of the disconfirming signal.** `_thesis.md` identifies "TSMC's packaging advantage narrows" as a thesis risk. This call provides no evidence of narrowing. Intel's EMIB is acknowledged but not treated as a near-term competitive threat to CoWoS's market position. Samsung was not mentioned in the advanced packaging context.

5. **CoWoS pricing remains opaque.** No advanced packaging pricing was discussed. All pricing questions focused on wafer pricing. Whether TSMC is capturing chokepoint-appropriate pricing on CoWoS remains an open question for future sources.

6. **HBM-CoWoS paired chokepoint completion strengthens cross-domain bridge thesis.** Post-S64 [[HBM-oligopoly]] canonical creation, the HBM-CoWoS upstream-vs-integration tier pair operationalizes Memory framework F6 → Foundry-Packaging tier dependency chain. AVGO 95% TSMC + HBM secured 2026-2028 = single most concentrated cross-chokepoint dependency in vault. Investment positioning at single-chokepoint exposure misses dependency-chain dynamics; dual-chokepoint exposure (HBM via [[HBM-oligopoly]] + CoWoS via this page) captures structural pricing power that single-chokepoint exposure cannot.

7. **TSEM reference-design supplier complementarity strengthens Layer 2 foundry-tier moat framing.** TSMC purchases TSEM PIC content for CoWoS at integrator scope (S62 CEO Ellwanger disclosure). Complementarity, not pure competition. **Refines TSMC's chokepoint position from sole-foundry-integration toward integrator-of-specialty-foundry-reference-designs at SiPh PDK foundry scope** — TSMC's moat extends beyond own advanced packaging to integration of best-in-class specialty foundry inputs. Strengthens rather than narrows the chokepoint thesis per `_thesis.md` "TSMC's packaging advantage narrows" disconfirming signal test.

## Open questions

1. **TSM Q2 2026 refresh propagation (highest priority).** TSM S3 baseline ~60 sessions stale at S65 refresh; **Q2 FY2026 release expected mid-July 2026 reporting timeline**. TSM refresh would substantively close cumulative refresh debt accumulated since S3 (S17 + S18 + S19 + S20 + S22 cross-validation cycles) + propagate accumulated cross-vault analytical product (TSEM reference-design complementarity + HBM-CoWoS paired chokepoint + NVDA $2B equity + GTC March 2026 + ONTO S54 metrology refresh). **Substantive strengthening trigger for this chokepoint page.**

2. **TSEM reference-design supplier complementarity bilateral verification at TSM-side.** Does TSM Q2 FY2026 call or future 20-F reference TSEM PIC content at CoWoS scope? S62 [[TSEM]] CEO Ellwanger disclosure establishes TSEM-side; TSM-side bilateral verification deferred per non-vault supplier-side mode + TSM Q2 2026 release pending.

3. **COUP/COUPE naming variant resolution.** Jensen used "COUP" at GTC March 2026; `frameworks.md` uses "COUPE"; TSEM Q1 2026 call references TSMC COUPE indirectly. Whether COUP and COUPE are the same technology or naming variants is unresolved. Resolution pending future cross-vault verification at TSM Q2 2026 + future NVDA refresh.

4. **TSMC CoWoS capacity allocation by customer split.** AVGO 95% TSMC + HBM secured 2026-2028 + NVDA dielet-avoidance reticle-limited dies + MRVL Taiwan ship-to 3% → 20% surge = three substantial customer demand vantages but customer-specific CoWoS allocation split NOT disclosed at TSM primary. NVDA Customer A 19% concentration (TSM 20-F FY2025 Note 38; anonymized per SEC convention) is closest proxy. Future TSM refresh propagation candidate.

5. **CoWoS pricing power realization.** Whether TSMC captures chokepoint-appropriate pricing on CoWoS remains opaque. Tier 3 source `raw/research/AI-power-energy-bottleneck-research-report.md` analogy from transformer-OEM scope ("backlog quality is underestimated... 15-25% multi-year price/cost expansion") raises whether CoWoS backlog quality is similarly underestimated. TSM Q1 2026 66.2% gross margin context (exceeds Layer 2 framework 40-60% range) suggests CoWoS pricing may be chokepoint-appropriate; explicit CoWoS-specific margin disclosure absent.

6. **COUP/CoPoS commercial ramp trajectory.** CoPoS pilot line under construction; production expected "a couple of years later" per Q1 2026 call. COUP/COUPE production status per NVDA GTC March 2026; commercial scale trajectory pending. Future TSM refresh + NVDA Q1 fiscal 2027 refresh propagation candidate.

7. **HBM-CoWoS dual-chokepoint dynamics.** Per S64 [[HBM-oligopoly]] paired chokepoint formalization: how does HBM4 16-die stack qualification trajectory interact with CoWoS allocation? AVGO 2026-2028 dual securing pattern suggests architect-customer side perceives dual-chokepoint risk; whether single-chokepoint vs dual-chokepoint allocation logic dominates at TSMC capacity planning side opaque. Future TSM refresh propagation candidate.

8. **Intel EMIB competitive evolution.** TSMC acknowledged EMIB as real alternative (Morgan Stanley Q1 2026 question) — not dismissive framing. EMIB substrate-based "more suitable for circular larger size chip design." Intel Foundry execution trajectory + EMIB customer adoption + AVGO/NVDA/MRVL dual-sourcing dynamics pre-registered for cross-vault [[foundry-competition]] theme refresh. TSMC's packaging advantage narrows disconfirming signal test candidate.

9. **OSAT capacity scaling impact on chokepoint moderation.** TSMC working with OSAT partners (ASE Technology + Amkor Technology) to expand advanced packaging capacity. ASE + Amkor non-vault per [[advanced-optical-packaging]] S31 Tier C candidate framing. OSAT-tier capacity scaling could gradually moderate chokepoint severity if expansion materializes; alternatively could perpetuate chokepoint via qualification cycle dynamics. Future cross-vault refresh propagation candidate at OSAT primary-source ingest (ASE Taiwanese ADR or Amkor US-listed canonical creation).

10. **Adjacent chokepoint refresh propagation trigger.** [[cpo-integration]] S32 baseline ~17 sessions stale + [[datacenter-laser-supply]] S27 baseline ~18 sessions stale + [[advanced-optical-packaging]] S31 baseline ~17 sessions stale — all candidates for refresh propagation post-S65 TSMC-CoWoS refresh + S62 [[TSEM]] + S64 [[HBM-oligopoly]] accumulated cross-vault analytical product. Sequential refresh propagation per S51 [[HALEU-fuel-chokepoint]] precedent cadence.

## Cross-references

- **[[HBM-oligopoly]]** (S64) — **Paired chokepoint upstream-vs-integration tier pair.** HBM oligopoly = upstream supplier-tier (SK Hynix + Samsung + Micron); TSMC-CoWoS (this page) = integration-tier for HBM base die stacking. First explicit upstream-vs-integration tier paired chokepoint structural type. See HBM integration tier paired chokepoint section above.
- **[[TSEM]]** (S62) — SiPh PDK foundry reference-design supplier complementarity at CoWoS scope; PH18 + PH45 SiPh PDK foundry; PIC content reference designs into TSMC CoWoS at major integrator scope per CEO Ellwanger Q1 2026 call.
- **[[nvidia-supply-chain-commitments]]** (S53) — Cross-vault NVIDIA partnership pattern relationship page; TSM Tier 2 cross-vault context entry (foundry-customer modality counterparty-attribution-only).
- **[[cpo-integration]]** (S32) — CPO integration mechanics chokepoint; COUP/COUPE foundry-tier integration cross-references this page; 9 vault company integration positioning.
- **[[advanced-optical-packaging]]** (S31) — Advanced optical packaging chokepoint at OSAT + finished-module scope; structurally distinct from CoWoS foundry-tier; ASE + Amkor OSAT-tier participants overlapping.
- **[[InP-supply]]** (S33) — InP substrate + epitaxial supply chokepoint upstream of HBM ↔ CoWoS integration scope.
- **[[transformer-supply]]** (S63) — Energy/Power chokepoint pair complement; distinct domain at distribution-side power infrastructure constraint.
- **[[datacenter-photonics-supply-chain]]** (S19) — Section 2.6 (Photonic foundries) for the COUPE vault-conflict reconciliation; Section 2.7 (Assembly / packaging / testing) for cross-layer context; Bucket C in the investability framing covers the foundry-packaging-connectivity layer.
- **[[CPO-platform-battle]]** (S22) — CPO platform-strategy archetype theme; NVDA Spectrum-X CPO production + Bailly platform competitive dynamics + Murphy bifurcation thesis.
- **[[foundry-competition]]** (S15) — Broader foundry competitive dynamics including Intel EMIB + Samsung Foundry + Intel Foundry.
- **[[IBIDEN]]** (S168) — the **FCBGA package substrate beneath the CoWoS package** (sequential-dependency adjacency): the CoWoS interposer-on-die module ultimately lands on an organic FCBGA substrate (the chip-to-board carrier) before the board — [[IBIDEN]] is that substrate node (~70-80% AI-server-substrate share). Substrate → CoWoS package → board; see [[pcb-interconnect-substrate-chokepoint]].

## Change log

- **2026-06-19 (S168 cross-reference):** Added a light [[IBIDEN]] cross-reference (ingested S168) — the FCBGA package substrate beneath the CoWoS package (sequential-dependency adjacency: substrate → CoWoS package → board). Cross-reference only; `last_updated` unchanged.
- **2026-05-29 (S110 cross-vault re-evaluation propagation — A5):** Propagated the MRVL Q1 FY2027 content deferred at the S102 refresh. (1) Added a CoWoS-specific demand vector to the Custom ASIC designer subsection — MRVL's Celestial **MRM-based scale-up "progressing in close collaboration with TSMC on CoWoS"** (qualitative, CoWoS-named; beyond the prior Taiwan-ship-to geographic proxy). (2) Refreshed the Cross-vault NVIDIA partnership roster **4 T1 → 5 T1** adding MRVL's $2.0B NVIDIA convertible-preferred ([[NVDA-platform-integration]] Mode 4 — equity + partnership + competitor overlap; equity Tier-1-confirmed, partnership scope pending NVDA bilateral). No capacity-constraint or thesis change; demand-side reinforcement only.
- **2026-05-15 (Session 65 1-stop chokepoint refresh — second 1-stop chokepoint refresh post-S51 [[HALEU-fuel-chokepoint]] precedent):** **First major-chokepoint full refresh in vault history.** 5 escalation triggers all NEGATIVE (no new primary-source ingest; vault participants stable; no new structural type; no new chokepoint creation; cross-vault analytical product established at S62 + S64 — propagation only). Substantive refresh additions ~120 lines (137 baseline → 257 final; expansion within Section 3.8 brevity discipline per S52 ETN precedent). **THREE NEW substantive sections delivered: (1) TSEM SiPh PDK foundry reference-design supplier complementarity (S62 NEW analytical product** — CEO Ellwanger explicit "TSMC wouldn't be buying our PIC for their CoWoS... we become the reference design for the major integrators"; first explicit primary-source documentation of cross-vault Layer 2 foundry-tier reference-design supplier complementarity pattern in vault history; methodology codification candidate Tranche 2C); **(2) HBM integration tier paired chokepoint (S64 NEW analytical product** — HBM upstream-vs-CoWoS integration tier pair formalization; new chokepoint pair structural type; sequential causation pattern documented; cross-domain 4-framework bridge); **(3) Cross-vault NVIDIA partnership pattern at CoWoS scope** — TSM Tier 2 cross-vault context entry per [[nvidia-supply-chain-commitments]] S53; 4 T1 + 7 T2 cross-vault pattern. **EXPANSIONS to existing sections:** Current capacity status (AVGO 2026-2028 HBM+CoWoS dual-chokepoint securing); Customer-side demand pressure NVDA perspective (NVDA $2B equity-plus-purchase materialization at LITE+COHR per S50 + NVDA GTC Spectrum-X CPO production); Equipment-tier demand signals (ONTO S54 refresh propagation — Atlas G6 head-to-head wins + Dragonfly G5 commercial ramp at HBM 2D+3D + Rigaku 27% strategic stake; TSMC + Samsung + SK Hynix all named via XBRL); Custom ASIC designer demand pressure (HBM-CoWoS dual-chokepoint securing context); Thesis implications (added 6th implication paired chokepoint completion + 7th implication TSEM reference-design supplier complementarity strengthens Layer 2 foundry-tier moat framing). **NEW Open questions section** (closes structural gap — only chokepoint canonical other than provisional wafer-level-siph-test previously without Open questions section); 10 items pre-registered including highest-priority TSM Q2 2026 refresh propagation candidate. **NEW Cross-references expansion** with [[HBM-oligopoly]] + [[TSEM]] + [[nvidia-supply-chain-commitments]] + [[cpo-integration]] + [[advanced-optical-packaging]] + [[InP-supply]] + [[transformer-supply]] + [[CPO-platform-battle]] + [[foundry-competition]] cross-references (vs prior single [[datacenter-photonics-supply-chain]] reference). **Section 4.6 ROI VALIDATED at 0 falsifications (20-instance zero-falsification streak post-S46 codification baseline; refresh propagation only; no kickoff hypothesis falsification candidates per Section 4.4).** A6 (g)/(g') count UNCHANGED at 8+2=10. Cross-vault NVIDIA partnership pattern UNCHANGED at 4 T1 + 7 T2 (no new NVIDIA verification at S65 refresh scope). Wikilink-clean streak: **48 sessions** post-S65. Files updated: 5 files (TSMC-CoWoS.md substantive refresh + TSEM.md cross-reference + HBM-oligopoly.md cross-reference + index.md + log.md; under hard cap 7). nvidia-supply-chain-commitments.md TSM Tier 2 entry refresh deferred per scope discipline (light cross-reference at S64 baseline preserved; substantive TSM-side update deferred to TSM Q2 2026 refresh post-mid-July 2026 reporting). **TSMC-CoWoS chokepoint refresh propagation cadence per S51 [[HALEU-fuel-chokepoint]] precedent durability VALIDATED at major-chokepoint-page scope** — 1-stop refresh protocol applicable at substantial-content-addition scope (~120 lines additions) when 5 escalation triggers all negative.
- **2026-05-15 (Session 64 cross-reference update — HBM oligopoly chokepoint canonical creation):** Added [[HBM-oligopoly]] cross-reference per Session 64 fourth canonical-from-first-creation chokepoint page synthesis (4th chokepoint structural type — "upstream oligopoly with vault-adjacent-scope substantiation"; Memory framework F6 vault coverage gap CLOSED). **Paired chokepoint pattern: HBM upstream-vs-CoWoS integration formalized** — HBM chokepoint = upstream supplier-tier (SK Hynix + Samsung + Micron); TSMC-CoWoS chokepoint (this page) = integration-tier for HBM base die stacking. Sequential chokepoint pairing distinct from [[transformer-supply]] + [[BTM-grid-bypass-workaround]] constraint-source-vs-workaround pair (S63 paired-chokepoint methodology); HBM-CoWoS pair = **upstream-vs-integration tier pair** — new chokepoint pair structural type (Tranche 2C methodology codification candidate). AVGO 95% TSMC wafer + HBM dependency at Q1 FY2026 = single most concentrated cross-chokepoint dependency in vault (HBM oligopoly supplier-tier + CoWoS integration-tier dual-chokepoint securing 2026-2028). MRVL Taiwan surge 3% → 20% as HBM-adjacent advanced packaging proxy preserved per S25 baseline. Cross-domain 4-framework bridge substantiated (F2 Layer + F5 Photonics adjacent + F6 Memory primary + F8 Equipment). No content edits beyond cross-reference resolution per scope discipline.
- **2026-04-19:** Created from TSM Q1 2026 earnings call (Tier 2). Covers capacity status (very tight, constrained through 2027+), technical challenges (warpage, mechanical stress, thermal), expansion plans (internal + OSAT), competitive alternatives (EMIB), and forward technology roadmap (CoPoS, SoIC).
- **2026-04-19:** Updated from NVDA Q4 FY2026 earnings call (Tier 2). Added customer-side demand pressure evidence: NVDA's dielet avoidance philosophy driving larger CoWoS packages, supply tightness confirmed from customer side, Blackwell deployment scale (9 GW). Structural demand intensification thesis strengthened by two-source triangulation.
- **2026-04-19:** Updated from TSM 20-F FY2025 (Tier 1). Added first quantitative context: non-wafer revenue (14% / NT$536.5B), 7 advanced backend fabs, Fab 23/24 capex allocation for advanced packaging, no material contracts observation, temporary receipts decline (NT$291B → NT$190B). CoWoS-specific breakout still unavailable.
- **2026-04-20:** Updated from AEHR (Q3 FY2026 call) and ONTO (10-Q Q3 FY2025, Q4 FY2025 call). Added equipment-tier demand signals section: AEHR explicitly names CoWoS as application, bookings 6x QoQ; ONTO's TSMC revenue (21%) and AP+HBM metrology growth >30% YoY as upstream leading indicators.
- **2026-04-23:** Updated from AVGO (10-K FY2025, 10-Q Q1 FY2026, Q1 FY2026 call) and MRVL (10-K FY2026, Q4 FY2026 call). Added custom ASIC designer demand pressure section: AVGO's 95% explicit TSMC wafer dependency (most explicit in vault), supply secured 2026-2028 with Kawwas attribution, six XPU customers approaching ~10 GW; MRVL's Taiwan surge (3%→20%, 10x in two years) as geographic proxy. Demand corroboration now spans four vantage points (customer-side NVDA, equipment-tier AEHR/ONTO, designer AVGO/MRVL).
- **2026-04-26:** Updated from NVDA GTC March 16, 2026 keynote (Tier 2). COUP/COUPE added to Evolution section — first primary-source COUP/COUPE reference from any vault company, TSMC co-development attribution, naming variant open question documented.
- **2026-05-24 (Session 84 cross-vault propagation post-S81 NVDA + S82 NVDA-platform-integration):** Added "NVDA Q1 FY2027 customer-side demand expansion" subsection at Customer-side demand pressure section. Single-customer GPU count milestones (Microsoft Fairwater hundreds of thousands Blackwell + AWS 1M+ Blackwell+Rubin + Google A5X 960k Rubin) reinforce CoWoS allocation demand. Vera Rubin Q3 2026 production trajectory + 7-chip/5-rack-scale platform CoWoS demand pull. $145B total supply commitment Q1 FY2027 material expansion. TSMC reciprocal non-naming reverted at Q1 FY2027 earnings call — GTC March 2026 venue-specific break did not propagate; pattern verdict venue-specific. Cross-references to [[NVDA-platform-integration]] S82 reciprocal naming asymmetry + 7-modality framework (no re-documentation). No tickers expansion.
- **2026-04-27:** Session 19 cross-reference. Added Cross-references section linking [[datacenter-photonics-supply-chain]].
- **2026-04-30 (Session 32 cross-reference — [[cpo-integration]] chokepoint page creation):** Cross-referenced from new chokepoint page [[cpo-integration]] (fourth canonical multi-source-synthesis chokepoint page in vault history; closes Tier 3 framework Chokepoint 10 dedicated chokepoint page coverage gap). COUPE foundry-tier integration mechanics + NVDA + TSM joint co-development modality + COUPE/COUP naming convention + Tier 1 silence preserved (zero COUPE/CPO mentions in 20-F FY2025 + Q1 2026 call) cross-referenced from [[cpo-integration]] TSM per-company integration positioning section + Value chain shift dynamics foundry-tier value capture subsection. CoPoS distinct future packaging technology preserved. No content edits to this chokepoint page.
