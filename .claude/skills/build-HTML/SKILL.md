---
name: build-HTML
description: "Turn ONE dense vault analysis page (a theme / chokepoint / thesis / framework / insight markdown page) into a plain-English, outsider-friendly HTML explainer in the Slock house theme, saved to raw/HTML/. It rewrites the analysis for a general audience who does NOT know the vault's terms (Tier, Layer, chokepoint, neocloud, capex…), builds a self-contained styled page, adds a KEY TAKEAWAYS section, and runs a deterministic QA check plus an independent fidelity-audit subagent before opening it. Use whenever the user wants to build / generate / render an easy-to-read HTML explainer, reading-layer, or 'plain-English version' of a vault theme/chokepoint/thesis/framework/insight page — e.g. '/build-HTML telecom-bust-analog.md', 'build an HTML explainer for HBM-oligopoly.md', 'make a readable HTML version of ai-frontier-systems.md', 'turn wiki/themes/<x>.md into a webpage'. The user passes the page as a `.md` filename (e.g. `transformer-supply.md`) or a full path; a bare slug also resolves. This skill is for ANALYSIS pages only — it is NOT for company pages (those use build-company-html) and it never edits canon; it only writes the gitignored artifact under raw/HTML/. Trigger on any request to produce a plain-language / easy-to-understand HTML page from a vault analysis markdown file; do NOT trigger for company pages, whole-site builds, or editing the source analysis."
---

# build-HTML — a plain-English HTML explainer of one analysis page

This skill turns one dense vault analysis page (`wiki/themes/*.md`, `wiki/chokepoints/*.md`, `wiki/insights/*.md`, `wiki/_thesis*.md`, or `raw/notes/frameworks*.md`) into a **self-contained, easy-to-read HTML explainer** in the **Slock** house theme, saved to `raw/HTML/`. The audience is an **outsider who does not know the vault's vocabulary** — so the skill's real work is a faithful *translation* into plain English, not a restyle. It exists because this exact artifact has been hand-built several times (`memory-wall`, `ai_memory_endgame`, `ai-frontier-systems`, `telecom-bust-analog`); the skill makes the theme, the plain-language rules, the disciplines, and the two-part QA **repeatable and consistent**.

It is the **plain-English sibling** of `build-company-html`: that skill deterministically renders a *company* page as-is into the Bloomberg-terminal *site* (`web/dist/`); this skill *rewrites* an *analysis* page into a *standalone Slock explainer* in `raw/HTML/`. Different input, different theme, different method — do not confuse them.

## The hard boundary (read first)

This is a **reading-layer / discovery tool**, not a canon tool. It MUST NOT, under any circumstances:
- edit, create, or delete the **source** page or ANY file under `wiki/` (theme / chokepoint / company / tracker / relationship / thesis markdown),
- edit `raw/notes/frameworks*.md`, `index.md`, `log.md`, `refresh_log.md`, `conventions-ledger.md`, or `CLAUDE.md`,
- write anywhere except `raw/HTML/`.

The source Markdown is **read-only** here — the skill only ever *reads* it, so the original page cannot be damaged, degraded, or changed. It writes **one** file: `raw/HTML/<source-slug>.html` (a gitignored local artifact — not the public Vercel site, not canon). Git stays Vic's — never commit. If the source *analysis* is wrong, that's a separate human-gated Markdown edit, not this skill's job.

## When to use

- The user invokes `/build-HTML <page>.md` or asks to build / generate / render a plain-English, easy-to-read, or "explainer" HTML page from a vault **analysis** page (theme / chokepoint / thesis / framework / insight). The user's convention is to pass the source as a `.md` filename (e.g. `transformer-supply.md`).
- After an analysis page is written/updated and the user wants a shareable, outsider-friendly version.

Do **not** use this for: a **company** page (use `build-company-html`), the whole public site (`python web/build.py`), or any request to change the source analysis (human-gated ingest).

## Inputs

One page reference. **The user's standing convention is to pass a `.md` filename** (e.g. `transformer-supply.md`, `HBM-oligopoly.md`) — the primary, expected form. A full path (`wiki/chokepoints/transformer-supply.md`) or a bare slug (`transformer-supply`) also resolve. Case-insensitive. **Derive the output name from the file stem** (strip `.md`) → `raw/HTML/<stem>.html`; never produce `<name>.md.html`. Resolve to the actual source file in Step 1.

