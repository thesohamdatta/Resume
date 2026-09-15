# Agent Prompts for Job Application Research Workflow

## Meta-Instructions for All Agents

**Anti-AI-Slop Protocol:**
- No generic advice ("be authentic", "show passion", "be yourself")
- No obvious statements ("proofread your email", "check for typos")
- No unsourced claims
- No buzzwords without concrete examples
- Prioritize **specific tactics** over platitudes
- Extract **direct quotes** from sources
- Flag **conflicting advice** and resolve it

**Source Quality Standards:**
- Prioritize 2020+ sources (current hiring practices)
- Credible institutions: MIT, Stanford, Harvard, Y Combinator, First Round Review
- Practitioner sources: recruiters, hiring managers, founders with hiring experience
- Avoid: generic career advice sites, AI-generated listicles, content marketing

**Output Structure:**
```markdown
# [Domain] Research

## Summary
[3-5 key takeaways, specific and actionable]

## Core Principles
[Fundamental truths backed by multiple sources]

## For Startups
[Specific tactics with examples]

## For MNCs
[Specific tactics with examples]

## Source Synthesis
[Where sources agree, where they conflict, resolution]

## Direct Quotes
[Key insights verbatim with attribution]

## Red Flags
[What NOT to do, common mistakes]

## Application to Soham
[How this applies to AI/ML role search specifically]
```

**sources.yaml format:**
```yaml
sources:
  - id: unique_id
    type: article|book|newsletter|blog|video
    title: "Exact Title"
    author: "Author Name"
    url: "https://..."
    date: "YYYY-MM-DD"
    credibility: high|medium|low
    key_insight: "One-sentence takeaway"
```

---

## Agent 1: Cold Email Research

**Domain:** Cold emailing for startup founder outreach and MNC recruiter outreach

**Objective:** Research email tactics that get responses from founders and recruiters in AI/ML roles

**Key Questions:**
1. Subject line formulas that get opened (startup vs MNC)
2. Email structure: hook → proof → ask
3. Optimal length (word count, paragraph count)
4. Follow-up cadence (when, how many times)
5. When to include resume vs portfolio link vs GitHub
6. Personalization depth required (generic vs hyper-specific)
7. Best time to send (day of week, time of day)
8. How to reference their work without sounding fake

**Target Sources:**
- Y Combinator essays on hiring ("How to Hire Engineers", founder posts)
- First Round Review hiring guides
- Lenny's Newsletter (recruiter perspective)
- Gergely Orosz (The Pragmatic Engineer)
- Startup founder Twitter threads on cold emails that worked
- Hacker News "Ask HN" threads on cold email success
- LinkedIn posts from technical recruiters

**Search Strategy:**
- "cold email to startup founder" site:ycombinator.com
- "cold email got me hired" site:news.ycombinator.com
- "how to email recruiters" Lenny Rachitsky
- "technical recruiting cold outreach" Gergely Orosz
- "founder cold email tips" site:firstround.com

**Quality Gate:**
- Minimum 8 sources
- At least 3 practitioner sources (founders/recruiters who hired someone from cold email)
- At least 2 real email examples that worked
- Startup vs MNC differences explicitly stated

**Output:** `research/job_application/cold_email/research.md` + `sources.yaml`

---

## Agent 2: Cover Letter Research

**Domain:** Cover letter writing for AI/ML roles

**Objective:** Determine when cover letters matter, what to include, startup vs MNC differences

**Key Questions:**
1. Do startups read cover letters? (hypothesis: mostly no)
2. Do MNCs read cover letters? (hypothesis: yes, especially for ATS)
3. Structure: opening hook, body content, closing ask
4. Optimal length (1 paragraph vs 1 page)
5. How to connect portfolio to job description
6. When to skip cover letters entirely
7. ATS optimization for MNCs
8. Personalization: company-specific vs template

**Target Sources:**
- Harvard Career Services guides
- Stanford career center cover letter resources
- MIT career advising (engineering-specific)
- Tech recruiter blogs (what they actually read)
- Y Combinator work at a startup advice
- LinkedIn posts from hiring managers

**Search Strategy:**
- "do startups read cover letters" site:ycombinator.com
- "cover letter for engineers" site:harvard.edu
- "ATS cover letter optimization" technical recruiting
- "hiring manager cover letter" site:linkedin.com

**Quality Gate:**
- Minimum 8 sources
- At least 2 recruiter perspectives
- Startup vs MNC differences explicit
- Clear guidance on when to skip entirely

**Output:** `research/job_application/cover_letter/research.md` + `sources.yaml`

---

## Agent 3: LinkedIn Profile Research

