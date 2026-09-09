# Governance and Regulation: Laws, Standards, Institutions, and the Control of Compute

## The regulatory landscape in one paragraph

By 2026 the world has three distinct regulatory models for AI. The European Union has enacted a comprehensive, risk-tiered statute (the AI Act) whose implementation it is now partly deferring under competitiveness pressure. The United States has no federal AI statute; it governs through executive orders that have swung between administrations, sectoral agency action, procurement conditions, a patchwork of state laws (with California and New York enacting the first frontier-model transparency laws), and a federal effort to preempt those state laws. China regulates content and alignment with state goals through detailed administrative rules issued rapidly by its cyberspace regulator, while treating AI development as a national priority. Everyone else is choosing among these models or waiting. Below the level of statute, a thicker layer of standards, voluntary commitments, safety frameworks, and institutional capacity is forming—and the most technically consequential governance lever, control of compute, remains mostly a geopolitical instrument rather than a safety one.

This chapter surveys each jurisdiction, the cross-cutting mechanisms (safety frameworks, evaluations, standards, liability, compute governance), the central debates, and what to expect.

## The European Union

### The AI Act

Adopted in 2024 after three years of negotiation, the AI Act is the first comprehensive statutory regime for AI. Its structure:

- **Prohibited practices** (effective February 2025): social scoring by governments, manipulative or exploitative systems, real-time remote biometric identification in public for law enforcement (with exceptions), emotion recognition in workplaces and schools, untargeted facial-image scraping, and predictive policing based on profiling alone.
- **General-purpose AI (GPAI) models** (obligations from August 2025): all providers must maintain technical documentation, publish training-content summaries, and comply with copyright law; providers of models with "systemic risk" (presumptively those trained above 10²⁵ FLOP, which covers all frontier models) must additionally conduct evaluations and adversarial testing, assess and mitigate systemic risks, report serious incidents, and ensure cybersecurity. A Code of Practice, finalized in July 2025 and signed by most major laboratories (with Meta a notable refusal and xAI signing only the safety chapter), provides the compliance pathway.
- **High-risk systems** (originally August 2026): AI used in critical infrastructure, education, employment, essential services, law enforcement, migration, and justice, plus safety components of regulated products. Obligations include risk management, data governance, documentation, human oversight, accuracy and robustness, and conformity assessment.
- **Transparency**: disclosure when interacting with AI, labeling of deepfakes and synthetic content, and (for GPAI) machine-readable marking of outputs.
- **Governance**: a European AI Office within the Commission (responsible for GPAI), national market-surveillance authorities, an AI Board, a scientific panel, and penalties up to 7% of global turnover for prohibited practices and 3% for other violations.

### The Digital Omnibus and the retreat

By 2025 European industry, several member-state governments, and the Draghi competitiveness report argued that the Act's timeline was unworkable—technical standards were not ready, national authorities were not staffed, and compliance costs would disadvantage European firms. The Commission's Digital Omnibus proposal (November 2025) deferred the high-risk obligations; political agreement in mid-2026 set standalone high-risk systems (Annex III) to December 2027 and product-embedded high-risk systems to August 2028, alongside simplifications to documentation, SME relief, and adjustments to the GPAI regime. The Act thus became "generally applicable" on 2 August 2026 with its most demanding provisions postponed.

### Assessment

The AI Act is the most serious attempt anywhere to regulate AI comprehensively, and its GPAI provisions constitute the only binding obligations on frontier laboratories in any major jurisdiction. Its weaknesses: it was designed around 2021-era product-safety thinking and had to be retrofitted for foundation models; its high-risk categories are administratively heavy; enforcement capacity is thin; and the deferral signals that Europe's political will is limited when competitiveness is at stake. Its strengths: the "Brussels effect" is real—laboratories build compliance into global products—and its transparency, labeling, and incident-reporting requirements are becoming de facto international norms. Whether it becomes the template (as GDPR did for privacy) or a cautionary tale depends on whether Europe develops an AI industry to go with its rules.

## The United States

### Federal

There is no comprehensive federal AI law and, as of 2026, little prospect of one passing Congress soon. Federal governance operates through:

