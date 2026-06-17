---
name: vault-hygiene
description: Run the deterministic vault health scan for the stocks-wiki vault — link integrity (every [[wikilink]] resolves, no self-links), index-sync (catalog ↔ disk), count-drift (stated counts vs actual file counts), frontmatter integrity, staleness, and tracker freshness. Use whenever the user asks to check vault health, find broken/unresolved wikilinks, check for stale pages or stale trackers, verify the index matches the files, catch count drift, or run a hygiene/lint pass. Trigger on "vault hygiene", "check links", "any broken wikilinks", "is the index in sync", "what's stale", "lint the vault", "vault health check". Read-only — it surfaces entropy and FLAGS it; it never edits canon.
---

# vault-hygiene — the self-maintaining health scan

This skill runs `scripts/vault_hygiene.py`, the deterministic entropy-defense engine for the vault (the self-maintaining loop, CLAUDE.md operational layer). It is the read-only sibling of `connection-finder` / `learning-monitor`: it SCANS and REPORTS, it does not edit.

## The boundary (read-only)

This skill MUST NOT edit any `wiki/` page, `index.md`, `log.md`, `_thesis*`, `frameworks*`, or `CLAUDE.md`. It runs a read-only scan and reports findings. When a check surfaces a real defect (an unresolved wikilink that's a typo, a dead index row, count drift), it **FLAGS it for a human-gated fix** — it never reconciles silently. Index-sync repairs (`build_index.py --write`) and link fixes are separate, human-gated actions.

## When to invoke

Any question about vault health, broken/unresolved wikilinks, stale pages or trackers, index/disk consistency, count drift, or a lint pass. Also: as the first step of the automation runner's weekly scan, and before/after a session that created or moved pages.

## Steps

1. **Run the scan** from the vault root:
   ```bash
   python3 scripts/vault_hygiene.py            # human-readable report
   python3 scripts/vault_hygiene.py --summary   # one line per check
   python3 scripts/vault_hygiene.py --json      # machine-readable
   ```
   It reuses `scripts/vault_parsers.py` (`extract_wikilinks` / `parse_frontmatter` / `get_last_updated`) and reads every page under `wiki/`.

2. **The six checks** (each → ✅ PASS / ⚠️ WARN / ❌ FAIL):
   - **link-integrity** — every `[[wikilink]]` resolves to an existing page; no self-links (§3.3); no casing mismatches. Unresolved links surface as WARN (could be an allowed forward-link per §3.3, OR a typo — the human judges).
   - **index-sync** — every `wiki/` file has an `index.md` row, and every index row points to a real file (FAIL on a dead catalog link).
   - **count-drift** — actual dir counts vs `index.md` section row counts vs the `~N` hints in the `agent-onboarding` skill (the exact drift class we hand-fix).
   - **frontmatter** — company pages have `type` / `tickers` / a valid `YYYY-MM-DD` `last_updated`; tier values are sane.
   - **staleness** — pages older than per-type thresholds (companies 90d / trackers 30d / else 120d).
   - **tracker-freshness** — the 5 trackers vs a 30-day threshold (called out from staleness).

3. **Interpret + flag (honest-verdict).** Lead with anything actionable: a `❌ FAIL` (real defect) first, then `⚠️ WARN`s worth a human look (typo-looking unresolved links, stale trackers). Self-links are a known, low-severity, pervasive WARN — note the count, don't alarm. For each genuine defect, name the file and the fix, and say plainly it's a human-gated change.

## Output

A scannable report: overall status, the six check lines, and the specific findings (which pages, which links, which counts). End by naming the top 1–3 things worth a human fix, or "vault clean" if all PASS. Remind once that this is read-only — nothing was edited.

## What this skill is NOT

- Not a fixer — it flags; the human (or a separate human-gated action) repairs.
- Not a canon writer — never touches `wiki/` / `index.md` / `log.md`.
- Not the calibration sweep (that's `calibration-check`, the self-evaluation loop).
