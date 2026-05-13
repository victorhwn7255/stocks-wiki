---
type: theme
tickers: [NVDA, COHR, LITE, GLW, VRT, ANET]
last_updated: 2026-04-28
---

# NVDA Platform Integration Pattern

## Thesis relevance

This page tracks how [[NVDA]] maintains its Layer 1 platform definer status through a distinctive pattern: absorbing best-in-class technologies through licensing, equity investments, and acquisitions rather than building everything internally. The pattern explains NVDA's platform stickiness and has direct implications for the thesis — each absorption deepens ecosystem lock-in, co-opts potential competitive threats, and partially internalizes supply chain dependencies.

The term "platform integration" is deliberate. NVDA is not vertically integrating — it does not manufacture chips, build fabs, or assemble systems. Instead, it extends its platform layer to encompass adjacent capabilities, maintaining architectural control while depending on [[TSM]] for physical manufacturing. The distinction matters: NVDA's power comes from platform control, not production control.

## The pattern

### Mellanox (acquired April 2020, ~$6.9B)

**What was absorbed:** InfiniBand networking and high-speed interconnect technology.

**What it became:** NVLink scale-up fabric and Spectrum-X scale-out networking. Full-year FY2026 networking revenue reached $31B — 10x the level at the time of the Mellanox acquisition (NVDA Q4 FY2026 call). Networking generated $11B in Q4 alone, up 3.5x YoY.

**Pattern significance:** Mellanox established the playbook. NVDA acquired a best-in-class technology in an adjacent domain (networking), integrated it into the platform, and turned it into a major growth vector. Jensen explicitly uses Mellanox as the framing analogy for subsequent moves.

**Integration timeline (per /raw/research/NVDA-absorb-extend-history.md, citing NVIDIA press releases and CFO commentary, 2019–2025):** Announced March 11, 2019; closed April 27, 2020 after regulatory approvals. Mellanox contributed 14% of NVDA revenue in its first quarter as part of NVIDIA (Q2 FY2021), confirming immediate operational integration rather than passive subsidiary treatment. However, networking revenue was not separately disclosed as its own line item until Q1 FY2025 ($3.2B) — four years after operational integration. The gap between operational absorption (2020) and public financial narration (2024) is itself a pattern signal: NVDA integrates first and narrates later, surfacing acquired capabilities as distinct revenue lines only once they reach scale significant enough to support an independent growth story.

### Groq (licensing + engineering team, February 2026)

**What was absorbed:** Low-latency inference technology via non-exclusive licensing agreement. Engineering team joined NVIDIA.

**What it will become:** At GTC (March 16, 2026), Jensen disclosed LP30 — the third-generation LPU, manufactured by Samsung. NVIDIA Dynamo is the disaggregated inference platform that separates decode (LP30) from prefill and attention (Blackwell GPUs), orchestrated through software. Jensen: "we'll extend our architecture with Groq as an accelerator in very much the ways that we extended NVIDIA's architecture with Mellanox" (NVDA Q4 FY2026 call). Dynamo is the integration framework: the LP30 is absorbed into the NVDA platform as a specialized accelerator, not operated independently (NVDA GTC March 16, 2026).

