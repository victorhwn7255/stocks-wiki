"""
vault_parsers.py — Shared parsing utilities for stocks-wiki vault files.

Provides frontmatter parsing, wikilink extraction, section enumeration, and
plaintext-ticker detection. No side effects; all functions return data
structures. Read-only access to wiki/ and raw/ directories.

Used by: scripts/find_connections.py.
Will be used by: future phase-0-verify, vault-lint skills.
"""

import re
from pathlib import Path
from typing import Optional

import yaml  # PyYAML — only external dependency

# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter block from markdown text.

    Returns (frontmatter_dict, body_text). If no frontmatter block is found,
    returns ({}, full_text). Graceful empty dict on PyYAML parse error.

    Frontmatter fields per CLAUDE.md v9 Section 3.2:
      type, tickers, layer, photonics_tier, memory_tier, energy_power_tier,
      equipment_tier, materials_tier, foreign_issuer, last_updated.
    """
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return {}, text
    try:
        fm = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    if not isinstance(fm, dict):
        fm = {}
    body = text[match.end():]
    return fm, body


def extract_tickers_from_frontmatter(fm: dict) -> list[str]:
    """Extract tickers list from parsed frontmatter dict.

    Returns list of uppercase ticker strings. Handles single-string, list,
    and absent cases. Normalizes to uppercase.
    """
    raw = fm.get("tickers", [])
    if isinstance(raw, str):
        return [raw.upper()]
    if isinstance(raw, list):
        return [str(t).upper() for t in raw if t]
    return []


def get_last_updated(fm: dict) -> Optional[str]:
    """Return last_updated string from frontmatter, or None if absent.

    Returns YYYY-MM-DD string as stored; no date parsing.
    """
    val = fm.get("last_updated")
    if val is None:
        return None
    return str(val)


# ---------------------------------------------------------------------------
# Wikilink extraction
# ---------------------------------------------------------------------------

WIKILINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


def extract_wikilinks(text: str) -> list[str]:
    """Extract all [[target]] wikilink targets from markdown body text.

    Returns list of raw target strings (may be ticker or page-name). Does not
    deduplicate — callers that need counts use this raw list. Handles both
    [[TICKER]] and [[page-name]] forms.

    Per CLAUDE.md v9 Section 3.3: casing-sensitive resolution; this function
    preserves original casing for callers to normalize as needed.
    """
    return WIKILINK_PATTERN.findall(text)


# Stopword set: common uppercase non-ticker tokens found in wiki prose.
# Excluding these from ticker matching reduces false positives to near-zero
# when combined with the known_tickers gate.
TICKER_PATTERN = re.compile(r"\b([A-Z]{2,5})\b")
TICKER_STOPWORDS = frozenset(
    {
        "AI", "CPO", "GPU", "API", "CEO", "CFO", "COO", "CTO", "IPO", "MA",
        "USA", "US", "UK", "EU", "UN", "SEC", "DOE", "NRC", "USD", "GBP",
        "YoY", "QoQ", "FY", "Q1", "Q2", "Q3", "Q4", "RD", "SBC", "FCF",
        "MDA", "GAAP", "EBIT", "EPS", "PCIe", "CIK", "CAGR",
        "BTM", "SMR", "SOFC", "MCFC", "VCSEL", "EML", "InP", "SiPh",
        "TSV", "CoWoS", "HBM", "DRAM", "NAND", "EUV", "ASML", "EPC",
        "ERCOT", "HVDC", "PPA", "UPS", "GOES", "MJDS", "HALEU",
        "COUPE", "COUP", "NVLink", "UALink", "LPO", "TAM", "CapEx",
        "CAPEX", "GW", "MW", "MWh", "GHz", "TB", "PB",
        "AND", "THE", "FOR", "NOT", "PER", "VIA", "FROM", "WITH",
        "INTO", "ITEM", "MORE", "THAN", "THIS", "THAT", "SUCH",
    }
)


def extract_plaintext_tickers(text: str, known_tickers: set[str]) -> list[str]:
    """Extract plaintext ticker mentions from body text, filtered to known vault tickers.

    Uses TICKER_PATTERN to find uppercase token sequences matching known_tickers.
    Stopword filter excludes common non-ticker uppercase tokens. Returns list
    (with duplicates) for counting purposes.

    Conservative: only matches tokens that are already known vault tickers,
    reducing false positives to near-zero. Does NOT attempt to discover new
    tickers from plaintext.
    """
    candidates = TICKER_PATTERN.findall(text)
    return [t for t in candidates if t in known_tickers and t not in TICKER_STOPWORDS]


# ---------------------------------------------------------------------------
# Section enumeration
# ---------------------------------------------------------------------------

SECTION_HEADER_PATTERN = re.compile(r"^#{1,4}\s+(.+)$", re.MULTILINE)


def extract_section_headers(body: str) -> list[str]:
    """Extract markdown section header titles from body text.

    Returns list of header text strings (stripped, without # prefix).
    Preserves order. Used for shared-section-topic detection in cluster analysis.
    """
    return [m.group(1).strip() for m in SECTION_HEADER_PATTERN.finditer(body)]


# Patterns to locate specific canonical sections.
# "## Source audit notes" header is the canonical annotation zone per CLAUDE.md
# Section 3.8. Allow whitespace variation and optional trailing tokens like
# " (per-source entries)" — match any header line beginning with "Source audit notes".
SOURCE_AUDIT_NOTES_HEADER = re.compile(
    r"^#{1,4}\s+Source audit notes.*$", re.MULTILINE | re.IGNORECASE
)
CHANGE_LOG_HEADER = re.compile(
    r"^#{1,4}\s+Change log.*$", re.MULTILINE | re.IGNORECASE
)


def extract_source_audit_notes_section(body: str) -> str:
    """Return text of the Source audit notes section only.

    Returns text between the "Source audit notes" header and the next top-level
    section (typically "Change log") or end-of-file. Returns "" if no Source
    audit notes header is found. Per CLAUDE.md Section 3.8, this is the
    canonical annotation zone for pattern instances.
    """
    match = SOURCE_AUDIT_NOTES_HEADER.search(body)
    if not match:
        return ""
    start = match.end()
    # End at next Change log header, or at end of file
    change_log_match = CHANGE_LOG_HEADER.search(body, start)
    end = change_log_match.start() if change_log_match else len(body)
    return body[start:end]


def extract_change_log_section(body: str) -> str:
    """Return text of the Change log section only.

    Returns text from "Change log" header to end of file. Returns "" if no
    Change log header is found. Some patterns are annotated in Change log
    entries (per Section 3.8 brevity convention) rather than Source audit notes.
    """
    match = CHANGE_LOG_HEADER.search(body)
    if not match:
        return ""
    return body[match.end():]


# ---------------------------------------------------------------------------
# Convenience wrappers
# ---------------------------------------------------------------------------


def read_page(path: Path) -> tuple[dict, str]:
    """Read a wiki page; return (frontmatter_dict, body_text).

    Returns ({}, "") on file-not-found or read error.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}, ""
    return parse_frontmatter(text)
