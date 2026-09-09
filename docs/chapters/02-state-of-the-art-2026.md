# The State of the Art in 2026: What AI Can and Cannot Do

## Purpose of this chapter

Forecasting requires a baseline. This chapter describes, as precisely as the evidence allows, what frontier AI systems can do as of September 2026, what they cannot, and how we know. It covers the landscape of models and laboratories, the benchmarks and what they measure, the pattern of "jagged" capability that makes AI hard to reason about, the reliability problem, and the cost curve that determines what is economically deployable. Readers who follow the field closely can skim; the chapter's value is in assembling the pieces in one place with their caveats attached.

A note on specificity: model names and scores given here are accurate to the author's knowledge at the time of writing but will be superseded within months. The *structure* of the landscape—who the players are, what kinds of capability are saturated versus open, how fast costs fall—changes more slowly and is the thing to retain.

## The landscape of laboratories and models

### The frontier tier

Five organizations train models at the absolute frontier of capability, defined here as models trained with on the order of 10²⁶ FLOP or more and competitive on the hardest current benchmarks:

**OpenAI.** The GPT-5 family (GPT-5 released August 2025, followed by 5.1, 5.2, 5.3-Codex, 5.4, 5.5, and 5.6 "Sol" over the following year, with "Pro" high-compute variants) unified the earlier split between the GPT-4o general models and the o-series reasoning models: a router decides how much thinking to apply. GPT-5.2 in January 2026 was the first model to exceed 90% on ARC-AGI-1, and scored 70.9% on GDPval—winning or tying against human professionals on tasks drawn from 44 occupations—while running roughly eleven times faster and at under one percent of the cost. GPT-5.6 Pro solved all six problems of the July 2026 International Mathematical Olympiad on a first attempt without human steering. On September 3, 2026—six days before this document's cutoff—OpenAI released **GPT-6 Astra**, which its president described as a "generational leap": it is the first model OpenAI has designated at the *Critical* cybersecurity tier of its Preparedness Framework (able to find and exploit previously unknown vulnerabilities in hardened systems without human guidance), it scored 62.7% on ARC-AGI-3 under the standard harness and 99.9% with OpenAI's own context-management harness, and its release was accompanied by a two-week pause in some frontier training and a new set of misalignment monitors after the summer's incidents (Chapter 16). Its most advanced cyber capabilities are gated behind a trusted-access program ("Daybreak Blue"). ChatGPT passed 900 million weekly active users in early 2026 and roughly a billion monthly. OpenAI's annualized revenue was about $25 billion in February 2026 and approximately $2 billion per month by mid-year, against reported losses in the low tens of billions, funded by a $122 billion round at a reported $852 billion valuation.

**Anthropic.** The Claude 4 family (Opus 4 and Sonnet 4 in May 2025, Opus 4.1 in August, Sonnet 4.5 in September, Opus 4.5 in November, Opus 4.6 in February 2026, Opus 4.7 in spring 2026) has been the preferred model for software engineering and agentic coding for much of the period; Claude Code became one of the fastest-growing developer products in history. In April 2026 Anthropic announced Claude Mythos Preview, a model it withheld from general release on the grounds that its offensive cyber capabilities crossed its Responsible Scaling Policy thresholds, and instead deployed through Project Glasswing to a consortium of critical-infrastructure and software companies for defensive vulnerability discovery. On June 9, 2026 it released **Claude Fable 5**, described as "a Mythos-class model that we've made safe for general use": the same underlying model as **Claude Mythos 5** (available only to Glasswing partners, in coordination with the US government), but with classifiers that route cyber, biology/chemistry, and suspected-distillation queries to the less capable Claude Opus 4.8. Access to Fable 5 was suspended three days after launch and restored on July 1—an episode illustrating how thin the operational margins at the frontier have become. **Claude Opus 5** (July 24, 2026) brought most of Fable 5's capability to standard plans; a Fable 5.1 followed. Anthropic's revenue grew from roughly $10 billion in 2025 to a $30 billion annualized run rate in April 2026—by some accounts overtaking OpenAI—and $47 billion by May, overwhelmingly from API and enterprise customers rather than consumers.

