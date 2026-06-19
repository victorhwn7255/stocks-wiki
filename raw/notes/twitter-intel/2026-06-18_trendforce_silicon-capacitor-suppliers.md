# Silicon Capacitor Suppliers — TrendForce infographic (Tier-5 capture)

**Source-tier verdict (gates everything): Tier 5 (social/staged-image) — signal for generating questions; NEVER cited as vault fact.**
This is a TrendForce-attributed infographic ("Key Suppliers in the Silicon Capacitor Market," data compiled by TrendForce, June 2026), staged as an image at `raw/notes/twitter-notes/major-silicon-capacitor-suppliers.jpg` (staged 2026-06-18). It is a single infographic, **not a thread** — no author handle, no engagement counts, no URL. The underlying TrendForce compilation would be ~Tier 3 if pulled from TrendForce directly; **as captured here (screenshot, no provenance) it is discovery-only** — verify every name/claim at primary before any page use. It is an *independent market-research* map (not a ticker pump / not aligned-commercial-incentive), but **qualitative-only — no shares, no TAM, no pricing, no AI-mix numbers.**

## TL;DR
Silicon capacitors — a silicon-process alternative/complement to ceramic MLCC for **chip-adjacent power decoupling** — are an emerging node in the AI power-delivery stack. The supplier map: **SEMCO + Murata** (both already MLCC-oligopoly leaders) plus specialists **AP Memory** (the most AI/HPC-pure), **ROHM** (consumer/IoT-tilted), and **Launchip** (China; PDN/RF). The on-thesis signal: the same full-stack passive owners (SEMCO, Murata) are positioning across BOTH ceramic and silicon caps — which **reinforces, rather than threatens**, the concentration thesis in [[MLCC-oligopoly]]'s "move the cap next to the chip" direction. AP Memory is the one genuinely new name worth watching.

