#!/usr/bin/env python3
"""
reverse_dcf.py — reverse DCF / market-implied-expectations engine.

Takes market cap as GIVEN and solves for what the market is implicitly assuming:
  (a) "the market is pricing in ~X% growth for Y years", and
  (b) "the price bakes in ≈$Z of explicit cash flow + a terminal business worth $W".
Plus the no-growth-value vs growth-premium (PVGO) split and a sensitivity table.

This is the deterministic math core behind the /valuation-check skill — agents do the
judgment (extracting inputs, assessing plausibility), this script does the arithmetic
(LLMs fumble the iterative solve). Methodology + conventions from the vault references
raw/research/reverse-dcf-{research,implementation-reference}.md (Damodaran / Rappaport-
Mauboussin / Koller-McKinsey).

Conventions hard-coded (per the references):
- FCFF↔WACC matching (firm value → +cash −debt → equity).
- Terminal value = perpetuity-growth (not exit-multiple); g_T ≤ R_f.
- ROIC→WACC convergence is the disciplined terminal default (growth value-neutral at maturity).
- SBC is expensed upstream (the caller passes FCF/margin already net of SBC) — never added back here.
- Hard guard: terminal g < WACC.
- Two paths: FCFF (profitable) and revenue × normalized-future-margin (pre-profit).

This is a personal analysis tool. It computes implied expectations ("the market is implying
X — is that plausible?"), NEVER a fair-value target or a buy/sell call. Output is discovery
material, never written to a wiki/ page.

Usage:
    # profitable name (FCFF path) — solve implied growth for a 10y horizon:
    # NOTE: use the =form for negative numbers (--net-debt=-50B) so argparse doesn't read them as flags.
    python scripts/reverse_dcf.py --path fcff --market-cap=5.0T --net-debt=-50B \\
        --fcff=49B --wacc=0.09 --terminal-g=0.03 --horizon=10

    # pre-profit name (revenue path) — solve implied revenue CAGR:
    python scripts/reverse_dcf.py --path revenue --market-cap=8.0B --net-debt=-0.5B \\
        --revenue=1.0B --terminal-margin=0.25 --sales-to-capital=2.5 --tax=0.25 \\
        --wacc=0.10 --terminal-g=0.03 --horizon=10

    # the skill calls it via --json (cleanest — no negative-number gotcha):
    python scripts/reverse_dcf.py --json '{"path":"fcff","market_cap":"5.0T",...}'

    # closed-form sanity check (single-stage Gordon inversion):
    python scripts/reverse_dcf.py --closed-form --ev 40789 --fcff 1176 --wacc 0.0917

    --json '{...}'  accepts the same inputs as one JSON blob (how the skill calls it).
"""

import argparse
import json
import math
import sys
from pathlib import Path

# sibling module — the base-rate plausibility scorer (the "is what's priced in plausible?" block)
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    import base_rate_score
except Exception:                                          # scorer optional — engine still runs without it
    base_rate_score = None


