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
