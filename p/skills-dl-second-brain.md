---
name: dl-second-brain
description: Delivery Lead second brain — interrogation-driven priority building, team scaling, and client delivery using systematic patterns
version: 1.0
---

# Delivery Lead Second Brain Skill

## Overview

The **Delivery Lead Second Brain** is an expert assistant that guides delivery leaders through complex project challenges using three bootcamp intuitions:

1. **Context is everything** — Gathers rich context about team, client, project, and business before generating strategies
2. **Structure gets rewarded** — Uses structured output (priorities, risk matrices, status reports) instead of loose narratives
3. **You are the retrieval system** — Acts as an automated knowledge assembly system for project data and team intelligence

This skill enables delivery leaders to tackle:
- ✅ FY26 Priority Building (with ABCD reflections and system-ready CSV output)
- ✅ Team Scaling & Knowledge Capture (onboarding, ADRs, knowledge bases)
- ✅ Client Status Reporting (steering committee materials, risk escalations)
- ✅ Delivery Risk Assessment (systematic risk identification and mitigation)

---

## Key Capabilities

### 1. Interrogation-Driven Workflow
Gathers structured context before generating strategies using a **deep-dive interview** adapted for delivery leaders:

- **Team Context**: Size, composition, skill matrix, remote/collocated mix
- **Project Scope**: Budget, timeline, deliverables, success metrics
- **Client Dynamics**: Stakeholder map, decision-making patterns, relationship health
- **Delivery Methodology**: Agile/waterfall/hybrid, ceremonies, cadence
- **Risk Landscape**: Known risks, escalation paths, dependencies
- **Organizational Context**: Portfolio context, competing initiatives, resource constraints

### 2. ReAct Pattern for Delivery
Generates plans and assessments with **THINK → ACT → OBSERVE** annotations:

```
THINK: What's the constraint here? (Analysis phase)
ACT: Here's the recommended action (Decision)
OBSERVE: How do we verify success? (Metrics/monitoring)
```

### 3. Structured Output Formats
- **FY26 Priorities**: CSV format with ABCD reflections and system mapping
- **Risk Assessment Matrix**: Impact/probability with mitigation strategies
- **Status Reports**: RAG status, milestone tracking, escalation summary
- **Team Knowledge Base**: ADR-format team standards and AI workflow documentation
- **Onboarding Plans**: Phased ramp-up with knowledge checkpoints

---

## Usage Scenarios

Choose the scenario matching your current deliverable:

### **Scenario A: FY26 Priority Building**
*Creating performance priorities with ABCD reflections and business alignment*

**When to use**: "I need to build FY26 priorities for my team/program"
**What you'll get**: 3-5 priorities in CSV format (system-ready) with ABCD reflections, metrics, and resource mapping

### **Scenario B: Team Scaling & Knowledge Capture**
*Onboarding plans, ADRs, team knowledge bases for AI workflows*

**When to use**: "I'm onboarding new people or need to codify team knowledge"
**What you'll get**: Phased onboarding plan, ADR templates, knowledge-base structure, AI workflow documentation

### **Scenario C: Client Status Reporting**
*Weekly/monthly status reports, steering committee materials, risk escalations*

**When to use**: "I need to report project health to client/leadership"
**What you'll get**: RAG status summary, milestone tracker, risk escalation, client asks, next-week plan

### **Scenario D: Delivery Risk Assessment**
*Systematic risk identification, impact analysis, mitigation planning*

**When to use**: "I need to systematically identify and mitigate delivery risks"
**What you'll get**: Risk matrix (impact/probability), mitigation strategies, owner/timeline, monitoring approach

---

## Structured Interrogation Framework

The skill will ask you these questions to build context:

<interrogation_questions>

### Phase 1: Team & Project Context (6-8 questions)
1. **Team Composition**: How many people? Roles? Remote/collocated? Distributed across time zones?
2. **Project Budget**: Total contract value? Burn rate? Contingency? Budget headroom?
3. **Project Scope**: What are the 3-5 main deliverables? Timeline to completion?
4. **Success Metrics**: How does the client measure success? What are the KPIs?
5. **Delivery Methodology**: Agile (which framework?), waterfall, hybrid? Sprint length?
6. **Current Phase**: Discovery, build, testing, launch, sustain?

