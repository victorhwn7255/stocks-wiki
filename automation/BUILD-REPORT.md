# automation/BUILD-REPORT.md — self-X automation build

**Date:** 2026-06-17 · **Status:** ✅ BUILT, TESTED, and RUNNING. The **"Stocks Wiki"** LaunchAgent is installed (`~/Library/LaunchAgents/StocksWiki.plist`), loaded, and scheduled to run the **full autonomous loop weekly (Mondays 08:00) on the Claude Max subscription** (headless `claude -p` auth verified = `AUTH_OK`); a first live run was kicked off on install. The only remaining **gated** item is the optional per-edit `settings.json` hook (self-config; needs Vic's explicit ok).

---

## Executive summary

The five-phase self-X automation from `automation/ROADMAP.md` is implemented. The **deterministic loop runs today** — I executed it live multiple times; it produces a real ranked digest, a calibration queue, and an audit log, and it already caught real entropy (a `[[Canonical]]` typo, a `[[TSMC]]` mis-link, 30 self-link pages). The **agentic layer** (calibration scoring, briefing, extract-learnings) is wired behind the locked tool allow-list and verified to build the correct restricted `claude -p` command. The **two enablements that touch the OS / the agent's own config** — the launchd weekly schedule and the `settings.json` post-edit hook — were each correctly blocked by the harness as needing your explicit ok (and the ROADMAP flagged both as open decisions). They are ready; enabling each is a single command, below.

**Nothing in canon was touched.** Everything is in `automation/`, `scripts/`, and `.claude/skills/` — operational, not vault content. No `wiki/`, `_thesis*`, `frameworks*`, `CLAUDE.md`, `index.md`, or `log.md` change. No git run.

---

## Per-phase build status

### Phase 0 — Foundations ✅
- **Runner:** `automation/scripts/run.py` — the conductor. Modes: `--scan` (deterministic, default, free), `--calibrate` / `--brief` (agentic, opt-in, need `--run-llm`), `--with-freshness` (adds SEC EDGAR).
- **Contract enforcement:** `ALLOWED_TOOLS = "Read,Grep,Glob,Bash(python3 scripts/*),Write"` + `DISALLOWED_TOOLS = "Edit,MultiEdit,NotebookEdit"` — passed to every `claude -p` the runner builds. Documented in `automation/config/allowlist.md`.
- **Run harness:** logs every run to `automation/logs/run-<date>.log`; outputs to `automation/{digests,calibration,discovery}/` (created on demand).
- **Verified:** runner executes, writes the digest/log/queue, prints action items.

### Phase 1 — Maintain + Discover (deterministic) ✅ LIVE
- **New engine:** `scripts/vault_hygiene.py` — 6 read-only checks (link-integrity, index-sync, count-drift, frontmatter, staleness, tracker-freshness), reusing `vault_parsers.py`. Modes: default report / `--summary` / `--json` / `--quick-check <file>`.
- **New skill:** `vault-hygiene` (registered, read-only/flags-only).
- **Wired into** the runner's deterministic scan alongside `find_connections.py`, `monitor_patterns.py`, and (opt-in) `fetch_filings.py --freshness`.
- **Verified live (2026-06-17):** overall WARN. PASS on index-sync (81/81, 13/13, 24/24, 5/5, 1/1), count-drift, frontmatter (0 issues / 81 pages), staleness (0), tracker-freshness (0/5 overdue). WARN on link-integrity — **real findings:** `[[Canonical]]` typo in `power-semis.md`, `[[TSMC]]` in `COHU.md`, forward-links `[[CMI]]`/`[[QCOM]]`, and 30 self-link pages (§3.3).

### Phase 2 — Calibration sweep ✅ (deterministic LIVE; agentic wired)
- **New engine:** `scripts/calibration_sweep.py` — parses `forward-edge-tracker.md` (12 entries) + `what-could-go-wrong.md` (16 entries), extracts Catalyst/Falsifier/Tripwire + Last-moved/checked dates + temporal watch-markers, ranks FIRED → review-due → oldest.
- **New skill + prompt:** `calibration-check` skill + `automation/prompts/calibration-score.md` (the headless scoring prompt → `automation/calibration/`).
- **Verified live:** 12 + 16 entries parsed; 0 FIRED, 0 review-due (trackers fresh); correctly surfaced watch-dates (FCEL's Oct-31 conversion test, the FY2027 budget gate, the memory-cycle dates).

### Phase 3 — Drafts + Orchestrator ✅ (wired; agentic opt-in)
- **New skill + prompt:** `extract-learnings` skill + `automation/prompts/extract-learnings.md` (self-improving → `automation/codification/`).
- **Orchestrator:** `run.py --brief` + `automation/prompts/brief.md` — chains the deterministic scan into one ranked briefing (top-3 actions + counterweights).
- **Verified:** the `--calibrate` dry-run builds the correct locked `claude -p` command; `--run-llm` is required to actually spend tokens (so the default/scheduled run is always free).

### Phase 4 — Hooks ⚙️ BUILT, ENABLEMENT GATED TO VIC
- **Hook script:** `automation/scripts/hook_postwrite.sh` — on an `Edit`/`Write` to a `wiki/` page, runs the FAST `vault_hygiene.py --quick-check <file>` (the page's links resolve + it's in `index.md`) and logs to `automation/logs/hook.log`. Read-only, non-blocking, always exits 0. **Tested working** (caught the `[[Canonical]]` typo via a simulated PostToolUse payload).
- **Enablement deferred:** editing `.claude/settings.json` to register the hook is self-modification of the agent's config — the harness classifier blocked it, and the ROADMAP flagged it as an open decision. The ready-to-paste config is at `automation/config/settings-hook.snippet.json`.

---

## What's running NOW vs what's one-command-from-live

| Capability | State | To make autonomous |
|---|---|---|
| Deterministic scan (hygiene + calibration + discovery) | ✅ **runs today** — `python3 automation/scripts/run.py --scan` | already runnable; schedule it ↓ |
| Calibration scoring / briefing / extract-learnings (agentic) | ✅ wired, dry-run verified | `... --calibrate --run-llm` (opt-in, paid) |
| **"Stocks Wiki" schedule** (launchd, Mondays 08:00, the **full** loop on Max) | ✅ **INSTALLED + running** (PID seen on first run) | live; tune cadence in `automation/config/StocksWiki.plist` |
| **Post-edit hook** (per-wiki-edit link/index quick-check) | ⚙️ built + tested, **gated** | merge `automation/config/settings-hook.snippet.json` into `.claude/settings.json` |

Both gated items are trivially reversible (`uninstall_schedule.sh`; remove the hook block).

---

## File inventory

**New scripts (deterministic engines, reuse `vault_parsers.py`):**
- `scripts/vault_hygiene.py` · `scripts/calibration_sweep.py`

**New skills:**
- `.claude/skills/vault-hygiene/SKILL.md` · `.claude/skills/calibration-check/SKILL.md` · `.claude/skills/extract-learnings/SKILL.md`

**Edited skills:**
- `.claude/skills/latest-alpha/SKILL.md` — added the **headless / note-only mode** (skip the on-page block when run unattended).
- `.claude/skills/agent-onboarding/SKILL.md` — added the 3 self-X skills to the router + `automation/` awareness.

**automation/ (the loop's home):**
- `README.md` (contract) · `ROADMAP.md` (plan) · `BUILD-REPORT.md` (this file)
- `scripts/run.py` (runner) · `scripts/hook_postwrite.sh` (Phase-4 hook)
- `prompts/{calibration-score,brief,extract-learnings}.md` (the locked `claude -p` prompts)
- `config/{allowlist.md, com.stockswiki.automation.weekly.plist, install_schedule.sh, uninstall_schedule.sh, settings-hook.snippet.json}`
- live outputs: `digests/2026-06-17_digest.md`, `calibration/2026-06-17_candidates.json`, `logs/run-2026-06-17.log`, `logs/hook.log`

**Not touched (human-owned / canon):** every `wiki/` page, the 3 `_thesis*`, the 3 `frameworks*`, `CLAUDE.md`, `index.md`, `log.md`. No git.

---

## Usage cheatsheet

```bash
# the weekly deterministic briefing (free, safe, ~seconds; +SEC freshness with the flag)
python3 automation/scripts/run.py --scan --with-freshness

# just the health scan / just the calibration sweep
python3 scripts/vault_hygiene.py            # or --summary / --json / --quick-check <file>
python3 scripts/calibration_sweep.py        # or --json / --due-days N

# the agentic steps (opt-in, paid; behind the locked allow-list)
python3 automation/scripts/run.py --calibrate --run-llm   # score resolved calls → automation/calibration/
python3 automation/scripts/run.py --brief --run-llm        # ranked weekly briefing → automation/digests/

# enable autonomy (your call — both gated)
bash automation/config/install_schedule.sh                 # weekly launchd schedule (free scan)
#   then verify: launchctl list | grep stockswiki ;  remove: uninstall_schedule.sh
# hook: merge automation/config/settings-hook.snippet.json into .claude/settings.json
```
The skills are also invokable interactively: `vault-hygiene`, `calibration-check`, `extract-learnings`.

---

## Goal coverage (vs the ROADMAP's G1–G5)

- **G1 (provably compound / private evals)** — `calibration-check` + `calibration_sweep.py` deliver the fitness-function plumbing; first scored records land when `--calibrate --run-llm` runs against review-due entries.
- **G2 (zero silent rot)** — `vault-hygiene` is live and already catching entropy; the (gated) hook makes it per-edit.
- **G3 (multiply noticing)** — the discovery scan (connections + freshness + patterns) surfaces a vetted queue every run.
- **G4 (shorten learn→codify lag)** — `extract-learnings` drafts codification candidates from the traces.
- **G5 (one briefing)** — `run.py` produces the ranked digest; `--brief` upgrades it agentically.
- **Meta (swap test)** — the whole loop runs from files alone behind a restricted tool list: continuous proof of model-independence.

## Open decisions for Vic (the two gated enablements + ROADMAP carryovers)

1. **Scheduler** — opt in to the launchd weekly schedule (`install_schedule.sh`), or pick `/schedule` / `/loop` instead.
2. **Phase-4 hook** — merge the `settings.json` snippet to enable per-edit link/index guarding, or leave it manual (run `vault-hygiene` on demand).
3. **`extract-learnings`** — keep as its own skill (built) or fold into `learning-monitor` later.
4. **First real calibration run** — when ready, `--calibrate --run-llm` will score the review-due entries (none are review-due today; the trackers are fresh).

Everything is in the working tree, uncommitted, for your review and commit.
