---
name: po-second-brain
description: PO/PM second brain — interrogation-driven requirements capture, sprint planning, and stakeholder communication using systematic patterns
version: 1.0
---

# PO/PM Second Brain Skill

## Overview

The **PO/PM Second Brain** is an expert assistant that guides Product Owners and Project Managers through complex planning and communication challenges using three bootcamp intuitions:

1. **Context is everything** — Gathers rich context about stakeholders, constraints, and success criteria before generating requirements
2. **Structure gets rewarded** — Uses structured output (user stories, roadmaps, reports) instead of loose narrative
3. **You are the retrieval system** — Acts as an automated knowledge retrieval system for project context and team alignment

This skill enables POs/PMs to tackle:
- ✅ Requirements capture (turning conversations into structured stories)
- ✅ Sprint planning (breaking epics into stories with estimates)
- ✅ Stakeholder communication (status reports, steering decks, escalations)
- ✅ Roadmap planning (prioritization using value/effort/risk framework)

---

## Key Capabilities

### 1. Interrogation-Driven Workflow
Gathers structured context before generating requirements using a **25-question style interview** adapted for POs/PMs:

- **Stakeholder Context**: Business goals, success definition, key stakeholders
- **Project Scope**: Epics, features, must-haves vs. nice-to-haves
- **Constraints**: Timeline, budget, team capacity, dependencies
- **Team Composition**: Team size, experience level, existing patterns
- **Risk & Acceptance**: Known risks, acceptance criteria patterns, validation approach

### 2. Spec-Kit Methodology
Generates requirements and plans using **Knowledge → Specification → Plan → Execution**:

```
Knowledge: What do we know about the problem? (From interrogation)
Specification: What are we building? (User stories, acceptance criteria)
Plan: How will we build it? (Roadmap, sprint breakdown, timeline)
Execution: Who does what, when? (Task assignments, dependencies)
```

### 3. Structured Output Formats
- **User Stories**: Title, acceptance criteria (Given/When/Then), story points, dependencies
- **Sprint Backlog**: Stories with estimates, priorities, capacity planning
- **Stakeholder Report**: Executive summary, progress, risks, asks with clear ownership
- **Prioritized Roadmap**: Ranked features with rationale (value/effort/risk scores)

---

## Usage Scenarios

Choose the scenario matching your current task:

### **Scenario A: Requirements Capture**
*Turning stakeholder conversations into structured user stories with acceptance criteria*

**When to use**: "We need to document requirements for our new feature"
**What you'll get**: User stories with acceptance criteria, priority ranking, dependency mapping, edge cases identified

### **Scenario B: Sprint Planning**
*Breaking epics into stories, estimating, identifying dependencies*

**When to use**: "Help me plan the next 2-week sprint"
**What you'll get**: Sprint backlog with estimates, capacity check, dependency graph, burn-down projections

### **Scenario C: Stakeholder Communication**
*Status reports, steering committee decks, risk escalations*

**When to use**: "I need a status report for exec leadership"
**What you'll get**: Executive summary, progress metrics, risks with mitigation, asks with clear impact statements

### **Scenario D: Roadmap Planning**
*Feature prioritization using value/effort/risk framework*

**When to use**: "We have 15 features to prioritize for Q2-Q3"
**What you'll get**: Ranked roadmap with rationale, resource allocation, timeline projections, risk adjustments

---

## Structured Interrogation Framework

The skill will ask you these questions to build context:

<interrogation_questions>

### Phase 1: Business Context (6-8 questions)
1. **Company/Product**: What are we building? (SaaS, internal tool, mobile app, etc.)
2. **Business Goal**: What's the north star metric? (Revenue, retention, cost savings, efficiency?)
3. **Current State**: How is this done today? (Manual process, competitor, legacy system?)
4. **Success Definition**: How will we know this is successful? (Metrics, adoption, feedback?)
5. **Stakeholders**: Who are the key stakeholders? (Executive sponsor, users, customers, team leads?)
6. **Timeline**: When do we need this? (Hard deadline, flexible, market window?)

### Phase 2: Scope & Requirements (5-7 questions)
7. **Scope Statement**: What's in scope, what's out? (MVP vs. future features?)
8. **Primary Users**: Who are the primary users? (Customer, internal, both?)
9. **Key Workflows**: What are 3-4 critical user flows? (Signup, payment, reporting, etc.)
10. **Constraints**: What's non-negotiable? (Technology, budget, team size, compliance?)
11. **Dependencies**: What other projects/systems does this depend on?
12. **Known Unknowns**: What risks or uncertainties exist?