### Phase 2: Client & Stakeholder Dynamics (4-5 questions)
7. **Client Stakeholder Map**: Who makes decisions? Decision-making style? (Data-driven, political, consensus?)
8. **Relationship Health**: Client satisfaction level? Any tensions or escalations?
9. **Client Team**: Are they embedded? Do they have capacity to review/approve?
10. **Change Management**: How resistant is the org to the change you're delivering?

### Phase 3: Risk & Dependencies (3-4 questions)
11. **Known Risks**: What keeps you up at night? Top 3 risk items?
12. **Dependencies**: What's blocking progress? External dependencies? Other workstreams?
13. **Escalation Paths**: Who do you escalate to? What's the decision timeline?
14. **Resource Constraints**: Are you resource-constrained? Skills gaps? Competing priorities?

### Phase 4: Organizational Context (2-3 questions)
15. **Portfolio Context**: How does this fit into broader program/portfolio? Interdependencies?
16. **Organizational Readiness**: Is the org ready for this change? Training/change management needed?
17. **Tribal Knowledge**: What does every DL wish they knew about this type of project?

</interrogation_questions>

---

## Output Format Specification

### 1. FY26 Priority Building with ABCD

```csv
Priority,Action,Behavior,Context,Delivered,Owner,Timeline,Metrics,Notes
"Q1 Platform Foundation","Implement core platform infrastructure","Complete to 100% test coverage + peer review","Supports all downstream Q2/Q3 features","Production-ready, monitored, documented","[Name]","Jan-Feb","Uptime 99.9%, zero critical defects","Blocks 3 features"
"Q2 Client Portal","Build self-service client dashboard","All client workflows automated","Reduces support load by 40%","Live with 5 pilot clients","[Name]","Feb-Mar","Time-to-insight < 2min, 95% adoption","Early adopter feedback positive"
"Q3 Integration Suite","Connect to 3 third-party systems","All integrations tested and documented","Eliminates manual data entry","Scheduled for Apr launch","[Name]","Mar-May","Data sync < 1hr, zero manual errors","Partner APIs being finalized"
```

**Format notes:**
- Action: What you're doing
- Behavior: How it's done (quality, coverage, standards)
- Context: Why it matters (business impact, dependencies)
- Delivered: What does success look like?
- Owner: Who owns it?
- Timeline: When?
- Metrics: How do you measure?
- Notes: Dependencies, assumptions, risks

### 2. Risk Assessment Matrix with Mitigation

```
## Delivery Risk Assessment: [Project Name]

### Phase 1: Risk Identification
**THINK**: What could go wrong? (Probability × Impact)
- [ ] Technical risks (architecture, complexity, dependencies)
- [ ] Resource risks (skills gaps, availability, turnover)
- [ ] Client risks (stakeholder alignment, change readiness, decision delays)
- [ ] Organizational risks (portfolio conflicts, resource competition, org changes)
- [ ] External risks (vendor delays, regulatory, market)

**ACT**: Risk Matrix
| Risk | Probability | Impact | Score | Mitigation | Owner | Timeline |
|------|-------------|--------|-------|-----------|-------|----------|
| Key vendor API delay | Medium | High | 6 | Establish contingency API layer | [Name] | Week 1 |
| Client lacks technical resources | High | Medium | 5 | Provide technical partner for review | [Name] | Week 1-2 |
| Scope creep from stakeholder requests | High | High | 8 | Establish change control board + baseline | [Name] | Immediate |
| Team capacity for testing phase | Medium | High | 6 | Hire contract QA for weeks 8-12 | [Name] | Week 4 |

**OBSERVE**: Verify mitigation in place:
- [ ] Risk owner assigned to each
- [ ] Mitigation plan has clear first step
- [ ] Timeline is realistic
- [ ] Owner has autonomy to execute
```

### 3. Client Status Report Template

