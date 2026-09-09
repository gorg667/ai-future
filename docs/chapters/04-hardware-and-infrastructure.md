# Hardware and Infrastructure: Chips, Datacenters, Energy, and the Physical Limits of AI

!!! abstract "In brief"
    - AI is bounded by a physical stack—TSMC, ASML, three HBM makers, CoWoS packaging—that is extraordinarily concentrated and slow to expand.
    - Power and grid interconnection, not chips, are now the binding constraint on US datacenter construction; responses include behind-the-meter gas, nuclear restarts, and multi-site training.
    - Global datacenter electricity roughly doubles to ~950 TWh (~3% of global) by 2030—large but absorbable globally, disruptive locally.
    - Export controls have slowed China's frontier and accelerated its chip industry; a Taiwan contingency is the single largest tail risk to everything in this document.

## Why the physical layer matters

AI is often discussed as if it were software—weightless, infinitely copyable, constrained only by ideas. It is not. Every token a frontier model produces is the result of trillions of arithmetic operations executed on silicon that had to be designed, fabricated in one of a handful of factories on Earth, packaged with memory, networked into clusters of hundreds of thousands of units, housed in buildings with specialized cooling, and fed with electricity at a scale comparable to a mid-sized city. The pace of AI progress over the next decade is bounded by how fast this physical stack can be built, and the geography of AI power is determined by who controls it.

This chapter covers the accelerator landscape (Nvidia and its challengers), the memory and packaging bottlenecks, networking and the shift to optics, the datacenter build-out and its power problem, the energy debate, alternative computing paradigms (photonic, neuromorphic, analog, quantum), and the semiconductor supply chain as a chokepoint.

## The accelerator landscape

### Nvidia's position

Nvidia holds roughly 80–90% of the market for AI training accelerators and a somewhat smaller but still dominant share of inference. Its position rests on three legs: hardware (the H100/H200 Hopper generation of 2022–2024; Blackwell B200/GB200 shipping in volume from late 2024, roughly 5 million units in 2025; and the Rubin generation announced January 2026 and shipping from the third quarter of 2026 after high-bandwidth-memory supply delays), software (CUDA and its two-decade ecosystem of libraries, which makes switching costly), and systems (NVLink interconnect and full-rack designs like the GB200 NVL72 and Vera Rubin NVL72/NVL144, sold as integrated units at $3.5–4 million per rack).

The Rubin GPU illustrates the generational cadence: roughly 336 billion transistors, up to 288 GB of HBM4 memory, about 22 TB/s of memory bandwidth, and a claimed multiple-fold improvement in inference throughput per watt over Blackwell. A specialized inference variant (Rubin CPX, with 128 GB of cheaper GDDR7 memory) targets long-context prefill. Nvidia's roadmap—Rubin Ultra in 2027, Feynman in 2028 with co-packaged optics—commits to an annual cadence that no competitor has matched. Datacenter revenue exceeded $150 billion annually in 2026, and the company's market capitalization has oscillated around $4–5 trillion.

### Challengers

**AMD** is the only merchant competitor at the frontier. The MI300X (2023) and MI325X/MI350 (2025) gained share in inference, particularly for open-weight models where the software stack (ROCm) matters less; the MI400 series (2026) targets training with a rack-scale design. AMD's share of AI accelerators is estimated at 5–10%. OpenAI's multi-gigawatt commitment to AMD (announced 2025) was the first major frontier-lab bet on a second supplier.

**Custom silicon** is the larger threat. Google's TPU is the most mature: the seventh generation (Ironwood, 2025) is used for both Gemini training and inference and is sold to external customers including, reportedly, Anthropic at multi-gigawatt scale. Amazon's Trainium 2 and 3 power Anthropic's Project Rainier cluster (hundreds of thousands of chips). Microsoft's Maia, Meta's MTIA, and OpenAI's own chip (developed with Broadcom, targeting 2026–2027) round out the hyperscaler programs. Analysts describe 2026 as the "custom silicon inflection": custom ASICs are estimated at 15–25% of AI accelerator spend and rising, because at hyperscaler volumes the savings of a chip tuned to one's own workloads exceed the costs of development. Broadcom and Marvell, which design these chips for the hyperscalers, have become major beneficiaries.

**Inference specialists**—Groq (deterministic SRAM-based chips with very high token throughput), Cerebras (wafer-scale chips with enormous on-chip memory), SambaNova, and others—have found niches in low-latency inference. Their share is small, but the direction matters: as inference grows to dominate compute demand, architectures optimized for it rather than for training gain ground.

