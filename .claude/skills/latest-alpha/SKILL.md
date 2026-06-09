---
name: latest-alpha
description: "Consolidate one company's recent developments between the lagging 10-Q/10-K cycles — pull SEC 8-K/424B5/6-K (Tier-1, timely) + investor-relations press releases + conference / investor-day materials (slides, webcasts) + reliable news, tier-rank by impact, and write a discovery note of primary-source-verifiable leads. Discovery-only: never edits canonical vault pages."
---

# latest-alpha — a company's recent developments, tier-ranked, between filings

This skill answers one question for a single company: **"what has actually moved since we last looked, and what of it can be verified at primary?"** It fills the gap the periodic filings leave — 10-Q/10-K land months late, so the timely signal lives in **8-Ks, financing filings, IR press releases, and reliable news**. This skill pulls all of that, sorts it by source tier and thesis impact, and turns it into a list of **leads to verify at the next primary source** — without letting any marketing-tier claim touch a canonical page.

## The hard boundary (read first — this is the whole point)

Recent IR / press / news sits **low in the vault's source hierarchy** (CLAUDE.md Section 2.2): SEC 8-K / 424B5 / 6-K are **Tier 1 and timely** (usable), earnings/IR commentary is **Tier 2** (management-colored), company press releases + financial news are **Tier 4** ("reliable for events, shallow on thesis"), and price-action / influencer chatter is **Tier 5** ("signal for questions; never cited"). Per CLAUDE.md Section 4.6, **marketing/IR + third-party summaries are NOT eligible for "Codified background"** — they go under "structural context to verify at primary."

Therefore this skill is **discovery-only**, with ONE narrow, fenced exception — the on-page digest block (Step 6b). It MUST NOT, under any circumstances:
- edit `wiki/_thesis.md`, `wiki/_thesis-defense-drones.md`, `wiki/_thesis-humanoid-robot.md` (human-owned anchors),
- edit any `raw/notes/frameworks*.md` (human-owned),
- edit, create, or delete any page under `wiki/`, OR edit any part of a company page **other than** the single fenced `Latest alpha` block on the run's own target company. Chokepoint / theme / relationship / layer pages are NEVER touched. On the target company page, frontmatter (incl. `last_updated`), Thesis role, Financial snapshot, and every verified section are NEVER touched — only the content between the `<!-- LATEST-ALPHA:START -->` / `<!-- LATEST-ALPHA:END -->` markers,
- touch `index.md`, `log.md`, `refresh_log.md`, or `conventions-ledger.md`.

It produces three artifacts: (1) the **discovery note** under `raw/notes/latest-alpha/`, (2) a **compact, fenced `Latest alpha` digest block** on the target company's page (Step 6b), and (3) a short chat summary. The on-page block is a *quarantined, dated, tier-tagged digest that links to the note* — never blended into canon, never asserted as verified fact. Anything that should reach the canonical analysis still goes through the **normal primary-source ingest**, human-gated (the two-stop protocol). The skill's job is to tell the user **what to go verify**, not to verify it. Mirror of `/youtube-intel`, plus this one fenced block.

## When to use

- The user invokes `/latest-alpha <TICKER>` (or names a company and asks "what's new / recent developments").
- A refresh is being scoped and the user wants the between-filings signal before deciding whether a real ingest is warranted.
- The user pastes a ticker and asks to "expand the knowledge base" from recent IR / press releases / news.

