# AI datacenter photonics supply chain

**Research date:** 2026-04-26  
**Scope:** AI datacenter optical I/O, not the full telecom optical-networking market.  
**Core framing:** 800G / 1.6T pluggable transceivers and CPO optical engines are the two main packaging architectures for AI datacenter optical I/O. They are not the whole supply chain. The real bottlenecks sit underneath: lasers, modulators, optical DSP / SerDes, photonic foundries, fiber attach, manufacturing / packaging / test, thermal integration, and eventually optical circuit switching.

**High-level conclusion:** the AI photonics stack is moving through three overlapping phases.

| Phase | Architecture | Why it exists | Main bottleneck | Investable interpretation |
|---|---|---|---|---|
| 2024-2027 volume ramp | 800G / 1.6T pluggable transceivers | Fastest deployable path using front-panel modules, existing switch chassis, and mature service models | 200G/lane lasers, DSP power, module yield, fiber attach, test throughput | Best near-term revenue capture sits with optical modules, laser chips, DSPs, contract manufacturing, test equipment, and high-density connectors. |
| 2025-2028 early CPO | CPO optical engines in switches | Reduces electrical trace length, front-panel density pressure, and optical interconnect power | optical-engine reliability, ELS standardization, fiber attach, thermal isolation, field serviceability | CPO is a platform shift led by switch/NIC vendors and vertically integrated AI systems; supplier value shifts toward silicon photonics engines, ELS lasers, advanced packaging, and connectors. |
| 2026+ network redesign | OCS + photonic fabrics + optical I/O | Avoids repeated optical-electrical-optical conversion and enables reconfigurable AI fabrics | control software, switch reliability, workload scheduling, photonic MEMS / LCOS / WSS manufacturing | OCS is less mature as a broad merchant market but is strategically important because Google and OCP are validating the architecture for AI networks. |

**Important distinction:** pluggables and CPO are packaging architectures. Lasers, modulators, DSPs, foundries, fiber attach, assembly/test, and thermal are bottleneck layers. Owning the architecture is not the same as owning the bottleneck. A module vendor may win near-term revenue; a laser supplier may own scarcity; a switch ASIC vendor may control system architecture; a photonic foundry may become the scaling gate if CPO adoption accelerates.

**Source-quality note:** this report prioritizes official company releases, standards organizations, and primary technical bodies. Industry research, trade press, and analyst commentary are used only where primary sources do not disclose enough detail.

## Near-term architecture: 800G / 1.6T pluggable transceivers

800G and 1.6T pluggables are the near-term workhorse for AI scale-out networks. They plug into front-panel cages on Ethernet / InfiniBand switches and connect GPU racks, leaf-spine fabrics, and datacenter clusters using short-reach or medium-reach fiber. The architecture is attractive because it preserves multi-vendor interoperability, field replacement, operational familiarity, and module-level yield isolation.

The technical transition is from 100G/lane to 200G/lane. OSFP defines an 8-lane pluggable form factor that supports 400G as 8×50G, 800G as 8×100G, and 1.6T as 8×200G.[^osfp] IEEE 802.3dj targets 200G/lane electrical and optical building blocks for 200G, 400G, 800G, and 1.6T Ethernet, while the Ethernet Alliance roadmap explicitly frames AI/ML as a driver pushing Ethernet toward 1.6T and beyond.[^ieee-dj][^ethernet-roadmap]

**What a pluggable transceiver does:**

| Function | Component layer | What matters technically | Main public/private suppliers |
|---|---|---|---|
| Convert switch electrical lanes into optical lanes | Optical module | OSFP / QSFP-DD mechanicals, CMIS management, thermal envelope, link budget | Coherent (COHR), Lumentum (LITE), Applied Optoelectronics (AAOI), Innolight / Zhongji Innolight (300308.SZ), Eoptolink (300502.SZ), Accelink (002281.SZ), Jabil (JBL), Fabrinet (FN), Foxconn/FIT Hon Teng (6088.HK) |
| Generate light | Laser chips / arrays | 100G→200G EML, VCSEL for very short reach, CW lasers for silicon photonics | Lumentum, Coherent, Sivers, Furukawa, Sumitomo Electric, Mitsubishi Electric, Broadcom, AAOI |
| Modulate data onto light | EML / silicon photonics / TFLN | bandwidth, drive voltage, insertion loss, extinction ratio, temperature stability | Lumentum, Coherent, Tower Semiconductor, OpenLight, HyperLight, Lumiphase, Lightwave Logic |
| Recover / condition signal | Optical DSP / SerDes | 200G PAM4 equalization, FEC, power per bit, gearbox functions, diagnostics | Marvell (MRVL), Broadcom (AVGO), MaxLinear (MXL), Credo (CRDO), Semtech (SMTC), MACOM (MTSI) |
| Attach fiber and maintain optical alignment | Connectors / ferrules / pigtails | density, insertion loss, cleaning, thermal/mechanical drift | Corning (GLW), Amphenol (APH), TE Connectivity (TEL), SENKO, US Conec, Sumitomo, Furukawa |
| Build at volume | Assembly / packaging / test | optical alignment yield, burn-in, TDECQ/BER test throughput, thermal test | Fabrinet, Jabil, Foxconn, Flex (FLEX), Sanmina (SANM), Keysight (KEYS), Anritsu (6754.T), VIAVI (VIAV), EXFO |

**Why 800G remains dominant near term:**

800G is already the scaled deployment point for many AI clusters because it fits current switch port densities and optical-module supply chains. 1.6T is the next wave, but its adoption depends on 200G/lane SerDes, 200G optical lanes, DSP yield, module thermals, and switch silicon availability. The practical sequencing is therefore: 800G volume → 1.6T selective deployment → 1.6T broader deployment as 200G/lane matures.

**Why 1.6T is strategically different from 800G:**

