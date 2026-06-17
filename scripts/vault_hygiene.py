#!/usr/bin/env python3
"""
vault_hygiene.py — deterministic vault health checks (the self-maintaining engine).

Read-only. Backs the `vault-hygiene` skill and the automation runner. Reuses
`vault_parsers.py` (parse_frontmatter / extract_wikilinks / get_last_updated).

Checks (each → PASS / WARN / FAIL):
  1. link-integrity     every [[wikilink]] resolves to an existing page; no self-links
  2. index-sync         every wiki/ file has an index.md row; every index row → a real file
  3. count-drift        actual dir counts vs index section row counts vs doc "~N" hints
  4. frontmatter        required fields present; last_updated a valid YYYY-MM-DD; tier values sane
  5. staleness          pages older than per-type thresholds (companies 90d / trackers 30d / else 120d)
  6. tracker-freshness  wiki/trackers/*.md older than 30d (called out from staleness)

Usage:
  python3 scripts/vault_hygiene.py            # human-readable report
  python3 scripts/vault_hygiene.py --json     # machine-readable (for the runner)
  python3 scripts/vault_hygiene.py --summary  # one line per check

Exit code 0 always (a report, not a gate) unless --strict (non-zero if any FAIL).
NEVER writes anything — pure read-only scan.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vault_parsers import (  # noqa: E402
    parse_frontmatter,
    extract_wikilinks,
    get_last_updated,
)

VAULT_ROOT = Path(__file__).resolve().parent.parent
WIKI = VAULT_ROOT / "wiki"
INDEX = VAULT_ROOT / "index.md"
ONBOARDING = VAULT_ROOT / ".claude" / "skills" / "agent-onboarding" / "SKILL.md"

# Page-type subdirectories under wiki/ (the catalogued types).
SUBDIRS = ["companies", "chokepoints", "themes", "trackers", "relationships"]

# Index.md H2 section name per subdir (for index-sync + count-drift).
INDEX_SECTION = {
    "companies": "Companies",
    "chokepoints": "Chokepoints",
    "themes": "Themes",
    "trackers": "Trackers",
    "relationships": "Relationships",
}

# Staleness thresholds (days) by page type.
STALE_DAYS = {
    "companies": 90,
    "chokepoints": 120,
    "themes": 120,
    "trackers": 30,
    "relationships": 120,
}

# Valid tier tokens (per CLAUDE.md Section 3.2). Layer allows 1-6; *_tier allows 1-5 + outside.
TIER_FIELDS = [
    "photonics_tier", "memory_tier", "energy_power_tier",
    "equipment_tier", "materials_tier", "defense_tier",
]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# index.md row: | [Name](wiki/<dir>/<file>.md) | ... | YYYY-MM-DD |
INDEX_ROW_RE = re.compile(r"\[([^\]]+)\]\((wiki/([a-z]+)/([^)]+)\.md)\)")
# trailing date cell in a table row
ROW_DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})\s*\|?\s*$")


def _today() -> date:
    return date.today()


def _iter_pages():
    """Yield (subdir, path, stem) for every wiki/<subdir>/*.md page."""
    for sub in SUBDIRS:
        d = WIKI / sub
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            yield sub, p, p.stem


def _valid_link_targets() -> set[str]:
    """All resolvable wikilink targets = every page filename stem across wiki/."""
    targets = set()
    for _sub, _p, stem in _iter_pages():
        targets.add(stem)
    return targets


def _parse_days(date_str: str | None) -> int | None:
    if not date_str or not DATE_RE.match(date_str):
        return None
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
    return (_today() - d).days


# ---------------------------------------------------------------------------
# Check 1 — link integrity
# ---------------------------------------------------------------------------
def check_link_integrity():
    targets = _valid_link_targets()
    targets_lower = {t.lower(): t for t in targets}
    # dedupe to unique (page, link) with an occurrence count
    unresolved: dict = {}
    self_links: dict = {}
    casing: dict = {}
    for _sub, p, stem in _iter_pages():
        text = p.read_text(encoding="utf-8")
        for raw in extract_wikilinks(text):
            link = raw.strip()
            if link in targets:
                if link == stem:
                    self_links[(p.name, link)] = self_links.get((p.name, link), 0) + 1
                continue
            if link.lower() in targets_lower:
                key = (p.name, link, targets_lower[link.lower()])
                casing[key] = casing.get(key, 0) + 1
            else:
                unresolved[(p.name, link)] = unresolved.get((p.name, link), 0) + 1

    def _u(d):  # unique-pair list, sorted by page
        return [{"page": k[0], "link": k[1], "count": v} for k, v in sorted(d.items())]

    casing_list = [{"page": k[0], "link": k[1], "target": k[2], "count": v}
                   for k, v in sorted(casing.items())]
    status = "PASS"
    if self_links or casing or unresolved:
        # forward-links (unresolved) are allowed per CLAUDE.md 3.3; self-links violate it →
        # all surface as WARN for human review, never auto-FAIL (read-only, propose-only).
        status = "WARN"
    return {
        "check": "link-integrity",
        "status": status,
        "unresolved": _u(unresolved),        # possible forward-links OR typos
        "self_links": _u(self_links),        # a page linking to itself (§3.3 defect)
        "casing_mismatch": casing_list,      # [[X]] vs file Xx (defect)
        "summary": f"{len(unresolved)} unresolved pair(s), {len(self_links)} self-link page-pair(s), "
                   f"{len(casing)} casing-mismatch (valid targets={len(targets)})",
    }


# ---------------------------------------------------------------------------
# Index parsing (shared by index-sync + count-drift)
# ---------------------------------------------------------------------------
def _index_rows_by_dir() -> dict[str, list[tuple[str, str]]]:
    """Return {subdir: [(display_name, file_stem), ...]} parsed from index.md."""
    out = {s: [] for s in SUBDIRS}
    if not INDEX.exists():
        return out
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        m = INDEX_ROW_RE.search(line)
        if not m:
            continue
        _name, _relpath, dirn, filestem = m.group(1), m.group(2), m.group(3), m.group(4)
        if dirn in out:
            out[dirn].append((_name, filestem))
    return out


# ---------------------------------------------------------------------------
# Check 2 — index sync
# ---------------------------------------------------------------------------
def check_index_sync():
    idx = _index_rows_by_dir()
    missing_from_index, missing_on_disk = [], []
    for sub in SUBDIRS:
        disk = {stem for _s, _p, stem in _iter_pages() if _s == sub}
        listed = {stem for _name, stem in idx.get(sub, [])}
        for stem in sorted(disk - listed):
            missing_from_index.append(f"{sub}/{stem}")
        for stem in sorted(listed - disk):
            missing_on_disk.append(f"{sub}/{stem}")
    status = "FAIL" if (missing_from_index or missing_on_disk) else "PASS"
    return {
        "check": "index-sync",
        "status": status,
        "missing_from_index": missing_from_index,  # file on disk, no index row
        "missing_on_disk": missing_on_disk,        # index row, no file (dead catalog link)
        "summary": f"{len(missing_from_index)} on-disk-not-indexed, "
                   f"{len(missing_on_disk)} indexed-but-missing",
    }


# ---------------------------------------------------------------------------
# Check 3 — count drift
# ---------------------------------------------------------------------------
def check_count_drift():
    idx = _index_rows_by_dir()
    rows = []
    drift = False
    for sub in SUBDIRS:
        disk_n = sum(1 for _s, _p, _st in _iter_pages() if _s == sub)
        index_n = len(idx.get(sub, []))
        match = disk_n == index_n
        if not match:
            drift = True
        rows.append({"type": sub, "disk": disk_n, "index": index_n, "match": match})
    # doc "~N" hints in agent-onboarding (the kind we hand-fixed)
    doc_hints = []
    if ONBOARDING.exists():
        txt = ONBOARDING.read_text(encoding="utf-8")
        for noun, sub in [("companies", "companies"), ("chokepoints", "chokepoints"),
                          ("themes", "themes"), ("trackers", "trackers"),
                          ("relationship", "relationships")]:
            for m in re.finditer(rf"~?(\d+)\s+{noun}", txt):
                stated = int(m.group(1))
                actual = sum(1 for _s, _p, _st in _iter_pages() if _s == sub)
                # allow ±1 slack for "~" approximate hints
                ok = abs(stated - actual) <= 1
                doc_hints.append({"noun": noun, "stated": stated, "actual": actual, "ok": ok})
                if not ok:
                    drift = True
                break  # first hint per noun is enough
    status = "WARN" if drift else "PASS"
    return {
        "check": "count-drift",
        "status": status,
        "rows": rows,
        "doc_hints": doc_hints,
        "summary": "disk-vs-index "
                   + ", ".join(f"{r['type']}={r['disk']}/{r['index']}" for r in rows),
    }


# ---------------------------------------------------------------------------
# Check 4 — frontmatter integrity (company pages)
# ---------------------------------------------------------------------------
def _tier_ok(val) -> bool:
    if val is None:
        return True
    s = str(val).strip().lower()
    if s in ("outside", "—", "-", ""):
        return True
    # accept single ints, comma/dash ranges of ints (e.g. "1, 2", "3-4", "4-6")
    parts = re.split(r"[,\-/]", s)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if part == "outside":
            continue
        if not part.isdigit():
            return False
    return True


def check_frontmatter():
    issues = []
    n = 0
    for sub, p, stem in _iter_pages():
        if sub != "companies":
            continue
        n += 1
        fm, _body = parse_frontmatter(p.read_text(encoding="utf-8"))
        if not fm:
            issues.append((p.name, "no frontmatter / unparseable"))
            continue
        if "type" not in fm:
            issues.append((p.name, "missing 'type'"))
        if "tickers" not in fm:
            issues.append((p.name, "missing 'tickers'"))
        lu = get_last_updated(fm)
        if lu is None:
            issues.append((p.name, "missing 'last_updated'"))
        elif not DATE_RE.match(str(lu)):
            issues.append((p.name, f"last_updated not YYYY-MM-DD: {lu!r}"))
        if "layer" in fm and not _tier_ok(fm.get("layer")):
            issues.append((p.name, f"bad layer value: {fm.get('layer')!r}"))
        for tf in TIER_FIELDS:
            if tf in fm and not _tier_ok(fm.get(tf)):
                issues.append((p.name, f"bad {tf} value: {fm.get(tf)!r}"))
    status = "FAIL" if issues else "PASS"
    return {
        "check": "frontmatter",
        "status": status,
        "issues": issues,
        "summary": f"{len(issues)} issue(s) across {n} company pages",
    }


# ---------------------------------------------------------------------------
# Check 5 + 6 — staleness + tracker-freshness
# ---------------------------------------------------------------------------
def check_staleness():
    stale, missing_date = [], []
    for sub, p, stem in _iter_pages():
        fm, _body = parse_frontmatter(p.read_text(encoding="utf-8"))
        lu = get_last_updated(fm)
        days = _parse_days(lu)
        if days is None:
            missing_date.append(f"{sub}/{stem}")
            continue
        threshold = STALE_DAYS.get(sub, 120)
        if days > threshold:
            stale.append({"page": f"{sub}/{stem}", "days": days, "threshold": threshold,
                          "last_updated": lu})
    stale.sort(key=lambda r: -r["days"])
    status = "WARN" if stale else "PASS"
    return {
        "check": "staleness",
        "status": status,
        "stale": stale,
        "missing_date": missing_date,
        "summary": f"{len(stale)} stale, {len(missing_date)} without a parseable last_updated",
    }


def check_tracker_freshness():
    rows = []
    overdue = False
    for sub, p, stem in _iter_pages():
        if sub != "trackers":
            continue
        fm, _body = parse_frontmatter(p.read_text(encoding="utf-8"))
        lu = get_last_updated(fm)
        days = _parse_days(lu)
        is_overdue = days is not None and days > STALE_DAYS["trackers"]
        if is_overdue or days is None:
            overdue = True
        rows.append({"tracker": stem, "last_updated": lu, "days": days,
                     "overdue": is_overdue})
    rows.sort(key=lambda r: -(r["days"] or 0))
    status = "WARN" if overdue else "PASS"
    return {
        "check": "tracker-freshness",
        "status": status,
        "rows": rows,
        "summary": f"{sum(1 for r in rows if r['overdue'])}/{len(rows)} trackers overdue "
                   f"(>{STALE_DAYS['trackers']}d)",
    }


CHECKS = [
    check_link_integrity,
    check_index_sync,
    check_count_drift,
    check_frontmatter,
    check_staleness,
    check_tracker_freshness,
]


def run_all() -> dict:
    results = [c() for c in CHECKS]
    worst = "PASS"
    order = {"PASS": 0, "WARN": 1, "FAIL": 2}
    for r in results:
        if order[r["status"]] > order[worst]:
            worst = r["status"]
    return {"as_of": _today().isoformat(), "overall": worst, "checks": results}


def _print_human(report: dict):
    icon = {"PASS": "✅", "WARN": "⚠️ ", "FAIL": "❌"}
    print(f"# Vault hygiene — {report['as_of']}  →  overall {icon[report['overall']]}{report['overall']}\n")
    for r in report["checks"]:
        print(f"{icon[r['status']]} {r['check']}: {r['summary']}")
        if r["check"] == "link-integrity":
            for x in r["casing_mismatch"]:
                print(f"     · CASING {x['page']} → [[{x['link']}]] (file is {x['target']})")
            for x in r["self_links"][:20]:
                print(f"     · self-link {x['page']} → [[{x['link']}]] (×{x['count']})")
            if len(r["self_links"]) > 20:
                print(f"     · … {len(r['self_links']) - 20} more self-link pages")
            for x in r["unresolved"][:25]:
                print(f"     · unresolved {x['page']} → [[{x['link']}]] (×{x['count']}) — forward-link or typo?")
            if len(r["unresolved"]) > 25:
                print(f"     · … {len(r['unresolved']) - 25} more unresolved")
        elif r["check"] == "index-sync":
            for x in r["missing_from_index"]:
                print(f"     · on disk, not in index: {x}")
            for x in r["missing_on_disk"]:
                print(f"     · in index, no file: {x}  ← dead catalog link")
        elif r["check"] == "count-drift":
            for row in r["rows"]:
                if not row["match"]:
                    print(f"     · {row['type']}: disk={row['disk']} index={row['index']}  ← drift")
            for h in r["doc_hints"]:
                if not h["ok"]:
                    print(f"     · onboarding says ~{h['stated']} {h['noun']}, actual {h['actual']}  ← drift")
        elif r["check"] == "frontmatter":
            for pg, msg in r["issues"][:25]:
                print(f"     · {pg}: {msg}")
        elif r["check"] == "staleness":
            for s in r["stale"][:15]:
                print(f"     · {s['page']}: {s['days']}d (>{s['threshold']}d) — {s['last_updated']}")
            if len(r["stale"]) > 15:
                print(f"     · … {len(r['stale']) - 15} more stale")
        elif r["check"] == "tracker-freshness":
            for row in r["rows"]:
                flag = "  ← OVERDUE" if row["overdue"] else ""
                print(f"     · {row['tracker']}: {row['days']}d ({row['last_updated']}){flag}")
        print()


def quick_check(file_path: str) -> int:
    """Fast single-file check (for the post-edit hook): the edited page's links resolve
    and the page is catalogued in index.md. ~50ms; no full-vault scan."""
    p = Path(file_path)
    if not (p.suffix == ".md" and "wiki" in p.parts and p.exists()):
        return 0  # not a wiki page — nothing to check
    targets = _valid_link_targets()
    targets_lower = {t.lower() for t in targets}
    text = p.read_text(encoding="utf-8")
    links = [ln.strip() for ln in extract_wikilinks(text)]
    unresolved = sorted({ln for ln in links if ln not in targets and ln.lower() not in targets_lower})
    self_link = p.stem in links
    in_index = INDEX.exists() and f"/{p.stem}.md)" in INDEX.read_text(encoding="utf-8")
    problems = []
    if unresolved:
        problems.append("unresolved " + ", ".join(f"[[{x}]]" for x in unresolved[:6]))
    if not in_index:
        problems.append("NOT in index.md")
    if self_link:
        problems.append("self-link (§3.3)")
    if problems:
        print(f"⚠️  {p.name}: " + "; ".join(problems))
        return 1
    print(f"✅ {p.name}: links resolve, indexed")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Deterministic vault hygiene scan (read-only).")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--summary", action="store_true", help="one line per check")
    ap.add_argument("--quick-check", metavar="PATH",
                    help="fast single-file check (links + index presence); for the post-edit hook")
    ap.add_argument("--strict", action="store_true", help="exit non-zero if any check FAILs")
    args = ap.parse_args()

    if args.quick_check:
        sys.exit(quick_check(args.quick_check))
    report = run_all()
    if args.json:
        print(json.dumps(report, indent=2))
    elif args.summary:
        icon = {"PASS": "✅", "WARN": "⚠️", "FAIL": "❌"}
        print(f"hygiene {report['as_of']}: overall {report['overall']}")
        for r in report["checks"]:
            print(f"  {icon[r['status']]} {r['check']}: {r['summary']}")
    else:
        _print_human(report)
    if args.strict and report["overall"] == "FAIL":
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
