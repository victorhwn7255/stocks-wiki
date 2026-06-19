#!/usr/bin/env python3
"""
find_connections.py — Surface candidate cross-page connections not yet captured
by chokepoint, theme, or relationship pages in the stocks-wiki vault.

Deterministic: same vault state -> same output. Pure local analysis; no
external APIs. Orchestrated by the `connection-finder` skill.

Usage:
    python scripts/find_connections.py
    python scripts/find_connections.py --vault-root /path/to/stocks-wiki
    python scripts/find_connections.py --top-n 5
    python scripts/find_connections.py --min-score 3.0
    python scripts/find_connections.py --no-recency       # disable recency weighting
    python scripts/find_connections.py --debug            # extra diagnostic output
    python scripts/find_connections.py --dismiss AVGO,NVT --reason "commercial tie, no page"
    python scripts/find_connections.py --list-dismissed   # show the curated skip-list
    python scripts/find_connections.py --undismiss AVGO,NVT

Requires: PyYAML (pip install pyyaml).
"""

import argparse
import sys
from collections import deque, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

# Allow running from any directory; add this script's parent to sys.path so
# vault_parsers can be imported without packaging.
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from vault_parsers import (  # noqa: E402
    extract_plaintext_tickers,
    extract_section_headers,
    extract_tickers_from_frontmatter,
    extract_wikilinks,
    get_last_updated,
    read_page,
)


# ---------------------------------------------------------------------------
# Dismissed-candidate memory (Vic-curated skip-list — kills recurring noise)
# ---------------------------------------------------------------------------
#
# When a surfaced HIGH SIGNAL cluster (e.g. "AVGO + NVT") is judged "not worth a
# page," it goes here and stops re-surfacing every scan. Reversible + git-tracked.
# Stored as: {"dismissed": [{"tickers": ["AVGO","NVT"], "reason": "...", "date": "YYYY-MM-DD"}]}

DISMISSED_PATH = SCRIPT_DIR / "find_connections_dismissed.json"


def _read_dismissed_records() -> list[dict]:
    import json
    if not DISMISSED_PATH.exists():
        return []
    try:
        return json.loads(DISMISSED_PATH.read_text(encoding="utf-8")).get("dismissed", [])
    except Exception:  # noqa: BLE001 — a malformed sidecar must never break the scan
        return []


def _write_dismissed_records(records: list[dict]) -> None:
    import json
    DISMISSED_PATH.write_text(
        json.dumps({"dismissed": records}, indent=2) + "\n", encoding="utf-8"
    )


def load_dismissed() -> set[frozenset]:
    """Return the dismissed ticker-sets (frozensets) to skip; empty if none/absent."""
    return {
        frozenset(t.upper() for t in r["tickers"])
        for r in _read_dismissed_records()
        if r.get("tickers")
    }


def _parse_ticker_csv(csv: str) -> list[str]:
    return sorted({t.strip().upper() for t in csv.split(",") if t.strip()})


def cmd_dismiss(tickers_csv: str, reason: str) -> str:
    tickers = _parse_ticker_csv(tickers_csv)
    if len(tickers) < 2:
        return "dismiss needs >=2 comma-separated tickers, e.g. --dismiss AVGO,NVT"
    records = _read_dismissed_records()
    if any(frozenset(r["tickers"]) == frozenset(tickers) for r in records):
        return f"already dismissed: {' + '.join(tickers)}"
    records.append(
        {
            "tickers": tickers,
            "reason": reason or "(no reason given)",
            "date": date.today().strftime("%Y-%m-%d"),
        }
    )
    _write_dismissed_records(records)
    return f"dismissed: {' + '.join(tickers)} — will no longer surface as a HIGH SIGNAL cluster."


def cmd_undismiss(tickers_csv: str) -> str:
    tickers = _parse_ticker_csv(tickers_csv)
    records = _read_dismissed_records()
    kept = [r for r in records if frozenset(r["tickers"]) != frozenset(tickers)]
    if len(kept) == len(records):
        return f"not in dismissed list: {' + '.join(tickers)}"
    _write_dismissed_records(kept)
    return f"restored: {' + '.join(tickers)} — eligible to surface again."


def cmd_list_dismissed() -> str:
    records = _read_dismissed_records()
    if not records:
        return 'No dismissed clusters. (Add one: --dismiss AVGO,NVT --reason "...")'
    lines = ["Dismissed connection candidates (skipped from HIGH SIGNAL):"]
    for r in records:
        lines.append(
            f"  - {' + '.join(r['tickers'])} — {r.get('reason', '')} "
            f"(dismissed {r.get('date', '?')})"
        )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Page loading
