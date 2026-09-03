#!/usr/bin/env python3
"""Generate the four national 'gold' hub sources (CFO recruiters, private equity
search firm, tech executive search firm, startup recruiters) on the exact
Arnold Executive Search template: same <head>/<style>, same section order,
same class names. Content only. No fee language, no unverified Gaea facts,
twelve-month guarantee is the only quantified claim.

Writes arnold_<slug>.html next to the other hub sources; build_site.py then
assembles dist/ from them.
"""
from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE = ROOT / "arnold_retained-executive-search.html"

GAEA_FAQ = ("Gaea Arnold is the Executive Search Leader and Founder of Arnold Executive Search. "
            "She personally runs every search on this site, from the intake brief through market "
            "mapping, direct outreach, shortlist calibration, and close. Every engagement is exclusive "
            "and contingent-first, starts without an up-front retainer, and carries a twelve-month guarantee.")

COMPETE = ('<p><span class="label">Heidrick &amp; Struggles / Korn Ferry / Spencer Stuart</span> '
           '— retained engagements and longer process design can be appropriate for a global or '
           'board-critical mandate. They are not the only answer when a company needs a focused, '
           'contingent-first search to begin without an up-front retainer.</p>')

PAGES = [
    # ------------------------------------------------------------------ CFO
    dict(
        slug="cfo-recruiters",
        title="CFO Recruiters",
        crumb="CFO Recruiters",
        subhead="Confidential, contingent-first CFO search for companies hiring a finance leader who fits the stage — first CFO, sponsor-backed, pre-IPO, turnaround, or succession.",
        answer="I recruit Chief Financial Officers and the finance leaders beneath them — VP Finance, Controller, FP&amp;A leadership — through direct, confidential outreach to people who are not applying anywhere. Contingent-first, no up-front retainer, twelve-month guarantee. Whether you searched for CFO recruiters, CFO headhunters, or a CFO executive search firm, this is the same engagement.",
        why_h2="Why a CFO search is different from a finance hire",
        why_p="A CFO decision is a board decision, not a department decision. The right candidate is usually running finance somewhere else, is not reading job posts, and will not take a first call from a generic recruiter. The mandate also changes by stage: the CFO who takes a company through its first audit is not the CFO who takes it through a sale. I start by defining which CFO you actually need before I touch the market.",
        fits=[
            ("First CFO for a scaling company", "For founder-led or growth-stage companies moving from a Controller or fractional finance lead to a full CFO who owns capital, board reporting, and the operating plan."),
            ("Sponsor-backed CFO searches", "For private-equity portfolio companies where the sponsor wants a CFO who has lived inside a value-creation plan, a lender relationship, and an exit process."),
            ("Confidential CFO replacement", "For boards and CEOs who need to replace a sitting CFO without the organization, the lender, or the market knowing a search is open."),
            ("VP Finance, Controller, and FP&amp;A leadership", "For the seats directly under the CFO, where the wrong hire shows up in the close, the forecast, and the board deck within a quarter."),
        ],
        how_h2="How I run a CFO search",
        how_p="I begin with the mandate: the next finance milestones, the board’s expectations, the reporting line, and what the CEO is not getting today. I map the narrow market of finance leaders who have done that specific work at a comparable stage, reach them directly and confidentially, and calibrate a shortlist against the mandate rather than a title. I stay in the process through references, offer, and close. The engagement is exclusive, contingent-first, and carries a twelve-month guarantee.",
        roles_h2="Roles I recruit",
        roles=[
            "Chief Financial Officer — first-time, sponsor-backed, pre-IPO, public-company, and turnaround profiles",
            "VP Finance and Head of Finance",
            "Corporate Controller and Chief Accounting Officer",
            "VP FP&amp;A and Head of Financial Planning",
            "Treasurer and VP Corporate Development, where the CFO mandate calls for it",
        ],
        terms_h2="CFO recruiters, CFO headhunters, CFO search firm — the same engagement",
        terms_p="Companies look for this service under several names: CFO recruiters, CFO headhunters, CFO recruiting firm, CFO search firm, CFO executive search firm. They all describe one thing — a confidential, direct-outreach search for a finance leader — and they differ mostly in whether the firm expects a retainer before it starts. I run that search contingent-first: no up-front retainer, an exclusive mandate, and a process built to retained-search standards.",
        faqs=[
            ("How long does a CFO search take?",
             "Long enough to get it right, and no longer. Because the engagement is contingent-first, there is no retainer negotiation before work starts; I begin market mapping the week the brief is agreed. The pace after that depends on how narrow the profile is, where the compensation sits, and how quickly your board can interview. I set a timeline in the brief and report against it."),
            ("What is the difference between a CFO recruiter and a CFO headhunter?",
             "In practice, nothing that should matter to you. “Headhunter” usually signals direct outreach to people who are not looking; “recruiter” can mean anything from that to sorting applicants. Every CFO search I run is direct outreach to sitting finance leaders. Ask any firm which of the two it is actually doing — the answer tells you what shortlist you will get."),
            ("Can you keep the search confidential from our current CFO?",
             "Yes. Confidential replacement searches are a normal part of CFO work. I agree with you on who inside the company knows, how candidates are briefed, and when the company is named. Outreach is direct and discreet, and nothing is posted publicly. The process is designed so that a sitting CFO, a lender, or the market does not learn of the search before you decide they should."),
            ("Do you also recruit VP Finance and Controllers?",
             "Yes. The seats under the CFO are where a weak hire shows up fastest — in the close, the forecast, and the board deck. I recruit VP Finance, Controller, Chief Accounting Officer, and FP&amp;A leadership with the same direct-outreach process. Often the right move is to define the CFO seat and the seat beneath it together, so the two hires fit each other."),
            ("Should we retain a firm or run this contingent?",
             "Retained is worth considering for a board-critical public-company mandate or a multi-role rebuild that needs deep governance. For most CFO searches, an exclusive contingent-first search gets the same direct-outreach rigor without an up-front retainer. I will tell you which I recommend for your mandate before we start; the retained option is explained on my retained executive search page."),
            ("How do you assess a CFO candidate beyond the résumé?",
             "I calibrate against the mandate: has this person owned the specific milestones you need next — a first audit, a debt raise, a sponsor exit, an IPO-readiness process — at a comparable stage and scale. Then I verify it through references with the CEO, board member, or sponsor who lived it. Title inflation is common in finance; the actual work history is what I check."),
            ("Who is Gaea Arnold?", GAEA_FAQ),
        ],
        compete_p="I run exclusive contingent CFO searches at retained-search execution standards — a different engagement model, not a boutique imitation of the retained firms. Direct outreach, clear calibration against the finance mandate, and a twelve-month guarantee.",
        related=[
            ("Private equity search firm →", "/private-equity-search-firm/"),
            ("Retained executive search →", "/retained-executive-search/"),
            ("Executive search firms →", "/executive-search-firms/"),
            ("Startup recruiters →", "/startup-recruiters/"),
        ],
    ),
    # ------------------------------------------------------- Private equity
    dict(
        slug="private-equity-search-firm",
        title="Private Equity Search Firm",
        crumb="Private Equity Search Firm",
        subhead="Contingent-first executive search for private equity sponsors and their portfolio companies — CEO, CFO, COO, and the functional leaders a value-creation plan depends on.",
        answer="I run confidential leadership searches for private equity firms and the companies they own: portfolio-company CEOs, CFOs, COOs, CROs, and the operating leaders who have to deliver the plan the deal was underwritten on. Direct outreach to people who are not looking, an exclusive mandate, no up-front retainer, twelve-month guarantee.",
        why_h2="Why sponsor-backed searches run differently",
        why_p="A portfolio-company hire has a clock on it. The plan was underwritten with a leadership assumption, the board meets monthly, and every quarter without the right operator is a quarter of value not created. The candidate market is also specific: leaders who have worked inside a sponsor-owned company know what a board deck, a lender covenant, and an exit process actually demand. I search that market directly rather than hoping it applies.",
        fits=[
            ("Post-close leadership upgrades", "For the CEO, CFO, or COO change a sponsor decided on during diligence and wants filled early in the hold period, quietly and without a public search."),
            ("Portfolio-company CFO and finance leadership", "For companies that need a CFO who has run a lender relationship, an add-on integration, and a sale process — and can build the finance function underneath."),
            ("Commercial and operating leaders for the plan", "For the CRO, VP Sales, COO, or VP Operations seat that carries the revenue or margin assumption in the value-creation plan."),
            ("Confidential searches around a transaction", "For mandates that cannot be visible before a signing, a refinancing, or a founder transition is announced."),
        ],
        how_h2="How I run a private equity search",
        how_p="I start with the deal thesis and the operating plan — what the sponsor needs this leader to make true, by when, and with what board support. I map the narrow market of people who have delivered that in a sponsor-backed setting, reach them directly and confidentially, and calibrate the shortlist against the plan rather than the title. The sponsor’s operating partner and the company’s CEO see the same information at the same time. The engagement is exclusive, contingent-first, and carries a twelve-month guarantee.",
        roles_h2="Roles I recruit for sponsors and portfolio companies",
        roles=[
            "Portfolio-company CEO and President",
            "Chief Financial Officer and VP Finance",
            "Chief Operating Officer and VP Operations",
            "Chief Revenue Officer and VP Sales",
            "Functional leaders tied to the value-creation plan — marketing, technology, people",
            "Investment professionals for the fund itself are a different market; if that is the seat, say so on the call and I will tell you whether it is a fit",
        ],
        terms_h2="Private equity headhunters, recruiters, search firms — the same engagement",
        terms_p="Sponsors and their portfolio companies look for this under different names: private equity headhunters, private equity recruiting firm, recruiters for private equity firms, private equity executive search firm. Whatever the label, the work is the same — direct, confidential outreach to operators who have delivered inside a sponsor-owned company. The difference between firms is whether they demand a retainer before starting and whether the person who took your brief is the person running the search. Here there is no up-front retainer, and I run the search myself.",
        faqs=[
            ("Do you work for the sponsor or the portfolio company?",
             "Both, and I say so up front. The mandate usually comes from the sponsor’s operating partner or deal team and is executed with the portfolio-company CEO and board. I agree at the start who owns decisions, who interviews, and who sees candidate information. Alignment between the sponsor and the management team is part of the search, not something I discover at offer stage."),
            ("How fast can a search start after close?",
             "Immediately. Because the engagement is contingent-first, there is no retainer negotiation delaying the start; I begin market mapping the week the brief is agreed. If you brief me during diligence, outreach can begin the day the deal signs. The pace after that depends on how narrow the profile is and how quickly the board can interview."),
            ("What makes a candidate “PE-ready”?",
             "They have operated under a sponsor’s board cadence and lived with the consequences: a monthly board deck that has to reconcile, a lender covenant that has to hold, an add-on that has to integrate, an exit process that has to close. I check for that specific experience and verify it with the sponsor or board member who was there. A large-company title without that context is not a substitute."),
            ("Can you run several searches across a portfolio?",
             "Yes, and it usually helps. A sponsor with a consistent view of what a portfolio-company CFO or CEO should look like gets a better result when one search partner carries that view from company to company. I scope each mandate separately and keep candidate information separate between companies, but the market knowledge compounds."),
            ("Retained or contingent for a sponsor-backed search?",
             "For most portfolio-company seats, an exclusive contingent-first search delivers retained-search rigor without an up-front retainer, which matters when the hold period is measured in quarters. Retained is worth considering for a multi-role leadership rebuild or a public-company mandate that needs deep governance. I will recommend one before we start — my retained executive search page explains how I decide."),
            ("Who is Gaea Arnold?", GAEA_FAQ),
        ],
        compete_p="I run exclusive contingent searches for sponsors at retained-search execution standards — a different engagement model, not a boutique imitation of the retained firms. Direct outreach, calibration against the value-creation plan, and a twelve-month guarantee.",
        related=[
            ("CFO recruiters →", "/cfo-recruiters/"),
            ("Retained executive search →", "/retained-executive-search/"),
            ("Executive search firms →", "/executive-search-firms/"),
            ("Tech executive search firm →", "/tech-executive-search-firm/"),
        ],
    ),
    # ------------------------------------------------------------- Tech exec
    dict(
        slug="tech-executive-search-firm",
        title="Tech Executive Search Firm",
        crumb="Tech Executive Search Firm",
        subhead="Confidential, contingent-first executive search for technology leadership — CTO, CIO, VP Engineering, CPO, CISO — and for the executives technology companies need in every function.",
        answer="I run technology executive searches two ways: technology leaders for any company — CTO, CIO, VP Engineering, Head of Product, CISO, VP Data and AI — and the full executive team for technology companies, from CEO and CFO to CRO and CMO. Direct outreach to leaders who are not job-searching, an exclusive mandate, no up-front retainer, twelve-month guarantee.",
        why_h2="Why technology leadership searches go wrong",
        why_p="The best technical leaders are rarely visible. They are shipping somewhere, they are cautious about recruiters, and their peers know their work long before a résumé does. Companies also confuse the seat: the VP Engineering who scales a large team is not the CTO who sets architecture and talks to the board, and hiring one when you needed the other costs a year. I define the seat first, then search the specific market for it.",
        fits=[
            ("CTO, CIO, and VP Engineering", "For companies that need a technology leader who can own architecture, delivery, and the engineering organization at the next stage of scale — or a CIO who runs technology as a business function."),
            ("Product, data, AI, and security leadership", "For Chief Product Officer, VP Product, VP Data, Head of AI, and CISO seats where the market is narrow and the wrong hire is expensive to undo."),
            ("Executive teams for technology companies", "For software and technology businesses hiring a CEO, CFO, CRO, CMO, or COO who has operated in a product-led, recurring-revenue company."),
            ("Confidential technology leadership replacements", "For boards and CEOs replacing a sitting technology leader without unsettling the engineering team or the market."),
        ],
        how_h2="How I run a technology executive search",
        how_p="I begin with the seat definition: what the business needs this leader to build, own, or fix; the reporting line; how the board and the engineering team will judge success. I map the narrow market of leaders who have done that specific work at a comparable stage and scale, reach them directly and confidentially, and calibrate the shortlist through references with the people who built alongside them. I stay in the process through offer, equity questions, and close. The engagement is exclusive, contingent-first, and carries a twelve-month guarantee.",
        roles_h2="Roles I recruit",
        roles=[
            "Chief Technology Officer, Chief Information Officer, Chief Digital Officer",
            "VP Engineering, Head of Engineering, VP Platform and Infrastructure",
            "Chief Product Officer, VP Product",
            "VP Data, Head of AI and Machine Learning, Chief Data Officer",
            "Chief Information Security Officer, VP Security",
            "CEO, CFO, CRO, CMO, and COO for software and technology companies",
        ],
        terms_h2="Tech executive recruiters, technology executive search firms — the same search",
        terms_p="Companies find this page searching for tech executive search firms, technology executive search firm, executive tech recruiters, or technology executive recruiters. The labels describe one engagement: direct, confidential outreach to senior technology leaders. What separates firms is whether they understand the difference between the seats, whether they demand a retainer before starting, and whether the person who took your brief runs the search. Here I run the search myself, with no up-front retainer.",
        faqs=[
            ("CTO or VP Engineering — how do I know which I need?",
             "Ask what the seat has to own. If the gap is architecture, technical strategy, and representing technology to the board and customers, that is a CTO. If the gap is delivery, hiring, process, and managing engineering managers, that is a VP Engineering. Many companies need the second and post the first. I settle this in the brief, because the two candidate markets barely overlap."),
            ("How do you evaluate a technical leader you cannot code-test?",
             "Through the people who built alongside them. I reference with engineers who reported to them, peers who depended on their systems, and executives who judged their delivery. I look for what they shipped, what they inherited and fixed, and what they chose not to build. Job titles and technology buzzwords tell me very little; the reference conversations tell me most of it."),
            ("Do you run remote and hybrid searches?",
             "Yes. For technology leadership the market is national and often remote, and I search it that way. If the seat requires presence — a hardware team, a regulated environment, an in-office engineering culture — I say so in the brief and search accordingly. Location is a filter I apply deliberately, not a default."),
            ("Can you handle equity-heavy compensation conversations?",
             "Yes. Senior technology candidates weigh equity, vesting, and the company’s capital position as carefully as salary, and they ask about it early. I make sure the company’s answers are ready before outreach and I manage the conversation through to a signed offer. I do not publish compensation figures on this site; we handle that on the call."),
            ("Contingent or retained for a technology executive search?",
             "For most technology leadership seats, an exclusive contingent-first search delivers retained-search rigor without an up-front retainer and starts the week the brief is agreed. Retained is worth considering for a board-critical mandate or a coordinated multi-role leadership build. I will recommend one before we start — my retained executive search page explains how I decide."),
            ("Who is Gaea Arnold?", GAEA_FAQ),
        ],
        compete_p="I run exclusive contingent technology searches at retained-search execution standards — a different engagement model, not a boutique imitation of the retained firms. Direct outreach, references with the people who built alongside the candidate, and a twelve-month guarantee.",
        related=[
            ("Startup recruiters →", "/startup-recruiters/"),
            ("Executive search firms →", "/executive-search-firms/"),
            ("CFO recruiters →", "/cfo-recruiters/"),
            ("IT staffing →", "/it-staffing/"),
        ],
    ),
    # --------------------------------------------------------------- Startup
    dict(
        slug="startup-recruiters",
        title="Startup Recruiters",
        crumb="Startup Recruiters",
        subhead="Contingent-first executive search for founders hiring the leaders who define a function — first VP Sales, first VP Engineering, first CFO, first Head of Marketing, COO.",
        answer="I recruit the first executives and key leaders for venture-backed and founder-led companies — the hires that turn a founder’s job into a function. Direct, confidential outreach to leaders who have built it at your stage, an exclusive mandate, no up-front retainer, twelve-month guarantee.",
        why_h2="Why startup executive hiring is a different search",
        why_p="A startup’s first VP is a bet on judgment, not on a résumé. The leader who thrives at a company with no process is not the leader who thrives inside a mature one, and large-company titles are the most common false positive in early-stage hiring. Founders also cannot afford a slow, retained process built for a global corporation. I run a founder-paced search: direct outreach to people who have built the function at your stage, and no up-front retainer.",
        fits=[
            ("Your first VP Sales or Head of Revenue", "For founders moving off founder-led sales who need a leader who has built a team and a repeatable motion at a comparable stage — not a large-company sales executive with a big team behind them."),
            ("Your first VP Engineering or CTO", "For technical founders who need a leader who can scale the team, the process, and the architecture without losing the pace that got the company here."),
            ("Your first CFO or Head of Finance", "For companies moving from bookkeeping and a fractional finance lead to a leader who owns the plan, the board reporting, and the next raise."),
            ("COO, Head of Marketing, and Head of People", "For the seats a founder is still personally covering that need an owner before the next stage."),
        ],
        how_h2="How I run a startup executive search",
        how_p="I begin with what the founder is actually doing today that this leader must take over, what the board expects the hire to change, and what the company can offer in cash, equity, and scope. I map the market of leaders who have built the function at a comparable stage, reach them directly and confidentially, and calibrate the shortlist against the stage rather than the title. I stay in the process through equity conversations, references, and close. The engagement is exclusive, contingent-first, and carries a twelve-month guarantee.",
        roles_h2="Roles I recruit for startups",
        roles=[
            "VP Sales, Head of Revenue, Chief Revenue Officer",
            "VP Engineering, CTO, Head of Product",
            "CFO, VP Finance, Head of Finance",
            "COO, Head of Operations",
            "VP Marketing, Head of Marketing",
            "Head of People, VP People",
        ],
        terms_h2="Recruiters for startups vs. a startup recruitment agency — what to expect",
        terms_p="Founders look for this under several names: startup recruiters, recruiters for startups, startup recruitment agency, startup executive search. The distinction that matters is scope. An agency that fills individual-contributor roles at volume is a different service from a search for the leader who will build that team. This page is the second: leadership and function-defining hires, run by me directly. If the seat is a volume hiring need, say so on the call and I will tell you whether it is a fit.",
        faqs=[
            ("What stage do you work with?",
             "Founder-led and venture-backed companies making leadership hires — typically the first executive in a function, or the leader who takes over a seat the founder has been covering. The stage matters less than the mandate: is this hire expected to build something that does not yet exist? If so, I search for people who have done exactly that."),
            ("Why not just use our investors’ network?",
             "Use it — and run a search alongside it. Investor networks surface people the investors already know, which is a valuable but narrow slice of the market. A direct search covers the leaders who have built the function at your stage and are not connected to your cap table. The best outcome is often the candidate nobody on the board had heard of."),
            ("How do you screen out big-company executives who will not thrive here?",
             "By checking what they personally built, not what their organization had. I ask what existed the day they started, what they created, and what they did when there was no team to delegate to. Then I verify it with the founder or executive who watched them do it. A leader who has only operated with a large team underneath them is a known risk at an early stage, and I say so."),
            ("Can you work with an equity-heavy offer?",
             "Yes. Early-stage candidates evaluate equity, vesting, and the company’s runway as seriously as base salary, and the right ones ask sharp questions about it. I make sure the company has its answers ready before outreach and I carry the conversation through to a signed offer. I do not publish compensation or fee figures on this site."),
            ("How quickly can you start?",
             "The week the brief is agreed. There is no retainer to negotiate, so market mapping starts immediately and outreach follows once we have aligned on the seat, the story, and what the company can offer. The pace after that depends on how narrow the profile is and how quickly the founders and board can interview."),
            ("Contingent or retained for a startup?",
             "Contingent-first, almost always. It removes the up-front retainer that stretches a startup’s budget and it fits the pace founders need. Retained is worth considering when you are building several leadership seats at once and want a single coordinated process. I explain how I decide on my retained executive search page, and I will recommend one before we start."),
            ("Who is Gaea Arnold?", GAEA_FAQ),
        ],
        compete_p="I run exclusive contingent searches for founders at retained-search execution standards — a different engagement model, not a boutique imitation of the retained firms. Direct outreach, calibration against the stage rather than the title, and a twelve-month guarantee.",
        related=[
            ("Tech executive search firm →", "/tech-executive-search-firm/"),
            ("CFO recruiters →", "/cfo-recruiters/"),
            ("Sales recruiters →", "/sales-recruiters/"),
            ("Marketing recruiters →", "/marketing-recruiters/"),
        ],
    ),
]