**Pattern significance:** The Groq deal is notable for both what it represents and what it reveals:
- *Platform strength:* NVDA absorbs a competitive threat (Groq's LPU was demonstrably better at low-latency decoding) by incorporating it into the platform rather than competing head-on.
- *Architectural non-optimality:* The fact that NVDA needed to license Groq's technology is evidence that NVDA's GPU architecture is not universally optimal for all inference workloads. Groq's LPU design was genuinely superior at low-latency decoding — specialized enough that NVDA chose to license rather than replicate. The wiki should hold both of these interpretations rather than selecting one.

C.J. Muse (Cantor Fitzgerald) asked directly whether NVDA should be "thinking about customized silicon either by workload or customer, as an increasing focus by NVIDIA" (NVDA Q4 FY2026 call). Jensen's response emphasized CUDA versatility and the "dielet tax" on competitors, but did not directly reject workload-specific silicon — leaving the strategic direction open.

### COHR and LITE (equity investments, March 2, 2026)

**What was absorbed:** $2B equity stake in each, plus multi-year strategic agreements, multi-billion dollar purchase commitments, and future capacity access rights for advanced laser components (per frameworks.md, announced March 2, 2026 — not from NVDA Q4 FY2026 call, which preceded the announcement by one week).

**What it represents:** NVDA is actively vertically securing its laser supply chain for the photonics roadmap. Both COHR and LITE are Layer 4 differentiated component suppliers. The investments pull them structurally closer to the NVDA platform ecosystem — from independent merchant suppliers to equity-aligned supply chain partners.

**Pattern significance:** This is a different modality from Mellanox (acquisition) and Groq (licensing). The equity-plus-purchase-commitment structure secures supply without requiring full acquisition. It signals that NVDA's photonics roadmap is concrete enough to warrant multi-billion dollar supply commitments, even though NVDA's primary commentary (the Q4 FY2026 call, one week earlier) did not discuss CPO or photonics at all. See [[CPO-platform-battle]].

**LITE-side perspective (from LITE Q2 FY2026 call, February 3, 2026):** [[LITE]]'s management did not name NVDA directly (the call predated the March 2 announcement by one month), but Hurlston disclosed "active negotiations with leading customers to offset our capital requirements in exchange for long-term supply assurances" (LITE Q2 FY2026 call). This framing characterizes the investment as a transactional arrangement — capital enablement for capacity expansion — rather than the strategic platform integration frame NVDA would later apply. LITE's precursor language emphasizes the capital constraint it was solving: H1 FY2026 free cash flow was ~$24.8M against ~$320M annualized capex.

**COHR-side perspective (from COHR Q2 FY2026 call, February 4, 2026):** [[COHR]]'s Anderson disclosed "a number of long-term supply agreements that we've either signed with customers or in the process of signing" with "often some sort of financial commitment from our customers, like investment for CapEx" (COHR Q2 FY2026 call). Anderson later described the deal as "an expansion of a more than 20-year relationship" (per March 2, 2026 NVDA/COHR press release — not from the three ingested COHR sources). COHR's precursor language emphasizes customer commitment and demand visibility rather than capital constraint — COHR had $634M operating cash flow against $441M capex in FY2025, a healthier self-funding position than LITE's.

**The perspectival comparison is thesis-significant.** Both companies disclosed investment negotiations on consecutive days covering the same quarter, but framed them differently:
- LITE: "offset our capital requirements in exchange for supply assurances" — investment fills a capital gap
- COHR: "financial commitment from our customers, like investment for CapEx" — investment formalizes demand-side commitment

Both framings are factually consistent: the same capital flow enables capacity expansion (supplier need) and secures supply access (NVDA's need). The perspectival gap reflects structural differences: LITE is capital-constrained and needed the investment; COHR has stronger cash generation and framed it as relationship formalization. See [[LITE]], [[COHR]], and [[datacenter-laser-supply]] for the full analyses.

### Ayar Labs (equity backing)

**What was absorbed:** Equity investment in silicon photonics startup. Ayar Labs is also backed by AMD (per frameworks.md).

**Pattern significance:** Ayar Labs is a silicon photonics design company — a potential component of future CPO platforms. NVDA's backing positions it to access Ayar's technology if the silicon photonics startup landscape consolidates. `_thesis.md` identifies a disconfirming signal here: if Ayar Labs or Lightmatter gets acquired by hyperscalers rather than merchant platform players, the open CPO platform thesis weakens.

### [[GLW]] (named ecosystem partner — counterparty-attribution-only)

**What was named:** [[GLW]] (Corning) was named as an ecosystem partner for NVDA's Spectrum-X / Quantum-X photonics switches in NVDA's March 2025 Spectrum-X Photonics announcement, alongside [[COHR]], [[LITE]], Foxconn, SENKO, and [[TSM]]. Tier 3 sources additionally characterized GLW as participating in CPO detachable fiber-to-chip interface co-development with GlobalFoundries and multicore-fiber collaboration with Sumitomo Electric.

**What is structurally different:** No NVDA equity investment. No multi-year purchase commitment disclosed. No licensing arrangement. The relationship is documented only through NVDA-side ecosystem-partner naming, not through one of the four absorption modalities (acquisition / licensing / equity-plus-purchase / equity-backing) above.

**Counterparty-attribution-only finding (Session 20).** GLW primary sources through Q4 2025 (10-K FY2025, 10-Q Q3 2025, Q4 2025 earnings call) do not reciprocally confirm NVDA-named ecosystem partner status, do not name NVDA outside a board-of-directors biography (Ms. Badani's prior employment), and do not document Spectrum-X / Quantum-X / GlobalFoundries / SENKO / Sumitomo / co-packaged / CPO partnerships. The Tier 3-derived ecosystem-partner narrative for Corning relies primarily on NVDA-side March 2025 announcement attribution, not target-company reciprocal confirmation. See [[datacenter-photonics-supply-chain]] Section 2.4 and the Open questions section for the cross-validation finding and the counterparty-attribution-only annotation discipline convention codification candidate.

**Pattern significance:** "Named in counterparty announcement" is structurally distinct from the four absorption modalities above. NVDA's platform integration pattern documented on this page is reflexively reciprocal — Mellanox, Groq, COHR/LITE, Ayar Labs all involve commercial transactions that both parties disclose. The GLW relationship is a different category: NVDA-side naming without reciprocal target-company commercial disclosure. Whether this category becomes more populated as additional Tier 3 ecosystem-partner claims surface in future ingests is open.

### [[VRT]] (named ecosystem partner — reciprocal-confirmation, technology development collaboration without equity)

**What was named and reciprocally confirmed:** [[VRT]] (Vertiv) is named as an NVIDIA ecosystem partner in NVDA Spectrum-X / AI factory venues. The partnership is **reciprocally confirmed in VRT primary sources at Tier 1 level** — VRT 10-K FY2025 Item 7 Outlook and Trends Strategic Partnerships subsection: "Our partnership with NVIDIA supports the development of advanced power and thermal infrastructure aligned with next-generation AI and high-performance computing architectures" (VRT 10-K FY2025).

**What is structurally different from the four absorption modalities:** No NVDA equity investment. No multi-year purchase commitment disclosed. No licensing arrangement. No acquisition. The relationship is **technology development collaboration** — joint development of "advanced power and thermal infrastructure aligned with next-generation AI and HPC architectures" — bilaterally documented but not reduced to a commercial transaction with NVDA equity, debt, or contractual purchase commitments at the modality level.

**What is structurally different from [[GLW]] counterparty-attribution-only:** Bilateral confirmation in target-company primary sources (Tier 1 level disclosure). Specific deployment example documented:

- VRT Q1 2026 earnings call (April 22, 2026), Albertazzi: "EMEA is absolutely part of the AI story, and we're seeing that play out with customer projects like EcoDataCenter in Sweden, designed to support the most demanding AI workloads with NVIDIA's latest generation Vera Rubin GPUs. **Vertiv OneCore was selected to deliver the full data center solution here, encompassing power, thermal, IT white space, and services**" (VRT Q1 2026 call).

This is the **first vault primary-source confirmation of NVIDIA Vera Rubin commercial deployment timing** — forward-looking data point relevant to future [[NVDA]] refresh sessions.

**Counterparty-attribution-only annotation discipline application — reciprocal-confirmation mode (third structural mode, Session 22 origination).** The discipline applies in three modes per the framing established Sessions 20-22 and codification-ready per Session 23 handoff. Vertiv is the first vault instance of reciprocal-confirmation mode. Annotation form: "named in NVIDIA Spectrum-X / AI factory ecosystem-partner venues; reciprocally confirmed in VRT 10-K FY2025 Item 7 Outlook and Trends Strategic Partnerships disclosure with EcoDataCenter Sweden Vera Rubin deployment example per Q1 2026 earnings call." See [[datacenter-photonics-supply-chain]] Section 2.8 and Vault-conflict reconciliations applied subsection for the three-mode framing.

**Pattern significance — sixth integration category, second non-absorption category.** Vertiv expands the integration framework along an axis distinct from both the four absorption modalities and from GLW counterparty-attribution-only. Structural taxonomy axes useful for future tracking:

| Modality | Equity? | Bilateral confirmation? | Commercial integration? |
|---|---|---|---|
| 1. Mellanox-style acquisition | N/A (full ownership) | Yes | Full (operational integration) |
| 2. Groq-style licensing + team | No | Yes | Substantial (license + acqui-hire) |
| 3. COHR/LITE-style equity + purchase | Yes (minority) | Yes | Substantial (equity + multi-year purchase commitments) |
| 4. Ayar Labs-style equity backing | Yes (minority) | Yes (with caveats) | Investment-level (equity, no acquisition) |
| 5. GLW counterparty-attribution-only | No | **No (asymmetric)** | Disclosed only on counterparty side |
| **6. VRT reciprocal-confirmation, technology development** | **No** | **Yes** | **Technology development collaboration; no equity, no purchase commitment, but bilaterally documented** |

The sixth modality fills a category that the original four absorption modalities did not anticipate: bilateral partnership without equity or commercial transaction commitment, documented as joint technology development. Whether this category becomes more populated as additional Tier 3 ecosystem-partner claims are cross-validated against target-company primary sources is open. Per the architecture primer's broader observation that "denser optical I/O and CPO do not live in isolation; they only scale when cooling, power delivery, and test workflows scale with them," Vertiv's reciprocal-confirmation modality is structurally consistent with NVIDIA needing thermal/power infrastructure ecosystem participation without absorbing the supplier into the equity stack.

### Model builder ecosystem investments

The Q4 FY2026 call referenced multiple model builder partnerships (NVDA Q4 FY2026 call):
- Anthropic: $10B investment, training on Grace Blackwell + Vera Rubin
- OpenAI: partnership agreement described as "close"
- Meta: deploying millions of GPUs + Spectrum-X; $10B infrastructure
- xAI: partnership referenced

These are a different category from the technology absorptions above — they are ecosystem investments that deepen platform lock-in at the customer layer rather than the technology layer. They ensure that the leading AI model builders are trained on and optimized for NVIDIA infrastructure, making platform switching increasingly costly.

## Pattern decomposition: control-driven vs. coordination-driven

The individual entries above decompose into two structurally distinct categories (per /raw/research/NVDA-absorb-extend-history.md):

**Control-driven absorption.** NVDA tends to fully absorb software and networking control points that materially extend the performance or programmability of its platform. Mellanox (high-speed interconnect → NVLink/Spectrum-X), Cumulus Networks (network OS → Spectrum switch software layer), Bright Computing (cluster management → Base Command Manager), Run:ai (GPU orchestration → AI Enterprise/Mission Control), and OmniML (model optimization → TensorRT Model Optimizer) all follow this pattern. In each case, NVDA acquired the company outright, operationally folded the technology into its platform stack, and eliminated the target as an independent actor — often retaining the product brand while absorbing the corporate entity (per /raw/research/NVDA-absorb-extend-history.md, citing NVIDIA announcements and product documentation, 2019–2026).

**Coordination-driven financing.** NVDA tends to take minority positions in suppliers, cloud partners, and ecosystem builders when capital, capacity, and roadmap influence matter more than legal control. CoreWeave ($2B, AI infrastructure capacity), Applied Digital (infrastructure financing), Nebius ($2.7B total, hyperscale AI cloud), Recursion ($50M, biotech compute), and Ayar Labs (optical I/O co-development) all remained independent after NVDA investment. The investments deepened commercial dependencies without triggering full integration — NVDA gained supply assurance, ecosystem leverage, and roadmap influence without operational control (per /raw/research/NVDA-absorb-extend-history.md, citing primary filings and press releases, 2022–2026). SoundHound is a useful falsifying case: NVDA disclosed a public-equity position, partnered technically, then exited the stake entirely — demonstrating that not all minority investments are permanent ecosystem commitments (per /raw/research/NVDA-absorb-extend-history.md, citing NVIDIA 13F and Barron's/Reuters reporting, 2024–2025).

The structural dividing line is control over execution versus coordination with suppliers and partners. When NVDA needs tighter product integration, software control, and architectural coherence, it buys outright. When it needs capacity, ecosystem expansion, or manufacturing leverage, it finances.

### Arm: the exception that sharpens the rule

The Arm acquisition attempt (announced September 2020, terminated February 2022 after CMA and FTC opposition) is the structurally central exception. NVDA did not settle for a minority position — it attempted full ownership of a foundational CPU dependency at ~$40B. The termination resulted from external regulatory opposition, not internal strategic preference. This matters for calibrating the pattern: NVDA's disposition is not "always choose minority positions for dependencies." When a dependency is strategically central enough and practically acquirable, NVDA has demonstrated willingness to attempt full absorption. What stopped the Arm pattern was regulation, not restraint (per /raw/research/NVDA-absorb-extend-history.md, citing NVIDIA/SoftBank announcements and CMA/FTC statements, 2020–2022).

### Expected trajectory for Lumentum and Coherent

On the historical record, the [[LITE]] and [[COHR]] investments structurally resemble the coordination-driven financing pattern — specifically the Ayar Labs/CoreWeave/Nebius precedents — rather than the Mellanox control-driven absorption pattern. The deal structures are minority financings ($2B each), not merger agreements. The commercial terms emphasize nonexclusive supply, multibillion-dollar purchase commitments, future capacity rights, and U.S.-based manufacturing support — hallmarks of ecosystem financing used to secure throughput and influence roadmaps in a supply-constrained market (per /raw/research/NVDA-absorb-extend-history.md, citing Lumentum 8-K and Coherent 8-K, March 2, 2026).

**Default expectation:** Continued strategic collaboration rather than near-term absorption. The relationships will likely deepen via escalating purchase commitments, capacity agreements, and roadmap alignment without control transactions.

**Falsification criteria:** If NVDA announces intent to acquire either [[LITE]] or [[COHR]] within 12–18 months of the March 2026 investments, this pattern analysis is falsified — the investments were acquisition precursors, not ecosystem financing. If the relationships continue deepening commercially without control transactions through mid-2027, the pattern holds.

**Caveat from the Arm precedent:** The pattern analysis does not rule out later escalation. If optics were to become as central to NVDA's platform differentiation as high-performance fabric became by 2019, and if one of these suppliers became both strategically indispensable and practically acquirable, the Arm/Mellanox side of the pattern says NVDA has the organizational disposition to seek deeper control. The current documentation does not support that reading — but the Arm case demonstrates that the boundary between coordination and control is structural, not permanent (per /raw/research/NVDA-absorb-extend-history.md).

## What this means for the thesis

1. **Each absorption strengthens ecosystem lock-in.** The platform becomes broader and stickier with each integration. Customers who build on NVLink + Spectrum-X + CUDA + Groq inference are more locked in than customers on CUDA alone.

2. **Competitive threats get co-opted rather than fought.** The Groq deal is the clearest example — rather than losing inference market share to a specialized competitor, NVDA absorbs the technology. This is a pattern available primarily to platform definers with the scale and ecosystem to make integration valuable.

3. **Supply chain dependencies get partially internalized.** The COHR/LITE investments reduce (but do not eliminate) NVDA's exposure to merchant laser supply volatility. The TSMC packaging dependency remains unaddressable through equity investment — there is no alternative provider. However, NVDA's co-development of COUP/COUPE packaging technology with TSMC (disclosed at GTC March 16, 2026) represents a different integration modality: joint technology creation rather than equity or acquisition. Jensen claimed NVDA and TSMC "invented the process technology" together (NVDA GTC March 16, 2026 — attributed per rhetorical claims convention). If accurate, this deepens the bilateral dependency: NVDA gains preferential access to a co-developed packaging technology, while TSMC gains a lead customer for a new platform offering. This makes [[TSM]] simultaneously a structural chokepoint and a co-development partner.

4. **The pattern has limits.** NVDA cannot absorb TSMC. It cannot absorb ASML. It cannot absorb the memory oligopoly. The platform integration pattern works for technology and supply chain components where alternatives exist and where NVDA's platform scale creates leverage. It does not work for Layer 2 infrastructure monopolies, which is why the NVDA-TSM dependency remains the most critical structural relationship in the thesis.

## Cross-references

- [[datacenter-photonics-supply-chain]] — Section 2.1 (Lasers) and Section 3 Bucket B (Optical device stacks) for the COHR/LITE March 2026 investments in the broader optical device stack context; Section 2.6 for the COUP/COUPE TSMC co-development modality.
- [[chokepoint-investability-priorities]] — Tier 3-anchored vault-canonical reference for 13-chokepoint photonics framework (created Session 25, A2 first canonical application). Chokepoint 7 (Switch ASIC / platform architecture) cross-references the six integration modalities documented on this page as operational mechanism through which NVDA full control-point authority (per `frameworks.md` v8 Framework 2.6) is exercised.
- [[ANET]] — vault company (Session 27 paired ingest with [[CRDO]]). Per Q4 2025 call: "We interoperate with NVIDIA, the recognized worldwide market leader in GPUs" (Jayshree Ullal). ANET-side counterparty-attribution-only mode framing of NVDA platform leadership; bilateral cross-validation pending. ANET is fifth member of Framework 2.6 control-point thread (NVDA / AVGO / MRVL / CSCO / ANET) — bottleneck participant with platform-tier ambition tier alongside [[CSCO]]. Distinct from the six integration modalities documented on this page: ANET represents an ecosystem-partner-without-equity relationship at the Layer 5 systems integrator tier rather than a platform-integration acquisition / licensing / equity / counterparty-attribution / reciprocal-confirmation modality. Structural co-location at AI networking ecosystem level; no NVDA-side equity / purchase commitment / licensing disclosed.

## Change log

- **2026-04-19:** Created from NVDA Q4 FY2026 earnings call (Tier 2) and frameworks.md. Documents four modalities of platform integration: acquisition (Mellanox), licensing (Groq), equity + purchase commitments (COHR/LITE), and equity backing (Ayar Labs), plus model builder ecosystem investments.
- **2026-04-19:** Updated from LITE Q2 FY2026 earnings call (Tier 2). Added LITE-side perspective on the equity investment: "capital offset in exchange for supply assurance" framing vs. NVDA's "vertically securing laser supply chain." Cross-validated dual framing preserved without adjudication.
- **2026-04-19:** Updated from COHR Q2 FY2026 earnings call (Tier 2) and March 2, 2026 press release context. Added COHR-side perspective: "financial commitment from customers" framing and "20-year relationship expansion." Three-way perspectival comparison now complete (NVDA/LITE/COHR).
- **2026-04-20:** Updated from Tier 3 research (/raw/research/NVDA-absorb-extend-history.md). Added pattern decomposition (control-driven absorption vs. coordination-driven financing with five examples each), Mellanox integration timeline precision (14% of Q2 FY2021 revenue; networking as separate line only from Q1 FY2025), Arm as structurally central exception (attempted full acquisition blocked by regulation), and forward-looking prediction for LITE/COHR with falsification criteria (12–18 month acquisition test).
- **2026-04-26:** Updated from NVDA GTC March 16, 2026 keynote (Tier 2). Groq section updated: LP30 (third-generation LPU) — Samsung manufacturing, Dynamo disaggregated inference platform, LP30 absorbed as specialized accelerator. COUP/TSMC co-development mechanism added to thesis implications (joint technology creation as distinct integration modality beyond equity or acquisition).
- **2026-04-27:** Session 19 cross-reference. Added Cross-references section linking [[datacenter-photonics-supply-chain]].
- **2026-04-27 (Session 20 ingest):** Added [[GLW]] subsection documenting counterparty-attribution-only ecosystem-partner status (named in NVDA's March 2025 Spectrum-X Photonics announcement; no NVDA equity / purchase commitment / licensing; not reciprocally confirmed in GLW primary sources through Q4 2025). Distinguished from the four absorption modalities (acquisition / licensing / equity-plus-purchase / equity-backing). New observation type: "named in counterparty announcement without reciprocal target-company commercial disclosure." [[GLW]] added to tickers.
- **2026-04-27 (Session 22 ingest):** Added [[VRT]] subsection documenting **sixth integration modality — reciprocal-confirmation, technology development collaboration without equity**. NVIDIA partnership reciprocally confirmed at Tier 1 level (VRT 10-K FY2025 Item 7 Outlook and Trends Strategic Partnerships) plus Tier 2 deployment specificity (Q1 2026 call EcoDataCenter Sweden Vera Rubin + Vertiv OneCore selected for full DC solution). Sixth modality is the second non-absorption category, structurally distinct from both the four absorption modalities and from [[GLW]] counterparty-attribution-only — bilateral confirmation without equity, purchase commitment, or acquisition commercialization. Three-mode counterparty-attribution-only annotation discipline framing introduced (over-claim + inversion + reciprocal-confirmation), with VRT as first reciprocal-confirmation mode instance. Structural taxonomy table added to position the six modalities along equity / bilateral confirmation / commercial integration axes. First vault primary-source confirmation of NVIDIA Vera Rubin commercial deployment timing (EcoDataCenter Sweden). [[VRT]] added to tickers.
- **2026-04-28 (Session 27 paired ingest — [[ANET]] cross-reference addition):** Cross-references section updated to add [[ANET]] entry. ANET-side framing of NVIDIA as "the recognized worldwide market leader in GPUs" documented (Jayshree Ullal Q4 2025 call) — counterparty-attribution-only mode pending bilateral cross-validation. ANET represents an ecosystem-partner-without-equity relationship at Layer 5 systems integrator tier; structurally distinct from the six integration modalities (acquisition, licensing, equity-plus-purchase, equity-backing, counterparty-attribution-only, reciprocal-confirmation). No new modality introduced; ANET noted as in-vault control-point thread fifth-member completion via Framework 2.6 placement (bottleneck participant with platform-tier ambition). [[ANET]] added to tickers.
- **2026-04-30 (Session 32 cross-reference — [[cpo-integration]] chokepoint page creation):** New chokepoint page [[cpo-integration]] cross-references this theme page in its NVDA per-company integration positioning section + COUPE platform integration subsection. Six-modality framework operationalized at CPO chokepoint: NVDA + TSM joint co-development modality (COUPE) + NVDA + LITE/COHR equity-plus-purchase modality ($2B March 2026 capital-offset-for-supply-assurance) + counterparty-attribution-only + reciprocal-confirmation modes annotated throughout chokepoint page per A1 three-mode framing. ELS architecture preservation of Layer 4 component-tier value through CPO transition documented as chokepoint mechanism — operationalizes equity-plus-purchase modality at scale-up CPO timing. No content edits to this theme page; cross-reference relationship now bidirectional via chokepoint page Cross-references section.
