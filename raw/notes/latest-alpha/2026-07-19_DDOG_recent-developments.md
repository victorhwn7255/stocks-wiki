# DDOG (Datadog, Inc.) — latest alpha, between-filings recent developments

**Run date:** 2026-07-19 · **Ticker:** DDOG · **Vault page:** `wiki/companies/DDOG.md` (`layer: outside` + all five `*_tier: outside`; `last_updated: 2026-07-18`)
**Window:** ~2026-05-07 (Q1 2026 10-Q/call, the canonical baseline) → 2026-07-19 (today).

**What this is (boundary disclaimer).** A Tier-3/4 **discovery log**, not vault canon. It consolidates recent SEC 8-Ks (Tier 1, timely), the DASH 2026 user-conference materials (Tier 2, management-colored), a tuck-in acquisition PR (Tier 4), and reliable news — tier-ranked, turned into a list of leads to **verify at the next primary source** (Datadog's Q2 2026 10-Q/8-K/call, expected ~early August 2026). Nothing here is canon; nothing here touched any `wiki/` page (note-only / headless mode). Not in `index.md`/`log.md`; does not count for accounting.

---

## TL;DR

- **The one genuinely material, not-yet-in-canon item: the Adaptive ML tuck-in acquisition (June 30, 2026)** — a frontier-AI startup building an RLOps (reinforcement-learning-ops) platform for enterprise post-training/agents, folded into "Datadog AI Research" to work on **world models + agentic LLM post-training for observability**. **Terms undisclosed.** This is Datadog moving up-stack from *observing* AI into *building/training* AI models — a strategy signal worth verifying at the Q2 filing.
- **DASH 2026 (June 9–10, NYC) was a big product event, not a financial one** — 100+ features, headlined by **autonomous Bits AI agents** (detect → validate → remediate), an **Agent Console** that monitors third-party coding agents (Claude Code, Cursor, GitHub Copilot), **AI Guard** (prompt-injection / agent-poisoning security), and **Bring Your Own Cloud (BYOC)**. All Tier 2 (management-colored); none of it is sized in dollars — it extends the vault's existing "custom-silicon heterogeneity tailwind" + "agentic-consumption" reads, it doesn't change them.
- **No financing, no guidance change, no new periodic report** since the Q1 baseline. The two 8-Ks in the window are **routine** (Q1 earnings release + annual-meeting vote results). **Q2 2026 earnings have NOT reported yet** — the next primary source is the real ingest cue.
- **Honest verdict: watch-list, not ingest-now.** The window is real but quiet on the numbers. Adaptive ML + DASH are strategy/product color to *verify at Q2*, not events that force pulling a source set early.

---

## Timeline of material events

| Date | Event | Where it lives | Tier / status |
|---|---|---|---|
| 2026-06-30 | **Acquired Adaptive ML** (RLOps / post-training startup) → Datadog AI Research; terms undisclosed | PR (globenewswire / datadoghq.com) | Tier 4 · `[verifiable]` at Q2 (M&A note / cash-flow line) |
| 2026-06-16 | 8-K — 2026 Annual Meeting vote results (Item 5.07): 4 directors elected, say-on-pay + auditor ratified, simple-majority shareholder proposal **rejected** | SEC 8-K | Tier 1 · routine / immaterial |
| 2026-06-09–10 | **DASH 2026** user conference (NYC) — 100+ features: autonomous Bits AI agents, Agent Console (monitors Claude Code/Cursor/Copilot), AI Guard, BYOC, Federated Logs | Conference / IR press release / blog | Tier 2 · `[forward]`/`[verifiable]` |
| 2026-05-07 | 8-K — Q1 2026 earnings release (Item 2.02) | SEC 8-K | Tier 1 · **already in canon** (Q1 call) |
| 2026-05-07 | **10-Q — Q1 2026 (period 2026-03-31)** | SEC 10-Q | Tier 1 · **already in canon** (the page's baseline) |
| 2026-04-22 | **GPU Monitoring GA** worldwide (GPU = ~14% of compute cost framing) | PR | Tier 4 · **already in canon** (page names GPU Monitoring); pre-baseline |

---

## Impact-ranked developments

1. **★ Adaptive ML acquisition (June 30, 2026) — the most material, not-in-canon item. Tier 4 (PR) · `[verifiable]`.** Datadog acquired Adaptive ML, a frontier-AI startup with an **RLOps platform** (build/own/deploy specialized enterprise agents + models), and put it inside "Datadog AI Research" to accelerate **world models + agentic LLM post-training for observability**. Terms undisclosed; team size undisclosed. Datadog frames it against its "$1B+ annual R&D." **Thesis read:** consistent with the page's agentic-consumption + training-as-a-market threads — but a *strategic escalation*: Datadog is moving from *monitoring* AI workloads to *training/post-training* models itself. Fits the tuck-in pattern the page already flags ("DDOG does tuck-ins"). Honest counterweight: an undisclosed-terms acqui-hire of a frontier-model team is a **capability/margin question**, not a revenue event — watch whether it pressures the thin GAAP profile (Open Q#5, SBC/dilution) or shows up as goodwill/IPR&D.
2. **★ DASH 2026 — autonomous Bits AI agents + Agent Console. Tier 2 · `[forward]`.** The headline: Bits AI agents that autonomously investigate/validate/remediate, plus an **Agent Console** centralizing monitoring of *third-party* coding agents (Claude Code, Cursor, GitHub Copilot). This is the **agentic-observability expansion** the Q1 call pre-flagged, now productized. It reinforces (does not change) the page's "usage bills whether a human or an agent drives it" thesis and the "monitor other people's AI agents" angle. Counterweight: 100+ features, zero revenue attribution — classic conference breadth; separability of the AI suite as a *market* stays contested (Open Q#1).
3. **AI Guard + BYOC + Federated Logs. Tier 2 · `[forward]`.** AI Guard (prompt-injection / agent-poisoning defense) extends the security suite into the agent-security niche; BYOC (process/index in the customer's own cloud object storage) + Federated Logs (query Databricks/ClickHouse in place) target the **soaring-log-cost** objection — a defense of the consolidation moat vs open-source/DIY. Refines, doesn't move, the thesis.
4. **Annual-meeting vote (8-K, June 16). Tier 1 · immaterial.** Routine: 4 directors elected, say-on-pay + Deloitte ratified. Note only: a **simple-majority-voting shareholder proposal was rejected** — the dual-class founder-control structure (Open Q#5 context) stays intact. Governance-neutral, no thesis impact.

---

## Named entities

| Entity | Claim | Vault page | Confidence |
|---|---|---|---|
| Adaptive ML | Acquired by DDOG 2026-06-30; RLOps / post-training platform → Datadog AI Research | (no page) | **Disclosed** (PR); terms undisclosed |
| Claude Code / Cursor / GitHub Copilot | Third-party coding agents now monitorable via DDOG **Agent Console** | (no pages) | **Disclosed** (DASH) — DDOG monitors them, not a commercial relationship claim |
| Databricks / ClickHouse | External stores queryable in-place via **Federated Logs** | (no pages) | **Disclosed** (DASH) |
| [[CSCO]] (Splunk) | Consolidation competitor — unchanged; DASH log-cost features sharpen the contest | [[CSCO]] | Disclosed (context) |
| "AI research divisions at two of the world's largest technology companies" | Q1 land deals (7- + 8-figure) | — | **Inferable** only — names NOT disclosed; keep unnamed |

---

## Contradictions / red flags

- **No contradiction with canon.** DASH + Adaptive ML *extend* the page's existing threads (agentic consumption, custom-silicon heterogeneity, training-as-a-market, tuck-in M&A); nothing reverses a vault finding.
- **Cross-venue disclosure-gap lens (CLAUDE.md §3.6).** DASH (June 9–10) disclosed the autonomous-Bits-AI / Agent Console / AI Guard / BYOC roadmap and the Adaptive ML deal (June 30) landed **after** the Q1 call (May 7) but **before** any Q2 filing. So there is a real **conference-and-PR-ahead-of-filing** window: these are Tier 2/4 now, not yet Tier 1. Honest framing — "product venue ahead of filing ≠ retreat"; DASH is Datadog's durable annual disclosure venue, and Q2 (~August) is the natural place this graduates. Flag it as a verify-at-primary set, don't over-read it.
- **Promotional-incentive note.** DASH coverage (100+ features, "AI and Observability Event of the Year") is IR/marketing framing (Tier 2/4) — count the *capabilities*, not the adjectives; none is sized. GuruFocus/StockTitan/Quiver framing is Tier 4 aggregator, used only to surface the PRs.

---

## Primary-source-verifiable leads → verify at the Q2 2026 10-Q / 8-K / call (~early August 2026)

1. **Adaptive ML — does it appear in the Q2 financials?** Look for an acquisition footnote / goodwill / IPR&D / intangibles line and any cash-flow "acquisitions, net of cash" figure — terms were undisclosed in the PR. Confirms deal size + whether it's material to the balance sheet. Bears on **Open Q#5** (SBC/dilution/GAAP-profit trajectory) if it's stock-funded or adds IPR&D.
2. **Does the AI-native / AI-cohort disclosure advance further (the separability trigger, Open Q#1)?** Q1 gave growth-contribution (~7pts of Q4 growth) + customer counts but no clean revenue **level**. Watch Q2 for an AI-cohort revenue % — that resolves the [[AI-implementation-deployment-layer]] separability contest. The Adaptive ML/AI-Research push makes a cleaner AI-segment disclosure more plausible.
3. **Largest-customer / AI-native usage — did the demand dial hold (Open Q#2/#3)?** Q1 was the strongest sequential existing-customer usage since Q1 2022, with the ex-AI-native base re-accelerating to mid-20s%. Verify at Q2: did the broadening hold, and did the "extra conservatism to our largest customer" prove warranted (any sequential usage deceleration)? This is the 2022-optimization tripwire feeding [[AI-demand-durability]] / [[what-could-go-wrong]] / [[telecom-bust-analog]].
4. **Training-as-a-market / GPU Monitoring traction (Open Q#4-adjacent).** DASH pushed autonomous agents + Agent Console; GPU Monitoring is GA. Verify at Q2 whether hyperscaler/"superintelligence-lab" training-monitoring wins are quantified or named, and whether "hyperscalers come to us" persists vs CloudWatch/Azure-Monitor in-housing — feeds [[hyperscaler-custom-ASIC]].
5. **Guidance — any FY2026 raise?** No guidance update in the window. Confirm at Q2 whether the FY2026 $4.3–4.34B (+25–27%) / non-GAAP-op-income $940–980M frame moves — and whether Adaptive ML/DASH costs shift the margin guide.

---

## Source-tier verdict (restated)

- **Tier 1 / ingest-relevant:** two 8-Ks in the window — both **already-known or routine** (Q1 earnings release = in canon; annual-meeting vote = immaterial). **No new periodic report** since the Q1 10-Q. The 10-Q flagged by the helper is the **existing baseline**, already in canon — **not** a fresh ingest cue.
- **Tier 2 (management-colored):** DASH 2026 product roadmap — verify-at-primary, not canon.
- **Tier 4 (events, shallow on thesis):** Adaptive ML PR (undisclosed terms) — the most material item, `[verifiable]` at Q2.
- **Tier 5 (signal only, not weighted):** stock up ~89% YTD per Yahoo Finance framing — noted, never weighted.
- **Canonical page left untouched** (note-only / headless mode): no edit to `wiki/companies/DDOG.md`, `index.md`, or `log.md`.

**Verdict: WATCH-LIST, not ingest-now.** The window has one genuinely new strategic event (Adaptive ML) and a big-but-unsized product event (DASH), but no new numbers, no financing, no guidance change, and **no new periodic report**. Nothing here forces pulling the Q2 set early — the correct action is to let Q2 2026 (~early August) be the real ingest, working through the five verify-leads above.

*Signal only (not weighted): DDOG reportedly ~+89% YTD (Yahoo Finance, Tier 5) — tape context, never a vault input.*

---

## Sources

- SEC EDGAR — [8-K 2026-06-16 (Item 5.07, annual meeting)](https://www.sec.gov/Archives/edgar/data/1561550/000162828026043590/ddog-20260615.htm); [8-K 2026-05-07 (Q1 earnings release)](https://www.sec.gov/Archives/edgar/data/1561550/000162828026031677/); [10-Q Q1 2026 (baseline, in canon)](https://www.sec.gov/Archives/edgar/data/1561550/000162828026032328/ddog-20260331.htm)
- [Datadog — Acquires Adaptive ML (June 30, 2026)](https://www.datadoghq.com/about/latest-news/press-releases/datadog-acquires-adaptive-ml-to-accelerate-its-investment-in-ai-research-and-development/) · [globenewswire mirror](https://www.globenewswire.com/news-release/2026/06/30/3320108/0/en/Datadog-Acquires-Adaptive-ML-to-Accelerate-Its-Investment-in-AI-Research-and-Development.html)
- [Datadog — DASH 2026 keynote / feature roundup](https://www.datadoghq.com/blog/dash-2026-new-feature-roundup-keynote/) · [DASH 2026 recap](https://www.datadoghq.com/blog/dash-2026-recap/) · [SiliconANGLE — 100+ features / autonomous AI ops](https://siliconangle.com/2026/06/09/datadog-launches-100-features-dash-push-autonomous-ai-ops/)
- [Datadog — GPU Monitoring GA (Apr 22, 2026; pre-baseline, in canon)](https://www.datadoghq.com/about/latest-news/press-releases/datadog-gpu-monitoring-launch/)
