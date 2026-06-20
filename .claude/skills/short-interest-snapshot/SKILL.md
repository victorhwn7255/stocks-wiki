---
name: short-interest-snapshot
description: Snapshot FINRA short interest for the vault's US-listed names into raw/data/short-interest/. Pulls the twice-monthly FINRA Consolidated Short Interest (official, all US exchanges) for every US-eligible vault ticker, joins SEC shares-outstanding for a % figure, writes one dated CSV, and reports the crowding/positioning signal. Discovery-only Tier-4 sentiment data — never canon. Use on /short-interest-snapshot, "snapshot the short interest", "pull short interest for the vault", or "how shorted are our names".
---

# short-interest-snapshot — capture FINRA short interest for the vault

This skill snapshots **short interest** (how much of each name is sold short, how crowded the bet is) for every US-listed vault company into `raw/data/short-interest/`, then reports the signal. It's a fully-automated pull from the **FINRA Consolidated Short Interest API** (official, anonymous, all US exchanges) — no paste, no API key, no browser.

It exists because short interest is a useful **sentiment/positioning overlay** on the contested, higher-beta names (watch the *trend* in days-to-cover and rising short interest), and a red-flag prompt to go run `/bear-case`. It is **not** a timing tool — FINRA data is twice-monthly and ~1–2 weeks lagged.

## The hard boundary (discovery-only)

This skill writes EXACTLY one file: a CSV under `raw/data/short-interest/`. It MUST NOT, under any circumstances:
- edit any `wiki/` page (company / chokepoint / theme / tracker / relationship), `index.md`, or `log.md`,
- edit `wiki/_thesis*.md` or `raw/notes/frameworks*.md` (human-owned anchors) or `CLAUDE.md`,
- run git.

The CSV is **Tier-4 sentiment data** — positioning, not fact; never cited as canon. Same contract family as `youtube-intel` / `latest-alpha` / `bear-case`. The data does not count toward `index.md` / `log.md` accounting (like everything under `raw/`).

## When to invoke

- `/short-interest-snapshot` (optionally `/short-interest-snapshot 2026-05-29` for a specific settlement date).
- "snapshot the short interest", "pull short interest for the vault", "how shorted are our names", "refresh the short-interest data", "which names are most crowded short".

Not for: a buy/sell call (it describes positioning, never recommends), a primary-source ingest (the human-gated two-stop), or float / squeeze-score data (those need a browser or a paid key — out of scope; see What this skill is NOT).

## Steps

### 1 — Run the fetch script

From the vault root:

```bash
python scripts/fetch_short_interest.py            # latest settlement, all US-eligible vault names
python scripts/fetch_short_interest.py --date 2026-05-29   # a specific settlement date
python scripts/fetch_short_interest.py --dry-run  # fetch + summarize, write nothing (preview)
```

The script auto-detects the latest FINRA settlement date, pulls each US-eligible vault ticker (FINRA short interest + SEC shares-outstanding → `pct_outstanding`), writes `raw/data/short-interest/short-interest_<settlement-date>.csv` (idempotent — same date overwrites), and prints a summary. If the network fails, it says so and writes nothing — never invent numbers.

### 2 — Report to the user (chat)

Lead with the **settlement date** and **how many of the ~70 vault names were captured** (plus any FINRA didn't carry). Then surface the signal from the script's summary, framed as **positioning, not a timing call**:
- **Most-crowded** names (highest days-to-cover) — the names with the largest short relative to trading volume.
- **Biggest rising short interest** (change% vs the prior settlement) — where skepticism is *building*.

Keep it plain-language. If a name's reading looks notable, suggest `/bear-case <TICKER>` to find out *why* the shorts are there — don't interpret it as a sell. End by noting where it saved (`raw/data/short-interest/…`) and that this is Tier-4 sentiment data, not canon.

## Output template (chat)

```
## Short interest — FINRA settlement <date> (N/70 vault names)

**Most crowded (days-to-cover):** TICKER d.t.c, TICKER d.t.c, …
**Rising short interest (vs prior settlement):** TICKER +x%, TICKER +x%, …
(Any names FINRA didn't carry: …)

Saved: raw/data/short-interest/short-interest_<date>.csv
```

## Disciplines

- **Discovery-only** — one CSV under `raw/data/short-interest/`; never canon, anchors, the agenda, or git.
- **Tier-4 sentiment** — positioning data, never asserted as fact; a rising-short reading is a *question to investigate* (`/bear-case`), not a verdict.
- **The `%` is outstanding-basis, not float** — state it. True float isn't reliably free; a few names (multi-class like `GOOGL`, recent IPOs / `META`) show a blank `pct_outstanding` by design rather than a guessed number. The core FINRA fields (shares short, change, days-to-cover) are present for every name.
- **Describe-don't-recommend** — no buy/sell/trim. Reframe "should I sell because it's shorted?" → "what would have to be true for the shorts to be right" (that's `/bear-case`).
- **Honest about staleness** — twice-monthly, ~1–2 weeks lagged; a sentiment gauge, not an entry/exit timer.
- **Plain language** in the chat summary.

## What this skill is NOT

- Not a buy/sell or timing tool — it captures positioning; interpretation lives in `/bear-case` and the risk pages.
- Not a float or squeeze-score source — FINRA gives short interest + days-to-cover; true % of float and the trading-logic squeeze score need a headless browser or a paid key (deliberately out of scope; the `%` here is shares-outstanding-basis).
- Not a primary-source ingest, and not a way to write to canon — the CSV is Tier-4 discovery data, human-gated like every other `raw/` artifact.
- Not for foreign-exchange-only vault names (the China A-share / Japan / Europe cohort) — they have no FINRA short interest and never appear (see `raw/data/short-interest/README.md`).