### Phase 3: Team & Capacity (3-4 questions)
13. **Team Size**: How many developers, designers, QA? What's the team composition?
14. **Team Experience**: What's your team's experience with this domain?
15. **Existing Patterns**: What design patterns, tech stack does the team use?
16. **Velocity**: What's your typical sprint velocity? (Story points, features per sprint?)

### Phase 4: Acceptance & Validation (3-4 questions)
17. **Acceptance Criteria Style**: Do you use Given/When/Then, checklist, or other format?
18. **Definition of Done**: What makes a story "done"? (Code review, tests, deployment, user validation?)
19. **Validation Approach**: How will stakeholders validate completion? (Demo, metrics, user testing?)
20. **Rollback Plan**: What's your safety net if something doesn't work?

### Phase 5: Knowledge & Decisions (2-3 questions)
21. **Decision Constraints**: Are there decisions that limit options? (Platform choices, compliance, etc.)
22. **Tribal Knowledge**: What does every PM wish they knew about this project?
23. **Competitive Intel**: How do competitors handle this? Any lessons learned?

</interrogation_questions>

---

## Output Format Specification

### 1. User Story with Acceptance Criteria

```markdown
## User Story: [Feature Title]

**Story ID**: PROJ-123
**Sprint**: Q2 Sprint 2
**Priority**: High
**Estimate**: 8 points
**Owner**: [Team member]

### Description
As a [user type], I want to [action], so that [benefit].

**Example**: As a **customer**, I want to **schedule a meeting with a sales rep**, so that **I can get personalized help without waiting**.

### Acceptance Criteria

Given the customer is on the Products page
When they click "Schedule Demo"
Then they see a calendar picker for available time slots

Given the customer selects a time slot
When they submit the form
Then an email confirmation is sent to them and their customer success rep

Given a customer tries to book outside business hours
When they submit
Then they see an error message and are offered the next available slot

### Edge Cases
- What if no time slots are available? (Show "Book a callback" form instead)
- What if customer's timezone is different? (Show times in their timezone)
- What if the sales rep's calendar is unavailable? (Auto-select next available rep)

### Dependencies
- Requires Calendar service integration (tracked in PROJ-456)
- Requires email notification system (existing)

### Success Criteria
- [ ] Calendar integration working end-to-end
- [ ] Email confirmations sent within 1 minute
- [ ] 80% of customers book within first 2 weeks
- [ ] No more than 5% booking errors
```

### 2. Sprint Backlog with Capacity Planning

```markdown
## Sprint 12 Backlog: Q2 Week 2-3

**Sprint Goal**: Launch customer meeting scheduling + payment integration
**Team Capacity**: 40 points (5 developers × 8 points/sprint)
**Forecast**: 38 points committed (95% utilization)

### High Priority Stories (15 points)
- [ ] PROJ-123: Schedule Demo Calendar Picker (8 pts) — Owner: Alice
- [ ] PROJ-124: Email Confirmation Emails (5 pts) — Owner: Bob
- [ ] PROJ-125: Calendar API Error Handling (2 pts) — Owner: Carol

**Dependencies**: None. Can start immediately.

### Medium Priority Stories (12 points)
- [ ] PROJ-126: Payment Gateway Integration (8 pts) — Owner: David
- [ ] PROJ-127: Invoice Generation (4 pts) — Owner: Eve

**Dependencies**: Blocked by PROJ-128 (3rd-party API credentials, expected EOD tomorrow)

### Nice-to-Have Stories (11 points)
- [ ] PROJ-128: Multi-timezone Support (5 pts) — Owner: Frank
- [ ] PROJ-129: Analytics Dashboard (6 pts) — Owner: Grace

**Dependencies**: None, can be deferred if other stories slip.

### Sprint Capacity Breakdown
| Developer | Committed | Max | Notes |
|-----------|-----------|-----|-------|
| Alice | 8 | 8 | Full capacity on calendar |
| Bob | 5 | 8 | Can take 3 more points |
| Carol | 2 | 8 | Light week, can help others |
| David | 8 | 8 | Full on payments |
| Eve | 4 | 8 | Can take 4 more points |
| **Total** | **38/40** | **40** | 2 point buffer |

### Risk Register
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|-----------|
| Calendar API rate limits | Medium | Medium | Add caching layer (Carol) |
| Payment vendor delays | High | Low | Have fallback processor (David) |
| Team unfamiliar with new auth system | Medium | Medium | Pair Frank with Alice |

### Burn-Down Projection
- **Day 1-3**: 35 points (steep initial progress)
- **Day 4-5**: 20 points (testing phase)
- **Day 6-7**: 2 points (buffer)
- **Expected completion**: Day 8 of 10 (healthy buffer)
```

