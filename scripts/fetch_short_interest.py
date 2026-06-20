#!/usr/bin/env python3
"""
fetch_short_interest.py — snapshot FINRA short interest for the vault's US-listed names.

Pulls the twice-monthly FINRA Consolidated Short Interest (official, anonymous, all US
exchanges + OTC) for every US-eligible vault ticker, joins SEC shares-outstanding to get
short interest as a % of shares OUTSTANDING (not float — true float isn't reliably free),
and writes one CSV per settlement date to raw/data/short-interest/.

Discovery-only: writes EXACTLY one CSV under raw/data/short-interest/. It never touches any
wiki/ page, the anchors, index.md, log.md, or git. The CSV is Tier-4 sentiment data
(positioning, not fact). The /short-interest-snapshot skill is the front door.

Data sources (no API key needed):
- FINRA  api.finra.org/data/group/otcMarket/name/consolidatedShortInterest  (POST, filtered)
- SEC    data.sec.gov/api/xbrl/companyconcept/.../EntityCommonStockSharesOutstanding.json

Usage:
    python scripts/fetch_short_interest.py                 # latest settlement, all vault names
    python scripts/fetch_short_interest.py --date 2026-05-29
    python scripts/fetch_short_interest.py --dry-run       # fetch + summarize, write nothing
    python scripts/fetch_short_interest.py --only NVDA,ORCL,MP   # a subset (testing)

Requires: requests (pip install requests)
"""

import argparse
import csv
import sys
import time
from pathlib import Path

import requests

# Reuse sibling-script logic (both live in scripts/, so add this dir to the path defensively).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from parse_short_interest import vault_companies, ADR_ALLOWLIST  # noqa: E402  (vault ticker classifier)
from fetch_filings import COMPANIES  # noqa: E402  (ticker -> CIK)

# A descriptive User-Agent satisfies both SEC (wants contact info) and FINRA.
UA = "stocks-wiki short-interest research (victorhwn725@gmail.com)"

FINRA_URL = "https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest"
SEC_CONCEPT_URL = "https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/{concept}.json"
# Tried in order; most single-class issuers tag the first, a few (e.g. GOOGL/AMZN) only the second.
SEC_CONCEPTS = ["dei/EntityCommonStockSharesOutstanding", "us-gaap/CommonStockSharesOutstanding"]

# Output schema — keep identical across every snapshot CSV (see raw/data/short-interest/README.md).
CANONICAL = [
    "settlement_date", "ticker", "company", "market_class", "shares_short",
    "prev_shares_short", "change_shares", "change_pct", "pct_outstanding",
    "shares_outstanding", "avg_daily_volume", "days_to_cover", "in_vault",
]


# ── FINRA ────────────────────────────────────────────────────────────────────
def _finra_post(session, filters, limit=10, offset=0):
    """POST the consolidated-short-interest dataset with EQUAL compareFilters. Returns
    (rows, total) — rows is the JSON array of records; total is the Record-Total header
    (the full match count, used to page to the newest record). ([], 0) on no-data/error."""
    body = {"limit": limit, "offset": offset, "compareFilters": filters}
    try:
        r = session.post(FINRA_URL, json=body, timeout=30,
                         headers={"Content-Type": "application/json",
                                  "Accept": "application/json", "User-Agent": UA})
        if r.status_code != 200:
            return [], 0
        data = r.json()
        rows = data if isinstance(data, list) else []
        return rows, int(r.headers.get("Record-Total", 0) or 0)
    except Exception:
        return [], 0


def finra_latest_settlement(session):
    """Latest settlement date in the dataset. FINRA returns records oldest-first and won't
    sort descending without the partition key, so we read NVDA's Record-Total (always present)
    and page to the last few records, taking the max settlementDate."""
    nvda = [{"compareType": "EQUAL", "fieldName": "symbolCode", "fieldValue": "NVDA"}]
    _, total = _finra_post(session, nvda, limit=1)
    if total:
        rows, _ = _finra_post(session, nvda, limit=5, offset=max(0, total - 5))
    else:
        rows, _ = _finra_post(session, nvda, limit=50)  # fallback if no header
    dates = [r.get("settlementDate") for r in rows if r.get("settlementDate")]
    return max(dates) if dates else None


def finra_row(session, settlement_date, ticker):
    """The single short-interest record for (ticker, settlement_date), or None."""
    rows, _ = _finra_post(session, [
        {"compareType": "EQUAL", "fieldName": "settlementDate", "fieldValue": settlement_date},
        {"compareType": "EQUAL", "fieldName": "symbolCode", "fieldValue": ticker},
    ], limit=5)
    return rows[0] if rows else None


