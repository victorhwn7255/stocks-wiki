# Short-interest data store

Raw, non-canon snapshots of US short-interest data. One CSV per FINRA settlement
date. This folder is a **Tier-4 sentiment data feed** (positioning, not fact) —
discovery material, never cited as canon. Like everything under `raw/`, nothing
here counts toward `index.md` / `log.md` accounting.

## Source

- **FINRA Consolidated Short Interest API** — official, anonymous, covers all US
  exchanges + OTC. Published **twice a month** (mid-month + month-end settlement)
  with a ~1–2 week reporting lag. The data is always somewhat stale — fine as a
  sentiment/positioning gauge, **not** an entry/exit timing tool.
- **SEC** `EntityCommonStockSharesOutstanding` (dei, us-gaap fallback) — the
  denominator for the `%` field. We use shares **outstanding**, not float: true
  public float isn't reliably available from a free, automatable source (Yahoo
  blocks bots). So `pct_outstanding` runs *lower* than the float % traders quote.

The honest "what it's good for" verdict: a sentiment overlay for the contested /
higher-beta names (watch the *trend* in days-to-cover + rising short interest),
mostly noise on the low-short mega-caps. Not a timing signal.

The skill that produces these files is **`/short-interest-snapshot`** →
`scripts/fetch_short_interest.py` (fully automated; no paste, no API key).

## Coverage of the vault (verified 2026-06-19)

FINRA is US-market only, so of the vault's company pages:

- **Coverable (US-listed):** the US-domestic names + 6 US-listed ADRs
  (`ARM`, `CCJ`, `NBIS`, `NOK`, `TSEM`, `TSM`) — **70 names**, all returned data
  in the 2026-05-29 snapshot.
- **Not coverable (foreign-exchange-only — never appear here):**
  `HARMONIC`, `IBIDEN`, `MURATA` (Japan); `HENGLI`, `TUOPU`, `SANHUA`,
  `SHUANGHUAN`, `ZHAOWEI`, `ZHONGDA`, `SLING` (China A-share / HK);
  `SIVE` (Nasdaq Stockholm); `SOI`, `XFAB` (Euronext Paris).

The script recomputes this split itself from each page's `foreign_issuer`
frontmatter + the ADR allowlist (`vault_companies()` in `parse_short_interest.py`),
so new vault pages are classified automatically (only a *new* foreign ADR needs
adding to `ADR_ALLOWLIST`).

## File naming

```
raw/data/short-interest/short-interest_<YYYY-MM-DD>.csv
```

`<YYYY-MM-DD>` = the **FINRA settlement date** of the snapshot (auto-detected, not
the day you ran it). ISO format so files sort chronologically. The twice-monthly
cadence means you accumulate a time series — the *diff* between two dates is the
signal (skepticism building vs fading).

## Column schema

Every snapshot CSV has exactly these columns, in this order:

| column              | meaning                                                          |
|---------------------|------------------------------------------------------------------|
| `settlement_date`   | FINRA settlement date (same as the filename) — self-describing    |
| `ticker`            | US ticker, uppercased                                            |
| `company`           | issuer name as FINRA reports it                                  |
| `market_class`      | FINRA market-class code (NNM = Nasdaq, NYSE, SC = small-cap, …)  |
| `shares_short`      | current short position (shares)                                 |
| `prev_shares_short` | short position at the prior settlement                          |
| `change_shares`     | change vs prior (shares) — the "rising short interest" signal    |
| `change_pct`        | change vs prior (%)                                             |
| `pct_outstanding`   | short interest as % of shares **outstanding** (≈ float, lower)   |
| `shares_outstanding`| SEC shares outstanding used as the % denominator                |
| `avg_daily_volume`  | FINRA average daily share volume                                |
| `days_to_cover`     | days-to-cover ratio (short interest ÷ avg daily volume)         |
| `in_vault`          | `true` if the ticker has a `wiki/companies/` page (always true)  |

Notes:
- **`pct_outstanding` is outstanding-basis, not float** — and it's *approximate*
  for a few names: multi-class issuers pair an all-class share count against
  FINRA's single-class short interest (e.g. `GOOGL`), and a handful tag shares in
  a way neither SEC concept exposes (e.g. `META`, recent IPOs) → the field is left
  **blank** rather than guessed. The core FINRA fields are present for every name.
- Values are stored largely **verbatim** as FINRA/SEC return them (raw store —
  fidelity over convenience). Clean on read (`pandas`) when you analyze.

## Adding a snapshot

Just run the skill (`/short-interest-snapshot`) or the script directly:

```bash
python scripts/fetch_short_interest.py              # latest settlement, all vault names
python scripts/fetch_short_interest.py --date 2026-05-29
python scripts/fetch_short_interest.py --dry-run    # fetch + summarize, write nothing
```

It auto-detects the latest FINRA settlement date, pulls each US-eligible vault
name (FINRA short interest + SEC shares-outstanding → `pct_outstanding`), writes
`short-interest_<date>.csv` here (idempotent — same date overwrites), and prints a
summary (most-crowded by days-to-cover, biggest rising short interest, any names
FINRA didn't carry).

> **Deprecated:** `scripts/parse_short_interest.py` was an earlier manual importer
> for a trading-logic.com paste/export (which carried squeeze score + % float).
> That site can't be fetched without a headless browser, so it's superseded by the
> FINRA-based `fetch_short_interest.py`. The old parser still works for a manual
> paste if you ever want the squeeze-score extras, but it writes a *different*
> (trading-logic) schema — don't mix the two in this folder.

## Git

These snapshots match the existing `.gitignore` pattern for bulk re-fetchable raw
(`raw/filings/`, `raw/news/`, `raw/transcripts/`). They're small text, and FINRA
only ever shows the *current* snapshot via this path, so committing them is how
you keep the history you can't re-fetch later. Whether to commit is a git decision
(Vic handles git) — this README + the schema are the durable convention either way.
