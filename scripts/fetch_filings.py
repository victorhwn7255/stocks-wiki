#!/usr/bin/env python3
"""
fetch_filings.py — Download the most recent SEC filings for the stocks-wiki seed set.

Default behavior:
- Downloads each filing as .htm from SEC EDGAR directly into the output folder
- Skips any filing already present

Usage:
    python fetch_filings.py
    python fetch_filings.py --ticker NVDA --form 10-K
    python fetch_filings.py --output-dir ./raw/filings
    python fetch_filings.py --freshness    # vault freshness scan; orchestrated by check-recent-earnings skill

Requires: requests (pip install requests)
"""

import argparse
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests

# SEC requires a User-Agent identifying the requester.
# Replace with your own name and email.
USER_AGENT = "Victor victorhwn725@gmail.com"

# Seed set: ticker -> (CIK, primary form types to fetch)
# TSM files 20-F annually instead of 10-K (foreign private issuer).
COMPANIES = {
    "NVDA": {"cik": "0001045810", "forms": ["10-K", "10-Q"]},
    "TSM":  {"cik": "0001046179", "forms": ["20-F"]},
    "AEHR": {"cik": "0001040470", "forms": ["10-K", "10-Q"]},
    "ONTO": {"cik": "0000704532", "forms": ["10-K", "10-Q"]},
    "LITE": {"cik": "0001633978", "forms": ["10-K", "10-Q"]},
    "AAOI": {"cik": "0001158114", "forms": ["10-K", "10-Q"]},
    "COHU": {"cik": "0000021535", "forms": ["10-K", "10-Q"]},
    "COHR": {"cik": "0000820318", "forms": ["10-K", "10-Q"]},
    "MRVL": {"cik": "0001835632", "forms": ["10-K", "10-Q"]},
    "AVGO": {"cik": "0001730168", "forms": ["10-K", "10-Q"]},
    "AXTI": {"cik": "0001051627", "forms": ["10-K", "10-Q"]},
    "VECO": {"cik": "0000103145", "forms": ["10-K", "10-Q"]},
    "ALAB": {"cik": "0001736297", "forms": ["10-K", "10-Q"]},
    "CSCO": {"cik": "0000858877", "forms": ["10-K", "10-Q"]},
    "GLW":  {"cik": "0000024741", "forms": ["10-K", "10-Q"]},
    "FN":   {"cik": "0001408710", "forms": ["10-K", "10-Q"]},
    "VRT":  {"cik": "0001674101", "forms": ["10-K", "10-Q"]},
    "CRDO": {"cik": "0001807794", "forms": ["10-K", "10-Q"]},
    "ANET": {"cik": "0001596532", "forms": ["10-K", "10-Q"]},
    "VIAV": {"cik": "0000912093", "forms": ["10-K", "10-Q"]},
    "PLAB": {"cik": "0000810136", "forms": ["10-K", "10-Q"]},
    "FLEX": {"cik": "0000866374", "forms": ["10-K", "10-Q"]},
    "ETN":  {"cik": "0001551182", "forms": ["10-K", "10-Q"]},
    "GEV":  {"cik": "0001996810", "forms": ["10-K", "10-Q"]},
    "BE":   {"cik": "0001664703", "forms": ["10-K", "10-Q"]},
    "CEG":  {"cik": "0001868275", "forms": ["10-K", "10-Q"]},
    "CAT":  {"cik": "0000018230", "forms": ["10-K", "10-Q"]},
    "BWXT": {"cik": "0001486957", "forms": ["10-K", "10-Q"]},
    "LEU":  {"cik": "0001065059", "forms": ["10-K", "10-Q"]},
    "CCJ":  {"cik": "0001009001", "forms": ["40-F", "6-K"]},
    "ENS":  {"cik": "0001289308", "forms": ["10-K", "10-Q"]},
    "FCEL": {"cik": "0000886128", "forms": ["10-K", "10-Q"]},
    "FLNC": {"cik": "0001868941", "forms": ["10-K", "10-Q"]},
    "TSEM": {"cik": "0000928876", "forms": ["20-F"]},
    "NVT":  {"cik": "0001720635", "forms": ["10-K", "10-Q"]},
    "MOD":  {"cik": "0000067347", "forms": ["10-K", "10-Q"]},
    "NOK":  {"cik": "0000924613", "forms": ["20-F"]},
    "AAON": {"cik": "0000824142", "forms": ["10-K", "10-Q"]},
    "MKSI": {"cik": "0001049502", "forms": ["10-K", "10-Q"]},
    "ARM":  {"cik": "0001973239", "forms": ["20-F", "6-K"]},
    "AMD":  {"cik": "0000002488", "forms": ["10-K", "10-Q"]},
    "INTC": {"cik": "0000050863", "forms": ["10-K", "10-Q"]},
    "MU":   {"cik": "0000723125", "forms": ["10-K", "10-Q"]},
    "SNDK": {"cik": "0002023554", "forms": ["10-K", "10-Q"]},
    "MP":   {"cik": "0001801368", "forms": ["10-K", "10-Q"]},
    "NVTS": {"cik": "0001821769", "forms": ["10-K", "10-Q"]},
}

HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/json"}


def get_company_filings(cik: str) -> dict:
    """Fetch the filings index for a company from EDGAR."""
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()


def find_latest_filing(filings_json: dict, form_type: str) -> dict | None:
    """Return metadata for the most recent filing of a given form type."""
    recent = filings_json["filings"]["recent"]
    for i, form in enumerate(recent["form"]):
        if form == form_type:
            return {
                "form": form,
                "filing_date": recent["filingDate"][i],
                "report_date": recent["reportDate"][i],
                "accession": recent["accessionNumber"][i],
                "primary_doc": recent["primaryDocument"][i],
            }
    return None


def find_latest_earnings_event(filings_json: dict, forms: list) -> dict | None:
    """Find the most recent earnings-event filing — proxy for scheduled earnings call date.

    For US filers (10-K/10-Q): most recent 8-K with Item 2.02 (Results of Operations
    and Financial Condition) — the SEC-canonical earnings-release item.
    For foreign issuers (20-F, 40-F, 6-K): most recent 6-K — substantive content
    (earnings vs other material events) is not flagged in EDGAR metadata; used as
    proxy with awareness that not all 6-Ks are earnings.

    The 8-K/6-K report_date is the event date (when earnings were released and the
    call held), which differs from the 10-Q filing_date that can lag by weeks.
    """
    recent = filings_json["filings"]["recent"]
    items_list = recent.get("items", [""] * len(recent["form"]))
    is_foreign = "20-F" in forms or "40-F" in forms or "6-K" in forms

    for i, form in enumerate(recent["form"]):
        if not is_foreign and form == "8-K" and "2.02" in (items_list[i] or ""):
            return {
                "form": form,
                "filing_date": recent["filingDate"][i],
                "report_date": recent["reportDate"][i],
                "accession": recent["accessionNumber"][i],
                "primary_doc": recent["primaryDocument"][i],
                "items": items_list[i],
            }
        if is_foreign and form == "6-K":
            return {
                "form": form,
                "filing_date": recent["filingDate"][i],
                "report_date": recent["reportDate"][i],
                "accession": recent["accessionNumber"][i],
                "primary_doc": recent["primaryDocument"][i],
            }
    return None


def build_document_url(cik: str, accession: str, filename: str) -> str:
    """Construct the URL to fetch the primary document of a filing."""
    acc_no_dashes = accession.replace("-", "")
    cik_int = str(int(cik))
    return f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc_no_dashes}/{filename}"


