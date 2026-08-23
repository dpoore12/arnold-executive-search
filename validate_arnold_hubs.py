from pathlib import Path
import re
from html import unescape
root = Path('/home/user/workspace/arnold_hubs')
for f in sorted(root.glob('arnold_*.html')):
    text=f.read_text()
    faqs=re.findall(r'<div class="faq-a">(.*?)</div>\s*</div>', text, re.S)
    wc=[]
    for x in faqs:
        plain=unescape(re.sub(r'<[^>]+>', ' ', x))
        wc.append(len(re.findall(r"\b[\w’'-]+\b",plain)))
    forb=[]
    for term in ['Dan Poore','Blue Signal','Senior Practice Director','world-class','industry-leading','best-in-class','unparalleled']:
        if term.lower() in text.lower(): forb.append(term)
    money=re.findall(r'\$\s*\d|\b\d+(?:\.\d+)?\s*%|\b\d+\s*(?:percent|percentage)\b',text,re.I)
    print(f.name, 'faqs=',len(faqs),'words=',wc,'forbidden=',forb,'money=',money,'photo=', 'src="gaea_arnold.jpg"' in text, 'title=',re.search(r'<title>(.*?)</title>', text).group(1))