At 800G, many designs can still use 8×100G optical lanes or 4×200G variants depending on reach and technology. At 1.6T, 8×200G becomes central. That pushes every layer harder: laser bandwidth, modulator linearity, DSP power, thermal density, connector density, factory test time, and hyperscaler qualification. Innolight’s 1.6T DR8 OSFP224 product, for example, uses 8 channels of 200G PAM4 electrical and optical parallel lanes for up to 500m over single-mode fiber.[^innolight-16t] Eoptolink likewise describes 1.6T OSFP products with DR8 and 2×FR4 reach variants for AI clusters and cloud datacenters.[^eoptolink-16t]

**Module types and where they fit:**

| Module type | Typical role in AI datacenters | Bottleneck layer | Interpretation |
|---|---|---|---|
| 800G SR / VR over multimode | Very short reach within racks / adjacent racks | VCSEL arrays, multimode fiber, connector density | Lower cost and power for short reach, but reach-limited. |
| 800G DR / FR over single-mode | Leaf-spine, rack-to-rack, short campus | EML / silicon photonics, DSP, single-mode fiber | Main AI scale-out workhorse. |
| 1.6T DR8 | 8×200G parallel single-mode links | 200G EML / SiPh, 1.6T DSP, test | First major 1.6T volume architecture. |
| 1.6T 2×FR4 / coherent-lite variants | Higher density / longer reach | WDM optics, DSP, lasers, thermal | Reduces fiber count but adds optical complexity. |
| LPO / LRO variants | Lower-power pluggable experiments | module-host co-design, link margin | Attractive power story, but more dependent on switch/channel control. |

**Who likely captures value in the pluggable phase:**

| Value capture zone | Why it captures value | Key companies / tickers | Key risk |
|---|---|---|---|
| 200G/lane lasers | Every high-speed optical lane needs a light source; 200G requires better bandwidth, linearity, and thermal behavior than 100G | Lumentum (LITE), Coherent (COHR), Sivers (SIVE.ST), Furukawa (5801.T), Sumitomo (5802.T), Mitsubishi Electric (6503.T) | Commoditization if module makers dual-source quickly; technology mix may shift from EML to SiPh/TFLN. |
| 1.6T optical DSP | DSP determines reach, BER margin, diagnostics, and module power | Marvell (MRVL), Broadcom (AVGO), MaxLinear (MXL), Credo (CRDO) | LPO / LRO architectures can reduce DSP content in selected links; CPO may alter the module-level DSP architecture. |
| Optical modules | Near-term revenue is visible because hyperscalers buy large module volumes | Coherent, AAOI, Innolight, Eoptolink, Accelink, Jabil, Fabrinet | Gross margins can compress as hyperscalers multi-source and module ASPs fall. |
| Contract manufacturing | Complexity of optical alignment and test creates manufacturing scarcity | Fabrinet (FN), Jabil (JBL), Foxconn/FIT, Flex, Sanmina | Customer concentration and price-down pressure. |
| Test equipment | 200G/lane increases test difficulty and factory bottleneck risk | Keysight, Anritsu, VIAVI, EXFO | Test equipment demand can be cyclical once capacity is installed. |

**Near-term read-through:** pluggables are the default architecture until CPO is qualified broadly enough to beat them on total cost, reliability, serviceability, and procurement simplicity. The near-term investment lens should therefore focus less on “CPO will replace transceivers” and more on “which pluggable bottleneck remains scarce during the 800G→1.6T transition?”

### Front-panel optical modules plugged into switches

Front-panel pluggables separate the optical module from the switch ASIC. The switch vendor supplies the ASIC, SerDes, cages, and thermal envelope; the optical module vendor supplies the pluggable transceiver; the datacenter operator can replace failed optics without replacing the switch. This field-service model is the biggest reason pluggables remain dominant.

**Architecture path:**

```text
Switch ASIC / SerDes → PCB traces → front-panel cage → pluggable transceiver → fiber plant → remote transceiver → remote switch
```

**Advantages:**

| Advantage | Why it matters |
|---|---|
| Field replaceability | Failed optics can be swapped without replacing the switch. |
| Multi-vendor procurement | Hyperscalers can qualify multiple module vendors and pressure pricing. |
| Yield isolation | Optical module yield is separated from switch ASIC yield. |
| Operational familiarity | Datacenter teams already know module inventory, cleaning, diagnostics, and replacement workflows. |
| Standards ecosystem | OSFP / QSFP-DD / CMIS / IEEE PMDs give buyers more vendor choice. |

**Disadvantages:**

| Disadvantage | Why it matters more at 1.6T |
|---|---|
| Electrical channel loss | PCB trace from switch ASIC to front-panel module becomes harder at 200G/lane. |
| Power density | DSP + laser + driver + thermal management inside a small module becomes difficult. |
| Front-panel density | More bandwidth per rack increases fiber and cage density pressure. |
| Cooling | Pluggables sit at the front panel, but module power still stresses airflow and heatsinks. |
| Cost per bit | Pluggable optics are serviceable but include duplicated module housings, DSPs, cages, and management overhead. |

**Switch/platform dependency:**

Pluggables depend on the switch ASIC roadmap. 51.2T switches made 800G front-panel ports mainstream; 102.4T-class switches make 1.6T ports more natural. Broadcom’s Tomahawk 6 is positioned as a 102.4Tbps switch chip for AI datacenters, and NVIDIA’s Spectrum-X / Quantum-X photonics roadmap shows 1.6Tbps-per-port systems as the direction of travel.[^broadcom-th6][^nvidia-photonics]

**Key companies and roles:**