Do **not** use this for: a deep primary-source ingest (that's the human-gated two-stop ingest), a broad topic/community sweep (that's `/last30days`), or a single named video (that's `/youtube-intel`).

## Inputs

One ticker (default), or a few tickers (one note each). Optional: a window override ("since March", "last 60 days") — otherwise the window anchors to the vault page's `last_updated`.

## Step 1 — Preconditions

- Resolve `python3` (for the EDGAR helper).
- Ensure the save dir exists: `mkdir -p raw/notes/latest-alpha/` (relative to vault root).
- The helper lives at `.claude/skills/latest-alpha/scripts/edgar_recent.py`.

## Step 2 — Anchor to the vault

Before searching, read the company's vault page so the run is "what's new **since we last ingested**" and the cross-references are accurate:
- `wiki/companies/<TICKER>.md` frontmatter → `last_updated` (sets the window), `layer` + `*_tier` (current placement), `foreign_issuer`.
- If no page exists, this is a discovery on a **not-yet-covered** name — note that; the window defaults to ~120 days.
- Skim the page's Open questions + any pre-registered tier-upgrade trigger — recent news that bears on a pre-registered trigger is the highest-value find.

## Step 3 — Tier-1 SEC anchor (run the helper)

Run the EDGAR helper, anchored to the page's `last_updated` (fall back to `--days 120` if no page):
```bash
python3 .claude/skills/latest-alpha/scripts/edgar_recent.py <TICKER> --since <LAST_UPDATED>
```
It prints, newest-first: **material-event / financing filings** (8-K, 424B5/S-3 financings, 6-K) with dates + document URLs, and separately flags any **periodic reports** (10-Q/10-K/20-F/40-F) in the window.

- **Periodic report in the window = a REAL-INGEST candidate, not latest-alpha.** Flag it ("a new 10-Q/10-K has been filed → this is a proper human-gated ingest, not a discovery note") and do not try to cover it here.
- **Read the 8-Ks that look material.** The helper's descriptions are sparse ("FORM 8-K"); `WebFetch` the specific filing URL to get the Item content when a date looks important (financing, customer, guidance, leadership, facility). Item 1.01 / 2.03 / 3.02 / 8.01 are the usual material ones.
- **Foreign / non-SEC filer:** the helper exits with "ticker not found in SEC map." That's expected for the A-share / EDINET cohort ([[SANHUA]], [[HARMONIC]], etc.) — the SEC anchor is N/A; fall back to IR + news only (Step 4) and say so.

## Step 4 — IR press releases, conference / investor-day materials + reliable news (balanced net)

Pull the secondary sources for the same window. **Balanced breadth** = SEC (Step 3) + company IR (press releases AND events/presentations) + recent conference appearances + top-tier news + fast filing-aggregators, with promo/pump sites blocked.

1. **Company IR newsroom — press releases (Tier 4, authoritative for PRs).** Find the IR press-release URL (search `"<Company> investor relations press releases"`; e.g. AAOI = `investors.ao-inc.com/news-events/press-releases`) and `WebFetch` it for the dated PR list. If `WebFetch` drops the socket, fall back to the StockTitan per-ticker news/filings page (a reliable dated mirror).
2. **IR Events & Presentations + conference materials (Tier 2 — primary commentary).** Distinct from the press-release page, and easy to miss: most IR sites have a separate **"Events & Presentations"** section where **investor-day decks, conference webcasts, and slide PDFs** are posted (search `"<Company> investor relations events presentations"`, or look for an `/events`/`/presentations` path on the IR domain). `WebFetch` it for recent + upcoming **investor days, analyst days, and industry-conference appearances** (e.g. **OFC** for photonics, **GTC**, technology days, sell-side conferences) plus any posted slides / webcast replay. Treat conference + investor-day *presentations* as **Tier 2** (management-colored, same tier as an earnings call); third-party conference *coverage* is Tier 3/4. A slide/webcast is often the **first** place a roadmap or customer detail appears, ahead of the next filing — exactly the timely signal this skill exists to surface.
   - **Apply the cross-venue disclosure gap lens (CLAUDE.md Section 3.6).** Flag when something material is disclosed at a conference / investor day / technology day but is NOT addressed at the adjacent earnings call or 10-Q — that venue asymmetry is itself a vault-tracked signal (canonical case: NVDA's CPO detail living at GTC while the earnings call stays silent). Honest-framing discipline: "silence at one venue ≠ retreat" if the disclosure venue is durable — note the pattern, don't over-read it. This is a primary candidate for the note's red-flags / verify-at-primary sections.
3. **Reliable news (Tier 4).** One or two `WebSearch` passes:
   - `"<Company> <TICKER> news <month year>"`
   - `"<Company> <TICKER> press release <year> [order|customer|financing|guidance|product]"`
   - Prefer Reuters / Bloomberg / WSJ / FT / SEC for the facts; **aggregators** (StockTitan, Quartr, TipRanks) are fine for *surfacing* 8-Ks/PRs fast but treat their framing as Tier 4.
   - **Block the obvious pump/promo sites** via `blocked_domains` (e.g. `stockstotrade.com`, `timothysykes.com`) — they recycle the same facts wrapped in hype; if a fact only appears there, mark it Tier-5 and verify elsewhere.
4. **Sentiment / price action (Tier 5, signal only).** Capture "what's driving the tape" (PT hikes, short interest, a leveraged ETF) in ONE line, explicitly labeled signal-only — never weight it.

## Step 5 — Classify + rank

For every item: tag the **source tier** (1/2/4/5), tag **verifiability** — `[verifiable]` (could be checked at a 10-K/10-Q/8-K/call), `[opinion]`, `[forward]` — and rank by **thesis impact** (does it strengthen / challenge / refine the relevant thesis, or is it off-thesis noise?). Flag **aligned commercial incentive** where present (IR talking its own book; sponsored coverage).

## Step 6 — Write the discovery note

Save to:
```
raw/notes/latest-alpha/<RUN_DATE>_<TICKER>_recent-developments.md
```
`<RUN_DATE>` = today (YYYY-MM-DD). Use this structure (the `2026-06-09_AAOI_recent-developments.md` note is the canonical exemplar — match it):

1. **Header** — run date, ticker, vault page + current placement (layer/tier, last_updated), and a one-paragraph **"what this is"** boundary disclaimer (Tier-3/4 discovery log, not canon, not in index.md).
2. **TL;DR** — 3-6 lines, plain language: the real signal *and* the honest counterweight in the same breath.
3. **Timeline of material events** — table: date × event × where-it-lives (8-K / 424B5 / PR / conference deck / news) × tier/status, newest first.
4. **Impact-ranked developments** — the bull driver(s) AND the honest-verdict counterweights (dilution, concentration, valuation), each with its tier + verifiability.
5. **Named entities** — table: entity × claim × vault-page (`[[TICKER]]` if it exists, plain text if not) × confidence, applying the **disclosed / inferable / unknown** discipline (analyst-inferred customer names stay hedged).
6. **Contradictions / red flags** — where news conflicts with vault findings, shows promotional incentive, or makes an unsupported leap.
7. **Primary-source-verifiable leads → verify at the next 10-Q/10-K/8-K** — the payoff: concrete, numbered things to confirm at primary, including anything that bears on a pre-registered tier-upgrade trigger.
8. **Source-tier verdict (restated)** — one line: which items are Tier-1/ingest-ready vs Tier-4/discovery-only; confirm the canonical page was left untouched.
9. **Sources** — the URLs used, as markdown links.

`raw/notes/latest-alpha/` is a Tier-3/4 discovery log, **not** vault canon and **not** in `index.md`/`log.md` — its files do not count for accounting, exactly like `raw/notes/video-intel/`, `refresh_log.md`, and `conventions-ledger.md`.

## Step 6b — Update the on-page `Latest alpha` digest block (the one canon-adjacent write)

Update a single, fenced, **compact** digest block on the **target company's** page. This is the ONLY edit the skill makes to any `wiki/` page, and it is bounded by HTML-comment markers so it can never bleed into canon. **Only do this for a company that has a `wiki/companies/<TICKER>.md` page AND was run this session** — never pre-create the block on other pages.

**Block template** (compact digest + link — the full write-up stays in the Step 6 note):
```markdown
<!-- LATEST-ALPHA:START -->
## ⚠️ Latest alpha — unverified, between-filings (as of <RUN_DATE>)

*Tier 3/4 discovery — NOT canonical. Recent 8-K / conference / news, to verify at the next primary source. Full detail + sources: [discovery note](../../raw/notes/latest-alpha/<RUN_DATE>_<TICKER>_recent-developments.md). Items graduate into canon (or are pruned) at the next 10-Q/10-K ingest.*

- **<headline>** (<venue: 8-K / 424B5 / conference / news>, <date>) — Tier <n> · <one clause; bull driver or honest counterweight>. `[verify: <what, where>]`
- … (4–6 bullets MAX — lead with the most material; always include the honest counterweight, not just the bull item)
- Related: [[TICKER]] [[TICKER]] (<why linked>)

*Signal only (not weighted): <PT hikes / leveraged ETF / short interest> — one line.*
<!-- LATEST-ALPHA:END -->
```

**Placement + write rules:**
- If the markers are **absent**, insert the whole marked block (markers included) **immediately before `## Change log`**. If the markers are **present**, **replace everything between them** (keep the markers). Never edit a single character outside the markers.
- **Compact only.** 4–6 bullets + one `Related:` line + one `Signal only` line. The page shows the digest; the note holds the detail. If you're tempted to paste the timeline table, stop — that lives in the note.
- **Tag every bullet** with its tier and a `[verify: …]` trigger. Apply the honest-verdict discipline: the block must surface the counterweight (dilution / concentration / governance), never just the bull story.
- **Cross-company = wikilinks ONLY.** Link related names in the `Related:` line; do NOT open or edit those companies' pages (no cascade).
- **Do NOT change frontmatter `last_updated`** — that field tracks primary-source canon only. Add nothing to `index.md` / `log.md` (the block does not count for accounting, like the note).

**Graduation + decay (anti-rot — enforce every run):** the block is **transient and rebuilt fresh each run for the current window**. When you rebuild it: **drop any item the page's canonical sections already reflect** — a primary ingest has since absorbed it, so let canon own it. Check the page body + Change log to decide this; do NOT rely on the `last_updated` date alone — that is the *ingest* date, and the ingest may cover only an earlier fiscal period, so an 8-K / conference event dated *before* `last_updated` but *after* the covered period-end is NOT yet in canon and should be KEPT. Also drop anything a since-run filing has confirmed. Keep only still-open, still-recent items, and if one is already in canon but newly relevant, mention it as "(already in canon)" rather than re-asserting it. The skill does NOT fold verified items into canon itself — that is the human-gated ingest's job; the skill only keeps the digest current and pruned. If, after pruning, nothing material remains, replace the bullets with a single line: `- (nothing material since last primary ingest)`.

## Disciplines to apply throughout (same as the vault)

- **Honest-verdict** — surface the dilution / concentration / red-flags *next to* the bull items, never buried. If the recent flow is all hype and no real signal, say so plainly and keep the note short.
- **Describe-don't-recommend** — no buy/sell. Reframe "should I buy X" into "what would have to be true for the thesis to hold."
- **Thesis tool, not portfolio tracker** — no P&L, no position sizing.
- **Section 4.6 four-tier discipline** — never present Tier-4/marketing as primary-verified. The deliverable is *what to verify*, not the verification.
- **Disclosed / inferable / unknown** (CLAUDE.md Section 3.3) — exact data only from filings; analyst-inferred customer names ("Amazon-linked") stay inferable + hedged.
- **Plain language** in the chat summary.

## Step 7 — Output to the user (chat)

Lead with the **TL;DR + tier verdict**, then the **top impact-ranked items** (bull driver + honest counterweight together), then the **verify-at-primary leads** (the actionable part), then where the note was saved + that the page's fenced `Latest alpha` block was refreshed (if the company has a page). Scannable, plain language. End by reminding (once) that this is discovery-only — nothing touched canon except the fenced, quarantined `Latest alpha` block; naming what to verify is the deliverable. If a new periodic report (10-Q/10-K) landed in the window, say so prominently — that's a real-ingest cue, not a latest-alpha output.

## What this skill is NOT

- Not a way to add IR / press / news claims to **canon** — its only on-page footprint is the fenced, explicitly non-canonical `Latest alpha` digest block; verified facts still enter canon only via the human-gated primary-source ingest.
- Not a primary-source ingest (that's the human-gated two-stop ingest of 10-K/10-Q/call).
- Not a broad topic sweep (use `/last30days`) or a single-video analysis (use `/youtube-intel`).
- Not a buy/sell recommender, and not a price/sentiment tracker (Tier-5 is signal-only, one line).
