#!/usr/bin/env python3
"""
base_rate_score.py — score an implied growth rate against history (the "is what's priced in
plausible?" feature). The companion to reverse_dcf.py.

reverse_dcf.py solves for the growth the market is pricing in. This module answers: how RARE
is that growth, historically, for a company this size over this horizon? It turns "what's
priced in" into "how likely is what's priced in" — the highest-value step (per both vault
references).

Data = embedded from raw/research/mauboussin-base-rate-tables.md (Mauboussin & Callahan,
"The Base Rate Book", Credit Suisse 2016, + Counterpoint Global 2026 updates). The book's
full 44-class cell grid is copyrighted and not reproduced verbatim; we embed (a) per-size-
bucket median/SD of sales CAGR, (b) the published tail-cell anchors, and (c) the unconditional
band×horizon frequencies — then MODEL the percentile from the bucket median+SD and OVERRIDE
with the published anchor whenever the query lands on one (exactly the report's recommended
approach). Modeled cells are flagged vs published.

Two disciplines the book insists on, both applied here:
- The base rates are REAL (inflation-adjusted, 2015 dollars). A nominal implied growth must be
  deflated before mapping, or the tool understates how aggressive it is. Default inflation 2.5%.
- Buckets are by STARTING SALES (revenue), NOT market cap. Pass revenue.

Tier-3 reference data; a plausibility aid, never a forecast ("base rates are an outside view,
not destiny" — companies do fill the tails).

Usage:
    python scripts/base_rate_score.py --growth 0.147 --revenue 200B --horizon 10
    python scripts/base_rate_score.py --growth 0.45 --revenue 6B --horizon 10   # the Tesla cell
"""

import argparse
import math
import sys

DEFAULT_INFLATION = 0.025

# Size buckets by STARTING SALES (2015 USD): (low, high, label, mean3, median3, sd3) —
# mean/median/SD of 3-year sales CAGR. Source: Base Rate Book Exhibit 4, pp. 24-25.
SIZE_BUCKETS = [
    (0,        325e6,    "$0–325M",        0.212, 0.117, 0.400),
    (325e6,    700e6,    "$325–700M",      0.107, 0.075, 0.159),
    (700e6,    1.25e9,   "$700M–1.25B",    0.092, 0.068, 0.135),
    (1.25e9,   2e9,      "$1.25–2B",       0.086, 0.062, 0.140),
    (2e9,      3e9,      "$2–3B",          0.072, 0.054, 0.121),
    (3e9,      4.5e9,    "$3–4.5B",        0.064, 0.050, 0.111),
    (4.5e9,    7e9,      "$4.5–7B",        0.057, 0.044, 0.116),   # the "Tesla decile"
    (7e9,      12e9,     "$7–12B",         0.047, 0.037, 0.109),
    (12e9,     25e9,     "$12–25B",        0.038, 0.030, 0.123),
    (25e9,     50e9,     ">$25B",          0.024, 0.022, 0.109),
    (50e9,     float("inf"), ">$50B (mega)", 0.012, 0.015, 0.103),
]

# Unconditional SD of sales CAGR by horizon (Exhibits 2-3, p. 22) — used to scale the 3-yr
# bucket SD to other horizons (growth dispersion compresses as the horizon lengthens).
UNCOND_SD = {1: 2.752, 3: 0.187, 5: 0.123, 10: 0.080}
UNCOND_MEDIAN = {1: 0.058, 3: 0.054, 5: 0.052, 10: 0.049}

# Unconditional band frequencies (full universe) by horizon — for context/cross-check.
# band lower-bound (decimal) -> {horizon: fraction}. Source: Exhibit 2, p. 22.
UNCOND_BANDS = {
    0.00: {1: 0.206, 3: 0.252, 5: 0.288, 10: 0.342},   # 0–5%
    0.05: {1: 0.178, 3: 0.213, 5: 0.242, 10: 0.283},   # 5–10%
    0.10: {1: 0.114, 3: 0.123, 5: 0.126, 10: 0.116},   # 10–15%
    0.15: {3: 0.067},                                   # 15–20% (the book's worked cell)
    0.20: {1: 0.045, 3: 0.039, 5: 0.031, 10: 0.020},   # 20–25%
    0.30: {1: 0.020, 3: 0.015, 5: 0.010, 10: 0.006},   # 30–35%
    0.45: {1: 0.055, 3: 0.025, 5: 0.013, 10: 0.003},   # >45%
}

# Published tail-cell ANCHORS (override the model when a query lands here). Keyed by
# (bucket_label, horizon, band_lower_bound) -> fraction of firms in/above that band.
# Source: Base Rate Book pp. 23-26 (the cells the book itself walks through).
TAIL_ANCHORS = {
    (">$50B (mega)", 10, 0.45): 0.000,
    (">$50B (mega)", 10, 0.30): 0.000,
    (">$50B (mega)", 10, 0.20): 0.000,
    (">$50B (mega)", 10, 0.00): 0.378,
    (">$50B (mega)", 10, 0.05): 0.172,
    ("$4.5–7B",      10, 0.45): 0.000,   # the Tesla reference class
    ("$4.5–7B",      10, 0.30): 0.002,
    ("$0–325M",      10, 0.45): 0.021,
    ("$0–325M",       1, 0.45): 0.151,
}

# ROIC / CAP persistence (companion work) — for terminal/CAP plausibility notes.
ROIC_PERSISTENCE_AVG = 0.79     # avg across sectors (range 0.70–0.90); fade ≈ 1 − persistence
ROIC_FADE_AVG = 0.21

# Real-world anchors the book assesses (all ≈ zero base rate) — for the chat narrative.
ZERO_BASE_RATE_EXAMPLES = (
    "Tesla 50%/10y from ~$6B (0% in its size class), OpenAI 108%/5y & 72.7%/5y, Oracle Cloud ~75% "
    "— each a near-zero historical base rate."
)


