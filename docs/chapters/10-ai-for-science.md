# AI for Science: From Instrument to Participant

!!! abstract "In brief"
    - AI is the most important new scientific instrument since the computer; its contribution to genuinely novel discovery is small but rising steeply.
    - Mathematics is furthest along (perfect IMO scores, open Erdős problems resolved); structural biology is solved; drug discovery is compressed at the front end but not in trials.
    - The 2026 Mythos-class models made the first specific, testable 'AI scientist' claims (10× drug-design acceleration, independently corroborated hypotheses); they await replication.
    - The experimental bottleneck—not intelligence—determines how fast AI science becomes transformative.

## The stakes

Of all the things AI might do, accelerating science is the one with the largest potential upside and the one most likely to be underestimated. Economic growth over the long run is driven almost entirely by the accumulation of knowledge. Since the mid-twentieth century, the rate of scientific progress per researcher has fallen—it takes more scientists, more money, and more time to produce each successive breakthrough (Bloom et al., "Are Ideas Getting Harder to Find?", 2020). If AI can reverse that trend, even modestly, the compounding effect over decades dwarfs any direct productivity gain from automating existing work. If it can do more than that—if AI systems can become genuine scientific participants, generating and testing hypotheses at machine speed—the consequences are hard to bound.

This chapter surveys what AI has actually done in science through 2026, domain by domain; the emergence of "AI scientist" systems; the bottlenecks that separate impressive results from transformed fields; and what to expect through the early 2030s. The summary: **AI is already the most important new scientific instrument since the computer, its contribution to genuinely novel discovery is small but rising steeply, and the physical-world bottlenecks (experiments, trials, manufacturing) will determine how fast that contribution becomes transformative.**

## Structural biology and the AlphaFold revolution

The paradigmatic success. Protein structure prediction—inferring a protein's three-dimensional shape from its amino-acid sequence—was a fifty-year grand challenge. DeepMind's AlphaFold 2 (2020, published 2021) solved it to experimental accuracy for most proteins; the AlphaFold Protein Structure Database released predicted structures for essentially every known protein (over 200 million). Demis Hassabis and John Jumper shared the 2024 Nobel Prize in Chemistry with David Baker, whose lab pioneered computational protein design.

The effects have been broad and measurable. Over three million researchers have used AlphaFold; it is cited in tens of thousands of papers; it has accelerated work on malaria vaccines, antibiotic resistance, plastic-degrading enzymes, and countless basic-biology questions. AlphaFold 3 (May 2024) extended prediction to complexes—proteins with DNA, RNA, ligands, and other molecules—which is what drug discovery requires. Open competitors (Boltz, Chai, RoseTTAFold) reproduced and extended the capability. Protein *design* (generating new proteins with specified functions, via diffusion models like RFdiffusion and language models like ESM) moved from academic demonstration to companies (Generate Biomedicines, Profluent, EvolutionaryScale, Latent Labs) producing novel binders, enzymes, and antibodies.

