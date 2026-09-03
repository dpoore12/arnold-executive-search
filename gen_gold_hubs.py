#!/usr/bin/env python3
"""Generate the five national 'gold' hub sources (retained executive search, CFO
recruiters, private equity search firm, tech executive search firm, startup
recruiters) on the exact Arnold Executive Search template: same <head>/<style>,
same section order family, same class names. Content only.

Sharpened against live page one for each term (Sep 2026): a snippet-ready
definition, a step-by-step process, a buyer checklist ("what to ask before you
sign"), comparison blocks that answer the People-Also-Ask questions, and FAQs.

Rules: first-person Gaea voice; no fee amounts, percentages or retainer figures;
no unverified Gaea facts; the twelve-month guarantee is the only quantified
claim; competitive positioning names only Heidrick & Struggles / Korn Ferry /
Spencer Stuart; 5-8 FAQs at 40-100 words.

Writes arnold_<slug>.html next to the other hub sources; build_site.py then
assembles dist/ from them.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE = ROOT / "TEMPLATE_REFERENCE_legal_recruiters.html"

GAEA_FAQ = ("Gaea Arnold is the Executive Search Leader and Founder of Arnold Executive Search. "
            "She personally runs every search on this site, from the intake brief through market "
            "mapping, direct outreach, shortlist calibration, and close. Every engagement is exclusive "
            "and contingent-first, starts without an up-front retainer, and carries a twelve-month guarantee.")

COMPETE = ('<p><span class="label">Heidrick &amp; Struggles / Korn Ferry / Spencer Stuart</span> '
           '— retained engagements and longer process design can be appropriate for a global or '
           'board-critical mandate. They are not the only answer when a company needs a focused, '
           'contingent-first search to begin without an up-front retainer.</p>')

PAGES = [
    # ------------------------------------------------------- Retained search
    dict(
        slug="retained-executive-search",
        title="Retained Executive Search",
        subhead="Retained executive search for board-critical and multi-role mandates — and a plain guide to when retained is the right model, from a firm whose default is contingent-first.",
        answer="I run retained executive searches for board-critical leadership mandates, confidential CEO and C-suite transitions, and coordinated multi-role builds. I also run exclusive contingent-first searches, so I will tell you which model fits your mandate rather than sell you the one with the retainer. Either way: direct outreach to leaders who are not looking, one accountable process, and a twelve-month guarantee.",
        define_h2="What retained executive search is",
        define_p="Retained executive search is an exclusive engagement in which a company commits to one search firm for a leadership hire and funds the search in stages rather than paying only when a candidate starts. In return the firm commits dedicated capacity: a full market map, direct and confidential outreach to sitting executives, a calibrated shortlist, and a managed process through offer and close.",
        why_h2="When retained is the right call — and when it is not",
        why_p="Retained search earns its structure when the mandate is board-critical, unusually confidential, or spread across several seats that need one coordinated process. It is the wrong reflex for a defined VP or functional executive search that a focused, exclusive contingent-first process can start this week. I compare urgency, complexity, confidentiality, and the candidate market before recommending either model — and I say which one I would choose if it were my money.",
        fits=[
            ("Board-critical CEO and C-suite mandates", "For succession, a CEO transition, or a leadership change where the board is involved and the cost of a miss is measured in years, not quarters."),
            ("Coordinated multi-role leadership builds", "For a founding team, a post-transaction rebuild, or several executive seats that benefit from one market map and one calibrated process."),
            ("Highly confidential searches", "For mandates that cannot be visible to the organization, a lender, an acquirer, or the market until you decide they should be."),
            ("Narrow, hard-to-reach candidate markets", "For roles where the qualified pool is small, mostly employed, and will only engage through sustained, direct, discreet outreach."),
        ],
        steps_h2="How a retained executive search works, step by step",
        steps_intro="The retained model is a committed process, not a longer version of a contingent one. This is how I run it.",
        steps=[
            "Mandate and governance — we agree the role definition, decision rights, success measures, confidentiality boundaries, and who interviews.",
            "Market map — I build the named candidate market for the seat: the companies, the functions, and the people who have done the work at comparable scale.",
            "Direct outreach — every credible candidate is approached personally and confidentially. Nothing is posted.",
            "Calibrated slate — a shortlist assessed against the mandate, with a written view of each candidate’s fit, risks, and motivation.",
            "Interviews, references, and offer — I run the process through your interviews, verify the work history with the people who saw it, and manage the offer to a signed acceptance.",
            "Start and guarantee — I stay involved through the start date, and every placement carries a twelve-month guarantee.",
        ],
        roles_h2="Mandates I run retained",
        roles=[
            "CEO and President succession or transition",
            "CFO, COO, CRO, and CTO seats where the board is directly involved",
            "Founding-team and post-transaction leadership builds run as one process",
            "Confidential replacements of a sitting executive",
            "Board director searches where the market is narrow and the approach must be discreet",
        ],
        compare_h2="Retained vs. contingent — the honest comparison",
        compare=[
            ("What you commit", "Retained: an exclusive mandate and a staged commitment before a candidate is hired. Contingent-first: an exclusive mandate with no up-front retainer."),
            ("What you get", "Retained: dedicated capacity and governance for the life of the search. Contingent-first: the same direct-outreach method, run at retained-search execution standards, on a defined mandate."),
            ("When each fits", "Retained: board-critical, highly confidential, or multi-role. Contingent-first: a defined executive seat where you want one accountable process that starts now."),
            ("What stays the same", "Direct outreach to people who are not looking, one person running the search from brief to close, and a twelve-month guarantee."),
        ],
        check_h2="What to ask a retained search firm before you sign",
        check_intro="Whether you retain me or someone else, these questions separate a committed search from an expensive one.",
        checks=[
            "Who actually runs the search after the pitch — the partner in the room, or a research team you never meet?",
            "What does the market map cover, and will we see it?",
            "How is confidentiality handled, and who inside our company needs to know?",
            "What are the milestones, and what happens if one is missed?",
            "What is the guarantee if the placement leaves?",
            "If you also run contingent searches, which model would you recommend for this seat, and why?",
        ],
        faqs=[
            ("What is the difference between contingent and retained search firms?",
             "A retained firm is engaged exclusively and funded in stages as the search progresses; a contingent firm is paid only when its candidate is hired, and often competes with other firms on the same role. The difference that matters to you is commitment: who is accountable, how much capacity is dedicated, and whether the outreach is direct. I run exclusive contingent-first searches with retained-search discipline, and retained searches where the mandate needs the added governance."),
            ("How much does a retained search cost?",
             "A retained engagement is structured as a staged commitment agreed in advance, with the balance tied to milestones rather than paid only on a hire. I do not publish fee figures on this site because the right structure depends on the mandate. On the call I will set out the structure for your seat and tell you plainly whether a contingent-first search would serve you as well."),
            ("How long does a retained executive search take?",
             "Long enough to map the market properly and run a calibrated process, and no longer. The phases are fixed — mandate, market map, outreach, slate, interviews, offer — and the pace is set by how narrow the profile is and how quickly your board can meet. I put a timeline in the brief and report against it every week."),
            ("When do you recommend retained over contingent?",
             "I recommend retained when a mandate is board-critical, unusually complex, highly confidential, or part of a coordinated multi-role build. Those conditions justify a dedicated, exclusive process with deeper governance. For a defined executive mandate that can move quickly, my contingent-first approach is usually the more practical starting point, and I will say so."),
            ("Can a contingent-first search still be confidential?",
             "Yes. Confidentiality depends on how the search is designed and conducted, not on the engagement model. I use direct, discreet outreach and agree what can be shared at each stage. For a highly sensitive or board-critical mandate, I assess whether the additional commitment and governance of a retained search is the better fit and tell you before we start."),
            ("Should we just use one of the large global retained firms?",
             "For a global CEO search or a public-company board mandate, Heidrick &amp; Struggles, Korn Ferry, and Spencer Stuart are built for that scale. For a defined leadership seat where you want the person who took the brief to run the search, start without an up-front retainer, and move in weeks, that is the engagement I run. The honest answer depends on the mandate, and I will give it to you on the call."),
            ("Who is Gaea Arnold?", GAEA_FAQ),
        ],
        compete_p="I run retained searches where the mandate calls for it and exclusive contingent searches at retained-search execution standards everywhere else — a different engagement model, not a boutique imitation of the retained firms. Direct outreach, one accountable process, and a twelve-month guarantee.",
        related=[
            ("Executive search firms →", "/executive-search-firms/"),
            ("CFO recruiters →", "/cfo-recruiters/"),
            ("Private equity search firm →", "/private-equity-search-firm/"),
            ("Executive headhunters →", "/executive-headhunters/"),
        ],
    ),
    # ------------------------------------------------------------------ CFO
    dict(
        slug="cfo-recruiters",
        title="CFO Recruiters",
        subhead="Confidential, contingent-first CFO search for companies hiring a finance leader who fits the stage — first CFO, sponsor-backed, pre-IPO, turnaround, or succession.",
        answer="I recruit Chief Financial Officers and the finance leaders beneath them — VP Finance, Controller, FP&amp;A leadership — through direct, confidential outreach to people who are not applying anywhere. Contingent-first, no up-front retainer, twelve-month guarantee. Whether you searched for CFO recruiters, CFO headhunters, or a CFO executive search firm, this is the same engagement.",
        define_h2="What a CFO recruiter actually does",
        define_p="A CFO recruiter runs a confidential search for a chief financial officer on a company’s behalf: defining the finance mandate, mapping the narrow market of finance leaders who have done that work at a comparable stage, approaching them directly, and managing the process through references and offer. The good ones recruit the seat, not the title — because the CFO who takes a company through its first audit is not the CFO who takes it through a sale.",
        why_h2="Why a CFO search is different from a finance hire",
        why_p="A CFO decision is a board decision, not a department decision. The right candidate is usually running finance somewhere else, is not reading job posts, and will not take a first call from a generic recruiter. The mandate also changes by stage, by ownership structure, and by what the CEO is not getting today. I start by defining which CFO you actually need before I touch the market.",
        fits=[
            ("First CFO for a scaling company", "For founder-led or growth-stage companies moving from a Controller or fractional finance lead to a full CFO who owns capital, board reporting, and the operating plan."),
            ("Sponsor-backed CFO searches", "For private-equity portfolio companies where the sponsor wants a CFO who has lived inside a value-creation plan, a lender relationship, and an exit process."),
            ("Confidential CFO replacement", "For boards and CEOs who need to replace a sitting CFO without the organization, the lender, or the market knowing a search is open."),
            ("VP Finance, Controller, and FP&amp;A leadership", "For the seats directly under the CFO, where the wrong hire shows up in the close, the forecast, and the board deck within a quarter."),
        ],
        steps_h2="How I run a CFO search",
        steps_intro="Every CFO search here follows the same six steps. The person who takes the brief is the person who does them.",
        steps=[
            "Mandate — the next finance milestones, the board’s expectations, the reporting line, and what the CEO is not getting today.",
            "Market map — the narrow set of finance leaders who have owned those milestones at a comparable stage and ownership structure.",
            "Direct outreach — personal, confidential approaches to sitting CFOs and finance leaders. Nothing is posted.",
            "Calibrated shortlist — assessed against the mandate rather than the title, with a written view of fit, risks, and motivation.",
            "References with the people who lived it — the CEO, board member, or sponsor who watched the audit, the raise, or the exit happen.",
            "Offer and start — I manage the offer to a signed acceptance, stay through the start date, and every placement carries a twelve-month guarantee.",
        ],
        roles_h2="Roles I recruit",
        roles=[
            "Chief Financial Officer — first-time, sponsor-backed, pre-IPO, public-company, and turnaround profiles",
            "VP Finance and Head of Finance",
            "Corporate Controller and Chief Accounting Officer",
            "VP FP&amp;A and Head of Financial Planning",
            "Treasurer and VP Corporate Development, where the CFO mandate calls for it",
        ],
        compare_h2="CFO recruiters, CFO headhunters, CFO search firm — what the labels mean",
        compare=[
            ("CFO recruiters", "The broadest label. It can mean direct outreach to sitting finance leaders or sorting applicants from a job post. Ask which one you are buying."),
            ("CFO headhunters", "Signals a direct, confidential approach to finance leaders who are not looking. That is how every CFO search here runs."),
            ("CFO executive search firm / CFO search firm", "Signals a full search process, and often a retainer before it starts. Here the process is the same — mandate, market map, outreach, calibrated slate — without the up-front retainer."),
        ],
        check_h2="How to choose a CFO recruiter — six questions to ask",
        check_intro="Lists of the top CFO recruiting firms will not tell you who will run your search. These questions will.",
        checks=[
            "Who runs the search after the intake call — the person you are talking to, or a research team?",
            "Which CFO profile do they think you need — first-time, sponsor-backed, pre-IPO, turnaround — and why?",
            "How do they reach sitting CFOs who are not looking, and how do they keep the search confidential?",
            "How do they verify a candidate’s finance milestones — the audit, the raise, the exit — beyond the résumé?",
            "What do they recommend for the seat under the CFO, and can they run both searches together?",
            "Is there an up-front retainer, and what is the guarantee if the placement leaves?",
        ],
        faqs=[
            ("What are the top CFO recruiting firms?",
             "The large global firms — Korn Ferry, Spencer Stuart, Heidrick &amp; Struggles — run retained CFO practices built for public-company and global mandates. Below that, the useful question is not who sits at the top of a list but who will run your search: the person who took the brief, or a team you never meet. Use the six questions above on any firm, including me."),
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
        subhead="Contingent-first executive search for private equity sponsors and their portfolio companies — CEO, CFO, COO, and the functional leaders a value-creation plan depends on.",
        answer="I run confidential leadership searches for private equity firms and the companies they own: portfolio-company CEOs, CFOs, COOs, CROs, and the operating leaders who have to deliver the plan the deal was underwritten on. Direct outreach to people who are not looking, an exclusive mandate, no up-front retainer, twelve-month guarantee.",
        define_h2="What a private equity search firm does",
        define_p="A private equity search firm recruits for one of two different markets. One places investment professionals into funds. The other — this one — recruits the leaders who run portfolio companies: CEO, CFO, COO, CRO, and the operating executives a value-creation plan depends on. If you are a candidate trying to break into a fund, this page will not help you. If you are a sponsor or a portfolio-company board with a seat to fill, it will.",
        why_h2="Why sponsor-backed searches run differently",
        why_p="A portfolio-company hire has a clock on it. The plan was underwritten with a leadership assumption, the board meets monthly, and every quarter without the right operator is a quarter of value not created. The candidate market is also specific: leaders who have worked inside a sponsor-owned company know what a board deck, a lender covenant, and an exit process actually demand. I search that market directly rather than hoping it applies.",
        fits=[
            ("Post-close leadership upgrades", "For the CEO, CFO, or COO change a sponsor decided on during diligence and wants filled early in the hold period, quietly and without a public search."),
            ("Portfolio-company CFO and finance leadership", "For companies that need a CFO who has run a lender relationship, an add-on integration, and a sale process — and can build the finance function underneath."),
            ("Commercial and operating leaders for the plan", "For the CRO, VP Sales, COO, or VP Operations seat that carries the revenue or margin assumption in the value-creation plan."),
            ("Confidential searches around a transaction", "For mandates that cannot be visible before a signing, a refinancing, or a founder transition is announced."),
        ],
        steps_h2="How I run a private equity search",
        steps_intro="The sponsor’s operating partner and the company’s CEO see the same information at the same time, at every step.",
        steps=[
            "Deal thesis and plan — what the sponsor needs this leader to make true, by when, and with what board support.",
            "Market map — the narrow set of operators who have delivered that inside a sponsor-owned company, at comparable scale.",
            "Direct outreach — personal, confidential approaches. If you brief me during diligence, outreach can begin the day the deal signs.",
            "Calibrated shortlist — assessed against the plan rather than the title, with fit, risks, and motivation written down.",
            "References with the sponsor or board member who was there — the covenant that held, the add-on that integrated, the exit that closed.",
            "Offer and start — managed to a signed acceptance, with a twelve-month guarantee on every placement.",
        ],
        roles_h2="Roles I recruit for sponsors and portfolio companies",
        roles=[
            "Portfolio-company CEO and President",
            "Chief Financial Officer and VP Finance",
            "Chief Operating Officer and VP Operations",
            "Chief Revenue Officer and VP Sales",
            "Functional leaders tied to the value-creation plan — marketing, technology, people",
            "Investment professionals for the fund itself are a different market; if that is the seat, say so on the call and I will tell you whether it is a fit",
        ],
        compare_h2="Private equity headhunters, recruiters, search firms — what the labels mean",
        compare=[
            ("Private equity headhunters", "A direct, confidential approach to operators who are not looking. That is the method here."),
            ("Private equity recruiting firm", "Often means fund-side hiring — associates and VPs for the investment team. Ask which market a firm actually serves before you brief it."),
            ("Private equity executive search firm", "Portfolio-company leadership search, frequently retained. Here it runs contingent-first: same process, no up-front retainer, and the person who took the brief runs it."),
        ],
        check_h2="What to ask a private equity search firm before you engage",
        check_intro="Lists of the best private equity recruiting firms mix fund recruiters with portfolio-leadership firms. These questions sort them.",
        checks=[
            "Do they recruit portfolio-company operators, fund investment staff, or both — and which practice would your search actually get?",
            "Who runs the search after the pitch, and how many portfolio searches is that person carrying right now?",
            "How do they define “PE-ready”, and how do they verify it?",
            "How do they keep the sponsor and the management team aligned during the search?",
            "Can outreach begin at signing, and is there an up-front retainer?",
            "What is the guarantee if the hire does not work out inside the hold period?",
        ],
        faqs=[
            ("What is a PE executive search firm?",
             "A firm that recruits senior leaders for private equity sponsors and the companies they own — portfolio-company CEOs, CFOs, COOs, and the operating executives tied to a value-creation plan. It is a different business from the recruiters who place associates and VPs into funds, although the two are often listed together. I run the portfolio-leadership side, contingent-first, with direct outreach to operators who are not looking."),
            ("Who are the best private equity recruiting firms?",
             "It depends on which market you mean. For placing associates and VPs into funds, the specialist fund recruiters are a separate industry from this page. For portfolio-company leadership, Korn Ferry, Spencer Stuart, and Heidrick &amp; Struggles run retained practices for the largest sponsors. For a defined portfolio seat that needs to start now, without an up-front retainer, with the person who took the brief running it — that is what I do."),
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
        subhead="Confidential, contingent-first executive search for technology leadership — CTO, CIO, VP Engineering, CPO, CISO — and for the executives technology companies need in every function.",
        answer="I run technology executive searches two ways: technology leaders for any company — CTO, CIO, VP Engineering, Head of Product, CISO, VP Data and AI — and the full executive team for technology companies, from CEO and CFO to CRO and CMO. Direct outreach to leaders who are not job-searching, an exclusive mandate, no up-front retainer, twelve-month guarantee.",
        define_h2="What a tech executive search firm does",
        define_p="A tech executive search firm recruits senior technology leaders — CTO, CIO, VP Engineering, Chief Product Officer, CISO — through direct, confidential outreach to people who are building somewhere else and not reading job posts. Some also recruit the whole executive team for technology companies. I do both, and I define the seat before I search, because the CTO market and the VP Engineering market barely overlap.",
        why_h2="Why technology leadership searches go wrong",
        why_p="The best technical leaders are rarely visible. They are shipping somewhere, they are cautious about recruiters, and their peers know their work long before a résumé does. Companies also confuse the seat: the VP Engineering who scales a large team is not the CTO who sets architecture and talks to the board, and hiring one when you needed the other costs a year. I define the seat first, then search the specific market for it.",
        fits=[
            ("CTO, CIO, and VP Engineering", "For companies that need a technology leader who can own architecture, delivery, and the engineering organization at the next stage of scale — or a CIO who runs technology as a business function."),
            ("Product, data, AI, and security leadership", "For Chief Product Officer, VP Product, VP Data, Head of AI, and CISO seats where the market is narrow and the wrong hire is expensive to undo."),
            ("Executive teams for technology companies", "For software and technology businesses hiring a CEO, CFO, CRO, CMO, or COO who has operated in a product-led, recurring-revenue company."),
            ("Confidential technology leadership replacements", "For boards and CEOs replacing a sitting technology leader without unsettling the engineering team or the market."),
        ],
        steps_h2="How I run a technology executive search",
        steps_intro="Six steps, run by the person who took your brief.",
        steps=[
            "Seat definition — what the business needs this leader to build, own, or fix; the reporting line; how the board and the engineering team will judge success.",
            "Market map — the narrow set of leaders who have done that specific work at a comparable stage and scale.",
            "Direct outreach — personal, confidential approaches to people who are not looking. Nothing is posted.",
            "References with the people who built alongside them — engineers who reported to them, peers who depended on their systems, executives who judged their delivery.",
            "Calibrated shortlist — assessed against the seat definition, with fit, risks, and motivation written down.",
            "Offer, equity questions, and close — managed to a signed acceptance, with a twelve-month guarantee on every placement.",
        ],
        roles_h2="Roles I recruit",
        roles=[
            "Chief Technology Officer, Chief Information Officer, Chief Digital Officer",
            "VP Engineering, Head of Engineering, VP Platform and Infrastructure",
            "Chief Product Officer, VP Product",
            "VP Data, Head of AI and Machine Learning, Chief Data Officer",
            "Chief Information Security Officer, VP Security",
            "CEO, CFO, CRO, CMO, and COO for software and technology companies",
        ],
        compare_h2="CTO, VP Engineering, CIO, CPO — which seat do you actually need?",
        compare=[
            ("CTO", "Owns architecture, technical strategy, and technology’s voice with the board, customers, and investors."),
            ("VP Engineering", "Owns delivery, hiring, process, and the engineering managers. Most scaling companies need this seat and post the other one."),
            ("CIO", "Runs technology as a business function: systems, security, vendors, and the internal roadmap."),
            ("CPO / VP Product", "Owns what gets built and why. The seat that has to pair with engineering leadership, not compete with it."),
        ],
        check_h2="What to ask a tech executive search firm before you sign",
        check_intro="Lists of the top technology executive search firms will not tell you who will run your search. These questions will.",
        checks=[
            "Which seat do they think you need — CTO or VP Engineering — and on what evidence?",
            "How do they evaluate a technical leader they cannot code-test?",
            "Who runs the search after the pitch — the person you spoke to, or a research team?",
            "How do they handle equity-heavy offers and candidates who ask hard questions about runway and capital?",
            "Do they search the seat nationally and remote-first, or only where they have an office?",
            "Is there an up-front retainer, and what is the guarantee if the hire leaves?",
        ],
        faqs=[
            ("CTO or VP Engineering — how do I know which I need?",
             "Ask what the seat has to own. If the gap is architecture, technical strategy, and representing technology to the board and customers, that is a CTO. If the gap is delivery, hiring, process, and managing engineering managers, that is a VP Engineering. Many companies need the second and post the first. I settle this in the brief, because the two candidate markets barely overlap."),
            ("How long does an executive search typically take?",
             "The phases are fixed — seat definition, market map, outreach, references, shortlist, offer — and the pace is set by how narrow the profile is and how quickly your team can interview. Because the engagement is contingent-first, there is no retainer negotiation delaying the start; market mapping begins the week the brief is agreed. I put a timeline in the brief and report against it."),
            ("How much do executive search firms charge?",
             "Retained firms charge a staged fee that begins with an up-front retainer; contingent firms are paid only when the hire starts. I run contingent-first with no up-front retainer and do not publish fee figures on this site, because the structure depends on the seat. On the call I will set out the structure for your search plainly, before any outreach begins."),
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
        subhead="Contingent-first executive search for founders hiring the leaders who define a function — first VP Sales, first VP Engineering, first CFO, first Head of Marketing, COO.",
        answer="I recruit the first executives and key leaders for venture-backed and founder-led companies — the hires that turn a founder’s job into a function. Direct, confidential outreach to leaders who have built it at your stage, an exclusive mandate, no up-front retainer, twelve-month guarantee.",
        define_h2="What startup recruiters do — and the four kinds you will find",
        define_p="“Startup recruiters” covers four different services, and founders waste months hiring the wrong kind. Job platforms give you applicants to screen. Fractional recruiters sit inside your company and run many requisitions. Agencies fill defined individual-contributor and manager roles from their networks. Executive search finds the leader who will build the function — the first VP Sales, the first VP Engineering, the first CFO. This page is the fourth.",
        why_h2="Why startup executive hiring is a different search",
        why_p="A startup’s first VP is a bet on judgment, not on a résumé. The leader who thrives at a company with no process is not the leader who thrives inside a mature one, and large-company titles are the most common false positive in early-stage hiring. Founders also cannot afford a slow, retained process built for a global corporation. I run a founder-paced search: direct outreach to people who have built the function at your stage, and no up-front retainer.",
        fits=[
            ("Your first VP Sales or Head of Revenue", "For founders moving off founder-led sales who need a leader who has built a team and a repeatable motion at a comparable stage — not a large-company sales executive with a big team behind them."),
            ("Your first VP Engineering or CTO", "For technical founders who need a leader who can scale the team, the process, and the architecture without losing the pace that got the company here."),
            ("Your first CFO or Head of Finance", "For companies moving from bookkeeping and a fractional finance lead to a leader who owns the plan, the board reporting, and the next raise."),
            ("COO, Head of Marketing, and Head of People", "For the seats a founder is still personally covering that need an owner before the next stage."),
        ],
        steps_h2="How to recruit for a startup — the founder’s sequence",
        steps_intro="Whether you run it yourself or with me, the sequence for a leadership hire is the same. Skipping a step is where most startup executive hires go wrong.",
        steps=[
            "Write down what you are doing today that this hire must take over. That is the real job description — not a list of requirements.",
            "Decide the stage-fit profile: someone who has built the function at your stage, not someone who managed it inside a large company.",
            "Settle the offer before outreach: cash, equity, vesting, scope, and the honest story of why now.",
            "Go direct. The leaders you want are not applying anywhere; they are found, approached, and persuaded.",
            "Reference against what they personally built, with the founder or executive who watched them do it — not against the title.",
            "Close with the founder in the room. The best candidates are choosing you, not the role — and the placement carries a twelve-month guarantee.",
        ],
        roles_h2="Roles I recruit for startups",
        roles=[
            "VP Sales, Head of Revenue, Chief Revenue Officer",
            "VP Engineering, CTO, Head of Product",
            "CFO, VP Finance, Head of Finance",
            "COO, Head of Operations",
            "VP Marketing, Head of Marketing",
            "Head of People, VP People",
        ],
        compare_h2="Startup recruiter, platform, fractional, or executive search — which one do you need?",
        compare=[
            ("Job platforms and marketplaces", "You post, candidates apply, you screen. Right for volume roles when you have the time to run the funnel yourself."),
            ("Fractional or embedded recruiters", "A recruiter inside your company for a period, running many requisitions at once. Right when you are hiring dozens of people."),
            ("Recruiting agencies", "Contingent firms filling individual-contributor and manager roles from their networks. Right for speed on a defined role."),
            ("Executive search for startups", "A direct, confidential search for the leader who will build a function. Right for the first VP, the first CFO, the COO — the hires this page is about."),
        ],
        check_h2="What to ask a startup recruiter before you sign",
        check_intro="Lists of the best recruitment agencies for startups mix all four kinds above. These questions tell you which one you are actually buying.",
        checks=[
            "Do they recruit leaders and function-builders, or fill volume roles — and which will your search get?",
            "Who runs the search: the person you spoke to, or a sourcer?",
            "How do they screen out large-company executives who will not thrive at your stage?",
            "How do they handle equity-heavy offers and candidates who ask about runway?",
            "Is there an up-front retainer, and what happens if the hire leaves within the year?",
        ],
        faqs=[
            ("How do you recruit for a startup?",
             "Start with what the founder is doing today that the hire must take over, define the stage-fit profile, settle cash, equity, and scope before outreach, then go direct — the leaders you want are not applying. Reference against what candidates personally built, and close with the founder in the room. That sequence is the search I run; the six steps above spell it out."),
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


def section(h2, body):
    return f"  <section>\n    <h2>{h2}</h2>\n{body}\n  </section>\n"


def render(p, head):
    head = re.sub(r"<title>.*?</title>", f"<title>{p['title']} — Arnold Executive Search</title>", head, count=1, flags=re.S)
    parts = []
    parts.append(section(p["define_h2"], f"    <p>{p['define_p']}</p>"))
    parts.append(section(p["why_h2"], f"    <p>{p['why_p']}</p>"))
    parts.append(section("Where this fits", "\n".join(f"    <h3>{h}</h3><p>{t}</p>" for h, t in p["fits"])))
    steps = "\n".join(f"      <li>{s}</li>" for s in p["steps"])
    parts.append(section(p["steps_h2"], f"    <p>{p['steps_intro']}</p>\n    <ol class=\"role-list\">\n{steps}\n    </ol>"))
    roles = "\n".join(f"      <li>{r}</li>" for r in p["roles"])
    parts.append(section(p["roles_h2"], f"    <ul class=\"role-list\">\n{roles}\n    </ul>"))
    parts.append(section(p["compare_h2"], "\n".join(f"    <h3>{h}</h3><p>{t}</p>" for h, t in p["compare"])))
    checks = "\n".join(f"      <li>{c}</li>" for c in p["checks"])
    parts.append(section(p["check_h2"], f"    <p>{p['check_intro']}</p>\n    <ul class=\"role-list\">\n{checks}\n    </ul>"))
    faqs = "\n".join(
        f'    <div class="faq-item">\n      <div class="faq-q">{q}</div>\n      <div class="faq-a">{a}</div>\n    </div>'
        for q, a in p["faqs"])
    parts.append(section("Frequently asked questions", faqs))
    parts.append(section("Competitive positioning", f'    <div class="compete-block">\n      {COMPETE}\n    </div>\n    <p>{p["compete_p"]}</p>'))
    related = "\n".join(f'      <a href="{href}">{t}</a>' for t, href in p["related"])
    parts.append(section("Related decisions", f'    <div class="related-links">\n{related}\n    </div>'))
    main = "\n".join(parts)
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
  <a href="#">Home</a> &nbsp;/&nbsp; <span>{p['title']}</span>
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

{main}
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
        assert 5 <= len(p["faqs"]) <= 8, (p["slug"], "faq count", len(p["faqs"]))
        for q, a in p["faqs"]:
            n = len(re.sub(r"&amp;", "&", a).split())
            assert 40 <= n <= 100, (p["slug"], q, n)
        body = out.read_text().split("</head>", 1)[1]   # body only; CSS has % units
        for bad in ("$", "%", "PLACEHOLDER", "world-class", "industry-leading", "best-in-class", "unparalleled",
                    "Cowen", "Russell Reynolds", "Egon Zehnder", "JM Search", "Stanton Chase"):
            assert bad not in body, (p["slug"], bad)
        words = len(re.sub(r"<[^>]+>", " ", body).split())
        print(f"wrote {out.name}  ~{words} words")
