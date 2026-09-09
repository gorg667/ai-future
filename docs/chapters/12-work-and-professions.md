# Work and Professions: A Sector-by-Sector Assessment

## How to read this chapter

Chapter 11 treated labor in aggregate. This chapter goes occupation by occupation, because the aggregate hides everything that matters to an individual deciding what to study, a firm deciding how to organize, or a policymaker deciding whom to help. For each sector it asks: what does AI do now, what is the evidence of effect, what is the plausible trajectory to 2030 and beyond, and what remains human. The assessments synthesize the deployment evidence, the capability trends of Chapters 2 and 8, and the physical-world constraints of Chapter 9.

A framework used throughout: tasks differ along three dimensions that determine exposure. **Digital vs. physical** (AI does digital tasks first). **Verifiable vs. judgment-based** (AI does verifiable tasks better and more reliably). **Low-stakes vs. high-stakes** (low-stakes tasks are delegated sooner because errors are tolerable). An occupation whose core tasks are digital, verifiable, and low-stakes—translation, tier-one customer support, routine code—is most exposed. One whose tasks are physical, judgment-based, and high-stakes—surgery, elder care, skilled trades in unpredictable environments—is least exposed, for now.

## Software engineering

**Now.** The most transformed profession. A large majority of developers use AI daily; at major technology companies, agents write a substantial share of new code (figures of 30–50% are cited), which humans review. Autonomous coding agents (Claude Code, Codex, Cursor, Devin, Jules) complete multi-hour tasks. Non-programmers build working applications through natural language. SWE-bench Verified exceeds 90%; METR's time horizon on software tasks passed sixteen hours.

