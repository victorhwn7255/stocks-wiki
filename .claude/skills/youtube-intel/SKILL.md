---
name: youtube-intel
description: Analyze a YouTube video (or several) into a vault-aware intelligence note for the stocks-wiki vault. Pulls the transcript with yt-dlp, classifies the source by Tier (YouTube is Tier 3 independent analysis at best, Tier 5 social at worst), extracts every named ticker / claim / number with per-speaker attribution, cross-references the existing vault pages (companies / chokepoints / themes / trackers / relationships) + three theses + three frameworks + the prior video-intel corpus, and surfaces concrete primary-source verification leads + tracker signals. DISCOVERY-ONLY — it never edits _thesis*, frameworks*, or any wiki page; it generates questions, tracker signals, and ingest leads, not canon.
---

# youtube-intel — turn a YouTube video into vault-aware intelligence

This skill converts a YouTube video into a structured intelligence note for the **stocks-wiki** vault. The user watches a lot of YouTube; this makes that watching a searchable, vault-aware, **self-compounding** research feed **without** letting low-tier video content leak into the canonical pages.

## The hard boundary (read first — this is the whole point)

YouTube sits at the **bottom of the vault's source hierarchy** (CLAUDE.md Section 2.2): independent analyst commentary is **Tier 3** ("cite, don't treat as fact"); a hype/reaction/influencer video is **Tier 5** social ("signal for generating questions; never cited"). Either way it is **never ground truth**.

Therefore this skill is **discovery-only**. It MUST NOT, under any circumstances:
- edit `wiki/_thesis.md`, `wiki/_thesis-defense-drones.md`, `wiki/_thesis-humanoid-robot.md` (human-owned anchors),
- edit any `raw/notes/frameworks*.md` (human-owned),
- edit, create, or delete any page under `wiki/` — `companies/`, `chokepoints/`, `themes/`, **`trackers/`**, or `relationships/`,
- touch `index.md`, `log.md`, `refresh_log.md`, or `conventions-ledger.md`.

**Tracker note (v10.0).** The `wiki/trackers/` folder — currently seven: `forward-edge-tracker`, `what-could-go-wrong`, `hyperscaler-capex`, `china-exposure`, `AI-credit-spread-watch`, `short-interest`, `forward-pe-watch` (verify against the folder — it grows) — is **status-bearing canon** (CLAUDE.md Section 3.20). This skill **reads and flags** trackers (the Tracker-signals block below is the highest-value output); it **never edits** them — a status change goes through a human-gated propagation, not here. The `layer` page type was **retired at v10.0** (no `wiki/layers/` exists).

It produces exactly two write artifacts: (1) the **intel note** under `raw/notes/video-intel/`, and (2) a one-line append to the **`raw/notes/video-intel/_index.md`** registry (Step 6). Plus a short chat summary. Anything that should actually reach a vault page goes through the **normal primary-source-verified ingest**, human-gated (the two-stop protocol), in a *separate* action the user explicitly asks for. The skill's job is to tell the user *what to go verify*, not to verify it or write it down as fact.

## When to use

- The user pastes one or more YouTube URLs and wants analysis / a transcript.
- The user invokes `/youtube-intel <url> [url2 ...]`.
- A vault task would benefit from mining a specific video the user names.

Do **not** use this skill to do broad web search across many videos — that is what `/last30days` is for. This skill is for **specific named videos**.

## Inputs

One or more YouTube URLs (watch links, `youtu.be` short links, or shorts). Optional user direction on output depth: "full transcript + analysis" vs "analysis + key quotes only" (default: analysis + key quotes, transcript saved to file).

## Step 1 — Preconditions

- `yt-dlp` must be on PATH (`command -v yt-dlp`). If missing, tell the user to run `brew install yt-dlp` and stop.
- Resolve a Python 3 interpreter for the cleaner (`python3`).
- Ensure the save dir exists: `raw/notes/video-intel/` (relative to the vault root). `mkdir -p` it.
- Ensure the registry exists: if `raw/notes/video-intel/_index.md` is missing, create it with the header block (see Step 6). It is appended to at the end of every run.

## Step 2 — Fetch captions + metadata (no video download)

For each URL, run a few cheap calls. **Never download the video itself** — captions + metadata only. **Clear the scratch dir first** so a crashed prior run can't leave a stale `.vtt` that the cleaner then auto-picks:

```bash
OUT="raw/notes/video-intel/.work"
rm -rf "$OUT"; mkdir -p "$OUT"
```

Metadata (title, channel, dates, counts — and the **description + chapters**, which carry disclosures / sponsor tags / guest firm that feed the Tier call in Step 4):
```bash
yt-dlp --skip-download --no-warnings \
  --print "%(id)s\t%(title)s\t%(channel)s\t%(uploader_id)s\t%(upload_date)s\t%(duration_string)s\t%(view_count)s\t%(like_count)s" \
  "<URL>"
yt-dlp --skip-download --no-warnings --print "%(chapters)s" "<URL>"     # [] if none
yt-dlp --skip-download --no-warnings --print "%(description).400s" "<URL>"  # disclosures / sponsor / links
```

Captions (English first, Chinese fallback). Keep the native `.vtt` — the cleaner consumes `.vtt` directly, so do NOT use `--convert-subs` (it needs ffmpeg and adds a failure point):
```bash
yt-dlp --skip-download --no-warnings \
  --write-subs --write-auto-subs \
  --sub-langs "en.*,en,zh-Hans,zh-Hant,zh" \
  -o "$OUT/%(id)s.%(ext)s" \
  "<URL>"
```

Handle these cases explicitly:
- **No captions at all** (no `.vtt` written): report "this video has no captions available" for that URL and skip to the next. Do not fabricate a transcript. (Optionally offer the user that you *could* download audio and transcribe, but that is a heavier, separate opt-in — do not do it automatically.)
- **Transient `HTTP 429 Too Many Requests`**: YouTube rate-limit from repeated yt-dlp calls. The English track usually still downloads before the limit hits a later language; if a needed track 429s, wait a moment and retry just that URL. Not a skill bug.
- **No-caption fallback (opt-in, esp. Chinese videos)**: if a video has NO caption track and a transcript is essential, a local speech-to-text tool can transcribe (and translate) the audio. Only do this if the user has a Whisper tool installed AND asks for it — it is heavier (downloads audio, runs a model, minutes not seconds). On Apple Silicon the fast option is `mlx-whisper` via `uvx`; it transcribes Chinese audio and can translate to English in one pass. Pattern: `yt-dlp -x --audio-format mp3 -o "$OUT/%(id)s.%(ext)s" "<URL>"` then `uvx mlx-whisper "$OUT/<id>.mp3" --language zh --task translate --output-dir "$OUT"` (drop `--task translate` to keep the original Chinese; ffmpeg required, present). Treat the result as an even lower-confidence transcript than auto-captions.
- **Chinese-only captions**: proceed; note in the output that the transcript is auto-translated from Chinese and carries extra transcription/translation uncertainty.
- **Members-only / age-restricted / private**: yt-dlp will error; report it plainly.

## Step 3 — Clean the transcript

Run the bundled cleaner on the **scratch directory** — it picks the best caption file itself (manual English first, Chinese last) so the shell never has to glob (brittle under zsh). The cleaner strips the WEBVTT header, timestamps, inline word-timing tags, and the rolling-duplicate lines auto-captions produce, then reflows into paragraphs:
```bash
python3 .claude/skills/youtube-intel/scripts/clean_subs.py "$OUT" > "$OUT/clean.txt"
```
Read `clean.txt`. This is the working transcript. If the cleaner reports "no .vtt/.srt caption file in directory", treat it as the no-captions case (Step 2).