# ── SEC ──────────────────────────────────────────────────────────────────────
def sec_shares_outstanding(session, cik):
    """Latest reported common shares outstanding, for the % denominator. Tries the dei concept
    then the us-gaap fallback. Sums distinct values at the latest period-end (so dual-class
    totals add up; amendments dedupe). Approximate for multi-class issuers — the all-class total
    is paired with FINRA's single-class short interest — and None if neither concept is tagged."""
    if not cik:
        return None
    for concept in SEC_CONCEPTS:
        try:
            r = session.get(SEC_CONCEPT_URL.format(cik=str(cik).zfill(10), concept=concept),
                           timeout=30, headers={"User-Agent": UA, "Accept": "application/json"})
            if r.status_code != 200:
                continue
            facts = r.json().get("units", {}).get("shares", [])
            if not facts:
                continue
            latest_end = max(f["end"] for f in facts if f.get("end"))
            vals = {f["val"] for f in facts if f.get("end") == latest_end and isinstance(f.get("val"), int)}
            if vals:
                return sum(vals)
        except Exception:
            continue
    return None


def _to_int(v):
    try:
        return int(str(v).replace(",", "").strip())
    except (ValueError, AttributeError):
        return None


# ── main ─────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="FINRA settlement date YYYY-MM-DD (default: auto-detect latest)")
    ap.add_argument("--vault-root", default=".", help="vault root (default: cwd)")
    ap.add_argument("--out", help="output path (default: raw/data/short-interest/short-interest_<date>.csv)")
    ap.add_argument("--only", help="comma-separated subset of tickers (testing)")
    ap.add_argument("--dry-run", action="store_true", help="fetch + summarize, write nothing")
    args = ap.parse_args()

    root = Path(args.vault_root)
    session = requests.Session()

    # 1) settlement date
    settle = args.date or finra_latest_settlement(session)
    if not settle:
        print("✗ could not determine a FINRA settlement date (network?). Pass --date YYYY-MM-DD.")
        return 1
    print(f"→ FINRA settlement date: {settle}")

    # 2) US-eligible vault tickers
    coverable = sorted(t for t, ok in vault_companies(root).items() if ok)
    if args.only:
        want = {t.strip().upper() for t in args.only.split(",") if t.strip()}
        coverable = [t for t in coverable if t in want]
    print(f"→ {len(coverable)} US-eligible vault tickers to pull")

    # 3) per ticker: FINRA short interest + SEC shares outstanding → % of outstanding
    out_rows, missing = [], []
    for i, tk in enumerate(coverable, 1):
        fr = finra_row(session, settle, tk)
        if not fr:
            missing.append(tk)
            rec = {k: "" for k in CANONICAL}
            rec.update(settlement_date=settle, ticker=tk, in_vault="true")
            out_rows.append(rec)
            print(f"  [{i}/{len(coverable)}] {tk:<7} — not in FINRA snapshot")
            continue
        shares_short = _to_int(fr.get("currentShortPositionQuantity"))
        so = sec_shares_outstanding(session, COMPANIES.get(tk, {}).get("cik"))
        pct = round(shares_short / so * 100, 2) if (shares_short and so) else ""
        out_rows.append({
            "settlement_date": settle,
            "ticker": tk,
            "company": fr.get("issueName", ""),
            "market_class": fr.get("marketClassCode", ""),
            "shares_short": fr.get("currentShortPositionQuantity", ""),
            "prev_shares_short": fr.get("previousShortPositionQuantity", ""),
            "change_shares": fr.get("changePreviousNumber", ""),
            "change_pct": fr.get("changePercent", ""),
            "pct_outstanding": pct,
            "shares_outstanding": so if so else "",
            "avg_daily_volume": fr.get("averageDailyVolumeQuantity", ""),
            "days_to_cover": fr.get("daysToCoverQuantity", ""),
            "in_vault": "true",
        })
        dtc = fr.get("daysToCoverQuantity", "?")
        print(f"  [{i}/{len(coverable)}] {tk:<7} short={fr.get('currentShortPositionQuantity','?'):>14}  "
              f"dtc={dtc}  pct_out={pct}")
        time.sleep(0.15)  # polite pacing (SEC asks <=10 req/s)

    # 4) summary
    covered = [r for r in out_rows if r["shares_short"]]
    print(f"\n=== snapshot {settle}: {len(covered)}/{len(coverable)} names with data ===")
    if missing:
        print(f"not in FINRA snapshot ({len(missing)}): {missing}")

    def _num(r, k):
        try:
            return float(str(r.get(k, "")).replace(",", ""))
        except ValueError:
            return float("-inf")
    top_dtc = sorted(covered, key=lambda r: _num(r, "days_to_cover"), reverse=True)[:5]
    top_rise = sorted(covered, key=lambda r: _num(r, "change_pct"), reverse=True)[:5]
    print("most-crowded (days-to-cover): " + ", ".join(f"{r['ticker']} {r['days_to_cover']}" for r in top_dtc))
    print("biggest rising short interest (change% vs prior): "
          + ", ".join(f"{r['ticker']} {r['change_pct']}%" for r in top_rise))

    # 5) write
    if args.dry_run:
        print("\ndry-run: no file written")
        return 0
    out = Path(args.out) if args.out else (
        root / "raw" / "data" / "short-interest" / f"short-interest_{settle}.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CANONICAL)
        w.writeheader()
        w.writerows(out_rows)
    print(f"\n✓ wrote {out} ({len(out_rows)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
