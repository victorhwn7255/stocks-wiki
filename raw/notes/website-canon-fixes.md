# Website-build canon punch-list

*Discovery note — NOT canon, not in `index.md`/`log.md`. A consolidated checklist of **content nits in the Markdown** surfaced while building + auditing the static website (companies · themes · thesis/frameworks · relationships · chokepoints). The website renders the Markdown **faithfully** — every item below is a defect in the *source* `.md`, so the fix belongs in canon (your domain), not in the build. Generated 2026-06-22 from 5 audit runs.*

## What this is / isn't
- **Render-faithful, not render-bugs.** The HTML shows exactly what the Markdown says; these are source typos / factual slips / malformed markup.
- **Already-fixed systematic issues are NOT here.** The audits also found render bugs with a *single* root cause (tight lists leaking dashes, abutting tables, 2-space-bullet flattening, subtitle wikilinks/bold, TOC `&` double-escape, the `ON`→`TRUE` ticker, wikilinks-in-code). Those were fixed **centrally in `web/build.py`** and are excluded from this list.
- **Human-owned files:** `raw/notes/frameworks*.md` is human-owned — the `frameworks` item below is flag-only, change at your discretion.
- Line numbers are the **source `.md`** lines. None of these block the site; fix when convenient.

---

## Tier A — visible errors / factual (worth fixing first)

| Page (`.md`) | Line | Issue | Suggested fix |
|---|---|---|---|
| `wiki/chokepoints/advanced-optical-packaging.md` | 59 / 66 | **Factual:** analysis paragraph says the 27.6% top customer is **"Microsoft"**, but the page's own data line (and the 10-K) say it's **NVIDIA** | `Microsoft 27.6%` → `NVIDIA 27.6%` |
| `wiki/companies/FN.md` | 49–61 | FY2025 snapshot table cites **"GLW 10-K FY2025"** (Corning) as the source of Fabrinet's own data | `GLW 10-K` → `FN 10-K` |
| `wiki/chokepoints/liquid-cooling.md` | 140 | **Broken link:** `**[[VRT] (Liebert):**` has one closing bracket → leaks literal `[[VRT]` (siblings FLEX/ETN/NVT/ANET resolve) | add the missing `]` → `[[VRT]]` |
| `wiki/themes/hyperscaler-custom-ASIC.md` | 218–219 | Change-log entry **split mid-sentence** — the S163 entry was pasted into the middle of the S119 entry (`…hyperscaler buildin` + `…theme.g no captive accelerator…`) | re-join the S119 sentence; separate the S163 tail |
| `wiki/companies/MOD.md` | 251–264 | Open-Questions list authored `1,2,12,13,14,3,4…11` → renders `1-14`, **breaking the page's own "Open Q#N" cross-references** | renumber sequentially + fix the in-body `#N` refs |
| `wiki/companies/VECO.md` | 165 / 173 | **Duplicate `## Customer concentration` section** (the 2nd a stale copy) → duplicate H2 `id` + duplicate TOC entry | delete the duplicate section |
| `wiki/companies/GLW.md` | 86 | Editing artifact in a table cell: `9M capex (Q1) — wait Q1 only:` | clean up the label |
| `wiki/companies/NVT.md` | 154 | Unfilled placeholder `$35.x M` renders as visible text | fill the decimal digit |

## Tier B — leaked markdown markup (literal `**` / inverted italics)

| Page (`.md`) | Line | Issue | Suggested fix |
|---|---|---|---|
| `wiki/companies/IBIDEN.md` | 12 | Subtitle has an **unclosed `**`** (`**Labeling note (load-bearing):…` never closed) → leaks literal `**`, loses the bold + line italic | close the bold (`**…**`) / balance the wrapper |
| `wiki/companies/MRVL.md` | 38 | Footnote `**GAAP net income inflated by $1.8B…` opens bold, never closed → leaks literal `**` | close the `**` |
| `wiki/companies/AVGO.md` | 41 | Footnote `**FY2024 depressed by $3,748M…` opens bold, never closed → leaks literal `**` | close the `**` |
| `wiki/chokepoints/BTM-grid-bypass-workaround.md` | 16 / 98 | Nested same-delimiter emphasis — `*word*` inside an outer `*"…"*` italic quote inverts (markdown closes the outer `<em>` at the inner `*`) | change the inner `*…*` to `**bold**` or `_underscore_` |

