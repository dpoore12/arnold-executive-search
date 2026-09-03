#!/usr/bin/env python3
"""Assemble the deployable static site for arnoldsearch.com from the hub prototypes."""
import re, os, shutil, html
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "dist"
DOMAIN = "https://arnoldsearch.com"

HUBS = [
    ("legal-recruiters", "TEMPLATE_REFERENCE_legal_recruiters.html"),
    ("executive-search-firms", "arnold_executive-search-firms.html"),
    ("it-staffing", "arnold_it-staffing.html"),
    ("accounting-staffing", "arnold_accounting-staffing.html"),
    ("healthcare-staffing", "arnold_healthcare-staffing.html"),
    ("sales-recruiters", "arnold_sales-recruiters.html"),
    ("marketing-recruiters", "arnold_marketing-recruiters.html"),
    ("executive-headhunters", "arnold_executive-headhunters.html"),
    ("retained-executive-search", "arnold_retained-executive-search.html"),
    ("construction-staffing", "arnold_construction-staffing.html"),
]

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

# Brand-consistent headshot placeholder until the real photo is supplied.
PHOTO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
<rect width="200" height="200" fill="#14213d"/>
<circle cx="100" cy="100" r="72" fill="none" stroke="#c9924a" stroke-width="3"/>
<text x="100" y="118" text-anchor="middle" font-family="Georgia, 'DM Serif Display', serif" font-size="58" fill="#c9924a">GA</text>
</svg>"""
(OUT / "gaea_arnold.svg").write_text(PHOTO_SVG)

hub_meta = []

for slug, fname in HUBS:
    s = (ROOT / fname).read_text()
    title = re.search(r"<title>(.*?) — Arnold Executive Search</title>", s).group(1)
    subhead = re.search(r'<p class="subhead">(.*?)</p>', s, re.S).group(1).strip()
    hub_meta.append((slug, title, subhead))

    # Head: description + canonical
    desc = html.escape(re.sub(r"<[^>]+>", "", subhead), quote=True)
    s = s.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'<meta name="description" content="{desc}">\n'
        f'<link rel="canonical" href="{DOMAIN}/{slug}/">',
    )

    # Photo
    s = re.sub(r'src="(PHOTO_PLACEHOLDER_)?gaea_arnold\.jpg"', 'src="/gaea_arnold.svg"', s)

    # Top nav + breadcrumb
    s = s.replace('<a href="#">Practice Areas</a>', '<a href="/#practice-areas">Practice Areas</a>')
    s = s.replace('<a href="#">About Gaea</a>', '<a href="/#about">About Gaea</a>')
    s = s.replace('<a href="#">Contact</a>', '<a href="#contact">Contact</a>')
    s = s.replace('<a href="#">Home</a>', '<a href="/">Home</a>')
    s = s.replace('<div class="brand"><span class="monogram">GA</span>Arnold Executive Search</div>',
                  '<a class="brand" href="/" style="border-bottom:none"><span class="monogram">GA</span>Arnold Executive Search</a>')

    # CTA band anchor + button
    s = s.replace('<div class="cta-band">', '<div class="cta-band" id="contact">')
    s = s.replace('<a href="#" class="cta-button">', '<a href="#contact" class="cta-button">')

    # Remaining "#" links (city / related-decision spokes not yet built) -> contact band
    s = s.replace('href="#"', 'href="#contact"')

    # Strip the internal draft note meant for Dan (not public copy)
    s = re.sub(r'\s*<div class="flag-note">\s*<strong>Draft note for Dan:</strong>.*?</div>', "", s, count=1, flags=re.S)

    d = OUT / slug
    d.mkdir()
    (d / "index.html").write_text(s)

# ---- Homepage: reuse the template's <head>/<style> so the look is identical ----
tpl = (ROOT / "TEMPLATE_REFERENCE_legal_recruiters.html").read_text()
head = tpl[: tpl.find("</head>")]
head = head.replace("<title>Legal Recruiters — Arnold Executive Search</title>",
                    "<title>Arnold Executive Search — Contingent Executive Search &amp; Specialized Recruiting</title>")
head = head.replace(
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    '<meta name="description" content="Arnold Executive Search — Gaea Arnold runs confidential, contingent executive search and specialized recruiting across legal, IT, sales, marketing, healthcare, accounting, and construction. No up-front retainer, twelve-month guarantee.">\n'
    f'<link rel="canonical" href="{DOMAIN}/">',
)
head = head.replace("</style>", """
  .hub-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 16px; margin-top: 18px; }
  .hub-card { display: block; background: #fff; border: 1px solid var(--rule); border-radius: 4px; padding: 20px 22px; border-bottom: 1px solid var(--rule); }
  .hub-card:hover { border-color: var(--bronze-light); }
  .hub-card h3 { margin: 0 0 8px; font-size: 21px; }
  .hub-card p { margin: 0; font-size: 15px; color: var(--ink-soft); line-height: 1.5; }
  .hub-card .go { display: block; margin-top: 12px; font-size: 14px; color: var(--bronze); }
</style>""")

cards = "\n".join(
    f'      <a class="hub-card" href="/{slug}/"><h3>{title}</h3><p>{re.sub(r"<[^>]+>", "", sub)}</p><span class="go">View practice →</span></a>'
    for slug, title, sub in hub_meta
)

home = f"""{head}</head>
<body>

<div class="topbar">
  <a class="brand" href="/" style="border-bottom:none"><span class="monogram">GA</span>Arnold Executive Search</a>
  <div class="topnav">
    <a href="#practice-areas">Practice Areas</a>
    <a href="#about">About Gaea</a>
    <a href="#contact">Contact</a>
  </div>
</div>

<div class="hero">
  <h1>Executive search that moves in weeks, not quarters</h1>
  <p class="subhead">Confidential, contingent executive search and specialized recruiting for companies that cannot afford a slow, generalist hiring process.</p>
  <div class="direct-answer">
    I run exclusive contingent searches at retained-search execution standards — direct, discreet outreach to leaders who are not job-searching, across legal, technology, sales, marketing, healthcare, finance, and construction. Contingent-first, no up-front retainer, twelve-month guarantee.
  </div>
  <div class="badges">
    <span class="badge">Contingent-First</span>
    <span class="badge">No Up-Front Retainer</span>
    <span class="badge">12-Month Guarantee</span>
  </div>
  <div class="author-strip">
    <img class="author-photo" src="/gaea_arnold.svg" alt="Gaea Arnold">
    <div>
      <div class="author-name">Gaea Arnold</div>
      <div class="author-title">Executive Search Leader &amp; Founder, Arnold Executive Search</div>
    </div>
  </div>
</div>

<main>

  <section id="practice-areas">
    <h2>Practice areas</h2>
    <p>Every search runs the same way: a direct brief, confidential outreach to the people actually worth pursuing, and a shortlist you can act on. Choose the practice closest to the seat you are trying to fill.</p>
    <div class="hub-grid">
{cards}
    </div>
  </section>

  <section id="about">
    <h2>About Gaea Arnold</h2>
    <p>Gaea Arnold is the Executive Search Leader and Founder of Arnold Executive Search. She personally runs every search on this site — no hand-off to a junior researcher after the intake call.</p>
    <p>[PLACEHOLDER — verified bio: years in search, in-house talent leadership background, sector focus, and notable engagements to be added once confirmed.]</p>
  </section>

  <section>
    <h2>How the engagement works</h2>
    <div class="compete-block">
      <p><span class="label">Heidrick &amp; Struggles / Korn Ferry / Spencer Stuart</span> — Fortune 500 fee bands, retained engagements, and multi-month timelines. The right lane for a global CEO search. Not the right lane for a company that needs a contingent-first search moving in weeks.</p>
    </div>
    <p>No up-front retainer, no multi-month intake process, and a twelve-month replacement guarantee on every placement. You pay when the hire starts.</p>
  </section>

</main>

<div class="cta-band" id="contact">
  <h2>Let's talk about the seat you're trying to fill</h2>
  <p>30 minutes. No pitch deck, no retainer discussion — just the actual brief and whether this is a fit.</p>
  <a href="#contact" class="cta-button">Schedule a 30-Minute Call</a>
  <div class="cta-contact">[PLACEHOLDER email] &nbsp;·&nbsp; [PLACEHOLDER phone]</div>
</div>

<footer>Arnold Executive Search — Gaea Arnold, Executive Search Leader &amp; Founder</footer>

</body>
</html>
"""
(OUT / "index.html").write_text(home)

# 404 -> homepage look
(OUT / "404.html").write_text(home.replace("<h1>Executive search that moves in weeks, not quarters</h1>",
                                           "<h1>Page not found</h1>").replace('<link rel="canonical" href="https://arnoldsearch.com/">', '<meta name="robots" content="noindex">'))

# sitemap + robots
urls = [f"{DOMAIN}/"] + [f"{DOMAIN}/{slug}/" for slug, _ in HUBS]
(OUT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls) + "\n</urlset>\n")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")

print("built", len(list(OUT.rglob("*.html"))), "html files ->", OUT)
