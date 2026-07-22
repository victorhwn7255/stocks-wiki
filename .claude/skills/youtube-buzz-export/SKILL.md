# youtube-buzz-export — turn recent video-intel into @youtube-buzz tweets

This skill is the bridge that feeds Ticker's **@youtube-buzz** account: it takes the
finance-video commentary the vault has captured over the **last 15 days** (the
`raw/notes/video-intel/` corpus) and turns the high-signal bits into attributed,
de-hyped, tweet-ready **source sections** in kicker-app — each one linking straight to
the source video so a reader can check the footage. @youtube-buzz is the vault's one
deliberately-different account: every other Ticker account rewords a filing-grade
primary fact; this one reworks what the smart-money commentariat *said on camera*, and
says so plainly (no confidence pill — the receipt is the video).

## The hard boundary (read first)

This skill is **discovery -> feed**, never canon. It MUST NOT:
- edit ANY `wiki/` page, `_thesis*`, `frameworks*`, `index.md`, `log.md`, `refresh_log.md`, or the video-intel notes themselves,
- treat video content as fact (it is Tier 3/5 — "signal for questions, never cited as truth"); the tweets are **reported speech**, always attributed, never asserted as the vault's own finding,
- add buy/sell / price-target / bullish-bearish language, or brag that someone "called it right".

It writes in exactly two places, both outside canon: (1) a **staging JSON** under `/tmp/`, and (2) via the existing `publish-ticker` merge, kicker-app's `content/sources.json` (SOURCES ONLY — the @youtube-buzz **account/persona is maintained directly in kicker `content/accounts.json`**, not emitted here). Seeding the DB (`pnpm db:seed`) is a **separate, human-gated** kicker step.

## When to use

- `/youtube-buzz-export` — refresh @youtube-buzz's reservoir after new video-intel notes have been saved (the normal cadence: Vic watches videos -> `/youtube-intel` saves notes -> this skill -> seed).
- Optional args: `--days N` (window, default 15), `--today YYYY-MM-DD` (pin the "now" for a reproducible run).

## Inputs

None required. The content comes from `raw/notes/video-intel/`. The account already exists in kicker (`@youtube-buzz`, kind `theme`, `maxDaily: 6`).

## Step 1 — Harvest the in-window notes (deterministic)

```bash
python3 .claude/skills/youtube-buzz-export/scripts/youtube_buzz_harvest.py --json
```
It returns, for every video-intel note whose `upload_date` is within the window AND that carries a `url:` header, the `channel`, `guest`, `url`, `headline`, and the note's own curated `TL;DR` + `Key claims` sections. Notes with no URL are reported under `skipped_no_url` (no receipt -> not eligible). Read the JSON.

**If `in_window_count` is 0: STOP.** Emit nothing and tell Vic "@youtube-buzz stays silent — no video-intel in the last {N} days (auto-pause)." This is correct behaviour ("when the tape's quiet, so are we"); the kicker engine's own `source_date` window also keeps the account quiet, so there is nothing to do.

## Step 2 — Rolling cross-note synthesis (the editorial pass)

Read across the in-window notes and pick the highest-signal items. This is what makes the account *insightful* rather than a per-video parrot. Prefer, in order:
- **Convergence** — the same claim from **two or more channels** (e.g. several desks flagging the hyperscaler capex-vs-ROI question). These are the strongest scorekeeper material: "three desks, one worry."
- **Disagreement** — two sources taking **opposite** reads (e.g. one desk says the spenders de-rate, another says the shortage prevents an overbuild). These become a **two-chip "watch both sides"** tweet.
- **Sharp single-source calls** — one named voice making a specific, checkable, non-obvious point.

Do NOT lean on `_consensus.md` — it is a periodically-seeded digest and is usually stale relative to the 15-day window (it will not cover the recent notes). If it happens to overlap the window, use its A/B/C framing as a prior only. Base the synthesis on the **raw in-window notes** the harvester returned. If `_consensus.md`'s newest entry predates the window, mention that to Vic once as a heads-up (a `/youtube-intel` consensus refresh is a separate, optional task) — it never blocks this run.

Aim for **~6-12 source sections** across the window — a reservoir deep enough to feed several days without the engine recycling. Each section is ONE distinct take; never two sections on the same claim.

## Step 3 — Draft each in the scorekeeper voice (generate)

