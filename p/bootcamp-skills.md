---
title: "Bootcamp Skills"
description: "5 role-specific skills — Swagger-style with copy buttons."
author: "Joey Lopez"
date: "2026-02-15"
tags: ["skills", "workshop", "teaching", "template"]
atom_id: 7
source_html: "bootcamp-skills.html"
url: "https://jrlopez.dev/p/bootcamp-skills.html"
generated: true
---

[← home ]()[bootcamp ]()[developer ]()[PO/PM ]()[delivery ]()[tech lead ]()[make skills ]()
# Bootcamp Skills Reference Five role-specific AI workflow guides. Pick your track, run the interrogation, get structured output. Joey Lopez · Sr. Data Engineer [developer ]()[PO/PM ]()[delivery lead ]()[tech lead ]()[make skills ]()Developer PO / PM Delivery Lead Tech Lead Make Skills skill spec ---
name : dev-second-brain
version : 1.0
description : Interrogation-driven code assistance — migrations, refactoring, features, debugging
patterns : [ReAct, spec-kit, structured-output]
---
## Developer Second Brain Gathers rich context about your codebase before suggesting changes. Uses ReAct (THINK→ACT→OBSERVE) to produce plans, diffs, and tests — not loose prose. Context is everything Structure gets rewarded You are the retrieval system ⇩ Download SKILL.md When to use each scenario
#### A — Code Migration "I need to migrate from Framework A to B" Migration plan, code diffs, test strategy, rollback plan.
#### B — Refactoring "I need to refactor this component" Refactoring goals, dependency map, extraction plan, test approach.
#### C — Feature Implementation "Build a new feature following our patterns" Feature spec, code stubs with TODOs, test outline, integration points.
#### D — Systematic Debugging "Track down root cause of production issue" Hypothesis, investigation steps, diagnostic queries, solution options. Interrogation Framework 15 questions · 4 phases ▶
#### Phase 1 — Current State (Q1–5)
 - **Language & Framework **What language/framework + version? (e.g., Python 3.11 + Django 4.2)
 - **Architecture Pattern **Monolith, microservices, event-driven, layered?
 - **Current Problem **What specifically needs to change? (one sentence)
 - **Scope **One file, one module, or multiple services?
 - **Team Size **How many developers? What is your role?
#### Phase 2 — Target State (Q6–8)
 - **Success Criteria **How will you know it is working? Metrics, tests, deployment success?
 - **Constraints **No downtime, budget limits, timeline?
 - **Dependencies **What other systems does this touch?
#### Phase 3 — Implementation Context (Q9–12)
 - **Test Coverage **Existing tests? Unit, integration, e2e?
 - **Team Conventions **Naming convention, error handling pattern, logging standard?
 - **Review Process **Automated checks, approval gates?
 - **Rollback Plan **Safety net if something goes wrong?
#### Phase 4 — Knowledge (Q13–15)
 - **Similar Changes **Have you done something like this before?
 - **Tribal Knowledge **What does every developer wish they knew about this codebase?
 - **Decision Log **Are there decisions that limit how you can change this? Starter Prompt Templates copy and paste ▶ Prompt Template — Scenario A (Migration) Copy