def render(p, head):
    head = head.replace("<title>Retained Executive Search — Arnold Executive Search</title>",
                        f"<title>{p['title']} — Arnold Executive Search</title>")
    fits = "\n".join(f"    <h3>{h}</h3><p>{t}</p>" for h, t in p["fits"])
    roles = "\n".join(f"      <li>{r}</li>" for r in p["roles"])
    faqs = "\n".join(
        f'    <div class="faq-item">\n      <div class="faq-q">{q}</div>\n      <div class="faq-a">{a}</div>\n    </div>'
        for q, a in p["faqs"])
    related = "\n".join(f'      <a href="{href}">{t}</a>' for t, href in p["related"])
    return f"""{head}</head>
<body>

<div class="topbar">
  <div class="brand"><span class="monogram">GA</span>Arnold Executive Search</div>
  <div class="topnav">
    <a href="#">Practice Areas</a>
    <a href="#">About Gaea</a>
    <a href="#">Contact</a>
  </div>
</div>

<div class="breadcrumb">
  <a href="#">Home</a> &nbsp;/&nbsp; <span>{p['crumb']}</span>
</div>

<div class="hero">
  <h1>{p['title']}</h1>
  <p class="subhead">{p['subhead']}</p>
  <div class="direct-answer">
    {p['answer']}
  </div>
  <div class="badges">
    <span class="badge">Contingent-First</span>
    <span class="badge">No Up-Front Retainer</span>
    <span class="badge">Twelve-Month Guarantee</span>
  </div>
  <div class="author-strip">
    <img class="author-photo" src="gaea_arnold.jpg" alt="Gaea Arnold">
    <div>
      <div class="author-name">Gaea Arnold</div>
      <div class="author-title">Executive Search Leader &amp; Founder, Arnold Executive Search</div>
    </div>
  </div>
</div>

<main>

  <section>
    <h2>{p['why_h2']}</h2>
    <p>{p['why_p']}</p>
  </section>

  <section>
    <h2>Where this fits</h2>
{fits}
  </section>

  <section>
    <h2>{p['how_h2']}</h2>
    <p>{p['how_p']}</p>
  </section>

  <section>
    <h2>{p['roles_h2']}</h2>
    <ul class="role-list">
{roles}
    </ul>
  </section>

  <section>
    <h2>{p['terms_h2']}</h2>
    <p>{p['terms_p']}</p>
  </section>

  <section>
    <h2>Frequently asked questions</h2>
{faqs}
  </section>

  <section>
    <h2>Competitive positioning</h2>
    <div class="compete-block">
      {COMPETE}
    </div>
    <p>{p['compete_p']}</p>
  </section>

  <section>
    <h2>Related decisions</h2>
    <div class="related-links">
{related}
    </div>
  </section>

</main>

<div class="cta-band">
  <h2>Let’s talk about the seat you’re trying to fill</h2>
  <p>30 minutes. No pitch deck — just the actual brief and whether this is a fit.</p>
  <a href="#" class="cta-button">Schedule a 30-Minute Call</a>
  <div class="cta-contact"></div>
</div>

<footer>Arnold Executive Search — Gaea Arnold, Executive Search Leader &amp; Founder</footer>

</body>
</html>
"""


if __name__ == "__main__":
    tpl = TEMPLATE.read_text()
    head = tpl[: tpl.find("</head>")]
    for p in PAGES:
        out = ROOT / f"arnold_{p['slug']}.html"
        out.write_text(render(p, head))
        # voice checks: FAQ answers 40-100 words, no fee language, no placeholders
        for q, a in p["faqs"]:
            n = len(a.split())
            assert 40 <= n <= 100, (p["slug"], q, n)
        s = out.read_text().split("</head>", 1)[1]   # body only; CSS has % units
        for bad in ("$", "%", "PLACEHOLDER", "world-class", "industry-leading", "best-in-class", "unparalleled"):
            assert bad not in s, (p["slug"], bad)
        print("wrote", out.name, len(s), "bytes")
