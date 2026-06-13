---
type: tracker
tickers: [CRWV, ORCL, MSFT, AVGO, NVDA, NBIS]
last_updated: 2026-06-13
---

# AI Credit Spread Watch — the cycle's fuel gauge

**What this tracks:** the gap between what AI-related borrowers pay to borrow and what ordinary, comparable borrowers pay — the earliest observable signal that the credit market funding the AI build-out is changing its mind. **Why it works:** the build-out is now credit-funded (big-five free cash flow is below capex; ~$1.5T of 2025-28 capex needs outside money — see [[AI-buildout-who-holds-the-risk]]), so the capex cycle cannot outlive its financing, and lenders reprice before equity holders do (all downside, no dream). In 2000, telecom bond spreads blew out months before the stocks broke. **Today's baseline reading is itself the finding: the gap is ~zero** — the BIS measured AI private-credit loans at 6.2pp spread vs 6.1pp for comparable non-AI loans (Bulletin 120, Jan 2026), while S&P's own models assign 70-90% loss-given-default to neocloud unsecured debt. One of the two markets is wrong; this page watches which one folds.

**Discipline:** describe-don't-recommend — this page reports dial readings, never buy/sell. Readings carry their as-of date; a dial is only as good as its last check. Per the tracker freshness rule, any session that touches a financing signal (a new facility's pricing, a rating action, a backstop restatement) updates the affected row same-session.

## The four layers (instruments + how to read them)

### Layer 1 — The baseline: what ordinary borrowers pay (free, daily, FRED)

| Series | What it is | Where |
|---|---|---|
| `BAMLH0A0HYM2` | US high-yield option-adjusted spread — risky borrowers in general | fred.stlouisfed.org (free, daily) |
| `BAMLC0A0CM` | US investment-grade OAS — safe borrowers in general | fred.stlouisfed.org |

These move with the whole credit market. They are the *control group*: AI-specific stress is only signaled when the AI instruments below widen **relative to** these.

### Layer 2 — The AI side: specific public securities (the real dial)

| Instrument | What it isolates | Where to read |
|---|---|---|
| **CRWV 9.75% 2031 unsecured notes** — yield vs the HY index | The purest public AI-credit instrument; the system's most leveraged public node | FINRA bond search (TRACE) / brokerage bond screen |
| **CRWV secured-vs-unsecured gap** — the A3-rated SPV paper (~5.9% at issue) vs the unsecured notes | Whether lenders still trust the *customer contracts* (the gap widening at the SECURED leg = doubting the contracts themselves — the loud alarm) | issue pricing in 8-Ks; TRACE |
| **ORCL vs MSFT bonds** (matched maturity) | The investment-grade "AI-leverage premium": debt-funded builder vs cash-rich payer. MSFT is the control, not a signal — subtracting it cancels general market conditions | FINRA/brokerage |

**Instrument-selection logic (why three probes, not all seven payers):** credit stress breaks the weakest link first — neocloud (CRWV, pure AI credit) → leveraged hyperscaler (ORCL, the marginal IG name) → fortress names last. The AA/AAA payers (MSFT/GOOGL/AMZN/META) carry almost no AI-specific spread signal while calm; watching them adds noise, not information (the BIS QR March 2026 CDS finding — differentiation "especially for hyperscalers with lower credit ratings" — confirms the weakest-link ordering). **Pre-registered expansion trigger:** if dial 4 (ORCL-vs-MSFT) turns 🟡, the next run ADDS META-vs-MSFT and AMZN-vs-MSFT pairs to test whether the repricing is Oracle-specific or spreading across the group. NBIS is covered via dial 6 rating actions + the Layer-3 deal sweep (foreign filer; bond data too thin for a clean dial).

### Layer 3 — Deal-by-deal new-issue pricing + PRIMARY-MARKET BEHAVIOR (caught by normal vault ingests)

Every new financing discloses its rate: CRWV's next DDTL (vs SOFR+2.25% on the March 2026 facility), each Apollo/Blackstone tranche, data-center ABS coupons, neocloud raises. Compare each new deal to the last — rising pricing deal-over-deal is the differential opening in real time. `/latest-alpha` runs and refresh ingests already surface these.

**The primary-market signature (added from the GS rates-desk read, 2026-06-12 video-intel — Tier 3):** the historically *earliest* crack is not secondary spreads but new-deal behavior — **new-issue concessions appearing** (deals needing extra yield over fair value to clear) and **failed takedowns** (buyers not showing up for parts of new issues). A GS rates co-head named exactly these as the watch signatures, placed them **12-18 months out (~mid/late 2027)**, with **2027 as the issuance squeeze point** (deeper capex cycle + deeper credit cycle + Treasury upping coupon supply). Secondary spreads can stay polite while concessions quietly widen — so any Tier-4 report of an AI/datacenter deal pricing wide-of-talk, downsized, or pulled is a dial-7 event even if dials 0-4 are calm. **Verification lead (open):** the same desk says "the private credit markets asked for a larger return earlier this year — it created a little bit of angst within the AI trade" — a candidate first-flinch precursor (~Q1 2026), unverified; confirm at Tier 4 and log here if real.

### Layer 4 — The referees' updates (the only view into private credit)

BIS Quarterly Review / Bulletins (the AI-vs-non-AI loan spread analysis itself), IMF GFSR (April + October), FSB reports. Private credit marks slowly and smooths losses — these periodic documents are the only window into the $800B channel the public proxies can't see. **Known blind spot:** the private side can deteriorate quietly while Layers 1-3 stay calm; never read calm public proxies as an all-clear on private credit.

