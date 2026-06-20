#!/usr/bin/env python3
"""parse_short_interest.py — normalize a short-interest table export into a CSV.

DEPRECATED — superseded by scripts/fetch_short_interest.py (the /short-interest-snapshot
skill), which pulls the same data automatically from the FINRA API (no paste needed).
trading-logic.com can't be fetched without a headless browser, so this manual-paste path
is kept only for the squeeze-score / %-float extras it carries. NOTE: it writes a
DIFFERENT (trading-logic) schema than fetch_short_interest.py — do not mix the two outputs
in raw/data/short-interest/. `vault_companies()` + `ADR_ALLOWLIST` below are still imported
and reused by fetch_short_interest.py.

Source: trading-logic.com/en/short-interest (US NYSE/Nasdaq, FINRA settlement
data, twice-monthly). This script does NOT fetch anything — it normalizes a
table you've exported/pasted into the vault's fixed schema and fills the
`settlement_date` + `in_vault` columns.

Output: raw/data/short-interest/short-interest_<settlement_date>.csv
See raw/data/short-interest/README.md for the schema + conventions.

Usage:
    python scripts/parse_short_interest.py export.csv --settlement-date 2026-05-29
    pbpaste | python scripts/parse_short_interest.py --settlement-date 2026-05-29
    python scripts/parse_short_interest.py export.csv --settlement-date 2026-05-29 --dry-run
"""
import argparse
import csv
import io
import re
import sys
from pathlib import Path

# Canonical output columns (order matters — every snapshot CSV is identical).
CANONICAL = [
    "settlement_date", "ticker", "company", "squeeze_score", "short_pct",
    "short_pct_float", "change_vs_prior", "change_1mo", "shares_short",
    "short_value_usd", "days_to_cover", "industry", "trend", "in_vault",
]

# Foreign issuers that are nonetheless US-listed (ADR/US shares) → FINRA short
# interest exists → coverable by the US site. Everything else flagged
# `foreign_issuer: true` in frontmatter is foreign-exchange-only (not coverable).
ADR_ALLOWLIST = {"ARM", "CCJ", "NBIS", "NOK", "TSEM", "TSM"}

# normalized source-header -> canonical field. Source column names are matched
# fuzzily (lowercased, non-alphanumerics stripped) so small label variations and
# export-vs-paste differences still map.
ALIASES = {
    "ticker": "ticker", "symbol": "ticker", "tickersymbol": "ticker",
    "company": "company", "companyname": "company", "name": "company",
    "squeezescore": "squeeze_score", "squeeze": "squeeze_score", "score": "squeeze_score",
    "shortinterest": "short_pct", "shortinterestpercent": "short_pct",
    "shortinterestpct": "short_pct", "shortint": "short_pct", "si": "short_pct",
    "shortpercent": "short_pct", "shortpct": "short_pct",
    "shortoffloat": "short_pct_float", "shortpercentfloat": "short_pct_float",
    "shortpctfloat": "short_pct_float", "shortfloat": "short_pct_float",
    "percentoffloat": "short_pct_float", "floatshort": "short_pct_float",
    "shortpercentoffloat": "short_pct_float",
    "change": "change_vs_prior", "changevsprior": "change_vs_prior",
    "changevspriorperiod": "change_vs_prior", "priorchange": "change_vs_prior",
    "changeprior": "change_vs_prior", "vsprior": "change_vs_prior",
    "onemonth": "change_1mo", "onemonthchange": "change_1mo", "1mochange": "change_1mo",
    "1month": "change_1mo", "change1m": "change_1mo", "change1mo": "change_1mo",
    "onemonthpercent": "change_1mo", "1m": "change_1mo", "mom": "change_1mo",
    "sharesshort": "shares_short", "sharesshorted": "shares_short",
    "shortshares": "shares_short", "shortvolume": "shares_short", "shares": "shares_short",
    "shortvalue": "short_value_usd", "dollarvalue": "short_value_usd",
    "value": "short_value_usd", "shortvalueusd": "short_value_usd",
    "shortdollarvalue": "short_value_usd", "shortinterestvalue": "short_value_usd",
    "daystocover": "days_to_cover", "dtc": "days_to_cover", "daystocoverratio": "days_to_cover",
    "industry": "industry", "sector": "industry", "industryclassification": "industry",
    "trend": "trend", "trendindicator": "trend",
}


def norm(h: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(h).lower())


