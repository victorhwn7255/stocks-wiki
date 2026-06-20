---
name: short-interest-intel
description: Refresh the short-interest tracker (wiki/trackers/short-interest.md + its .html) from the latest FINRA snapshot. Pulls new data via /short-interest-snapshot's fetcher, regenerates ONLY the fenced data tables, appends a dated change-log entry (the trend history is never overwritten), bumps the date, and regenerates the HTML — leaving the frame, the confirm/challenge intel prose, the watch-list, and the reviewed "Vault read" stances untouched. Cadence-aware (short interest is twice-monthly, so it no-ops on a settlement already on the page). Use on /short-interest-intel, "refresh the short-interest tracker", "update the short-interest intel", or after a new FINRA settlement lands.
---

# short-interest-intel — refresh the short-interest tracker from new data

This skill closes the short-interest loop: it pulls the latest FINRA snapshot and **refreshes the tracker in place, keeping the same format** — without losing the trend history or the reviewed judgment. It is the analysis layer on top of `/short-interest-snapshot` (which only collects raw data). Built on the `/spread-watch` pattern: a deterministic script does the mechanical refresh; the skill wraps it and narrates.

## The hard boundary (read first)

This skill edits **exactly one canon page** and one derived file, in a bounded way:
- `wiki/trackers/short-interest.md` — **only** the fenced data block (`<!-- SHORT-INTEREST-DATA:START … END -->`), **plus** one appended `## Change log` bullet, **plus** the frontmatter `last_updated`.
- `wiki/trackers/short-interest.html` — regenerated.

It MUST NOT, under any circumstances:
- edit anything in `short-interest.md` **outside** the fenced block — the frame, the `## Intel` confirm/challenge prose, the `## Watch-list` (that is the human-curated judgment layer, **carried forward**),
- edit any **other** `wiki/` page, `wiki/_thesis*.md`, `raw/notes/frameworks*.md`, `CLAUDE.md`, `index.md`, or `log.md`,
- run git, or cascade to any other page (flag, don't edit).

The data is **Tier-4 sentiment** (positioning, not fact). The "Vault read" stance map is **carried forward** — proposed changes go to chat for review, never auto-written. Describe-don't-recommend throughout.

## When to invoke

- `/short-interest-intel` (optionally `/short-interest-intel 2026-06-13` for a specific settlement).
- "refresh the short-interest tracker", "update the short-interest intel", "pull the new short interest and update the page", or after a new FINRA settlement lands (twice-monthly).

Not for: building the tracker from scratch (done), a buy/sell call, or a primary-source ingest.

## Steps

### 1 — Pull the latest data

```bash
python scripts/fetch_short_interest.py            # refresh the CSV (auto-detects latest settlement)
```

### 2 — Refresh the tracker (bounded, cadence-aware)

```bash
python scripts/short_interest_intel.py --update-tracker
```

This reads the latest CSV, compares its settlement to the one on the page, and:
- **same settlement** → prints "no new settlement … nothing to update" and **changes nothing** (no churn). Stop here and report that.
- **new settlement** → replaces the fenced data tables, appends a dated change-log bullet, bumps `last_updated`, regenerates the HTML, and prints a **review list** (judgment that may need a human look — e.g. a new CHALLENGE name in the tables with no Intel-prose entry; a prose name that dropped below threshold).

Use `--dry-run` to preview a unified diff without writing.

### 3 — Report to the user (chat)

- **No new settlement:** say so plainly ("the latest FINRA settlement is still <date>, already on the tracker — nothing to refresh") and stop.
- **Refreshed:** lead with the settlement date and **what moved** (from the script's output — biggest risers/fallers, new entrants to the tables, the standouts), framed as **positioning, not a timing call**. Then surface the script's **review list as proposals** — "these may need a judgment update; want me to draft them?" — but **do not** edit the Intel prose yourself. Note that the HTML was regenerated and where both files live. Plain language.

## Output template (chat, refreshed case)

```
## Short-interest tracker refreshed — FINRA settlement <date>

**What moved:** rising — TICKER +x% …; covering — TICKER −x% …; new to the tables — TICKER …
**Standouts:** <the most-shorted / most-crowded / biggest riser>

Updated: wiki/trackers/short-interest.md (data block + change log) + short-interest.html

For your review (judgment layer — not auto-edited):
- <the script's review flags, as proposals>
```

## Disciplines

- **Bounded canon write** — only the fenced data block + one change-log line + frontmatter date + the HTML. The judgment prose and the "Vault read" stances are **carried forward**, never auto-overwritten.
- **Trend history is sacred** — the change log is **appended**, never rewritten. The diff between settlements is the signal.
- **Cadence-aware** — no churn when the settlement hasn't changed.
- **Tier-4 / describe-don't-recommend** — a heavy or rising short is a *question to investigate* (`/bear-case`), never a verdict or a trade signal.
- **Propose, don't cascade** — review flags and any cross-page implications (e.g. a `[[forward-edge-tracker]]` refinement) are surfaced in chat, not edited.
- **Plain language** in the chat summary.

## What this skill is NOT

- Not a way to rewrite the whole tracker — it refreshes the data and *proposes* judgment updates; the confirm/challenge intel stays human-curated.
- Not a buy/sell or timing tool, not a float / squeeze-score source (the `%` is shares-outstanding basis), and not a primary-source ingest.
- Not a license to edit `index.md` / `log.md` or any other page — it flags, it does not cascade. (Vic handles git.)
