---
type: company
tickers: [MRVL]
layer: 3
photonics_tier: 3
last_updated: 2026-05-27
---

# Marvell Technology (MRVL)

## Thesis role

Layer 3 specialized designer — the first Layer 3 company page in the vault. MRVL designs custom ASICs, interconnect silicon (PAM DSPs, coherent DSPs, AEC, retimers), and networking switches (Teralynx, UALink) for hyperscaler data center customers. Fabless model; dependent on [[TSM]] for leading-edge logic and advanced packaging (CoWoS, InFo, EMIB explicitly named in 10-K).

**CPO platform contestant.** One of five named contestants in [[CPO-platform-battle]] via Photonic Fabric, acquired through Celestial AI (closed February 2, 2026). MRVL is the only vault company where management treats CPO as a revenue line with quantified projections: $500M annualized run rate by Q4 FY2028, $1B by Q4 FY2029 (MRVL Q4 FY2026 call).

*Control-point distinction (per `raw/research/photonics-chokepoint-table.md`, Tier 3 source).* MRVL exhibits bottleneck-tier optical DSP/PHY component participation with control-point aspirations via Celestial Photonic Fabric. Per the framework: "secondary architecture name." MRVL's architectural authority is more limited than [[NVDA]] / [[AVGO]] but more substantive than pure component supplier role would suggest — Photonic Fabric chiplets co-packaged into XPUs and switches give MRVL platform-tier influence at the scale-up CPO transition. Honest-verdict framing per fourth discipline: control-point aspiration is real but not yet realized; Layer 3→2 trajectory triggers (per `frameworks.md` Section 2.5) remain unmet as of FY2026. Cross-reference: control-point thread spans [[NVDA]], [[AVGO]], [[MRVL]], [[CSCO]], [[ANET]] within vault per framework five-company set.

**Layer 3 → Layer 2 trajectory (in-progress, not upgraded).** Per CLAUDE.md v5 Layer straddling tension convention, MRVL's current revenue structure anchors Layer 3: GAAP gross margin 51.0% (Layer 3 range, well below TSM's 66.2% or NVDA's 75.2%), custom ASIC economics carry lower margins than standard products (MRVL 10-Q Q3 FY2026), revenue still 26% non-data-center, and customer warrants reduce recognized revenue — competitive economics, not infrastructure pricing power. The trajectory toward Layer 2 is real: data center grew from 40% to 74% of revenue in two years, custom silicon doubled YoY, Celestial AI adds photonic infrastructure capability. Upgrade trigger: GAAP margins approaching 60%+, Celestial/CPO revenue exceeding $500M annual, and custom ASIC mix demonstrably improving rather than diluting margins. None met in FY2026.

## Financial snapshot

### FY2026 annual (10-K, Tier 1)

| Metric | FY2026 | FY2025 | FY2024 |
|--------|--------|--------|--------|
| Revenue | $8,194.6M | $5,767.3M | $5,507.7M |
| Revenue YoY | +42% | +5% | — |
| GAAP gross margin | 51.0% | 41.3%* | 41.6% |
| GAAP operating income | $1,322.9M | ($720.3M) | ($567.7M) |
| GAAP EPS (diluted) | $3.07** | ($1.02) | ($1.08) |
| Non-GAAP EPS (diluted) | $2.84 | $1.57 | — |
| Data center revenue | $6,100.3M (74%) | $4,164.2M (72%) | $2,216.7M (40%) |
| Operating cash flow | $1,750.5M | $1,681.2M | $1,370.5M |

*FY2025 COGS included $357.9M restructuring impairment; normalized margin higher. **GAAP net income inflated by $1.8B automotive divestiture gain. (MRVL 10-K FY2026)

### Q3 FY2026 quarterly (10-Q, Tier 1 — pre-Celestial baseline)

| Metric | Q3 FY2026 | Q3 FY2025 |
|--------|-----------|-----------|
| Revenue | $2,074.5M | $1,516.1M |
| Revenue YoY | +37% | — |
| GAAP gross margin | 51.6% | 23.0%* |
| Data center | $1,517.9M (73%) | $1,101.1M (73%) |

*Distorted by $356.8M restructuring charges. (MRVL 10-Q Q3 FY2026)

### Forward outlook (Tier 2 — management guidance, MRVL Q4 FY2026 call)