```
You are a Developer Second Brain using the ReAct pattern (THINK→ACT→OBSERVE).
I need to migrate [OLD FRAMEWORK/VERSION] to [NEW FRAMEWORK/VERSION].

Before generating any plan, ask me the following questions one phase at a time:
Phase 1: Language/framework, architecture, scope, team size, current pain point
Phase 2: Success criteria, constraints, dependencies
Phase 3: Test coverage, team conventions, rollback plan
Phase 4: Prior similar changes, tribal knowledge, decision constraints

After I answer all phases, produce:
1. Implementation plan with THINK/ACT/OBSERVE annotations
2. Code diffs (before/after) for the critical path
3. Test strategy matrix (component | test type | approach | coverage)
4. Pre-deployment checklist
```
Prompt Template — Scenario C (Feature Implementation) Copy
```
You are a Developer Second Brain.
I need to implement [FEATURE NAME] following our existing team conventions.

Interrogate me through 4 phases before generating anything:
Phase 1: Language/framework, architecture pattern, current module structure, scope
Phase 2: Success criteria, constraints, dependencies
Phase 3: Test pattern, naming conventions, error handling style, code review process
Phase 4: Tribal knowledge, any architectural constraints

Then produce:
- Code stubs with clear TODO annotations (following our exact conventions)
- Test file skeleton (matching our test pattern)
- Integration checklist
- Pre-merge checklist
```
Prompt Template — Scenario D (Debugging) Copy
```
You are a Developer Second Brain using systematic debugging (ReAct).
I have a production issue: [DESCRIBE SYMPTOM]

Before generating hypotheses, ask me:
1. What is the exact error or unexpected behavior?
2. When did it start? After what change?
3. What have you already tried?
4. What do the logs show?
5. Which components or services are involved?

Then generate:
THINK: Top 3 hypotheses ranked by probability
ACT: Investigation steps for each hypothesis (specific commands/queries)
OBSERVE: What to look for — how to confirm or rule out each hypothesis
```
Output Templates ReAct plan · test matrix · checklist ▶ Implementation Plan (ReAct Format) Copy
```
## Migration Plan: [Component] from [Old] to [New]

### Phase 1: Preparation
**THINK**: What needs to be true before we start?
- [ ] Dependencies installed
- [ ] Tests passing
- [ ] Backup created

**ACT**: Run these commands:
```bash
# setup steps
```

**OBSERVE**: Verify with:
```bash
# verification commands
```

### Phase 2: Core Change
**THINK**: What is changing and why?
- Breaking change X affects Y consumers
- New API requires Z configuration

**ACT**: Apply these changes:
```diff
- old_code()
+ new_code()
```

**OBSERVE**: Test coverage:
- [ ] Unit test for new_code()
- [ ] Integration test for X→Y flow
- [ ] No regression in unchanged code

### Phase 3: Verification
**THINK**: How do we know this is safe?
**ACT**: Run full test suite
**OBSERVE**: Success criteria met
```
Test Strategy Matrix Copy
```
| Component    | Test Type   | Approach                        | Coverage                  |
|--------------|-------------|---------------------------------|---------------------------|
| [Component]  | Unit        | Mock async response             | Function returns correctly |
| [Service]    | Integration | Real async client               | Full workflow with I/O     |
| [API Handler]| E2E         | Load test                       | 100 concurrent requests   |
| [Rollback]   | Regression  | Before/after comparison         | No breaking changes       |
```
Pre-Deployment Checklist Copy
```
## Pre-Deployment Checklist

### Code Quality
- [ ] Tests pass (unit + integration + e2e)
- [ ] Code review approved
- [ ] No new warnings in linter/type checker
- [ ] No security issues in dependency scan
- [ ] Documentation updated

### Performance & Stability
- [ ] Load test shows no degradation
- [ ] Error handling covers edge cases
- [ ] Logging added for debugging
- [ ] Monitoring/alerting updated

### Rollback Safety
- [ ] Rollback plan documented
- [ ] Migration is reversible (if database changes)
- [ ] Feature flag allows instant disable
- [ ] Previous version can run in parallel if needed
```

ReAct Pattern Reference THINK What is the constraint here? Analyze the problem space, map dependencies, identify what could break. ACT Apply the code change. Show the concrete diff or implementation stub. OBSERVE How do we verify? List the test commands, metrics, and success criteria. When to use this skill vs. your IDE ▶

| Task  || Use IDE  || Use This Skill  |

| Syntax autocomplete  || IDE  ||  |

| Quick bug fix  || IDE  ||  |

| Migrate framework  ||  || This skill  |

| Refactor large component  ||  || This skill  |

| New feature matching patterns  ||  || This skill  |

| Root cause debugging  ||  || This skill  |

| Architecture code review  ||  || This skill  |

skill spec ---
name : po-second-brain
version : 1.0
description : Requirements capture, sprint planning, stakeholder communication, roadmap prioritization
patterns : [spec-kit, Given/When/Then, value-effort-risk scoring]
---
## PO / PM Second Brain Gathers context about stakeholders, constraints, and success criteria before generating requirements, sprint backlogs, or roadmaps — never guesses. Context is everything Structure gets rewarded You are the retrieval system ⇩ Download SKILL.md When to use each scenario
#### A — Requirements Capture "We need to document requirements for our new feature" User stories with Given/When/Then, priority ranking, dependency mapping, edge cases.
#### B — Sprint Planning "Help me plan the next 2-week sprint" Sprint backlog with estimates, capacity check, dependency graph, burn-down projections.
#### C — Stakeholder Communication "I need a status report for exec leadership" Executive summary, progress metrics, risks with mitigation, asks with clear impact statements.
#### D — Roadmap Planning "We have 15 features to prioritize for Q2–Q3" Ranked roadmap with rationale, resource allocation, timeline projections, risk adjustments. Interrogation Framework 23 questions · 5 phases ▶
#### Phase 1 — Business Context (Q1–6)
 - **Company / Product **What are we building? SaaS, internal tool, mobile app?
 - **Business Goal **North star metric — revenue, retention, cost savings, efficiency?
 - **Current State **How is this done today? Manual, competitor, legacy?
 - **Success Definition **Metrics, adoption, feedback that signals success?
 - **Stakeholders **Executive sponsor, users, customers, team leads?
 - **Timeline **Hard deadline, flexible, market window?
