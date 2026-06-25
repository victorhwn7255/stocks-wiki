---
name: forward-pe-watch
description: Update the S&P 500 Forward P/E Watch tracker — fetch the current index level (FRED SP500, automatic), take the LSEG operating EPS estimates (CY2026 / CY2027 / NTM) from pasted args or a Vic-staged weekly PDF, compute the forward P/E for each horizon, decompose every move into a price effect vs an earnings-revision effect, and read the revision momentum. Maintains ONE page (wiki/trackers/forward-pe-watch.md) + its index.md row; never cascades, never recommends, never sets price targets. Use when Vic invokes /forward-pe-watch, pastes the weekly LSEG EPS numbers, stages an LSEG/FactSet earnings-dashboard PDF, or asks to "update the P/E watch / check the forward P/E."
---

# forward-pe-watch — the S&P 500 forward-P/E valuation dial

This skill tracks the S&P 500 **forward P/E on 2026 and 2027 estimated EPS** (plus the NTM/F4Q figure) over time. It runs a simple deterministic pipeline — **extract the LSEG report → append the CSV (the single source of truth) → derive 5 insights from the series → report** — and keeps **one** vault page current as the human-readable mirror: `wiki/trackers/forward-pe-watch.md`. The 5 insights are: **(1) decomposition** (is the multiple cheaper because earnings rose or price fell?), **(2) revision momentum + accel/decel**, **(3) forward-vs-trailing spread** (how much growth is priced), **(4) the horizon spread** (CY2026 / NTM-F4Q / CY2027), and **(5) what-it-means + vault cross-check**. It is the macro-valuation companion to `/spread-watch` (the financing dial) — same shape, different instrument. (This is a deliberately single-context, scripted skill — no multi-agent orchestration; the reliability comes from the helper script doing the arithmetic and the CSV being ground truth.)

## The hard boundary (read first — this is the whole point)

The skill writes **exactly three things**: (1) the vault page `wiki/trackers/forward-pe-watch.md` (readings table + latest-read block + change log + frontmatter `last_updated`), (2) that page's row date in `index.md`, and (3) **a new appended row in the raw-data file `raw/data/forward-earnings/forward-earnings-raw-data.csv`** (the machine-readable series; append-only, never overwrite prior rows). It MUST NOT edit any other wiki page (theme, chokepoint, company, the other trackers, `_thesis*`, `frameworks*`), and MUST NOT touch `log.md`, `refresh_log.md`, or `conventions-ledger.md`. **If a reading implies another page should change, FLAG it in chat for a follow-up — do not cascade.**

Disciplines (binding):
- **Describe-don't-recommend.** Valuation dials only — **never buy/sell, never a price target.**
- **One source across the series.** Default **LSEG / I-B-E-S operating EPS**. **Never mix LSEG and FactSet within the series** (the ~3–5% methodology gap reads as a fake move). FactSet is an occasional cross-check, mentioned in chat, never a row.
- **Never invent EPS.** If the weekly number isn't in hand and the last row is stale, flag it — don't guess.
- **Every row carries its source + as-of date.**

## When to invoke
- `/forward-pe-watch`, or "update the P/E watch," "check the forward P/E," "the forward multiple," "did the P/E move."
- Optional args: pasted EPS — `/forward-pe-watch 2026 340.82 2027 399.25` (and optionally `ntm 369`).
- A Vic-staged **LSEG/FactSet weekly earnings-dashboard PDF** (or screenshot) in `raw/data/forward-earnings/LSEG_reports/` (read it with the Read tool — PDF- and image-native).
- It's low-frequency by nature: the underlying number moves **weekly**, so a run a week (or when a slide/PDF lands) is the natural cadence.

## How a run works — 3 steps (extract → CSV → derive-5 → report)

