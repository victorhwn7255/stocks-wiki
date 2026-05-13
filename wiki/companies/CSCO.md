---
type: company
tickers: [CSCO]
layer: 3
photonics_tier: 4
last_updated: 2026-04-27
---

# Cisco Systems (CSCO)

## Thesis role

CSCO is a $57B revenue enterprise networking, security, and observability company; this page treats only the thesis-relevant businesses: Acacia coherent optics, Silicon One networking silicon, optical/photonic interconnect, hyperscaler AI infrastructure relationships, and CPO commentary. Non-thesis segments (security, collaboration, observability, services) are acknowledged in Financial snapshot only.

**Layer 3 per frameworks.md v5 with Layer 3/5 straddling tension.** frameworks.md places CSCO at Layer 3 (Specialized Designers, "Silicon One + Acacia"). Source evidence reveals a straddling tension structurally analogous to [[AAOI]]'s Layer 4/5 straddling: CSCO designs its own silicon (Layer 3 capability) but sells complete networking systems (Layer 5 revenue model). The contrast with [[MRVL]] — the other Layer 3 occupant — is structural:

| Dimension | MRVL (Layer 3) | CSCO (Layer 3 per frameworks.md) |
|-----------|----------------|----------------------------------|
| Silicon sales model | Merchant — custom ASICs, DSPs sold to hyperscalers as components | Captive — Silicon One used in CSCO's own switches and routers |
| Optical sales model | Merchant — coherent DSPs sold to transceiver makers | Captive — Acacia technology embedded in Cisco-branded pluggables |
| Customer visibility | 14% Customer A, 37% Distributor A, named XPU programs | No customer >10%, no named AI customers |
| What customer buys | Marvell chips | Cisco networking systems |

Layer 3 classification maintained per frameworks.md; the straddling tension is flagged honestly. CSCO's higher consolidated margins (64.9% GM) reflect the diversified system-vendor model, not Layer 3 specialization economics.

**photonics_tier 4 — new Framework 5 placement.** CSCO has real silicon photonics capability: 1.6T OSFP and 800G LPO "both built with Cisco silicon photonics technology" (Q2 FY2026 call), Acacia scaling at hyperscalers with "triple-digit growth in bookings" (Q2 FY2026 call), and claimed CPO technology readiness. But CPO is explicitly deferred ("not imminent right now"), Acacia is captive (no merchant DSP sales), and zero CPO investment or revenue targets are disclosed. Tier 4 reflects the current state — real but indirect photonics exposure. Less committed than [[MRVL]] (Tier 3, $3.25-5.5B Celestial, $500M/$1B targets); more capable than [[ALAB]] (Tier 4, $31.1M aiXscale, zero optical revenue).

**CPO platform contestant — acknowledged deferral.** One of five named contestants in [[CPO-platform-battle]]. CSCO's CPO posture is the weakest of the five: zero investment, zero revenue targets, zero scale-up product. But Robbins claims technology readiness and frames non-adoption as customer-driven — an "acknowledged deferral" distinct from [[AVGO]]'s active dismissal. See CPO positioning section below.

*Control-point distinction (per `raw/research/photonics-chokepoint-table.md`, Tier 3 source).* CSCO exhibits bottleneck participation with platform-tier ambition via Silicon One + acquired Acacia coherent + 1.6T LPO with Cisco silicon photonics technology. Per the framework: "secondary architecture name." CSCO's CPO acknowledged-deferral position (per [[CPO-platform-battle]]) reflects ambivalent platform-tier commitment — Robbins frames non-adoption as customer-driven choice. The control-point distinction is complementary to the Layer 3/5 straddling tension already documented above: CSCO designs silicon (Layer 3 capability) but sells networking systems (Layer 5 revenue model), with platform-tier authority weaker than [[NVDA]]/[[AVGO]] but stronger than pure system integrator role would suggest. Cross-reference: control-point thread spans [[NVDA]], [[AVGO]], [[MRVL]], [[CSCO]], [[ANET]] within vault per framework five-company set.

## Financial snapshot

### FY2025 annual (10-K, Tier 1)

| Metric | FY2025 | FY2024 | FY2023 |
|--------|--------|--------|--------|
| Total revenue | $56,654M | $53,803M | $56,998M |
| Networking | $28,304M (-3%) | $29,229M | $34,570M |
| Security | $8,094M (+59%) | $5,075M | $3,859M |
| Collaboration | $4,154M (+1%) | $4,113M | $4,052M |
| Observability | $1,055M (+26%) | $837M | $661M |
| Services | $15,046M (+3%) | $14,550M | $13,856M |
| Product gross margin | 63.7% | 63.5% | 61.5% |
| R&D | $9,300M (16.4%) | $7,983M | $7,551M |
| Purchase commitments | $7,599M (+47%) | $5,158M | $7,253M |
| No customer >10% | — | — | — |

