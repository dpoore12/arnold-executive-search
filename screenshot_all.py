from playwright.sync_api import sync_playwright
import os

files = [
    "arnold_executive-search-firms.html",
    "arnold_it-staffing.html",
    "arnold_sales-recruiters.html",
    "arnold_healthcare-staffing.html",
    "arnold_accounting-staffing.html",
    "arnold_marketing-recruiters.html",
    "arnold_executive-headhunters.html",
    "arnold_retained-executive-search.html",
    "arnold_construction-staffing.html",
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1000, "height": 1400})
    for f in files:
        page.goto(f"http://localhost:5002/{f}")
        page.wait_for_timeout(400)
        out = f"/home/user/workspace/arnold_hubs/shot_{f.replace('.html','')}.png"
        page.screenshot(path=out, full_page=True)
        print(out)
    browser.close()