**Evidence.** Task studies show 25–55% speedups on well-defined work; the METR randomized trial showed slowdowns for experts on familiar complex codebases with early-2025 tools, reversed with later ones. Job postings for developers fell about a third from the 2022 peak; hiring of new computer-science graduates collapsed relative to trend (the "Canaries" study's most exposed group); demand for senior engineers who can specify, review, and architect remained strong; total developer employment has been roughly flat while output per developer rose sharply.

**Trajectory.** By 2028, most code is written by agents; the developer's job is specification, architecture, review, and system-level judgment. Team sizes shrink; the productivity of small teams rises enormously; the number of software products explodes as the cost of building falls. The entry-level route via "write code for two years" disappears and is not obviously replaced. By 2030, the distinction between "developer" and "person who directs agents to build software" blurs. Demand for software does not appear to be saturating—cheaper software creates demand for more software (the Jevons pattern)—which is the strongest argument that developer employment holds up better than naïve substitution implies.

**What remains human.** Deciding what to build, understanding users, navigating organizational politics, judging trade-offs, taking responsibility for consequences.

## Customer service and support

**Now.** The largest enterprise deployment of agents. Voice and chat agents resolve a majority of tier-one contacts at companies that have deployed them (Klarna's 2024 claim that its AI did the work of 700 agents—later partly walked back as it rehired humans for quality—and deployments by Sierra, Decagon, Intercom Fin, Salesforce Agentforce, and incumbents). Humans handle escalations and complex cases, often AI-assisted.

**Evidence.** Brynjolfsson et al.'s study showed +14% productivity for humans with AI assistance; full automation of simple contacts is now routine. Call-center employment is falling; the Philippines and India, whose business-process-outsourcing sectors employ millions, face structural pressure. Customer service is among the occupations with the steepest young-worker declines in the Canaries data.

**Trajectory.** By 2028, tier-one support is overwhelmingly automated; human roles concentrate in complex, emotional, high-value, and regulated interactions. Total employment falls substantially (author's estimate: 30–50% in advanced economies by 2030, more in outsourcing hubs). Quality is mixed: automated agents beat bad human service and lose to good human service, and firms differ in which they replace.

## Writing, content, translation, and marketing

**Now.** Generative AI produces marketing copy, product descriptions, SEO content, first drafts, summaries, and translations at near-zero cost and adequate-to-good quality. Translation between major languages is at professional quality for most content; interpretation is real-time. A large share of new web content is machine-generated.

**Evidence.** Freelance markets show declining postings and rates for writing and translation since 2023 (Hui, Reshef, and Zhou, 2024, found writing-related freelance jobs down about 30% after ChatGPT, with earnings falling). Translation employment is falling and shifting toward post-editing and high-stakes (legal, literary, diplomatic) work. Marketing teams are smaller and produce more. Journalism's contraction predates AI; AI accelerates the collapse of the traffic-based business model (Chapter 13).

**Trajectory.** Routine commercial writing and translation are largely automated by 2028. What survives: writing where the author's identity, judgment, or relationship is the product; translation where liability or nuance is critical. The market bifurcates into cheap generated volume and premium human-signed work.

## Law

**Now.** AI performs document review, due diligence, contract analysis and drafting, legal research, and first-draft memos at levels competitive with junior associates (Harvey, CoCounsel, Lexis+ AI, Westlaw AI, firm-internal tools). Frontier models pass the bar exam in top percentiles. Hallucinated citations have led to sanctions against lawyers in hundreds of documented incidents, which has enforced a verification norm.

**Evidence.** Large firms report substantial savings on research and review; the billable-hour model is under pressure as clients refuse associate rates for AI-assisted work. Associate hiring at large firms has softened; paralegal and legal-assistant postings have fallen. Access to justice may improve as legal help becomes cheap for individuals and small businesses.

**Trajectory.** By 2028, the junior-associate function is largely AI-performed under partner supervision; firms restructure around fewer, more senior lawyers and AI leverage; pricing shifts to value. Litigation strategy, negotiation, client counseling, courtroom advocacy, and professional liability remain human—partly by regulation (unauthorized-practice rules), partly by nature. The number of lawyers declines slowly; the number of legal tasks performed rises sharply.

## Medicine and healthcare

**Now.** AI matches or exceeds specialists on diagnostic benchmarks in radiology, dermatology, pathology, and ophthalmology; it passes licensing exams at top percentiles; ambient documentation (Abridge, Nuance DAX, Ambience) that listens to visits and writes notes is the most widely adopted clinical AI, used by hundreds of thousands of clinicians; clinical reference tools (OpenEvidence, used by a majority of US physicians by some counts) answer questions with citations; triage, scheduling, coding, and prior-authorization tools are pervasive administratively. Drug discovery is covered in Chapter 10.

**Evidence.** Documentation AI measurably reduces burnout and after-hours charting. Diagnostic AI in screening (mammography in Scandinavia and the UK; diabetic retinopathy; lung nodules) improves detection and reduces workload in trials. But randomized trials of AI-assisted diagnosis by physicians show smaller-than-expected gains—in some, the AI alone outperformed physician-plus-AI because physicians overrode correct suggestions. Deployment lags capability because of regulation (FDA clearance is device-by-device), liability, reimbursement, workflow integration, and professional resistance.

**Trajectory.** Administrative and documentation work is largely automated by 2028—the single largest efficiency gain available, since administration is roughly a quarter of US health spending. Diagnostic AI becomes standard of care in imaging and pathology, with radiologists supervising rather than reading every study. By 2030, most patients in wealthy countries interact with an AI clinician for triage and routine questions before a human. Nursing, physical care, procedures, and the relational core remain human and in shortage; robotics does not solve care labor before the 2030s. Healthcare *employment* may not fall—demand is enormous and unmet—but its composition shifts toward care and away from paperwork.

**Regulatory note.** Medicine is where the gap between what AI *can* do and what it is *allowed* to do is widest, and most defensibly so. The pace is set by regulators and liability regimes, not by model capability.

## Finance and accounting

**Now.** Bookkeeping, reconciliation, invoice processing, tax preparation, audit sampling, financial analysis, report generation, compliance monitoring, fraud detection, and customer service are heavily AI-assisted or automated. Investment research (summarizing filings, calls, news) is transformed; quantitative trading has used machine learning for decades.

**Evidence.** Big Four firms have cut graduate hiring and restructured around AI; bookkeeping employment is falling; the CPA pipeline was already shrinking. Banks report large efficiency gains in operations and compliance and have slowed headcount growth. Junior analyst roles are contracting.

**Trajectory.** By 2028, routine accounting, audit, and analysis are largely automated; the professions consolidate toward judgment, advisory, and liability-bearing roles (the audit signature; the fiduciary relationship). Finance is high-verifiability and high-digitization, so exposure is high; it is also heavily regulated, which preserves roles regulation requires.

## Education

**Now.** Students use AI universally—for explanation, tutoring, and, extensively, for doing assignments. Teachers use it for planning, grading, feedback, and differentiation. AI tutors (Khanmigo, Google's LearnLM tools, Duolingo, many others) deliver personalized instruction at scale. Assessment is in crisis: take-home written work no longer reflects student capability; institutions have shifted to in-class, oral, and project-based assessment.

**Evidence.** Well-designed AI tutoring shows large gains (a 2024–25 Harvard study found students learned more than twice as much in less time with an AI tutor than in an active-learning classroom; World Bank pilots in Nigeria showed gains equivalent to roughly two years of typical schooling in six weeks). Unrestricted use to avoid effort shows *negative* effects (a 2024 Wharton study found students using unrestricted ChatGPT for practice did worse on exams). Tool design determines the outcome.

**Trajectory.** Personalized AI tutoring becomes universal in wealthy countries by 2028 and spreads where devices exist—the most consequential positive application for the Global South. Teachers shift toward motivation, socialization, mentorship, and oversight; teacher employment does not fall (class sizes and schooling's custodial function are not AI-solvable). Higher education faces a deeper crisis: the credential's signaling value erodes, the entry-level jobs degrees led to are contracting, and the cost structure is unsustainable. Expect consolidation and a shift toward experiential and verified learning.

## Creative industries

**Now.** Image, video, music, and voice generation are at commercial quality (Chapter 9). Concept art, storyboards, stock imagery, background music, voice-over, and commercial illustration are being generated rather than commissioned. Hollywood's 2023 strikes secured contractual limits on AI for writers and actors; video-game voice actors struck in 2024–25. Artists' lawsuits against training companies have produced partial licensing settlements.

**Evidence.** Freelance illustration and stock photography have contracted sharply; commercial voice-acting has fallen; music licensing is shifting toward generated tracks. Top-tier creative work—where the creator's identity is the product—is less affected and in some cases more valuable as a mark of authenticity. Production costs are falling, which may expand output.

**Trajectory.** The bottom and middle of the commercial creative market is largely automated by 2028; the premium on human authorship, live performance, and authenticity rises; new creative forms (interactive, personalized, generative) emerge; fewer people earn a living from traditional creative work while more people create. Copyright law (Chapter 5) and labor agreements set the terms.

## Management, consulting, and analysis

**Now.** Research, slides, data analysis, memo drafting, meeting summaries, and project tracking are heavily AI-assisted. Consulting firms have adopted aggressively while facing pressure on the leverage model. The BCG "jagged frontier" study showed consultants 40% better on tasks within AI's competence and worse outside it.

**Trajectory.** Middle-management layers that primarily aggregate, report, and coordinate are thinned; spans of control widen; firms flatten. Consulting shifts toward implementation, judgment, and accountability; the pyramid becomes a column. Strategy, stakeholder management, and accountability remain human. "Manager of agents" becomes a common role.

## Skilled trades and physical work

**Now.** Electricians, plumbers, carpenters, HVAC technicians, mechanics, welders, and construction workers are largely unaffected in core tasks. AI helps with diagnosis (photo-based fault identification), scheduling, quoting, and paperwork. Construction robotics is limited to specific tasks in early deployment.

**Evidence.** Demand and wages for the trades have risen, partly from datacenter and infrastructure construction—AI is a net creator of trades jobs near-term. Training pipelines are strained.

**Trajectory.** The trades are the least exposed major group through 2030 and among the best-paid relative to training cost. Beyond 2030, general-purpose robotics (Chapter 9) begins to affect structured physical work (factory, warehouse) and later unstructured work (construction, repair); trades in unpredictable environments are the last redoubt. A young person choosing a career in 2026 with a 20-year horizon should note that "unexposed" means "later," not "never."

## Transportation and logistics

**Now.** Robotaxis operate at scale in a dozen-plus cities; driverless trucking runs commercially on Texas corridors; warehouse automation is mature; delivery drones operate in limited areas. Roughly 5 million Americans drive for a living.

**Trajectory.** Highway trucking begins losing drivers to autonomy in the late 2020s, with a long tail (first/last mile, local delivery, adverse conditions); ride-hail drivers face falling demand in robotaxi cities over 2027–2032; warehouse labor shifts from picking to supervising. This is the largest physical-world displacement of the 2030s and disproportionately affects men without degrees.

## Agriculture, manufacturing, and energy

Agriculture is already highly mechanized; AI adds precision (weeding, spraying, harvesting robots, yield prediction) and mostly affects remaining manual harvest labor over the 2030s. Manufacturing has used industrial robots for decades; foundation-model perception and VLA policies make robots flexible enough for high-mix, low-volume work, expanding automation into small factories over 2028–2035. Energy sees AI in grid management, exploration, and operations, and is a net job creator through the buildout.

## Government and public sector

Adoption is slow, procurement is hard, the workforce is older; but potential is large (casework, benefits processing, permitting, tax administration, translation). Some governments (Singapore, Estonia, the UAE, the UK incrementally, the US federal push of 2025–26) move faster. The public sector will be a late adopter whose eventual transformation is large and where job-loss politics are most sensitive.

## Care work

Childcare, elder care, disability support, nursing, and social work are physical, relational, high-stakes, and in chronic shortage. AI assists with documentation, monitoring, and companionship (Chapter 13) but does not replace the core. These are among the fastest-growing occupations in every aging society, among the least exposed through the 2030s—and among the lowest paid, a policy problem AI does not solve and may sharpen as other work is automated.

## Cross-cutting patterns

1. **The entry-level problem is universal.** In every cognitive profession, AI does what juniors did, and firms hire fewer juniors. The professions have not solved how to train the next generation of seniors. This is the most important labor-market issue of the late 2020s and is under-discussed relative to headline unemployment.
2. **Regulation sets the pace in high-stakes fields.** Medicine, law, finance, and aviation change at the speed of their regulators, not their models.
3. **The premium shifts to judgment, accountability, and relationships.** What humans retain is deciding, being responsible, and dealing with other humans.
4. **Physical work is later, not immune.** The 2030s are for manual work what the late 2020s are for cognitive work.
5. **Occupation counts mislead.** Most occupations will not disappear; most will shrink, restructure, or change content. Displacement happens task by task and shows in hiring long before unemployment.
6. **Demand elasticity matters.** Where demand for output is elastic (software, legal help, medical advice, education), cheaper production expands consumption and cushions employment. Where inelastic (customer support, translation of fixed content), cost savings become fewer workers.

## Exposure summary

| Occupation group | Exposure to 2030 | Primary mechanism | Likely employment trend | What remains human |
|---|---|---|---|---|
| Software engineering | Very high | Agents write code | Flat to declining; restructured | Specification, architecture, judgment |
| Customer service | Very high | Agents handle contacts | Large decline | Complex, emotional, regulated cases |
| Writing / translation / marketing | Very high | Near-zero-cost generation | Large decline in routine; bifurcation | Identity, voice, high-stakes nuance |
| Law | High | Research, review, drafting | Slow decline; restructured | Strategy, advocacy, counseling, liability |
| Finance / accounting | High | Analysis, reconciliation, audit | Decline in routine roles | Judgment, advisory, fiduciary duty |
| Medicine (clinical) | Moderate | Diagnosis, documentation | Stable to growing; restructured | Care, procedures, relationships, responsibility |
| Education | Moderate | Tutoring, grading, planning | Stable; changed | Motivation, socialization, oversight |
| Creative | High (commercial) / Low (top tier) | Generation | Decline in commercial; premium on authenticity | Authorship, performance, identity |
| Management / consulting | Moderate-high | Analysis, coordination | Thinning of middle layers | Strategy, accountability, people |
| Skilled trades | Low | Diagnosis, paperwork | Growing to 2030; robotics after | Unstructured physical work |
| Transportation | Moderate, rising | Autonomy | Decline begins late 2020s | Edge cases; local delivery (for now) |
| Manufacturing / warehouse | Moderate, rising | Flexible robots | Decline in manual roles | Supervision, maintenance |
| Care work | Low | Assistance only | Growing | Nearly everything |
| Government | Low now, high potential | Casework, processing | Slow change | Discretion, accountability |
