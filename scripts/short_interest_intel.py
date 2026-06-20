#!/usr/bin/env python3
"""
short_interest_intel.py — refresh the short-interest tracker from the latest snapshot.

The engine behind the /short-interest-intel skill, and the single source of truth for the
shared digest (rankings + the STANCE judgment map) that both the .md tracker and the .html
dashboard consume.

It performs a BOUNDED, cadence-aware refresh of wiki/trackers/short-interest.md:
- replaces ONLY the fenced data block (<!-- SHORT-INTEREST-DATA:START/END -->) with the latest
  tables,
- APPENDS a dated bullet to the Change log (the trend history is never overwritten),
- bumps frontmatter last_updated,
- regenerates wiki/trackers/short-interest.html,
- and leaves everything else — the frame, the Intel confirm/challenge prose, the watch-list —
  untouched. The STANCE map (the "Vault read") is carried forward, edited deliberately here.

Tier-4 sentiment data; describe-don't-recommend. Cadence: short interest is twice-monthly, so a
run on a settlement already on the page is a no-op (no churn).

Usage:
    python scripts/short_interest_intel.py --render-md          # print the data block, write nothing
    python scripts/short_interest_intel.py --update-tracker     # the bounded refresh + HTML regen
    python scripts/short_interest_intel.py --update-tracker --dry-run   # show a unified diff only
    python scripts/short_interest_intel.py --update-tracker --force     # re-render same settlement (testing)
"""

import argparse
import csv
import datetime
import difflib
import re
import subprocess
import sys
from pathlib import Path

# ── Judgment layer (single source of truth — the reviewed "Vault read") ───────
# ticker -> (stance, thesis-label); stance in {confirm, challenge, neutral}.
# Carried forward across refreshes; edit deliberately. Mirrors the .md Intel prose.
STANCE = {
    "LEU":  ("challenge", "HALEU enrichment chokepoint"),
    "CORZ": ("confirm",   "AI-datacenter host / landlord"),
    "NVTS": ("confirm",   "power semis (800V DC)"),
    "AMPX": ("neutral",   "defense silicon-anode batteries"),
    "NBIS": ("confirm",   "neocloud (GPU renter)"),
    "MP":   ("challenge", "rare-earth-magnet chokepoint"),
    "COHU": ("neutral",   "semi test (counterpoint)"),
    "LITE": ("challenge", "photonics / CPO laser"),
    "AEHR": ("neutral",   "advanced-packaging test"),
    "AAOI": ("confirm",   "transceiver assembler"),
    "NOVT": ("challenge", "humanoid sensor / datacenter"),
    "AXTI": ("neutral",   "InP substrates"),
    "VECO": ("neutral",   "semi equipment"),
    "BE":   ("neutral",   "fuel cells / BTM power"),
    "VPG":  ("confirm",   "humanoid force/torque sensor"),
    "AVAV": ("challenge", "defense drones"),
    "OUST": ("confirm",   "lidar / Physical-AI sensing"),
    "POWI": ("neutral",   "power semis"),
    "MRCY": ("challenge", "defense electronics"),
}

# Standout cards (ticker -> headline note) — curated, mirrors the change-log highlights.
STANDOUTS = [
    ("LEU",  "Loudest disagreement — crowd most-short the vault's strongest nuclear-fuel thesis"),
    ("CORZ", "Confirms the 100%-CoreWeave concentration risk — heavy and rising"),
    ("MP",   "Rare-earth chokepoint the vault is bullish on — inverse divergence"),
    ("NOVT", "Most-crowded short in the vault (10.0 days-to-cover)"),
    ("ONTO", "Skepticism spiking — short interest +78.5% vs the prior settlement"),
]

# Reading-rule thresholds (kept here so md + html agree).
SHORT_PCT_MIN = 8.0
DTC_MIN = 4.0
RISE_MIN = 15.0
FALL_MAX = -10.0

START = "<!-- SHORT-INTEREST-DATA:START -->"
END = "<!-- SHORT-INTEREST-DATA:END -->"


# ── shared data helpers ──────────────────────────────────────────────────────
def fnum(r, k):
    try:
        return float(str(r.get(k, "")).replace(",", ""))
    except (ValueError, TypeError):
        return None


def numf(v):
    try:
        return f"{int(float(str(v).replace(',', ''))):,}"
    except (ValueError, TypeError):
        return v or "—"