| Metric | FY2027 outlook | FY2028 outlook |
|--------|---------------|----------------|
| Revenue | ~$11B (+30%) | ~$15B (~40%) |
| Data center growth | +40% YoY | ~+50% YoY |
| Non-GAAP EPS | — | "well over $5" |
| Custom silicon | ~$1.95B (~30% growth) | "at least double" YoY |
| Switch revenue | >$600M | — |
| Interconnect growth | >50% YoY | — |

Murphy characterized the $5 EPS as "just a floor" (MRVL Q4 FY2026 call). Guidance revisions have trended upward: FY2027 rose from $9.4B (Sep 2025) to $10B (Dec 2025) to $11B (Mar 2026). FY2028 rose from ~$13B to ~$15B in one quarter. See [[AI-demand-durability]] for cross-company demand convergence.

## Product portfolio and technology

**Custom ASICs.** MRVL's proven ASIC platform leverages IP including "ultra-high-speed SerDes, ARM compute, security, storage, silicon photonics and advanced packaging, including die to die interconnects, chiplets, co-packaged optics ('CPO') and custom high-bandwidth memory ('HBM')" (MRVL 10-K FY2026). Process nodes: 5nm in production, 3nm in progress, 2nm and 1.4nm (A14) in development with gate-all-around transistor design and backside power delivery. Advanced packaging: CoWoS, InFo, and EMIB explicitly named for 2.5D/3D/3.5D interposer designs. Custom revenue: $1.5B FY2026, doubled YoY, with 20+ design wins/products in production or going to production (MRVL Q4 FY2026 call).

**Interconnect portfolio.** PAM DSPs (first-to-market claim at every PAM generation; 200G per lane productized, 400G demonstrated), coherent and coherent-lite DSPs (1.6T shipping, 2nm next-gen sampling), DCI modules (targeting all five major US hyperscalers), AEC DSPs (design wins at three Tier 1 hyperscalers), LPO chipsets, and PCIe retimers. Combined AEC + retimer revenue ~$200M FY2027, more than doubling YoY (MRVL Q4 FY2026 call).

**Networking switches.** Teralynx scale-out switches: 12.8T sustained, 51.2T ramping, 100T sampling H1 FY2027. Scale-up: UALink 115T solutions sampling H2 FY2027, volume production FY2028. Switch revenue exceeded $300M FY2026, guided to >$600M FY2027 (MRVL Q4 FY2026 call).

## Celestial AI acquisition and Photonic Fabric

**Acquisition terms.** Closed February 2, 2026 (subsequent to FY2026 fiscal year end). Cash consideration ~$1.3B ($1.0B net of ~$300M cash acquired). Stock: ~24.5M MRVL shares. Contingent earn-outs: additional cash and shares contingent on revenue milestones through FY2029 — total consideration up to ~$5.5B including earn-outs (MRVL 10-K FY2026). The revenue-milestone earn-out structure is analytically comparable to [[AAOI]]'s Amazon warrant: a contingent equity instrument where the company signals conviction about future revenue by tying consideration to achievement. The earn-out's ~$2.2B incremental value ($5.5B minus ~$3.3B at close) is MRVL's implicit bet that Celestial revenue will materialize at scale through FY2029.

**Photonic Fabric technology.** First-generation product is a chiplet "integrating all required electrical and optical components, including drivers, TIAs, equalizers, SerDes, microcontrollers, modulators, photodiodes, and waveguides, into a compact form factor" (MRVL 10-K FY2026). This component integration maps to the silicon photonics architecture described in the primer: a monolithic photonic integrated circuit combining active modulation, detection, and passive routing on a single substrate (silicon-photonics-primer.md). Purpose-built for scale-up networking — chiplets co-packaged into both custom XPUs and scale-up switches, on both sides of the link (MRVL Q4 FY2026 call).

**Xconn acquisition.** Closed February 10, 2026. ~$280M cash + ~2.1M MRVL shares. Advanced PCIe 6.0 and CXL 3.1 switching silicon (monolithic, up to 256 lanes). Expands UALink scale-up switching capability (MRVL 10-K FY2026).

