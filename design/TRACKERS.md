# Handoff — Home page + the 6 Trackers (Stocks Wiki Terminal)

Companion to `README.md` (which holds the full visual system: tokens, type, the terminal shell, and the Home / Company / Chokepoint / Structure templates). **Read `README.md` first** — this doc only adds the **Home page (current version)**, the **navigation model**, and the **six Tracker page templates** that were built after it.

Everything here is the **Terminal** design (`Stocks Wiki Terminal.dc.html`). The HTML files in this folder are **design references, not production code** — recreate the look/behavior in your static-site stack from these specs; don't ship the prototype runtime (`support.js`).

All six trackers are real `type: tracker` pages in the vault. Use **realistic sample data** (the figures below are carried verbatim from the source markdown) so the prototype feels real, but in production each tracker's data comes from its `.md` (frontmatter + body tables + fenced data blocks).

---

## Shared tracker template (build this once)

Every tracker page is the same skeleton inside the terminal shell (sidebar + command bar + tape + section-tab header):

1. **Breadcrumb** — `home / trackers / <name>` (mono, `--text-3`).
2. **Title row** — `<h1>` (25px, 600) + a bordered tagline pill (e.g. "the cycle's fuel gauge").
3. **Standfirst** — one paragraph, `--text-2`, max-width ~780px; the "what this tracks / why it works" line.
4. **Status banner** — a bordered strip with the page's headline state (a status lamp + big label + 2–4 key readings). Color = the composite state.
5. **Hero artifact** — the one thing that page exists to show (dial board / screener / cards / matrix / heatmap / tripwire board).
6. **Supporting panels** — secondary tables/lists.
7. **Footer** — a muted "research, not advice" disciplines line (every tracker carries one).

