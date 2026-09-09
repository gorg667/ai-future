# Multimodality and Embodiment: Vision, Video, Voice, Robots, and Self-Driving

## The gap between bits and atoms

Everything in the preceding chapters concerns AI operating on information: text, code, images, and audio flowing through digital systems. The physical world is different. It is continuous rather than discrete, it does not pause while a model thinks, it provides sparse and delayed feedback, it punishes errors with broken objects and injured people, and it generates almost none of the training data that made language models possible—there is no internet-scale corpus of robot experience. Hans Moravec observed in the 1980s that the things humans find hardest (chess, calculus) are easy for computers, and the things humans find effortless (walking, picking up a cup) are hardest for machines. Moravec's paradox held for four decades and is only now beginning to weaken.

This chapter covers the multimodal capabilities that connect models to perception (vision, audio, video generation), and then the two domains where AI meets the physical world at scale: autonomous vehicles, which are a decade into deployment and finally succeeding, and general-purpose robotics, which is at the beginning of its own foundation-model moment. The conclusion is that **embodied AI lags cognitive AI by roughly five to ten years, is now progressing on a recognizable version of the same recipe, and will be commercially significant in structured environments before 2030 and in unstructured ones after.**

## Multimodal perception and generation

### Vision understanding

Vision-language models became standard in 2023 (GPT-4V, Gemini, Claude 3) and native in 2024–2026: frontier models process images and video as first-class inputs alongside text. Capabilities in 2026:

- **Recognition and description**: at or above human level for common objects, scenes, text in images, charts, diagrams, and documents.
- **Medical imaging**: specialist-level in controlled studies for dermatology, radiology (chest X-ray, CT, mammography), pathology, and ophthalmology; dozens of FDA-cleared AI devices in radiology; deployment in screening programs (breast cancer in Sweden, Denmark, and the UK; diabetic retinopathy in India and Thailand). The gap between study performance and clinical deployment remains large, for regulatory, liability, and workflow reasons.
- **Screen understanding**: the foundation of computer-use agents; reliable enough for production.
- **Weaknesses**: fine spatial reasoning ("which object is farther from the camera?"), counting beyond small numbers, precise measurement, reading analog clocks and gauges, and out-of-distribution imagery. Vision models remain far less robust than language models to adversarial and unusual inputs.

### Audio and speech

Real-time, full-duplex speech (OpenAI's Advanced Voice Mode, Gemini Live, and successors) with natural prosody, interruption handling, and emotional expression became mainstream in 2024–2025. Speech recognition is at human parity in clean conditions across major languages and improving in noisy and accented speech. Speech synthesis is indistinguishable from human in short passages; voice cloning from a few seconds of audio is trivial and is a major fraud vector (impersonation of executives and family members for financial scams is a documented, growing crime category). Real-time translation with voice preservation—the "Babel fish"—works in earbuds and video calls. Music generation (Suno, Udio, Google's Lyria, and others) produces commercial-quality songs from prompts; the industry has moved from litigation toward licensing.

### Image generation and editing

Text-to-image (DALL·E, Midjourney, Stable Diffusion, Imagen, Flux, and the natively multimodal frontier models from 2025) is photorealistic, stylistically controllable, and—since 2025—conversationally editable with consistent characters and legible text. The distinction between "generated" and "photographed" is no longer detectable by eye and only partially by forensic tools. Consequences: stock photography and illustration markets have contracted sharply; advertising and product photography are increasingly generated; and the evidentiary status of images is contested (Chapter 13).

### Video generation

The fastest-moving generative modality. From Sora's announcement (February 2024) through Veo 3 (May 2025, with synchronized audio), Sora 2 (September 2025, with a social app), Kling, Runway Gen-4, Hailuo, and Seedance, video generation went from impressive-but-flawed clips to coherent, photorealistic, sound-synced sequences of up to several minutes. Physical consistency is much improved but not perfect; long-range narrative coherence remains hard. Applications: advertising, pre-visualization, social content, education, and the beginnings of AI-generated episodic content. Video models are also implicit world models (Chapter 6) and are being used to generate training data for robots.

### 3D and spatial