def hshares(v):
    """Abbreviate a share count: 284722716 -> '284.7M', 1.21e9 -> '1.21B'."""
    try:
        n = float(str(v).replace(",", ""))
    except (ValueError, TypeError):
        return "—"
    if n >= 1e9: return f"{n/1e9:.2f}B"
    if n >= 1e6: return f"{n/1e6:.1f}M"
    if n >= 1e3: return f"{n/1e3:.0f}K"
    return f"{n:.0f}"


def find_csv(root, date=None):
    d = root / "raw" / "data" / "short-interest"
    if date:
        p = d / f"short-interest_{date}.csv"
        return p if p.exists() else None
    files = sorted(d.glob("short-interest_*.csv"))
    return files[-1] if files else None


def load_snapshot(root, date=None):
    p = find_csv(root, date)
    if not p:
        return None, None
    rows = list(csv.DictReader(p.open()))
    settle = rows[0]["settlement_date"] if rows else None
    return rows, settle


def rankings(rows):
    ms = sorted([r for r in rows if (fnum(r, "pct_outstanding") or 0) >= SHORT_PCT_MIN],
                key=lambda r: fnum(r, "pct_outstanding") or 0, reverse=True)
    mc = sorted([r for r in rows if (fnum(r, "days_to_cover") or 0) >= DTC_MIN],
                key=lambda r: fnum(r, "days_to_cover") or 0, reverse=True)
    ris = sorted([r for r in rows if (fnum(r, "change_pct") or 0) >= RISE_MIN],
                 key=lambda r: fnum(r, "change_pct") or 0, reverse=True)
    fal = sorted([r for r in rows if (fnum(r, "change_pct") or 0) <= FALL_MAX],
                 key=lambda r: fnum(r, "change_pct") or 0)
    return ms, mc, ris, fal


# ── markdown rendering ───────────────────────────────────────────────────────
def _g(r, k, suffix=""):
    v = fnum(r, k)
    return f"{v:g}{suffix}" if v is not None else "—"


def _chg(r):
    v = fnum(r, "change_pct")
    if v is None:
        return "—"
    return f"+{v:g}%" if v > 0 else f"{v:g}%"


def _vr(tk):
    stance = STANCE.get(tk, ("neutral", ""))[0]
    return {"confirm": "**CONFIRM**", "challenge": "**CHALLENGE**", "neutral": "—"}[stance]


def render_md_block(rows, settle):
    """The inner content of the fenced data section (everything the skill regenerates)."""
    ms, mc, ris, fal = rankings(rows)
    notable = {r["ticker"] for grp in (ms, mc, ris, fal) for r in grp}
    L = [f"<!-- SETTLEMENT: {settle} -->", ""]

    L += [f"### Most shorted (short interest as % of shares outstanding, ≥{SHORT_PCT_MIN:g}%)", "",
          "| ticker | short interest | short %out | days-to-cover | Δ vs prior | vault read | thesis |",
          "|---|---|---|---|---|---|---|"]
    for r in ms:
        tk = r["ticker"]; thesis = STANCE.get(tk, ("neutral", ""))[1]
        L.append(f"| **{tk}** | {hshares(r.get('shares_short'))} | {_g(r,'pct_outstanding','%')} | "
                 f"{_g(r,'days_to_cover')} | {_chg(r)} | {_vr(tk)} | {thesis} |")

    L += ["", f"### Most crowded (days-to-cover ≥{DTC_MIN:g})", ""]
    L.append(" · ".join(f"{r['ticker']} {_g(r,'days_to_cover')}" for r in mc) or "—")

    L += ["", "### Movers (change vs the prior settlement)", ""]
    L.append("- **Skepticism building (rising short):** "
             + (" · ".join(f"{r['ticker']} {_chg(r)}" for r in ris) or "—"))
    L.append("- **Bears covering (falling short):** "
             + (" · ".join(f"{r['ticker']} {_chg(r)}" for r in fal) or "—"))

    L += ["", f"*(The other {len(rows) - len(notable)} vault names sit below all thresholds — "
          "low short interest, nothing notable.)*"]
    return "\n".join(L)


def render_changelog_line(rows, settle, run_date):
    ms, mc, ris, _ = rankings(rows)
    top_short = f"{ms[0]['ticker']} {_g(ms[0],'pct_outstanding','%')}" if ms else "—"
    top_dtc = f"{mc[0]['ticker']} {_g(mc[0],'days_to_cover')}d" if mc else "—"
    top_rise = f"{ris[0]['ticker']} {_chg(ris[0])}" if ris else "—"
    return (f"- **{run_date} (settlement {settle}):** Auto-refresh via `/short-interest-intel` "
            f"({len(rows)} names). Most-shorted {top_short}; most-crowded {top_dtc}; "
            f"biggest riser {top_rise}.")


