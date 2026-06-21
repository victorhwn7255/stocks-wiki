# Handoff: Stocks Wiki — Bloomberg-Terminal Research Vault

## Overview
"Stocks Wiki" is the human-facing reading layer for a personal investment-research vault of ~132 interlinked Markdown pages, organized around three theses (AI-datacenter supply chain, Defense & Drones, Humanoid Robots). The design renders that Markdown as a fast, navigable static site whose job is to **make the vault's hidden structure visible** — value-capture layers, tier scores, chokepoint-durability grades, and the wikilink graph — in a dense **Bloomberg-terminal** aesthetic.

It is a knowledge tool for thinking, **not** a trading app: it describes where value sits and how durable a moat is, and never gives buy/sell calls, price targets, or position sizing. The terminal "tape" deliberately streams *structural* data (layers, tiers, severities), never prices.

The build pipeline assumption: a script converts each `.md` → an `.html` page using these **templates/components**. So implement reusable templates (one Company template that works for all 84 company pages, one Chokepoint template for all 15, etc.), not one-off pages.

## About the Design Files
The files in this bundle are **design references created in HTML** — prototypes showing the intended look and behavior, **not production code to copy directly**. They are authored as a single self-contained "Design Component" that uses a small runtime (`support.js`) plus inline styles and a logic class. Your task is to **recreate these designs in the target codebase's environment** (React/Vue/Svelte/Astro/plain templating — whatever fits a static-site generator), using its established patterns. If no environment exists yet, the brief calls for a **static, offline-friendly site** (vanilla or the lightest framework; client-side JS only for search/graph/theme/command-bar). Do **not** ship the prototype's runtime.

To preview the prototype locally: open `Stocks Wiki Terminal.dc.html` in a browser (it needs `support.js` beside it, included here). Fonts load from Google Fonts; for a true offline build, self-host IBM Plex Mono.

## Fidelity
**High-fidelity (hifi).** Final colors, typography, spacing, and interactions are specified below and should be recreated faithfully. Two design files are included:
- `Stocks Wiki Terminal.dc.html` — **the approved primary design** (Bloomberg terminal). Build this.
- `Stocks Wiki.dc.html` — the earlier "clean dark dashboard" variant, included only as reference for an alternate (softer) treatment. Not the target.

Everything below describes the **Terminal** design.

---

## Design Tokens

### Color — CSS custom properties (dark/terminal is the default theme)
| Token | Value | Use |
|---|---|---|
| `--bg` | `#000000` | App background (pure black) |
| `--sidebar` | `#000000` | Sidebar background |
| `--surface` | `#0a0c0f` | Panel/card background |
| `--surface-2` | `#13171c` | Raised/active/zebra background |
| `--inset` | `#050607` | Inset wells (search field, tape strip, progress track) |
| `--border` | `#272d34` | Default 1px borders / dividers |
| `--border-2` | `#3b434c` | Stronger borders, active outlines |
| `--text` | `#e8eaec` | Primary text |
| `--text-2` | `#99a0a8` | Secondary text |
| `--text-3` | `#646c75` | Muted labels, meta |
| `--accent` | `#f7a21b` | **Bloomberg amber** — command bar, headers, links, key chrome |
| `--accent-ink` | `#000000` | Text/icon on amber fills |
| `--accent-dim` | `rgba(247,162,27,.15)` | Amber tint backgrounds (active nav, callouts) |
| `--up` | `#4defc4` | Positive / "operational" / live dot (teal) |
| `--down` | `#ff4d42` | Negative / severe / chokepoint (red) |
| `--shadow` | `none` | Terminals are flat — no drop shadows |

Accent is themeable (data-attribute `data-accent`): `amber` (default), `blue` `#2f9bff`, `teal` `#4defc4`, `red` `#ff4d42`.

A secondary **light "paper" theme** exists (`[data-theme=light]`): `--bg:#f3efe6`, `--sidebar:#eee9dd`, `--surface:#ffffff`, `--surface-2:#f6f2ea`, `--inset:#efe9dc`, `--border:#ddd6c7`, `--border-2:#c8bfab`, `--text:#1c1a14`, `--text-2:#5d5747`, `--text-3:#8f8773`, `--accent:#b56a00`, `--up:#0f8a5f`, `--down:#cc3a30`. Dark is primary.

