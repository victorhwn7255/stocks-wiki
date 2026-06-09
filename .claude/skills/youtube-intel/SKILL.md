---
name: youtube-intel
description: Analyze a YouTube video (or several) into a vault-aware intelligence note for the stocks-wiki vault. Pulls the transcript with yt-dlp, classifies the source by Tier (YouTube is Tier 3 independent analysis at best, Tier 5 social at worst), extracts every named ticker / claim / number, cross-references the existing vault pages and three theses, and surfaces concrete primary-source verification leads. DISCOVERY-ONLY — it never edits _thesis*, frameworks*, or any wiki page; it generates questions and ingest leads, not canon.
---

# youtube-intel — turn a YouTube video into vault-aware intelligence

This skill converts a YouTube video into a structured intelligence note for the **stocks-wiki** vault. The user watches a lot of YouTube; this makes that watching a searchable, vault-aware research feed **without** letting low-tier video content leak into the canonical pages.

## The hard boundary (read first — this is the whole point)

YouTube sits at the **bottom of the vault's source hierarchy** (CLAUDE.md Section 2.2): independent analyst commentary is **Tier 3** ("cite, don't treat as fact"); a hype/reaction/influencer video is **Tier 5** social ("signal for generating questions; never cited"). Either way it is **never ground truth**.

Therefore this skill is **discovery-only**. It MUST NOT, under any circumstances:
- edit `wiki/_thesis.md`, `wiki/_thesis-defense-drones.md`, `wiki/_thesis-humanoid-robot.md` (human-owned anchors),
- edit any `raw/notes/frameworks*.md` (human-owned),
- edit, create, or delete any page under `wiki/` (company / chokepoint / theme / relationship / layer),
- touch `index.md`, `log.md`, `refresh_log.md`, or `conventions-ledger.md`.

It produces exactly two artifacts: (1) the **intel note** saved under `raw/notes/video-intel/`, and (2) a short summary in chat. Anything that should actually reach a vault page goes through the **normal primary-source-verified ingest**, human-gated (the two-stop protocol), in a *separate* action the user explicitly asks for. The skill's job is to tell the user *what to go verify*, not to verify it or write it down as fact.

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

## Step 2 — Fetch captions + metadata (no video download)

For each URL, run two cheap calls. **Never download the video itself** — captions + metadata only.

Metadata:
```bash
yt-dlp --skip-download --no-warnings \
  --print "%(id)s\t%(title)s\t%(channel)s\t%(uploader_id)s\t%(upload_date)s\t%(duration_string)s\t%(view_count)s\t%(like_count)s" \
  "<URL>"
```

