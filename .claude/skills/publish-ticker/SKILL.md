---
name: publish-ticker
description: Export ONE approved stocks-wiki vault page (company / chokepoint / theme) into the kicker-app (Ticker) content bridge — a persona account + grounded source sections written into kicker-app/content/accounts.json and sources.json, scrubbed of all internal notation and proprietary-sourced material. Use when the user asks to "publish <PAGE> to ticker/kicker", "export <TICKER> to the feed", "create the <PAGE> persona/account", or "add <PAGE> to the kicker content bridge". Input is a vault page name or ticker (e.g. "HALEU-fuel-chokepoint", "AVAV"). This is the ONLY mechanism by which vault knowledge crosses into the public app.
---

# publish-ticker — export a vault page across the content bridge

This skill is the crane on the vault side of the one-way bridge to **kicker-app** (the Ticker feed product at `/Users/victor_he/Projects/kicker-app`). It reads ONE canonical vault page, distills a **persona account** (voice + bio + tier-tagged "knows" claims) and **source sections** (the generation reservoir the tweet engine rewords), scrubs everything for public consumption, and merges the result into kicker's `content/accounts.json` + `content/sources.json`. Kicker re-validates everything on its side (zod schemas in CI + an LLM attribution audit) — two gates, one per side of the bridge.

## The hard boundary (read first)

- **Vault side is READ-ONLY.** Never edit any vault file (wiki/, index.md, log.md, raw/, CLAUDE.md). This skill only reads.
- **Writes go to exactly two files:** `kicker-app/content/accounts.json` and `kicker-app/content/sources.json`, via the merge script (upsert — never clobber other entries).
- **Git stays the user's, on BOTH repos.** The expected end state is an uncommitted diff in kicker-app that the user reviews.
- **Nothing derived from proprietary/paywalled sources crosses the bridge** (Fundstrat, LSEG, J.P. Morgan research, paywalled transcripts). If a fact's only support is such a source, it does not export.
- **Human gate:** the user reviews the kicker diff and runs (or delegates) the kicker-side import: `pnpm validate-content` → `pnpm engine:audit-sources` → `pnpm db:seed`.

## When to use

- `/publish-ticker <PAGE>` — e.g. `/publish-ticker HALEU-fuel-chokepoint`, `/publish-ticker AVAV`.
- After a vault ingest/refresh, to push the sharpened page's facts to the feed ("refresh AVAV's ticker sources").
- Batch launches ("publish the remaining chokepoints") — run the process per page; one staging file per page is fine.

Do **not** use for: thesis/framework/tracker/relationship pages (no account kind exists for them — trackers may map to `theme` ONLY if the user explicitly asks); pages with `last_updated` older than ~90 days without flagging staleness to the user first; anything the user has not approved for publishing.

## Field mapping (vault page → kicker account)

| Kicker field | Derivation |
|---|---|
| `handle` | Company: `@TICKER`. Chokepoint/theme: `@kebab-slug` shortened sensibly (`@HALEU-fuel`, `@who-holds-the-risk`). Must match `^@[A-Za-z0-9-]+$`. |
| `kind` | `company` / `chokepoint` / `theme` from the page's vault type. |
| `vault_page` | **REQUIRED.** The vault page's filename stem, verbatim (e.g. `HALEU-fuel-chokepoint`, `training-to-inference-shift`, `AVAV`) — NOT the shortened handle. This is the mechanical join key for kicker's `/check-accounts` coverage checker; the merge script errors if it is missing or the file does not exist under `wiki/<kind-plural>/`. |
| `display_name` | Company legal-short name; chokepoint/theme: plain-English name. |
| `domain` | `"AI datacenter"`, `"Defense"`, `"Robotics"`, or `"Materials"` — from the page's thesis domain. |
| `avatar` | Company: the ticker. Chokepoint: 3–4 letter code (pattern: TRF, HBM). Theme: omit (renders nodes glyph). |
| `desc` | One-line third-person directory descriptor. Plain language. |
| `bio` | First-person, in character, distilled from the page's **Thesis role + honest verdict**. May carry the page's verified numbers; NEVER an invented one. The persona's charm lives here — pre-empt the obvious question, own the uncomfortable fact. |
| `persona_card.voice` | One or two sentences: who the account is + temperament, derived from how the page actually frames the entity (weary bottleneck, imperial incumbent, forensic tracer…). |
| `persona_card.constraints` | ALWAYS the standard four, verbatim: (1) "Only rewords a source section it is handed; never introduces a fact, number, or ticker that is not in that source." (2) "Describes, never recommends - no buy/sell language, price targets, or bullish/bearish framing." (3) "Preserves every hedge and uncertainty from the source." (4) "Stays in character, but the character never changes the facts." |
| `freshness` | `"research verified <N>d ago"` computed from the page's `last_updated` at export time (display copy; refreshed on re-export). |
| `research_slug` | OMIT in v1 (research-page export is a future addition). |
| `supply_chain` | 2–5 related handles that ALREADY EXIST in kicker's accounts.json (check first — never point at a handle that is not there). |
| `knows` | 3–5 of the page's strongest claims, each `{claim, tier}` — the claims a profile visitor should see. Same scrub + tier rules as sources. |

