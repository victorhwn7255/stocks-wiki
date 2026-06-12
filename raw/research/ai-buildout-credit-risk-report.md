# AI Build-out Credit Risk — verified research report (2026-06-13)

**Provenance:** multi-agent deep-research run (107 agents; 5 angles; 25 sources fetched; 125 claims extracted; top 25 adversarially verified 3-vote each → 24 confirmed / 1 refuted). Brief seeded with vault-primary context (AVGO $29B backstop, NVDA instruments, AMZN→Anthropic stack, CRWV debt, ORCL RPO, Meta/Alphabet SPV-VIE). **Tier status:** the BIS / IMF / FSB / S&P / SEC documents cited are primary official-sector and regulatory sources; Morgan Stanley figures are sell-side (Tier 3) even where relayed by official bodies; blogs were used for surfacing only. Anchor source for the planned theme page per Section 3.13 conventions.

## Verdict (as found, not assumed)

**The honest middle, tilted toward load-bearing at the margin.** The financing machinery is no longer a marginal wrapper: hyperscaler free cash flow has already fallen below capex (the regime flip), and roughly half of projected 2025-2028 AI capex must come from outside capital. But it is not yet a telecom-2000-scale leverage episode: the boom is ~1% of US GDP (half the dot-com rise), official bodies judge stability risk contained-but-conditional, and the average private-credit fund holds only ~5% AI exposure. The loss-bearers are now mappable, and the underwriting warning light is on.

## Confirmed findings (each verified 3-0)

### 1. The central sizing — half the build-out needs outside money
AI infrastructure capex 2025-2028 projected at **~$2.9T, of which ~$1.5T from external capital**: ~$800B private credit (asset-based finance the largest channel) + ~$200B investment-grade tech bonds + ~$150B data-center ABS/CMBS + ~$350B plug (sovereign/PE/VC/other). Source: Morgan Stanley (Jul-Aug 2025), relayed as baseline by the **FSB** (Report on Vulnerabilities in Private Credit, May 6, 2026, Graph 4.1, co-sourced Bank of England) and consistent with **IMF GFSR April 2026** (hyperscalers fund 70% of $3.4T through 2029; >$100B bonds raised since Jan 2025). Caveat: the granular split is one sell-side estimate; MS itself says the $1.5T is biased HIGHER if hyperscalers pull back capex (pushing more onto credit markets); FSB cites a higher McKinsey alternative ($5.2T by 2030).

### 2. The regime flip — free cash flow is now BELOW capex
**BIS Bulletin No. 120 (Jan 7, 2026), literally titled "from cash flows to debt":** the big-five payers (Alphabet, Amazon, Meta, Microsoft, Oracle) have seen "free cash flows... lag capital expenditures in absolute amounts." FSB: "internal cash flows from technology companies are proving insufficient." Corroboration: MUFG (Dec 2025) sees 2026 big-five capex of $660-690B consuming ~100% of operating cash flow vs a ~40% ten-year average; hyperscalers now hold more debt than cash for the first time (Janus Henderson). **The single strongest datapoint against the marginal-wrapper reading.**

### 3. Private credit — fast concentration in flow, modest in stock
Outstanding private credit to AI-related firms: **near zero → $200B+ (~8% of all private credit)**; ~$40B originated in 2025; BIS projects $300-600B by 2030. AI's share of private-credit **deal value hit 34% in 2025** (vs ~17% prior-5yr average). Counterweight: only ~20% of funds participate; AI is ~5% of the average fund's book. (BIS Bulletin 120 + FSB May 2026.) Definition caveat: "AI-related" uses broad PitchBook verticals.

### 4. The mispricing signal — the underwriting warning light
**Private-credit lenders price AI loans essentially identically to non-AI loans** — spreads 6.2 vs 6.1pp, maturities 4.7 vs 4.8 years, secured share 46% vs 48%; the difference stays insignificant after controlling for loan and borrower characteristics. BIS's own inference: "either lenders may be underestimating the risks of AI investments (just as their exposures are growing significantly) or equity markets may be overestimating the future cash flows AI could generate." **One of the two markets is wrong.** (BIS Bulletin 120, verbatim-verified.)

### 5. The system-scale counterweight (the marginal-wrapper case)
Data-center + IT-manufacturing investment ≈ **1% of US GDP** — similar to the mid-2010s shale boom, half the dot-com-era rise in IT investment; BIS calls macro/stability risks "moderate"; IMF finds investment-grade appetite "very healthy" and stability risks "contained." **Boundary (the killed claim):** the stronger assertion that the IMF verdict "directly supports the marginal-wrapper reading" was REFUTED 1-2 — both institutions condition the all-clear on AI firms meeting high earnings expectations, and note the post-dot-com investment contraction was the largest on record despite that boom also being small vs GDP. Note: total IT investment at ~5% of GDP now EXCEEDS the 2000 peak.

### 6. Circularity is quantified, not just alleged
**IMF staff: ~7pp of the ~12pp Sep-Dec 2025 return across the seven AI-circle firms** (Amazon, AMD, Alphabet, Intel, Microsoft, Nvidia, Oracle) **is attributable to correlation-reinforcement within the circular-financing circle — ~$40B of average market cap on a ~$2T base** — warning the circle "may simultaneously report inflated revenues, potentially detached from fundamentals" (GFSR Apr 2026, fn. 30). BIS: financing structures "might mask leverage by moving it off the balance sheet. Yet leverage does not disappear by being out of sight"; investor doubts about long-term data-center collateral value flagged.

