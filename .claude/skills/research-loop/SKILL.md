---
name: research-loop
description: Vault-aware deep research on a topic, interactively. Scopes the topic into 15-20 angles, researches each (research → adversarial challenge → verify), runs 10 grounded agents that tie the findings to the existing vault, then synthesizes one cited Tier-3 report with a "Vault connections" section. The on-demand sibling of the headless automation/scripts/research_loop.py. Discovery-only — saves ONE report to raw/research/interactive/ and never edits canon, the agenda, or any wiki page. Use when the user runs /research-loop <topic>, or asks to research a topic AND connect it to the vault (the gap /deep-research [web-only] and connection-finder [vault-only] each leave).
---

# research-loop — vault-aware deep research, interactively

This skill researches a topic deeply **and grounds it in your vault** — the one thing neither `/deep-research` (web research, vault-blind) nor `connection-finder` (vault cross-referencing, no new research) does. It's the interactive sibling of the headless nightly loop (`automation/scripts/research_loop.py`): same architecture (scope → research → connections → synthesis), but it runs on the **Workflow tool** (fast, ~16 concurrent, harness handles throttles) instead of headless `claude -p`, with a richer per-angle pass (research → **challenge** → verify).

## The hard boundary (discovery-only)

This skill writes EXACTLY ONE file: the report at `raw/research/interactive/<DATE>_<slug>.md`. It MUST NOT, under any circumstances:
- edit any `wiki/` page (company / chokepoint / theme / tracker / relationship), `index.md`, or `log.md`,
- edit `wiki/_thesis*.md` or `raw/notes/frameworks*.md` (human-owned anchors) or `CLAUDE.md`,
- touch `raw/research/topics-list.md` or the nightly agenda (interactive runs are ad-hoc — they never mark topics done),
- run git.

The report is **Tier-3 discovery material**, human-gated to canon — it names what to verify; verified facts still reach canon only through the normal two-stop primary-source ingest. Same contract family as `youtube-intel` / `bear-case` / `priced-in`.

## When to use

- The user invokes `/research-loop <topic>`.
- The user wants to research a topic **and** see how it connects to the vault (which pages it confirms/challenges/extends, what's missing).

Not for: a quick web-only question (use `/deep-research`), surfacing connections among *existing* pages with no new research (use `connection-finder`), or a primary-source ingest (the human-gated two-stop).

## Steps

1. **Preconditions.** `mkdir -p raw/research/interactive/`. Take the topic from the user (any ad-hoc topic — it need not be on `topics-list.md`).

2. **Run the workflow.** Invoke the saved Workflow (the skill invocation IS the multi-agent opt-in):
   ```
   Workflow({ name: "research-loop", args: { topic: "<the user's topic>" } })
   ```
   It runs four phases — **Scope** (15-20 adaptive angles) → **Research** (each angle: research → adversarial challenge → verify, concurrent) → **Connect** (10 grounded vault-connection agents) → **Synthesize** (one report). It runs in the background; the user can watch the phases live with **`/workflows`**. The workflow returns `{ topic, report, angles, connections }`.

3. **Save the report.** Take the returned `report` markdown and **Write** it to:
   ```
   raw/research/interactive/<YYYY-MM-DD>_<slug>.md
   ```
   `<slug>` = lowercase, hyphenated, ASCII, ~6-8 words of the topic. The skill (you) does this single write — not a sub-agent. Do NOT write anything else.

4. **Report to the user (chat).** Lead with the report's **one-paragraph verdict**, then the **Vault connections** highlights (which pages it confirms/challenges/extends + any new-page candidates), then where it saved (`raw/research/interactive/…`) and that it was watchable via `/workflows`. Plain language. End by reminding once that this is discovery-only — Tier-3, human-gated; the report names what to verify at primary sources, and nothing in canon or the agenda was touched.

## What the workflow does (for reference)

`.claude/workflows/research-loop.js` — the orchestration:
- **Scope:** one agent → 15-20 distinct angles (adaptive to topic breadth; capped at 20).
- **Research:** `pipeline()` over the angles — each runs research (5-8 web searches) → **challenge** (find the strongest *disconfirming* evidence; rewrite two-sided) → verify (fact-check). Angles run concurrently (~16 cap).
- **Connect:** `parallel()` over the **10 connection specs** (companies×2, themes×2, chokepoints CONFIRM + CHALLENGE, trackers+relationships, thesis+frameworks, prior-research [unverified-tagged], coverage-gaps) — each greps its slice of the vault and reports CONFIRM/CHALLENGE/EXTEND links, honest-verdict. These specs **mirror** `automation/scripts/research_loop.py` — keep the two in sync.
- **Synthesize:** one agent → the cited report (verdict · value chain · analysis · Vault connections · what-to-verify).

The workflow's agents are **read-only** (web + grep); the workflow returns the report as a string (no filesystem access); this skill does the single disk write.

## Disciplines

- **Discovery-only** — one report to `raw/research/interactive/`; never canon, anchors, or the agenda.
- **Honest-verdict** — the challenge pass + the chokepoint-challenge connection agent keep every report two-sided; surface `[contested]`/`[unverified]` flags, don't bury them.
- **Tier discipline** — the report is Tier-3 (web-sourced); it names primary-source leads, it does not assert canon.
- **Describe-don't-recommend; no price targets / position sizing.**
- **Plain language** in the chat summary.

## What this skill is NOT

- Not `/deep-research` (web-only, vault-blind) and not `connection-finder` (vault-only, no new research) — it's both at once.
- Not the headless nightly loop (`research_loop.py`) — that's the unattended, agenda-driven version; this is on-demand and never touches the agenda.
- Not a primary-source ingest, and not a way to write to canon (it flags candidates; the human gate is unchanged).