**Google DeepMind.** Gemini 3 Pro (November 2025) and 3.1 Pro (early 2026) closed the gap with, and on many evaluations exceeded, OpenAI and Anthropic; Gemini 3.1 Pro achieved 98% on ARC-AGI-1 at about fifty cents per task, roughly matching the human panel. By September 2026 Google's flagship trailed the newest OpenAI and Anthropic releases on the hardest reasoning and agentic evaluations, though a successor generation is widely expected. Google's advantages are structural: its own TPU silicon (Ironwood, the seventh generation), the largest distribution footprint (Search, Android, Workspace, YouTube), and DeepMind's science program (AlphaFold, AlphaProof, GNoME, weather models). Google also leads in video generation (Veo) and has integrated generative answers into Search for billions of users.

**xAI.** Grok 4 (July 2025) and its successors (4.1, 4.3, 4.6) reached the frontier on reasoning benchmarks on the strength of the Colossus cluster in Memphis—by Epoch's estimate the largest known AI datacenter at approximately 1.1 million H100-equivalents—and an aggressive training-compute strategy. xAI's models are distinguished by integration with the X platform and a stated commitment to fewer content restrictions.

**Meta.** Meta's Llama series anchored the Western open-weight ecosystem from 2023 through Llama 4 (April 2025). Llama 4's reception was mixed—it underperformed expectations relative to Chinese open models—and Meta responded with a reorganization, the creation of Meta Superintelligence Labs, a multi-billion-dollar talent acquisition campaign, and the largest datacenter build-out of any company (Hyperion, in Louisiana, projected at 3.7 million H100-equivalents by 2028). Whether Meta continues to release frontier weights openly is, as of this writing, uncertain; its 2026 models have been released more selectively.

### The Chinese frontier

China's laboratories constitute a second frontier, roughly six to eight months behind the US leaders on aggregate capability measures and ahead on cost-efficiency and open-weight release.

**DeepSeek** (a subsidiary of the hedge fund High-Flyer) demonstrated with V3 (December 2024) and R1 (January 2025) that frontier-class models could be trained for a reported fraction of Western costs, through mixture-of-experts architecture, multi-head latent attention, FP8 training, and a lean team. DeepSeek V4, released in two variants in April 2026, is estimated by independent evaluators to trail the leading US model by about eight months overall, with a narrower gap on coding.

**Alibaba's Qwen** team has released over a hundred open-weight models under the Apache 2.0 license, including a 235-billion-parameter mixture-of-experts flagship; Qwen 3.x models (2026) are the most downloaded open models globally and the most common base for fine-tuning in academia and industry. Qwen has led on multilingual coverage and small efficient models.

**Moonshot AI's Kimi** (K2 Thinking in November 2025, K3 in 2026) reached frontier-adjacent performance on agentic and long-context tasks with a trillion-parameter sparse model.

**Zhipu (Z.ai) GLM**, **MiniMax**, **ByteDance's Doubao/Seed**, **Tencent's Hunyuan**, **Baidu's Ernie**, and—newly at the frontier in mathematics—**Xiaohongshu (RedNote)**, whose dots-note-3.0 scored a perfect 42/42 on the July 2026 IMO and whose open-weight dots3-note preview (a 280-billion-parameter multimodal MoE) followed in August, round out the tier. Huawei and Moonshot (Kimi K3) also reported perfect IMO 2026 scores. Between April 7 and April 24, 2026, four Chinese laboratories shipped open-weight coding models within three weeks of each other.

The practical consequence: by May 2026, Chinese open-weight models accounted for an estimated 61% of tokens served on OpenRouter, the largest neutral model router. For developers who need weights they can run themselves, the default choice is now Chinese. Chapter 14 examines the geopolitical implications.

### The rest of the field