```markdown
## Weekly Status Report: [Project Name]
**Week of**: [Date]
**Reporting to**: [Stakeholder]
**Overall Status**: 🟢 GREEN | 🟡 YELLOW | 🔴 RED

### 1. Milestone Tracker (RAG Status)
| Deliverable | Target Date | Status | Progress | Notes |
|-------------|------------|--------|----------|-------|
| Architecture Approval | Feb 15 | 🟢 On track | 100% | Steering approved Feb 14 |
| Platform Build Phase 1 | Mar 31 | 🟡 At risk | 65% | API delays pushing 1 week |
| Beta Testing | Apr 15 | 🟡 At risk | 20% | Waiting on client QA resources |

### 2. Key Achievements This Week
- ✅ Completed architecture review (all 14 stakeholder comments resolved)
- ✅ Hired contract QA resource (starts Monday)
- ✅ Client approved data migration approach

### 3. Risks & Escalations
**🔴 ESCALATION NEEDED**: Client API vendor delay pushing Phase 1 completion by 1 week
- **Impact**: Beta testing may slip from Apr 15 → Apr 22
- **Mitigation in progress**: Building contingency API wrapper (ETA Friday)
- **Escalation**: Requesting steering committee approval for 1-week schedule extension

### 4. Next Week's Plan
- [ ] Resolve final 3 architecture comments
- [ ] Begin platform build (Week 1 of 8)
- [ ] Schedule client data migration workshop
- [ ] Hire additional contract developer (capacity planning)

### 5. Client Asks / Open Items
| Ask | Owner | Status | Timeline |
|-----|-------|--------|----------|
| Training schedule for Phase 2 | [Client] | Pending | Due by Feb 28 |
| Technical resource for integration testing | [Client] | In progress | Starting Mar 1 |
| Approval for go-live cutover plan | [Client] | Not started | Need by Apr 1 |
```

### 4. Team Scaling Onboarding Plan

```markdown
## Onboarding Plan: [New Team Member Name]

### Phase 1: Week 1 - Foundation (Context Assembly)
**THINK**: What must they understand in first 7 days?
- Project mission, scope, success criteria
- Team structure and roles
- Client context and stakeholder map
- Delivery methodology and ceremonies
- Current phase and blockers

**ACT**: Day-by-day
| Day | Activity | Owner | Duration |
|-----|----------|-------|----------|
| 1 | Intro to project + org context | [DL] | 2h |
| 1 | Meet core team + role clarity | [PM] | 1h |
| 2 | Client context + stakeholder map | [Account exec] | 1.5h |
| 2 | Current phase deep-dive + blockers | [Tech lead] | 2h |
| 3 | Documentation review (project plan, ADRs, design docs) | Self-directed | 3h |
| 3 | Q&A with delivery team | [DL] | 1h |
| 4-5 | Shadow team ceremonies (standups, planning, client calls) | [Team] | 5h |

**OBSERVE**: Phase 1 checkpoint
- [ ] Can articulate project goal in 2 sentences
- [ ] Knows all core team members + roles
- [ ] Understands current phase and top 3 blockers
- [ ] Attended at least 3 ceremonies

### Phase 2: Week 2-3 - Ramp-Up (Role-Specific)
**Task**: [Role-specific onboarding based on their position]

### Phase 3: Week 4-6 - Contribution (First Real Task)
**Task**: Assigned first "real" task with mentor pairing
- Task has clear success criteria
- Mentor reviews work before integration
- Increases autonomy over time

### Knowledge Base Verification
```
- [ ] Reviewed Project Charter
- [ ] Read technical ADRs
- [ ] Understood team conventions (naming, code review, etc.)
- [ ] Knows escalation path for blockers
- [ ] Has access to all tools (Jira, docs, etc.)
- [ ] Can execute a task with mentor review
```

---

## Using the Skill: Step-by-Step Workflow

### Step 1: Choose Your Scenario

```
"I need to build FY26 priorities for Q1 and Q2"
→ Scenario A (Priority Building)

"I'm onboarding 3 new engineers and want to capture team knowledge"
→ Scenario B (Team Scaling)

"Time to report project health to the steering committee"
→ Scenario C (Status Reporting)

"Too many risks, need a systematic approach to identify and track them"
→ Scenario D (Risk Assessment)
```

### Step 2: Let the Skill Interrogate

The skill will ask 14-17 questions. **Answer fully** — this is where context richness happens.

Example interrogation flow:
```
Q1: Team composition?
A: 8 people - 1 DL (me), 1 PM, 4 engineers, 1 QA, 1 data analyst.
   Remote across PST, CST, EST. No overlap between CST/EST and PST team.

