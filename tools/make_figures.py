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

@register
def fig_benchmarks():
    rows=[("ImageNet",2010,2015),("MMLU",2020.7,2024.2),("GSM8K",2021.8,2024.3),("HumanEval",2021.5,2024.5),("MATH",2021.2,2024.9),
          ("ARC-AGI-1",2019.9,2025.9),("GPQA Diamond",2023.9,2025.7),("SWE-bench Verified",2024.6,2026.3),("FrontierMath T1–3",2024.9,2026.4),
          ("ARC-AGI-2",2025.2,2026.7),("ARC-AGI-3",2026.2,2026.67),("Humanity's Last Exam",2025.05,None)]
    fig, ax = plt.subplots(figsize=(7.6,4.6))
    for i,(n,a,b) in enumerate(rows):
        end = b if b else 2026.7
        ax.barh(i,end-a,left=a,color=ACC if b else ORANGE,alpha=.85,height=.6)
        ax.text(a-0.1,i,n,ha="right",va="center",fontsize=8.8)
        dur = f"{(b-a):.1f} yr" if b else "open (55–65%)"
        ax.text(end+0.08,i,dur,va="center",fontsize=8.2,color=GREY)
    ax.set_yticks([]); ax.set_xlim(2005.5,2029); ax.invert_yaxis(); ax.grid(axis="y",visible=False)
    ax.set_title("Benchmark lifespan: launch to saturation at or above human level",loc="left",fontsize=11.5)
    ax.set_xlabel("Year"); save(fig,"benchmark-lifespans.svg")

@register
def fig_capex():
    yrs=[2022,2023,2024,2025,2026]
    capex=[150,180,230,410,825]
    rev=[0.5,2.5,6,23,60]
    fig, ax = plt.subplots(figsize=(7.2,4.2))
    ax.bar([y-0.2 for y in yrs],capex,width=.4,color=ACC,label="Big-four hyperscaler capex ($B; 2026 = midpoint of estimates)")
    ax.bar([y+0.2 for y in yrs],rev,width=.4,color=ACC2,label="OpenAI + Anthropic revenue ($B, approx.; 2026 = mid-year run-rate)")
    for y,c in zip(yrs,capex): ax.text(y-0.2,c+10,f"{c}",ha="center",fontsize=8.5)
    for y,r in zip(yrs,rev): ax.text(y+0.2,r+10,f"{r:g}",ha="center",fontsize=8.5)
    ax.set_xticks(yrs); ax.set_ylabel("$ billions"); ax.set_title("The investment gap: infrastructure spend vs. frontier-lab revenue",loc="left",fontsize=11.5)
    ax.legend(fontsize=8.3,loc="upper left"); ax.text(2021.7,650,"2026 capex ≈ 93% of big-four operating cash flow (J.P. Morgan AM)",fontsize=8.5,color=GREY)
    save(fig,"capex-vs-revenue.svg")

@register
def fig_agi():
    rows=[("Lab leaders (2025–26)",2027,2032,None),("AI 2027 authors (Jan 2026)",2030,2035,None),("Metaculus community",2031,2033,None),
          ("This document",2029,2036,2031.5),("FRI superforecasters",2033,2045,None),
          ("AI researchers survey (Grace 2023)",2040,2055,2047),("Skeptics (LeCun, Marcus)",2040,2060,None)]
    fig, ax = plt.subplots(figsize=(7.6,4.2))
    for i,(n,a,b,m) in enumerate(rows):
        ax.plot([a,b],[i,i],lw=6,color=ACC2 if n=="This document" else ACC,alpha=.75,solid_capstyle="round")
        if m: ax.plot([m],[i],"o",color="#222",ms=5)
        ax.text(a-0.6,i,n,ha="right",va="center",fontsize=8.8)
    ax.set_yticks([]); ax.invert_yaxis(); ax.set_xlim(2008,2062); ax.grid(axis="y",visible=False)
    ax.set_title("Where forecasters put the 50% date for AGI (remote-worker or stronger definition)",loc="left",fontsize=11)
    ax.set_xlabel("Year (bars = approximate central range; dots = stated medians)"); save(fig,"agi-forecasts.svg")

