---
name: spread-watch
description: Refresh the AI credit spread tracker (wiki/trackers/AI-credit-spread-watch.md) — the dial for whether AI-related borrowers pay more than comparable ordinary borrowers, the earliest observable signal of a financing-led AI capex cycle turn. Pulls FRED HY/IG controls via scripts/spread_watch.py, checks the manual AI-instrument dials, applies the binding reading rule, and updates that ONE tracker page (flag — never edit — any other page). Use on /spread-watch or asks like "check the spreads", "how's AI credit", "has the credit market blinked", "update the spread watch"; optional pasted yields, e.g. "/spread-watch crwv 11.2 orcl 5.6 msft 4.9".
---

# spread-watch — refresh the AI credit spread tracker

This skill refreshes `wiki/trackers/AI-credit-spread-watch.md` — the vault's instrument for the gap between what AI-related borrowers pay and what ordinary, comparable borrowers pay, the earliest observable signal of the AI capex cycle's financing-led ending. It runs the data pull, applies the reading rule, updates the readings table with dated entries, and cross-checks the five-dial cycle-turn dashboard.

## The hard boundary

This skill edits exactly ONE vault page: `wiki/trackers/AI-credit-spread-watch.md` (readings table + its change log + frontmatter `last_updated`), plus that page's row date in `index.md`. It MUST NOT edit any other wiki page, any theme, the risk register, or any company page — if a reading implies another page should change (e.g., a tripwire fires at [[what-could-go-wrong]]), FLAG it in chat for a follow-up action; do not cascade. Describe-don't-recommend: dial readings and status colors, never buy/sell.

## When to invoke

- `/spread-watch` or any ask like "check the spreads," "how's AI credit," "run the spread tracker," "has the credit market blinked," "update the spread watch."
- Before/within a refresh session touching AVGO / CRWV / NBIS / ORCL or any AI-financing event (the §3.20 freshness obligation: touched signal → same-session status update).
- Optional args: pasted manual yields, e.g. `/spread-watch crwv 11.2 orcl 5.6 msft 4.9`.

## Steps

### 1 — Layer 1 (automatic): run the script

```bash
python3 scripts/spread_watch.py            # controls only
python3 scripts/spread_watch.py --crwv X --orcl Y --msft Z   # with pasted manual dials
```

Pulls FRED HY (`BAMLH0A0HYM2`) + IG (`BAMLC0A0CM`) OAS with 1m/3m trends (curl fallback built in). If the fetch fails twice, record "fetch failed" with date — never invent a number.

### 2 — Layer 2 (manual dials): check staleness, use what's given

Read the tracker's readings table. For dials 2 (CRWV 2031 unsecured yield) and 4 (ORCL-vs-MSFT gap): if the user passed values, use them; if the as-of date is >45 days old and no values were given, do NOT guess — mark the row "stale, needs manual FINRA/TRACE reading" and tell the user exactly where to look (finra-markets.morningstar.com bond search, or a brokerage bond screen).

### 3 — Layer 3 (deal pricing): sweep recent vault artifacts

Grep `raw/notes/latest-alpha/` notes and the change logs of [[AVGO]] [[CRWV]] [[NBIS]] [[ORCL]] for financing events since the tracker's `last_updated` (new facility, notes issuance, tranche, rating action). Any disclosed rate becomes a dial-5 update; any rating action becomes dial 6.

### 4 — Layer 4 (the referees, quarterly cadence): only if due

If the BIS/IMF/FSB row is >80 days old, run ONE WebSearch pass for new publications (BIS Quarterly Review / Bulletin AI-lending update; IMF GFSR chapter; FSB private-credit report). Update dial 1 only from these official-sector documents — never from news characterizations of them.

### 5 — Update the tracker page

- Rewrite changed rows in the readings table: new reading + as-of date + status color per the legend (⚪ baseline/unread · 🟢 easing · 🟡 widening vs control · 🔴 gap open + confirmed on a second dial).
- **The reading rule is binding:** 🟡 requires an AI instrument widening while the Layer-1 controls are calm; 🔴 additionally requires confirmation on a second dial. General risk-off (controls widening too) is NOT an AI signal — say so explicitly.
- One-sentence change-log entry; bump frontmatter `last_updated`; sync the page's `index.md` Trackers-row date.

### 6 — Report (chat, plain language; FIXED five-section template)

```
## Spread Watch — <date> (run #N)

### Readings
| # | Dial | Now | Prior (last run) | Change | 3-mo trend | Status |
(every dial, every run — including unchanged ones; "prior" = the last logged reading)

### What moved, and how fast
(the changes + the RATE of change — pp/month, and whether it is accelerating;
 always state the control-group comparison: did the AI dials move MORE than the
 FRED controls? That is the is-it-AI-specific test.)

### What it means (plain language)
(2-4 sentences max. Calm is a valid and complete answer. If a status color
 changed, the why in one sentence each.)

### Cycle-turn cross-check: N of 5 dashboard dials flashing
(one line per flashing dial with its home page; if N >= 2, say
 "THE TURN SIGNAL IS LIVE" prominently and flag — never edit — affected pages.)

### Actions
- Operational: (what this run updated/flagged)
- For you to fetch: (stale manual dials + exactly where to read them)
- Watch next: (dated upcoming checkpoints — next 10-Q, next BIS/IMF release)
```

**"Actions" boundary (binding):** operational / fetch / watch-next ONLY. Never buy/sell/trim/hedge language — describe-don't-recommend holds even when the turn signal is live; the skill's job is that the user cannot miss the signal, not to act on it.

## Disciplines

- Honest-verdict: if everything is calm, say "calm" — a tracker that manufactures urgency is broken. The current baseline (controls historically tight, AI gap ~zero) IS the finding until something moves.
- Every reading carries its as-of date; the blind spot is stated when relevant (private credit marks slowly — calm public proxies ≠ all-clear on the $800B private channel).
- Tier discipline: FRED/TRACE/8-K/rating-agency = usable; news characterizations of spreads = Tier 4, verify against the instrument.
- No P&L, no positions, no price targets.

## What this skill is NOT

- Not a portfolio or price tracker — credit instruments only.
- Not a license to edit other pages (flag, don't cascade).
- Not a forecast machine — it reports the fuel gauge; interpretation beyond the reading rule belongs to the analysis pages ([[AI-buildout-who-holds-the-risk]]).