### 7. Who eats the loss — the chain is traceable
(a) **Private-credit investors are first-loss** on the ~$800B channel; FSB names the triggers: a shortfall in electricity supply, or **data-center overcapacity** ("development outpaces demand for AI related services"). (b) Behind the funds: **insurers, sovereign wealth funds, pensions, endowments, high-net-worth retail** (Morgan Stanley). (c) Banks are not insulated: top-5 banks hold **63% of committed BDC lending** (FSB). (d) Securitization is real but niche: **$46B of data-center ABS/CMBS** issued since 2018 (record 2025), expected ~$150B by 2028; IMF warns a capex retrenchment + procyclical tightening exposes data-center lenders to refinancing risk (GFSR Box 1.3).

### 8. GPU-collateralized debt got an investment-grade blessing — the live test case
**CoreWeave DDTL 4.0 (March 31, 2026, 8-K Ex 99.1): $8.5B delayed-draw term loan rated A3 (Moody's) / A-low (DBRS) — the FIRST investment-grade-rated financing secured by GPU/HPC infrastructure + an associated customer contract.** Non-recourse; secured by substantially all assets of a single-purpose subsidiary (CoreWeave Compute Acquisition Co. VIII, LLC) + ONE customer contract (customer named only as "leading AI enterprise"; secondary reporting suggests Meta). Pricing SOFR+2.25% floating / ~5.9% fixed, March 2032 maturity; anchored by Blackstone Credit & Insurance. The ~340bp+ gap vs CRWV's 9.75%-coupon unsecured 2031 notes shows the market rates **the contract, not the company** — lenders' recovery rides one AI customer's payments plus GPU residual value.

### 9. Neocloud corporate credit — speculative-grade, explicit loss math, and (honestly) IMPROVING
S&P on CoreWeave: **B+ (May 19, 2025)**, unsecured notes rated B with **recovery rating 5 = 10-30% recovery (70-90% loss-given-default)**; 62% of 2024 revenue from Microsoft; 3 suppliers >76% of purchases; pre-registered triggers FFO/debt <12% or CFO/debt <10%. **April 9, 2026 update: outlook revised to POSITIVE** and B+ affirmed even as S&P-adjusted debt nearly tripled to ~$29.9B with a ~$7.2B 2025 FCF deficit — because backlog hit $66.8B and largest-customer backlog concentration fell 85% → ~35%. Upgrade conditional on remediating internal-control material weaknesses by end-2026 + FFO/debt >12%. These thresholds are ready-made quarterly early-warning instruments.

### 10. The depreciation stress test — the obsolescence tail quantified
**IMF GFSR Box 1.4:** hyperscalers' implied PP&E useful life ~7 years; GPUs "could face obsolescence within two years." A stylized **3-year useful-life scenario: aggregate EBIT margin −9pp+, hyperscaler debt $800B → $1T+, debt-weighted CDS spreads +~60bp** (vs a current 20-160bp range). IMF labels it "essentially a business risk... not an imminent financial stability risk" — but it is the quantified answer to "what if chips age faster than the books assume."

## What did NOT survive verification (honest gaps)

- **Part B (OpenAI/Anthropic committed-vs-raised funding-gap tables): NO surviving claims.** The commitment headlines circulating are largely unverifiable at primary; the theme page must scope this to vault-primary evidence only (AMZN 10-Q Anthropic stack; AVGO filings) and flag the lab-level gap as an open question.
- **Part D (Lucent/Nortel magnitudes + timeline): NO surviving claims** — the telecom-2000 comparison stays a named Tier-3 analogy (video-intel 2026-03-24), not verified history, until separately researched.
- **Blue Owl/Oracle $10B walk-away: unverified** (surfaced via CNBC/DataCenterDynamics in the source pool but no claim survived) — keep as Tier-4 watch item.
- **No verified instance yet of an AI financing structure failing, being drawn, impaired, or repriced** — the strongest honest point FOR the benign reading as of June 2026.
- Per-fund AI lending volumes at Apollo/Blackstone/Ares/KKR/Brookfield: unverified.

## Early-warning instruments (observable quarterly)

1. AVGO 10-Q backstop maximum-exposure restatement (next: Q3 FY2026, ~Sept 2026) — does $29B grow?
2. CRWV: S&P FFO/debt 12% + CFO/debt 10% thresholds; unsecured-vs-SPV spread gap; refinancing wall into 2030/2031 maturities.
3. BIS-style AI-vs-non-AI loan spread differential (currently ~zero = the warning light itself).
4. Data-center ABS/CMBS issuance pace vs the $150B-by-2028 path + any spread widening.
5. Depreciation-life changes in hyperscaler 10-Ks (the 7-year implied life vs 2-year obsolescence).
6. Lease-default / impairment / "drawn" language appearing in ANY filing (the what-could-go-wrong tripwires).
7. FSB's named triggers: electricity-supply shortfall; data-center vacancy/overcapacity data.

## Primary sources

- BIS Bulletin No. 120, "The AI boom: from cash flows to debt" (Jan 7, 2026) — bis.org/publ/bisbull120.pdf
- IMF Global Financial Stability Report, April 2026, Ch. 1 incl. Box 1.3 (securitization) + Box 1.4 (obsolescence scenario) — imf.org
- FSB, Report on Vulnerabilities in Private Credit (May 6, 2026) — fsb.org/uploads/P060526.pdf
- CoreWeave 8-K Ex 99.1, DDTL 4.0 (Mar 31, 2026) — sec.gov; CoreWeave IR release
- S&P Global Ratings, CoreWeave research updates (May 19, 2025; Apr 9, 2026)
- Morgan Stanley, "Credit Markets: AI financing gap" (Thoughts on the Market, Aug 2025) — sell-side, Tier 3
- Moody's commentary on hyperscaler lease-risk disclosure (via DataCenterDynamics; Tier 4 relay)
