#!/usr/bin/env python3
"""forward_pe_watch.py — compute the S&P 500 forward P/E dial for the Forward P/E Watch tracker.

Layer 1 (automatic): fetches the current S&P 500 index level from FRED `SP500`
(free CSV endpoint, no API key; curl fallback for sandboxed environments).

Layer 2 (manual): you paste the LSEG/I-B-E-S operating EPS estimates (CY2026,
CY2027, and NTM if you have it). The script NEVER invents EPS — if you don't
paste them it just prints the index level and asks for them.

It then prints the forward P/E for 2026 / 2027 / NTM, and — if you also paste the
prior reading (--prior-*) — the price-vs-earnings DECOMPOSITION of each P/E move
(the "is the multiple cheaper because earnings rose or because price fell?" read)
plus the EPS revision deltas. Stateless: prints to stdout, writes nothing.

The tracker page (wiki/trackers/forward-pe-watch.md) holds the dated series and
the reading discipline (single-source LSEG; operating basis; as-of dates).

Usage:
  python3 forward_pe_watch.py --eps2026 340.82 --eps2027 399.25
  python3 forward_pe_watch.py --eps2026 340.82 --eps2027 399.25 --epsntm 369 \\
        --prior-level 7365 --prior-eps2026 340.82 --prior-eps2027 399.25
  python3 forward_pe_watch.py --level 7400 --eps2026 341 --eps2027 401   # paste level if fetch fails
"""
import argparse
import csv
import io
import subprocess
import sys
import urllib.request
from datetime import date, timedelta

FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd={start}"
SP500 = "SP500"


def fetch_series(sid: str):
    """Fetch a FRED series as a list of (iso-date, float) — urllib, curl fallback."""
    start = (date.today() - timedelta(days=200)).isoformat()
    url = FRED_CSV.format(sid=sid, start=start)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "stocks-wiki forward-pe-watch"})
        with urllib.request.urlopen(req, timeout=15) as r:
            text = r.read().decode("utf-8", errors="ignore")
    except Exception:
        text = subprocess.run(
            ["curl", "-s", "-m", "30", url],
            capture_output=True, text=True, check=True,
        ).stdout
    rows = []
    for rec in csv.reader(io.StringIO(text)):
        if len(rec) != 2 or rec[0] in ("DATE", "observation_date"):
            continue
        try:
            rows.append((rec[0], float(rec[1])))
        except ValueError:
            continue  # '.' = missing observation (holiday/weekend)
    return rows


def ntm_weight(today=None):
    """Fraction weight on the CURRENT calendar year for an NTM (next-12-month)
    blend: w = (days left in this year) / 365. NTM EPS = w*CY + (1-w)*CYnext."""
    today = today or date.today()
    year_end = date(today.year, 12, 31)
    days_left = (year_end - today).days
    return max(0.0, min(1.0, days_left / 365.0))


def pe(level, eps):
    return level / eps if (level and eps) else None


