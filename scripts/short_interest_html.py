#!/usr/bin/env python3
"""
short_interest_html.py — render a short-interest snapshot CSV into a styled, self-contained
HTML dashboard (the visual companion to wiki/trackers/short-interest.md).

Reads the data deterministically from raw/data/short-interest/short-interest_<date>.csv and
applies the tracker's reading rule (most-shorted / most-crowded / movers, thresholds). The
confirm/challenge stance + the rankings + the data helpers are imported from
short_interest_intel.py (the single source of truth), so this dashboard and the .md tracker
can never drift.

Tier-4 sentiment view — positioning, not fact; describe-don't-recommend. Output is a derived
artifact, not canon.

Usage:
    python scripts/short_interest_html.py                  # latest CSV in raw/data/short-interest/
    python scripts/short_interest_html.py --date 2026-05-29
    python scripts/short_interest_html.py --out wiki/trackers/short-interest.html
"""

import argparse
import csv
import sys
from pathlib import Path

# Shared core — single source of truth for the stance map, standout cards, and data helpers
# (so the .md tracker and this .html dashboard can never drift). Lives in short_interest_intel.py.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from short_interest_intel import (  # noqa: E402
    STANCE, STANDOUTS, fnum, hshares, numf, find_csv, rankings,
)

CSS = """
:root { --bg:#0f1115; --card:#171a21; --line:#262b36; --txt:#e6e9ef; --mut:#9aa3b2;
        --confirm:#f59e0b; --challenge:#818cf8; --neutral:#6b7280; --up:#ef4444; --down:#22c55e; }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--txt);
       font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
.wrap { max-width:1080px; margin:0 auto; padding:32px 24px 64px; }
h1 { font-size:26px; margin:0 0 4px; }
h2 { font-size:18px; margin:34px 0 12px; padding-bottom:6px; border-bottom:1px solid var(--line); }
.sub { color:var(--mut); margin:0 0 8px; }
.tier { display:inline-block; font-size:12px; color:var(--mut); border:1px solid var(--line);
        border-radius:999px; padding:2px 10px; margin-top:8px; }
.cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(195px,1fr)); gap:12px; margin:18px 0 6px; }
.card { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:14px 16px; }
.card .tk { font-size:20px; font-weight:700; }
.card .note { color:var(--mut); font-size:13px; margin-top:4px; }
table { width:100%; border-collapse:collapse; background:var(--card); border:1px solid var(--line);
        border-radius:12px; overflow:hidden; font-size:14px; }
th,td { padding:9px 12px; text-align:right; border-bottom:1px solid var(--line); white-space:nowrap; }
th:first-child,td:first-child { text-align:left; }
th:last-child,td:last-child { text-align:left; white-space:normal; }
th { color:var(--mut); font-weight:600; font-size:12px; text-transform:uppercase; letter-spacing:.03em; }
tr:last-child td { border-bottom:none; }
.tk { font-weight:700; }
.badge { display:inline-block; font-size:11px; font-weight:700; border-radius:6px; padding:2px 8px; }
.confirm   { background:rgba(245,158,11,.16); color:var(--confirm); }
.challenge { background:rgba(129,140,248,.16); color:var(--challenge); }
.neutral   { background:rgba(107,114,128,.16); color:var(--mut); }
.dot { font-weight:700; }
.note { color:var(--mut); font-size:13px; margin:8px 0 0; }
.foot { color:var(--mut); font-size:12px; margin-top:40px; border-top:1px solid var(--line); padding-top:14px; }
.intel { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:4px 18px; }
.intel li { margin:10px 0; }
.intel .lead { color:var(--txt); font-weight:700; }
a { color:#7dd3fc; }
"""


def short_bg(p):
    if p is None:
        return ""
    if p >= 20: return "background:rgba(239,68,68,.30)"
    if p >= 12: return "background:rgba(239,68,68,.18)"
    if p >= 8:  return "background:rgba(245,158,11,.16)"
    return ""


def dtc_cell(d):
    if d is None:
        return "—"
    style = "color:var(--up);font-weight:700" if d >= 5 else ("color:var(--confirm)" if d >= 4 else "")
    return f'<span style="{style}">{d:g}</span>'


def chg_cell(c):
    if c is None:
        return "—"
    col = "var(--up)" if c > 0 else "var(--down)" if c < 0 else "var(--mut)"
    sign = "+" if c > 0 else ""
    return f'<span style="color:{col}">{sign}{c:g}%</span>'


