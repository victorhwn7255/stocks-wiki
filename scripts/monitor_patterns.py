#!/usr/bin/env python3
"""
monitor_patterns.py — Surface codified pattern accumulation state across the
stocks-wiki vault. Orchestrated by the `learning-monitor` skill.

Operationalizes inter-session learning: scans wiki/**/*.md + log.md for
codified monitoring-pattern annotation tokens, counts current instances,
compares against MEMORY.md tracked counts, and flags threshold crossings.

Deterministic: same vault state -> same output. Pure local analysis.

Usage:
    python scripts/monitor_patterns.py
    python scripts/monitor_patterns.py --vault-root /path/to/stocks-wiki
    python scripts/monitor_patterns.py --full-body   # scan body, not just SAN+CL
    python scripts/monitor_patterns.py --debug

Requires: PyYAML.
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from vault_parsers import (  # noqa: E402
    extract_change_log_section,
    extract_source_audit_notes_section,
    parse_frontmatter,
    read_page,
)


# Default MEMORY.md location for drift comparison.
DEFAULT_MEMORY_PATH = Path.home() / ".claude" / "projects" / (
    "-Users-victor-he-Downloads-Code-stocks-wiki"
) / "memory" / "MEMORY.md"


# ---------------------------------------------------------------------------
# PATTERN REGISTRY — the core data structure of this skill
# ---------------------------------------------------------------------------
#
# Each pattern dict contains:
#   id:               internal identifier (snake_case)
#   name:             human-readable display name
#   claude_md_ref:    CLAUDE.md section reference
#   tokens:           list of regex patterns (case-insensitive) to count
#   filter_tokens:    list of regex patterns to EXCLUDE (negative-test phrases)
#   threshold:        int — codification threshold; None for running-count patterns
#   threshold_type:   "codification" | "running_count"
#   scope:            "page_san_cl" (Source audit notes + Change log)
#                     | "page_full" (entire body)
#                     | "log_md" (parse from log.md only)
#                     | "frontmatter" (frontmatter tier-field check)
#   memory_token:     regex matched in MEMORY.md "Key framework facts" to extract count
#   sub_patterns:     optional list of {id, name, tokens} sub-patterns
# ---------------------------------------------------------------------------


PATTERN_REGISTRY: list[dict] = [
    {
        "id": "tier1_tier2_framing_gap",
        "name": "Tier 1/Tier 2 framing gap",
        "claude_md_ref": "Section 3.4",
        "tokens": [r"Tier 1\s*/\s*Tier 2 framing gap"],
        "filter_tokens": [
            r"not triggered",
            r"no clear (?:sixth|new) instance",
            r"UNCHANGED",
            r"remains at",
            r"still at",
        ],
        "threshold": 3,
        "threshold_type": "codification",
        "scope": "page_san_cl",
        "memory_token": r"Tier 1/Tier 2 framing gap[:\s]+(\d+)\s+counted",
        "sub_patterns": [
            {"id": "risk_framing", "name": "risk-framing", "tokens": [r"risk-framing"]},
            {
                "id": "customer_concentration",
                "name": "customer-concentration",
                "tokens": [r"customer-concentration"],
            },
            {
                "id": "geographic_concentration",
                "name": "geographic-concentration",
                "tokens": [r"geographic-concentration"],
            },
        ],
    },
    {
        "id": "ceo_combativeness",
        "name": "CEO combativeness",
        "claude_md_ref": "Section 3.7",
        "tokens": [r"CEO combativeness", r"combative management passage"],
        "filter_tokens": [
            r"not triggered",
            r"convention not triggered",
            r"remains at 2 instances",
            r"UNCHANGED",
        ],
        "threshold": 3,
        "threshold_type": "codification",
        "scope": "page_san_cl",
        "memory_token": r"CEO combativeness[^.]*?(\d+)\s+current",
    },
    {
        "id": "reciprocal_non_naming",
        "name": "Reciprocal non-naming",
        "claude_md_ref": "MEMORY.md monitoring",
        "tokens": [r"reciprocal non-naming"],
        "filter_tokens": [r"UNCHANGED"],
        "threshold": None,
        "threshold_type": "running_count",
        "scope": "page_san_cl",
        "memory_token": r"Reciprocal non-naming[:\s]+(\d+)\s+active",
    },
    {
        "id": "cross_venue_disclosure_gap",
        "name": "Cross-venue disclosure gap",
        "claude_md_ref": "Section 3.6",
        "tokens": [r"[Cc]ross-venue disclosure gap", r"[Cc]ross-venue gap"],
        "filter_tokens": [r"UNCHANGED", r"remains at"],
        "threshold": 3,
        "threshold_type": "codification",
        "scope": "page_san_cl",
        "memory_token": r"Cross-venue[^.]*?(\d+)",
    },
    {
        "id": "a6_g_gprime",
        "name": "A6 sub-pattern (g)/(g') kickoff verification variance",
        "claude_md_ref": "Section 4.5",
        "tokens": [r"A6\s*\(g\)", r"A6\s*\(g'\)"],
        "filter_tokens": [
            r"UNCHANGED",
            r"count\s+remains",
            r"no new",
        ],
        "threshold": 5,
        "threshold_type": "codification",
        "scope": "page_san_cl",
        "memory_token": r"A6[^.]*?(?:g\)/\(g')[^.]*?(\d+)",
    },
    {
        "id": "a6_h",
        "name": "A6 sub-pattern (h) source filename verification",
        "claude_md_ref": "Section 4.5",
        "tokens": [r"A6\s*\(h\)"],
        "filter_tokens": [r"UNCHANGED"],
        "threshold": 3,
        "threshold_type": "codification",
        "scope": "page_san_cl",
        "memory_token": r"A6\s*\(h\)[^.]*?(\d+)",
    },
    {
        "id": "a1_three_mode",
        "name": "A1 three-mode framing (counterparty-attribution-only)",
        "claude_md_ref": "Section 3.5",
        "tokens": [
            r"counterparty-attribution-only",
            r"three-mode framing",
        ],
        "filter_tokens": [],
        "threshold": None,
        "threshold_type": "running_count",
        "scope": "page_san_cl",
        "memory_token": None,
        "sub_patterns": [
            {"id": "over_claim", "name": "over-claim", "tokens": [r"\bover-claim\b"]},
            {"id": "inversion", "name": "inversion mode", "tokens": [r"\binversion\b"]},
            {
                "id": "reciprocal_confirmation",
                "name": "reciprocal-confirmation",
                "tokens": [r"reciprocal-confirmation"],
            },
        ],
    },
    {
        "id": "honest_verdict_trigger",
        "name": "Honest-verdict trigger discipline",
        "claude_md_ref": "Section 3.10",
        "tokens": [
            r"honest-verdict trigger",
            r"honest-verdict discipline",
        ],
        "filter_tokens": [
            r"not triggered",
            r"not firing",
            r"NOT firing",
        ],
        "threshold": 3,
        "threshold_type": "codification",
        "scope": "page_san_cl",
        "memory_token": None,
    },
    {
        "id": "outside_framework_placement",
        "name": "Outside Framework placement",
        "claude_md_ref": "Section 3.10",
        "tokens": [],  # handled via frontmatter scope
        "filter_tokens": [],
        "threshold": None,
        "threshold_type": "running_count",
        "scope": "frontmatter",
        "memory_token": None,
        "sub_patterns": [
            {"id": "outside_photonics", "name": "Outside photonics", "tokens": []},
            {"id": "outside_energy_power", "name": "Outside energy/power", "tokens": []},
            {"id": "outside_equipment", "name": "Outside equipment", "tokens": []},
            {"id": "outside_materials", "name": "Outside materials", "tokens": []},
        ],
    },
    {
        "id": "aschenbrenner_participants",
        "name": "Cross-vault Aschenbrenner thesis participants",
        "claude_md_ref": "log.md tracking",
        "tokens": [r"Aschenbrenner"],
        "filter_tokens": [],
        "threshold": None,
        "threshold_type": "running_count",
        "scope": "log_md",
        "memory_token": None,
    },
    {
        "id": "btm_workaround_participants",
        "name": "BTM grid-bypass workaround participants",
        "claude_md_ref": "Section 3.15 Pathway 2 (S57)",
        "tokens": [r"BTM[- ]grid-bypass", r"grid-bypass workaround"],
        "filter_tokens": [],
        "threshold": None,
        "threshold_type": "running_count",
        "scope": "page_san_cl",
        "memory_token": None,
    },
]


# ---------------------------------------------------------------------------
# Page loading
# ---------------------------------------------------------------------------


PAGE_TYPE_DIRS = {
    "company": "wiki/companies",
    "chokepoint": "wiki/chokepoints",
    "theme": "wiki/themes",
    "relationship": "wiki/relationships",
    "layer": "wiki/layers",
}


def load_all_pages(vault_root: Path) -> dict[str, dict]:
    """Load all wiki pages + log.md into a keyed dict.

    Keys are filename stems (uppercase for company pages). log.md is stored
    under key 'LOG'. Each value is a dict with {path, type, fm, body, san, cl}.
    """
    pages: dict[str, dict] = {}
    for page_type, subdir in PAGE_TYPE_DIRS.items():
        dir_path = vault_root / subdir
        if not dir_path.is_dir():
            continue
        for md_file in sorted(dir_path.glob("*.md")):
            fm, body = read_page(md_file)
            if not body:
                continue
            key = md_file.stem.upper() if page_type == "company" else md_file.stem
            pages[key] = {
                "path": md_file,
                "type": page_type,
                "fm": fm,
                "body": body,
                "san": extract_source_audit_notes_section(body),
                "cl": extract_change_log_section(body),
            }
    log_path = vault_root / "log.md"
    if log_path.is_file():
        try:
            log_body = log_path.read_text(encoding="utf-8")
            pages["LOG"] = {
                "path": log_path,
                "type": "log",
                "fm": {},
                "body": log_body,
                "san": "",
                "cl": "",
            }
        except (OSError, UnicodeDecodeError):
            pass
    return pages


# ---------------------------------------------------------------------------
# Pattern scanning
# ---------------------------------------------------------------------------


def _get_scan_text(page: dict, scope: str, full_body: bool) -> str:
    """Return the text region of the page to scan per pattern scope."""
    if scope == "page_full" or full_body:
        return page["body"]
    if scope == "page_san_cl":
        return page["san"] + "\n" + page["cl"]
    if scope == "log_md":
        return page["body"] if page["type"] == "log" else ""
    return ""


CONTEXT_WINDOW = 200  # chars before+after a match to scan for negative markers


# Universal negative-test markers applied to all patterns (in addition to
# pattern-specific filter_tokens). These phrases indicate the page is
# DISCUSSING a pattern's non-occurrence, not recording a new instance.
UNIVERSAL_FILTER_TOKENS = [
    r"NOT triggered",
    r"not triggered",
    r"NOT firing",
    r"not firing",
    r"NOT combative",
    r"\bnot combative\b",
    r"ZERO new",
    r"no new instance",
    r"no clear (?:new|sixth|next)",
    r"\bno new\b",
    r"convention not triggered",
    r"remains at",
    r"unchanged",
    r"UNCHANGED",
    r"awaiting (?:a |the )?(?:third|next) instance",
]


def _context_passes_filters(
    text: str, match_start: int, match_end: int, filter_tokens: list[str]
) -> bool:
    """Return True if the match's local context contains NO filter tokens.

    Checks a window of CONTEXT_WINDOW chars before and after the match position.
    This handles negative-test phrases that span multiple sentences/lines in a
    long Source audit notes paragraph (e.g., "ZERO new CEO combativeness instances
    observed in Q1 2026").
    """
    window_start = max(0, match_start - CONTEXT_WINDOW)
    window_end = min(len(text), match_end + CONTEXT_WINDOW)
    context = text[window_start:window_end]
    combined_filters = UNIVERSAL_FILTER_TOKENS + filter_tokens
    for ftok in combined_filters:
        if re.search(ftok, context, re.IGNORECASE):
            return False
    return True


def _count_pattern_matches_in_text(
    text: str, tokens: list[str], filter_tokens: list[str]
) -> tuple[int, list[str]]:
    """Count distinct match positions, applying proximity-based filtering.

    Returns (match_count_minus_duplicates, sample_snippets up to 5).
    Matches are deduplicated by extracted snippet (±60 chars around match)
    to avoid double-counting near-identical mentions within a single page.
    """
    if not tokens:
        return 0, []
    combined = "|".join(f"(?:{t})" for t in tokens)
    matcher = re.compile(combined, re.IGNORECASE)
    seen_snippets: set[str] = set()
    samples: list[str] = []
    for m in matcher.finditer(text):
        if not _context_passes_filters(text, m.start(), m.end(), filter_tokens):
            continue
        snippet_start = max(0, m.start() - 60)
        snippet_end = min(len(text), m.end() + 60)
        snippet = text[snippet_start:snippet_end].strip()
        # Normalize whitespace for dedup
        normalized = re.sub(r"\s+", " ", snippet)
        if normalized in seen_snippets:
            continue
        seen_snippets.add(normalized)
        if len(samples) < 5:
            samples.append(snippet[:160])
    return len(seen_snippets), samples


def scan_pattern(
    pattern: dict, pages: dict[str, dict], full_body: bool = False
) -> dict:
    """Scan all pages for one pattern; return result dict.

    Result keys:
      pattern_id, name, vault_count, sub_pattern_counts (dict id->count),
      matching_pages (list of page keys), samples (list of line samples).

    For "frontmatter" scope: special-case — count pages whose frontmatter
    contains tier-fields with value "outside".
    """
    result = {
        "pattern_id": pattern["id"],
        "name": pattern["name"],
        "vault_count": 0,
        "sub_pattern_counts": {},
        "matching_pages": [],
        "samples": [],
    }
    if pattern["scope"] == "frontmatter":
        return _scan_frontmatter_outside(pattern, pages, result)

    matching_pages: list[str] = []
    all_samples: list[str] = []
    for key, page in pages.items():
        if pattern["scope"] == "log_md" and page["type"] != "log":
            continue
        if pattern["scope"] != "log_md" and page["type"] == "log":
            continue
        scan_text = _get_scan_text(page, pattern["scope"], full_body)
        if not scan_text:
            continue
        count, samples = _count_pattern_matches_in_text(
            scan_text, pattern["tokens"], pattern["filter_tokens"]
        )
        if count > 0:
            matching_pages.append(key)
            for s in samples[:2]:
                all_samples.append(f"{key}: {s}")
    result["matching_pages"] = matching_pages
    result["samples"] = all_samples[:8]
    # For log_md scope: count is the total LINES matched in log.md (e.g., Aschenbrenner)
    # For page scope: count is number of pages with at least one match
    if pattern["scope"] == "log_md":
        log_page = pages.get("LOG")
        if log_page:
            total_lines, _ = _count_pattern_matches_in_text(
                log_page["body"], pattern["tokens"], pattern["filter_tokens"]
            )
            result["vault_count"] = total_lines
        else:
            result["vault_count"] = 0
    else:
        result["vault_count"] = len(matching_pages)

    # Sub-pattern counts (page-scoped only; sum per-page sub-pattern matches)
    sub_patterns = pattern.get("sub_patterns") or []
    for sub in sub_patterns:
        sub_pages = 0
        sub_tokens = sub.get("tokens") or []
        if not sub_tokens:
            continue
        for key in matching_pages:
            page = pages[key]
            scan_text = _get_scan_text(page, pattern["scope"], full_body)
            count, _ = _count_pattern_matches_in_text(
                scan_text, sub_tokens, pattern["filter_tokens"]
            )
            if count > 0:
                sub_pages += 1
        result["sub_pattern_counts"][sub["id"]] = sub_pages

    return result


def _scan_frontmatter_outside(
    pattern: dict, pages: dict[str, dict], result: dict
) -> dict:
    """Special scan: count pages with `*_tier: outside` frontmatter values."""
    tier_fields = [
        ("photonics_tier", "outside_photonics"),
        ("energy_power_tier", "outside_energy_power"),
        ("equipment_tier", "outside_equipment"),
        ("materials_tier", "outside_materials"),
    ]
    sub_counts: dict[str, int] = {sub_id: 0 for _, sub_id in tier_fields}
    matching_pages: set[str] = set()
    samples: list[str] = []
    for key, page in pages.items():
        if page["type"] != "company":
            continue
        fm = page["fm"]
        for field, sub_id in tier_fields:
            val = fm.get(field)
            if isinstance(val, str) and val.lower() == "outside":
                sub_counts[sub_id] += 1
                matching_pages.add(key)
                if len(samples) < 6:
                    samples.append(f"{key}: {field}=outside")
    result["vault_count"] = len(matching_pages)
    result["sub_pattern_counts"] = sub_counts
    result["matching_pages"] = sorted(matching_pages)
    result["samples"] = samples
    return result


# ---------------------------------------------------------------------------
# log.md convention-count parsing (authoritative source for codified counts)
# ---------------------------------------------------------------------------
#
# Recent log.md session entries contain Phase 4 reflection blocks with explicit
# convention counts. These are Vic-curated authoritative values, more reliable
# than page-mention scans. Format examples (from log.md sessions 54-59):
#
#   - Tier 1/Tier 2 framing gap: **6 + 1 obs** (unchanged)
#   - CEO combativeness: **2** (unchanged; Murphy + Hock Tan)
#   - A6 (g)/(g') subtype: **8 + 2 = 10 combined** (unchanged)
#   - Cross-vault Aschenbrenner thesis pattern: **19+ participants** post-S59
#
# Each pattern's log_token regex extracts the count from these blocks.
# ---------------------------------------------------------------------------


LOG_COUNT_TOKENS = {
    "tier1_tier2_framing_gap": (
        r"Tier 1/Tier 2 framing gap:\s*\*\*(\d+)(?:\s*\+\s*\d+\s*obs)?\*\*"
    ),
    "ceo_combativeness": r"CEO combativeness:\s*\*\*(\d+)\*\*",
    "a6_g_gprime": r"A6 \(g\)/\(g'\)[^*]*?\*\*[\d\s+=]*?(\d+)\s+combined\*\*",
    "a6_h": r"A6 \(h\)[^*\n]*?\*\*(\d+)\s*(?:instance)?\*\*",
    "aschenbrenner_participants": (
        # Match both Convention-counts colon format AND narrative "strengthens to"
        # format. log.md is descending-order (most recent at top) so first match wins.
        r"Aschenbrenner thesis pattern(?:\s+strengthens to|:)\s*\*\*(\d+)\+?"
    ),
    "reciprocal_non_naming": r"[Rr]eciprocal non-naming:\s*\*\*(\d+)",
    "cross_venue_disclosure_gap": (
        r"[Cc]ross-venue (?:disclosure )?gap:\s*\*\*(\d+)"
    ),
    "btm_workaround_participants": (
        # Match either explicit count in Phase 4 reflection or 4-participant phrase
        r"BTM grid-bypass[^*\n]{0,200}\*\*(\d+)[- ]participant"
        r"|"
        r"(\d+)-participant cross-vault BTM grid-bypass"
    ),
    "honest_verdict_trigger": (
        r"[Hh]onest-verdict trigger discipline[^*\n]*?\*\*(\d+)\s+instance"
    ),
}


def parse_log_convention_counts(log_path: Path) -> dict[str, int | None]:
    """Parse log.md for most-recent explicit pattern counts (defined below)."""
    counts: dict[str, int | None] = {p["id"]: None for p in PATTERN_REGISTRY}
    if not log_path.is_file():
        return counts
    try:
        text = log_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return counts

    for pattern_id, token_regex in LOG_COUNT_TOKENS.items():
        m = re.search(token_regex, text)
        if m:
            # Patterns may have multiple capture groups (e.g., BTM with alternation);
            # take the first non-None group.
            for g in m.groups():
                if g:
                    try:
                        counts[pattern_id] = int(g)
                        break
                    except (ValueError, IndexError):
                        pass
    return counts


# ---------------------------------------------------------------------------
# MEMORY.md drift parsing
# ---------------------------------------------------------------------------


def parse_memory_counts(memory_path: Path) -> dict[str, int | None]:
    """Parse MEMORY.md 'Key framework facts' section for tracked pattern counts.

    Returns dict mapping pattern_id -> tracked_count (or None if pattern not found).
    Uses each pattern's memory_token regex to extract the count.
    """
    counts: dict[str, int | None] = {p["id"]: None for p in PATTERN_REGISTRY}
    if not memory_path.is_file():
        return counts
    try:
        text = memory_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return counts

    # Extract "Key framework facts" section
    section_match = re.search(
        r"##\s+Key framework facts[^\n]*\n(.*?)(?=\n##\s+|\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_match:
        # Fall back to full file scan
        section_text = text
    else:
        section_text = section_match.group(1)

    for pattern in PATTERN_REGISTRY:
        token = pattern.get("memory_token")
        if not token:
            continue
        # Try Key framework facts section first; if no match, fall back to the
        # full MEMORY.md text. Some patterns (e.g., CEO combativeness in this
        # vault's MEMORY.md) are tracked in the Backlog items section instead.
        m = re.search(token, section_text, re.IGNORECASE | re.DOTALL)
        if not m and section_text is not text:
            m = re.search(token, text, re.IGNORECASE | re.DOTALL)
        if m:
            try:
                counts[pattern["id"]] = int(m.group(1))
            except (ValueError, IndexError):
                pass
    return counts


# ---------------------------------------------------------------------------
# Drift computation + classification
# ---------------------------------------------------------------------------


def compute_drift(
    scan_results: list[dict], memory_counts: dict[str, int | None]
) -> list[dict]:
    """Annotate each scan result with drift vs MEMORY.md."""
    out = []
    for r in scan_results:
        pid = r["pattern_id"]
        memory_count = memory_counts.get(pid)
        if memory_count is None:
            drift = None
            direction = "untracked"
        else:
            drift = r["vault_count"] - memory_count
            if drift > 0:
                direction = "vault ahead"
            elif drift < 0:
                direction = "memory ahead"
            else:
                direction = "equal"
        out.append({**r, "memory_count": memory_count, "drift": drift, "direction": direction})
    return out


def classify_patterns(annotated: list[dict]) -> dict[str, list[dict]]:
    """Bucket patterns by status: at_threshold / approaching / running_count / unobserved."""
    buckets = {
        "at_threshold": [],
        "approaching": [],
        "running_count": [],
        "unobserved": [],
    }
    for r in annotated:
        # Look up threshold from the registry
        pattern = next((p for p in PATTERN_REGISTRY if p["id"] == r["pattern_id"]), None)
        if pattern is None:
            continue
        threshold = pattern.get("threshold")
        threshold_type = pattern.get("threshold_type")
        vault_count = r["vault_count"]
        if vault_count == 0:
            buckets["unobserved"].append(r)
        elif threshold_type == "codification" and threshold is not None:
            if vault_count >= threshold:
                buckets["at_threshold"].append(r)
            else:
                buckets["approaching"].append(r)
        else:
            buckets["running_count"].append(r)
    # Sort each bucket
    buckets["at_threshold"].sort(key=lambda r: -r["vault_count"])
    buckets["approaching"].sort(key=lambda r: -r["vault_count"])
    buckets["running_count"].sort(key=lambda r: -r["vault_count"])
    return buckets


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------


def _format_drift_annotation(r: dict) -> str:
    """Build a short drift annotation string for a result."""
    mc = r["memory_count"]
    drift = r["drift"]
    direction = r["direction"]
    if direction == "untracked":
        return "MEMORY.md: untracked"
    if direction == "equal":
        return f"MEMORY.md: {mc} | drift: 0 (equal)"
    sign = "+" if drift > 0 else ""
    return f"MEMORY.md: {mc} | drift: {sign}{drift} ({direction})"


def _format_sub_patterns(r: dict, pattern: dict) -> str:
    """Format sub-pattern counts for a pattern that has them."""
    sub_patterns = pattern.get("sub_patterns") or []
    if not sub_patterns or not r["sub_pattern_counts"]:
        return ""
    parts = []
    for sub in sub_patterns:
        count = r["sub_pattern_counts"].get(sub["id"], 0)
        parts.append(f"{sub['name']}: {count}")
    return " | ".join(parts)


def format_report(
    buckets: dict[str, list[dict]],
    annotated: list[dict],
    memory_path: Path,
    scan_date: date,
) -> str:
    """Format the 4-section markdown report."""
    today_str = scan_date.strftime("%Y-%m-%d")
    out = [f"## Learning monitor — pattern accumulation state ({today_str})", ""]

    # --- AT THRESHOLD (action needed) ---
    out.append("**Patterns at codification threshold (action needed):**")
    if buckets["at_threshold"]:
        for r in buckets["at_threshold"]:
            pattern = next(p for p in PATTERN_REGISTRY if p["id"] == r["pattern_id"])
            threshold = pattern["threshold"]
            drift_str = _format_drift_annotation(r)
            src = r.get("count_source", "page-scan")
            unit = "instances" if src == "log.md" else "page mentions"
            out.append("")
            out.append(
                f"- {r['name']} ({pattern['claude_md_ref']}) — "
                f"vault: {r['vault_count']} {unit} (source: {src}) | "
                f"threshold: {threshold} | {drift_str}"
            )
            if src == "log.md" and r.get("page_mention_count", 0) > 0:
                out.append(
                    f"  Supplementary: {r['page_mention_count']} pages mention pattern"
                )
            sub_str = _format_sub_patterns(r, pattern)
            if sub_str:
                out.append(f"  Sub-patterns: {sub_str}")
            if r["matching_pages"]:
                pages_str = ", ".join(r["matching_pages"][:6])
                more = ""
                if len(r["matching_pages"]) > 6:
                    more = f" (and {len(r['matching_pages']) - 6} more)"
                out.append(f"  Pages: {pages_str}{more}")
    else:
        out.append("- (no patterns at codification threshold)")
    out.append("")

    # --- APPROACHING THRESHOLD ---
    out.append("**Patterns approaching threshold (monitoring active):**")
    if buckets["approaching"]:
        for r in buckets["approaching"]:
            pattern = next(p for p in PATTERN_REGISTRY if p["id"] == r["pattern_id"])
            threshold = pattern["threshold"]
            drift_str = _format_drift_annotation(r)
            gap = threshold - r["vault_count"]
            src = r.get("count_source", "page-scan")
            unit = "instances (source: log.md)" if src == "log.md" else "page mentions"
            out.append("")
            out.append(
                f"- {r['name']} ({pattern['claude_md_ref']}) — "
                f"vault: {r['vault_count']} {unit} | threshold: {threshold} | "
                f"{gap} more to trigger codification | {drift_str}"
            )
            if r["matching_pages"]:
                pages_str = ", ".join(r["matching_pages"][:5])
                out.append(f"  Pages: {pages_str}")
    else:
        out.append("- (no patterns approaching threshold)")
    out.append("")

    # --- RUNNING COUNTS ---
    out.append("**Running-count patterns (no codification threshold):**")
    if buckets["running_count"]:
        for r in buckets["running_count"]:
            pattern = next(p for p in PATTERN_REGISTRY if p["id"] == r["pattern_id"])
            drift_str = _format_drift_annotation(r)
            src = r.get("count_source", "page-scan")
            if src == "log.md":
                unit = "instances (source: log.md)"
            elif pattern["scope"] == "log_md":
                unit = "log lines"
            else:
                unit = "page mentions"
            out.append("")
            out.append(
                f"- {r['name']} ({pattern['claude_md_ref']}) — "
                f"vault: {r['vault_count']} {unit} | {drift_str}"
            )
            sub_str = _format_sub_patterns(r, pattern)
            if sub_str:
                out.append(f"  Sub-patterns: {sub_str}")
            if r["matching_pages"] and pattern["scope"] != "log_md":
                pages_str = ", ".join(r["matching_pages"][:5])
                more = ""
                if len(r["matching_pages"]) > 5:
                    more = f" (and {len(r['matching_pages']) - 5} more)"
                out.append(f"  Pages: {pages_str}{more}")
    else:
        out.append("- (no running-count patterns observed)")
    out.append("")

    # --- DRIFT SUMMARY TABLE ---
    out.append(f"**Drift vs MEMORY.md ({memory_path.name}):**")
    out.append("")
    out.append("| Pattern | Vault | MEMORY.md | Drift |")
    out.append("|---|---|---|---|")
    for r in annotated:
        if r["direction"] == "untracked":
            drift_cell = "untracked"
        elif r["direction"] == "equal":
            drift_cell = "0"
        else:
            sign = "+" if r["drift"] > 0 else ""
            drift_cell = f"{sign}{r['drift']} ({r['direction']})"
        memory_cell = "—" if r["memory_count"] is None else str(r["memory_count"])
        out.append(f"| {r['name']} | {r['vault_count']} | {memory_cell} | {drift_cell} |")
    out.append("")

    # --- UNOBSERVED ---
    if buckets["unobserved"]:
        out.append("**Patterns codified but zero vault instances found:**")
        for r in buckets["unobserved"]:
            pattern = next(p for p in PATTERN_REGISTRY if p["id"] == r["pattern_id"])
            out.append(f"- {r['name']} ({pattern['claude_md_ref']}) — 0 instances")
        out.append("")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def run_monitor_scan(
    vault_root: Path,
    memory_path: Path,
    full_body: bool = False,
    debug: bool = False,
) -> str:
    """Run the full pattern scan; return markdown report.

    Source-of-truth hierarchy for pattern counts:
      1. log.md most-recent Convention counts (authoritative; Vic-curated)
      2. Wiki page scan (supplementary; surfaces page mentions for verification)
      3. MEMORY.md (drift baseline; often stale)

    When log.md provides an explicit count, it overrides the page-scan count
    for vault_count. The page-scan count is preserved under page_mention_count
    for supplementary display.
    """
    today = date.today()
    pages = load_all_pages(vault_root)
    if debug:
        print(
            f"DEBUG: loaded {len(pages)} pages "
            f"(including log.md: {'LOG' in pages})",
            file=sys.stderr,
        )

    scan_results = [scan_pattern(p, pages, full_body=full_body) for p in PATTERN_REGISTRY]

    # Override vault_count with authoritative log.md counts where available
    log_path = vault_root / "log.md"
    log_counts = parse_log_convention_counts(log_path)
    if debug:
        print(f"DEBUG: log_counts = {log_counts}", file=sys.stderr)
    for r in scan_results:
        log_count = log_counts.get(r["pattern_id"])
        # Preserve page-scan count as supplementary
        r["page_mention_count"] = r["vault_count"]
        if log_count is not None:
            r["vault_count"] = log_count
            r["count_source"] = "log.md"
        else:
            r["count_source"] = "page-scan"

    memory_counts = parse_memory_counts(memory_path)
    if debug:
        print(f"DEBUG: memory_counts = {memory_counts}", file=sys.stderr)

    annotated = compute_drift(scan_results, memory_counts)
    buckets = classify_patterns(annotated)

    return format_report(buckets, annotated, memory_path, today)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--vault-root",
        type=Path,
        default=Path.cwd(),
        help="Vault root directory (default: cwd).",
    )
    parser.add_argument(
        "--memory-path",
        type=Path,
        default=DEFAULT_MEMORY_PATH,
        help="Path to MEMORY.md for drift comparison.",
    )
    parser.add_argument(
        "--full-body",
        action="store_true",
        help="Scan entire body, not just Source audit notes + Change log.",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Emit diagnostic output to stderr.",
    )
    args = parser.parse_args()

    report = run_monitor_scan(
        args.vault_root,
        args.memory_path,
        full_body=args.full_body,
        debug=args.debug,
    )
    print(report)


if __name__ == "__main__":
    main()
