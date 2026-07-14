---
name: ceo-persona
description: Build a company Ticker account's voice from its REAL earnings-call transcripts — analyze the CEO/CFO's tone, vocabulary, cadence, and Q&A behavior in raw/transcripts/<TICKER>/, distill a voice card, and write the voice into the kicker-app account's persona_card so the account tweets in its management's register (e.g. @NVDA sounds like Jensen Huang). Use when the user asks to "/ceo-persona <TICKER>", "give <TICKER> its CEO voice", "make NVDA tweet like Jensen", "re-voice <TICKER>", or as the voice step inside a company /publish-ticker export. Input is one ticker with a vault page.
---

# ceo-persona — excavate a company account's voice from its earnings calls

Company accounts on Ticker should not sound like a generic finance bot wearing a logo. Every listed company already HAS a voice — its executives perform it every quarter under analyst pressure, and those transcripts sit in `raw/transcripts/<TICKER>/`. This skill extracts that voice fingerprint and installs it in the kicker account's `persona_card.voice`, which is exactly what the tweet engine consumes at generation time. Facts are excavated from the vault page (that's `/publish-ticker`'s job); voice is excavated from the primary record (this skill's job).

## The hard boundary (read first)

- **Transcripts contribute ZERO facts.** This skill mines HOW management speaks, never WHAT it claimed. No number, customer, product, or forward statement moves from a transcript into any account, bio, source, or claim. Facts cross the bridge only via `/publish-ticker`, only from the vault page. (This keeps the ingest source-set discipline intact — the transcript is already part of the page's ingest sources; the skill adds no new factual channel.)
- **Voice-informed, NOT impersonation.** The account speaks *in the register of its management's public calls* — cadence, vocabulary, posture. It never claims to BE the named person, and it never fabricates first-person quotes attributed to a real person. Direct executive quotes may appear in feed content only if they are already page-verified facts exported as sources.
- **The promotional-intensity strip.** Earnings-call voice is structurally bullish (the vault grades it Tier 2, management-colored). Adopt the rhythm and the verbal tics; drop the hype adjectives and superlative stacking. Jensen's cadence survives; "incredible demand" does not. The voice card must include an explicit strip list (which of this speaker's habits to keep, which to drop).
- **The standard four constraints always sit below the voice and always win** — they stay verbatim in every account; "the character never changes the facts."
- **Writes:** vault side — ONLY `raw/notes/voice-cards/<TICKER>.md` (a non-canon note dir, same class as `raw/notes/latest-alpha/`; never in index.md/log.md, no accounting). Kicker side — ONLY via the publish-ticker merge script (`.claude/skills/publish-ticker/scripts/publish_ticker.py`), never by editing kicker's content files directly. Never any other vault file. **Git stays the user's on both repos.**
- **Paywalled transcripts do not cross.** If a call transcript is AI-summary-only or from a proprietary/paywalled source, do not mine it — use the fallback (below).

## When to use

- `/ceo-persona <TICKER>` — standalone: re-voice an existing kicker account.
- As **Step 0 of a company `/publish-ticker` export** (the standard Wave-3+ flow): build the voice card first, then write the full export with the voice already installed — one merge instead of two.
- After a refresh ingest adds a new transcript: re-run to keep the voice current (a CEO change is the obvious trigger).

