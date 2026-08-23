from pathlib import Path
import re
from html import escape

root = Path('/home/user/workspace/arnold_hubs')
template = (root / 'TEMPLATE_REFERENCE_legal_recruiters.html').read_text()
# Preserve the approved document head and CSS byte-for-byte, as requested.
head = template[:template.index('<body>')]

common_intro = '''  <div class="flag-note">
    <strong>Draft note for final review:</strong> [PLACEHOLDER — confirm Gaea Arnold’s real bio, relevant sector background, and verified placement evidence before publication. This page intentionally contains no unverified personal credentials, tenure, client names, or placement history.]
  </div>'''

common_compete = '''  <section>
    <h2>Competitive positioning</h2>
    <div class="compete-block">
      <p><span class="label">Heidrick &amp; Struggles / Korn Ferry / Spencer Stuart</span> — retained engagements and longer process design can be appropriate for a global or board-critical mandate. They are not the only answer when a company needs a focused, contingent-first search to begin without an up-front retainer.</p>
    </div>
    <p>I run exclusive contingent searches at retained-search execution standards — a different engagement model, not a boutique imitation of the retained firms. I use direct outreach, clear calibration, and a twelve-month guarantee.</p>
  </section>'''

common_cta = '''<div class="cta-band">
  <h2>Let’s talk about the seat you’re trying to fill</h2>
  <p>30 minutes. No pitch deck — just the actual brief and whether this is a fit.</p>
  <a href="#" class="cta-button">Schedule a 30-Minute Call</a>
  <div class="cta-contact">[PLACEHOLDER email] &nbsp;·&nbsp; [PLACEHOLDER phone]</div>
</div>

<footer>Arnold Executive Search — Gaea Arnold, Executive Search Leader &amp; Founder</footer>

</body>
</html>
'''

def faq(q, a):
    return f'''    <div class="faq-item">\n      <div class="faq-q">{q}</div>\n      <div class="faq-a">{a}</div>\n    </div>'''

def faq_placeholder(q, text):
    return f'''    <div class="faq-item">\n      <div class="faq-q">{q}</div>\n      <div class="faq-a"><div class="flag-note">[PLACEHOLDER — {text}]</div></div>\n    </div>'''

def section(title, content):
    return f'''  <section>\n    <h2>{title}</h2>\n{content}\n  </section>'''

def city_section(items, hub_label):
    links = '\n'.join(f'      <a href="#">{label} →</a>' for label in items)
    return section('Markets covered', f'''    <p>Current city and topic pages for this hub:</p>
    <div class="city-grid">
{links}
    </div>''')

def related_section(items):
    links = '\n'.join(f'      <a href="#">{item} →</a>' for item in items)
    return section('Related decisions', f'''    <div class="related-links">
{links}
    </div>''')

def author():
    return '''  <div class="author-strip">
    <img class="author-photo" src="gaea_arnold.jpg" alt="Gaea Arnold">
    <div>
      <div class="author-name">Gaea Arnold</div>
      <div class="author-title">Executive Search Leader &amp; Founder, Arnold Executive Search</div>
    </div>
  </div>'''

def page(d):
    title = d['title']
    hero = f'''<body>

<div class="topbar">
  <div class="brand"><span class="monogram">GA</span>Arnold Executive Search</div>
  <div class="topnav">
    <a href="#">Practice Areas</a>
    <a href="#">About Gaea</a>
    <a href="#">Contact</a>
  </div>
</div>

<div class="breadcrumb">
  <a href="#">Home</a> &nbsp;/&nbsp; <span>{title}</span>
</div>

<div class="hero">
  <h1>{title}</h1>
  <p class="subhead">{d['subhead']}</p>
  <div class="direct-answer">
    {d['direct']}
  </div>
  <div class="badges">
    <span class="badge">Contingent-First</span>
    <span class="badge">No Up-Front Retainer</span>
    <span class="badge">Twelve-Month Guarantee</span>
  </div>
{author()}
</div>

<main>

{common_intro}

{section(d['why_title'], d['why'])}

{section('Where this fits', d['fits'] + '''\n    <div class="proof-note">\n      [PLACEHOLDER — real, verified evidence of Gaea’s relevant placements: role, seniority, organization type, and outcome. Do not publish client names, counts, tenure, or any achievement claim until confirmed.]\n    </div>''')}

{section(d['how_title'], d['how'])}

{d['market']}

{section('Frequently asked questions', chr(10).join(d['faqs']))}

{common_compete}

{related_section(d['related'])}

</main>

{common_cta}'''
    # Content only is substituted below the template's immutable head/style.
    return re.sub(r'<title>.*?</title>', f'<title>{title} — Arnold Executive Search</title>', head) + hero