# ── number parsing (accept 5.0T / 49B / -50M / 0.09 / 9%) ─────────────────────
def num(v):
    """Parse a human number: 5.0T, 49B, 850M, 1,200, 9%, -50B, or a bare float."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(",", "").replace("$", "")
    if not s:
        return None
    mult = 1.0
    if s.endswith("%"):
        return float(s[:-1]) / 100.0
    suf = s[-1].upper()
    if suf in ("T", "B", "M", "K"):
        mult = {"T": 1e12, "B": 1e9, "M": 1e6, "K": 1e3}[suf]
        s = s[:-1]
    return float(s) * mult


def hmoney(x):
    """Human-readable money: 1.23e12 → '$1.23T'."""
    if x is None:
        return "—"
    a = abs(x)
    for suf, d in (("T", 1e12), ("B", 1e9), ("M", 1e6)):
        if a >= d:
            return f"${x/d:,.2f}{suf}"
    return f"${x:,.0f}"


# ── core: forward EV as a function of the stage-1 growth rate ─────────────────
def ev_from_growth_fcff(g, base_fcff, wacc, term_g, horizon, term_wacc=None):
    """PV of an explicit FCFF stream growing at g for `horizon` years + perpetuity TV.
    term_wacc (default = wacc, the constant-WACC majority convention) is the rate used in
    the terminal Gordon denominator only — set it lower to model a firm that de-risks at
    maturity (the minority 'fading WACC' convention). Returns (ev, pv_exp, pv_term, fcff_N)."""
    tw = term_wacc if term_wacc is not None else wacc
    pv_exp = 0.0
    for t in range(1, horizon + 1):
        fcff = base_fcff * (1 + g) ** t
        pv_exp += fcff / (1 + wacc) ** t
    fcff_N = base_fcff * (1 + g) ** horizon
    tv = fcff_N * (1 + term_g) / (tw - term_g)          # Gordon on year-N+1 FCFF
    pv_term = tv / (1 + wacc) ** horizon                 # discounted back at the explicit-period WACC
    return pv_exp + pv_term, pv_exp, pv_term, fcff_N


def ev_from_revenue_path(g1, *, revenue0, cur_margin, terminal_margin, sales_to_capital,
                         tax, wacc, term_g, horizon, terminal_g_fade=0.04, term_wacc=None):
    """Pre-profit path: revenue grows at g1 fading linearly to terminal_g_fade; operating
    margin ramps linearly from cur_margin to terminal_margin by year N; reinvestment =
    ΔRevenue / sales_to_capital; FCFF = EBIT(1−tax) − reinvestment. term_wacc (default=wacc)
    is the terminal Gordon denominator rate (set lower for a maturing firm). Returns
    (ev, pv_explicit, pv_terminal, fcff_N, revenue_N, cagr)."""
    tw = term_wacc if term_wacc is not None else wacc
    pv_exp = 0.0
    rev_prev = revenue0
    fcff_N = 0.0
    rev = revenue0
    for t in range(1, horizon + 1):
        frac = (t - 1) / max(horizon - 1, 1)
        g_t = g1 + (terminal_g_fade - g1) * frac          # growth fades g1 → terminal_g_fade
        margin_t = cur_margin + (terminal_margin - cur_margin) * (t / horizon)
        rev = rev_prev * (1 + g_t)
        ebit = rev * margin_t
        reinvest = (rev - rev_prev) / sales_to_capital if sales_to_capital else 0.0
        fcff = ebit * (1 - tax) - reinvest
        pv_exp += fcff / (1 + wacc) ** t
        fcff_N = fcff
        rev_prev = rev
    tv = fcff_N * (1 + term_g) / (tw - term_g)
    pv_term = tv / (1 + wacc) ** horizon
    cagr = (rev / revenue0) ** (1 / horizon) - 1
    return pv_exp + pv_term, pv_exp, pv_term, fcff_N, rev, cagr


# ── solver: bisection on a monotonic f(x) = EV(x) − target ───────────────────
def solve(f, lo, hi, target, tol=1e-6, iters=200):
    """Bisection for the x in [lo,hi] with f(x)=target. f must be monotonic increasing.
    Returns x or None if the target isn't bracketed."""
    flo, fhi = f(lo) - target, f(hi) - target
    if flo > 0 and fhi > 0:
        return None                                       # target below the feasible floor
    if flo < 0 and fhi < 0:
        return None                                       # target above the feasible ceiling
    for _ in range(iters):
        mid = (lo + hi) / 2
        fm = f(mid) - target
        if abs(fm) < tol * max(1.0, abs(target)):
            return mid
        if fm < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# ── closed-form single-stage Gordon inversion (mature-name sanity check) ─────