### Semantic encoding colors (these carry meaning — keep them stable across themes)
These are NOT theme tokens; they're data-encoding hexes used in badges, charts, dots.

**Thesis domain** (used for dots, chips, graph nodes):
| Domain | Hex |
|---|---|
| AI-datacenter | `#2f9bff` (blue) |
| Defense & Drones | `#f7a21b` (amber) |
| Humanoid Robots | `#4defc4` (teal) |
| Materials (sub) | `#ff8a3c` (orange) |
| None / neutral | `#646c75` |

**Chokepoint-quality grade** (durability gradient, hot→cool):
| Grade | Hex | Meaning |
|---|---|---|
| Physics / yield-grade | `#ff4d42` | Hardest to replicate |
| Precision-manufacturing | `#f7a21b` | Middle |
| Integration / assembly | `#2f9bff` | Easiest to compete away |

**Severity scale** (index 0–5, used for fuel-chain pips, 5 = "Acute & Binding"):
`['#2a2f36','#3f8f6e','#cdb24a','#f0913a','#ff7a42','#ff4d42']` — fill `score` pips with the color at index `score`.

**Value-capture layer scale** (Layer 1→6, cool→warm):
`['#5ab0ff','#4defc4','#9bd64f','#f7a21b','#ff7a3c','#ff5a4a']` — Layer 1 (platform) is index 0.

Badge intensity convention for tier scores (1–5, **lower = more central**): tiers 1–2 render as a **solid fill** of the domain color with black text; tiers 3–5 render as a tinted background (`rgba(domain, .10)`) with colored text and a domain-colored border whose opacity fades as the tier number rises (more central = more saturated).

Helper used throughout: `hexA(hex, alpha)` → converts a `#rrggbb` to `rgba()`.

### Typography
- **One family, monospace, everywhere:** `'IBM Plex Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace`. Applied globally (`#app, #app *`). This all-mono treatment is core to the terminal feel.
- Weights used: 400, 500, 600, 700.
- Letter-spacing: labels/uppercase use `.3px–.8px`; body uses `0–.1px`.
- Type sizes (px): hero h1 `30`, page h1 `27`, structure h1 `25`; section header (h2) `14` (uppercase, 600, amber, letter-spacing `.6px`); body prose `14.5`/line-height `1.65`; table cells `13`; KPI numbers `18–23`; labels/meta `9.5–11`; tape `10–11`; nav items `13`.
- Headings & most labels are **UPPERCASE**. Page-title h1s are sentence case.

### Shape, spacing, motion
- **Border-radius: 0 everywhere** (`#app *{border-radius:0}`). Square panels, square chips, square "dots". This is essential to the look — do not round anything.
- Borders: 1px solid `--border`. Panels are boxy with full borders (never single-side accent stripes — an earlier accent-border treatment was explicitly rejected).
- Spacing rhythm: page padding `30–34px` desktop; panel padding `12–20px`; gaps `6–14px`; section header top margin `~26px`.
- Shadows: **none**.
- Motion: blinking cursor/dots `@keyframes blink{0%,48%{opacity:1}49%,100%{opacity:0}}` (~1.1s `step-end`); tape marquee `@keyframes tape{from{translateX(0)}to{translateX(-50%)}}` (~52s linear, list duplicated ×2 for seamless loop); content slide-in `@keyframes fadeUp{from{translateY(7px)}to{none}}` (do **not** animate opacity to 0 — it can strand content invisible).
- Selection color: `--accent-dim`. Scrollbars: thin (10px), thumb `--border-2`.

---

## Global Layout / App Shell
Two-column CSS grid: `grid-template-columns: 284px 1fr` (sidebar | main), `min-height:100vh`.

### Sidebar (left, 284px, sticky full height, `--sidebar` bg, 1px right border)
Top→bottom:
1. **Brand block** (padding 18px, bottom border): a 26px amber square logo (an up-and-to-the-right line-chart glyph in `--accent-ink`) + wordmark `STOCKS·WIKI` (mono 13.5px 600) + subtitle `research vault · 132 pages` (10px `--text-3`). Click → Home.
2. **Search field** (inset well, square): magnifier icon, text input "Search titles, tickers…", a `/` kbd hint. Typing shows a **results dropdown** (absolute, `--surface` panel, 1px `--border-2`) listing up to 7 matches over titles + tickers; each row has a type tag + title; click routes. Empty → "No matches."
3. **Thesis-domain filter**: label "THESIS DOMAIN" + 4 square chips — `All`, `AI-DC`, `Defense`, `Humanoid` — each with a leading domain-color square. Selecting a domain **dims** (opacity .4) nav items not in that domain.
4. **Nav groups** (scrollable): six groups in this order with counts — **Companies (84)**, **Chokepoints (15)**, **Themes (23)**, **Trackers (6)**, **Relationships (1)**, **Thesis (3)**. Each group = an uppercase label + count, then items. Each item = a domain-color square dot + title + optional ticker (mono, right). The **current page** is highlighted (background `--accent-dim`, text `--text`). Hover → `--surface-2`.
5. **Footer row**: theme toggle button (sun/moon icon + LIGHT/DARK) + version `v · 2026.06`.

