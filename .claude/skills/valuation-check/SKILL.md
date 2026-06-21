---
name: valuation-check
description: Reverse-DCF / market-implied-expectations check for one stock. Takes market cap as GIVEN and solves for what the market is implicitly assuming — the market is pricing in ~X% growth for Y years, and the price has baked in roughly $Z of future cash flow (explicit + terminal split) — then scores that implied growth against historical base rates (how rare it is for a company that size) and builds bull/base/bear. Two-agent orchestration around a deterministic engine — Agent 1 extracts inputs and runs the math, Agent 2 verifies and assesses plausibility. Discovery-only — writes ONE note to raw/notes/valuation-check/, never a wiki page, never a buy/sell. The quantitative cousin of /priced-in. Use on /valuation-check TICKER market-cap, or "what's priced into X", "reverse DCF on X", "what growth is baked into X".
---

# valuation-check — what the market is implicitly assuming (reverse DCF)

This skill runs a **reverse DCF**: instead of forecasting cash flows to derive a fair value, it takes the **current market cap as given** and solves for **what the market must believe** to justify it. The deliverables are the two headline reads you wanted — *"the market is pricing in ~X% growth for Y years"* and *"the price bakes in ≈$Z of future cash flow"* (split honestly into explicit-period + terminal value) — plus a base-rate plausibility verdict and bull/base/bear scenarios.

It is the **quantitative cousin of `/priced-in`** (which does the *qualitative* narrative-saturation read) and complements `/bear-case` (risk). The math lives in a deterministic script (`scripts/reverse_dcf.py` + `scripts/base_rate_score.py`) — LLMs fumble the iterative solve, so **agents do only the judgment**; the script does the arithmetic. Methodology is grounded in `raw/research/reverse-dcf-research.md` + `raw/research/reverse-dcf-implementation-reference.md` + `raw/research/mauboussin-base-rate-tables.md`.

## The hard boundary (read first — this is the whole point)

This skill computes the exact things the vault BANS from its pages — market cap, multiples, implied growth, price-vs-value. So it is **discovery-only**. It writes EXACTLY ONE file: the note at `raw/notes/valuation-check/<DATE>_<TICKER>_valuation-check.md`. It MUST NOT, under any circumstances:
- edit any `wiki/` page (company / chokepoint / theme / tracker / relationship), `index.md`, or `log.md`,
- edit `wiki/_thesis*.md` / `raw/notes/frameworks*.md` (human-owned anchors) or `CLAUDE.md`,
- run git.

Framing is **describe-don't-recommend**: *"the market is implying X — is that plausible?"*, **never** "fair value is Y" or "buy/sell." No price targets. The note is Tier-3 discovery material; nothing reaches canon. Same contract family as `/priced-in` / `/bear-case` / `/latest-alpha`. `raw/notes/valuation-check/` does not count for accounting (like the other discovery logs).

## When to invoke

- `/valuation-check <TICKER> <market-cap> [deep]` (e.g. `/valuation-check NVDA 5.1T`, or `/valuation-check NVDA 5.1T deep`).
- "what's priced into X", "reverse DCF on X", "what growth is baked into X's price", "is X priced for perfection".

**Market cap is REQUIRED and user-provided** — it needs a live share price, which isn't reliably auto-fetchable (do NOT auto-fetch). If the user omits it, ask for the current market cap (or price × shares) and stop until given. Optional overrides: WACC, horizon, terminal g.

**The organizing question (lead everything with it).** Every run answers one question in plain words: **"For the price to make sense, what does `<TICKER>` have to BECOME?"** The engine emits this as a `★ For the price to make sense, X must:` block — the ranked list of what must be true (the growth, the margin, clearing the history bar) plus the lever the answer hinges on most. That block leads the note AND the chat summary. It is the whole point — never bury it under the mechanics.

**Depth flag.** Default = the 2-agent run (extract+compute → adversarial verify). Add `deep` to turn on a **3rd red-team pass** (Step 3.5) for thesis-critical names — an agent that ONLY tries to find the most defensible inputs that would FLIP the verdict before you conclude.

Not for: a buy/sell call, a fair-value point estimate, a primary-source ingest, or any name where reverse DCF is the wrong tool (see the weak-fit flags below).

## Steps

### 1 — Preconditions
- `mkdir -p raw/notes/valuation-check/`.
- Confirm the market cap is in hand (ask if missing). Note net cash/debt if the user gave it; else Agent 1 pulls it from the filing.

### 2 — Agent 1: Extract + Compute (the input-judgment agent)
Spawn a sub-agent (Agent tool) to assemble clean inputs and run the engine. Its brief:
- Read `wiki/companies/<TICKER>.md` **`Financial snapshot`** as the primary source (human-verified canon); fall back to the latest filing in `raw/filings/<TICKER>/` for anything missing.
- **Choose the path:** `fcff` for a profitable, positive-FCF name; `revenue` (revenue × normalized-future-margin) for a pre-profit name (e.g. NVTS/CRWV).
- Assemble inputs: market_cap (user), net_debt (debt − cash; negative = net cash), **current revenue** (for the base-rate size bucket), shares; and for `fcff`: latest TTM/normalized **FCFF** (SBC **expensed**, NOT added back — use FCF already net of SBC); for `revenue`: current operating margin, a **normalized terminal margin** (benchmark mature sector peers — Damodaran sector margins in the research ref), sales-to-capital (~2–3), tax.
- **Pick a defensible WACC** from the reference bands (large-cap stable 7–9%, growth 9–12%) by the company's size/sector/leverage, or CAPM if the page gives a beta — and STATE it (Agent 2 will challenge it; the engine's sensitivity table already flexes ±1%).
- Run the engine via `--json` (cleanest) — **always pass `"name":"<TICKER>"`** so the engine leads with the "For the price to make sense, `<TICKER>` must ___" framing:
  ```bash
  python scripts/reverse_dcf.py --json '{"name":"NVDA","path":"fcff","market_cap":"5.1T","net_debt":"-50B","fcff":"120B","revenue":"200B","wacc":0.09,"terminal_g":0.03,"horizon":10}'
  ```
  (Passing `revenue` auto-enables the base-rate block; the engine also emits the `★ what-must-be-true` block + the ranked lever sensitivity.)