def download_document(url: str, dest_path: Path) -> None:
    """Download a document from EDGAR to a local path."""
    r = requests.get(url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    dest_path.write_bytes(r.content)


def build_filename(ticker: str, form: str, report_date: str) -> str:
    """Build the target filename following the wiki's convention.

    Example: NVDA-10K-2026-01-26.htm
    """
    form_clean = form.replace("-", "").replace(" ", "")
    return f"{ticker}-{form_clean}-{report_date}.htm"


def fetch_for_company(
    ticker: str,
    config: dict,
    output_dir: Path,
) -> None:
    """Fetch the most recent filing(s) for a company."""
    print(f"\n→ {ticker} (CIK {config['cik']})")

    try:
        filings = get_company_filings(config["cik"])
    except Exception as e:
        print(f"  ✗ Failed to fetch filings index: {e}")
        return

    time.sleep(0.15)  # Stay well under the 10 req/sec limit

    for form_type in config["forms"]:
        filing = find_latest_filing(filings, form_type)
        if not filing:
            print(f"  ✗ No {form_type} found")
            continue

        filename = build_filename(ticker, filing["form"], filing["report_date"])
        htm_path = output_dir / filename

        if htm_path.exists():
            print(f"  ◦ {filename} already fetched, skipping")
            continue

        url = build_document_url(
            config["cik"], filing["accession"], filing["primary_doc"]
        )

        try:
            download_document(url, htm_path)
            print(f"  ✓ {filename}  (filed {filing['filing_date']})")
        except Exception as e:
            print(f"  ✗ Failed to download {filename}: {e}")

        time.sleep(0.15)


# ---------------------------------------------------------------------------
# Freshness mode — orchestrated by .claude/skills/check-recent-earnings/SKILL.md
# ---------------------------------------------------------------------------


def parse_date(date_str: str) -> datetime:
    """Parse YYYY-MM-DD date string."""
    return datetime.strptime(date_str, "%Y-%m-%d")


def estimate_next_filing(report_date_str: str, form_type: str) -> str | None:
    """Estimate next filing date based on cadence rules.

    Cadence assumptions (large accelerated filer windows):
    - 10-Q / 6-K: next quarter end (~3 months) + 40-day filing window
    - 10-K: next fiscal year end (~12 months) + 60-day filing window
    - 20-F: next fiscal year end (~12 months) + 4-month filing window
    - 40-F: next fiscal year end (~12 months) + 90-day filing window
    """
    if not report_date_str:
        return None
    last_period_end = parse_date(report_date_str)
    if form_type in ("10-Q", "6-K"):
        next_period_end = last_period_end + timedelta(days=92)
        next_filing = next_period_end + timedelta(days=40)
    elif form_type == "10-K":
        next_period_end = last_period_end + timedelta(days=365)
        next_filing = next_period_end + timedelta(days=60)
    elif form_type == "20-F":
        next_period_end = last_period_end + timedelta(days=365)
        next_filing = next_period_end + timedelta(days=120)
    elif form_type == "40-F":
        next_period_end = last_period_end + timedelta(days=365)
        next_filing = next_period_end + timedelta(days=90)
    else:
        return None
    return next_filing.strftime("%Y-%m-%d")


def add_trading_days(start: datetime, n: int) -> datetime:
    """Add N trading days, skipping weekends only.

    Does not exclude US market holidays — approximation acceptable for ~20-day windows
    where 1-2 day skew is operationally tolerable. The window is used to bound an
    earnings-calendar query; a holiday-induced 1-day overshoot returns at most a couple
    extra rows on the boundary, which downstream date filtering handles.
    """
    current = start
    added = 0
    while added < n:
        current += timedelta(days=1)
        if current.weekday() < 5:  # Mon-Fri
            added += 1
    return current


_NASDAQ_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.nasdaq.com",
    "Referer": "https://www.nasdaq.com/",
}


def fetch_nasdaq_earnings_for_date(date_str: str) -> list:
    """Query Nasdaq earnings calendar for a single date. Returns list of rows.

    Each row contains keys: symbol, name, time, fiscalQuarterEnding, epsForecast,
    marketCap, lastYearRptDt, lastYearEPS, noOfEsts. Returns [] on any failure.
    """
    url = "https://api.nasdaq.com/api/calendar/earnings"
    try:
        r = requests.get(
            url, params={"date": date_str}, headers=_NASDAQ_HEADERS, timeout=15
        )
        if r.status_code != 200:
            return []
        data = r.json() or {}
        rows = ((data.get("data") or {}).get("rows")) or []
        return rows
    except Exception:
        return []


