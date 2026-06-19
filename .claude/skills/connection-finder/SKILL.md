---
name: connection-finder
description: Scan the stocks-wiki vault and surface candidate cross-page connections not yet captured by existing chokepoint, theme, or relationship pages. Use this skill whenever the user asks about uncaptured analytical patterns, candidate new chokepoint or theme pages, cross-company relationships not yet synthesized, what connections exist between vault tickers, which ticker clusters might warrant a new page, what patterns are emerging across the vault, or which existing pages need refresh because new tickers should be added. Trigger on phrases like "find connections", "what cross-vault patterns", "candidate chokepoints", "what relationships are missing", "which tickers cluster together", "surface new themes", "what should we synthesize next", "any uncaptured patterns", "connection candidates", "refresh candidates for pages", "which pages need updating", or any question about analytical patterns across multiple vault tickers that don't yet have a dedicated page or that fall outside an existing page's frontmatter scope. The skill SURFACES candidates only — it does NOT write pages. Page synthesis is agent reasoning work that follows this skill's output.
---

# Connection finder — stocks-wiki cross-vault pattern surfacing

This skill returns a 3-section ranked list of candidate cross-page connections not yet captured by existing chokepoint, theme, or relationship pages. It exists because the vault has 31+ company pages plus 9 chokepoints + 8 themes + 1 relationship page, and new analytical synthesis opportunities (like the S57 BTM-grid-bypass-workaround.md chokepoint that connected BE+FCEL+GEV+CAT) only become visible when co-mention density is measured systematically across the full graph.

The deterministic boundary is critical: this skill SURFACES candidates with evidence. It does NOT write chokepoint, theme, or relationship pages. Page synthesis is agent reasoning work that follows the skill's output, validated against CLAUDE.md v9 Sections 3.12 (theme types) + 3.14 (paired ingests) + 3.15 (Pathway 1/2 chokepoint creation) page-type rules.

## When to invoke

Invoke this skill when the user asks any question about uncaptured analytical patterns or cross-page connection candidates. The skill is the right tool whenever the question would otherwise require manually scanning all 31+ company pages for co-mention patterns.

Examples of questions that should trigger this skill:
- "Find connections across the vault"
- "What cross-vault patterns haven't we synthesized yet?"
- "Are there candidate chokepoint pages we're missing?"
- "Which tickers cluster together?"
- "What should we synthesize next?"
- "Any emerging themes across the power infrastructure pages?"
- "Surface relationship candidates"
- "What patterns are emerging since the last session?"
- "Which existing pages need refresh — what tickers should be added?"

## Workflow

Execute these steps in order:

### 1. Verify vault state

Confirm `scripts/find_connections.py` and `scripts/vault_parsers.py` exist. If absent, the workhorse needs to be built first — surface that as a prerequisite gap and stop.

### 2. Run the connection-finder workhorse script

Execute via Bash from the vault root:

```bash
python scripts/find_connections.py
```

Optional flags:
- `--vault-root /path/to/vault` — override vault root (default: cwd)
- `--top-n 5` — cap per section (default: 5)
- `--min-score 3.0` — minimum raw co-mention score for cluster membership (default: 3.0; try 5.0 for tighter HIGH SIGNAL)
- `--no-recency` — disable recency weighting (treat all pages as equally recent)
- `--debug` — emit diagnostic counts to stderr

Dismissed-candidate memory (kills recurring noise):
- `--dismiss AVGO,NVT --reason "..."` — retire a cluster Vic has judged "not worth a page"; it stops surfacing as HIGH SIGNAL on every future scan.
- `--list-dismissed` — show the curated skip-list.
- `--undismiss AVGO,NVT` — restore a cluster so it can surface again.

The skip-list lives in `scripts/find_connections_dismissed.json` (git-tracked, Vic-curated, fully reversible). A dismissed ticker-set is silently excluded from HIGH SIGNAL — so the same low-value cluster doesn't re-appear run after run, and (because the automation's `research_agenda.py --propose` mines this script) it also stops polluting the nightly "Proposed" queue. **When Vic says "dismiss that one" about a surfaced cluster, run `--dismiss` with his reason; never hand-edit the JSON by guessing.**

The script:
1. Loads all wiki pages (companies + chokepoints + themes + relationships)
2. Builds co-mention matrix across all pages (weighted: +2 for reciprocal company-page wikilinks, +1 for shared non-company-page mentions, +1 for plaintext on company pages)
3. Identifies already-captured pairs from non-company page frontmatter + body wikilinks
4. Scores remaining pairs by raw_score × recency_factor (30d=1.0 / 90d=0.85 / 180d=0.70 / older=0.55)
5. **HIGH SIGNAL** — Density-constrained clustering of uncaptured pairs: each pair seeds a cluster; extension requires the new ticker to have qualifying-score edges to at least 2 existing cluster members (triangle requirement); max cluster size 5
6. **MEDIUM SIGNAL** — Per-page refresh candidates: for each chokepoint/theme/relationship page, finds external tickers (not in frontmatter) with high affinity (sum of co-mention scores) to existing page members
7. **LOW SIGNAL** — Count only: pairs already captured by an existing page
8. Suggests page type per HIGH SIGNAL cluster per CLAUDE.md v9 page-type rules

### 3. Apply vault context to output