**CPO revenue projections.** $500M annualized run rate Q4 FY2028; $1B annualized Q4 FY2029. Celestial + Xconn combined ~$250M aggregate revenue FY2028 (full-year, not run rate). First-gen chiplet in high-volume manufacturing now. "Large-scale commercial deployment of CPO for scale-up connectivity starting next year" — FY2028 (MRVL Q4 FY2026 call). Scale-up interconnect TAM: >$10B by 2030.

**Tier 1 / Tier 2 framing gap.** The 10-K's treatment of Celestial AI is corporate and procedural: "not practicable to disclose" preliminary purchase price allocation, zero revenue attribution, subsequent event framing. The earnings call's treatment is commercially aggressive: $500M/$1B run rate targets stated as operating forecasts, "fully engaged in bringing Celestial's first-generation chiplet into high-volume manufacturing," Murphy never uses "research" or "experimental" language. This is the widest Tier 1/Tier 2 framing gap in the vault — the filing presents a just-closed acquisition with undisclosed financials while the call presents a near-term commercial product with quantified multi-year revenue trajectory. Both are factually accurate within their respective disclosure conventions, but a wiki reader relying on only one tier would reach substantially different conclusions about Celestial's commercial maturity.

## CPO platform positioning

**Murphy's bifurcation: scale-out vs. scale-up.** The most consequential CPO finding in the vault. Murphy explicitly states CPO for scale-out is "relatively limited" relative to pluggable transceivers — a longstanding view, unchanged. CPO for scale-up is "inflecting in a pretty big way." UALink is "a perfect use case" for CPO. Integration with Innovium Teralynx for scale-out: POCs done, "not our current plan today," ready to react when needed (MRVL Q4 FY2026 call, Rolland Q&A). This bifurcation restructures the CPO analysis — see [[CPO-platform-battle]] for implications.

**Competitive landscape.** The 10-K names CPO competitors explicitly: Ayar Labs (NVDA-backed photonic chiplet), Lightmatter, and Ranovus — the first explicit CPO competitor naming in any vault filing (MRVL 10-K FY2026). Also names [[AVGO]] (Broadcom), [[NVDA]], AMD, [[CSCO]] (Cisco), and [[ALAB]] (Astera Labs) as direct competitors. Notable absence: [[COHR]], [[LITE]], and [[AAOI]] are NOT listed as competitors, consistent with MRVL operating at Layer 3 (designer) rather than Layer 4 (component supplier).

**"1 large customer" initial deployment.** CPO scale-up shipping at one large customer initially; remaining scale-up deployments copper-based. Copper coexistence acknowledged as persisting "for some time" (MRVL Q4 FY2026 call).

**Custom ASIC competitive dynamics.** [[NVDA]] never named on the call — reciprocal non-naming pattern now observed at Layers 1, 2, and 3. [[AVGO]] never named but is clearly the "competition from another supplier" at the lead XPU customer (multiple analysts referenced this). [[ALAB]] is named as a direct competitor in ALAB's 10-K FY2025, and both companies compete in the scale-up fabric switching market — MRVL via UALink switches and Photonic Fabric, ALAB via Scorpio X-Series and NVLink Fusion. See [[hyperscaler-custom-ASIC]] for the cross-company competitive landscape. Murphy was emotionally defensive on custom silicon competitive noise: "Do you see me blinking? You don't... I'm very fired up on this topic" — referencing "analysts retracting notes" and "articles that weren't even accurate at all" (Murphy, MRVL Q4 FY2026 call). This is the most combative management passage in the vault. The defensive intensity signals live competitive pressure that standard corporate language would obscure.