def fetch_confirmed_upcoming_calls(
    vault_tickers: set, today: datetime, trading_days: int = 20
) -> dict:
    """Query Nasdaq earnings calendar across a trading-day window.

    Iterates weekdays from today+1 through today+N-trading-days, querying each
    weekday and filtering to vault tickers. Returns dict ticker -> {date, time,
    eps_forecast, fiscal_q}. If a ticker appears on multiple dates (rare), keeps
    the earliest.
    """
    end = add_trading_days(today, trading_days)
    confirmed = {}
    current = today + timedelta(days=1)
    while current <= end:
        if current.weekday() < 5:
            date_str = current.strftime("%Y-%m-%d")
            rows = fetch_nasdaq_earnings_for_date(date_str)
            for row in rows:
                sym = (row.get("symbol") or "").strip().upper()
                if sym in vault_tickers and sym not in confirmed:
                    confirmed[sym] = {
                        "date": date_str,
                        "time": row.get("time") or "",
                        "eps_forecast": row.get("epsForecast") or "",
                        "fiscal_q": row.get("fiscalQuarterEnding") or "",
                    }
            time.sleep(0.15)  # Be polite to Nasdaq
        current += timedelta(days=1)
    return confirmed


def _format_nasdaq_time(raw: str) -> str:
    """Normalize Nasdaq `time` field for display: drop "time-" prefix; map to short label."""
    if not raw:
        return ""
    mapping = {
        "time-pre-market": "pre-market",
        "time-after-hours": "after-hours",
        "time-not-supplied": "",
    }
    if raw in mapping:
        return mapping[raw]
    return raw.replace("time-", "")


def parse_index_md_last_updated(index_path: Path) -> dict:
    """Parse index.md companies table and return ticker -> last_updated mapping."""
    if not index_path.exists():
        return {}
    text = index_path.read_text()
    mapping = {}
    for line in text.splitlines():
        # Match table rows like: | [NVDA](wiki/companies/NVDA.md) | NVDA | 1 | ... | 2026-04-27 |
        m = re.match(
            r"\|\s*\[([A-Z]+)\]\([^)]+\)\s*\|\s*([A-Z]+)\s*\|.*\|\s*(\d{4}-\d{2}-\d{2})\s*\|",
            line,
        )
        if m:
            ticker = m.group(2).strip()
            last_updated = m.group(3).strip()
            mapping[ticker] = last_updated
    return mapping


def compute_freshness_per_ticker(ticker: str, config: dict) -> dict:
    """Query SEC EDGAR + compute freshness signals for one ticker.

    Returns dict with: most_recent_earnings (filing dict or None);
    next_filings (list of {form, estimated, last}); error (if query failed).
    """
    try:
        filings_json = get_company_filings(config["cik"])
    except Exception as e:
        return {"ticker": ticker, "error": str(e)}

    forms = config["forms"]

    # Earnings-relevant form types per filer category.
    # Recent earnings = most recent quarterly OR annual filing (proxy for "earnings call recently happened").
    if "10-K" in forms or "10-Q" in forms:
        earnings_forms = ["10-Q", "10-K", "8-K"]
    elif "20-F" in forms:
        earnings_forms = ["20-F", "6-K"]
    elif "40-F" in forms or "6-K" in forms:
        earnings_forms = ["40-F", "6-K"]
    else:
        earnings_forms = forms

    most_recent_earnings = None
    for form_type in earnings_forms:
        match = find_latest_filing(filings_json, form_type)
        if match and (
            most_recent_earnings is None
            or match["filing_date"] > most_recent_earnings["filing_date"]
        ):
            most_recent_earnings = match

    # Earnings-event filing: 8-K Item 2.02 (US) or 6-K (foreign) — proxy for actual
    # earnings call/release date, which can pre-date the 10-Q formal filing by weeks.
    earnings_event = find_latest_earnings_event(filings_json, forms)

    next_filings = []
    for form_type in forms:
        last = find_latest_filing(filings_json, form_type)
        if last and last.get("report_date"):
            est = estimate_next_filing(last["report_date"], form_type)
            if est:
                next_filings.append(
                    {"form": form_type, "estimated": est, "last_filed": last["filing_date"]}
                )

    return {
        "ticker": ticker,
        "forms": forms,
        "most_recent_earnings": most_recent_earnings,
        "earnings_event": earnings_event,
        "next_filings": next_filings,
    }