who_faq = lambda topic: faq('Who is Gaea Arnold?', '[PLACEHOLDER — real bio sentence needed. Currently verified only as “Executive Search Leader and Founder, Arnold Executive Search.” A real biography must confirm her professional background, relevant practice focus, and any credentials before publication. No years-of-experience, affiliation, client, or placement claim will be published until verified.]')

data = []

data.append({
'slug':'executive-search-firms','title':'Executive Search Firms','subhead':'Exclusive contingent executive search for VP-and-above leadership, board-level mandates, and founder or CEO transitions.','direct':'I run exclusive contingent executive search for companies hiring VP-and-above leadership. I position the search against large retained firms on speed, direct outreach, and no up-front retainer, with a twelve-month guarantee.',
'why_title':'Why executive search needs a named-market approach','why':'''    <p>Senior leadership mandates rarely become easier after a job post goes live. A credible VP or C-suite candidate is often performing well, not looking publicly, and evaluating risk before taking a first conversation. I start by defining the actual leadership problem, the mandate, and the narrow candidate market that can solve it.</p>
    <div class="flag-note">[PLACEHOLDER — Gaea’s verified executive-search sector focus, geography, and leadership-search background. Confirm before publication; no personal search history is assumed here.]</div>''',
'fits':'''    <h3>C-suite and VP-level leadership search</h3><p>For organizations hiring a senior leader who must set direction, build a function, or take ownership of a material operating outcome.</p>
    <h3>Board-level and transition searches</h3><p>For board-sensitive mandates, founder succession, CEO transition planning, and other leadership changes that require discretion.</p>
    <h3>Functional VP searches</h3><p>For VP Sales, VP Marketing, VP Finance, VP Operations, and adjacent functional leadership seats where the operating context matters as much as the title.</p>''',
'how_title':'How I run an executive search','how':'''    <p>I begin with the business mandate, decision rights, success measures, and the candidate market — not a generic title search. I then conduct direct, confidential outreach, calibrate the shortlist against the actual mandate, and keep the process moving through interviews and close. The engagement is exclusive, contingent-first, and backed by a twelve-month guarantee.</p>''',
'market':city_section([f'Executive Search Firms {x}' for x in ['Atlanta','Boston','Chicago','Dallas','Washington DC','Denver','Houston','New York City','Philadelphia','San Francisco','Seattle']], 'Executive Search Firms'),
'faqs':[
faq('How is this different from a large retained search firm?', 'Large retained firms can be a fit for certain board-critical mandates with a longer process design. I run an exclusive, contingent-first search instead: I focus on the defined leadership market, use direct outreach, and begin without an up-front retainer. The decision should follow the mandate’s urgency, confidentiality, and candidate-market difficulty.'),
faq('What leadership levels do you cover?', 'This hub is designed for VP-and-above leadership mandates, including C-suite, functional VP, board-level, and founder or CEO transition searches. The right scope depends on the authority of the seat and the candidate market. I define that scope before outreach so the process is built around the actual decision, not merely the title.'),
faq('How do you reach executives who are not job-searching?', 'I use direct, confidential outreach rather than relying on an applicant flow. The first conversation is about the mandate, timing, and potential fit, not a public announcement. That approach lets sitting leaders consider a role without exposing their interest to a current employer or a broad professional network.'),
faq('When is an exclusive search the right choice?', 'An exclusive search is most useful when the organization wants one accountable process, clear market coverage, and consistent communication. It is especially helpful when the leadership brief is narrow or confidential. I align on the mandate and outreach approach first, then run the search as a focused process rather than competing submissions.'),
who_faq('executive search')],
'related':['C-suite vs. functional VP search','Board-level search planning','Founder and CEO transition planning','Confidential leadership replacement']
})

