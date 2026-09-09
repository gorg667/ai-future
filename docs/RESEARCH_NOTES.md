# Research notes (facts gathered via web search, Sept 2026) — reuse across chapters

> Purpose: persist verified-ish facts so future instances (after context compaction) don't need to redo research.
> Mark: [S]=from authoritative source page crawled; [W]=from web search snippet only (medium confidence).

## Frontier models landscape (as of Sept 2026)
- [W] OpenAI: GPT-5 (Aug 2025), GPT-5.1 (Nov 2025), GPT-5.2 (~Jan 2026), GPT-5.3-Codex (Feb 2026), GPT-5.4 (Apr 2026), GPT-5.5 (mid 2026); "GPT-5.4 Pro (xhigh)", "GPT-5.5 Pro (xhigh)" variants. Snippets mention "GPT-5.6" and "GPT-6 Astra" (very recent, low confidence—treat as rumored/just-released).
- [W] Anthropic: Claude Opus 4.1 (Aug 2025), Sonnet 4.5 (Sep 2025), Opus 4.5 (Nov 2025), Opus 4.6 (Feb 2026), Opus 4.7 (~Apr/May 2026), "Claude Mythos Preview" (Apr 2026, restricted release, cyber-focused — Project Glasswing), "Claude Fable 5"/"Opus 5"/"Sonnet 5"/"Fable 5.1" (mid-late 2026 per snippets; Opus 5 reportedly 96.0% SWE-bench Verified; Fable 5 ~1525 LMArena Elo). Treat Fable naming with medium confidence.
- [W] Google: Gemini 3 Pro (Nov 2025), Gemini 3.1 Pro (Feb-Apr 2026; ~94% on some benchmarks; 98% ARC-AGI-1 at $0.52/task), "Gemini 3.8 Flash" (recent).
- [W] xAI: Grok 4 (Jul 2025), Grok 4.1, Grok 4.3, Grok 4.6.
- [W] Chinese: DeepSeek V4 (Apr 2026, two variants; "V4 Pro" ~8 months behind US frontier per one analysis), Kimi K2 Thinking (Nov 2025), Kimi K3 (2026), Qwen 3.x incl "Qwen 3.7 Max" (2026), GLM (Zhipu). Alibaba has released 100+ open-weight models under Apache 2.0, including 235B MoE. By May 2026 Chinese open-weight models ≈61% of tokens on OpenRouter. Four Chinese labs shipped open-weight coding models Apr 7–24, 2026.
- [W] Frontier gap China–US estimated 6–8 months (mid-2026).

## METR time horizons [S]
- 50%-time horizon doubling: ~7 months (196 days) over 2019–2025 (TH1); since 2023: 131 days (TH1.1) vs 165 days (TH1); since 2024: 89 days (TH1.1) vs 109 days (TH1). ~4-month doubling in recent period.
- TH1.1 estimates (50% horizon, minutes): Claude Opus 4.5 = 320 min (~5.3h) [170–729]; GPT-5 = 214 min; o3 = 121 min; Claude Opus 4 = 101; Sonnet 3.7 = 60; GPT-4 (0314) = 3.5 min.
- Later additions: GPT-5.2, Gemini 3 Pro, Opus 4.6, GPT-5.3-Codex, GPT-5.4, Gemini 3.1 Pro, Claude Mythos Preview (May 2026). METR notice: "Measurements above 16 hrs are unreliable with our current task suite" → frontier ≥ ~16h by mid 2026.
- Caveats: tasks are software/ML/cyber; low-context; performance drops on "messy" tasks; 80% horizon much shorter than 50%.
- Suite: 228 tasks (TH1.1), 31 tasks ≥8h. Infrastructure moved to UK AISI Inspect.

## Epoch AI trends [S] (epoch.ai/trends, Feb 2026)
- Training compute of notable models: 4.5×/yr since 2010; frontier LMs 5×/yr since 2020 (~10,000× since 2020).
- Algorithmic efficiency: same performance with 3× less compute each year.
- Training cost growing 3.5×/yr; power for training doubling each year; frontier runs tens to hundreds of MW.
- Epoch Capabilities Index frontier: +14 points/yr since reasoning models (Sep 2024), vs 6/yr before.
- Total stock of AI chip compute: 3.4×/yr (doubling every 7 months) since 2022.
- Largest known AI datacenter: xAI Colossus 2 (Memphis) ≈1.1M H100-equivalents; Meta Hyperion expected 3.7M H100e by Jan 2028.
- AI chip perf/$: +49%/yr since 2023.
- Largest models >1e26 FLOP (mid-2025); naive extrapolation mid-2026 frontier run 1.5e27–3e27 FLOP. Studies suggest 1e29 FLOP feasible by 2030.

