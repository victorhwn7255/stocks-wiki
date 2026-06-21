# Quantitative Base-Rate Data Extraction: Mauboussin & Callahan's "The Base Rate Book" (Sales Growth) and Companion ROIC Persistence Work

## TL;DR
- The September 26, 2016 "Base Rate Book" (Credit Suisse Global Financial Strategies) sales-growth chapter (pp. 19–32) publishes a full-universe distribution (Exhibits 2–3, p. 22) with a 3-year mean CAGR of 8.1%, median 5.4%, and standard deviation 18.7%, plus an 11-size-bucket × 4-horizon grid (Exhibit 4, pp. 24–25) showing high growth becomes vanishingly rare as starting revenue rises.
- Sales growth is weakly persistent: the one-year autocorrelation is r = 0.30, falling to 0.17 (3-yr) and 0.19 (5-yr) (Exhibits 8–9, pp. 28–29); ROIC/CFROI is far more persistent, with the companion "Competitive Advantage Period" report (April 14, 2026) reporting an average sector persistence factor of 0.79 and average fade of 0.21 (Exhibit 11).
- The summary statistics and a small set of headline "no company achieved this" figures ARE directly published and extractable; the full cell-by-cell distribution grids (44 reference classes in Exhibit 4) are proprietary and should be stored/looked up programmatically rather than transcribed wholesale.

## Key Findings