(CSCO 10-K FY2025)

### Q2 FY2026 quarterly (10-Q, Tier 1)

| Metric | Q2 FY2026 | Q2 FY2025 |
|--------|-----------|-----------|
| Total revenue | $15,349M | $13,991M |
| Revenue YoY | +10% | — |
| Networking | $8,294M (+21%) | $6,850M |
| Gross margin | 65.0% | 65.1% |
| Purchase commitments | $10,055M (+32% vs Jul 2025) | — |
| WIP inventory | $684M (+162% vs Jul 2025) | — |

(CSCO 10-Q Q2 FY2026)

### AI infrastructure trajectory (Tier 2 — Q2 FY2026 call)

| Metric | Q2 FY2026 | Q1 FY2026 | FY2025 total |
|--------|-----------|-----------|--------------|
| Hyperscaler AI orders | $2.1B | $1.3B | ~$2.1B |
| AI mix | 60% systems / 40% optics | — | — |
| FY2026 AI order target | >$5B (raised) | — | — |
| FY2026 AI revenue target | >$3B | — | — |

(CSCO Q2 FY2026 call)

## Silicon One platform

"Our single, unified, and scalable networking silicon architecture" (CSCO 10-K FY2025). Deployed across campus switching (9350/9610), data center switching (N9300 with embedded DPUs), and routing (8000 series). 1 millionth Silicon One chip shipped Q2 FY2026. G300 102.4T chip launched at Cisco Live Amsterdam — "positioning Cisco in an exclusive group of silicon providers delivering over 100 terabits per second switching speeds" (Robbins, Q2 FY2026 call).

**Silicon One ramp tied to webscale demand.** Purchase commitments of $7.6B (FY2025, up 47% YoY) and $10.1B (Q2 FY2026, up 32% vs. Jul 2025) are explicitly tied to "manufacturing Cisco Silicon One and other products to meet demand from webscale and other customers" (CSCO 10-K FY2025; CSCO 10-Q Q2 FY2026). The front-loading is dramatic: $7.2B of $7.6B due within one year (FY2025); $9.6B of $10.1B due within one year (Q2 FY2026). WIP inventory surged 162% ($261M → $684M). No specific webscale customers are named; the filing provides no further detail on which customers or product configurations drive the commitments.

**"Silicon diversity" positioning.** Robbins frames Silicon One as the alternative to incumbent merchant silicon: "we've talked a lot over the years about their desire to have silicon diversity. So that's a starting point for why they're interested in us being successful" (Q2 FY2026 call). This implicitly positions Silicon One against [[AVGO]] Tomahawk without naming the competitor. Differentiation claimed through programmability and power efficiency. No share-gain claims. No hyperscaler design wins named.

**AMD/HUMAIN JV.** CSCO announced plans to form a joint venture with AMD and HUMAIN to deliver up to 1 GW of AI infrastructure by 2030, beginning with 100 MW in Saudi Arabia (Q2 FY2026 call). CSCO participating in non-NVDA AI infrastructure builds.

**Foundry dependency.** The 10-K is silent on where Silicon One is fabricated. No TSMC, no foundry named anywhere. Manufacturing section describes contract manufacturers for PCB assembly only.

### NVIDIA-as-partner framing

CSCO is the only vault company that frames [[NVDA]] as a partner rather than a competitor or unnamed presence. Robbins: "Jensen was recently with us at our AI summit and talked about the power of their GPU and compute with our networking and security" (Q2 FY2026 call). NVIDIA field engagements increased 70% sequentially. "By and large, we are the network standard, particularly when we're partnering with NVIDIA in the enterprise right now" (Robbins, Q2 FY2026 call).

This contrasts with every other vault company's NVDA framing: [[MRVL]] maintains reciprocal non-naming; [[AVGO]] names NVDA as the competitive benchmark ("you're also competing against NVIDIA"); [[ALAB]] positions in NVDA's NVLink Fusion ecosystem but as a connectivity enabler. CSCO's partner framing reflects a complementary competitive position: CSCO sells networking infrastructure that surrounds NVDA GPU clusters rather than competing with NVDA's compute platform.

The 10-K simultaneously lists NVDA as a competitor ("Nvidia Corporation" in the competition section) — a Tier 1/Tier 2 framing divergence where the filing names a competitor that the call frames as a partner.

## Acacia and optical strategy

