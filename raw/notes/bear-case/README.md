# bear-case — the ranked per-stock risk map, discovery log

Output of the `/bear-case` skill. Each file is the **complete, ranked bear case for one stock** — what could go wrong, how real each risk is, and what to watch — by fusing the vault's structured risk homes (the `what-could-go-wrong` register, forward-edge-tracker, the company page's Risk-factors + Open-questions, chokepoint/theme pages, spread-watch) with `/latest-alpha` (timely 8-K/news) + `/last30days` (crowd narrative) + a reliable-source web pass. It is the **bottom-up dual** of the top-down `what-could-go-wrong` register, and productizes the vault's 4th discipline ("host tensions honestly") at the per-stock level.

**This is a Tier-3/4 discovery log, NOT vault canon.** Same status as `priced-in/`, `latest-alpha/`, and `video-intel/`:
- Not in `index.md` / `log.md`; these files do not count for accounting.
- **Honest-verdict / anti-doom is load-bearing:** every risk is graded for how *real* it is, overblown ones are marked overblown, and every report closes with "the steelman against this whole bear case." A run that finds catastrophe everywhere is a failed run.
- **Tier discipline:** a 10-K fact ≠ a Reddit panic. Canon (Tier 1/2) > latest-alpha (Tier 1-timely/3/4) > web (Tier 3/4) > last30days (Tier 4/5, sentiment-only). Every risk tier-tagged.
- **Ranked on gradable axes, never fake probabilities:** Severity × Evidence (FACT-today / SCENARIO / RUMOR) × Proximity. Each top risk carries a **tripwire** — the observable that tells you it's firing.
- **Describe-don't-recommend:** no buy/sell, no price targets, no position-revealing. Reframed as "what would have to be true for the thesis to break."
- Anything that should reach a `wiki/` page (a register entry for a new system-level risk) is a separate, **human-gated** action — the skill only flags candidates.

File naming: `<RUN_DATE>_<TICKER>_bear-case.md` (e.g. `2026-06-14_CRWV_bear-case.md`).
