# Build spec — Arnold Executive Search top-10 hub pages (9 remaining)

## Reference template (COPY THIS EXACTLY — same CSS, same section order, same class names)
`/home/user/workspace/arnold_hubs/TEMPLATE_REFERENCE_legal_recruiters.html` — this is the Dan-approved prototype for the Legal Recruiters hub under the new Gaea Arnold / Arnold Executive Search brand. Copy its `<head>`, `<style>` block, topbar, breadcrumb, hero structure, author-strip, section layout, FAQ block, competitive-positioning block, related-links grid, and CTA band verbatim — only the content inside changes per hub. Do not redesign, do not change colors/fonts/spacing, do not change the section order.

Photo file: `/home/user/workspace/arnold_hubs/gaea_arnold.jpg` — reference it as `src="gaea_arnold.jpg"` (relative path, same folder) in every page's `<img class="author-photo">` tag.

## Hard rules (non-negotiable)
1. **Full brand swap on all 9 pages.** Gaea Arnold is the sole first-person "I" author. Zero mentions of Dan Poore, Blue Signal Search, Senior Practice Director, or any Dan-specific bio/credential language anywhere in these 9 files. Topbar brand = "Arnold Executive Search" with "GA" monogram, exactly as in the template.
2. **No fabricated facts about Gaea.** The only verified fact about her is: name "Gaea Arnold", title "Executive Search Leader & Founder, Arnold Executive Search", and her photo. Do NOT invent: years of experience, past employers, credentials, certifications, placement counts, client names, testimonials, or sector-specific background beyond what's generic to the hub topic itself.
   - Anywhere the old Dan template had a specific verified Dan/Blue Signal proof claim (e.g. "placed a CUO at a $1B+ GWP platform"), replace with a `[PLACEHOLDER — ...]` block describing exactly what real input is needed, styled with the `.proof-note` or `.flag-note` class (see template). Do not soften this into vague marketing language instead of a placeholder — an honest placeholder is required, not a rewritten unverifiable claim.
   - The "Who is Gaea Arnold?" FAQ answer must stay a `[PLACEHOLDER — ...]` in every file, worded like the template's version.
   - Contact info (email/phone) stays `[PLACEHOLDER email]` / `[PLACEHOLDER phone]` in every file — do not reuse Dan's dpoore@bluesignal.com or his phone number.
3. **Keep the universal, non-Dan-specific claims** that describe the search methodology itself, not Gaea's personal history: contingent-first, no up-front retainer, twelve-month guarantee, confidential/direct outreach methodology, "I run exclusive contingent searches at retained-search execution standards" competitive positioning language. These are positioning claims about how the search runs, not personal credentials, so they carry over as first-person "I" statements for Gaea same as they did for Dan — EXCEPT do not carry over any sentence that implies a specific firm affiliation history (e.g. "this search runs under Blue Signal Search, a national firm...") since that proof-note was Dan-specific and has no Gaea equivalent yet — replace those specific affiliation-proof blocks with `[PLACEHOLDER]` too.
4. **Master voice rules apply** (same as every hub on this site): first-person singular "I", short active sentences, consultative/direct/opinionated tone, no "world-class"/"industry-leading"/"best-in-class"/"unparalleled", no third-person corporate voice, every FAQ answer 40-100 words, 5-8 FAQ questions per hub, competitive positioning only names Heidrick & Struggles / Korn Ferry / Spencer Stuart (never boutique competitors).
5. **Real keyword/city data only** — use the exact city/sub-page names and hub index keyword volumes given below per hub (from Ahrefs, already verified) to build the "Markets covered" city grid section. Do not invent cities not listed.
6. **File naming**: save each as `/home/user/workspace/arnold_hubs/arnold_<hub-slug>.html` using the exact hub_slug given below.

## Per-hub content facts (real data — use these, don't invent additional specifics)

### 1. executive-search-firms (index vol 1,700/mo)
Direct answer angle: Gaea runs exclusive contingent executive search for companies hiring VP-and-above leadership, positioned against large retained firms on speed and lack of up-front retainer.
Cities (from Ahrefs, use these exact ones): Atlanta, Boston, Chicago, Dallas, Washington DC, Denver, Houston, New York City, Philadelphia, San Francisco, Seattle.
Featured roles/sub-segments: C-suite and VP-level generalist leadership search, board-level searches, founder/CEO transition searches, functional VP searches (Sales, Marketing, Finance, Ops).
FAQ angle to include: "How is this different from a large retained search firm?" — contingent-first vs retained fee bands/timelines.

### 2. it-staffing (index vol 1,700/mo)
Direct answer angle: Gaea runs contract, contract-to-hire, and direct-hire IT staffing — developers, infrastructure, cybersecurity, help desk — for companies that can't wait on a generalist staffing agency's pipeline.
Sub-pages/topics (use these exact ones, note these are topic pages not all cities): Contract-to-hire IT staffing, Cybersecurity staffing agency, Help desk staffing agency, plus city pages: Austin, Chicago, Dallas, Houston, Los Angeles, New York City.
Featured roles/sub-segments: Software engineers/developers, infrastructure/cloud engineers, cybersecurity analysts and engineers, help desk/support tiers, IT project managers.
FAQ angle to include: "Contract, contract-to-hire, or direct hire — how do I choose?"