**Tier 3 substrate addition (per `raw/research/CPO-for-AIDC-Infrastructure.md` 2026-05-26 + `raw/research/CPO-in-AIDC.md` 2026-05-27; in-place refresh per Vic instruction; not counted as separate session).** Tier 3 dual-source framework positions MRVL at value-chain Layer A (Photonic Die / Optical Engine) + Layer B (DSP / SerDes / Switch Silicon) — substantively spans 2 of 6 value-chain layers; rare structural breadth among CPO ecosystem participants. **AWS endorsement quotation per Tier 3 source:** Dave Brown VP Compute & ML Services on Celestial acquisition: *"we believe optical interconnects will play an important role in the future of AI infrastructure"* — substantive AWS-side validation at Celestial scale-up architecture scope. Per Report 1 framing: "highest-beta strategic challenger because it spans custom XPU enablement, switching, photonics, and optical DSP, but it has more execution dependence." **Tier 3 reports announced deal terms** (Marvell 8-K Dec 2 2025: ~$3.25B upfront [$1B cash + ~$2.25B in ~27.2M shares] + up to ~27.2M earnout shares; total ~$6B deal value) substantively reconcile with vault primary-substantiated closed-deal terms (Feb 2 2026; $1.3B cash + ~24.5M shares + total up to ~$5.5B per 10-K FY2026); minor variance per disclosure-timing convention (announcement vs. close). Per Section 5.2: Tier 3 source's competitive positioning language at MRVL strategically-relevant scope captured observationally; conviction labels EXCLUDED. Per CPO-for-AIDC-Infrastructure.md (2026-05-26) + CPO-in-AIDC.md (2026-05-27).

## Customer concentration and hyperscaler trajectory

| Customer | FY2024 | FY2025 | FY2026 | Trend |
|----------|--------|--------|--------|-------|
| Customer A (direct) | <10% | 13% | **14%** | Growing — custom ASIC customer reaching scale |
| Distributor A | 24% | 34% | **37%** | Accelerating — likely handles largest custom programs |

(MRVL 10-K FY2026)

Four customers represented 73% of gross AR at January 31, 2026. Distributor A at 37% ($3.0B+) is the highest single-channel concentration in the vault. Neither customer is named.

**Customer warrants.** Two revenue-milestone-vesting instruments: FY2025 warrant (4.2M shares at $87.77, 7-year exercise, 5-year vesting, $227.6M fair value; 0.7M vested as of Jan 31, 2026) and FY2026 warrant (1.0M shares at $87.00, 6-year exercise, 5-year vesting, $55.4M fair value; associated with Celestial acquisition). Both recognized as revenue reductions. The existence of two separate warrants confirms at least two major custom programs with equity-participation structures (MRVL 10-K FY2026).

**Hyperscaler positioning.** Murphy claims "extremely strong position with the top four U.S. hyperscalers and then the next level" with diversified product mix across each. DCI modules targeting all five major US hyperscalers. AEC design wins at three Tier 1 hyperscalers. OpenAI partnership with "lead XPU customer" referenced by Harlan Sur (JPMorgan) on the call — Murphy did not dispute (MRVL Q4 FY2026 call).

## Portfolio rationalization

**Automotive ethernet divestiture.** Sold to Infineon Technologies for $2.5B cash, August 14, 2025. Pre-tax gain $1.8B. Goodwill derecognized $524.7M. Murphy framed as active redeployment: "divesting our automotive Ethernet business for a double-digit revenue multiple and rapidly redeploying the proceeds into two highly strategic acquisitions" (MRVL Q4 FY2026 call). Proceeds funded Celestial AI and Xconn acquisitions.

**FY2025 restructuring.** $702.7M in restructuring charges to "increase R&D investment in the data center end market and reduce investment in new product development in other end markets including the cancellation of certain future product releases" (MRVL 10-K FY2026). MRVL went all-in on data center/AI.

**End-market consolidation.** Beginning Q4 FY2026, five end markets (enterprise networking, carrier infrastructure, consumer, automotive/industrial, data center) collapsed to two: data center and "communications and other." Creates apples-to-apples comparison challenges with prior periods.

**Geographic shift: Taiwan surge.** Taiwan ship-to revenue surged from $161.9M (3%) in FY2024 to $1,657.3M (20%) in FY2026 — 10x in two years. The filing caveats that ship-to destination is not end-customer location. The magnitude and timing (coinciding with custom ASIC ramp) strongly suggest TSMC advanced packaging dependency — custom ASICs shipped to Taiwan for CoWoS/InFo integration, then re-exported (MRVL 10-K FY2026). This corroborates the [[TSMC-CoWoS]] chokepoint from the demand side.

## Open questions

