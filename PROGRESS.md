# PROGRESS / HANDOFF LOG — "The Future of AI" comprehensive review

> READ THIS FIRST after any context compaction. It is the single source of truth for
> what has been done, what remains, and how to continue with minimal degradation.

## User requirements (verbatim intent)
- Produce the best possible, most comprehensive, most detailed, most in-depth, well-researched
  review/guide on the FUTURE OF AI and everything related.
- No time or word limit. Be thorough.
- Final output: (1) a Markdown document, (2) a website to read it.
- Push to GitHub CONSTANTLY (straight to `main`, NO branches, NO PRs) because the session may
  be interrupted by credit exhaustion. Context compaction will also happen — so document reasoning
  here and commit incrementally.

## Repo
- Remote: https://github.com/gorg667/ai-future.git  (branch: main)
- GitHub creds already configured via setup_github_environment (re-run it if push fails with 401/403).
- Push command: `cd /home/user/webapp && git add -A && git commit -m "..." && git push origin main`

## Architecture decisions
- `docs/chapters/NN-slug.md` — one file per chapter. Written one at a time, committed after each.
- `docs/THE_FUTURE_OF_AI.md` — the assembled single Markdown document (built by `build.py`
  concatenating chapters in order). Regenerate with `python3 build.py`.
- `site/` — static website. `build.py` converts each chapter to HTML using `markdown` python lib
  (pip install markdown) with TOC, sidebar navigation, dark/light theme, search, reading progress.
  Pure static HTML/CSS/JS so it can be hosted on GitHub Pages (from `/site` folder or `docs`).
  DECISION: output site into `/docs-site`? No — keep `site/` and also copy to root `index.html`
  so GitHub Pages "deploy from main root" works. build.py writes `site/*.html` and `index.html`.
- Style: authoritative, cited (inline references to real papers/reports with names+years),
  balanced (optimist/skeptic views), explicit uncertainty, forecasts with dates & probabilities.
- Date of writing: September 2026 (sandbox date). Knowledge is grounded up to training data;
  where unsure of 2025–2026 specifics, phrase carefully and flag uncertainty rather than fabricate.

