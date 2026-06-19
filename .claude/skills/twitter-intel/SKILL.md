---
name: twitter-intel
description: Turn a Vic-staged X/Twitter thread (a PDF export in raw/notes/twitter-notes/, or pasted thread text) into a vault-aware intelligence note — named tickers, key claims tagged verifiable/opinion/forward, vault cross-references, and primary-source-verifiable ingest leads. Twitter/X is Tier 5 (social) — signal for generating questions, NEVER cited as vault fact. Discovery-only — writes a note to raw/notes/twitter-intel/ and nothing else; never edits wiki/ pages, the _thesis/frameworks anchors, index.md, or log.md. Use when the user invokes /twitter-intel, pastes an X/Twitter thread or x.com/twitter.com URL, or asks to analyze a staged twitter-notes file.
---

# twitter-intel — turn an X/Twitter thread into vault-aware intelligence

This skill converts a Twitter/X thread into a structured intelligence note for the **stocks-wiki** vault. Vic stages threads (as PDF exports) in `raw/notes/twitter-notes/`; this skill mines them into searchable, vault-aware research **without** letting bottom-tier social content leak into the canonical pages. It is the Twitter sibling of `youtube-intel`.

## The hard boundary (read first — this is the whole point)

X/Twitter sits at the **very bottom of the vault's source hierarchy** (CLAUDE.md Section 2.2): it is **Tier 5 social** — "signal for generating questions; never cited." Unlike `youtube-intel` (which can land at Tier 3 for a genuine independent analyst), **a Twitter thread is Tier 5 by default** — the only per-run judgment is whether to flag it as *aligned commercial incentive* (someone talking their own book / pumping a ticker / promoting a newsletter) or to dismiss it as pure noise. It is **never** ground truth.

Therefore this skill is **discovery-only**. It MUST NOT, under any circumstances:
- edit `wiki/_thesis.md`, `wiki/_thesis-defense-drones.md`, `wiki/_thesis-humanoid-robot.md` (human-owned anchors),
- edit any `raw/notes/frameworks*.md` (human-owned),
- edit, create, or delete any page under `wiki/` (company / chokepoint / theme / tracker / relationship),
- touch `index.md`, `log.md`, `refresh_log.md`, or `conventions-ledger.md`.

It produces exactly two artifacts: (1) the **intel note** under `raw/notes/twitter-intel/`, and (2) a short summary in chat. Anything that should actually reach a vault page goes through the **normal primary-source-verified ingest**, human-gated (the two-stop protocol), in a *separate* action the user explicitly asks for. The skill's job is to tell the user **what to go verify**, not to verify it. (Mirror of `youtube-intel`, minus the Tier-3 possibility — Twitter has a hard Tier-5 floor.)

## When to use

- The user invokes `/twitter-intel <file-or-ticker>` or pastes an X thread / `x.com` / `twitter.com` URL and wants analysis.
- The user points at a staged file in `raw/notes/twitter-notes/` (e.g. `AAOI-2026-06-14.pdf`) and asks to mine it.
- A vault task would benefit from analysing a specific thread Vic has staged.

Do **not** use this for a broad multi-post community sweep (that's `/last30days`), a named video (that's `/youtube-intel`), or a primary-source ingest.

## Inputs

