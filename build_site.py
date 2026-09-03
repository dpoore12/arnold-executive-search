#!/usr/bin/env python3
"""Assemble the deployable static site for arnoldsearch.com from the hub sources.

Run:  python3 build_site.py   (regenerates the four gold hub sources first)

Rules enforced here (sitewide):
  * nothing that reads "[PLACEHOLDER" ever reaches dist/
  * no legal-recruiters hub (killed) — /legal-recruiters/ 301s to /
  * contact/booking lives in ONE place: BOOKING_URL / CONTACT_EMAIL below
  * fee-language lock: no dollar amounts, percentages, or fee mechanics
"""
import re, json, shutil, html, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "dist"
DOMAIN = "https://arnoldsearch.com"

# ---- Contact. Fill these in and rebuild; every page picks them up. ----------
BOOKING_URL = ""      # e.g. "https://calendly.com/<gaea>/30min"
CONTACT_EMAIL = ""    # e.g. "gaea@arnoldsearch.com"

# Order = order on the homepage grid. Gold (national client-intent) pages first.
HUBS = [
    ("executive-search-firms",      "arnold_executive-search-firms.html"),
    ("retained-executive-search",   "arnold_retained-executive-search.html"),
    ("cfo-recruiters",              "arnold_cfo-recruiters.html"),
    ("private-equity-search-firm",  "arnold_private-equity-search-firm.html"),
    ("tech-executive-search-firm",  "arnold_tech-executive-search-firm.html"),
    ("startup-recruiters",          "arnold_startup-recruiters.html"),
    ("executive-headhunters",       "arnold_executive-headhunters.html"),
    ("sales-recruiters",            "arnold_sales-recruiters.html"),
    ("marketing-recruiters",        "arnold_marketing-recruiters.html"),
    ("it-staffing",                 "arnold_it-staffing.html"),
    ("accounting-staffing",         "arnold_accounting-staffing.html"),
    ("healthcare-staffing",         "arnold_healthcare-staffing.html"),
    ("construction-staffing",       "arnold_construction-staffing.html"),
]
KILLED = ["legal-recruiters"]

GAEA_FAQ = ("Gaea Arnold is the Executive Search Leader and Founder of Arnold Executive Search. "
            "She personally runs every search on this site, from the intake brief through market "
            "mapping, direct outreach, shortlist calibration, and close. Every engagement is exclusive "
            "and contingent-first, starts without an up-front retainer, and carries a twelve-month guarantee.")

if BOOKING_URL:
    CTA_HREF = BOOKING_URL
    CTA_ATTR = ' target="_blank" rel="noopener"'
elif CONTACT_EMAIL:
    CTA_HREF = f"mailto:{CONTACT_EMAIL}?subject=Executive%20search%20inquiry"
    CTA_ATTR = ""
else:
    CTA_HREF = "/#contact"
    CTA_ATTR = ""
CONTACT_LINE = (f'<div class="cta-contact"><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></div>'
                if CONTACT_EMAIL else "")

# The four gold hub sources are generated from the template (gen_gold_hubs.py)
subprocess.run([sys.executable, str(ROOT / "gen_gold_hubs.py")], check=True)

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

# One shared stylesheet for the built site (identical CSS, one cacheable file)
_tpl_css = re.search(r"<style>(.*?)</style>", (ROOT / "arnold_retained-executive-search.html").read_text(), re.S).group(1)
HUB_GRID_CSS = """
  .hub-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 16px; margin-top: 18px; }
  .hub-card { display: block; background: #fff; border: 1px solid var(--rule); border-radius: 4px; padding: 20px 22px; border-bottom: 1px solid var(--rule); }
  .hub-card:hover { border-color: var(--bronze-light); }
  .hub-card h3 { margin: 0 0 8px; font-size: 21px; }
  .hub-card p { margin: 0; font-size: 15px; color: var(--ink-soft); line-height: 1.5; }
  .hub-card .go { display: block; margin-top: 12px; font-size: 14px; color: var(--bronze); }
"""
(OUT / "style.css").write_text(_tpl_css.strip("\n") + "\n" + HUB_GRID_CSS.strip("\n") + "\n")
STYLE_LINK = '<link rel="stylesheet" href="/style.css">'

def externalize_css(s):
    return re.sub(r"<style>.*?</style>", STYLE_LINK, s, count=1, flags=re.S)
(OUT / ".gitignore").write_text(".vercel\n")