def format_freshness_report(
    freshness_data: list,
    staleness_map: dict,
    today: datetime,
    confirmed_calls: dict | None = None,
) -> str:
    """Format 3-section markdown report sorted by refresh-ingest priority."""
    today_str = today.strftime("%Y-%m-%d")
    thirty_days_ago = today - timedelta(days=30)
    thirty_days_from_now = today + timedelta(days=30)

    # Section 1 — Recent earnings (last 30 days). Sort by call date descending. Cap at 6.
    # Prefer earnings_event (8-K Item 2.02 / 6-K) report_date — the actual earnings call
    # date. Fall back to 10-Q/10-K/20-F/40-F formal filing date for the rare small-cap
    # case where earnings are filed without an 8-K Item 2.02 within window. Non-earnings
    # 8-Ks (e.g., proxy/governance) are intentionally excluded — they don't signal
    # earnings activity even when more recent than the last earnings call.
    periodic_forms = {"10-Q", "10-K", "20-F", "40-F"}
    recent = []
    for d in freshness_data:
        if d.get("error"):
            continue
        ee = d.get("earnings_event")
        if ee:
            ee_date_str = ee.get("report_date") or ee["filing_date"]
            if parse_date(ee_date_str) >= thirty_days_ago:
                recent.append((d["ticker"], ee_date_str, ee["form"], True))
                continue
        mre = d.get("most_recent_earnings")
        if (
            mre
            and mre["form"] in periodic_forms
            and parse_date(mre["filing_date"]) >= thirty_days_ago
        ):
            recent.append((d["ticker"], mre["filing_date"], mre["form"], False))
    recent.sort(key=lambda x: x[1], reverse=True)

    # Section 2 — Upcoming filings (next 30 days). Sort by estimated date ascending. Cap at 9.
    upcoming = []
    for d in freshness_data:
        if d.get("error"):
            continue
        for nf in d.get("next_filings", []):
            est_date = parse_date(nf["estimated"])
            if today < est_date <= thirty_days_from_now:
                upcoming.append((d["ticker"], nf["estimated"], nf["form"]))
    upcoming.sort(key=lambda x: x[1])

    # Section 3 — Stale tickers (90+ days since vault refresh). Sort by staleness descending. Cap at 3.
    stale = []
    for d in freshness_data:
        ticker = d["ticker"]
        last_updated = staleness_map.get(ticker)
        if last_updated:
            try:
                days_stale = (today - parse_date(last_updated)).days
                if days_stale >= 90:
                    stale.append((ticker, last_updated, days_stale))
            except ValueError:
                pass
    stale.sort(key=lambda x: x[2], reverse=True)

    # Build markdown output.
    out = [f"## Vault freshness scan ({today_str})", ""]

    out.append(f"**Recent earnings (last 30 days):** {len(recent)} tickers")
    if recent:
        shown = recent[:6]
        # Annotate when fallback to 10-Q/10-K filing date (no 8-K Item 2.02 found) — date
        # is then the formal filing, not the earnings call. Star marker preserves clarity.
        out.append(
            "- "
            + " / ".join(
                f"{t} (call {d})" if is_call else f"{t} ({f} filed {d}*)"
                for t, d, f, is_call in shown
            )
        )
        if len(recent) > 6:
            out.append(f"  and {len(recent) - 6} more")
        if any(not is_call for _, _, _, is_call in shown):
            out.append("  * = no 8-K Item 2.02 within window; formal filing date shown")
    else:
        out.append("- (none in vault reported in past 30 days)")
    out.append("")

    # Section 2 — Confirmed upcoming earnings calls (next 20 trading days). Source: Nasdaq.
    # Distinct from Section 3 cadence-estimated filings: these are announced calls (when the
    # call will be held + transcript available), whereas Section 3 estimates formal 10-Q/10-K
    # filings that typically lag the call by 1-4 weeks.
    confirmed_calls = confirmed_calls or {}
    twenty_trading_days_out = add_trading_days(today, 20)
    confirmed_list = []
    for ticker, info in confirmed_calls.items():
        try:
            call_date = parse_date(info["date"])
            if today < call_date <= twenty_trading_days_out:
                confirmed_list.append((ticker, info["date"], info.get("time", "")))
        except (ValueError, KeyError):
            pass
    confirmed_list.sort(key=lambda x: x[1])

    out.append(
        f"**Confirmed upcoming earnings calls (next 20 trading days):** "
        f"{len(confirmed_list)} tickers (source: Nasdaq)"
    )
    if confirmed_list:
        shown = confirmed_list[:9]
        out.append(
            "- "
            + " / ".join(
                f"{t} ({d}{' ' + _format_nasdaq_time(tm) if _format_nasdaq_time(tm) else ''})"
                for t, d, tm in shown
            )
        )
        if len(confirmed_list) > 9:
            out.append(f"  and {len(confirmed_list) - 9} more")
    else:
        out.append("- (none confirmed in next 20 trading days)")
    out.append("")

    out.append(f"**Upcoming quarterly filings (next 30 days):** {len(upcoming)} tickers expected")
    if upcoming:
        shown = upcoming[:9]
        out.append(
            "- "
            + " / ".join(f"{t} {f} est. {d}" for t, d, f in shown)
        )
        if len(upcoming) > 9:
            out.append(f"  and {len(upcoming) - 9} more")
    else:
        out.append("- (none expected in next 30 days)")
    out.append("")

    out.append(f"**Stale tickers (no refresh in 90+ days):** {len(stale)} tickers")
    if stale:
        shown = stale[:3]
        out.append(
            "- "
            + " / ".join(f"{t} (last refresh {d}; {days}d)" for t, d, days in shown)
        )
        if len(stale) > 3:
            out.append(f"  and {len(stale) - 3} more")
    else:
        out.append("- (no tickers stale beyond 90 days)")
    out.append("")

    # Footer with errors if any.
    errors = [(d["ticker"], d["error"]) for d in freshness_data if d.get("error")]
    if errors:
        out.append("**Query errors (excluded from above):**")
        for ticker, err in errors:
            out.append(f"- {ticker}: {err}")
        out.append("")

    return "\n".join(out)