def closed_form_g(ev, fcff, wacc):
    """V = FCFF·(1+g)/(WACC−g)  ⇒  g = (V·WACC − FCFF)/(V + FCFF). Mature firms only."""
    return (ev * wacc - fcff) / (ev + fcff)


def _implied_headline(cfg):
    """The single implied-growth number for a cfg (g for fcff, CAGR for revenue), or None if
    the price isn't bracketed. Used for lever-sensitivity ("how much each input bends the answer")."""
    wacc, tw, tg, h = cfg["wacc"], cfg.get("terminal_wacc"), cfg["terminal_g"], int(cfg["horizon"])
    if tg >= wacc:
        return None
    ev_t = cfg["market_cap"] + cfg.get("net_debt", 0.0)
    if cfg["path"] == "fcff":
        if not cfg.get("fcff") or cfg["fcff"] <= 0:
            return None
        return solve(lambda x: ev_from_growth_fcff(x, cfg["fcff"], wacc, tg, h, tw)[0], -0.50, 1.50, ev_t)
    g1 = solve(lambda x: ev_from_revenue_path(
        x, revenue0=cfg["revenue"], cur_margin=cfg.get("current_margin", 0.0),
        terminal_margin=cfg["terminal_margin"], sales_to_capital=cfg["sales_to_capital"],
        tax=cfg.get("tax", 0.25), wacc=wacc, term_g=tg, horizon=h, term_wacc=tw)[0], -0.20, 1.00, ev_t)
    if g1 is None:
        return None
    return ev_from_revenue_path(
        g1, revenue0=cfg["revenue"], cur_margin=cfg.get("current_margin", 0.0),
        terminal_margin=cfg["terminal_margin"], sales_to_capital=cfg["sales_to_capital"],
        tax=cfg.get("tax", 0.25), wacc=wacc, term_g=tg, horizon=h, term_wacc=tw)[5]   # the CAGR


def lever_sensitivity(cfg, base_headline):
    """Rank the inputs by how much each BENDS the implied-growth answer — the quantified
    'what the verdict hinges on'. Returns [(lever, delta_per_bump, bump_label), …] desc."""
    levers = []
    def bump(key, delta, label):
        c = dict(cfg); c[key] = cfg.get(key, 0) + delta
        v = _implied_headline(c)
        if v is not None and base_headline is not None:
            levers.append((label, abs(v - base_headline), f"{label} ±{abs(delta)*100:g}pt"))
    bump("wacc", 0.01, "WACC")
    bump("terminal_g", 0.01, "terminal growth")
    if cfg["path"] == "revenue":
        bump("terminal_margin", 0.05, "terminal margin")   # the dominant lever for pre-profit names
    levers.sort(key=lambda x: x[1], reverse=True)
    return levers