## Current readings

| # | Dial | Reading | As of | Status |
|---|---|---|---|---|
| 0 | Layer-1 controls (FRED) | HY OAS **2.80pp** (+0.01/1m, −0.29/3m) · IG OAS **0.75pp** — both historically very tight; the control group itself shows broad credit complacency | 2026-06-10 (first script run 2026-06-13) | ⚪ Baseline set — calm controls |
| 1 | AI-vs-non-AI private-credit spread (BIS) | **6.2 vs 6.1pp — gap ~zero**, RE-CONFIRMED in BIS QR March 2026 ("lenders judge AI-related loans to be as risky as the average loan"). New adjacent color from the same QR: hyperscaler **CDS spreads rose, especially for lower-rated hyperscalers** (first differentiated pricing, at the CDS layer not loans); **BDC stocks −10% with NAV discounts deepening** Oct 2025-Feb 2026 (a private-credit stress proxy); SaaS direct loans $500B+/19% of the book sit adjacent to the AI exposure | Mar 2026 (BIS QR r_qt2603u/v; checked 2026-06-13) | ⚪ loans still gap-zero; CDS layer starting to differentiate — watch |
| 2 | CRWV unsecured 2031 yield vs HY index | ~11.5% reported vs HY 2.80pp — raw gap ~+8.7pp | ~Q1 2026 (secondary report; coupon 9.75% confirmed) | ⚪ **STALE >45d — needs manual FINRA/TRACE reading** |
| 3 | CRWV secured-vs-unsecured gap | ~340bp+ (SPV ~5.9% fixed vs unsecured) | Mar 2026 (8-K issue pricing) | ⚪ Baseline set |
| 4 | ORCL-vs-MSFT bond gap | (not yet read) | — | ⚪ Needs first manual reading |
| 5 | Latest new-issue pricing | CRWV DDTL 4.0 at SOFR+2.25% / ~5.9% fixed (A3) | Mar 31, 2026 (8-K) | ⚪ Baseline set |
| 6 | Rating actions | S&P CRWV outlook → POSITIVE (B+ affirmed); thresholds FFO/debt 12% / CFO/debt 10% | Apr 9, 2026 | 🟢 Improving, honestly noted |
| 7 | Primary-market behavior (new-issue concessions / failed takedowns) | None observed; GS desk clock says 12-18mo away, 2027 squeeze point; the "~Q1 2026 private-credit repricing" precursor is UNVERIFIED | Jun 12, 2026 (Tier 3, GS desk) | ⚪ The earliest-crack dial — currently quiet |

Status legend: ⚪ baseline/unread · 🟢 easing · 🟡 widening vs control · 🔴 gap open + confirmed at a second dial.

**Reading rule:** one dial widening = noise (could be general risk-off or single-name trouble). **The signal = the AI instruments widening while the Layer-1 control series stay calm, confirmed on a second dial.** Run `python3 scripts/spread_watch.py` for the Layer-1 pull + differential worksheet.

## The cycle-turn dashboard (this page is one dial of five)

The vault's full early-warning system for the AI capex cycle, one row per ending-type — this page owns row 1; the others live at their canonical homes (dashboard-not-duplicate):

| Ending it catches | Dial | Canonical home |
|---|---|---|
| **Financing-led** (credit reprices → builds stop) | the spread differential (this page) | here |
| **Voluntary-cut** (hyperscalers blink) | capex guidance + the "any two disconfirming signals = cycle turning" rule | [[hyperscaler-capex]] |
| **Demand-led** (consumer breaks first) | memory spot-vs-contract divergence | [[memory-shortage-winners-losers]] |
| **Counterparty-led** (a frontier lab stumbles) | AVGO backstop ceiling + drawn/impairment language | [[AI-buildout-who-holds-the-risk]] |
| **Any of the above** | the risk-register tripwires (Entries 5 + 6) | [[what-could-go-wrong]] |

**Two or more rows flashing together = the turn.** One alone = investigate, don't conclude.

## Change log

- **2026-06-13 (run #2 addendum):** Dial 7 added — primary-market behavior (new-issue concessions / failed takedowns), the historically-earliest crack, named with a 12-18-month clock + 2027 squeeze point by a GS rates-desk co-head (video-intel 2026-06-12, Tier 3); the "~Q1 2026 private-credit repricing" precursor logged as an unverified lead. Instrument-selection logic + ORCL-🟡 expansion trigger also documented (Vic question).
- **2026-06-13 (run #2, same day):** Layer-4 check (was due, Jan-2026 row): dial 1 updated from BIS QR March 2026 — loan-spread parity RE-CONFIRMED; new color: hyperscaler CDS rising (especially lower-rated — the first differentiated AI pricing, at the CDS layer), BDC −10%/NAV discounts deepening (private-credit stress proxy), SaaS $500B direct-loan adjacency. Controls unchanged (HY 2.80 / IG 0.75, 06-10). Dials 2/4 flagged stale — need manual FINRA readings.
- **2026-06-13 (S158):** Created per Vic request (standalone tracker; the spread-differential instrument from [[AI-buildout-who-holds-the-risk]] made operational). Four-layer instrument stack + six-dial readings table (baselines from BIS Bulletin 120, CRWV 8-K/S&P actions) + the five-dial cycle-turn dashboard. Companion script `scripts/spread_watch.py` added. Dials 2 and 4 await first manual FINRA/TRACE readings.