**Sources confirmed and read directly.** I located and read the full PDF of "The Base Rate Book: Integrating the Past to Better Anticipate the Future," Michael J. Mauboussin, Dan Callahan, and Darius Majd, Credit Suisse Global Financial Strategies, dated **September 26, 2016** (the user's "September 2016"; the cover date is Sep 26, not Sep 4). The Sales Growth chapter runs pp. 19–32. I also read the CFROI persistence section (pp. 12–17), the companion Counterpoint Global / Morgan Stanley "Competitive Advantage Period: The Neglected Value Driver" (Consilient Observer, April 14, 2026), "Bayes and Base Rates" (Consilient Observer, February 10, 2026), and "Measuring the Moat" (2024), plus corroborating secondary literature.

### 1. Sample definition (directly stated, p. 21)
- Universe: "the top 1,000 global companies by market capitalization since 1950." Represents "roughly 60 percent of the global market capitalization and includes all sectors."
- Includes dead companies (mergers/acquisitions the main cause of disappearance).
- Horizons: CAGR of sales computed for 1, 3, 5, and 10 years per firm.
- All figures inflation-adjusted to 2015 dollars.
- Total observations (Exhibit 2 / appendix, pp. 22, 31–32): 1-Yr 56,883; 3-Yr 53,266; 5-Yr 49,874; 10-Yr 41,645.
- Modest survivorship bias acknowledged (p. 23): a 10-year sample firm had to survive 10 years; "about one-half of all public companies cease to exist within ten years of being listed." (The underlying mortality finding the book draws on is Daepp, Hamilton, West & Bettencourt, "The mortality of companies," *Journal of the Royal Society Interface*, Vol. 12, No. 106, April 1, 2015: "the typical half-life of a publicly traded company is about a decade, regardless of business sector.")

### 2. Unconditional (full-universe) sales-growth distribution — Exhibits 2 and 3 (p. 22)
Summary statistics by horizon (full universe, directly published):

| Statistic | 1-Yr | 3-Yr | 5-Yr | 10-Yr |
|---|---|---|---|---|
| Mean | 14.8% | 8.1% | 6.9% | 5.8% |
| Median | 5.8% | 5.4% | 5.2% | 4.9% |
| Std Dev | 275.2% | 18.7% | 12.3% | 8.0% |

The 1-year standard deviation of 275.2% reflects extreme small-base/outlier effects; the multi-year figures are the usable ones. The book notes the distribution is "skewed to the right," so the median is the better central indicator (p. 22).

Selected directly-quoted band frequencies (full universe; the numbers the book itself walks through):
- 15–20% CAGR over 3 years: **6.7%** of companies (the worked example on p. 21: 3,589 of 53,266 instances).
- The ">45%" band collapses with horizon: **5.5% (1-Yr) → 2.5% (3-Yr) → 1.3% (5-Yr) → 0.3% (10-Yr)**.
- The modal "0–5%" band rises with horizon: **20.6% → 25.2% → 28.8% → 34.2%** (1/3/5/10-Yr).
- "5–10%" band: **17.8% / 21.3% / 24.2% / 28.3%**.
- "10–15%" band: 11.4% / 12.3% / 12.6% / 11.6%.
- "20–25%" band: 4.5% / 3.9% / 3.1% / 2.0%.
- "30–35%" band: 2.0% / 1.5% / 1.0% / 0.6%.
- **23% of companies had negative real sales growth over 3 years, and 20% shrank over 5 years** (pp. 26–27).

### 3. Size-conditioned distribution — Exhibit 4 (pp. 24–25)
The book sorts the universe into deciles by prior-year sales, plus added analyses of mega (>$50B) companies — "44 reference classes (11 size ranges times 4 time horizons)" (p. 26). The 11 size ranges (in 2015 USD) are:
$0–325M; $325–700M; $700–1,250M; $1,250–2,000M; $2,000–3,000M; $3,000–4,500M; $4,500–7,000M; $7,000–12,000M; $12,000–25,000M; >$25,000M; and >$50,000M (mega).

Central finding (directly stated, p. 26): "as firm size increases the mean and median growth rates decline, as does the standard deviation of the growth rates."

Mean / Median / Std Dev of 3-year CAGR by size bucket (directly published in Exhibit 4 headers, pp. 24–25):

| Starting sales | Mean (3-Yr) | Median (3-Yr) | Std Dev (3-Yr) |
|---|---|---|---|
| $0–325M | 21.2% | 11.7% | 40.0% |
| $325–700M | 10.7% | 7.5% | 15.9% |
| $700–1,250M | 9.2% | 6.8% | 13.5% |
| $1,250–2,000M | 8.6% | 6.2% | 14.0% |
| $2,000–3,000M | 7.2% | 5.4% | 12.1% |
| $3,000–4,500M | 6.4% | 5.0% | 11.1% |
| $4,500–7,000M | 5.7% | 4.4% | 11.6% |
| $7,000–12,000M | 4.7% | 3.7% | 10.9% |
| $12,000–25,000M | 3.8% | 3.0% | 12.3% |
| >$25,000M | 2.4% | 2.2% | 10.9% |
| >$50,000M (mega) | 1.2% | 1.5% | 10.3% |

Headline size × band × horizon facts directly walked through in the book:
- Smallest decile ($0–325M): even at 10 years, **2.1%** of firms sustained >45% CAGR; the ">45%" 1-year rate is 15.1%.
- **Tesla worked example (p. 23):** assessing Elon Musk's Feb 2015 earnings-call goal to reach "a market capitalization of about $700 billion in 10 years" (approaching Apple's then-largest-in-the-world cap) implied by ~50% annual sales growth from a ~$6B base — for the $4.5–7B reference class, **NO company sustained >45% CAGR over 10 years**; you have to drop to the 30–35% band to find any, and even there it is "only one-fifth of 1 percent of the sample" (~0.2%).
- **Mega (>$50B):** the ">45%" 10-year rate is 0.0%; the 30–35% 10-year rate is 0.0%; even 20–25% over 10 years is 0.0%. Mega-cap 10-year growth is overwhelmingly concentrated in the 0–5% (37.8%) and 5–10% (17.2%) bands.

### 4. Persistence / mean-reversion of sales growth — Exhibits 8–9 (pp. 28–29)
- **One-year sales-growth autocorrelation: r = 0.30** (top 1,000 global companies, 1950–2015, ~55,000 company-years, inflation-adjusted, winsorized at 2nd/98th percentiles).
- **Correlation by horizon: 0.30 (1-Yr), 0.17 (3-Yr), 0.19 (5-Yr).**
- Interpretation (directly stated, p. 28–29): low correlation ⇒ rapid regression to the mean; "the median growth rate should receive the majority of the weight for forecasts of three years or longer."
- Sales growth ↔ Total Shareholder Return (Exhibit 7, p. 27): **r = 0.20 (1-Yr), 0.25 (3-Yr), 0.28 (5-Yr)**; period 1985–2015.
- Sales growth ↔ GDP (Exhibit 6, p. 26): U.S. real GDP vs. median sales growth, **r = 0.66**; U.S. real GDP grew 3.2%/yr (SD 2.4%), 1950–2015.