def run_freshness_scan(companies: dict, index_path: Path) -> str:
    """Top-level freshness scan orchestration. Returns markdown report string."""
    today = datetime.now()
    staleness_map = parse_index_md_last_updated(index_path)
    freshness_data = []
    for ticker, config in companies.items():
        result = compute_freshness_per_ticker(ticker, config)
        freshness_data.append(result)
        time.sleep(0.15)  # Stay well under SEC EDGAR 10 req/sec limit
    # Confirmed upcoming earnings calls from Nasdaq (~20 calls covering the trading-day
    # window). Tier separate from SEC EDGAR — graceful empty result on failure.
    confirmed_calls = fetch_confirmed_upcoming_calls(set(companies.keys()), today, 20)
    return format_freshness_report(freshness_data, staleness_map, today, confirmed_calls)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ticker",
        help="Fetch filings for a single ticker (default: all seed companies)",
    )
    parser.add_argument(
        "--form", help="Limit to a single form type (e.g., 10-K, 10-Q)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("./raw/filings"),
        help="Where to save filings (default: ./raw/filings)",
    )
    parser.add_argument(
        "--freshness",
        action="store_true",
        help="Vault freshness scan: query SEC EDGAR for all tickers + emit ranked report (no fetch).",
    )
    parser.add_argument(
        "--index-path",
        type=Path,
        default=Path("./index.md"),
        help="Path to index.md for vault staleness cross-reference (--freshness mode).",
    )
    args = parser.parse_args()

    if USER_AGENT.endswith("@example.com"):
        print(
            "ERROR: Edit USER_AGENT at the top of this script to include "
            "your real name and email before running. SEC requires this.",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.ticker:
        companies = {args.ticker: COMPANIES[args.ticker]}
    else:
        companies = COMPANIES

    # Freshness scan: query-only; no file downloads.
    if args.freshness:
        report = run_freshness_scan(companies, args.index_path)
        print(report)
        return

    args.output_dir.mkdir(parents=True, exist_ok=True)

    if args.form:
        for c in companies.values():
            c["forms"] = [args.form] if args.form in c["forms"] else []

    for ticker, config in companies.items():
        if config["forms"]:
            fetch_for_company(ticker, config, args.output_dir)

    print(f"\nDone. Filings saved to {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()