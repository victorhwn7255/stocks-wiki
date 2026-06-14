---
name: bear-case
description: "The complete, ranked bear case for one stock — what could go wrong, how real each risk is, and what to watch — by fusing the vault's structured risk homes (the what-could-go-wrong register, forward-edge-tracker, the company page, chokepoint/theme pages, spread-watch) with /latest-alpha + /last30days + a reliable-source web pass. Ranks on Severity × Evidence × Proximity (never fake probabilities), gives a tripwire per top risk, and closes with the steelman. Discovery-only: never edits canonical vault pages."
---

# bear-case — the complete, ranked risk map for one stock

When you hold or are weighing a position, the question that matters is **"what kills this?"** — the full failure map, ranked, with a watch-list. The vault already holds rich risk material, but it's scattered across the `what-could-go-wrong` register, the forward-edge-tracker, each company page's Risk-factors + Open-questions, the chokepoint/theme pages, and spread-watch. `/bear-case` is the **one command** that pulls it all together for a single name, adds fresh signal, ranks it honestly, and pre-registers what to watch. It is the **bottom-up dual** of the top-down `[[what-could-go-wrong]]` register, and it productizes the vault's 4th discipline ("host tensions honestly") at the per-stock level.

It is architecturally the same plumbing as `/priced-in` (an orchestrator that invokes `/latest-alpha` + `/last30days` and fuses with canon) **pointed at a different question.** `priced-in` asks "is the good news already in the price?" (both sides, narrative-saturation). `bear-case` is **risk-only, deeper on the downside, ranked, and ends in a watch-list.**

## The hard boundary + the one discipline that makes this safe (read first)

**The trap.** A "what could go wrong" sweep — especially one that reads `/last30days` (Reddit / X, which skews fear and hype) — naturally becomes a **doom machine** that scares you out of good positions. The fix is the vault's honest-verdict discipline, applied ruthlessly: **grade every risk for how REAL it is, mark overblown ones overblown, and close every report with one line — "the steelman against this whole bear case."** A run that finds 8 catastrophic risks for every stock is a failed run.

This skill is **discovery-only**. It MUST NOT:
- edit `wiki/_thesis.md`, `wiki/_thesis-defense-drones.md`, `wiki/_thesis-humanoid-robot.md` (human-owned),
- edit any `raw/notes/frameworks*.md` (human-owned),
- edit, create, or delete any page under `wiki/` (company / chokepoint / theme / relationship / layer / tracker) — including `what-could-go-wrong`, `forward-edge-tracker`, and any `Latest alpha` block,
- touch `index.md`, `log.md`, `refresh_log.md`, or `conventions-ledger.md`.

It produces exactly two artifacts: (1) the **discovery report** under `raw/notes/bear-case/`, and (2) a scannable chat summary. Anything that should reach a vault page (e.g. a new *system-level* risk that belongs in the `what-could-go-wrong` register) is a **separate, human-gated** action the user asks for — this skill only **flags** the candidate. Same boundary as `/priced-in` and `/latest-alpha`.