# ---------------------------------------------------------------------------


PAGE_TYPE_DIRS = {
    "company": "wiki/companies",
    "chokepoint": "wiki/chokepoints",
    "theme": "wiki/themes",
    "relationship": "wiki/relationships",
    "tracker": "wiki/trackers",
}


def load_vault_pages(vault_root: Path) -> dict[str, dict]:
    """Load all wiki pages from wiki/ subdirectories into a keyed dict.

    Keys: ticker (companies) or filename stem (other types).
    Values: PageRecord dicts with path, type, tickers, last_updated, wikilinks,
    plaintext_tickers (populated after company_ticker_set is known),
    section_headers, body.

    Determinism: files processed in sorted(glob()) order.
    """
    pages: dict[str, dict] = {}
    for page_type, subdir in PAGE_TYPE_DIRS.items():
        dir_path = vault_root / subdir
        if not dir_path.is_dir():
            continue
        for md_file in sorted(dir_path.glob("*.md")):
            fm, body = read_page(md_file)
            if not fm:
                continue
            key = md_file.stem.upper() if page_type == "company" else md_file.stem
            pages[key] = {
                "path": md_file,
                "type": page_type,
                "tickers": extract_tickers_from_frontmatter(fm),
                "last_updated": get_last_updated(fm),
                "wikilinks": extract_wikilinks(body),
                "plaintext_tickers": [],  # filled after company ticker set known
                "section_headers": extract_section_headers(body),
                "body": body,
            }
    return pages


def build_company_ticker_set(pages: dict[str, dict]) -> set[str]:
    """Return set of all ticker strings from company-type pages.

    Used to scope co-mention counting to vault-actual tickers, preventing
    false-positive matches on non-vault ticker tokens in body text.
    """
    return {key for key, page in pages.items() if page["type"] == "company"}


def populate_plaintext_tickers(pages: dict[str, dict], company_tickers: set[str]) -> None:
    """Mutate pages dict: fill plaintext_tickers using known company ticker set."""
    for page in pages.values():
        page["plaintext_tickers"] = extract_plaintext_tickers(
            page["body"], company_tickers
        )


# ---------------------------------------------------------------------------
# Co-mention matrix
# ---------------------------------------------------------------------------


def _normalize_target(target: str) -> str:
    """Wikilink target may be 'TICKER' or 'page-name'; return uppercase for ticker test."""
    return target.upper().strip()


def build_co_mention_matrix(
    pages: dict[str, dict],
    company_tickers: set[str],
) -> dict[frozenset, int]:
    """Build undirected co-mention count matrix across all vault pages.

    Per-page scoring per ticker pair (X, Y):
      - [[X]] wikilink in Y's company page body: +2
      - [[Y]] wikilink in X's company page body: +2
      - [[X]] or [[Y]] wikilink in chokepoint/theme/relationship body: +1 each
      - Plaintext X mention in Y's company page body: +1
      - Plaintext Y mention in X's company page body: +1
      - Plaintext X + Y co-mention on non-company page: +1 (combined; not per-token)

    Returns dict mapping frozenset({X, Y}) -> total_score.

    Self-pairs ({X, X}) are excluded.
    """
    matrix: dict[frozenset, int] = defaultdict(int)

    for page_key, page in pages.items():
        page_type = page["type"]
        wikilinked_tickers = {
            _normalize_target(t)
            for t in page["wikilinks"]
            if _normalize_target(t) in company_tickers
        }
        plaintext_tickers_on_page = set(page["plaintext_tickers"])

        if page_type == "company":
            host_ticker = page_key  # e.g., NVDA
            # Wikilinks pointing FROM host page TO another company: +2 per pair
            for target in wikilinked_tickers:
                if target == host_ticker:
                    continue
                matrix[frozenset({host_ticker, target})] += 2
            # Plaintext mentions of other companies on host page: +1 per pair
            # (deduplicate so multiple mentions of same ticker contribute once)
            for target in plaintext_tickers_on_page:
                if target == host_ticker:
                    continue
                if target in wikilinked_tickers:
                    continue  # avoid double-counting; wikilink already gave +2
                matrix[frozenset({host_ticker, target})] += 1
        else:
            # Non-company pages contribute +1 per co-occurring ticker pair on
            # the same page (combining wikilinked + plaintext into a single set
            # to avoid double-counting on this page).
            tickers_on_page = wikilinked_tickers | plaintext_tickers_on_page
            tickers_list = sorted(tickers_on_page)
            for i, t1 in enumerate(tickers_list):
                for t2 in tickers_list[i + 1:]:
                    matrix[frozenset({t1, t2})] += 1

    return dict(matrix)


