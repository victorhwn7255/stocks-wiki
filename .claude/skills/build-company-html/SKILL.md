---
name: build-company-html
description: Build (render) the Bloomberg-terminal HTML page for ONE company in the stocks-wiki vault from its wiki/companies/<TICKER>.md markdown, then run a deterministic QA audit and report pass/fail before opening it. Use this skill whenever the user wants to generate, build, render, rebuild, or refresh the website/HTML page for a specific company by ticker — e.g. "/build-company-html NVDA.md", "/build-company-html NVDA", "build the company page for NVDA", "render NVDA's webpage", "regenerate INTC's HTML page", "make the site page for SANHUA", "rebuild the HTML for TSM", or "I just ingested CRDO, build its web page". The input is normally a company .md filename (e.g. NVDA.md) or a bare ticker (NVDA). The skill is company-specialized (NOT for chokepoint / theme / tracker / thesis / framework pages). It renders canon VERBATIM into the terminal site (web/dist/) — it does NOT rewrite; for a plain-English rewritten explainer of an ANALYSIS page use its sibling build-HTML instead. It only writes the gitignored build artifact under web/dist/ — it never edits wiki/ markdown, index.md, log.md, or any canon. Trigger on any request to produce or update the rendered HTML for a single named company; do not trigger for whole-vault site builds or for non-company page types.
---

# build-company-html — render + QA one company's terminal HTML page

This skill turns one company's canonical Markdown (`wiki/companies/<TICKER>.md`) into its rendered Bloomberg-terminal HTML page under `web/dist/`, then **proves it rendered correctly** with a deterministic QA audit and an honest pass/fail report. It exists because a bare `python web/build.py --only <TICKER>` produces a page but gives **no signal that the page is right** — and the company set has genuinely tricky frontmatter shapes (int `layer`, `"1, 2"` straddle, `"outside"` placement, foreign issuers, `memory_tier`) that have silently rendered wrong before (a badge-less INTC, a mis-colored SANHUA). The skill's value is **build + QA + honest verdict**, not just "run the build."

**Sibling skill (pick the right one):** this skill **renders a *company* page verbatim** into the terminal *site* (`web/dist/`) — canon-faithful, no rewriting. Its sibling **`build-HTML`** does the opposite — it **rewrites an *analysis* page** (theme / chokepoint / thesis / framework / insight) into a **plain-English, outsider-friendly Slock explainer** saved to `raw/HTML/`. Different input, theme, and method. If the ask is "make an easy-to-read / plain-English version of a theme or chokepoint page," that's `build-HTML`, not this skill.

## The hard boundary (read first)

This skill is a **build-artifact tool**, not a canon tool. It MUST NOT, under any circumstances:
- edit, create, or delete any file under `wiki/` (company / chokepoint / theme / tracker / relationship / thesis markdown) — including the target `wiki/companies/<TICKER>.md` itself,
- edit `raw/notes/frameworks*.md`, `index.md`, `log.md`, `refresh_log.md`, `conventions-ledger.md`, or `CLAUDE.md`,
- touch any page type OTHER than companies.

It writes **only** to `web/dist/` (a gitignored build artifact, regenerated from Markdown) by invoking `web/build.py`. The Markdown vault stays the single source of truth and is read-only here. Git stays Vic's — never commit. If a company's *content* is wrong, that is a separate human-gated Markdown edit, not this skill's job; this skill only renders what already exists and reports what it sees.

## When to use

- The user invokes `/build-company-html <TICKER>.md` (or a bare `<TICKER>`) or asks to build / render / rebuild / refresh the HTML or website page for a specific **company**.
- Right after a company's Markdown was ingested/edited and the user wants its rendered page updated.

Do **not** use this for:
- a whole-vault build (just run `python web/build.py`);
- a **plain-English / easy-to-read explainer** of a theme / chokepoint / thesis / framework / insight page → that's the **`build-HTML`** sibling (it rewrites into a Slock explainer in `raw/HTML/`);
- rendering a non-company **analysis** page into the terminal site → those have their own templates in the full build (`python web/build.py`);
- any request to change the company's Markdown/analysis (that's a human-gated ingest, not a render).

## Inputs

One company reference — a **`.md` filename** (`NVDA.md`, the user's standing convention) or a **bare ticker** (`NVDA`). Strip any trailing `.md` and upper-case the stem to get `<TICKER>` (matches `wiki/companies/<TICKER>.md`). Case-insensitive. Optional: `fast` to use the single-page build (`--only`) instead of the full site build (see Step 3).

## Step 1 — Preconditions

- Resolve `python3`.
- Confirm `web/build.py` exists (the generator + audit engine). If missing, stop and say the website generator isn't set up.
- Normalize the input: strip a trailing `.md` and upper-case the stem → `<TICKER>`. Confirm `wiki/companies/<TICKER>.md` exists. If it does **not**, run the audit anyway (Step 2) to get the suggested near-matches, then STOP — report that there's no such company page and list the near-matches. **Never create the Markdown** (that's a canon/ingest action, not this skill). (If the `.md` resolves to an analysis page rather than a company — e.g. a theme/chokepoint — redirect: rendering into the terminal site is `python web/build.py`; a plain-English explainer is the `build-HTML` sibling.)

