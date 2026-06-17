# automation/ROADMAP.md — the self-X implementation plan

Living plan for the vault's background / headless automation (the "self-learning loop"). Read alongside `automation/README.md` (the safety contract). This file *sequences* the build; each phase gets its own go-ahead — nothing here is wired up yet.

---

## North Star

The vault is a learning loop. Mapped to Nadella's three pillars: **queryable knowledge base** (strong), **RL-from-traces** (good, but human-gated), **private evals** (the gap). This automation has one job:

> **Defend and accelerate the vault's compounding rate against entropy, while keeping the human gate fully intact.**

Everything below is **DISCOVERY-ONLY + PROPOSE-ONLY** behind the `README.md` contract: it writes only inside `automation/`, never edits canon, never runs git, never bumps `last_updated`. Automation fills the queues; Vic empties them.

## Goals & objectives (measurable)

| Goal | Why it matters | Expected outcome (measurable) |
|---|---|---|
| **G1 — make the loop *provably* compound** | the missing private-evals pillar; today the vault accumulates but can't prove its calls improve | a calibration log → a first **accuracy %** within ~a quarter (the §4.6 falsification streak generalized from process- to analytical-accuracy) |
| **G2 — zero silent rot** | entropy (staleness, drift, the codification backlog, the full-read wall) is the real threat to "the edge that holds" | link-graph always clean; count/index drift caught by machine; staleness surfaced weekly |
| **G3 — multiply *noticing*, not *hours*** | the vault grows because Vic notices things; automating the noticing is pure leverage | a weekly **vetted discovery queue**; faster growth at the same human effort |
| **G4 — shorten the learn→codify lag** | codification candidates pile up waiting for attention | backlog **age trending down**; proposals **pre-drafted** to gate |
| **G5 — one briefing, not N scans** | the convenience layer that makes G1–G4 actually get used | **one ranked weekly briefing** (top-3 actions + the rest logged) Vic actually reads |

**Meta-goal — prove the swap test continuously.** Every headless run is a fresh, unattended model operating the vault *from the files alone*, behind a restricted tool list — so a working automation layer is ongoing proof that the vault's knowledge is model-independent (sovereignty, in Nadella's terms).

**Non-goals (the boundary *is* the safety model).** NOT automating judgment, NOT auto-writing canon, NOT replacing Vic. Automation does the mechanical 80% (scanning, date-checking, surfacing, drafting, scoring); Vic keeps the 20% (verdicts, taste, what matters).

## Architecture — "build the logic once, invoke it two ways"

- **Deterministic logic → `scripts/`** (cron-safe, no LLM, no cost). **Agentic logic → skills** (the interactive front door + the canonical reasoning). **`automation/` = the headless runner + the output queues + the contract.**
- Each capability is a **skill backed by a script** — the vault's existing pattern (`check-recent-earnings`→`fetch_filings.py`, `connection-finder`→`find_connections.py`, `spread-watch`→`spread_watch.py`). The automation runner then invokes the same skill/script **headlessly** with a locked tool allow-list. No logic is duplicated.
- **Output homes (all under `automation/`, never `raw/notes/`):** `calibration/` (self-eval), `discovery/` (self-discovery queue), `codification/` (self-improve drafts), `logs/` (audit trail), `digests/` (the briefings). `raw/notes/<skill>/` stays the home for *interactive* discovery notes; `automation/` is the *loop's* home.
- **Cost discipline:** deterministic scans do the filtering; agentic jobs run weekly and only on the narrowed candidate set — never a nightly full-vault read of the ~290k-token canon.

## What gets automated

Split by whether it needs an LLM. **Deterministic = cron, free, zero canon-risk. Agentic = `claude -p`/SDK, metered, runs only on the narrowed set.**

- **Self-maintaining (deterministic):** link-integrity (every `[[wikilink]]` resolves, no self-links), count-drift (stated counts vs actual file counts), frontmatter-integrity (valid fields/tier values/dates), staleness (extended to non-company pages), index-sync (catalog ↔ disk round-trip), tracker-freshness (the 5 trackers vs a threshold).
- **Self-discovering:** freshness/new-filings + connection + pattern scans (exist) → *[agentic]* candidate triage + stale-name `latest-alpha` → `discovery/`.
- **Self-evaluation (agentic — the headline):** calibration sweep over `forward-edge-tracker` + `what-could-go-wrong` + Open-questions / "what would change the verdict" → score `RIGHT/WRONG/PARTIAL/STILL-OPEN` with evidence → `calibration/`; deterministic roll-up → the accuracy scorecard.
- **Self-improving:** pattern accumulation (exists) → *[agentic]* extract-learnings draft → `codification/`.
- **Self-learning (SDK):** orchestrate the above → one ranked weekly briefing → `digests/`.

## Skills & hooks plan

A full skills/hooks/scripts audit (2026-06-17) found: **8 of 10 skills are headless-safe as-is**; only `latest-alpha` and `spread-watch` write to canon; **no hooks exist**; and `vault_parsers.py` already exposes `extract_wikilinks()` + `parse_frontmatter()` for the new hygiene scripts to reuse.

