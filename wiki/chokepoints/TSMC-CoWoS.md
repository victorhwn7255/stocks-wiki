---
type: chokepoint
tickers: [TSM, NVDA, AEHR, ONTO, AVGO, MRVL]
last_updated: 2026-04-27
---

# TSMC CoWoS — Advanced Packaging Chokepoint

## What CoWoS is

CoWoS (Chip-on-Wafer-on-Substrate) is [[TSM]]'s advanced packaging platform used today for integrating high-bandwidth memory (HBM) stacking with leading-edge logic dies. It is the primary packaging technology for AI accelerators, enabling the multi-die configurations that GPUs, custom ASICs, and AI training/inference chips require.

CoWoS is a *current* bottleneck — well-documented allocation constraints exist today. This distinguishes it from TSMC's COUPE (silicon photonics engine), which is a *forward-looking* chokepoint still ramping to volume production. The wiki treats them as distinct chokepoints with different time horizons per the analytical framework.

## Current capacity status

Advanced packaging capacity is "very tight" as of Q1 2026 (TSM Q1 2026 call). TSMC is currently producing the largest reticle size CoWoS available in the market. The main supply approach for AI chip packaging today remains large-sized CoWoS combined with system-level and wafer-level integration (TSM Q1 2026 call).

Supply constraints in advanced packaging are expected to persist through at least 2027, paralleling front-end wafer capacity tightness (TSM Q1 2026 call). C.C. Wei confirmed that demand continues to increase and supply remains insufficient, with TSMC working to "speed it up" by pulling forward construction and equipment schedules.

### Quantification from Tier 1 filing

The TSM 20-F FY2025 provides the first quantitative context for advanced packaging, though no CoWoS-specific breakout exists:

- **Non-wafer revenue:** Packaging, testing, mask making, and other services = 14% of net revenue = NT$536,501M in FY2025 (TSM 20-F FY2025, Note 22a). This is the broadest available proxy for advanced packaging revenue; it includes testing and mask making alongside packaging and is not CoWoS-specific.
- **Backend fabs:** 7 advanced backend fabs as of the filing date (TSM 20-F FY2025).
- **Capex allocation:** FY2025 capex was allocated in part to "expanding capacity for specialty technologies and advanced packaging, including building/facility expansion for Fab 23 and Fab 24" (TSM 20-F FY2025, p.33). This confirms advanced packaging has its own identified capex category, not merely embedded in front-end wafer spending.
- **No material contracts:** "TSMC is not currently a party to any material contract, other than contracts entered into in the ordinary course of business" (TSM 20-F FY2025, p.61). Even the largest advanced packaging customer relationships are classified as ordinary course — no single customer supply agreement rises to SEC materiality.
- **Temporary receipts from customers:** NT$189,858M as of December 2025, down 35% from NT$291,102M in December 2024 (TSM 20-F FY2025, Note 22c). These are advance capacity reservation payments. The decline could reflect increased capacity availability, changing reservation terms, or balance sheet reclassification — flagged as an open question in [[TSM]].

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

### Equipment-tier demand signals

Two equipment-tier companies provide upstream confirmation of CoWoS demand intensity:

**[[AEHR]]** explicitly names "CoWoS" as an application for its FOX-NP burn-in systems, positioning Known-Good Die (KGD) testing as economically critical for multi-die advanced packaging — a defective die in a CoWoS package wastes the entire package (AEHR Q3 FY2026 call). AEHR's bookings surged 6x QoQ to $50.9M in Q3 FY2026, with advanced packaging test driving the semiconductor segment's growth from 3% to 25% of revenue (AEHR 10-K FY2025; AEHR 10-Q Q3 FY2026).

**[[ONTO]]** derives substantial revenue from TSMC — its largest named customer at 21% of Q3 FY2025 revenue (ONTO 10-Q Q3 FY2025). ONTO's advanced packaging and HBM metrology revenue grew >30% YoY (ONTO Q4 FY2025 call), and its $240M+ VPA pipeline is concentrated in HBM measurement. As the metrology supplier to the CoWoS chokepoint holder, ONTO's demand trajectory is a leading indicator: metrology tool orders precede wafer starts.

Equipment orders are a structural leading indicator for packaging capacity deployment. Both companies' demand signals are consistent with the CoWoS constraint intensifying rather than easing.