## What it produces
- A discovery report → `raw/notes/bear-case/<RUN_DATE>_<TICKER>_bear-case.md` (Tier-3/4 discovery log; NOT vault canon; not in `index.md`/`log.md` — doesn't count for accounting, like `priced-in/` + `latest-alpha/` + `video-intel/`).
- A scannable chat summary: **the #1 thing that breaks this → the ranked bear case → the watch-list → the steelman line.**

## When to use
- The user invokes `/bear-case <TICKER>` (or asks "what could go wrong with X", "what's the bear case on X", "what are the risks with X", "what kills this position").
- Stress-testing a name you hold or are weighing.

Do **not** use this for: a buy/sell call (it describes risk, it does not recommend), a primary-source ingest (the human-gated two-stop ingest), or the "is it priced in" question (that's `/priced-in`).

## Inputs
One ticker (must be a vault-covered name for the full value; uncovered names get a thin web-only version, flagged). Optional depth flag: `quick` (`/bear-case <T> quick` — vault + a fast 8-K check only). Default is `deep`.

## Step 1 — Preconditions
- Resolve `python3` (quick mode uses `/latest-alpha`'s EDGAR helper).
- Ensure the save dir exists: `mkdir -p raw/notes/bear-case/`.
- Note the depth mode: **`deep`** (default — vault + latest-alpha + last30days + web) vs **`quick`** (vault + EDGAR 8-K check only; no last30days/web).

## Step 2 — Anchor to canon + harvest the vault's structured risk homes (THE differentiator)
This is the value-add — without it the skill just re-derives risks from scratch and misses the cross-vault hits. Read and aggregate:

1. **The company page** `wiki/companies/<TICKER>.md` (Tier 1/2 — highest weight): Risk-factors summary, Open questions, Thesis-role honest-verdict / weak-fit notes, customer-concentration tables, financial-fragility sections (debt / dilution / cash burn), Caveat #9 Layer-straddling tensions, A1 over-claim flags. No page → "**uncovered name** — thin web-only version, low confidence."
2. **The cross-vault risk hits** — `grep -l "<TICKER>" wiki/trackers/*.md`, then pull the *specific* content naming the ticker:
   - `[[what-could-go-wrong]]` — the exact register entries naming it (these are the system-level risks that hit this name).
   - `[[forward-edge-tracker]]` — any consensus-vs-vault divergence entry (esp. an *inverse* divergence = the vault is already less bullish than the market).
   - `[[AI-credit-spread-watch]]` — if it's a credit name (CRWV/ORCL/NBIS/AVGO), the relevant dial + reading.
3. **Fragility flags on theme/chokepoint pages** — `grep -l "<TICKER>" wiki/chokepoints/*.md wiki/themes/*.md`; surface where it's framed as a counterpoint, displaced, or structurally weak (e.g. [[AAOI]] on [[cpo-integration]]; an Outside-Framework placement; a memory-shortage victim row).
4. **Multi-thesis names** (MP / NVDA / AVGO / PLTR / HARMONIC) — harvest risks across **all** their domains, not just one.

## Step 3 — Timely layer (fresh risks — newer than the last ingest)
- **DEEP:** invoke the latest-alpha skill, then read its note:
  ```
  Skill("latest-alpha", args="<TICKER>")
  ```
  Read `raw/notes/latest-alpha/<RUN_DATE>_<TICKER>_recent-developments.md` (reuse a same-day note if one already exists — do not re-run). Mine it for **risk events**: dilution / new shelf, guidance cut, a lost or concentrated customer, governance changes, financing stress, an SPV/backstop disclosure.
- **QUICK:** skip the full skill; run the EDGAR helper for recent 8-Ks only:
  ```
  python3 .claude/skills/latest-alpha/scripts/edgar_recent.py <TICKER>
  ```
  and read any material 8-K (financing / customer / guidance / leadership).

## Step 4 — Narrative layer (DEEP only — what the crowd FEARS)
Invoke the last30days skill:
```
Skill("last30days", args="<TICKER>")
```
It auto-generates its own plan; read its raw artifact (newest `~/Documents/Last30Days/<slug>-raw-*.md`). **Use it ONLY to (a) surface what the crowd fears and (b) gauge whether a risk is widely-known vs under-the-radar** — never as a source of fact (Tier 4/5: "signal for questions, never cited"). **This is where the anti-doom discipline bites hardest** — the crowd over-weights scary narratives; treat every social-sourced risk as a *question to verify*, grade it RUMOR until a higher tier confirms it, and discard pure panic. Thin coverage → say so and lower confidence.

## Step 5 — Reliable-source web pass (DEEP only — validate + size the real risks)
A focused WebSearch on the *specific* risks surfaced so far, to validate and size them at Tier 3/4: rating-agency views (Moody's/S&P/Fitch), reputable analyst risk flags, sector risk reports, regulatory actions. Prefer Reuters / Bloomberg / WSJ / FT / SEC / rating agencies; block promo/pump sites. Cite with attribution; never treat as established fact. The goal is to turn a vague worry into a sized, sourced risk — or to retire it.

## Step 6 — Structure into the fixed taxonomy + rank
Sort every surfaced risk into the taxonomy (adapt emphasis to company type — a moonshot's shape [dilution / cash burn / narrative-outrunning-proof] differs from a fortress's, a chokepoint-owner's [policy / geology / single-customer], or a neocloud's [refi / concentration / circular financing]):

- **Thesis / structural** — what breaks the core structural story (displacement, the chokepoint de-risking, the moat eroding).
- **Customer concentration** — single-customer / top-5 dependence; counterparty credit.
- **Competitive / displacement** — a technology transition or rival that erodes the position.
- **Financial** — debt load, refinancing walls, dilution pattern, cash burn, margin compression.
- **Expectations / narrative-saturation** — how much good news is already assumed (framed via saturation, **never** via price/multiples).
- **Macro / cycle** — which `what-could-go-wrong` register entries hit this name (capex cycle, credit shock, policy).
- **Governance / management** — leadership, accounting, insider, control-weakness flags.

Each risk carries five tags:
- **Tier** — source quality (T1 filing / T2 call / T3 analysis / T4 news / T5 social).
- **Severity** — thesis-ending · serious · flesh-wound.
- **Evidence** — **FACT-today** (a number in a filing now) · **SCENARIO** (a plausible future) · **RUMOR** (social/unconfirmed). *This is the honest substitute for fake probabilities.*
- **Proximity** — dated catalyst (name the date) · ongoing · someday.
- **Realness grade** — strong · moderate · weak · **overblown** (the anti-doom check; call weak risks weak).
- **Tripwire** — the observable that tells you this risk is firing (a 10-Q line item, a rating action, a spread-watch dial, a contract non-renewal).

**Rank** by Severity × Evidence × Proximity. A FACT-today + thesis-ending + dated-catalyst risk leads; a SCENARIO + someday risk trails. Lead the report with the single highest-ranked item: **"the #1 thing that breaks this."**

## Step 7 — Save + report
Save the full report to `raw/notes/bear-case/<RUN_DATE>_<TICKER>_bear-case.md` (header + depth/coverage caveat + the #1 break + the ranked taxonomy with all five tags per risk + the consolidated watch-list + the **steelman** line + a sources line + a one-line "register-candidate?" verdict). Then emit the chat summary (Step 8). If a genuinely new *system-level* risk surfaced (one that would hit many names), **flag** it as a `[[what-could-go-wrong]]` register candidate — do not write the register.

## Disciplines to apply throughout (the guardrails — without these it becomes a doom machine)
1. **Honest-verdict / anti-doom.** Grade each risk's realness; mark overblown ones overblown; **close every report with "the steelman against this whole bear case."** Matters most because last30days skews fear. If the honest verdict is "this name's risks are mostly priced/mitigated," say so plainly.
2. **Tier discipline.** A 10-K fact ≠ a Reddit panic. Canon (Tier 1/2) > latest-alpha (Tier 1-timely/3/4) > web (Tier 3/4) > last30days (Tier 4/5, sentiment-only). Every risk tier-tagged; a social fear never ranks equal to a filing fact (grade it RUMOR until confirmed higher).
3. **Honest ranking, not fake probabilities.** Severity × Evidence × Proximity — never invented percentages or "70% chance."
4. **Describe-don't-recommend; thesis-tool-not-tracker.** No buy/sell, no position-revealing. Reframe "should I sell?" → "what would have to be true for the thesis to break." No price targets / market cap / valuation multiples (price action only as a labeled "signal-only" line).
5. **Discovery-only.** Never edits canon; the report lives in `raw/notes/bear-case/`. Register/canon updates are separate human-gated actions — flag, don't cascade.
6. **Plain language** in the chat output.
7. **Honest about coverage.** Thin last30days/web coverage → say so and lower confidence; uncovered name → flag the weak canon anchor.

## Step 8 — Output to the user (chat)
Lead with the headline, then the ranked case, scannable and plain:
- **The #1 thing that breaks this** — one line.
- **The ranked bear case** — the top risks, each with its tier · Severity/Evidence/Proximity · realness grade · tripwire (compact; the full set lives in the saved note).
- **The watch-list** — the tripwires consolidated into "what to watch" (the actionable payoff).
- **The steelman** — one line: the honest case *against* this whole bear case (what the bears are missing / what's already mitigated or priced).
- Where the report saved + (if any) the `[[what-could-go-wrong]]` register-candidate flag.
End by reminding (once) that this is discovery-only and risk-lens-only — nothing touched canon; the deliverable is the ranked bear case + the watch-list, honestly graded.

## What this skill is NOT
- Not a buy/sell recommender — it maps risk, it does not tell you what to do.
- Not a valuation tool — it never computes or cites price, market cap, multiples, or price targets.
- Not a doom generator — risks are graded for realness, overblown ones are marked, and every run closes with the steelman.
- Not the "is it priced in" question (that's `/priced-in`), not a primary-source ingest (the human-gated two-stop ingest), and not a way to write to canon or the register (it only flags candidates).
- Not a fact source from social — last30days is used for fear/saturation signal only, never as ground truth.