def review_flags(text, ms, mc):
    """Surface (not apply) judgment that may need a human look: CHALLENGE names now in the
    tables with no Intel-prose entry, and prose names that have dropped out of the tables."""
    intel = text.split("## Intel", 1)[1].split("## Watch-list", 1)[0] if "## Intel" in text else ""
    in_tables = {r["ticker"] for grp in (ms, mc) for r in grp}
    flags = []
    for tk in sorted(t for t in in_tables if STANCE.get(t, ("", ""))[0] == "challenge"):
        if not re.search(rf"\b{re.escape(tk)}\b", intel):
            flags.append(f"CHALLENGE name **{tk}** is in the tables but has no Intel-prose entry — consider adding one.")
    for tk in sorted(STANCE):
        if STANCE[tk][0] in ("confirm", "challenge") and re.search(rf"\*\*{re.escape(tk)}\b", intel) and tk not in in_tables:
            flags.append(f"**{tk}** has an Intel entry but dropped below all thresholds this settlement — consider pruning/marking.")
    return flags


# ── the bounded canon edit ───────────────────────────────────────────────────
def update_tracker(root, force=False, dry_run=False):
    rows, settle = load_snapshot(root)
    if not rows:
        print("✗ no snapshot CSV in raw/data/short-interest/ — run /short-interest-snapshot first")
        return 1
    page = root / "wiki" / "trackers" / "short-interest.md"
    if not page.exists():
        print(f"✗ tracker not found: {page}")
        return 1
    text = page.read_text()
    if START not in text or END not in text:
        print(f"✗ fence markers ({START} … {END}) not found in the tracker — insert them once first.")
        return 1

    m = re.search(r"<!-- SETTLEMENT: (\d{4}-\d{2}-\d{2}) -->", text)
    current = m.group(1) if m else None
    if current == settle and not force:
        print(f"✓ no new settlement (page already at {settle}). Nothing to update.")
        return 0

    run_date = datetime.date.today().isoformat()
    block = render_md_block(rows, settle)
    new = re.sub(re.escape(START) + r".*?" + re.escape(END),
                 START + "\n" + block + "\n" + END, text, flags=re.S)
    new = re.sub(r"^last_updated:.*$", f"last_updated: {run_date}", new, count=1, flags=re.M)
    new = new.replace("## Change log\n",
                      "## Change log\n\n" + render_changelog_line(rows, settle, run_date) + "\n", 1)

    ms, mc, _, _ = rankings(rows)
    if dry_run:
        diff = difflib.unified_diff(text.splitlines(True), new.splitlines(True),
                                    fromfile="short-interest.md (current)", tofile="short-interest.md (refreshed)")
        sys.stdout.writelines(diff)
        print(f"\n[dry-run] would refresh {current or 'none'} → {settle}; nothing written.")
        return 0

    page.write_text(new)
    # regenerate the HTML (one-directional: this engine subprocesses the renderer)
    html = Path(__file__).resolve().parent / "short_interest_html.py"
    subprocess.run([sys.executable, str(html), "--vault-root", str(root)], check=False)

    print(f"✓ refreshed wiki/trackers/short-interest.md: {current or 'none'} → {settle} "
          f"({len(rows)} names) + regenerated HTML + appended change log.")
    flags = review_flags(text, ms, mc)
    if flags:
        print("\nFor your review (judgment layer — NOT auto-edited):")
        for f in flags:
            print("  • " + f)
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vault-root", default=".")
    ap.add_argument("--render-md", action="store_true", help="print the fenced data block, write nothing")
    ap.add_argument("--update-tracker", action="store_true", help="bounded refresh of the tracker + HTML")
    ap.add_argument("--force", action="store_true", help="re-render even on the same settlement (testing)")
    ap.add_argument("--dry-run", action="store_true", help="with --update-tracker: print a unified diff only")
    args = ap.parse_args()
    root = Path(args.vault_root)

    if args.render_md:
        rows, settle = load_snapshot(root)
        if not rows:
            print("✗ no snapshot CSV found"); return 1
        print(render_md_block(rows, settle))
        return 0
    if args.update_tracker:
        return update_tracker(root, force=args.force, dry_run=args.dry_run)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