# ── orchestration ────────────────────────────────────────────────────────────
def run(cfg):
    out = {"inputs": cfg, "warnings": [], "guards": []}
    wacc = cfg["wacc"]
    term_wacc = cfg.get("terminal_wacc")                  # None = constant WACC (majority default)
    term_g = cfg["terminal_g"]
    horizon = int(cfg["horizon"])

    # --- guards (the references' §11) ---
    if term_g >= wacc:
        out["guards"].append(f"BLOCKED: terminal g ({term_g:.1%}) ≥ WACC ({wacc:.1%}) — Gordon TV diverges.")
        return out
    if term_g > cfg.get("rf", 0.045):
        out["warnings"].append(f"terminal g {term_g:.1%} exceeds R_f≈{cfg.get('rf',0.045):.1%} "
                               "(Damodaran cap: a firm cannot outgrow the economy forever).")

    market_cap = cfg["market_cap"]
    net_debt = cfg.get("net_debt", 0.0)                   # debt − cash; can be negative (net cash)
    ev_target = market_cap + net_debt                     # EV = equity + net debt
    out["ev_target"] = ev_target

    if cfg["path"] == "fcff":
        base_fcff = cfg["fcff"]
        if base_fcff <= 0:
            out["guards"].append("BLOCKED: FCFF ≤ 0 on the fcff path — use --path revenue for a pre-profit name.")
            return out
        g = solve(lambda x: ev_from_growth_fcff(x, base_fcff, wacc, term_g, horizon, term_wacc)[0],
                  -0.50, 1.50, ev_target)
        if g is None:
            out["guards"].append("no implied growth brackets the price in [−50%, +150%] — check inputs/path.")
            return out
        ev, pv_exp, pv_term, fcff_N = ev_from_growth_fcff(g, base_fcff, wacc, term_g, horizon, term_wacc)
        out["implied_growth"] = g
        out["headline_growth"] = f"~{g*100:.1f}% FCFF growth/yr for {horizon} years, then {term_g:.1%} forever"
        # no-growth (steady-state) value vs PVGO
        no_growth_ev = base_fcff / wacc
        out["no_growth_value"] = no_growth_ev
        out["pvgo"] = ev_target - no_growth_ev

    elif cfg["path"] == "revenue":
        rev0 = cfg["revenue"]
        f = lambda x: ev_from_revenue_path(
            x, revenue0=rev0, cur_margin=cfg.get("current_margin", 0.0),
            terminal_margin=cfg["terminal_margin"], sales_to_capital=cfg["sales_to_capital"],
            tax=cfg.get("tax", 0.25), wacc=wacc, term_g=term_g, horizon=horizon, term_wacc=term_wacc)[0]
        g1 = solve(f, -0.20, 1.00, ev_target)
        if g1 is None:
            ev_hi = f(1.00)
            if ev_hi < ev_target:
                out["guards"].append(
                    f"PRICE NOT DCF-JUSTIFIABLE at these inputs: even +100% initial revenue growth produces "
                    f"only {hmoney(ev_hi)} EV vs the {hmoney(ev_target)} the price implies — a real signal "
                    f"(the market needs a HIGHER terminal margin than {cfg['terminal_margin']:.0%}, a faster "
                    f"margin ramp, or is pricing on hope, not cash flow). Re-run with a higher --terminal-margin.")
            else:
                out["guards"].append("price below even −20% growth — check inputs/path.")
            return out
        ev, pv_exp, pv_term, fcff_N, rev_N, cagr = ev_from_revenue_path(
            g1, revenue0=rev0, cur_margin=cfg.get("current_margin", 0.0),
            terminal_margin=cfg["terminal_margin"], sales_to_capital=cfg["sales_to_capital"],
            tax=cfg.get("tax", 0.25), wacc=wacc, term_g=term_g, horizon=horizon, term_wacc=term_wacc)
        out["implied_initial_growth"] = g1
        out["implied_revenue_cagr"] = cagr
        out["terminal_revenue"] = rev_N
        out["headline_growth"] = (f"~{g1*100:.0f}% initial revenue growth fading to ~4% "
                                  f"(≈{cagr*100:.0f}% {horizon}y CAGR), reaching a {cfg['terminal_margin']:.0%} "
                                  f"mature operating margin")
        out["no_growth_value"] = None                     # undefined for a currently-unprofitable firm
        out["pvgo"] = None
    else:
        out["guards"].append(f"unknown path '{cfg['path']}' (use fcff|revenue)")
        return out

    # --- shared outputs: the Z/W decomposition ---
    out["pv_explicit"] = pv_exp                            # $Z
    out["pv_terminal"] = pv_term                           # $W
    out["tv_fraction"] = pv_term / ev if ev else None
    out["headline_bakedin"] = (f"of {hmoney(ev_target)} enterprise value, ≈{hmoney(pv_exp)} is explicit "
                               f"{horizon}y cash flow + ≈{hmoney(pv_term)} a terminal business "
                               f"({out['tv_fraction']:.0%} of value sits in the terminal — the most "
                               "assumption-sensitive piece)")
    if out["tv_fraction"] and out["tv_fraction"] > 0.85:
        out["warnings"].append(f"terminal value is {out['tv_fraction']:.0%} of EV — very assumption-heavy; "
                               "sensitize WACC and terminal g.")

    # --- base-rate plausibility (needs starting revenue to pick the size bucket) ---
    revenue = cfg.get("revenue")
    if base_rate_score and revenue:
        if cfg["path"] == "revenue":
            g_for_score, is_sales = out["implied_revenue_cagr"], True   # implied CAGR == sales growth
        else:
            g_for_score, is_sales = out["implied_growth"], False        # FCFF growth as a sales proxy
        out["base_rate"] = base_rate_score.score(
            g_for_score, revenue, horizon,
            inflation=cfg.get("inflation", base_rate_score.DEFAULT_INFLATION),
            growth_is_sales=is_sales)
    elif not revenue:
        out["warnings"].append("pass --revenue to enable the base-rate plausibility score "
                               "(buckets the implied growth against history by company size).")

    # --- "What must be true" — the organizing framing: for the price to make sense, X must ___ ---
    who = cfg.get("name", "this business")
    musts = []
    base_hl = out.get("implied_revenue_cagr") if cfg["path"] == "revenue" else out.get("implied_growth")
    if cfg["path"] == "fcff":
        musts.append(f"grow free cash flow ~{out['implied_growth']*100:.1f}%/yr for {horizon} years "
                     f"(then {term_g:.1%} forever) — while sustaining the margins/returns behind the FCFF base")
    else:
        musts.append(f"grow revenue ~{out['implied_initial_growth']*100:.0f}%/yr fading down "
                     f"(≈{out['implied_revenue_cagr']*100:.0f}% over {horizon}y)")
        musts.append(f"AND expand its operating margin to ~{cfg['terminal_margin']:.0%} at maturity")
    if out.get("base_rate"):
        br = out["base_rate"]
        musts.append(f"clear the history bar: a {br['growth_real']*100:.0f}% real growth for a "
                     f"{br['size_bucket']}-sales company was done by only ≈{br['fraction_achieving']*100:.1f}% "
                     f"of firms ever → {br['verdict']}")
    levers = lever_sensitivity(cfg, base_hl) if base_hl is not None else []
    out["what_must_be_true"] = {
        "who": who, "musts": musts,
        "levers": [(lab, d) for (lab, d, _) in levers],
        "top_lever": (levers[0] if levers else None),
    }

    # --- sensitivity: implied growth across WACC × terminal-g (fcff path) ---
    if cfg["path"] == "fcff":
        grid = {}
        for w in (wacc - 0.01, wacc, wacc + 0.01):
            row = {}
            for tg in (term_g - 0.01, term_g, term_g + 0.01):
                if tg >= w:
                    row[f"{tg:.0%}"] = None
                    continue
                gg = solve(lambda x: ev_from_growth_fcff(x, cfg["fcff"], w, tg, horizon)[0],
                           -0.50, 1.50, ev_target)
                row[f"{tg:.0%}"] = gg
            grid[f"{w:.0%}"] = row
        out["sensitivity"] = grid
    return out


