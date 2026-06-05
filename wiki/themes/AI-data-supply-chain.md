---
type: theme
tickers: [INOD]
last_updated: 2026-06-05
---

# AI Data Supply Chain — the "picks-and-shovels" of AI training data

*Tier 3-anchored theme (per CLAUDE.md Section 3.13). Anchored on two commissioned research reports — `raw/research/ai-data-supply-chain-report.md` (round 1) + `raw/research/ai-data-supplier-report.md` (round 2, primary-source verification). Structural framework paraphrased in wiki voice; report figures are Tier 3 and carry verify-at-primary status until a name is ingested. The one name ingested with primary sources to date is [[INOD]], whose figures are primary-verified.*

## Thesis relevance

This theme maps the **data** side of the AI boom — the companies that supply, license, clean, label, and evaluate the data that trains and aligns AI models — through the vault's chokepoint / value-capture lens. It is adjacent to, but distinct from, the AI-datacenter supply chain (compute / photonics / memory / power / equipment): that chain is the physical *buildout*; this is the *feedstock*. Companies here sit **outside** the datacenter per-domain frameworks — they carry no `layer`/`*_tier` — and are organized by where they fall on a value-capture gradient instead.

The demand-side hook ties back to [[AI-demand-durability]]: high-quality public training text is getting scarce (the "data wall" — frontier labs have largely exhausted the open web; commissioned-report Tier-3 estimate of median exhaustion ~2028), which is what could turn *data* from a commodity input into a genuine constraint. Scarcity raises the value of a unique **owned corpus** (a stock you own) far more durably than it raises the value of annotation **labor** (a flow you rent).

## The value-capture gradient (the centerpiece)

The defining finding: "AI-data picks-and-shovels" flatters the whole group, but the moat gradient is steep — the same shape as the Defense chokepoint-quality gradient (own-the-chokepoint beats sell-the-service):

| Tier | Position | Moat | Examples |
|---|---|---|---|
| **Toll booth** | Proprietary data fused to a sticky professional workflow | Highest — can't relabel or synthesize around it | RELX, Thomson Reuters, S&P Global, Moody's |
| **Scarce corpus** | A uniquely scaled, licensable dataset | Real but narrower (non-exclusive licensing) | Reddit (RDDT) |
| **Challenged owner** | Owns a real library but the core demand is being displaced | Eroding | Getty (GETY) / Shutterstock (SSTK) |
| **Fragile expert services** | Premium expert-RLHF / evaluation labor | High-growth but rented-land (customer-concentrated) | Scale AI, Surge AI, Mercor (all private) |
| **Commodity labor** | Annotation / labeling / data-prep services | Lowest — labor arbitrage, low switching costs | **[[INOD]]**, Appen, TELUS Digital |

**Ownership alone is not the moat — ownership *plus* workflow lock-in is.** A hyperscaler can't relabel its way around Westlaw headnotes (Thomson Reuters won exactly this point in *v. Ross*), credit-rating histories, or LexisNexis case law; it *can* in-house a room of annotators.

## Two headline findings