| Role | Public companies | Private / non-US-listed / ecosystem companies | Notes |
|---|---|---|---|
| Switch ASICs / platforms | Broadcom (AVGO), NVIDIA (NVDA), Cisco (CSCO), Marvell (MRVL), Arista (ANET, system integrator) | — | Controls the electrical interface, port speed, and switch architecture. |
| Optical modules | Coherent (COHR), Lumentum (LITE), AAOI (AAOI), Jabil (JBL), Fabrinet (FN) | Innolight, Eoptolink, Accelink, Source Photonics, Hisense Broadband | Module margin depends on vertical integration and hyperscaler qualification. |
| Lasers / optical components | Lumentum, Coherent, Sivers, MACOM, Broadcom | Furukawa, Sumitomo, Mitsubishi, NTT Innovative Devices | 200G EML and high-power CW lasers are strategic. |
| DSP / SerDes | Marvell, Broadcom, MaxLinear, Credo, Semtech | — | 1.6T DSP power and yield are central to module economics. |
| Connectors / fiber plant | Corning, Amphenol, TE Connectivity | SENKO, US Conec, Sumitomo, Furukawa | High-density, low-loss fiber attach becomes more important with parallel optics. |
| Test | Keysight, Anritsu, VIAVI, EXFO | Spirent, Tektronix | Test time can become a production bottleneck at 1.6T. |

**Main watch items:**

- 1.6T module qualification status at NVIDIA, Meta, Microsoft, Google, Amazon, Oracle, and xAI.
- Ratio of 800G vs 1.6T shipments.
- 100G/lane vs 200G/lane mix.
- DSP-lite, LPO, or LRO adoption that could reduce full-DSP content.
- Laser supply tightness, especially 200G EML and high-power CW lasers.
- Factory yield and test throughput at Fabrinet / Jabil / Foxconn ecosystems.
- Connector density, cleaning, and insertion-loss issues as fiber counts rise.

## Next architecture: CPO optical engines

CPO moves optical engines close to, or onto the same package as, the switch ASIC. The goal is to shorten the highest-speed electrical path. Instead of driving 200G/lane signals across a long PCB path into a front-panel pluggable, the switch ASIC talks over much shorter electrical links to optical engines around the package. The optical engines then launch light into fibers that reach the faceplate.

NVIDIA announced Spectrum-X Photonics and Quantum-X Photonics in March 2025 as co-packaged optics networking switches, with 1.6Tbps-per-port switches and claimed energy / resiliency benefits versus traditional pluggable-transceiver networks.[^nvidia-photonics] Broadcom announced Bailly as a 51.2Tbps CPO switch in 2024 and Davisson as a 102.4Tbps CPO Ethernet switch in 2025.[^broadcom-bailly][^broadcom-davisson]

**Architecture path:**

```text
Switch ASIC package → short electrical links → optical engine chiplets → fiber attach / pigtails → faceplate connectors → fiber plant
                                  ↑
                         external laser source or integrated laser
```

**Why CPO exists:**

| Driver | Explanation |
|---|---|
| Electrical loss at high lane rates | 200G/lane and beyond make long PCB traces expensive in power, equalization, and signal integrity. |
| Front-panel power density | Pluggables concentrate heat and DSP power at the front panel. |
| Port density | AI switches need much more bandwidth per rack unit. |
| Reliability at AI scale | Million-GPU-class fabrics make link failures economically meaningful. NVIDIA frames its photonics switches around both energy efficiency and network resiliency.[^nvidia-siph] |
| System-level optimization | CPO lets a system vendor co-design switch silicon, optical engines, lasers, fiber attach, cooling, and diagnostics. |

**CPO is not automatically “better” in every deployment:**

| CPO challenge | Why it matters |
|---|---|
| Field serviceability | A failed optical engine is harder to replace than a failed front-panel pluggable. |
| Yield coupling | Packaging optics with the switch increases the consequence of optical-engine defects. |
| Thermal stress | Optical components dislike heat, but switch ASICs are among the hottest chips in the rack. |
| Fiber management | Dense fiber attach from package to faceplate must survive assembly, service, vibration, cleaning, and airflow constraints. |
| Standards maturity | CPO needs ecosystem standards for optical engines, external laser sources, management, safety, and test. |
| Procurement model | Hyperscalers lose some module-level multi-sourcing if the switch platform controls the optics. |

**CPO product/platform map:**

| Platform / supplier | Public status | What it indicates | Investable angle |
|---|---|---|---|
| NVIDIA Spectrum-X Photonics / Quantum-X Photonics | Announced 2025; ecosystem partners include TSMC, Coherent, Corning, Foxconn, Lumentum, and SENKO.[^nvidia-photonics] | Vertical integration from switch platform into photonics supply chain | NVDA controls architecture; LITE/COHR/GLW/SENKO/Foxconn/FIT may capture component/manufacturing value. |
| Broadcom Bailly 51.2T / Davisson 102.4T CPO | Bailly 51.2T announced 2024; Davisson 102.4T announced 2025.[^broadcom-bailly][^broadcom-davisson] | Merchant Ethernet switch silicon moving CPO into deployable systems | AVGO captures switch ASIC and CPO platform economics; ecosystem suppliers still needed for ELS/fiber/test. |
| Marvell + Celestial AI | Marvell completed Celestial AI acquisition in 2026 to expand optical connectivity capabilities.[^marvell-celestial] | Optical I/O is moving from module edge into package/system interconnect | MRVL gains photonic fabric and custom silicon integration optionality. |
| Ayar Labs / Alchip / TSMC COUPE | Private ecosystem; Ayar and Alchip disclosed co-packaged optics work for next-gen AI infrastructure.[^ayar-alchip] | Optical I/O chiplets can become a building block for AI accelerators and switch ASICs | TSMC / packaging ecosystem matters; Ayar remains private. |
| Ranovus ODIN | Ranovus announced Jabil collaboration for mass production of ODIN optical engine.[^ranovus-jabil] | CPO engines can be supplied as merchant optical-engine components | Jabil gains manufacturing exposure; Ranovus remains private. |
| Coherent / OpenLight / Tower / GF | Component and foundry ecosystem | CPO needs lasers, photonic integrated circuits, and manufacturable SiPh | COHR, TSEM, GFS, and private OpenLight are indirect enablers. |

