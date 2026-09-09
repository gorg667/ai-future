# Architectures Beyond the Transformer: What Might Replace or Extend the Current Paradigm

!!! abstract "In brief"
    - The transformer will not be replaced wholesale before 2030, but frontier systems are becoming hybrids (mostly linear/SSM layers, minority full attention, fine-grained MoE).
    - Memory and continual learning are the largest unsolved architectural gap and not obviously a scaling problem; the author estimates 50% by 2029, 75% by 2032.
    - World models matter most for robotics; for language, the 'autoregression is a dead end' critique looks premature.
    - The first system most people call AGI will be recognizably descended from the 2017 transformer, heavily modified.

## Framing

The transformer has been the dominant architecture for nine years—an eternity in a field where the previous champions (LSTMs, convolutional networks) lasted a similar span before being displaced. Its dominance rests on three properties: it parallelizes across the sequence during training, it scales predictably, and it is general across modalities. Its weaknesses are also well understood: attention costs grow quadratically with sequence length; it has no persistent memory beyond its context window; it does not learn from experience after training; it processes the world as sequences of discrete tokens, which is natural for text and awkward for continuous perception and control; and it is a poor fit for the hierarchical, model-based planning that humans and animals use.

This chapter surveys the research directions that aim to fix these weaknesses—some by modifying the transformer, some by replacing components, some by building fundamentally different systems—and assesses which are likely to matter by 2030. The organizing conclusion: **the transformer will not be replaced wholesale before 2030, but frontier systems will be hybrids in which attention is one component among several, and the most important advances will be in memory and continual learning rather than in the sequence-mixing primitive itself.**

## Efficient sequence modeling: attention and its alternatives

### The quadratic problem

Standard attention computes an interaction between every pair of tokens in the context, so cost grows with the square of sequence length. For a million-token context this is a trillion pairwise operations per layer. The key-value (KV) cache that stores past tokens for generation grows linearly and dominates inference memory for long contexts. These costs made long-context and long-horizon operation expensive, motivating a decade of research into alternatives.

### Approaches that modify attention

- **Sparse and local attention** restricts each token to a subset of others (a local window, strided patterns, learned blocks). Longformer and BigBird were early examples; DeepSeek's Native Sparse Attention (NSA) and DeepSeek Sparse Attention (DSA, used from V3.2 onward in 2025) learn which blocks to attend to and achieve large speedups on long sequences with minimal quality loss. Most frontier models now use sparse or sliding-window attention in a subset of layers.
- **Grouped-query and multi-head latent attention** shrink the KV cache by sharing keys and values across heads (GQA, from Llama 2 onward) or compressing them into a low-rank latent (MLA, DeepSeek V2 onward). MLA cut DeepSeek's KV cache by more than 90% relative to standard attention and was a key enabler of its cost efficiency.
- **Sequence-parallel and ring attention** distribute long sequences across many devices, enabling multi-million-token contexts at the cost of communication.
- **Hardware-aware kernels** (FlashAttention 1–3) do not change the math but reorganize memory access to approach hardware limits; they made exact attention practical at lengths formerly infeasible.

### Approaches that replace attention

- **Linear attention** (Katharopoulos et al., 2020, and descendants) reformulates attention as a recurrent kernel with constant per-token cost. Early versions lost quality; later variants (RetNet, Gated Linear Attention, Gated DeltaNet, RWKV-7) close much of the gap.
- **State-space models** (S4, 2021; Mamba, Gu and Dao, 2023; Mamba-2, 2024) treat sequences as a continuous dynamical system with a fixed-size hidden state, giving linear-time processing and constant-memory generation. At large scale, pure SSMs underperform on tasks requiring precise retrieval from context (exact copying, in-context learning of specific associations), because a fixed-size state cannot store arbitrary detail.
- **Hybrids** combine SSM or linear-attention layers (for efficient bulk processing) with a minority of full-attention layers (for precise retrieval). Jamba (AI21, 2024), Nvidia's Nemotron-H (2025), Falcon-H1, IBM Granite 4, Google's Gemma 3n, Alibaba's Qwen3-Next (2025: Gated DeltaNet plus periodic full attention plus high-sparsity MoE, at frontier-class quality for a fraction of inference cost), and Moonshot's Kimi Linear (2025, at a trillion parameters) use hybrid designs.

### Assessment

By 2026 the practical consensus is that **hybrids win**: roughly three-quarters of layers can be linear-time with a quarter full attention, at near-parity quality and large efficiency gains. Attention is not being replaced; it is being rationed. By 2030, "transformer" will likely refer to a family of hybrid architectures in which pure softmax attention is a minority component.

## Sparsity: mixture-of-experts and beyond

### Mixture-of-experts

A mixture-of-experts (MoE) model replaces each dense feed-forward layer with many parallel "experts" and a router that sends each token to a few of them. Total parameters can be enormous (DeepSeek V3: 671 billion; Kimi K2: 1 trillion; Llama 4 Behemoth: ~2 trillion) while active parameters per token remain modest (37 billion for V3; 32 billion for K2), so compute scales with active parameters. MoE was introduced to modern deep learning by Shazeer et al. (2017), scaled by Google (GShard, Switch Transformer), reportedly used in GPT-4, and from 2024 became universal at the frontier.

