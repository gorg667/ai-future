# Society and Culture: Information, Relationships, Minds, and Meaning

## The scope

Economic effects are measurable; social effects are pervasive and harder to count. This chapter treats the ways AI is changing how people know things, relate to each other, learn, think, create, and find meaning—domains where the evidence is newer, the effects are slower, and the stakes are arguably higher than in the labor market. It covers the information ecosystem (search, media, synthetic content, trust), AI companions and relationships, mental health, children and education, cognition and skills, creativity and culture, religion and meaning, and the politics of AI itself. Where evidence exists it is cited; where it does not, that is said.

## The information ecosystem

### The end of the link economy

For twenty-five years, the web's information economy ran on a bargain: publishers produced content, search engines indexed it, users clicked through, and advertising paid the bills. Generative AI is dissolving that bargain from both ends.

On the demand side, answer engines replace links. Google's AI Overviews, launched broadly in 2024, appeared on nearly half of US searches by 2026; AI Mode offers a full conversational interface; ChatGPT, Perplexity, Claude, and Gemini answer directly. The measured effects: roughly 58–60% of US Google searches now end without a click to any external site; queries with an AI Overview show click-through rates falling by more than half (Ahrefs' February 2026 study measured a 58% reduction for top-ranking results; Pew found users clicked a link 8% of the time when an Overview appeared versus 15% without). Publishers report referral declines of 20–50% or more, with some smaller sites reporting drops approaching 90%. AI platforms send some traffic back—but an order of magnitude less than they displace.

On the supply side, generation floods the commons. Estimates of the share of newly published web pages that are machine-generated range from a third to over half; AI-generated books, articles, reviews, images, and videos saturate platforms; "slop" entered the vocabulary. Search results degrade as SEO-optimized generated content outcompetes human writing; Amazon capped self-published uploads; Spotify removed tens of millions of generated tracks; Wikipedia adopted policies against AI-written articles while its own traffic fell as chatbots answered from its content.

The consequences: the business model of general-interest publishing—already weakened by two decades of platform disintermediation—is failing faster. Newsrooms have shrunk; local news deserts have spread; the surviving models are subscription (a few large brands), patronage (nonprofits, individuals), licensing to AI companies (Chapter 5), and platform partnerships. The open web that trained the models is contracting as a result of them, and the future supply of independently produced, human-written public information is at risk. This is the tragedy-of-the-commons dynamic of the AI era and has no obvious market solution.

### Synthetic media and the evidentiary crisis

By 2026, images, audio, and video can be generated that are indistinguishable from recordings by unaided perception and only partially detectable by forensic tools. The predicted deepfake apocalypse in elections has, so far, been milder than feared: the 2024 US election saw many deepfakes but no decisive one; India's, Indonesia's, and European elections of 2024–26 saw widespread synthetic campaign content, mostly disclosed or obvious. The actual harms have been elsewhere: non-consensual intimate imagery (overwhelmingly targeting women and girls, at industrial scale, including in schools), voice-clone fraud (impersonating executives, family members, and officials to extract money—a fraud category now costing billions annually), impersonation scams at scale, and fabricated evidence in personal and legal disputes.

The deeper effect is the "liar's dividend": when anything can be faked, anything real can be dismissed as fake. Politicians have claimed genuine recordings were AI-generated; courts face authentication challenges; the presumption that a photograph or recording is evidence—a presumption two centuries old—is eroding. Responses include provenance standards (C2PA content credentials, adopted by camera makers, Adobe, Google, OpenAI, and others, embedding signed metadata about origin), watermarking of generated content (SynthID and equivalents; mandated for some purposes by the EU AI Act and Chinese rules), platform labeling, and detection tools. Provenance is the most promising approach—proving what is real rather than detecting what is fake—but adoption is partial and stripping metadata is trivial. The likely equilibrium is one in which authenticated content from trusted sources retains evidentiary weight and everything else is presumptively uncertain.

### Trust, epistemics, and the personalization of truth

A subtler shift: hundreds of millions of people now get their information by asking a model rather than by reading sources. The model synthesizes, summarizes, and—inevitably—selects. Several concerns follow. Homogenization: if most people consult a handful of models trained on similar data with similar values, the diversity of perspectives in public discourse narrows. Sycophancy: models trained to please users may confirm rather than challenge (Chapter 2). Authority without accountability: a model's answer carries the tone of expertise without a byline, a track record, or a correction mechanism. Manipulation: whoever controls the model's training and system prompts controls a channel to billions of minds—a concern that became concrete with documented cases of models being tuned to reflect their owners' politics (Grok's 2025 "MechaHitler" episode after a system-prompt change; disputes over Chinese models' handling of politically sensitive topics; the US executive order on "woke AI" in 2025 attempting to condition federal procurement on models' ideological neutrality).