## Step 1 — Resolve the source (and reject company pages)

- Resolve `python3`.
- The input is normally a **`.md` filename** (the user's convention, e.g. `transformer-supply.md`). Take the file stem (strip a trailing `.md`) and find the source across the analysis locations, in order: `wiki/themes/`, `wiki/chokepoints/`, `wiki/insights/`, `wiki/_thesis*.md`, `raw/notes/frameworks*.md`. A full path resolves directly; a bare slug also resolves. If it resolves to `wiki/companies/<TICKER>.md` (or looks like a ticker), **STOP** and tell the user this skill is for analysis pages — company pages use `build-company-html`.
- If nothing matches, STOP and list near-matches. **Never create the source** (that's a canon action).
- The output filename is `raw/HTML/<stem>.html` (the source's `.md` stem) — do not double-append (`<name>.md.html` is wrong).
- Read the source with the existing parser — reuse, don't re-implement:
  ```python
  # scripts/vault_parsers.py already exposes read_page(path) -> (frontmatter, body)
  ```
  Note `type` and `last_updated` from frontmatter; capture the tickers list (to convert to company names later).

## Step 2 — Understand the page + build the translation map

Read the whole page carefully. Identify:
- its **honest verdict / bottom line** (most analysis pages state one up front — it becomes the explainer's lead),
- its **claims and, critically, their hedges + confidence levels** (Tier-3 `[verify:]` flags, "not proven", "disputed", "as of <date>"),
- its **structure** (the sections that carry the argument),
- the **named entities** (tickers → the company names an outsider knows).

Then build the **jargon → plain-English map** for THIS page. Standard translations (extend per page):
- **Tier 1/2/3 confidence** → a chip legend: **Solid** (well-established / multi-source), **Needs checking** (one source, verify), **Disputed** (evidence both ways).
- **chokepoint / un-floodable layer** → "the part you can't quickly make more of".
- **neocloud / CLEC** → "debt-heavy GPU-rental companies".
- **Layer 1–6 / value-capture position** → "where in the chain the money is made".
- **capex / FCF / book-to-bill / MFU** → plain phrases ("building spend", "spare cash", "orders vs shipments", "how much the chips are actually used").
- **tickers** → **company names** (Nvidia, Micron, CoreWeave…). **Drop internal `[[wikilinks]]` entirely** — an outsider can't follow them.

## Step 3 — Write the plain-English rewrite (fidelity-first)

Rewrite the page for a general reader: short sentences, everyday words, concrete analogies, company names. The one rule that governs everything: **simplify the wording, never the claim.** Every caveat, hedge, confidence level, and "as-of" date in the source must survive into the explainer (as the confidence chips + honest "the catch" notes) — a plain-English version that quietly drops the hedges is a *distortion*, not a simplification. No new external facts: everything in the explainer must trace back to the source page.

Carry the vault's disciplines into the copy: **no buy/sell, no price targets, no position sizing**; keep an explicit **"educational only — not investment advice"** framing; present any cited market/stock history as history, not a prediction.

Draft the **KEY TAKEAWAYS** section here too (Step 5 spec), so it gets audited with the rest.

## Step 4 — Build the Slock HTML

- Read the theme source of truth: `raw/HTML/HTML-theme/slock-design-system.md` + `slock-theme.json`. **Pin the Slock theme** (cream + yellow, 2px black borders, 0px radius, hard `2px 2px 0` shadows, Space Grotesk + Space Mono). **Never** use the other file there (`atmospheric-glass-DESIGN.md`) — it's unused.
- Reuse the proven component kit from the exemplars `raw/HTML/telecom-bust-analog.html` and `raw/HTML/memory-wall-hbm-bandwidth-mu-vs-sndk.html` (copy their `:root` variable block verbatim): the loud yellow `header.hero`, the white `.about` box **with the confidence-chip legend**, `.stats` row, `h2.sec` + `.nbox` numbered section heads, `.card` + `.acc-*` accents, `.analogy` peach callouts, `.bullbear` (green/red) two-column, `.warn` (yellow header) callouts, `ol.steps` numbered lists, `.tablewrap` tables (black header + yellow mono labels), `.insight`, the `.salt` mono footnote, the footer, and the top scroll-progress bar.
- Self-contained single file; Google-Fonts CDN link is fine (the exemplars use it).
- Save to **`raw/HTML/<source-slug>.html`** — simple slug matching the source page, **no date prefix**.

## Step 5 — KEY TAKEAWAYS (a hard requirement — two labeled parts)

Add exactly one KEY TAKEAWAYS section near the end, in **two visibly-separated, provenance-labeled parts**:

- **① What to remember** — 3–5 plain bullets that faithfully summarize the *page's own* conclusions. No new claims.
- **② Our read** — 1–2 points of added synthesis (the single thing that matters most / what to watch), rendered in a **visually distinct, clearly-tagged block** (e.g. teal accent + an explicit label like *"our take — not the report's finding"*, mirroring the "Added by Claude — not vault canon" banner on `ai-frontier-systems.html`). Constraints: **grounded in the page** (no new external facts, so the audit can verify it) and carrying **no advice / price targets**.

The label is the safety mechanism: an outsider must never mistake ② (our angle) for ① (the source's conclusion).

## Step 6 — QA: deterministic check + independent fidelity audit

Two-part QA — the mechanical half is a script, the meaning half is a fresh agent:

1. **Deterministic check** — run the bundled validator and parse its JSON:
   ```bash
   python3 .claude/skills/build-HTML/scripts/check_html.py raw/HTML/<slug>.html
   ```
   It verifies: HTML parses, saved under `raw/HTML/`, **Slock tokens present + zero glassmorphism**, **no insider jargon in the visible text** (Tier/Layer/chokepoint/neocloud/CLEC/MFU/FCF/capex/book-to-bill/wikilink/…), no price-target/buy-sell language, and a labeled KEY TAKEAWAYS. Fix every hard-fail it reports and re-run until it passes.

2. **Fidelity-audit subagent** — spawn a FRESH subagent (Agent tool, `Explore` or general-purpose) that has NOT seen the drafting. Its PRIMARY job is meaning-fidelity, which the author is worst-placed to self-check. Give it the source path + the HTML path and ask it to verify:
   - every substantive claim in the HTML traces to the source, with **no invented facts**;
   - the source's **hedges / confidence levels / "as-of" dates survived** (nothing over-stated by dropping a caveat);
   - the disciplines hold (no buy/sell, no price targets, "not advice" present);
   - the KEY TAKEAWAYS **①** is a faithful summary and **②** "our read" is **grounded in the page + clearly labeled as opinion**;
   - plain-language quality (would a non-expert understand it?).
   Ask it to return a short list of any distortions/omissions/leaks with fixes. **Apply the fixes**, then re-run the deterministic check.

## Step 7 — Report + open

Lead with the verdict. Emit a scannable checklist (✅/⚠️/❌ from the script + the audit — one line each), the `file://…/raw/HTML/<slug>.html` link, then open it:
```bash
open "raw/HTML/<slug>.html"
```
Restate the boundary once: the run touched **only** `raw/HTML/` (a gitignored artifact); the source page and all canon are untouched; git is left to Vic. If a hard check failed and couldn't be fixed, say so plainly at the top — don't bury it.

## Disciplines

- **Fidelity over polish** — simplify the words, never the claim; every hedge survives. A slick page that quietly overstates the source is a failed run. This is why an independent audit agent (not just the author) signs off.
- **Honest-verdict** — the QA report names defects plainly; the deterministic script + the audit produce the pass/fail, not vibes.
- **Plain language** — for the outsider audience: no vault vocabulary in the visible text (the script enforces this), company names not tickers, no internal links.
- **Describe-don't-recommend** — no buy/sell, no price targets, no position sizing; "educational only — not investment advice" framing stays; past stock history is history, not a call.
- **Read-only on canon / no cascade** — reads the source, writes only `raw/HTML/`, never edits the analysis or any other page, never commits.

## What this skill is NOT

- Not for **company** pages — that's `build-company-html` (a different theme + the terminal site).
- Not a whole-site builder (`python web/build.py`) and not part of the public Vercel deploy — `raw/HTML/` is local/gitignored.
- Not a way to edit the source analysis — it only reads canon and renders a plain-English artifact.
- Not a summarizer that drops the hedges — fidelity (caveats + confidence intact) is the whole point.
- Not a committer — git stays Vic's.
