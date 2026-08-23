from pathlib import Path
import re
from html import unescape
root=Path('/home/user/workspace/arnold_hubs')
expected={
'arnold_executive-search-firms.html':['Executive Search Firms Atlanta','Executive Search Firms Boston','Executive Search Firms Chicago','Executive Search Firms Dallas','Executive Search Firms Washington DC','Executive Search Firms Denver','Executive Search Firms Houston','Executive Search Firms New York City','Executive Search Firms Philadelphia','Executive Search Firms San Francisco','Executive Search Firms Seattle'],
'arnold_it-staffing.html':['Contract-to-hire IT staffing','Cybersecurity staffing agency','Help desk staffing agency','IT Staffing Austin','IT Staffing Chicago','IT Staffing Dallas','IT Staffing Houston','IT Staffing Los Angeles','IT Staffing New York City'],
'arnold_sales-recruiters.html':['Sales Recruiters Austin','Sales Recruiters Boston','Sales Recruiters Chicago','Sales Recruiters Dallas','Sales Recruiters Denver','Sales Recruiters New York City','Sales Recruiters San Francisco','Sales Recruiters Seattle'],
'arnold_healthcare-staffing.html':['Healthcare Staffing Atlanta','Healthcare Staffing Chicago','Healthcare Staffing Los Angeles','Healthcare Staffing Orlando'],
'arnold_accounting-staffing.html':['Accounting Staffing Dallas'],
'arnold_marketing-recruiters.html':['Marketing Recruiters Atlanta','Marketing Recruiters Boston','Marketing Recruiters Chicago','Marketing Recruiters Dallas','Marketing Recruiters Houston','Marketing Recruiters Minneapolis','Marketing Recruiters New York City','Marketing Recruiters Seattle'],
'arnold_executive-headhunters.html':['Executive Headhunters Chicago','Executive Headhunters Dallas','Executive Headhunters Denver','Executive Headhunters Houston','Executive Headhunters New York','Executive Headhunters San Diego','Executive Headhunters Seattle'],
'arnold_construction-staffing.html':['Construction labor staffing agency','Construction Staffing Houston','Electrician staffing agency','Skilled trades staffing agency'],
}
ref=(root/'TEMPLATE_REFERENCE_legal_recruiters.html').read_text()
css=lambda s: re.search(r'<style>(.*?)</style>',s,re.S).group(1)
for f in sorted(root.glob('arnold_*.html')):
    doc=f.read_text()
    body=re.search(r'<body>(.*)</body>',doc,re.S).group(1)
    visible=unescape(re.sub(r'<[^>]+>',' ',body))
    faqs=re.findall(r'<div class="faq-a">(.*?)</div>\s*</div>',body,re.S)
    lens=[]
    for answer in faqs:
        words=re.findall(r"\b[\w’'-]+\b",unescape(re.sub(r'<[^>]+>',' ',answer)))
        lens.append(len(words))
    forbidden=[x for x in ['Dan Poore','Blue Signal','Senior Practice Director','world-class','industry-leading','best-in-class','unparalleled'] if x.lower() in visible.lower()]
    corporate_we=bool(re.search(r'\bwe\b',visible,re.I))
    money=bool(re.search(r'\$\s*\d|\b\d+(?:\.\d+)?\s*%|\b\d+\s*(?:percent|percentage)\b',visible,re.I))
    required_photo='src="gaea_arnold.jpg"' in doc
    required_contact='[PLACEHOLDER email]' in doc and '[PLACEHOLDER phone]' in doc
    css_match=css(doc)==css(ref)
    if f.name=='arnold_retained-executive-search.html':
        links=[]
        market_ok='Contingent vs. retained — how I decide' in body and 'class="city-grid"' not in body
    else:
        markets=re.search(r'<h2>Markets covered</h2>.*?<div class="city-grid">(.*?)</div>',body,re.S).group(1)
        links=[unescape(re.sub(r'<[^>]+>',' ',x)).replace('→','').strip() for x in re.findall(r'<a[^>]*>(.*?)</a>',markets,re.S)]
        market_ok=links==expected[f.name]
    result=all([5<=len(faqs)<=8,all(40<=n<=100 for n in lens),not forbidden,not corporate_we,not money,required_photo,required_contact,css_match,market_ok])
    print(f'{f.name}: {"PASS" if result else "FAIL"}; FAQs={len(faqs)} {lens}; css={css_match}; markets={market_ok}; photo={required_photo}; contact={required_contact}; forbidden={forbidden}; corporate_we={corporate_we}; fee_amount_or_percent={money}')
