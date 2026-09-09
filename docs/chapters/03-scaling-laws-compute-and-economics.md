# Scaling Laws, Compute, and the Economics of Training

## The central question

Almost every disagreement about the future of AI reduces to a disagreement about scaling: whether pouring more compute, data, and engineering into current methods will keep producing capability gains, and if so for how long and at what cost. If scaling continues, the trend lines of the last decade imply systems by 2030 that are qualitatively beyond anything now deployed. If it stalls, the current generation of models—very capable but jagged and unreliable—may be roughly what we live with for a long time, improved at the margins.

This chapter lays out what scaling laws actually say, the empirical record, the three inputs (compute, data, algorithms) and their trends, the shift from pretraining to post-training and inference-time scaling, the economics of frontier training runs, and the case for and against continued scaling through 2030.

## What scaling laws say

### The original findings

Kaplan et al. (2020) trained hundreds of transformer language models across a range of sizes and found that test loss *L* followed power laws in three quantities, each measured with the others held non-limiting:

- In parameters *N*: L(N) ∝ N^(−0.076)
- In dataset size *D* (tokens): L(D) ∝ D^(−0.095)
- In compute *C* (FLOP): L(C) ∝ C^(−0.050)

The exponents are small, meaning that reducing loss requires large multiplicative increases in inputs, but the relationships held across seven orders of magnitude without bending. The paper's most consequential claim was that the returns to scale showed no sign of saturating within the range tested.

Hoffmann et al. (2022, "Chinchilla") corrected the allocation. Kaplan's recipe had implied that compute should go mostly to parameters; Chinchilla found that data and parameters should scale roughly equally, with about 20 tokens of training data per parameter for compute-optimal training. A 70-billion-parameter model trained on 1.4 trillion tokens outperformed the 280-billion-parameter Gopher. This finding reshaped the industry: subsequent frontier models were trained on far more data relative to their size, and the "data wall" (Chapter 5) became a concern precisely because the Chinchilla recipe demanded so much of it.

Subsequent work refined the picture. Models are now often *overtrained* relative to Chinchilla-optimal—trained on more tokens than the compute-optimal recipe—because a smaller model trained longer is cheaper to serve at inference, and inference costs dominate over a model's lifetime. Llama 3's 8-billion-parameter model was trained on 15 trillion tokens, roughly 1,900 tokens per parameter, nearly a hundred times the Chinchilla ratio.

### What loss buys

Loss—the model's average surprise at the next token—is not capability. The link between them is empirical and non-linear. Some capabilities improve smoothly with loss; others appear to emerge suddenly at a threshold (in-context learning, chain-of-thought reasoning, certain arithmetic). Schaeffer et al. (2023) argued that many "emergent" capabilities are artifacts of discontinuous metrics—a task scored pass/fail looks emergent when the underlying continuous probability of correctness is rising smoothly. The debate matters for forecasting: smooth scaling makes capability predictable; genuine emergence means surprises in both directions.

The practical position most researchers hold: aggregate benchmark performance scales predictably enough with compute that laboratories plan training runs around it, and Epoch AI and others can fit trend lines that have held for years. But the *specific* capabilities that appear at each level are not predictable in advance, and there are surprises—both pleasant (in-context learning, tool use generalization) and unpleasant (persistent hallucination, sycophancy).

### Scaling beyond language

The same power-law structure has been found in vision transformers, speech, protein models, video generation, and reinforcement learning from human feedback. Mixture-of-experts models follow their own scaling laws. Scaling laws for reasoning models relate performance to inference compute (Chapter 7). The generality of the phenomenon is why "scale" is treated as a fundamental lever rather than a trick specific to text.

## The three inputs and their trends

### Compute

Epoch AI, which maintains the most careful public database, finds:

- Training compute for notable AI models has grown about **4.5× per year** since 2010, and about **5× per year** for frontier language models since 2020—roughly 10,000× over six years.
- The largest publicly known training runs passed 10²⁵ FLOP with GPT-4 (2023), 10²⁶ FLOP with Grok 3 and the largest 2025 models, and are estimated in the 10²⁶–3×10²⁷ range for the largest 2026 runs. Naive extrapolation of the 5×/year trend implies runs of 10²⁸–10²⁹ FLOP by 2029–2030.
- The compute available in the *total stock* of AI chips has grown at **3.4× per year** since 2022, doubling every seven months.
- Power for the largest training runs has doubled roughly every year; frontier runs now consume tens to hundreds of megawatts for months.

For scale: 10²⁶ FLOP is roughly the number of grains of sand on Earth, multiplied by a hundred thousand. Executed on a hundred thousand H100 GPUs at realistic utilization, a 10²⁶ FLOP run takes on the order of three months. A 10²⁹ FLOP run would require a cluster of several million next-generation accelerators—the scale that Meta's Hyperion and OpenAI/Microsoft's Stargate campuses are designed for—and several gigawatts of power.

### Algorithms

Algorithmic progress is the multiplier on compute. Epoch's estimate is that the compute needed to reach a fixed level of language-model performance has fallen by about **3× per year** since 2012—"algorithmic efficiency" gains that compound with hardware gains. Ho et al. (2024) found a halving time for the compute needed to reach a given performance of roughly eight months. Other estimates range from 2× to 4× per year depending on task and period.

The sources are many: architecture (transformer; mixture-of-experts; multi-head latent attention; grouped-query attention), training recipes (better learning rate schedules, data mixing, curriculum), numerical formats (FP16 → BF16 → FP8 → FP4), data quality (filtering, deduplication, synthetic augmentation), and post-training methods (RLHF, DPO, RL with verifiable rewards). DeepSeek V3's reported $5.6 million training cost for a GPT-4-class model—against widely estimated costs of $50–100 million for GPT-4 itself two years earlier—illustrates the cumulative effect, though the figure excluded prior research and infrastructure.

Combined with hardware progress (chip price-performance rising ~49% per year), effective compute for a fixed dollar has been growing at roughly 10× per year or more. This is the engine behind the cost collapse described in Chapter 2.

### Data

Frontier models are trained on tens of trillions of tokens—on the order of the entire useful public text of the internet. Chapter 5 examines the "data wall" in detail. The summary: high-quality human-written text is finite (Epoch estimates the total stock of public human text at roughly 300 trillion tokens, of which perhaps a tenth to a third is usable), the largest runs are approaching that limit, and the response has been synthetic data, multimodal data, and reinforcement learning environments that generate their own signal. Whether these substitutes preserve the scaling curve is one of the field's central uncertainties.

## The shift: from pretraining to post-training to inference

### The 2024 plateau in pretraining

Through late 2024, several reports (from *The Information*, Reuters, Bloomberg) described disappointing internal results at the largest pretraining runs—OpenAI's Orion, Google's next Gemini, Anthropic's largest Claude—relative to the gains expected from scaling laws. Ilya Sutskever, who had been scaling's most prominent advocate, said publicly that "results from scaling up pre-training have plateaued" and that "the 2010s were the age of scaling; now we're back in the age of wonder and discovery."

Interpretations differ. Some argue the plateau was real: the returns to the next order of magnitude of pretraining compute were smaller than the previous one, because high-quality data was exhausted and because loss improvements at that level translate into fewer visible capability gains. Others argue the plateau was an artifact: the runs were engineering-limited (a 10²⁶ FLOP run has to deal with hardware failures, networking, and numerical instability at unprecedented scale), the benchmarks were saturating, and the models that eventually shipped (GPT-4.5, Gemini 2.5, Claude 4 Opus, Grok 3) were in fact meaningfully better on hard tasks. Both are partly right. What is not in dispute is that the industry's *response* was to redirect effort toward two other axes.

### Post-training scaling