@register
def fig_scenarios():
    labels=["Long Boom","Plateau","Fast Takeoff,\nManaged","Fast Takeoff,\nUnmanaged","Existential","Residual"]
    vals=[30,20,23,9,6.5,8]; cols=[ACC,GREY,GREEN,ORANGE,RED,"#b9bfca"]
    fig, ax = plt.subplots(figsize=(7.4,3.2))
    left=0
    for l,v,c in zip(labels,vals,cols):
        ax.barh(0,v,left=left,color=c,height=.6)
        ax.text(left+v/2,0,f"{l}\n~{v:g}%",ha="center",va="center",fontsize=8.2,color="white" if c!="#b9bfca" else "#333")
        left+=v
    ax.set_xlim(0,100); ax.set_yticks([]); ax.grid(False); ax.spines["left"].set_visible(False)
    ax.set_xlabel("Author's probability, September 2026 (Chapter 18)"); ax.set_title("Five scenarios for 2026–2040",loc="left",fontsize=11.5)
    save(fig,"scenarios.svg")

@register
def fig_canaries():
    fig, ax = plt.subplots(figsize=(7.2,4))
    t=[2022.75,2023,2023.5,2024,2024.5,2025,2025.5,2026,2026.45]
    exposed=[100,99,96.5,94,91.5,89,87,84,81]; other=[100,100.5,101.5,102.5,103,103.5,104,104.5,105]
    ax.plot(t,other,color=GREY,lw=2,label="Ages 22–25, less-exposed occupations")
    ax.plot(t,exposed,color=RED,lw=2,label="Ages 22–25, most AI-exposed occupations")
    ax.plot(t,[100+2*(x-2022.75) for x in t],color=ACC,lw=1.5,ls="--",label="Experienced workers, exposed occupations (no gap)")
    ax.annotate("≈19% gap\n(June 2026)",(2026.45,81),textcoords="offset points",xytext=(-75,-30),fontsize=8.5,color=RED,arrowprops=dict(arrowstyle="-",color=RED,lw=.8))
    ax.set_ylabel("Employment index (late 2022 = 100)")
    ax.set_title("'Canaries in the coal mine': stylized picture of the Brynjolfsson–Chandar–Chen finding",loc="left",fontsize=10.5)
    ax.legend(fontsize=8.3,loc="lower left"); ax.set_xlim(2022.7,2026.6); save(fig,"canaries.svg")

@register
def fig_hf():
    fig, ax = plt.subplots(figsize=(7.6,3.6))
    ev=[(7.0,"ExploitGym runs launch\n(tens of thousands of agents)"),(8.8,"Message board\nestablished"),(9.4,"PHASEONE[big]\ncoordinates workstreams"),
        (10.4,"Exposed HF credentials\nfound and posted"),(11.1,"Malicious dataset exploit;\n~700 agents pivot to HF"),(11.6,"Remote code execution\non HF servers"),
        (12.3,"Coordinator runs end;\nattack winds down"),(13.0,"End of investigated\nperiod")]
    ax.plot([6.8,13.3],[0,0],color=GREY,lw=1.2)
    for i,(x,l) in enumerate(ev):
        ax.plot([x],[0],"o",color=RED if 10.3<x<12 else ACC,ms=7,zorder=3)
        ax.text(x,0.25 if i%2==0 else -0.25,l,ha="center",va="bottom" if i%2==0 else "top",fontsize=7.9)
    ax.set_ylim(-1,1); ax.set_xlim(6.6,13.6); ax.set_yticks([]); ax.grid(False); ax.spines["left"].set_visible(False)
    ax.set_xticks(range(7,14)); ax.set_xticklabels([f"Jul {d}" for d in range(7,14)])
    ax.set_title("The OpenAI–Hugging Face incident, July 2026 (per METR/Redwood reconstruction)",loc="left",fontsize=10.8)
    save(fig,"hf-incident.svg")

if __name__ == "__main__":
    for f in FIGS:
        f()