**Domain:** LinkedIn profile optimization for AI/ML engineers

**Objective:** Maximize recruiter search visibility and network reach

**Key Questions:**
1. Headline formula for AI/ML roles (keywords + positioning)
2. About section structure (length, tone, content)
3. How to list projects vs experience (which first?)
4. Skills endorsement strategy (which skills to prioritize)
5. Recommendations: who to ask, what to request
6. Featured section: what to showcase
7. Recruiter search filters (what keywords they use)
8. Profile completeness score impact

**Target Sources:**
- LinkedIn's official optimization guides
- Austin Belcak (LinkedIn expert, "Cultivated Culture")
- Tech recruiter LinkedIn posts
- "How I got hired" LinkedIn threads
- Wonsulting (LinkedIn optimization specialists)
- Gergely Orosz on LinkedIn for engineers

**Search Strategy:**
- "LinkedIn headline for engineers" Austin Belcak
- "LinkedIn optimization" site:linkedin.com/business/talent
- "recruiter LinkedIn search" technical hiring
- "LinkedIn profile AI engineer" optimization

**Quality Gate:**
- Minimum 8 sources
- At least 3 recruiter perspectives (what they search for)
- Specific keyword lists for AI/ML roles
- Before/after examples

**Output:** `research/job_application/linkedin_profile/research.md` + `optimization.md` + `sources.yaml`

---

## Agent 4: Startup Application Tactics

**Domain:** How to apply to startups (wearable AI, personal AI, voice AI)

**Objective:** Optimal application strategy for early-stage companies

**Key Questions:**
1. Direct founder email vs application portal (which gets more responses?)
2. Where to find startup job postings (YC, AngelList, personal networks)
3. How to research founders before emailing
4. Application volume per week (realistic targets)
5. Follow-up strategy (timing, cadence)
6. Portfolio vs resume (what to send first)
7. Referral vs cold outreach success rates
8. How to identify companies actively hiring

**Target Sources:**
- Y Combinator "Work at a Startup"
- First Round Review hiring posts
- Hacker News "Who's Hiring" threads
- Startup founder blog posts on hiring
- AngelList/Wellfound best practices
- Indie Hackers hiring discussions

**Search Strategy:**
- "how to apply to startups" site:ycombinator.com
- "startup job search strategy" site:firstround.com
- "cold email startup founder" success stories
- "YC startup hiring" site:news.ycombinator.com

**Quality Gate:**
- Minimum 8 sources
- At least 3 founder perspectives (what gets their attention)
- Wearable AI / AI hardware startup-specific insights if available
- Application volume benchmarks

**Output:** `research/job_application/application_tactics/startup_strategy.md` + `sources.yaml`

---

## Agent 5: MNC Application Tactics

**Domain:** How to apply to large tech companies (Google, Microsoft, Amazon, Meta)

**Objective:** Optimize for ATS, recruiter pipelines, referral networks

**Key Questions:**
1. LinkedIn Easy Apply vs full application (success rate differences)
2. ATS optimization (resume parsing, keyword density)
3. Referral strategy (how to ask, who to ask, success rate boost)
4. Application volume per week (realistic targets)
5. Follow-up after application (when, how)
6. Recruiter InMail response rates
7. Internal job board vs external postings
8. New grad vs experienced hire pipelines