- **Executive orders.** Biden's EO 14110 (October 2023) required reporting of large training runs (above 10²⁶ FLOP), red-teaming, and safety standards development, and created the AI Safety Institute at NIST. Trump rescinded it in January 2025; his AI Action Plan (July 2025) emphasized deregulation, infrastructure, exports, and "ideological neutrality" in federally procured models; a December 2025 executive order ("Ensuring a National Policy Framework for AI") asserted federal preemption of state AI laws, created a Justice Department AI Litigation Task Force to challenge them, and conditioned discretionary federal funding on states' AI policies; March 2026 legislative recommendations proposed a uniform federal framework with express preemption. National-security-focused orders addressed frontier models and critical infrastructure.
- **Agency action.** The FTC (unfair and deceptive practices; enforcement against AI-washing and against companion-app harms to minors), the EEOC and CFPB (discrimination in hiring and lending), the FDA (medical devices; hundreds of cleared AI products), the SEC (disclosure), the FCC (AI robocalls), the Copyright Office (registration and training-data reports), and NIST (the AI Risk Management Framework; the renamed Center for AI Standards and Innovation, which evaluates frontier models under voluntary agreements) all regulate AI within existing mandates.
- **Export controls** (Commerce Department; Chapter 14).
- **Procurement.** The federal government is the largest buyer; its terms (OMB guidance; the "unbiased AI principles" order) shape products.
- **Voluntary commitments.** The 2023 White House commitments from frontier laboratories (red-teaming, watermarking, information sharing) and subsequent agreements with the safety institute on pre-deployment testing.

### State