### 5. ROIC / CFROI persistence and fade (companion work)

**Within the Base Rate Book itself (CFROI section, pp. 12–16):**
- Four-year CFROI correlation by sector (Exhibit 8, p. 14): Consumer Staples **0.78**, Consumer Discretionary 0.67, Health Care 0.64, Industrials 0.62, Utilities 0.57, Telecom 0.55, Information Technology 0.50, Financials 0.43, Materials 0.41, Energy **0.35** (range of standard deviations 0.04–0.14).
- One-year CFROI correlation (Exhibit 7, p. 13): Consumer Staples **0.89**, Energy **0.64**.
- The book stresses one-year correlations overstate the fade rate (a one-year r of 0.89 compounds to 0.63 over four years, but the observed four-year r is 0.78).
- Mean CFROI levels (p. 16): Consumer Staples 9.3% (SD 0.6%); Energy 4.9% (SD 1.7%), 1983–2015.

**"Competitive Advantage Period: The Neglected Value Driver" (Counterpoint Global / Morgan Stanley, April 14, 2026):**
- **Average persistence factor across sectors: 0.79, ranging 0.70 to 0.90** (Exhibit 11). These imply **fade rates of 0.10 to 0.30, averaging 0.21**.
- **Five-year ROIC correlation coefficients by decade (Exhibit 12): 0.45 (1970s) → 0.39 (1980s) → 0.31 (1990s) → 0.38 (2000s) → 0.37 (2010s).** Persistence dropped through the end of the 20th century (rising competition) then rebounded in the 21st.
- One-year correlations overstate fade: e.g., consumer discretionary one-year r of ~0.725 would imply a 5-year r of ~0.19, but the observed 5-year r is 0.37.
- Recommended practice: use five-year correlations as the basis for the fade rate (fade = 1 − persistence factor); large companies have had consistently higher persistence than small ones since the mid-1980s (Exhibit 13). Implied competitive-advantage period for most U.S. companies is in the 5–20 year range.

**Older ROIC quintile-persistence work (Mauboussin, "Death, Taxes, and Reversion to the Mean," December 2007; "Measuring the Moat"):**
- ~**41%** of firms starting in the top ROIC quintile were still top-quintile after ~9–10 years; ~**64%** remained in the top two quintiles; roughly three-in-four did not fall to the bottom two quintiles after 10 years.
- Heavy churn in between: fewer than half of the 41% stayed top-quintile every year, so under ~4% of the total sample stayed continuously top-quintile.

### 6. Companion Counterpoint Global sales-growth updates
The framework has been refreshed using **U.S. public companies, 1950–2024** (Counterpoint Global; Compustat; FactSet). In "Bayes and Base Rates" (Consilient Observer, February 10, 2026), updated 5-year size-bucket statistics include:
- **$2–5B starting sales (Exhibit 3): 18,897 firm-period observations (2,229 unique companies); mean 5-yr CAGR 7.0%, std dev 10.6%.** "No public company has grown this fast for five years in the last three-quarters of a century" relative to the forecast assessed.
- **$8–12B starting sales (Exhibit 5): ~4,385 firm-period observations; mean 5-yr CAGR 5.7%, std dev 9.6%.**
- This update reports mean and standard deviation by bucket but **does not publish medians**. High-growth tails are extremely thin: per endnote, only "one-tenth of one percent of companies grow at a compound annual rate of 55–60 percent" in the realized data.
- These reports assess (without endorsing) aggressive company projections against the base rates. Examples: OpenAI's projection of $145B 2029 revenue from $3.7B in 2024 = a **108% 5-year CAGR**, and a rolled-forward $200B-by-2030 figure = **72.7% CAGR** (no company with starting sales ≥$6.5B across "more than 16,400 firm-periods from 1950 to 2024" ever achieved it); Oracle Cloud's ~75% CAGR target (no company with sales ≥$5.6B achieved it). For external context, OpenAI subsequently reported $13.1B of 2025 revenue and projected 2030 revenue "more than $280 billion" (CNBC, Feb 20, 2026); Oracle's CEO guided OCI revenue to $144B by FY2030 (Oracle, Sept 2025). All such projections are management forecasts, explicitly speculative.