def _print(out):
    if out.get("guards"):
        for g in out["guards"]:
            print(f"✗ {g}")
        return
    print("── Reverse DCF — market-implied expectations ──")
    print(f"EV (market cap + net debt): {hmoney(out['ev_target'])}")
    # the organizing framing FIRST — "for the price to make sense, X must ___"
    wmbt = out.get("what_must_be_true")
    if wmbt and wmbt["musts"]:
        print(f"\n★ For the price to make sense, {wmbt['who']} must:")
        for i, m in enumerate(wmbt["musts"], 1):
            print(f"   {i}. {m}")
        if wmbt.get("top_lever"):
            lab, d, blab = wmbt["top_lever"]
            print(f"   ↳ the answer hinges most on the {lab} ({blab} moves the implied growth ~{d*100:.1f}pt); "
                  "it is a conditional read, not a fact.")
    print()
    print("→ " + out["headline_growth"])
    print("→ " + out["headline_bakedin"])
    if out.get("no_growth_value") is not None:
        ng, pvgo = out["no_growth_value"], out["pvgo"]
        ev = out["ev_target"]
        print(f"→ price decomposition: {hmoney(ng)} no-growth value (assets in place) "
              f"+ {hmoney(pvgo)} growth premium (PVGO = {pvgo/ev:.0%} of EV)")
    if out.get("sensitivity"):
        print("\nSensitivity — implied growth across WACC (rows) × terminal g (cols):")
        cols = list(next(iter(out["sensitivity"].values())).keys())
        print("  WACC \\ g_T   " + "   ".join(f"{c:>6}" for c in cols))
        for w, row in out["sensitivity"].items():
            cells = "   ".join((f"{v*100:5.1f}%" if v is not None else "   n/a") for v in row.values())
            print(f"     {w:>5}     {cells}")
    if out.get("base_rate") and base_rate_score:
        print()
        print(base_rate_score.render(out["base_rate"]))
    for w in out.get("warnings", []):
        print(f"⚠️  {w}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", help="all inputs as one JSON object (how the skill calls it)")
    ap.add_argument("--closed-form", action="store_true", help="single-stage Gordon inversion sanity check")
    ap.add_argument("--path", choices=["fcff", "revenue"], default="fcff")
    ap.add_argument("--market-cap"); ap.add_argument("--net-debt")
    ap.add_argument("--ev", help="enterprise value directly (closed-form mode)")
    ap.add_argument("--fcff"); ap.add_argument("--revenue")
    ap.add_argument("--current-margin"); ap.add_argument("--terminal-margin")
    ap.add_argument("--sales-to-capital"); ap.add_argument("--tax")
    ap.add_argument("--wacc"); ap.add_argument("--rf"); ap.add_argument("--terminal-g")
    ap.add_argument("--terminal-wacc", help="WACC in the terminal Gordon denominator (default = --wacc; "
                    "set lower to model a firm that de-risks at maturity)")
    ap.add_argument("--horizon", default="10")
    ap.add_argument("--inflation", help="expected inflation for the base-rate real-adjustment (default 2.5%)")
    args = ap.parse_args()

    if args.closed_form:
        g = closed_form_g(num(args.ev), num(args.fcff), num(args.wacc))
        print(f"closed-form implied perpetuity g = {g*100:.2f}%  "
              f"(EV {hmoney(num(args.ev))}, FCFF {hmoney(num(args.fcff))}, WACC {num(args.wacc):.2%})")
        return 0

    if args.json:
        cfg = json.loads(args.json)
        cfg = {k: (num(v) if k not in ("path", "name") else v) for k, v in cfg.items()}
    else:
        cfg = {
            "path": args.path,
            "market_cap": num(args.market_cap), "net_debt": num(args.net_debt) or 0.0,
            "fcff": num(args.fcff), "revenue": num(args.revenue),
            "current_margin": num(args.current_margin) or 0.0,
            "terminal_margin": num(args.terminal_margin), "sales_to_capital": num(args.sales_to_capital),
            "tax": num(args.tax) if args.tax else 0.25,
            "wacc": num(args.wacc), "rf": num(args.rf) if args.rf else 0.045,
            "terminal_wacc": num(args.terminal_wacc) if args.terminal_wacc else None,
            "terminal_g": num(args.terminal_g) if args.terminal_g else 0.03,
            "horizon": int(num(args.horizon)),
            "inflation": num(args.inflation) if args.inflation else 0.025,
        }
    if cfg.get("market_cap") is None or cfg.get("wacc") is None:
        ap.error("need at least --market-cap and --wacc (or a --json blob with them)")
    _print(run(cfg))
    return 0


if __name__ == "__main__":
    sys.exit(main())