#### Phase 2 — Scope & Requirements (Q7–12)
 - **Scope Statement **What is in scope, what is out? MVP vs. future?
 - **Primary Users **Customer, internal, both?
 - **Key Workflows **3–4 critical user flows?
 - **Constraints **Non-negotiable technology, budget, compliance?
 - **Dependencies **Other projects or systems this depends on?
 - **Known Unknowns **Risks or uncertainties?
#### Phase 3 — Team & Capacity (Q13–16)
 - **Team Size **Developers, designers, QA?
 - **Team Experience **Domain familiarity?
 - **Existing Patterns **Tech stack, design patterns?
 - **Velocity **Story points per sprint?
#### Phase 4 — Acceptance & Validation (Q17–20)
 - **Acceptance Criteria Style **Given/When/Then, checklist, other?
 - **Definition of Done **Code review, tests, deployment, user validation?
 - **Validation Approach **Demo, metrics, user testing?
 - **Rollback Plan **Safety net if something does not work?
#### Phase 5 — Knowledge & Decisions (Q21–23)
 - **Decision Constraints **Platform choices, compliance that limit options?
 - **Tribal Knowledge **What does every PM wish they knew about this project?
 - **Competitive Intel **How do competitors handle this? Starter Prompt Templates copy and paste ▶ Prompt Template — Scenario A (Requirements Capture) Copy
```
You are a PO/PM Second Brain using the spec-kit methodology (Knowledge → Specification → Plan → Execution).

I need to capture requirements for [FEATURE/PROJECT NAME].

Interrogate me through 5 phases before generating anything:
Phase 1: Business goal, current state, success definition, stakeholders, timeline
Phase 2: Scope (in/out), primary users, critical workflows, constraints, dependencies
Phase 3: Team size, experience, velocity
Phase 4: Acceptance criteria format, definition of done, validation approach
Phase 5: Decision constraints, tribal knowledge

Then generate:
- 3-5 user stories in Given/When/Then format
- Edge cases for each story
- Dependency map
- Priority ranking with rationale
```
Prompt Template — Scenario D (Roadmap Prioritization) Copy
```
You are a PO/PM Second Brain.
I have [N] features to prioritize for [TIME HORIZON].

Ask me these questions before scoring:
1. What is the primary business goal for this period?
2. What is the team's capacity (story points per sprint, sprints available)?
3. What are the hard constraints (compliance, dependencies, deadlines)?
4. What does "high value" mean for this business? (Revenue, retention, cost savings?)
5. What are the top 3 risks we want to avoid?

Then produce a ranked roadmap using:
 Priority Score = (Value × 3 + Revenue Impact) - (Effort × 2 + Risk × 1.5)
 Tier 1: Launch now | Tier 2: Plan for next quarter | Tier 3: Defer

Format: table with Rank, Feature, Value, Effort, Risk, Impact, Owner, Status, Rationale
```
Output Templates user story · sprint backlog · stakeholder report ▶ User Story with Acceptance Criteria Copy
```
## User Story: [Feature Title]

**Story ID**: PROJ-123
**Sprint**: Q2 Sprint 2
**Priority**: High
**Estimate**: 8 points

### Description
As a [user type], I want to [action], so that [benefit].

### Acceptance Criteria

Given [context]
When [action]
Then [expected outcome]

Given [context]
When [action]
Then [expected outcome]

### Edge Cases
- What if [edge case A]? → [handling]
- What if [edge case B]? → [handling]

### Dependencies
- Requires [system/story] (tracked in PROJ-XXX)

### Success Criteria
- [ ] [Metric 1]
- [ ] [Metric 2]
```
Stakeholder Status Report Copy
```
## Q[N] Progress Report
**Period**: [Date range]
**Overall Status**: GREEN / YELLOW / RED

## Executive Summary
**The Ask**: [One ask with clear impact and cost]

## Progress Snapshot

### Completed
- [Story/feature] — [outcome metric]

### In Progress
- [Story/feature] — [% complete, on track / at risk]

## Metrics
| Metric            | Target | Current | Status |
|-------------------|--------|---------|--------|
| [Metric 1]        | [val]  | [val]   | GREEN  |
| [Metric 2]        | [val]  | [val]   | YELLOW |

## Risk Register
| Risk           | Impact | Status  | Owner | Mitigation |
|----------------|--------|---------|-------|-----------|
| [Risk 1]       | High   | Active  | [name]| [plan]   |

## What We Need From You
| Ask               | Impact                    | Timeline         |
|-------------------|---------------------------|------------------|
| [Decision needed] | [What slips if delayed]   | [Date]           |
```
Prioritized Roadmap Copy
```
## Q[N]-Q[N+1] Product Roadmap

### Prioritization Formula
Priority Score = (Value × 3 + Revenue Impact) - (Effort × 2 + Risk × 1.5)

### Tier 1: Launch Now
| Rank | Feature | Value | Effort | Risk | Impact | Owner | Status |
|------|---------|-------|--------|------|--------|-------|--------|
| 1    | [name]  | 5     | 3      | 1    | [why]  | [who] | [%]    |

### Tier 2: Plan Next Quarter
| Rank | Feature | Value | Effort | Risk | Impact | Owner | Status |
|------|---------|-------|--------|------|--------|-------|--------|
| 5    | [name]  | 4     | 4      | 2    | [why]  | [who] | backlog|

### Tier 3: Defer
| Rank | Feature | Reason for Deferral |
|------|---------|---------------------|
| 9    | [name]  | Low demand, high complexity |
```
skill spec ---
name : dl-second-brain
version : 1.0
description : Priority building, team scaling, client status reporting, delivery risk assessment
patterns : [ABCD-priorities, RAG-status, risk-matrix, onboarding-plan]
---
## Delivery Lead Second Brain Gathers rich context about team, client, project, and business before generating strategies. Output is matrices, CSV exports, and checklists — not narratives. Context is everything Structure gets rewarded You are the retrieval system ⇩ Download SKILL.md When to use each scenario
#### A — Priority Building "I need to build priorities for Q1 and Q2" 3–5 priorities in CSV format with ABCD reflections, metrics, resource mapping.
#### B — Team Scaling "I am onboarding 3 new engineers" Phased onboarding plan, ADR template, knowledge-base structure.
#### C — Client Status Reporting "I need to report to steering committee" RAG status summary, milestone tracker, risk escalation, client asks, next-week plan.
#### D — Risk Assessment "Too many risks, need a systematic approach" Risk matrix with impact/probability, mitigation strategies, owners and timelines. Interrogation Framework 17 questions · 4 phases ▶
#### Phase 1 — Team & Project Context (Q1–6)
 - **Team Composition **How many people? Roles? Remote/collocated? Time zones?
 - **Project Budget **Total contract value? Burn rate? Contingency?
 - **Project Scope **3–5 main deliverables? Timeline to completion?
 - **Success Metrics **How does the client measure success? KPIs?
 - **Delivery Methodology **Agile, waterfall, hybrid? Sprint length?
 - **Current Phase **Discovery, build, testing, launch, sustain?