## Chapter plan (status: [ ] todo, [~] in progress, [x] done+pushed)
00 [x] Front matter, how to read, executive summary
01 [x] A brief history of AI & why this moment is different (from Dartmouth to transformers to agents)
02 [x] The state of the art in 2026: frontier models, capabilities, benchmarks, what's solved/unsolved
03 [x] Scaling laws, compute, and the physics/economics of training (FLOPs, data walls, algorithmic efficiency, inference-time compute)
04 [x] Hardware & infrastructure: GPUs/TPUs/ASICs, energy, datacenters, memory bandwidth, networking, photonics, neuromorphic, quantum
05 [x] Data: the data wall, synthetic data, licensing, curation, RL environments
06 [x] Architectures beyond the transformer: SSMs, mixture-of-experts, diffusion LMs, world models, JEPA, neurosymbolic, continual learning
07 [x] Reasoning, test-time compute, RL, verifiers, and the path to reliable problem-solving
08 [x] Agents: autonomy, tool use, computer use, multi-agent systems, agent economies, protocols (MCP, A2A)
09 [x] Multimodality & embodiment: vision, audio, video generation, robotics, humanoids, self-driving
10 [x] AI for science: AlphaFold-class breakthroughs, math, materials, drug discovery, AI scientists
11 [x] Economics: productivity, labor, wages, task automation, firm structure, GDP scenarios, inequality
12 [x] Work & professions: sector-by-sector (software, medicine, law, education, creative, finance, manufacturing)
13 [x] Society & culture: information ecosystem, relationships/companions, education, mental health, creativity, attention
14 [x] Geopolitics: US–China, chips/export controls, sovereign AI, Europe, Gulf, Global South, military AI
15 [x] Governance & regulation: EU AI Act, US executive orders/state laws, China, international bodies, standards, compute governance
16 [x] Safety & alignment: technical alignment agenda, interpretability, evals, misuse (bio/cyber), loss of control, open weights debate
17 [x] AGI & superintelligence: definitions, timelines (expert surveys, forecasts), takeoff scenarios, intelligence explosion arguments
18 [x] Scenarios 2026–2040: several detailed scenario narratives with probabilities & signposts
19 [x] Open problems & research frontiers (what we don't know)
20 [x] Practical guide: for individuals, students, workers, founders, executives, policymakers, researchers
21 [x] Glossary
22 [x] Bibliography / further reading
23 [x] Appendix: forecasting table, key numbers, timeline of milestones

## Workflow per chapter
1. Write `docs/chapters/NN-slug.md` (aim 4,000–9,000 words each; dense, structured, with tables).
2. `python3 build.py` (regenerates assembled MD + site).
3. Commit + push. Update this file's checklist.

## Log (append newest at bottom)
- 2026-09-09: Repo empty. Created skeleton, PROGRESS.md, chapter plan.
- 2026-09-09: Research notes saved (docs/RESEARCH_NOTES.md). Ch00, Ch01 done. Next: Ch02 state of the art. NOTE: if build.py fails with no module markdown run: python3 -m pip install markdown pymdown-extensions
- Ch02 done. Next: Ch03 scaling laws & compute economics.
- Ch03 done. Next: Ch04 hardware & infrastructure.
- Ch04 done. Next: Ch05 data.
- Ch05 done. Next: Ch06 architectures beyond transformer.
- Ch06 done (rewritten after interruption lost it). Next: Ch07 reasoning/RL/test-time compute. LESSON: commit immediately after each Write; if interrupted mid-write, check file exists.
- Ch07 done. Next: Ch08 agents.
- Ch08 done. Next: Ch09 multimodality & embodiment/robotics.
- Ch09 done. Next: Ch10 AI for science.
- Ch10 done. Next: Ch11 economics.
- Ch11 done. Next: Ch12 work & professions sector by sector.
- Ch12 done (rewritten after 2nd interruption). Next: Ch13 society & culture.
- Ch13 done. Next: Ch14 geopolitics.
- Ch14 done. Next: Ch15 governance & regulation.
- Ch15 done. Next: Ch16 safety & alignment.
- Ch16 done. Next: Ch17 AGI & superintelligence.
- Ch17 done. Next: Ch18 scenarios 2026–2040.
- Ch18 done (rewritten after 3rd interruption). Next: Ch19 open problems, then 20 practical guide, 21 glossary, 22 bibliography, 23 appendix.
- Ch19 done. Next: Ch20 practical guide.
- Ch20 done. Next: Ch21 glossary, 22 bibliography, 23 appendix.
- Ch21 done. Next: 22 bibliography, 23 appendix.
- Ch22 done. Next: 23 appendix (forecast table, key numbers, timeline), then final QA pass + README.
- Ch23 done. ALL 24 CHAPTERS COMPLETE. Next: README.md, QA pass (check site renders, links), consider GitHub Pages deploy note.
- README.md written. Site QA: 24 pages, 0 broken links, tables rendered, search.json 24 entries. HTTP serve OK.
- STATUS: PROJECT COMPLETE (v1). Possible future work: enable GitHub Pages in repo settings (user action), deeper fact-check pass on [W]-marked items, add diagrams.

---

# V2 IMPROVEMENT PASS (session 2, 2026-09-09) — READ THIS AFTER COMPACTION

## User instruction (session 2)
"Fully review everything you made and do the best possible improvements you see fit. Change/add/remove/research
whatever. No time limit." Push straight to main constantly; no branches/PRs. Document reasoning here.

## Full-review findings (all 24 chapters read end to end)
Strengths: coherent voice, explicit uncertainty, forecast register, good cross-referencing. Weaknesses found:
1. **Stale/inconsistent numbers vs. live web (Sept 2026)**:
   - HLE: doc says ~59% (Fable 5.1). Web (Sep 8 2026): benchlm/llm-stats say Claude Fable 5.1 = 65%; pricepertoken says
     Fable 5 55.5%. Sources disagree → state "roughly 55–65% depending on leaderboard/config" and name the models.
   - ARC-AGI-3: doc says "30–60% by Sep 2026". arcprize.org/blog/astra (Sep 3 2026): GPT-6 Astra SOTA; benchlm: Astra 62.7%,
     Opus 5 30.2% (Jul 24 2026), GPT-5.6 Sol 7.8%. Launch scores: Opus 4.6 (Max) 0.50%, Gemini 3.1 Pro 0.37%, GPT-5.4 0.26%.
     ARC-AGI-3 technical report = arXiv 2603.24621 (Apr 22 2026). → update Ch02/07/17/23 with named models + dates.
   - METR: ai2027-tracker (May 2026): best model ~16–20h 50% horizon, 3–4h 80% horizon, CI 5–66h. Consistent with doc.
   - EU AI Act Omnibus: provisional political agreement **7 May 2026**; Council final green light **29 June 2026**
     (doc said "mid-2026"/"~Aug 2026"). Annex III → 2 Dec 2027; Annex I → 2 Aug 2028; **watermarking/transparency
     (Art. 50) → 2 Dec 2026** (was Feb 2027 in proposal). Also bans "nudification apps". → fix Ch15, RESEARCH_NOTES, Ch23 timeline.
   - Ch02 landscape mentions "Claude 5 generation" vaguely; web shows Claude Opus 5, Claude Fable 5/5.1, "Claude Mythos 5",
     GPT-6 Astra, GPT-5.6 Sol all exist by Sep 2026. Name them in Ch02 with medium-confidence flag.
2. **Ch01 Part III header says "(2020–2024)" but Part IV starts late 2024** — fine. But Ch01 timeline table lacks 2021 AlphaFold
   context detail; OK. Minor.
3. **Ch03 repeats Ch02 cost curve**; acceptable but trim redundancy? Decided: keep (chapters must stand alone).
4. **Ch11 table**: "Federal Reserve surveys" row fine. Missing: any 2026 macro productivity data point → add note.
5. **Ch16 missing**: nothing on "AI welfare/model welfare" beyond Ch13 — fine. Missing explicit section on **evaluation
   awareness undermining safety cases**; covered briefly. OK.
6. **Missing content (gaps to fill)**: (a) no diagrams/figures at all — add SVG charts generated in build.py (matplotlib
   available) for: compute trend, METR horizon, cost decline, scenario probabilities, AGI forecast spread, capex vs revenue;
   (b) no "How to read the numbers / confidence legend" box; (c) no per-chapter "Key takeaways" summary boxes —
   add 3–5 bullet "In brief" admonition at top of each chapter (big readability win); (d) no PDF/EPUB export — pandoc is
   available → add `site/THE_FUTURE_OF_AI.epub` and PDF if feasible; (e) no favicon (404 in console) → add inline SVG favicon;
   (f) no "changelog / version" page; (g) no cross-chapter "Where numbers disagree" section — add to Appendix.
7. **Site UX**: sidebar TOC search works; missing: keyboard nav (←/→ between chapters), "back to top", print stylesheet,
   font-size control, reading-time on index OK. Add `<link rel=canonical>`, OpenGraph meta, sitemap. Add figures with captions.
8. **Build**: works. Add `--check` mode that verifies internal links + anchors.

## V2 task list (status)
- [x] Plan written to PROGRESS.md and pushed
- [x] T1 Fact updates DONE (all chapters touched; see docs/RESEARCH_NOTES.md "Session-2 verification" for sources). Major additions: GPT-6 Astra, Fable/Mythos/Opus 5, HF incident + METR/Redwood, Anthropic/AISI incidents, Pacing the Frontier, FRONTIER Act, ARC-AGI-3 solved, IMO 2026, capex $750-900B, EU Omnibus dates. Appendix E (source disagreements) + F (changelog) added.
  LESSON: sandbox reset twice mid-task and wiped uncommitted edits AND git credentials. Commit after EVERY file edit; re-run setup_github_environment if push 401s; `pip install markdown pymdown-extensions` needed after reset.
- [x] T2 "In brief" boxes on chapters 00–20 (tools/add_briefs.py, idempotent; rendered as abstract admonition; briefs also feed index cards)
- [x] T3 Nine SVG figures (tools/make_figures.py → docs/fig/, copied to site/fig/ by build.py; placed via tools/add_figures.py): compute-trend, metr-horizon, inference-cost, benchmark-lifespans, capex-vs-revenue, agi-forecasts, scenarios, canaries, hf-incident. Embedded in Ch02, 03, 08, 11, 16, 17, 18.
- [x] T4 Site UX: data-URI favicon, ←/→ keyboard nav, back-to-top, print CSS, font-size control, canonical + OpenGraph meta, sitemap.xml, index "start here" cards. PlaywrightConsoleCapture: 0 console errors.
- [x] T5 Appendix E "Where sources disagree" + confidence legend; Appendix F changelog (v1/v2).
- [x] T6 EPUB via pandoc → site/THE_FUTURE_OF_AI.epub (367 KB), linked from sidebar + index. (PDF skipped: no LaTeX engine; EPUB + print stylesheet cover the use case.)
- [x] T7 Link checker in build.py (skips http/mailto/data:/$ template hrefs) → 0 problems. README rewritten for v2. Final consistency sweep done (exec-summary AGI median aligned with Ch17; HLE leftover in Ch07 fixed; grep for stale 30–60% ARC / 600–750 capex / 50%-by-2032 → only legitimate hits remain).

## Log (v2)
- Plan written. Starting T1.
- T1 done across all chapters; RESEARCH_NOTES "Session-2 verification" appended.
- T2–T6 done; build_site rewritten; site regenerated.
- Sandbox reset a THIRD time after the "card brief styling" commit: lost the ch00/ch07 consistency edits + pip packages. Redid them, committed, pushed.
- README v2, PROGRESS updated. Final full build (with EPUB) + push = end of v2 pass.

## How to continue (for a fresh instance)
1. `cd /home/user/webapp && git status -sb` — should be clean and `main...origin/main`. If push 401s → run setup_github_environment.
2. `pip install markdown pymdown-extensions matplotlib` (lost on every sandbox reset). pandoc is at /usr/bin/pandoc.
3. Edit chapters in docs/chapters/; run `python3 tools/add_briefs.py` only if changing briefs (BRIEFS dict); `python3 tools/make_figures.py` if changing figure data; `python3 build.py` to regenerate everything; commit + push straight to main after EVERY edit.
4. Any new fact revision → also add a line to Appendix F changelog (docs/chapters/23-appendix.md) and, if sources disagree, to Appendix E.
5. Possible v3 ideas (not started): PDF via weasyprint/LaTeX if installed; per-chapter reading-time in sidebar; automated freshness check script that lists claims with dates older than N months; translate "In brief" boxes into a standalone one-page summary.