### 3. Stakeholder Report (Executive Summary)

```markdown
## Q2 Progress Report & Steering Committee Update

**Period**: Week 1-2 of Q2 2026
**Report Date**: March 15, 2026
**Audience**: Executive Leadership, Steering Committee

---

## Executive Summary

**Status**: 🟢 On Track
**Overall Progress**: 52% of Q2 roadmap complete (target: 50%)
**Key Milestone**: Customer onboarding portal launches March 25 (on schedule)

### The Ask
We need approval to add **1 designer and 1 QA engineer** to the team for Q3 to maintain velocity given increased feature requests. **Impact**: Prevents 2-week roadmap slip. **Cost**: $65K for 3 months.

---

## Progress Snapshot

### Completed (This Period)
✅ **User Authentication System** (PROJ-100-110)
- All acceptance criteria met
- 94% test coverage
- Zero critical bugs in QA
- Customer acceptance testing passed

✅ **Payment Integration** (PROJ-120-125)
- Stripe and PayPal connected
- End-to-end testing complete
- Ready for March 25 launch

### In Progress (Next 2 Weeks)
🔵 **Customer Onboarding Portal** (PROJ-200-210)
- 60% complete, on track for March 25
- Demo scheduled March 20 for executive feedback
- No blockers identified

🔵 **Analytics Dashboard** (PROJ-300-310)
- 35% complete, slight lag on data pipeline work
- Reassigned best engineer (Carol) to help; expect to catch up by March 22

### At Risk / Upcoming
🟡 **Mobile App Redesign** (PROJ-400-410)
- Starts April 1, depends on new design resource
- Current designer (Frank) overallocated at 120% capacity
- **Mitigation**: Hire contractor designer by March 25

---

## Metrics That Matter

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Feature Delivery Rate | 12 features/quarter | 11 features (on pace) | 🟢 On track |
| Customer Adoption | 500 signups/month | 480 (March) | 🟡 Slightly below |
| Quality (P1 bugs) | <2 per sprint | 1 avg | 🟢 Healthy |
| Team Satisfaction | >8/10 | 7.8/10 | 🟡 Slight burnout signals |
| Time to Market | 2-week sprints | 2 weeks avg | 🟢 Consistent |

---

## Risk Register

| Risk | Impact | Status | Owner | Mitigation |
|------|--------|--------|-------|-----------|
| **Designer capacity (Frank at 120%)** | High | 🔴 Active | Sarah | Hire contractor, redistribute work |
| **Analytics data pipeline delay** | Medium | 🟡 Watching | Carol | Assigned best engineer, on track |
| **Customer adoption below forecast** | High | 🟡 Watching | Marketing | A/B test onboarding UX, gather feedback |
| **Mobile app timeline compression** | Medium | 🟢 Mitigated | Product | Hired contractor designer |

---

## What We Need From You

| Ask | Impact | Timeline |
|-----|--------|----------|
| **Approve 2 hires for Q3** | Prevents 2-week roadmap slip | Decision needed by March 31 |
| **Review design contractor proposal** | Keeps mobile app on schedule | Decision needed by March 25 |
| **Feedback on onboarding portal demo** | Ensures customer alignment | March 20 demo |

---

## Next Steps
1. **March 20**: Executive demo of customer onboarding portal
2. **March 25**: Launch customer onboarding portal to production
3. **March 31**: Staffing decision on Q3 hires (impacts roadmap)
4. **April 1**: Mobile app redesign begins with contractor designer

---

**Report prepared by**: [Your name]
**Questions?**: [Contact info]
```

### 4. Prioritized Roadmap with Rationale

