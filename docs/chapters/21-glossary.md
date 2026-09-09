# Glossary

Terms used in this document, defined as they are used here. Where a term is contested, the contest is noted.

**Agent.** An AI system that pursues a goal over multiple steps by taking actions (calling tools, operating software, writing and running code) and observing results, with limited or no human intervention between steps. Contrast with a chatbot, which responds once per human turn. See Chapter 8.

**AGI (artificial general intelligence).** Contested. Used here, unless qualified, to mean the *remote-worker standard*: a system that can do essentially any cognitive task a human expert can do working remotely, at comparable quality and reliability and lower cost. Other definitions range from "human-level on benchmarks" (already met) to "learns any domain like a child" (not met). See Chapter 17.

**Alignment.** The property of an AI system reliably doing what its principals intend, including in situations not anticipated during training. *Misalignment* includes reward hacking, goal misgeneralization, deception, and power-seeking. See Chapter 16.

**Alignment faking.** A model strategically behaving as its trainers want during training or evaluation while intending to behave differently when unobserved, in order to preserve its existing dispositions. Documented in 2024. See Chapter 16.

**ARC-AGI.** A family of benchmarks (Chollet, 2019 onward) testing induction of novel rules from few examples—designed to resist memorization and measure fluid intelligence. ARC-AGI-1 was effectively solved in 2025–26; ARC-AGI-2 and the interactive ARC-AGI-3 (2026) remain active. See Chapter 2.

**ASI (artificial superintelligence).** A system that substantially exceeds the best humans at essentially all cognitive tasks, including scientific research and strategy.

**ASL (AI Safety Level).** Anthropic's tiered framework in its Responsible Scaling Policy, in which capability thresholds (biological uplift, cyber offense, autonomous research) trigger required security and deployment safeguards. Analogous frameworks: OpenAI's Preparedness Framework, DeepMind's Frontier Safety Framework.

**Attention.** The mechanism in transformers by which each position in a sequence computes a weighted combination of all other positions. Cost scales with the square of sequence length in its standard form. See Chapter 6.

**Benchmark saturation.** The state in which the best models score at or near a benchmark's ceiling, so it no longer discriminates among them. Most 2023-era benchmarks were saturated by 2026. See Chapter 2.

**Chain of thought (CoT).** A model's intermediate reasoning, produced as text before its final answer. *CoT monitoring* reads this reasoning for safety purposes; *CoT faithfulness* is the degree to which it reflects the model's actual computation. See Chapters 7, 16.

**Chinchilla-optimal.** The compute-optimal ratio of training data to model parameters (roughly 20 tokens per parameter) found by Hoffmann et al. (2022). Modern models are often trained well beyond it to reduce inference cost. See Chapter 3.

**Compute.** Computational work, measured in FLOP (floating-point operations). *Training compute* is the total used to train a model; *inference compute* is that used to run it. Frontier training runs in 2026 are on the order of 10²⁶–10²⁷ FLOP. See Chapter 3.

**Compute governance.** Policies that monitor or control access to AI compute (chips, datacenters, cloud) as a lever over AI development. In 2026 mostly export controls. See Chapter 15.

**Continual learning.** The ability to learn from new experience over time without forgetting prior knowledge. Not achieved in deployed frontier models; the key architectural open problem. See Chapter 6.

**Co-packaged optics (CPO).** Integration of optical transceivers directly onto a switch or accelerator package, replacing copper and pluggable optics for high-bandwidth interconnect. See Chapter 4.

**CoWoS.** TSMC's chip-on-wafer-on-substrate advanced packaging, required to connect GPU dies to HBM; a supply-chain bottleneck. See Chapter 4.

**Data wall.** The limit imposed by the finite stock of high-quality human-generated text available for pretraining. See Chapter 5.

**Deepfake / synthetic media.** AI-generated or altered images, audio, or video depicting events or statements that did not occur.

