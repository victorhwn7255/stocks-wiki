---
type: company
tickers: [MSFT]
layer: outside
photonics_tier: outside
memory_tier: outside
energy_power_tier: outside
equipment_tier: outside
materials_tier: outside
last_updated: 2026-06-02
---

# MSFT — Microsoft Corporation

## Thesis role

Microsoft is the vault's **first hyperscaler / demand-side company page**, ingested for two purposes: (1) as a **demand-side anchor** for calibrating supply-chain chokepoint exposure — MSFT is the source of the CAPEX flow the rest of the vault tracks downstream; and (2) as the **first primary-source test of the [[software-AI-moat-durability]] research goal** (which software moats AI amplifies vs. erodes). It is *not* ingested as a supply-chain value-capture participant.

**Placement framing (honest-verdict, Section 2.1).** A hyperscaler sits *above* Layer 1 in `frameworks.md` v10.1 — it is the **demand source** (Framework 3 dependency map, which already lists "MSFT FY26 $190B+") and the **CAPEX deployer** (Framework 10 allocation starting point), not a position within the six supply-side value-capture layers. The framework's layers and per-domain tiers describe value capture *to* the hyperscaler, not the hyperscaler's own supply-side position. MSFT therefore carries `layer: outside` and `outside` on all five per-domain tiers — it captures no supply-side chokepoint rent; it *funds* the chokepoints. This mirrors [[CEG]]'s first-generator handling (off-framework "Adjacent" placement rather than a forced supply-side tier).

**`frameworks.md` demand-side placement — RESOLVED (codified S189, 2026-07-19).** MSFT was the first demand-side / hyperscaler page and the origin of the app-layer-gap flag. The demand-side placement is now codified — **CLAUDE.md Section 3.21 + frameworks.md Framework 10.1**: `layer: outside` + all-`*_tier: outside` is a *documented* value (MSFT = the **capex-payer** sub-role, the source of the Framework 10 CAPEX flow), theme-anchored not framework-placed. `_thesis.md` unchanged.

**Research-goal verdict (validated at primary; see [[software-AI-moat-durability]]).** MSFT's own structure is the cleanest illustration of the theme's **billed-unit discriminator**: its **consumption-metered** leg (Azure) is *amplified* by AI (agents consume more compute), while its **seat-metered** leg (M365 Copilot, ~$30/user add-on) is *contested* (seat monetization undercut by agents, low penetration). The Tier-3 scorecard verdict — **Durable (infra/Azure) + Contested (Copilot seat monetization)** — holds at primary.

## Financial snapshot

Two periods kept separate per Section 4.1 (no blending). **Section 2.11 applies** — MSFT's fiscal year ends June 30 (month+ offset); **Q3 FY2026 = calendar Q1 2026**, period-parity with vault peers' Q1 2026 disclosures.

**Segment recast (Section 2.1 mid-fiscal-year disclosure shift).** Effective FY2025, MSFT recomposed its three segments — "In August 2024 we announced changes… bringing the commercial components of Microsoft 365 together in Productivity and Business Processes… Prior period segment information has been recast" (FY2025 10-K). Comparatives below are restated; cross-period comparisons use recast figures.

**FY2025 (10-K; year ended June 30 2025; vs FY2024):**

| Metric | FY2025 | FY2024 | YoY |
|---|---|---|---|
| Total revenue | $281.7B | $245.1B | +15% |
| Operating income | $128.5B | $109.4B | +17% |
| Net income | $101.8B | $88.1B | +16% |
| Diluted EPS | $13.64 | $11.80 | +16% |
| Productivity & Business Processes | $120.8B | $106.8B | +13% |
| Intelligent Cloud | $106.3B | $87.5B | +21% |
| More Personal Computing | $54.6B | $50.8B | +7% |
| Microsoft Cloud gross margin % | 69% | — | ↓ on AI-infra scaling |

**Q3 FY2026 (10-Q; quarter ended March 31 2026 = calendar Q1 2026; call April 29 2026):**

| Metric | Q3 FY2026 | Q3 FY2025 | YoY |
|---|---|---|---|
| Total revenue | $82.9B | $70.1B | +18% |
| Operating income | $38.4B | $32.0B | +20% |
| Net income | $31.8B | $25.8B | +23% |
| Diluted EPS | $4.27 | $3.46 | +23% |
| Microsoft Cloud revenue | $54.5B | — | +29% |
| Microsoft Cloud gross margin % | 66% | — | ↓ from 69% FY2025; Q4 guided ~64% (call) |
| Company gross margin % | 68% | — | ↓ on AI-infra scaling |