#### Phase 2 — Client & Stakeholder Dynamics (Q7–10)
 - **Client Stakeholder Map **Who makes decisions? Data-driven, political, or consensus style?
 - **Relationship Health **Client satisfaction level? Any tensions or escalations?
 - **Client Team **Are they embedded? Do they have capacity to review/approve?
 - **Change Management **How resistant is the org to the change you are delivering?
#### Phase 3 — Risk & Dependencies (Q11–14)
 - **Known Risks **What keeps you up at night? Top 3 risk items?
 - **Dependencies **What is blocking progress? External dependencies?
 - **Escalation Paths **Who do you escalate to? Decision timeline?
 - **Resource Constraints **Skills gaps, competing priorities?
#### Phase 4 — Organizational Context (Q15–17)
 - **Portfolio Context **How does this fit broader program/portfolio?
 - **Organizational Readiness **Is the org ready for this change?
 - **Tribal Knowledge **What does every DL wish they knew about this type of project? Starter Prompt Templates copy and paste ▶ Prompt Template — Scenario A (Priority Building with ABCD) Copy
```
You are a Delivery Lead Second Brain.
I need to build FY priorities for [PROGRAM/PROJECT NAME].

Before generating anything, ask me:
Phase 1: Team composition, budget, deliverables, success metrics, methodology, current phase
Phase 2: Stakeholder map, relationship health, client capacity, change management
Phase 3: Top 3 risks, blocking dependencies, escalation paths
Phase 4: Portfolio context, org readiness, tribal knowledge

Then generate:
- 3-5 priorities in CSV format using ABCD columns:
 Priority, Action, Behavior, Context, Delivered, Owner, Timeline, Metrics, Notes
- Strategic narrative for steering committee
- Risk matrix (top 5 risks with Impact, Probability, Mitigation, Owner)
- Execution checklist by quarter
```
Prompt Template — Scenario C (Weekly Status Report) Copy
```
You are a Delivery Lead Second Brain.
I need to write a weekly status report for [PROJECT NAME] to send to [AUDIENCE].

Ask me:
1. What is the overall status? GREEN / YELLOW / RED — and why?
2. What milestones were supposed to happen this week? What happened?
3. What are the top 3 achievements?
4. What risks have escalated or changed since last week?
5. What do you need the client/leadership to decide or action this week?
6. What is the specific plan for next week?

Then generate a ready-to-send status report with:
- Executive summary (2 sentences)
- Milestone tracker (RAG table)
- Achievements this week
- Risks & escalations (with specific impact if not resolved)
- Next week plan
- Client asks with deadlines
```
Output Templates ABCD CSV · status report · risk matrix · onboarding plan ▶ Priority Building — ABCD CSV Format Copy
```
Priority,Action,Behavior,Context,Delivered,Owner,Timeline,Metrics,Notes
"Q1 Foundation","[what you are doing]","[how — quality, coverage, standards]","[why it matters — business impact]","[what success looks like]","[owner]","[dates]","[measurable metrics]","[dependencies, risks]"
"Q2 Adoption","[what you are doing]","[how — quality, coverage, standards]","[why it matters — business impact]","[what success looks like]","[owner]","[dates]","[measurable metrics]","[dependencies, risks]"
```
Weekly Status Report Copy
```
## Weekly Status Report: [Project Name]
**Week of**: [Date]
**Overall Status**: GREEN / YELLOW / RED

### 1. Milestone Tracker
| Deliverable     | Target Date | Status | Progress | Notes |
|-----------------|------------|--------|----------|-------|
| [Milestone 1]   | [date]      | GREEN  | 100%     | [note]|
| [Milestone 2]   | [date]      | YELLOW | 65%      | [risk]|

### 2. Key Achievements This Week
- [Achievement 1]
- [Achievement 2]

### 3. Risks & Escalations
**ESCALATION NEEDED**: [Risk description]
- **Impact**: [What slips if not resolved]
- **Mitigation in progress**: [What is being done]
- **Ask**: [Specific decision or action needed]

### 4. Next Week's Plan
- [ ] [Action 1]
- [ ] [Action 2]

### 5. Client Asks / Open Items
| Ask     | Owner   | Status   | Timeline |
|---------|---------|----------|----------|
| [ask 1] | [client]| Pending  | [date]   |
```
Risk Assessment Matrix Copy
```
| Risk                      | Probability | Impact | Score | Mitigation                 | Owner  | Timeline |
|---------------------------|-------------|--------|-------|----------------------------|--------|----------|
| [Key vendor delay]        | Medium      | High   | 6     | Build contingency layer    | [name] | Week 1   |
| [Scope creep]             | High        | High   | 8     | Change control board       | [name] | Immediate|
| [Team capacity — testing] | Medium      | High   | 6     | Hire contract QA for wk 8  | [name] | Week 4   |

Score = Probability (1-3) × Impact (1-3)
```
Team Onboarding Plan Copy
```
## Onboarding Plan: [New Team Member]

### Phase 1: Week 1 — Foundation
| Day   | Activity                                     | Owner    | Duration |
|-------|----------------------------------------------|----------|----------|
| 1     | Project mission, scope, success criteria      | [DL]     | 2h       |
| 1     | Meet core team + role clarity                 | [PM]     | 1h       |
| 2     | Client context + stakeholder map              | [AE]     | 1.5h     |
| 2     | Current phase deep-dive + blockers            | [TL]     | 2h       |
| 3     | Documentation review (plan, ADRs, design docs)| Self     | 3h       |
| 4-5   | Shadow team ceremonies                        | [Team]   | 5h       |

### Phase 1 Checkpoint
- [ ] Can articulate project goal in 2 sentences
- [ ] Knows all core team members and roles
- [ ] Understands current phase and top 3 blockers
- [ ] Attended at least 3 ceremonies

### Phase 3: Week 4-6 — First Real Task
- Assigned task has clear success criteria
- Mentor reviews work before integration
- Autonomy increases over time
```
skill spec ---
name : tl-second-brain
version : 1.0
description : ADRs, metaprompting, technical spike planning, team technical standards
patterns : [Tree-of-Thoughts, ADR, metaprompt, cursorrules]
---
## Tech Lead Second Brain Guides architectural decisions through Tree of Thoughts (GENERATE→EVALUATE→DECIDE), builds metaprompts for team amplification, and codifies standards as .cursorrules. Context is everything Structure gets rewarded You are the retrieval system ⇩ Download SKILL.md When to use each scenario
#### A — Architecture Decision Record "Should we decompose our monolith or use strangler fig?" 3 options via Tree of Thoughts, ADR document, implementation roadmap.
#### B — Metaprompting "I need each engineer to get role-specific architecture guidance" Metaprompt with backend/DevOps/QA/security role branches, usage examples.
#### C — Technical Spike Planning "Should we migrate to Kubernetes? Need data before committing" Spike plan with investigation phases, success criteria, decision gates, time-box.
#### D — Team Technical Standards "Our async/await patterns are inconsistent across the team" .cursorrulesfile with patterns, anti-patterns, examples, rationale. Interrogation Framework 17 questions · 4 phases ▶
#### Phase 1 — Current Architecture (Q1–6)
 - **Current System Design **Monolith, microservices, event-driven, hybrid?
 - **Technology Stack **Languages, frameworks, databases, message queues, versions?
 - **Scale Context **Transactions/sec? Users? Data volume? Growth rate?
 - **Team Size & Skills **How many engineers? Key expertise areas? Skill gaps?
 - **Operational Maturity **CI/CD, monitoring, on-call model?
 - **Technical Debt **Biggest pain point? What slows down development?
