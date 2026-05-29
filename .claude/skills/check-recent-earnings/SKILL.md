---
name: check-recent-earnings
description: Scan all US-listed (SEC-registered) tickers in the stocks-wiki vault and return a ranked freshness report (recent earnings calls + upcoming filings + stale tickers) sorted by refresh-ingest priority. Use this skill whenever the user asks about recent earnings calls, vault freshness, upcoming 10-Q / 10-K / 20-F / 40-F filings, refresh-ready tickers, vault staleness, or which vault names just reported. Trigger on phrases like "check recent earnings", "what tickers had earnings calls recently", "vault freshness scan", "next filings available for ingest", "which tickers are due for refresh", "any new 10-Qs from our vault", or any operational question about SEC filing freshness across vault tickers. Don't skip this skill just because the user didn't say the word "freshness" — any question about recent earnings or filing dates across multiple vault tickers should trigger this skill rather than manual ticker-by-ticker lookup.
---

# Check recent earnings — stocks-wiki vault freshness scan

This skill returns a 5-section ranked freshness report covering all US-listed (SEC-registered) vault tickers, sorted by refresh-ingest priority. It exists because the vault has dozens of SEC-registered tickers across multiple filing types (10-K, 10-Q, 20-F, 40-F, 6-K), and manual ticker-by-ticker SEC EDGAR + earnings-calendar checking is tedious and error-prone. **Non-US-listed vault companies are intentionally out of scope — see Scope below.** The skill orchestrates a single command that surfaces five operationally useful signals: which tickers JUST reported earnings (refresh-ready), which tickers have CONFIRMED upcoming calls within the next 20 trading days (ingest queue with announced dates), which tickers will report SOON per cadence estimation (broader ingest queue), which tickers are STALE relative to vault refresh cadence (refresh candidates), and which NEW filings are available to download from SEC EDGAR but are not yet saved locally (an actionable download list). The skill itself downloads nothing — it lists what can be pulled and prints the command to pull it. When you do run the download command, new filings land in a `raw/filings/newly_fetched/` staging subfolder for review before you move them into `raw/filings/` post-ingest.

## Scope

This skill covers **US-listed, SEC-registered vault tickers only** — every ticker in the COMPANIES dict in `scripts/fetch_filings.py`. That set includes US-listed foreign-issuer ADRs that file with SEC EDGAR on 20-F or 40-F cadence (e.g., TSM, TSEM, NOK, ARM, CCJ) — these are in scope because they have a CIK and an EDGAR submissions endpoint.

**Non-US-listed vault companies are intentionally excluded.** Companies listed only on foreign exchanges (e.g., XFAB and SOI on Euronext Paris, SIVE on Nasdaq Stockholm) do not file with SEC EDGAR, have no CIK, and are not in the COMPANIES dict — so they never appear in this scan, by design. Track their filing freshness manually via each company's investor-relations page. Do not add non-US-listed tickers to the COMPANIES dict; there is no SEC submissions endpoint to query for them, so the scan cannot cover them.

## When to invoke

Invoke this skill when the user asks any operational question about vault filing freshness or refresh-ingest planning. The skill is the right tool whenever the question would otherwise require checking SEC EDGAR for each vault ticker individually.

Examples of questions that should trigger this skill:
- "Has anyone in our vault reported earnings recently?"
- "What tickers are coming up for 10-Q refresh?"
- "Which vault names should I refresh next?"
- "Vault freshness scan"
- "Did TSM file the 20-F yet?"
- "Any new earnings calls I should ingest?"
- "Check recent earnings"
- "Next 10-K available for ingest"

## Workflow

Execute these steps in order:

### 1. Verify vault state

Read the COMPANIES dict in `scripts/fetch_filings.py` to enumerate vault tickers. The COMPANIES dict is the canonical source of which tickers are in the vault — when new tickers are added there, they automatically participate in this skill's scan. Confirm the file exists and the dict is parseable; if not, surface the error and stop.