def vault_companies(vault_root: Path) -> dict:
    """Return {ticker: coverable_bool} for every wiki/companies/ page.

    coverable = US-listed (foreign_issuer not true) OR a known US-listed ADR.
    Reads the filename stem AND any `tickers: [...]` frontmatter so a page whose
    slug differs from its market ticker is still matched.
    """
    out: dict = {}
    comp_dir = vault_root / "wiki" / "companies"
    for f in sorted(comp_dir.glob("*.md")):
        try:
            head = "".join(f.read_text(errors="ignore").splitlines(keepends=True)[:20])
        except Exception:
            head = ""
        foreign = bool(re.search(r"^foreign_issuer:\s*true\b", head, re.M))
        tickers = {f.stem.upper()}
        m = re.search(r"^tickers:\s*\[([^\]]*)\]", head, re.M)
        if m:
            for t in m.group(1).split(","):
                t = t.strip().strip("'\"").upper()
                if t:
                    tickers.add(t)
        for t in tickers:
            coverable = (not foreign) or (t in ADR_ALLOWLIST)
            out[t] = out.get(t, False) or coverable
    return out


def read_rows(text: str):
    """Parse the export into a list of row-lists. Auto-detect delimiter; fall
    back to whitespace-split for a copy-pasted table."""
    sample = text[:8192]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t;|")
        return list(csv.reader(io.StringIO(text), dialect))
    except Exception:
        rows = []
        for ln in text.splitlines():
            if ln.strip():
                rows.append(re.split(r"\t|\s{2,}", ln.rstrip()))
        return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", nargs="?", help="input file (CSV/TSV/pasted table); omit to read stdin")
    ap.add_argument("--settlement-date", required=True,
                    help="FINRA settlement date YYYY-MM-DD (filename + settlement_date column)")
    ap.add_argument("--vault-root", default=".", help="vault root (default: cwd)")
    ap.add_argument("--out", help="output path (default: raw/data/short-interest/short-interest_<date>.csv)")
    ap.add_argument("--dry-run", action="store_true", help="parse + summarize, write nothing")
    args = ap.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.settlement_date):
        ap.error("--settlement-date must be YYYY-MM-DD")

    root = Path(args.vault_root)
    text = Path(args.input).read_text(errors="ignore") if args.input else sys.stdin.read()
    if not text.strip():
        ap.error("no input (pass a file or pipe a table on stdin)")

    rows = read_rows(text)
    if len(rows) < 2:
        ap.error("need a header row + at least one data row")

    header = [str(c).strip() for c in rows[0]]
    colmap: dict = {}
    unmapped = []
    for i, h in enumerate(header):
        canon = ALIASES.get(norm(h))
        if canon and canon not in colmap:
            colmap[canon] = i
        elif not canon:
            unmapped.append(h)
    if "ticker" not in colmap:
        ap.error(f"could not find a ticker column. header was: {header}")

    vc = vault_companies(root)
    vault_all = set(vc)
    us_eligible = {t for t, c in vc.items() if c}

    out_rows = []
    matched = set()
    for r in rows[1:]:
        if not any(str(c).strip() for c in r):
            continue
        def get(field):
            i = colmap.get(field)
            return str(r[i]).strip() if i is not None and i < len(r) else ""
        tk = get("ticker").upper()
        if not tk:
            continue
        in_vault = tk in vault_all
        if in_vault:
            matched.add(tk)
        rec = {k: "" for k in CANONICAL}
        for field in colmap:
            rec[field] = get(field)
        rec["ticker"] = tk
        rec["settlement_date"] = args.settlement_date
        rec["in_vault"] = "true" if in_vault else "false"
        out_rows.append(rec)

    missing_us = sorted(us_eligible - matched)
    # ---- summary (stderr) ----
    print(f"parsed {len(out_rows)} rows · {len(matched)} vault tickers matched "
          f"(of {len(us_eligible)} US-eligible)", file=sys.stderr)
    if unmapped:
        print(f"unmapped source columns (dropped): {unmapped}", file=sys.stderr)
    print(f"matched vault tickers: {sorted(matched)}", file=sys.stderr)
    print(f"US-eligible vault names NOT in this snapshot ({len(missing_us)}): {missing_us}",
          file=sys.stderr)
    print("  (a missing US name = the site's filtered ~2,533-row table doesn't carry it, "
          "usually low short interest — not a data error)", file=sys.stderr)

    if args.dry_run:
        print("dry-run: no file written", file=sys.stderr)
        return 0

    out = Path(args.out) if args.out else (
        root / "raw" / "data" / "short-interest" / f"short-interest_{args.settlement_date}.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CANONICAL)
        w.writeheader()
        w.writerows(out_rows)
    print(f"wrote {out} ({len(out_rows)} rows)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