#### Phase 2 — Target State & Constraints (Q7–10)
 - **Strategic Goal **What problem are we solving? Business driver?
 - **Success Metrics **Latency, throughput, developer velocity?
 - **Hard Constraints **Budget, timeline, compliance, team availability?
 - **Integration Requirements **Other systems that must integrate?
#### Phase 3 — Organizational Context (Q11–14)
 - **Team Maturity **Can the team handle microservices, distributed systems, new frameworks?
 - **Appetite for Change **How much disruption is acceptable?
 - **Support & Tooling **What infrastructure already exists?
 - **Decision Authority **Who decides? What is the approval process?
#### Phase 4 — Risk & Knowledge (Q15–17)
 - **Similar Decisions **Have we done something like this before?
 - **Hidden Risks **What keeps you up at night about this decision?
 - **Decision Timeline **When does this need to be made? How long to implement? Starter Prompt Templates copy and paste ▶ Prompt Template — Scenario A (ADR with Tree of Thoughts) Copy
```
You are a Tech Lead Second Brain using Tree of Thoughts (GENERATE→EVALUATE→DECIDE).
I need an Architecture Decision Record for: [DECISION QUESTION]

Before generating options, interrogate me through 4 phases:
Phase 1: Current architecture, tech stack, scale, team composition, tech debt
Phase 2: Strategic goal, success metrics, hard constraints, integration requirements
Phase 3: Team maturity, change appetite, existing tooling, decision authority
Phase 4: Prior similar decisions, risks, decision timeline

Then generate:
ADR-NNN with:
- Context (problem statement, constraints, success criteria)
- 3 fundamentally different options (not variations on one idea)
 Each option: THINK (how it works) → EVALUATE (pros/cons/risks)
- Decision with clear rationale (which constraint it best fits)
- Consequences (positive, negative, action items with timeline)
```
Prompt Template — Scenario B (Metaprompt Generation) Copy
```
You are a Tech Lead Second Brain.
I want a metaprompt for [ARCHITECTURE TOPIC — e.g., "caching strategy design"].

The metaprompt should, when given to any team member, generate role-specific guidance.

Ask me:
1. What is the architectural decision or topic?
2. What are the performance targets and constraints?
3. What roles need different guidance? (Backend, DevOps, QA, Security?)
4. What are the team's existing patterns I want to enforce?
5. What are the top 3 anti-patterns we want to prevent?

Then generate a metaprompt that includes:
- Primary mission (what the role should produce)
- Interrogation questions the role must answer first
- Role-specific generation sections (one per role)
- Rationale section explaining key trade-offs
```
Prompt Template — Scenario D (.cursorrules Team Standards) Copy
```
You are a Tech Lead Second Brain.
I need a .cursorrules file for [PROJECT/TEAM NAME].

Ask me:
1. What is the one-sentence vision for our architecture?
2. What are the 3-4 most critical patterns to enforce? (async/await, error handling, logging, service contracts?)
3. For each pattern: what does the team do WRONG today?
4. For each pattern: what does the CORRECT implementation look like?
5. What are the top 3 anti-patterns you keep seeing in code review?
6. Under what conditions can engineers break these patterns?

Then generate a .cursorrules file with:
- Vision statement
- Core patterns (each with PATTERN code example and ANTI-PATTERN code example)
- Code review checklist
- When to break the rules (explicit conditions)
```
Output Templates ADR · spike plan · .cursorrules ▶ Architecture Decision Record (ADR) Copy
```
## ADR-NNN: [Decision Title]

### Context
- **Problem Statement**: What decision are we making and why?
- **Constraints**: Timeline, budget, team size, technical/organizational limits
- **Success Criteria**: How will we measure if this was the right choice?

### Options (Tree of Thoughts)

#### Option A: [Approach Name]
**THINK**: How would this work? (architecture sketch)
**EVALUATE**:
Pros:
- [pro 1]
Cons:
- [con 1]
Risks:
- [ ] High: [risk]
- [ ] Medium: [risk]

#### Option B: [Approach Name]
[same structure]

#### Option C: [Approach Name]
[same structure]

### Decision
**CHOOSE**: Option [A/B/C]
**Rationale**: Best fits [constraint]. Team capability: [assessment]. Risk profile: [acceptable risks].

### Consequences
#### Positive
- [benefit 1]
#### Negative
- [trade-off 1]
#### Action Items
- [ ] [Action] — [Owner] — [Date]
```
Technical Spike Plan Copy
```
## Technical Spike: [Investigation Topic]

### Objective
**Question**: Should we migrate to [technology/pattern]?
**Time-box**: [1-2 weeks]
**Success Criteria**:
- [ ] Proof-of-concept running
- [ ] Performance benchmarks vs. current system
- [ ] Team impact assessment (learning curve, hiring needs)
- [ ] 3-year cost/benefit analysis
- [ ] Risk mitigation strategy documented

### Decision Gates
| Gate            | Criteria                              | Owner       | Target |
|-----------------|---------------------------------------|-------------|--------|
| POC Success     | POC runs on developer laptop          | [Engineer]  | Day 3  |
| Performance     | Meets latency targets                 | [Engineer]  | Day 6  |
| Team Fit        | Learning curve acceptable             | [TL]        | Day 7  |
| Financial       | 3-year TCO justifies migration cost   | [PM]        | Day 8  |

### Explicitly Not in Scope
- Full migration plan
- Integration with all downstream systems
- Vendor negotiation
```
.cursorrules — Team Standards File Copy
```
# .cursorrules — Team Technical Standards for [Project]

## Vision
[1 sentence: "We are an async-first microservices team that values observable deployments."]

## Core Patterns

### 1. Async/Await
# PATTERN
async def get_user(user_id: int):
   user = await db.query(f"SELECT * FROM users WHERE id = {user_id}")
   return user

# ANTI-PATTERN
def get_user(user_id: int):  # Blocks request thread
   return requests.get(f"https://userapi.com/{user_id}")

### 2. Error Handling
# PATTERN — Named exceptions with full context
class PaymentProcessingError(Exception):
   def __init__(self, user_id: int, amount: float, reason: str): ...

# ANTI-PATTERN
except Exception as e:
   logger.error(f"Error: {e}")  # No context!

### 3. Logging
# PATTERN — Structured JSON, always queryable
logger.info("order_created", extra={"order_id": order.id, "amount": order.total})

# ANTI-PATTERN
logger.info(f"Order {order.id} created")  # Not queryable

## Code Review Checklist
- [ ] No synchronous I/O in async functions
- [ ] All exceptions named and contextual
- [ ] Logging is structured JSON
- [ ] Service boundaries clear (input/output contracts)
- [ ] Tests cover happy path + at least 2 error scenarios
- [ ] Type hints on all function signatures

## When to Break These Patterns
Only with explicit TL approval and documented rationale.
File issue: `patterns: [pattern-name]: [reason for exception]`
```
Tree of Thoughts Pattern Reference ▶ GENERATE What are 3 fundamentally different approaches? Not variations — genuinely different options that each solve the problem in a distinct way. EVALUATE For each option: pros, cons, and risks. Be honest about trade-offs. Prevent premature convergence on the familiar option. DECIDE Which option best balances constraints and team capabilities? State rationale explicitly. Acknowledge which risks you are accepting. skill spec ---
name : make-skills
version : 1.0
description : Capstone — turn your repeated work into a production-ready interrogation-driven skill
phases : [task-discovery, pattern-extraction, skill-generation]
output : SKILL.md file you can save and use immediately
---
## Make Skills — Capstone Stop using skills. Start building them. A 3-phase workflow that extracts the pattern hidden in your weekly work and turns it into a reusable AI workflow. Context is everything Structure gets rewarded You are the retrieval system ⇩ Download SKILL.md **The Capstone Reveal **— After you generate your first skill you will see: it ASKS questions (retrieval), it ASSEMBLES your answers into structured context (augmentation), it FEEDS that context to the AI for generation (generation). You just built a RAG system. Every skill is a RAG system. When to build a skill
#### A — Repeatable Document Creation "I create [documents] at least weekly" Sales decks, RFP responses, project briefs, technical specs.
#### B — Code Generation or Migration "I build [code structures] repeatedly" Microservice scaffolding, API contract implementation, database migration planning.
#### C — Analysis or Decision Support "I analyze [situations] and produce structured recommendations" Architecture reviews, competitive analysis, incident post-mortems.
#### D — Communication or Planning "I create [communications] regularly" Meeting agendas, status reports, project proposals, email templates. 3-Phase Workflow task discovery · pattern extraction · skill generation ▶
#### Phase 1 — Task Discovery (15 min)
 - **Weekly Task **What task do you repeat at least weekly?
 - **Current Process **Walk me through your steps today, step by step.
 - **Input Requirements **What information do you need before starting?
 - **Quality Definition **What does GOOD output look like? What does BAD look like?
 - **Audience **Who uses your output and how?
