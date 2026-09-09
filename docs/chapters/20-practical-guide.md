# A Practical Guide: What to Do, for Individuals, Organizations, and Governments

## The principle: robustness across scenarios

The preceding chapters describe a future with wide variance. Advice that depends on one scenario coming true is a bet; advice that helps across most scenarios is a strategy. This chapter tries to give the latter. For each audience it distinguishes actions that are robust (good in nearly every scenario), actions that are hedges (cheap insurance against particular scenarios), and actions to avoid (bets that look attractive in one scenario and fail badly in others). Where the advice is contested, it says so.

A meta-principle first. The single most important thing anyone can do is **use the tools seriously**. Every chapter of this document rests on capabilities that are available to anyone with an internet connection for a few dollars a month or free. Most people—including most executives and policymakers making decisions about AI—have a mental model of the technology formed by a chatbot they tried in 2023. That model is two to three years out of date, which in this field is the difference between a curiosity and a colleague. An hour a week with frontier models and agents, applied to one's actual work, is worth more than any report—including this one.

## For individuals

### Students choosing what to study

**Robust.** Learn to learn; the specific content of most curricula will be outdated, and the capacity to acquire new domains quickly is what remains valuable. Develop deep expertise in *something*—AI complements experts and substitutes for generalists doing routine work (Chapter 12); depth is where judgment lives. Study things that involve the physical world, other people, or high-stakes accountability (medicine, engineering that builds things, skilled trades, care, teaching, leadership), or things that build the capacity to direct and evaluate AI (mathematics, statistics, computer science with an emphasis on systems and judgment rather than syntax, writing as thinking, domain knowledge). Learn to use AI as a tutor, not a substitute: the evidence (Chapter 12) shows the same tool produces large gains or losses depending on how it is used.

**Hedge.** Acquire at least one skill that is physical or relational and hard to automate before 2035; it is insurance against the fast scenarios. Build a portfolio of demonstrated work rather than relying on credentials, whose signaling value is eroding.

**Avoid.** Training narrowly for entry-level cognitive roles that AI now performs—routine coding, paralegal work, junior analysis, content production, translation—without a plan for how to become senior. Assuming a degree is a job. Assuming the trades are permanently safe (they are safe *later*).

**Contested.** Whether to study computer science. The author's view: yes, if one learns how systems work and how to direct them, and no, if one learns to write code by hand as a trade. Demand for people who can build with AI is rising; demand for people who can only do what AI does is falling.

### Workers in exposed occupations

**Robust.** Become the person in your organization who uses AI best—the multiplier is real and visible (Chapter 11). Move toward the parts of your role that involve judgment, relationships, accountability, and context that AI lacks. Document and develop the tacit knowledge that makes you hard to replace. Build financial resilience: the transition may involve gaps.

**Hedge.** Develop a second competence—ideally physical, relational, or in a regulated domain. Maintain networks; most transitions happen through people.

**Avoid.** Waiting for clarity. The evidence of Chapter 11 is that adjustment is happening through hiring, not layoffs—which means the signal comes late for those already employed and the window for repositioning is now.

### Workers in less-exposed occupations

Use AI to handle the paperwork and administration that surround the core work; the productivity gain is real and mostly accrues to you. Watch robotics (Chapter 9) if your work is physical; the 2030s will bring change. Do not assume immunity.

### Everyone

Understand the failure modes: hallucination, sycophancy, injection, and the jagged frontier (Chapter 2). Verify before relying. Protect yourself against AI-enabled fraud (voice cloning is trivial; establish verification protocols with family and colleagues). Be deliberate about AI companionship, especially for children (Chapter 13). Preserve some unaided skills on purpose, as people did with arithmetic. Follow the signposts of Chapter 18; the future will announce itself in METR's numbers and the employment statistics before it arrives in daily life.

## For founders and builders

**Robust.** Build on the assumption that models get better, cheaper, and more agentic on the trend of the last three years—products that are valuable only because current models are limited will be obsolete on release. Build where the model is not the product: proprietary data, workflow integration, distribution, trust, and domain expertise are the moats (Chapter 5). Solve the reliability problem in a specific vertical rather than the capability problem in general—reliability is where the value is (Chapter 8). Design for agents as users, not only humans; the protocols (MCP, A2A, commerce protocols) are the new platform layer.

**Hedge.** Multi-model architectures; do not depend on one laboratory's pricing or policy. Prepare for a financial correction (Chapter 3): raise when possible, extend runway, and do not assume the 2025–26 capital environment persists.

**Avoid.** Thin wrappers; features the laboratories will ship themselves; anything premised on AI staying at its current level; ignoring security (agent deployments without least privilege will produce the incidents of Chapter 8, and liability will follow).

**Contested.** Whether to build for a fast-takeoff world. The author's view: build for the long boom, hedge for the plateau, and do not bet the company on superintelligence arriving on any schedule.

## For executives and organizations

**Robust.** Treat AI as a general-purpose technology requiring organizational redesign, not a tool to bolt on—the 95%-of-pilots-fail finding (Chapter 11) is about organizations, not models. Start with the tasks where verification is cheap and stakes are low; expand as reliability is demonstrated. Invest in data readiness, integration, and the people who will direct agents. Measure actual outcomes, not adoption metrics. Redesign the entry-level pipeline deliberately: if juniors are no longer needed for junior work, decide how you will develop the next generation of seniors, because no one else will (Chapter 12). Adopt security practices for agents from the start—least privilege, approval gates for irreversible actions, logging, sandboxing.

**Hedge.** Scenario-plan for both the plateau and the fast takeoff; the decisions that differ between them (headcount, capital, product) are the ones to make reversibly. Maintain human expertise in critical functions even where AI is cheaper; it is insurance against correlated failure and the basis for oversight.