Post-training—everything done to a model after pretraining—was for years a small fraction of total compute. RLHF used perhaps 1% of pretraining FLOP. From 2024, post-training compute grew rapidly, driven by reinforcement learning on reasoning tasks. Reports suggest that for the leading 2025–2026 reasoning models, RL compute is comparable to or exceeds pretraining compute. Grok 4's training was reported to use as much compute in RL as in pretraining. The reasoning-model recipe—generate many attempts at problems with verifiable answers, reward correct ones, update the policy—is highly scalable because it does not require human labels, only verifiers, and its returns have so far followed their own power law. Chapter 7 covers this in depth.

### Inference-time scaling

The third axis is compute spent at inference. A reasoning model that thinks for ten thousand tokens outperforms one that thinks for a hundred, on a predictable curve: OpenAI's o1 announcement showed log-linear improvement in AIME accuracy with test-time compute. Techniques include longer chains of thought, sampling many solutions and selecting by majority or by a verifier, tree search over reasoning steps, and iterative refinement. The o3 ARC-AGI-1 result ran at multiple compute levels: 76% at about $20 per task, 87.5% at over a thousand dollars per task.

Inference-time scaling changes the economics of capability. Before, the only way to get a smarter answer was to train a bigger model, an upfront cost amortized over all queries. Now, a user can buy a smarter answer on demand by paying for more thinking. This creates a market for capability at the point of use and means the frontier of *achievable* performance is set by willingness to pay as much as by the model. It also means inference compute demand grows not just with users but with the depth of reasoning per query, which underlies the infrastructure build-out (Chapter 4).

### The current picture

By 2026, "scaling" means scaling three things: pretraining (still growing, at a somewhat slower rate), RL post-training (growing fastest), and inference-time compute (growing with deployment and task difficulty). Epoch's Capabilities Index shows the frontier advancing at 14 points per year since the introduction of reasoning models, more than double the earlier rate. Whatever plateau pretraining hit, aggregate progress accelerated.

## The economics of frontier training

### Costs

Epoch estimates that the cost of frontier training runs (hardware amortization plus energy, excluding staff and research) has grown about 3.5× per year: roughly $2 million for GPT-2-class runs in 2019, $50–100 million for GPT-4 in 2022–23, several hundred million for the largest 2024–25 runs, and on the order of a billion dollars or more for the largest 2026 runs. Extrapolated, a frontier run in 2028–2030 costs $10–100 billion. Dario Amodei has publicly said he expects $10 billion training runs by around 2026–27 and $100 billion runs by the end of the decade. Sam Altman has spoken of trillion-dollar infrastructure ambitions.

