# Prompt for Claude Code

Paste the block below into Claude Code, run from your repository root with this `design/` folder inside it. Replace the bracketed `[…]` choices first.

---

Read `design/README.md` in full — it's the complete spec for "Stocks Wiki," a Bloomberg-terminal reading layer for a Markdown research vault. The HTML files in `design/` (`Stocks Wiki Terminal.dc.html` = the target design, `Stocks Wiki.dc.html` = an alternate "clean dashboard" reference) are **design references, not code to copy** — do not ship their runtime (`support.js`).

Recreate the **Terminal** design in [this repo's existing stack / a new static site using Astro — pick the best fit and confirm with me first], as **reusable templates** driven by the Markdown frontmatter — one Company template that works for all 84 company pages, one Chokepoint template for all 15, plus Theme / Tracker / Thesis. The site must be **static and offline-friendly** (self-host the IBM Plex Mono font; client-side JS only for search, the command bar, the graph, and the theme toggle).

Build, in this order:
1. **App shell** — sidebar nav (six grouped sections with counts + the thesis-domain filter that dims non-matching items), client-side search over titles + tickers, and the **terminal command bar** (live UTC clock, blinking cursor, `<GO>`, and the exact routing rules in the README). Plus the structural **tape** (streams layers/tiers/severities — never prices) and the colored **F-key** tabs.
2. **Company page template** (verify against the NVDA example) and **Chokepoint page template** (HALEU example, red accent).
3. **Three Structure views** — chokepoint durability board, value-chain layer map, and the wikilink connection graph.
4. **Reusable components** — badge (type / layer / tier / ticker), wide scrollable table, callout, wikilink, backlink panel, severity-pip meter.
5. **Markdown pipeline** — parse YAML frontmatter (`type`, `tickers`, `layer`, `*_tier`, `last_updated`), render the body, resolve `[[Target]]` / `[[Target|alias]]` wikilinks (render unresolved/forward-references as dimmed, non-clickable), and build a **backlink index** ("what links here") at generate time.

Match the README's **design tokens, all-monospace typography, square panels (border-radius 0 everywhere), and the semantic color encodings** (domain, chokepoint grade, severity scale, layer scale) exactly. Keep the discipline: this is a research tool — no buy/sell, price targets, or position sizing anywhere.

**Before writing code:** propose a file/route structure and confirm the framework with me. Then implement **one Company page end-to-end** (frontmatter → fully rendered template) so I can review it before you scale to all 132 pages.

---

## Notes
- Tell Claude Code which framework to use up front (or let it propose one and approve before it builds).
- Reviewing one fully-rendered Company page first is the fastest way to catch token/spacing issues before they're repeated 132×.
- The full visual spec — every hex value, the type scale, the command-bar behavior, responsive rules, and component specs — lives in `README.md` in this folder.
