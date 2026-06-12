#!/usr/bin/env python3
"""build_index.py — generate index.md's Companies table from page frontmatter.

Frontmatter is the single source of truth; this script eliminates hand-sync drift
between wiki/companies/*.md and index.md (the drift class flagged in index.md's
own header note). Established at CLAUDE.md v9.9 (2026-06-13).

Default: print the generated Companies table to stdout and DIFF it against the
table currently in index.md (read-only; safe to run anytime).
--write: replace the Companies table section in index.md in place.

Column semantics mirror index.md: per-domain tier columns reflect frontmatter
as-written; absent field = "—"; explicit outside = "outside". Defense column from
defense_tier. Layer from layer (quoted hybrids like "4-6" or "1, 2" preserved).
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPANIES_DIR = ROOT / "wiki" / "companies"
INDEX = ROOT / "index.md"

COLUMNS = [
    ("Photonics", "photonics_tier"),
    ("Memory", "memory_tier"),
    ("Energy/Power", "energy_power_tier"),
    ("Equipment", "equipment_tier"),
    ("Materials", "materials_tier"),
    ("Defense", "defense_tier"),
]


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        key, _, val = line.partition(":")
        fm[key.strip()] = val.strip().strip('"')
    return fm


def ticker_of(fm: dict, path: Path) -> str:
    raw = fm.get("tickers", "")
    m = re.match(r"\[(.*?)\]", raw)
    return (m.group(1).split(",")[0].strip() if m else path.stem)


def build_rows() -> list[str]:
    rows = []
    for path in sorted(COMPANIES_DIR.glob("*.md")):
        fm = parse_frontmatter(path)
        if fm.get("type", "company") != "company":
            continue
        name = path.stem
        ticker = ticker_of(fm, path)
        layer = fm.get("layer", "—") or "—"
        cells = [fm.get(field, "—") or "—" for _, field in COLUMNS]
        updated = fm.get("last_updated", "—")
        rows.append(
            f"| [{name}](wiki/companies/{path.name}) | {ticker} | {layer} | "
            + " | ".join(cells)
            + f" | {updated} |"
        )
    return rows


def build_table() -> str:
    header = (
        "| Page | Ticker | Layer | "
        + " | ".join(col for col, _ in COLUMNS)
        + " | Last Updated |"
    )
    sep = "|" + "---|" * (3 + len(COLUMNS) + 1)
    return "\n".join([header, sep] + build_rows())


def current_table() -> str:
    text = INDEX.read_text(encoding="utf-8")
    m = re.search(r"(\| Page .*?\|\n\|[-| ]+\|\n(?:\|.*\|\n)+)", text)
    return m.group(1).rstrip("\n") if m else ""


def write_table(table: str) -> None:
    text = INDEX.read_text(encoding="utf-8")
    cur = current_table()
    if not cur:
        sys.exit("ERROR: could not locate the Companies table in index.md; not writing.")
    INDEX.write_text(text.replace(cur, table + "\n"), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true", help="replace the table in index.md")
    args = ap.parse_args()

    table = build_table()
    if args.write:
        write_table(table)
        print(f"index.md Companies table rewritten from frontmatter ({len(build_rows())} rows).")
        return

    print(table)
    cur = current_table()
    if not cur:
        print("\n[diff] WARNING: existing table not found in index.md", file=sys.stderr)
        return
    def norm(r: str) -> str:
        return re.sub(r"\s*\|\s*", "|", r.strip())

    cur_rows = set(norm(r) for r in cur.splitlines() if r.strip().startswith("| ["))
    new_rows = set(norm(r) for r in table.splitlines() if r.strip().startswith("| ["))
    drift_old = sorted(cur_rows - new_rows)
    drift_new = sorted(new_rows - cur_rows)
    if not drift_old and not drift_new:
        print("\n[diff] index.md table matches frontmatter exactly — no drift.", file=sys.stderr)
    else:
        print(f"\n[diff] DRIFT: {len(drift_old)} stale row(s) in index.md, {len(drift_new)} row(s) differ from frontmatter:", file=sys.stderr)
        for r in drift_old:
            print(f"  index.md : {r}", file=sys.stderr)
        for r in drift_new:
            print(f"  frontmatter: {r}", file=sys.stderr)


if __name__ == "__main__":
    main()