**CPO adoption read-through:** CPO is most compelling when system vendors can control the whole platform: switch ASIC, package, optical engine, lasers, cooling, management, and service model. That favors NVIDIA and Broadcom initially. For broad merchant adoption, the industry needs standardized optical engines, external laser modules, fiber attach, diagnostics, and repair workflows.

### Optics moved close to / onto the switch ASIC package

Moving optics close to the switch ASIC changes the value chain. The optical module is no longer a fully independent front-panel product. Instead, value shifts into optical chiplets, silicon photonics engines, ELS modules, package-level fiber attach, and liquid/thermal integration.

**CPO component stack:**

| CPO layer | What it does | Bottleneck | Supplier map |
|---|---|---|---|
| Switch ASIC | Packet switching / routing at 51.2T, 102.4T, and beyond | SerDes, radix, routing software, power | NVIDIA, Broadcom, Cisco, Marvell |
| Optical engine | Converts short-reach electrical I/O into optical I/O near the ASIC | photonic integration, modulator performance, receiver sensitivity, test | NVIDIA internal, Broadcom, Coherent, OpenLight, Ranovus, Ayar Labs, Celestial/Marvell, Lightmatter, Nubis |
| External laser source | Supplies high-power continuous-wave light to optical engines | reliability, power efficiency, eye safety, field replacement | Lumentum, Coherent, Furukawa, Sivers, Sumitomo, Broadcom |
| Fiber attach | Couples engine output to faceplate fibers | insertion loss, alignment, density, repairability | Corning, SENKO, US Conec, Amphenol, TE, Sumitomo, Foxconn/FIT |
| Package / substrate | Integrates ASIC, optical engines, electrical links, and thermal stack | co-packaging yield and warpage | TSMC, Amkor, ASE, Foxconn, Jabil, Intel Foundry, Broadcom ecosystem |
| Thermal | Keeps ASIC hot zone and optics stable | liquid cooling, cold plates, thermal isolation | Vertiv, Schneider Electric, Eaton/Boyd, Modine, nVent, CoolIT, Asetek |
| Test / diagnostics | Validates package-level optical links | wafer-level photonic test, known-good-die, burn-in | Keysight, Anritsu, FormFactor, Advantest, Teradyne, VIAVI |

**Why external lasers matter in CPO:**

A major CPO design choice is whether lasers are integrated inside the optical engine or placed externally. OIF’s ELSFP Implementation Agreement defines a front-panel pluggable external laser source form factor delivering continuous-wave light to co-packaged optical engines; OIF highlights field replacement and the cooler front-panel region as key advantages.[^oif-elsfp][^oif-framework] Furukawa’s 2024 work on blind-mate, high-power external laser sources shows why ELS is becoming a real subsystem rather than a lab concept.[^furukawa-els]

**CPO value migration:**

| From pluggable world | To CPO world | Value migration |
|---|---|---|
| Module vendor owns full transceiver | Switch vendor / platform owner controls optical engine | More value shifts to NVIDIA / Broadcom / switch platform owner. |
| Laser inside each module | External laser banks may feed multiple optical engines | Laser vendors remain strategic, but product format changes. |
| Front-panel connector to module | Package-to-faceplate fiber attach | Corning / SENKO / US Conec / Amphenol become more important. |
| Module-level DSP | Shorter electrical path may reduce DSP burden or change where equalization happens | MRVL/AVGO/MXL/CRDO must adapt product segmentation. |
| Module-level test | Wafer/package/system optical test | Keysight/Anritsu/FormFactor/VIAVI become more involved earlier in manufacturing. |
| Airflow-cooled pluggables | Liquid-cooled switch / optical package | Vertiv/Eaton/Schneider/Modine/nVent become part of photonics reliability. |

**CPO adoption gates:**

- Demonstrated field reliability of optical engines near hot switch ASICs.
- Standardized ELS modules with eye safety, blind-mate connectors, and hot-swap service.
- Known-good optical-engine test before expensive package assembly.
- CPO repair strategy acceptable to hyperscalers.
- Supply chain capacity for SiPh wafers, InP lasers, fiber attach, and advanced packaging.
- Software / telemetry stack for diagnosing optical faults without pluggable module replacement.

## Supporting photonics infrastructure

The supporting infrastructure is the real bottleneck map. The product architecture may be “pluggable” or “CPO,” but both architectures depend on the same physical layers: light generation, modulation, signal processing, fiber coupling, foundry capacity, assembly/test, and heat removal. The more AI clusters scale, the more these layers matter.

| Infrastructure layer | Near-term importance | CPO importance | Why it is a bottleneck |
|---|---:|---:|---|
| Lasers / ELS | Very high | Very high | Every optical link needs light; 200G/lane and CPO require high-performance lasers. |
| Modulators | High | Very high | Lane speed and power depend on modulator bandwidth and drive voltage. |
| Optical DSP / SerDes | Very high | High | 200G/lane PAM4 needs signal recovery; CPO changes where DSP value sits. |
| Fiber attach / connectors | High | Very high | More bandwidth creates fiber-density and alignment problems. |
| Optical circuit switches | Medium today | High later | OCS can redesign AI fabrics and reduce OEO conversions. |
| Photonic foundries | High | Very high | SiPh/TFLN/BTO scaling requires manufacturable processes and PDKs. |
| Assembly / packaging / testing | Very high | Very high | Optical manufacturing yield and test throughput can become the capacity constraint. |
| Thermal / liquid cooling | High | Very high | CPO places optics near hot ASICs; AI racks require liquid cooling. |

### Lasers / external laser sources

Lasers are the most basic chokepoint: no laser, no optical link. In pluggables, lasers sit inside the module or photonic integrated circuit. In CPO, lasers may move outside the optical engine as ELS modules that feed multiple optical engines with continuous-wave light.

