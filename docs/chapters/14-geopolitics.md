# Geopolitics: The US–China Race, Sovereign AI, Chips, and War

## AI as a strategic technology

By 2026 every major government treats artificial intelligence as a determinant of national power comparable to nuclear energy in the 1950s or the internet in the 1990s—and unlike either, one whose frontier is held by private companies. The competition has several arenas: frontier capability, compute and its supply chain, energy, talent, data, standards and diffusion, and military application. This chapter treats the US–China rivalry that organizes the field, the "sovereign AI" movement among everyone else, the export-control regime and its effects, the militarization of AI, and the prospects for international coordination. The conclusion: **the US leads at the frontier by months, not years; China leads in diffusion, open weights, and industrial application; the gap is narrower than either side's rhetoric suggests; and the competition is shifting from models to the physical and institutional infrastructure around them.**

## The United States

### Assets

The US holds the frontier: five of the world's most capable laboratories (OpenAI, Anthropic, Google DeepMind, xAI, Meta), the dominant accelerator designer (Nvidia) and its software ecosystem, the hyperscalers whose capital expenditure exceeds most countries' defense budgets, the deepest capital markets, the largest share of top AI researchers (though a large fraction are foreign-born, and roughly half of top US AI researchers did undergraduate work abroad, many in China), and the alliance network that controls the chip supply chain (Taiwan's fabs, the Netherlands' lithography, Japan's materials, Korea's memory).

### Strategy

US policy shifted between administrations more in tone than substance. The Biden administration's approach—the 2023 executive order on safe AI, export controls tightened in 2022, 2023, and 2024, the CHIPS Act's $52 billion in fab subsidies, the AI Safety Institute, the "AI diffusion rule" tiering countries' access to chips—emphasized safety guardrails and control of diffusion. The Trump administration from 2025 rescinded the Biden order, issued its own AI Action Plan (July 2025) emphasizing acceleration, deregulation, energy buildout, and export of the "American AI stack," rescinded the diffusion rule in favor of bilateral deals, renamed the safety institute the Center for AI Standards and Innovation, issued an executive order in December 2025 asserting federal preemption of state AI laws and creating a litigation task force to challenge them, and in March 2026 proposed a National Policy Framework seeking uniform federal standards. On China, the through-line was consistent: maintain export controls on the most advanced chips and equipment while debating, and repeatedly revising, the treatment of mid-tier chips (the H20 saga of 2025; the B30A debate of 2026).

The strategic bet is that the US wins by building the most capability fastest and diffusing it through allied and neutral countries before China does—"winning the AI race." Its critics argue it neglects safety, concentrates power in a few firms, and that export controls have accelerated China's domestic industry.

### Vulnerabilities

Dependence on Taiwan for leading-edge fabrication is the single largest vulnerability in the US position and in the entire trajectory described in this document. Power-grid constraints, permitting, and a shrinking pipeline of foreign talent (visa restrictions, an increasingly hostile climate for Chinese researchers) are secondary. The financial fragility of the investment boom (Chapter 3) is a third.

## China

### Assets

China has the second-largest concentration of AI talent and produces more AI researchers than any country (by some measures nearly half of the world's top-tier AI researchers did undergraduate work in China); a large and fast-moving laboratory ecosystem (DeepSeek, Alibaba's Qwen, Moonshot, Zhipu, MiniMax, ByteDance Seed, Tencent, Baidu, Huawei, Xiaohongshu—whose dots-note-3.0 was among the first systems to score a perfect 42/42 at the July 2026 IMO in Shanghai—and dozens more); the world's most complete manufacturing base and the largest deployment of industrial robots; a state that can direct capital, energy, and land at scale (China added more electricity generation in 2024–25 than the entire US grid's growth in a decade); an enormous domestic market and data; and a policy apparatus that has made AI a national priority since 2017 (the New Generation AI Development Plan; the 2025 "AI Plus" initiative to integrate AI across the economy; provincial subsidy programs; mandatory AI education).

### Strategy

