---
name: CS153
description: Ingest ONE Stanford CS153 "Frontier Systems" course lecture (a YouTube link) into the dedicated course corpus at raw/notes/stanford-cs153/. Fetches the transcript with yt-dlp, cleans it, saves it into that folder, analyzes the lecture through the vault's three theses + chokepoint-quality gradient with per-speaker incentive leans (CS153 speakers are Tier 3/5 talking their books — Jensen=NVDA, Altman=OpenAI, a16z partners, Vahdat=Google, Nolan=Founders Fund), and appends a stack-layer-structured entry to raw/notes/stanford-cs153/notes.md. PURPOSE-BUILT so course lectures never land in the general video-intel feed — use this, NOT /youtube-intel, for any CS153 video. DISCOVERY-ONLY: it never edits _thesis*, frameworks*, trackers, index.md, log.md, or any wiki page; the ai-frontier-systems theme page is built SEPARATELY and human-gated.
---

# CS153 — build the Stanford CS153 "Frontier Systems" course corpus

This skill turns the **Stanford CS153 Frontier Systems** course (Spring 2026, taught by leading AI-industry figures) into a single, vault-aware research corpus. The user feeds the course's YouTube lectures **one at a time**; each run saves that lecture's transcript and folds its investment-relevant insights into one consolidated, stack-structured `notes.md`. When the course is complete, the corpus (all transcripts + `notes.md`) becomes the source material for a human-gated **`ai-frontier-systems`** theme page.

## Why this exists separately from `/youtube-intel`

`/youtube-intel` is for **general, standalone** videos and hard-codes its output to `raw/notes/video-intel/` (one disconnected note + a registry row per video). A *course* is the opposite: one coherent corpus that should accumulate into **one synthesis**, not a dozen scattered notes. So CS153 lectures get their **own folder and their own consolidated file** — and a **dedicated trigger** so there is never a judgment call about where a course video lands.

**The routing rule (load-bearing — this is the whole reason the skill exists):**
- `/CS153 <url>` → Stanford CS153 lecture → transcript into `raw/notes/stanford-cs153/` + entry into `raw/notes/stanford-cs153/notes.md`.
- `/youtube-intel <url>` → any other video → `raw/notes/video-intel/`.
- **Never** route a CS153 lecture through `/youtube-intel`, and never route a general video through `/CS153`. The trigger decides the folder — do not improvise.

## The hard boundary (read first — same as youtube-intel)

CS153 lectures sit at the **bottom of the vault's source hierarchy** (CLAUDE.md Section 2.2): a genuine first-principles infra lecture (Vahdat, Jensen on architecture) is **Tier 3** ("cite, don't treat as fact"); a book-talking / promotional segment (Altman on demand, a16z partners) is effectively **Tier 5**. Either way it is **never ground truth.**

Therefore this skill is **discovery-only**. It MUST NOT, under any circumstances:
- edit `wiki/_thesis.md`, `wiki/_thesis-defense-drones.md`, `wiki/_thesis-humanoid-robot.md` (human-owned anchors),
- edit any `raw/notes/frameworks*.md` (human-owned),
- edit, create, or delete any page under `wiki/` — `companies/`, `chokepoints/`, `themes/`, `trackers/`, or `relationships/`,
- touch `index.md`, `log.md`, `refresh_log.md`, or `conventions-ledger.md`.

It writes to **exactly two places**: (1) a cleaned transcript file in `raw/notes/stanford-cs153/`, and (2) the consolidated `raw/notes/stanford-cs153/notes.md`. Nothing else. The `ai-frontier-systems` theme page is built later, as a **separate, human-gated action** under the Tier-3-anchored convention (CLAUDE.md Section 3.13 / "A2") — see the last section.

## When to use / when NOT to use

