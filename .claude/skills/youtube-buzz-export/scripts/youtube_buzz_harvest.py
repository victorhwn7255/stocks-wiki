#!/usr/bin/env python3
"""youtube-buzz harvester — the deterministic half of /youtube-buzz-export.

Finds the video-intel notes inside the freshness window (default: the last 15 days,
keyed on each note's upload_date) and extracts the material a drafter needs to write
attributed, scorekeeper-voice tweets: the channel/guest/url receipt and the note's
own curated sections (TL;DR + Key claims). It does NOT write tweets, select claims,
or merge anything — that judgement is the skill's generate->verify step. This script
is pure, read-only, and gives the agent a clean machine-readable work-list.

A note with no `url:` header is skipped (no receipt -> not eligible; the whole point
of @youtube-buzz is that the source video IS the citation).

Usage:
  python3 youtube_buzz_harvest.py [--days 15] [--today YYYY-MM-DD]
      [--vault-root <path>] [--json]

Output (--json): {generated, window_days, cutoff, in_window:[...], skipped_no_url:[...],
                  out_of_window: N}. Without --json, a human-readable summary.
"""
import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[4]
NOTES_DIR = VAULT_ROOT / "raw" / "notes" / "video-intel"
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})_")


def parse_frontmatter(text):
    """Minimal YAML-ish frontmatter reader for the flat scalars we need."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val and val[0] in "\"'" and val[-1:] == val[0]:
            val = val[1:-1]
        fm[key] = val
    return fm


def extract_section(text, header):
    """Return the body of a '## <header>' section up to the next '## '."""
    lines = text.splitlines()
    out, capturing = [], False
    for ln in lines:
        if ln.startswith("## "):
            if capturing:
                break
            capturing = ln[3:].strip().lower().startswith(header.lower())
            continue
        if capturing:
            out.append(ln)
    return "\n".join(out).strip()


def note_date(fm, path):
    """Prefer the frontmatter upload_date; fall back to the filename prefix."""
    ud = fm.get("upload_date", "")
    if re.match(r"^\d{4}-\d{2}-\d{2}$", ud):
        return ud
    m = DATE_RE.match(path.name)
    return m.group(1) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=15)
    ap.add_argument("--today", default=date.today().isoformat())
    ap.add_argument("--vault-root")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    notes_dir = (Path(args.vault_root) / "raw" / "notes" / "video-intel") if args.vault_root else NOTES_DIR
    if not notes_dir.is_dir():
        sys.exit(f"FATAL: video-intel dir not found at {notes_dir}")

    today = date.fromisoformat(args.today)
    cutoff = (today - timedelta(days=args.days)).isoformat()

    in_window, skipped_no_url, out_of_window = [], [], 0
    for path in sorted(notes_dir.glob("*.md")):
        if path.name.startswith("_"):  # _index.md, _consensus.md
            continue
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        d = note_date(fm, path)
        if not d:
            continue
        if d < cutoff:
            out_of_window += 1
            continue
        url = fm.get("url", "").strip()
        rec = {
            "date": d,
            "channel": fm.get("channel", "").strip(),
            "guest": fm.get("guest", "").strip(),
            "url": url,
            "headline": fm.get("headline", "").strip(),
            "note_file": path.name,
        }
        if not url:
            skipped_no_url.append(rec)
            continue
        rec["tldr"] = extract_section(text, "TL;DR")
        rec["key_claims"] = extract_section(text, "Key claims")
        in_window.append(rec)

    result = {
        "generated": today.isoformat(),
        "window_days": args.days,
        "cutoff": cutoff,
        "in_window_count": len(in_window),
        "in_window": in_window,
        "skipped_no_url": skipped_no_url,
        "out_of_window": out_of_window,
    }

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    print(f"video-intel harvest — today {today}, window {args.days}d (cutoff {cutoff})")
    print(f"in-window notes with a URL: {len(in_window)}   "
          f"skipped (no url): {len(skipped_no_url)}   out-of-window: {out_of_window}\n")
    if not in_window:
        print("NO in-window notes -> @youtube-buzz stays silent (auto-pause). "
              "Emit an empty run; the engine's source_date filter also keeps it quiet.")
        return
    for r in in_window:
        print(f"- {r['date']}  {r['channel']}  ({r['url']})")
        if r["guest"]:
            print(f"    guest: {r['guest']}")
        if r["headline"]:
            print(f"    headline: {r['headline'][:160]}...")
    if skipped_no_url:
        print("\nskipped (no url receipt):")
        for r in skipped_no_url:
            print(f"  - {r['date']} {r['channel']} ({r['note_file']})")


if __name__ == "__main__":
    main()
