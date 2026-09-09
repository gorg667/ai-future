#!/usr/bin/env python3
"""
Build script for "The Future of AI" review.

- Reads docs/chapters/NN-slug.md (sorted).
- Writes docs/THE_FUTURE_OF_AI.md (assembled single document with TOC).
- Writes site/index.html + site/NN-slug.html (static website) and copies index to repo root
  so GitHub Pages "deploy from main / root" works (root index.html redirects to site/).

Usage: python3 build.py
Requires: pip install markdown pymdown-extensions
"""
import os, re, json, html, glob, datetime, shutil, sys
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
CH_DIR = os.path.join(ROOT, "docs", "chapters")
FIG_DIR = os.path.join(ROOT, "docs", "fig")
SITE = os.path.join(ROOT, "site")
os.makedirs(SITE, exist_ok=True)

TITLE = "The Future of AI"
SUBTITLE = "A comprehensive review and guide — technology, economics, society, geopolitics, safety, and what comes next"
BUILD_DATE = datetime.date(2026, 9, 9).isoformat()
VERSION = "2.0"
REPO_URL = "https://github.com/gorg667/ai-future"
SITE_URL = "https://gorg667.github.io/ai-future/site/"
FAVICON = ("data:image/svg+xml," + "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%230f1115'/%3E%3Ccircle cx='32' cy='32' r='16' fill='none' stroke='%236ea8fe' stroke-width='5'/%3E"
           "%3Ccircle cx='32' cy='32' r='5' fill='%23b388ff'/%3E%3C/svg%3E")

MD_EXT = [
    "extra", "toc", "tables", "sane_lists", "admonition", "attr_list", "md_in_html",
    "pymdownx.superfences", "pymdownx.details", "pymdownx.tilde", "pymdownx.betterem",
    "pymdownx.tasklist", "footnotes",
]
MD_CFG = {"toc": {"permalink": "¶", "toc_depth": "2-3"}}


def read_chapters():
    files = sorted(glob.glob(os.path.join(CH_DIR, "*.md")))
    chapters = []
    for f in files:
        base = os.path.basename(f)
        m = re.match(r"(\d+)-(.+)\.md$", base)
        if not m:
            continue
        num, slug = m.group(1), m.group(2)
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        title_m = re.search(r"^#\s+(.+)$", text, re.M)
        title = title_m.group(1).strip() if title_m else slug.replace("-", " ").title()
        words = len(re.findall(r"\w+", text))
        chapters.append(dict(num=num, slug=slug, title=title, text=text, words=words,
                             html_name=f"{num}-{slug}.html"))
    return chapters


def strip_title(text):
    return re.sub(r"^#\s+.+\n", "", text, count=1)


def md_for_assembled(text):
    """Chapter files reference figures as ../fig/X (relative to docs/chapters/). The assembled file lives in docs/."""
    return text.replace("](../fig/", "](fig/")