```markdown
## Q2-Q3 Product Roadmap

**Planning Horizon**: 24 weeks
**Total Features Under Consideration**: 18
**Committed (Q2)**: 12 features | 40 points
**Planning (Q3)**: 6 features | TBD

---

## Prioritization Framework

Each feature is scored on **Value (1-5)**, **Effort (1-5)**, **Risk (1-5)**, producing priority rank:

```
Priority Score = (Value × 3 + Revenue Impact) - (Effort × 2 + Risk × 1.5)
Rank 1-5 = Highest priority (launch first)
Rank 6-10 = Medium priority (launch if capacity)
Rank 11+ = Future or defer
```

---

## Ranked Roadmap: Q2-Q3

### Tier 1: Launch Now (Q2, Weeks 1-6)

| Rank | Feature | Value | Effort | Risk | Impact | Owner | Status |
|------|---------|-------|--------|------|--------|-------|--------|
| 1 | **Payment Integration** | 5 | 4 | 2 | Revenue generation | David | 90% done |
| 2 | **Customer Onboarding Portal** | 5 | 3 | 1 | Reduces support burden 40% | Alice | 60% done |
| 3 | **Email Notifications** | 4 | 2 | 1 | Critical for adoption | Bob | Backlog |
| 4 | **User Authentication Upgrade** | 4 | 3 | 3 | Security compliance | Carol | 80% done |

**Rationale**: All four features unlock revenue, reduce support load, and have clear success metrics. Payment and onboarding are customer-facing and high-impact. Should complete by March 31.

**Resource Allocation**: Alice (onboarding), David (payments), Carol (auth), Bob (notifications) — total 15 points.

---

### Tier 2: Plan for Q3 (Weeks 7-12)

| Rank | Feature | Value | Effort | Risk | Impact | Owner | Status |
|------|---------|-------|--------|------|--------|-------|--------|
| 5 | **Analytics Dashboard** | 5 | 4 | 2 | Reveals user patterns | Frank | Backlog |
| 6 | **Mobile App Redesign** | 4 | 5 | 3 | Improves engagement | Grace | Blocked: contractor |
| 7 | **API Rate Limiting** | 3 | 2 | 1 | Prevents abuse | Carol | Backlog |
| 8 | **Advanced Search** | 3 | 3 | 2 | Nice-to-have UX | Henry | Backlog |

**Rationale**: Analytics reveals what users care about (informs future prioritization). Mobile redesign is high-effort but high-value. API work is technical debt but necessary for scale.

**Dependencies**: Mobile redesign blocked by contractor hiring (expected March 31). Analytics depends on payment data (will be available from Q2 launch).

---

### Tier 3: Defer to Q4+ (If Capacity)

| Rank | Feature | Value | Effort | Risk | Reason for Defer |
|------|---------|-------|--------|------|-----------------|
| 9 | **Bulk CSV Import** | 2 | 4 | 2 | Low customer demand |
| 10 | **Custom Workflows** | 2 | 5 | 3 | Complex, low ROI |
| 11 | **Advanced Permissions** | 3 | 3 | 1 | Can be addressed in Q4 |
| 12+ | **Mobile Offline Mode** | 1 | 4 | 4 | Rare use case, high risk |

**Rationale**: These features are either low-impact (bulk import), high-complexity with low ROI (custom workflows), or not yet critical (offline). Revisit in Q4.

---

## Timeline & Capacity Projection

```
Q2 (Weeks 1-6): Tier 1 Features
├─ Week 1-3: Finish Payment + Onboarding (15 points)
├─ Week 3-5: Email notifications (8 points)
├─ Week 5-6: Auth upgrade buffer (7 points)
└─ Week 6: Customer demo + launch to production

Q3 (Weeks 7-12): Tier 2 Features
├─ Week 7-9: Analytics dashboard (12 points, requires new designer + mobile contractor)
├─ Week 9-11: Mobile redesign (15 points, with contractor)
├─ Week 11-12: API work + polish (5 points)
└─ Week 12: Stability & buffer

Q4+: Tier 3 + Customer-Driven Features
```

---

## Risk Adjustments

**Team capacity**: Current team at 90% capacity. Tier 2 assumes **1 designer + 1 contractor** hired by March 31.
**Timeline risk**: If contractor hire slips, Mobile redesign (Rank 6) moves to Q4.
**Market risk**: Mobile app redesign could be reprioritized if competitor launches; have contingency.

---

## Success Metrics (How We'll Know This Worked)

By end of Q3:
- ✅ Payment integration processing >$100K/month
- ✅ Onboarding portal adopted by >70% of new customers
- ✅ Analytics dashboard reveals >3 actionable customer insights
- ✅ Mobile app engagement increases 25% post-redesign
- ✅ Team satisfaction improves to >8.5/10

---

**Roadmap Last Updated**: March 15, 2026
**Next Review**: April 1, 2026
**Stakeholders**: Product, Engineering, Design, Executive
```

---

## Using the Skill: Step-by-Step Workflow

### Step 1: Choose Your Scenario
```
"I need to capture requirements from our stakeholder interviews"
→ Scenario A (Requirements Capture)

"Help me plan the next 2-week sprint from our backlog"
→ Scenario B (Sprint Planning)

"I need to brief executives on Q2 progress and risks"
→ Scenario C (Stakeholder Communication)

"I have 20 features to prioritize for the next 2 quarters"
→ Scenario D (Roadmap Planning)
```