The lesson: where a scientific problem has (a) abundant structured data, (b) a clear objective, and (c) a way to verify predictions, AI can solve it outright. Structural biology had all three (the Protein Data Bank's 200,000 experimentally solved structures; the CASP competition as a benchmark; crystallography for verification).

## Drug discovery

The natural next step—and the domain where the gap between promise and delivery is widest. AI is now used across the pipeline: target identification (mining genomic and literature data), hit discovery (screening virtual libraries of billions of molecules), lead optimization (predicting binding, toxicity, and pharmacokinetics), and clinical-trial design and patient selection.

Progress markers as of 2026:

- Dozens of AI-discovered or AI-designed molecules have entered clinical trials. Insilico Medicine's rentosertib (for idiopathic pulmonary fibrosis), the first drug with both an AI-discovered target and AI-generated structure, completed a positive Phase 2a in 2025 and moved toward later-stage trials. Recursion, Exscientia (merged with Recursion), Relay, Schrödinger, Iambic, Generate, and others have candidates in Phase 1–2.
- Isomorphic Labs (Alphabet's drug-discovery company built on AlphaFold) entered its first clinical trials with AI-designed oncology and immunology candidates in 2026, backed by partnerships with Eli Lilly and Novartis worth up to $3 billion and its own $600 million raise.
- Every major pharmaceutical company has AI partnerships and internal programs; Nvidia's BioNeMo and similar platforms are standard infrastructure.

What has not yet happened: no AI-discovered drug has completed Phase 3 and reached approval on the strength of its AI origin. The reason is structural. AI compresses the discovery phase (from years to months) but clinical trials—the expensive, slow, and highest-failure part of the pipeline—operate on human biology and regulatory timelines that AI does not speed up. A drug discovered in 2024 reaches the market, if it succeeds, around 2030–2032. The first approvals of AI-designed drugs are plausible by 2027–2028; whether AI drugs *succeed more often* in trials (the real prize—current failure rates are around 90%) will not be known statistically until the early 2030s. Early signals (Phase 1 success rates for AI-derived molecules appear higher than historical averages, though sample sizes are small and selection effects are likely) are encouraging.

The frontier is "virtual cells" and "digital twins"—models of cellular biology detailed enough to simulate the effect of an intervention before trying it. The Arc Institute's Evo (genome-scale language models), the Chan Zuckerberg Initiative's virtual-cell program, and several startups are pursuing this. Success would shift biology from an experimental to a partially computational science.

## Mathematics

Mathematics is where AI's move from tool to participant is most visible, because verification is perfect (a proof is checkable) and no physical experiment is needed.

- **Competition mathematics is solved.** AlphaGeometry (January 2024) reached near-gold IMO geometry; AlphaProof and AlphaGeometry 2 (July 2024) reached silver on the full IMO; OpenAI and DeepMind systems achieved gold (5/6) in July 2025 with natural-language proofs graded by former medalists; at the July 2026 IMO in Shanghai, at least six systems—GPT-5.6 Pro, Claude Opus 5 and Fable 5, Kimi K3, Xiaohongshu's dots-note-3.0, and a Huawei model—scored a perfect 42/42, a result only about seven human contestants achieved. Olympiad mathematics is no longer a discriminating test.
- **Research-level problems are falling.** FrontierMath's research-tier problems went from 2% (2024) to substantial fractions solved (2026). In 2025–2026, frontier models and specialized systems contributed to resolving several open problems: DeepMind's AlphaProof Nexus (2026) autonomously resolved 9 of 353 open Erdős problems and proved 44 conjectures from the Online Encyclopedia of Integer Sequences, with formal Lean proofs; mathematicians working with GPT-5-class models reported solutions to long-open Erdős problems, often by locating and adapting overlooked literature (an important form of contribution, though not the same as novel insight) and sometimes by genuinely new arguments. A systematic 2026 survey categorized AI contributions to Erdős problems into six types ranging from literature retrieval to complete novel proofs.
- **AlphaEvolve** (DeepMind, May 2025) used an evolutionary search over code generated by Gemini to discover improved algorithms: a faster method for 4×4 complex matrix multiplication (the first improvement on Strassen's 1969 result for that case), better solutions to a dozen open problems in combinatorics and analysis (the kissing number in 11 dimensions, several packing problems), and practical speedups to Google's datacenter scheduling and TPU design. Successor systems in 2026 extended this to broader mathematical discovery.
- **Formalization.** Lean's Mathlib library, the formalization of major results (Fermat's Last Theorem project, the Polynomial Freiman–Ruzsa conjecture in weeks), and AI-assisted autoformalization are making machine-checkable mathematics the norm for AI–human collaboration.

Terence Tao, the most prominent mathematician engaging with these tools, has described the trajectory as moving from "AI as a very good graduate student who needs supervision" toward genuine collaborator, while noting that the hardest part of research mathematics—knowing which questions matter—remains human. The author expects that by 2028 AI systems will routinely resolve open problems of moderate difficulty in most areas of mathematics and will be co-authors on a meaningful fraction of papers; the resolution of a problem of Fields-Medal significance primarily by AI is plausible before 2032.

## Weather, climate, and earth science

A quiet revolution. Numerical weather prediction—simulating atmospheric physics on supercomputers—was one of the great achievements of twentieth-century computing. Between 2022 and 2024, machine-learning models (Huawei's Pangu-Weather, Nvidia's FourCastNet, DeepMind's GraphCast and then GenCast, ECMWF's AIFS, Microsoft's Aurora) trained on decades of reanalysis data matched or exceeded the accuracy of the best physics-based systems for medium-range forecasts while running in seconds on a single chip rather than hours on a supercomputer. GenCast (December 2024) beat ECMWF's ensemble on 97% of metrics for up to 15 days. By 2026 the European Centre runs AIFS operationally alongside its physical model; national weather services worldwide are adopting hybrid approaches; and AI forecasts outperform traditional models on most metrics. Extreme-event prediction (hurricane tracks, heat waves) has improved measurably, with direct consequences for disaster preparedness. Climate modeling (long-range, with coupled ocean–atmosphere dynamics) is harder because there is less data and the physics matters more, but AI emulators are accelerating it.

## Materials and chemistry

DeepMind's GNoME (November 2023) predicted 2.2 million new crystal structures, of which 380,000 were estimated stable—a claimed order-of-magnitude increase in known stable materials, though subsequent analysis found many were trivial variants or duplicates. Microsoft's MatterGen and MatterSim (2024–25), Meta's OMat24 dataset, and Orbital, CuspAI, Periodic Labs (founded 2025 by former OpenAI and DeepMind researchers with $300 million to build autonomous materials labs), and Lila Sciences pursue the same goal: AI-driven discovery of batteries, catalysts, superconductors, and carbon-capture materials.

The bottleneck here is synthesis and testing. Predicting a material is fast; making it and measuring its properties is slow, and many predicted materials cannot be synthesized. Self-driving laboratories—robotic systems that synthesize and characterize materials autonomously (Lawrence Berkeley's A-Lab, the Acceleration Consortium in Toronto, and commercial equivalents)—close the loop, but at scales of hundreds of samples per week, not the millions that computation produces. The economically consequential results (a better battery cathode, a cheaper catalyst for green hydrogen) are plausible before 2030 and would be among the first cases where AI-driven science visibly changes an industry.

Chemistry more broadly has seen AI for retrosynthesis planning (mature and in commercial use), reaction prediction, and spectroscopy interpretation. Quantum-chemistry emulators (neural network potentials replacing density functional theory) are making molecular simulation orders of magnitude faster.

## Physics, astronomy, and fusion

AI processes the data floods of modern experiments: the LHC's trigger systems, gravitational-wave detection, galaxy classification, exoplanet identification. DeepMind's collaboration with the Swiss Plasma Center (2022) demonstrated RL control of tokamak plasma; Commonwealth Fusion, TAE, and others use AI for plasma control and design optimization. In theoretical physics, AI systems have rediscovered known laws from data (AI Feynman and successors) and begun proposing new candidate relations. The 2026 frontier is AI systems that propose experiments; the long-term question is whether AI can produce conceptual breakthroughs (new theories) as opposed to solutions within existing frameworks. No clear example exists yet.

## Neuroscience, genomics, and medicine

Genomic language models (Evo 2, Nucleotide Transformer, and others) predict the effects of mutations and design sequences; CRISPR guide design and delivery optimization are AI-assisted; single-cell atlases are being organized by foundation models. In neuroscience, AI decodes neural activity (brain-to-text and brain-to-speech interfaces reached practical fluency in 2024–2026, with Neuralink, Synchron, Paradromics, and academic groups in clinical trials) and models of the visual cortex derived from deep networks are among the field's best.

In clinical medicine, the results are more mixed: AI matches specialists in imaging and diagnostic reasoning benchmarks (Chapter 12), but randomized trials of AI-assisted diagnosis show smaller gains than expected, partly because physicians do not use the tools optimally. Medicine illustrates that scientific capability and practical impact are separated by human systems.

## The "AI scientist"

### What exists

By 2026 several systems attempt to automate the research loop itself:

- **Google's AI co-scientist** (February 2025), a multi-agent Gemini system that generates, debates, and ranks hypotheses. In validation studies it independently proposed a mechanism for bacterial gene transfer that a laboratory had discovered but not yet published, and suggested drug repurposing candidates for leukemia that were validated in vitro.
- **FutureHouse** (a nonprofit backed by Eric Schmidt) released a platform of agents (Crow, Falcon, Owl, Phoenix) for literature search, synthesis, and chemistry, and its Robin system, which in 2025 proposed and (with human execution) validated a candidate treatment for dry age-related macular degeneration. Its Kosmos system (late 2025) ran multi-day autonomous research cycles producing reports whose claims were largely reproducible on audit.
- **Sakana's AI Scientist** (2024–25) generated complete machine-learning papers end to end; one passed peer review at an ICLR workshop in a controlled experiment. **Autoscience's Carl** and similar systems followed.
- **Frontier laboratories** describe internal use of models for experiment design, code, and analysis in AI research itself—the recursive application discussed in Chapter 17. OpenAI's stated goal (2025) is an "automated AI research intern" by 2026 and an "automated researcher" by 2028; Anthropic has made similar statements about compressing "decades of progress into years" in biology. Anthropic's June 2026 launch of Claude Mythos 5 included the most concrete claims yet: its protein-design experts reported roughly a tenfold acceleration of parts of the drug-design process, with the model choosing binding sites, running design tools, and recovering from failures without human assistance on 14 targets (nine yielding strong candidates); in blinded comparisons its molecular-biology hypotheses were preferred about 80% of the time over the previous generation's, with one—a mechanism for an *E. coli* protein—independently corroborated by a laboratory working on the same problem; and in a week of largely autonomous work it assembled single-cell data across 138 species and trained a model that outperformed a recently published *Science* paper at a hundredth the size. These are the developer's own claims and await independent replication, but they are specific and testable in a way that earlier "AI scientist" claims were not.
- **Anthropic's Claude for Life Sciences, OpenAI's science initiatives, and Microsoft Discovery** are productized research assistants used across pharma and academia.

### Assessment of contribution

The honest evaluation as of September 2026: AI scientist systems produce competent, incremental, increasingly useful work; they have generated a growing number of validated novel findings, including at least one independently corroborated mechanistic hypothesis in molecular biology; they have not yet produced a result that the field regards as a major discovery attributable primarily to the AI. The gap between "useful collaborator" and "major discovery" narrowed visibly in 2026, particularly with the Mythos-class models, and the author's forecast dates below have moved earlier by about a year relative to what would have been written in early 2026. Their contributions are strongest in literature synthesis (finding connections across a corpus no human can read), hypothesis enumeration, code and analysis, and mathematical/computational domains with built-in verification. They are weakest at taste—choosing important problems—and at the experimental execution that most sciences require.

The rate of improvement is fast. The number of papers with substantive AI contribution is rising steeply; the fraction of arXiv submissions in some fields with AI-generated text is estimated at over a third; and the peer-review system is straining under volume (leading venues report submission growth of 30–50% per year and have begun using AI to review AI-written papers, with predictable concerns). A "reproducibility and quality" crisis in the literature is a plausible near-term side effect.

## Bottlenecks

Why has AI's scientific impact, though real, not yet been transformative?

1. **The experimental bottleneck.** Most sciences require physical experiments. Computation can propose; only experiment can confirm. Self-driving labs, cloud labs (Emerald, Strateos), and high-throughput automation are expanding throughput, but by factors of ten, not a million. Fields with cheap or virtual experiments (mathematics, computer science, computational chemistry, weather) move fastest; fields with expensive ones (clinical medicine, ecology, particle physics) slowest.
2. **The data bottleneck.** Structural biology succeeded because of the Protein Data Bank—decades of curated experimental data. Most fields lack an equivalent. Materials, chemistry, and biology are now building them, often with AI-driven labs as the generator.
3. **The verification bottleneck.** Outside mathematics and code, AI outputs must be checked by humans or by experiment. Scientific literature is full of errors, and AI trained on it inherits them.
4. **The taste bottleneck.** Knowing which questions matter is the scarcest scientific skill and the one AI shows least. AI scientists produce many plausible hypotheses; humans still select.
5. **The institutional bottleneck.** Funding cycles, publication norms, regulatory approval, and career incentives operate on multi-year timescales that AI does not accelerate. A drug trial takes as long as it takes.
6. **The conceptual bottleneck.** Revolutionary science—new frameworks, not solutions within frameworks—may require something current AI does not do. Or it may emerge from scale and search. This is unknown.

## Forecast

| Domain | 2026 | 2028 | 2032 |
|---|---|---|---|
| Mathematics | Open problems occasionally resolved; competition math solved | AI routinely resolves moderate open problems; co-author on many papers | Major (Fields-level) result with AI as primary contributor plausible |
| Structural biology / protein design | Solved prediction; design in commercial use | Designed proteins in clinic routinely | Designed enzymes/binders as standard tools |
| Drug discovery | Dozens of AI-derived candidates in Phase 1–2 | First approvals of AI-designed drugs | Evidence on whether AI drugs succeed more often; discovery time halved industry-wide |
| Materials | Predictions abundant; synthesis bottleneck | Self-driving labs at scale; first commercially significant AI-discovered material | Materials discovery routinely AI-led |
| Weather | AI operational at major centers | AI-hybrid standard; extreme-event skill improved | Climate emulation at high resolution |
| AI scientist systems | Competent assistants; few validated novel findings | Routine autonomous incremental research in computational fields | Substantial fraction of published research AI-led in some fields |
| Peer review / literature | Straining | AI-mediated review; provenance standards | Restructured publication norms |

The larger question—whether AI-accelerated science produces a discontinuity in the rate of human progress—depends on the bottlenecks above, and especially on the experimental one. The author's view is that the 2026–2030 period will show AI transforming the *computational* sciences and the *discovery* phases of the experimental sciences, with the *validation* phases catching up through automation over the 2030s. The compounding effect on economic growth will be visible in the statistics with a lag; the compounding effect on AI research itself is the subject of Chapter 17.
