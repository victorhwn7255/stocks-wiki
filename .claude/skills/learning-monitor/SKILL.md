---
name: learning-monitor
description: Surface the current accumulation state of codified monitoring patterns across the stocks-wiki vault — count instances per pattern, flag threshold crossings (codification candidates), and detect drift vs MEMORY.md tracked counts. Use this skill whenever the user asks about pattern accumulation, codification readiness, which patterns are at threshold, what patterns are due for codification, vault learning state, monitoring counts, MEMORY.md drift, or any question about inter-session learning state. Trigger on phrases like "monitor patterns", "what patterns are at threshold", "codification readiness", "are we due for codification", "pattern accumulation state", "what's accumulated since last codification", "is MEMORY.md current", "check learning monitor", "what patterns hit threshold", "scan for codification candidates". The skill SCANS and COUNTS — it does NOT codify patterns (that's codification-session agent work) and does NOT propose new patterns (that's analytical work).
---

# Learning monitor — pattern accumulation state surfacing

This skill operationalizes **inter-session learning** — the phenomenon of monitoring-pattern accumulation across many ingest sessions. Patterns get annotated in Source audit notes + Change log entries as they occur; their cumulative counts get tracked in log.md "Convention counts" blocks within Phase 4 reflection. Both sources drift relative to MEMORY.md if not periodically reconciled.

Without systematic surfacing, pattern visibility depends on what the agent reads in any given session: a pattern is only "visible" if the current session touches the pages where it lives. `learning-monitor` makes the codification-readiness signal **queryable on demand** by scanning both log.md (authoritative Vic-curated counts) and wiki page annotations (supplementary evidence).