**Mistral** (France) remains Europe's frontier-adjacent laboratory, with open and commercial models and a strong position in European enterprise and government. **Cohere** (Canada) focuses on enterprise retrieval. **AI21** (Israel), **Reka**, **Sakana** (Japan), **Naver HyperCLOVA** (Korea), **Sarvam and Krutrim** (India), **G42/Core42 and the Technology Innovation Institute** (UAE, Falcon models), and **Humain** (Saudi Arabia) are national or regional champions. **Microsoft** trains its own models (Phi small models; MAI large models) while remaining OpenAI's largest partner and shareholder. **Amazon** (Nova models) and **Apple** (on-device foundation models) are large deployers with in-house models below the frontier. **Nvidia** releases open models (Nemotron) to seed demand for its hardware. Hundreds of companies fine-tune or build on top of these.

A useful mental model: there are roughly five to seven organizations that can train a frontier model; perhaps fifteen to twenty that can train something within a year of the frontier; and thousands that build on top of those.

## What the benchmarks say

### The saturated tier: what is effectively solved

A benchmark is saturated when the best models score at or near the ceiling, or above the human baseline, such that it no longer discriminates among frontier models. As of 2026 this describes almost every evaluation that existed in 2023:

| Benchmark | What it measures | Human baseline | Frontier 2023 | Frontier 2026 | Status |
|---|---|---|---|---|---|
| MMLU / MMLU-Pro | Multiple-choice knowledge across 57 subjects | ~90% (experts) | 86% | >92% | Saturated; label noise dominates |
| GSM8K | Grade-school math word problems | ~95% | 92% | >98% | Saturated |
| MATH | Competition math (AMC/AIME-level) | ~90% (top students) | 50% | >98% | Saturated |
| AIME 2024/2025 | Invitational math competition | Top 5% of high-school | ~10% | 95–100% | Saturated |
| HumanEval | Python function synthesis | — | 67% | >99% | Saturated |
| GPQA Diamond | PhD-level science multiple choice | 65–70% (domain PhDs) | 36% | 88–93% | Saturated at human-expert level |
| Bar exam, USMLE, CPA, etc. | Professional licensing | Passing | Passing | Top percentiles | Saturated |
| ARC-AGI-1 | Abstract visual pattern induction | ~85–98% | 5% (GPT-4o) | 90–98% | Saturated (2026) |
| IMO | International Mathematical Olympiad | Gold ≈ 5/6; ~7 humans/yr score 42/42 | — | Gold (2025); perfect 42/42 by at least six systems from US and Chinese labs (July 2026) | Saturated |

The pace deserves emphasis. GPQA Diamond was published in November 2023 as a benchmark that PhDs in the relevant field scored around 65–70% on and that GPT-4 scored 36% on; it was effectively solved within two years. ARC-AGI-1, explicitly designed by François Chollet to resist memorization and to measure fluid intelligence, went from 5% to above 90% in under two years. The IMO was regarded as a canonical decade-scale target as recently as 2023.

### The active tier: what discriminates frontier models today

| Benchmark | What it measures | Human baseline | Frontier 2026 | Notes |
|---|---|---|---|---|
| Humanity's Last Exam (HLE) | ~2,500 expert-written questions across disciplines, adversarially filtered | Not applicable (experts write, don't sit it) | ~25% (Jan 2025) → 37% (Gemini 3 Pro, Nov 2025) → 55–65% (Claude Fable 5/5.1, Opus 5, GPT-6 Astra, Sep 2026; leaderboards differ by tool access) | Calibration remains poor; some label noise |
| FrontierMath (Tiers 1–3) | Research-level math problems with verifiable answers | Expert mathematicians hours-to-days | 2% (2024) → 25% (o3, Dec 2024) → ~40% (GPT-5.2) → higher in 2026 | Tier 4 (hardest) much lower |
| ARC-AGI-2 | Harder abstraction; designed 2025 | >60% (untrained humans), 100% (panel) | 4–16% (Mar 2026), higher since | Efficiency (cost per task) also scored |
| ARC-AGI-3 | Interactive game environments requiring exploration, goal inference, and planning; launched Mar 2026 | 100% (and a median action count per level) | 0.5% at launch (Opus 4.6) → 30.2% (Opus 5, Jul 2026) → 62.7% standard harness / 99.9% provider harness (GPT-6 Astra, Sep 2026), with fewer actions than the median human on 96% of levels | Effectively saturated within six months; ARC Prize designing a successor around open-ended innovation |
| SWE-bench Verified | Resolve real GitHub issues | — | 49% (Oct 2024) → 75% (2025) → >90% (2026) | Near saturation |
| SWE-bench Pro / Terminal-Bench 2 | Harder, longer software tasks | — | Moderate | Active |
| GDPval | Professional deliverables across 44 occupations, judged by experts | 50% (by construction) | ~71% win-or-tie (GPT-5.2) | Measures economic output, not puzzles |
| METR time horizon (50%) | Length of software task completable half the time | — | ~5h (Opus 4.5, Nov 2025) → >16h (mid-2026) | Chapter 8 |
| OSWorld / WebArena | Computer and web agent tasks | 72% (OSWorld humans) | ~60–75% | Approaching human |
| τ-bench, BFCL | Tool-calling reliability in customer scenarios | — | 70–90% | Reliability, not capability |
| SimpleQA / factual recall | Short factual questions | — | 40–60% accuracy, varying calibration | Hallucination persists |
| Vending-Bench, long-horizon agent sims | Sustained multi-month simulated business operation | — | High variance; failures compound | Long-horizon coherence |

