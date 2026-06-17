# automation/ — the stocks-wiki self-X layer

Operational home for all background / headless automation of the vault (the "self-learning loop" — its scripts, prompts, run logs, and output queues). Sibling to `scripts/` and `prompts/`: **operational infrastructure, not vault content** (CLAUDE.md §1.3). Not canon, not read during onboarding, not counted in `index.md` / `log.md` — same status as `scripts/`, `prompts/`, and `raw/notes/<skill>/`. It exists so automation has one home and never touches canon.

## The contract (the whole safety model)

Every automated run — cron script or headless `claude -p` / Agent SDK agent — is **DISCOVERY-ONLY + PROPOSE-ONLY**. It MUST NOT:

- edit any `wiki/` page, `wiki/_thesis*` or `raw/notes/frameworks*` (human-owned anchors), `CLAUDE.md`, `index.md`, `log.md`, `refresh_log.md`, or `conventions-ledger.md`;
- run `git` (Vic commits everything himself);
- bump any page's `last_updated`.

It writes **only** inside `automation/` — plus the Tier-3 research zone `raw/research/self-research/` (where the daily deep-research saves reports) and `raw/research/topics-list.md` (the agenda it updates). Both are research material, **not canon**. When something belongs in canon, it **drops a proposal in a queue here for a separate, human-gated action — it never cascades.** Verified facts still reach canon only through the normal two-stop ingest.

**Enforcement:** headless runs launch with a restricted tool allow-list — `Read, Grep, Glob, Bash` + `Write` scoped to `automation/` only, **no `Edit` on `wiki/`**. That restriction is what makes unattended runs safe; don't loosen it. This is the vault's existing discovery-only contract extended to scheduled/headless mode — the human gate is unchanged: automation fills the queues, Vic empties them.

## Layout

Subfolders are created on demand by the scripts (`mkdir -p`, the `raw/notes/<skill>/` pattern) — none are pre-committed. Intended:

- **infra:** `scripts/` (code), `prompts/` (locked `claude -p` prompts), `config/` (schedules + allow-lists)
- **output queues:** `calibration/` (self-evaluation — scored falsifier/test outcomes), `discovery/` (self-discovery — surfaced candidates), `codification/` (self-improvement — drafted proposals you gate)
- **run records:** `logs/` (audit trail), `digests/` (the prioritized briefings you read)

## Status

Scaffold only — nothing wired up. Proposed rollout: (1) cron the deterministic scripts + a hygiene check → `digests/`; (2) headless calibration sweep → `calibration/` (the self-evaluation loop); (3) Agent SDK orchestrator → one ranked weekly briefing; (4) event hooks (index rebuild + link check). Human-gated follow-ups not yet done: a one-line awareness note in the `agent-onboarding` skill, and a one-line mention in CLAUDE.md §1.3 (human-owned — propose at a codification session).