### Custom ASIC designer demand pressure (AVGO and MRVL perspectives)

Two custom ASIC designers provide demand-side corroboration for the CoWoS chokepoint from the perspective of TSMC's largest fabless customers:

**[[AVGO]] — 95% explicit TSMC dependency.** "Approximately 95% of the wafers manufactured by our CMs were produced by TSMC" (AVGO 10-K FY2025) — the most explicit foundry dependency disclosure in the vault. AVGO's wafer requirements "represent a meaningful portion of TSMC's total production capacity" (AVGO 10-K FY2025). Supply chain "fully secured for 2026 through 2028" per Hock Tan, including leading-edge wafers, HBM, substrates, and "T-glass" — TSMC's advanced packaging substrate referenced by name without attribution to TSMC (AVGO Q1 FY2026 call). Charlie Kawwas: "We're probably the first one to secure that up to 2028 or beyond" (AVGO Q1 FY2026 call). With AI semiconductor revenue at $8.4B in Q1 FY2026 (+106% YoY) and six custom XPU customers approaching ~10 GW aggregate deployment in 2027, AVGO represents a substantial and accelerating demand driver for CoWoS capacity. Taiwan ship-to revenue crossed 10% for the first time at $6,451M in FY2025 (AVGO 10-K FY2025).

**[[MRVL]] — Taiwan surge as geographic proxy.** Taiwan ship-to revenue surged from $161.9M (3%) in FY2024 to $1,657.3M (20%) in FY2026 — 10x in two years — strongly suggesting TSMC advanced packaging dependency as custom ASICs ship to Taiwan for CoWoS/InFo integration (MRVL 10-K FY2026). COO Koopmans named supply binding constraints explicitly: "advanced wave fabrication, advanced packaging, large body substrates" (MRVL Q4 FY2026 call).

Both companies corroborate the CoWoS chokepoint from the demand side: AVGO explicitly, MRVL through geographic and supply language. Together with the NVDA customer-side evidence (dielet avoidance driving larger CoWoS packages) and the equipment-tier signals ([[AEHR]], [[ONTO]]), the demand case for CoWoS constraint intensification is now supported from four distinct vantage points in the supply chain.

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

## Thesis implications

CoWoS capacity tightness directly supports the thesis that value concentrates at structural chokepoints. Evidence from this call:

1. **The chokepoint is active and intensifying.** Capacity is "very tight," demand continues to increase, and supply-demand balance is not expected before 2027 at the earliest. This is not a theoretical future constraint — it is a present reality affecting every AI chip customer.

2. **Technical difficulty reinforces the moat.** Mechanical stress, warpage, and thermal challenges at larger die sizes are getting harder, not easier, as AI chips grow. TSMC's accumulated experience in solving these problems is a durable competitive advantage. Competitors face a moving target.

3. **The OSAT expansion signal.** TSMC opening advanced packaging to OSAT partners is evidence of genuine constraint severity. It also implies the chokepoint may gradually widen if OSAT capacity scales — a dynamic to monitor.

4. **No evidence of the disconfirming signal.** `_thesis.md` identifies "TSMC's packaging advantage narrows" as a thesis risk. This call provides no evidence of narrowing. Intel's EMIB is acknowledged but not treated as a near-term competitive threat to CoWoS's market position. Samsung was not mentioned in the advanced packaging context.

5. **CoWoS pricing remains opaque.** No advanced packaging pricing was discussed. All pricing questions focused on wafer pricing. Whether TSMC is capturing chokepoint-appropriate pricing on CoWoS remains an open question for future sources.

## Cross-references

- [[datacenter-photonics-supply-chain]] — Section 2.6 (Photonic foundries) for the COUPE vault-conflict reconciliation; Section 2.7 (Assembly / packaging / testing) for cross-layer context; Bucket C in the investability framing covers the foundry-packaging-connectivity layer.

## Change log

