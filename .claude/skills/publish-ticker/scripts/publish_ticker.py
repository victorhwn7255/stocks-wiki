#!/usr/bin/env python3
"""publish-ticker merge script.

Takes a staging JSON ({"accounts": [...], "sources": [...]}) produced by the
publish-ticker skill, runs mechanical scrub + shape checks, and upserts the
entries into kicker-app's content/accounts.json and content/sources.json.

Usage:
  python3 publish_ticker.py /tmp/publish-ticker-<page>.json [--dry-run]
      [--kicker /Users/victor_he/Projects/kicker-app]

Exit codes: 0 ok, 1 validation/scrub failure (nothing written).
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

KINDS = {"company", "chokepoint", "theme"}
TIERS = {"solid", "needs", "disputed", "open"}
HANDLE_RE = re.compile(r"^@[A-Za-z0-9-]+$")
SOURCE_ID_RE = re.compile(r"^src-[a-z0-9-]+$")

# Scrub: ERROR patterns (internal notation / advice language) - block the merge.
SCRUB_ERRORS = [
    (re.compile(r"\[\["), "wikilink notation [[...]]"),
    (re.compile(r"\bSection \d+\.\d+"), "vault section reference"),
    (re.compile(r"\bCLAUDE\.md\b"), "internal file reference"),
    (re.compile(r"\b(raw|wiki)/[A-Za-z0-9_./-]+"), "internal file path"),
    (re.compile(r"\brefresh_log\b"), "internal log reference"),
    (re.compile(r"\bTier [1-5]\b"), "vault tier jargon (map to kicker tier instead)"),
    # buy/sell advice language; allow "sell-side" (a noun) and "sell-off".
    (re.compile(r"\b(buy|sell(?!-side|-off))\b(?! signal)", re.IGNORECASE), "buy/sell language"),
    (re.compile(r"\bprice[- ]?target\b", re.IGNORECASE), "price-target language"),
    (re.compile(r"\b(bullish|bearish|overweight|underweight)\b", re.IGNORECASE), "sentiment/advice language"),
]
# Scrub: WARN patterns - print loudly, do not block (human judges).
SCRUB_WARNINGS = [
    (re.compile(r"\b(Fundstrat|LSEG)\b", re.IGNORECASE), "possible proprietary-source mention"),
    (re.compile(r"\bJ\.?P\.?\s?Morgan\b", re.IGNORECASE), "possible proprietary-source mention"),
    (re.compile(r"\bchokepoint\b", re.IGNORECASE), "vault term 'chokepoint' in outsider text (bio/desc ok if explained; consider 'bottleneck')"),
]

REQ_ACCOUNT = ["handle", "kind", "vault_page", "desc", "bio", "persona_card"]
REQ_SOURCE = ["id", "account", "section_title", "body_text", "tier"]

# vault_page is the join key for kicker's /check-accounts coverage checker: the
# originating wiki page's filename stem. Validate it points at a real page so a
# typo can never break the vault<->account linkage. The vault root is derived
# from this script's own location (.claude/skills/publish-ticker/scripts/).
VAULT_ROOT = Path(__file__).resolve().parents[4]
KIND_DIRS = {"company": "companies", "chokepoint": "chokepoints", "theme": "themes"}


def text_fields(obj, prefix=""):
    """Yield (path, string) for every string in a nested structure."""
    if isinstance(obj, str):
        yield prefix, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from text_fields(v, f"{prefix}.{k}" if prefix else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from text_fields(v, f"{prefix}[{i}]")


def scrub(entry, label, errors, warnings):
    for path, s in text_fields(entry):
        # Exemptions: enum values, the vault_page join key, the source_date, and a
        # video_links URL are structured data, not prose (a youtube.com URL would
        # otherwise trip the internal-path pattern). The standard persona constraints
        # legitimately QUOTE the banned advice words in order to ban them.
        if (
            path in ("kind", "tier", "vault_page", "source_date")
            or path.endswith((".kind", ".tier", ".vault_page"))
            or (path.startswith("video_links[") and path.endswith(".url"))
        ):
            continue
        in_constraints = "persona_card.constraints" in path
        for rx, why in SCRUB_ERRORS:
            if in_constraints and why in ("buy/sell language", "sentiment/advice language", "price-target language"):
                continue
            m = rx.search(s)
            if m:
                errors.append(f"{label} {path}: {why} -> ...{s[max(0, m.start()-30):m.end()+30]}...")
        for rx, why in SCRUB_WARNINGS:
            m = rx.search(s)
            if m:
                warnings.append(f"{label} {path}: {why} -> ...{s[max(0, m.start()-30):m.end()+30]}...")


def validate(staging, existing_handles):
    errors, warnings = [], []
    accounts = staging.get("accounts", [])
    sources = staging.get("sources", [])
    if not accounts and not sources:
        errors.append("staging file has neither accounts nor sources")

    staged_handles = set()
    for a in accounts:
        label = f"account {a.get('handle', '?')}"
        for f in REQ_ACCOUNT:
            if not a.get(f):
                errors.append(f"{label}: missing required field '{f}'")
        if a.get("handle") and not HANDLE_RE.match(a["handle"]):
            errors.append(f"{label}: bad handle format")
        if a.get("kind") not in KINDS:
            errors.append(f"{label}: kind must be one of {sorted(KINDS)}")
        pc = a.get("persona_card") or {}
        if not pc.get("voice") or not isinstance(pc.get("constraints"), list) or len(pc.get("constraints", [])) < 4:
            errors.append(f"{label}: persona_card needs voice + the 4 standard constraints")
        vp, kind_dir = a.get("vault_page"), KIND_DIRS.get(a.get("kind", ""))
        if vp and kind_dir and not (VAULT_ROOT / "wiki" / kind_dir / f"{vp}.md").is_file():
            errors.append(f"{label}: vault_page '{vp}' not found at wiki/{kind_dir}/{vp}.md (typo, or wrong kind?)")
        for i, k in enumerate(a.get("knows", []) or []):
            if k.get("tier") not in TIERS or not k.get("claim"):
                errors.append(f"{label}: knows[{i}] needs claim + valid tier")
        for h in a.get("supply_chain", []) or []:
            if h not in existing_handles and h not in {x.get("handle") for x in accounts}:
                errors.append(f"{label}: supply_chain points at unknown handle {h}")
        if a.get("handle"):
            staged_handles.add(a["handle"])
        scrub(a, label, errors, warnings)

    for s in sources:
        label = f"source {s.get('id', '?')}"
        for f in REQ_SOURCE:
            if not s.get(f):
                errors.append(f"{label}: missing required field '{f}'")
        if s.get("id") and not SOURCE_ID_RE.match(s["id"]):
            errors.append(f"{label}: id must match src-<kebab>")
        if s.get("tier") not in TIERS:
            errors.append(f"{label}: tier must be one of {sorted(TIERS)}")
        acct = s.get("account")
        if acct and acct not in existing_handles and acct not in staged_handles:
            errors.append(f"{label}: account {acct} not found in kicker accounts or staging")
        body = s.get("body_text", "")
        if body and not (120 <= len(body) <= 1200):
            warnings.append(f"{label}: body_text length {len(body)} outside the comfortable 120-1200 range")
        # Optional fields used by time-bound / commentary accounts (e.g. @youtube-buzz):
        # source_date drives the engine's freshness window; video_links are the "watch
        # the footage" receipts the feed renders in place of a tier pill.
        sd = s.get("source_date")
        if sd is not None and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(sd)):
            errors.append(f"{label}: source_date '{sd}' must be YYYY-MM-DD")
        vl = s.get("video_links")
        if vl is not None:
            if not isinstance(vl, list) or not vl:
                errors.append(f"{label}: video_links must be a non-empty list when present")
            else:
                for i, v in enumerate(vl):
                    if not isinstance(v, dict) or not v.get("channel") or not v.get("url"):
                        errors.append(f"{label}: video_links[{i}] needs both channel and url")
        scrub(s, label, errors, warnings)

    return errors, warnings


def upsert(target, items, key):
    added, updated, unchanged = [], [], []
    index = {t.get(key): i for i, t in enumerate(target)}
    for item in items:
        k = item.get(key)
        if k in index:
            if target[index[k]] == item:
                unchanged.append(k)
            else:
                target[index[k]] = item
                updated.append(k)
        else:
            target.append(item)
            added.append(k)
    return added, updated, unchanged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("staging")
    ap.add_argument("--kicker", default="/Users/victor_he/Projects/kicker-app")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    kicker = Path(args.kicker)
    acc_path = kicker / "content" / "accounts.json"
    src_path = kicker / "content" / "sources.json"
    for p in (acc_path, src_path):
        if not p.exists():
            sys.exit(f"FATAL: {p} not found - wrong --kicker path?")

    staging = json.loads(Path(args.staging).read_text())
    accounts = json.loads(acc_path.read_text())
    sources = json.loads(src_path.read_text())
    existing_handles = {a.get("handle") for a in accounts}

    errors, warnings = validate(staging, existing_handles)
    for w in warnings:
        print(f"WARN  {w}")
    if errors:
        for e in errors:
            print(f"ERROR {e}")
        sys.exit(1)

    a_add, a_upd, a_same = upsert(accounts, staging.get("accounts", []), "handle")
    s_add, s_upd, s_same = upsert(sources, staging.get("sources", []), "id")

    print(f"accounts: +{len(a_add)} added {a_add}, ~{len(a_upd)} updated {a_upd}, ={len(a_same)} unchanged")
    print(f"sources:  +{len(s_add)} added {s_add}, ~{len(s_upd)} updated {s_upd}, ={len(s_same)} unchanged")

    if args.dry_run:
        print("DRY RUN - nothing written.")
        return

    acc_path.write_text(json.dumps(accounts, indent=2, ensure_ascii=False) + "\n")
    src_path.write_text(json.dumps(sources, indent=2, ensure_ascii=False) + "\n")
    print(f"WROTE {acc_path}")
    print(f"WROTE {src_path}")
    print("Next (kicker-side, user-gated): review `git diff content/`, then")
    print("  pnpm validate-content && pnpm engine:audit-sources && pnpm db:seed")


if __name__ == "__main__":
    main()