def decompose(p_old, e_old, p_new, e_new):
    """Exact decomposition of the P/E change into a price effect and an earnings
    effect. price effect = (P_new - P_old)/E_old ; earnings effect = P_new*(1/E_new - 1/E_old).
    The two sum exactly to (P_new/E_new - P_old/E_old)."""
    pe_old = p_old / e_old
    pe_new = p_new / e_new
    price_eff = (p_new - p_old) / e_old
    earn_eff = p_new * (1.0 / e_new - 1.0 / e_old)
    return pe_old, pe_new, (pe_new - pe_old), price_eff, earn_eff


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", type=float, help="S&P 500 index level (override; else fetched from FRED)")
    ap.add_argument("--eps2026", type=float, help="LSEG CY2026 operating EPS estimate ($)")
    ap.add_argument("--eps2027", type=float, help="LSEG CY2027 operating EPS estimate ($)")
    ap.add_argument("--epsntm", type=float, help="LSEG NTM (next-12-mo) EPS ($); else blended from 2026/2027")
    ap.add_argument("--prior-level", type=float, help="prior reading: S&P level")
    ap.add_argument("--prior-eps2026", type=float, help="prior reading: CY2026 EPS")
    ap.add_argument("--prior-eps2027", type=float, help="prior reading: CY2027 EPS")
    ap.add_argument("--prior-epsntm", type=float, help="prior reading: NTM EPS")
    args = ap.parse_args()

    print("=" * 72)
    print("FORWARD P/E WATCH — S&P 500 (Layer-1 index level from FRED; EPS = LSEG, manual)")
    print("=" * 72)

    # --- Layer 1: index level ---
    level = args.level
    asof = "pasted"
    if level is None:
        try:
            rows = fetch_series(SP500)
            if rows:
                asof, level = rows[-1]
            else:
                print("  SP500: no data returned — paste with --level")
        except Exception as e:
            print(f"  SP500: FETCH FAILED ({e}) — paste with --level")
    if level is not None:
        print(f"  S&P 500 level: {level:,.2f}  (as of {asof})")

    # --- Layer 2: EPS (never invented) ---
    e26, e27 = args.eps2026, args.eps2027
    if e26 is None or e27 is None:
        print("-" * 72)
        print("  EPS estimates not pasted. Provide --eps2026 and --eps2027 (LSEG operating,")
        print("  from the weekly S&P 500 Earnings Dashboard). The script never invents EPS.")
        print("  NTM blend / decomposition need them. Re-run with the numbers.")
        return 0

    w = ntm_weight()
    entm = args.epsntm if args.epsntm is not None else (w * e26 + (1 - w) * e27)
    ntm_note = "pasted" if args.epsntm is not None else f"blended (w={w:.2f} on CY2026)"

    print("-" * 72)
    print("FORWARD P/E (level / estimated EPS)")
    print("-" * 72)
    if level is not None:
        print(f"  2026:  {level:,.0f} / {e26:.2f}  = {pe(level, e26):.1f}x")
        print(f"  2027:  {level:,.0f} / {e27:.2f}  = {pe(level, e27):.1f}x")
        print(f"  NTM:   {level:,.0f} / {entm:.2f}  = {pe(level, entm):.1f}x   ({ntm_note})")

    # --- Decomposition vs prior (price-vs-earnings) ---
    pl, p26, p27 = args.prior_level, args.prior_eps2026, args.prior_eps2027
    if level is not None and pl and p26 and p27:
        print("-" * 72)
        print("DECOMPOSITION vs prior reading  (ΔP/E = price effect + earnings effect)")
        print("-" * 72)
        print(f"  Price:     {pl:,.0f} -> {level:,.0f}   ({(level/pl - 1)*100:+.1f}%)")
        print(f"  2026 EPS:  {p26:.2f} -> {e26:.2f}   ({(e26/p26 - 1)*100:+.1f}%)")
        print(f"  2027 EPS:  {p27:.2f} -> {e27:.2f}   ({(e27/p27 - 1)*100:+.1f}%)")
        for label, eo, en in (("2026", p26, e26), ("2027", p27, e27)):
            pe_o, pe_n, d, pf, ef = decompose(pl, eo, level, en)
            print(f"  {label} P/E: {pe_o:.1f}x -> {pe_n:.1f}x  (Δ {d:+.2f})  "
                  f"= price {pf:+.2f} + earnings {ef:+.2f}")
        print("  Read: multiple compressing on RISING earnings (earnings effect <0) is the")
        print("  'cheaper for the right reason' case; compressing on FALLING price is not.")
    else:
        print("-" * 72)
        print("  For the price-vs-earnings decomposition, also pass --prior-level,")
        print("  --prior-eps2026, --prior-eps2027 (the last row on the tracker).")

    print("-" * 72)
    print("Discipline: one source (default LSEG) across the series; operating EPS (reads")
    print("lower P/E than trailing GAAP); every row carries its as-of date. Update")
    print("wiki/trackers/forward-pe-watch.md after each run. Describe, don't recommend.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