## Segments & cloud

Three reportable segments post-recast: **Productivity & Business Processes** (M365 Commercial + Consumer, LinkedIn, Dynamics), **Intelligent Cloud** (Azure + server products), **More Personal Computing** (Windows, Gaming, Search/advertising, devices). Intelligent Cloud is the AI/Azure-bearing segment and the fastest-growing (+21% FY2025; the Q3 FY2026 segment grew +30% per the 10-Q).

**Azure** revenue grew **+40% (+39% constant currency)** in Q3 FY2026, accelerating, with AI services a growing within-Azure contributor (MSFT Q3 FY2026 call). **Microsoft Cloud** revenue reached $54.5B (+29%) at a 66% gross margin — down from 69% in FY2025 and guided to ~64% in Q4 — the compression attributed to scaling AI infrastructure (MSFT Q3 FY2026 10-Q + call). The Microsoft-Cloud gross-margin trajectory under inference load is the live instance of the margin-compression watch metric on [[software-AI-moat-durability]].

## AI monetization & the billed-unit lens

This section connects directly to the [[software-AI-moat-durability]] research goal — MSFT is the first scorecard name validated against its own primary sources, and its structure splits cleanly along the theme's **billed-unit discriminator**:

- **Consumption-billed (Durable / amplified):** Azure (+40%, accelerating) is metered by compute consumption; agent activity *increases* usage. This is the leg the supply-chain thesis ultimately serves.
- **Seat-billed (Contested):** M365 Copilot is a per-seat add-on (~$30/user). Management reported **over 20M paid Copilot seats**, with seat adds **+250% YoY**, the count of customers with 50,000+ seats quadrupling YoY, and Accenture at 740,000 seats — the largest win to date (MSFT Q3 FY2026 call, Tier 2). The theme's contested framing holds: seat monetization depends on per-seat value surviving agent substitution, and Copilot penetration remains a low single-digit share of the ~450M-seat M365 commercial base.
- **AI revenue is a call-only non-GAAP construct.** Management stated the "AI business surpassed $37 billion ARR, up 123%" (Q3 FY2026 call). This figure appears **only on the call (Tier 2)** — neither the 10-K nor the 10-Q breaks out a discrete AI revenue line; AI revenue is embedded in Azure / M365 / GitHub. This is the MSFT analog of the disclosure-quality caveat the theme flags (ARR/bookings constructs vs. a clean consumption line); see Source audit notes for the Tier-1/Tier-2 framing gap.

## CAPEX & demand-durability

MSFT is the vault's **first direct hyperscaler-CAPEX primary source** (previously the vault carried only NVDA's analyst-estimate ~$700B aggregate; see [[AI-demand-durability]] + the [[hyperscaler-capex]] payer-comparison tracker). Per the Q3 FY2026 10-Q + call:

- **Capex:** additions to property & equipment were **$30.9B** in Q3 (cash; up ~85% YoY from $16.7B; ~$31.9B including finance leases per the call, down sequentially on finance-lease delivery timing); $80.1B over nine months. Management guided **~$190B for calendar-year 2026** and Q4 capex to **>$40B** (call). Roughly two-thirds of spend is short-lived assets (servers/GPUs — the portion management frames as correlating with revenue) and one-third long-lived (datacenters/land/power, 15-year-plus lives).
- **Backlog:** total remaining performance obligations **$633B** (10-Q); commercial RPO grew +26% YoY *excluding OpenAI* (call) — i.e., OpenAI is a material RPO component.
- **The capex-vs-revenue "disconnect."** CFO Amy Hood directly addressed investor concern that capex is growing faster than revenue, emphasizing the short-lived-asset share that correlates with revenue and the $600B+ book of business (Q3 FY2026 call). This is the demand-durability bifurcation made concrete at a hyperscaler — the consumption/infra leg is monetizing; the productivity-seat leg is the unproven leg per [[software-AI-moat-durability]]. Framework 10 (CAPEX flow) treats MSFT as a top-of-diagram demand source.

## Custom silicon

MSFT operates two in-house silicon lines, now primary-source-confirmed (previously Tier-3 / counterparty per [[hyperscaler-custom-ASIC]]):

- **Maia 200** AI accelerator — "over 30% improved tokens per dollar compared to the latest silicon in our fleet," live in the Iowa and Arizona datacenters (Q3 FY2026 call).
- **Cobalt** server CPU — deployed in nearly half of datacenter regions, running workloads for Databricks, Siemens, and Snowflake; supply expanding (Q3 FY2026 call).