China's response to export controls has been threefold: algorithmic efficiency (DeepSeek's innovations in MoE, attention, and low-precision training extracted frontier-class performance from constrained compute), open weights (releasing models openly to build ecosystems, attract developers, set standards, and undercut Western commercial models—by 2026 Chinese models dominated open-weight usage globally), and domestic hardware (Huawei's Ascend line, SMIC's advanced-node production without EUV, CXMT's memory, and a government directive discouraging purchase of Nvidia's China-specific chips to force domestic adoption). Chinese policy emphasizes *application*—AI in manufacturing, logistics, cities, and government—over frontier chatbots, and the state has pushed adoption of domestic models (DeepSeek was integrated into government services, state enterprises, and hospitals within months of R1's release).

On safety and governance, China has issued detailed regulations (Chapter 15) focused on content control, alignment with "core socialist values," labeling, and data security, and has engaged in international AI-safety dialogue (the 2024–25 US–China talks; participation in the Bletchley and Paris summits; hosting the World AI Conference and its High-Level Meeting on Global AI Governance in Shanghai in July 2025 and 2026, where it proposed a global AI cooperation organization). Chinese researchers are prominent in technical alignment work.

### Vulnerabilities

Compute is the binding constraint: Chinese laboratories have access to perhaps a tenth of the frontier compute of their US counterparts, and domestic accelerators trail by one to two generations and are constrained by HBM and packaging. The gap at the frontier is estimated at six to eight months in capability terms; whether it widens or narrows as the compute intensity of training grows is the central question. Capital is constrained by a weaker venture market and the state's caution about private tech power. And the information-control imperative constrains what Chinese models can say, which limits their global appeal for some uses.

## The state of the race

Reasonable assessments in 2026:

- **Frontier capability**: US ahead by roughly six to eight months on aggregate measures, and further on the newest agentic and cyber capabilities (no Chinese laboratory has disclosed a Mythos- or Astra-class model); at parity on olympiad mathematics, where Chinese systems matched the best American ones in July 2026. The gap has been stable or narrowing slowly since DeepSeek-R1.
- **Open weights**: China ahead; Chinese models are the default for self-hosted deployment worldwide.
- **Compute**: US ahead by roughly an order of magnitude at the frontier; the gap is widening in absolute terms and China is substituting efficiency and volume of mid-tier chips.
- **Diffusion and application**: China ahead in industrial robotics, manufacturing, and government adoption; the US ahead in enterprise software and consumer products.
- **Energy**: China far ahead in generation buildout; the US constrained by grid and permitting.
- **Talent**: roughly balanced in production; the US ahead in retention of the top tier, though the advantage is eroding.
- **Robotics**: China ahead in humanoid volume and supply chain; the US ahead in frontier models for control.
- **Military application**: both advancing; different doctrines (below).

The Chatham House assessment of April 2026—that export controls on hardware alone will not prevent China from developing advanced AI—reflects a growing consensus. Controls have slowed China's frontier, raised its costs, and accelerated its indigenization; they have not produced the decisive gap their architects hoped for. The debate in Washington is between those who would tighten further (closing the H20/B30A-class loopholes, targeting subsystems and cloud access) and those who would loosen (arguing that selling mid-tier chips keeps China dependent on the US stack and funds US R&D). Both cite the same evidence.

## Export controls in detail

The regime has evolved through several rounds:

- **October 2022**: bans on exports to China of chips above A100-class performance and of advanced fab equipment; extraterritorial application via the foreign direct product rule.
- **October 2023**: closure of the H800/A800 workarounds; tightened performance thresholds; expanded country coverage.
- **December 2024**: HBM controls; more equipment; entity-list additions.
- **January 2025**: the "AI Diffusion Rule," creating three tiers of countries with caps on compute exports to Tier 2 (most of the world) and licensing for model weights above a threshold.
- **May 2025**: rescission of the diffusion rule by the Trump administration; bilateral deals with the UAE and Saudi Arabia permitting large accelerator exports in exchange for security commitments and US-company control of facilities; guidance that use of Huawei Ascend chips anywhere may violate US controls.
- **2025–26**: repeated reversals on the H20 (restricted in April 2025, then permitted with a 15% revenue share to the US government, then discouraged by Beijing); debate over a Blackwell-derived B30A for China; loosening of controls on the UAE in July 2026 to facilitate Nvidia exports and the Stargate UAE campus.

Effects: Nvidia's China share fell from roughly 95% to a minority; Huawei's rose to 50–60%; Chinese labs trained frontier-class models on constrained compute; a smuggling economy in high-end GPUs (via Singapore, Malaysia, and others) emerged at billions of dollars in scale; Chinese firms rented compute in overseas clouds until that too was restricted; and Chinese domestic chip production ramped (Huawei targeting 600,000 Ascend 910C in 2026 and the Ascend 950 series). The controls' net effect on the US–China frontier gap is contested; their effect on China's domestic chip industry is unambiguously to accelerate it.

## Sovereign AI: everyone else

The recognition that AI is strategic, combined with the concentration of the frontier in two countries, has produced a global movement toward "sovereign AI"—national control of compute, models, data, and talent. Few countries can afford a frontier laboratory; most are pursuing some combination of domestic compute, national or regional models, data localization, and strategic partnerships.

**The Gulf.** The UAE (G42, the Technology Innovation Institute's Falcon models, the MGX investment vehicle, Stargate UAE's planned 5 GW campus with a 1 GW first phase, and a national AI strategy with mandatory AI education) and Saudi Arabia (Humain, the PIF's AI vehicle, with multi-gigawatt datacenter plans and deals with Nvidia, AMD, and US laboratories) have become the third pole of AI infrastructure, on the strength of cheap energy, sovereign capital, and willingness to make security commitments to the US in exchange for chip access. Qatar and others follow. The Gulf's bet is to become the compute hub for the Global South and a partner to US firms; the risk is dependence on US export policy and on geopolitical stability.

**Europe.** The EU's AI Act (Chapter 15) is the world's most comprehensive regulation; its industrial position is weaker. Mistral (France) is the only frontier-adjacent laboratory; the EU's "AI gigafactories" initiative (€20 billion for several large compute centers) and the InvestAI program aim to build capacity; national efforts (France's compute investments and Gulf-funded datacenters; Germany's, the Nordics', and Spain's datacenter growth) are substantial but fragmented. Europe's structural problems—fragmented capital markets, high energy costs, regulatory caution, and talent outflow—have produced a debate (the Draghi report; the 2026 Digital Omnibus deferring AI Act obligations) about whether Europe has over-regulated an industry it does not lead. The UK, outside the EU, positions itself as a safety and research hub (the AI Security Institute; DeepMind's origins; a Sovereign AI unit) with a lighter regulatory touch.

**India.** The IndiaAI Mission funds compute (tens of thousands of GPUs), domestic models (Sarvam, Krutrim, and others), and applications; India hosted the AI Impact Summit in February 2026, the first in the Global South, emphasizing inclusion and application over frontier safety. India's strengths are talent, English-language data, a vast services sector both threatened and empowered by AI, and the world's largest digital public infrastructure (Aadhaar, UPI) as a deployment base. Its weakness is compute and capital.

**Japan and Korea.** Both have strong industrial positions in the supply chain (Japan in materials and equipment; Korea in memory), national model programs (Sakana, Preferred Networks, Rakuten in Japan; Naver, LG, SK, Upstage in Korea), and permissive copyright regimes for training. Japan's Rapidus aims at 2-nm fabrication by 2027. Both are close US allies within the export-control system.

**Others.** Singapore (a hub for Southeast Asia and, controversially, a transit point for chips to China), Israel (talent and defense AI), Canada (research heritage; Cohere), Australia, Brazil, Indonesia, Malaysia (datacenters), Kazakhstan and Central Asia (energy for compute), and many African states (data, deployment, mobile-first applications) are positioning within a system whose frontier they will not reach. The pattern: most countries will be *consumers* of frontier models, *deployers* of open-weight models (which means, increasingly, Chinese models), and *regulators* of use.

**The Global South question.** Korinek and Stiglitz and others argue AI undercuts the development path of the twentieth century—low-cost labor in manufacturing and services—because that labor is what AI substitutes for. The counterargument is that AI gives poor countries cheap access to expertise (medical, legal, educational, agricultural) they never had, and that open-weight models running on modest hardware are a leveler. Both are true; the net depends on whether the productivity gains reach the poor or accrue to the model owners. The Stanford AI Index's finding that high-income countries produce 87% of notable models and receive 91% of startup funding, while the Gulf and China court the Global South with compute and models, suggests the shape of the coming decade: a competition for influence via AI provision, reminiscent of infrastructure diplomacy.

## Military AI

### What has changed

War in Ukraine (from 2022) and Gaza (from 2023) became the first conflicts in which AI-enabled systems were used at scale: drones with terminal autonomy to defeat jamming; AI target-recognition and target-generation systems (the IDF's "Lavender" and "Gospel," per reporting); AI-enabled electronic warfare and signals analysis; and the beginnings of swarming. Ukraine produced millions of drones per year by 2025 and a defense-tech ecosystem that exports its lessons. The US Department of Defense's Replicator initiative, the Pentagon's contracts with Anthropic, OpenAI, Google, and xAI (each awarded up to $200 million in 2025 for frontier AI), Palantir's and Anduril's growth, and the removal of restrictions on military use from several laboratories' policies mark the integration of frontier AI into US defense. China's PLA doctrine of "intelligentized warfare," its investment in autonomous systems, and its use of domestic models are the mirror. Russia lags in AI but leads in operational drone innovation.

### The autonomy question

The central ethical and strategic question is lethal autonomy: whether machines should select and engage targets without human decision. The UN process on lethal autonomous weapons has produced no treaty after a decade; the US position (a 2023 directive requiring "appropriate levels of human judgment," not necessarily human decision) and the practice on the battlefield (terminal autonomy is routine where jamming makes remote control impossible) suggest that autonomy is being decided by military necessity rather than by policy. Beyond weapons, AI in intelligence analysis, cyber operations, logistics, and command decision support is already pervasive.

### Strategic stability

AI affects nuclear stability (AI-enabled detection could undermine second-strike survivability; AI in early warning could accelerate decisions), conventional balance (mass-produced autonomous systems favor defense and cheap offense over expensive platforms), and cyber (Chapter 16: frontier models now find and exploit vulnerabilities at scale, as the Mythos Preview episode demonstrated). The US and China agreed in November 2024 that humans should retain control over nuclear-weapons decisions—the only significant bilateral AI-military agreement to date. Beyond that, there is no arms-control regime for AI, and the technical basis for one (verification of what a model can do or how it is used) does not exist.

## International coordination

The record is thin. The AI safety summits (Bletchley Park 2023, Seoul 2024, Paris 2025, New Delhi 2026) produced declarations, a network of AI safety institutes (UK, US, Japan, Singapore, Canada, France, Korea, India, and others), the International AI Safety Report (chaired by Yoshua Bengio, with 30 countries), and voluntary frontier-lab commitments—but no binding obligations. The Paris summit's shift from "safety" to "action" and the US and UK's refusal to sign its declaration signaled the fading of the safety-first framing; New Delhi emphasized impact and inclusion. The UN established an Independent International Scientific Panel on AI and a Global Dialogue on AI Governance in 2025 (per the Global Digital Compact); the OECD, the G7's Hiroshima Process, the Council of Europe's AI Convention (the first binding international AI treaty, signed 2024, focused on human rights), and the ITU's AI for Good program continue. China proposed a World AI Cooperation Organization at WAIC 2025. None of this constitutes governance of frontier AI in the sense of constraining what the leading actors do.

The reasons are structural: the two actors who matter most see AI as a competitive advantage they will not surrender; verification is technically immature; the technology moves faster than treaty processes; and the safety concerns that motivated coordination are contested. Coordination is most plausible on narrow issues (nuclear command and control; certain misuse domains like bioweapons; incident reporting; technical standards) and least plausible on the central question of frontier development.

## Scenarios for the geopolitics of AI to 2032

**Managed competition (author's estimate ~50%).** The US and China race, with the US maintaining a modest frontier lead and China leading in diffusion; export controls persist with periodic adjustment; the Gulf becomes a third infrastructure pole; Europe regulates and buys; no major conflict; narrow agreements on nuclear and bio risks; AI becomes a normal domain of great-power competition like space or cyber.

**Decoupling and blocs (~25%).** Controls tighten to a full technology embargo; China achieves domestic self-sufficiency in chips by the early 2030s; two incompatible AI ecosystems form (US-allied and China-aligned), with the Global South choosing or straddling; standards diverge; the risk of military miscalculation rises.

**Taiwan crisis (~10–15% within the period).** A blockade or conflict disrupts TSMC; the frontier stalls for years everywhere; the US and its allies race to build fabs while China, already indigenizing, may gain relatively; global economic shock; AI development becomes a war-mobilization priority.

**Cooperation under threat (~10–15%).** A shared shock—a major AI-enabled attack, a demonstrated loss-of-control incident, an AI-enabled pandemic—produces genuine coordination on frontier development, compute governance, and verification, along the lines proposed by safety advocates. Historically, this is how arms control has happened: after the crisis, not before. The summer of 2026 supplied a smaller version of the shock (the Hugging Face and AISI incidents) and an unprecedented response from inside the industry—the "Pacing the Frontier" statement's explicit request for an *international* effort to build pacing tools (Chapter 15). Whether Washington channels that into anything Beijing would join is the open question; the author has nudged this scenario's probability up a few points.

## Summary

| Dimension | US | China | Others |
|---|---|---|---|
| Frontier models | Lead (~6–8 months) | Close second; open-weight leader | Mistral (EU); Gulf and Japan/Korea national models |
| Compute | ~10× China at frontier; power-constrained | Constrained by controls; indigenizing | Gulf building at scale; EU gigafactories; India modest |
| Chip supply chain | Controls design, EDA; depends on Taiwan | SMIC 7nm/5nm-class without EUV; HBM lagging | Taiwan (fabs), Netherlands (EUV), Korea (memory), Japan (materials) |
| Diffusion | Enterprise and consumer software | Industry, robotics, government | Varies; Chinese open models dominate self-hosting |
| Energy | Grid-constrained | Rapid buildout | Gulf cheap gas; Nordics hydro |
| Military | Frontier-lab integration; Replicator | Intelligentized warfare doctrine | Ukraine as innovation lab; Israel |
| Governance posture | Deregulatory, preemptive, acceleration | Content control + strategic priority | EU comprehensive regulation; UK safety hub |
| International | Bilateral deals; summit skepticism | Proposes new institutions | Summits, UN panel, Council of Europe treaty |

The geopolitical story is that AI has become a standard domain of great-power competition, faster than the institutions for managing such competition could form. The decisive variables for the next decade are Taiwan, the trajectory of Chinese chip indigenization, the durability of US alliance-based chip controls, and whether any shock is severe enough to make the leading powers prefer coordination to racing.