On **≤900px**: sidebar becomes a fixed off-canvas drawer (`translateX(-101%)`, slides in when `data-nav-open='1'` on `#app`), with a dark scrim; a hamburger in the command bar opens it.

### Main column
Contains the **terminal header** (sticky, always visible) then the routed screen. Right-hand pages (Company, Chokepoint) add a 270px right rail (`grid-template-columns:1fr 270px`); rail hidden ≤900px.

---

## The Terminal Header (signature element — three stacked strips, sticky top of main)

**Strip 1 — Command line** (height 38px, black, bottom border):
- (mobile only) hamburger button, amber.
- Left context block: a 9px amber square + **route label** (amber, 700) + **route kind** (muted). The label updates per page: Home→`HOME / vault`, Company→`NVDA US / equity`, Chokepoint→`HALEU / chokepoint`, Structure→`STRUCTURE / analytics`.
- A muted `│` divider, then an amber `›` prompt.
- **Command input** (flex-1, transparent, uppercase, 12px): placeholder `ENTER TICKER OR PAGE — e.g. NVDA, HALEU, STRUCTURE`.
- A **blinking amber block cursor** (8×15px, `blink` animation).
- A **`<GO>`** button (amber fill, black text, 700).
- Right meta (hidden ≤640px): a blinking teal live-dot + **live UTC clock** `HH:MM:SS` (amber) + `UTC`.

**Command behavior:** on Enter or `<GO>`, parse the typed string (case-insensitive) and route:
- `^nvda|nvidia` → Company (NVDA)
- `^haleu|leu|centrus` → Chokepoint (HALEU)
- `^home|menu|hub` → Home
- contains `graph|network|connection` → Structure (graph view)
- contains `map|layer` → Structure (value-chain map)
- contains `board|leader|choke|struct|analy` → Structure (leaderboard)
- otherwise fuzzy-match the search index (title includes term, or ticker exact) → route to that page; fallback Home.
- Clear the input after routing.

**Strip 2 — Structural tape** (height 24px, `#050607`, overflow hidden): an inline-flex row, `tape` marquee (~52s linear infinite, list duplicated for seamless loop). Each cell = ticker (white, 600) + a colored meta token, separated by 1px right borders. Tokens stream **structure, not prices**, e.g.:
`NVDA L1·PHO1` (blue) · `TSM L2` (blue) · `HALEU SEV 5/5` (red) · `HBM PHYS-GRADE` (red) · `MP MAT1·HUM` (teal) · `CoWoS PRECISION` (amber) · `LEU L4·ENRICH` · `BWXT L4·DEF` (amber) · `6324 HUM·GEAR` (teal) · `CPO INTEGRATION` · `ASML L2·EQUIP` · `COHR L3·OPTICS` · `AVGO CTRL-POINT` · `OPEN-Q 12 ACTIVE` (amber) · `VAULT 132 PAGES` (amber).

**Strip 3 — Function keys** (height 30px, black, bottom border): four nav "keys" — each a small colored key-chip (`F1`–`F4`, black text) + label, separated by 1px borders, active key gets `--surface-2` bg + `--text` color:
- `F1 HOME` (amber) · `F2 COMPANY` (blue) · `F3 CHOKEPOINT` (red) · `F4 STRUCTURE` (teal).
- Right-aligned muted tagline `RESEARCH · NOT ADVICE` (hidden ≤640px).

---

## Screens / Views