The CSV `raw/data/forward-earnings/forward-earnings-raw-data.csv` is the **single source of truth**: the report is read **once** to populate it, and every insight is computed from the **series in the CSV** — not re-derived from memory or a single prior reading. The tracker page is the human-readable mirror of that series.

### Step 1 — Read the report → update the CSV (the ground truth)
1. **Anchor.** Read `wiki/trackers/forward-pe-watch.md` (page `last_updated`) **and the existing CSV** — the prior rows ARE the series the Step-2 decomposition + momentum run against.
2. **Get this week's numbers**, in order of preference:
   - **Staged report** (the norm): the LSEG **S&P 500 Earnings Scorecard** PDF/screenshot in `raw/data/forward-earnings/LSEG_reports/` (`LSEG-YYYY-MM-DD.pdf`). `Read` it and pull from **Exhibit 24** (per-share **CY2025–CY2028 EPS** + quarterly) and **Exhibit 23** (the **S&P close** + LSEG's stated **Forward P/E + Trailing P/E** + the **forward-4-quarter (F4Q) EPS** — use F4Q as NTM directly). F4Q includes the in-progress quarter, so its forward P/E (e.g. 21.0×) sits above a CY2027 P/E (e.g. 18.6×) — same data, different horizon; capture both.
   - **Pasted args** — `/forward-pe-watch 2026 <e26> 2027 <e27>` (NTM/close optional).
   - **Neither + last CSV row >10 days old** → do NOT guess. Flag "stale — needs the weekly LSEG number," point to the [LSEG dashboard](https://lipperalpha.refinitiv.com/category/sp-500/this-week-in-earnings/) (or FactSet's Friday PDF), and stop.
   - **Never invent a missing field.** LSEG is the default source; FactSet is a cross-check only — never mixed into the series.
3. **Append the CSV row** — the data of record, **append-only, date-sorted, never overwrite**. Columns (exact order): `report_date, index, close_date, index_close, trailing_eps_t4q, trailing_pe, forward_eps_f4q, forward_pe, eps_2025, eps_2026, eps_2027, eps_2028, pe_2026_calc, pe_2027_calc, eps_2026_q1, eps_2026_q2, eps_2026_q3, eps_2026_q4, eps_2027_q1, eps_2027_q2, eps_2027_q3, eps_2027_q4, source_file`. (`pe_*_calc` = the **report's own close** ÷ that year's EPS; `source_file` = the `LSEG_reports/…pdf` path. Blank, never invented, for any missing field.)
4. **Append the tracker readings-table row** (same raw data — the human mirror): date, level, 2026/2027/NTM EPS, the three P/Es, source/as-of. Keep older rows (compress the oldest into a one-line "earlier rows" note past ~15).

### Step 2 — Derive the 5 insights from the CSV (the analysis)
Compute all five **from the CSV series** — the helper does the arithmetic and fetches the live level:
```bash
python3 .claude/skills/forward-pe-watch/scripts/forward_pe_watch.py --eps2026 <E26> --eps2027 <E27> \
    [--epsntm <F4Q>] --prior-level <prev_close> --prior-eps2026 <prev_E26> --prior-eps2027 <prev_E27>
```
**Guard — close consistency:** the **decomposition + momentum run CSV-row-to-CSV-row** (report closes vs report closes — apples to apples). The script's **live FRED `SP500` level is a *supplementary* "where the dials sit today" line only**, never mixed into the historical math (a 5-day drift between the report close and "now" would otherwise contaminate the decomposition).

1. **Decomposition** — for each horizon, **ΔP/E = price effect + earnings effect** vs the prior CSV row. Compressing on a *negative earnings effect* (rising EPS) = "cheaper for the right reason"; on a *negative price effect* (price down) = risk-off, not value.
2. **Revision momentum + accelerating/decelerating** — ΔEPS for 2026 & 2027 across recent rows, and whether the revision *pace* is speeding up / steady / slowing. **Guard — needs ≥3 rows;** on a shorter series say *"momentum needs another week or two of history"* rather than computing noise. Track momentum off the **EPS series**, never a 2nd-derivative of the ratio.
3. **Forward-vs-trailing spread (growth priced in)** — forward P/E vs trailing P/E ⇒ the earnings growth the market is paying for (forward < trailing ⇒ growth expected; quantify the implied %). Note the operating-vs-GAAP gap (LSEG trailing *operating* ≈ 25–26× vs multpl *GAAP* ≈ 31–32×) so the forward number isn't read as "cheap" outright.
4. **Horizon spread** — show all three (CY2026 / NTM-F4Q / CY2027) so a bullish single number can't quietly borrow the furthest-out year; name which horizon any external "forward P/E" is using.
5. **What it means + vault cross-check** — 2–3 plain sentences ("steady" is valid). Does it flag the AI thesis? Revision roll-over while price holds → [[AI-demand-durability]] / [[what-could-go-wrong]] / [[hyperscaler-capex]]; multiple expanding ahead of E → the reverse-DCF "priced-in" reference (`raw/research/2026-06-21_reverse-dcf-implementation-reference.md`). If nothing: "no cross-vault flag."

**Then finalize the page:** write the 5 insights into the tracker's **"Latest read — decomposition + revision momentum"** block (this block *is* the 5 insights in prose), add a **one-sentence change-log entry**, **bump `last_updated`**, and **sync the `index.md` Trackers-row date** to match. Touch nothing else (no `log.md`, no other page).

### Step 3 — Report back to Vic (chat; fixed template = the 5 insights)
```
## Forward P/E Watch — <date>

### Readings
2026: <X>× · 2027: <Y>× · NTM/F4Q: <Z>×   (report close <level> @ <report date>; EPS LSEG <as-of>)
Live: S&P <fred level> today → ~<X'>×/<Y'>×/<Z'>× (supplementary)

### 1. Decomposition — what moved & why
<P/E Δ per horizon> = price effect <±A> + earnings effect <±B>.
One line: cheaper/dearer, and for the right reason (earnings) or not (price)?

### 2. Revision momentum (+ accel/decel)
2026 EPS <±$> / 2027 EPS <±$> vs last row; pace accelerating / steady / decelerating.
(≥3 rows needed for accel/decel — else "needs more history.")

### 3. Forward-vs-trailing — growth priced in
Forward <F>× vs trailing <T>× ⇒ ~<g>% earnings growth priced. (Operating, not GAAP.)

### 4. Horizon spread
CY2026 <X>× · NTM/F4Q <Z>× · CY2027 <Y>× — the honest "next-12-mo" multiple is NTM.

### 5. What it means + vault cross-check
2–3 plain sentences. Flag or "no cross-vault flag."

### Watch next
Next weekly LSEG dashboard; the as-of date of the EPS used.
```
End with one line: appended the raw-data CSV + updated the tracker page + its index row (maintenance, not an ingest); nothing else touched.

## Disciplines recap
- **No buy/sell, no price targets.** Dials and decomposition only.
- **One consistent source; never mix within the series; every row dated.**
- **Never invent the level or the EPS** — fetch or paste, else flag stale.
- **Momentum off the EPS series, not the noisy ratio 2nd-derivative.**
- **Operating-EPS basis** reads lower than trailing GAAP — note it so the forward number isn't mistaken for "cheap" outright.
- Not an ingest: no `log.md` / `refresh_log.md` entry; the tracker's own change log is the record. Runs after the creation session are propagation/maintenance, not new sessions.

## What this skill is NOT
- Not a stock-level valuation tool (it's the index-level macro dial).
- Not a recommender or a price-target generator.
- Not a discovery-note skill (it *maintains* a tracker page, like `/spread-watch` — it does not write a `raw/notes/` note).
- Not an auto-scraper of LSEG/FactSet — the EPS is manual-fed (paste or staged PDF) by design, because the clean weekly numbers live in PDFs.
