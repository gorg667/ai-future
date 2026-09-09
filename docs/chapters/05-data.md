# Data: The Wall, the Workarounds, and the Fight Over Who Owns It

!!! abstract "In brief"
    - The stock of high-quality human text is finite and largely consumed; the data wall is real for raw web text and has been partly circumvented.
    - Synthetic data works where there is a verifier (math, code) and is fragile where there is not; RL environments are the new data industry.
    - Courts are converging on: training on lawfully acquired data is fair use, piracy is penalized, outputs that reproduce works are actionable; licensing markets help large publishers only.
    - The open web is contracting as a result of the models trained on it; interaction data and proprietary corpora favor incumbents.

## The problem stated

A language model is a compression of its training data. Its knowledge, its style, its reasoning patterns, and its blind spots are inherited from what it read. For a decade, the recipe for a better model was a bigger model trained on more data, and the data was free: the public web, digitized books, code repositories, and scientific papers, scraped and filtered. That era is ending for three reasons. The stock of high-quality human text is finite and largely consumed. The legal and commercial terms under which it was taken are being contested in courts and renegotiated in licensing deals. And the internet is filling with model-generated content, so that future scrapes are increasingly of the outputs of past models.

This chapter examines how much data there is, when it runs out, what the substitutes are, how well they work, the legal landscape, and the emerging economy of data. The conclusion, in brief: the "data wall" is real for raw web text, has already been partly circumvented by synthetic data and reinforcement learning, and the decisive question is whether those substitutes deliver *generality* or only *competence in verifiable domains*.

## How much data is there?

### The stock of text

Epoch AI's 2024 analysis "Will We Run Out of Data?" estimated the total stock of public human-generated text at roughly 300 trillion tokens (with a range of 100 trillion to 1 quadrillion), counting the indexed web, books, and other sources. After quality filtering and deduplication—removing spam, boilerplate, machine translation, and near-duplicates—the usable portion for training is much smaller, perhaps 10–30% of the total.

Frontier training runs have consumed a large fraction of this. Llama 3 (2024) was trained on 15 trillion tokens; Llama 4, Qwen 3, and 2025–2026 frontier models on 30–40 trillion or more, often with multiple passes (epochs) over the highest-quality subsets. Epoch's central projection was that, at the historical growth rate of training data, frontier models would exhaust the effective stock of public text between 2026 and 2032, with a median around 2028. Since the analysis, the growth of dataset sizes has slowed—partly because of the wall itself and partly because effort shifted to post-training—so the date has drifted later, but the fundamental constraint stands: **there is at most about one more order of magnitude of human text to be had, and much of it is low quality.**

### What is not counted

The estimate covers *public* text. Substantial additional text exists in forms that are harder to access:

- **Private and enterprise data.** Corporate documents, emails, chat logs, and internal wikis dwarf the public web but are fragmented, confidential, and legally encumbered. Enterprise AI deployments use this data for retrieval and fine-tuning but it is not available for frontier pretraining.
- **Platform data.** Meta, Google, Microsoft, ByteDance, and Tencent hold vast proprietary corpora (social posts, YouTube transcripts, Gmail, Office documents, Douyin). They use some of it—Meta trains on public Facebook and Instagram posts; Google on YouTube—within legal and policy limits. This is a structural advantage for platform companies over pure laboratories.
- **Non-English and low-resource languages.** The web is disproportionately English (roughly half of content), and models are correspondingly better in English. Other high-resource languages (Chinese, Spanish, German, Japanese, French, Russian) have substantial corpora; thousands of languages have almost nothing. Chinese laboratories have an advantage in Chinese-language data that Western laboratories partially lack.
- **Books.** Anna's Archive and Library Genesis—pirate libraries containing millions of books—were used by several laboratories, as court filings in the *Kadrey v. Meta* and *Bartz v. Anthropic* cases revealed. The legal exposure this created (Anthropic's $1.5 billion settlement in 2025 was the largest copyright settlement in history) has changed practice: laboratories now buy and scan physical books or license from publishers.
- **Scientific literature.** Roughly 200 million papers exist, a majority behind paywalls. Licensing deals with publishers (Wiley, Taylor & Francis, Springer Nature, Elsevier) have made much of this available to laboratories since 2024.

### Other modalities

Text is the binding constraint because it is the most information-dense modality per token and the one that most directly encodes reasoning. Other modalities are more abundant:

- **Video.** YouTube alone holds hundreds of thousands of hours uploaded per day—on the order of 10¹⁵ tokens if tokenized at typical rates—and platforms like Douyin, TikTok, and Twitch add comparable volumes. Video is the largest untapped reservoir and is central to world-model research (Chapter 6). It is also redundant (most video frames add little information) and expensive to process.
- **Images.** Billions of image-text pairs from web crawls (LAION and successors) trained the generation models; proprietary platforms hold tens of billions more.
- **Audio.** Podcasts, radio, and music are large but less useful for reasoning.
- **Code.** GitHub's public repositories (roughly 100 billion tokens of high-quality code, more with lower quality) have been fully consumed. Code is unusual in that it comes with a verifier (does it run? do the tests pass?), which makes synthetic generation easy and reliable.
- **Sensor and robot data.** Tiny by comparison but growing (Chapter 9).
- **Genomic, chemical, and scientific data.** Structured, large, and increasingly important for scientific AI (Chapter 10).

## Why data quality matters more than quantity

The Chinchilla scaling law treats all tokens as equal. They are not. A series of results since 2022 established that data quality is a lever comparable to scale:

- **Textbook-quality data.** Microsoft's Phi series (2023–2025) trained small models on curated "textbook-like" text and synthetic exercises, achieving performance comparable to models several times larger trained on web text.
- **Filtering and deduplication.** The FineWeb and DCLM projects (2024) showed that careful filtering of Common Crawl—removing low-quality pages via classifiers trained on human judgments of educational value—improved downstream performance more than adding more raw data. FineWeb-Edu, filtered for educational content, outperformed much larger unfiltered sets.
- **Data mixing and curriculum.** The proportions of code, math, web, books, and multilingual content, and the order in which they are presented, materially affect capabilities. Adding code improves reasoning even on non-code tasks. Frontier laboratories treat their data mixtures as core intellectual property.
- **Annealing.** Ending training with a phase of very high-quality data (curated math, code, and instruction data) disproportionately improves final performance.

The implication is that the effective size of the usable corpus depends on how well one can identify and weight quality, and that the "wall" is soft: better filtering can extract more from the same raw stock. But this lever, too, has limits—one cannot filter one's way to more information than the corpus contains.

## Synthetic data

### What it is

Synthetic data is training data generated by a model rather than by humans. It takes several forms:

1. **Rephrasing and augmentation.** Rewriting existing text in different styles, expanding terse documents, translating across languages. This increases the effective number of tokens without adding new information; it helps models learn robustness to phrasing but does not push the knowledge frontier.
2. **Instruction and dialogue data.** Generating question-answer pairs, conversations, and task demonstrations. Alpaca (2023) used GPT-3.5 to generate fine-tuning data for Llama; virtually all post-training since has used model-generated instruction data. The Nemotron and Qwen teams have published detailed synthetic-data pipelines.
3. **Distillation.** A large "teacher" model generates outputs; a smaller "student" is trained to reproduce them. DeepSeek's R1 distillations into Qwen and Llama models, and the cost collapse of capable small models generally, depend on distillation. It transfers capability but does not create it.
4. **Verified reasoning traces.** A model generates many solution attempts to problems with checkable answers (math, code, formal proofs); only correct ones are kept; the model is trained on them. This is the mechanism behind reasoning models and is the most important form of synthetic data.
5. **Self-play and environment interaction.** A model generates its own problems, or interacts with a simulated environment, and learns from outcomes—the AlphaZero recipe applied to language.

### Does it work?

The evidence is mixed and domain-dependent.

**It works where there is a verifier.** In mathematics, code, formal logic, and games, a model can generate millions of candidate solutions, check them mechanically, and train on the correct ones. This produces genuine capability gains—the reasoning-model revolution (Chapter 7) is a synthetic-data success story. DeepSeek-R1's training involved generating hundreds of thousands of verified reasoning traces; AlphaProof generated and proved millions of formal statements. The bottleneck shifts from data to compute (generating and checking candidates) and to the design of problems and verifiers.

**It is fragile where there is not.** Shumailov et al. (2024, *Nature*) demonstrated "model collapse": training successive generations of models on their predecessors' unfiltered outputs leads to loss of diversity and drift toward the mode—tails of the distribution disappear. The result was widely cited as showing synthetic data is a dead end. Subsequent work (Gerstgrasser et al., 2024; Bertrand et al., 2024) showed that collapse is largely avoided when synthetic data *accumulates* alongside real data rather than replacing it, and when it is filtered by quality. The practical position is: synthetic data is a supplement and an amplifier, not a substitute for the human corpus, and its value depends on the quality of the filter.