- **2026-05-15 (Session 64 cross-reference update — HBM oligopoly chokepoint canonical creation):** Added [[HBM-oligopoly]] cross-reference per Session 64 fourth canonical-from-first-creation chokepoint page synthesis (4th chokepoint structural type — "upstream oligopoly with vault-adjacent-scope substantiation"; Memory framework F6 vault coverage gap CLOSED). **Paired chokepoint pattern: HBM upstream-vs-CoWoS integration formalized** — HBM chokepoint = upstream supplier-tier (SK Hynix + Samsung + Micron); TSMC-CoWoS chokepoint (this page) = integration-tier for HBM base die stacking. Sequential chokepoint pairing distinct from [[transformer-supply]] + [[BTM-grid-bypass-workaround]] constraint-source-vs-workaround pair (S63 paired-chokepoint methodology); HBM-CoWoS pair = **upstream-vs-integration tier pair** — new chokepoint pair structural type (Tranche 2C methodology codification candidate). AVGO 95% TSMC wafer + HBM dependency at Q1 FY2026 = single most concentrated cross-chokepoint dependency in vault (HBM oligopoly supplier-tier + CoWoS integration-tier dual-chokepoint securing 2026-2028). MRVL Taiwan surge 3% → 20% as HBM-adjacent advanced packaging proxy preserved per S25 baseline. Cross-domain 4-framework bridge substantiated (F2 Layer + F5 Photonics adjacent + F6 Memory primary + F8 Equipment). No content edits beyond cross-reference resolution per scope discipline.
- **2026-04-19:** Created from TSM Q1 2026 earnings call (Tier 2). Covers capacity status (very tight, constrained through 2027+), technical challenges (warpage, mechanical stress, thermal), expansion plans (internal + OSAT), competitive alternatives (EMIB), and forward technology roadmap (CoPoS, SoIC).
- **2026-04-19:** Updated from NVDA Q4 FY2026 earnings call (Tier 2). Added customer-side demand pressure evidence: NVDA's dielet avoidance philosophy driving larger CoWoS packages, supply tightness confirmed from customer side, Blackwell deployment scale (9 GW). Structural demand intensification thesis strengthened by two-source triangulation.
- **2026-04-19:** Updated from TSM 20-F FY2025 (Tier 1). Added first quantitative context: non-wafer revenue (14% / NT$536.5B), 7 advanced backend fabs, Fab 23/24 capex allocation for advanced packaging, no material contracts observation, temporary receipts decline (NT$291B → NT$190B). CoWoS-specific breakout still unavailable.
- **2026-04-20:** Updated from AEHR (Q3 FY2026 call) and ONTO (10-Q Q3 FY2025, Q4 FY2025 call). Added equipment-tier demand signals section: AEHR explicitly names CoWoS as application, bookings 6x QoQ; ONTO's TSMC revenue (21%) and AP+HBM metrology growth >30% YoY as upstream leading indicators.
- **2026-04-23:** Updated from AVGO (10-K FY2025, 10-Q Q1 FY2026, Q1 FY2026 call) and MRVL (10-K FY2026, Q4 FY2026 call). Added custom ASIC designer demand pressure section: AVGO's 95% explicit TSMC wafer dependency (most explicit in vault), supply secured 2026-2028 with Kawwas attribution, six XPU customers approaching ~10 GW; MRVL's Taiwan surge (3%→20%, 10x in two years) as geographic proxy. Demand corroboration now spans four vantage points (customer-side NVDA, equipment-tier AEHR/ONTO, designer AVGO/MRVL).
- **2026-04-26:** Updated from NVDA GTC March 16, 2026 keynote (Tier 2). COUP/COUPE added to Evolution section — first primary-source COUP/COUPE reference from any vault company, TSMC co-development attribution, naming variant open question documented.
- **2026-04-27:** Session 19 cross-reference. Added Cross-references section linking [[datacenter-photonics-supply-chain]].
- **2026-04-30 (Session 32 cross-reference — [[cpo-integration]] chokepoint page creation):** Cross-referenced from new chokepoint page [[cpo-integration]] (fourth canonical multi-source-synthesis chokepoint page in vault history; closes Tier 3 framework Chokepoint 10 dedicated chokepoint page coverage gap). COUPE foundry-tier integration mechanics + NVDA + TSM joint co-development modality + COUPE/COUP naming convention + Tier 1 silence preserved (zero COUPE/CPO mentions in 20-F FY2025 + Q1 2026 call) cross-referenced from [[cpo-integration]] TSM per-company integration positioning section + Value chain shift dynamics foundry-tier value capture subsection. CoPoS distinct future packaging technology preserved. No content edits to this chokepoint page.