Do **not** use for: chokepoint/theme accounts (their voice comes from the page's analytical posture, not from any executive); companies without a vault page (account = page is the iron rule); mining transcripts for facts (that is an ingest).

## Process

### 1 — Locate the transcripts

`ls raw/transcripts/<TICKER>/` from the vault root (`/Users/victor_he/Projects/stocks-wiki`). Use the **latest 2 earnings calls**, plus any keynote/investor-day transcript present (a keynote shows the unconstrained register; the earnings Q&A shows the constrained one — the contrast is fingerprint gold).

- **No folder / no usable transcript** → fallback: derive the voice from the vault page's posture (the pre-skill method), and label the voice card `source: page-posture fallback (no transcript)`. Say so in the report.
- PDFs: read with the `pages` parameter. Prepared remarks live in the first ~third; then sample **3–5 Q&A exchanges**, preferring ones where an analyst pushes back — pressure is where the fingerprint is most genuine. Reading every page is unnecessary; ~8–12 pages per call suffices.

### 2 — Extract the fingerprint (fixed dimensions)

Score the speaker(s) on all of these, with 1–2 verbatim micro-examples each (examples live on the voice card only — they never cross the bridge):

1. **Sentence rhythm & length** — clipped vs looping; trains of short declaratives vs nested clauses.
2. **Signature vocabulary & verbal tics** — recurring words, fillers, catchphrase constructions ("the way to think about that is…", "look,…", "okay?").
3. **Metaphor habitat** — where their analogies come from (factories, physics, sports, history).
4. **Pushback behavior** — deflect with charm / answer bluntly / drown in detail / reframe the question.
5. **Bad-news delivery** — fronted, buried, reframed as investment, or owned flatly.
6. **Hedging style** — how uncertainty is voiced ("we don't guide beyond…", ranges, "as we see it today").
7. **Refusals** — what they decline to answer and the refusal formula.
8. **CEO vs CFO split** — CEO carries personality; CFO carries how numbers are spoken. The account is a blend: CEO register for narrative, CFO register for figures.

### 3 — Write the voice card → `raw/notes/voice-cards/<TICKER>.md`

Template:

```markdown
# Voice card — <TICKER> (<Company>)
- built: <YYYY-MM-DD> · source: <transcripts used, with dates> · speakers: <CEO name (CEO), CFO name (CFO)>
- boundary: voice only — zero facts cross from transcripts; not impersonation (register, not identity)

## Fingerprint
(one short block per dimension 1–8, each with a verbatim micro-example)

## Keep / strip (the promotional-intensity filter)
- KEEP: <habits that carry character without hype>
- STRIP: <superlative stacking, hype adjectives, forward-cheerleading — listed concretely for THIS speaker>

## How this voice says things (3–4 sample rewrites)
- Neutral fact: "<a page-style sentence>" → In voice: "<the same fact, same hedges, this register>"
(samples must add no facts and keep every hedge)

## persona_card.voice (the distillation that ships)
"<2–4 sentences — see Step 4>"
```

The card is the durable artifact: richer than what ships, re-usable at every re-export, diffable when a new transcript lands.

### 4 — Distill into `persona_card.voice`

2–4 sentences, written as instructions the tweet engine can follow: who speaks (first person as the company, in its management's register — name the register, not the person as identity), the cadence, 2–3 named verbal habits, the numbers-register (CFO mode), and the strip rule. It must compress the card, not summarize the company.

### 5 — Install into kicker (via the bridge, upsert)

- **Standalone re-voice:** read the account's current entry from `kicker-app/content/accounts.json`, update ONLY `persona_card.voice` (and `bio` phrasing IF the user asked — bio facts stay page-verified), and emit the FULL account object into `/tmp/publish-ticker-<ticker>-voice.json` (`{"accounts":[…], "sources":[]}`) — the merge script upserts whole entries, so the staging object must be complete.
- **Inside a full export:** hand the distillation to the `/publish-ticker` draft; one staging file, one merge.
- Then: `python3 .claude/skills/publish-ticker/scripts/publish_ticker.py <staging> --dry-run` → review → merge → `cd /Users/victor_he/Projects/kicker-app && pnpm validate-content`.

### 6 — Report

Voice card path + the shipped `persona_card.voice` + which transcripts fed it + the keep/strip list, and the reminder that the user reviews the kicker diff and commits himself.

## Disciplines

- **One careful pass, no optimization loop.** Draft the card from the transcripts, smoke-check the samples, ship. Do not iterate the voice through repeated generations.
- **Honest fallback.** No transcript → page-posture voice, labeled as such. Never fake a fingerprint.
- **Distinctness check.** Before shipping, compare against the neighboring company voices in accounts.json — if two accounts would read alike, sharpen what the transcripts actually distinguish.
- **Foreign-language calls** (A-share / EDINET cohort): if the transcript is translated, fingerprint structure and behavior (dimensions 4–8) rather than vocabulary — translation destroys tics but preserves posture. Label the card.
- **Plain language** in chat; the voice card itself may quote the speaker verbatim.

## What this skill is NOT

- Not a fact channel — nothing factual moves from transcript to feed. Ever.
- Not impersonation or parody of a real person — register, not identity; no fabricated quotes.
- Not a chokepoint/theme voicer — those personas come from the page's analytical posture.
- Not a committer (either repo), not a kicker schema editor, not a bulk auto-runner — one ticker per run, user reviews every diff.