**Acacia scaling at hyperscalers.** "Acacia reported its strongest quarter to date, with triple-digit growth in bookings. All major hyperscalers are deploying its market-leading coherent pluggable optics for data center interconnect and scale-across use cases" (Robbins, Q2 FY2026 call). Growth across both 400G and 800G coherent optics with 800G "ramping significantly." Revenue not separately disclosed — buried in $28.3B Networking segment.

**New pluggables announced.** 1.6 Tbps OSFP and 800G LPO, "both built with Cisco silicon photonics technology" (Robbins, Q2 FY2026 call). LPO positioned as a bridge technology offering "huge power savings, greater efficiency for AI scale-out" — the near-term answer to CPO's power proposition.

**Filing-level invisibility.** Acacia appears in the 10-K only in two contexts: amortization ("fully amortized in larger part from our fiscal 2021 acquisition of Acacia" — CSCO 10-K FY2025) and patent litigation (Ramot v. Cisco and Acacia). Zero Acacia product descriptions, zero coherent DSP mentions, zero optical technology roadmap content. The 10-Q mentions Acacia only in the same litigation context. "Routed optical networking systems and our pluggable optic solutions" receives one sentence in the 10-K's Internet Infrastructure section with no elaboration.

**Tier 1/Tier 2 framing gap — the widest technology-disclosure gap in the vault.** The filings present Acacia as a fully amortized historical acquisition and Silicon One as a supply chain obligation; the call presents both as centerpieces of AI networking strategy with "strongest quarter," "triple-digit bookings," and "all major hyperscalers deploying." This gap is wider than [[MRVL]]'s Celestial disclosure gap (where the 10-K at least described CPO in product descriptions). A wiki reader relying on only Tier 1 would not know Acacia's technology or current commercial status. This is the fifth instance of the Tier 1/Tier 2 framing gap convention, alongside MRVL Celestial, AVGO COT risk, AVGO rack leasing, and AXTI competitor count.

## CPO positioning

**"Acknowledged deferral" — a distinct CPO variant.** Robbins directly addresses CPO when asked by Samik Chatterjee (JPMorgan):

> "we absolutely believe it's going to happen. We don't believe it's actually imminent right now... we have the technology to build it, and we will as customers want it. But today, they want choice." (Robbins, Q2 FY2026 call)

> "customers want the differentiation between optics and silicon so they have choice and they don't get locked in." (Robbins, Q2 FY2026 call)

This is structurally distinct from [[AVGO]]'s active dismissal: Hock Tan dismisses CPO's technology ("bright, shiny objects") while claiming leadership optionality ("we are the lead in CPOs"). Robbins acknowledges CPO's inevitability ("we absolutely believe it's going to happen") while framing current non-adoption as customer-driven ("they want choice"). Robbins does not claim CPO leadership and does not champion an alternative technology (no copper/SerDes argument). The customer-choice framing serves CSCO's current business — Acacia pluggables benefit from CPO deferral — but is less positionally constraining than Hock Tan's dismissal. If CPO wins scale-up, AVGO will need to reverse a public position; CSCO will not.

**Scale-up: explicitly no product.** "We haven't made any announcements on scale-up... we expect in the future to have products and revenue from scale-up, but we haven't announced anything" (Robbins, Q2 FY2026 call). This is the most candid non-position in the vault — no attempt to overstate readiness. See [[CPO-platform-battle]] for the four-way executive comparison.

**Filing-level silence.** Zero CPO, co-packaged optics, silicon photonics, photonic integration, or coherent DSP mentions across both filings. Consistent with the tiered silence pattern — thesis-relevant photonics technology appears on calls before filings.

## Open questions

1. **Acacia revenue disclosure.** Acacia revenue is buried in Networking. Until sub-segment disclosure improves, thesis-relevant optical revenue cannot be quantified. Watch for separate optical/AI breakout in future filings.
2. **Silicon One vs. Tomahawk share trajectory.** "Silicon diversity" is a second-source framing, not a share-gain claim. Watch for hyperscaler design win disclosures and whether $10B+ purchase commitments translate to meaningful switching market share.
3. **Scale-up technology commitment.** CSCO has no scale-up product, no announced technology, and no timeline. Watch for product announcements and whether CSCO chooses CPO, copper, or LPO for scale-up.
4. **CPO contestant sustainability.** CSCO is the weakest of five contestants by commitment level. If MRVL and AVGO accelerate CPO investments, does CSCO remain a contestant or fade to systems integrator of others' CPO platforms?
5. **Layer 3/5 classification.** If Silicon One achieves meaningful merchant adoption (sold as standalone silicon, not embedded in Cisco systems), Layer 3 classification strengthens. If Silicon One remains captive, Layer 5 reclassification may be warranted.

## Source audit notes