### NEW skills to build
1. **`vault-hygiene`** *(Phase 1)* — self-maintaining. Backed by a NEW `scripts/vault_hygiene.py` (link-integrity + count-drift + frontmatter-integrity + index-sync check + tracker-freshness + staleness-extension), **reusing `vault_parsers.py`**. Read-only/report (the `connection-finder` / `learning-monitor` family). Interactive + headless.
2. **`calibration-check`** *(Phase 2 — THE missing pillar)* — self-evaluation. Backed by a NEW `scripts/calibration_sweep.py` (deterministic: extract dated catalysts/falsifiers from the two trackers + OQ sections, flag overdue/testable); the skill/agent layer scores resolved items → `automation/calibration/`.
3. **`extract-learnings`** *(Phase 3, optional)* — self-improving agentic draft layer on top of `learning-monitor` / `monitor_patterns.py` → `automation/codification/`. (Overlap noted: `learning-monitor` *counts*; this *drafts*.)

### NEW scripts
`scripts/vault_hygiene.py`, `scripts/calibration_sweep.py`, plus the `automation/scripts/` runner (Phase 1) and the SDK orchestrator (Phase 3).

### EXISTING skills to EDIT
1. **`latest-alpha`** — add a **headless / note-only mode** (skip the on-page fenced `<!-- LATEST-ALPHA -->` block when run unattended; write only the `raw/notes/latest-alpha/` note). The block is a canon-page write that the strict no-`wiki/`-edit allow-list would block — note-only mode makes headless stale-name discovery comply cleanly. Minor edit.
2. **`agent-onboarding`** — add `automation/` awareness (operational layer, not canon, not read at onboarding — like `scripts/` / `prompts/`) + add the two new skills to the router.

### EXISTING skills/scripts REUSED as-is (no edit)
- `check-recent-earnings` (freshness + staging download — headless-safe), `connection-finder`, `learning-monitor`, `chokepoint-eval`, `bear-case` / `priced-in` / `youtube-intel` (all read-only or discovery-to-`raw/notes`).
- Scripts: `fetch_filings.py --freshness`, `find_connections.py`, `monitor_patterns.py`, `spread_watch.py`, `spread_chart.py` (cron-safe). `build_index.py` used in **diff/check mode** (read-only) for index-sync detection; `--write` stays human-gated (or becomes the Phase-4 hook action).
- **`spread-watch` stays INTERACTIVE** — it writes a canon tracker + index, so it stays human-gated. The automation runs only its underlying `spread_watch.py` data pull (read-only) for the digest and **flags** "tracker needs update"; it never runs the canon-writing skill headlessly.

### NEW hooks (Phase 4)
A PostToolUse / Stop hook in `settings.json` → on `wiki/` frontmatter change, run `build_index.py` (check) + the link-integrity check; surface drift. None exist today. (A config change to Vic's harness — proposed, needs his ok; can use the `update-config` skill.)

## The phased roadmap

| Phase | Build | Definition of done | Effort | Delivers |
|---|---|---|---|---|
| **0 — Foundations** | run-harness (logs each run to `logs/`; locked tool allow-list in `config/`); pick cadence (weekly) + trigger | one job runs headless, logged, behind the allow-list | small | the rails |
| **1 — Maintain + Discover** *(deterministic)* | `scripts/vault_hygiene.py` + `vault-hygiene` skill; wire existing scans into one `scan` entrypoint → `digests/` | a weekly hygiene+discovery digest, **zero LLM** | a weekend | **G2 + G3 (scan)** now |
| **2 — Calibration sweep** *(agentic — headline)* | `scripts/calibration_sweep.py` + `calibration-check` skill + the `calibration/` record format | `calibration/` filling with scored outcomes; first roll-up scorecard | med | **G1 — the missing pillar** |
| **3 — Drafts + Orchestrator** *(agentic + SDK)* | `extract-learnings` → `codification/`; the SDK conductor → one ranked briefing | a Monday-morning briefing: top-3 actions + the rest logged | larger | **G4 + G5** |
| **4 — Hooks** *(guardrails)* | `settings.json` hook: index rebuild + link check on save | index + graph never drift, no session needed | small | reinforces **G2** |

**Sequencing rule:** deterministic before agentic; **manual-trigger first, then schedule** (run each job by hand, confirm it's genuinely useful, *then* cron it). Each phase ships standalone value; no orchestrator before the scans exist.

## Success metrics

- **G1** — ≥20 scored calibration records + a first accuracy % within a quarter.
- **G2** — silent-drift incidents at zero; link-graph clean.
- **G3** — ingest-from-queue hit rate (how often a queued candidate becomes a real ingest).
- **G4** — codification-backlog age trending down.
- **G5** — % of weekly briefings that produce ≥1 action.

## Risks & guardrails

- **Cost** — set a weekly token budget for the agentic jobs; deterministic scans do the filtering, so the LLM never full-reads the canon nightly.
- **Queue-rot** — if a digest isn't ruthlessly prioritized (top-3, counterweight included), it gets ignored and becomes noise; kill any job that produces noise.
- **The hard line** — never loosen the tool allow-list; never auto-canon; `latest-alpha` headless = note-only; `spread-watch` stays interactive.
- **Maintenance burden** — every script is code to maintain; build the 2–3 highest-leverage first (Phases 1–2), defer the rest.

## Open decisions for Vic (recorded, not blocking)

1. **Scheduler** — launchd plist vs the harness `/schedule` routines vs `/loop`.
2. **`extract-learnings`** — its own skill, or a mode of `learning-monitor`.
3. **Phase-4 hook** — opt in to editing `settings.json` now, or defer.

## Status

Plan crystallized 2026-06-17. Nothing built. Recommended first move: **Phase 1** (a weekend of plain Python — entropy-defense + scan-level discovery, zero LLM cost, and it produces the filtered candidate set Phase 2 needs), then **Phase 2** (the calibration sweep — the strategic payoff).