One of:
- **A staged PDF** in `raw/notes/twitter-notes/` — the default. Vic captures a thread as a PDF named `<TICKER>-<DATE>.pdf` (e.g. `AAOI-2026-06-07.pdf`). **The Read tool reads PDFs natively** — no extraction/cleaner script is needed (unlike `youtube-intel`'s `clean_subs.py`); just `Read` the file (use the `pages` param for a long thread).
- **Pasted thread text** — if Vic pastes the thread directly into chat, use it as-is.
- **A URL** — accept it for context, but note that **X is auth-walled**: a direct fetch usually fails. Ask Vic to stage a PDF (or paste the text) rather than relying on a fetch. **Never fabricate thread content from a URL alone.**

## Step 1 — Preconditions

- Ensure the save dir exists: `mkdir -p raw/notes/twitter-intel/` (relative to the vault root).
- Identify the input: a staged PDF path, pasted text, or (rarely) a URL.

## Step 2 — Read the thread

- **PDF:** `Read` the file directly (it renders the thread text + visible images). The export carries X UI chrome (trending sidebar, Follow buttons, engagement counts) — mentally strip that; the substance is the thread body. Capture the **author handle**, the **post date**, and the **engagement counts** (these gauge reach, not truth).
- **Pasted text:** use it as-is.
- If the thread is in another language, render claims in English but keep the **original text for every company name, ticker, and key phrase** in parentheses (the same name-fidelity discipline as `youtube-intel` — names are exactly what gets mangled).

## Step 3 — Classify the source by Tier (mandatory; the floor is fixed)

State it plainly: **Tier 5 (social) — signal for generating questions; never cited.** Then judge the *kind* of Tier-5 source:
- **Independent retail/analyst thread** — reasoning from public data. Still Tier 5, but the *questions* it raises may be worth verifying.
- **Aligned commercial incentive** — the author is talking their own book, pumping a ticker, promoting a newsletter/Substack, or is company IR. Flag it explicitly (CLAUDE.md "skip promotional content and aligned commercial incentive") and keep the note short + skeptical.
- **Pure hype / reaction** — no checkable substance. Say so in one line and stop; don't manufacture relevance.

The Tier-5 verdict gates how much weight every downstream claim gets — which is "verify before trusting," always.

## Step 4 — Analyze into the intel note

Cross-reference the vault as you go: for every company/ticker named, check whether a page exists (`grep -i "<ticker>" index.md` or look under `wiki/companies/`), and which theme/chokepoint pages it touches. Use the three theses as the evaluation lens (does this **strengthen / challenge / refine** a thesis, or is it off-thesis noise?).

Produce this structure (in the saved note and, condensed, in chat):

1. **Header** — author handle, thread date, source file (or "pasted"), engagement counts, URL if known, and the **Tier-5 verdict** from Step 3 (at the top — it gates everything).
2. **TL;DR** — 3-5 lines: the thread's core claim in plain language.
3. **Named entities** — a table of every ticker/company × the claim made about it × whether a **vault page exists** (`[[TICKER]]` if yes, plain text if no). Flag any name that looks garbled.
4. **Key claims + numbers** — bulleted, each tagged: `[verifiable]` (could be checked at a 10-K/10-Q/20-F/8-K/earnings call) · `[opinion]` (the author's read) · `[forward]` (speculative/future-looking).
5. **Vault cross-reference** — which existing pages/themes/chokepoints this touches; for each, whether it **confirms / challenges / adds to** the relevant thesis, or is **off-thesis**. Name pages with `[[wikilinks]]` only when they exist.
6. **Ingest leads** — the payoff: concrete, **primary-source-verifiable** follow-ups (e.g. *"Thread claims AAOI landed a hyperscaler 800G order → verify in the next AAOI 10-Q / 8-K"*), plus any **new-name candidates** that might cross the page-creation threshold (3+ sources / chokepoint-central).
7. **Contradictions / red flags** — where the thread conflicts with vault findings, shows promotional incentive, or makes an unsupported leap.
8. **Source-tier verdict (restated)** — one line: "Tier 5 — do not cite as vault fact; use to generate questions; verify against primary sources before any page edit."

Disciplines throughout (same as the vault): **honest-verdict** (if it's hype with no signal, say so and keep the note short — don't manufacture relevance); **describe-don't-recommend** (reframe "should I buy X" into "what would have to be true"); **plain language** in the chat summary; never treat a thread number/name as exact.

## Step 5 — Save the note

Write the full note (header → analysis → raw thread text appendix) to:
```
raw/notes/twitter-intel/<THREAD_DATE>_<author-or-ticker-slug>_<topic-slug>.md
```
- `<THREAD_DATE>` = the thread's post date (YYYY-MM-DD); fall back to the staged file's date, then today.
- Slugs: lowercase, hyphenated, ASCII, trimmed to ~40 chars.
- Put the **raw thread text** at the bottom under `## Thread (Tier 5 — not a primary source)` so it is greppable later, but keep the **analysis at the top**.
- Append a one-row entry to `raw/notes/twitter-intel/_index.md` (create it if absent), mirroring `raw/notes/video-intel/_index.md`: `| <date> | <author> | T5 | <tickers> | <trackers touched> | <one-line gist> |`.

`raw/notes/twitter-intel/` is a Tier-5 intel log — **not** vault canon and **not** in `index.md`/`log.md`; its files do not count for accounting, exactly like `raw/notes/video-intel/`, `refresh_log.md`, and `conventions-ledger.md`.

## Output to the user (chat)

Lead with the **Tier-5 verdict + TL;DR**, then the **named-entities** read, then the **ingest leads** (the actionable part), then where the note was saved. Keep it scannable and plain-language. End by reminding (once) that this is discovery-only — nothing touched the vault pages, and naming what to verify is the deliverable.

## What this skill is NOT

- Not a way to add Twitter claims to the vault directly (that violates the source hierarchy — Tier 5 is never cited).
- Not a broad multi-post community sweep (use `/last30days`) or a single-video analysis (use `/youtube-intel`).
- Not a primary-source ingest (the human-gated two-stop ingest of 10-K/10-Q/call).
- Not a buy/sell recommender.