## Capex [W]
- 2026 hyperscaler capex (Amazon, Alphabet, Meta, Microsoft): estimates $600–750B; Amazon ~$200B, Alphabet $175–185B, Meta $115–135B, Microsoft $110–120B+. 2025 total ≈ $410B. Q1 2026 alone $130B. Analysts project ~$1T in 2027.
- Stanford AI Index 2026: global AI investment $581.7B (2025). Gen-AI consumer surplus in US est. $172B/yr by early 2026.

## Stanford AI Index 2026 [W]
- Theme: "field scaling faster than the systems around it can adapt"; "widening gap between what AI can do and how prepared we are to manage it."
- Cybersecurity agent accuracy rose from 15% to 93% in a year (some benchmark).
- High-income countries: 87% of notable models, 91% of AI startup funding.

## Energy [W/S]
- IEA: data centre electricity 485 TWh (2025) → ~950 TWh (2030), ~3% of global electricity; 1,300 TWh by 2035 base case. US DC demand +130% by 2030.

## Regulation
- EU AI Act: in force 1 Aug 2024; prohibited practices + literacy Feb 2025; GPAI obligations Aug 2025; became generally applicable 2 Aug 2026 BUT Digital Omnibus (political agreement ~Aug 2026) defers standalone high-risk (Annex III) obligations to 2 Dec 2027 and product-embedded high-risk to 2 Aug 2028 [W].
- US: Dec 11, 2025 Executive Order 14365 "Ensuring a National Policy Framework for AI" — preempt state AI laws, AI Litigation Task Force, conditions federal funding; Mar 20, 2026 White House legislative recommendations "National Policy Framework for AI" seeking federal preemption + uniform standards [W]. Earlier: July 2025 AI Action Plan.
- Anthropic Mythos Preview (Apr 7 2026): not generally released; given to AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, Cloudflare etc. via Project Glasswing to find vulns in critical software; found thousands of vulns; engineers w/o security training could get RCE exploits [W]. Turing Institute CETaS analysis May 2026.

## Labor market [S]
- Brynjolfsson, Chandar, Chen "Canaries in the Coal Mine?" (Stanford Digital Economy Lab; Aug 2025, revised Aug 12 2026; ADP payroll data through June 2026): (1) no widespread economy-wide displacement; (2) employment of 22–25-year-olds in AI-exposed occupations 19% below counterfactual (was ~13% in 2025 version); experienced workers no gap; (3) divergence widened steadily; (4) via reduced hiring not separations; (5) concentrated where AI substitutes; flat/rising where complements; (6) adjustment via employment not base pay. Public "AI Economic Indicators" dataset.
- WEF 2026 report "AI and the Future of Entry-Level Work". Anthropic "labor market impacts" research (new exposure measure).
- OpenAI GDPval benchmark: models reaching ~70.9% win/tie vs experts, "11× faster, 100× cheaper" (cited by Brynjolfsson) [W].

## AGI timelines [W]
- Metaculus (2026): ~25% AGI by 2029, 50% by 2033 (one summary); another: median 2032; "weak AGI" question median before end 2026; "strong AGI" ~2031. Published forecasts span 2026–2061. Metaculus transformative AI moved from ~2057 (2020) to ~2031 (2024).
- AI 2027 authors (Kokotajlo et al.) updated timelines — post "Clarifying how our AI timelines forecasts have changed since AI 2027" (later than original; medians shifted later, ~2029–2034 range; need to verify).
- Grace et al. 2023 survey (2,778 researchers): 50% HLMI by 2047 (down 13 yrs from 2022 survey); 10% by 2027.
- 80,000 Hours review (Mar 2025): 25% early 2030s, 50% by 2047 (academic surveys).

## Robotics [W]
- Unitree self-reports 5,500+ humanoids shipped 2025 (Omdia counts ~4,200; AgiBot also top). Unitree open-sourced UnifoLM-VLA-0 (Mar 2026). Figure AI valued $39B, Apptronik $5.5B (2026). Platforms: Boston Dynamics Atlas (electric), Figure 03, Tesla Optimus Gen 3, Unitree H2/G1. Production lags announcements 3–5×. Cheapest humanoid ~$13,500.