1. **The publicly-investable pure-play *supplier* surface is razor-thin — essentially one name of size: [[INOD]].** Once the incumbents that keep their data are removed, the only US-listed "sells-data/labeling-into-the-AI-boom" pure-play of meaningful size is Innodata, with Reddit a scarce-corpus hybrid whose actual licensing line is small (~5–6% of revenue). The interesting expert-RLHF middle (Scale / Surge / Mercor) is all **private**. So the category is far thinner than the narrative implies.
2. **The highest-quality "AI-data" names win by *not* selling shovels.** The toll-booth compounders (RELX, Thomson Reuters, S&P Global, Moody's, FactSet) **restrict** training use of their data, sell permissioned "AI-ready" access, and build their own AI products — so by their own disclosure they are **AI-*deployer* incumbents, not data suppliers**. Their AI value is embedded-product uplift on an existing sticky business, not data sold into the supply chain. The corollary is uncomfortable: the companies whose actual *business* is supplying the AI boom are thin and structurally fragile; the great businesses keep their gold and use it themselves.

## Supplier vs AI-deployer incumbent (the split that matters)

- **Suppliers (sell into the AI boom):** [[INOD]] (pure commodity→expert services); Reddit (partial, scarce corpus); Getty/Shutterstock (permissioned license-out atop a declining core); News Corp / Wiley / Universal Music / Warner Music (episodic license-out checks); the private trio (Scale / Surge / Mercor).
- **Incumbents (keep their data, deploy their own AI):** RELX, Thomson Reuters, S&P Global, Moody's, FactSet, Morningstar.

The single most important distribution development: the **entitlement / MCP-server model** (FactSet's production-grade MCP server; Moody's, S&P, LSEG, Morningstar connectors). MCP (Model Context Protocol) lets an AI agent query a data source live, so owners monetize AI *access* **without surrendering training rights** — "have your cake and eat it," and the most durable model in the chain.

## Three risk pillars

1. **Hyperscaler in-housing (demonstrated, not hypothetical).** Google terminated Appen and internalized rater capacity; Meta's $14.3B Scale stake routed work in-house, prompting Google/OpenAI/xAI to pull back. In-housing is a hard ceiling on commodity-labeling margins — but does not threaten the toll-booth data owners.
2. **Synthetic-data bifurcation.** Synthetic data is a complement, not a substitute: it already displaces commodity annotation in *verifiable* domains (code, math via reward-checkable training), but recursive training on synthetic data causes "model collapse" (Shumailov et al., *Nature* 2024), so expert-judgment and safety data stay human-dependent. The market splits: **commodity labeling loses, expert RLHF wins.**
3. **Copyright tilted pro-developer.** 2025 rulings (Bartz v. Anthropic; Kadrey v. Meta) made training-as-fair-use the trajectory, collapsing any "owners get paid regardless" symmetry. Owners now get paid only with **both** unique data **and** enforcement leverage (registration, contract/ToS, technical gating). The one clean large transfer — the **$1.5B Anthropic settlement** — is for *pirated acquisition*, not for training being infringement. NYT v. OpenAI is the live swing factor.

## The investable surface (vault action)

- **Ingest / anchor:** [[INOD]] — the one liquid US-listed pure-play supplier (ingested S135; the theme's anchor).
- **Watch (no page yet):** Reddit (RDDT) — scarce corpus, but underwrite it as an advertising business with a data-licensing call option; Cloudflare (NET) — the pay-per-crawl "toll-collector" and the leading indicator for the "can owners charge crawlers?" thesis, but immaterial to revenue today; Getty/Shutterstock (GETY/SSTK) — a clean displacement-analysis case (license AND get displaced).
- **Separate scope decision (NOT this theme):** the incumbents RELX / Thomson Reuters / S&P Global / Moody's / FactSet — AI-deployer compounders, not suppliers; a distinct question (their own theme, or out of scope).
- **Private → mention-only:** Scale AI / Surge AI / Mercor (the expert-RLHF middle; not investable in public markets).

## Open questions (primary-source verification triggers — A2)

1. **Pure-play count.** Does the public AI-data-*supplier* category grow past one name of size? Only if it does would a dedicated `data_tier` framework codification (human-owned) be warranted — held for now (YAGNI at n=1).
2. **The toll-booth incumbents.** If Vic elects to bring RELX / TRI / SPGI / MCO into the vault, each is a standard primary-source ingest — and the disintermediation question (does AI erode the *workflow* that makes the data sticky?) gets tested at primary then.
3. **Reddit licensing materiality.** Does RDDT "Other revenue" reaccelerate with disclosed usage-based pricing, or stay a small option?
4. **The toll-collection layer.** Does a major AI lab publicly agree to pay-per-crawl / RSL terms, or does Cloudflare break out pay-per-crawl revenue? Either would move NET from watch to live.

## Source audit notes

- **Provenance + attribution.** Anchored on two **commissioned research reports** (Tier 3 independent analysis, `raw/research/`): round 1 (structural map) + round 2 (primary-source verification addendum, June 2026). Team-authored — closer to a sell-side report than to Vic's human-owned `frameworks.md`; the structural framework is scaffolding paraphrased in wiki voice, **not** human-owned canon. Per Section 2.2, report figures are Tier 3 and carry **verify-at-primary** status; only [[INOD]]'s figures have been primary-verified (S135).
- **Describe-don't-recommend.** The underlying reports carried buy/sell framing ("overweight RELX," "avoid Appen"); that is stripped here — placements are stated as value-capture / what-would-have-to-be-true, per Section 2.1.
- **The data-wall + TAM figures** (median exhaustion ~2028; labeling TAM $1.1–4.9B; "labs spend ~$1B/yr each") are Tier-3 / press estimates, directional only.

## Cross-references

- [[INOD]] — the anchor pure-play (commodity→expert-services supplier); the one primary-verified name.
- [[AI-demand-durability]] — the demand-side sibling; the data wall is a demand-side constraint, and AI-data spend is the recipient side of frontier-lab budgets.
- [[PLTR]] — adjacent: an AI-native data/analytics platform (a *consumer*/deployer, not a data supplier); INOD does Federal computer-vision work in concert with Palantir.

## Change log

- **2026-06-05 (S135 — creation):** Created as a Tier-3-anchored theme on the two commissioned AI-data-supply-chain research reports, alongside the [[INOD]] first-canonical ingest. Centerpiece: the owner-vs-labeler value-capture gradient + the two headline findings (the public pure-play *supplier* surface is ≈ one name; the high-quality names win by keeping their data). Three risk pillars (in-housing / synthetic bifurcation / pro-developer copyright + the MCP-entitlement model). Investable surface: INOD the one pure-play ingest; RDDT/NET/GETY/SSTK watch; incumbents (RELX/TRI/SPGI/MCO/FDS) flagged separate-scope; Scale/Surge/Mercor private/mention-only. No `data_tier` codification (YAGNI at n=1). `tickers: [INOD]` (only primary-sourced name).
