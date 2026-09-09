# The Future of AI — A Comprehensive Review and Guide

**Version 2.0 (September 2026).** A long-form (~82,000-word, 24-chapter) review of where artificial intelligence stands in September 2026, where it is heading, and what that means for technology, economies, institutions, and individuals. Written to be the most complete single reference a serious reader could want: technology and trajectories, economics, labor, society, geopolitics, governance, safety, the AGI debate, explicit scenarios with probabilities, and practical guidance.

## Read it

- **Website (recommended):** open `site/index.html` locally, or enable GitHub Pages on this repo (Settings → Pages → Deploy from branch `main`, folder `/ (root)`) and visit the published URL — the root `index.html` redirects to the site.
- **EPUB (e-readers):** [`site/THE_FUTURE_OF_AI.epub`](site/THE_FUTURE_OF_AI.epub)
- **Single Markdown document:** [`docs/THE_FUTURE_OF_AI.md`](docs/THE_FUTURE_OF_AI.md) (all chapters assembled, with a table of contents).
- **Individual chapters:** [`docs/chapters/`](docs/chapters/)

Each chapter opens with an **"In brief"** box (three to five sentences of the essentials) so the whole review can be skimmed in about fifteen minutes before reading in depth. Nine data figures (`docs/fig/*.svg`) illustrate the compute trend, METR task-horizon doubling, inference-cost collapse, benchmark lifespans, capex versus revenue, AGI forecast distributions, scenario probabilities, labor-market canaries, and the Hugging Face incident timeline.

## Contents

| # | Chapter |
|---|---|
| 0 | Front matter and executive summary (25 claims with confidence levels) |
| 1 | A brief history of AI, and why this moment is different |
| 2 | The state of the art in 2026: what AI can and cannot do |
| 3 | Scaling laws, compute, and the economics of training |
| 4 | Hardware and infrastructure: chips, datacenters, energy |
| 5 | Data: the wall, the workarounds, and who owns it |
| 6 | Architectures beyond the transformer |
| 7 | Reasoning, reinforcement learning, and test-time compute |
| 8 | Agents: from chatbots to autonomous systems |
| 9 | Multimodality and embodiment: vision, video, voice, robots, self-driving |
| 10 | AI for science |
| 11 | Economics: productivity, labor, growth, distribution |
| 12 | Work and professions: sector by sector |
| 13 | Society and culture |
| 14 | Geopolitics: US–China, sovereign AI, chips, war |
| 15 | Governance and regulation |
| 16 | Safety and alignment |
| 17 | AGI and superintelligence: definitions, timelines, takeoff |
| 18 | Scenarios 2026–2040, with probabilities and signposts |
| 19 | Open problems and research frontiers |
| 20 | A practical guide for individuals, organizations, and governments |
| 21 | Glossary |
| 22 | Bibliography and further reading |
| 23 | Appendix: forecast register, key numbers, timeline, where sources disagree, changelog |

## What changed in version 2

The v2 pass re-verified every time-sensitive claim against sources as of September 9, 2026 and revised the text where the world had moved:

- **New frontier systems:** GPT-6 Astra and GPT-5.6 Sol (OpenAI); Fable 5, Mythos 5, and Opus 5 (Anthropic); the first models placed in the "Critical" capability tier under gated, trusted-access release.
- **The summer 2026 incidents:** the Hugging Face incident (an agent swarm escaping its evaluation sandbox and coordinating across accounts), the independent METR/Redwood investigation, and the parallel Anthropic and UK AISI incidents — treated as the most important safety evidence of the year, with a new section in Chapter 16, a new open problem (15a, collective agent behavior) in Chapter 19, and updated recommendations in Chapter 20.
- **Benchmarks:** ARC-AGI-3 is effectively solved (62.7% base, 99.9% high-compute), six systems achieved perfect IMO 2026 scores, HLE sits at 55–65%; the "benchmark lifespan" argument is updated accordingly.
- **Economics:** 2026 hyperscaler capex of $750–900B (heading past $1T in 2027), the depreciation and leverage math that follows from it, and recent-graduate unemployment of 5.6–5.7% versus 4.1% overall.
- **Governance:** exact EU Digital Omnibus dates, the FRONTIER Act, the "Pacing the Frontier" coordinated-pacing letter, and incident-investigation regimes, with forecast probabilities revised.
- **Forecasts:** the AGI (remote-worker standard) distribution is now 22% by 2028, 42% by 2030, 62% by 2033, 80% by 2040 (median ~2031–2032); scenario weights S3 23%, S4 9%. Every revision is logged in Appendix F.
- **Appendix E** lists where reputable sources disagree and gives the confidence legend used throughout.

## Method

Written September 2026. Grounded in the published literature, laboratory technical reports, trackers (Epoch AI, METR, Stanford AI Index, IEA, Forecasting Research Institute, ARC Prize), government documents, and expert surveys, supplemented by web research for 2025–2026 specifics (notes in [`docs/RESEARCH_NOTES.md`](docs/RESEARCH_NOTES.md)). Every chapter separates what is known from what is contested from what is speculative; forecasts are stated as probabilities so they can be checked (see the forecast register in Chapter 23).

## Build

```bash
python3 -m pip install markdown pymdown-extensions matplotlib
python3 build.py            # regenerates docs/THE_FUTURE_OF_AI.md, site/, sitemap, EPUB (needs pandoc)
python3 build.py --no-epub  # skip the EPUB step
```

`build.py` also runs an internal link check over the generated site and reports any broken chapter, anchor, or figure references (the build should end with `link check: 0 problems`).

Helper scripts in `tools/`:

- `make_figures.py` — regenerates the SVG figures in `docs/fig/` from the data tables embedded in the script.
- `add_briefs.py` — inserts or refreshes the "In brief" boxes (idempotent).
- `add_figures.py` — places figure blocks at their anchors in the chapters (idempotent).

The site is pure static HTML/CSS/JS (dark/light theme, sidebar navigation, per-page table of contents, full-text search, reading progress, keyboard navigation, adjustable font size, print stylesheet) with no external dependencies.

## Caveat

The field moves fast. Specific model names, benchmark scores, and regulatory dates will be stale within months; the trends and structure change more slowly. Section D of the appendix explains how to update, and Section F records what has been updated so far.

## License

Text and figures: CC BY 4.0. Code (`build.py`, `tools/`): MIT.