**Q2 FY2026 earnings call (Tier 2, February 11, 2026).** CPO directly asked and substantively answered — Robbins' "acknowledged deferral" is the clearest public CPO positioning from any switch silicon vendor. Acacia "strongest quarter" / "triple-digit booking growth" / "all major hyperscalers deploying" — the only commercial visibility into Acacia in any source. NVDA named as partner (unique in vault — Jensen at Cisco AI Summit, 70% sequential engagement increase). Silicon One G300 102.4T launched; 1M chips shipped. AI orders $2.1B Q2 hyperscaler ($1.3B Q1), FY2026 targets raised to >$5B orders / >$3B revenue. Robbins tone: confident and promotional but NOT combative — third CEO combativeness instance not triggered. 11 analysts; 1 CPO question (Chatterjee, JPMorgan); zero questions on Acacia revenue, Silicon One share vs. Tomahawk, or scale-up technology. Scale-up explicitly: "haven't made any announcements."

**10-Q Q2 FY2026 (Tier 1, filed February 17, 2026).** Zero CPO/silicon photonics/coherent DSP/pluggable mentions. Silicon One only in purchase commitment context. "AI Infrastructure solutions" used repeatedly but never defined — no breakout of what products or silicon constitute AI Infrastructure. Networking $8,294M Q2 (+21% YoY). Purchase commitments $10,055M (+32% vs. Jul 2025), primarily Silicon One and memory. WIP inventory +162% ($261M → $684M). "Bespoke product designs" risk for cloud customers. No competitors named.

**10-K FY2025 (Tier 1, filed September 9, 2025).** Widest technology-disclosure gap in vault. Acacia reduced to amortization footnote ("fully amortized") and litigation co-defendant. Zero Acacia product, technology, or roadmap descriptions. Zero CPO/silicon photonics/coherent DSP. Silicon One described as "unified networking silicon architecture" but with no AI-specific framing. Named competitors: Arista, Broadcom, Ciena, NVDA, Huawei — MRVL and JNPR not named. No customer >10% in FY2025/2024/2023. Purchase commitments $7,599M (+47%), tied to Silicon One for webscale customers. R&D $9,300M (16.4%) — highest absolute spend in vault. $355M supplier settlement from terminated shortage-era supply arrangements (unnamed supplier, $450M in forfeited prepayments). No foundry named; no TSMC.

## Change log

- **2026-04-26:** Created from CSCO 10-K FY2025 (Tier 1), CSCO 10-Q Q2 FY2026 (Tier 1), CSCO Q2 FY2026 earnings call (Tier 2). First CSCO page. Layer 3 with Layer 3/5 straddling tension. photonics_tier 4. Fifth and final CPO contestant page. Resolves last forward wikilink in vault. Three-source coverage from inception.
- **2026-04-27 (Session 24 chokepoint research framework integration — Integration 1):** Added control-point distinction paragraph to Thesis role section per Tier 3 source `raw/research/photonics-chokepoint-table.md`. CSCO framed as bottleneck participant with platform-tier ambition (secondary architecture name per framework). Refinement attention flag (per Stop 2 instructions) handled: verified Session 16 canonical Layer 3/5 straddling tension framing on line 15 uses identical "designs its own silicon (Layer 3 capability) but sells complete networking systems (Layer 5 revenue model)" framing as proposed control-point distinction text — alignment confirmed, applied text as drafted without inline refinement. Cross-reference structure includes four-company control-point thread + ANET plain-text reference. A6 framework-placement verification confirmed Layer 3 with Layer 3/5 straddling tension per `frameworks.md` v7. Confidence: MEDIUM-HIGH.
- **2026-04-27 (Session 25):** Cross-referenced from new theme page [[chokepoint-investability-priorities]] Chokepoint 7 (Switch ASIC / platform architecture) per A2 first canonical application. Per `frameworks.md` v8 Framework 2.6 codification: CSCO bottleneck participant with platform-tier ambition. No content edits.
- **2026-04-28 (Session 27 ANET wikilink completion + [[ANET]] same-tier addition):** Control-point thread cross-reference plain-text "Arista Networks (ANET — not currently a vault company page)" replaced with `[[ANET]]` wikilink. Five-company control-point thread now in-vault complete. [[ANET]] joins CSCO at "bottleneck participant with platform-tier ambition" Framework 2.6 placement (Session 27). CPO positioning observation: ANET maintains tighter CPO silence than CSCO acknowledged-deferral framing — ANET 10-K + Q4 2025 call ZERO CPO mentions vs CSCO Robbins acknowledged non-adoption with customer-driven framing. Distinct silence-pattern data point at Layer 5 systems integrator level. No content edits beyond wikilink completion.