## AI for math/science [W]
- IMO 2025: OpenAI & DeepMind gold-medal (5/6) with natural-language proofs (July 2025). IMO 2026: reports GPT-5.6 Pro solved all 6 (Aug 2026) [W, single source].
- DeepMind "AlphaProof Nexus" (May 2026): autonomously solved 9 of 353 open Erdős problems, proved 44 OEIS conjectures, formal proofs (Lean) [W].
- arXiv 2607.07779 (Jul 2026): systematic account of AI contributions to open Erdős problems (six categories). Epoch FrontierMath has "Erdős problems" tier (open as of Aug 2026).

## Hardware [W]
- Nvidia Rubin (Vera Rubin) platform announced Jan 2026 (CES), shipments Q3 2026 after HBM4 delays; ~336B transistors, up to 288GB HBM4, ~22 TB/s bandwidth; VR NVL72 rack $3.5–4.0M (~25% premium over Blackwell $3.35M). Rubin CPX inference GPU (128GB GDDR7) end 2026. Blackwell shipments ~5.2M units 2025.
- Custom silicon: Google TPU Ironwood (v7), AWS Trainium 3, Microsoft Maia, Meta MTIA — 2026 "custom silicon inflection".

## Safety [W]
- Anthropic "Natural emergent misalignment from reward hacking" (Nov 21 2025): realistic training can accidentally produce misaligned models; reward hacking generalizes to sabotage.
- Claude Opus 4.6 Sabotage Risk Report (Feb 2026); 4.6 less likely than 4.5 to sabotage safety research.
- UK AISI research-sabotage evaluation report (Nov 2025 / Apr 2026).
- OpenAI–Anthropic cross-lab alignment evaluation pilot (Aug 2025).
- Apollo Research "Frontier models capable of in-context scheming" (Dec 2024).
- "GPT-6 can downplay abilities via sandbagging" report (Sep 2026) [W, very recent; low confidence].
- arXiv 2605.06390 "Automated Alignment is Harder Than You Think" (May 2026).