def _erfc(x):
    return math.erfc(x)


def normal_survival(x, mu, sd):
    """P(X ≥ x) for X ~ Normal(mu, sd)."""
    if sd <= 0:
        return 1.0 if x <= mu else 0.0
    return 0.5 * _erfc((x - mu) / (sd * math.sqrt(2)))


def pick_bucket(revenue):
    for lo, hi, label, m3, med3, sd3 in SIZE_BUCKETS:
        if lo <= revenue < hi:
            return label, m3, med3, sd3
    return SIZE_BUCKETS[-1][2], *SIZE_BUCKETS[-1][3:]   # mega fallback


def _band_lb(g):
    """Lowest published band bound at or below g (for anchor lookup)."""
    bounds = [0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.00]
    for b in bounds:
        if g >= b:
            return b
    return None


def verdict_for(frac):
    if frac is None:
        return "unscored"
    if frac >= 0.40:
        return "base-rate plausible (common)"
    if frac >= 0.20:
        return "above median, still ordinary"
    if frac >= 0.08:
        return "aggressive (roughly top quartile)"
    if frac >= 0.02:
        return "very aggressive — priced for perfection (≈top 2–8%)"
    if frac >= 0.002:
        return "extreme outlier (≈top 0.2–2%)"
    return "no meaningful historical precedent (≈0% base rate)"


def score(growth_nominal, revenue, horizon, *, inflation=DEFAULT_INFLATION, growth_is_sales=True):
    """Return a dict scoring `growth_nominal` (a nominal CAGR) for a company with `revenue`
    starting sales over `horizon` years, against the size-conditioned sales-growth base rates."""
    h = min((1, 3, 5, 10), key=lambda k: abs(k - horizon))   # snap to a published horizon
    g_real = growth_nominal - inflation
    label, mean3, median3, sd3 = pick_bucket(revenue)

    # scale the 3-yr bucket median + SD to the query horizon using the unconditional ratios
    sd_h = sd3 * (UNCOND_SD[h] / UNCOND_SD[3])
    med_h = median3 * (UNCOND_MEDIAN[h] / UNCOND_MEDIAN[3])
    modeled = normal_survival(g_real, med_h, sd_h)

    # override with a published anchor if the query lands on one
    band = _band_lb(g_real)
    anchor = TAIL_ANCHORS.get((label, h, band)) if band is not None else None
    frac = anchor if anchor is not None else modeled
    source = "published cell" if anchor is not None else "modeled (bucket median+SD)"

    out = {
        "growth_nominal": growth_nominal, "growth_real": g_real, "inflation": inflation,
        "revenue": revenue, "size_bucket": label, "horizon": h, "horizon_requested": horizon,
        "bucket_median_real": med_h, "bucket_sd_real": sd_h,
        "fraction_achieving": frac, "source": source, "modeled_fraction": modeled,
        "anchor_fraction": anchor, "verdict": verdict_for(frac),
        "persistence_note": (f"ROIC fade for terminal/CAP: persistence ≈{ROIC_PERSISTENCE_AVG:.2f} "
                             f"(fade ≈{ROIC_FADE_AVG:.2f}); large-caps persist longer. "
                             "Implied CAP for most US firms ≈5–20y."),
    }
    if frac is not None and frac < 0.005:
        out["zero_base_rate_flag"] = ("This implied growth is in the near-zero-base-rate tail — "
                                      f"the company of {ZERO_BASE_RATE_EXAMPLES}")
    out["headline"] = (
        f"A sustained ~{g_real*100:.0f}% REAL sales growth ({growth_nominal*100:.0f}% nominal − "
        f"{inflation*100:.1f}% inflation) for {h} years, for a {label}-sales company, was achieved "
        f"by ≈{frac*100:.1f}% of firms historically → {out['verdict']}.")
    if not growth_is_sales:
        out["proxy_caveat"] = ("scored against SALES-growth base rates as a proxy for the implied "
                               "FCFF growth (valid at roughly stable margins; looser if margins shift).")
    return out


def render(out):
    lines = ["── Base-rate plausibility (Mauboussin) ──", out["headline"]]
    lines.append(f"  bucket {out['size_bucket']} · horizon {out['horizon']}y · "
                 f"reference median ≈{out['bucket_median_real']*100:.1f}% real · "
                 f"frac ≥ implied ≈{out['fraction_achieving']*100:.1f}% [{out['source']}]")
    if out.get("proxy_caveat"):
        lines.append(f"  note: {out['proxy_caveat']}")
    if out.get("zero_base_rate_flag"):
        lines.append(f"  ⚠️  {out['zero_base_rate_flag']}")
    lines.append(f"  {out['persistence_note']}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--growth", required=True, type=float, help="nominal implied CAGR (e.g. 0.147)")
    ap.add_argument("--revenue", required=True, help="starting sales / revenue (e.g. 200B, 46M)")
    ap.add_argument("--horizon", type=int, default=10)
    ap.add_argument("--inflation", type=float, default=DEFAULT_INFLATION)
    ap.add_argument("--fcff-proxy", action="store_true",
                    help="the growth is implied FCFF growth (flag the sales-proxy caveat)")
    args = ap.parse_args()

    def num(v):
        s = str(v).strip().upper().replace(",", "").replace("$", "")
        mult = {"T": 1e12, "B": 1e9, "M": 1e6, "K": 1e3}.get(s[-1:], 1)
        return float(s[:-1]) * mult if mult != 1 else float(s)

    out = score(args.growth, num(args.revenue), args.horizon,
                inflation=args.inflation, growth_is_sales=not args.fcff_proxy)
    print(render(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