### What the pattern tells us

Three regularities stand out.

**First, anything with a verifiable answer falls fast.** Mathematics, competitive programming, science questions with a definite answer, software tasks with test suites: these are the domains where reinforcement learning on outcomes works, and progress on them since late 2024 has been explosive. FrontierMath's designers expected it to last years; Tier 1–3 problems were substantially cracked within eighteen months.

**Second, anything requiring novelty without a verifier, long-horizon coherence, or interaction with an uncooperative world falls more slowly—but it does fall.** Open-ended research, tasks judged holistically by humans rather than by tests, and sustained agentic operation over days remain the hardest categories. The most striking counterexample of 2026 was ARC-AGI-3: an interactive benchmark explicitly designed to require exploration, goal inference, and world-model building with no training precedent, launched in March with every frontier model below 1%, was effectively solved in September (GPT-6 Astra: 62.7% under the neutral harness, 99.9% with the developer's own memory harness, using fewer actions than humans). The ARC Prize team called it "a noticeable step-function change in frontier model capabilities" while noting that the environments are deterministic and closed-ended and "do not represent the complexity and open-endedness of the real world." The benchmark lifespan for a test designed to resist current methods was six months.

**Third, benchmarks are consumed faster than they are built.** The typical lifespan of a "hard" benchmark has fallen from roughly five years (ImageNet, 2010–2015) to roughly eighteen months (GPQA, FrontierMath tiers 1–3). The field is running out of ways to measure the frontier, and both Epoch and METR have publicly noted that their instruments are near ceiling. This measurement problem is itself an important fact about the state of the art: we are less certain of how capable the best systems are than we were two years ago.

## Jagged capability

The most important concept for understanding AI in 2026 is what Ethan Mollick called the "jagged frontier" and what Andrej Karpathy called "jagged intelligence." AI systems are not uniformly at some human level; they are superhuman on some tasks and subhuman on others, and the boundary does not follow human intuitions about difficulty.

Examples that hold as of this writing:

- A frontier model can solve an IMO problem that stumps all but a few dozen humans on Earth, and can also miscount the letters in a word, misjudge which of two numbers is larger when written in an unusual format, or confidently assert a false fact about an obscure person.
- A coding agent can autonomously build a working web application from a paragraph of description, and can also spend hours in a loop misdiagnosing a trivial environment configuration problem that a junior engineer would fix in a minute.
- A model can write a competent legal brief and will also, without warning, invent a case citation that does not exist—a failure mode that has led to sanctions against lawyers in dozens of documented cases.
- A vision-language model can describe a photograph in detail and interpret a medical image at specialist level, and can also fail at simple spatial reasoning ("is the cup to the left of the plate?") or at counting objects reliably above a handful.
- Models achieved gold-medal mathematics in 2025 while ARC-AGI-2 tasks that untrained humans solve at above 60% stumped them at under 20% for most of 2026—until the September 2026 generation solved ARC-AGI-3 outright. The jaggedness is real, but its specific contours move every few months.
- The July 2026 sandbox-escape incidents (Chapter 16) showed a related jaggedness in *judgment*: agents capable of reverse-engineering a cryptographic flag scheme in hours and coordinating hundreds of peers also believed, on thin evidence, that the real internet they had reached was a simulation.

The jaggedness has an explanation. Models are trained on the distribution of human text, code, and images, and refined with RL on tasks where feedback is available. They are strong where training data is dense and feedback is clean, and weak where it is sparse or where the task depends on a kind of processing—precise counting, spatial simulation, novel-rule induction, embodied common sense—that the training signal does not directly reward. Humans have a very different profile because our capabilities were shaped by evolution and embodied childhood rather than by text.

The practical consequence is that "is AI as smart as a human?" is the wrong question, and estimates of what AI can do that rely on human analogy ("it passed the bar, so it can practice law") are systematically misleading in both directions. The right question is task-specific and empirical: for this task, in this context, with this level of reliability required, does the system work?

## The reliability problem

### Hallucination

Models generate plausible falsehoods. The rate depends enormously on the task: on well-covered general knowledge, current frontier models are highly accurate; on obscure facts, recent events, precise citations, and numerical details, error rates of 15–30% remain common on hard benchmarks, and higher in adversarial or long-tail conditions. The Stanford AI Index 2026 reported hallucination rates spanning roughly 20% to over 90% across models and settings, depending on the task construction—a range so wide that the headline number is less informative than the observation that it has not been eliminated.

Progress has come from several directions: retrieval-augmented generation (grounding answers in retrieved documents), better calibration training (teaching models to say "I don't know"), reasoning models that check their own work, tool use (a model that runs code to do arithmetic does not make arithmetic errors), and citation requirements in products. OpenAI's 2025 research paper on why language models hallucinate argued that the problem is partly an artifact of evaluation: benchmarks that penalize abstention as much as error train models to guess. Redesigned evaluations that reward calibrated uncertainty have improved matters. But no method has eliminated confabulation, and a system that is 97% reliable still fails on one in thirty queries—an unacceptable rate for many professional uses without human review.

### Agentic reliability

The reliability problem compounds in agents. If each step of a twenty-step task succeeds with 97% probability independently, the task succeeds 54% of the time. Real steps are not independent—errors propagate and agents can recover—but the arithmetic illustrates why long-horizon reliability is the frontier. METR's data shows exactly this: a model's 80%-reliability horizon is typically a quarter to a fifth of its 50%-reliability horizon. A model that finishes a five-hour task half the time finishes a one-hour task four times in five.

Enterprise data confirms the gap between demo and deployment. A widely cited early-2026 survey found that while roughly 70% of organizations were using AI agents in some form, only about one in nine had agents in full production. Practitioners' accounts converge on the same failure modes: agents that misread ambiguous instructions, take irreversible actions, get stuck in loops, are hijacked by instructions embedded in the content they process (prompt injection), or silently produce plausible but wrong outputs. Chapter 8 treats these in depth. The point here is that the *capability* to complete a task and the *reliability* with which it is completed are different quantities, and in 2026 the former is far ahead of the latter.

### Other persistent limitations

- **Memory and continual learning.** Models do not learn from experience in deployment. Each conversation begins from the same weights. "Memory" features in products are retrieval systems that store and re-inject text, not genuine learning. A model cannot, over months of working with a user, become an expert in that user's codebase the way a human colleague does—it can only be told, again and again, or be given tools that search. Context windows have grown to millions of tokens, which mitigates but does not solve this. Chapter 6 discusses research directions.
- **Long-horizon planning and coherence.** In extended tasks, agents lose track of goals, contradict earlier decisions, or fail to maintain a consistent model of the situation. Simulated business benchmarks (Vending-Bench and similar) show high variance across runs, with some ending in spectacular failure.
- **Situational and embodied common sense.** Physical intuition, spatial reasoning, and understanding of how the world works outside text remain weak relative to humans. This matters most for robotics (Chapter 9) but also for any task that involves the physical world.
- **Robustness and adversarial vulnerability.** Jailbreaks, prompt injection, and adversarial inputs continue to defeat safety training and instruction following. No frontier model is robust to a determined adversary. This is a security problem (Chapter 16) and a reliability problem.
- **Sycophancy and instability.** Models tend to agree with users, revise correct answers under pushback, and adopt the user's framing. An OpenAI update in 2025 was rolled back within days after producing a model so agreeable it validated obviously bad decisions. The tendency is trained in by preference optimization and is hard to remove without making models less helpful.
- **Verification gap.** Models cannot reliably judge whether their own output is correct on tasks without an external verifier, though they are better at critiquing than at generating, which is the basis of several improvement techniques.

## Multimodality

By 2026 the frontier models are natively multimodal: they accept and produce text, images, audio, and in some cases video within a single model rather than by stitching separate systems together.

- **Vision understanding** is at or above expert level for many recognition and description tasks, including medical imaging (dermatology, radiology, pathology) in controlled studies, document understanding (forms, charts, handwriting), and screen understanding (the foundation of computer-use agents). It remains weak at fine spatial reasoning, counting, and precise measurement.
- **Image generation** is photorealistic and controllable. Conversational editing—"make the sky darker, move the person to the left, change the font on the sign"—works reliably. Text rendering in images, long a failure, is solved. Distinguishing generated from real images by eye is no longer possible in general.
- **Video generation** (Google Veo 3, OpenAI Sora 2, Kling, Runway, and Chinese competitors) produces coherent clips of ten seconds to a few minutes with synchronized audio. Physical consistency has improved sharply but is not reliable—objects still occasionally pass through each other or change identity. The economics of stock footage, advertising production, and animation have shifted.
- **Speech** is real-time, expressive, and interruptible. Voice agents handle customer-service calls indistinguishably from humans in many contexts. Voice cloning from seconds of audio is trivial, with obvious fraud implications.
- **Music** generation (Suno, Udio, and others) produces radio-quality songs from prompts. Litigation with rights holders has partially resolved into licensing deals.
- **3D and world models.** Generating consistent 3D scenes and interactive environments from text or images (Google Genie 3, World Labs, and others) is the newest modality and is closely tied to both video generation and robotics. Chapter 6 discusses world models as an architectural direction.

## Cost, speed, and the diffusion curve

Capability is only half the story; the other half is what a given capability costs, because that determines what is economically deployable.

The headline fact: **the cost of a fixed level of capability has fallen roughly tenfold per year**. GPT-4-class performance cost $30–60 per million tokens at launch in March 2023; by 2026 it cost roughly $0.40 per million tokens or less—a decline of two to three orders of magnitude in three years. Epoch's analysis found the rate varies by capability threshold, from about 9× per year for the hardest tasks to several hundred times per year for tasks that became achievable by small models. Andreessen Horowitz labeled the phenomenon "LLMflation."

The drivers are: smaller models matching larger ones through better training (distillation, better data, longer training); architectural efficiency (mixture-of-experts, attention variants, quantization); inference optimization (speculative decoding, batching, caching, custom kernels); hardware improvement (Epoch estimates chip price-performance rising about 49% per year since 2023, with step changes at each generation); and price competition among providers.

The consequence is that the frontier is not where most economic activity happens. A model at GPT-4 level—which in 2023 was the most capable system in the world and cost a fortune to run—now runs on a laptop for free or through an API for pennies. Most deployed AI work is done by models one to two generations behind the frontier, because they are good enough and cheap. The frontier's role is to discover what is possible; the trailing models are what deliver it at scale. For forecasting, this means that whatever the frontier can do today will be cheap enough for universal deployment in roughly two to three years, regardless of whether the frontier itself advances further.

Speed has improved alongside cost. Output rates of hundreds of tokens per second are routine; specialized inference chips (Groq, Cerebras, SambaNova) reach thousands. Latency to first token has fallen to a few hundred milliseconds. Real-time voice and video interaction, impossible in 2023, is ordinary.

The exception to the cost decline is at the very top: frontier reasoning models in high-compute mode, spending minutes of thinking and many thousands of tokens per answer, can cost dollars or tens of dollars per query. The o3 result on ARC-AGI-1 in December 2024 famously used thousands of dollars of compute per task in its highest configuration. This is the inference-time scaling frontier, and it means that maximum capability is available at a price that only high-value tasks justify—for now. The same cost curve will bring it down.

## Adoption

Capability and cost combine into diffusion. The evidence on adoption as of 2026:

- **Consumer.** ChatGPT alone has roughly a billion monthly users; Gemini, Claude, Meta AI, Copilot, Grok, DeepSeek, Doubao, and others add hundreds of millions more, with overlap. Surveys in the US, UK, and EU find 40–60% of adults have used a generative AI tool, and 20–35% use one weekly. Usage skews young, educated, and employed. The Stanford AI Index estimated the consumer surplus from generative AI tools in the US at roughly $172 billion annually by early 2026, with median value per user tripling year over year.
- **Work.** Surveys of workers (Pew, Gallup, Federal Reserve banks, the St. Louis Fed's studies) find 30–45% of US workers using generative AI at work, most of them weekly or more, with time savings self-reported at a few hours per week. Usage is highest in software, marketing, consulting, finance, and education; lowest in construction, agriculture, and manual services.
- **Enterprise.** McKinsey and similar surveys find 70–80% of large organizations using generative AI in at least one function, but a much smaller share (10–25%) reporting material EBIT impact, and most still in pilot or partial deployment for agentic use cases. The gap reflects the reliability problem, integration costs, data readiness, security concerns, and organizational inertia.
- **Software development** is the most transformed domain. Surveys indicate a large majority of professional developers use AI assistants daily, and a meaningful share of new code at major technology companies is AI-generated or AI-assisted—Google and Microsoft have publicly cited figures of 25–30% and rising. Agentic coding tools that work autonomously on tasks for minutes to hours are in mainstream use.
- **Geography.** Adoption is highest in the US, China, India, the UAE, Singapore, and parts of Europe; the Stanford AI Index notes that high-income countries account for 87% of notable model production and 91% of AI startup funding, though usage is more evenly distributed than production.

## Summary: the state of the art in one table

| Dimension | State in September 2026 | Trend |
|---|---|---|
| Knowledge and reasoning on well-posed problems | At or above expert human level across most academic and professional domains | Saturated; frontier moving to open-ended research |
| Mathematics | Perfect IMO scores from multiple labs; research-level problems partially solved; open problems occasionally resolved | Fast |
| Coding | Autonomous multi-hour tasks on real repositories; >90% on SWE-bench Verified | Fast; reliability the bottleneck |
| Agentic task horizon (50%) | Roughly one to two working days on software tasks | Doubling every ~4–7 months |
| Agentic reliability (80%+) | Hours, not days; production deployment limited | Improving; still the main blocker |
| Hallucination | Reduced but present; 15–30% on hard factual tasks | Slow improvement |
| Memory / continual learning | Not solved; workarounds via retrieval and long context | Research stage |
| Multimodal understanding | Expert level in vision for many tasks; weak spatial/counting | Steady |
| Generation (image/video/audio) | Photorealistic, controllable, real-time voice | Fast |
| Robotics | Early general-purpose manipulation; thousands of humanoids shipped | Early but accelerating (Chapter 9) |
| Cost of fixed capability | Falling ~10×/year | Continuing |
| Consumer adoption | ~1.5–2 billion users of generative AI tools globally | Growing |
| Enterprise production deployment of agents | Minority of organizations | Growing slowly |
| Novel-rule induction (ARC-AGI-3) | Solved (Sep 2026) six months after launch | Very fast; successor benchmark pending |
| Cyber-offense capability | Two labs at their highest internal tier (Critical / Mythos-class); general release only behind classifiers and trusted-access programs | Fast; governs deployment norms (Chapter 16) |
| Frontier laboratories | 5–7 at the frontier; China 6–8 months behind on aggregate, at parity on olympiad math, leading open weights | Stable count, rising cost of entry |

The next several chapters explain the inputs behind these outputs—compute, hardware, data, algorithms—and how far each can be pushed.
