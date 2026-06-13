# The AI Implementation & Deployment Layer: Who Gets Paid to Put AI Into Production?
*Structural research anchor — drafted June 2026; trailing-12-month disclosures weighted most heavily. No stock recommendations, price targets, or valuation arguments. This document deliberately does NOT re-derive overall software-moat durability for the names the user already tracks; those appear only where they have implementation-layer-specific facts, marked "cross-reference only."*

## 1. Executive Summary

The single clearest finding: **AI-implementation revenue is real and disclosed today almost exclusively in the human-labor link (systems integrators), and even there it is reported as bookings/pipeline rather than recognized revenue. Everywhere else in the chain — orchestration, context plumbing, agent identity/security, observability — usage is growing but clean disclosed revenue line items barely exist.** The five most load-bearing findings, each with its strongest single piece of evidence:

1. **The deployment-labor link is where money is actually changing hands, and it is disclosed only as bookings, not clean revenue.** IBM reported its generative-AI "book of business" at more than $12.5 billion inception-to-date, with more than $10.5 billion in Consulting signings, per its January 28, 2026 Q4 release quoting CEO Arvind Krishna ("Our generative AI book of business now stands at more than $12.5 billion") — and IBM said it will *stop reporting the metric separately starting Q1 2026*. Accenture disclosed GenAI new bookings of $1.8B in Q4 FY25 and $5.9B for full FY25. **Tier: management-defined bookings constructs (b), not GAAP revenue.**

2. **Agent identity is concentrating around a chokepoint, validated by the largest cybersecurity acquisition ever — but nobody has disclosed material runtime-security revenue.** Palo Alto Networks closed its ~$25 billion CyberArk acquisition on Feb 11, 2026 explicitly to "secure every identity — human, machine, and agentic." Yet across Okta, CrowdStrike, Zscaler, and the combined PANW/CyberArk, **no company has disclosed a clean agent-identity or AI-runtime-security revenue line.** Okta CEO Todd McKinnon (CNBC, May 28, 2026): agentic AI is "not billions of dollars of token spend right now, it's plumbing for what's going to be required for the next five and 10 years." **Tier: M&A fact (a) + management characterization (b).**

3. **AI observability is so far a feature of existing observability platforms, not a separable disclosed market.** Datadog shipped LLM Observability (GA), Agent Monitoring, and LLM Experiments, but **declined on its Q4 2025 call (Feb 10, 2026) to give a percent-of-revenue figure for its AI cohort.** Revenue is metered on LLM spans — a consumption model aligned with agent adoption — but undisclosed in magnitude.

4. **The "consumption/outcome" pricing pivot is real and partially disclosed, but small.** Salesforce reported $800M Agentforce ARR, up 169% Y/Y, with 29,000 cumulative deals (Feb 25, 2026 Q4 FY26 release; combined Agentforce + Data 360 ARR exceeded $2.9B) — a management ARR construct on a consumption meter ($2/conversation or ~$0.10/action). Globant disclosed only $20.6M ARR from its token-priced "AI Pods." Both are aligned-incentive models but immaterial relative to total revenue.

5. **Disconfirming evidence is abundant: the gap between AI-pilot hype and P&L impact is the dominant story.** MIT NANDA's "The GenAI Divide: State of AI in Business 2025" (lead author Aditya Challapally), based on 150 leader interviews, a 350-employee survey, and 300 public deployments, found "about 5% of AI pilot programs achieve rapid revenue acceleration; the vast majority stall," against an estimated $30–40B invested. SI revenue growth remains low-single-digit even as AI bookings balloon (Infosys cut FY26 guidance to 1–3%; IBM Consulting full-year 2025 revenue grew 0.4%), and the same agentic-coding tools driving the bookings are compressing the billable-hours base — Accenture's six-month $865M restructuring cut roughly 11,000 staff.