data.append({
'slug':'it-staffing','title':'IT Staffing','subhead':'Contract, contract-to-hire, and direct-hire IT staffing for technical teams that need candidates beyond a generalist agency pipeline.','direct':'I run contract, contract-to-hire, and direct-hire IT staffing for companies hiring developers, infrastructure and cloud engineers, cybersecurity talent, help desk teams, and IT project managers. I use direct outreach and focused screening when a generalist staffing pipeline cannot move fast enough.',
'why_title':'Why IT staffing needs technical calibration','why':'''    <p>IT staffing fails when a process treats every technical role as interchangeable. A support-tier hire, cloud engineer, cybersecurity analyst, and software developer each require a different conversation about environment, tools, delivery pressure, and the actual work. I clarify the operating need before I build the candidate market.</p>
    <div class="flag-note">[PLACEHOLDER — confirm Gaea’s verified IT-staffing scope, technical screening inputs, and delivery model before publication. No personal technical credentials or placement results are assumed.]</div>''',
'fits':'''    <h3>Software engineering and development</h3><p>For teams hiring developers and software engineers around a defined product, platform, or delivery need.</p>
    <h3>Infrastructure, cloud, and cybersecurity</h3><p>For infrastructure and cloud engineers, cybersecurity analysts and engineers, and technical roles where environment fit matters.</p>
    <h3>Help desk and IT project delivery</h3><p>For help desk and support tiers, IT project managers, and teams that need reliable coverage without a generic candidate handoff.</p>''',
'how_title':'How I run IT staffing','how':'''    <p>I start with the work, the environment, the level of urgency, and the employment path. From there, I use direct outreach and role-specific screening to distinguish candidates who can operate in the stated setting from those whose experience only resembles it on paper. The process stays focused on speed, fit, and clear communication.</p>''',
'market':city_section(['Contract-to-hire IT staffing','Cybersecurity staffing agency','Help desk staffing agency'] + [f'IT Staffing {x}' for x in ['Austin','Chicago','Dallas','Houston','Los Angeles','New York City']], 'IT Staffing'),
'faqs':[
faq('Contract, contract-to-hire, or direct hire — how do I choose?', 'Choose based on the duration of the work, the certainty of the long-term headcount, and how much performance evidence you need before making a permanent decision. Contract staffing fits defined coverage or project needs. Contract-to-hire adds an evaluation period. Direct hire fits a clearly permanent seat. I clarify those conditions before outreach.'),
faq('What IT roles do you cover?', 'The current scope includes software engineers and developers, infrastructure and cloud engineers, cybersecurity analysts and engineers, help desk and support tiers, and IT project managers. Each search begins with the specific work and environment. I do not treat a broad “IT” title as enough information to run a useful candidate conversation.'),
faq('How do you screen technical candidates?', 'I screen against the operating context supplied for the role: the work to be done, the technology environment, the team interface, and the expected level of ownership. I also assess communication and decision-making because technical capability alone does not confirm that someone can succeed in the team’s actual delivery conditions.'),
faq('Can you support an urgent coverage gap?', 'Urgency changes the process, but it should not erase calibration. I first establish the immediate work, the must-have conditions, and the employment path, then use focused outreach instead of waiting for a generic applicant flow. That creates a clearer path to candidates who understand the assignment and can engage quickly.'),
who_faq('IT staffing')],
'related':['Contract-to-hire staffing decisions','Cybersecurity team hiring','Help desk coverage planning','Direct-hire IT staffing']
})