def badge(tk):
    stance, _ = STANCE.get(tk, ("neutral", ""))
    label = {"confirm": "CONFIRM", "challenge": "CHALLENGE", "neutral": "—"}[stance]
    return f'<span class="badge {stance}">{label}</span>'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="settlement date YYYY-MM-DD (default: latest CSV)")
    ap.add_argument("--vault-root", default=".")
    ap.add_argument("--out", help="output path (default: wiki/trackers/short-interest.html)")
    args = ap.parse_args()

    root = Path(args.vault_root)
    csv_path = find_csv(root, args.date)
    if not csv_path:
        print("✗ no snapshot CSV found in raw/data/short-interest/ — run /short-interest-snapshot first")
        return 1
    rows = list(csv.DictReader(csv_path.open()))
    settle = rows[0]["settlement_date"] if rows else "?"

    most_shorted, most_crowded, risers, fallers = rankings(rows)

    H = []
    H.append("<!doctype html><html lang='en'><head><meta charset='utf-8'>")
    H.append("<meta name='viewport' content='width=device-width,initial-scale=1'>")
    H.append(f"<title>Short Interest Watch — {settle}</title><style>{CSS}</style></head><body><div class='wrap'>")
    H.append("<h1>Short Interest Watch</h1>")
    H.append(f"<p class='sub'>What the crowd is betting against in the vault &middot; FINRA settlement <b>{settle}</b> &middot; {len(rows)} names</p>")
    H.append("<span class='tier'>Tier-4 sentiment &middot; positioning, not fact &middot; describe-don't-recommend</span>")

    # standout cards
    by_tk = {r["ticker"]: r for r in rows}
    H.append("<div class='cards'>")
    for tk, note in STANDOUTS:
        r = by_tk.get(tk, {})
        p = fnum(r, "pct_outstanding")
        ss = hshares(r.get("shares_short"))
        metric = f"{p:g}% out" if p is not None else (f"+{fnum(r,'change_pct'):g}% chg" if fnum(r, "change_pct") else "")
        sub = f"{ss} short &middot; {metric}" if metric else f"{ss} short"
        H.append(f"<div class='card'><div class='tk'>{tk} <span style='font-size:13px;color:var(--mut)'>{sub}</span></div>"
                 f"<div class='note'>{note}</div></div>")
    H.append("</div>")
    H.append("<p class='note'>The signal is the outliers and movers below — not the levels on the low-short mega-caps "
             "(NVDA 1.2%, MSFT 1.2%, GOOGL 0.7% = noise). <b style='color:var(--confirm)'>CONFIRM</b> = crowd agrees with a "
             "vault caution. <b style='color:var(--challenge)'>CHALLENGE</b> = crowd shorts a name the vault is bullish on "
             "(inverse divergence &rarr; run /bear-case).</p>")

    # most shorted
    H.append("<h2>Most shorted — short interest as % of shares outstanding (&ge;8%)</h2>")
    H.append("<table><tr><th>Ticker</th><th>Short interest</th><th>Short %out</th><th>Days-to-cover</th><th>&Delta; vs prior</th><th>Vault read</th><th>Thesis</th></tr>")
    for r in most_shorted:
        tk = r["ticker"]; p = fnum(r, "pct_outstanding")
        thesis = STANCE.get(tk, ("neutral", ""))[1]
        H.append(f"<tr><td class='tk'>{tk}</td>"
                 f"<td>{hshares(r.get('shares_short'))}</td>"
                 f"<td style='{short_bg(p)}'>{p:g}%</td>"
                 f"<td>{dtc_cell(fnum(r,'days_to_cover'))}</td>"
                 f"<td>{chg_cell(fnum(r,'change_pct'))}</td>"
                 f"<td>{badge(tk)}</td><td>{thesis}</td></tr>")
    H.append("</table>")

    # most crowded
    H.append("<h2>Most crowded — days-to-cover (&ge;4)</h2>")
    H.append("<table><tr><th>Ticker</th><th>Days-to-cover</th><th>Short interest</th><th>Short %out</th><th>&Delta; vs prior</th><th>Vault read</th></tr>")
    for r in most_crowded:
        tk = r["ticker"]; p = fnum(r, "pct_outstanding")
        H.append(f"<tr><td class='tk'>{tk}</td><td>{dtc_cell(fnum(r,'days_to_cover'))}</td>"
                 f"<td>{hshares(r.get('shares_short'))}</td>"
                 f"<td style='{short_bg(p)}'>{p:g}%</td><td>{chg_cell(fnum(r,'change_pct'))}</td><td>{badge(tk)}</td></tr>")
    H.append("</table>")

    # movers
    H.append("<h2>Movers — change vs the prior settlement</h2>")
    H.append("<div class='cards'><div class='card'><div class='note' style='margin:0 0 6px'>"
             "<b style='color:var(--up)'>Skepticism building</b> (rising short)</div>")
    H.append(" &middot; ".join(f"<b>{r['ticker']}</b> {chg_cell(fnum(r,'change_pct'))}" for r in risers) or "—")
    H.append("</div><div class='card'><div class='note' style='margin:0 0 6px'>"
             "<b style='color:var(--down)'>Bears covering</b> (falling short)</div>")
    H.append(" &middot; ".join(f"<b>{r['ticker']}</b> {chg_cell(fnum(r,'change_pct'))}" for r in fallers) or "—")
    H.append("</div></div>")

    # intel lists from the stance map
    conf = [tk for tk in STANCE if STANCE[tk][0] == "confirm" and tk in by_tk]
    chal = [tk for tk in STANCE if STANCE[tk][0] == "challenge" and tk in by_tk]
    H.append("<h2>Where the crowd agrees vs. disagrees with the vault</h2><div class='intel'><ul>")
    H.append("<li><span class='lead' style='color:var(--confirm)'>Crowd agrees (confirm):</span> "
             + ", ".join(conf) + " — heavy short on names the vault is already cautious on.</li>")
    H.append("<li><span class='lead' style='color:var(--challenge)'>Crowd disagrees (challenge):</span> "
             + ", ".join(chal) + " — heavy short on names the vault is bullish on; stress-test each with /bear-case "
             "(catalyst + falsifier in the .md tracker).</li>")
    H.append("</ul></div>")

    H.append("<p class='foot'>Generated from <code>raw/data/short-interest/short-interest_"
             f"{settle}.csv</code> (FINRA + SEC) by <code>scripts/short_interest_html.py</code>. "
             "Companion to <code>wiki/trackers/short-interest.md</code>. "
             "Tier-4 sentiment data — a heavy short is a question to investigate, never a trade signal.</p>")
    H.append("</div></body></html>")

    out = Path(args.out) if args.out else (root / "wiki" / "trackers" / "short-interest.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(H))
    print(f"✓ wrote {out}  (settlement {settle}, {len(rows)} names)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
