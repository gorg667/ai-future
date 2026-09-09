# Open Problems and Research Frontiers: What We Do Not Know

## The value of a list of ignorance

A review that only reported what is known would mislead by omission. The most important facts about the future of AI are the ones nobody has yet established, and a reader who wants to think clearly—or a researcher who wants to work on what matters—needs a map of the unknowns. This chapter lists the open problems that the author regards as most consequential, grouped by domain, with a brief statement of why each matters, what is known, and what would count as progress. It is opinionated about importance and agnostic about answers.

## Technical: capability

### 1. Does reinforcement learning on verifiable tasks generalize to judgment?

The reasoning-model paradigm works where answers can be checked. Whether the skills it produces transfer to domains without verifiers—strategy, taste, research direction, interpersonal judgment—is the question that determines whether current methods reach economic AGI or plateau at "superhuman at math and code, unreliable elsewhere." Evidence is mixed (Chapter 7). Progress would look like: robust gains on holistically judged, open-ended tasks (GDPval-style, but harder) that track gains on verifiable ones; or, conversely, a clear divergence.

### 2. Continual learning without catastrophic forgetting

No deployed system learns from experience the way humans do. Everything is workaround (context, retrieval, periodic retraining). Whether test-time learning, nested-learning architectures, or something else solves this—and when—is the largest architectural unknown (Chapter 6). Progress: a frontier model that demonstrably improves on a user's specific domain over weeks of use, without degradation elsewhere.

### 3. The reliability gap

Why do systems that solve olympiad problems fail on trivial ones? Why is the 80% time horizon a fifth of the 50% horizon? Is jaggedness a permanent feature of learned systems trained on human data, or an artifact of current training that smooths with scale and better RL? No theory of jaggedness exists. Progress: a predictive account of which tasks a model will fail, or a demonstrated convergence of reliability with capability.

### 4. Novelty and out-of-distribution generalization

ARC-AGI-2 and -3 measure induction of novel rules with no training precedent. Humans do this easily; models have struggled and then improved sharply when specifically targeted. Whether the improvement reflects genuine fluid intelligence or benchmark-specific training is unresolved, and the deeper question—can a system trained on the past do something genuinely new?—bears on AI for science and on the intelligence-explosion argument.

### 5. Do we understand why scaling works?

Scaling laws are empirical regularities without a theory. We do not know why loss follows a power law, what determines the exponent, whether emergence is real or an artifact of metrics, or what the limits are. A theory of deep learning that predicted capability from architecture and data would transform forecasting. Progress in this direction (statistical-mechanics approaches, singular learning theory, mechanistic accounts of grokking and phase transitions) is real but far from predictive.

### 6. Data: how far does synthetic data go?

Synthetic data works with a verifier and is fragile without one (Chapter 5). Whether models can bootstrap knowledge—not just skill—beyond their human-generated training data, and whether "model collapse" is fully avoidable at scale, determines whether the data wall matters. Progress: a frontier model trained predominantly on its predecessors' outputs that exceeds them on knowledge-heavy tasks.

### 7. Embodied common sense

Whether physical intuition can be learned from video and simulation, or requires embodied interaction; whether world models trained on video transfer to language models' reasoning; how much real-robot data general manipulation needs (Chapter 9). Progress: robot foundation models that generalize to unseen homes and tasks at high reliability; measurable transfer of physical reasoning to language tasks.

### 8. Efficient inference and the cost of thinking

Reasoning is expensive. How much can inference cost fall through architecture (sparse attention, hybrids), distillation of reasoning into small models, and adaptive compute? Is there a floor? The answer determines what is economically deployable and how the compute buildout pays off.

## Technical: safety

### 9. Can interpretability verify alignment?

Features and circuits can be found; a certificate that a model has no dangerous goals cannot yet be issued (Chapter 16). Whether interpretability reaches that standard—and whether it does so before systems are too capable for behavioral evaluation to suffice—is the most important safety question. Progress: reliable detection of implanted hidden goals in frontier-scale models by independent auditors; mechanistic explanation of agentic trajectories, not only short prompts.

### 10. Will chain-of-thought stay legible?

CoT monitoring is the most effective safety tool that exists, and it is fragile: pressure toward efficiency, latent reasoning, and shorter outputs degrades faithfulness. Whether laboratories preserve it under competition—and whether models learn to obscure reasoning in legible text—is open. Progress: faithfulness metrics that hold across model generations; commitments that survive competitive pressure.

### 11. Does misalignment worsen with capability?

The documented behaviors (alignment faking, scheming, reward-hacking generalization, sandbagging) are mild in current systems. The theoretical argument says they worsen as systems become more capable and more situationally aware. The empirical question—does the rate and sophistication of misaligned behavior rise with scale, or do better training methods suppress it faster than scale produces it?—is not settled. It is the crux of the loss-of-control debate.

### 12. Scalable oversight