### 1) Home / Landing
- **Eyebrow** `INVESTMENT-RESEARCH VAULT` (amber, uppercase, 11px).
- **Hero h1** "Three theses, one supply-chain map." (30px, 600) + lede paragraph (15px `--text-2`) ending with muted "Describes structure; never recommends."
- **Stat strip**: 6-cell grid (1px gaps over `--border`, boxy): `132 pages`, `84 companies`, `15 chokepoints`, `23 themes`, `6 trackers`, `3 theses`. Big mono number (23px) + label. Collapses to 2 cols ≤640px.
- **Thesis domains**: 3-card grid (collapses to 1 col ≤640px). Each card = a square domain-tinted icon tile + uppercase domain tag (domain color) + title + 1-line description + footer counts (`62 co.` / `11 chokepoints`). Hover: border→`--border-2`, lift `translateY(-2px)`. Click → Structure. Content:
  - **AI Datacenter** (blue): "Compute, memory, photonics, power, equipment & materials — the core chokepoints." 62 co. / 11 chokepoints.
  - **Defense & Drones** (amber): "Unmanned systems and the value chain behind autonomous defense." 14 co. / 2 chokepoints.
  - **Humanoid Robots** (teal): "The embodied-AI value chain: actuators, reducers, sensors, magnets." 8 co. / 2 chokepoints.
- **Two-column lower section** (1.3fr / 1fr):
  - **Recently updated** list panel: rows with domain dot + title + type tag + `MM-DD` date. Items (in order): HALEU fuel chain · chokepoint · 06-14; Humanoid robot value chain · theme · 06-08; NVDA — NVIDIA · company · 05-24; HBM oligopoly · chokepoint · 05-22; Memory shortage winners & losers · theme · 05-18; Forward-edge tracker · tracker · 05-15.
  - **Top chokepoints** mini-board: header + "view board →" link (→ Structure). Rows = rank + name + a square grade-color swatch. Below: grade legend (3 squares). Top 5 = HALEU enrichment, HBM oligopoly, InP / laser substrate supply, Rare-earth magnet substrate, TSMC-CoWoS advanced packaging.
- **Footer disclaimer** (top border, muted): "…It is **not investment advice**: no buy/sell calls, no price targets, no position sizing."

### 2) Company page template (example content: NVDA)
Two-column (`1fr 270px`), left main max-width 840px.
- **Breadcrumb** (mono): `home / companies / NVDA`.
- **Header row**: a `COMPANY` type pill (amber, bordered) + a ticker pill `▲ NVDA` (up-arrow in teal) + `updated 2026-05-24`.
- **Title** h1 "NVIDIA Corporation" + subtitle "The platform definer of the AI compute supply chain."
- **Badge bar** (boxy panel): the per-page structural badges, divided by vertical rules, ending with muted "most central →":
  - **L1** square badge (layer-1 blue tint) → label "Layer 1 / Platform definer".
  - **PHO·1** badge (solid blue fill, black text) → "Photonics Tier 1 / Structural chokepoint".
- **Sections** (each: amber uppercase h2 + prose; section ids for the TOC):
  - **Thesis role** (`#role`) — two paragraphs. Inline **wikilinks** to `TSM`, `TSMC-CoWoS` (see Wikilink component). Then a **callout** (boxy `--surface-2` panel, amber info icon): the 75.2% gross-margin / multi-layer value-capture note.
  - **Financial snapshot** (`#fin`) — sub-label `Q1 FY2027 · period ending 2026-04-26`. A 4-up **KPI grid**: `Revenue $82B / +85% YoY`, `Data Center $75B / +92% YoY`, `Gross margin 75.0% / non-GAAP`, `Free cash flow $49B / record qtr` (delta colored: up=teal, neutral=muted). Then the **wide table** (see Table component): columns Platform | Sub-market | Revenue | QoQ | Scope; rows Data Center·Hyperscale·$38B·+12%, Data Center·ACIE·$37B·+31%, Edge Computing·—·$6.4B·+10%. Footnote about venue-asymmetric disclosure.
  - **Supply-chain dependencies** (`#supply`) — prose with wikilinks `TSM`, `Coherent`, `Lumentum`, `NVDA-platform-integration`.
  - **Open questions** (`#oq`) — numbered list (`01/02/03`, amber index) with bottom-bordered rows.
  - Footer disclaimer line.
- **Right rail** (270px, sticky, left border): **On this page** TOC (links to the section ids; hover→amber) + **Linked from N** backlinks panel (boxy chips: domain dot + title + type tag; click routes). Backlinks: TSM, HBM oligopoly, TSMC-CoWoS packaging, CPO platform battle, Humanoid robot value chain, AI-demand durability, NVDA platform integration.