### 3. sales-recruiters (index vol 1,000/mo)
Direct answer angle: Gaea recruits quota-carrying sales talent and sales leadership — AEs, SDRs, sales directors, VP Sales — for companies where a bad sales hire costs a full quarter of pipeline.
Cities: Austin, Boston, Chicago, Dallas, Denver, New York City, San Francisco, Seattle.
Featured roles/sub-segments: SDR/BDR, Account Executive (SMB/Mid-Market/Enterprise), Sales Director, VP Sales/CRO, Sales Engineer.
FAQ angle to include: "How do you evaluate a sales candidate's real track record vs. inflated quota claims?"

### 4. healthcare-staffing (index vol 1,500/mo)
Direct answer angle: Gaea places healthcare staffing across nursing, allied health, and healthcare operations leadership for hospitals, clinics, and healthcare systems facing coverage gaps.
Cities: Atlanta, Chicago, Los Angeles, Orlando.
Featured roles/sub-segments: RN/nursing staff, allied health (PT/OT/imaging techs), healthcare operations leadership, clinical department heads.
FAQ angle to include: "Do you handle travel/contract nursing or only permanent placement?" — answer honestly that this is a placeholder for scope Gaea needs to confirm, don't assume.

### 5. accounting-staffing (index vol 1,600/mo)
Direct answer angle: Gaea places accounting and finance staffing — from AP/AR to Controller-level — for companies scaling finance ops or covering an urgent gap.
Cities: Dallas (only one with real data — "accounting staffing dallas").
Featured roles/sub-segments: AP/AR clerks, staff accountants, senior accountants, Controllers, Accounting Managers.
FAQ angle to include: "Contingent staffing vs. contingent executive search — where's the line for accounting hires?" since this hub spans both staffing-level and leadership-level roles.

### 6. marketing-recruiters (index vol 1,000/mo)
Direct answer angle: Gaea recruits marketing talent and leadership — from content/demand gen specialists to CMO — for companies where marketing ROI accountability is the real hiring bar.
Cities: Atlanta, Boston, Chicago, Dallas, Houston, Minneapolis, New York City, Seattle.
Featured roles/sub-segments: Demand gen/growth marketing, content/brand marketing, product marketing, marketing operations, VP Marketing/CMO.
FAQ angle to include: "How do you screen for marketers who can prove ROI, not just run campaigns?"

### 7. executive-headhunters (index vol 900/mo)
Direct answer angle: Gaea runs confidential executive headhunting — direct, discreet outreach to passive senior candidates who aren't job-searching, for companies that can't risk a public search.
Cities: Chicago, Dallas, Denver, Houston, New York, San Diego, Seattle.
Featured roles/sub-segments: Confidential C-suite replacement, board-sensitive searches, competitor lift-outs, passive-candidate-only searches.
FAQ angle to include: "What's the difference between a headhunter and a recruiter?" — direct outreach to passive/non-searching candidates vs. sourcing from applicants.

### 8. retained-executive-search (index vol 1,300/mo)
Direct answer angle: Gaea offers retained search as an option for board-critical or multi-role founding-team searches, alongside her contingent-first default — this hub should explain the retained model itself and when it's the right call, contrasted honestly against her own contingent-first positioning.
No city sub-pages in the data (single flagship page only) — build this as a single comprehensive hub page without a "Markets covered" city grid section; replace that section with a deeper "Contingent vs. retained — how I decide" section instead.
FAQ angle to include: "When do you recommend retained over contingent?", "What does a retained fee structure look like?" — answer the second one carefully: describe the retained model mechanics (upfront commitment, exclusivity, milestone billing) WITHOUT stating specific dollar amounts or percentages, consistent with the sitewide fee-language lock.

### 9. construction-staffing (index vol 1,000/mo)
Direct answer angle: Gaea places skilled trades and construction labor staffing — electricians, general labor, skilled trades — plus construction staffing leadership, for contractors and developers facing labor shortages.
Cities/topics: Construction labor staffing agency, Houston, Electrician staffing agency, Skilled trades staffing agency.
Featured roles/sub-segments: General construction labor, electricians, skilled trades (plumbers, HVAC techs, carpenters), construction project leadership/superintendents.
FAQ angle to include: "Do you handle both W-2 staffing and 1099/subcontractor placement?" — flag as placeholder if scope isn't confirmed, don't assume.

## Sitewide fee-language lock (applies to ALL 9 pages, no exceptions)
No dollar amounts, percentages, retainer figures, or fee mechanics anywhere. Allowed: "contingent-first", "no up-front retainer", "twelve-month guarantee" (the only quantified claim allowed sitewide). This is a locked project rule — do not include benchmark fee ranges even as "positioning context."

## Output
Save all 9 files to `/home/user/workspace/arnold_hubs/`. When done, write a short `BUILD_LOG.md` in the same folder listing each file created and a one-line confirmation that it followed the template/rules above, plus explicitly flag any hub where you had to deviate from the spec (e.g. retained-executive-search's different section structure) so Dan can review those deviations specifically.