**Net verdict on the core thesis:** The implementation layer *will* monetize, but as of mid-2026 the durable, disclosed money sits with accountability-absorbing labor (IBM, Accenture, Palantir's embedded model) and with consumption-metered infrastructure (MongoDB, Datadog). The pure-tooling links are strategically important chokepoints (agent identity especially) but remain pre-revenue-disclosure, and are the most exposed to model-provider and hyperscaler encroachment.

---

## 2. Value-Chain Map — Market-Structure Verdict Per Link

| Link | Verdict | One-line reasoning |
|---|---|---|
| **1. Integration & orchestration (iPaaS, agent frameworks, MCP)** | **Contested → commoditizing** | Anthropic donated MCP to the Linux Foundation's Agentic AI Foundation on Dec 9, 2025 (co-founded with Block and OpenAI); per the Dec 2025 ecosystem update, "more than 10,000 active public MCP servers" and "97M+ monthly SDK downloads." The protocol layer is now a public good; value accrues to whoever owns governed connectors + the underlying data. |
| **2. Enterprise context plumbing (vector/retrieval, catalogs, governance)** | **Concentrating** | Consolidating into platform databases (MongoDB Atlas vector search) and into governance acquisitions (Salesforce closed Informatica, ~$8B equity, $25.00/share, Nov 18, 2025); standalone vector DBs squeezed. |
| **3. Agent identity, security & governance** | **Concentrating (chokepoint)** | Identity is the natural control point for autonomous agents; PANW's $25B CyberArk close + Okta's repositioning show platform players racing to own it. Runtime security still nascent and undisclosed. |
| **4. Evaluation & observability** | **Contested** | Incumbent observability platforms (Datadog) fold AI monitoring into existing span-based billing; a private eval cohort (Braintrust, Galileo, LangSmith) contests pre-production evals. |
| **5. Deployment labor (SIs, FDEs, MSP/MSSP accountability)** | **Fragmenting at the commodity end, concentrating at the accountability end** | Labor-arbitrage SIs face hour deflation; the durable position is contractual accountability / regulated-market access (IBM, Palantir embedded, FedRAMP holders). |
| **6. Vertical implementation platforms** | **Concentrating but thinly public** | Most vertical AI deployers are private; among publics, Palantir (gov/commercial ontology) is the clearest, with the FDE model now being copied by the model labs themselves (OpenAI's Tomoro acquisition; Anthropic enterprise JV). |

---

## 3. Company Scorecard

*a = disclosed in filing/earnings release; b = management claim/metric on call; c = announcement/marketing. Figures labeled with period & source tier.*

| Company / Ticker | Chain link(s) | Billed unit | AI-implementation revenue evidence (a/b/c) | Structural verdict | Top risk | Single falsifier |
|---|---|---|---|---|---|---|
| **Accenture (ACN)** | 5 (labor) | Project + managed-services hours | GenAI new bookings $1.8B in Q4 FY25, $5.9B full FY25 (a/b, Q4 FY25 8-K). Advanced AI ~$2.2B bookings / ~$1.1B revenue in Q1 FY26 (b). FY26 revenue guide 2–5% LC (a). | Contested | Agentic coding compresses billable hours faster than AI projects scale; ~11,000 cut in $865M program | Advanced AI quarterly revenue stalls/declines for 2+ quarters while total bookings flat |
| **IBM (IBM)** | 5 (labor) + 1/2 (watsonx) | Consulting signings + software ACV | GenAI book >$12.5B inception-to-date Q4 2025; >$10.5B Consulting signings (b); metric to be discontinued Q1 2026. Consulting FY25 revenue +0.4% (a). | Contested | Book is signings not revenue; consulting revenue barely growing; loses its headline metric | Consulting segment revenue declines Y/Y for 2 quarters despite rising AI work |
| **EPAM (EPAM)** | 5 (labor) | Project-hours / engineers | No clean AI revenue line; "AI-readiness/data foundation" demand cited (b). FY25 revenue $5.46B +15%, net income −17%, organic CC +3–5% (a). | Contested → exposed | Pure engineering labor; margin compression (GAAP IFO 9.0–9.7% of rev) | EPAM discloses AI revenue line >10% of total, OR organic growth turns negative |
| **Globant (GLOB)** | 5 (labor) + 6 | Shifting seat→token subscription ("AI Pods") | AI Pods exit-rate ARR $20.6M FY25 (b); $283M Pods pipeline (b/c). Total FY25 revenue $2.455B +1.6%; Q4 −4.7% Y/Y (a). | Contested → exposed | Revenue declining; AI Pods immaterial vs total | AI Pods ARR fails to reach ~$75M+ run-rate by end-2026 |
| **Cognizant (CTSH)** | 5 (labor) | Project + managed services | No clean AI line; "agentification at scale," two >$1B AI-era deals Q2 25 (b). TTM bookings $27.8B (a). Revenue +6–7% CC (a). | Contested | Labor arbitrage; AI deals not separately quantified | Book-to-bill falls below 1.0x for 2 quarters |
| **Infosys (INFY)** | 5 (labor) | Project + managed services | 2,500+ GenAI + 200+ agentic projects (b); no revenue breakout. FY26 guidance cut to 1–3% CC (a). | Contested → exposed | Guidance cut signals AI not offsetting core deflation | FY27 guidance falls below 1% or turns negative |
| **Palantir (PLTR)** | 6 (vertical) + 5 (embedded FDE) | Platform subscription + bundled deployment | Q1 2026 revenue $1.633B, +85% Y/Y; US commercial $595M +133%; US gov $687M +84%; FY26 guide raised to ~$7.66B / ~71% (a). No FDE/services breakout (a). | **Durable** | Expectations/concentration; no services transparency | US commercial growth decelerates below ~40% Y/Y for 2 consecutive quarters |
| **Salesforce (CRM)** | 1/6 (Agentforce surface) — *cross-reference only* | Consumption ($2/convo, ~$0.10/action) | Agentforce ARR $800M, +169% Y/Y, 29,000 deals, end FY26 (b); Agentforce+Data 360 ARR >$2.9B (b). | Contested | Consumption ramp slower than seat-model erosion | Agentforce ARR growth decelerates sharply / cRPO disappoints |
| **MongoDB (MDB)** | 2 (context plumbing) | Consumption (Atlas) | Vector-search customers ~doubled Y/Y (b); no clean "AI revenue" line. Total FY26 rev $2.46B +23%; Q4 +27%; Atlas 75% of rev (a). | Durable (contested) | Vector search commoditized by hyperscalers / Postgres pgvector | Atlas growth decelerates below ~20% while vector adoption flattens |
| **Datadog (DDOG)** | 4 (observability) — *cross-reference only* | Consumption (LLM spans) | LLM Obs >1,000 customers, spans +10x in 6 months (b); **declined to disclose AI cohort % of revenue** Q4 25 call (a/b). ~5,500 customers send AI data (b). | Contested | AI observability is a feature, not separable; inference-cost margin pressure | Datadog discloses AI cohort >10% of revenue (would confirm separability) |
| **Palo Alto Networks (PANW)** | 3 (agent identity) — *cross-reference only* | Platform subscription / ARR | Closed ~$25B CyberArk acquisition Feb 11, 2026 to secure "human, machine, agentic" identity (a). No isolated agent-identity revenue (a). | Concentrating (durable if integration works) | Integration debt (Venafi, Zilla, Protect AI); agent-identity TAM still rhetorical | 2+ years pass with no disclosed agentic-identity ARR contribution |
| **CyberArk (now PANW)** | 3 (agent identity) | Subscription ARR | Standalone FY25 total ARR $1.44B +23%; subscription ARR $1.267B (88% of ARR) (a). Agentic identity = positioning, not a disclosed line (c). | Concentrating | Now inside PANW; agent revenue unquantified | — |
| **Okta (OKTA)** | 3 (agent identity) | Per-user + new-product uplift | "Okta for AI Agents" GA Apr 30, 2026 (c); CEO McKinnon: AI "not billions… it's plumbing" (b). No agent revenue line (a). New products ~25% of Q1 FY27 bookings (b). | Contested | Hyperscaler-native identity (Bedrock AgentCore) embeds the capability | Okta discloses a quantified, material "AI Agents" ARR (>5% of total) |
| **CrowdStrike (CRWD)** | 3/4 (AI security) — *cross-reference only* | Module subscription / ARR | Charlotte AI AgentWorks launched Mar 2026 (c); no disclosed AI-agent-security ARR (a). | Contested | AI security bundled, not separately monetized yet | Discloses Charlotte/agent-security ARR as standalone material line |
| **Zscaler (ZS)** | 3 (AI security) — *cross-reference only* | ARR / consumption | "AI Security" named a growth pillar, not quantified (b); acquired SPLX, intent to buy Symmetry Systems (c). | Contested | Pillar rhetoric, no disclosed agent-security revenue | Discloses AI-security ARR breakout |
| **Boomi (private, Dell/Francisco Partners)** | 1 (iPaaS) | Platform subscription | 33,000+ agents deployed via Agentstudio (c); 347% ROI TEI study (c, vendor-commissioned). Private — no public revenue. | Contested | Not public; agent-native iPaaS entrants | n/a (private) |

---

## 4. Honest Counterpoints — Where the Implementation Story Does NOT Hold Up

- **SI bookings ≠ SI revenue, and the gap is widening.** IBM's GenAI book grew from ~$5B (Q1 25) to >$12.5B (Q4 25) — a management-defined construct mixing software transactional revenue, new SaaS ACV, and consulting *signings*. Over the same period IBM Consulting full-year revenue grew just 0.4%. Tellingly, IBM is retiring the metric in Q1 2026 — removing the single most-cited proof point for the SI-AI thesis. Bookings are accumulating faster than they convert; the same is true at Accenture, where record bookings coexist with FY26 revenue guidance of only 2–5% local currency.

- **The agentic-coding tools that create the AI projects also destroy the billable hours.** Accenture's roughly $14B market-cap drop after Anthropic's Claude Code launch, and its $865M restructuring (CEO Julie Sweet: the firm is "exiting people on a compressed timeline where reskilling is not a viable path for the skills we need"), are the clearest market signals that labor-arbitrage SIs face a structural squeeze. EPAM (net income −17% in FY25) and Globant (revenue −4.7% in Q4) are the disconfirming cases: strong AI narrative, deteriorating fundamentals.

- **Agent identity / runtime security is a strategically real chokepoint with essentially zero disclosed revenue.** The PANW–CyberArk deal proves strategic conviction, but as of mid-2026 *no* public company breaks out agent-identity or AI-runtime-security revenue. Okta's own CEO calls it "plumbing for the next five and ten years." This is the largest hype-vs-disclosed-revenue gap in the chain. SACR/Stanford and Okta's own framing distinguish three runtime-security layers (deterministic governance, behavioral analysis, non-deterministic governance) — but the disclosure on all three is product GA, not revenue.

- **AI observability may never be a separable market.** Datadog folds LLM/agent monitoring into span-based billing, charges no separate eval fee, and *won't* disclose an AI cohort figure — all consistent with it being a feature that drives consumption, not a standalone product line. The private eval cohort (Braintrust, Galileo, LangSmith) is contesting the *pre-production* evaluation niche, but Datadog's bundling structurally undercuts standalone eval pricing.

- **MCP commoditizes the connector layer it was meant to monetize.** As an open Linux Foundation standard (donated Dec 9, 2025), MCP makes connectors a public good; value migrates to governed data and identity, not to the protocol. The "iPaaS gets paid for agent integration" thesis is weakened, not strengthened, by MCP's success — though governed, audited, regulated-grade connector management (Boomi, MuleSoft) retains some defensibility.

---

## 5. Lane-Level Falsifiers — Conditions Under Which "Implementation Layer Monetizes Next" FAILS

1. **Model providers absorb the tooling layer.** OpenAI/Anthropic/Google ship native agent platforms, SDKs, connectors (MCP), and now forward-deployed-engineer units (OpenAI's Tomoro acquisition, Anthropic's enterprise JV reportedly valued ~$1.5B). If the labs capture deployment, independent orchestration/eval/identity tooling never reaches disclosed scale.
2. **Enterprise AI spend stays concentrated in tokens/infra.** If dollars stay with model inference and GPU/cloud (hyperscalers, NVIDIA) and never migrate to the deployment/governance layer, the implementation links stay thin. Okta's "not billions of token spend" comment is consistent with this risk today.
3. **SI hours deflate faster than AI projects grow.** If agentic coding compresses integration-hours demand faster than new AI mandates appear, SI *revenue* (not just bookings) declines — already visible in Infosys's guidance cut and Globant's revenue decline.
4. **In-housing wins.** MIT NANDA found vendor-built tools succeed ~2x vs internal builds *today* — but if agentic dev tools invert that, the labor link erodes.
5. **The pilot-to-production gap never closes.** If the ~95% no-rapid-P&L-impact rate persists, AI budgets get cut and the entire chain's bookings fail to convert.

---

## 6. Watch-List of Dated Triggers (Next 2–4 Quarters)

- **Accenture Q3 FY26 earnings (~June 2026):** Does Advanced AI quarterly *revenue* (~$1.1B base) keep climbing, and does total revenue accelerate? The key bookings→revenue conversion test.
- **IBM Q1/Q2 2026 earnings (Apr/Jul 2026):** First quarters *without* the GenAI book-of-business metric — watch whether Consulting revenue growth finally inflects, since the headline number is gone.
- **Salesforce Q1–Q2 FY27 (mid/late 2026):** Agentforce ARR trajectory past $800M; whether consumption offsets seat-model erosion.
- **Datadog FY26 quarters:** Whether management ever discloses an AI cohort % of revenue — the separability test.
- **Okta FY27 quarters:** Whether "Okta for AI Agents" (GA Apr 30, 2026) produces any disclosed material ARR.
- **PANW post-CyberArk integration (FY26 reporting):** First disclosure (if any) of agentic-identity ARR contribution.
- **Palantir Q2 2026 (guide $1.797–1.801B):** Whether US commercial growth holds above ~120%.
- **Globant 2026:** AI Pods ARR run-rate vs the immaterial $20.6M FY25 base; guided return to organic growth by mid-2026.

---

## 7. Source Appendix (tiering of load-bearing claims)

**Primary (filings / earnings releases / call transcripts):**
- Accenture Q2 FY26 8-K & 10-Q (bookings $22.1B, revenue $18.0B); Q4 FY25 8-K (GenAI bookings $1.8B Q4 / $5.9B FY25; ~11,000 headcount cut, $865M program, CFO Angie Park / CEO Julie Sweet); Q1 FY26 call (Advanced AI ~$2.2B bookings, ~$1.1B revenue).
- IBM Q1–Q4 2025 8-Ks & 2025 Annual Report (GenAI book $5B→$7.5B→$9.5B→$12.5B; >$10.5B Consulting signings; Consulting FY25 +0.4%; book-of-business definition in Exhibit 99.2; Jan 28, 2026 Q4 release; metric to be discontinued Q1 2026).
- EPAM Q1–Q3 2025 8-Ks (revenue, margin, headcount); FY25 figures.
- Globant Q4/FY2025 release & call (AI Pods ARR $20.6M; total revenue $2.455B; Q4 −4.7%).
- Cognizant Q1–Q3 2025 8-Ks (TTM bookings $27.8B; revenue +6–7% CC).
- Infosys FY25/FY26 6-Ks (FY26 guidance cut to 1–3% CC; 2,500+ GenAI / 200+ agentic projects).
- Palantir Q1 2026 8-K/release (revenue $1.633B +85%; US commercial $595M +133%; US gov $687M +84%; FY26 guide ~$7.66B / ~71%; Q2 guide $1.797–1.801B). *No FDE/services breakout — confirmed structural gap; only Commercial/Government segments reported.*
- Salesforce Q4 FY26 release (Feb 25, 2026): Agentforce ARR $800M +169%, 29,000 deals; Agentforce + Data 360 ARR >$2.9B. Salesforce–Informatica close (Nov 18, 2025; ~$8B equity, $25.00/share).
- MongoDB Q3/Q4 FY26 8-Ks & 10-Q (Q4 revenue $695.1M +27%; FY26 $2.46B +23%; Atlas 75% of rev; vector adoption ~doubled).
- Datadog Q4 2025 8-K & call transcript (Feb 10, 2026) — explicitly declined to give AI cohort % of revenue; LLM Obs >1,000 customers, spans +10x in 6 months.
- PANW & CyberArk 8-Ks (CyberArk close Feb 11, 2026, ~$25B, $45.00 cash + 2.2005 PANW shares; CyberArk FY25 ARR $1.44B +23%, subscription ARR $1.267B).
- Okta Q1 FY27 release & call (May 28, 2026) — "Okta for AI Agents" GA Apr 30, 2026; new products ~25% of Q1 bookings; CEO McKinnon CNBC quote ("not billions of dollars of token spend right now, it's plumbing for what's going to be required for the next five and 10 years").

**Secondary / industry research:** MIT NANDA "The GenAI Divide: State of AI in Business 2025" (lead author Aditya Challapally; 150 interviews, 350-employee survey, 300 deployments; ~5% achieve rapid revenue acceleration; $30–40B invested); Forrester / Everest / Chartis on PANW–CyberArk rationale; Gartner/Forrester MCP-adoption forecasts; Anthropic MCP ecosystem update (Dec 9, 2025: Linux Foundation Agentic AI Foundation donation with Block and OpenAI; 10,000+ active public servers; 97M+ monthly SDK downloads).

**Press / vendor marketing (flagged, lower tier):** Boomi 347% ROI TEI study (vendor-commissioned) and "33,000+ agents" claim; Agentforce third-party pricing guides; FDE salary/role blogs (marktechpost, hashnode, jobsbyculture); Globant AI-Pod margin claims (~45–60%) cited via Yahoo/Investing.com.

**Private competitive frontier (context only — not public; flagged clearly):** Sierra (agent deployment, Bret Taylor) most directly threatens the SIs and outcome-deployers; Braintrust / Galileo / LangSmith / Arize / Langfuse contest Datadog at the eval/observability layer; agent-security startups (Permiso and others) and hyperscaler-native identity (AWS Bedrock AgentCore) pressure Okta/PANW. None disclose revenue.

**Explicit uncertainty / could-not-verify:** No public company discloses a clean agent-identity or AI-runtime-security revenue line (verified absent across Okta, PANW/CyberArk, CrowdStrike, Zscaler) — this is the chain's biggest hype-vs-disclosure gap. Palantir does not break out FDE/services revenue. Datadog AI-cohort revenue is undisclosed by management choice. Globant AI-Pod gross margins are management/secondary, not filing-disclosed. SI "AI bookings" metrics are management-defined constructs that should never be read as recognized revenue.

---

### Ranking the six links by revenue-reality TODAY (Specific Question #1)
1. **Deployment labor (link 5)** — real money, but disclosed as *bookings/signings* (IBM >$12.5B book, Accenture $5.9B FY25 GenAI bookings), not clean revenue. Accenture's ~$1.1B/quarter Advanced AI revenue is the closest thing to a disclosed recognized-revenue figure in the entire chain.
2. **Context plumbing (link 2)** — consumption revenue is real and recognized (MongoDB Atlas +29%), but not isolated as "AI."
3. **Evaluation & observability (link 4)** — real consumption revenue (Datadog LLM spans), magnitude undisclosed; likely a feature, not a market.
4. **Vertical platforms (link 6)** — Palantir's growth is real and recognized, but the "AI implementation" portion isn't broken out from platform revenue.
5. **Agent identity & security (link 3)** — strategically validated by $25B M&A, but *zero* disclosed agent-specific revenue.
6. **Integration & orchestration (link 1)** — least real as disclosed revenue; the standard (MCP) is open/free and commoditizing.

### Companies that crossed 10% of total revenue from disclosed AI-implementation work (Specific Question #2)
**None can be cleanly verified from filings.** The closest candidates are management constructs, not GAAP line items: Palantir's US commercial (~36% of Q1 2026 revenue, $595M) is AI-platform revenue but not labeled "AI implementation"; Accenture's ~$1.1B Advanced AI quarterly revenue is ~6% of ~$18B quarterly revenue (b). IBM's >$12.5B book is inception-to-date bookings, not a revenue percentage. This null result is itself a load-bearing finding.