Captions (English first, Chinese fallback). Keep the native `.vtt` — the cleaner consumes `.vtt` directly, so do NOT use `--convert-subs` (it needs ffmpeg and adds a failure point):
```bash
OUT="raw/notes/video-intel/.work"   # scratch; cleaned text is what we keep
mkdir -p "$OUT"
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

Before analysing content, judge what kind of source this is and state it:
- **Tier 3 (independent analysis)** — an independent analyst / research channel reasoning from public data. Usable as "cite, don't treat as fact."
- **Tier 5 (social)** — reaction, hype, influencer, promotional, or anonymous-tip content. "Generates questions; never cited."
- **Aligned commercial incentive** — if the channel is talking its own book, sponsored, pumping a ticker, or is company IR, flag it explicitly per CLAUDE.md ("skip promotional content and aligned commercial incentive"). Promotional content gets a short, skeptical note, not a full work-up.

The Tier verdict gates how much weight every downstream claim gets.

## Step 5 — Analyze into the intel note

Cross-reference the vault as you go: for every company/ticker the video names, check whether a page exists (`grep -i "<ticker>" index.md` or look under `wiki/companies/`), and which theme/chokepoint pages it touches. Use the three theses as the evaluation point (does this **strengthen / challenge / refine** a thesis, or is it off-thesis noise?).

Produce this structure (in the saved note and, condensed, in chat):

1. **Header** — title, channel, upload date, duration, view/like counts, URL, and the **Tier verdict** from Step 4.
2. **TL;DR** — 3-5 lines: the video's core thesis in plain language.
3. **Named entities** — a table of every ticker/company mentioned × the claim made about it × whether a **vault page exists** (`[[TICKER]]` if yes, plain text if no). Flag any name that looks **garbled by auto-captions** (esp. Chinese names + tickers — e.g. "Sanhua" misheard as "son hua", "Tuopu" as "two pu") so a misheard name is never taken as fact.
4. **Key claims + numbers** — bulleted, with approximate timestamps where useful, each tagged:
   - `[verifiable]` — could be checked against a 10-K/10-Q/20-F/earnings call/8-K,
   - `[opinion]` — the speaker's read/projection,
   - `[forward]` — speculative/future-looking.
5. **Vault cross-reference** — which existing pages/themes/chokepoints this touches; for each, whether it **confirms / challenges / adds to** the relevant thesis, or is **off-thesis**. Name the pages with `[[wikilinks]]` only when they exist.
6. **Ingest leads** — the payoff. Concrete, **primary-source-verifiable** follow-ups, e.g. *"Claims Sanhua received a $685M Optimus order (Oct 2025) → verify in Sanhua H-share filing + any Tesla 8-K."* Include any **new-name candidates** that might cross the page-creation threshold (3+ sources / chokepoint-central).
7. **Contradictions / red flags** — where the video conflicts with vault findings, or shows promotional incentive, or makes an unsupported leap.
8. **Source-tier verdict (restated)** — one line: "Tier 3/5 — do not cite as vault fact; use to generate questions; verify against primary sources before any page edit."

Disciplines to apply throughout (same as the vault's):
- **Honest-verdict** — if the video is hype with no real signal, say so plainly and keep the note short. Don't manufacture relevance.
- **Describe-don't-recommend** — no buy/sell. Reframe "should I buy X" into "what would have to be true."
- **Plain language** in the chat summary (the user prefers simple words); vault voice only inside any *proposed* page content (which this skill does not write anyway).
- **Auto-caption caveat** — never treat a transcript number/name as exact; flag anything that reads as a transcription error.

## Step 6 — Save the note

Write the full note (header → transcript → analysis) to:
```
raw/notes/video-intel/<UPLOAD_DATE>_<channel-slug>_<title-slug>.md
```
- `<UPLOAD_DATE>` = the video's `upload_date` (YYYY-MM-DD); fall back to today's date if unknown.
- Slugs: lowercase, hyphenated, ASCII, trimmed to ~40 chars.
- Put the **full cleaned transcript** at the bottom of the file under `## Transcript (Tier 3/5 — not a primary source)` so it is greppable later, but keep the **analysis at the top**.
- Then clean up the scratch dir: `rm -rf raw/notes/video-intel/.work`.

`raw/notes/video-intel/` is a Tier-3/5 intel log, **not** vault canon and **not** in `index.md`/`log.md` — its files do not count for accounting, exactly like `refresh_log.md` and `conventions-ledger.md`.

## Output to the user (chat)

Lead with the **Tier verdict + TL;DR**, then the **named-entities** read, then the **ingest leads** (the actionable part), then where the note was saved. Keep it scannable and plain-language. End by reminding (once) that this is discovery-only — nothing touched the vault pages, and naming what to verify is the deliverable.

## Long-form videos (podcasts, 1h+)

Captioned long videos are fully supported — caption fetch and cleaning are length-independent. A 2-hour video is ~18-20k words (~25-30k tokens); read all of it, do not sample. What changes is the analysis shape:

- **Pull chapter markers if present** and use them to structure the analysis by segment:
  ```bash
  yt-dlp --skip-download --no-warnings --print "%(chapters)s" "<URL>"
  ```
  If the creator added chapters, organize Key claims + Vault cross-reference by chapter/segment; if not, segment by topic shift yourself.
- **Extract signal, do not recap.** The deliverable for a long podcast is the 8-15 claims/entities that matter, each with an approximate timestamp so it is jump-to-able — never a linear minute-by-minute summary.
- **Timestamps are load-bearing here.** Tag every claim and named entity with `(~HH:MM)` so the user can verify the moment in a 2-hour file.
- **No-caption long videos are the heavy path.** Whisper on 2 hours of audio is 10-30+ minutes plus an audio download — only take that path on explicit user request (Step 2 fallback). Podcasts almost always have captions, so this is rare.
- The saved MD file's appended transcript will be large; that is fine (it is a greppable log). Keep the full transcript, not a trimmed one.

## What this skill is NOT

- Not a way to add YouTube claims to the vault directly (that violates the source hierarchy).
- Not a broad multi-video search (use `/last30days`).
- Not a video downloader — captions + metadata only.
- Not a buy/sell recommender.