These reciprocally confirm the [[MRVL]] Microsoft custom-silicon partnership tracked in [[hyperscaler-custom-ASIC]]. Cobalt is an Arm-based design (alongside AWS Graviton and Google Axion), relevant to the Vera-CPU competitive framing on that page.

## OpenAI relationship

MSFT disclosed (mostly on the Q3 FY2026 call, Tier 2) a **restructured OpenAI arrangement**: access to OpenAI's frontier-model IP **royalty-free through 2032**, a revenue-share arrangement persisting **through 2030**, an equity stake, and OpenAI as a large compute customer across AI-accelerator and other compute. The FY2025 10-K reflects net recognized **equity-method losses** on the investment ("Other, net"). OpenAI is a material remaining-performance-obligation component (commercial RPO grew +26% YoY *excluding* OpenAI per the call).

**Tier-3 claim not supported at primary.** The [[software-AI-moat-durability]] anchor flagged a Tier-3 claim that "OpenAI = 45% of Azure RPO." No primary source (10-K, 10-Q, or call) discloses any such percentage; the relationship is material but unquantified at this granularity. Recorded as a Tier-3 non-corroboration (Section 4.5 discipline boundary).

## Open questions

1. **Placement codification — RESOLVED (S189).** The vault added the demand-side placement category (CLAUDE.md §3.21 + frameworks.md Framework 10.1); MSFT is the **capex-payer** sub-role. The `layer: outside` extension is now a documented value.
2. **AI revenue disclosure.** Does a clean Tier-1 AI revenue line ever appear, or does AI remain embedded in Azure/M365 with ARR a call-only non-GAAP construct? (A clean consumption line would strengthen the Durable verdict; continued embedding sustains the disclosure-quality caveat.)
3. **OpenAI RPO quantification.** Will MSFT quantify the OpenAI share of RPO, validating or refuting the unverified Tier-3 "45%" figure?
4. **Copilot seat economics.** Does per-seat Copilot monetization hold as agents mature, or does seat-count deflation appear (the theme's central contested-leg test)?
5. **Capex-revenue convergence.** Does the short-lived-asset capex share convert to revenue fast enough to close the "disconnect," or does the gap widen (the demand-durability timing risk)?

## Source audit notes

- **Tier-1/Tier-2 framing gap (Section 3.4; "filings omit commercial detail calls disclose" sub-pattern).** The most material AI metrics — AI ARR ($37B/+123%), Copilot seat counts, the Azure growth rate, capex guidance (~$190B CY2026), and the OpenAI deal terms — are disclosed only on the **call**; the 10-K and 10-Q embed AI in Azure/M365/GitHub with no discrete line and ARR is a non-GAAP call construct. Documented as a tier-asymmetric gap.
- **Segment recast (Section 2.1).** FY2025 recomposition (Aug 2024; prior periods recast) documented at the financial snapshot; comparatives restated. MSFT is a new instance of the mid-fiscal-year disclosure-shift pattern.
- **CEO/CFO tone.** Satya Nadella confident ("most consequential platform shift"); Amy Hood notably defensive on the capex-vs-revenue "disconnect," emphasizing the short-lived-asset/revenue correlation and the $600B+ book of business. No combativeness — CEO-combativeness count UNCHANGED.
- **Tier-3 non-corroboration.** "OpenAI = 45% of Azure RPO" and "$37.5B short-lived-asset capex" (from the [[software-AI-moat-durability]] anchor) not supported at primary — the latter conflated Q2 *total* capex with short-lived-asset capex. Expected Tier-3 non-corroboration per Section 4.5, not a kickoff falsification.

## Change log

- **2026-06-02 (S112 — creation):** First-canonical ingest from FY2025 10-K (Tier 1) + Q3 FY2026 10-Q (Tier 1) + Q3 FY2026 call (Tier 2; Apr 29 2026). Vault's first hyperscaler / demand-side page. Placement `layer: outside` + all `*_tier outside` (demand source / CAPEX deployer, off the supply-side ladder; mirrors [[CEG]] first-generator handling); frameworks.md hyperscaler-placement gap flagged for codification (not edited). First primary-source validation of the [[software-AI-moat-durability]] MSFT scorecard verdict (Durable infra/Azure + Contested Copilot-seat — held); two anchor Tier-3 claims (OpenAI=45%-of-Azure-RPO; $37.5B short-lived capex) not supported at primary. Section 2.11 (June 30 FY; Q3 FY2026 = calendar Q1 2026) + Section 2.1 segment recast applied.