## Step 2 — Validate (audit the source, before building)

Run the deterministic audit in machine-readable mode:

```bash
python3 web/build.py --audit <TICKER> --json
```

This re-indexes the whole vault (so wikilinks resolve and backlinks are accurate) and prints one JSON object. Parse it. Confirm:
- `exists: true` and `frontmatter_ok: true` — if `exists:false`, STOP and surface `near_matches`.
- `type: "company"` — if not company, STOP (wrong page type for this skill).
- `placement` is a recognized shape (a numeric `layer`, a `"1, 2"` straddle, or `"outside"`; tiers numeric or `"outside"`). An unrecognized/empty placement is a red flag worth calling out.

At this point the page may not be freshly built — that's expected; `render.built` will be `false` until Step 3. This validate pass is "is the *source* sane?"

## Step 3 — Build

Default: full site build (keeps the shared sidebar nav, search index, and structural tape consistent across every page — no per-page drift):

```bash
python3 web/build.py
```

This is ~2-3 seconds for all pages. If the user passed `fast`, use the single-page build instead — quicker, but it can leave *other* pages' nav/search slightly stale until the next full build:

```bash
python3 web/build.py --only <TICKER>
```

## Step 4 — QA (audit again, now with render checks)

Re-run the audit. The built HTML now exists, so the `render` block populates:

```bash
python3 web/build.py --audit <TICKER> --json
```

Map the JSON to a pass/fail checklist (this is the deliverable — be honest, don't rubber-stamp):

| Check | Pass when |
|---|---|
| Page + frontmatter | `exists` && `frontmatter_ok` && `type == "company"` |
| Placement recognized | `placement` is a numeric layer / `"1, 2"` straddle / `"outside"` (not empty/garbled) |
| Structural badge | `badge_count >= 1` — list `badges` (e.g. `L1 · PHO·1`) |
| Domain classified | `domain` ∈ {ai, def, hum, mat}; ⚠️ flag if `none` (gray dot — usually an outside-placed name not anchoring a known thesis) |
| Wikilinks | report `resolved`/`total`; **list `dead_list`** so the user can eyeball typo-vs-intentional-forward-ref (a few dead = normal forward-refs like `[[QCOM]]`; a spike = a likely typo) |
| TOC + backlinks | `toc_sections >= 1` and `backlinks` count (0 backlinks is allowed but worth noting) |
| Render correct | `render.built` && `render.company_pill` && `render.breadcrumb_ok` |
| Tickers | `tickers` non-empty |

## Step 5 — Report + open

Emit a scannable, plain-language summary: the ticker + title, the ✅/⚠️/❌ checklist above (one line each), and the `file://…/web/dist/companies/<TICKER>.html` link. Then open it (macOS):

```bash
open "web/dist/companies/<TICKER>.html"
```

Lead with the verdict: "✅ <TICKER> built clean" or "⚠️ <TICKER> built, but: <the flags>". If any **hard** check fails (no badge, render broken, wrong type), say so plainly at the top and don't bury it.

## Step 6 — Boundary check (restate)

Confirm in the report (once) that the run touched **only** `web/dist/` (a gitignored artifact) — nothing under `wiki/` or canon was edited, and git is left to Vic. If the user actually wanted to change the company's *content*, remind them that's a separate human-gated Markdown ingest, not this skill.

## Disciplines

- **Honest-verdict** — the QA report names defects plainly; a run that finds a problem and says "all good" is a failed run. Pass/fail comes from the deterministic `--audit` facts, not vibes.
- **Plain language** — simple words in the chat summary.
- **Describe-don't-recommend / no canon cascade** — this renders structure; it never edits analysis, never writes canon, never commits.
- **Companies only** — if asked for a chokepoint/theme/etc., say it's out of scope and route: a **plain-English explainer** of that page → the **`build-HTML`** sibling; rendering it into the terminal site → the whole-site build (`python web/build.py`).

## What this skill is NOT

- Not a whole-vault site builder (use `python web/build.py` directly).
- Not a renderer for non-company page types.
- Not a **plain-English rewriter** — it renders canon verbatim; for an easy-to-read explainer of an analysis page use the **`build-HTML`** sibling (Slock theme, `raw/HTML/`).
- Not a way to create or edit a company's Markdown / analysis — it renders existing canon to HTML only.
- Not a committer — `web/dist/` is gitignored; git stays Vic's.