For each selected item, write a `body_text` of ~140-600 characters (the engine reads THIS and rewords it into the final tweet, so write it already tweet-shaped and clean). The voice is **the deadpan scorekeeper's desk** — speaks as "we", dry and unimpressed, reads the commentariat like a box score:
- **Attribute at institution/speaker level**, always: "GS's flow desk", "JPM-AM's Cembalest", "DataTrek", "Baker (Atreides)". It is what *they* said, not what we conclude.
- **Keep every hedge** the source kept ("may", "starting to", "if", "so far"). Never upgrade a maybe to a fact.
- **Report the substance, not the label.** If a speaker "is bullish", say what they claimed (the mechanism/number), never the word "bullish".
- **Let a disagreement stand** as a disagreement; don't pick a winner or add a prediction of our own.
- **Never crow.** No "nailed it", no "called it right", no scorekeeping-as-prophecy.
- No tickers/numbers/names that are not in the note. No hashtags, no emoji, no @-handles.

For adversarial robustness (the DDOG-fabrication lesson), draft with a **generate -> verify** loop — ideally N parallel drafters then per-item verifiers via a Workflow, or at minimum draft then self-critique each. **The verifier is not optional** — it is the gate that has caught fabricated numbers and stripped hedges before.

## Step 4 — Adversarially verify each (the gate)

Check every draft, fail-closed (rewrite or drop on any fail):
1. **Grounded** — every fact/number/name/date traces to the backing note (no invention; a value must sit inside any range the note gives).
2. **Attributed** — the claim is tied to who said it; it never reads as the vault's own finding.
3. **Hedges preserved** — the source's uncertainty survived.
4. **No advice** — no buy/sell/hold, no price target/level, no bullish/bearish/overweight/underweight, no "should".
5. **No brag** — nobody is framed as having called it right; no added prediction.
6. **Receipt present** — 1-3 `video_links`, each the actual source video URL from the note(s) the claim came from (a disagreement tweet carries both).
7. **Clean of vault-internal vocab** — no `[[wikilinks]]`, no "the page/vault/canon/feed", no "Tier N", no file paths.

## Step 5 — Assemble the staging JSON (sources only)

Write `/tmp/publish-ticker-youtube-buzz.json` = `{ "sources": [ ... ] }`. Each source:

```json
{
  "id": "src-yt-<kebab-topic>",
  "account": "@youtube-buzz",
  "section_title": "<a short human title, e.g. 'The spender de-rating'>",
  "body_text": "<the attributed, scrubbed, scorekeeper-voice take>",
  "tier": "open",
  "qualifier": "video commentary - not a filing",
  "vault_ref": "video-intel: <channel>, <date>",
  "source_date": "<the note's upload_date, YYYY-MM-DD>",
  "video_links": [ { "channel": "<channel name>", "url": "<video url>" } ]
}
```
Rules that keep the merge clean:
- **`tier` is always `"open"`** — it is never displayed for this account (PostCard renders the ▶ video chips instead of the pill), but the kicker schema requires a tier; `open` is the honest neutral.
- **`vault_ref` is a human label, NEVER a path** — `raw/...`/`wiki/...` paths are blocked by the merge scrub; the real link lives in `video_links`.
- **`source_date` = the backing note's `upload_date`** (the harvester's `date`). This is what the engine's 15-day window filters on, so a stale reservoir silently ages out.
- **`video_links`**: 1-3, one per source video actually used. For a convergence take, link the strongest 1-2; for a disagreement take, link **both** sides.
- **`id`**: stable `src-yt-<kebab>` so re-runs upsert (never duplicate).

## Step 6 — Dry-run merge, review, then merge

```bash
python3 .claude/skills/publish-ticker/scripts/publish_ticker.py /tmp/publish-ticker-youtube-buzz.json --dry-run
```
The merge re-scrubs every field (buy/sell, price-target, sentiment, wikilinks, vault jargon, internal paths) and validates shape incl. `source_date`/`video_links`. Fix any ERROR and re-run until clean. A WARN naming a bank/desk (e.g. "J.P. Morgan") is expected here — institution attribution is the point — and does not block; sanity-check it is genuine attribution, not a leaked proprietary detail. Then drop `--dry-run` to write `content/sources.json`.

Report to Vic: how many sources added/updated, the convergence/disagreement split, and the two remaining **human-gated** steps that are HIS: review `git diff content/`, then `pnpm validate-content && pnpm db:seed`. Never run git or `db:seed`.

## What this skill is NOT

- Not a way to put video claims into canon (that is the human-gated primary-source ingest; this only feeds the feed).
- Not the account/persona author — the @youtube-buzz persona lives in kicker `content/accounts.json`; this emits sources only.
- Not a buy/sell recommender, and not a "who called it right" scoreboard.
- Not a `_consensus.md` refresh (it reads the raw in-window notes; a consensus rebuild is a separate `/youtube-intel`-side task).