def build_markdown(chapters):
    out = [f"# {TITLE}\n", f"### {SUBTITLE}\n", f"*Version {VERSION}, built {BUILD_DATE}. "
           f"Total length: {sum(c['words'] for c in chapters):,} words across {len(chapters)} chapters. "
           f"Source and updates: {REPO_URL}*\n",
           "\n---\n", "## Table of contents\n"]
    for c in chapters:
        anchor = re.sub(r"[^a-z0-9]+", "-", c["title"].lower()).strip("-")
        out.append(f"- [{c['title']}](#{anchor}) *({c['words']:,} words)*")
    out.append("\n---\n")
    for c in chapters:
        out.append(md_for_assembled(c["text"]).rstrip() + "\n\n---\n")
    path = os.path.join(ROOT, "docs", "THE_FUTURE_OF_AI.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    return path


CSS = r"""
:root{--bg:#0f1115;--bg2:#161a22;--fg:#e6e8ee;--muted:#9aa3b2;--acc:#6ea8fe;--acc2:#b388ff;--border:#262c38;--code:#1c2230;--mark:#3b3a1a}
[data-theme=light]{--bg:#fbfbfd;--bg2:#ffffff;--fg:#1c1e26;--muted:#5b6473;--acc:#2457c5;--acc2:#6d3fd0;--border:#e3e6ec;--code:#f2f4f8;--mark:#fff3b0}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--fg);line-height:1.7;font-size:17px}
a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline}
#progress{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--acc),var(--acc2));width:0;z-index:99}
.layout{display:grid;grid-template-columns:300px minmax(0,1fr) 240px;min-height:100vh}
nav.side{position:sticky;top:0;height:100vh;overflow-y:auto;border-right:1px solid var(--border);background:var(--bg2);padding:18px 14px}
nav.side .brand{font-weight:800;font-size:18px;margin-bottom:6px;display:block;color:var(--fg)}
nav.side .sub{font-size:12px;color:var(--muted);margin-bottom:14px}
nav.side input{width:100%;padding:8px 10px;border-radius:8px;border:1px solid var(--border);background:var(--bg);color:var(--fg);margin-bottom:12px}
nav.side ol{list-style:none;padding:0;margin:0}
nav.side li a{display:block;padding:6px 8px;border-radius:6px;font-size:14px;color:var(--fg)}
nav.side li a:hover{background:var(--code);text-decoration:none}
nav.side li a.active{background:var(--code);color:var(--acc);font-weight:600}
nav.side li a small{color:var(--muted);display:block;font-size:11px}
main{padding:36px 56px 100px;max-width:900px;width:100%;margin:0 auto}
aside.toc{position:sticky;top:0;height:100vh;overflow-y:auto;padding:24px 14px;border-left:1px solid var(--border);font-size:13px}
aside.toc .toc ul{list-style:none;padding-left:10px;margin:0}
aside.toc .toc>ul{padding-left:0}
aside.toc a{color:var(--muted);display:block;padding:3px 0}
aside.toc a:hover{color:var(--acc)}
h1{font-size:2.2rem;line-height:1.2;margin:.2em 0 .6em}h2{font-size:1.6rem;margin-top:2.2em;border-bottom:1px solid var(--border);padding-bottom:.3em}h3{font-size:1.25rem;margin-top:1.8em}h4{font-size:1.05rem;margin-top:1.4em}
.headerlink{opacity:0;margin-left:6px;font-size:.8em}h2:hover .headerlink,h3:hover .headerlink{opacity:.6}
p,li{max-width:76ch}
blockquote{margin:1.2em 0;padding:.6em 1.2em;border-left:4px solid var(--acc2);background:var(--code);border-radius:6px;color:var(--fg)}
table{border-collapse:collapse;width:100%;margin:1.4em 0;font-size:.92em;display:block;overflow-x:auto}
th,td{border:1px solid var(--border);padding:8px 10px;text-align:left;vertical-align:top}th{background:var(--code)}
code{background:var(--code);padding:2px 5px;border-radius:4px;font-size:.9em}pre{background:var(--code);padding:14px;border-radius:8px;overflow-x:auto}pre code{background:none;padding:0}
.admonition{padding:12px 16px;border-radius:8px;border:1px solid var(--border);background:var(--code);margin:1.3em 0}
.admonition-title{font-weight:700;margin:0 0 6px}
.admonition.warning{border-color:#d9a54a}.admonition.note{border-color:var(--acc)}.admonition.tip{border-color:#4fbf8b}.admonition.danger{border-color:#e05a5a}
.meta{color:var(--muted);font-size:14px;margin-bottom:24px}
.pager{display:flex;justify-content:space-between;gap:12px;margin-top:60px;padding-top:20px;border-top:1px solid var(--border)}
.pager a{padding:10px 14px;border:1px solid var(--border);border-radius:8px;flex:1}
.pager a span{display:block;color:var(--muted);font-size:12px}
.topbar{display:none}
button.theme{border:1px solid var(--border);background:var(--bg);color:var(--fg);border-radius:8px;padding:6px 10px;cursor:pointer;font-size:13px}
.hero{padding:30px 0 10px}.hero h1{font-size:3rem}.hero p.lead{font-size:1.25rem;color:var(--muted);max-width:70ch}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin:26px 0}
.card{border:1px solid var(--border);border-radius:12px;padding:16px;background:var(--bg2);display:block;color:var(--fg)}
.card:hover{border-color:var(--acc);text-decoration:none}.card .n{color:var(--acc);font-weight:700;font-size:12px}.card h3{margin:.3em 0 .4em;font-size:1.05rem}.card small{color:var(--muted)}
mark{background:var(--mark);color:inherit}
footer{color:var(--muted);font-size:13px;margin-top:40px}
@media(max-width:1200px){.layout{grid-template-columns:280px minmax(0,1fr)}aside.toc{display:none}}
@media(max-width:860px){.layout{grid-template-columns:1fr}nav.side{position:fixed;left:-320px;width:300px;transition:left .2s;z-index:50}nav.side.open{left:0}.topbar{display:flex;align-items:center;gap:10px;padding:10px 14px;border-bottom:1px solid var(--border);position:sticky;top:0;background:var(--bg2);z-index:40}main{padding:20px 18px 80px}body{font-size:16px}}
"""

JS = r"""
(function(){
  const t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);
  window.toggleTheme=function(){const cur=document.documentElement.getAttribute('data-theme')==='light'?'dark':'light';document.documentElement.setAttribute('data-theme',cur);localStorage.setItem('theme',cur);};
  window.toggleNav=function(){document.querySelector('nav.side').classList.toggle('open');};
  window.addEventListener('scroll',()=>{const h=document.documentElement;const p=h.scrollTop/(h.scrollHeight-h.clientHeight)*100;document.getElementById('progress').style.width=p+'%';});
  // sidebar filter + full-text search over search index
  const inp=document.getElementById('q');const list=document.getElementById('chlist');const res=document.getElementById('results');
  let idx=null;
  async function loadIdx(){if(idx)return idx;try{const r=await fetch(window.SITE_BASE+'search.json');idx=await r.json();}catch(e){idx=[];}return idx;}
  if(inp){inp.addEventListener('input',async()=>{const q=inp.value.trim().toLowerCase();
    [...list.querySelectorAll('li')].forEach(li=>{li.style.display=(!q||li.textContent.toLowerCase().includes(q))?'':'none';});
    if(q.length<3){res.innerHTML='';return;}
    const ix=await loadIdx();const out=[];
    for(const d of ix){const i=d.text.toLowerCase().indexOf(q);if(i>=0){const s=Math.max(0,i-60);out.push({d,snip:d.text.slice(s,i+90)});if(out.length>=25)break;}}
    res.innerHTML=out.map(o=>`<li><a href="${window.SITE_BASE}${o.d.url}"><b>${o.d.title}</b><small>…${o.snip.replace(/</g,'&lt;')}…</small></a></li>`).join('')||'<li><small>No matches</small></li>';
  });}
  // active TOC highlight
  const heads=[...document.querySelectorAll('main h2, main h3')];const links=[...document.querySelectorAll('aside.toc a')];
  if(heads.length&&links.length){const obs=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){links.forEach(l=>l.style.color='');const l=links.find(l=>l.getAttribute('href')==='#'+e.target.id);if(l)l.style.color='var(--acc)';}})},{rootMargin:'0px 0px -75% 0px'});heads.forEach(h=>obs.observe(h));}
})();
"""


def page(chapters, title, body_html, toc_html="", active=None, prev=None, nxt=None, base="", meta=""):
    nav_items = "".join(
        f'<li><a href="{base}{c["html_name"]}" class="{"active" if active == c["num"] else ""}">'
        f'{html.escape(c["title"])}<small>Chapter {int(c["num"])} · {c["words"]:,} words</small></a></li>'
        for c in chapters)
    pager = ""
    if prev or nxt:
        pager = '<div class="pager">'
        pager += (f'<a href="{base}{prev["html_name"]}"><span>← Previous</span>{html.escape(prev["title"])}</a>' if prev else '<a href="index.html"><span>←</span>Home</a>')
        pager += (f'<a href="{base}{nxt["html_name"]}" style="text-align:right"><span>Next →</span>{html.escape(nxt["title"])}</a>' if nxt else '<a href="index.html" style="text-align:right"><span>→</span>Home</a>')
        pager += "</div>"
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — {TITLE}</title>
<meta name="description" content="{html.escape(SUBTITLE)}">
<style>{CSS}</style>
<script>window.SITE_BASE="{base}";</script>
</head><body><div id="progress"></div>
<div class="topbar"><button class="theme" onclick="toggleNav()">☰ Chapters</button><b>{TITLE}</b><span style="flex:1"></span><button class="theme" onclick="toggleTheme()">◐</button></div>
<div class="layout">
<nav class="side"><a class="brand" href="{base}index.html">{TITLE}</a><div class="sub">Comprehensive review · built {BUILD_DATE}</div>
<input id="q" placeholder="Search all chapters…" autocomplete="off"><ol id="results"></ol><ol id="chlist">{nav_items}</ol>
<div style="margin-top:14px"><button class="theme" onclick="toggleTheme()">◐ Toggle theme</button></div>
<div class="sub" style="margin-top:14px"><a href="{base}../docs/THE_FUTURE_OF_AI.md">Single Markdown file</a> · <a href="https://github.com/gorg667/ai-future">GitHub</a></div></nav>
<main>{meta}{body_html}{pager}<footer>Built {BUILD_DATE}. Text is provided as an analytical review; forecasts are uncertain by nature. </footer></main>
<aside class="toc">{toc_html}</aside>
</div><script>{JS}</script></body></html>"""


def build_site(chapters):
    search = []
    for i, c in enumerate(chapters):
        md = markdown.Markdown(extensions=MD_EXT, extension_configs=MD_CFG)
        body = md.convert(c["text"])
        toc = md.toc if hasattr(md, "toc") else ""
        prev = chapters[i - 1] if i > 0 else None
        nxt = chapters[i + 1] if i + 1 < len(chapters) else None
        meta = f'<div class="meta">Chapter {int(c["num"])} of {len(chapters)} · {c["words"]:,} words · ~{max(1, c["words"] // 230)} min read</div>'
        with open(os.path.join(SITE, c["html_name"]), "w", encoding="utf-8") as fh:
            fh.write(page(chapters, c["title"], body, f'<div class="sub" style="font-size:12px;color:var(--muted);margin-bottom:8px">On this page</div>{toc}', c["num"], prev, nxt, "", meta))
        plain = re.sub(r"<[^>]+>", " ", body)
        plain = html.unescape(re.sub(r"\s+", " ", plain))
        search.append({"title": c["title"], "url": c["html_name"], "text": plain})
    with open(os.path.join(SITE, "search.json"), "w", encoding="utf-8") as fh:
        json.dump(search, fh)
    # index
    total = sum(c["words"] for c in chapters)
    cards = "".join(
        f'<a class="card" href="{c["html_name"]}"><div class="n">CHAPTER {int(c["num"])}</div><h3>{html.escape(c["title"])}</h3><small>{c["words"]:,} words · ~{max(1, c["words"] // 230)} min</small></a>'
        for c in chapters)
    hero = f"""<div class="hero"><h1>{TITLE}</h1><p class="lead">{html.escape(SUBTITLE)}.</p>
<p class="meta">{len(chapters)} chapters · {total:,} words · roughly {total // 230 // 60}h {total // 230 % 60}m of reading · built {BUILD_DATE}</p>
<p>This is a long-form, structured review of where artificial intelligence stands, where it is heading, and what that means for technology, economies, institutions, and individuals. It is written to be read linearly or consulted chapter by chapter. Each chapter states what is known, what is contested, and what to watch for. Forecasts are given with explicit uncertainty.</p>
<p><a href="../docs/THE_FUTURE_OF_AI.md">Download / read the single Markdown document →</a></p></div>
<h2>Chapters</h2><div class="cards">{cards}</div>"""
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page(chapters, "Home", hero, "", None, None, None, ""))
    # root redirect for GitHub Pages
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=site/index.html"><a href="site/index.html">Open the review</a>')
    with open(os.path.join(ROOT, ".nojekyll"), "w") as fh:
        fh.write("")


if __name__ == "__main__":
    chs = read_chapters()
    p = build_markdown(chs)
    build_site(chs)
    print(f"Built {len(chs)} chapters, {sum(c['words'] for c in chs):,} words -> {p} and site/")