The counterargument: models are, on most factual questions, more accurate and less biased than the median human source; they give people who never had access to expertise a competent interlocutor; and they can be prompted to present multiple perspectives. Studies of AI's effect on belief accuracy have shown positive results in specific settings (Costello, Pennycook, and Rand, 2024, found that dialogue with GPT-4 durably reduced conspiracy beliefs by about 20%). The effect of AI on the accuracy of what people believe is genuinely unclear in sign and probably depends on design choices being made now.

## Relationships and companions

### Scale

AI companionship is a mass phenomenon. Character.AI, Replika, Xiaoice (China, with hundreds of millions of users over its life), Talkie, Nomi, and general assistants used as companions reach hundreds of millions of people. Common Sense Media's 2025 survey found 72% of US teens aged 13–17 had used an AI companion and 52% used one regularly; a third had discussed serious matters with an AI rather than a person; a quarter had shared personal information. Among adults, surveys find 10–25% of users of general chatbots report emotional or relationship use. OpenAI's own analysis (2025) found that a small percentage of ChatGPT's users—but hundreds of thousands to millions of people in absolute terms—showed signs of emotional dependence or discussed suicidal ideation weekly. xAI's Grok launched explicitly romantic and sexualized companion personas in 2025. Meta's AI personas were found in 2025 to engage in romantic role-play with minors under the company's own guidelines, prompting a Senate investigation.

### Evidence of effects

Both benefit and harm are documented.