# ---------------------------------------------------------------------------
# Already-captured pair detection
# ---------------------------------------------------------------------------


PAGE_TYPE_PRIORITY = {"relationship": 3, "chokepoint": 2, "theme": 1, "layer": 0}


def build_captured_pairs(pages: dict[str, dict]) -> dict[frozenset, tuple[str, str]]:
    """Identify ticker pairs already captured by non-company pages.

    A pair (X, Y) is captured iff there exists at least one chokepoint, theme,
    relationship, or layer page where BOTH X and Y appear in frontmatter tickers
    OR are wikilinked in the body.

    Returns dict: frozenset({X, Y}) -> (capturing_page_name, capturing_page_type).
    For pairs in multiple pages, returns the highest-priority page type
    (relationship > chokepoint > theme > layer).
    """
    captured: dict[frozenset, tuple[str, str]] = {}

    for page_key, page in pages.items():
        if page["type"] == "company":
            continue
        page_type = page["type"]
        fm_tickers = set(page["tickers"])
        wikilinked = {
            _normalize_target(t) for t in page["wikilinks"]
        }
        # Restrict body wikilinks to those that look like company tickers
        # (uppercase 2-5 chars; matches TICKER_PATTERN shape — this lets
        # [[page-name]] not contaminate the set).
        wikilinked_tickers = {t for t in wikilinked if t.isupper() and 2 <= len(t) <= 5}
        tickers_on_page = fm_tickers | wikilinked_tickers

        tickers_list = sorted(tickers_on_page)
        for i, t1 in enumerate(tickers_list):
            for t2 in tickers_list[i + 1:]:
                pair = frozenset({t1, t2})
                existing = captured.get(pair)
                if existing is None:
                    captured[pair] = (page_key, page_type)
                else:
                    existing_priority = PAGE_TYPE_PRIORITY.get(existing[1], -1)
                    new_priority = PAGE_TYPE_PRIORITY.get(page_type, -1)
                    if new_priority > existing_priority:
                        captured[pair] = (page_key, page_type)

    return captured


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------