data.append({
'slug':'sales-recruiters','title':'Sales Recruiters','subhead':'Contingent sales recruiting for quota-carrying talent and sales leadership, from SDR and AE hires through VP Sales and CRO mandates.','direct':'I recruit quota-carrying sales talent and sales leadership — SDRs, BDRs, account executives, sales directors, VP Sales, CROs, and sales engineers — for companies where a bad sales hire can cost a full quarter of pipeline. I focus the search on the real motion, market, and accountability of the seat.',
'why_title':'Why sales hiring needs more than title matching','why':'''    <p>A sales title says little about the motion behind it. The same account executive label can mean a different buyer, cycle, deal size, segment, technical burden, and level of ownership. I define the commercial environment first, then evaluate candidates against the role the business actually needs filled.</p>
    <div class="flag-note">[PLACEHOLDER — Gaea’s verified sales-recruiting background, market focus, and placement evidence. Do not add revenue, attainment, client, or placement claims until they are confirmed.]</div>''',
'fits':'''    <h3>SDR, BDR, and account executive searches</h3><p>For SMB, mid-market, and enterprise account executive roles, plus early-funnel talent that must operate in a specific sales motion.</p>
    <h3>Sales leadership searches</h3><p>For sales directors, VP Sales, and CRO mandates where the leader must shape team execution as well as carry the business target.</p>
    <h3>Sales engineering searches</h3><p>For sales engineers who must translate product and technical context into a credible commercial conversation.</p>''',
'how_title':'How I run a sales search','how':'''    <p>I start by separating the title from the selling environment: buyer, segment, sales cycle, product complexity, territory, handoffs, and management expectations. I then use direct outreach and structured screening to test what a candidate actually owned. The result is a shortlist tied to the commercial brief, not a stack of broadly similar resumes.</p>''',
'market':city_section([f'Sales Recruiters {x}' for x in ['Austin','Boston','Chicago','Dallas','Denver','New York City','San Francisco','Seattle']], 'Sales Recruiters'),
'faqs':[
faq('How do you evaluate a sales candidate’s real track record versus inflated quota claims?', 'I ask for the operating context behind any attainment claim: the segment, buyer, territory, sales cycle, starting conditions, handoffs, and what the candidate personally owned. A number without context does not show repeatability. The goal is to understand the candidate’s actual contribution and whether it maps to the sales motion you need.'),
faq('What sales roles do you recruit?', 'This hub covers SDR and BDR roles, account executives across SMB, mid-market, and enterprise segments, sales directors, VP Sales and CRO mandates, and sales engineers. I calibrate the search to the actual commercial role because title overlap alone can hide major differences in buyer, cycle, product complexity, and responsibility.'),
faq('Do you recruit individual contributors and leaders?', 'Yes. Individual-contributor and leadership searches require different evaluation criteria, but both begin with the commercial reality of the seat. For individual contributors, I focus on the motion and ownership. For leaders, I also assess how the candidate would shape execution, hiring, inspection, and cross-functional decisions.'),
faq('Why use direct outreach for a sales search?', 'Strong sales candidates are often performing in an existing role and are not spending time in public applicant channels. Direct outreach creates a confidential first conversation about the mandate and the commercial environment. It also gives the search a better chance of reaching people whose experience is relevant but not actively marketed.'),
who_faq('sales recruiting')],
'related':['SDR vs. account executive hiring','Enterprise sales hiring','Sales leadership mandate design','Sales engineer search planning']
})

data.append({
'slug':'healthcare-staffing','title':'Healthcare Staffing','subhead':'Healthcare staffing across nursing, allied health, and healthcare operations leadership for hospitals, clinics, and systems managing coverage gaps.','direct':'I place healthcare staffing across nursing, allied health, and healthcare operations leadership for hospitals, clinics, and healthcare systems facing coverage gaps. I focus the search on the specific coverage need, clinical setting, and level of operational responsibility.',
'why_title':'Why healthcare staffing requires setting-specific context','why':'''    <p>Healthcare coverage needs are rarely generic. The clinical setting, patient demand, department workflow, schedule pressure, and leadership interface all shape what a workable candidate match looks like. I begin by clarifying those conditions so the search reflects the actual coverage gap rather than a broad credential label.</p>
    <div class="flag-note">[PLACEHOLDER — confirm Gaea’s verified healthcare-staffing scope, clinical credential-verification process, and sector experience. No clinical expertise, compliance process, or placement history is assumed.]</div>''',
'fits':'''    <h3>RN and nursing staff</h3><p>For nursing coverage needs where the department context and schedule requirements must be clear from the start.</p>
    <h3>Allied health staffing</h3><p>For PT, OT, imaging technicians, and other allied-health roles that support a specific care setting.</p>
    <h3>Healthcare operations and clinical leadership</h3><p>For healthcare operations leadership and clinical department heads responsible for a team, service line, or department outcome.</p>''',
'how_title':'How I run a healthcare staffing search','how':'''    <p>I establish the care setting, coverage requirement, work expectations, and level of responsibility before outreach begins. I then hold candidate conversations against those conditions rather than assuming that a broad role label is enough. This keeps the process anchored to the practical needs of the hospital, clinic, or healthcare system.</p>''',
'market':city_section([f'Healthcare Staffing {x}' for x in ['Atlanta','Chicago','Los Angeles','Orlando']], 'Healthcare Staffing'),
'faqs':[
faq_placeholder('Do you handle travel or contract nursing, or only permanent placement?', 'Gaea must confirm whether travel nursing, contract nursing, permanent placement, or another combination is within scope. The final answer should state only the verified engagement types, any applicable setting limits, and the process for assessing a coverage brief. Do not represent any nursing service as available until this scope is confirmed.'),
faq('What healthcare roles do you cover?', 'The current hub scope includes RN and nursing staff, allied-health professionals such as PT, OT, and imaging technicians, healthcare operations leadership, and clinical department heads. A search begins with the actual care setting and work requirement. I do not assume that one department’s staffing need transfers directly to another.'),
faq('How do you approach a coverage gap?', 'I begin by clarifying what must be covered, where the role sits in the workflow, and what schedule or operational conditions shape success. That makes the outreach brief more useful and helps separate candidates whose background is broadly similar from candidates who can operate in the stated environment.'),
faq('Can you support confidential healthcare leadership searches?', 'Confidentiality is especially important when a leadership search affects a department, care team, or ongoing operational transition. I use direct, discreet outreach rather than a public-first process, then share the mandate only as appropriate in the candidate conversation. The goal is to protect the organization while testing genuine fit.'),
who_faq('healthcare staffing')],
'related':['Nursing coverage planning','Allied-health staffing needs','Healthcare operations leadership search','Clinical department head search']
})