**China's domestic accelerators** are covered below under export controls. Huawei's Ascend 910C (two 910B dies packaged together, fabricated at SMIC on a 7-nm-class process, roughly 60% of an H100 on inference) is the workhorse; the Ascend 950 series (2026) targets Blackwell-class performance with domestic HBM. Cambricon, Moore Threads, Biren, and others compete. Huawei's share of China's AI chip market rose from near zero in 2023 to an estimated 50–60% in 2026 as Nvidia's fell from 95% to a minority.

### The efficiency trend

Epoch estimates that AI chip performance per dollar has risen about 49% per year since 2023 in constant dollars, with gains arriving in steps as spending shifts to each new generation. Performance per watt improves at a similar rate. Across a decade this compounds to roughly 50× more compute per dollar. A key contributor is lower-precision arithmetic: training has moved from FP32 to BF16 to FP8, and inference to FP4 and below, each halving of precision roughly doubling throughput. Precision cannot fall indefinitely—below 4 bits, quality degradation becomes hard to manage—so this particular lever is nearing exhaustion, and future gains must come from architecture, packaging, and process.

## Memory and packaging: the real bottleneck

The arithmetic units on a GPU are rarely the constraint; feeding them data is. Large language model inference is memory-bandwidth-bound: each generated token requires reading the entire set of model weights (or the active experts, for MoE models) plus the growing key-value cache from memory. This has made **high-bandwidth memory (HBM)**—stacks of DRAM dies bonded directly next to the processor—the most critical and most constrained component in the AI supply chain.

HBM is manufactured by three companies: SK Hynix (the leader, with roughly half the market), Samsung, and Micron. Capacity has been sold out for years ahead; HBM4, the generation required for Rubin and its competitors, entered volume production in 2026 after yield problems that delayed Nvidia's schedule. HBM is also where Chinese accelerators are most constrained—CXMT's domestic HBM lags by several generations—and where export controls have bitten hardest.

**Advanced packaging** is the second bottleneck. Connecting GPU dies to HBM stacks requires TSMC's CoWoS (chip-on-wafer-on-substrate) process or equivalents. CoWoS capacity roughly tripled between 2024 and 2026 and remains fully booked. Nvidia is estimated to consume more than half of it. Intel's Foveros and EMIB, Samsung's I-Cube, and domestic Chinese alternatives are less mature. Huawei cannot access CoWoS at all and uses monolithic or less advanced approaches.

Beyond HBM, the industry is exploring processing-in-memory, larger SRAM caches (the Cerebras and Groq approach), and new memory hierarchies for the KV-cache problem. None is a near-term substitute for more HBM.

## Networking: from copper to light

Training a frontier model requires tens to hundreds of thousands of accelerators to exchange gradients and activations continuously. Inference of large MoE models across many chips requires similar communication. Networking has therefore become a first-order design constraint and a large fraction of cluster cost.

Two scales matter. **Scale-up** networking connects chips within a rack or pod at maximum bandwidth—Nvidia's NVLink (1.8 TB/s per GPU in Blackwell, higher in Rubin), Google's ICI, and the emerging open UALink standard. **Scale-out** networking connects racks across the datacenter—InfiniBand (Nvidia/Mellanox) and increasingly Ethernet with AI-specific extensions (the Ultra Ethernet Consortium), at 800 Gb/s per port moving to 1.6 Tb/s.