### Step 2: Let the Skill Interrogate
The skill will ask 20-25 questions. **Answer fully and honestly** — this is where context richness happens.

Example interrogation flow:
```
Q1: What are we building?
A: A customer onboarding portal for our SaaS product

Q2: What's the business goal?
A: Reduce customer implementation time from 4 weeks to 2 weeks, improve retention

Q3: Who are the key stakeholders?
A: CEO, VP of Customer Success, sales team, 3-4 pilot customers

Q4: What's your timeline?
A: Must launch March 25 for Q2 goals, before sales kickoff

Q5: How many developers?
A: Team of 5, mixed seniority. This is new domain for most of them.

[... continues through all 25 questions ...]
```

### Step 3: Review Generated Artifacts
The skill will output:
- ✅ User stories with acceptance criteria (Given/When/Then format)
- ✅ Sprint backlog with capacity planning and burn-down projections
- ✅ Stakeholder report with executive summary and asks
- ✅ Prioritized roadmap with value/effort/risk scoring

### Step 4: Align & Execute
Take generated artifacts to team:
- Share user stories in backlog tool (Jira, Linear, Asana)
- Review sprint backlog with team in planning meeting
- Present stakeholder report to exec sponsors
- Walk through roadmap with engineering leads to refine estimates

---

## Design Principles

### Principle 1: Context Over Guessing
**Never generate requirements without understanding:**
- What problem does this solve for customers?
- What constraints exist (timeline, budget, team)?
- What does success look like (metrics, not just features)?
- What could go wrong (risks, dependencies)?

The interrogation phase ensures rich context before any artifacts.

### Principle 2: Structure Over Narrative
**Always output:**
- Structured user stories (not rambling requirements docs)
- Ranked backlogs (not brain dumps)
- Executive summaries (not long narratives)
- Prioritized roadmaps (not wishlists)

Bootcamp intuition: Structure gets rewarded.

### Principle 3: Spec-Kit Methodology
**Always follow knowledge → specification → plan → execution:**
- **Knowledge**: What did we learn in interrogation?
- **Specification**: What are we building? (User stories)
- **Plan**: How will we build it? (Sprint backlog, timeline)
- **Execution**: Who does what? (Task ownership, dependencies)

This ensures nothing is missed.

### Principle 4: Acceptance Criteria Over Vagueness
**Every story includes:**
- Given/When/Then format (testable conditions)
- Edge cases identified
- Definition of Done criteria
- Explicit success metrics

This prevents the "I thought it meant..." conversations.

---

## Example: Complete Workflow

### Scenario: Requirements Capture for Customer Onboarding Portal

**You say:**
```
We need to build a customer onboarding portal.
It should help new customers get set up quickly without talking to our support team.
We have 5 developers, need to launch in 6 weeks, and we have 3 pilot customers willing to test.
```

**Skill interrogates (Phase 1: Business Context):**
```
Q1: What's the north star metric?
→ "Reduce implementation time from 4 weeks to 2 weeks"

Q2: Current state?
→ "Support team manually walks each customer through setup via Zoom calls"

Q3: Success definition?
→ "70% of new customers complete onboarding without support intervention"

Q4: Key stakeholders?
→ "VP of Customer Success (sponsor), 3 pilot customers, support team, sales"

Q5: Timeline?
→ "Hard deadline March 25 for Q2 goals"
```

**Skill interrogates (Phase 2: Scope & Requirements):**
```
Q6: Primary user?
→ "New customers (SMB to mid-market companies)"

Q7: Key workflows?
→ "1) Create account & login, 2) Configure settings, 3) Upload data, 4) Run first report, 5) Invite team members"

Q8: Constraints?
→ "Must work with existing auth system, no new infrastructure, budget $50K for contractor design help"

Q9: Known risks?
→ "Customers may have complex legacy data formats; support team will need training"
```

**Skill interrogates (Phase 3: Team & Capacity):**
```
Q10: Team composition?
→ "3 backend engineers, 1 frontend engineer, 1 QA, design contractor (4 weeks), I'm the PM"

Q11: Team experience?
→ "Backend experienced with Python/FastAPI; frontend new to React; no one knows our data formats"

Q12: Velocity?
→ "Typically 20 points per 2-week sprint"
```

**Skill interrogates (Phase 4: Acceptance & Validation):**
```
Q13: Acceptance criteria style?
→ "Given/When/Then format, we track with Jira"

Q14: Definition of Done?
→ "Code review approved, >80% test coverage, deployed to staging, pilot customer tested"

Q15: Validation?
→ "Pilot customers demo with VP of Customer Success; if 2/3 say 'ready', we ship"
```

