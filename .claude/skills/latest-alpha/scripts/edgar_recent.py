#!/usr/bin/env python3
"""
edgar_recent.py — pull a company's recent SEC filings for the /latest-alpha skill.

Maps TICKER -> CIK via SEC's company_tickers.json, then reads the EDGAR
submissions feed and prints recent material-event + financing + periodic
filings (newest first) with dates and document URLs.

This is the Tier-1 ANCHOR for /latest-alpha: 8-K / 424B5 / 6-K are primary AND
timely, so they fill the gap between the lagging 10-Q / 10-K cycles. Discovery
only — nothing here is written to the vault; the skill turns these into
"verify at primary" leads. Periodic reports (10-Q/10-K/20-F/40-F) that land in
the window are flagged separately as REAL-INGEST candidates, not latest-alpha.

Usage:
    python3 edgar_recent.py AAOI
    python3 edgar_recent.py AAOI --since 2026-05-10     # anchor to page last_updated
    python3 edgar_recent.py AAOI --days 180
    python3 edgar_recent.py AAOI --all                  # every form, no filter
    python3 edgar_recent.py AAOI --forms 8-K,4,424B5    # custom form set

SEC requires a descriptive User-Agent with contact info; override via SEC_UA env var.
"""
import argparse
import datetime
import json
import os
import sys
import urllib.request

UA = os.environ.get("SEC_UA", "stocks-wiki latest-alpha research (victorheweinan725@yahoo.com.sg)")
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"

# Default form set: material events + financings + periodic reports.
DEFAULT_FORMS = {
    "8-K", "8-K/A",
    "6-K", "6-K/A",
    "424B5", "424B3", "424B4",
    "S-1", "S-1/A", "S-3", "S-3/A", "S-3ASR",
    "FWP",
    "SC 13D", "SC 13D/A", "SC 13G", "SC 13G/A",
    "10-Q", "10-Q/A", "10-K", "10-K/A",
    "20-F", "20-F/A", "40-F", "40-F/A",
}
PERIODIC = {"10-Q", "10-K", "20-F", "40-F", "10-Q/A", "10-K/A", "20-F/A", "40-F/A"}


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def find_cik(ticker):
    ticker = ticker.upper()
    m = _get(TICKERS_URL)
    for row in m.values():
        if row.get("ticker", "").upper() == ticker:
            return int(row["cik_str"]), row.get("title", "")
    return None, None


def main():
    ap = argparse.ArgumentParser(description="Recent SEC filings for a ticker (latest-alpha Tier-1 anchor).")
    ap.add_argument("ticker")
    ap.add_argument("--since", help="YYYY-MM-DD; only filings on/after this date (anchor to page last_updated)")
    ap.add_argument("--days", type=int, default=120, help="lookback window if --since omitted (default 120)")
    ap.add_argument("--forms", help="comma-separated form override (e.g. 8-K,4,424B5)")
    ap.add_argument("--all", action="store_true", help="show every form, no filter")
    args = ap.parse_args()

    if args.since:
        try:
            since = datetime.date.fromisoformat(args.since)
        except ValueError:
            print(f"bad --since date (want YYYY-MM-DD): {args.since}", file=sys.stderr)
            sys.exit(2)
    else:
        since = datetime.date.today() - datetime.timedelta(days=args.days)

    forms = None
    if args.forms:
        forms = {f.strip() for f in args.forms.split(",") if f.strip()}
    elif not args.all:
        forms = DEFAULT_FORMS

    try:
        cik, name = find_cik(args.ticker)
    except Exception as e:
        print(f"error fetching SEC ticker map: {e}", file=sys.stderr)
        sys.exit(1)
    if cik is None:
        print(f"ticker not found in SEC map: {args.ticker.upper()}", file=sys.stderr)
        print("  (foreign / non-SEC filer? then the SEC anchor is N/A for this name — "
              "use IR + news only, like the A-share / EDINET vault cohort.)", file=sys.stderr)
        sys.exit(3)

    try:
        subs = _get(SUBS_URL.format(cik=cik))
    except Exception as e:
        print(f"error fetching submissions for CIK {cik}: {e}", file=sys.stderr)
        sys.exit(1)

    rec = subs.get("filings", {}).get("recent", {})
    forms_l = rec.get("form", [])
    dates = rec.get("filingDate", [])
    accs = rec.get("accessionNumber", [])
    docs = rec.get("primaryDocument", [])
    descs = rec.get("primaryDocDescription", [])
    rpts = rec.get("reportDate", [])

    rows = []
    for i in range(len(forms_l)):
        form = forms_l[i]
        fdate = dates[i] if i < len(dates) else ""
        try:
            d = datetime.date.fromisoformat(fdate)
        except ValueError:
            continue
        if d < since:
            continue
        if forms is not None and form not in forms:
            continue
        acc = accs[i] if i < len(accs) else ""
        doc = docs[i] if i < len(docs) else ""
        desc = descs[i] if i < len(descs) else ""
        rpt = rpts[i] if i < len(rpts) else ""
        acc_nodash = acc.replace("-", "")
        if doc:
            url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc_nodash}/{doc}"
        else:
            url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type={form}"
        rows.append((fdate, form, desc, rpt, url))

    rows.sort(key=lambda r: r[0], reverse=True)

    print(f"# {name} ({args.ticker.upper()}) — CIK {cik}")
    print(f"# filings on/after {since.isoformat()}  ({len(rows)} matched)")
    print()
    if not rows:
        print("(no matching filings in window)")
        return

    periodic_hits = [r for r in rows if r[1] in PERIODIC]
    if periodic_hits:
        print("## PERIODIC REPORTS in window — REAL-INGEST candidates (not just latest-alpha):")
        for fdate, form, desc, rpt, url in periodic_hits:
            print(f"  {fdate}  {form:8}  period={rpt or '?'}")
            print(f"            {url}")
        print()

    print("## Material-event / financing filings (Tier-1, timely):")
    any_me = False
    for fdate, form, desc, rpt, url in rows:
        if form in PERIODIC:
            continue
        any_me = True
        print(f"  {fdate}  {form:8}  {desc or ''}".rstrip())
        print(f"            {url}")
    if not any_me:
        print("  (none — only periodic reports in window)")


if __name__ == "__main__":
    main()
