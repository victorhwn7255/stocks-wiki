# priced-in — what's priced in vs. not, discovery log

Output of the `/priced-in` skill. Each file answers two questions for one stock — **what is already priced in** vs. **what is not yet priced in** — by fusing vault canon + `/latest-alpha` (60-day events) + `/last30days` (crowd narrative), through the forward-edge lens ([[forward-edge-tracker]] / CLAUDE.md §3.18).

**This is a Tier-3/4 discovery log, NOT vault canon.** Same status as `latest-alpha/` and `video-intel/`:
- Not in `index.md` / `log.md`; these files do not count for accounting.
- "Priced in" is judged by **narrative saturation, not valuation math** — an honest *proxy*, not a measurement. No stock price / market cap / multiples / price targets appear, by design.
- The "not priced in" half always splits into **upside AND risk** (describe-don't-recommend; honest-verdict — not a bull-thesis generator).
- Anything that should reach a `wiki/` page (a canon update, or a forward-edge-tracker entry) is a separate, **human-gated** action — the skill only flags candidates.

File naming: `<RUN_DATE>_<TICKER>_priced-in.md` (e.g. `2026-06-09_AAOI_priced-in.md`).