---

### Skill Generates: User Stories

```markdown
## User Story: Create Account & Login

**Story ID**: ONBOARD-101
**Sprint**: Q2 Sprint 2-3
**Priority**: Critical (blocks all other workflows)
**Estimate**: 5 points
**Owner**: Frontend engineer

### Description
As a **new customer**, I want to **create an account and log in**, so that **I can start configuring my settings**.

### Acceptance Criteria

Given I'm on the landing page
When I click "Get Started"
Then I see a sign-up form asking for company name, email, and password

Given I fill in valid information
When I click "Create Account"
Then my account is created and I'm logged in
And I see the onboarding dashboard (next workflow)

Given I already have an account
When I click "Log In"
Then I see a login form
And after entering credentials, I'm logged in to the dashboard

Given I try to log in with invalid credentials
When I click "Log In"
Then I see an error message "Invalid email or password"
And my account is NOT locked (retry allowed)

Given I forget my password
When I click "Forgot Password"
Then I receive a password reset email within 1 minute
And I can set a new password via the email link

### Edge Cases
- What if customer enters email already used? (Show error, suggest login)
- What if password is too weak? (Show strength meter, enforce minimum complexity)
- What if customer closes browser before email confirmation? (Session expires after 24 hours, can resend)

### Dependencies
- ONBOARD-100: Design the login/signup UI (frontend)
- Uses existing OAuth provider (auth system)
- No new backend work needed

### Acceptance Checklist
- [ ] Frontend: Sign-up form renders correctly
- [ ] Backend: Account created in database with hashed password
- [ ] Email: Welcome email sent within 1 minute
- [ ] Security: No SQL injection, password validation works
- [ ] Test coverage: >80% of login paths tested
- [ ] Pilot test: 2/3 pilot customers successfully sign up
```

```markdown
## User Story: Configure Settings

**Story ID**: ONBOARD-102
**Sprint**: Q2 Sprint 3
**Priority**: High
**Estimate**: 8 points
**Owner**: Backend engineer

### Description
As a **new customer**, I want to **configure my basic settings** (company name, timezone, data retention policy), so that **the system knows how to handle my data**.

### Acceptance Criteria

Given I just logged in
When I navigate to Settings
Then I see a form with fields: Company Name, Timezone, Data Retention (30/90/365 days), Industry

Given I fill in settings and click "Save"
Then my settings are saved to the database
And I see a confirmation message "Settings saved successfully"
And the settings are immediately applied to my dashboard

Given I change my timezone from UTC to EST
When I save
Then all timestamps displayed on my dashboard now show EST
And the change takes effect immediately

Given a field is required (e.g., Company Name)
When I try to save without filling it
Then I see an inline error message "Company name is required"
And the form is not submitted

Given I accidentally navigate away
When I come back
Then my unsaved changes are NOT lost (browser stores locally)
And I can either save or discard

### Edge Cases
- What if customer selects a timezone not in our supported list? (Use closest match, show note)
- What if customer changes retention policy? (Data older than new policy is NOT deleted retroactively, only new data follows new policy)
- What if customer's industry isn't in our list? (Allow free-text entry)

### Dependencies
- ONBOARD-101: Customer must be logged in first
- Uses existing database table (no migration needed)

### Acceptance Checklist
- [ ] Frontend: Settings form renders and saves
- [ ] Backend: Settings persisted to database
- [ ] Timezone: All timestamps converted correctly
- [ ] Data retention: Policy logic documented for future data handling
- [ ] Test coverage: >80% of settings paths tested
- [ ] Pilot test: 2/3 customers confirm settings work as expected
```

---

### Skill Generates: Sprint Backlog