**Avoid.** Layoffs justified by AI before the AI works (several firms reversed such decisions in 2024–26). Deploying agents with broad credentials. Assuming your industry is immune because it is regulated—regulation slows, it does not stop. Confusing vendor demos with production reliability.

**For boards.** AI is now a fiduciary matter: capability, risk, and workforce transition belong on the agenda with the same seriousness as cybersecurity became after 2015. Ask what would change about the business if the remote-worker standard of AGI were met in 2030, and whether the current strategy survives it.

## For researchers

**In AI.** The highest-leverage open problems (Chapter 19) are continual learning, the RL-generalization question, interpretability at scale, scalable oversight, and evaluation infrastructure. Safety and interpretability remain far less resourced than capability relative to their importance; the marginal researcher does more good there. Preserve chain-of-thought legibility. Publish evaluations honestly, including failures.

**Outside AI.** Every empirical field is being transformed by AI as instrument (Chapter 10); researchers who master the tools will outproduce those who do not, and the transition will be fast. The most valuable contributions from outside AI are domain expertise for building verifiers and environments, rigorous evaluation of AI's claimed effects (much of the current evidence is weak), and the social-science research on labor, cognition, and development that is desperately under-supplied relative to the questions (Chapter 19).

**For funders.** The ratio of capability spending to safety, interpretability, evaluation, and social-impact research is orders of magnitude out of proportion to the stakes. This is the clearest philanthropic and public-research gap of the decade.

## For policymakers

### Robust across scenarios

1. **Build state capacity to understand the technology.** Government evaluation institutes with pre-deployment access (the UK model), technical staff in regulators, and mandatory transparency from frontier developers (the California/New York model) are prerequisites for everything else and are cheap. A government that cannot evaluate frontier models cannot govern them.

2. **Make frontier safety frameworks binding with independent verification.** The laboratories have written the frameworks; require adherence, incident reporting, and third-party audit. This costs the labs little and creates the infrastructure for stronger action if needed.

3. **Harden the physical layer against misuse.** DNA synthesis screening, critical-infrastructure cybersecurity (the Glasswing model of defender-first access should be institutionalized), and hardware-enabled compute verification. These reduce catastrophic-misuse risk regardless of how capability develops.

4. **Prepare the labor-transition infrastructure before the transition.** Modernized unemployment insurance, portable benefits, wage insurance, and retraining are the consensus economist recommendations (Chapter 11); they are inadequate for the fast scenarios but necessary for all of them. Build the data systems (real-time employment tracking by AI exposure, as the Stanford indicators do) so that policy can respond to what is happening rather than to last year's statistics.

5. **Solve the energy and permitting bottleneck.** Whatever one thinks about AI, the grid needs to grow for electrification anyway; interconnection reform, transmission, and firm clean generation serve both. Make datacenters pay their full grid costs and be flexible loads.

6. **Protect children and the vulnerable now.** Companion-chatbot rules, age verification, engagement-optimization limits, and mental-health safeguards (Chapter 13) do not require resolving any debate about AGI and address harms occurring today.

7. **Content provenance.** Mandate or strongly incentivize C2PA-style provenance for public-facing generated content and for platforms; it is the only scalable answer to the evidentiary crisis.

8. **Fund the public goods AI erodes.** Independent journalism, open knowledge (Wikipedia and its kin), and public data are being consumed by the models that undermine their business models; treat them as infrastructure.

### Hedges for the fast scenarios

9. **Design broad-based distribution mechanisms before they are needed**—sovereign or public wealth funds with stakes in AI firms, equal capital–labor taxation, and the administrative capacity for universal transfers. These are politically hard in calm times and badly designed in crises; do the design now, activate later.

10. **Develop the international coordination infrastructure now**: incident reporting, compute verification research, scientist-to-scientist channels with China, and agreed red lines (nuclear command and control is the one that exists; bio and critical infrastructure are the obvious next). Crisis-time coordination requires peacetime plumbing.

11. **Create a decision point.** Establish, in law, the conditions under which frontier development would be paused or nationalized and who decides—so that the decision, if it comes, is made by an accountable body under pre-agreed rules rather than by a CEO or in panic.

### Avoid

- Regulating the technology of 2023 (the EU's original high-risk regime) rather than the technology of 2026–30 (frontier agents).
- Preempting state laws without replacing them with anything—the US risk in 2026.
- Treating AI safety and AI competitiveness as opposites; the countries that can verify what their models do will be the ones others trust to deploy them.
- Assuming the plateau. Policy that is only right if progress stalls is a bet against the trend.
- Assuming the fast takeoff. Policy that shuts down development in anticipation of catastrophe cedes the frontier to actors who will not.

### On the central tension

Policymakers face a genuine dilemma that this document cannot resolve: the safety case says slow down and coordinate; the competition case says speed up and win; and both are right about something. The author's judgment is that the two are less opposed than the discourse suggests—capacity to evaluate, verify, and control frontier systems is a *competitive* advantage (it is what allows a country to deploy AI in defense, infrastructure, and government with confidence), and the measures listed as robust above are ones that the competitive framing should endorse. The genuine trade-off arises only at the frontier of frontier development—whether to build the next system before its predecessor is understood—and that is the decision for which item 11 exists.

## For everyone: a closing note on posture

The two failure modes of thinking about AI are denial and fatalism. Denial says the technology is hype and nothing needs to change; the evidence of the first ten chapters refutes it. Fatalism says the technology is destiny and nothing can be done; the evidence of the last eight chapters refutes it—the variance between good and bad futures is dominated by human choices about design, deployment, distribution, and governance that are being made now and are still open. The appropriate posture is the one this document has tried to model: take the technology seriously, take the uncertainty seriously, watch the signposts, and act on what is robust.