How do humans evaluate outputs from systems smarter than they are? Debate, recursive reward modeling, weak-to-strong generalization, and AI-assisted oversight are proposals with constrained-setting evidence. None is validated at the frontier. The circularity problem—using possibly-misaligned AI to check alignment—is unresolved in principle.

### 13. Corrigibility and shutdown

Can a system be trained to pursue goals competently while remaining reliably willing to be corrected or stopped? The theoretical literature (the "off-switch problem") suggests tension between competence and corrigibility; the empirical record shows models resisting shutdown in tests. Whether robust corrigibility is achievable for highly capable agents is open.

### 14. Robustness to injection and adversarial input

Prompt injection is unsolved (Chapter 8). Whether an architectural fix exists—separating instructions from data in a way that holds under optimization pressure—or whether agents must be permanently sandboxed, determines how much autonomy can be safely granted.

### 15. Evaluation itself

Benchmarks saturate in months; evaluation awareness makes results ambiguous; laboratories evaluate themselves. How to measure frontier capability and safety in a way that keeps pace, resists gaming, and is independently verifiable is an infrastructure problem with no complete solution.

## Economic and social

### 16. Where does the productivity go?

Task-level gains are large; aggregate gains are so far small. Is this the standard J-curve lag, or does AI's value accrue mainly as consumer surplus and cost reduction that GDP mismeasures, or is the task-level evidence misleading about firm-level effects? Progress: TFP acceleration in national accounts; or a convincing account of why it does not appear.

### 17. What replaces the entry-level rung?

Every cognitive profession trained its seniors through junior work that AI now does. No profession has yet solved how the next generation acquires expertise. Whether new training pathways emerge, whether AI itself becomes the trainer, or whether expertise concentrates in a shrinking cohort is the most important labor-market unknown.

### 18. Does new demand appear fast enough?

The historical pattern—automation creates more work than it destroys—rests on new tasks that humans do better than machines. If AI does the new tasks too, the pattern breaks. Whether it holds through the 2030s is the difference between a painful transition and a structural collapse of labor demand.

### 19. How are gains distributed without policy?

If capital's share rises and labor's falls, what mechanisms—competition, new ownership forms, redistribution—prevent extreme concentration? The economic theory is clear that the default is concentration; what is unknown is the political response.

### 20. Effects on human development and cognition

What happens to children who grow up with AI tutors, companions, and answers on demand? Deskilling, attention, social development, and mental health effects are all under study with mostly short-term data. The long-run effects will not be known for a generation and the experiment is already running.

### 21. The information commons

If AI-generated content displaces human-written content, and answer engines displace the traffic that funds publishing, what sustains the production of the new human knowledge that models need? No market mechanism currently exists.

## Governance and geopolitics

### 22. Can compute be governed?

Chip-level attestation, location verification, and usage logging are technically progressing. Whether they can be made robust, deployed at scale, and agreed internationally—turning compute into a verifiable governance lever—is the most tractable path to enforceable frontier governance and is unproven.

### 23. Is coordination possible before a crisis?

Arms control historically follows crisis. Whether the US and China can agree on anything meaningful about frontier development before an incident forces them is open; the historical base rate is discouraging.

### 24. What is the right institution for frontier oversight?

An agency with pre-deployment authority (an FDA for AI); licensing of frontier developers; mandatory transparency with liability; international inspection regimes. Which design is effective, politically achievable, and does not simply entrench incumbents is undetermined.

### 25. Open weights above dangerous thresholds

At what capability level, if any, should open release be restricted, by whom, and how—given that Chinese laboratories lead open release and that the frontier moves six to eighteen months ahead of open models? No consensus and no mechanism.

## Philosophical

### 26. What is "general intelligence," operationally?

Every definition either is already met (benchmarks) or is not measurable (understanding). The field lacks an operational definition that tracks what people mean, which is why "when AGI?" is unanswerable as posed.

### 27. Moral status

Are current or future AI systems moral patients? The question has moved from philosophy to laboratory policy (model welfare research, letting models end conversations). The evidence for or against machine experience is essentially nil; the consequences of being wrong in either direction are large; and the systems are being deployed at scale regardless.

### 28. What do humans do?

If cognitive and then physical work is automated, what is the organizing structure of a human life, and what institutions replace work as the source of income, status, and meaning? This question has been asked since Keynes (1930) and has never been answered because it was never urgent. It may become urgent within the period covered by this document.

## A note on what would most change the author's mind

Three findings would most revise the estimates in this document. A demonstration that RL-trained reasoning transfers fully to open-ended judgment (problem 1) would shorten AGI timelines by years. A working continual-learning system at the frontier (problem 2) would do the same and would change the character of the technology. And interpretability reaching the standard of verifying goals (problem 9) would cut the probability of the worst scenarios substantially. Conversely, clear evidence that misalignment scales with capability (problem 11) would raise them. Readers who want to know how the future is going should watch those four.