```markdown
## Sprint 2-3 Backlog: Onboarding Portal MVP

**Sprint Goal**: Launch customer onboarding portal MVP with account creation, settings, and data upload.
**Team Capacity**: 40 points (5 developers × 8 points/sprint)
**Forecast**: 38 points committed

### Stories (In Priority Order)

#### Critical Path (Must Have)
- [x] ONBOARD-101: Create Account & Login (5 pts) — Frontend engineer — **DONE**
- [x] ONBOARD-102: Configure Settings (8 pts) — Backend engineer — **IN PROGRESS**
- [ ] ONBOARD-103: Upload Data (13 pts) — Backend + Frontend — **BACKLOG**
- [ ] ONBOARD-104: Run First Report (8 pts) — Backend + Frontend — **BACKLOG**
- [ ] ONBOARD-105: Invite Team Members (4 pts) — Backend — **BACKLOG**

**Subtotal**: 38 points

#### Nice-to-Have (If Time)
- [ ] ONBOARD-106: Dark Mode (3 pts) — DEFER
- [ ] ONBOARD-107: Mobile-Responsive Design (5 pts) — DEFER

---

### Capacity Breakdown

| Person | Role | Committed (pts) | Capacity (pts) | Buffer |
|--------|------|-----------------|-----------------|--------|
| Alice | Frontend | 13 (login + upload UI) | 8 | -5 ⚠️ |
| Bob | Backend | 13 (settings + upload) | 8 | -5 ⚠️ |
| Carol | Backend | 12 (reports + integration) | 8 | -4 ⚠️ |
| David | Backend | 8 (invite team) | 8 | 0 |
| Eve | QA | 4 (test planning, edge cases) | 8 | +4 |
| **Total** | | **50 points** | **40** | **-10 ⚠️** |

**⚠️ PROBLEM**: We're overcommitted by 10 points. Either reduce scope or extend timeline.

**RECOMMENDATION**:
- Defer ONBOARD-105 (Invite Team Members) to Sprint 4 (4 pts)
- This brings us to 34 committed points, 6 point buffer
- Adjusts Alice and Bob to 8 and 9 points respectively (achievable)

---

### Dependency Graph

```
ONBOARD-101 (Login)
    ↓ (required by)
ONBOARD-102 (Settings)
    ↓ (required by)
ONBOARD-103 (Upload Data)
    ↓ (required by)
ONBOARD-104 (First Report)

Parallel: ONBOARD-105 (Invite Team) can start once ONBOARD-101 done

Blockers:
- ONBOARD-103 blocked by: Contract with data provider (expected March 18)
- ONBOARD-104 blocked by: Report templates from Product (expected March 15)
```

---

### Risk & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|-----------|
| Data upload parsing fails | High | Medium | Carol pair-programs with David, use CSV validation library |
| Over-committed team | High | High | **ACTION**: Defer ONBOARD-105 to next sprint |
| Report templates delayed | Medium | Medium | Have placeholder reports ready; update design once templates arrive |
| Pilot customer unavailable | Medium | Low | We have 3 pilots; need 2/3 for sign-off |

---

### Burn-Down Projection

```
Sprint Day 1-3: 38 → 20 points (steep initial progress)
Sprint Day 4-5: 20 → 8 points (testing phase)
Sprint Day 6-7: 8 → 2 points (final polish)
Sprint Day 8-10: 2 → 0 points (buffer)

Expected: Complete 34 committed points by Day 7, 6 point buffer for overflow
```

---

### Pre-Sprint Review Checklist
- [ ] All stories estimated by full team
- [ ] Dependencies identified and documented
- [ ] Risk register reviewed
- [ ] Pilot customer availability confirmed (schedule demo for Day 8)
- [ ] Contract with data provider expected (March 18)
- [ ] Report templates ready from Product (March 15)
```

---

### Skill Generates: Stakeholder Report

```markdown
## Onboarding Portal Status: Steering Committee Update

**Date**: March 15, 2026
**Project**: Customer Onboarding Portal MVP
**Sponsor**: VP of Customer Success
**Status**: 🟢 On Track

---

## Executive Summary

**What We're Doing**: Building a portal to let customers self-onboard (reduce support workload by 60%).

**Status**: Account creation ✅ done, settings in progress, data upload next week.

**Timeline**: Launching March 25 (on schedule) with 3 pilot customers.

**The Ask**: Keep current team allocation through Q2. No budget or headcount changes needed.

---

## Progress This Week

### Completed
✅ **Account Creation & Login** (ONBOARD-101)
- All acceptance criteria met
- Pilot customer tested, zero issues
- Ready to move to production

### In Progress
🔵 **Settings Configuration** (ONBOARD-102)
- 80% complete
- On track to complete March 18
- No blockers

### Upcoming
⏳ **Data Upload** (ONBOARD-103)
- Starts March 19
- Depends on data provider contract (expected March 18)
- Contingency: If contract delayed, we have placeholder workflow ready

---

## Key Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Features complete | 80% by March 20 | 50% (2/4 features) | 🟡 Slightly behind |
| Pilot test sign-off | 2/3 customers | 2/3 piloting | 🟢 On track |
| Test coverage | >80% | 82% | 🟢 Healthy |
| Production readiness | Day 25 | On pace for Day 25 | 🟢 On track |

---

## Risks & Mitigations

| Risk | Status | Mitigation |
|------|--------|-----------|
| Data provider contract signed | 🟡 Watching | Contract lawyer expediting; fallback: placeholder API |
| Report templates delayed | 🟡 Watching | Have basic template ready; fine-tune after launch |
| Pilot customer feedback slow | 🟢 Mitigated | Scheduled weekly syncs; have 3 pilots so feedback redundancy |

---

## What We Need

**No asks at this time.** All required resources allocated. Keep current team through March 25 launch.

---

**Next Steering Update**: March 22
**Launch Date**: March 25
**Owner**: [PM name]
```