MoE's advantages: more knowledge per unit of compute; natural specialization; efficient scaling. Its costs: memory (all experts resident), load-balancing complexity, and communication overhead when experts are spread across devices. DeepSeek's contributions—auxiliary-loss-free load balancing, fine-grained experts (256 small experts, 8 active), shared experts, and FP8 training—made very sparse MoE practical and are now standard.

The direction is toward *more* sparsity: more and smaller experts; sparsity in attention as well as feed-forward layers; eventually per-token routing over the whole network. Expert specialization also offers routes to modular updating (retraining one expert without touching others) and interpretability.

### Other conditional computation

- **Mixture-of-depths** lets tokens skip layers, allocating compute by difficulty.
- **Speculative and multi-token decoding** (Medusa, EAGLE, DeepSeek V3's multi-token prediction) generate several tokens per forward pass.
- **Activation sparsity** exploits the fact that most neurons are inactive for most inputs; it is central to on-device inference.

## Memory and continual learning: the unsolved core

### The problem

Current models have three kinds of memory, none of which resembles human memory:

1. **Parametric memory**—knowledge in the weights. Vast, but frozen at the training cutoff; not updatable without retraining; not reliably editable.
2. **Context (working) memory**—the tokens in the current window. Precise but expensive, transient, and limited.
3. **External memory**—retrieval over databases, files, or vector stores, injected into context. Flexible but shallow: the model does not *learn* from what it retrieves.

The consequence: a model cannot become better at a user's specific codebase, a physician's specific patient population, or a firm's specific processes through experience. It can be told, repeatedly, and given tools to look things up, but it does not consolidate experience into skill the way a human colleague does over months. This is arguably the largest single gap between current AI and the generality that AGI definitions require, and it is not obviously a scaling problem.

### Approaches

**Longer contexts.** Contexts went from 4,000 tokens (GPT-3) to 128,000 (GPT-4 Turbo) to 1–2 million (Gemini 1.5+) to 10 million in research settings. Effective use of long context has improved ("needle in a haystack" is saturated; realistic multi-hop long-context benchmarks are not). Long context plus retrieval is the dominant practical solution in 2026. But it is a workaround: cost grows with context; nothing is consolidated; the model starts every session from the same weights.

**Retrieval-augmented generation and agentic memory.** Products store summaries of past interactions, preferences, and documents and retrieve them at inference (ChatGPT memory, Claude projects and memory, enterprise systems). Research on structured memory—MemGPT/Letta, Mem0, Zep, hierarchical summarization, knowledge graphs—improves what is stored and how it is found. Useful and improving, but engineering scaffolds around a stateless model.

**Test-time learning and fast weights.** A more radical approach updates parameters during inference. Google's Titans (Behrouz et al., 2025) added a neural long-term memory module trained at test time to memorize surprising information; its successor framework, Nested Learning (NeurIPS 2025), reconceived a model as a hierarchy of learning systems updating at different rates—fast layers for immediate context, slower ones for consolidated knowledge—an explicit analogy to human memory consolidation. Test-time training (TTT) layers (Sun et al., 2024) make the hidden state itself a small model updated by gradient descent on the incoming sequence. These showed strong long-context results and are being incorporated into hybrid architectures, but no frontier model has yet shipped a system that visibly learns over time in the hands of users.

**Continual and lifelong learning.** The classical obstacle is catastrophic forgetting: fine-tuning on new data degrades performance on old. Decades of research (elastic weight consolidation, replay, progressive networks, parameter-efficient adapters like LoRA) yield partial solutions for narrow updates but not for open-ended accumulation of knowledge and skill. Frontier laboratories do periodic retraining rather than continual learning. Several researchers—Dwarkesh Patel's widely discussed 2025 essay made the case publicly—identify continual learning as the key missing capability and expect it within roughly three to seven years; others think long context plus retrieval plus periodic retraining will be "good enough" for most economic purposes.

**Model editing.** Techniques to surgically update facts in weights (ROME, MEMIT, successors) work for simple facts at small scale and degrade at large scale. Not a route to general continual learning.

### Assessment

Memory and continual learning are the most important architectural frontier, the least solved, and the hardest to forecast. Practical workarounds will continue to improve and capture much of the economic value—a model that can be given a million tokens of relevant context and good retrieval is very useful even if it does not learn. But the qualitative gap—a system that becomes an expert in *your* problem through experience—likely requires test-time learning or nested-learning approaches to mature. The author's estimate: 50% by 2029, 75% by 2032. When it happens, it will be a discontinuity in usefulness comparable to the introduction of reasoning models.

## World models and non-autoregressive approaches

### The critique

Yann LeCun has argued since 2022 that autoregressive language models are a dead end for human-level intelligence: they predict tokens rather than modeling the world; they cannot plan; they lack persistent memory; and text is too impoverished a medium to learn the physics and common sense a child learns by observation. His alternative, "A Path Towards Autonomous Machine Intelligence" (2022), centers on a **world model** that predicts abstract representations of future states (not pixels or tokens), trained by self-supervised learning on video and sensor data and used by a planner to choose actions. The Joint Embedding Predictive Architecture (JEPA) and its instantiations—I-JEPA, V-JEPA, V-JEPA 2 (2025, with demonstrated zero-shot robot planning)—implement this. LeCun left Meta in late 2025 to found Advanced Machine Intelligence (AMI) Labs in Paris, which raised over a billion dollars in early 2026 to pursue JEPA-based world models for physical and social reasoning.

### Generative world models

A different strand builds world models as *generative* simulators. Google DeepMind's Genie, Genie 2, and Genie 3 (2025) generate interactive, controllable environments from a prompt, in real time, with state persisting over minutes—a learned game engine. World Labs' Marble (2025) generates navigable 3D worlds. Nvidia's Cosmos (2025) is a family of world foundation models for physical AI, generating physically plausible video conditioned on actions, used to train robots in simulation. Wayve's GAIA and Tesla's internal models simulate driving. Video generators (Sora, Veo) are implicitly world models.

These systems (a) generate training data for robots and agents, (b) let agents plan by imagining consequences, and (c) provide interactive RL environments. Their weaknesses are physical inconsistency and compute cost.

### Diffusion language models

Autoregressive generation is sequential and hard to revise. Diffusion models generate by iteratively denoising an entire sequence, offering parallel generation and natural in-filling. Discrete diffusion for text (LLaDA and others, 2024–25) and commercial efforts (Inception Labs' Mercury; Google's Gemini Diffusion, 2025) demonstrated text and code generation at several times autoregressive speed with competitive quality at small scale. Whether diffusion LMs reach frontier quality is unresolved; they are plausible as fast, cheap models for specific uses before 2030 and a long shot as a frontier replacement.

### Assessment

World models matter most for robotics and embodied AI (Chapter 9), where the LeCun critique is strongest—text does not teach manipulation. For language and reasoning, autoregressive transformers plus RL have delivered so much that the "dead end" argument looks premature; reasoning models do plan, in the sense of exploring and revising chains of thought. The likely synthesis by 2030: language models with world-model components for physical and spatial reasoning trained on video; generative world models as simulators for training agents and robots; JEPA-style predictive representations as one input to multimodal systems rather than a replacement.

## Neurosymbolic and hybrid reasoning systems

The oldest debate in AI—learning versus logic—has been partly dissolved by systems that combine them. AlphaGeometry (2024) pairs a language model proposing constructions with a symbolic deduction engine. AlphaProof works in Lean, so every step is machine-verified. Reasoning models call code interpreters, computer-algebra systems, and theorem provers as tools. The durable form of neurosymbolic AI is not a new architecture but a *system design*: learned components propose; formal components check. This is central to AI for mathematics (Chapter 10) and to reliability (Chapter 7).

## Small models, on-device AI, and specialization

A counter-trend to frontier scaling is the rise of small, efficient models. Microsoft's Phi, Google's Gemma 3/3n, Meta's small Llamas, Alibaba's Qwen 3 0.6B–8B range, Apple's on-device foundation models, and Mistral's small models deliver 2023-frontier capability at 1–10 billion parameters, running on phones and laptops. Techniques: distillation, high-quality synthetic training data, quantization to 4 bits or below, and edge-designed architectures.

By 2030 most AI inference will happen on devices or on small hosted models, with frontier models reserved for hard problems—a tiered architecture already visible in GPT-5's router and every hyperscaler's product line. Implications: privacy (data stays on device), cost (near-zero marginal), latency, and geopolitics (open small models spread capability everywhere).

## What the frontier architecture of 2030 probably looks like

| Component | 2026 frontier | Likely 2030 frontier |
|---|---|---|
| Sequence mixing | Mostly full attention with sparse/MLA variants; some hybrids | Hybrid: majority linear/SSM layers, minority full attention |
| Feed-forward | Fine-grained MoE (hundreds of experts, ~5% active) | Sparser MoE; routing at multiple granularities |
| Precision | FP8 training, FP4 inference | FP4/FP6 training; sub-4-bit mixed-precision inference |
| Context | 200K–2M tokens | 10M+ effective, with hierarchical memory |
| Memory | Context + RAG + agentic scaffolds | Plus test-time learned memory modules; early continual learning |
| Modalities | Native text, image, audio; video in/out | Plus 3D, action, and sensor streams; world-model components |
| Reasoning | RL-trained chain of thought; tool calls | Plus learned search, verifiers, formal-method integration |
| Training | Pretrain → SFT → large RL | Plus continual post-training on deployment data; many more RL environments |
| Deployment | Frontier cloud + small on-device | Tiered routing across device, edge, cloud |

The deeper question—whether these incremental changes suffice for human-level generality, or whether a qualitatively new idea is needed—is taken up in Chapter 17. The architectural evidence cuts both ways. The transformer's critics have been right that its weaknesses (memory, continual learning, embodiment) are real and persistent; they have been wrong, repeatedly, about how far it could go without solving them. The most defensible forecast: the architecture keeps absorbing its critics' ideas as components, and the first system most people call AGI will be recognizably descended from the 2017 transformer, heavily modified.
