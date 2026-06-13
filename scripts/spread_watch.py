#!/usr/bin/env python3
"""spread_watch.py — pull the credit-spread baseline for the AI Credit Spread Watch tracker.

Fetches the two FRED control series (free CSV endpoint, no API key):
  BAMLH0A0HYM2  — US High Yield OAS (risky borrowers in general)
  BAMLC0A0CM    — US Investment Grade OAS (safe borrowers in general)

Prints latest level, 1-month and 3-month change, then a differential worksheet
with paste-in slots for the manual dials (CRWV 2031 unsecured yield from FINRA
TRACE; ORCL/MSFT matched-maturity yields). The AI-specific signal is the gap
vs these controls — see wiki/trackers/AI-credit-spread-watch.md for reading rules.

Usage:
  python3 scripts/spread_watch.py
  python3 scripts/spread_watch.py --crwv 11.5            # paste CRWV unsecured yield (%)
  python3 scripts/spread_watch.py --orcl 5.6 --msft 4.9  # paste matched-maturity yields (%)
"""
import argparse
import csv
import io
import subprocess
import sys
import urllib.request
from datetime import date, timedelta

SERIES = {
    "BAMLH0A0HYM2": "High-Yield OAS (control: risky borrowers)",
    "BAMLC0A0CM": "Investment-Grade OAS (control: safe borrowers)",
}
FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd={start}"


def fetch_series(sid: str):
    start = (date.today() - timedelta(days=200)).isoformat()
    url = FRED_CSV.format(sid=sid, start=start)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "stocks-wiki spread-watch"})
        with urllib.request.urlopen(req, timeout=15) as r:
            text = r.read().decode("utf-8", errors="ignore")
    except Exception:
        # some sandboxed/proxied environments block urllib but allow curl
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
            continue  # '.' = missing observation
    return rows


def nearest(rows, target_iso):
    """Last observation on/before target date."""
    best = None
    for d, v in rows:
        if d <= target_iso:
            best = (d, v)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--crwv", type=float, help="CRWV 9.75%% 2031 unsecured yield, %% (from FINRA TRACE)")
    ap.add_argument("--orcl", type=float, help="ORCL bond yield, %% (matched maturity)")
    ap.add_argument("--msft", type=float, help="MSFT bond yield, %% (same maturity as --orcl)")
    args = ap.parse_args()

    print("=" * 72)
    print("AI CREDIT SPREAD WATCH — Layer-1 controls (FRED, daily)")
    print("=" * 72)

    latest = {}
    for sid, label in SERIES.items():
        try:
            rows = fetch_series(sid)
        except Exception as e:
            print(f"  {sid}: FETCH FAILED ({e}) — check connectivity")
            continue
        if not rows:
            print(f"  {sid}: no data returned")
            continue
        d_now, v_now = rows[-1]
        m1 = nearest(rows, (date.fromisoformat(d_now) - timedelta(days=30)).isoformat())
        m3 = nearest(rows, (date.fromisoformat(d_now) - timedelta(days=91)).isoformat())
        latest[sid] = v_now
        chg1 = f"{(v_now - m1[1]):+.2f}pp/1m" if m1 else "n/a"
        chg3 = f"{(v_now - m3[1]):+.2f}pp/3m" if m3 else "n/a"
        print(f"  {label}")
        print(f"    {sid}: {v_now:.2f}pp  (as of {d_now};  {chg1};  {chg3})")

    hy = latest.get("BAMLH0A0HYM2")
    ig = latest.get("BAMLC0A0CM")

    print("-" * 72)
    print("DIFFERENTIAL WORKSHEET (the AI-specific signal = gap vs controls)")
    print("-" * 72)

    if args.crwv is not None and hy is not None:
        # OAS is a spread; a bond *yield* ~= risk-free + spread. Approximate the
        # CRWV spread-vs-index by comparing its yield premium over the HY index
        # level change over time — record the raw gap and watch its TREND.
        gap = args.crwv - hy
        print(f"  Dial 2 — CRWV unsecured yield {args.crwv:.2f}% vs HY OAS {hy:.2f}pp")
        print(f"           raw gap {gap:+.2f}pp  → log this number; the TREND is the signal")
    else:
        print("  Dial 2 — CRWV 2031 yield: paste with --crwv (read from FINRA TRACE:")
        print("           finra-markets.morningstar.com → bond search → CoreWeave)")

    if args.orcl is not None and args.msft is not None:
        print(f"  Dial 4 — ORCL {args.orcl:.2f}% vs MSFT {args.msft:.2f}%  → AI-leverage premium "
              f"{(args.orcl - args.msft):+.2f}pp")
    else:
        print("  Dial 4 — ORCL-vs-MSFT gap: paste with --orcl / --msft (matched maturities)")

    if ig is not None and hy is not None:
        print(f"  Context — HY-over-IG quality spread: {(hy - ig):+.2f}pp")

    print("-" * 72)
    print("Reading rule: AI dials widening while controls stay calm, confirmed on a")
    print("second dial = the signal. Update wiki/trackers/AI-credit-spread-watch.md")
    print("readings table (with as-of dates) after each run.")


if __name__ == "__main__":
    sys.exit(main())
