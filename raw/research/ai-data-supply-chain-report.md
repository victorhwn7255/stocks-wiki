# The AI Data Supply Chain: Who Owns a Toll Booth, and Who Is Selling a Commodity

## TL;DR
- **The central hypothesis largely holds, with one important refinement.** Durable, toll-booth value sits with owners of unique, licensable proprietary data — but the strongest moats are NOT the headline-grabbing media licensors (Reddit, Getty, News Corp); they are the workflow-embedded specialized-data compounders (RELX, Thomson Reuters, S&P Global, Moody's) whose data is fused to switching-cost-heavy professional software. The pure data-labeling/annotation businesses are indeed largely commoditizing labor arbitrage with thin moats and extreme customer concentration.
- **The exception that refines the thesis:** expert/frontier RLHF and evaluation data (PhD-level, domain-specific human feedback) is a genuine, growing, premium niche where private players (Surge AI, Mercor) are capturing real value — but it sits on rented land (roughly a dozen frontier-lab customers) and is being attacked by both in-housing and synthetic data. This is high-growth but structurally fragile, not a toll booth.
- **For a 2–3 year horizon, the cleanest public expressions are the specialized-data compounders (RELX, Thomson Reuters, S&P Global, Moody's), plus Reddit (RDDT) as the one scaled, genuinely scarce text corpus.** The names to be most skeptical of are the pure-play labelers re-narrated as "AI picks-and-shovels": Innodata (INOD) on customer concentration, and the now-impaired/delisted Appen (APX.AX) and TELUS Digital (taken private October 2025).

## Key Findings

1. **The "data wall" is real but slow-moving, and it shifts value to data OWNERS, not data LABORERS.** Epoch AI (Villalobos et al., peer-reviewed, ICML 2024) estimates the stock of human-generated public text at roughly 300 trillion tokens and projects that "language models will completely exhaust this stock between 2026 and 2032, or even earlier if overtrained," with a median exhaustion year of 2028. High-quality text is the binding constraint. This scarcity raises the value of a unique proprietary corpus (a stock you own) far more durably than it raises the value of annotation labor (a flow you rent).

2. **Customer concentration is the defining fragility of the labeling layer.** Per Innodata's Q1 2025 Form 10-Q, "one customer in the DDS segment generated approximately 61% and 24% of the Company's total revenues for the three months ended March 31, 2025 and 2024, respectively" (concentration eased to ~58% by FY2025, still extreme). Appen lost its Google contract — $82.8M of its $273M 2023 sales, ~30% — overnight in early 2024, with the company stating it had "no prior knowledge of Google's decision to terminate." Scale AI lost Google (a ~$200M/yr relationship) and saw OpenAI and xAI pull back within weeks of Meta's $14.3B investment. Concentration on a dozen frontier-lab buyers means any single procurement decision is an existential event.

3. **The hyperscaler in-housing threat is demonstrated, not hypothetical.** Google terminating Appen and internalizing search-rater capacity, and Meta acquiring its way to a captive data operation via Scale, are proof points that the largest buyers will internalize data ops when it suits them. This caps the durable margin of any pure-services labeler.

4. **Copyright law is breaking AMBIGUOUSLY, which paradoxically favors the data owners commercially regardless of legal outcome.** Where rulings favor rightsholders (Thomson Reuters v. Ross, Feb 2025) they force licensing; where they favor AI developers (Bartz v. Anthropic and Kadrey v. Meta, June 2025; Getty v. Stability UK, Nov 2025) they entrench the "license-the-big-players-to-avoid-the-fight" equilibrium that has already produced $2B+ of signed deals. Either way, owners of clean, rights-cleared, indemnifiable corpora get paid.

5. **Synthetic data is a complement, not yet a substitute, for expert human data.** The peer-reviewed Nature paper by Shumailov et al. (2024), "AI models collapse when trained on recursively generated data," shows that training generative AI on recursively generated content "can lead to a collapse in the ability of the models to generate diverse high-quality output" — collapse is effectively guaranteed when training purely on synthetic data, but avoidable when synthetic is mixed with real/human data and verified. The practical consequence: commodity bulk annotation is being automated away, while expert human feedback and verification become MORE valuable — bifurcating the labeling market.

6. **The specialized/financial data owners are NOT licensing core data to labs — they are restricting it and building their own AI products.** S&P Global, Moody's, FactSet, Morningstar, LSEG and Bloomberg uniformly keep proprietary data out of third-party training corpora and instead sell "AI-ready," permissioned access (often via entitlement-based MCP servers) and embedded GenAI tools. This is the strongest moat in the entire value chain: proprietary data + workflow lock-in + the optionality to license on their own terms later.

## Details

### The seven-layer value chain, with companies placed

**Layer 1 — Data owners/licensors (proprietary corpora).** Where durable value concentrates, but highly heterogeneous:
- *Text/forum:* Reddit (RDDT) — the standout scarce, scaled, conversational corpus.
- *Image/video:* Getty Images (GETY), Shutterstock (SSTK) — merging; structurally challenged demand even as they monetize licensing.
- *Audio/music:* Universal Music (UMG), Warner Music (WMG) — newly proven licensors after the Udio/Suno settlements.
- *News/text:* News Corp (NWSA) — ~$250M/5yr OpenAI deal; "woo and sue."
- *Scientific/legal:* RELX (RELX), Thomson Reuters (TRI), Wiley (WLY), Pearson (PSO).
- *Financial:* S&P Global (SPGI), Moody's (MCO), FactSet (FDS), Morningstar (MORN), LSEG, Bloomberg (private).

**Layer 2 — Data brokers/aggregators/marketplaces.** Really Simple Licensing (RSL) clearinghouse; TollBit, ProRata, Cloudflare pay-per-crawl infrastructure. Mostly private/early; an emerging toll-collection layer.

**Layer 3 — Data processing/curation/ETL.** Innodata (INOD) straddles this and Layer 4; Snorkel AI (private, programmatic labeling).

**Layer 4 — Labeling/annotation/RLHF/human feedback.** Public: Innodata (INOD), TELUS Digital (TIXT, now private), Appen (APX.AX). Private: Scale AI, Surge AI, Mercor, iMerit, Sama, Labelbox, Toloka, Invisible Technologies, CloudFactory. The commoditizing layer, bifurcating into commodity bulk (losing) and expert RLHF (winning, but fragile).

**Layer 5 — Synthetic data generation.** Gretel (acquired by NVIDIA, 2025), Mostly AI, Tonic.ai — mostly private or absorbed.

**Layer 6 — Evaluation/benchmarking/trust-&-safety/red-teaming.** Surge AI (AdvancedIF, EnterpriseBench), Scale AI (Scale Validate), Innodata (safety/red-teaming). A growing premium niche.

**Layer 7 — Adjacent data infrastructure (flagged, not over-weighted).** Snowflake (SNOW), Databricks (private), Palantir (PLTR), MongoDB (MDB). Important but not "data supply" per se.

### Tiered moat matrix (highest to lowest value capture)

**Tier 1 — True toll booths (unique, non-replicable, workflow-embedded data).** RELX, Thomson Reuters, S&P Global, Moody's. *Why protected:* proprietary editorial/analytical datasets fused to mission-critical professional software with multi-year contracts and ~90%+ retention. A hyperscaler cannot relabel or synthesize around Westlaw headnotes (Thomson Reuters won exactly this point against Ross), credit-rating histories, or LexisNexis case law. AI-attributable revenue is mostly embedded-product uplift (Lexis+AI, Protégé, CreditCompanion, Capital IQ Pro), NOT training-data licensing — a feature, not a bug, because it is recurring and sticky.

**Tier 2 — Scarce standalone corpora (real but narrower moats).** Reddit (RDDT) — uniquely scaled human conversational data, cited as the most-referenced source in AI answers; News Corp, UMG/WMG — proven licensors but non-exclusive, lumpy deals. *Why partially protected:* the data is genuinely scarce, but licensing is non-exclusive and revenue is concentrated in a few AI-lab payers.

**Tier 3 — Challenged owners.** Getty (GETY)/Shutterstock (SSTK) — own real image libraries but face demand erosion from generative substitutes; monetizing licensing defensively.

**Tier 4 — Premium services with network effects (fragile).** Surge AI, Mercor, Scale AI — expert RLHF/eval. High growth, real expertise-matching network effects, but rented-land customer concentration and in-housing/synthetic threats.

**Tier 5 — Commoditizing labor arbitrage (lowest).** Innodata (INOD), Appen, TELUS Digital AI Data Solutions, iMerit, Sama, CloudFactory. *Why exposed:* low switching costs, customer concentration, wage arbitrage that hyperscalers can replicate or internalize.

### Deep dive: Reddit (RDDT) — the one scaled, scarce text corpus

Reddit is the clearest public "scarce data" story. AI licensing sits in "Other revenue," which COO Jen Wong described as ~10% of total revenue and "valuable revenue." Known deals: Google ~$60M/yr (signed Feb 2024, the day of its IPO filing) and OpenAI (estimated ~$70M/yr); total disclosed licensing to date ~$203M. CEO Steve Huffman has signaled pricing power on renewals: "Every variable has changed since we signed those first deals. Our corpus is bigger, it's more distinct, more essential." Reddit is pushing toward dynamic/usage-based pricing and backs the RSL licensing clearinghouse.

Financials are strong: FY2024 revenue $1.3B (+62%); Q3 2025 revenue $585M (+68% YoY), net income $163M, 91.0% gross margin, $183M free cash flow. Note that "Other revenue" (which contains licensing) was only +7% YoY in Q3 2025 to $36M — i.e., the licensing line is NOT currently the growth engine; advertising is. **Bear case:** licensing is non-exclusive and a small revenue slice; the Perplexity litigation and traffic/SEO dependence on Google are risks; if AI answers cannibalize Reddit's own traffic, the flywheel weakens. **Moat verdict: Tier 2, Medium-High conviction.**

### Deep dive: Thomson Reuters (TRI) & RELX (RELX) — the toll booths

These are the structural winners. **Thomson Reuters** won the landmark *Thomson Reuters Enter. Ctr. GmbH v. Ross Intelligence Inc.*, No. 1:20-cv-00613 (D. Del., Feb. 11, 2025): Judge Stephanos Bibas found Ross directly infringed copyrights in 2,243 Westlaw headnotes and rejected fair use, holding that even "a headnote taken verbatim from an opinion is a carefully chosen fraction of the whole" with "enough 'creative spark' to be original," and that the fourth factor (market harm — including the market for AI training data) was "undoubtedly the single most important element of fair use." The case is on interlocutory appeal to the Third Circuit (No. 25-2153, filed Sept. 2025). This is the single most important pro-rightsholder AI-training precedent to date, and it directly protects TR's own asset.

**RELX** has pivoted hard to embedded AI: Lexis+AI and Protégé in Legal (20% of 2024 revenue, growing ~9% YTD underlying in 2025), with company-wide H1 2025 underlying revenue +7%, adjusted operating profit +9%, 100% cash conversion, and £1.5B of 2025 buybacks rising to a planned £2.25B in 2026. **Moat verdict for both: Tier 1, High conviction.** A competitor cannot synthesize around decades of proprietary editorial/analytical data fused to lawyer/risk-professional workflows.

### Deep dive: the financial-data owners (SPGI, MCO, FDS, MORN, LSEG, Bloomberg) — controlled-access toll booths

A uniform, telling pattern: **no public financial-data owner licenses core proprietary data to AI labs for foundation-model training.** Instead they (a) contractually restrict training use, (b) sell "AI-ready," permissioned data at a premium, and (c) build their own embedded GenAI products.
- **S&P Global (SPGI):** explicit that customer licenses do not grant rights to train third-party models; launched a Kensho LLM-ready API and Capital IQ Pro GenAI enhancements, with CreditCompanion in RatingsDirect. Management has pointed to clients paying meaningful premiums for AI-ready access. Q4 2025 revenue +9%, ~47% operating margin.
- **Moody's (MCO):** Moody's Research Assistant (launched Dec 2023 on Microsoft Azure OpenAI + Moody's proprietary "Data Estate," now covering 190,000+ companies); strategy of an integrated "Risk Operating System."
- **FactSet (FDS):** ~50% of data is "proprietary and enriched"; guided 30–50bps of FY2025 ASV growth from GenAI products; AI Document Search beta to 85,000+ users.
- **Morningstar (MORN):** states "client data is never used to train AI models"; building Intelligence Engine and entitlement-based Microsoft Copilot/MCP access (including exclusive PitchBook data).
- **LSEG:** "LSEG Everywhere" — delivering *licensed* data via an LSEG-managed MCP server inside Microsoft Copilot; 33+ petabytes of AI-ready content.
- **Bloomberg (private):** built its own BloombergGPT (~51% of its training tokens from proprietary "FinPile") rather than licensing data out — though independent research found GPT-4 outperformed it on most financial NLP tasks, a caution on proprietary-LLM ROI.

**Moat verdict: Tier 1, High conviction** for SPGI/MCO/RELX/TRI; the "restrict + build + license-on-our-terms" posture is the most durable model in the chain.

### Deep dive: Innodata (INOD) — the public labeler bull/bear

Innodata is the purest public way to play AI data engineering, and the financials have been spectacular: FY2024 revenue $170.5M (+96%); FY2025 revenue $251.7M (+48% organic), adjusted EBITDA $57.9M (+68%), net income $32.2M, ending cash/ST investments $82.2M. It serves "five of the Magnificent Seven" plus other big-tech/AI labs (eight Big Tech customers disclosed). Management guides 35%+ growth for 2026 and is expanding into pre-training data, robotics/physical-AI datasets, and safety/red-teaming.

**The bear case is structural and specific:** customer concentration. Per the Q1 2025 10-Q, one customer was ~61% of revenue (easing to ~58% for FY2025). This is the Appen risk in waiting — a single procurement shift at one hyperscaler could halve revenue. Its services (data annotation, fine-tuning support, evaluation) have low switching costs versus a hyperscaler's in-house team or a rival labeler, and pricing for commodity annotation faces downward pressure from automation and synthetic data. Innodata's defense is to move up-market into harder, expert, safety-critical data — the same move Scale and Surge are making, which means margins compress as everyone crowds the premium tier. **Moat verdict: Tier 5 trending toward Tier 4; conviction on the equity is Low-to-Medium and entirely execution/concentration-dependent.** Growth is real but contract-dependent, not annuity-like.

### Deep dive: Scale AI and the private labeler shake-up

Scale AI is the cautionary tale for the whole "labeling = picks-and-shovels" narrative. Revenue grew ~$760M (2023) → ~$870M (2024), with a reported ~$1.5B exit run-rate. Then Meta's $14.3B investment for a 49% non-voting stake (June 2025, $29B valuation) — structured to hire founder Alexandr Wang — triggered Google (~$200M/yr), OpenAI and xAI to pull or pause work over confidentiality/competitive concerns. Scale laid off 200 employees (~14%) in July 2025 and pivoted hard to government: a $99M DoD contract (Aug 2025), a $100M follow-on (Sept), then a $500M DoD deal (May 2026). The episode proves the core fragility: **when your largest shareholder becomes a competitor's parent, your neutrality — your only real moat — evaporates.**

The beneficiaries were rivals: **Surge AI** (bootstrapped, reportedly >$1B revenue in 2024, profitable, ~50,000 expert contractors; raising at a reported $15–25B valuation) and **Mercor** (a $350M Series C in Oct 2025 at ~$10B valuation, reportedly ~$450–500M ARR by late 2025, up from ~$100M in March). These expert-RLHF players have genuine expertise-matching network effects, but the SAME dozen frontier labs are their customers — the concentration risk simply migrated. **Moat verdict: Tier 4, and not directly investable in public markets.**

### Risk-theme memo: Hyperscaler in-housing
Evidence FOR the threat: Google's termination of Appen; Meta's vertical integration of Scale; frontier labs building internal data teams. Evidence AGAINST (mitigants): labs still cannot scale expert human feedback internally fast enough, hence the Surge/Mercor boom; specialized data (legal, financial, medical) cannot be internalized at all. Conclusion: in-housing is a hard ceiling on commodity-labeling margins but does not threaten Tier 1 data owners.

### Risk-theme memo: Synthetic data
Synthetic data displaces commodity annotation (machines do volume) but cannot replace expert human feedback or unique real-world corpora (model-collapse risk per Shumailov et al., Nature 2024; humans audit and set policy). Gartner's Alexander Linden has been cited predicting that "by 2030, synthetic data will completely overshadow real data in AI models," adding "high-quality, high-value AI models simply won't be possible without the use of synthetic data" — treat this as a vendor-friendly directional projection, not fact. Timeline: synthetic is already standard for augmentation in 2025–2026; full substitution for frontier post-training is not here. Winners: owners of real data (scarcity rises) and synthetic-software vendors (Gretel/NVIDIA). Losers: commodity bulk labelers.

### Risk-theme memo: Copyright & litigation
- **Pro-rightsholder:** Thomson Reuters v. Ross (Feb 2025, no fair use); Getty's limited UK trademark win over Stability AI ([2025] EWHC 2863 (Ch), Nov 4, 2025); UMG–Udio and WMG settlements (Oct–Nov 2025) forcing licensed AI music.
- **Pro-developer:** Bartz v. Anthropic and Kadrey v. Meta (June 2025, training ruled transformative/fair use); Getty's abandonment of its UK primary-infringement and database claims (couldn't prove UK-based training) — the core "is training infringement?" question was left undecided in the UK.
- **Net read:** legal ambiguity persists, but the COMMERCIAL equilibrium — labs paying institutional rightsholders to de-risk — is already entrenched ($2B+ in deals). This is a tailwind for owners of clean, indemnifiable corpora and roughly neutral-to-negative for pure scrapers. The unresolved US fair-use questions (NYT v. OpenAI; Getty's refiled N.D. Cal. case, now in mediation) remain the key swing factor.

## Recommendations

**Stage 1 — Core positions (act now), 2–3 year horizon:**
- **Overweight the Tier 1 toll booths: RELX and Thomson Reuters,** and secondarily **S&P Global and Moody's.** These convert the data-scarcity theme into recurring, sticky, margin-expanding revenue without the customer-concentration fragility of the labelers. Benchmarks to watch: underlying organic revenue growth sustaining high-single-digits and AI-product (Lexis+AI/Protégé, CreditCompanion, Capital IQ Pro) attach rates. Thesis breaks if generative search materially disintermediates professional research workflows (watch retention dropping below ~90%).
- **Selective position in Reddit (RDDT)** as the one scaled, scarce public text corpus with demonstrated pricing power. Falsifying signal: licensing ("Other revenue") stalling AND ad growth decelerating simultaneously; a Perplexity-style adverse ruling that weakens enforcement.

**Stage 2 — Tactical / watch-list:**
- **Innodata (INOD):** trade, don't marry. The growth is real but the ~58–61% single-customer concentration makes it a high-beta proxy for frontier-lab capex. Re-rate UP only if top-customer concentration falls below ~35% while growth holds; exit signal is any disclosed large-customer reduction (the "Appen tell").
- **Getty/Shutterstock (GETY/SSTK):** event-driven on merger completion and AI-licensing monetization, but structurally challenged demand caps the upside. Avoid as a core holding.

**Stage 3 — Avoid / not investable:**
- **Appen (APX.AX):** secular decline, proven in-housing victim.
- **TELUS Digital (TIXT):** taken private by TELUS Corp (closed Oct 31, 2025) — no longer investable.
- **Private labelers (Scale, Surge, Mercor):** thesis-relevant but only accessible via secondaries; the Scale episode shows the neutrality moat is brittle.

**Thresholds that would change the call:** (1) A Third Circuit reversal of Thomson Reuters v. Ross re-establishing broad fair use for training would weaken the "forced licensing" tailwind for data owners. (2) Evidence that frontier labs can substitute synthetic + in-house expert data at scale (e.g., a major lab publicly cutting external data spend) would further impair the labelers. (3) A scaled, EXCLUSIVE data-licensing deal (vs. today's non-exclusive norm) would materially re-rate whichever owner signs it.

## Caveats
- **Disclosure gaps are pervasive.** Most AI-licensing deal values are press estimates, not audited figures (Reddit-Google ~$60M, OpenAI ~$70M, News Corp ~$250M/5yr are all reported, not filed). Labelers and labs do not name their concentrated customers ("a prominent social media company," "five of the Magnificent Seven"). Treat customer-concentration figures and private-company revenues (Scale, Surge, Mercor) as directional.
- **Private-market valuations are not investable and may be distorted** by strategic/acqui-hire dynamics (Scale's $29B is anchored to Meta's talent grab, not standalone cash flow; Surge's $15–25B and Mercor's $10B marks are negotiation-stage).
- **Synthetic-data displacement timing is genuinely uncertain;** the bifurcation thesis (commodity loses, expert wins) is well-supported but the crossover date is not knowable.
- **Legal outcomes remain unsettled;** the key US fair-use questions (NYT v. OpenAI; Getty's refiled N.D. Cal. case) are unresolved as of mid-2026.
- Several supporting datapoints (BloombergGPT cost/token figures, some private-company revenues, certain earnings-call quotes) come from secondary aggregators rather than primary transcripts and are flagged as such; the structural conclusions do not depend on any single contested number.

---

**Bottom line for the reader's test — "who owns a toll booth and who is selling a commodity?"** Toll booths: RELX, Thomson Reuters, S&P Global, Moody's (proprietary data fused to sticky workflows), with Reddit as the one scaled standalone-corpus toll booth. Commodities: the pure labelers — Innodata (INOD), Appen (APX.AX), TELUS Digital — selling rentable human labor into a market their largest customers can in-house or automate. The expert-RLHF middle (Scale, Surge, Mercor) is lucrative but private and structurally fragile, not a toll booth.