### 2. Run the freshness query workhorse script

Execute via Bash:

```bash
python scripts/fetch_filings.py --freshness
```

This script (the workhorse for this skill) queries SEC EDGAR `/submissions/CIK*.json` for each ticker in the COMPANIES dict, queries the Nasdaq earnings calendar across a 20-trading-day window for confirmed upcoming calls, computes recent + confirmed-upcoming + cadence-estimated + stale signals, cross-checks each ticker's latest SEC filing against the local `raw/filings/` archive AND its `newly_fetched/` staging subfolder to flag not-yet-downloaded filings, and emits a 5-section markdown report to stdout. The cross-check is read-only — freshness mode never downloads anything.

**Two-source architecture.**
- SEC EDGAR (canonical) — Sections 1, 3, 4 (past filings, cadence-estimated filings, vault staleness)
- Nasdaq earnings calendar (announcements-aggregator) — Section 2 (confirmed upcoming calls). Iterates ~20 weekday dates over the trading-day window, filters to vault tickers. Graceful degradation: if Nasdaq returns nothing or fails, Section 2 reports zero tickers; the rest of the scan is unaffected. Source tier is distinct from SEC EDGAR — the section is explicitly labeled "(source: Nasdaq)".

The script branches on the `forms` dict per ticker to handle filing-type variation:
- US-domiciled (`forms: ["10-K", "10-Q"]`) — query most recent 10-K + 10-Q + 8-K. The **earnings call date** is sourced from the most recent 8-K with Item 2.02 (Results of Operations and Financial Condition) — the SEC-canonical earnings-release item. The 8-K's `reportDate` is the event date (when earnings were released and the call held), which differs from the 10-Q filing date that can lag by weeks.
- SEC-registered foreign issuer with 20-F annual cadence (`forms: ["20-F"]`; e.g., TSM) — earnings call date sourced from most recent 6-K `reportDate`.
- MJDS Canadian (`forms: ["40-F", "6-K"]`; e.g., CCJ) — earnings call date sourced from most recent 6-K `reportDate`.
- Non-US-listed / non-SEC-registered foreign issuer — **out of scope** (see Scope). Not added to the COMPANIES dict and never queried; there is no SEC submissions endpoint for these. Track manually via the company IR page.

**Non-earnings 8-K filtering.** Companies file 8-Ks for many material events beyond earnings (proxy/governance, executive changes, M&A, etc.). The Item 2.02 filter ensures only earnings 8-Ks contribute to the call-date signal — non-earnings 8-Ks within the 30-day window do NOT cause the ticker to appear in Recent earnings. This is intentional: a ticker shouldn't show "Recent earnings" activity for non-earnings filings.

**Fallback for periodic-only filers.** When no 8-K Item 2.02 (US) or 6-K (foreign) is found within the 30-day window but a 10-Q/10-K/20-F/40-F was filed in that window, the formal filing date is shown with an asterisk annotation clarifying that the call occurred earlier. This handles the rare small-cap case of earnings reported via 10-Q without an accompanying earnings 8-K.

If the script doesn't exist or doesn't have `--freshness` mode yet, the workhorse needs to be built — surface that as a prerequisite gap and stop.

### 3. Cross-reference vault staleness

The script already cross-references `index.md` `last_updated` column for vault staleness comparison. Confirm the script output includes the staleness section. If staleness data is missing, fall back to filing-date-only output and flag staleness as a known gap.

### 4. Format output per template

The script output should already match the template below. If formatting deviates, normalize before returning to user. Apply count caps and "and N more" footers as needed.

## Output template

Always use this exact 5-section structure:

```
## Vault freshness scan ({YYYY-MM-DD})

**Recent earnings (last 30 days):** {N} tickers
- TICKER1 (call {YYYY-MM-DD}) / TICKER2 (call {YYYY-MM-DD}) / ...
[show top 6 by call date descending; if N > 6, append "and {N-6} more"]
[fallback annotation: TICKER ({form} filed {YYYY-MM-DD}*) — applied when no 8-K Item 2.02 / 6-K within window; asterisk footer line "* = no 8-K Item 2.02 within window; formal filing date shown" appended when any fallback row present]

**Confirmed upcoming earnings calls (next 20 trading days):** {N} tickers (source: Nasdaq)
- TICKER1 ({YYYY-MM-DD} after-hours) / TICKER2 ({YYYY-MM-DD} pre-market) / TICKER3 ({YYYY-MM-DD}) / ...
[show top 9 by call date ascending; if N > 9, append "and {N-9} more"]
[time-of-day annotation: "after-hours" / "pre-market" / omitted when Nasdaq reports time-not-supplied]

**Upcoming quarterly filings (next 30 days):** {N} tickers expected
- TICKER1 est. ({YYYY-MM-DD}) / TICKER2 est. ({YYYY-MM-DD}) / ...
[show top 9 by estimated date ascending; if N > 9, append "and {N-9} more"]

**Stale tickers (no refresh in 90+ days):** {N} tickers
- TICKER1 (last refresh {YYYY-MM-DD}; {N} days) / ...
[show top 3 by staleness descending; if N > 3, append "and {N-3} more"]

**New filings available to download (not yet in raw/filings/):** {N} filings
- TICKER1 10-Q (filed {YYYY-MM-DD}) → `TICKER1-10Q-{REPORTDATE}.htm`
- TICKER2 10-K (filed {YYYY-MM-DD}) → `TICKER2-10K-{REPORTDATE}.htm`
[one bullet per filing; show top 12 by filing date descending; if N > 12, append "and {N-12} more"]
  Fetch all: `python scripts/fetch_filings.py`
  Fetch one: `python scripts/fetch_filings.py --ticker TICKER --form FORM`
  (files stage in raw/filings/newly_fetched/ — move to raw/filings/ after ingest)
[empty case: "- (local filings dir already current with the latest filings)"]
```

**Recent earnings date semantics.** The date shown in Section 1 is the **earnings call / release date** (8-K Item 2.02 `reportDate` for US filers; 6-K `reportDate` for foreign issuers) — NOT the 10-Q/10-K formal filing date. This is the date the earnings press release was issued and the conference call held, which is what matters for refresh-ingest timing (transcript availability, primary-source readiness). The 10-Q formal filing can lag by weeks; the "call" date is the operationally useful signal.

**Confirmed upcoming calls vs cadence-estimated filings.** Section 2 (Nasdaq) shows **confirmed** call dates within the next 20 trading days — companies have publicly announced these via press release / IR page, and Nasdaq aggregates. Section 3 (cadence-estimated) shows **estimated** formal-filing dates (10-Q / 10-K / 20-F / 40-F) derived from prior-period cadence; these are heuristics, not announcements, and intentionally extend beyond Section 2's window. A ticker may appear in both with different dates — Section 2 = the call; Section 3 = the formal SEC filing that follows. Operationally, Section 2 tells you when the transcript becomes available; Section 3 tells you when the 10-Q is expected.