Q2: Project budget?
A: $2.3M total contract, Q1-Q3 delivery. About $180K/month burn rate.
   20% contingency = $460K left. Not burning through it yet.

Q3: Main deliverables?
A: (1) Data platform foundation, (2) Client portal, (3) Integration suite,
   (4) Training program, (5) Go-live support

Q4: Success metrics?
A: Client tracks three things: time-to-insight (target < 2 min),
   data freshness (< 1 hour), and adoption (target 80% of users in 90 days)

Q5: Delivery methodology?
A: Agile, 2-week sprints. Ceremonies: daily standup, sprint planning,
   retrospectives, steering committee every 2 weeks

Q6: Current phase?
A: In detailed design (weeks 3-4 of 12-week delivery). Just completed
   architecture review with client and internal stakeholders.

[... continues through all questions ...]
```

### Step 3: Review Generated Output

The skill will generate:
- ✅ Structured priorities in CSV (Scenario A)
- ✅ Onboarding plan + ADR template (Scenario B)
- ✅ Status report ready to send to client (Scenario C)
- ✅ Risk matrix with mitigation plans (Scenario D)

### Step 4: Execute with Confidence

Use the generated output as:
- **For priorities**: Load into your system or tracking system, share with team, measure against metrics
- **For onboarding**: Follow day-by-day plan, use checkpoints to verify ramp-up
- **For status**: Send to client/leadership with no edits (it's already structured)
- **For risks**: Monitor mitigation progress weekly, escalate if probability/impact changes

---

## Design Principles

### Principle 1: Context Over Guessing
**Never generate a strategy without understanding:**
- What problem are we solving?
- What are the hard constraints?
- What does the client really value?
- What could derail this?

The interrogation phase ensures we have rich context before any recommendations.

### Principle 2: Structure Over Narrative
**Always output:**
- Matrices and tables (not paragraphs)
- CSV export (not "here's a summary")
- Checklists (not suggestions)
- Metrics and owners (not vague goals)

Bootcamp intuition: Structure gets rewarded.

### Principle 3: Verification by Default
**Every strategy includes:**
- Why we're recommending it (THINK)
- The specific action (ACT)
- How to verify it's working (OBSERVE + metrics)

ReAct pattern enforces accountability.

### Principle 4: Organizational Awareness
**Always respect:**
- Client decision-making style
- Team capacity and skill gaps
- Portfolio and competing priorities
- Organizational change readiness

This is where interrogation pays dividends.

---

## Example: Complete Workflow

### Scenario: FY26 Priority Building for $2.3M Digital Transformation Project

**You say:**
```
I'm the Delivery Lead on a $2.3M digital transformation project for a financial services client.
I need to create FY26 priorities that align with our quarterly planning and map to ABCD.
The team is 8 people, we're in design phase, and I need to present this to steering next week.
```

**Skill interrogates (Phase 1: Team & Project Context):**
```
Q1: Team composition?
→ "8 people: 1 DL, 1 PM, 4 engineers, 1 QA, 1 analyst. Distributed PST/CST/EST."

Q2: Project budget?
→ "$2.3M total, $180K/month burn, 20% contingency remaining ($460K)."

Q3: Main deliverables?
→ "(1) Data platform foundation, (2) Client portal, (3) Integrations,
   (4) Training, (5) Go-live support. 12-week timeline total."

Q4: Success metrics?
→ "Client cares about: time-to-insight < 2 min, data freshness < 1 hour,
   adoption 80% in 90 days post-launch."

Q5: Delivery methodology?
→ "Agile, 2-week sprints. Daily standups, sprint planning, retros,
   steering every 2 weeks."

Q6: Current phase?
→ "Week 3-4 of 12. Just completed architecture review. All stakeholders approved design."
```

**Skill interrogates (Phase 2: Client & Stakeholder Dynamics):**
```
Q7: Stakeholder map?
→ "Executive sponsor (SVP Finance), two program managers, three power users
   from operations, one IT director. Sponsor is data-driven, PMs are collaborative,
   power users are skeptical about change."

Q8: Relationship health?
→ "Good. Sponsor is engaged, PMs are responsive. Power users are worried about
   adoption but participating actively."

Q9: Client technical resources?
→ "They have 1 dedicated technical person for reviews + integration testing.
   OK but not deep."