**Diffusion model.** A generative model that produces output by iteratively removing noise from a random starting point. Dominant for images and video; experimental for text. See Chapters 6, 9.

**Distillation.** Training a smaller model to reproduce the outputs of a larger one, transferring capability at lower cost. See Chapter 5.

**Emergent misalignment.** Broad misaligned behavior arising from narrow training (e.g., on insecure code, or from reward hacking), generalizing to unrelated domains. Documented 2025. See Chapter 16.

**Epoch Capabilities Index (ECI).** Epoch AI's composite measure of frontier model capability across benchmarks; rising ~14 points per year since reasoning models.

**Export controls.** US (and allied) restrictions on the sale of advanced AI chips, chip-making equipment, and related items to China and other destinations. See Chapters 4, 14.

**FLOP.** Floating-point operation; the unit of compute. 10²⁶ FLOP ≈ one hundred thousand H100 GPUs running for about three months.

**Foundation model.** A large model pretrained on broad data that can be adapted to many tasks. Language models, vision-language models, and robot policies (VLAs) are all foundation models.

**Frontier model.** A model at or near the current maximum of capability, typically trained with 10²⁶ FLOP or more by one of a handful of laboratories.

**FrontierMath.** Epoch AI's benchmark of research-level mathematics problems with verifiable answers, in tiers of difficulty. See Chapter 2.

**GDPval.** OpenAI's 2025 benchmark of professional deliverables across 44 occupations, judged by human experts against human professionals' work. See Chapter 2.

**GPAI (general-purpose AI).** The EU AI Act's term for foundation models; those trained above 10²⁵ FLOP are presumed to pose "systemic risk" and face additional obligations. See Chapter 15.

**GRPO (Group Relative Policy Optimization).** The reinforcement-learning algorithm popularized by DeepSeek for training reasoning models, using group-relative advantages instead of a value network. See Chapter 7.

**Hallucination.** A model's generation of plausible but false content. Reduced but not eliminated in 2026 models. See Chapter 2.

**HBM (high-bandwidth memory).** Stacked DRAM placed adjacent to the processor; the most constrained component in AI hardware. See Chapter 4.

**Humanity's Last Exam (HLE).** A 2025 benchmark of expert-written questions across disciplines, adversarially filtered; frontier scores rose from ~25% to ~59% by late 2026.

**Inference.** Running a trained model to produce outputs. *Inference-time compute* (or *test-time compute*) is compute spent during inference, including extended reasoning; its scaling is a second axis of capability. See Chapter 7.

**Intelligence explosion.** A hypothesized feedback loop in which AI systems improve AI systems, producing rapid, possibly discontinuous, capability growth. See Chapter 17.

**Interpretability.** Research into understanding a model's internal computations. *Mechanistic interpretability* seeks circuit-level explanation; *sparse autoencoders* decompose activations into interpretable features. See Chapter 16.

**Jagged frontier / jagged intelligence.** The uneven capability profile of AI systems—superhuman on some tasks, subhuman on others, along boundaries that do not match human intuition. See Chapter 2.

**JEPA (Joint Embedding Predictive Architecture).** LeCun's family of self-supervised world-model architectures that predict abstract representations rather than raw pixels or tokens. See Chapter 6.

**KV cache.** The stored keys and values from prior tokens that a transformer uses during generation; grows with context length and dominates inference memory.

**Loss of control.** The scenario in which highly capable AI systems can no longer be corrected or stopped by humans. See Chapters 16, 18.

**MCP (Model Context Protocol).** An open standard (Anthropic, 2024; Linux Foundation, 2025) for connecting models to tools and data. See Chapter 8.

**METR time horizon.** The length of task (in human-expert time) that an AI agent can complete with a given probability (50% or 80%), measured on a suite of software and research tasks; the principal longitudinal measure of agentic capability. See Chapter 8.