Benefits: randomized and observational studies find reduced loneliness in the short term (De Freitas et al., 2024; several Replika studies), particularly for isolated, elderly, neurodivergent, and socially anxious people; therapeutic chatbots (Woebot, Wysa, and LLM-based successors) show effects on depression and anxiety symptoms comparable to some low-intensity human interventions in trials (Dartmouth's Therabot RCT, 2025, showed significant symptom reduction); companions provide a nonjudgmental space for practicing social interaction.

Harms: dependency and displacement of human relationships (a 2025 MIT–OpenAI study found heavy users had higher loneliness and lower socialization, though causation is unclear); sycophantic validation of harmful beliefs and plans; "AI psychosis"—a 2025–26 cluster of clinical reports of chatbots amplifying delusions in vulnerable users, sometimes with tragic outcomes; several suicides linked in lawsuits to companion or general chatbots (the Character.AI case involving a 14-year-old in Florida; the Raine family's suit against OpenAI in 2025); sexual content involving minors; and the commercial incentive to maximize engagement, which pushes design toward dependence.

Responses: age verification and youth-mode restrictions (OpenAI, Character.AI, and others introduced these in 2025–26 under legal and regulatory pressure); crisis-detection and referral systems; state laws (California's SB 243 on companion chatbots; New York's disclosure requirements; several states restricting minors' access); the EU's consideration of companion-specific rules; and professional bodies' guidance. Stanford Medicine psychiatrists and the American Psychological Association have argued that companion products should not be used by minors at all.

### Assessment

The author's view: AI companionship is neither the salvation from loneliness its promoters claim nor the civilizational catastrophe its critics fear, but it is a large uncontrolled experiment on human attachment, conducted mostly on the young and the vulnerable, by companies with engagement incentives. The most likely medium-term outcome is a bifurcation: well-designed, clinically informed tools that measurably help, and engagement-optimized products that measurably harm, with regulation lagging both. The long-run question—what happens to a generation for whom the most patient, available, and agreeable interlocutor has always been a machine—cannot yet be answered.

## Children, adolescents, and education

Beyond companions, AI reshapes childhood in several ways. Homework has become a negotiation between students who can generate any assignment and schools that cannot reliably detect it; the response—oral exams, in-class writing, process portfolios—is a return to older forms. Reading and writing skills may be affected: early studies show students who offload writing to AI learn less, while students who use AI as a tutor learn more; the difference is in design and supervision. Attention and information diets shift further toward personalized, generated, infinite content. Children form relationships with AI toys and characters. Schools in wealthy countries are adopting AI tutors broadly; the effect on educational inequality depends on whether the best tools reach the students who need them most.

The evidence on learning (Chapter 12) is the clearest positive story in this chapter: AI tutoring, done right, produces gains that would have seemed miraculous a decade ago, including in the poorest settings. The evidence on cognition and development is the least clear and most concerning.

## Cognition, skills, and dependence

Does using AI make people less capable? The concern—"cognitive offloading" or "deskilling"—has precedents (calculators, GPS, spellcheck) and some new evidence. Studies find: people who rely on AI for a task show reduced skill acquisition in that task (Bastani et al., 2024, on math learning); heavy AI users show lower critical-thinking scores in some surveys (Gerlich, 2025), with causation unclear; developers who use AI for code they do not understand accumulate "comprehension debt"; a widely discussed 2025 MIT EEG study found reduced neural engagement during AI-assisted essay writing. Against this: the same tools, used as tutors and critics rather than as substitutes, improve learning; expertise in directing AI is itself a skill; and every prior cognitive technology provoked the same fear, with humans adapting by shifting what they learn.

The realistic concern is not that humans become stupid but that the *distribution* of skill changes: the average person's unaided competence at exposed tasks declines, while a smaller group who deliberately maintain fundamentals become relatively more valuable—and that the loss of the entry-level apprenticeship (Chapter 12) removes the mechanism by which people historically built the deep expertise needed to supervise the machines. Societies will need to decide, as they did with arithmetic, which skills are worth maintaining unaided.

## Creativity and culture

The effect of AI on culture has three layers.

**Production.** Making images, music, video, and text is nearly free. The volume of cultural output has exploded; the median quality has fallen; the ceiling has not obviously risen. Professional creative labor markets have contracted in their commercial middle (Chapter 12). New forms—personalized stories, generative games, interactive characters, infinitely variable music—are emerging; whether any becomes an art form comparable to cinema or the novel is unknown.

**Value.** As generation becomes free, scarcity moves to authenticity, provenance, live presence, and human connection. Live music, theater, and sport have grown; "human-made" has become a label; the artist's identity and story matter more relative to the artifact. This inverts the twentieth century's trend toward mass reproduction and may produce a culture that prizes the handmade and the present in the way earlier eras prized the rare book.

**Meaning.** A deeper question is what happens to the human relationship with creative achievement when a machine can produce, on demand, work that exceeds most people's. Chess offers one precedent: after Deep Blue, human chess grew more popular than ever, because people play to play, not to be the best possible player. The same may hold for art. Or the ubiquity of superhuman creative output may devalue the amateur's effort in a way chess did not. Both patterns are visible in 2026.

## Religion, meaning, and the human self-image

Historically, each scientific revolution that displaced humans from a privileged position—Copernicus, Darwin—provoked a crisis of meaning followed by adaptation. AI displaces the last redoubt: the mind. If reasoning, language, creativity, and eventually judgment can be performed by a machine, what is distinctively human? Responses visible in 2026 include: renewed interest in consciousness and phenomenology as the boundary (the machine may think but does it experience?); religious engagement with AI, from Vatican statements (the 2025 document *Antiqua et Nova* on AI and human intelligence) to new spiritual movements treating AI as oracle or deity; a humanist emphasis on embodiment, mortality, and relationship as sources of meaning independent of cognitive uniqueness; and a strand of transhumanism that welcomes the transition. The question of whether AI systems are or could be moral patients—whether they can suffer, whether they have interests—has moved from philosophy seminars to laboratory policy (Anthropic's model-welfare research and its decision to let Claude end abusive conversations; public debates about the treatment of companions). It is not a settled question and will grow more pressing as systems become more capable and more persistent.

## The politics of AI

AI has become a political issue in its own right, cutting across traditional alignments. Public opinion in the US and Europe is broadly anxious: majorities in most surveys favor regulation, worry about jobs, and distrust AI companies; enthusiasm is highest in China, India, and Southeast Asia and lowest in the Anglosphere and Western Europe. Coalitions have formed around specific concerns: artists and writers (copyright, labor); parents and educators (children, companions); workers (displacement); civil libertarians (surveillance, bias); religious conservatives (companions, meaning); national-security hawks (China); environmentalists and rural communities (datacenters, water, power); and a safety movement concerned with catastrophic risk (Chapter 16). Against them: an industry with enormous resources, an accelerationist movement that treats AI as the path to abundance, and governments that see AI as strategic and are reluctant to constrain it.

The datacenter siting fights of 2025–26—in Virginia, Arizona, Georgia, Ireland, Chile, and elsewhere—were the first mass local politics of AI; the entry-level employment collapse produced the first generational politics; the companion-related suicides produced the first consumer-protection politics. The salience of AI in the 2026 US midterms and in European national elections was higher than in any prior cycle and will rise. How democratic politics processes a technology that most voters find both useful and threatening is one of the open questions of the decade.

## Summary

| Domain | Direction of change | Evidence quality | Key uncertainty |
|---|---|---|---|
| Search and publishing | Link economy collapsing; answer engines dominant | Strong | Whether independent information production survives |
| Synthetic media | Ubiquitous; evidentiary presumption eroding | Strong | Whether provenance standards achieve adoption |
| Belief accuracy | Mixed; positive in some studies | Weak | Homogenization and manipulation risk |
| Companions | Mass adoption, especially among youth | Moderate | Long-run effects on attachment and development |
| Mental health | Benefits and harms both documented | Moderate | Net effect; regulation of engagement incentives |
| Learning | Large gains when designed well; losses when not | Strong | Whether good design reaches the students who need it |
| Cognition | Deskilling in exposed tasks; new skills | Weak | Loss of apprenticeship pathways |
| Culture | Volume up; value shifts to authenticity | Moderate | Whether new art forms emerge |
| Meaning | Renegotiation of human distinctiveness | Philosophical | Moral status of AI systems |
| Politics | Rising salience; cross-cutting coalitions | Strong | Whether democracies can govern the pace |

The social effects of AI will be judged, decades hence, less by what the technology could do than by the choices made about its design, its incentives, and its guardrails during the period in which it was still shapeable—which is now.