---

## Advanced Usage: Combining with Bootcamp Patterns

### Using with Priority Builder Pattern
Map your product work to ABCD:
```
Action: Build customer onboarding portal
Behavior: Reduce implementation time 50%, ship with 70% adoption
Context: Self-serve lowers support burden, improves NPS
Delivered: Launch-ready, 3 pilot customers validated
```

### Using with ReAct Pattern
Systematically prioritize features:
```
THINK: What delivers value soonest? What's blocked?
ACT: Score features on value/effort/risk matrix
OBSERVE: Does ranked backlog align with business goals?
```

### Using with Tree of Thoughts
Complex roadmap decisions:
```
Generate: 3 prioritization approaches (customer-driven, revenue-driven, risk-driven)
Evaluate: Which aligns with company strategy?
Choose: Revenue-driven approach because it funds next headcount
```

---

## When to Use This Skill vs. Spreadsheet

| Task | Use Spreadsheet | Use Skill |
|------|-----------------|-----------|
| Quick vote on feature priority | ✅ Fast | ❌ Overkill |
| One-off status update | ✅ Simple | ❌ Overhead |
| Structured sprint planning | ❌ Too chaotic | ✅ **This skill** |
| **Requirements for complex feature** | ❌ Gets messy | ✅ **This skill** |
| **Roadmap for uncertain futures** | ❌ Too many assumptions | ✅ **This skill** |
| **Stakeholder alignment meeting** | ❌ Scattered | ✅ **This skill** |
| **Risk register with mitigations** | ❌ Spreadsheets don't capture logic | ✅ **This skill** |

---

## Bootcamp Integration

### For Facilitators
Use this skill in **Session 3: Applied Patterns** when discussing:
- Spec-kit methodology (knowledge → spec → plan → execution)
- Structured interrogation for context-gathering
- Alignment through structured artifacts
- Stakeholder communication patterns

### For Participants (Role-Fork Exercise)
**Use this skill when:**
- You're the "PO" or "PM" in a role-fork scenario
- You need to capture requirements from stakeholders
- You're planning a sprint or roadmap
- You need to communicate status to executives
- You're new to product management and need guidance

**Expected outcome:**
- Understand how interrogation surfaces hidden constraints
- See spec-kit methodology in action
- Generate executive-ready artifacts in minutes
- Build alignment through structured, repeatable formats

---

## FAQ

**Q: Will this skill tell me what features to build?**
A: No. It surfaces the context and structure to *help you decide*. You have the domain expertise and business intuition; this skill structures that thinking.

**Q: What if I don't know the answers to all 25 interrogation questions?**
A: That's expected! The skill will ask follow-ups to clarify. Unknown answers are insights — they reveal what you need to discover.

**Q: How is this different from just asking an LLM for a roadmap?**
A: The interrogation phase forces you to think through business context, team capacity, and risks *before* generating artifacts. Bad interrogation = bad roadmap. Rich interrogation = trusted roadmap.

**Q: Can I use this for agile projects with ongoing backlog refinement?**
A: Yes. Use it for sprint planning (refresh every 2 weeks) and quarterly roadmap reviews. The skill works iteratively.

**Q: What if my team has a different estimation system (T-shirt sizes, fibonacci)?**
A: Tell the skill during interrogation: "We estimate with T-shirt sizes (S/M/L/XL)." It will adjust the output format.

**Q: Can I use this for non-tech products?**
A: Absolutely. The framework works for any product/project with stakeholders, scope, and timeline. Interrogation questions adapt to your domain.

---

## References

- **Spec-Kit Methodology**: Joey's Prompt Engineering Bootcamp v2, Session 1
- **Given/When/Then Format**: Cucumber/BDD specification patterns (Wynne & Hellesøy, 2012)
- **Roadmap Prioritization**: RICE framework (Rice, Eisenhower, Cost, Effort)
- **Stakeholder Communication**: HBR "The Art of the Executive Summary" (2023)

---

**Version**: 1.0
**Last Updated**: 2026-03-18
**For**: Joey's Prompt Engineering Bootcamp v2