**Chinese-language videos — prefer the original track and translate it yourself.** The dir auto-pick favors English, which for a Chinese-spoken video means a YouTube *auto-translated* `en` track (machine-translation of a transcript — doubly lossy). If the video is spoken in Chinese, instead pass the **original** `zh-Hans`/`zh-Hant` file explicitly and translate it during analysis (your translation beats YouTube's MT):
```bash
python3 .claude/skills/youtube-intel/scripts/clean_subs.py "$OUT/<id>.zh-Hans.vtt" > "$OUT/clean.txt"
```
Then in the analysis, render claims in English but keep the **original Chinese for every company name, ticker, and key phrase** in parentheses (e.g. "Sanhua (三花智控)") — Chinese names are exactly what auto-captions and MT mangle, so preserving the source characters lets a name be verified rather than guessed.

## Step 4 — Classify the source by Tier (mandatory)

Before analysing content, judge what kind of source this is and state it. Use the **channel + description + guest credentials** (pulled in Step 2) to make the call:
- **Tier 3 (independent analysis)** — an independent analyst / research channel reasoning from public data. Usable as "cite, don't treat as fact."
- **Tier 5 (social)** — reaction, hype, influencer, promotional, or anonymous-tip content. "Generates questions; never cited."
- **Aligned commercial incentive** — if the channel is talking its own book, sponsored, pumping a ticker, or is company IR, flag it explicitly per CLAUDE.md ("skip promotional content and aligned commercial incentive"). Promotional content gets a short, skeptical note, not a full work-up.
- **Incentive lean (within Tier 3).** Even a top analyst carries a lean — disclosed positions, a live ratings book, a fund's holdings. Name it (the strongest notes do: "guest owns NVDA; talking his ratings book"). The lean does not demote the Tier; it calibrates which claims to discount.

The Tier verdict gates how much weight every downstream claim gets.

## Step 4.5 — Corpus cross-check (do this BEFORE writing the analysis)

The point of the feed is that it **compounds** — a video is never analysed from a blank slate. Before writing, grep the existing notes for the names and big claims this video makes:
```bash
grep -ril "<ticker-or-name>" raw/notes/video-intel/ | grep -v "$(basename <this-note>)"
```
For each prior note that covers the same entity or claim, surface **what our own video feed has already said, and whether this video AGREES or DISAGREES.** Two Tier-3 sources disagreeing on the same fact is the single highest-value open-question signal — it is exactly what should become an ingest lead. (Reference: the Rasgon note's Broadcom-custom-silicon claim ran *against* Jensen's "Anthropic = ~100% of TPU growth" from the earlier Dwarkesh note — that cross-video tension is the gold the feed exists to surface.) Record the result in the **Cross-video corpus check** section (Step 5).

## Step 5 — Analyze into the intel note

Cross-reference the vault as you go: for every company/ticker the video names, check whether a page exists (`grep -i "<ticker>" index.md` or look under `wiki/companies/`), and which chokepoint / theme / **tracker** / relationship pages it touches. Use the **three theses** (AI-datacenter, Defense & Drones, Humanoid Robots) as the evaluation point (does this **strengthen / challenge / refine** a thesis, or is it off-thesis noise?), and place any new chokepoint candidate on the **chokepoint-quality gradient** (Framework 12: geology/physics > precision-manufacturing > policy).

The note has a **fixed spine (always present)** plus **conditional blocks that appear only when the video earns them** — a hype video with no signal collapses to the spine + "no real signal" and stays short (honest-verdict discipline); a dense podcast lights up every conditional block.

**Note template (top → bottom):**

**1. Frontmatter** *(always)* — YAML for corpus queryability:
```yaml
---
type: video-intel
source_tier: 3                 # 3 or 5
channel: "Steve Eisman"
guest: "Stacy Rasgon (Bernstein)"
upload_date: 2026-06-08
url: https://www.youtube.com/watch?v=...
entities: [NVDA, AVGO, AMD, INTC, MU]      # named AND has a vault page
new_names: [QCOM, ASML, LRCX, KLAC]         # named, NO vault page yet
trackers_touched: [hyperscaler-capex, what-could-go-wrong, forward-edge-tracker]
headline: "one-line core finding in plain language"
---
```

**2. Header** *(always)* — title, channel, guest, upload date, duration, view/like counts, URL.

**3. Source-tier verdict** *(always — placed at the top because it gates everything)* — the Tier call from Step 4 + the incentive lean, in a sentence or two.

**4. TL;DR** *(always)* — 3-5 lines: the video's core thesis in plain language.

**5. Named entities** *(always)* — a table, one row per ticker/company:

| Entity | Speaker | Claim in video | Vault relation | Page? |
|---|---|---|---|---|

  - **Speaker** = who made the claim (load-bearing in multi-guest formats — a host who owns the stock vs a neutral analyst vs a guest talking his book carry different weight).
  - **Vault relation** = confirms / challenges / adds / off-thesis.
  - **Page?** = `[[TICKER]]` if a page exists, plain text if not.
  - End the table with an **auto-caption garble line** flagging every name/number that reads like a transcription error (esp. Chinese names + tickers — "Sanhua" misheard as "son hua", "Tuopu" as "two pu") so a misheard name is never taken as fact.

**6. Key claims + numbers** *(always)* — bulleted, grouped by speaker or by segment, each:
  - **attributed to the speaker** (mandatory),
  - tagged `[verifiable]` (checkable against a 10-K/10-Q/20-F/earnings call/8-K) · `[opinion]` (the speaker's read) · `[forward]` (speculative/future),
  - timestamped `(~HH:MM)` where useful.
  - For the **3-5 most load-bearing or most surprising claims, include a verbatim quote** with timestamp — a quote is more verifiable and makes a better ingest lead than a paraphrase. Paraphrase the rest in plain language.
  - **Every number heard in audio is soft**: render with `~` and a verify tag by default; never quote a spoken number as exact.

**7. Cross-video corpus check** *(when prior notes touch these entities — from Step 4.5)* — what the vault's own video feed has already said about these names/claims, and whether this video **agrees or disagrees**. Disagreements become ingest leads.

**8. Vault cross-reference** *(always — a 5-type checklist so no page-type is skipped)* — walk: **company → chokepoint → theme → tracker → relationship**. For each touched page, tag **confirms / challenges / adds**, name it with `[[wikilinks]]` only when it exists. (Trackers get only a pointer here — their detail lives in block 9.)

**9. Tracker signals** *(required — consider EVERY tracker in `wiki/trackers/` [seven at last count]; output the ones touched, one line "No tracker signals" if none)* — discovery-only flags, never edits:
  - **[[forward-edge-tracker]]** — what **consensus narrative** does this video represent (a YouTube video *is* the Tier-3/4 consensus), and where does the vault's primary-grounded view **diverge**? That is exactly a forward-edge "Consensus vs Vault view" pair.
  - **[[what-could-go-wrong]]** — any **tripwire event** ("Meta cut capex" = a fired tripwire) or a new **tripwire candidate** (e.g. the Burry depreciation short)? A fired tripwire is a calibration event (block 13 footer).
  - **[[hyperscaler-capex]]** — the watch numbers (e.g. GOOGL $180B / AMZN $220B / META $135B), each tagged "verify vs guidance."
  - **[[china-exposure]]** / **[[AI-credit-spread-watch]]** — any signal that moves these.
  - **[[short-interest]]** / **[[forward-pe-watch]]** — crowd-positioning claims about a vault name, or index-level valuation/EPS-revision claims (a "market is at X× forward earnings" line is a dial cross-check, never a fact).

**10. Framework & chokepoint placement** *(when a chokepoint / new-name candidate surfaces)* — place any new chokepoint candidate on the **chokepoint-quality gradient** (geology/physics > precision-mfg > policy) and flag it for `/chokepoint-eval`. State the thesis verdict: **strengthens / challenges / refines** which of the three theses, or off-thesis.

**11. Ingest leads** *(always — the payoff)* — concrete, **primary-source-verifiable** follow-ups, e.g. *"Claims Sanhua received a $685M Optimus order (Oct 2025) → verify in Sanhua H-share filing + any Tesla 8-K → [[SANHUA]] refresh."* Include any **new-name candidates** that might cross the page-creation threshold (3+ sources / chokepoint-central).

**12. Vault blind spots / coverage gaps** *(when the video exposes one)* — names the video raised that the vault **does not cover despite a framework slot for them** (e.g. ASML / Lam / KLA / AMAT with no pages despite the `equipment_tier` framework). This is a `/connection-finder` lead — surface it rather than letting it pass.

**13. Contradictions / red flags** *(when any exist)* — where the video conflicts with vault findings, shows promotional incentive, or makes an unsupported leap.

**14. Self-learning hand-offs** *(always — footer routing so the feed flows into the loop)* — explicit next-skill routing:
  - new ticker cluster with no page → `/connection-finder`
  - new chokepoint candidate → `/chokepoint-eval`
  - a fired tripwire / catalyst event → `/calibration-check`
  - an ingest-ready name → the normal human-gated two-stop ingest
  - one-line restated tier verdict: "Tier 3/5 — do not cite as vault fact; verify against primary sources before any page edit."

**15. Transcript appendix** *(always)* — see Step 6.

Disciplines to apply throughout (same as the vault's):
- **Honest-verdict** — if the video is hype with no real signal, say so plainly and keep the note short (spine only). Don't manufacture relevance or light up conditional blocks that have nothing in them.
- **Describe-don't-recommend** — no buy/sell. Reframe "should I buy X" into "what would have to be true." No price targets, position sizes, or valuation calls.
- **Plain language** in the chat summary (the user prefers simple words); vault voice only inside any *proposed* page content (which this skill does not write anyway).
- **Auto-caption caveat** — never treat a transcript number/name as exact; flag anything that reads as a transcription error.

## Step 6 — Save the note + append to the registry

**(a) Save the note.** Write the full note (frontmatter → analysis → transcript) to:
```
raw/notes/video-intel/<UPLOAD_DATE>_<channel-slug>_<title-slug>.md
```
- `<UPLOAD_DATE>` = the video's `upload_date` (YYYY-MM-DD); fall back to today's date if unknown.
- Slugs: lowercase, hyphenated, ASCII, trimmed to ~40 chars.
- Put the **full cleaned transcript** at the bottom under `## Transcript (Tier 3/5 — not a primary source)` so it is greppable later, but keep the **analysis at the top**.
- Then clean up the scratch dir: `rm -rf raw/notes/video-intel/.work`.

**(b) Append one row to the registry.** Add a single line to `raw/notes/video-intel/_index.md` (create the file with this header if it does not exist):
```
# video-intel registry (Tier 3/5 — NOT vault canon)

Append-only, newest at bottom. One row per /youtube-intel run. Lets the corpus be queried
as a feed (recurring claims, consensus drift, what we've said about a name) without grepping
every note. Not in index.md / log.md — does not count for accounting (like refresh_log.md).

| Date | Channel / guest | Tier | Entities | Trackers | Headline |
|---|---|---|---|---|---|
```
Row format: `| 2026-06-08 | Eisman / Rasgon (Bernstein) | T3 | NVDA AVGO AMD MU INTC | hyperscaler-capex, what-could-go-wrong | NVDA lags on constraint-rotation; AI ROI is the only real risk |`

A **recurring claim across rows** (e.g. "power is the binding constraint" in 6+ videos) is itself a consensus signal worth calling out in the chat summary and, if strong, as a `/connection-finder` lead.

`raw/notes/video-intel/` is a Tier-3/5 intel log, **not** vault canon and **not** in `index.md`/`log.md` — its files (notes + registry) do not count for accounting, exactly like `refresh_log.md` and `conventions-ledger.md`.

## Output to the user (chat)

Lead with the **Tier verdict + TL;DR**, then the **named-entities** read, then the **tracker signals + ingest leads** (the actionable part), then any **cross-video tension** or **blind spot** worth flagging, then where the note was saved. Keep it scannable and plain-language. End by reminding (once) that this is discovery-only — nothing touched the vault pages, and naming what to verify is the deliverable.

## Long-form videos (podcasts, 1h+)

Captioned long videos are fully supported — caption fetch and cleaning are length-independent. A 2-hour video is ~18-20k words (~25-30k tokens); read all of it, do not sample. What changes is the analysis shape:

- **Segment-by-segment extraction (do not single-pass a long transcript).** A single linear read over a 2-hour file misses claims. Pull chapter markers if present:
  ```bash
  yt-dlp --skip-download --no-warnings --print "%(chapters)s" "<URL>"
  ```
  If the creator added chapters, work **one segment at a time** — extract that segment's claims + entities before moving on — then merge into the Key-claims block. If there are no chapters, segment by topic shift yourself. For a very long, dense video, you may fan out one sub-agent per chapter to extract in parallel, then merge the results (and dedupe) — but the merged note still follows the one Step-5 template.
- **Extract signal, do not recap.** The deliverable for a long podcast is the 8-15 claims/entities that matter, each with an approximate timestamp so it is jump-to-able — never a linear minute-by-minute summary.
- **Timestamps are load-bearing here.** Tag every claim and named entity with `(~HH:MM)` so the user can verify the moment in a 2-hour file.
- **No-caption long videos are the heavy path.** Whisper on 2 hours of audio is 10-30+ minutes plus an audio download — only take that path on explicit user request (Step 2 fallback). Podcasts almost always have captions, so this is rare.
- The saved MD file's appended transcript will be large; that is fine (it is a greppable log). Keep the full transcript, not a trimmed one.

## What this skill is NOT

- Not a way to add YouTube claims to the vault directly (that violates the source hierarchy).
- Not a broad multi-video search (use `/last30days`).
- Not a video downloader — captions + metadata only.
- Not a tracker editor — it *flags* tracker signals; a status change is a separate human-gated propagation.
- Not a buy/sell recommender.
