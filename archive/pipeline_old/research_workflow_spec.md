# Job Application Research Workflow Spec

## Objective
Comprehensive research on job application best practices for AI/ML roles at startups and MNCs, covering cold emailing, cover letters, LinkedIn optimization, and application tactics.

## Output Structure
```
research/job_application/
├── cold_email/
│   ├── research.md          # Core research findings
│   ├── templates.md         # Email templates by scenario
│   └── sources.yaml         # Source metadata
├── cover_letter/
│   ├── research.md
│   ├── templates.md
│   └── sources.yaml
├── linkedin_profile/
│   ├── research.md
│   ├── optimization.md      # Profile optimization tactics
│   └── sources.yaml
├── application_tactics/
│   ├── startup_strategy.md
│   ├── mnc_strategy.md
│   └── sources.yaml
├── portfolio_building/
│   ├── research.md
│   └── sources.yaml
└── networking/
    ├── research.md
    └── sources.yaml
```

## Research Domains

### 1. Cold Email (Priority: High)
**Focus**: Founder outreach for startups, recruiter outreach for MNCs
**Key questions**:
- Subject line formulas that get opened
- Email structure (hook → proof → ask)
- Length constraints (word count)
- Follow-up cadence
- When to include resume vs portfolio link
- Personalization depth required

**Target sources**:
- Y Combinator essays on hiring
- First Round Review hiring guides
- Startup founder Twitter threads on cold emails
- Recruiter blogs (Lenny's Newsletter, Gergely Orosz)

### 2. Cover Letter (Priority: Medium)
**Focus**: When to write one, what to include, startup vs MNC differences
**Key questions**:
- Do startups read cover letters? (hypothesis: mostly no)
- MNC cover letter structure for ATS
- How to connect portfolio to job description
- Length: 1 paragraph vs full page?

**Target sources**:
- Harvard Career Services guides
- Stanford career center
- Tech recruiter LinkedIn posts

### 3. LinkedIn Profile (Priority: High)
**Focus**: ATS optimization, recruiter search visibility, network building
**Key questions**:
- Headline formula for AI/ML roles
- About section structure
- How to list projects vs experience
- Skills endorsement strategy
- Recommendations: who to ask, what to request

**Target sources**:
- LinkedIn's own optimization guides
- Tech recruiter best practices
- Austin Belcak (LinkedIn expert)

### 4. Application Tactics (Priority: High)
**Focus**: Where to apply, how to track, when to follow up
**Key questions**:
- Startup: direct founder email vs application portal?
- MNC: Easy Apply vs full application?
- Application volume (how many per week?)
- Tracking system (spreadsheet structure)
- Follow-up timing

**Target sources**:
- Hacker News "Who's Hiring" threads
- Y Combinator Work at a Startup
- Blind forum discussions

### 5. Portfolio Building (Priority: Medium)
**Focus**: What to showcase, how to present technical depth
**Key questions**:
- GitHub pinned repos strategy
- Portfolio website: necessary or overkill?
- Case studies: how much detail?
- Video demos vs README?

**Target sources**:
- Hiring manager interviews
- Technical blog posts on portfolio reviews

### 6. Networking (Priority: Low)
**Focus**: Conferences, online communities, warm introductions
**Key questions**:
- Best AI/ML communities for job seekers
- How to ask for intros
- Conference ROI for job searching

**Target sources**:
- Tech community guides
- Y Combinator founder advice

## Agent Orchestration Strategy

### Phase 1: Parallel Research (8 agents, ~30 min)
Each agent researches one domain independently:
1. **cold-email-agent**
2. **cover-letter-agent**
3. **linkedin-agent**
4. **startup-tactics-agent**
5. **mnc-tactics-agent**
6. **portfolio-agent**
7. **networking-agent**
8. **meta-synthesis-agent** (waits for all, synthesizes cross-cutting insights)

### Phase 2: Template Generation (4 agents, ~15 min)
After research completes:
1. **email-template-agent** (generates 5 cold email templates)
2. **cover-letter-template-agent** (generates 3 cover letter templates)
3. **linkedin-template-agent** (generates profile section templates)
4. **tracking-template-agent** (generates application tracking spreadsheet)

### Agent Context Template

Each research agent receives:
```yaml
domain: [domain name]
objective: [specific research objective]
key_questions: [list of questions to answer]
target_sources:
  - credible_institutions: [MIT, Stanford, Harvard, Y Combinator]
  - practitioner_sources: [recruiters, hiring managers, founders]
  - avoid: [generic career advice sites, AI-generated listicles]
output_format:
  - research.md: structured findings with citations
  - sources.yaml: metadata for every source used
constraints:
  - prioritize 2020+ sources (current practices)
  - cite every claim with source
  - extract direct quotes for key insights
  - flag conflicting advice across sources
  - no AI slop: avoid generic advice, prioritize specific tactics
quality_gate:
  - minimum 8 credible sources per domain
  - at least 3 practitioner sources (real hiring experience)
  - direct applicability to AI/ML roles at startups/MNCs
```

## Output Format Standards

### research.md structure
```markdown
# [Domain] Research

## Summary (3-5 key takeaways)

## Core Principles
[Fundamental truths backed by multiple sources]

## Tactical Guidance

### For Startups
[Specific tactics, templates, examples]

### For MNCs
[Specific tactics, templates, examples]

## Source Synthesis
[Where sources agree, where they conflict, what to trust]

## Direct Quotes
[Key insights verbatim with attribution]

## Red Flags to Avoid
[Common mistakes, what NOT to do]

## Application to Soham's Situation
[How this research applies specifically]
```

### sources.yaml structure
```yaml
sources:
  - id: yc_founder_hiring_2024
    type: article
    title: "How to Hire Your First Engineer"
    author: "Y Combinator"
    url: "https://..."
    date: "2024-03-15"
    credibility: high
    key_insight: "Founders read cold emails, prioritize GitHub proof over resume"
    
  - id: lenny_recruiter_2023
    type: newsletter
    title: "What Recruiters Actually Look For"
    author: "Lenny Rachitsky"
    url: "https://..."
    date: "2023-11-20"
    credibility: high
    key_insight: "LinkedIn headline is the #1 search filter"
```

## Quality Standards

### Anti-AI-Slop Checklist
- ❌ Generic advice ("be authentic", "show passion")
- ❌ Obvious statements ("proofread your email")
- ❌ Unsourced claims
- ❌ Conflicting advice without resolution
- ❌ Buzzword soup without concrete examples

### Quality Markers
- ✅ Specific tactics with examples
- ✅ Direct quotes from credible sources
- ✅ Conflicting advice analyzed and resolved
- ✅ Applicability to AI/ML roles stated explicitly
- ✅ Recent sources (2020+)
- ✅ Practitioner validation (not just theory)

## Success Criteria

### Completeness
- All 6 domains researched
- Minimum 8 sources per domain
- Templates generated for actionable domains

### Quality
- Every claim cited
- No generic advice
- Startup vs MNC differences clarified
- Applicability to Soham's situation explicit

### Usability
- Structured markdown (easy to navigate)
- YAML metadata (machine-parsable)
- Templates ready to customize
- Tracking systems ready to deploy

## Timeline
- Phase 1 (Research): ~30 minutes (parallel)
- Phase 2 (Templates): ~15 minutes (parallel)
- Total: ~45 minutes

## Agent Prompts (Next Step)
Write individual agent prompts with:
1. Domain-specific context
2. Source targeting strategy
3. Output structure
4. Quality gates
5. Anti-slop constraints