**Laser types:**

| Laser type | Main use | Strength | Weakness | Key suppliers |
|---|---|---|---|---|
| EML / EA-DFB | 800G / 1.6T single-mode pluggables | high bandwidth, mature for datacom | harder at 200G/lane, thermal/power constraints | Lumentum, Coherent, Mitsubishi Electric, Sumitomo, Broadcom, NTT Innovative Devices |
| DFB + silicon photonics | silicon photonics pluggables and CPO | integrates with SiPh PICs; external laser options | laser-PIC coupling and packaging complexity | OpenLight, Coherent, Lumentum, Sivers, Tower/OpenLight ecosystem |
| VCSEL | short-reach multimode optics | low cost and efficient for very short reach | reach-limited; multimode fiber constraints | Coherent, Broadcom, Lumentum, Eoptolink ecosystem |
| High-power CW laser / ELS | CPO optical engines | one external laser bank can feed multiple engines; field replaceable | eye safety, power, reliability, connectorization | Lumentum, Coherent, Furukawa, Sivers, Sumitomo, Broadcom |

**Why 200G EML matters:** Lumentum highlighted differential-drive EA-DFB / EML work supporting high-speed links for 1.6TbE and AI/cloud infrastructure.[^lumentum-ofc] Coherent’s OFC 2026 investor material emphasized a broad laser portfolio, including InP lasers for CPO ELSFP applications and 1.6T transceiver demonstrations.[^coherent-ofc]

**Why ELS matters:** OIF’s ELSFP standard turns lasers into a field-replaceable system component. This is strategically important because one of the biggest objections to CPO is serviceability. If lasers are the highest-failure-risk optical component, externalizing them to the faceplate improves maintainability.

**Public-equity map:**

| Company | Ticker | Exposure type | Purity |
|---|---:|---|---:|
| Lumentum | LITE | EML lasers, datacom lasers, CPO/AI optics strategic supplier | High |
| Coherent | COHR | lasers, transceivers, SiPh, InP, VCSELs, OCS | High |
| Sivers Semiconductors | SIVE.ST | lasers for low-power optical modules and AI datacenter links | Medium |
| Furukawa Electric | 5801.T | ELS demonstrations, fiber/optical components | Medium |
| Sumitomo Electric | 5802.T | optical fiber, connectors, laser/components | Medium |
| Mitsubishi Electric | 6503.T | EML / optical device ecosystem | Low-Medium |
| Broadcom | AVGO | laser/DSP/SiPh/CPO platform plus switch ASIC | Medium, but strategic |

**Watch items:** 200G EML yield, 400G/lane roadmaps, high-power CW laser availability, ELSFP adoption, Nvidia/Broadcom supplier concentration, laser pricing vs module ASP declines, 6-inch InP wafer capacity.

### Modulators: EML, silicon photonics, TFLN, BTO, polymers

Modulators are where electrical data becomes optical data. They determine lane speed, optical reach, drive voltage, power, and thermal tolerance. The modulator technology choice is one of the most important architectural decisions in 1.6T / 3.2T optics.

**Technology comparison:**

| Modulator platform | Current role | Why it matters | Maturity | Companies / exposure |
|---|---|---|---|---|
| EML / EA-DFB | Mainstream 800G and early 1.6T single-mode pluggables | compact, mature, strong for DR/FR | High | Lumentum, Coherent, Mitsubishi, Sumitomo, NTT Innovative Devices |
| Silicon photonics MZM / microring | Pluggables, CPO engines, integrated PICs | CMOS-compatible, scalable, supports WDM and CPO | High-Medium | Broadcom, Intel, NVIDIA/TSMC ecosystem, Tower, GF, OpenLight, Coherent |
| TFLN | Next-gen high-speed, low-voltage modulation | very high bandwidth and low drive voltage; promising for 400G/lane | Medium | HyperLight, Fujitsu, Liobate, UMC/Jabil ecosystem |
| BTO-on-silicon | Emerging low-power electro-optic modulation | strong Pockels effect; potential high-speed/low-power SiPh integration | Early-Medium | Lumiphase, imec/Veeco ecosystem |
| Electro-optic polymers | Emerging ultra-low-voltage, high-bandwidth modulation | potential direct-drive and low power | Early | Lightwave Logic (LWLG), NLM Photonics, SilOriX |

**EML:** EML is the incumbent for many 800G/1.6T pluggables. Its advantage is maturity and integration of laser and modulator. Its risk is that 200G/lane and 400G/lane push bandwidth and drive-voltage limits.

**Silicon photonics:** SiPh is the natural platform for CPO because it can integrate waveguides, splitters, modulators, photodiodes, and WDM structures on a wafer-scale process. OpenLight’s 1.6T DR8 PIC, for example, integrates DFB lasers, 224G modulators, and SOAs, showing why heterogeneous III-V-on-silicon integration matters for AI datacenter optics.[^openlight-16t]

**TFLN:** TFLN is the speculative but technically important modulator material for 400G/lane and eventually 3.2T. Ciena, HyperLight, Keysight, and McGill demonstrated 448G / 3.2T-class optical transmission work using HyperLight TFLN modulators.[^ciena-hyperlight] HyperLight later introduced 400G-per-lane TFLN PICs for next-generation AI interconnects, emphasizing low insertion loss, low drive voltage, and high electro-optic bandwidth.[^hyperlight-400g]

**BTO:** Barium titanate is an emerging electro-optic material for high-speed, low-power modulation on silicon. imec and Veeco announced work on 300mm-compatible BTO integration, describing BTO as promising for high-speed and low-power modulation in high-speed optical transceivers and other emerging applications.[^imec-bto]