The script output is deterministic signal. Before surfacing to Vic:
- Verify HIGH SIGNAL candidates against current vault context. A candidate cluster appearing as HIGH SIGNAL may already be substantively discussed on an existing page even if not formally captured in frontmatter — apply honest-verdict discipline.
- For MEDIUM SIGNAL refresh candidates: confirm the external ticker's primary-source evidence supports the page's analytical frame before recommending synthesis.
- Filter false positives where evident — co-mention density does not equal analytical meaningfulness.

### 4. Format output per template

The script output should already match the template below. If formatting deviates, normalize before returning to Vic.

## Output template

```
## Cross-vault connection candidates (YYYY-MM-DD)

**HIGH SIGNAL — new candidates not yet captured:**

1. TICKER_A + TICKER_B + TICKER_C (cluster_score: N.N) — suggested: [chokepoint|theme|relationship]
   Evidence:
     - TICKER_A↔TICKER_B raw_score=N (recency×0.NN)
     - TICKER_A↔TICKER_C raw_score=N (recency×0.NN)
   Tier context: [descriptive tier placement per ticker, e.g., "Photonics Tier 2 component supplier [[COHR]]"]
   Rationale: [page-type suggestion rationale]

[top 5 by cluster_score; "and N more" footer]

**MEDIUM SIGNAL — refresh candidates (extend existing pages):**

1. [[existing-page-name]] (page_type; N existing tickers)
   External candidates to consider for refresh: [[TICKER_X]] (affinity N.N), [[TICKER_Y]] (affinity N.N)
   Top candidate [[TICKER_X]] supported by co-mentions with: [[T1]] score=N.N, [[T2]] score=N.N

[top 5 by top-candidate-affinity; "and N more" footer]

**LOW SIGNAL — captured (no action needed):** N pairs already appear in existing chokepoint/theme/relationship pages.
```

## Output discipline

- Concise output. Do not append analytical commentary beyond the template unless Vic explicitly asks for elaboration. The skill exists for fast candidate surfacing, not synthesis.
- Apply descriptive language convention per CLAUDE.md preamble: pair tier numbers with descriptive scope ("Photonics Tier 2 component supplier", "Energy/Power Tier 1 critical infrastructure").
- For MEDIUM SIGNAL: name the specific existing page to refresh, not a generic instruction.
- Date format YYYY-MM-DD consistently.

## Scope boundary — what this skill does NOT do

- Does NOT write chokepoint, theme, relationship, or company pages
- Does NOT synthesize narratives or analytical prose
- Does NOT validate connection meaningfulness — that is agent reasoning work
- Does NOT access external APIs or networks (pure local analysis)
- Does NOT modify any wiki files
- Does NOT ingest new primary sources
- Does NOT apply CLAUDE.md Section 3.15 Pathway 1/2 chokepoint criteria — it surfaces score and suggests type; agent applies criteria
- Does NOT apply CLAUDE.md Section 3.10 Outside Framework placement four-criterion test
- Does NOT decide whether a candidate cluster meets the Section 3.15 multi-source threshold for canonical creation
- Does NOT determine tier placements for any company

The skill produces a ranked evidence list. All analytical judgment is reserved for the agent session that follows the skill's output.

## Source-of-truth discipline

This skill maintains *almost* zero static state. All signals derive from current vault file state at time of invocation (same vault state produces same output, deterministic), and the script reads company pages directly via `wiki/companies/*.md` glob — no ticker list to maintain. The **one** piece of curated state is `scripts/find_connections_dismissed.json` — the Vic-curated skip-list of clusters not worth re-surfacing (managed via `--dismiss` / `--undismiss`, fully reversible).

When new company pages are added to `wiki/companies/`, they automatically participate in the next scan. No SKILL.md update required for new tickers. Same applies to new chokepoint/theme/relationship pages — they automatically participate in captured-pair detection.

## Maintenance

This skill requires SKILL.md updates if:
- Output format conventions change at chat-side or via codification session
- Workhorse script location changes from `scripts/find_connections.py`
- Scoring formula or clustering algorithm changes substantively
- New page types are introduced (currently: companies / chokepoints / themes / relationships / layers)

The workhorse script (`scripts/find_connections.py`) is where co-mention weights, score thresholds, cluster algorithm parameters, and recency factors live. Updates to those operational parameters happen in the script, not in SKILL.md.

## Known limitations

- High-degree tickers (NVDA, TSM, AVGO) participate in many pairs by structural prominence; cluster scores may over-represent their importance. The captured-pair zeroing for HIGH SIGNAL mitigates this for already-captured connections, but unmade connections involving high-degree tickers may still surface prominently — agent applies discretion.
- "Affinity" in MEDIUM SIGNAL is sum of co-mention scores; it doesn't validate whether the external ticker has thesis-relevant exposure to the page's domain. A ticker can have high mechanical affinity but weak domain fit — that's honest-verdict agent work.
- Page-type suggestion uses keyword heuristics over section headers + first-500-chars of body. It's a starting hypothesis, not a binding designation; agent validates against CLAUDE.md Sections 3.12-3.15.
- Connected-components clustering was rejected in favor of density-constrained triangle-extension clustering because the dense vault graph caused single-component explosions. Current clustering caps at 5 tickers per cluster and requires ≥2 qualifying edges for extension.