Q10: Change management readiness?
→ "Medium. They've done one prior digital transformation (3 years ago, was painful).
   Training budget approved. Need champions in each department."
```

**Skill interrogates (Phase 3: Risk & Dependencies):**
```
Q11: Top risks?
→ "(1) Their legacy system has data quality issues we're discovering late
   (Q2 risk). (2) One critical engineer might leave in Q2 (personal situation).
   (3) Adoption risk if training isn't top-notch."

Q12: Dependencies?
→ "Waiting on their data team for schema finalization (should be 2 weeks).
   We handle everything else. No other workstreams blocking us."

Q13: Escalation paths?
→ "Steering committee every 2 weeks. Sponsor makes final calls.
   Any schedule impact needs sponsor approval."

Q14: Resource constraints?
→ "We're not constrained (staffed fully for this phase). Client is the constraint.
   Their power users will be busy with quarterly closing in late Feb."
```

**Skill interrogates (Phase 4: Organizational Context):**
```
Q15: Portfolio context?
→ "This is one of 3 concurrent projects for our practice. Others are not dependent.
   This is the flagship project for the client relationship."

Q16: Org readiness for change?
→ "They've announced the initiative but haven't trained people yet.
   We're responsible for training in Phase 3. Change management is light."

Q17: What should we know?
→ "The previous transformation failed on adoption. This client doesn't trust new systems.
   User acceptance is the real risk, not technical delivery."
```

**Skill generates: FY26 Priorities CSV**

```csv
Priority,Action,Behavior,Context,Delivered,Owner,Timeline,Metrics,Notes
"Q1 Foundation: Data Platform Build","Engineer data ingestion pipeline, core analytics, reporting APIs","Code reviewed to team standards, 95% test coverage, all architecture ADRs documented, client schema finalized and validated","Unblocks all downstream work. Client has painful manual processes today. This is the 'why' for the project.","Production-ready data pipeline, ingesting 3 source systems, 50+ reports available","[Tech Lead]","Jan-Feb (9 weeks remaining)","Pipeline latency < 15min, data freshness < 1h, zero failed ingests over 2 weeks","Depends on client data team schema work. Schedule risk if slips. Mitigation: our team building interim schema."
"Q1 Foundation: Client Portal MVP","Build self-service client dashboard with role-based views, export capability, real-time KPI dashboards","Full end-to-end tested, accessibility compliant, 2 rounds of user feedback integrated, training materials drafted","Client power users will use this daily. Adoption depends on UX quality. This is proof-of-concept for the broader change.","Live portal with 5 core reports, 3 user roles, < 2s load time, 95% uptime","[PM + 2 eng]","Jan-Feb","Page load < 2s, adoption 40% by Feb 28, NPS > 7 from power user testing","Need user feedback loop starting week 4. Risk: poor UX adoption if not tested with real users early."
"Q1-Q2 Integration: Legacy System Connectors","Build adapters for 3 critical legacy systems, handle ETL complexity, document data mappings","All adapters unit tested, integration tested with production-like data, data reconciliation manual spot-checks 100% passed, runbooks written","Client has painful manual exports today. Automating these saves 200 hours/month. Quick wins build momentum.","All 3 adapters live and validated, automating 4 manual processes","[Data eng]","Feb-Mar (5 weeks)","Zero manual data entry errors, 200+ hours/month automation, audit trail complete","Data quality issues emerging (legacy system has ~10% bad records). Mitigation: data cleansing ADR and strategy by week 5."
"Q2 Adoption: Training Program & Change Management","Develop train-the-trainer program, facilitate dept-specific training, identify and empower champions in each area","Train-the-trainer pilot with 3 power users, training materials > 90% positive feedback, at least 1 champion per department trained and ready","The previous transformation failed on adoption. This is existential risk. Real focus here. Need user buy-in.","100% of target users trained, 3+ champions active per department, readiness assessment passed","[PM + 2 trainers]","Feb-Mar (launching Mar 1)","Training completion 90%, champion engagement > 80%, user readiness survey >= 7/10","Schedule: can't start until portal is stable (end of Feb). Mitigation: dry-run materials now with team."
"Q3 Delivery: Go-Live & Post-Launch Support","Orchestrate cutover, monitor production launch for 30 days, handle day-1 issues, measure business impact","All runbooks tested in staging, incidents < 2h resolution, support team briefed and on standby, success metrics dashboard live","This is the finish line. Quality here determines relationship health. Need flawless execution.","Live system, 90%+ adoption in 30 days, business metrics improving (time-to-insight target met)","[DL + full team]","Mar (launches week 12)","Uptime 99.9%, incident resolution < 2h, NPS post-launch >= 8, adoption 80% by week 4","Risk: if training didn't land, adoption will be low. Mitigation: have support team ready with 24/7 coverage week 1."
```

**Skill generates: Strategic Context for Steering**

```
## FY26 Narrative for Steering Committee