**Polymers:** Electro-optic polymer modulators remain earlier-stage than EML or SiPh. Their attraction is potentially very low drive voltage and high bandwidth, but the commercial proof points that matter are reliability, foundry integration, packaging, and high-volume qualification.

**Investment lens:**

- EML is the near-term revenue bottleneck.
- SiPh is the CPO scaling platform.
- TFLN is the 3.2T / 400G-per-lane optionality layer.
- BTO and polymers are asymmetric technology options but require more evidence of high-volume manufacturing and reliability.

### Optical DSP / SerDes

Optical DSPs and SerDes are the hidden engines inside high-speed optics. They compensate for channel loss, perform equalization, support FEC, monitor link quality, and often integrate drivers or gearbox functions. At 1.6T, the DSP becomes both a performance enabler and a power problem.

Marvell’s 1.6T optical DSP portfolio is a central example: its Ara 3nm 1.6T PAM4 DSP integrates eight 200G electrical lanes and eight 200G optical lanes in a standardized module form factor.[^marvell-ara] Marvell expanded its 1.6T optical DSP portfolio in 2026, optimizing for different high-volume use cases.[^marvell-16t] MaxLinear’s Rushmore is another 1.6T PAM4 DSP family targeting optics and active copper interconnects.[^maxlinear-rushmore]

**DSP value chain:**

| DSP function | Why it matters | Companies |
|---|---|---|
| PAM4 signal recovery | 200G/lane signals have tight margins | Marvell, Broadcom, MaxLinear, Credo |
| FEC / diagnostics | hyperscalers need link reliability and telemetry | Marvell, Broadcom, MaxLinear |
| Gearbox | converts 8×100G host lanes to 4×200G optical or other mappings | Marvell, Broadcom, MaxLinear |
| LPO / LRO support | shifts equalization burden between module and host | Broadcom, Marvell, Credo, MaxLinear |
| Active electrical cables | extends copper reach inside racks | Credo, Marvell, Semtech, Broadcom |
| SerDes IP | embedded in switch ASICs, NICs, custom silicon | Broadcom, Marvell, Synopsys, Cadence, Alphawave/Qualcomm ecosystem |

**Public-equity map:**

| Company | Ticker | Exposure | Notes |
|---|---:|---|---|
| Marvell | MRVL | 1.6T optical DSP, AEC DSP, custom silicon, Celestial AI optical I/O | Strong optical DSP and custom AI infrastructure positioning. |
| Broadcom | AVGO | switch ASIC, 200G/lane SerDes, DSP, CPO | Most vertically integrated merchant Ethernet supplier. |
| MaxLinear | MXL | 1.6T PAM4 DSP | Smaller-cap DSP exposure; execution and customer adoption matter. |
| Credo | CRDO | AEC, optical DSP, low-power connectivity | Strong copper-extension and emerging optical DSP story. |
| Semtech | SMTC | signal integrity / high-speed connectivity components | More diversified, lower purity. |
| Synopsys / Cadence | SNPS / CDNS | SerDes IP and EDA for high-speed interfaces | Tool/IP exposure rather than optical module exposure. |

**Key debate:** full DSP vs DSP-lite vs LPO. Full DSP gives better reach, diagnostics, and margin, but burns power. LPO can save power by removing DSP from the module, but it requires tighter host/module co-design and may be harder at 200G/lane. The investable implication is not “DSP disappears”; it is “DSP content fragments by reach, power budget, and hyperscaler architecture.”

### Fiber attach / connectors

Fiber attach becomes more strategic as bandwidth rises because parallel optics multiply fiber counts and CPO moves fiber coupling inside the switch system. At 1.6T and CPO, the bottleneck is not just “fiber.” It is low-loss, high-density, serviceable, thermally stable optical coupling from the photonic engine to the datacenter fiber plant.

Corning and NVIDIA framed CPO as extending fiber connectivity right to photonic chips inside equipment, improving power efficiency and lowering latency.[^corning-nvidia] SENKO joined NVIDIA’s photonics ecosystem to supply optical connectivity for Spectrum-X and Quantum-X photonics switches.[^senko-nvidia] Corning also announced AI-focused fiber, cable, connector, and CPO-related products at OFC 2026, including multicore fiber and next-generation connectors.[^corning-ofc]

**Connector / attach layers:**

| Layer | Role | Bottleneck | Supplier map |
|---|---|---|---|
| Front-panel pluggable connectors | Connect module to external fiber plant | density, insertion loss, cleaning | SENKO, US Conec, Corning, Amphenol, TE, CommScope ecosystem |
| High-density CPO faceplate | Terminate many fiber paths from optical engines | routing, bend radius, serviceability | Corning, SENKO, US Conec, Amphenol, Foxconn/FIT |
| Internal pigtails / fiber ribbons | Carry light from optical engine to faceplate | alignment, strain relief, thermal drift | Corning, Furukawa, Sumitomo, SENKO |
| Detachable fiber connectors | Allow package/system assembly and service | blind-mate precision, loss, contamination | Corning, SENKO, US Conec, GF ecosystem |
| Multicore fiber | Increase density per cable | splicing, connector ecosystem, interoperability | Corning, Sumitomo, Furukawa, YOFC |

**Public-equity map:**

| Company | Ticker | Exposure | Purity |
|---|---:|---|---:|
| Corning | GLW | fiber, cable, connector, CPO fiber attach, AI datacenter supply | Medium-High |
| Amphenol | APH | high-speed copper/optical interconnect, OSFP cables, datacenter connectors | Medium-High |
| TE Connectivity | TEL | high-speed connectors and datacenter interconnects | Medium |
| Sumitomo Electric | 5802.T | fiber, optical cable, connector ecosystem | Medium |
| Furukawa Electric | 5801.T | fiber/cable and ELS optical components | Medium |
| Foxconn/FIT Hon Teng | 6088.HK | connectors, cable assemblies, CPO ELS ecosystem | Medium |