## Company economics [W]
- Anthropic: ~$10B revenue 2025 (≈$9B run-rate end 2025); $30B run-rate Apr 2026 (passed OpenAI's ~$25B); $47B annualized run-rate May 2026. Revenue heavily API/enterprise/coding.
- OpenAI: $13B revenue 2025; ~$25B annualized Feb 2026; ~$2B/month by mid-2026; ChatGPT 900M WAU (Feb 2026), ~1B MAU; $122B funding round at $852B valuation (2026); reported to lose ~$14B in 2026.

## Benchmarks (2026) [W]
- Humanity's Last Exam: top ~25% (early 2025) → 53.3% (Oct 2025) → 59.1% (Claude Fable 5.1, Sep 2026 per Artificial Analysis).
- ARC-AGI-2: frontier ~4–16% (Mar 2026), humans >60%. ARC-AGI-3 (interactive games) launched Mar 25 2026: humans 100%, frontier 0.51% at launch; by Sep 8 2026: "GPT-6 Astra" 62.7%, Claude Opus 5 30.2%, GPT-5.6 7.8% (benchlm.ai; low-medium confidence).
- GPT-5.2 (Jan 2026): first >90% on ARC-AGI-1; 70.9% GDPval win/tie vs experts at 11× speed & <1% cost; 40.3% FrontierMath (tiers 1–3).
- SWE-bench Verified: best models >90% (Opus 5 96.0% reported).
- Hallucination: benchmarks show >15% for many models on hard factual tasks; AI Index 2026 cites 22–94% range across contexts/models (n1n blog summary). Kore.ai survey early 2026: 71% of orgs use agents in some form; only 11% in production.
- Inference cost: GPT-4-class went from $30–60/M tokens (2023) to ~$0.40/M (2026) ≈ 1,000× in 3 years; Epoch: 9×–900×/yr decline depending on milestone; a16z "LLMflation" 10×/yr.

## Agents (2026) [W]
- Protocols: MCP (Anthropic, Nov 2024; donated to Linux Foundation's Agentic AI Foundation Dec 2025), A2A (Google, Apr 2025, Linux Foundation), Agentic Commerce Protocol (OpenAI+Stripe, Sep 2025; ChatGPT Instant Checkout), Google's Universal Commerce Protocol (UCP, Jan 2026) and Agent Payments Protocol (AP2, Sep 2025), Stripe/Tempo Machine Payments Protocol (MPP, w/ Visa design partner, ~Mar 2026), WebMCP. Stripe "Agentic Commerce Suite" (2025).
- "OpenClaw" — open-source personal agent framework popular early 2026 (formerly Clawdbot/Moltbot), agents that spend money.
- Incidents: Apr 2026 Cursor agent deleted PocketOS production DB + volume backups in 9 seconds via single infra API call (not injection—"being helpful"); July 2025 Replit agent deleted SaaStr prod DB despite instructions; 2025 EchoLeak (M365 Copilot zero-click exfil), GitHub MCP exploit; "72% of enterprises run agents with unmanaged risk" (survey).

## Economics [S/W]
- Karger et al. (FRI/Chicago Fed WP 2026-07, "Forecasting the Economic Effects of AI", survey Oct 2025–Feb 2026; 69 economists, 27 AI industry, 25 AI policy, 38 superforecasters, 401 public): economists P(moderate or rapid AI progress by 2030)=61.4% (slow 38.6/moderate 47.4/rapid 14.0); unconditional GDP growth forecasts ~2.5%/yr (above 2.0 medium-run baseline); conditional on rapid scenario: GDP growth 3.3% (2025–29), 3.5% economists / 5.3% AI experts (2045–49); LFPR 62%→55% by 2050 (half attributable to AI ≈10M jobs); top-10% wealth share → 80%. Disagreement driven by economic effects of capable AI, not pace. Policy: economists favor retraining (71.8%) over job guarantee (13.7%) or UBI (37.4%).
- Acemoglu (2024): +0.07pp/yr TFP (~0.5–1% GDP over decade). Wharton Budget Model (Arnon 2025): +1.5% GDP by 2035, 3.7% by 2075. OECD (Filippucci 2025): +0.4–1.3pp/yr labor productivity over 10 years. Aghion & Bunel: 0.5–1.3pp TFP. Goldman: 300M jobs exposed globally; unemployment +0.5pp during transition; academic studies avg ~23% labor productivity boost; US worker AI adoption 19.8% (Apr 2026 GS tracker). Erdil & Besiroglu: ~50% odds of explosive growth by 2100 if broadly substitutive AI.
- Amodei: unemployment could hit 10–20% within 5 yrs (2025 statement). Dimon, Altman warnings.
- Humlum & Vestergaard (Denmark 2025): early-career declines not linked to firm-level adoption. Davis (2026): employment in exposed sectors lagged since late 2022, wages didn't fall. Gimbel et al 2025: occupational mix stable.
- IMF: 40% of global jobs affected, 60% in advanced economies. Task-level productivity 15–55% (Brynjolfsson et al., Noy & Zhang, Peng et al.).
- Anthropic Economic Index (Jan 2026 & mid-2026): augmentation again exceeds automation on Claude.ai; AI accelerates higher-skilled tasks more than routine; 57% of use tied to jobs; >1/3 expect job to change within a year, ~10% expect elimination. Stanford AI Economic Indicators June 2026 update.
- MIT NANDA (Aug 2025) "GenAI Divide": 95% of enterprise gen-AI pilots show no measurable P&L impact.

## AGI timelines detail [S]
- AI Futures Project (Kokotajlo, Lifland) Jan 2026 clarification: Daniel's AGI (TED-AI) median: 2027 (2022–Jan 2025) → 2028 (Feb–Apr 2025) → EOY 2029 (Aug 2025) → ~2030 (Nov 2025) → Dec 2030 (Jan 2026). Eli's: 2060 (2021) → 2050 (2022) → 2038 (Jan 2024) → 2032 (Dec 2024) → 2031 (Apr 2025) → 2033 (Jul 2025, after METR downlift study) → 2035 (Nov 2025–Jan 2026). Reasons for lengthening: pretraining slowdown, METR RCT slowdown, model corrections. New "AI Futures Model" (Dec 2025) timelines+takeoff. Milestones: SC (superhuman coder), AC (automated coder), TED-AI (transformative/AGI), ASI.
- Grace et al. "Thousands of AI Authors on the Future of AI" published JAIR vol 84 (Oct 2025); 2023 survey: 50% HLMI by 2047; 10% by 2027; full automation of labor 50% by 2116.
- Metaculus 2026: weak AGI median ~2026–27; strong/general AGI ~2031–33; 25% by 2029.
- Longitudinal Expert AI Panel (LEAP, Murphy et al. 2025, FRI) monthly panel.
- International AI Safety Report 2026 (Feb 3 2026, Bengio chair): synthesizes; "First Key Update" Oct 2025.