In the absence of federal law, states legislated. By 2026 roughly a thousand AI bills had been introduced and over a hundred enacted, covering deepfakes in elections and intimate imagery (most states), disclosure of AI use in various contexts, healthcare and insurance decision-making, employment screening, companion chatbots (California's SB 243; New York), government use, and—most consequentially—frontier models:

- **California SB 53** (Transparency in Frontier AI Act, September 2025, effective January 2026): the first US frontier-model law. Developers above a compute and revenue threshold must publish safety frameworks, report critical incidents, and protect whistleblowers; it replaced the vetoed SB 1047 (2024), which would have imposed liability and shutdown requirements, with a "trust but verify" transparency model.
- **New York RAISE Act** (signed December 2025, effective January 2027): similar transparency and incident-reporting requirements for large developers, with attorney-general enforcement.
- **Colorado AI Act** (2024): comprehensive duties for high-risk AI in consequential decisions; delayed twice, narrowed, now effective January 2027.
- **Texas TRAIGA** (effective January 2026): prohibitions on specific harmful uses, a regulatory sandbox, and government-use rules—a lighter-touch model.
- **Utah, Illinois, and others**: disclosure and sectoral rules.

The federal preemption push of 2025–26 (a proposed ten-year moratorium on state AI laws was stripped from the 2025 reconciliation bill by a 99–1 Senate vote; the December executive order pursued the goal administratively) has produced litigation and uncertainty. The constitutional question—whether the executive can preempt state law without congressional action—is unresolved. The practical result is that state laws remain on the books, companies comply with the strictest (California's), and Congress is under pressure to legislate a national standard that would displace them.

### Assessment

US governance is fragmented, reactive, and shaped by the administration in power, with the result that the world's leading AI developers operate under thinner binding obligations than in Europe or China—while being subject to the most intense scrutiny from courts (copyright, product liability, wrongful death), from state attorneys general, and from the press. The most durable elements are the technical infrastructure (NIST frameworks, evaluation capacity), the sectoral regulators, and the emerging state frontier-transparency model. The most likely path to federal legislation is a bargain that trades preemption for national transparency and incident-reporting standards resembling SB 53.

## China

China has regulated AI faster and more specifically than any other major power, through administrative rules from the Cyberspace Administration of China (CAC) and allied ministries rather than through comprehensive statute:

- **Algorithmic recommendation rules** (2022): transparency, user opt-out, and prohibition of manipulative practices.
- **Deep synthesis rules** (2023): labeling and consent for synthetic media.
- **Generative AI measures** (August 2023): providers must ensure content reflects "core socialist values," take responsibility for training data legality, label outputs, protect personal information, and register with the CAC—creating a licensing regime under which hundreds of models have been approved.
- **AI content labeling measures** (effective September 2025): mandatory explicit and implicit (metadata) labels on all AI-generated content, with platform obligations to detect and label.
- **Standards**: TC260's technical standards on training-data security, content moderation, and model safety, which function as de facto binding requirements.
- **A draft comprehensive AI law** has circulated since 2023 but has not been enacted; the State Council's legislative plans list it as a lower priority than development.
- **AI safety**: China participated in international dialogues, established an AI safety governance framework (2024), and its 2025 "AI Plus" policy paired promotion with "safe and controllable" development. Chinese laboratories publish safety research and have adopted some frontier-safety practices.

Assessment: China's regime is stringent on content and information control, permissive on development and industrial use, and effective in the sense that it is enforced—the CAC can and does remove non-compliant models. It is the model most likely to be adopted by authoritarian and semi-authoritarian states. Its relevance to frontier-safety concerns is limited: it governs what models say, not what they might do.

## Other jurisdictions

- **United Kingdom**: a "pro-innovation" sectoral approach; no AI statute (a bill has been repeatedly delayed); the AI Security Institute (renamed from Safety in 2025) as the most capable government evaluator of frontier models; copyright reform contested.
- **Japan**: an AI Promotion Act (2025) with soft obligations and a permissive copyright regime; emphasis on the Hiroshima Process and interoperability.
- **South Korea**: the AI Basic Act (passed December 2024, effective January 2026)—the second comprehensive national statute after the EU's, with lighter obligations.
- **Canada**: the AI and Data Act died with the 2025 parliament; sectoral and provincial rules.
- **Brazil**: a comprehensive bill modeled partly on the EU passed the Senate in 2024 and remains in the lower house.
- **India**: no statute; guidelines, advisories, and the IT Rules; an emphasis on development and inclusion.
- **Council of Europe**: the Framework Convention on AI and Human Rights (2024), the first binding international AI treaty, signed by the EU, UK, US (under Biden), and others; general principles rather than specific obligations.

## Cross-cutting mechanisms

### Frontier safety frameworks

The most consequential governance of frontier AI in 2026 is self-governance: the published frameworks under which laboratories evaluate models for dangerous capabilities and commit to safeguards before deployment. Anthropic's Responsible Scaling Policy (2023, revised repeatedly) defines AI Safety Levels with capability thresholds (bio, cyber, autonomous replication, AI R&D) that trigger security and deployment requirements; Anthropic reported reaching ASL-3 with Claude Opus 4 in 2025 and withheld Mythos Preview from general release in 2026 on cyber grounds. OpenAI's Preparedness Framework (2023, revised 2025) rates models on tracked categories; OpenAI classified its 2025 agents as "high" on biological capability and applied safeguards. Google DeepMind's Frontier Safety Framework defines Critical Capability Levels. xAI, Meta, Microsoft, Amazon, and several Chinese laboratories (Zhipu, Alibaba) published frameworks following the Seoul commitments. The Frontier Model Forum coordinates among laboratories.

These frameworks are voluntary, self-assessed, revisable, and uneven, and critics note that laboratories have loosened thresholds under competitive pressure. California's SB 53 and New York's RAISE Act make publishing and following such frameworks a legal obligation; the EU's Code of Practice requires similar content. They are, for now, the de facto standard for frontier governance.

### Evaluations and institutes

A capacity for independent evaluation of frontier models has emerged: the UK AI Security Institute (the best-resourced, with pre-deployment access to major models and the open-source Inspect framework now used by METR and others), the US Center for AI Standards and Innovation, institutes in Japan, Singapore, Korea, Canada, France, and India, and nonprofit evaluators (METR for autonomy; Apollo Research for scheming; SecureBio and others for bio; the Center for AI Safety; Epoch for benchmarks). Cross-laboratory evaluation (the OpenAI–Anthropic pilot of 2025) and third-party red-teaming are becoming norms. The gap is that evaluations measure what they can measure, models are improving faster than evaluations can be built (Chapter 2), and there is no authority to act on evaluation results other than the laboratory itself.

### Standards

NIST's AI Risk Management Framework (2023) and generative-AI profile (2024); ISO/IEC 42001 (AI management systems, 2023) and the 23894 risk-management standard; the EU's harmonized standards under development by CEN-CENELEC (delayed, a reason for the Omnibus); C2PA for content provenance; and emerging standards for agent protocols, model documentation (model cards, system cards), and incident reporting. Standards do the practical work of turning principles into checklists; their development is slow and dominated by industry.

### Liability

Courts are shaping AI governance through ordinary tort, product, and contract law: copyright (Chapter 5); wrongful-death suits against companion and chatbot providers; defamation suits over hallucinated claims; product-liability theories treating models as defective products (a Florida court in 2025 rejected the argument that chatbot output is protected speech, allowing a wrongful-death suit to proceed); employment-discrimination suits over AI screening; and securities suits over AI-related disclosures. The EU's revised Product Liability Directive (2024) explicitly covers software and AI; the separate AI Liability Directive was withdrawn in 2025. Liability is a powerful and under-appreciated governance mechanism because it operates without new statutes and shifts incentives directly; its weakness is that it acts after harm and is slow.

### Compute governance

Because frontier AI requires enormous, physically concentrated, supply-chain-constrained compute, compute is the most monitorable and controllable input. Proposals (Sastry et al., 2024, "Computing Power and the Governance of AI") include: registration and reporting of large training runs (the rescinded Biden order required this above 10²⁶ FLOP; the EU's 10²⁵ threshold triggers GPAI obligations); know-your-customer rules for cloud providers; hardware-enabled mechanisms (on-chip attestation, location verification, usage logging); international compute agreements; and, at the extreme, caps or moratoria. In practice, compute governance in 2026 is almost entirely export control—a geopolitical instrument aimed at China—rather than a safety instrument aimed at frontier development generally. The technical groundwork (chip-level verification research at several institutions; Nvidia's location-verification software in 2025) is advancing, and compute governance is the mechanism most likely to be invoked if a crisis demands rapid constraint on frontier development.

## The central debates

**Safety versus speed.** The 2023–24 framing—that frontier AI posed catastrophic risks requiring precautionary regulation—lost political ground in 2025 to the framing that AI is a race the West must win and that regulation cedes it to China. The vetoing of SB 1047, the rescission of the Biden order, the Paris summit's pivot, the EU's Omnibus, and the preemption push all reflect this shift. Whether it reverses depends on whether a salient incident occurs (Chapter 16) and on the evidence of harm from deployed systems.

**Federal versus state; national versus international.** The US preemption fight and the EU's struggle with member-state implementation are instances of a general problem: AI is global and fast; jurisdictions are local and slow. The Brussels effect and de facto industry standards fill the gap imperfectly.

**Open versus closed.** Whether open-weight models above some capability should be restricted is contested (Chapter 16). The EU's GPAI regime exempts open models from some obligations; the US has moved from considering restrictions (the 2024 NTIA report declined to recommend them) to promoting open models as strategic exports; China's open-weight strategy is state-endorsed.

**Regulating models versus regulating uses.** The EU regulates both; the US sectoral approach regulates uses; frontier frameworks regulate models. The trend is toward a layered system: transparency and safety obligations on frontier developers; use-specific rules in high-stakes domains; liability for harms.

**Who evaluates, and who can act.** Laboratories evaluate themselves; government institutes evaluate with consent; no body can compel a pause. The establishment of an authority with power to require pre-deployment evaluation and to condition deployment on results—an FDA for frontier AI—is the proposal most often made and least likely to be enacted absent a crisis.

## What to expect

| Item | Likely trajectory to 2030 |
|---|---|
| EU AI Act | Implemented with deferred timelines; GPAI regime becomes global baseline; high-risk regime simplified further |
| US federal law | Modest probability (~35%) of a national transparency-plus-preemption statute by 2028; otherwise continued executive/state patchwork |
| State laws | Persist; California and New York frontier laws set de facto national standard unless preempted |
| China | Continued rapid administrative rulemaking; comprehensive law possible but not prioritized; content control tightens as models improve |
| Frontier safety frameworks | Become legally required in more jurisdictions; thresholds contested; incidents test them |
| Evaluation institutes | Grow in capacity; gain pre-deployment access as norm; remain without enforcement power |
| Compute governance | Chip-level verification matures technically; remains export-control-focused unless a crisis |
| Liability | Major verdicts and settlements reshape companion, content, and agent products |
| International | Narrow agreements (nuclear C2, incident reporting, bio); no frontier treaty absent shock |
| Content provenance | C2PA-style standards widely adopted; labeling mandated in EU and China; partial in US |

Governance is, in short, behind the technology and likely to remain so through the decade—closing the gap only in response to visible harms. The mechanisms that exist are meaningful (frontier frameworks, evaluation capacity, transparency laws, liability) but none constrains the central trajectory. The next chapter examines why that matters.
