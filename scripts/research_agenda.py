#!/usr/bin/env python3
"""
research_agenda.py — manage the self-research agenda (raw/research/topics-list.md).

Deterministic helper for the automation's daily deep-research step:
  --pick            print the top Pending question (clean text) for the deep-research prompt
  --mark-done PATH  move the top Pending item → Researched (with today's date + report path)
  --propose         append connection-finder HIGH-signal clusters to the Proposed section

Reads/writes ONLY raw/research/topics-list.md (Tier-3 research zone — not canon). Never
touches wiki/ / index.md / log.md / the anchors.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
TOPICS = VAULT_ROOT / "raw" / "research" / "topics-list.md"

PENDING_HDR = "## Pending"
RESEARCHED_HDR = "## Researched"
PROPOSED_HDR = "## Proposed by automation"
# a Pending item line: "1. [P1] <question> — *<source>*"
ITEM_RE = re.compile(r"^\s*\d+\.\s+(?:\[[^\]]+\]\s*)?(.*)$")


def _read() -> str:
    return TOPICS.read_text(encoding="utf-8") if TOPICS.exists() else ""


def _today() -> str:
    return date.today().isoformat()


def _header_index(lines: list[str], header: str) -> int | None:
    for i, ln in enumerate(lines):
        if ln.startswith(header):
            return i
    return None


def _pending_item_lines(lines: list[str]) -> list[int]:
    start = _header_index(lines, PENDING_HDR)
    end = _header_index(lines, RESEARCHED_HDR)
    if start is None:
        return []
    end = end if end is not None else len(lines)
    out = []
    for i in range(start + 1, end):
        s = lines[i].strip()
        if s and s[0].isdigit() and ITEM_RE.match(s):
            out.append(i)
    return out


def _clean_question(raw: str) -> str:
    m = ITEM_RE.match(raw.strip())
    q = m.group(1) if m else raw.strip()
    return re.split(r"\s+—\s+\*", q)[0].strip()  # drop the trailing " — *source*" note


def cmd_pick() -> str:
    lines = _read().splitlines()
    items = _pending_item_lines(lines)
    if not items:
        return ""
    return _clean_question(lines[items[0]])


def cmd_mark_done(report_path: str) -> None:
    lines = _read().splitlines()
    items = _pending_item_lines(lines)
    if not items:
        return
    top = items[0]
    question = _clean_question(lines[top])
    del lines[top]                                   # remove from Pending
    # renumber remaining Pending items 1..N — both the list number AND the [Pn] tag,
    # so the whole list visibly shifts up the priority order.
    for n, li in enumerate(_pending_item_lines(lines), 1):
        lines[li] = re.sub(r"^\s*\d+\.", f"{n}.", lines[li])
        lines[li] = re.sub(r"\[P\d+\]", f"[P{n}]", lines[li], count=1)
    # insert the Researched entry right under the Researched header
    rh = _header_index(lines, RESEARCHED_HDR)
    if rh is not None:
        lines.insert(rh + 1, f"- {_today()} — {question} → {report_path}")
    TOPICS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _connection_clusters() -> list[str]:
    """HIGH-signal uncaptured cross-page clusters from the connection-finder."""
    try:
        res = subprocess.run(["python3", "scripts/find_connections.py"],
                             cwd=str(VAULT_ROOT), capture_output=True, text=True, timeout=180)
    except Exception:  # noqa: BLE001
        return []
    clusters, in_high = [], False
    for ln in res.stdout.splitlines():
        if "HIGH SIGNAL" in ln:
            in_high = True
            continue
        if in_high and ln.startswith("**"):
            break
        m = re.match(r"^\s*\d+\.\s+(.+?)\s+\(cluster_score", ln)
        if m:
            clusters.append(m.group(1).strip())
    return clusters


def _open_questions(cap: int = 4) -> list[tuple[str, str]]:
    """One genuine question per theme/chokepoint page's 'Open questions' section —
    the vault's own pre-registered 'what we don't know yet'."""
    out = []
    for sub in ("themes", "chokepoints"):
        d = VAULT_ROOT / "wiki" / sub
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            text = p.read_text(encoding="utf-8")
            m = re.search(r"^#{1,4}\s+Open questions.*$", text, re.MULTILINE | re.IGNORECASE)
            if not m:
                continue
            rest = text[m.end():]
            nxt = re.search(r"^#{1,4}\s+", rest, re.MULTILINE)
            section = rest[: nxt.start()] if nxt else rest
            for line in section.splitlines():
                s = line.strip().lstrip("-*0123456789.) ").strip()
                if "?" in s and 40 <= len(s) <= 240:
                    out.append((p.stem, s))
                    break  # one per page
            if len(out) >= cap:
                return out
    return out


def cmd_propose() -> None:
    """Surface candidate research topics from multiple vault sources → the Proposed section
    (staging; Vic promotes to Pending). Each is phrased as a scoped question. Deterministic."""
    existing = _read()
    items: list[tuple[str, str]] = []  # (dedupe_token, line)
    for c in _connection_clusters():
        items.append((c, f"Is the **{c}** cluster an investable cross-vault chokepoint / theme, "
                         f"and who owns the value? — connection-finder cluster, {_today()}"))
    for page, q in _open_questions():
        items.append((q[:40], f"{q} — open question on [[{page}]], {_today()}"))
    new, seen, low = [], set(), existing.lower()
    for tok, line in items:
        t = tok.strip().lower()
        if t and t not in seen and t not in low:
            seen.add(t)
            new.append(line)
    new = new[:6]  # cap per run — avoid flooding the staging section
    if not new:
        return
    lines = existing.splitlines()
    ph = _header_index(lines, PROPOSED_HDR)
    if ph is None:
        return
    for j, b in enumerate(new):
        lines.insert(ph + 1 + j, f"- {b}")
    TOPICS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Manage the self-research agenda.")
    ap.add_argument("--pick", action="store_true")
    ap.add_argument("--mark-done", metavar="REPORT_PATH")
    ap.add_argument("--propose", action="store_true")
    args = ap.parse_args()
    if args.pick:
        sys.stdout.write(cmd_pick())
    elif args.mark_done:
        cmd_mark_done(args.mark_done)
    elif args.propose:
        cmd_propose()


if __name__ == "__main__":
    main()