**Watch items:** CPO fiber-attach qualification, connector standard adoption, multicore fiber adoption, hyperscaler fiber procurement deals, cleaning/contamination failures, faceplate density constraints, PRIZM / SN / SN-MT / MPO evolution.

### Optical circuit switches

Optical circuit switching (OCS) is the next architecture beyond “just faster links.” OCS reconfigures optical paths directly in the optical domain, reducing the need for electrical packet switching and repeated optical-electrical-optical conversions. It is not a replacement for Ethernet switches everywhere; it is a fabric-level tool for workloads where traffic patterns can be scheduled or where topology reconfiguration improves utilization.

Google’s Jupiter evolution is the strongest public validation. Google reports that its Jupiter datacenter fabric evolution delivered 5× higher speed and capacity, 30% lower capex, and 41% lower power, with optical circuit switches and software-defined networking as key enablers.[^google-jupiter] OCP launched an Optical Circuit Switching project in July 2025, and Google stated that it extensively uses OCS in datacenters as part of Jupiter/AI network architectures and Project Apollo for TPU systems.[^ocp-ocs]

**OCS architecture path:**

```text
GPU/TPU racks → optical transceivers / fibers → optical circuit switch → dynamically assigned light paths → remote racks / pods
```

**Why OCS matters for AI:**

| AI problem | OCS relevance |
|---|---|
| Training jobs generate structured east-west traffic | circuits can be scheduled around known traffic flows. |
| Electrical packet switching consumes power | OCS can reduce OEO conversions and packet-switching layers. |
| Large clusters suffer failures and congestion | reconfigurable optical paths can improve resilience and utilization. |
| TPU/GPU pods need topology flexibility | OCS can rewire fabrics without physically rewiring fiber. |

**Supplier map:**

| Company | Ticker / status | OCS role |
|---|---:|---|
| Coherent | COHR | Optical circuit switch products for AI datacenter networks; also lasers/transceivers. |
| Lumentum | LITE | OCS and laser/optical component ecosystem; demonstrated OCS with Marvell DSP modules at OFC 2026.[^marvell-lumentum-ocs] |
| Google | GOOGL | Internal deployment and architecture validation. |
| Marvell | MRVL | DSP ecosystem around modules used with OCS. |
| Calient | Private | MEMS optical switching. |
| Polatis / HUBER+SUHNER | Private / listed parent in Switzerland | optical switching and fiber management. |
| Lumetrix / other startups | Private | emerging OCS technologies. |

**Investment lens:** OCS is a more strategic but less near-term revenue layer than pluggables. It becomes more important if AI cluster scale makes static Clos fabrics too expensive or power-hungry. The most attractive public exposure is probably indirect: Coherent / Lumentum for optical switching and lasers, Marvell for DSP around optical fabrics, Google for proof of deployment, and connector/fiber suppliers for the fiber plant.

### Photonic foundries

Photonic foundries are the manufacturing base for silicon photonics and emerging modulator platforms. As the industry moves from discrete optics to integrated photonic engines, foundry capacity and process design kits become strategic. The bottleneck is not simply wafer starts; it is qualified photonic PDKs, active/passive device libraries, III-V integration, thermal models, wafer-level optical test, packaging recipes, and yield learning.

GlobalFoundries expanded its silicon photonics strategy by acquiring Advanced Micro Foundry in Singapore in 2025, adding silicon photonics technology, capacity, and R&D to its portfolio.[^gf-amf] Tower Semiconductor announced silicon photonics work for 1.6T datacenter optical modules designed for NVIDIA networking protocols, saying its technology enables up to double the data rate of prior silicon photonics solutions.[^tower-nvidia] TSMC’s COUPE platform is widely watched because it links silicon photonics with advanced packaging for AI interconnects.[^tsmc-coupe]

**Foundry map:**

| Foundry / platform | Public status | Photonics role | Strategic relevance |
|---|---:|---|---|
| TSMC COUPE | TSM | silicon photonics + advanced packaging | Most important if optical I/O moves into AI accelerator / switch packages. |
| GlobalFoundries Fotonix + AMF | GFS | silicon photonics foundry and Singapore capacity | Broad merchant SiPh capacity; Singapore footprint. |
| Tower Semiconductor | TSEM | silicon photonics and SiGe foundry | 1.6T optical modules and NVIDIA networking protocols. |
| UMC + HyperLight / Wavetek / Jabil ecosystem | UMC | scalable TFLN manufacturing partnership | Important for TFLN if 400G/lane ramps. |
| OpenLight platform | Private / Synopsys-Jabil heritage | heterogeneous III-V on silicon PICs | Enables integrated lasers, SOAs, modulators on SiPh. |
| Intel silicon photonics | INTC | internal and merchant photonics heritage | Strong technology base, but commercial foundry positioning must be watched. |
| imec / AIM Photonics | research ecosystem | process development and prototyping | Not direct module revenue, but important for next-gen platforms. |

**Why foundries matter more in CPO than pluggables:**

- Pluggables can be assembled from discrete optical components.
- CPO needs high-yield integrated photonic engines.
- Package-level optics require known-good photonic die before integration with expensive switch ASICs.
- Foundry PDK quality determines how many startups and module vendors can design around the process.
- Advanced packaging and photonic wafer test become inseparable.

**Watch items:** TSMC COUPE production milestones, GF/AMF customer traction, Tower capex and customer commitments, OpenLight volume production orders, UMC/HyperLight TFLN scale-up, wafer-level optical test automation, availability of qualified photonic PDKs.

### Assembly / packaging / testing

Optics is harder to manufacture than ordinary electronics because performance depends on sub-micron alignment, optical coupling loss, laser burn-in, thermal cycling, fiber cleanliness, and high-speed electrical/optical compliance. At 1.6T, a module that works on a bench is not enough; it must be manufactured in volume with acceptable yield and test time.

