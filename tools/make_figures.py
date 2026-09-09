#!/usr/bin/env python3
"""Generate SVG figures for the review into docs/fig/ (build.py copies them to site/fig/).
Data points are the ones cited in the chapters (Epoch, METR, ARC Prize, company reports, author estimates).
Run: python3 tools/make_figures.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "fig")
os.makedirs(OUT, exist_ok=True)

ACC = "#3b6fd6"; ACC2 = "#8b5cf6"; GREY = "#7a8494"; RED = "#d05a5a"; GREEN = "#3fa876"; ORANGE = "#e0a040"
TXT = "#5b6473"
rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10.5,
    "axes.edgecolor": GREY, "axes.labelcolor": TXT, "xtick.color": TXT, "ytick.color": TXT, "text.color": TXT,
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.color": "#aeb6c4",
    "grid.linewidth": 0.5, "grid.alpha": 0.6, "figure.facecolor": "none", "axes.facecolor": "none",
    "savefig.facecolor": "none", "savefig.transparent": True, "legend.frameon": False,
})

def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), format="svg", bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)

FIGS = []
def register(f):
    FIGS.append(f); return f

@register
def fig_compute():
    pts = [(2012.8,"AlexNet",4.7e17),(2017.5,"Transformer",7.4e18),(2019.1,"GPT-2",1.5e21),(2020.4,"GPT-3",3.1e23),
           (2022.3,"PaLM",2.5e24),(2023.2,"GPT-4",2.1e25),(2024.5,"Llama 3.1 405B",3.8e25),(2025.1,"Grok 3",4.6e26),
           (2025.6,"GPT-5 (est.)",8e26),(2026.5,"Largest 2026 (est.)",2e27)]
    fig, ax = plt.subplots(figsize=(7.6,4.4))
    ax.set_yscale("log")
    tx=[2020,2030]; ty=[3.1e23*5**(t-2020.4) for t in tx]
    ax.plot(tx,ty,"--",color=GREY,lw=1,label="≈5×/year trend (Epoch, frontier LMs since 2020)")
    ax.scatter([p[0] for p in pts],[p[2] for p in pts],color=ACC,zorder=3,s=34)
    for x,l,y in pts:
        ax.annotate(l,(x,y),textcoords="offset points",xytext=(5,-3),fontsize=8.2)
    ax.axhspan(1e29,4e29,color=ORANGE,alpha=.15); ax.text(2012.6,1.3e29,"~10²⁹ FLOP: feasible by 2030 (Epoch)",fontsize=8.5,color=ORANGE)
    ax.set_xlim(2012,2030.5); ax.set_ylim(1e17,1e30)
    ax.set_ylabel("Training compute (FLOP)"); ax.set_title("Frontier training compute, 2012–2026, with extrapolation",loc="left",fontsize=11.5)
    ax.legend(loc="lower right",fontsize=8.5)
    save(fig,"compute-trend.svg")

@register
def fig_metr():
    pts=[(2019.1,"GPT-2",0.05),(2020.4,"GPT-3",0.15),(2022.9,"GPT-3.5",0.6),(2023.2,"GPT-4",3.5),(2024.4,"GPT-4o",9),
         (2024.7,"o1-preview",22),(2025.1,"Claude 3.7",60),(2025.3,"o3",121),(2025.6,"GPT-5",214),(2025.9,"Opus 4.5",320),(2026.35,"Spring-2026 frontier (>16 h)",1000)]
    fig, ax = plt.subplots(figsize=(7.6,4.4)); ax.set_yscale("log")
    xs=[p[0] for p in pts]; ys=[p[2] for p in pts]
    ax.scatter(xs[:-1],ys[:-1],color=ACC,s=34,zorder=3); ax.scatter([xs[-1]],[ys[-1]],color=ACC,s=40,zorder=3,marker="^")
    for x,l,y in pts: ax.annotate(l,(x,y),textcoords="offset points",xytext=(6,-3),fontsize=8.2)
    t=[2019,2027.5]
    ax.plot(t,[0.05*2**((tt-2019.1)*12/7) for tt in t],"--",color=GREY,lw=1,label="7-month doubling (2019–25 fit)")
    ax.plot([2024,2027.5],[9*2**((tt-2024.4)*12/4) for tt in [2024,2027.5]],":",color=ACC2,lw=1.3,label="4-month doubling (since 2024)")
    ax.axhspan(960,1e5,color=RED,alpha=.08); ax.text(2019.2,1300,"METR: measurements above 16 h unreliable with current suite",fontsize=8.3,color=RED)
    for y,l in [(60,"1 hour"),(480,"1 work day"),(2400,"1 work week"),(9600,"1 work month")]:
        ax.axhline(y,color="#aeb6c4",lw=.6); ax.text(2027.55,y,l,fontsize=7.8,color=GREY,va="center")
    ax.set_xlim(2018.8,2028.6); ax.set_ylim(0.03,3e4)
    ax.set_ylabel("50%-success task length (minutes of human time)")
    ax.set_title("METR time horizon of frontier agents",loc="left",fontsize=11.5); ax.legend(loc="lower right",fontsize=8.5)
    save(fig,"metr-horizon.svg")

@register
def fig_cost():
    pts=[(2023.2,"GPT-4 launch",45),(2023.9,"GPT-4 Turbo",15),(2024.4,"GPT-4o",7.5),(2024.6,"Llama 3.1 70B (hosted)",0.9),
         (2025.0,"DeepSeek V3",0.5),(2025.5,"small-model class",0.6),(2026.3,"2026 open/small models",0.3)]
    fig, ax = plt.subplots(figsize=(7.2,4.2)); ax.set_yscale("log")
    ax.plot([p[0] for p in pts],[p[2] for p in pts],"-o",color=ACC,ms=5)
    for x,l,y in pts: ax.annotate(l,(x,y),textcoords="offset points",xytext=(6,4),fontsize=8.2)
    ax.plot([2023.2,2026.3],[45,45/10**3.1],"--",color=GREY,lw=1,label="≈10×/year decline")
    ax.set_ylim(0.1,100); ax.set_xlim(2023,2026.9)
    ax.set_ylabel("Blended $ per million tokens"); ax.set_title("Price of GPT-4-class capability, 2023–2026 (approx.)",loc="left",fontsize=11.5)
    ax.legend(fontsize=8.5); save(fig,"inference-cost.svg")

if __name__ == "__main__":
    for f in FIGS:
        f()
