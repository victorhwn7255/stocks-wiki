#!/usr/bin/env python3
"""spread_chart.py — visualize the AI-vs-ordinary borrower spread history.

Companion to wiki/trackers/AI-credit-spread-watch.md. Two panels:
  1. The ruler: FRED HY + IG option-adjusted spreads (daily) with the known
     CRWV bond observations overlaid as dated anchor points (pure-AI public
     debt only EXISTS since mid-2025 — episodic points, not a daily line).
  2. The private-credit proxy: BIZD (VanEck BDC ETF) daily price — the listed
     shadow of the $800B private-credit channel (the BIS itself used BDC moves).

Output: raw/research/charts/ai-credit-spread-history-<date>.png
Usage:  python3 scripts/spread_chart.py
"""
import csv
import io
import json
import subprocess
import sys
from datetime import date, datetime

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

START = "2025-01-01"
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd=" + START
YAHOO = "https://query1.finance.yahoo.com/v8/finance/chart/BIZD?range=18mo&interval=1d"

# Known pure-AI credit observations (yield %, date, label, source tag)
CRWV_POINTS = [
    ("2025-07-15", 9.75, "CRWV 2031 unsecured\nissued at 9.75% coupon", "8-K/10-K"),
    ("2026-02-15", 11.5, "CRWV 2031 ~11.5% yield\n(secondary report, unconfirmed)", "Tier 4"),
    ("2026-03-31", 5.9, "CRWV $8.5B SPV DDTL\n~5.9% fixed, rated A3", "8-K"),
]
EVENTS = [
    ("2026-01-07", "BIS Bulletin 120:\nAI loans = non-AI loans"),
    ("2026-02-23", "Software-credit scare\n(IGV worst day since '08)"),
    ("2026-06-11", "GS desk: concessions\n12-18mo away"),
]


def curl(url, browser_ua=False):
    cmd = ["curl", "-s", "--http1.1", "-m", "30"]
    if browser_ua:
        cmd += ["-A", "Mozilla/5.0"]  # Yahoo requires it; FRED rejects it
    return subprocess.run(cmd + [url], capture_output=True, text=True, check=True).stdout


def fred(sid):
    rows = []
    for rec in csv.reader(io.StringIO(curl(FRED.format(sid=sid)))):
        if len(rec) == 2 and rec[0] not in ("DATE", "observation_date"):
            try:
                rows.append((datetime.fromisoformat(rec[0]), float(rec[1])))
            except ValueError:
                pass
    return rows


def bizd():
    d = json.loads(curl(YAHOO, browser_ua=True))["chart"]["result"][0]
    out = []
    for ts, c in zip(d["timestamp"], d["indicators"]["quote"][0]["close"]):
        if c is not None:
            t = datetime.fromtimestamp(ts)
            if t >= datetime.fromisoformat(START):
                out.append((t, c))
    return out


def main():
    hy, ig, bz = fred("BAMLH0A0HYM2"), fred("BAMLC0A0CM"), bizd()
    if not hy or not ig:
        sys.exit("FRED fetch failed")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 9), sharex=True,
                                   gridspec_kw={"height_ratios": [3, 2]})
    fig.suptitle("AI borrowers vs ordinary borrowers — the spread history\n"
                 "(tracker: wiki/trackers/AI-credit-spread-watch.md)", fontsize=13)

    # Panel 1 — the ruler + AI anchor points
    ax1.plot(*zip(*hy), lw=1.6, color="#c0392b", label="High-Yield OAS (ordinary risky borrowers)")
    ax1.plot(*zip(*ig), lw=1.6, color="#2471a3", label="Investment-Grade OAS (ordinary safe borrowers)")
    ax1.set_ylabel("spread / yield, % points")
    hy_d = {d.date(): v for d, v in hy}

    for ds, y, label, tag in CRWV_POINTS:
        dt = datetime.fromisoformat(ds)
        ax1.scatter([dt], [y], s=70, zorder=5,
                    color="#7d3c98" if "SPV" not in label else "#1e8449",
                    marker="D")
        # nearest HY value for the raw gap annotation
        near = min(hy_d, key=lambda k: abs((k - dt.date()).days))
        gap = y - hy_d[near]
        ax1.annotate(f"{label}\nraw gap vs HY: {gap:+.1f}pp  [{tag}]",
                     xy=(dt, y), xytext=(8, 6), textcoords="offset points",
                     fontsize=7.5, color="#4a235a")
    ax1.set_ylim(0, 13)
    ax1.legend(loc="upper left", fontsize=9)
    ax1.set_title("The ruler stays flat and historically tight — while the only pure-AI bonds "
                  "price 7-9pp above it (and the A3 SPV far below the company's own unsecured)",
                  fontsize=9.5)

    # Panel 2 — private-credit proxy
    ax2.plot(*zip(*bz), lw=1.4, color="#1a5276", label="BIZD (listed BDC ETF — private-credit proxy)")
    ax2.set_ylabel("BIZD price, $")
    ax2.legend(loc="lower left", fontsize=9)
    ax2.set_title("The private-credit shadow: BDC selloff during the Feb-Apr software-credit scare "
                  "= the one live rehearsal (BIS QR: BDCs −10%, NAV discounts deepened)", fontsize=9.5)

    for ds, txt in EVENTS:
        dt = datetime.fromisoformat(ds)
        for ax in (ax1, ax2):
            ax.axvline(dt, color="gray", lw=0.8, ls="--", alpha=0.6)
        ax2.annotate(txt, xy=(dt, ax2.get_ylim()[0]), xytext=(4, 8),
                     textcoords="offset points", fontsize=7, color="dimgray")

    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.text(0.01, 0.005,
             "Sources: FRED (ICE BofA OAS, daily) · CRWV 8-K/10-K issue pricing + Tier-4 secondary report · "
             "Yahoo (BIZD). Pure-AI public debt exists only since mid-2025 — the AI side is anchor points, "
             "not a daily series. Discovery artifact, not canon.",
             fontsize=7, color="gray")

    import os
    os.makedirs("raw/research/charts", exist_ok=True)
    out = f"raw/research/charts/ai-credit-spread-history-{date.today().isoformat()}.png"
    fig.tight_layout(rect=[0, 0.02, 1, 0.97])
    fig.savefig(out, dpi=130)
    print(f"saved: {out}")


if __name__ == "__main__":
    main()