## Tier mapping (vault source hierarchy → kicker tier chips)

| Vault evidence | Kicker `tier` | `qualifier` example |
|---|---|---|
| Tier 1 (10-K/10-Q/20-F/8-K, official-sector docs) | `solid` | `from the 10-K` |
| Tier 2 (earnings call, company statements) | `solid` | `from the earnings call` |
| Tier 3 (analyst/independent research, vault deep-research) | `needs` | `estimate` / `independent analysis` |
| Tier 4 (reliable news) | `needs` | `reported, not yet filed` |
| Contested / conflicting evidence | `disputed` | — |
| Page Open questions | `open` | — |

## Source sections (the reservoir — where most of the value is)

For each page export **2–5 sections**, chosen for post-worthiness (the striking, self-contained facts — concentration numbers, lead times, sole-producer claims, pre-registered falsifiers, open questions):

- `id`: `src-<handle-without-@, lowercase>-<kebab-topic>` (e.g. `src-haleu-fuel-enrichment-monopoly`).
- `section_title`: short plain title.
- `body_text`: a faithful plain-language rewrite of the page's verified facts — **every hedge preserved, no number invented, no claim strengthened**. 3–8 sentences. This text is what the engine hands models, so it must stand alone (no pronouns pointing outside it).
- `tier` + `qualifier` per the mapping table.
- `vault_ref`: human breadcrumb, `"<PAGE> <source-type> / <topic>"` (e.g. `"HALEU chokepoint page / enrichment capacity"`).

**The attribution rule (authoring-time, non-negotiable):** every fact in a source must be truthfully assertable BY that account in first person. A company account holds only ITS OWN facts (its revenue, its filings, its customers). Facts about a relationship or system (A is B's only customer; the bond that ties them) belong to a **theme/chokepoint** account that speaks in third person — or to the OTHER company whose fact it actually is. This is the defect class kicker's `engine:audit-sources` exists to catch; author so it never fires.

## Scrub rules (what may never cross the bridge)

1. No `[[wikilinks]]` — replace with plain names.
2. No vault notation: "Section N.N", "Tier 1/2/3" (as jargon — map to the kicker tier instead), "CLAUDE.md", "canonical", file paths (`raw/`, `wiki/`), session/log references.
3. Plain language throughout (the vault's own plain-language word list applies: bottleneck not chokepoint where it reads better, "backs up" not "corroborates", etc. — audience knows NO vault terms).
4. Describe-don't-recommend: no buy/sell, price targets, bullish/bearish, position language. ("sell-side analysts" as a noun is fine.)
5. No P&L, no valuation multiples, no price levels.
6. Nothing whose only support is a proprietary/paywalled source.

The merge script enforces the mechanical subset of these with regex checks and refuses to merge on violations.

## Process

1. **Resolve + read the page.** Confirm it exists under `wiki/companies|chokepoints|themes/`. Note `last_updated`; if >90 days stale, tell the user and ask whether to proceed or refresh first.
2. **Draft the export** as a staging JSON file at `/tmp/publish-ticker-<page>.json`:
   `{"accounts": [ {…} ], "sources": [ {…}, … ]}` — shapes exactly per the mappings above.
3. **Dry-run the merge:** `python3 .claude/skills/publish-ticker/scripts/publish_ticker.py /tmp/publish-ticker-<page>.json --dry-run` — review the scrub report and ADD/UPDATE summary.
4. **Merge:** same command without `--dry-run`. The script upserts into kicker's two content files (never touches other entries) and pretty-prints consistently.
5. **Report to the user:** what was exported (account + N sources, tiers used), the scrub/attribution notes, and the kicker-side next steps — review `git diff content/` in kicker-app, then `pnpm validate-content && pnpm engine:audit-sources && pnpm db:seed` (or hand those to the kicker agent). For a **new company** account, also remind: (a) run `/ceo-persona <TICKER>` for the voice card, and (b) add the logo at kicker's `public/avatars/<TICKER>.png` (square PNG, ≥400×400, exact-case filename) — the feed shows a monogram tile until it exists; kicker's `/check-accounts` reports it as LOGO MISSING. Remind once: git on both repos stays the user's.

## Disciplines

- **Honest-verdict travels with the content.** If the page's best fact is hedged, the source text carries the hedge. The persona may be charming; it may not be more certain than the vault.
- **The persona bio is the ONLY place personality gets facts** — and only page-verified ones. Sources are voice-neutral; voice is applied at generation time.
- **Never pad.** A page with 2 strong publishable facts exports 2 sources, not 5.
- **Re-export is an upsert.** After a vault refresh, run the skill again: sources update in place (same ids where the topic persists), freshness bumps, the diff shows exactly what changed.

## What this skill is NOT

- Not a committer (either repo). Not a kicker-app builder (the app's schemas/gates are the kicker agent's).
- Not a research tool — it exports what the vault has already verified; it never adds analysis.
- Not a bulk auto-publisher: one page per run, user reviews every diff. Batches are sequential runs.
- Not a research-page exporter (wiki_pages/full research content) — v1 is accounts + sources only; flag research-page export as a future extension when the user asks.
