---
name: priced-in
description: "Per-stock report answering two simple questions — what is ALREADY priced in vs. what is NOT yet priced in — by fusing vault canon + /latest-alpha (60-day events) + /last30days (crowd narrative). Judges 'priced in' by narrative saturation, never valuation math; the 'not priced in' half always splits into upside AND risk. Discovery-only: never edits canonical vault pages."
---

# priced-in — what's priced in vs. what isn't, for one stock

The stock market is a **forward pricing mechanism**: by the time a fact is widely known, it's largely in the price. So the edge in analyzing a name is knowing **what's already priced in** (no edge left) vs. **what isn't yet** (where the edge is). This skill answers exactly those two questions for one ticker, by fusing three layers the vault already has — and it's the on-demand, per-stock version of the forward-edge layer (`[[forward-edge-tracker]]` / CLAUDE.md §3.18).

## The hard boundary + the one idea that makes this safe (read first)

**The trap.** "Priced in" sounds like it needs price reasoning — stock price, valuation multiples, price targets. The vault **bans all of that** from analysis (CLAUDE.md §2.1 thesis-tool-not-portfolio-tracker; §3.18). So this skill must answer a price-about question **without doing price math.**

**The fix — judge "priced in" by NARRATIVE SATURATION, not valuation.**
- **Priced in** = already in the consensus conversation: widely disclosed, widely discussed, already reacted to. (Measured by `/last30days` saturation + the analyst/IR framing + `/latest-alpha` events the market has already moved on from.)
- **Not priced in** = what the *structural* (vault) analysis sees that the conversation doesn't yet.

This is an honest **proxy, not a measurement** — the skill can know "what's in the narrative vs. what the structure sees the narrative missing," but it cannot literally know what the price embeds. **Say this every run.**

This skill is therefore **discovery-only**. It MUST NOT:
- edit `wiki/_thesis.md`, `wiki/_thesis-defense-drones.md`, `wiki/_thesis-humanoid-robot.md` (human-owned),
- edit any `raw/notes/frameworks*.md` (human-owned),
- edit, create, or delete any page under `wiki/` (company / chokepoint / theme / tracker / relationship / insight) — including the `forward-edge-tracker` and any `Latest alpha` block,
- touch `index.md`, `log.md`, `refresh_log.md`, or `conventions-ledger.md`.

It produces exactly two artifacts: (1) the **discovery report** under `raw/notes/priced-in/`, and (2) a short two-bucket chat summary. Anything that should reach a vault page (a canon update, or a `forward-edge-tracker` entry) is a **separate, human-gated** action the user asks for — this skill only *flags* candidates. Same boundary as `/latest-alpha` and `/youtube-intel`.