data.append({
'slug':'accounting-staffing','title':'Accounting Staffing','subhead':'Accounting and finance staffing from AP and AR through Controller-level roles for organizations scaling finance operations or covering an urgent gap.','direct':'I place accounting and finance staffing — from AP and AR to Controller-level roles — for companies scaling finance operations or covering an urgent gap. I distinguish the day-to-day staffing need from the leadership mandate so the search matches the level of ownership required.',
'why_title':'Why accounting staffing requires level-specific definition','why':'''    <p>Accounting titles can conceal a wide difference in responsibility. An urgent AP or AR coverage need is not the same problem as a Controller search, and neither should be managed as a generic finance requisition. I start with the work, close-cycle pressure, systems context, and decision authority of the role.</p>
    <div class="flag-note">[PLACEHOLDER — Gaea’s verified accounting and finance search scope, systems background, and placement evidence. No credential, client, or seniority claim is assumed.]</div>''',
'fits':'''    <h3>AP, AR, and staff accounting</h3><p>For operational accounting coverage involving AP and AR clerks, staff accountants, and senior accountants.</p>
    <h3>Accounting management</h3><p>For Accounting Managers who need to own a team, process, or portion of the close and reporting environment.</p>
    <h3>Controller-level leadership</h3><p>For Controller mandates that combine accounting accountability with finance-operations leadership.</p>''',
'how_title':'How I run an accounting staffing search','how':'''    <p>I clarify whether the seat is primarily a coverage assignment, a permanent operations hire, or a leadership mandate. Then I assess candidates against the work, systems environment, close-cycle expectations, and required level of judgment. That prevents a staffing-level process from being used for a Controller-level decision, or the reverse.</p>''',
'market':city_section(['Accounting Staffing Dallas'], 'Accounting Staffing'),
'faqs':[
faq('Contingent staffing versus contingent executive search — where is the line for accounting hires?', 'The line is the level and nature of the mandate, not simply the department name. A focused AP, AR, or staff-accountant coverage need is a staffing assignment. A Controller or accounting-leadership mandate may require an executive-search approach because it carries broader decision authority. I define the role’s ownership before choosing the process.'),
faq('What accounting roles do you cover?', 'The current scope includes AP and AR clerks, staff accountants, senior accountants, Controllers, and Accounting Managers. I start by clarifying the actual work, systems context, and level of ownership. That is important because similar titles can represent very different needs across finance organizations and growth stages.'),
faq('Can you help with an urgent accounting gap?', 'Yes, provided the brief identifies the work that cannot wait, the required systems or process context, and the expected employment path. I use that information to focus outreach and screening. An urgent gap still benefits from a clear definition, because a fast process without calibration often creates a second hiring problem later.'),
faq('How do you assess Controller candidates?', 'For a Controller-level mandate, I assess the accounting responsibilities, leadership expectations, systems environment, close-cycle demands, and decision authority attached to the role. The title alone is not enough. The candidate conversation has to show whether the person can operate in the organization’s actual finance environment and take ownership at the needed level.'),
who_faq('accounting staffing')],
'related':['AP and AR coverage planning','Staff accountant hiring','Accounting Manager search','Controller-level search']
})