#### Phase 2 — Pattern Extraction (10 min)
 - **Task Category **Code generation, document creation, analysis, communication, or planning?
 - **Context Requirements **What 5–7 pieces of information always change but are always needed?
 - **Question Design **What questions should the skill ask to gather that context?
 - **Output Structure **What sections, ordering, and format for the output?
#### Phase 3 — Skill Generation (automatic)
 - **Formatting **Converts your answers into proper SKILL.md structure
 - **Example Generation **Creates a worked example (interrogation → output)
 - **Integration Notes **Explains how the skill connects to RAG, ReAct, bootcamp patterns Starter Prompt Template copy and paste ▶ Prompt Template — Make-Skills Capstone Copy
```
You are a Make-Skills capstone assistant. Help me build a production-ready SKILL.md for a task I repeat at work.

Run me through 3 phases:

PHASE 1 — Task Discovery (ask all 5 questions, one at a time):
1. What task do you repeat at least weekly at work?
2. Walk me through how you do it today, step by step.
3. What information do you need to gather before you start?
4. What does GOOD output look like? What does BAD look like?
5. Who is the audience for your output?

PHASE 2 — Pattern Extraction (ask all 4 questions):
6. Which category best fits your task: code generation, document creation, analysis, communication, or planning?
7. What are 5-7 pieces of context that always change but are always needed?
8. What questions should the skill ask the user to gather that context?
9. What structure should the output follow? (section headings, ordering, format)

PHASE 3 — Generate the skill file:
Using all my answers, generate a complete SKILL.md with:
- YAML frontmatter (name, version, description)
- Overview section (what it does, 3 intuitions)
- Structured interrogation framework (formatted as phases)
- Output format specification (with template)
- Complete worked example (interrogation → output)
- Reflection: explain what the participant just built (the RAG reveal)
```
Generated Skill File Template the structure your skill will follow ▶ SKILL.md — Generated Structure Copy
```
---
name: [your-task-name]
description: [your task] interrogation-driven skill
version: 1.0
---

# [Your Skill Name]

## Overview
[Purpose, target audience, core value]
[The 3 bootcamp intuitions as they apply to your task]

## Key Capabilities
[What this skill does — derived from Phase 2 answers]

## Structured Interrogation Framework

### Phase 1: [Context gathering]
[Your questions, formatted as numbered list with bold category + question]

### Phase 2: [Structure definition]
[Your output structure requirements]

## Output Format Specification

```[your format]
[Your template with all sections filled in with examples]
```

## Example: Complete Workflow

### Interrogation Phase
[Worked example: Q1: → "answer" Q2: → "answer" ...]

### Generated Output
[Sample output your skill produces from those answers]

## Reflection: What You Just Built

- It ASKS questions → that is retrieval
- It ASSEMBLES your answers into structured context → that is augmentation
- It FEEDS that context to the AI → that is generation

You just built a RAG system. Every skill is a RAG system.
```
Should you build a skill for this task? ▶

| Build a skill if…  || Skip skills if…  |

| You do this at least weekly  || You do it once per quarter  |

| Output affects others  || Output is just for you  |

| It takes 30+ minutes  || It takes 2 minutes (template works fine)  |

| You always gather the same information  || The process changes dramatically each time  |

| Others could use it too  || It is already fully automated  |

**Skill composition: **Once you have a few skills you can chain them. Spec-generator output feeds into plan-generator, which feeds into test-strategy-generator. That is a workflow, not just a skill. Joey Lopez · 2026 · [jrlopez.dev ]()[home ]()· [bootcamp ]()· [developer ]()· [PO/PM ]()· [delivery ]()· [tech lead ]()· [make skills ]()