## What a silicon capacitor is (and why it's on-thesis)
Silicon capacitors are capacitors built in a **silicon (semiconductor) process** — trench/3D structures — rather than stacked ceramic. They offer very high frequency/density, ultra-thin profiles, and can be placed **land-side/top-side immediately next to the die, or embedded in the package substrate**. That is the same "decoupling cap must sit microseconds from the GPU" job the [[MLCC-oligopoly]] page describes — silicon caps are the **premium, chip-adjacent edge** of that function (where ceramic MLCC physically can't go). They are a **complement today, not a wholesale MLCC replacement.**

## Named entities
| Supplier | Ticker (inferred — verify) | Claim (per infographic) | Vault page? | Vault context |
|---|---|---|---|---|
| SEMCO (Samsung Electro-Mechanics) | 009150 KS | Silicon cap; top-side/land-side/embedded architectures; AI server, AP, ADAS | No (plain-text in [[MLCC-oligopoly]]) | MLCC "scale attacker"; now also silicon cap |
| Murata | 6981 JP | High-frequency, high-density silicon caps; optical/networking, RFPA, auto, medical | No (1st-ingest candidate in [[MLCC-oligopoly]]) | Full-stack MLCC owner; silicon cap via IPDiA heritage |
| AP Memory | 6531 TT | S-SiCap, discrete silicon caps, silicon-cap IPC; **AI/HPC, advanced packaging, SoC integration, GPU/ASIC peripherals** | No | **NEW name** — most AI/HPC-pure of the list |
| ROHM | 6963 JP | Miniature silicon caps + built-in TVS diode; smartphones, wearables, IoT, optical modules | No (in [[MLCC-oligopoly]] resistor share) | Consumer/IoT-tilted; weak AI-datacenter fit |
| Launchip | private / China | High-cap / HF / UHF / HV silicon caps; RF bypass, filtering, PDN, industrial | No | China silicon-cap specialist; PDN/RF tilt |

## Key claims (tagged)
- Silicon-cap suppliers span Korea (SEMCO), Japan (Murata, ROHM), Taiwan (AP Memory), China (Launchip). `[verifiable]` (supplier/product-line existence at company sites/filings) · `[opinion]` (the "key suppliers" curation is TrendForce's).
- SEMCO offers **top-side/land-side/embedded** silicon-cap architectures for **AI server**. `[verifiable]` at SEMCO disclosures.
- Murata's silicon caps target **optical/networking + RFPA**, not primarily AI-server decoupling. `[verifiable]`.
- **AP Memory's silicon caps explicitly target AI/HPC + advanced packaging + GPU/ASIC peripherals** — the most AI-datacenter-direct of the five. `[verifiable]` at AP Memory (6531 TT) filings.
- No share / TAM / pricing / AI-mix data given. `[opinion/map-only]`.

## Vault cross-reference
- **[[MLCC-oligopoly]]** — directly relevant to the page's "embedded-MLCC trend (the most chokepoint-like direction)" section. Silicon caps are a **competing technology base** for the chip-adjacent/embedded decoupling job. Two readings, both to verify at primary: (a) **substitution-tail RISK** — silicon caps erode the top-bin MLCC kernel at the highest-frequency/embedded edge; (b) **reinforcement** — the SAME owners (SEMCO, Murata) hold both, so the concentration thesis survives a technology shift. The infographic supports (b) over (a). **REFINES** (adds a competing-technology dimension); does not challenge the quality-but-cyclical verdict.
- **[[pcb-interconnect-substrate-chokepoint]]** — "embedded" silicon caps sit in the package substrate (Layer 3 / advanced packaging) — light adjacency to the substrate node.
- **Power-delivery / 800V-HVDC / PDN** thread — silicon caps are part of the chip-level power-delivery network the vault tracks around [[power-semis]] + the NVDA 800V transition. No dedicated PDN page; adjacency noted only.
- **Murata first-ingest pick STRENGTHENED** — Murata doing both ceramic *and* silicon caps reinforces the "full-stack passive owner" rationale for making it the [[MLCC-oligopoly]] first primary ingest.

## Ingest leads (the payoff — primary-source-verifiable)
1. **Murata ingest (already the pre-registered MLCC first ingest):** add a check for its **silicon-capacitor line** (IPDiA-derived) — does it disclose silicon-cap revenue / AI exposure? Would strengthen the "full-stack passive owner" case (MLCC + silicon cap under one roof). Verify at Murata FY2026 securities report + earnings materials.
2. **SEMCO (009150 KS):** verify the "top-side/land-side/embedded silicon cap for AI server" claim when the third MLCC ingest (SEMCO) is run.
3. **AP Memory (6531 TT) — NEW-NAME CANDIDATE:** the most AI/HPC-pure silicon-cap play (AI/HPC + advanced packaging + GPU/ASIC peripherals). Verify silicon-cap revenue mix + advanced-packaging exposure at its TWSE filings. **Does NOT yet meet the 3-source / chokepoint-central page-creation threshold** (single Tier-5 source) — flag and watch; promote only if it recurs in 2+ more (primary/Tier-3) sources or proves chokepoint-central.
4. **The competing-technology question for [[MLCC-oligopoly]]:** does silicon cap take share of the chip-adjacent decoupling job (substitution-tail erosion of the top-bin MLCC kernel), or do the incumbents own both? Resolve via **primary** product roadmaps (Murata / SEMCO / TDK / Taiyo Yuden) + teardown evidence — NOT from this infographic.

## Contradictions / red flags
- **Qualitative-only:** no shares, TAM, pricing, or AI-mix numbers — low checkable substance; a supplier map, not a thesis.
- **"Not an exhaustive list"** (TrendForce's own caveat): absence ≠ non-participation (e.g., TDK, Taiyo Yuden, legacy IPDiA, Empower Semiconductor, and others not shown).
- **Capture provenance unknown:** staged as an image with no author/URL; TrendForce branding present but unverified as to where it was lifted from. The Tier-5 floor holds.
- **Don't overstate substitution:** silicon caps are a premium complement at the highest-frequency/embedded edge, not a wholesale MLCC replacement; the [[MLCC-oligopoly]] quality-but-cyclical verdict is unaffected.

## Source-tier verdict (restated)
**Tier 5 — do not cite as vault fact; use to generate questions; verify against primary sources before any page edit.** Discovery-only run: nothing in `wiki/`, `index.md`, `log.md`, or the human-owned anchors was touched.

---

## Thread (Tier 5 — not a primary source)
TrendForce infographic — "Key Suppliers in the Silicon Capacitor Market" (data compiled by TrendForce, June 2026). Transcribed table:

| Supplier | Product and Technology Focus | Applications |
|---|---|---|
| SEMCO | Silicon capacitor, top-side/land-side/embedded architectures | AI server, AP, ADAS |
| Murata | High-frequency, high-density silicon capacitors | Optical/networking, RFPA, automotive, medical applications |
| AP Memory | S-SiCap, discrete silicon capacitors, silicon-capacitor IPC | AI/HPC, advanced packaging, SoC integration, GPU/ASIC peripherals |
| ROHM | BTD1RVFL miniature silicon capacitors with built-in TVS diode | Smartphones, wearables, small IoT devices, optical modules, high-frequency communications |
| Launchip | High-capacitance, high-frequency, ultra-high-frequency, high-voltage silicon capacitors | RF bypass, filtering, tuning, PDN, communications and industrial control |

Note (verbatim): "Not an exhaustive list of suppliers. Source: data compiled by TrendForce, June 2026."
