---
type: company
tickers: [GOOGL]
layer: outside
photonics_tier: outside
memory_tier: outside
energy_power_tier: outside
equipment_tier: outside
materials_tier: outside
last_updated: 2026-06-02
---

# GOOGL — Alphabet Inc.

## Thesis role

Alphabet is the vault's **second hyperscaler / demand-side page** ([[MSFT]], S112, was the first) and the **first ingest undertaken explicitly under the hyperscaler PAYER / SPENDER tracking program** — the set of companies that *fund* the AI-datacenter buildout the rest of the vault tracks downstream (program scope: [[MSFT]] + GOOGL + AMZN + META + ORCL + CRWV). MSFT is the program's founding member but predated the program framing — it was ingested for the [[software-AI-moat-durability]] research goal, with demand-side capex a secondary product; GOOGL is the first ingest whose *primary* purpose is the demand-side signal. It is ingested for two purposes: (1) as a **direct primary-source hyperscaler-CAPEX signal** feeding [[AI-demand-durability]] — Alphabet is one of the four hyperscalers underlying the ~$640-720B 2026 aggregate the chokepoint thesis depends on; and (2) as a **custom-silicon operator** (TPU + Axion) for [[hyperscaler-custom-ASIC]] and [[AI-agentic-CPU-orchestration-reemergence]]. It is *not* ingested as a supply-chain value-capture participant, and — unlike [[MSFT]]/[[NOW]]/[[PLTR]] — it is *not* on the [[software-AI-moat-durability]] application-layer scorecard (it is a hyperscaler/platform, not a seat/consumption/outcome SaaS name).