**It does not add knowledge.** A model cannot generate facts about the world it does not know. Synthetic data can improve reasoning, robustness, format-following, and coverage of rare cases, but the model's knowledge of history, science, culture, and current events is bounded by human-generated sources. This is why retrieval, tool use, and continual learning (Chapter 6) matter: they are the ways a model gets new information after training.

### The emerging recipe

By 2026 frontier training runs use synthetic data extensively in a layered way: human web data (filtered and deduplicated) as the base; heavy synthetic augmentation in code, math, and reasoning; model-generated instruction data for post-training; and RL on verifiable tasks as the largest consumer of compute. Estimates of the synthetic share of frontier training tokens range from 20% to over 50%. The human corpus has become the *foundation* rather than the *whole* of training.

## Reinforcement learning environments

The most consequential development in data since 2024 is the shift from static datasets to interactive environments. A reasoning model trained with RL does not need a dataset of solutions; it needs a set of *problems* and a *verifier*. The problems can be generated, mined, or purchased; the verifier can be a test suite, a formal proof checker, a symbolic solver, a simulated environment, or another model.

This has created a new industry. Companies like Scale AI, Surge, Mercor, Turing, Toloka, and dozens of startups have shifted from labeling data to building RL environments: realistic simulations of software engineering tasks, customer-service interactions, scientific workflows, financial analysis, legal research, and computer use, each with graders. Laboratories spend hundreds of millions of dollars a year on environments; Meta's 2025 investment of over $14 billion in Scale AI was partly a bet on this. Expert humans—PhD mathematicians, senior engineers, physicians—are hired to write hard problems and evaluate solutions at rates of hundreds of dollars per hour. The "data labor" market has moved up-skill.

The limits of this approach define the limits of the reasoning paradigm. Environments with clean verifiers (math, code) are abundant. Environments with noisy or subjective verifiers (writing quality, strategic judgment, scientific taste, interpersonal skill) are hard to build and vulnerable to reward hacking—the model learns to satisfy the grader rather than the intent. The question of whether capability learned in verifiable environments *generalizes* to domains without verifiers is the central open problem (Chapter 7).

## The legal landscape

### Copyright

The training of models on copyrighted text, images, and code without permission is the subject of dozens of lawsuits in the United States, the United Kingdom, the European Union, Japan, India, and China. The central US question is whether such training is "fair use." As of 2026 the picture is:

- **Training on lawfully acquired books is likely fair use.** Judge Alsup in *Bartz v. Anthropic* (June 2025) held that using purchased books to train a model was "quintessentially transformative" and fair, but that acquiring pirated copies was not; Anthropic settled the piracy claims for $1.5 billion (about $3,000 per book across roughly 500,000 works). Judge Chhabria in *Kadrey v. Meta* (June 2025) also ruled for Meta on fair use but emphasized that the plaintiffs had failed to show market harm, leaving the door open to future claims that do.
- **Output-side infringement remains live.** *New York Times v. OpenAI and Microsoft* (filed December 2023) alleges both training infringement and regurgitation of articles in outputs; it proceeded through discovery in 2025–2026. Getty Images' UK case against Stability AI produced a 2025 ruling largely favoring Stability on the training claims. Music publishers' cases against Anthropic (lyrics) and the record labels' cases against Suno and Udio produced partial licensing settlements.
- **The EU** requires GPAI model providers under the AI Act to publish a "sufficiently detailed summary" of training content and to respect rights-holders' opt-outs under the text-and-data-mining exception. Compliance mechanisms (the Code of Practice, effective August 2025) are still being tested.
- **Japan** has the most permissive regime (its 2018 copyright amendment permits TDM for any purpose); **Singapore** is similar; **China** courts have found AI-generated images copyrightable by their human prompter in some cases and have ruled against unauthorized style imitation in others.

The trajectory is toward a settlement: training on lawfully obtained data is fair use or licensed; piracy is penalized; outputs that reproduce protected works are actionable; and a licensing market develops for high-value content. This is roughly what happened with music sampling and with search engines' use of snippets.

### The licensing economy