**Target Sources:**
- Gergely Orosz (The Pragmatic Engineer)
- Blind forum discussions (anonymous employee insights)
- Tech company career blogs (Google, Microsoft)
- Recruiter blogs (Lenny's Newsletter)
- "Cracking the Coding Interview" author blogs
- LinkedIn talent solutions posts

**Search Strategy:**
- "MNC application strategy" Gergely Orosz
- "ATS optimization for engineers" site:linkedin.com
- "tech company referral" site:teamblind.com
- "Google hiring process" site:reddit.com/r/cscareerquestions

**Quality Gate:**
- Minimum 8 sources
- At least 3 recruiter perspectives
- ATS keyword lists for AI/ML roles
- Referral vs non-referral success rate data

**Output:** `research/job_application/application_tactics/mnc_strategy.md` + `sources.yaml`

---

## Agent 6: Portfolio Building Research

**Domain:** Technical portfolio optimization for AI/ML roles

**Objective:** What to showcase, how to present projects for maximum impact

**Key Questions:**
1. GitHub pinned repos strategy (which 6 to pin)
2. Portfolio website: necessary or overkill for AI roles?
3. Project case studies: how much detail, what structure
4. Video demos vs README (what works better)
5. Open source contributions: how to showcase
6. Blog posts: technical depth vs accessibility
7. What hiring managers actually look at (GitHub vs portfolio site)
8. Red flags to avoid (unfinished projects, toy examples)

**Target Sources:**
- Hiring manager interviews (what they review)
- "How I got hired at X" blog posts
- GitHub best practices for job seekers
- Technical blog posts on portfolio reviews
- Y Combinator posts on engineer portfolios
- First Round Review hiring guides

**Search Strategy:**
- "GitHub portfolio for engineers" hiring manager
- "technical portfolio" site:ycombinator.com
- "engineer portfolio website" worth it
- "open source contributions" job search

**Quality Gate:**
- Minimum 8 sources
- At least 2 hiring manager perspectives
- Specific examples of strong portfolios
- AI/ML-specific guidance where available

**Output:** `research/job_application/portfolio_building/research.md` + `sources.yaml`

---

## Agent 7: Networking Research

**Domain:** Networking tactics for AI/ML job seekers

**Objective:** Online communities, conferences, warm introductions

**Key Questions:**
1. Best AI/ML communities for job seekers (Discord, Slack, forums)
2. How to ask for introductions (double opt-in, email templates)
3. Conference ROI for job searching (which conferences, how to network)
4. Twitter/X networking for AI roles (how to engage with founders)
5. Informational interviews: how to ask, what to ask
6. LinkedIn networking: connection requests, InMail
7. Meetups vs online communities (which is more effective)
8. How to follow up after networking events

**Target Sources:**
- Y Combinator networking advice
- First Round Review community building
- Tech community guides (Lenny's Newsletter)
- "How I got hired through networking" stories
- Conference speaker/organizer posts on effective networking
- Career coaches specializing in tech

**Search Strategy:**
- "networking for job search" site:ycombinator.com
- "warm introduction email" template
- "tech community for job seekers" AI ML
- "conference networking strategy"

**Quality Gate:**
- Minimum 6 sources (lower priority domain)
- At least 2 practitioner stories (hired through networking)
- Specific community recommendations for AI/ML

**Output:** `research/job_application/networking/research.md` + `sources.yaml`

---

## Agent 8: Meta-Synthesis Agent

**Domain:** Cross-cutting insights across all research domains

**Objective:** Synthesize themes, resolve conflicts, extract meta-patterns

**Dependencies:** Waits for agents 1-7 to complete

**Key Questions:**
1. What themes appear across multiple domains?
2. Where do sources conflict? How to resolve?
3. What's the overall application strategy (priority order)?
4. Startup vs MNC: what's fundamentally different?
5. What matters most for AI/ML roles specifically?
6. Time allocation: where to invest effort?
7. Common mistakes across all domains?
8. Quick wins vs long-term investments?

**Input:** All research.md files from agents 1-7

**Output:** `research/job_application/synthesis.md`

Structure:
```markdown
# Job Application Meta-Synthesis

## Overall Strategy
[Priority order, time allocation, quick wins]

## Startup vs MNC Differences
[Fundamental strategic divergence]

## AI/ML Role Specifics
[What's unique about AI/ML hiring]

## Common Themes
[Patterns across cold email, LinkedIn, portfolio, etc.]

## Conflict Resolution
[Where sources disagreed, how we resolved it]

## Time Allocation
[Where to invest effort: 70% X, 20% Y, 10% Z]

## Red Flags Across Domains
[Universal mistakes to avoid]

## Application to Soham's Situation
[Specific tactical roadmap]
```

---

## Workflow Orchestration

### Phase 1: Parallel Research (Agents 1-7)
Launch simultaneously, ~30 min runtime each:
- cold-email-agent
- cover-letter-agent
- linkedin-agent
- startup-tactics-agent
- mnc-tactics-agent
- portfolio-agent
- networking-agent

### Phase 2: Synthesis (Agent 8)
After Phase 1 completes, ~15 min runtime:
- meta-synthesis-agent

### Phase 3: Template Generation (Parallel)
After synthesis, launch 4 template agents:
1. **email-template-agent**: 5 cold email templates
2. **cover-letter-template-agent**: 3 cover letter templates
3. **linkedin-template-agent**: Profile section templates
4. **tracking-template-agent**: Application tracking spreadsheet

**Total estimated time:** ~50 minutes
**Total agents:** 11 (7 research + 1 synthesis + 3 template)

### Success Criteria
- All research.md files created with minimum source counts met
- No generic advice (anti-slop protocol enforced)
- Startup vs MNC differences explicit in every domain
- sources.yaml metadata complete for every source
- Synthesis resolves conflicts and extracts meta-patterns
- Templates ready to customize for Soham's applications