**Placement framing (honest-verdict, Section 2.1).** A hyperscaler sits *above* Layer 1 in `frameworks.md` v10.1 — it is the **demand source** (Framework 3 dependency map, which already lists "Alphabet 2026 $180-190B") and the **CAPEX deployer** (Framework 10 allocation starting point), not a position within the six supply-side value-capture layers. Alphabet therefore carries `layer: outside` and `outside` on all five per-domain tiers — it captures no supply-side chokepoint rent; it *funds* the chokepoints. This follows the [[MSFT]] demand-side precedent (and mirrors [[CEG]]'s first-generator off-framework handling).

**`frameworks.md` gap flag (for a future codification session; human-owned, not edited).** GOOGL is the fourth demand-side page (after MSFT + NOW + PLTR) to press the same gap: the framework has no dedicated "demand-side / hyperscaler / CAPEX-deployer" category, and `layer: outside` extends the `layer` field beyond its documented 1–6 range. The hyperscaler-as-custom-silicon-commissioner role (Alphabet designs TPUs, AVGO builds them) compounds the question. Raised here per Section 1.1; `frameworks.md` and `_thesis.md` were not edited.

## Financial snapshot

Two periods kept separate per Section 4.1 (no blending). **Section 2.11 N/A** — Alphabet is a calendar-year (December 31) filer; Q1 2026 = calendar Q1 2026, directly period-parity with vault peers.

**The equity-securities-gain caveat (read operating income as the clean performance metric).** In both periods, net income is materially inflated by below-the-operating-line gains on equity securities — unrealized fair-value remeasurements that flow through other income (expense), net (OI&E) under ASU 2016-01. CFO Anat Ashkenazi: the Q1 OI&E increase was "primarily due to unrealized gains in our non-marketable equity securities portfolio" (GOOGL Q1 2026 call). These gains are volatile and non-operating; operating income (+15% FY2025, +30% Q1 2026) is the cleaner read of the business than net income (+32% / +81%).

**FY2025 (10-K; year ended December 31 2025; vs FY2024):**

| Metric | FY2025 | FY2024 | YoY |
|---|---|---|---|
| Total revenue | $402.8B | $350.0B | +15% |
| Operating income | $129.0B | $112.4B | +15% |
| Operating margin | 32.0% | 32.1% | flat |
| Net income | $132.2B | $100.1B | +32% |
| Diluted EPS | $10.81 | $8.04 | +34% |
| Google Services revenue | $342.7B | $304.9B | +12% |
| Google Cloud revenue | $58.7B | $43.2B | +36% |
| Google Cloud operating income | $13.9B | $6.1B | +128% |
| Capex (purchases of P&E) | $91.4B | $52.5B | +74% |

**Q1 2026 (10-Q; quarter ended March 31 2026; call April 29 2026; vs Q1 2025):**

| Metric | Q1 2026 | Q1 2025 | YoY |
|---|---|---|---|
| Total revenue | $109.9B | $90.2B | +22% (+19% cc) |
| Operating income | $39.7B | $30.6B | +30% |
| Operating margin | 36.1% | 34% | +2 pts |
| Net income | $62.6B | $34.5B | +81% *(equity-gain-inflated)* |
| Diluted EPS | $5.11 | $2.81 | +82% |
| Gain on equity securities (in OI&E) | $36.9B | $9.8B | — *(non-operating)* |
| Google Services revenue | $89.6B | $77.3B | +16% |
| Google Cloud revenue | $20.0B | $12.3B | +63% |
| Google Cloud operating income | $6.6B | $2.2B | ~3x |
| Capex (purchases of P&E) | $35.7B | $17.2B | +107% |

## CAPEX & demand-durability

This is the section the hyperscaler-payer program exists to source — Alphabet's capex is a primary-source demand signal for the chokepoint thesis (cross-ref [[AI-demand-durability]] + the [[hyperscaler-capex]] payer-comparison tracker). Per the Q1 2026 10-Q + call:

- **Capex run-rate inflecting.** Q1 2026 purchases of property & equipment were **$35.7B, up +107% YoY** (from $17.2B); property & equipment, net rose from $246.6B to $281.0B in the quarter (GOOGL Q1 2026 10-Q). FY2025 capex was $91.4B (+74% YoY).
- **FY2026 guidance raised to $180–190B** (from $175–185B), with the raise attributed to "investment related to the acquisition of Intersect, which closed in March" (GOOGL Q1 2026 call) — Intersect Power being an energy/power asset, so the raise is partly an *energy-infrastructure* commitment, not only compute. Management cited "unprecedented internal and external demand for AI compute resources."
- **2027 capex guided to "significantly increase" vs 2026** (CFO Ashkenazi). At ~$90B → ~$185B → "significantly higher," Alphabet capex roughly doubled in 2026 and is set to step up again.
- **Energy as a named forward cost.** Ashkenazi flagged that scaling technical infrastructure "will continue to put pressure on the P&L in the form of higher depreciation expense and related data center operations costs, such as energy" (GOOGL Q1 2026 call) — a direct primary-source link from hyperscaler capex to the power/energy chokepoint.
- **Backlog as forward-demand proxy.** Total remaining performance obligations were **$467.6B, of which $462.3B is Google Cloud** ("nearly doubled quarter-on-quarter to over $460 billion" per Pichai); >50% expected to recognize as revenue over the next 24 months (GOOGL Q1 2026 10-Q). This is the demand-side mirror of the supply-side backlogs the rest of the vault reports.

The ~$180-190B Alphabet figure now primary-sources a second hyperscaler component of the ~$640-720B 2026 aggregate underlying [[AI-demand-durability]] (alongside [[MSFT]]'s ~$190B). Framework 10 (CAPEX flow) treats Alphabet as a top-of-diagram demand source.

## Google Cloud inflection

The standout of the quarter is Google Cloud reaching profitability scale, not just revenue growth:

- **Revenue $20.0B in Q1 2026, +63% YoY** — exceeding $20B for the first time (GOOGL Q1 2026 10-Q; call).
- **Operating income tripled to $6.6B** (from $2.2B), an operating margin of ~33% vs ~18% a year prior — revenue acceleration *and* margin expansion simultaneously (GOOGL Q1 2026 10-Q). FY2025 Cloud operating income had already grown +128% to $13.9B.
- **Enterprise AI is now the primary Cloud growth driver** "for the first time" (Pichai); revenue from products built on Alphabet's GenAI models grew nearly **800% YoY**; 330 Cloud customers each processed >1T tokens over the trailing 12 months (35 exceeded 10T) (GOOGL Q1 2026 call).
- **Wiz** (cloud security) closed in March, reported within the Google Cloud segment; management guided a low-single-digit-percentage-point headwind to Cloud operating margin for the remainder of 2026 from the acquisition (GOOGL Q1 2026 call). The Wiz + Intersect acquisitions drove goodwill from $33.4B to $57.8B and intangibles from $1.3B to $9.4B in the quarter (GOOGL Q1 2026 10-Q).

## Custom silicon — TPU + Axion

Alphabet operates the vault's most mature hyperscaler custom-silicon program, now primary-source-confirmed (previously tracked counterparty-side via [[AVGO]] and Tier-3 via the [[ARM]] letter):

- **8th-generation TPUs.** TPU 8t (training; "three times the processing power of Ironwood and two times the performance") + TPU 8i (inference; "80% better performance per dollar than the prior generation") (GOOGL Q1 2026 call). Cross-ref [[hyperscaler-custom-ASIC]].
- **Axion** — Alphabet's Arm-based server CPU, now the **host CPU for TPU 8t and TPU 8i, replacing x86 host processors** (GOOGL Q1 2026 call). This primary-confirms the Axion role previously documented counterparty-side on [[AI-agentic-CPU-orchestration-reemergence]] (sourced from the ARM Q4 FY2026 letter).
- **NVIDIA alongside in-house.** Pichai framed "custom TPUs, Axion CPUs, and the latest NVIDIA GPUs" as "the industry's widest variety of compute options," and said Alphabet will be "among the first to offer NVIDIA Vera Rubin NVL72" (GOOGL Q1 2026 call) — the multi-architecture procurement pattern documented at [[AI-agentic-CPU-orchestration-reemergence]] (Google quad-architecture: Axion + Xeon + NVIDIA + TPU).
- **External TPU sales — a strategic shift.** Alphabet will "begin to deliver TPUs to a select group of customers in their own data centers" (Pichai; Ashkenazi), moving TPU from captive silicon toward a merchant-ish hardware offering. Named external TPU users include Thinking Machines Lab, Hudson River Trading, and Boston Dynamics. Revenue is expected to be a small percent in 2026 with the majority realized in 2027, and lumpy by shipment timing (GOOGL Q1 2026 call). AVGO is Alphabet's TPU design/manufacturing partner — see Source audit notes for the [[AVGO]] reciprocal-confirmation.

## AI monetization & Search

- **Gemini.** 350M paid subscriptions across consumer AI plans (YouTube + Google One the key drivers); Gemini Enterprise paid monthly active users +40% QoQ; first-party models now process >16B tokens/minute via direct API, up from 10B last quarter (GOOGL Q1 2026 call).
- **Search.** "AI continues to drive search usage and queries are at an all-time high"; AI Overviews and AI Mode drive incremental usage; cost of core AI responses is down >30% since upgrading to Gemini 3, "thanks to continued hardware and engineering breakthroughs" (GOOGL Q1 2026 call). Search & other revenue grew to $60.4B in the quarter (GOOGL Q1 2026 10-Q).
- **Embedded-AI disclosure gap.** As with [[MSFT]], there is no discrete Tier-1 "AI revenue" line — AI monetization is embedded in Search/Services and Google Cloud. The 800%-GenAI-products, token-throughput, and Gemini-subscription figures are call-only (Tier 2). See Source audit notes.

## Open questions

1. **Placement codification.** Does the vault add an explicit hyperscaler / demand-side framework category (and resolve the `layer: outside` extension)? Now pressed by four demand-side pages (MSFT + NOW + PLTR + GOOGL). Pre-registered for a future codification session.
2. **Clean AI revenue line.** Does a discrete Tier-1 AI/Gemini revenue line ever appear, or does it remain embedded in Search + Cloud?
3. **Cloud margin trajectory.** Does the ~33% Cloud operating margin hold and expand as scale builds, net of the Wiz headwind — or does enterprise-AI mix pressure it?
4. **External-TPU-sales scale + NVDA competition.** How large does merchant TPU delivery become in 2027, and does selling TPUs into customers' own datacenters intensify Alphabet's competition with [[NVDA]] (and deepen the [[AVGO]] partnership)?
5. **Capex ROIC at $180-190B + the 2027 step-up.** Pichai repeatedly invoked a "robust ROIC framework" for allocating constrained compute; does the returns case hold as capex roughly doubles again? (The demand-durability timing risk — capex deployed ahead of monetization — applies here as it does to [[MSFT]].)
6. **Equity-securities-gain volatility.** Reported net income / EPS will swing with the marked-to-market equity portfolio; the operating line is the durable comparison.

## Source audit notes

- **Equity-securities-gain net-income inflation.** Q1 2026 net income (+81%) and diluted EPS (+82%) are materially inflated by a $36.9B gain on equity securities recorded in OI&E (vs $9.8B a year prior; OI&E net +237% to $37.7B). CFO attributed it to "unrealized gains in our non-marketable equity securities portfolio." Operating income (+30%) is the clean performance metric; the page presents net income with this caveat rather than as a clean result. FY2025 net income (+32% vs +15% operating income) reflects the same dynamic.
- **Tier-1/Tier-2 framing gap (Section 3.4; "filings omit commercial detail calls disclose" sub-pattern) — mild/moderate.** The capex guidance ($180-190B), GenAI-product growth (~800%), token throughput, Gemini subscription counts, TPU 8t/8i specs, and the external-TPU-sales plan are disclosed only on the **call**; the 10-Q embeds AI in Cloud + Services with no discrete line. The Google Cloud backlog ($462.3B) *is* in the 10-Q. Documented as a tier-asymmetric gap; no contradiction (the call amplifies the filings).
- **[[AVGO]] reciprocal-confirmation (A1 reciprocal-confirmation).** AVGO names Google as its lead XPU customer ("7th-gen Ironwood TPU; stronger demand from next-gen TPUs in 2027+," AVGO Q1 FY2026 call). GOOGL primary now reciprocally confirms the TPU program (TPU 8t/8i + Axion host CPU + external sales) — the counterparty-side disclosure is bilaterally confirmed. Propagated to [[hyperscaler-custom-ASIC]].
- **CEO/management tone.** Pichai, CBO Philipp Schindler, and CFO Anat Ashkenazi were measured and confident; no combativeness. In Q&A, Brian Nowak (MS) pressed on Search ROIC and TPU third-party pricing strategy (answered directly); Justin Post (BofA) asked about AI-deal margins with generative-AI companies — Pichai declined to comment on specific contracts but cited the "robust ROIC framework" (measured deflection, not combative). **CEO-combativeness count UNCHANGED (Section 3.7).**

## Change log

- **2026-06-02 (S115 — creation):** First-canonical ingest from FY2025 10-K (Tier 1) + Q1 2026 10-Q (Tier 1) + Q1 2026 call (Tier 2; Apr 29 2026). First ingest under the hyperscaler PAYER/SPENDER program (2nd hyperscaler page after [[MSFT]]; 4th demand-side page overall, after MSFT/NOW/PLTR). Placement `layer: outside` + all `*_tier outside` (demand source / CAPEX deployer; per [[MSFT]] precedent); frameworks demand-side gap re-flagged (not edited). Section 2.11 N/A (calendar FY). Verified financials direct from the income statements (FY2025 rev $402.8B / op income $129.0B / net income $132.2B / EPS $10.81 / capex $91.4B; Q1 2026 rev $109.9B / op income $39.7B / net income $62.6B / EPS $5.11 / capex $35.7B), with the $36.9B equity-securities-gain net-income-inflation caveat. CAPEX watch (Vic standing request): FY2026 guidance raised to $180-190B (incl. Intersect/energy), 2027 "significantly increase," Cloud backlog $462.3B, energy named as forward cost. Google Cloud inflection (rev $20.0B +63%; op income tripled to $6.6B). TPU 8t/8i + Axion + external-TPU-sales shift primary-confirmed; [[AVGO]] reciprocal-confirmation. NOT on the [[software-AI-moat-durability]] scorecard (hyperscaler, not app-layer SaaS). CEO-combativeness UNCHANGED at 2. Cross-vault propagation: [[AI-demand-durability]] (capex subsection + ticker) + [[hyperscaler-custom-ASIC]] (TPU subsection + ticker) + [[AI-agentic-CPU-orchestration-reemergence]] (Axion primary-confirmation + ticker) + [[AVGO]] (wikilink).