## What it produces
- A discovery report → `raw/notes/priced-in/<RUN_DATE>_<TICKER>_priced-in.md` (Tier-3/4 discovery log; NOT vault canon; not in `index.md`/`log.md` — its files don't count for accounting, like `raw/notes/latest-alpha/` + `video-intel/`).
- A scannable **two-bucket chat summary**: ✅ priced in / 🔍 not priced in.

## When to use
- The user invokes `/priced-in <TICKER>` (or asks "what's priced into X / what's not priced in yet").
- Sizing up a name before a deeper look — the fast "where's the edge" read.

Do **not** use this for: a primary-source ingest (the human-gated two-stop ingest), a pure recent-events pull (that's `/latest-alpha` alone), or a buy/sell call (this describes what's priced, it does not recommend).

## Inputs
One ticker. Optional: a note on what the user already believes ("I'm bullish on the laser story") — useful for honest-verdict framing, but never lets the output tilt bullish.

## Step 1 — Preconditions
- Resolve `python3` (the composed `/latest-alpha` uses its EDGAR helper).
- Ensure the save dir exists: `mkdir -p raw/notes/priced-in/`.

## Step 2 — Anchor to canon (the structural truth = the backbone)
Read `wiki/companies/<TICKER>.md` (Tier 1/2 — the highest-weight layer):
- **Thesis role** — the structural position + honest verdict (this is what the narrative may be missing).
- **Open questions** + any pre-registered **tier-upgrade trigger** — these are the vault's own pre-registered "not-yet-resolved" items, i.e. prime "not priced in" candidates.
- Any existing **`[[forward-edge-tracker]]`** entry for the name (the curated consensus-vs-vault view, if one exists).
- No page exists → flag "**uncovered name — canon anchor is weak**"; lean harder on latest-alpha + last30days and lower confidence accordingly.

## Step 3 — Timely layer (the recent events)
Invoke the latest-alpha skill for the name:
```
Skill("latest-alpha", args="<TICKER> last 60 days")
```
Then read the note it writes at `raw/notes/latest-alpha/<RUN_DATE>_<TICKER>_recent-developments.md` (if a same-day note already exists, reuse it rather than re-running). This gives the Tier-1-timely 8-K/financing events, conference disclosures, and the "signal only" price-action line. Events here that the market has *already reacted to* → **priced in**; events still filing-unconfirmed or just-surfaced → candidate **not priced in**.

## Step 4 — Narrative / sentiment layer (what the crowd is saying)
Invoke the last30days skill for the name:
```
Skill("last30days", args="<TICKER>")
```
It auto-generates its own query plan and its setup is complete. Read its raw artifact — glob `~/Documents/Last30Days/` for the newest `*-raw-*.md` produced by the run. **Use it ONLY to gauge narrative saturation** — how heavily, and in which direction, the crowd (Reddit / HN / web / YouTube) is talking — never as a source of fact (it's Tier 4/5: "signal for questions, never cited"). 
- **Heavy, one-directional chatter** (a name is "all over fintwit/Reddit") → that storyline is **saturated = priced in**.
- **Thin coverage** (obscure name, little chatter) → say so plainly and degrade to "canon + latest-alpha only"; the priced-in read is lower-confidence.

## Step 5 — Synthesize into the two buckets (the forward-edge lens)
Cross the three layers. Weight **canon (Tier 1/2) > latest-alpha (Tier 1-timely/3/4) > last30days (Tier 4/5)**.

- **✅ Already priced in** — what's saturated in the narrative + widely disclosed + already reacted to. Include **both** the bull points *and* the bear points the crowd already knows (e.g. "the ramp + the guidance raise" *and* "the known dilution"). These are no longer edge.
- **🔍 NOT priced in** — what the structural read sees that the conversation doesn't. **ALWAYS split two ways:**
  - **(a) Un-priced upside / optionality** — latent structural levers the narrative under-weights (e.g. a pre-registered tier-upgrade trigger that hasn't fired). Each with a **catalyst** (the dated event that would force the market to price it).
  - **(b) Un-priced risk** — structural fragilities the hype glosses (concentration, dilution magnitude, a governance flag, a displacement threat unnamed in filings). Each with a **catalyst / what to watch.**
  Tier-tag every item; add a one-line confidence note.

## Step 6 — Save + report
Save the full report to `raw/notes/priced-in/<RUN_DATE>_<TICKER>_priced-in.md` (header + the proxy/coverage caveat + the two buckets with tiers/catalysts + a sources line + a one-line "tracker-candidate?" verdict). Then emit the chat summary (Step 7). If a high-conviction divergence surfaced, **flag** that it's a `[[forward-edge-tracker]]` entry candidate — do not write the tracker.

## Disciplines to apply throughout (the guardrails — without these this becomes a hype machine)
1. **Narrative-saturation proxy, NOT valuation math.** No stock price / market cap / multiples / price targets in the analysis. Price action / PTs appear only as **labeled "signal-only" evidence of attention/saturation**, never as a valuation conclusion.
2. **"Not priced in" MUST include risk, not just upside.** The AAOI lesson: the un-priced thing was the *downside* (dilution, auditor change), not hidden upside. A "not priced in" bucket with only upside is a failure — regenerate it.
3. **Tier discipline + canon-priority.** Canon outranks latest-alpha outranks last30days. last30days measures *sentiment*, never asserts *fact*. Tag every item.
4. **Discovery-only.** Never edits canon; the report lives in `raw/notes/priced-in/`. Tracker/canon updates are separate human-gated actions.
5. **Describe-don't-recommend; thesis-tool-not-tracker.** No buy/sell, no position-revealing. Reframe "is it a buy?" → "what's priced and what isn't."
6. **Honest about the proxy + coverage.** Every run states "priced in = a narrative proxy, not a measurement," and flags thin-coverage names.
7. **Plain language** in the chat summary.

## Step 7 — Output to the user (chat)
Lead with a one-line framing, then the two buckets, scannable and plain:
- **✅ Priced in** — 3–6 tier-tagged bullets (bull *and* bear points the crowd already holds).
- **🔍 Not priced in** — *un-priced upside* (with catalysts) **and** *un-priced risk* (with catalysts); both halves mandatory.
- **Narrative-saturation read** — one line: how covered the name is → how reliable the priced-in call is, plus the proxy caveat.
- Where the report saved + (if any) the `[[forward-edge-tracker]]` entry-candidate flag.
End by reminding (once) that this is discovery-only and a narrative proxy — nothing touched canon; the deliverable is the two-bucket read + what to watch.

## What this skill is NOT
- Not a valuation tool — it never computes or cites price, market cap, multiples, or price targets.
- Not a buy/sell recommender — it describes what's priced, not what to do.
- Not a primary-source ingest (the human-gated two-stop ingest), and not a way to write to canon or the forward-edge tracker (it only flags candidates).
- Not a fact source from social — last30days is used for saturation/sentiment only, never as ground truth.