### Program Health
🟢 **GREEN** — On track for Q1 foundation, Q2 adoption, Q3 launch.

### Why These Priorities?
**Sequencing is critical:**
1. **Q1 Foundation** (8 weeks): Build platform + portal. This is the hardest technical work. Must finish before clients use it.
2. **Q2 Adoption** (4 weeks): Train, empower champions, build trust. This is the real risk. Previous transform failed here.
3. **Q3 Launch** (4 weeks): Go-live with full team support. Measure impact.

### Biggest Risks & Mitigations
| Risk | Mitigation | Owner |
|------|-----------|-------|
| Data quality issues in legacy system | Data cleansing strategy by Feb, staged ingestion | Tech lead |
| Key engineer departure in Q2 | Document critical knowledge now, hire contractor backup | DL |
| Adoption fails (like last time) | Invest heavily in training + champions, measure readiness | PM |
| Client power users not engaged | Early UX testing with real users, feedback loop | PM |

### What We Need From Client
- [ ] Data team schema finalization (by Feb 1)
- [ ] 1 dedicated technical resource for integration testing
- [ ] Commitment to 3+ champions per department for training
- [ ] Go-live cutover plan approval by Mar 15
```

**Skill generates: Verification Checklist**

```markdown
## FY26 Execution Checklist

### Q1 Foundation (Weeks 1-8)
- [ ] Architecture approved by steering (done)
- [ ] Data pipeline ingesting all 3 sources
- [ ] Portal MVP live with 5 core reports
- [ ] User feedback collected and integrated
- [ ] Training materials drafted and ready
- [ ] Integration roadmap for 3 legacy systems finalized

### Q2 Adoption (Weeks 9-12)
- [ ] Train-the-trainer pilot with power users
- [ ] Department-specific training sessions scheduled
- [ ] Champions identified and briefed
- [ ] Readiness survey shows >= 7/10
- [ ] Legacy system integrations live and tested

### Q3 Launch (Weeks 13-16)
- [ ] Go-live cutover plan approved
- [ ] Support team on standby (24/7)
- [ ] Business metrics dashboard live
- [ ] Day-1 incidents resolved < 2 hours
- [ ] Post-launch NPS >= 8