def _to_date(value) -> date | None:
    """Coerce a frontmatter date value to a datetime.date, or None if invalid."""
    if value is None:
        return None
    if isinstance(value, date):
        return value
    try:
        return datetime.strptime(str(value).strip(), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def _recency_factor(pair_last_updated: date | None, today: date) -> float:
    """Map most-recent last_updated age to a recency factor in [0.55, 1.0]."""
    if pair_last_updated is None:
        return 0.55
    age_days = (today - pair_last_updated).days
    if age_days <= 30:
        return 1.0
    if age_days <= 90:
        return 0.85
    if age_days <= 180:
        return 0.70
    return 0.55


def score_candidate_pairs(
    co_mention_matrix: dict[frozenset, int],
    captured_pairs: dict[frozenset, tuple[str, str]],
    pages: dict[str, dict],
    today: date,
    recency_weight: bool = True,
) -> list[dict]:
    """Score and rank all ticker pairs by signal strength.

    Returns list of dicts:
      {pair, raw_score, recency_factor, captured, captured_by,
       captured_type, final_score}
    Sorted by final_score descending.

    Captured pairs are NOT zeroed here — the cluster + format steps decide
    which sections to surface them in. final_score retains the captured pairs'
    full score; downstream filters branch on `captured` flag.
    """
    out = []
    for pair, raw in co_mention_matrix.items():
        t1, t2 = sorted(pair)
        page1 = pages.get(t1)
        page2 = pages.get(t2)
        d1 = _to_date(page1.get("last_updated") if page1 else None)
        d2 = _to_date(page2.get("last_updated") if page2 else None)
        candidates = [d for d in (d1, d2) if d is not None]
        most_recent = max(candidates) if candidates else None
        rf = _recency_factor(most_recent, today) if recency_weight else 1.0

        capture = captured_pairs.get(pair)
        captured = capture is not None
        final = raw * rf

        out.append(
            {
                "pair": pair,
                "tickers": [t1, t2],
                "raw_score": raw,
                "recency_factor": rf,
                "captured": captured,
                "captured_by": capture[0] if capture else None,
                "captured_type": capture[1] if capture else None,
                "final_score": round(final, 2),
            }
        )

    out.sort(key=lambda x: (-x["final_score"], x["tickers"]))
    return out


# ---------------------------------------------------------------------------
# Cluster detection via BFS connected components
# ---------------------------------------------------------------------------


def detect_clusters(
    scored_pairs: list[dict],
    min_score_threshold: float = 3.0,
    max_cluster_size: int = 5,
    dismissed: set[frozenset] | None = None,
) -> list[dict]:
    """Surface candidate connections as small high-density clusters (or single pairs).

    Strategy: avoid the connected-components-explosion failure mode by requiring
    cluster-internal density. A pair seeds a candidate; cluster extension only
    occurs if the new ticker has a qualifying score with at least 2 existing
    cluster members (i.e., forms a triangle). Hard cap at max_cluster_size.

    Steps:
      1. Filter to uncaptured pairs with raw_score >= threshold; sort by score.
      2. Greedy cluster construction:
         - Each top-scoring pair seeds a candidate cluster (unless one of its
           tickers is already in a higher-score cluster).
         - Extend cluster greedily: add ticker T if T has qualifying-score pairs
           with at least 2 existing cluster members.
         - Stop at max_cluster_size.
      3. Pairs that remain unclustered (singletons) surface as 2-ticker
         candidates.

    Returns list of cluster dicts: {tickers, cluster_score, evidence, pairs}.
    Sorted by cluster_score descending.
    """
    dismissed = dismissed or set()
    qualifying = [
        p for p in scored_pairs
        if p["raw_score"] >= min_score_threshold
        and not p["captured"]
        and p["pair"] not in dismissed  # a dismissed 2-ticker pair never seeds a cluster
    ]
    if not qualifying:
        return []

    # Index by frozenset for O(1) lookup
    pair_index: dict[frozenset, dict] = {p["pair"]: p for p in qualifying}
    # Adjacency: ticker -> set of (other_ticker, score)
    adjacency: dict[str, dict[str, float]] = defaultdict(dict)
    for p in qualifying:
        t1, t2 = p["tickers"]
        adjacency[t1][t2] = p["final_score"]
        adjacency[t2][t1] = p["final_score"]

    # Sort pairs by final_score descending; tickers already sorted alphabetically
    sorted_pairs = sorted(qualifying, key=lambda p: (-p["final_score"], p["tickers"]))

    clusters = []
    seen_tickers: set[str] = set()
    for seed_pair in sorted_pairs:
        t1, t2 = seed_pair["tickers"]
        # Skip if EITHER ticker is already absorbed into a higher-scoring cluster.
        # High-degree tickers (NVDA, TSM) otherwise seed multiple clusters with
        # their many uncaptured neighbors. The single-absorption guard preserves
        # the "each ticker appears in at most one cluster" invariant.
        if t1 in seen_tickers or t2 in seen_tickers:
            continue
        cluster_tickers = [t1, t2]
        cluster_pairs = [seed_pair]
        cluster_score = seed_pair["final_score"]
        seen_tickers.update([t1, t2])

        # Greedy triangle extension: find candidate tickers with qualifying-score
        # edges to >= 2 existing members
        while len(cluster_tickers) < max_cluster_size:
            best_candidate = None
            best_candidate_score = 0.0
            best_candidate_pairs: list[dict] = []
            # Candidates = tickers with edges to ≥ 1 cluster member, not yet in cluster,
            # AND not already absorbed elsewhere (else a high-degree ticker could appear
            # in two clusters simultaneously).
            candidates: set[str] = set()
            for member in cluster_tickers:
                candidates.update(adjacency[member].keys())
            candidates -= set(cluster_tickers)
            candidates -= seen_tickers
            for candidate in candidates:
                # Count qualifying edges to cluster members
                connecting_pairs = []
                edge_sum = 0.0
                for member in cluster_tickers:
                    if candidate in adjacency[member]:
                        edge_sum += adjacency[member][candidate]
                        connecting_pairs.append(
                            pair_index[frozenset({member, candidate})]
                        )
                # Triangle requirement: ≥ 2 qualifying edges to existing members
                if len(connecting_pairs) >= 2 and edge_sum > best_candidate_score:
                    best_candidate = candidate
                    best_candidate_score = edge_sum
                    best_candidate_pairs = connecting_pairs
            if best_candidate is None:
                break
            cluster_tickers.append(best_candidate)
            cluster_pairs.extend(best_candidate_pairs)
            cluster_score += best_candidate_score
            seen_tickers.add(best_candidate)

        cluster_tickers = sorted(cluster_tickers)
        clusters.append(
            {
                "tickers": cluster_tickers,
                "cluster_score": round(cluster_score, 2),
                "evidence": _collect_evidence(cluster_tickers, cluster_pairs),
                "pairs": cluster_pairs,
            }
        )

    # Drop any formed cluster whose exact ticker-set Vic has dismissed (handles 3+
    # ticker dismissals; the qualifying-pair filter above already handles 2-ticker ones).
    if dismissed:
        clusters = [c for c in clusters if frozenset(c["tickers"]) not in dismissed]
    clusters.sort(key=lambda c: (-c["cluster_score"], c["tickers"]))
    return clusters


def _collect_evidence(tickers: list[str], pairs: list[dict]) -> list[str]:
    """Build human-readable evidence strings for a cluster, deduplicating pairs."""
    seen = set()
    lines = []
    for p in pairs:
        key = frozenset(p["tickers"])
        if key in seen:
            continue
        seen.add(key)
        t1, t2 = p["tickers"]
        lines.append(
            f"{t1}↔{t2} raw_score={p['raw_score']}"
            f" (recency×{p['recency_factor']:.2f})"
        )
        if len(lines) >= 6:
            break
    return lines


def build_refresh_candidates(
    pages: dict[str, dict],
    scored_pairs: list[dict],
    company_tickers: set[str],
    min_affinity: float = 6.0,
    top_n_per_page: int = 3,
) -> list[dict]:
    """Surface refresh candidates per non-company page.

    For each chokepoint/theme/relationship page P with ticker set Tp, find external
    tickers X (X in company_tickers, X not in Tp) where sum of co-mention scores
    between X and members of Tp exceeds min_affinity. Surface top-N candidates per
    page. Output is one entry per (page, external_ticker) pair, grouped under page.

    Returns list of refresh-candidate dicts: {page_name, page_type, existing_tickers,
    external_candidates: [{ticker, affinity, supporting_pairs}, ...]}.
    Sorted by max affinity descending.
    """
    # Index co-mention scores: {(t1, t2)} -> final_score
    pair_score_lookup: dict[frozenset, float] = {
        p["pair"]: p["final_score"] for p in scored_pairs
    }

    refresh_list = []
    for page_key, page in pages.items():
        if page["type"] == "company":
            continue
        existing_fm_tickers = set(page["tickers"])
        wikilinked = {
            _normalize_target(t) for t in page["wikilinks"]
        }
        wikilinked_tickers_on_page = {
            t for t in wikilinked if t in company_tickers
        }
        existing_tickers = existing_fm_tickers | wikilinked_tickers_on_page
        if len(existing_tickers) < 2:
            continue

        external_candidates = []
        for x in company_tickers - existing_tickers:
            supporting_pairs = []
            affinity = 0.0
            for t in existing_tickers:
                score = pair_score_lookup.get(frozenset({x, t}), 0.0)
                if score > 0:
                    affinity += score
                    supporting_pairs.append((t, score))
            if affinity >= min_affinity and len(supporting_pairs) >= 2:
                supporting_pairs.sort(key=lambda s: -s[1])
                external_candidates.append(
                    {
                        "ticker": x,
                        "affinity": round(affinity, 2),
                        "supporting_pairs": supporting_pairs[:5],
                    }
                )
        external_candidates.sort(key=lambda c: -c["affinity"])
        if external_candidates:
            refresh_list.append(
                {
                    "page_name": page_key,
                    "page_type": page["type"],
                    "existing_tickers_count": len(existing_tickers),
                    "external_candidates": external_candidates[:top_n_per_page],
                    "top_affinity": external_candidates[0]["affinity"],
                }
            )

    refresh_list.sort(key=lambda r: -r["top_affinity"])
    return refresh_list


# ---------------------------------------------------------------------------
# Page-type suggestion
# ---------------------------------------------------------------------------


STRUCTURAL_KEYWORDS = (
    "supply", "constraint", "capacity", "chokepoint", "bottleneck",
    "shortage", "lead time", "backlog", "allocation",
)
DYNAMIC_KEYWORDS = (
    "platform", "competition", "battle", "dynamic", "transition",
    "adoption", " vs ", "versus",
)
COMMERCIAL_KEYWORDS = (
    "customer", "supplier", "partnership", "equity", "agreement",
    "contract", "revenue", "concentration",
)


def _gather_cluster_text(tickers: list[str], pages: dict[str, dict]) -> str:
    """Concatenate section headers + first 500 chars of body for cluster member pages."""
    parts = []
    for t in tickers:
        page = pages.get(t)
        if not page:
            continue
        parts.extend(page["section_headers"])
        parts.append(page["body"][:500])
    return "\n".join(parts).lower()


def suggest_page_type(
    cluster: dict, pages: dict[str, dict], existing_captures: dict[frozenset, tuple[str, str]]
) -> dict:
    """Suggest page type for a candidate cluster.

    Rules (first match wins):
      1. cluster pairs overlap existing capturing page (>= 2 cluster pairs already
         captured by same page): "REFRESH"
      2. len(tickers) >= 4 AND structural-bottleneck signals: "chokepoint"
      3. len(tickers) >= 3 AND dynamic-framing signals: "theme"
      4. len(tickers) <= 3 AND commercial-tie signals: "relationship"
      5. fallback: "theme"

    Returns dict: {page_type, rationale, existing_page}.
    """
    tickers = cluster["tickers"]
    # REFRESH check
    capture_pages = []
    for p in cluster["pairs"]:
        cap = existing_captures.get(p["pair"])
        if cap:
            capture_pages.append(cap[0])
    if capture_pages:
        # If 2+ cluster pairs map to the same existing page, mark as REFRESH
        from collections import Counter

        counter = Counter(capture_pages)
        top_page, top_count = counter.most_common(1)[0]
        if top_count >= 2:
            return {
                "page_type": "REFRESH",
                "rationale": (
                    f"{top_count} cluster pairs overlap with existing page "
                    f"[[{top_page}]]"
                ),
                "existing_page": top_page,
            }

    text = _gather_cluster_text(tickers, pages)
    has_structural = any(kw in text for kw in STRUCTURAL_KEYWORDS)
    has_dynamic = any(kw in text for kw in DYNAMIC_KEYWORDS)
    has_commercial = any(kw in text for kw in COMMERCIAL_KEYWORDS)
    n = len(tickers)

    if n >= 4 and has_structural:
        return {
            "page_type": "chokepoint",
            "rationale": (
                "4+ tickers cluster with structural-bottleneck framing "
                "(supply/capacity/lead-time signals)"
            ),
            "existing_page": None,
        }
    if n >= 3 and has_dynamic:
        return {
            "page_type": "theme",
            "rationale": (
                "3+ tickers cluster with dynamic framing "
                "(platform/competition/transition signals)"
            ),
            "existing_page": None,
        }
    if n <= 3 and has_commercial:
        return {
            "page_type": "relationship",
            "rationale": (
                "2-3 tickers with commercial-tie evidence "
                "(customer/supplier/partnership signals)"
            ),
            "existing_page": None,
        }
    return {
        "page_type": "theme",
        "rationale": "fallback default (no strong structural/commercial signal)",
        "existing_page": None,
    }


# ---------------------------------------------------------------------------
# Tier context formatting
# ---------------------------------------------------------------------------


TIER_DESCRIPTIVE = {
    ("layer", 1): "Platform definer Layer 1",
    ("layer", 2): "Captive foundry Layer 2",
    ("layer", 3): "Specialized designer Layer 3",
    ("layer", 4): "Specialty component supplier Layer 4",
    ("layer", 5): "Module/system assembler Layer 5",
    ("layer", 6): "Scale manufacturer Layer 6",
    ("photonics_tier", 1): "Photonics Tier 1",
    ("photonics_tier", 2): "Photonics Tier 2 component supplier",
    ("photonics_tier", 3): "Photonics Tier 3 component supplier",
    ("photonics_tier", 4): "Photonics Tier 4 specialty supplier",
    ("photonics_tier", 5): "Photonics Tier 5 assembler",
    ("energy_power_tier", 1): "Energy/Power Tier 1 critical infrastructure",
    ("energy_power_tier", 2): "Energy/Power Tier 2",
    ("energy_power_tier", 3): "Energy/Power Tier 3",
    ("energy_power_tier", 4): "Energy/Power Tier 4 specialty",
    ("energy_power_tier", 5): "Energy/Power Tier 5",
    ("materials_tier", 1): "Materials Tier 1",
    ("materials_tier", 2): "Materials Tier 2",
}


def _tier_context_for_ticker(ticker: str, pages: dict[str, dict]) -> str:
    """Build descriptive tier context label for a ticker per CLAUDE.md convention."""
    page = pages.get(ticker)
    if not page:
        return ticker
    # Re-read frontmatter to access tier fields not stored in PageRecord
    try:
        import yaml
        text = page["path"].read_text(encoding="utf-8")
        from vault_parsers import parse_frontmatter
        fm, _ = parse_frontmatter(text)
    except Exception:
        return ticker

    descriptors = []
    layer = fm.get("layer")
    if isinstance(layer, int):
        key = ("layer", layer)
        if key in TIER_DESCRIPTIVE:
            descriptors.append(TIER_DESCRIPTIVE[key])
    for field in ("photonics_tier", "memory_tier", "energy_power_tier",
                  "equipment_tier", "materials_tier"):
        val = fm.get(field)
        if isinstance(val, int):
            key = (field, val)
            if key in TIER_DESCRIPTIVE:
                descriptors.append(TIER_DESCRIPTIVE[key])
    if descriptors:
        return f"{descriptors[0]} [[{ticker}]]"
    return f"[[{ticker}]]"


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------


def format_report(
    new_candidate_clusters: list[dict],
    refresh_candidates: list[dict],
    low_signal_count: int,
    pages: dict[str, dict],
    suggestions: dict[int, dict],
    scan_date: date,
    top_n: int = 5,
) -> str:
    """Format the 4-section markdown report.

    new_candidate_clusters: from detect_clusters (uncaptured).
    refresh_candidates: from build_refresh_candidates (per-page external additions).
    suggestions: page-type suggestion per new cluster index.
    """
    today_str = scan_date.strftime("%Y-%m-%d")
    out = [f"## Cross-vault connection candidates ({today_str})", ""]

    # -- HIGH SIGNAL: new candidates --
    out.append("**HIGH SIGNAL — new candidates not yet captured:**")
    if new_candidate_clusters:
        for i, cluster in enumerate(new_candidate_clusters[:top_n]):
            suggestion = suggestions.get(i, {})
            tickers = cluster["tickers"]
            score = cluster["cluster_score"]
            page_type = suggestion.get("page_type", "theme")
            rationale = suggestion.get("rationale", "")
            out.append("")
            out.append(
                f"{i + 1}. {' + '.join(tickers)} "
                f"(cluster_score: {score}) — suggested: {page_type}"
            )
            out.append("   Evidence:")
            for ev in cluster["evidence"]:
                out.append(f"     - {ev}")
            tier_lines = [_tier_context_for_ticker(t, pages) for t in tickers]
            out.append(f"   Tier context: {' + '.join(tier_lines)}")
            if rationale:
                out.append(f"   Rationale: {rationale}")
        if len(new_candidate_clusters) > top_n:
            out.append("")
            out.append(f"  and {len(new_candidate_clusters) - top_n} more")
    else:
        out.append("- (no new candidate clusters above threshold)")
    out.append("")

    # -- MEDIUM SIGNAL: per-page refresh candidates --
    out.append("**MEDIUM SIGNAL — refresh candidates (extend existing pages):**")
    if refresh_candidates:
        for i, refresh in enumerate(refresh_candidates[:top_n]):
            page_name = refresh["page_name"]
            page_type = refresh["page_type"]
            existing_count = refresh["existing_tickers_count"]
            externals = refresh["external_candidates"]
            ext_summary = ", ".join(
                f"[[{c['ticker']}]] (affinity {c['affinity']})" for c in externals
            )
            out.append("")
            out.append(
                f"{i + 1}. [[{page_name}]] ({page_type}; {existing_count} existing tickers)"
            )
            out.append(f"   External candidates to consider for refresh: {ext_summary}")
            top_external = externals[0]
            top_t = top_external["ticker"]
            support = top_external["supporting_pairs"]
            supp_str = ", ".join(
                f"[[{t}]] score={s:.1f}" for t, s in support[:3]
            )
            out.append(
                f"   Top candidate [[{top_t}]] supported by co-mentions with: {supp_str}"
            )
        if len(refresh_candidates) > top_n:
            out.append("")
            out.append(f"  and {len(refresh_candidates) - top_n} more")
    else:
        out.append("- (no refresh candidates surfaced)")
    out.append("")

    # -- LOW SIGNAL --
    out.append(
        f"**LOW SIGNAL — captured (no action needed):** "
        f"{low_signal_count} pairs already appear in existing "
        f"chokepoint/theme/relationship pages."
    )
    out.append("")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Top-level orchestration
# ---------------------------------------------------------------------------


def run_connections_scan(
    vault_root: Path,
    top_n: int = 5,
    min_score: float = 3.0,
    recency_weight: bool = True,
    debug: bool = False,
) -> str:
    """Run the full v1 scan; return markdown report string."""
    today = date.today()
    pages = load_vault_pages(vault_root)
    if not pages:
        return (
            f"## Cross-vault connection candidates ({today.strftime('%Y-%m-%d')})\n\n"
            f"ERROR: no wiki pages loaded from {vault_root}. "
            f"Verify wiki/companies/, wiki/chokepoints/, wiki/themes/, "
            f"wiki/relationships/ directories exist."
        )
    company_tickers = build_company_ticker_set(pages)
    populate_plaintext_tickers(pages, company_tickers)

    if debug:
        print(f"DEBUG: loaded {len(pages)} pages; {len(company_tickers)} company tickers", file=sys.stderr)

    matrix = build_co_mention_matrix(pages, company_tickers)
    captured = build_captured_pairs(pages)
    scored = score_candidate_pairs(matrix, captured, pages, today, recency_weight)

    if debug:
        print(f"DEBUG: {len(matrix)} co-mention pairs; "
              f"{len(captured)} captured pairs; "
              f"{sum(1 for s in scored if s['captured'])} scored-and-captured",
              file=sys.stderr)

    # HIGH SIGNAL: density-constrained clusters from NOT-CAPTURED qualifying pairs,
    # minus any Vic-dismissed cluster (the curated skip-list — kills recurring noise).
    new_clusters = detect_clusters(
        scored, min_score_threshold=min_score, dismissed=load_dismissed()
    )

    # MEDIUM SIGNAL: per-page refresh candidates (external tickers with high
    # affinity to existing page members)
    refresh_candidates = build_refresh_candidates(
        pages, scored, company_tickers, min_affinity=min_score * 2.0, top_n_per_page=3
    )

    # Page-type suggestions for new clusters
    suggestions = {}
    for i, cluster in enumerate(new_clusters):
        suggestions[i] = suggest_page_type(cluster, pages, captured)

    low_signal_count = sum(1 for s in scored if s["captured"])

    return format_report(
        new_clusters,
        refresh_candidates,
        low_signal_count,
        pages,
        suggestions,
        today,
        top_n=top_n,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--vault-root",
        type=Path,
        default=Path.cwd(),
        help="Vault root directory (default: cwd).",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=5,
        help="Cap per section (default: 5).",
    )
    parser.add_argument(
        "--min-score",
        type=float,
        default=3.0,
        help="Minimum raw co-mention score for cluster membership (default: 3.0).",
    )
    parser.add_argument(
        "--no-recency",
        action="store_true",
        help="Disable recency weighting.",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Emit diagnostic counts to stderr.",
    )
    parser.add_argument(
        "--dismiss",
        metavar="T1,T2",
        help="Add a ticker-set to the dismissed skip-list (won't re-surface as HIGH SIGNAL).",
    )
    parser.add_argument(
        "--reason",
        default="",
        help="Reason note recorded with --dismiss.",
    )
    parser.add_argument(
        "--undismiss",
        metavar="T1,T2",
        help="Remove a ticker-set from the dismissed skip-list.",
    )
    parser.add_argument(
        "--list-dismissed",
        action="store_true",
        help="Print the dismissed skip-list and exit.",
    )
    args = parser.parse_args()

    # Dismissed-list management commands run and exit (no scan).
    if args.list_dismissed:
        print(cmd_list_dismissed())
        return
    if args.dismiss:
        print(cmd_dismiss(args.dismiss, args.reason))
        return
    if args.undismiss:
        print(cmd_undismiss(args.undismiss))
        return

    report = run_connections_scan(
        args.vault_root,
        top_n=args.top_n,
        min_score=args.min_score,
        recency_weight=not args.no_recency,
        debug=args.debug,
    )
    print(report)


if __name__ == "__main__":
    main()