These numbers include only the compute for the final run. Total costs include failed and exploratory runs (often several times the final run), the research staff (frontier researchers command compensation in the millions; Meta's 2025 hiring campaign reportedly offered packages in the hundreds of millions for a handful of individuals), data acquisition and licensing, and the datacenters themselves.

### Capital expenditure

Hyperscaler capital expenditure is the most visible measure of the AI investment boom. Combined capex of Amazon, Microsoft, Alphabet, and Meta was roughly $230 billion in 2024, about $410 billion in 2025, and is on track for $600–750 billion in 2026 (Amazon around $200 billion; Alphabet $175–185 billion; Meta $115–135 billion; Microsoft $110–120 billion or more). The first quarter of 2026 alone saw about $130 billion. Analysts project the total approaching a trillion dollars in 2027. Adding Oracle, CoreWeave and other neoclouds, xAI, sovereign projects (Stargate UAE, Saudi Humain, European gigafactories), and Chinese hyperscalers roughly doubles the figure.

For context: total US business investment in structures and equipment runs about $3.5 trillion a year. AI datacenter investment is approaching a fifth of that. Several economists have estimated that AI-related investment accounted for a majority of US GDP growth in some 2025–2026 quarters. The Stanford AI Index put global private AI investment at $582 billion for 2025.

### Revenue and the return question

Against these outlays, revenue is growing very fast from a smaller base. OpenAI's annualized revenue rose from about $13 billion for 2025 to roughly $25 billion by early 2026; Anthropic's from about $10 billion for 2025 to a $47 billion run rate by May 2026. Microsoft, Google, and Amazon each report AI-attributable cloud revenue in the tens of billions. Nvidia's datacenter revenue—the sell-side of the same transaction—exceeded $150 billion annually. Application-layer companies (Cursor, Harvey, Perplexity, Glean, and hundreds more) collectively add tens of billions more.

The return question has several layers:

1. **Is there enough revenue to justify the capex?** At a 5-year depreciation schedule, $700 billion in annual capex requires roughly $140 billion a year in incremental gross profit just to cover depreciation, before any return. Current AI revenues across the industry are in the low hundreds of billions and growing 100%+ per year. On current growth the numbers close by 2027–2028; if growth slows to 30–40%, they do not for several more years.

2. **Is the revenue circular?** A significant share flows in loops: Microsoft invests in OpenAI, which spends on Azure; Nvidia invests in laboratories and neoclouds that buy Nvidia chips; Oracle's largest contract is with OpenAI, financed in part by OpenAI's fundraising. Circularity is not fraud—it is how capital-intensive industries bootstrap—but it means headline revenue overstates external demand.

3. **What is the depreciation life of the assets?** GPUs are commonly depreciated over five to six years, but AI accelerator generations improve so fast (Blackwell to Rubin in eighteen months, with roughly 2× performance per generation) that older chips lose economic value faster. If the effective life is three years, the required return roughly doubles. On the other hand, older chips remain useful for inference of smaller models, and demand for inference has consistently exceeded supply.

4. **Is the technology delivering measurable value?** Chapter 11 examines the productivity evidence. The short version: task-level gains are large and well-documented; firm-level gains are real but smaller and uneven; macro-level gains are so far modest, as is typical for general-purpose technologies in their first decade.

The author's assessment: the investment boom has the characteristics of both a genuine technology build-out (railways, electrification, the internet) and a speculative overshoot (1840s railway mania, 1999 telecoms). In each historical case, the technology was real, the eventual returns were enormous, and many of the specific investors lost their money because capacity was built ahead of demand and financing structures could not survive the wait. The probability of a significant correction in AI-related equity and credit markets before 2030 is high—perhaps 50–60%—and the probability that such a correction indicates the technology has failed is low. Chapter 18 treats a "correction" scenario explicitly.

## Can scaling continue through 2030?

Epoch's 2024 analysis "Can AI Scaling Continue Through 2030?" identified four constraints and concluded that runs of 2×10²⁹ FLOP were feasible by 2030 if investment continued. Updated for 2026:

**Power.** A 10²⁹ FLOP run on 2030-era hardware requires roughly 5–10 GW of sustained power. Campuses of that scale are under construction (Stargate Abilene targeting 1.2 GW and expanding; Meta Hyperion planned at 2 GW growing to 5 GW; xAI Colossus 2 at over 1 GW; Microsoft Fairwater sites; multiple Gulf projects). Grid interconnection is the bottleneck: US interconnection queues run three to five years, and transformer and gas-turbine supply chains are backed up. Responses include behind-the-meter gas generation, restarted nuclear plants, small modular reactor contracts, and geographically distributed training. Power is a real constraint that pushes costs up and timelines out, but it is not a hard ceiling before 2030. The IEA projects datacenter electricity roughly doubling from 485 TWh in 2025 to 950 TWh in 2030, about 3% of global electricity—large but absorbable.

**Chip manufacturing.** TSMC's advanced-node and CoWoS packaging capacity, and SK Hynix/Samsung/Micron high-bandwidth-memory capacity, are the binding constraints on accelerator supply. Both expanded aggressively 2024–2026 (CoWoS capacity roughly tripled; HBM4 entered volume production in 2026 after delays). Epoch estimated chip production could support 10²⁹ FLOP runs by 2030 if a large fraction of leading-edge capacity is devoted to AI. Chapter 4 details.

**Data.** Discussed in Chapter 5. Text is the binding constraint for pretraining scaling; synthetic data and RL environments are the workaround. Multimodal data (video especially) is abundant but less information-dense per token.

**Latency and parallelism.** Training runs cannot be shortened indefinitely by adding chips because of communication overhead and the sequential nature of gradient descent. Epoch estimated a "latency wall" around 10³⁰–10³² FLOP for current approaches—beyond 2030 targets. Distributed training across multiple datacenters (as Gemini reportedly used) relaxes single-site constraints.

**Capital.** The least discussed and possibly most binding constraint. A $100 billion training run requires an organization with the balance sheet to fund it and the expectation of returns to justify it. Only a handful of companies and states can. Whether investors continue to fund the trajectory depends on revenue growth and on the absence of a financial shock—which brings the analysis back to the return question above.

### The case for continued scaling

1. Every previously predicted wall (data, 2022; pretraining returns, 2024) has been circumvented within a year or two by a new axis of scaling.
2. The compute build-out for 2027–2029 is already financed and under construction; the chips will exist and will be used.
3. RL post-training and inference-time scaling are early on their curves, with no sign of diminishing returns yet.
4. Algorithmic progress at 3×/year is independent of hardware and has shown no slowdown.
5. AI is increasingly used to accelerate AI research itself (coding, experiment design, data curation), which could steepen the algorithmic curve (Chapter 17).

### The case against

1. Pretraining returns visibly diminished in 2024; the field is now relying on newer, less-proven axes.
2. RL on verifiable tasks may generalize poorly beyond domains with verifiers—the gains on math and code may not transfer to open-ended reasoning, judgment, or novelty.
3. Benchmarks are saturating faster than they can be built, so it is genuinely hard to know whether the top of the curve is bending.
4. Physical constraints (power, chips) will raise marginal costs, and capital markets may not fund runs at $50–100 billion if returns are unclear.
5. The remaining hard problems—reliability, memory, continual learning, embodied common sense—may not be scaling problems at all, requiring new ideas that have no timeline.

### Assessment

The author's judgment is that scaling in the broad sense—more effective compute applied to training and inference, via whatever mix of axes—continues through at least 2028 with high confidence (85%+), because the infrastructure is built, the algorithms are improving, and the returns so far are strong enough to justify the spend. Whether scaling continues to deliver *the same kind* of capability gains—smooth improvement toward general expert-level competence—is less certain (60–70%). And whether it addresses the qualitative gaps (reliability, memory, embodiment) is genuinely uncertain (perhaps 50%); these may require ideas that scaling makes possible but does not itself supply.

## Key numbers to remember

| Quantity | Value | Source |
|---|---|---|
| Frontier training compute growth | ~5×/year (LMs since 2020) | Epoch |
| Largest 2026 training runs | ~10²⁶–3×10²⁷ FLOP | Epoch estimates |
| Algorithmic efficiency gain | ~3×/year | Epoch |
| Chip price-performance gain | ~49%/year (since 2023) | Epoch |
| Total AI compute stock growth | 3.4×/year | Epoch |
| Frontier training cost growth | ~3.5×/year | Epoch |
| Largest 2026 frontier run cost | ~$1B+ (compute only) | Estimates |
| Hyperscaler capex 2026 | $600–750B (big four) | Company guidance |
| Global private AI investment 2025 | ~$582B | Stanford AI Index |
| Cost of GPT-4-class inference | $30–60/M tokens (2023) → ~$0.40/M (2026) | Multiple |
| Epoch Capabilities Index frontier progress | 14 pts/yr since reasoning models (vs 6 before) | Epoch |
| Data centre electricity | 485 TWh (2025) → ~950 TWh (2030) | IEA |
| Feasible training run by 2030 | ~10²⁹ FLOP | Epoch |