**New filings available to download (Section 5).** Lists the latest filing of each tracked form (per the ticker's `forms` in the COMPANIES dict — 10-K/10-Q for US filers; 20-F/40-F/6-K for SEC-registered foreign issuers) that exists on SEC EDGAR but is **not yet saved locally** — absent from BOTH the base archive dir (`raw/filings/`) AND its `newly_fetched/` staging subfolder. The presence check mirrors the default download mode's skip-if-present logic across both directories, so the list is an exact preview of what `python scripts/fetch_filings.py` (without `--freshness`) would fetch. A filing already sitting in staging (fetched but not yet ingested) is therefore NOT re-listed. Each row shows the target filename in the vault naming convention (`TICKER-FORM-REPORTDATE.htm`, e.g. `NVDA-10K-2026-01-26.htm`, where the date is the SEC `reportDate` / period-end). **The skill lists only; it never downloads** — run the printed `Fetch all` / `Fetch one` command to actually retrieve files, which download into the `raw/filings/newly_fetched/` staging area (a quarantine to review before you move them into `raw/filings/` post-ingest). Note these are SEC primary documents saved as `.htm` (not `.pdf`), and earnings-call transcripts are not on EDGAR, so they never appear in this list. Distinct from Section 1 (Recent earnings = *which tickers reported*) and Section 3 (estimated *future* filings): Section 5 is *files that exist now and are missing locally*.

**20 trading days window.** Computed by stepping forward weekdays only from the scan date; US market holidays are NOT excluded (approximation). For a scan run on a Tuesday, 20 trading days ≈ 4 calendar weeks. A holiday-induced 1-day overshoot returns at most a couple of boundary rows that downstream date filtering handles.

**Why these specific count caps:** 6 / 9 / 3 / 12 reflect Vic-curated operational display sizing — recent earnings and upcoming filings are the highest-value signals (more rows worth surfacing); stale tickers are tail-risk signals (3 rows sufficient to flag attention without overwhelming); the new-filings download list caps at 12 (it is the actionable pull list, so it surfaces more rows) with a single `Fetch all` command covering anything beyond the cap. The caps are display-only; the underlying scan covers all in-scope (US-listed, SEC-registered) vault tickers.

**Why these sections:** Recent earnings = "ready to ingest now" (refresh ingest can proceed immediately with primary sources available); confirmed upcoming calls + upcoming filings = "ingest queue" (refresh ingest sequencing for next 1-4 weeks); stale tickers = "refresh candidates" (operational hygiene check; tickers drifting out of vault canonical recency); new filings available to download = "actionable pull list" (the latest SEC filings not yet saved locally, with the exact `fetch_filings.py` command to retrieve them).

## Output discipline

- Concise output. Do not append explanatory paragraphs after the 5-section template unless the user explicitly asks for elaboration. The skill exists for fast operational scanning, not analytical commentary.
- Date format `YYYY-MM-DD` consistently.
- Apply descriptive language convention per `CLAUDE.md` preamble — say "10-Q" or "quarterly filing", not numerical shorthand without context.
- Foreign-issuer tickers (TSM, CCJ) appear in the same scan with their own filing-type cadence; do not exclude them.
- If the script returns zero tickers in any section, state explicitly (e.g., "Recent earnings (last 30 days): 0 tickers — none in vault reported in past 30 days").

## Source-of-truth discipline

This skill maintains zero static state. SEC EDGAR is the canonical source for past filing dates; estimated next filings are derived from filing cadence (large accelerated filer windows: 10-Q within 40 days of quarter end; 10-K within 60 days of fiscal year end; 20-F within 4 months of fiscal year end). When new **US-listed (SEC-registered)** tickers are added to `scripts/fetch_filings.py` COMPANIES dict, they automatically appear in the next scan. No manual ticker list maintenance. Non-US-listed names are out of scope per Scope and are never added to the dict.

This is intentionally distinct from `index.md` (which is canonical for vault page catalog state) and `log.md` (canonical for session-by-session activity). The skill produces a derived view; canonical sources remain authoritative.

## Maintenance

This skill is invocation-only. The SKILL.md does not require updates when new tickers are added — the COMPANIES dict in `scripts/fetch_filings.py` carries that change.

The SKILL.md does require updates if:
- New filing-type categories emerge (e.g., non-SEC-registered foreign issuer ingest sub-protocol codified per CLAUDE.md Section 4.2 future extension)
- Output format conventions change at chat-side or via codification session
- Workhorse script location changes from `scripts/fetch_filings.py`

The workhorse script (`scripts/fetch_filings.py --freshness` mode) is where filing-cadence logic, staleness thresholds, and section sorting live. Updates to those operational parameters happen in the script, not in SKILL.md.