### Health Metrics to Track Weekly
- [ ] Story velocity on track
- [ ] Defect backlog < 20
- [ ] Client satisfaction (steering feedback)
- [ ] Team capacity (no burnout)
- [ ] Risk register (top 5 risks monitored)
```

---

## Advanced Usage: Combining with Bootcamp Patterns

### Using with Spec-Driven Development
Create specs for each priority before implementation:
```
Scenario A → CSV priorities
+ Spec-driven dev → One-page spec per priority
+ ReAct planning → Implementation phases with THINK/ACT/OBSERVE
```

### Using with Persona Patterns
Different roles, different perspectives:
```
Career Coach Persona: "Here's how this builds your career narrative"
Delivery Expert Persona: "Here's how to execute flawlessly"
Client Advocate Persona: "Here's why this matters to the business"
```

### Using with Few-Shot Learning
Learn from past projects:
```
Previous project: $1.8M, 10 weeks, 95% on-time
This project: $2.3M, 12 weeks, similar team size
Pattern: Adoption was bottleneck last time
Recommendation: Front-load Q2 adoption work
```

---

## When to Use This Skill vs. Email/Meetings

| Task | Use Email/Meetings | Use Skill |
|------|-------------------|-----------|
| Update team on daily status | ✅ Standup | ❌ Overkill |
| Quick schedule change | ✅ Slack | ❌ Overkill |
| **Build FY26 priorities** | ❌ Messy | ✅ **This skill** |
| **Assess delivery risks systematically** | ❌ Missed items | ✅ **This skill** |
| **Create status report for steering** | ❌ Takes 2 hours | ✅ **This skill** |
| **Onboard new team member** | ❌ Inconsistent | ✅ **This skill** |
| **Build team knowledge base** | ❌ Nobody maintains it | ✅ **This skill** |
| **Present client situation analysis** | ❌ Just your gut | ✅ **This skill** |

---

## Bootcamp Integration

### For Facilitators
Use this skill in **Session 3: Delivery Patterns** when discussing:
- ReAct pattern for delivery decisions
- Real-world delivery scenarios
- Systematic problem-solving for leadership

### For Participants (Role-Fork Exercise)
**Use this skill when:**
- You're the "Delivery Lead" in a role-fork scenario
- You need to create priorities or status reports
- You're building team knowledge or onboarding people
- You're systematically assessing risks

**Expected outcome:**
- Understand how structured interrogation builds strategic context
- See ReAct pattern in action with delivery decisions
- Generate production-ready priorities/reports that impress stakeholders

---

## FAQ

**Q: Will this skill make all my delivery decisions for me?**
A: No. It structures your thinking and generates output. You make the final calls based on organizational context it can't know.

**Q: What if I'm not sure about the answers to interrogation questions?**
A: That's useful signal! It means you need to gather that context. The skill will help you identify what you're missing.

**Q: How is this different from just asking an LLM for advice?**
A: The interrogation phase ensures the recommendations fit YOUR project, client, and team — not a generic best practice that doesn't apply.

**Q: Can I use this for different delivery methodologies?**
A: Yes. Tell the skill your methodology (Agile, waterfall, hybrid, Scrum, Kanban, etc.) in Phase 1, and it adapts.

**Q: What if my client doesn't fit the patterns in this skill?**
A: Tell it during interrogation: "Our client makes decisions by consensus, very slow." It will adjust the risk assessment and recommendations.

**Q: I don't have time for a full interrogation. Can we skip questions?**
A: You could, but interrogation is where the value happens. Even 5 minutes answering key questions beats 30 minutes guessing.

**Q: Can I use this for a subcontractor or partner delivery?**
A: Yes. The framework applies to any delivery context. Just adjust the stakeholder map in Phase 2 interrogation.

---

## Real Example Outputs

### Output 1: FY26 Priorities CSV (Ready to Load into your system)
```
Priority,Action,Behavior,Context,Delivered,Owner,Timeline,Metrics
"Platform Foundation","Engineer core data pipeline","95% test coverage, architecture reviewed, client schema approved","Unblocks Q2 work, client has painful manual processes","Production-ready ingestion for 3 systems","[Tech Lead]","Jan-Feb","Latency <15min, uptime 99.9%"
```

### Output 2: Risk Matrix (Ready to Share with Steering)
```
| Risk | Probability | Impact | Mitigation | Owner | Status |
|------|-------------|--------|-----------|-------|--------|
| Data quality issues | High | High | Cleansing strategy by Feb 1 | [Name] | In progress |
| Key engineer leaves | Medium | High | Document knowledge, hire backup | [Name] | Monitoring |
| Adoption fails | Medium | Critical | Champions + training focus | [PM] | Active |
```

### Output 3: Status Report (Ready to Send to Client)
```
## Weekly Status Report
**Project**: Digital Transformation
**Overall Status**: 🟢 GREEN
**Milestone Progress**: [Table showing on-time delivery]
**Escalations**: [List of items needing client action]
**Next Week**: [Specific, actionable plan]
```

---

## References

- **ReAct Pattern**: Yao et al. (2022) "ReAct: Synergizing Reasoning and Acting in Language Models"
- **Persona Pattern**: White et al. (2023) "A Prompt Pattern Catalog to Enhance Prompt Engineering"
- **Few-shot Learning**: Brown et al. (2020) "Language Models are Few-Shot Learners"
- **Delivery Leadership**: Schwaber & Sutherland (2020) "Scrum: The Art of Doing Twice the Work in Half the Time"
- **Risk Management**: PMBOK Guide (2021) Project Management Institute

---

**Version**: 1.0
**Last Updated**: 2026-03-18
**For**: Joey's Prompt Engineering Bootcamp v2 — Delivery Lead Track