data.append({
'slug':'marketing-recruiters','title':'Marketing Recruiters','subhead':'Marketing recruiting from content and demand generation specialists to VP Marketing and CMO leadership, with ROI accountability at the center of the brief.','direct':'I recruit marketing talent and leadership — from content and demand-generation specialists to VP Marketing and CMO roles — for companies where marketing ROI accountability is the real hiring bar. I define the business outcome, operating context, and ownership before I build the candidate market.',
'why_title':'Why marketing hiring must begin with accountability','why':'''    <p>Marketing titles are broad; the accountability behind them is not. A demand-generation role, product-marketing mandate, brand leadership seat, and CMO search each require a different definition of the business result, decision rights, channels, and cross-functional role. I make that accountability explicit before outreach.</p>
    <div class="flag-note">[PLACEHOLDER — Gaea’s verified marketing-recruiting sector focus, functional experience, and placement evidence. Do not add campaign, ROI, client, or placement claims until they are confirmed.]</div>''',
'fits':'''    <h3>Demand generation and growth marketing</h3><p>For roles responsible for building demand, improving growth execution, and connecting marketing activity to a defined business outcome.</p>
    <h3>Content, brand, and product marketing</h3><p>For specialists and leaders who must articulate a market position, support sales, or connect product context to customer-facing work.</p>
    <h3>Marketing operations and executive leadership</h3><p>For marketing-operations roles, VP Marketing mandates, and CMO searches where systems, measurement, and leadership all matter.</p>''',
'how_title':'How I run a marketing search','how':'''    <p>I start with the outcome the business expects marketing to influence, then map the role’s scope, channels, systems, and collaboration points. I use direct outreach and structured conversations to test whether candidates can explain their contribution with evidence and context. That keeps the shortlist tied to accountability, not campaign vocabulary.</p>''',
'market':city_section([f'Marketing Recruiters {x}' for x in ['Atlanta','Boston','Chicago','Dallas','Houston','Minneapolis','New York City','Seattle']], 'Marketing Recruiters'),
'faqs':[
faq('How do you screen for marketers who can prove ROI, not just run campaigns?', 'I ask candidates to explain the business context, target audience, operating constraints, measurement approach, and their own role in the result. A campaign description without ownership or outcome context is not enough. The goal is to understand how the marketer makes decisions, connects activity to accountability, and would work in your environment.'),
faq('What marketing roles do you recruit?', 'The scope includes demand generation and growth marketing, content and brand marketing, product marketing, marketing operations, VP Marketing, and CMO mandates. I calibrate each search around the business outcome and operating model because the same title can carry very different responsibilities across companies, markets, and growth stages.'),
faq('Do you recruit specialists and marketing leaders?', 'Yes. Specialist roles require clarity on the work, systems, channels, and collaboration model. Leadership mandates also require a view of decision rights, team design, and accountability. I separate those requirements at the start so a candidate is not evaluated against a vague blend of execution and executive expectations.'),
faq('Why does direct outreach matter for marketing searches?', 'Strong marketers and marketing leaders are often engaged in existing work and may not be visible in an applicant flow. Direct outreach allows a focused, confidential discussion about the business problem and role scope. It also gives the process a better chance to reach candidates whose background fits the mandate but is not publicly signaled.'),
who_faq('marketing recruiting')],
'related':['Demand generation hiring','Product marketing search planning','Marketing operations hiring','VP Marketing and CMO search']
})

data.append({
'slug':'executive-headhunters','title':'Executive Headhunters','subhead':'Confidential executive headhunting for board-sensitive, passive-candidate, and competitor-sensitive leadership searches.','direct':'I run confidential executive headhunting: direct, discreet outreach to passive senior candidates who are not job-searching. It is designed for companies that cannot risk a public search, including confidential C-suite replacements, board-sensitive mandates, competitor lift-outs, and passive-candidate-only searches.',
'why_title':'Why confidential headhunting is different','why':'''    <p>A confidential executive search cannot depend on public visibility. The candidate market may include leaders who would never apply, while the organization may need to avoid signaling a replacement, strategic shift, or competitor approach. I use targeted outreach and careful information control to open credible conversations without turning the mandate into a public event.</p>
    <div class="flag-note">[PLACEHOLDER — Gaea’s verified confidential-search background and placement evidence. Confirm actual experience before publication; no prior confidential mandate, client, or competitor claim is assumed.]</div>''',
'fits':'''    <h3>Confidential C-suite replacement</h3><p>For situations where an organization needs to explore a senior replacement without publicizing the change.</p>
    <h3>Board-sensitive searches</h3><p>For mandates where board visibility, leadership succession, or the nature of the role requires a more controlled process.</p>
    <h3>Competitor lift-outs and passive-candidate-only searches</h3><p>For organizations seeking a specific leadership profile from a defined market while keeping outreach direct and discreet.</p>''',
'how_title':'How I run an executive headhunting search','how':'''    <p>I begin by defining the mandate, confidentiality boundaries, and named candidate market. Outreach is direct and individual rather than public-first. I share the opportunity with care, assess fit against the actual leadership brief, and keep the client informed without widening exposure unnecessarily. The process is designed for thoughtful conversations, not broad signaling.</p>''',
'market':city_section([f'Executive Headhunters {x}' for x in ['Chicago','Dallas','Denver','Houston','New York','San Diego','Seattle']], 'Executive Headhunters'),
'faqs':[
faq('What’s the difference between a headhunter and a recruiter?', 'A headhunter’s core method is direct outreach to passive senior candidates who are not actively job-searching. A recruiter may also manage applicants or inbound interest. For confidential executive mandates, I lead with targeted, discreet outreach because the strongest relevant leaders are often employed and should not have to signal interest publicly.'),
faq('How do you protect a confidential search?', 'I define confidentiality boundaries before outreach, then approach candidates individually and with appropriate discretion. I do not treat public visibility as the default. The candidate conversation is staged around what can be shared responsibly, while the process stays focused on testing fit without unnecessary exposure for the organization or the candidate.'),
faq('Can you approach candidates at competitors?', 'Competitor lift-outs are within the hub’s featured search types, but every mandate requires careful boundaries and an accurate brief. I use direct outreach to discuss the opportunity confidentially, not mass contact. The goal is to identify relevant leaders and assess genuine interest without turning a targeted market approach into public noise.'),
faq('When should a search be kept off public job boards?', 'A public posting is usually the wrong first move when the mandate involves a confidential replacement, board sensitivity, a defined competitor market, or a passive-candidate-only brief. In those situations, direct outreach lets the organization control the message, test the market discreetly, and avoid broadcasting a leadership change before it is ready.'),
who_faq('executive headhunting')],
'related':['Confidential C-suite replacement','Board-sensitive leadership search','Competitor lift-out planning','Passive-candidate executive search']
})