The deterministic boundary is critical: this skill SCANS and COUNTS. It does NOT codify patterns (that's the codification-session work that updates `CLAUDE.md` + `frameworks.md`). It does NOT propose new patterns (that's analytical work; preserves Vic's ownership of pattern naming).

## When to invoke

Invoke this skill when the user asks any question about pattern accumulation state, codification readiness, or MEMORY.md drift. The skill is the right tool whenever the question would otherwise require manually grepping wiki content for codified pattern annotations or scanning log.md tails to assemble cumulative counts.

Examples of questions that should trigger this skill:
- "What patterns are at codification threshold?"
- "Are we due for codification?"
- "Pattern accumulation state"
- "Monitor patterns"
- "Is MEMORY.md current?"
- "What patterns hit threshold since last codification?"
- "What patterns are accumulating?"
- "Codification readiness check"
- "What's at 3 instances and ready to codify?"

## Workflow

Execute these steps in order:

### 1. Verify vault state

Confirm `scripts/monitor_patterns.py` and `scripts/vault_parsers.py` exist. If absent, the workhorse needs to be built first — surface that as a prerequisite gap and stop.

### 2. Run the learning-monitor workhorse script

Execute via Bash from the vault root:

```bash
python scripts/monitor_patterns.py
```

Optional flags:
- `--vault-root /path/to/vault` — override vault root (default: cwd)
- `--memory-path /path/to/MEMORY.md` — override MEMORY.md location (default: standard Claude Code memory path)
- `--full-body` — scan entire page body, not just Source audit notes + Change log
- `--debug` — emit diagnostic counts to stderr

The script's source-of-truth hierarchy:
1. **`log.md` "Convention counts" blocks** — authoritative Vic-curated counts (per Phase 4 reflection convention codified Session 38). Most recent session entry wins (descending-order log convention).
2. **Wiki page annotation scan** — supplementary; surfaces page mentions for verification. Used when log.md does not provide an explicit count for a pattern.
3. **`MEMORY.md` "Key framework facts" section** — drift baseline; often stale relative to vault state.

### 3. Apply vault context to output

The script output is deterministic signal. Before surfacing to Vic:
- Verify threshold-crossing patterns against current vault context. A pattern showing at threshold may already have been informally codified or addressed in a recent session — apply honest-verdict discipline.
- Drift annotations indicate MEMORY.md staleness; the agent decides whether MEMORY.md update is warranted (the skill does NOT auto-update MEMORY.md).
- For page-scan counts (where log.md doesn't provide an explicit count): treat as approximate — pages may *discuss* a pattern without representing a new instance. Verify by inspecting sample text.

### 4. Format output per template

The script output should already match the template below.

## Output template

```
## Learning monitor — pattern accumulation state (YYYY-MM-DD)

**Patterns at codification threshold (action needed):**
[patterns where vault_count >= threshold; with source attribution: log.md vs page-scan]

**Patterns approaching threshold (monitoring active):**
[patterns where 1 <= vault_count < threshold; "N more to trigger codification"]

**Running-count patterns (no codification threshold):**
[patterns with running counts: Aschenbrenner participants, A1 three-mode, Outside Framework, etc.]

**Drift vs MEMORY.md ({MEMORY.md path}):**
[table: pattern | vault | MEMORY.md | drift direction]

**Patterns codified but zero vault instances found:** [omitted if all patterns observed]
```

## Output discipline

- Concise output. Do not append analytical commentary beyond the template unless Vic explicitly asks for elaboration. The skill exists for fast accumulation-state surfacing, not synthesis.
- Apply descriptive language convention per CLAUDE.md preamble where applicable.
- Date format YYYY-MM-DD consistently.
- Always show source attribution per pattern: "(source: log.md)" for authoritative counts; "(source: page-scan)" for supplementary counts.
- For page-scan counts: include note when count likely over-represents instances ("Supplementary: N pages mention pattern").

## Scope boundary — what this skill does NOT do

- Does NOT codify new conventions in CLAUDE.md, frameworks.md, or MEMORY.md
- Does NOT propose new pattern candidates (no heuristic "this phrase repeats — codification candidate" output)
- Does NOT update MEMORY.md automatically when drift is detected — agent applies judgment
- Does NOT write to log.md
- Does NOT validate pattern meaningfulness — that is codification-session reasoning work
- Does NOT access external APIs or networks
- Does NOT modify any wiki files
- Does NOT decide whether a threshold-crossing pattern warrants codification — surfaces signal; agent applies CLAUDE.md Section 5.3 evolution discipline

The skill produces a counts-and-drift table. All codification judgment is reserved for the agent session that follows the skill's output.

## Source-of-truth discipline

This skill maintains zero static state. All signals derive from current vault file state at time of invocation. Same vault state produces same output (deterministic).

The pattern token registry lives at the top of `scripts/monitor_patterns.py` as `PATTERN_REGISTRY` — a list of dicts naming each codified pattern, its CLAUDE.md section reference, search tokens, filter tokens (negative-test markers to exclude), threshold, threshold type, scope, and MEMORY.md/log.md regex extraction patterns. When new patterns are codified at codification sessions, the registry must be updated.

## Maintenance

This skill requires script + SKILL.md updates if:
- New monitoring patterns are codified in CLAUDE.md (add to PATTERN_REGISTRY)
- Annotation phrasings change at codification sessions (update tokens/filter_tokens)
- MEMORY.md or log.md format conventions change (update parsers)
- Output format conventions change at chat-side

The workhorse script (`scripts/monitor_patterns.py`) is where the PATTERN_REGISTRY, token regexes, count-source hierarchy, and filtering logic live. Updates to those operational parameters happen in the script, not in SKILL.md.

## Known limitations

- **Page-scan over-counting.** For patterns without explicit log.md counts (e.g., Honest-verdict trigger discipline), the vault count reflects page MENTIONS, not confirmed INSTANCES. Pages discussing a pattern (e.g., "convention not triggered") may match despite filter tokens — the filter is line-level + proximity-based but cannot perfectly discriminate discussion from instance recording. Treat page-scan counts as approximate; verify samples.
- **Negative-test filter false negatives.** The universal filter list catches common negative-test phrasings ("not triggered", "UNCHANGED", "remains at", etc.) but may miss novel phrasings. Patterns may be over-counted if a negative-test phrasing isn't in the filter list.
- **MEMORY.md staleness.** MEMORY.md auto-loaded at session start is updated by the agent at session end via persistence — but counts often lag actual vault state. Drift values indicate the gap; agent decides whether to update MEMORY.md.
- **Log.md regex precision.** The log.md count parser regex requires specific phrasings (typically `**N**` formatting per Convention counts block convention). Phrasing drift across sessions may cause some patterns to fall back to page-scan when log.md should be authoritative.
- **No new-pattern discovery.** v1 is strictly scan-and-count for already-codified patterns. Emergent patterns require Vic's analytical noticing + codification session formalization, not skill-side heuristic surfacing.