- **Use** when the user invokes `/CS153 <url>` (or pastes a Stanford CS153 Frontier Systems lecture link and says it's for the course).
- **Do NOT use** for any non-CS153 video — that's `/youtube-intel`. If a pasted link's channel is not "Stanford Online" / the title doesn't read as a CS153 Frontier Systems lecture, **stop and confirm** with the user before treating it as course material.

## Inputs

One Stanford CS153 lecture YouTube URL per run (watch link or `youtu.be` short link). Default output depth: full transcript saved + a structured synthesis entry in `notes.md`. The user may say "transcript only" (skip the analysis) or "deep" (expand a dense lecture).

## Step 0 — Setup (idempotent; run every time)

```bash
cd /Users/victor_he/Projects/stocks-wiki            # ALWAYS anchor to vault root first (avoids cwd-drift)
mkdir -p raw/notes/stanford-cs153/.work
```

- If `raw/notes/stanford-cs153/notes.md` does **not** exist, create it from the backbone template (see "notes.md structure" at the bottom). The backbone is **layer-structured from the start** (energy → silicon → memory/packaging → networking → data centers → models → software → security → geopolitics, plus a cross-cutting-metrics bucket and an agree/diverge cross-walk) so it converts cleanly into the theme page later. It already exists in this vault — do not overwrite it.
- **Preconditions:** `command -v yt-dlp` and `python3` must be present (see youtube-intel preconditions if missing).

## Step 1 — Fetch captions + metadata (no video download)

Clear scratch first so a crashed prior run can't leave a stale `.vtt` the cleaner then auto-picks:
```bash
cd /Users/victor_he/Projects/stocks-wiki
OUT="raw/notes/stanford-cs153/.work"
rm -rf "$OUT"; mkdir -p "$OUT"
```

Metadata (title, channel, dates, duration — and chapters + description, which carry the lecture's structure + speaker affiliation that feed the Tier call):
```bash
yt-dlp --skip-download --no-warnings \
  --print "%(id)s\t%(title)s\t%(channel)s\t%(upload_date)s\t%(duration_string)s\t%(view_count)s" "<URL>"
yt-dlp --skip-download --no-warnings --print "%(chapters)s" "<URL>"        # [] if none — used for segment-by-segment reading
yt-dlp --skip-download --no-warnings --print "%(description).600s" "<URL>"  # speaker bio / course context
```

Captions (English; keep native `.vtt`, the cleaner consumes it directly — do NOT use `--convert-subs`):
```bash
yt-dlp --skip-download --no-warnings \
  --write-subs --write-auto-subs --sub-langs "en.*,en" \
  -o "$OUT/%(id)s.%(ext)s" "<URL>"
```

- **No captions at all:** report it. Offer the opt-in local-Whisper fallback (heavy; only if the user asks) per the youtube-intel pattern. Do not fabricate a transcript.
- **HTTP 429:** transient yt-dlp rate-limit; wait a moment and retry just that URL.

## Step 2 — Clean the transcript

Reuse the proven youtube-intel cleaner (single source of truth — strips VTT header, timestamps, inline word-timing tags, rolling auto-caption duplicates, reflows into paragraphs):
```bash
python3 .claude/skills/youtube-intel/scripts/clean_subs.py "$OUT" > "$OUT/clean.txt"
```
Read `clean.txt`. If the cleaner reports "no .vtt/.srt", treat as the no-captions case.

## Step 3 — Save the transcript into the corpus

Write the cleaned transcript to a stable, sortable filename in the corpus folder:
```
raw/notes/stanford-cs153/<UPLOAD_DATE>_<speaker-slug>.md
```
- `<UPLOAD_DATE>` = `YYYY-MM-DD`; `<speaker-slug>` = lowercase-hyphenated lead speaker (e.g. `2026-05-13_jensen-huang.md`).
- Give the file a small header (lecture title, speaker + affiliation, URL, upload date, duration), then the full cleaned transcript under `## Transcript (Tier 3/5 — not a primary source)`.
- **Idempotency:** if a transcript file for this lecture already exists, or the Lecture-log table in `notes.md` already has its row, do not duplicate — update in place and say so.
- **Already-analyzed-elsewhere case:** the Jensen Huang lecture (`tsQB0n0YV3k`) is already worked up at `raw/notes/video-intel/2026-05-13_stanford-cs153_jensen-huang-compute-behind-intelligence.md`. If a lecture is already analyzed elsewhere in the vault, still fetch its transcript here for corpus completeness, but in `notes.md` **point to the existing analysis** rather than redoing it.
- Then clean up scratch: `rm -rf raw/notes/stanford-cs153/.work`.

## Step 4 — Classify tier + incentive lean (mandatory)

State plainly, per lecture: which **Tier** (3 = independent first-principles infra reasoning; 5 = book-talking / promotional) and the **incentive lean** of the speaker. CS153 speakers almost all carry a lean — name it, because it calibrates which claims to discount:
- **Jensen Huang** (NVDA CEO) — every demand/energy/share claim sells NVDA's book; the *architecture framework* is informative, the *magnitudes* are not.
- **Sam Altman** (OpenAI) — inference-demand maximalist; "cheap intelligence → infinite demand" is the frontier-lab house view.
- **Amin Vahdat** (Google Fellow, AI infra) — densest infra content; lean is pro-Google-stack/TPU but the *value-per-gigawatt* framework is the highest-value idea in the course.
- **Anjney Midha / Ben Horowitz** (a16z) — talking the a16z portfolio + the demand-elasticity bull case (same lean as the Andreessen videos in the feed).
- **Scott Nolan** (Founders Fund / General Matter) — energy/enrichment; lean toward the nuclear-fuel thesis he's invested in.
- Others (ElevenLabs, Black Forest, Luma, YC, product/security speakers) — narrower, often lower investment-signal.

The Tier verdict gates how much weight every downstream claim gets.

## Step 5 — Analyze (the core)

- **Segment-by-segment for long lectures.** These run 60–90 min (~15–20k words). If chapters exist (Step 1), work one segment at a time — extract that segment's claims + entities before moving on — then merge. Do NOT single-pass a 20k-word transcript; it drops claims.
- **Evaluate through the three theses + the chokepoint-quality gradient.** Primary lens is the **AI-datacenter** thesis (compute / photonics / memory / energy-power / equipment / materials). Note the rare Defense/Humanoid touch (robotics usually shows up only as an inference-demand driver). For any chokepoint candidate, place it on the gradient (geology/physics > precision-manufacturing > policy; Framework 12).
- **Fact-check against the companion report.** `raw/notes/reports/stanford-cs153-invest-in-ai-stack.md` is a Tier-3 pre-built synthesis of the whole course — use it as the backbone, but **verify its per-lecture claims against the actual transcript** and correct what it got wrong (it has known broken figures — e.g. a Meta-capex cashtag artifact, a dropped Broadcom number). Per-lecture depth the report compressed away is exactly what this corpus adds.
- **Honest-verdict discipline — lectures are NOT equal.** Vahdat / Jensen / Nolan / Altman are dense investment signal and earn deep entries. Voice / visual / product-management lectures may earn three lines. Do not manufacture relevance or force equal depth.
- **Every spoken number is soft.** Render with `~` and a verify tag; never quote an audio number as exact. CS153 figures are Tier-3 → verify-at-primary before they could ever reach canon.
- **Cross-link the vault as you go.** For each company/chokepoint named, note whether a page exists and which thesis/chokepoint/tracker it touches — but only as a *flag* (discovery-only); never edit those pages.

## Step 6 — Append the lecture into `notes.md` (by stack layer)

This is the consolidating step — do NOT write a standalone per-video note. For each lecture, update `raw/notes/stanford-cs153/notes.md`:
1. **Lecture log** — add one row: `#` · speaker (affiliation) · upload date · transcript filename · Tier · depth verdict · one-line takeaway.
2. **Synthesis by stack layer** — drop this lecture's speaker-attributed insights into the relevant layer bucket(s). Attribute every claim to the speaker + tag `[verifiable]` / `[opinion]` / `[forward]`. Keep the best 2–4 load-bearing claims as short verbatim quotes with timestamps.
3. **Agree / diverge vs vault canon** — if the lecture confirms or diverges from a primary-grounded vault view, add a one-line cross-walk entry (this is the raw material for the theme page's distinct job — the independent-Tier-3-lens map).
4. **Open questions → primary-source verification triggers** — pre-register what to check at a 10-K/10-Q/call before any of this reaches the theme page.

Apply CLAUDE.md Section 3.8 brevity discipline — `notes.md` is a working synthesis, not a transcript dump (the transcript already lives in its own file).

## Step 7 — Output to the user (chat)

Lead with the **Tier verdict + incentive lean + TL;DR**, then the **2–4 highest-value insights** (with the layer each fed), then any **agree/diverge vs the vault** worth flagging, then **what to verify at primary**, then where the transcript + notes were saved. Plain language. End by reminding once: discovery-only — nothing touched the wiki pages; naming what to verify is the deliverable; the `ai-frontier-systems` page is built separately.

## Building the `ai-frontier-systems` theme page (separate; human-gated; do NOT do inside this skill)

When the course is complete, the page is built as a **Tier-3-anchored theme page** (CLAUDE.md Section 3.13 / "A2"), in a separate action the user explicitly asks for:
- **Anchor:** the `stanford-cs153/` corpus + the companion report, attribution explicit in the body + frontmatter (`tickers` = provenance; note the Tier-3/5 anchor).
- **Its distinct job (avoid duplicating `_thesis.md` + existing themes):** the CS153 "AI factory" framework as a *named, independent Tier-3 lens* on the vault's thesis — the value-per-gigawatt / tokens-per-watt metric set, the bottleneck-migration timeline, speaker-attributed views, and an **agree/diverge cross-walk** against the vault's primary-grounded canon.
- **No verification at construction**; Open questions pre-registers primary-source verification triggers; counterparty claims annotated per the A1 three-mode framing (Section 3.5).
- It's canon, so it goes through the normal two-stop, human-approved build — **never** written by this skill.

## notes.md structure (the backbone seeded at Step 0)

```
# Stanford CS153 "Frontier Systems" — course notes (Tier 3/5 — NOT vault canon)
> ROUTING + discovery-only banner
## Course meta            (source, companion report, status)
## Lecture log            (table: # | speaker | date | transcript file | tier | depth | one-line)
## Synthesis by stack layer
  ### 0. Cross-cutting metrics (value-per-GW, tokens-per-watt, MW funnel, bottleneck migration)
  ### 1. Energy & power      ### 2. Silicon & accelerators
  ### 3. Memory & advanced packaging   ### 4. Networking, fabrics & optics
  ### 5. Data centers, neoclouds & hyperscalers   ### 6. Models, apps & demand formation
  ### 7. AI-native software & operating models     ### 8. Security, resilience & sovereignty
  ### 9. Geopolitics, export controls & supply chain
## Agree / diverge vs vault canon   (running cross-walk — the theme page's distinct job)
## Open questions → primary-source verification triggers
```

## Long-form / no-caption handling

Captioned long lectures are fully supported (caption fetch + cleaning are length-independent). No-caption lectures: offer the opt-in local Whisper fallback (`mlx-whisper` via `uvx`; heavy, minutes not seconds) only if the user asks — never auto-run it. Treat any Whisper output as an even lower-confidence transcript.