1. **Layer 2 upgrade trigger:** What margin/revenue threshold would warrant reclassification? Watch Celestial revenue ramp, GAAP gross margin trajectory, and whether custom ASIC mix shift improves or dilutes margins over FY2027-FY2028.
2. **Celestial ramp execution risk:** $0 → $500M annualized run rate in ~2 years is an extremely steep assumption. Full FY2028 Celestial + Xconn is only ~$250M; the $500M is a Q4 exit rate.
3. **Custom ASIC margin dilution:** Murphy noted XPU (custom silicon) is lower-margin while XPU-attached (NIC, CXL, retimer) is "more margin-rich." As custom grows from $1.5B to >$3B, does margin mix improve or compress?
4. **Customer vertical integration:** 10-K explicitly flags: "some large customers may begin developing and making their own semiconductor solutions." AI-driven design tools lowering barriers to entry cited as new risk (MRVL 10-K FY2026).
5. **Single-customer CPO dependency:** Initial CPO scale-up deployment at "1 large customer." What happens if that customer delays or switches?
6. **AVGO competitive dynamics at lead XPU customer:** Murphy's emotional defensiveness signals live pressure. Monitor for design win shifts.
7. **Earn-out dilution:** Celestial contingent consideration through FY2029 creates ongoing dilution risk if revenue milestones are met.

## Source audit notes

**10-Q Q3 FY2026 (Tier 1, filed December 3, 2025).** Pre-Celestial baseline — the cleanest financial snapshot of MRVL before the defining acquisition. Zero mentions of CPO, silicon photonics, optical DSP, PAM, or SerDes in the filing proper. "Electro-optics portfolio" appears once in MD&A passing. Custom ASIC lower-margin economics disclosed in risk factors: "this business model tends to have a lower gross margin." Customer warrant structure ($227.6M, revenue-milestone vesting) is thesis-significant but buried in equity compensation notes. Taiwan ship-to surge from 7% to 20% of 9M revenue (4.2x increase) is the strongest geographic proxy for TSMC advanced packaging dependency in any vault filing. The filing explicitly caveats geographic revenue: "not necessarily indicative of the geographic location of the Company's end customers."

**10-K FY2026 (Tier 1, filed March 11, 2026).** First filing to incorporate Celestial AI post-close. Product descriptions are extensive on CPO, Photonic Fabric, and silicon photonics — but confined to Item 1 (Business description), absent from MD&A. Names Ayar Labs, Lightmatter, and Ranovus as direct competitors — first explicit CPO competitor naming in any vault filing. TSMC never named despite obvious dependency; CoWoS, InFo, and EMIB named as packaging technologies. Customer A at 14% and Distributor A at 37% (both growing rapidly from FY2024) represent the fastest-accelerating concentration metrics in the vault. New AI-specific risk factor: "AI-driven design tools may lower traditional barriers to entry in the semiconductor industry." $300M IPR&D on balance sheet (indefinite-lived, 9-year expected useful life) — likely from a prior acquisition's unfinished technology program.

**Q4 FY2026 earnings call (Tier 2, March 5, 2026).** Most CPO-substantive source in the vault. Murphy leads prepared remarks with Celestial/Photonic Fabric and quantifies $500M/$1B run rate targets — stated as operating forecasts, not aspirational. Only Christopher Rolland (Susquehanna) of 12 analysts asked directly about CPO — producing the deepest CPO Q&A in any vault session. No analyst asked about competitive positioning vs. Ayar Labs or [[AVGO]]'s CPO efforts. Murphy's tone is aggressively confident throughout, bordering on promotional but backed by specific numbers. Defensive/emotional on custom silicon competitive noise ("Do you see me blinking?"). [[NVDA]] never named — reciprocal non-naming extends to Layer 3. COO Koopmans names supply binding constraints explicitly: "advanced wave fabrication, advanced packaging, large body substrates" — the most specific non-TSM supply constraint language in the vault, directly corroborating [[TSMC-CoWoS]].

## Change log