The physical limit being hit is that copper cannot carry these bandwidths more than a meter or two, and pluggable optical transceivers consume substantial power (a significant fraction of a cluster's non-compute energy). The response is **co-packaged optics (CPO)**: integrating the optical engine directly onto the switch or accelerator package. Nvidia announced CPO for its Spectrum-X and Quantum-X switches in 2025 and for the Feynman GPU platform in 2028; Broadcom, Lightmatter, Ayar Labs, and others are shipping or sampling; the Open Compute Project began standardizing CPO interfaces in 2026. The transition from electrical to optical interconnect inside the datacenter is the largest change to computing architecture in decades and is essential for the multi-gigawatt clusters now being planned.

## The datacenter build-out

### Scale

The largest AI datacenter campuses under construction or planned as of 2026:

| Campus | Owner | Location | Scale (planned) | Notes |
|---|---|---|---|---|
| Colossus 2 | xAI | Memphis, Tennessee | >1 GW; ~1.1M H100-equivalents | Largest known operational (Epoch) |
| Hyperion | Meta | Richland Parish, Louisiana | 2 GW → 5 GW; ~3.7M H100e by 2028 | Largest planned in US |
| Prometheus | Meta | New Albany, Ohio | ~1 GW (2026) | Gas-powered |
| Stargate Abilene | OpenAI / Oracle / Crusoe | Abilene, Texas | 1.2 GW+ | First Stargate site; further sites in TX, NM, OH, MI, WI |
| Fairwater | Microsoft | Wisconsin, Atlanta, others | Multi-GW across sites | "AI superfactory" networked across sites |
| Project Rainier | Amazon / Anthropic | Indiana and others | ~2.2 GW; hundreds of thousands of Trainium | Anthropic training |
| Stargate UAE | OpenAI / G42 / others | Abu Dhabi | 1 GW (first phase), 5 GW campus | Largest outside US |
| Humain | Saudi PIF | Saudi Arabia | Multi-GW planned | Sovereign |
| Various | Alibaba, ByteDance, Tencent, China Telecom | China (Inner Mongolia, Guizhou, etc.) | Multi-GW aggregate | Domestic chips increasingly |

The total AI datacenter capacity globally is estimated at 30–50 GW in 2026 and on track for 100+ GW by 2030. For scale, a gigawatt is the output of a large nuclear reactor and the consumption of roughly 750,000 US homes.

### The power problem

Power, not chips or capital, is now the most frequently cited constraint on datacenter construction in the United States. The reasons:

- **Interconnection queues.** Connecting a gigawatt load to the grid requires transmission studies and upgrades that take three to seven years in most US regions. Utilities in Virginia, Texas, Georgia, and Arizona have queues of tens of gigawatts of requested datacenter load.
- **Equipment supply.** Large power transformers have lead times of two to four years; gas turbines from GE Vernova, Siemens Energy, and Mitsubishi are sold out into 2028–2029; switchgear and cabling are constrained.
- **Generation.** New generation takes years. Solar and batteries are fastest but intermittent; gas plants are the default for firm power; nuclear is the long-term aspiration.

The responses have been creative and sometimes controversial:

- **Behind-the-meter generation.** xAI's Memphis site ran on dozens of mobile gas turbines before grid connection, drawing air-quality complaints. Meta's Prometheus and several Stargate sites include dedicated gas plants. This bypasses the interconnection queue but locks in fossil generation.
- **Nuclear restarts and PPAs.** Microsoft's agreement to restart Three Mile Island Unit 1 (renamed Crane, targeting 2027, ~835 MW); Meta's January 2026 agreements with Vistra, TerraPower, and Oklo for up to 6.6 GW by 2035, including a 20-year, 1.1-GW deal with Constellation's Clinton plant; Amazon's Susquehanna and X-energy deals; Google's Kairos Power SMR agreement. The Carnegie Endowment and others have cautioned that most of this capacity is either existing plants relabeled or new plants that will not deliver before the 2030s.
- **Geographic dispersion.** Training across multiple sites connected by high-bandwidth fiber (Microsoft's Fairwater network; Google's multi-datacenter Gemini training) relaxes single-site power limits.
- **Demand flexibility.** Datacenters agreeing to curtail during grid peaks in exchange for faster interconnection—a Duke University study estimated that flexible loads could add tens of gigawatts to US grids without new generation.
- **Going where power is.** Gulf states (cheap gas, sovereign capital), Nordic countries (hydro, cooling), Texas (deregulated market, fast permitting), and parts of the US Midwest have become datacenter magnets.

## The energy debate

### How much electricity does AI use?

The International Energy Agency's base case has global datacenter electricity consumption roughly doubling from about 485 TWh in 2025 to about 950 TWh in 2030—around 3% of global electricity—and reaching 1,300 TWh by 2035. AI-specific consumption is a growing share of that, perhaps a third to a half by 2030. In the United States, datacenters used about 4–5% of electricity in 2025 and are projected by the IEA and Lawrence Berkeley National Laboratory to reach 9–12% by 2030, with the IEA estimating US datacenter demand growing 130% over the period. Ireland, where datacenters already consumed over 20% of electricity, has imposed connection moratoria; Virginia's Loudoun County is the densest datacenter cluster on Earth.

### Is it a lot?

Both framings are true. Globally, 3% of electricity is comparable to aviation's share of emissions—significant but not dominant; air conditioning, industrial heat, and transport are far larger. Datacenter growth is also a small fraction of the overall electricity growth expected from electrification of vehicles, heating, and industry in the 2030s. Locally, however, a 2-GW campus in a rural county is a shock to grid planning, water use, and land use, and utility rate cases in several states have become political fights over who pays for grid upgrades that serve datacenters.

The per-query energy of a chatbot interaction is modest—Google reported in 2025 that a median Gemini text prompt used about 0.24 Wh, roughly nine seconds of television—but total usage is what matters, and reasoning models and agents multiply tokens per task by one to three orders of magnitude. Video generation is far more energy-intensive than text.

### Carbon

Hyperscalers' 2030 net-zero commitments have collided with AI growth: Microsoft's and Google's reported emissions rose 30–50% between 2020 and 2025. Their response has been to sign unprecedented volumes of clean-power contracts (the hyperscalers are the largest corporate buyers of renewables and nuclear in the world), to invest in geothermal (Fervo), fusion (Helion, Commonwealth Fusion), and advanced nuclear, and to argue that AI-enabled efficiency gains elsewhere will offset datacenter emissions. Critics point out that near-term marginal generation is largely gas. The honest summary is that AI is a meaningful but not decisive factor in the global energy transition, and that its net effect on emissions depends on policy and on whether the efficiency claims materialize.

### Water

Datacenter cooling uses water directly (evaporative cooling) and indirectly (thermoelectric generation). Estimates for large campuses run to millions of gallons per day. The industry is shifting toward closed-loop and liquid cooling (which Blackwell and Rubin racks require anyway, at 100+ kW per rack) and toward siting in cooler or wetter regions, but water has become a local siting issue in Arizona, Texas, Chile, Uruguay, and Spain.

## Alternative computing paradigms

Digital CMOS accelerators will dominate through 2030. But their limits are visible—Moore's Law transistor scaling has slowed to roughly 2× every three years, power density is at the edge of what liquid cooling can remove, and memory bandwidth is the binding constraint—and several alternatives are being pursued.

**Photonic computing.** Beyond optical interconnect (which is happening), some companies (Lightmatter, Lightelligence, Q.ANT, and others) are building processors that perform matrix multiplication with light, promising very high throughput at low power. Demonstrations exist; commercial products for general AI workloads do not yet. The interconnect application is the near-term win; photonic *compute* is a 2030s question.

**Neuromorphic and analog computing.** Chips that mimic spiking neurons (Intel Loihi, IBM NorthPole, BrainChip) or compute in the analog domain (Mythic, IBM's analog AI research) offer large energy savings for specific workloads, particularly edge inference. They have not been competitive for large-scale training or LLM inference and are unlikely to be before 2030.

**In-memory computing.** Performing arithmetic inside memory arrays (using resistive RAM, phase-change memory, or SRAM) eliminates the data-movement bottleneck. Samsung, SK Hynix, and academic groups have demonstrations; the technology is likely to appear first as accelerator components rather than as standalone processors.

**Quantum computing.** Quantum computers are not a substitute for AI accelerators and will not run neural networks faster in any relevant timeframe. Their relevance to AI is indirect: quantum simulation of chemistry and materials could generate training data and validate AI-predicted molecules; and AI is being used to design quantum error-correction codes and control systems. Progress in quantum hardware has been real—Google's Willow chip (2024) demonstrated below-threshold error correction; IBM, Quantinuum, IonQ, and others have roadmaps to fault-tolerant machines in the early 2030s—but "quantum AI" as a near-term capability multiplier is mostly marketing.

**Biological and reversible computing.** Speculative. Reversible computing (avoiding the energy cost of erasing bits) has theoretical appeal as the Landauer limit approaches, and a few startups (Vaire) are pursuing it; biological computing with living neurons (Cortical Labs) is a research curiosity.

The realistic 2030 hardware stack is: advanced digital accelerators (Nvidia, Google, AMD, custom) on 2-nm and 1.4-nm-class processes with backside power delivery and gate-all-around transistors, stacked with HBM4E/HBM5, connected by co-packaged optics, in liquid-cooled racks of 200–600 kW, in campuses of one to ten gigawatts. The gains will come from packaging, precision, architecture specialization, and scale more than from transistor density.

## The semiconductor supply chain as chokepoint

### Concentration

The AI hardware supply chain is extraordinarily concentrated:

- **Leading-edge logic fabrication:** TSMC (Taiwan) produces roughly 90% of the world's most advanced chips, including every Nvidia, AMD, Google, and Apple AI chip. Samsung is a distant second; Intel is attempting to re-enter with its 18A process. TSMC's Arizona fabs began volume production in 2025 but represent a small fraction of capacity and lag Taiwan by a node.
- **Lithography:** ASML (Netherlands) is the sole supplier of extreme-ultraviolet lithography machines, without which sub-7-nm production is impractical.
- **HBM:** SK Hynix, Samsung (both Korea), Micron (US).
- **Advanced packaging:** TSMC, with Intel and Samsung far behind.
- **Design tools:** Synopsys and Cadence (US) dominate electronic design automation.
- **Chemicals and materials:** Japan (photoresists, wafers), with some concentration in single suppliers.

This concentration is why Taiwan's security is an AI question, why the Netherlands and Japan were brought into US export controls, and why every major economy has launched a subsidy program (the US CHIPS Act, the EU Chips Act, Japan's Rapidus, Korea's K-Chips Act, China's Big Fund and successors).

### Export controls

The United States has since October 2022 restricted the export to China of advanced AI accelerators, the equipment to make them, and (from 2024–2025) HBM. The rules have been revised repeatedly: the H800/A800 workarounds were closed in October 2023; the H20 (a deliberately hobbled chip) was permitted, then restricted in April 2025, then permitted with a revenue-share arrangement in mid-2025, then complicated by Chinese government discouragement of its purchase; the Biden-era "AI diffusion rule" tiering the world into three groups was rescinded by the Trump administration in May 2025 and replaced by bilateral deals (notably with the UAE and Saudi Arabia, permitting large accelerator exports in exchange for security commitments). Chapter 14 covers the geopolitics.

The technical effect: Chinese laboratories have access to far less compute than US laboratories—Epoch and others estimate the gap at roughly an order of magnitude at the frontier—and must rely on smuggled Nvidia chips, pre-ban inventory, remote access to overseas clouds, and domestic accelerators that are one to two generations behind and constrained by HBM and packaging. Yet Chinese models trail the frontier by only six to eight months, because algorithmic efficiency (DeepSeek's innovations; heavy use of MoE and distillation) and open-weight collaboration have substituted for compute. The controls have slowed China's frontier and accelerated its domestic chip industry. Huawei planned to double Ascend 910C output to around 600,000 units in 2026 and is ramping the Ascend 950; SMIC is producing 7-nm and attempting 5-nm-class chips without EUV, at poor yields and high cost. Most analysts expect China to reach rough parity in accelerator *design* by 2028–2030 while remaining behind in *manufacturing* volume and memory for longer.

## What to expect: hardware and infrastructure through 2030

| Dimension | 2026 | 2028 (projection) | 2030 (projection) |
|---|---|---|---|
| Leading accelerator | Nvidia Blackwell Ultra / Rubin; TPU v7 | Rubin Ultra / Feynman; TPU v8–9; OpenAI custom | 1.4-nm-class; co-packaged optics standard |
| Chip price-performance | ~1.5×/year | ~1.4×/year | ~1.3×/year (precision gains exhausted) |
| Largest cluster | ~1 GW; ~1M H100e | ~3–5 GW; ~5M H100e | ~5–10 GW; multi-site training routine |
| Global AI DC power | ~30–50 GW | ~70–100 GW | 100–150 GW |
| Global DC electricity | ~500 TWh | ~750 TWh | ~950–1,100 TWh (IEA) |
| Nvidia share of accelerators | ~80% | ~65–75% | ~55–70% |
| Custom ASIC share | ~15–25% | ~25–35% | ~30–40% |
| China domestic accelerator share (China market) | ~50–60% | ~70–80% | ~85–95% |
| Frontier training run | 10²⁶–3×10²⁷ FLOP; ~$1B+ | ~10²⁸ FLOP; ~$10B | ~10²⁹ FLOP; ~$50–100B |
| Binding constraint | HBM, CoWoS, power interconnection | Power, capital | Capital, power, latency wall |

The overall picture is that the physical layer can support continued scaling through 2030 at enormous cost, with power and capital replacing chips as the binding constraints, optics replacing copper, and custom silicon eroding but not ending Nvidia's dominance. The wildcard is a Taiwan contingency, which would halt the frontier for years; it is the single largest tail risk to the entire trajectory described in this document.