data.append({
'slug':'retained-executive-search','title':'Retained Executive Search','subhead':'A clear guide to retained executive search, when it is the right option, and how it compares with my contingent-first default.','direct':'I offer retained executive search as an option for board-critical mandates or multi-role founding-team searches, alongside my contingent-first default. The right model depends on the importance, complexity, confidentiality, and exclusivity required by the mandate — not on a one-size-fits-all process.',
'why_title':'When retained executive search is the right call','why':'''    <p>Retained search can be the right model when a board-critical mandate, a high-stakes leadership transition, or a multi-role founding-team build requires a dedicated, exclusive process. It is not automatically the right choice for every senior search. I compare the mandate’s urgency, complexity, candidate market, and governance needs before recommending a model.</p>
    <div class="flag-note">[PLACEHOLDER — confirm Gaea’s verified retained-search experience and scope before publication. No retained mandate history, client example, or placement outcome is assumed.]</div>''',
'fits':'''    <h3>Board-critical leadership mandates</h3><p>For searches where board involvement, succession, or the consequences of a missed leadership decision call for an intentionally dedicated process.</p>
    <h3>Multi-role founding-team searches</h3><p>For a coordinated set of founding-team or early leadership hires where the work benefits from a shared market map and close calibration.</p>
    <h3>Complex or highly confidential searches</h3><p>For mandates with a narrow candidate market, sensitive circumstances, or a need for sustained exclusivity and governance.</p>''',
'how_title':'How I run a retained executive search','how':'''    <p>A retained search begins with a committed, exclusive mandate, a detailed role definition, and agreement on how the process will be governed. I build the candidate market, conduct direct outreach, calibrate the slate, and manage the process through decision and close. The model is designed for work that needs sustained attention and clear shared commitment.</p>''',
'market':section('Contingent vs. retained — how I decide', '''    <p>I use contingent-first as the default when the mandate can move through a focused, exclusive search without an up-front retainer. I recommend considering retained search when the role is board-critical, the search is unusually complex or confidential, or several founding-team roles need a coordinated process.</p>
    <h3>Contingent-first</h3><p>Best suited to a defined executive mandate where the organization wants an exclusive, direct-outreach process that begins without an up-front retainer and carries a twelve-month guarantee.</p>
    <h3>Retained</h3><p>Best suited to a mandate requiring a committed, exclusive process, deeper governance, and sustained attention across a complex leadership decision or multi-role build.</p>'''),
'faqs':[
faq('When do you recommend retained over contingent?', 'I recommend considering retained when a mandate is board-critical, unusually complex, highly confidential, or part of a coordinated multi-role founding-team build. Those conditions can justify a dedicated, exclusive process with deeper governance. For a defined executive mandate that can move quickly, my contingent-first approach may be the more practical starting point.'),
faq('What does a retained fee structure look like?', 'A retained model begins with an up-front commitment and an exclusive mandate. The engagement then follows defined checkpoints and agreed milestone billing as the search progresses. The exact structure should be discussed for the particular mandate. This page does not publish dollar amounts, percentages, retainer figures, or other fee details.'),
faq('Is retained search always more thorough?', 'No. Thoroughness comes from the clarity of the mandate, the quality of market mapping, direct outreach, calibration, and decision process. Retained search is useful when the assignment needs sustained, dedicated attention and governance. An exclusive contingent-first search can also be rigorous when the leadership brief is defined and the candidate market can be reached directly.'),
faq('Can a contingent-first search still be confidential?', 'Yes. Confidentiality depends on how the search is designed and conducted, not solely on the engagement model. I use direct, discreet outreach and agree on what can be shared at each stage. For a highly sensitive or board-critical mandate, I assess whether the additional commitment and governance of retained search is the better fit.'),
faq('What is the first decision before choosing a search model?', 'The first decision is what the mandate actually requires: the role’s importance, complexity, confidentiality, candidate-market difficulty, and decision process. I use those conditions to compare contingent-first and retained approaches. The point is not to force a model onto every search; it is to choose a process that matches the risk and scope of the leadership decision.'),
who_faq('retained executive search')],
'related':['Contingent-first executive search','Board-critical search planning','Founding-team leadership build','Confidential leadership mandate']
})