Generating 3D assets, scenes, and navigable environments from text or images (World Labs' Marble, Google's Genie 3, Nvidia's Cosmos, and others) matured in 2025–2026. This is the modality that connects generation to embodiment: a system that can imagine a 3D world consistently can, in principle, plan actions within it.

## Autonomous vehicles

### Where things stand

Self-driving is the oldest embodied-AI deployment and the one most often cited as a cautionary tale about timelines: Google's project began in 2009; confident predictions of ubiquitous robotaxis by 2020 failed. Yet by 2026 it is also a success story—the first physical-world AI operating at commercial scale without humans in the loop.

- **Waymo** (Alphabet) operates fully driverless ride-hailing in about a dozen US metropolitan areas (Phoenix, San Francisco, Los Angeles, Austin, Atlanta, Miami, Dallas, Houston, San Antonio, Orlando, Washington DC, and others in rollout), with about 3,000 vehicles, roughly 500,000 paid rides per week in mid-2026, over 100 million fully autonomous miles by mid-2025 and several times that since, and freeway operation. Its safety record—published peer-reviewed comparisons showing roughly 80–90% fewer injury crashes and serious-injury crashes than human drivers over the same roads—is the strongest evidence that AI can exceed humans at a safety-critical physical task. It remains unprofitable, with losses estimated in the low billions per quarter, and its expansion is constrained by vehicle supply, mapping, and regulation. Annualized revenue was estimated at a few hundred million dollars in early 2026.
- **Baidu Apollo Go** is the closest competitor, with over 22 million cumulative rides, more than 350,000 weekly rides at peak, fully driverless operation in Wuhan, Beijing, Shenzhen, and other Chinese cities, and international expansion (Dubai, Abu Dhabi, Switzerland). Pony.ai and WeRide operate at smaller scale in China and the Gulf.
- **Tesla** launched a robotaxi service in Austin in June 2025 with safety monitors and expanded through 2026, and has shipped supervised Full Self-Driving to millions of vehicles. Its camera-only, end-to-end-learned approach differs from Waymo's lidar-plus-maps stack. Its rate of unsupervised expansion has lagged its announcements, and it operates below fleet capacity.
- **Zoox** (Amazon) operates purpose-built vehicles in Las Vegas and San Francisco. **Wayve** (UK) and **Nuro** provide end-to-end driving software to automakers. **May Mobility**, **Motional**, and others operate at smaller scale. Cruise (GM) was shut down in late 2024 after a pedestrian-dragging incident and regulatory fallout—a reminder of how a single failure can end a program.
- **Trucking**: Aurora began driverless commercial freight in Texas in 2025; Kodiak, Plus, and Waabi are in or near commercial operation. Highway trucking is structurally easier than urban driving and economically compelling.

### Lessons

Self-driving took roughly fifteen years from research demonstration to commercial deployment. The reasons for the delay are instructive for robotics generally: the long tail of rare situations; the need for reliability many orders of magnitude beyond demo performance (a car that handles 99.9% of situations crashes constantly); the cost and slowness of collecting real-world data; regulatory and liability caution; and the shift in method—from hand-engineered modular pipelines to end-to-end learned systems—that had to happen mid-course. The breakthrough came from data scale (billions of miles, real and simulated), foundation-model-style learning, and enormous capital patience.

### Forecast

By 2030 the author expects robotaxis to operate in most large US and Chinese metropolitan areas and a growing number of cities in Europe, the Gulf, and Asia; driverless highway trucking to be routine on major corridors; and consumer vehicles to offer eyes-off highway driving broadly. The transition of the full vehicle fleet will take decades, but the demonstration that AI drives more safely than humans will have been made at scale, with consequences for insurance, urban planning, and the roughly 5 million Americans (and tens of millions globally) who drive for a living.

## General-purpose robotics

### Why robotics is hard

Language models had three gifts robotics lacked: internet-scale data, a discrete and forgiving action space (tokens), and instant, safe feedback. Robots must perceive continuous, cluttered, changing environments; control high-dimensional bodies with imperfect actuators and sensors; act in real time; and learn from experience that is slow, expensive, and dangerous to collect. A robot that drops a glass has destroyed its training example.

Historically, robotics addressed this with engineering: structured environments (factory cells), fixed tasks, hand-designed controllers. Industrial robots—about four million installed worldwide, a majority in China—are precise, fast, and fundamentally dumb: they repeat programmed motions. The goal of the current wave is the opposite: general-purpose robots that can be told what to do in natural language and figure out how in unstructured environments.

### The foundation-model recipe arrives

Between 2023 and 2026 the recipe that worked for language was adapted to robotics:

**Vision-language-action (VLA) models.** A VLA takes camera images and a language instruction and outputs robot actions, built on a pretrained vision-language model that supplies world knowledge and language understanding, with an action head trained on robot demonstrations. Google's RT-1 (2022) and RT-2 (2023) established the approach; the open-source OpenVLA (2024) and Octo democratized it; Physical Intelligence's π0 (October 2024), π0.5 (2025, generalizing to unseen homes), and π*0.6 (2025–26, improving from real-world failures and corrections via RL) set the pace among startups; Figure's Helix (February 2025) runs a dual-system architecture (a slow VLM for reasoning, a fast policy for control) on its humanoids; Google DeepMind's Gemini Robotics (March 2025), Gemini Robotics 1.5 and the on-device variant (2025), and Gemini Robotics 2 and ER 2 (2026) bring the Gemini family's reasoning to embodied control; Nvidia's GR00T N1 provides an open foundation model for humanoids; Unitree open-sourced a VLA (UnifoLM-VLA-0) in March 2026.

**Data at scale.** The Open X-Embodiment dataset (2023) pooled demonstrations from dozens of labs and robot types. Companies now collect data through fleets of teleoperated robots (Tesla, Figure, 1X, Agility, and Chinese firms run warehouses of operators), through human video (egocentric footage of people doing tasks, used to pretrain motion priors), and through simulation (Nvidia Isaac, Genesis, and generative world models producing synthetic experience). Data remains the binding constraint, and the "robot data flywheel"—deploy robots, collect experience, improve, deploy more—is the strategy every company is pursuing.

**Simulation-to-real transfer.** Training in simulation is fast, cheap, and safe; the challenge is that simulated physics and rendering differ from reality. Progress in domain randomization, photorealistic rendering, and learned simulators (world models) has made sim-to-real practical for locomotion (the reason quadrupeds and humanoids now walk robustly) and increasingly for manipulation.

**Reinforcement learning in the real world.** Fine-tuning policies from real-world outcomes and human corrections (π*0.6's approach, and analogous work at Google and others) closes the loop, so robots improve on the job.

### Humanoids

The humanoid form factor became the focus of investment in 2024–2026 for a simple reason: the built environment is designed for human bodies, so a robot with a human form can, in principle, do anything a human worker does without changing the environment. The landscape:

- **Tesla Optimus**: Gen 3 unveiled 2026; Musk has forecast millions of units per year, a forecast the author discounts heavily given the company's record on timelines; actual deployment is in Tesla's own factories at small scale.
- **Figure AI**: Figure 02 and 03; pilot deployment at BMW; valued at about $39 billion in 2026; Helix VLA; targeting home deployment.
- **Agility Robotics Digit**: bipedal but not humanoid in detail; the first humanoid-class robot in paid commercial work (moving totes at GXO and Amazon warehouses).
- **Boston Dynamics Atlas** (Hyundai): electric redesign (2024); factory pilots at Hyundai; the most capable dynamic mover.
- **1X NEO**: home-focused, soft-bodied; consumer pre-orders opened 2025 at about $20,000, with teleoperation fallback.
- **Apptronik Apollo**: Google DeepMind partnership; valued at $5.5 billion.
- **Unitree** (China): the volume leader—self-reported 5,500+ humanoids shipped in 2025 (analysts estimate around 4,200), with the G1 at about $16,000 and H2 flagship; also the dominant quadruped maker. **AgiBot**, **UBTech**, **Fourier**, **Galbot**, **Xpeng**, and dozens of other Chinese companies; China's government has designated humanoids a strategic industry, and China produces the majority of units globally.

Reality check: production volumes lag announcements by three to five times; the total global humanoid fleet in 2026 is on the order of tens of thousands, most in demonstrations, research, and pilots; the number doing sustained economically productive work unsupervised is small. Battery life (two to four hours), hand dexterity, reliability, and cost ($20,000–150,000) remain limiting. The bull case rests on the same logic as language models—that scale of data and compute will produce general competence—and the evidence so far is that manipulation capability is improving at a rate reminiscent of language models circa 2019–2020: impressive demos, rapidly improving generality, not yet reliable enough for unsupervised deployment in unstructured settings.

### Non-humanoid robotics

Humanoids get the attention; other forms do the work. Warehouse robots (Amazon's more than one million, Symbotic, Locus, Geek+), surgical robots (Intuitive's da Vinci performing millions of procedures, with increasing autonomy research), agricultural robots (weeding, harvesting), drones (delivery pilots by Zipline, Wing, and Amazon; and the transformation of warfare—Chapter 14), quadrupeds for inspection, and cobots in manufacturing are all being upgraded with foundation-model perception and language interfaces. The near-term economic impact of AI in robotics will come mostly from making these specialized systems more flexible, not from humanoids.

### Forecast

| Milestone | Author's median | Range |
|---|---|---|
| Humanoids in sustained unsupervised warehouse/factory work at >10,000 units | 2028 | 2027–2030 |
| >100,000 humanoids shipped per year globally | 2029 | 2028–2032 |
| General-purpose home robot doing laundry, dishes, tidying reliably, <$30,000 | 2031 | 2029–2036 |
| Robot manipulation matching skilled human on most factory tasks | 2032 | 2029–2040 |
| Robotaxis in majority of large US and Chinese metros | 2029 | 2028–2032 |
| Driverless trucking routine on major US corridors | 2028 | 2027–2030 |
| AI-controlled surgical subtasks autonomous in routine use | 2030 | 2028–2035 |

The author's overall assessment: robotics is where language models were in 2019–2020—the recipe is identified, the scaling is beginning, and the results are improving fast but not yet reliable. The lag behind cognitive AI is five to ten years, and it is closing, because the cognitive models supply the perception and reasoning that robotics lacked. The economic and social implications (Chapter 11–12) are that physical labor is *not* immune to automation; it is simply later in the queue, and the 2030s will be for manual work what the late 2020s are for cognitive work.

## Implications of embodiment for AI generally

Two further points deserve mention.

**Embodiment as a path to common sense.** The LeCun critique (Chapter 6) holds that text alone cannot teach the physics and causality that underlie common sense. Robots and world models trained on video and interaction are the test of that claim. If embodied models develop robust physical intuition and it transfers back to language models—as multimodal training already partially does—it would address one of the persistent weaknesses of current AI.

**Embodiment as the boundary of safety.** An AI that acts only in software can be sandboxed, monitored, and rolled back. An AI that controls physical systems—vehicles, robots, infrastructure—cannot be undone. The safety frameworks of Chapter 16 were designed largely around digital risks; extending them to embodied systems is an open problem that becomes urgent as robots leave the factory.