## Tier C — cosmetic content nits (fix when convenient)

| Page (`.md`) | Line | Issue | Suggested fix |
|---|---|---|---|
| `wiki/companies/ETN.md` | 126–129 | FY2025 segment backlogs **sum to ~$29.4B vs the stated $19.6B total** (~$10B gap — verify which is right) | reconcile the figures |
| `wiki/companies/NVDA.md` | 131 | FY2027 tax-rate `7-19%` — likely a dropped digit (page later says `17-19%`) | `7-19%` → `17-19%` |
| `wiki/companies/PLAB.md` | 140 | Stray `VIAV` in `Per VIAV PLAB 10-K FY2025…` (copy-paste from the paired VIAV ingest) | drop `VIAV` |
| `wiki/companies/PLAB.md` | 40–48 | FY2025 annual-results table mixes Q4 quarterly rows under annual (FY2025/FY2024/FY2023) column headers | re-label columns or move the Q4 rows |
| `wiki/companies/VRT.md` | 281 | "Five acquisitions" prose vs a four-row acquisitions table (STL omitted) | reconcile count/table |
| `wiki/companies/AAOI.md` | 49 / 107 | FY2025 accumulated deficit `$491.0M` vs `$490.1M` across two tables (~$0.9M) | align the figure |
| `wiki/companies/COHR.md` | 92 / 105 | Stale Dec-31-2025 balance-sheet block sits *below* the newer Q3 FY2026 table | remove/date the stale block |
| `wiki/companies/OUST.md` | 21 / 46 | Unlabeled cash figure in the intro reads as conflicting with the FY2025 table (different dates) | date the intro figure |
| `wiki/companies/LEU.md` | 26 | CFO surname `Tonelli` (5×) vs `Tinelli` (3×) | pick one spelling |
| `wiki/companies/LITE.md` | frontmatter | `last_updated: 2026-05-10` lags the newest change-log entry (2026-05-15) | bump `last_updated` |
| `wiki/chokepoints/cpo-integration.md` | 396–414 | Open-questions list duplicate authored numbering (`1-8,7,8,9-14`) + in-body refs cite authored numbers | renumber + fix refs |
| `raw/notes/frameworks.md` *(human-owned)* | 1281 / 1283 | Duplicate `12.` list number (the 2nd should be `13.`) | flag-only — renumber at your discretion |
| `wiki/chokepoints/chokepoint-investability-priorities.md` | 3 | `ALAB` + `COHU` in frontmatter `tickers` but never discussed in the prose | add coverage or trim the tickers |
| `wiki/chokepoints/HALEU-fuel-chokepoint.md` | 68 | Stray `$` in `(+$~40-50× current capacity)` makes a multiplier read as a dollar amount | drop the `$` |

---

## Recurring habits (root patterns, for future awareness)
1. **Hand-numbered lists that drift** (MOD, cpo-integration, frameworks) — markdown auto-renumbers, so the rendered page looks fine but internal `#N` cross-references break. Safest to let markdown number and reference items by name, not number.
2. **Unbalanced/malformed emphasis** (IBIDEN, MRVL, AVGO unclosed `**`; BTM nested italics; liquid-cooling `[[VRT]`) — a stray/missing `*`/`]` leaks literal markup.
3. **Copy-paste artifacts from paired ingests** (FN cites GLW, PLAB says VIAV) — leftover wrong-ticker references.

*Tier A ≈ 8 items, Tier B ≈ 4, Tier C ≈ 14 → ~26 total, each a 1-line edit. The build renders all of them faithfully today; this list is purely for tidying the source.*