- Return: the engine output (incl. the `★ what-must-be-true` block) + **every input choice with its rationale + source** (so Agent 2 can audit it). Flag if reverse DCF is a **weak fit** here — cyclical at peak/trough (use normalized earnings), bank/financial (FCFF undefined → flag, don't force), holdco (sum-of-parts), distressed.

### 3 — Agent 2: Verify + Assess (the adversarial agent)
Spawn a second sub-agent to check Agent 1, not echo it. Its brief:
- **Adversarially re-check each input against the filing:** is the FCFF normalized (one-offs stripped, SBC expensed)? Is the terminal margin defensible vs mature peers, not best-in-class? Is the WACC reasonable? Is the path right? Correct anything wrong and note it.
- **Judge plausibility** using the engine's **base-rate block** (the implied growth's historical percentile by size) + a TAM/history sanity check — is the implied growth "common / aggressive / priced-for-perfection / no precedent"?
- **Build bull / base / bear** by re-running `reverse_dcf.py` with the **2–3 highest-sensitivity drivers** varied (revenue CAGR, terminal margin, CAP/horizon, occasionally WACC) — report each scenario's implied growth + Z/W + base-rate verdict. Keep the terminal disciplined (ROIC→WACC) so scenarios don't diverge through the terminal back door.
- **Sharpen the "what must be true" list** — for each must in the engine's `★` block, add the qualitative color from the filings: is the required margin one the company has *never hit*? Is the required growth one *no peer its size achieved*? That plain-language "what would have to be true" is the headline deliverable.
- Return the verification verdict (what held up / what it corrected) + the sharpened what-must-be-true list + the scenario table.

### 3.5 — Agent 3: Red-team (ONLY when `deep`)
If the user passed `deep`, spawn a third agent whose ONLY job is to **try to flip the verdict**: find the most *defensible* set of inputs (the genuine bull case — a higher-but-arguable terminal margin, a normalized-up cash flow, a lower WACC) that would make the price look reasonable, and run them. Then report honestly: does the verdict survive the strongest fair attack, or does it flip? This guards against a confident-but-fragile conclusion on thesis-critical names. Return: the strongest steelman inputs + whether the verdict held.

### 4 — Write the note (the skill does this single write)
`raw/notes/valuation-check/<RUN_DATE>_<TICKER>_valuation-check.md`:
1. **Header** — run date, ticker, market cap used, the one-paragraph "what this is" boundary (Tier-3 reverse-DCF discovery; not canon; not a fair-value/buy-sell).
2. **★ For the price to make sense, `<TICKER>` must become ___** — LEAD with this. The ranked what-must-be-true list (the growth, the margin, clearing the history bar), each with Agent-2's plain-language color ("a margin it has never hit"; "growth no peer its size achieved") + the lever the answer hinges on most.
3. **The two headlines** — *"the market is pricing in ~X% growth for Y years"* + *"the price bakes in ≈$Z explicit + $W terminal (TV% of value)"*.
4. **Price decomposition** — no-growth value vs growth premium (PVGO %).
5. **Plausibility** — the base-rate percentile + verdict (the killer line); the sensitivity table.
6. **Bull / base / bear** — the scenario table (implied growth + plausibility per case); + the red-team verdict if `deep` (did it survive the strongest fair attack?).
7. **Assumptions + Agent-2 verification** — the full input set (outputs are conditional on it), what Agent 2 corrected, and the weak-fit caveat if any.
8. **Sources** — wiki snapshot + filing used.

### 5 — Report to the user (chat)
**Lead with the framing in plain words:** *"For the price to make sense, `<TICKER>` would have to become ___"* — then the ranked what-must-be-true list (growth + margin + how rare that is), then **bull/base/bear** in one line each (+ the red-team result if `deep`), then where it saved. Plain language. End by reminding once that this is discovery-only and implied-expectations-only — it says what the market is betting on and how rare that is, NOT whether to buy.

## Disciplines

- **Discovery-only** — one note under `raw/notes/valuation-check/`; never canon, anchors, index/log, or git.
- **Describe-don't-recommend** — implied-expectations framing only ("the market is betting on X; historically that's top-N% rare"); never a fair value, price target, or buy/sell.
- **Math in the script, judgment in the agents** — agents never do the DCF arithmetic by hand; they pick inputs and assess. Every number traces to a `reverse_dcf.py` run.
- **SBC expensed, never added back**; terminal value perpetuity-growth with g ≤ R_f; the outputs are **conditional on the assumption set** — always show it.
- **Honest about fit** — if reverse DCF is the wrong tool for this name (cyclical/bank/holdco/distressed), say so plainly rather than print a confident-looking but meaningless number.
- **Plain language** in the chat summary.

## What this skill is NOT

- Not a fair-value or price-target tool — it computes what's *implied*, not what's *right*.
- Not a buy/sell recommender, and not a way to write valuation numbers onto any `wiki/` page.
- Not a primary-source ingest (the human-gated two-stop), and not the qualitative "is the good news priced in" read (that's `/priced-in`) or the risk map (that's `/bear-case`) — it's the quantitative what's-priced-in.