data.append({
'slug':'construction-staffing','title':'Construction Staffing','subhead':'Construction labor and skilled-trades staffing, plus construction leadership search, for contractors and developers facing labor shortages.','direct':'I place skilled trades and construction labor staffing — electricians, general labor, skilled trades, and construction staffing leadership — for contractors and developers facing labor shortages. I start with the actual site, trade, schedule, and leadership need so the search reflects the work that must be done.',
'why_title':'Why construction staffing starts with the worksite','why':'''    <p>Construction staffing needs are shaped by the trade, site conditions, schedule, safety context, project phase, and supervision structure. A broad request for labor does not tell a candidate what the work demands or tell a client whether the match can hold. I clarify the specific job context before outreach begins.</p>
    <div class="flag-note">[PLACEHOLDER — confirm Gaea’s verified construction-staffing scope, trade coverage, compliance process, and placement evidence. No safety credential, worker classification, client, or project claim is assumed.]</div>''',
'fits':'''    <h3>General construction labor</h3><p>For contractors and developers who need labor coverage tied to a defined site, project phase, and schedule.</p>
    <h3>Electricians and skilled trades</h3><p>For electricians, plumbers, HVAC technicians, carpenters, and other skilled trades where the work requirements must be clear.</p>
    <h3>Construction leadership</h3><p>For construction project leadership and superintendent roles that carry site, crew, and project-delivery responsibility.</p>''',
'how_title':'How I run a construction staffing search','how':'''    <p>I begin with the trade or role, project context, schedule pressure, worksite expectations, and leadership interface. I then use focused outreach and screening to distinguish broadly related experience from relevant construction work. This keeps the process connected to the practical conditions of the project rather than an undifferentiated labor request.</p>''',
'market':city_section(['Construction labor staffing agency','Construction Staffing Houston','Electrician staffing agency','Skilled trades staffing agency'], 'Construction Staffing'),
'faqs':[
faq_placeholder('Do you handle both W-2 staffing and 1099 or subcontractor placement?', 'Gaea must confirm which worker classifications and placement arrangements are within scope. The final answer should state only the verified options, the relevant worksite or trade limits, and any required compliance process. Do not represent W-2 staffing, 1099 placement, or subcontractor placement as available until the service scope is confirmed.'),
faq('What construction roles do you cover?', 'The current scope includes general construction labor, electricians, skilled trades such as plumbers, HVAC technicians, and carpenters, plus construction project leadership and superintendents. I start with the specific work and site context. That matters because a trade label alone does not establish the practical requirements of the assignment.'),
faq('How do you approach a construction labor shortage?', 'I first clarify the role or trade, project phase, schedule pressure, worksite conditions, and level of supervision. That information creates a more useful outreach brief and helps screen for relevant experience. A focused process is more productive than treating every available construction candidate as interchangeable labor coverage.'),
faq('Do you recruit construction leadership as well as trades?', 'Yes. Construction project leadership and superintendent roles are part of this hub’s stated scope alongside general labor and skilled trades. Leadership searches require additional clarity about site ownership, team coordination, project-delivery expectations, and decision authority. I separate those leadership requirements from trade-staffing needs before building the candidate market.'),
who_faq('construction staffing')],
'related':['Construction labor staffing','Electrician staffing needs','Skilled-trades coverage','Construction superintendent search']
})

for d in data:
    out = root / f"arnold_{d['slug']}.html"
    out.write_text(page(d))
    print(out)