**Mixture-of-experts (MoE).** An architecture in which each layer contains many parallel sub-networks ("experts") and a router activates only a few per token, decoupling total parameters from compute per token. See Chapter 6.

**Model collapse.** Degradation of models trained on successive generations of unfiltered synthetic data; avoided in practice by filtering and mixing with human data. See Chapter 5.

**Multimodal.** Processing or generating multiple modalities (text, image, audio, video) within one model.

**Open weights.** A model whose trained parameters are publicly downloadable, allowing local use and fine-tuning. Distinct from "open source" (which would also include training data and code). See Chapters 14, 16.

**Post-training.** Everything done to a model after pretraining: supervised fine-tuning, RLHF, reinforcement learning on reasoning, safety training. Now comparable in compute to pretraining at the frontier. See Chapter 3.

**Pretraining.** The initial training of a model on a large corpus by next-token prediction (or analogous objective). See Chapter 3.

**Prompt injection.** An attack in which instructions embedded in content a model processes (a web page, email, document) hijack the model's behavior. Unsolved for agents. See Chapter 8.

**RAG (retrieval-augmented generation).** Retrieving relevant documents and inserting them into a model's context before generation, to ground answers and extend knowledge.

**Reasoning model.** A model trained with reinforcement learning to produce extended chains of thought before answering and whose performance improves with more inference compute. o1 (2024) was the first widely available example. See Chapter 7.

**Reward hacking / specification gaming.** A model satisfying the letter of its reward signal without achieving the intended goal (e.g., editing tests instead of fixing code). See Chapter 7.

**RLHF (reinforcement learning from human feedback).** Training a model against a reward model learned from human preference comparisons. The technique that made chatbots usable. See Chapter 1.

**RLVR (reinforcement learning with verifiable rewards).** RL where reward comes from an automatic checker (correct answer, passing tests, valid proof). The engine of reasoning models. See Chapter 7.

**Sandbagging.** A model strategically underperforming on an evaluation, e.g., to avoid triggering safeguards. See Chapter 16.

**Scaling laws.** Empirical power-law relationships between model loss and compute, parameters, and data (Kaplan et al., 2020; Hoffmann et al., 2022). See Chapter 3.

**Scheming.** A model covertly pursuing goals misaligned with its principals, including deceiving them about its behavior. Documented in constructed evaluations from 2024. See Chapter 16.

**Sovereign AI.** National efforts to control domestic AI compute, models, data, and talent. See Chapter 14.

**State-space model (SSM).** A sequence architecture (S4, Mamba) with linear-time processing and constant-size state; used in hybrids with attention. See Chapter 6.

**Superhuman coder / automated researcher.** Forecasting milestones: an AI that matches the best human AI-research engineer (coder), and one that can run the full AI research loop including generating ideas (researcher). See Chapter 17.

**SWE-bench Verified.** A benchmark of real GitHub issues to be resolved by editing code; frontier models exceeded 90% in 2026.

**Sycophancy.** A model's tendency to agree with or flatter users, including revising correct answers under pushback. A product of preference training. See Chapters 2, 16.

**Synthetic data.** Training data generated by a model rather than by humans. See Chapter 5.

**Takeoff.** The speed of progress from roughly human-level AI to vastly superhuman AI. *Fast* (months to a few years) versus *slow* (a decade or more). See Chapter 17.

**Test-time training (TTT).** Updating some model parameters during inference on the incoming sequence; an approach to memory and continual learning. See Chapter 6.

**Time horizon.** See METR time horizon.

**Transformer.** The neural network architecture (Vaswani et al., 2017) based on self-attention that underlies essentially all frontier models. See Chapters 1, 6.

**VLA (vision-language-action model).** A robot foundation model that maps camera images and language instructions to motor actions, built on a pretrained vision-language model. See Chapter 9.

**World model.** A learned model of environment dynamics that predicts future states given actions; used for planning, simulation, and training agents and robots. See Chapter 6.
