---
type: theme
tickers: [TSM, NVDA, TSEM, XFAB, CSCO]
last_updated: 2026-05-29
---

# Foundry Competition

## Thesis relevance

The durability of [[TSM]]'s chokepoint status depends on the competitive landscape remaining unfavorable to challengers. `_thesis.md` identifies "TSMC's packaging advantage narrows" as a disconfirming signal — if Intel Foundry, Samsung, or ASE meaningfully close the gap on advanced packaging, TSMC's structural position becomes less durable. This page tracks competitive evidence across the foundry and advanced packaging landscape.

## Competitive landscape

### Intel

**Terafab initiative:** Intel's Terafab initiative was noted by JPMorgan analyst Gokul Hariharan, who described it as a customer (of TSMC) also trying to "build chips on their own" and having "signed deals with Samsung a few months back" (TSM Q1 2026 call).

C.C. Wei's assessment: "both Intel and Tesla, they are TSMC's customer. So — but again, they are our competitors and we view Intel as a formidable competitors and do not underestimate them. But having said that, there are no shortcuts, the fundamental rule of the foundry game never change. They need a technology leadership, manufacturing excellence and customer trust and most of all, the service" (TSM Q1 2026 call).

**EMIB packaging:** Morgan Stanley analyst Charlie Chan raised Intel's EMIB (Embedded Multi-die Interconnect Bridge) as a competitive alternative to [[TSMC-CoWoS]] for large-reticle AI chip packaging, noting it is "substrate-based, more suitable for circular larger size chip design" (TSM Q1 2026 call).

C.C. Wei acknowledged the competitive offering without dismissing it: "we understand that our competitors also offer very attractive technology. But we work on that. So our customers can have more choices and then we can do more business with our customers" (TSM Q1 2026 call). TSMC is developing its own large-reticle packaging solutions in response.

**Assessment:** Intel is pursuing both leading-edge logic foundry (Terafab) and advanced packaging (EMIB) as competitive threats to TSMC. Neither currently represents a near-term market share risk per this source, but the fact that analysts devoted three separate question lines to competition in this call suggests the topic is gaining attention.