# Brand-consistent headshot placeholder until the real photo is supplied.
PHOTO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
<rect width="200" height="200" fill="#14213d"/>
<circle cx="100" cy="100" r="72" fill="none" stroke="#c9924a" stroke-width="3"/>
<text x="100" y="118" text-anchor="middle" font-family="Georgia, 'DM Serif Display', serif" font-size="58" fill="#c9924a">GA</text>
</svg>"""
(OUT / "gaea_arnold.svg").write_text(PHOTO_SVG)


# Scope questions the prototypes left as placeholders. Answered without
# claiming a scope Gaea has not confirmed: the call settles it.
SCOPE_FAQ = {
    "Do you handle travel or contract nursing, or only permanent placement?":
        "Say which you need in the brief and I will tell you plainly whether it is a fit before any "
        "outreach starts. This page covers the hub’s stated scope — nursing staff, allied health, and "
        "healthcare operations leadership — and I would rather confirm the engagement model for your "
        "specific coverage need on the call than publish a blanket claim here.",
    "Do you handle both W-2 staffing and 1099 or subcontractor placement?":
        "Say which arrangement you need in the brief and I will tell you plainly whether it is a fit "
        "before outreach starts. Employment structure changes the candidate market, the compliance "
        "obligations, and the timeline, so I confirm it for the specific project on the call rather "
        "than publish a blanket claim here.",
}


def strip_placeholders(s):
    """Remove every draft/proof block that carries [PLACEHOLDER ...] and swap the
    'Who is Gaea Arnold?' answer for the verified-only version."""
    s = re.sub(r'\s*<div class="flag-note">.*?</div>', "", s, flags=re.S)
    # FAQ answers that were a placeholder flag-note are now empty: fill or drop
    def _faq(m):
        q = m.group(1)
        a = SCOPE_FAQ.get(html.unescape(q))
        return (m.group(0).replace('<div class="faq-a"></div>', f'<div class="faq-a">{a}</div>')
                if a else "")
    s = re.sub(r'\s*<div class="faq-item">\s*<div class="faq-q">(.*?)</div>\s*<div class="faq-a"></div>\s*</div>',
               _faq, s, flags=re.S)
    s = re.sub(r'\s*<div class="proof-note">\s*\[PLACEHOLDER.*?</div>', "", s, flags=re.S)
    s = re.sub(r'(<div class="faq-q">Who is Gaea Arnold\?</div>\s*<div class="faq-a">).*?(</div>)',
               lambda m: m.group(1) + GAEA_FAQ + m.group(2), s, flags=re.S)
    s = re.sub(r'\s*<div class="cta-contact">.*?</div>', ("\n  " + CONTACT_LINE) if CONTACT_LINE else "", s, flags=re.S)
    return s


hub_meta = []
for slug, fname in HUBS:
    s = (ROOT / fname).read_text()
    title = re.search(r"<title>(.*?) — Arnold Executive Search</title>", s).group(1)
    subhead = re.search(r'<p class="subhead">(.*?)</p>', s, re.S).group(1).strip()
    hub_meta.append((slug, title, subhead))

    desc = html.escape(re.sub(r"<[^>]+>", "", subhead), quote=True)
    s = s.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'<meta name="description" content="{desc}">\n'
        f'<link rel="canonical" href="{DOMAIN}/{slug}/">',
    )
    s = re.sub(r'src="(PHOTO_PLACEHOLDER_)?gaea_arnold\.jpg"', 'src="/gaea_arnold.svg"', s)
    s = externalize_css(s)

    # Top nav + breadcrumb
    s = s.replace('<a href="#">Practice Areas</a>', '<a href="/#practice-areas">Practice Areas</a>')
    s = s.replace('<a href="#">About Gaea</a>', '<a href="/#about">About Gaea</a>')
    s = s.replace('<a href="#">Contact</a>', '<a href="#contact">Contact</a>')
    s = s.replace('<a href="#">Home</a>', '<a href="/">Home</a>')
    s = s.replace('<div class="brand"><span class="monogram">GA</span>Arnold Executive Search</div>',
                  '<a class="brand" href="/" style="border-bottom:none"><span class="monogram">GA</span>Arnold Executive Search</a>')

    # CTA band
    s = s.replace('<div class="cta-band">', '<div class="cta-band" id="contact">')
    s = s.replace('<a href="#" class="cta-button">', f'<a href="{CTA_HREF}"{CTA_ATTR} class="cta-button">')

    s = strip_placeholders(s)

    # Any remaining "#" links (city / spoke pages not yet built) -> contact band
    s = s.replace('href="#"', 'href="#contact"')

    assert "PLACEHOLDER" not in s, (slug, "placeholder survived")
    d = OUT / slug
    d.mkdir()
    (d / "index.html").write_text(s)

# ---- Homepage: reuse the template's <head>/<style> so the look is identical ----
tpl = (ROOT / "arnold_executive-search-firms.html").read_text()
head = tpl[: tpl.find("</head>")]
head = head.replace("<title>Executive Search Firms — Arnold Executive Search</title>",
                    "<title>Arnold Executive Search — Contingent Executive Search &amp; Specialized Recruiting</title>")
head = head.replace(
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    '<meta name="description" content="Arnold Executive Search — Gaea Arnold runs confidential, contingent executive search for companies hiring leadership: CFO and finance, private equity portfolio companies, technology, startups, sales, marketing, healthcare, accounting, IT, and construction. No up-front retainer, twelve-month guarantee.">\n'
    f'<link rel="canonical" href="{DOMAIN}/">',
)
head = externalize_css(head + "</head>").replace("</head>", "")

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
    I run exclusive contingent searches at retained-search execution standards — direct, discreet outreach to leaders who are not job-searching — for CFO and finance seats, private equity portfolio companies, technology, startups, sales, marketing, healthcare, accounting, IT, and construction. Contingent-first, no up-front retainer, twelve-month guarantee.
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
    <p>Gaea Arnold is the Executive Search Leader and Founder of Arnold Executive Search. She personally runs every search on this site — the intake brief, the market map, the direct outreach, the shortlist, and the close — with no hand-off to a junior researcher after the first call.</p>
  </section>

  <section>
    <h2>How the engagement works</h2>
    <div class="compete-block">
      <p><span class="label">Heidrick &amp; Struggles / Korn Ferry / Spencer Stuart</span> — retained engagements and multi-month timelines. The right lane for a global CEO search. Not the right lane for a company that needs a contingent-first search moving in weeks.</p>
    </div>
    <p>No up-front retainer, no multi-month intake process, and a twelve-month replacement guarantee on every placement. The search is exclusive, the outreach is direct and confidential, and the person who takes your brief is the person who runs it.</p>
  </section>

</main>

<div class="cta-band" id="contact">
  <h2>Let's talk about the seat you're trying to fill</h2>
  <p>30 minutes. No pitch deck, no retainer discussion — just the actual brief and whether this is a fit.</p>
  <a href="{CTA_HREF if CTA_HREF != '/#contact' else '#contact'}"{CTA_ATTR} class="cta-button">Schedule a 30-Minute Call</a>
  {CONTACT_LINE}
</div>

<footer>Arnold Executive Search — Gaea Arnold, Executive Search Leader &amp; Founder</footer>

</body>
</html>
"""
assert "PLACEHOLDER" not in home
(OUT / "index.html").write_text(home)