Keysight frames 800G / 1.6T transceiver test around hyperscale datacenter migration from 400G to 800G and 1.6T, emphasizing that manufacturers must scale production quickly while maintaining yield.[^keysight-test] Jabil’s photonics page highlights its 1.6T pluggable transceiver work for intra-datacenter and AI connectivity.[^jabil-photonics]

**Manufacturing stack:**

| Step | What can go wrong | Bottleneck suppliers |
|---|---|---|
| Photonic wafer fabrication | wafer yield, device variability, thermal drift | TSMC, GFS, Tower, UMC, OpenLight, imec ecosystem |
| Laser attach / integration | coupling loss, burn-in failures, heat | Coherent, Lumentum, OpenLight, Sivers, Jabil, Fabrinet |
| Optical alignment | insertion loss, active alignment time | Fabrinet, Jabil, Foxconn, Flex, Sanmina |
| Module assembly | thermal design, EMI, mechanical tolerance | Fabrinet, Jabil, Foxconn/FIT, Flex, Sanmina |
| Package-level CPO assembly | known-good-die, substrate warpage, fiber routing | TSMC, ASE, Amkor, Jabil, Foxconn, Broadcom/NVIDIA ecosystem |
| Compliance test | BER, TDECQ, jitter, FEC margin | Keysight, Anritsu, VIAVI, EXFO, Tektronix |
| System burn-in | failures under sustained traffic and temperature | module vendors, hyperscalers, switch OEMs |

**Public-equity map:**

| Company | Ticker | Exposure | Notes |
|---|---:|---|---|
| Fabrinet | FN | optical component and module contract manufacturing | High relevance to AI optics volume, customer concentration risk. |
| Jabil | JBL | photonics manufacturing, 1.6T modules, Ranovus/HyperLight ecosystem | Diversified EMS with increasing photonics exposure. |
| Foxconn / FIT Hon Teng | 2317.TW / 6088.HK | connectors, cable assemblies, CPO ELS ecosystem | Important NVIDIA ecosystem role. |
| Flex | FLEX | EMS / datacenter hardware manufacturing | Lower purity but relevant. |
| Sanmina | SANM | optical/electronics manufacturing | Lower purity. |
| Keysight | KEYS | 800G/1.6T electrical and optical test | High-quality picks-and-shovels exposure. |
| Anritsu | 6754.T | optical sampling oscilloscope and 200G/lane test | Japanese test exposure. |
| VIAVI | VIAV | fiber, optical, and network test | Datacenter and telecom optical test exposure. |
| FormFactor | FORM | wafer probe / photonic test relevance | More indirect but important for wafer-level SiPh scaling. |

**Why testing can be a hidden bottleneck:**

At 1.6T, production needs both optical and electrical validation: optical eye quality, TDECQ, BER, jitter, lane skew, DSP margin, CMIS firmware, thermal cycling, and interoperability. A factory can have enough assembly capacity but still miss shipments if test time is too long or yield learning is slow.

**Watch items:** test capex lead times, 1.6T test-cell throughput, yield disclosures from module vendors, hyperscaler qualification cycles, known-good optical die workflows, factory automation, and failure rates under AI traffic patterns.

### Thermal / liquid cooling

Thermal is part of the photonics supply chain because optical performance is temperature-sensitive and AI switches are power-dense. CPO makes this harder by putting optical engines near the switch ASIC. NVIDIA’s Quantum-X Photonics switches use a liquid-cooled design to cool onboard silicon photonics, according to NVIDIA-related ecosystem disclosures.[^nvidia-liquid] More broadly, Vertiv describes coolant distribution units and liquid cooling as necessary infrastructure for AI datacenters.[^vertiv-thermal]

**Thermal problem map:**

| Heat source / sensitivity | Why it matters | Supplier layer |
|---|---|---|
| Switch ASIC | 51.2T / 102.4T switches are high-power chips | cold plates, CDUs, facility water loops |
| Optical engines | optical wavelength, insertion loss, and modulator behavior drift with temperature | thermal isolation, heat spreaders, packaging materials |
| Lasers | laser efficiency and lifetime are temperature-sensitive | ELS placement, TEC decisions, monitoring |
| Pluggables | module front-panel airflow can limit power budget | cages, heatsinks, airflow design |
| CPO package | optics and ASIC share mechanical/thermal environment | advanced package thermal co-design |

**Public-equity map:**

| Company | Ticker | Exposure |
|---|---:|---|
| Vertiv | VRT | liquid cooling infrastructure, CDUs, power/cooling systems for AI datacenters |
| Eaton | ETN | power infrastructure; expanding thermal/liquid cooling through Boyd Thermal acquisition announced in 2025.[^eaton-boyd] |
| Schneider Electric | SU.PA | datacenter power/cooling infrastructure |
| Modine | MOD | datacenter thermal management and liquid cooling exposure |
| nVent | NVT | electrical/thermal infrastructure, racks, enclosures |
| Asetek | ASTK.CO | liquid cooling technology |
| CoolIT Systems | Private | direct liquid cooling for AI servers |
| Boyd | private/pending Eaton acquisition | thermal materials and liquid cooling |
| Coherent | COHR | advanced materials, thermoelectric / thermal photonics adjacency |

**CPO-specific thermal implications:**

- External lasers reduce thermal load inside the optical engine.
- Liquid cooling becomes more important as switch ASIC and photonics share a package/chassis.
- Thermal stability is a reliability issue, not just an efficiency issue.
- Field failure analysis must distinguish laser aging, photonic drift, connector contamination, and ASIC thermal stress.
- Cooling suppliers become indirect photonics enablers because a CPO switch cannot scale if optics cannot stay within a stable thermal window.

**Watch items:** liquid-cooled switch adoption, CPO cold-plate design wins, CDU capacity, facility water readiness, thermal interface materials, laser placement decisions, and reliability data from NVIDIA/Broadcom photonics switches.