Since 2023 laboratories have signed content deals worth billions in aggregate: OpenAI with News Corp (reported $250 million over five years), Axel Springer, the Associated Press, the Financial Times, Condé Nast, Vox, The Atlantic, and Reddit ($60 million a year); Google with Reddit ($60 million a year) and others; Microsoft, Amazon, and Meta with news organizations; multiple laboratories with Shutterstock, Getty, and academic publishers. Reddit, Stack Overflow, and Wikipedia have moved from open access to paid API tiers for AI companies. Cloudflare in 2025 began blocking AI crawlers by default and introduced pay-per-crawl.

The economics are lopsided. Licensing revenue is meaningful for a few large publishers and trivial for most creators. The value of any individual document to a model trained on trillions of tokens is close to zero; the value of the corpus is enormous; and there is no mechanism to distribute the latter to the contributors of the former. Proposals for collective licensing (analogous to music performance rights) and for "data dividends" have not been implemented at scale.

### The web's changing terms

The open web was built on an implicit bargain: publishers allow crawling in exchange for traffic from search. AI breaks this: answer engines and AI overviews satisfy queries without a click. Publishers report referral traffic declines of 20–50% from Google since AI Overviews launched; some describe it as existential. The responses—blocking crawlers, paywalls, licensing, litigation—reduce the future supply of open text. Meanwhile, the share of new web content that is AI-generated has risen sharply; estimates of the share of new pages that are machine-generated range from a third to over half. Future crawls will thus be smaller, more encumbered, and more contaminated. Laboratories that already hold pre-2023 snapshots of the web have an asset that is no longer reproducible.

## Data as a strategic asset

Several implications follow.

**Platform companies have a structural advantage.** Google (Search, YouTube, Gmail, Android), Meta (Facebook, Instagram, WhatsApp), Microsoft (Office, GitHub, LinkedIn), Amazon (retail, AWS), ByteDance (TikTok, Douyin), and Tencent (WeChat) generate proprietary data at a scale no laboratory can match, and increasingly capture user interactions with their own AI products—which are themselves valuable training signal.

**Interaction data is the new frontier.** Every conversation with ChatGPT, every Claude Code session, every Gemini query is potential training data (subject to user consent and privacy settings). Laboratories with the most users learn the most about what users want and how models fail. This is a flywheel that favors incumbents.

**Enterprise data is the value in enterprise AI.** For businesses, the differentiator is not the model (which is a commodity) but the proprietary data the model is connected to. This is why retrieval-augmented generation, enterprise search, and data integration are large markets.

**Countries are asserting data sovereignty.** The EU's data regulations, India's push for domestic data residency, China's data-export controls, and Gulf states' investments in national datasets reflect a recognition that data, like compute, is a strategic resource. Sovereign AI (Chapter 14) is as much about data as about chips.

**Data privacy constrains and shapes AI.** GDPR enforcement against AI companies (Italy's temporary ban on ChatGPT in 2023; fines and investigations since), health-data regulations, and children's privacy rules limit what can be trained on and how. Federated learning, differential privacy, and synthetic data are partial technical responses.

## Forecast: data through 2030

| Question | Assessment |
|---|---|
| Does the text data wall stop frontier progress? | No. Pretraining data growth slows, but post-training and RL environments carry progress. Confidence: high. |
| Does synthetic data cause model collapse at the frontier? | No, given filtering and accumulation alongside human data. Confidence: high. |
| Does RL on verifiable tasks generalize to non-verifiable domains? | Partially. Reasoning skills transfer; judgment and taste transfer less. Confidence: medium. This is the key uncertainty. |
| Do licensing markets become a major revenue source for creators? | Modestly for large publishers; negligibly for individuals. Confidence: medium-high. |
| Does the legal system settle on training-as-fair-use for lawfully acquired data? | In the US, probably yes with output-side limits; the EU is more restrictive. Confidence: medium. |
| Do video and multimodal data become the main pretraining input? | Video becomes central for world models and robotics; text remains the core for reasoning. Confidence: medium-high. |
| Does interaction data from deployed products become the largest data advantage? | Yes; incumbents benefit. Confidence: high. |
| Do laboratories buy or generate expert data at scale? | Yes; the expert data market grows to several billion dollars a year. Confidence: high. |

The data story, then, is one of transition rather than exhaustion. The free lunch of the open web is over. What replaces it is a mix of synthetic generation, RL environments, licensed corpora, proprietary interaction data, and multimodal reservoirs—all more expensive, more legally structured, and more concentrated in the hands of large players than the corpus that built the first generation of models.