# 404 -> homepage look, noindex
(OUT / "404.html").write_text(
    home.replace("<h1>Executive search that moves in weeks, not quarters</h1>", "<h1>Page not found</h1>")
        .replace(f'<link rel="canonical" href="{DOMAIN}/">', '<meta name="robots" content="noindex">'))

# sitemap + robots
urls = [f"{DOMAIN}/"] + [f"{DOMAIN}/{slug}/" for slug, _ in HUBS]
(OUT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls) + "\n</urlset>\n")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")

# Vercel config. dist/vercel.json is used when the Vercel project's root is dist/
# (Perplexity's CLI deploy); the repo-root vercel.json makes a Git-connected
# project with root "/" serve dist/ with identical behaviour.
redirects = []
for k in KILLED:
    redirects += [{"source": f"/{k}", "destination": "/", "permanent": True},
                  {"source": f"/{k}/", "destination": "/", "permanent": True}]
cfg = {"cleanUrls": True, "trailingSlash": True, "redirects": redirects}
(OUT / "vercel.json").write_text(json.dumps(cfg) + "\n")
(ROOT / "vercel.json").write_text(json.dumps({"outputDirectory": "dist", **cfg}) + "\n")

built = sorted(p.relative_to(OUT).as_posix() for p in OUT.rglob("*.html"))
for p in OUT.rglob("*.html"):
    assert "PLACEHOLDER" not in p.read_text(), p
print("built", len(built), "html files ->", OUT)
print("contact:", "booking=" + (BOOKING_URL or "-"), "email=" + (CONTACT_EMAIL or "-"))