**Intel-CEO own-side view (No Priors podcast, 2026-06-18; Tier 3 — CEO talking his book).** Lip-Bu Tan's framing *confirms* the gap from Intel's own mouth rather than challenging the moat: he calls Intel **"very distant from TSMC"** on foundry performance, frames the catch-up as a multi-year **"trust business"** that only **"surfaces up" by ~2030-2032**, and says "we have a lot of respect for TSMC… we both need more capacity." He recounts the explicit **doubled-down decision** — to keep, not exit, foundry, against "a lot of voices… very expensive, not going to work" — backed by an industrial-policy capital stack: a **US-government equity stake** (he analogizes to the Taiwan government's early TSMC stake), **NVIDIA's ~$5B investment**, and **SoftBank**. Net: the Intel CEO's own account is *consistent with* this page's verdict — TSMC's "no shortcuts" moat intact, Intel a credible-but-multi-year challenger — and does **not** trip the `_thesis.md` "TSMC's packaging advantage narrows" disconfirming signal. `[verify: INTC filings — foundry roadmap + the NVDA $5B / SoftBank / US-gov capital stack; see the [[INTC]] /latest-alpha block]`

### Samsung

Samsung is making "first true inroads" into AI foundry — this was the analyst framing (Needham's Charles Shi), not management's (TSM Q1 2026 call). The specific win: Samsung is currently manufacturing [[NVDA]]'s LPU (language processing unit).

C.C. Wei's response was carefully worded: "We are working with our customers for their next-generation LPU anyway. And we are very confident in our technology position, and we will work hard to capture every piece of business possible" (TSM Q1 2026 call). This confirms TSMC is aware of the Samsung win and is actively competing for the next-generation LPU.

**Assessment:** Samsung's LPU win is narrow but symbolically significant — it represents Samsung's first meaningful AI chip manufacturing engagement. Whether this expands beyond LPU into GPUs or AI accelerators would be a much more material competitive development. Monitor for broadening.

**LPU terminology update (NVDA Q4 FY2026 call + TSM 20-F FY2025):** The NVDA Q4 FY2026 call does not use the term "LPU" at all. The Vera Rubin platform is enumerated as seven named products — Vera CPU, Rubin GPU, NVLink 6 Switch, ConnectX-9, SuperNIC, BlueField-4 DPU, Spectrum-6 Ethernet Switch — none called "LPU." The Groq licensing deal is discussed separately as a technology integration (non-exclusive licensing agreement for low-latency inference), not as a chip product being manufactured at Samsung. The TSM 20-F FY2025 also does not use the term "LPU" anywhere in 244 pages (TSM 20-F FY2025). The TSM Q1 2026 call's reference to Samsung manufacturing "NVDA's LPU" now remains unresolved after three independent sources. The original reference may have been imprecise analyst/management shorthand, or the LPU may be an unannounced product. Defer to future product-focused sources (GTC, analyst day).

**LPU resolution candidate via Groq LP30 (cross-vault link, [[NVDA-platform-integration]]).** A plausible reconciliation now exists: at GTC March 16, 2026, Jensen disclosed **LP30 — the third-generation LPU, manufactured by Samsung** — absorbed into the NVDA platform as a specialized low-latency-decode accelerator via NVIDIA Dynamo (per [[NVDA-platform-integration]] Groq modality). The Samsung-manufactures-an-LPU fact is therefore substantiated at the vault, and the most likely referent of the TSM Q1 2026 call's "NVDA's LPU at Samsung" is the **Groq LP30**, not a discrete NVDA-branded product. Epistemic hedge preserved: NVDA never explicitly equated "NVDA's LPU" with Groq's LP30, and the TSM-call phrasing was analyst shorthand — so this is a strong cross-vault link, not a confirmed identity. Competitively, it sharpens the Samsung read: Samsung's "AI foundry inroad" is an **inference-accelerator (LPU) win co-opted into the NVDA ecosystem**, not a GPU/leading-edge-logic win — narrower than the analyst "first true inroads" framing implied.

### ASE and OSAT competition

TSMC acknowledged working with OSAT partners to expand advanced packaging capacity (TSM Q1 2026 call). Laura Chen (Citigroup) asked specifically about TSMC's strategy with OSAT partners and whether TSMC is "expanding more in the advanced packaging" relative to OSATs.

C.C. Wei positioned this as collaborative rather than competitive: TSMC works with OSATs to expand total available capacity. This framing suggests TSMC does not currently view OSATs as competitive threats in advanced packaging, but as supplementary capacity providers. Whether this relationship remains collaborative as advanced packaging value grows is an open question.

## TSMC's competitive defense

C.C. Wei's competitive defense rested on four pillars, articulated repeatedly throughout the Q&A (TSM Q1 2026 call):

1. **Technology leadership** — leading-edge process and advanced packaging capability
2. **Manufacturing excellence** — yield, quality, and execution at scale
3. **Customer trust** — track record and relationship depth
4. **"No shortcuts"** — it takes 2-3 years to build a new fab and 1-2 more years to ramp it. This structural timeline means competitive threats develop slowly and are visible well in advance.

The "no shortcuts" argument is TSMC's strongest competitive moat signal. It implies that even if Intel or Samsung achieves technical parity in a specific process node, the 3-5 year timeline to build and ramp capacity means TSMC's installed base advantage persists for the duration of the thesis window (2026-2028).

**Tier 1 vs. Tier 2 competitive disclosure:** The TSM 20-F FY2025 competition section (p.21) lists competition categories generically — "dedicated foundries, integrated device manufacturers (IDMs) with different business models, and system companies that have foundry capabilities" — without naming Samsung, Intel, or any specific competitor (TSM 20-F FY2025). This is notably less informative than the Q1 2026 call's specific Samsung LPU win, Intel Terafab, and EMIB packaging commentary. The divergence illustrates a Tier 1/Tier 2 calibration point: for competitive dynamics assessment, Tier 2 earnings call commentary provides more analytical value than Tier 1 filing disclosure, which is constrained by legal conservatism. The Tier 1 competition section confirms TSMC acknowledges competitive threats exist but provides no basis for evaluating their severity.

**Capacity tightness as defensive moat:** An underappreciated dynamic: when supply is constrained everywhere (as it currently is), customers cannot easily shift volume to competitors even if competitive alternatives exist. The constraint itself reinforces incumbency. This dynamic would reverse if demand softens or TSMC's capacity catches up, making [[AI-demand-durability]] a critical dependency for the competitive moat.

## Tiered EUV dependency chain

The competitive landscape is shaped upstream by a single equipment dependency: ASML's monopoly position in EUV lithography. All frontier foundries depend on ASML, but the nature and binding force of that dependency differs by foundry (per /raw/research/ASML-EUV-foundry-dependency.md):

**[[TSM]] — deepest integration, highest sensitivity.** TSMC has the largest EUV installed base in the industry — a TSMC statement quoted by The Register in November 2024 indicated its EUV tool count in 2023 was 10x the 2019 level and represented approximately 56% of the global installed base, though this specific figure is an external reconstruction, not a filing disclosure (per /raw/research/ASML-EUV-foundry-dependency.md, citing The Register November 2024). N7+ was the first high-volume foundry EUV process; N5, N3, N2, and A16 all require EUV. TSMC's node cadence is inseparable from ASML allocation, installation, and process learning. The scanner monopoly and the foundry execution moat reinforce one another rather than substituting.

**Samsung — EUV-dependent but not always EUV-constrained.** Samsung's logic nodes from SF7 onward (SF5, SF4, SF3 GAA+EUV, SF2) are all EUV-dependent (per /raw/research/ASML-EUV-foundry-dependency.md, citing Samsung Foundry logic-node pages). However, Samsung's more immediate bottleneck has often been customer demand, ramp confidence, and yield rather than absolute tool availability. Reuters reported in October 2024 that Samsung had delayed accepting some ASML EUV equipment for its Taylor, Texas fab because the fab lacked major customers. This episode is analytically important: "EUV dependency" and "EUV currently binding" are not the same thing. Samsung depends on ASML for its frontier nodes, but in 2024-2025 that dependence did not always translate into an immediate tool-shortage constraint (per /raw/research/ASML-EUV-foundry-dependency.md, citing Reuters October 18, 2024).

**Intel — differentiated by High-NA EUV.** Intel 18A requires low-NA EUV; Intel 14A is explicitly tied to High-NA EUV as an "industry first" (per /raw/research/ASML-EUV-foundry-dependency.md, citing Intel foundry process page and High NA press kit). Intel received and assembled the industry's first High-NA EUV system (EXE:5000), with acceptance testing on the EXE:5200B reported in December 2025. Intel's 14A differentiation strategy depends on being earlier to High-NA in production than TSMC or Samsung — making ASML's High-NA production ramp a critical dependency for Intel's competitive positioning.

**SMIC — outside the EUV chain entirely.** SMIC cannot access ASML EUV under current export controls. Its 7 nm-class N+2 process uses DUV multipatterning, which TechInsights has confirmed is possible but at materially higher process complexity and likely lower yields. Reuters' June 2025 report that Huawei's new laptop used SMIC's older 7 nm-class N+2 rather than the expected 5 nm-equivalent N+3 suggests the absence of EUV remains a meaningful brake on commercial scaling below 7 nm. SMIC's competitive position is therefore structurally capped at a different level than the three EUV-equipped foundries (per /raw/research/ASML-EUV-foundry-dependency.md, citing TechInsights and Reuters June 23, 2025).

### EUV supply is not monotonically binding

The research's temporal observation is important for calibration: EUV supply has not been a single permanent constraint from 2020-2026. ASML's 2024 annual report described 2024 as a transition year — 44 EUV systems recognized (down from 53 in 2023), "several fab push-outs" because AI was not benefiting all customers equally, and competitive foundry dynamics influencing lithography timing. By 2025-2026, the balance swung back toward AI-led tightening: 48 EUV systems in 2025 including first High-NA, Q1 2026 outlook raised to €36-40B as customers accelerated capacity plans (per /raw/research/ASML-EUV-foundry-dependency.md, citing ASML 2024 Annual Report and ASML Q1 2026 press release). This prevents the wiki from treating EUV constraint as a single monotonic shortage story.

### Two-speed geopolitical dynamic

EUV access to China is effectively blocked under current export controls. ASML stated in 2023 that EUV systems were already controlled; Dutch controls were extended to additional DUV immersion models in September 2024. The active policy frontier is not EUV (already restricted) but whether the West will tighten DUV immersion exports and service restrictions on already-installed equipment. Reuters reported in April 2026 that proposed U.S. legislation would broaden pressure for countrywide DUV immersion restrictions and tighter service provisions for named firms such as SMIC (per /raw/research/ASML-EUV-foundry-dependency.md, citing ASML 2024 Annual Report, Government of the Netherlands September 2024, and Reuters April 2026). This creates a two-speed dynamic: the first speed is static (China cannot buy the frontier scanner), the second is dynamic (the West is still debating how far to squeeze the DUV/service workaround path). SMIC's present 7 nm-class capability appears to depend precisely on that workaround path.

## Specialty foundry sub-scope (distinct from leading-edge logic competition)

The competition dynamics above concern **leading-edge logic foundry** (TSMC vs Intel vs Samsung at N2/N3/A14 + advanced packaging). A structurally separate sub-scope is **specialty foundry** at mature/specialty process nodes, where two vault canonicals sit: [[TSEM]] (S62; Israeli) and [[XFAB]] (S99; Belgian). Both are foreign-issuer specialty foundries; both occupy Layer 2 on different grounds than TSM.

Specialty-foundry competitive dynamics differ from leading-edge logic in kind, not just degree:

- **No EUV dependency.** Specialty foundries run mature nodes (XFAB 1.0μm → 110nm; TSEM 200mm + selected 300mm), so the ASML EUV chokepoint that shapes leading-edge competition does not bind them. Their competitive moat is process specialization (analog/mixed-signal IP, SiPh PDK, SiC/GaN, MEMS), not transistor density.
- **Customer migration cost is the moat.** Long product lifecycles (XFAB cites >15 years; sole-source on most products + AEC-Q100 automotive qualification) make customer migration to another foundry equivalent to a new development. This durable-incumbency profile is what places both at Layer 2 despite mature-node positioning.
- **Non-overlapping specializations.** [[TSEM]] is silicon-photonics-PDK + analog/RF-focused; [[XFAB]] is wide-bandgap-power (SiC/GaN) + automotive-CMOS-focused. They are structural peers, not direct competitors — distinct from the head-to-head TSM/Intel/Samsung leading-edge contest.

Specialty-foundry competitors named at primary include GlobalFoundries, UMC, Infineon, STMicroelectronics, Wolfspeed, and onsemi (the latter three at the SiC/GaN end where XFAB competes). Specialty-foundry sub-scope is a monitoring lane distinct from the leading-edge thesis; it does not bear on the `_thesis.md` "TSMC's packaging advantage narrows" disconfirming signal.

## Evidence tracker

| Date | Source | Signal | Direction |
|------|--------|--------|-----------|
| 2026-06-18 (Tier 3) | No Priors / Lip-Bu Tan (Intel CEO) | Intel CEO calls Intel "very distant from TSMC," ~2030-32 catch-up, "trust business"; doubled-down on foundry (US-gov + NVDA ~$5B + SoftBank backing) | Confirms TSMC moat — Intel admits the gap; does not trip the disconfirming signal |
| 2026-05-13 | [[CSCO]] Q3 FY2026 call | First named Silicon One hyperscaler design wins (P200 ×2 + G200) + $16.0B purchase commitments — a large leading-edge networking-silicon foundry-demand datapoint | Informational — foundry-demand signal; foundry undisclosed (see note) |
| 2026-04-16 | TSM Q1 2026 call | Samsung wins NVDA LPU manufacturing | Slight negative for TSMC |
| 2026-04-16 | TSM Q1 2026 call | EMIB raised as packaging alternative | Neutral — acknowledged, not acute |
| 2026-04-16 | TSM Q1 2026 call | Intel Terafab noted | Neutral — early stage, 3-5yr timeline |
| 2026-04-16 | TSM Q1 2026 call | "No shortcuts" defense repeated | Positive for TSMC moat thesis |
| 2026-04-16 | TSM Q1 2026 call | TSMC confident in winning next-gen LPU | Positive — active competitive response |
| 2026-02-25 | NVDA Q4 FY2026 call | Groq licensing + team absorbed into NVDA | Neutral — competitive threat co-opted, not supply-chain relevant |
| 2026-02-25 | NVDA Q4 FY2026 call | LPU term absent from Vera Rubin enumeration | Informational — Samsung LPU win context remains unclear |
| 2026-02-25 | NVDA Q4 FY2026 call | NVDA dielet avoidance → large reticle-limited dies | Positive for TSMC — intensifies CoWoS demand |
| 2025-12-31 | TSM 20-F FY2025 | Competition section generic — no named competitors | Informational — Tier 1 legal conservatism vs. Tier 2 call candor |
| 2025-12-31 | TSM 20-F FY2025 | LPU term absent from 244-page Tier 1 filing | Informational — third source silent on LPU terminology |
| 2025 (Tier 3) | ASML-EUV research | ASML shipped 48 EUV systems in 2025 (up from 44 in 2024), including first High-NA | Positive for TSMC — frontier tool supply expanding |
| 2024-10-18 (Tier 3) | Reuters via ASML research | Samsung delayed Taylor fab EUV acceptance — lacked major customers | Negative for Samsung — EUV access ≠ EUV utilization |
| 2025-12 (Tier 3) | Intel via ASML research | Intel completed High-NA EUV (EXE:5200B) acceptance testing | Neutral — Intel 14A differentiation advancing but unproven in production |
| 2024 (Tier 3) | ASML Annual Report via research | 2024 was a "transition year" — fab push-outs, not all customers benefiting from AI equally | Informational — EUV constraint is cyclical, not monotonic |

**Net assessment (three primary sources + Tier 3 research):** TSMC's competitive position appears intact and is now framed by an additional upstream dimension: TSMC's installed-base lead in ASML EUV (~56% of global fleet, per external reconstruction) reinforces its downstream execution moat. Samsung's Taylor fab episode demonstrates that EUV access without customer pull does not translate into competitive pressure. Intel's High-NA strategy is the most differentiated competitive angle — earlier adoption at 14A — but remains unproven in production foundry volume. SMIC is structurally capped outside the EUV chain. The disconfirming signal ("TSMC's packaging advantage narrows") is not triggered by any source's evidence. The EUV dependency chain adds a new dimension: TSMC's advantage is partly derivative of being ASML's largest and most experienced downstream customer.

*Foundry-demand / disclosure-gap note ([[CSCO]] Q3 FY2026, S108):* Cisco's first named Silicon One hyperscaler design wins (P200 ×2 scale-across + G200 scale-out) plus a $16.0B purchase-commitment surge mark a large new leading-edge networking-silicon foundry-demand vector — yet the CSCO FY2025 10-K names **no foundry** for Silicon One (no TSMC, no foundry attribution anywhere). This is a Tier 1 foundry-attribution gap consistent with this page's Tier 1/Tier 2 disclosure-asymmetry thread (a major leading-edge silicon buyer disclosing zero foundry relationship). It does not bear on the "packaging advantage narrows" disconfirming signal — surfaced as a foundry-demand + disclosure-gap observation only.

## Change log

- **2026-04-19:** Created from TSM Q1 2026 earnings call (Tier 2). Covers Intel (Terafab, EMIB), Samsung (NVDA LPU win), OSAT dynamics, and TSMC's "no shortcuts" competitive defense.
- **2026-04-19:** Updated from NVDA Q4 FY2026 earnings call (Tier 2). Added LPU terminology update (term absent from NVDA call), Groq licensing to evidence tracker, NVDA dielet avoidance as CoWoS demand signal. Net assessment updated to reflect two-source view.
- **2026-04-19:** Updated from TSM 20-F FY2025 (Tier 1). Added Tier 1 vs. Tier 2 competitive disclosure observation (20-F competition section generic, less useful than Q1 call). Updated LPU terminology to three-source absence. Added two evidence tracker rows.
- **2026-04-20:** Updated from Tier 3 research (/raw/research/ASML-EUV-foundry-dependency.md). Added tiered EUV dependency chain section (TSMC deepest integration ~56% installed base, Samsung EUV-dependent but demand/yield often more binding, Intel differentiated by High-NA first-mover, SMIC outside EUV chain). Added EUV temporal nuance (2024 transition year, 2025-26 AI tightening). Added two-speed geopolitical dynamic (EUV blocked; active frontier is DUV/service restrictions). Added four evidence tracker rows. Net assessment updated to reflect upstream EUV dimension.
- **2026-05-28 (S99 cross-reference update — XFAB canonical creation):** Added "Specialty foundry sub-scope" section distinguishing mature/specialty-node foundry competition (TSEM + XFAB, no EUV dependency, customer-migration-cost moat, non-overlapping specializations) from leading-edge logic competition (TSM/Intel/Samsung). Added [[TSEM]] + [[XFAB]] to tickers per Section 3.2(b) provenance. Specialty-foundry sub-scope is a monitoring lane distinct from the `_thesis.md` packaging-advantage disconfirming signal.
- **2026-05-29 (S110 cross-vault re-evaluation propagation — A7):** Resolved the long-standing "Samsung manufactures NVDA's LPU" puzzle via cross-vault link to [[NVDA-platform-integration]] (Groq **LP30**, 3rd-gen LPU, Samsung-manufactured, GTC March 16 2026, absorbed via Dynamo) — epistemic hedge preserved; sharpens Samsung's read as an inference-accelerator win co-opted into the NVDA ecosystem, not a leading-edge-logic win. Added a CSCO Q3 FY2026 (S108) evidence-tracker row + foundry-demand/disclosure-gap note (first named Silicon One hyperscaler wins + $16.0B commitments, but zero foundry named at Tier 1). Added [[CSCO]] to tickers per Section 3.2(b) provenance. No change to the "packaging advantage narrows" disconfirming-signal assessment.
- **2026-06-29 (Tier-3 video datapoint — No Priors / Lip-Bu Tan, Intel CEO):** Added the Intel-CEO own-side view to the Intel subsection + a top evidence-tracker row — Tan confirms Intel is "very distant from TSMC" (~2030-32 catch-up; "trust business"), the doubled-down foundry decision, and the industrial-policy capital stack (US-gov + NVDA ~$5B + SoftBank). CONFIRMS the TSMC-moat verdict (the CEO admits the gap) — disconfirming signal untripped. `last_updated` unchanged (Tier-3, not a primary refresh).