### The book's own stated cautions
- Base rates are an "outside view" to be blended with the "inside view," not a deterministic forecast; "companies will fill the tails of the distribution" (p. 29).
- Distributions are inflation-adjusted, whereas most analyst forecasts include inflation — adjust before comparing (p. 26).
- Reference-class outcomes can change over time (non-stationary but stable enough to be useful).
- Survivorship and selection biases are present (only survivors populate longer horizons; fast-growers self-select into public listing, p. 26).
- Getting the reference class right (correct size bucket and horizon) is "crucial" (p. 23).

## Details

**What IS directly published / extractable (high confidence):**
- All summary statistics (mean, median, std dev) for the full universe by horizon (Exhibits 2–3, p. 22).
- All mean/median/std dev by size bucket for each horizon (Exhibit 4 headers, pp. 24–25).
- The full-universe band frequencies in Exhibit 2 (p. 22) and observation counts in the appendix (pp. 31–32).
- Correlation coefficients (sales autocorrelation, sales–TSR, sales–GDP, CFROI by sector).
- The decade-by-decade ROIC five-year correlations and persistence/fade summary from the CAP report (Exhibits 11–12).

**What is NOT individually published as quotable headline figures (store/look up, do not transcribe wholesale):**
- The complete cell-by-cell percentage grid for each of the 44 size × horizon reference classes in Exhibit 4 (every CAGR band × every size bucket × every horizon). Individual cells exist in the published exhibit, but reproducing the entire grid verbatim would copy a proprietary copyrighted table. A software lookup tool should store these as a structured dataset and surface single cells on demand.
- Interpolated values between bands or between size buckets are NOT in the source — any such figure must be flagged as an estimate, not a stated value.

## Recommendations
1. **Build the lookup as a keyed dataset, not a reproduced table.** Key on (size bucket, CAGR band, horizon) → frequency, plus (size bucket, horizon) → {mean, median, std dev}. Populate the conditional grid from Exhibit 4 (pp. 24–25) and the unconditional one from Exhibit 2 (p. 22). Surface one cell per query rather than displaying the full grid.
2. **Default to the median, not the mean,** for point forecasts, because the distribution is right-skewed (book's guidance, p. 22). Show the std dev to convey dispersion.
3. **Always inflation-adjust the user's forecast** (subtract expected inflation) before mapping onto these 2015-dollar base rates; otherwise the tool will understate how aggressive a nominal forecast is.
4. **Weight toward the base rate for horizons ≥3 years,** given sales-growth correlations of 0.17–0.19; for 1-year forecasts allow more inside-view weight (r = 0.30 is still low).
5. **For ROIC/margin durability, use a fade model:** start from sector four-year CFROI r (Exhibit 8, p. 14) or the CAP report's persistence factors (avg 0.79, fade 0.21), and let large-cap status raise persistence.
6. **Flag interpolated vs. stated values explicitly** in the UI, and cite exhibit + page for every stated figure.
7. **Threshold that changes the recommendation:** if a user's forecast lands beyond the highest populated band for the relevant size bucket/horizon (e.g., any >45% 10-year claim for a multi-billion-dollar starting base), surface the "zero or near-zero historical base rate" warning, mirroring the Tesla/OpenAI/Oracle examples.

## Caveats
- The cover date is September 26, 2016, not September 4. The standalone "Sales Growth" module the user also referenced (March 4, 2015 / Feb 23, 2016) used the **S&P 1500, 1994–2014** (~23,914 3-yr observations) with a slightly different worked example (20–25% band over 3 years = 4.4%). The consolidated 2016 book uses the **top-1,000-global, 1950–2015** universe. Figures differ between the two; this report uses the consolidated 2016 book as the primary source and notes the 2015 module where relevant.
- The Counterpoint "Bayes and Base Rates" update is dated **February 10, 2026** (not 2025) and uses a U.S. 1950–2024 universe; its buckets report mean and std dev but not medians.
- Quintile-persistence percentages (41%, 64%) come from Mauboussin's 2007 work and "Measuring the Moat," not the 2016 Base Rate Book; cite accordingly.
- All company growth projections discussed in the updates (OpenAI, Oracle, Tesla) are company/management forecasts whose plausibility is being assessed against base rates — they are not predictions endorsed by the authors.
- Respect copyright: extract summary statistics and the specific figures the authors themselves quote; do not republish entire proprietary exhibits.