### Reusable tracker components (spec these as partials)
- **Status pill / lamp** — the universal state token. Square 9–13px swatch + an uppercase mono label. States & colors: `calm`/`baseline` = `--calm` (#646c75), `easing`/`nominal`/`NOT FIRED` = `--up` (#4defc4), `watch`/`widening`/`PENDING` = `--watch` (#f7a21b), `fired`/`confirmed` = `--down` (#ff4d42). Lamps **animate** (`@keyframes lamp{0%,100%{opacity:.55}50%{opacity:1}}`, ~1.4s) ONLY for watch/fired states — calm/nominal stay steady, so a healthy board reads quiet.
- **As-of stamp + freshness flag** — every reading shows its date; a reading older than 45 days gets a red `STALE >45d` flag, unread ones a dim `UNREAD` flag, building ones an amber `WATCH` flag. This honors the vault's freshness discipline — never hide a stale reading, flag it.
- **Reading-rule callout** — a `--surface-2` box, amber `!`, one bold sentence stating how to read the page (e.g. "one dial widening = noise; the signal is AI instruments widening while controls stay calm").
- **Wide table** — full 1px border, `overflow-x:auto` wrapper with `min-width` so it scrolls on mobile, `--surface-2` uppercase-mono header, zebra rows via `--inset`, numeric cells mono + right-aligned.
- **Sortable header** — click toggles asc/desc, active column shows `▾`/`▴`.

---

## Navigation model (changed since README)

The shell's navigation has two coordinated parts:

- **Sidebar = collapsible folders (VS Code style).** Each section header (`COMPANIES 84`, `CHOKEPOINTS 15`, …) has a chevron (`▾` open / `▸` collapsed) and toggles its item list on click. Independent toggles (multiple open at once). Items are indented under their header. Order: Companies · Chokepoints · Themes · Trackers · Thesis · Frameworks · Relationships.
- **Header = section tabs (replaces the old F-key bar).** A row of tabs: `HOME · COMPANIES · CHOKEPOINTS · THEMES · TRACKERS · THESIS · FRAMEWORKS`, each with its section-color dot, active tab highlighted (`--surface-2` bg). Clicking a tab opens a **section index page**; clicking HOME → home. The command-bar context label (top-left) updates to the section name + "index".
- **Section index page** — a generic listing of a section's pages: title + color dot + count + a 1-line description, then a 2-col grid of that section's pages. Built/live pages are clickable and tagged `LIVE` (teal); not-yet-built pages render dimmed and non-clickable (the forward-reference convention). This gives every top-bar tab a real destination.
- **Command bar** routes by keyword too: `nvda`, `haleu`, `spread`/`credit`, `short`, `forward`/`edge`, `capex`/`hyperscaler`, `china`/`taiwan`, `wrong`/`risk`, plus section names (`companies`, `trackers`, …) and `graph`/`map`/`board` (Structure views).

Section colors (used for tab dots, section-index headers, nav dots): Home/Trackers = amber `#f7a21b` (Trackers index header uses `#ff8a3c`), Companies/AI = blue `#2f9bff`, Chokepoints = red `#ff4d42`, Themes = violet `#a98bf5`, Thesis/Humanoid = teal `#4defc4`, Frameworks = slate `#7d8aa0`, Defense = amber `#f7a21b`.

---

## HOME page (current)

Order, top → bottom (max-width 1180px, centered):
1. **Eyebrow** `INVESTMENT-RESEARCH VAULT` (amber) → **hero h1** "Three theses, one supply-chain map." → lede ending muted "Describes structure; never recommends."
2. **Stat strip** — 6-cell bordered grid (1px gaps): `132 pages · 84 companies · 15 chokepoints · 23 themes · 6 trackers · 3 theses`. Collapses to 2 cols on mobile.
3. **Thesis domains** — 3 cards (AI blue / Defense amber / Humanoid teal): square domain-tinted icon tile + uppercase tag + title + 1-line desc + footer counts (`62 co. / 11 chokepoints`). Hover lifts. Click → Structure. Collapses to 1 col on mobile.
4. **Two-column lower block** (1.3fr / 1fr):
   - **Recently updated** — list panel, rows = domain dot + title + type tag + `MM-DD` date. Current order (newest first): `AI credit spread watch · tracker · 06-21` (routes to that tracker), `HALEU fuel chain · chokepoint · 06-14`, `Humanoid robot value chain · theme · 06-08`, `NVDA — NVIDIA · company · 05-24`, `HBM oligopoly · chokepoint · 05-22`, `Memory shortage winners & losers · theme · 05-18`, `Forward-edge tracker · tracker · 05-15`.
   - **Top chokepoints** mini-board + "view board →" link (→ Structure leaderboard); rows = rank + name + grade-color swatch; below it the 3-grade legend.
5. **Footer disclaimer** — "…not investment advice: no buy/sell calls, no price targets, no position sizing."

---

## The 6 Trackers

### 1. AI Credit Spread Watch — a dial board
- **Status banner:** composite signal `GAP ~ZERO · NO DIAL CONFIRMED` + three readings (AI loan spread `6.2pp` vs non-AI `6.1pp`, differential `+0.1pp` teal).
- **Reading rule:** "one dial widening = noise; the signal is the AI instruments widening while the Layer-1 controls stay calm, confirmed on a second dial."
- **Hero = the 9-dial board:** a 3-col grid of square tiles, dials 0–8. Each tile: `DIAL n` + status lamp & label, the dial name (bold), the reading (prose), and a footer with the as-of date + a freshness flag. Current states: dial 1 `WATCH` (amber, pulsing), dial 2 `STALE >45d` (red flag), dials 4 & 8 `UNREAD` (dim), dial 6 `EASING` (teal), the rest `calm`. (The 9 dials, readings and dates are in `AI-credit-spread-watch.md`'s "Current readings" table.)
- **Supporting:** the **four-layer instrument stack** (L1 controls → L2 AI instruments → L3 deal pricing → L4 referee docs, as 4 boxes with colored tags) and the **cycle-turn dashboard** (5 ending-types, one row per dial; this page owns row 1, highlighted `HERE`; "two or more flashing = the turn").
- **Data shape:** an array of dials `{n, status, name, reading, asOf, flag}`; a 4-item layer list; a 5-row cycle table.

### 2. Short Interest Watch — a screener
- **Settlement banner:** `FINRA consolidated · settlement 2026-05-29 · 70/70 vault names · Tier-4 sentiment · ~1–2wk lag`. (The data block in the md is machine-refreshed and fenced — keep that boundary: table auto-generated, prose human-curated.)
- **Reading rule:** signal is outliers & movers, not levels on low-short mega-caps. `CONFIRM` (teal) = heavy short on a name the vault is cautious on; `CHALLENGE` (amber) = heavy short on a name the vault is bullish on (inverse divergence, the high-value item). Thresholds: notable ≥ 8% · crowded ≥ 5 DTC · mover ± 15%.
- **Hero = sortable screener table:** columns `Ticker · Short int · % out · Days-cover · Δ prior · Vault read · Thesis`. Numeric headers sortable (default `% out` desc). Δ colored (rising = red, covering = teal); DTC ≥ 5 highlighted amber; vault-read as a CONFIRM/CHALLENGE tag; ticker has a domain dot. 18 rows (≥ 8% of shares out) from `short-interest.md` — e.g. LEU 30.39% CHALLENGE, CORZ 22.6% CONFIRM, NVTS 19.68% CONFIRM, …
- **Supporting:** 3-panel row — **Most crowded** (DTC ≥ 4), **Skepticism building** (rising short, red), **Bears covering** (falling short, teal); then **Intel** two columns — "Crowd agrees" (CONFIRM names + 1-line) vs "Crowd disagrees" (CHALLENGE inverse-divergence names + 1-line).
- **Data shape:** rows `{ticker, shortInt, pctOut, daysToCover, deltaPct, vaultRead, thesis, domain}`; three short mover lists; two intel lists.

### 3. Forward-Edge Tracker — consensus-vs-vault cards
- **Domain filter:** segmented control `ALL · AI · HUMANOID · DEFENSE` (filters the card list).
- **Hero = divergence cards** (12 total). Each card: header = subjects (domain dot) + a durability badge (`DURABILITY HIGH` teal / `MED` amber / `CONTINGENT` slate) + an `INVERSE DIVERGENCE` badge (red) on the inverse entries (AAOI, FCEL). Body = a 2-column split: **Consensus** (left, `--inset`, muted) vs **Vault view** (right, `--surface`, accent label). Footer = **Catalyst →** (teal label) and **Falsifier →** (red label), then "last moved · date". **Contract: every card must carry both a catalyst and a falsifier.**
- The 12 entries (from `forward-edge-tracker.md`): AI — power>compute, custom-silicon→TSM, AAOI (inverse), FCEL (inverse), memory-shortage cycle-clock, AI-financing regime-flip, "bottleneck game is over" meta, inference-sustains-chokepoints; Humanoid — investor-access lens, order-vs-capacity gamble; Defense — chokepoints>platforms, FY2027-request-not-law.
- **Discipline:** "Consensus" is described as a structural narrative / observable mechanism — never price, market cap, or analyst targets.
- **Data shape:** entries `{domain, subjects, durability, inverse, consensus, vaultView, catalyst, falsifier, lastMoved}`.

### 4. Hyperscaler Capex — a comparison matrix
- **Aggregate band:** 4 stats — `$640–720B` Big-4 2026 · `~$700–770B` incl. ORCL · `~$830B` top-9 global · `~94%` of OCF consumed.
- **Hero = the 7-payer matrix** (wide, scrollable). Columns `Payer · FY2026 guidance (+ style tag) · Latest-Q (+ YoY) · In-house silicon · Backlog/RPO · Funding note`. Each payer row has a left color bar + `BUILD` (blue) / `RENT` (orange) tag; guidance-style tag colored (RANGE/POINT teal = firm, QUALITATIVE/DEFERRED amber = soft). 7 rows: MSFT, GOOGL, AMZN, META, ORCL (build) + CRWV, NBIS (rent/neocloud). Figures from `hyperscaler-capex.md`.
- **Supporting:** **disconfirming-signal grid** (6 cells, all "none observed" teal; the "Neocloud refi failure" cell carries a `MOST SENSITIVE` amber badge — the canary; caption "any two together = the cycle is turning"); then **"visible only when read together"** — 4 cross-cutting dynamics (memory cost-push, in-house-silicon lever, the NVIDIA circularity, the financing shift).
- **Data shape:** payer rows `{payer, kind, guidance, guidanceStyle, latestQ, latestQyoy, silicon, backlog, note}`; aggregate stats; 6 signals; 4 dynamics.

### 5. China & Taiwan Exposure — an 8-axis heatmap
- **Domain filter:** `ALL · AI DATACENTER · DEFENSE`.
- **Hero = the exposure heatmap** (table, scrollable). Columns `Name · Mag · [A B C D E F G H exposure cells] · Evidence`. Each row: a magnitude badge (`ULTRA` red / `HIGH` orange / `MED` amber / `LOW` slate) and 8 small cells — a cell is **filled with the row's magnitude color** if the name carries that axis, dim (`--inset`) if not. So the grid reads as a heatmap by magnitude. ~18 rows from `china-exposure.md` (TSM Ultra C+H; NVDA High A,B,D,E,F,H; AVGO 95%-TSMC; … MP/TDY/LSCC on the Defense side).
- **The 8 axes (A–H):** A China revenue · B Supply/sourcing · C Taiwan-fab/China-assembly · D Outbound export-control · E Inbound export-control · F Chinese competitor · G Adversary-demand (defense) · H China operations. Show an **axis key** (2-col) + a **magnitude legend** below the table.
- **Supporting:** **the structural hedge** — a chip row of the no/minimal-exposure names (MSFT, GOOGL, META, ORCL, NBIS, CRWV, BE, CCJ, CEG, LEU, FLNC, VRT, INOD), teal-bordered, with the note that naming what *isn't* exposed is itself the hedge.
- **Standfirst frames the two structural facts:** correlated-not-diversifiable, and direction-matters-more-than-magnitude.
- **Data shape:** rows `{ticker, domain, axes:"CH"|"ABDEFH"|…, magnitude, evidence}`; the 8-axis key; the hedge list. (Concentration % are Tier-3 — note "verify at primary"; flag billing-address-vs-end-demand.)

### 6. What Could Go Wrong — a tripwire status board
- **Status banner:** green-bordered `ALL TRIPWIRES NOMINAL` + big `0 / 16` FIRED + "as of 2026-06-12".
- **Hero = the register**, grouped by domain (AI 9 / Defense 4 / Humanoid 3). Each domain has a colored section header (count + rule); each entry row: number (`01`…`16`), risk title (bold), `Tripwire:` condition (muted), `canonical home · <page>` (accent), and a right-side status — `NOT FIRED` (teal) / `PENDING` (amber, the Blue UAS date-certain one) / `FIRED` (red, none currently). Lamp animates only for non-nominal.
- **Footer:** "all 32 thesis falsifiers reconcile to these 16 entries; Tier 3/4 may *name* a risk, only primary sources *fire* a tripwire." **No price/valuation tripwires, ever.**
- **Data shape:** entries `{n, domain, title, tripwire, canonicalHome, status}`; status defaults `nominal`.

---

## Build-pipeline notes (Markdown → tracker pages)
- Each tracker's frontmatter is `type: tracker` + `tickers: []` + `last_updated`. The **body carries the data**: dials/competition tables (markdown tables), the short-interest **fenced auto-refresh block** (`<!-- SHORT-INTEREST-DATA:START -->` … `:END -->` with a `<!-- SETTLEMENT: date -->`), the capex matrix table, the china 8-axis matrix table, the risk-register entries.
- Parse those into the data shapes above and feed the components. Keep the **machine vs human boundary** the short-interest page declares: regenerate the fenced data block, preserve the curated prose around it.
- The freshness discipline is load-bearing: surface each reading's `as-of` and compute the `STALE >45d` flag at build time (or client-side from the date).
- Keep the disciplines visible: every tracker renders a "research, not advice" footer; no buy/sell, price targets, or position sizing anywhere.

## Files in this bundle
- `Stocks Wiki Terminal.dc.html` — the design reference containing the home page + all six trackers (now current). Open with `support.js` beside it.
- `README.md` — the full visual system + Home/Company/Chokepoint/Structure + component specs. Read first.
- `Stocks Wiki.dc.html` — the alternate "clean dashboard" reference (not the target).
- `support.js` — prototype runtime (local preview only; not for production).
