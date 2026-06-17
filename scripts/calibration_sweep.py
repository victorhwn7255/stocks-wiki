#!/usr/bin/env python3
"""
calibration_sweep.py — deterministic half of the self-evaluation loop.

Read-only. Parses the vault's pre-registered falsifiers / dated catalysts / tripwires
from the two trackers (and, optionally, Open-questions sections) and emits a CANDIDATE
LIST of entries that are due for review — the input the agentic scorer (`claude -p`
calibration prompt) then judges against current primary state.

It does NOT score (that needs reasoning + current-state reading) and does NOT write to
canon. It surfaces WHAT to check and flags overdue / temporally-triggered items.

Sources:
  wiki/trackers/forward-edge-tracker.md   — entries with Catalyst / Falsifier / Last moved
  wiki/trackers/what-could-go-wrong.md    — entries with Tripwire / Status / Last checked

Usage:
  python3 scripts/calibration_sweep.py            # human-readable candidate list
  python3 scripts/calibration_sweep.py --json      # machine-readable (for the runner)
  python3 scripts/calibration_sweep.py --due-days 30
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
FORWARD_EDGE = VAULT_ROOT / "wiki" / "trackers" / "forward-edge-tracker.md"
RISK_REGISTER = VAULT_ROOT / "wiki" / "trackers" / "what-could-go-wrong.md"

ISO_DATE = re.compile(r"\b(20\d\d-\d\d-\d\d)\b")
MONTHS = ("January|February|March|April|May|June|July|August|September|October|November|December")
TEMPORAL = re.compile(
    rf"\b(Q[1-4]\s*FY?\s*20\d\d|Q[1-4]\b|FY\s?20\d\d|fiscal\s+20\d\d|"
    rf"(?:{MONTHS})(?:\s+\d{{1,2}})?(?:,?\s+20\d\d)?|20\d\d-\d\d-\d\d)\b",
    re.IGNORECASE,
)
# a bolded bullet field: "- **Catalyst / re-rate triggers:** text..."
FIELD_RE = re.compile(r"^\s*-\s*\*\*([^:*]+?):?\*\*\s*(.*)$")


def _today() -> date:
    return date.today()


def _days_since(iso: str | None) -> int | None:
    if not iso:
        return None
    try:
        d = datetime.strptime(iso, "%Y-%m-%d").date()
    except ValueError:
        return None
    return (_today() - d).days


def _first_iso(text: str) -> str | None:
    m = ISO_DATE.search(text or "")
    return m.group(1) if m else None


def _temporal_markers(text: str) -> list[str]:
    seen, out = set(), []
    for m in TEMPORAL.finditer(text or ""):
        s = re.sub(r"\s+", " ", m.group(1)).strip()
        key = s.lower()
        if key not in seen and not ISO_DATE.fullmatch(s):  # ISO handled separately as the date
            seen.add(key)
            out.append(s)
    return out


def _split_entries(text: str) -> list[tuple[str, str]]:
    """Split a tracker body into (title, block) on '### ' headers."""
    parts = re.split(r"^###\s+", text, flags=re.MULTILINE)
    entries = []
    for part in parts[1:]:
        lines = part.splitlines()
        title = lines[0].strip() if lines else ""
        block = "\n".join(lines[1:])
        entries.append((title, block))
    return entries


def _fields(block: str) -> dict[str, str]:
    """Collect bolded '- **Label:** value' fields from an entry block."""
    out = {}
    for line in block.splitlines():
        m = FIELD_RE.match(line)
        if m:
            label = m.group(1).strip().lower()
            out[label] = m.group(2).strip()
    return out


def _match_field(fields: dict, *needles: str) -> str:
    for label, val in fields.items():
        for n in needles:
            if n in label:
                return val
    return ""


def sweep_forward_edge(due_days: int) -> list[dict]:
    if not FORWARD_EDGE.exists():
        return []
    out = []
    for title, block in _split_entries(FORWARD_EDGE.read_text(encoding="utf-8")):
        f = _fields(block)
        catalyst = _match_field(f, "catalyst")
        falsifier = _match_field(f, "falsifier")
        last_moved_raw = _match_field(f, "last moved", "last_moved")
        last_moved = _first_iso(last_moved_raw)
        days = _days_since(last_moved)
        markers = sorted(set(_temporal_markers(catalyst) + _temporal_markers(falsifier)))
        review_due = days is not None and days >= due_days
        out.append({
            "source": "forward-edge-tracker",
            "title": re.sub(r"\s+", " ", title).strip(),
            "last_moved": last_moved,
            "days_since": days,
            "review_due": review_due,
            "has_catalyst": bool(catalyst),
            "has_falsifier": bool(falsifier),
            "temporal_markers": markers,
            "catalyst": catalyst[:400],
            "falsifier": falsifier[:400],
        })
    return out


def sweep_risk_register(due_days: int) -> list[dict]:
    if not RISK_REGISTER.exists():
        return []
    out = []
    for title, block in _split_entries(RISK_REGISTER.read_text(encoding="utf-8")):
        f = _fields(block)
        tripwire = _match_field(f, "tripwire")
        status = _match_field(f, "status")
        last_checked_raw = _match_field(f, "last checked", "last_checked")
        last_checked = _first_iso(last_checked_raw)
        days = _days_since(last_checked)
        fired = bool(re.search(r"\bFIRED\b", status)) and not re.search(r"NOT\s+FIRED", status)
        partial = bool(re.search(r"\bPARTIAL\b", status, re.IGNORECASE))
        markers = sorted(set(_temporal_markers(tripwire)))
        review_due = days is not None and days >= due_days
        out.append({
            "source": "what-could-go-wrong",
            "title": re.sub(r"^\d+\.\s*", "", re.sub(r"\s+", " ", title).strip()),
            "last_checked": last_checked,
            "days_since": days,
            "review_due": review_due,
            "fired": fired,
            "partial": partial,
            "temporal_markers": markers,
            "tripwire": tripwire[:400],
            "status": status[:300],
        })
    return out


def run(due_days: int) -> dict:
    fe = sweep_forward_edge(due_days)
    rr = sweep_risk_register(due_days)
    candidates = sorted(
        fe + rr,
        key=lambda e: (
            not e.get("fired", False),                    # fired risks first
            not e.get("review_due", False),               # then review-due
            -(e.get("days_since") or 0),                  # then oldest
        ),
    )
    return {
        "as_of": _today().isoformat(),
        "due_days": due_days,
        "counts": {
            "forward_edge": len(fe),
            "risk_register": len(rr),
            "review_due": sum(1 for e in candidates if e.get("review_due")),
            "fired": sum(1 for e in candidates if e.get("fired")),
        },
        "candidates": candidates,
    }


def _print_human(report: dict):
    c = report["counts"]
    print(f"# Calibration sweep — {report['as_of']}  "
          f"(due-threshold {report['due_days']}d)\n")
    print(f"forward-edge entries: {c['forward_edge']} · risk-register entries: {c['risk_register']} · "
          f"review-due: {c['review_due']} · FIRED: {c['fired']}\n")
    print("Candidates to score against current primary state (oldest / fired first):\n")
    for e in report["candidates"]:
        tag = "🔴 FIRED" if e.get("fired") else ("⏳ REVIEW-DUE" if e.get("review_due") else "·")
        anchor = e.get("last_moved") or e.get("last_checked") or "—"
        days = e.get("days_since")
        days_s = f"{days}d" if days is not None else "no-date"
        print(f"[{tag}] ({e['source']}) {e['title']}")
        print(f"        last touched {anchor} ({days_s})")
        if e["source"] == "forward-edge-tracker":
            miss = []
            if not e["has_catalyst"]:
                miss.append("NO CATALYST")
            if not e["has_falsifier"]:
                miss.append("NO FALSIFIER")
            if miss:
                print(f"        ⚠️  {' + '.join(miss)} (entry contract violation)")
        if e.get("temporal_markers"):
            print(f"        watch dates: {', '.join(e['temporal_markers'][:8])}")
        print()


def main():
    ap = argparse.ArgumentParser(description="Deterministic calibration sweep (read-only).")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--due-days", type=int, default=30,
                    help="days since last-moved/last-checked to flag REVIEW-DUE (default 30)")
    args = ap.parse_args()
    report = run(args.due_days)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        _print_human(report)
    sys.exit(0)


if __name__ == "__main__":
    main()