- **2026-05-27 (in-place refresh per Vic instruction; not counted as separate session — Tier 3 substrate addition per `CPO-for-AIDC-Infrastructure.md` 2026-05-26 + `CPO-in-AIDC.md` 2026-05-27):** Added Tier 3 dual-source substrate paragraph at CPO platform positioning subsection: AWS endorsement quotation (Dave Brown VP); MRVL spans value-chain Layer A + Layer B substantive structural breadth; Marvell 8-K Dec 2 2025 announced terms reconciliation with vault primary-substantiated closed-deal terms (Feb 2 2026); Tier 3 competitive positioning at strategically-relevant scope captured observationally per Section 5.2 (conviction labels EXCLUDED). last_updated 2026-04-27 → 2026-05-27.
- **2026-04-22:** Created from MRVL 10-Q Q3 FY2026 (Tier 1), MRVL 10-K FY2026 (Tier 1), MRVL Q4 FY2026 earnings call (Tier 2). First Layer 3 company page. Three-source coverage from inception. Template-setting for specialized designer tier.
- **2026-04-23:** Session 12 audit execution (non-ingest). Added [[AI-demand-durability]] cross-reference.
- **2026-04-23:** Session 14 cross-reference. Added [[ALAB]] competitive context in custom ASIC section and [[hyperscaler-custom-ASIC]] cross-reference.
- **2026-04-27 (Session 24 chokepoint research framework integration — Integration 1):** Added control-point distinction paragraph to Thesis role section per Tier 3 source `raw/research/photonics-chokepoint-table.md`. MRVL framed as bottleneck-tier with control-point aspirations via Celestial Photonic Fabric. Honest-verdict framing per fourth discipline: control-point aspiration is real but not yet realized. Cross-reference structure includes four-company control-point thread + ANET plain-text reference. A6 framework-placement verification confirmed Layer 3 with Layer 3→2 trajectory in progress per `frameworks.md` v7. Confidence: MEDIUM-HIGH.
- **2026-04-27 (Session 25):** Cross-referenced from new theme page [[chokepoint-investability-priorities]] Chokepoint 2 (Optical DSP / PHY power-performance) and Chokepoint 7 (Switch ASIC / platform architecture) per A2 first canonical application. Per `frameworks.md` v8 Framework 2.6 codification: MRVL bottleneck-tier with control-point aspirations. No content edits.
- **2026-04-28 (Session 27 ANET wikilink completion + [[CRDO]] same-tier addition):** Control-point thread cross-reference plain-text "Arista Networks (ANET — not currently a vault company page)" replaced with `[[ANET]]` wikilink. Five-company control-point thread now in-vault complete. [[CRDO]] joins MRVL at "bottleneck-tier with control-point aspirations" Framework 2.6 placement (Session 27 paired ingest at smaller operational scale than MRVL Photonic Fabric / Celestial). No content edits beyond wikilink completion.
- **2026-04-28 (Session 30 multi-source chokepoint synthesis):** Cross-referenced from new chokepoint page [[optical-dsp-phy-supply]] (second canonical multi-source-synthesis chokepoint page in vault history after [[InP-supply]] Session 13; closes Chokepoint 2 Optical DSP/PHY dedicated chokepoint page coverage gap per S27-S30 photonics completion arc). MRVL Ara 3nm 1.6T PAM4 DSP + Inphi-inherited coherent DSPs + Photonic Fabric (Celestial AI) + custom ASIC franchise content synthesized into chokepoint page per Session 9 ingest baseline + Session 19 Celestial codification + Session 24 Framework 2.6 codification. No content edits.
- **2026-04-30 (Session 32 multi-source chokepoint synthesis):** Cross-referenced from new chokepoint page [[cpo-integration]] (fourth canonical multi-source-synthesis chokepoint page in vault history; closes Tier 3 framework Chokepoint 10 (vault canonical Tier 3 Rank numbering) dedicated chokepoint page coverage gap). MRVL Photonic Fabric direct CPO platform-tier competitor positioning + Celestial AI acquisition closed February 2, 2026 (~$1.3B cash + up to $5.5B with earn-outs) + first-generation chiplet integrating drivers/TIAs/equalizers/SerDes/microcontrollers/modulators/photodiodes/waveguides + commercial deployment FY2028 + $500M annualized run rate Q4 FY2028 + $1B Q4 FY2029 + scale-up interconnect TAM >$10B by 2030 + Murphy bifurcation thesis (Scale-up CPO inflecting "in a pretty big way" vs Scale-out CPO "relatively limited") synthesized into chokepoint page per Session 9 ingest baseline + Session 19 Celestial codification + Session 24 Framework 2.6 codification + Session 30 [[optical-dsp-phy-supply]] precedent. Murphy bifurcation thesis preserved as analytical structure throughout chokepoint page per Option C single-page bifurcation handling. Tier 1/Tier 2 framing gap (widest in vault) preserved per [[optical-dsp-phy-supply]] canonical observation. No content edits.
