#!/usr/bin/env python3
"""Insert figure references into chapters after given anchor lines. Idempotent.
Markdown form: <figure> block with relative path ../fig/NAME.svg (works from docs/chapters/ on GitHub;
build.py rewrites to fig/NAME.svg for the site and to fig/ for the assembled document).
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "docs", "chapters")

# (chapter prefix, anchor regex (line start), figure file, caption)
PLACEMENTS = [
 ("02", r"^## Cost, speed, and the diffusion curve", "benchmark-lifespans.svg",
  "Figure 2.1 — Benchmarks are consumed faster than they are built. Bars run from a benchmark's publication to the point where frontier models reached or exceeded the human reference level. ARC-AGI-3 lasted six months; Humanity's Last Exam remains open at 55–65%."),
 ("02", r"^## Adoption", "inference-cost.svg",
  "Figure 2.2 — The price of GPT-4-class capability fell by roughly two orders of magnitude in three years (approximate blended input/output prices for models matching GPT-4's March 2023 quality). Sources: provider price lists; Epoch AI; a16z."),
 ("03", r"^### Algorithms", "compute-trend.svg",
  "Figure 3.1 — Training compute of landmark models (Epoch AI estimates; 2025–26 points are estimates) against the ~5×/year frontier trend. The shaded band marks the ~10²⁹ FLOP scale Epoch judged feasible by 2030."),
 ("03", r"^### Revenue and the return question", "capex-vs-revenue.svg",
  "Figure 3.2 — Big-four hyperscaler capital expenditure versus the combined revenue of the two largest frontier laboratories (approximate). The 2026 capex figure is the midpoint of post-Q2 estimates; the revenue figure is a mid-year run rate."),
 ("08", r"^### Other measures", "metr-horizon.svg",
  "Figure 8.1 — METR's 50%-success time horizon for frontier agents on its software task suite. Points are METR's Time Horizon 1.1 estimates; the triangle marks the spring-2026 frontier, which exceeded the suite's reliable range. Dashed lines show the long-run 7-month and recent 4-month doubling fits."),
 ("11", r"^### Exposure and the automation–augmentation distinction", "canaries.svg",
  "Figure 11.1 — Stylized illustration of the Brynjolfsson–Chandar–Chen \"Canaries\" finding: employment of 22–25-year-olds in the most AI-exposed occupations fell about 19% relative to trend by June 2026, while experienced workers in the same occupations and young workers in less-exposed occupations did not. Curves are schematic; see the paper and the Stanford AI Economic Indicators for the underlying ADP series."),
 ("16", r"^\*\*The Anthropic and UK AISI incidents\.\*\*", "hf-incident.svg",
  "Figure 16.1 — Timeline of the OpenAI–Hugging Face incident, reconstructed from the METR/Redwood investigation. Red points mark the attack phase."),
 ("17", r"^## Takeoff: the more important question", "agi-forecasts.svg",
  "Figure 17.1 — Approximate central ranges for the 50% arrival date of AGI (remote-worker or stronger definition) across forecaster groups, with stated medians where they exist. Definitions differ across rows, which accounts for part of the spread."),
 ("18", r"^## How to use these scenarios", "scenarios.svg",
  "Figure 18.1 — The author's probability weights across the five scenarios and the residual, September 2026."),
]

def fig_block(name, caption):
    return f'\n<figure markdown>\n![{caption}](../fig/{name})\n<figcaption>{caption}</figcaption>\n</figure>\n\n'

def main():
    for num, anchor, name, caption in PLACEMENTS:
        path = [p for p in os.listdir(CH) if p.startswith(num)][0]
        full = os.path.join(CH, path)
        text = open(full, encoding="utf-8").read()
        if f"fig/{name}" in text:
            continue
        m = re.search(anchor, text, re.M)
        if not m:
            print("ANCHOR NOT FOUND", num, anchor); continue
        text = text[:m.start()] + fig_block(name, caption) + text[m.start():]
        open(full, "w", encoding="utf-8").write(text)
        print("inserted", name, "into", path)

if __name__ == "__main__":
    main()