### 3) Chokepoint page template (example: HALEU)
Same two-column structure. Accent for this page type is **red** (`#ff4d42`) instead of amber on the type pill and section headers.
- Breadcrumb `home / chokepoints / HALEU fuel chain`; `CHOKEPOINT` pill (red); `updated 2026-06-14`.
- Title "HALEU fuel-chain chokepoint" + subtitle.
- **Two header panels** side by side:
  - **Severity (HALEU enrichment)**: five 13×22px pips all filled red + big `5/5` + "Acute & Binding".
  - **Chokepoint quality**: a red square + "Physics / yield-grade" + "Hardest to replicate — sole NRC-licensed Western producer."
- **Related tickers** chip row: `LEU BWXT CCJ BE GEV CEG` (mono bordered chips).
- Sections (red uppercase h2s):
  - **Chokepoint identification** (`#cid`) — prose + a red-toned **callout** ("Sequential dependency…").
  - **Six-layer fuel chain** (`#chain`) — six boxy rows, each: layer name + source sub-line + a 5-pip severity meter (filled to `score` in the severity color) + `score/5`. The **anchor** row (HALEU enrichment, 5/5) is highlighted with a red border + inset ring. Rows: Mining 3, Conversion 4, LEU enrichment 4, **HALEU enrichment 5 (anchor)**, Deconversion 4, Fabrication 3.
  - **Western competition status** (`#comp`) — table: Competitor | Timeline | Status. Status is a colored tag: OPERATIONAL (teal), FUNDED (amber), PRE-FID / PRE-LICENSE (red). Rows: Centrus (LEU) · operational; URENCO USA · pre-FID; Orano·Project IKE · funded; General Matter · pre-license.
  - Footer disclaimer.
- **Right rail**: TOC + "Linked from 4" (LEU — Centrus, BWXT, Commodity supercycle, China exposure).

### 4) Structure visualizations
Header (eyebrow + h1 "Make the hidden structure visible" + lede) and a **segmented tab control** (uppercase, active tab = `--surface-2` bg + `--border-2` outline + amber text): **Chokepoint board · Value-chain map · Connection graph**.

- **Chokepoint board (leaderboard)**: grade legend, then a boxy list ranked by **durability** (not size). Each row: rank + a 4px grade-color bar + name + sub-line (`grade · tickers`) + a 120px durability progress bar (filled `dur%` in grade color over an inset track) + a domain dot. 10 rows from HALEU enrichment (99) down to Actuator assembly (40). HALEU row click → Chokepoint page. Caption explains physics > precision > integration ordering.
- **Value-chain map**: six boxy rows L1–L6, each: a layer-color square badge (`L1`…`L6`) + title + sub + a wrap of mono company chips (hover border→layer color). L1 Platform definer (NVDA, AVGO, MRVL, ANET) → L6 Raw materials (Uranium, Rare earths, Gallium). NVDA chip → Company; LEU chip → Chokepoint. Caption explains the cool→warm gradient.
- **Connection graph**: an SVG (`viewBox 0 0 900 540`) centered on a large **NVDA** node, two rings of neighbors, straight edges (each = a wikilink), node radius ∝ backlink count, node color by domain/type (AI blue, humanoid teal, chokepoint red, theme gray). Hover brightens; click a *built* node (NVDA) navigates. Legend + caption below.

---

## Reusable Component Specs
Implement these as components/partials the Markdown→HTML build can emit:

- **Badge — type pill**: uppercase mono 10px, 3px 8px padding, 1px border, square; color by page type (company=amber, chokepoint=red, theme/tracker as needed).
- **Badge — layer**: square tile, `Ln`, background `hexA(layerColor,.16)`, text layerColor, 1px border `hexA(layerColor,.5)`.
- **Badge — tier score**: `DOMAIN·n` (e.g. `PHO·1`). Tier 1–2 = solid domain fill + black text; tier 3–5 = `hexA(domain,.10)` bg + domain text + domain border fading with tier number. Lower n = more central = more saturated.
- **Badge — ticker chip**: mono 11px, 1px `--border-2`, square, `--text-2`.
- **Table**: full 1px `--border` frame, `overflow-x:auto` wrapper (financial tables are wide — `min-width` ~560–620px so they scroll on mobile), `--surface-2` header row with uppercase mono 10.5px muted headers, 1px row dividers, zebra via `--inset` on alternate rows, numeric cells mono and right-aligned.
- **Callout**: boxy `--surface-2` panel, 1px `--border`, 14×16px padding, optional leading accent icon. (Note: **no single-side accent border** — flat full border only.)
- **Wikilink**: inline `<a>`. **Resolved** = `--accent` text + 1px dotted underline + pointer, hover tint, routes in-site. **Unresolved / forward-reference** = `--text-3` text + 1px dashed underline + `not-allowed` cursor + opacity .7, **non-clickable** (title: "forward-reference (page not yet created)"). `[[Target]]` and `[[Target|alias]]` both supported.
- **Backlink panel**: "Linked from N" + boxy chips (domain dot + title + type tag), click routes.
- **Severity pip meter**: N square pips; fill `score` of them with `SEV[score]`.

---

## Interactions & Behavior
- **Routing**: client-side view switch between Home / Company / Chokepoint / Structure (+ Structure sub-views leaderboard/map/graph). Current nav item & function key reflect the active route. In a static-site build, these can be real pages/URLs; the prototype does it in-app.
- **Command bar**: parse + route as specified above; clears on submit.
- **Search**: live client-side filter over an index of titles + tickers; dropdown of ≤7; click routes. (Build a JSON index at generate time.)
- **Domain filter**: dims non-matching nav items (opacity .4); does not remove them.
- **Theme toggle**: swaps `data-theme` (dark↔light "paper").
- **Hover states**: nav/list rows → `--surface-2`; cards → border `--border-2` + 2px lift; tabs/keys → `--surface-2`; wikilinks/TOC → amber.
- **Live clock**: updates every 1s (UTC HH:MM:SS).
- **Animations**: tape marquee (~52s), blinking cursor/dots (~1.1–1.6s), content `fadeUp` slide (never animate opacity→0).

## Responsive Behavior
- **≤900px**: single column; sidebar becomes an off-canvas drawer (hamburger in command bar + scrim); right rails hidden; function-key strip scrolls horizontally.
- **≤640px**: stat strip → 2 cols; thesis grid → 1 col; command-bar clock/meta + the `RESEARCH · NOT ADVICE` tagline hidden (`.hide-sm`); tables scroll horizontally.
- Primary target is laptop; phone must stay glanceable.

## State Management
- `route` ('home' | 'company' | 'chokepoint' | 'structure'), plus `viz` ('leaderboard' | 'layermap' | 'graph') for Structure.
- `active` (current nav item title, for highlight), `domain` (filter), `q` (search query), `cmd` (command input), `theme`, `navOpen`, `now` (clock tick).
- Data is static/derived (nav groups, leaderboard rows, layer map, graph nodes/edges, tape items, page content). In production these come from the Markdown frontmatter + body and a generated link/backlink index.

## Data model (from Markdown frontmatter)
Each page carries YAML: `type` (company|chokepoint|theme|tracker|relationship|thesis), `tickers: []`, `layer` (1–6, companies), one or more `*_tier` scores (`photonics_tier`, `energy_power_tier`, `defense_tier`, `equipment_tier`, `humanoid_tier`, `materials_tier`; ~1–5, lower=more central), `last_updated`. Body is Markdown (headings, tables, blockquotes, `[[wikilinks]]`). The renderer must: resolve wikilinks (dim unresolved), compute backlinks ("what links here"), and surface layer/tier/severity as the badges/meters above.

## Assets
- **Font**: IBM Plex Mono (weights 400/500/600/700). Prototype loads from Google Fonts; **self-host for offline**.
- **Icons**: all inline SVG (logo line-chart glyph, search, menu/hamburger, sun/moon, info, link, thesis-domain glyphs). No icon library — recreate as small inline SVGs or your codebase's icon set.
- No raster images. No external CDN beyond the font (which should be self-hosted).

## Files in this bundle
- `Stocks Wiki Terminal.dc.html` — **primary** design (Bloomberg terminal). Build this.
- `Stocks Wiki.dc.html` — alternate "clean dark dashboard" reference (not the target).
- `support.js` — the prototype runtime (needed only to open the HTML locally; **not** for production).

> Reminder: these HTML files are **design references**. Recreate the look/behavior in your static-site stack using the tokens and specs above — don't ship the prototype runtime.
