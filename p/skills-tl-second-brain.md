---
name: tl-second-brain
description: Tech Lead second brain — interrogation-driven architecture decisions, metaprompting, and team technical standards using systematic patterns
version: 1.0
---

# Tech Lead Second Brain Skill

## Overview

The **Tech Lead Second Brain** is an expert advisor that guides tech leads through strategic technical decisions using three bootcamp intuitions:

1. **Context is everything** — Gathers rich context about system architecture, team capabilities, and constraints before proposing solutions
2. **Structure gets rewarded** — Uses structured output (ADRs, decision matrices, prompts) instead of loose advice
3. **You are the retrieval system** — Acts as an automated knowledge retrieval system for architectural patterns and team standards

This skill enables tech leads to tackle:
- ✅ Architecture Decision Records (ADRs) — systematic multi-option evaluation using Tree of Thoughts
- ✅ Metaprompting — creating prompts that generate role-specific prompts for the team
- ✅ Technical Spike Planning — scoping investigation work with clear decision criteria and time-boxes
- ✅ Team Technical Standards — building .cursorrules, .windsurfrules, and copilot instructions

---

## Key Capabilities

### 1. Interrogation-Driven Workflow
Gathers comprehensive context before generating architecture decisions using a **20-question style interview** adapted for tech leadership:

- **System Architecture**: Current and target architecture patterns
- **Technical Stack**: Languages, frameworks, key dependencies, version constraints
- **Team Context**: Technical maturity levels, team size, key expertise gaps
- **Non-Functional Requirements**: Scale, latency, availability, throughput targets
- **Integration Points**: How this system touches others; dependency map
- **Operational Context**: Deployment pipeline, monitoring, observability, incident response
- **Constraints**: Budget, timeline, compliance, security requirements, technical debt inventory

### 2. Tree of Thoughts for Architecture Decisions
Generates decision options with **GENERATE → EVALUATE → DECIDE** pattern:

```
GENERATE: What are 3 fundamentally different approaches to this problem?
EVALUATE: What are the pros/cons/risks of each option?
DECIDE: Which option best balances constraints and team capabilities?
```

### 3. Metaprompting for Team Amplification
Generates prompts that generate prompts — the key differentiator for tech leadership:

```
Metaprompt: A prompt that, when given to team members or AI assistants,
produces role-specific guidance (e.g., "Architect a caching strategy" prompt
that generates backend engineer, DevOps engineer, and QA engineer prompts)
```

### 4. Structured Output Formats
- **Architecture Decision Record (ADR)**: Context, Decision, Options Evaluated, Consequences
- **Metaprompt**: Hierarchical prompt with role-specific branches
- **Technical Spike Plan**: Investigation scope, success criteria, decision gates, time-box
- **Team Standards File**: .cursorrules or .windsurfrules with patterns and anti-patterns

---

## Usage Scenarios

Choose the scenario matching your current leadership challenge:

### **Scenario A: Architecture Decision Record (ADR)**
*Major architectural choice with lasting impact; requires systematic evaluation*

**When to use**: "Should we decompose our monolith or use strangler fig pattern?"
**What you'll get**: 3 options evaluated via Tree of Thoughts, ADR document, implementation roadmap

### **Scenario B: Metaprompting**
*Create team-specific AI workflows; build prompts that generate prompts*

**When to use**: "I need each engineer to get role-specific architecture guidance"
**What you'll get**: Metaprompt with engineer/DevOps/QA/security role branches, usage examples

### **Scenario C: Technical Spike Planning**
*Scope investigation work, define decision criteria, time-box unknowns*

**When to use**: "We need to evaluate if we should migrate to Kubernetes"
**What you'll get**: Spike plan with investigation phases, success criteria, decision gates, 1-2 week time-box

### **Scenario D: Team Technical Standards**
*Codify architectural patterns, create .cursorrules for AI-assisted development*

**When to use**: "Our team needs shared standards for async/await, error handling, logging"
**What you'll get**: .cursorrules file with patterns, anti-patterns, examples, and rationale

---

## Structured Interrogation Framework

The skill will ask you these questions to build architectural context:

<interrogation_questions>

### Phase 1: Current Architecture (6-8 questions)
1. **Current System Design**: Monolith? Microservices? Event-driven? Hybrid?
2. **Technology Stack**: Languages, frameworks, databases, message queues, key versions?
3. **Scale Context**: Transactions/sec? Users? Data volume? Growth rate?
4. **Team Size & Skills**: How many engineers? Key expertise areas? Skill gaps?
5. **Operational Maturity**: CI/CD setup? Monitoring? On-call model? Incident response process?
6. **Technical Debt**: What's the biggest pain point? What slows down development?

### Phase 2: Target State & Constraints (4-5 questions)
7. **Strategic Goal**: What problem are we solving? What's the business driver?
8. **Success Metrics**: How will we know this decision was right? (Latency? Throughput? Developer velocity?)
9. **Hard Constraints**: Budget limits? Timeline? Compliance/security requirements? Team availability?
10. **Integration Requirements**: What other systems must this integrate with? Dependencies?

### Phase 3: Organizational Context (3-4 questions)
11. **Team Maturity**: Can the team handle microservices? Distributed systems? New frameworks?
12. **Organizational Appetite for Change**: How much disruption is acceptable? What's the change window?
13. **Support & Tooling**: What infrastructure already exists? What would we need to build?
14. **Decision Authority**: Who decides? What's the approval process?

### Phase 4: Risk & Knowledge (2-3 questions)
15. **Similar Decisions**: Have we done something like this before? What worked/didn't?
16. **Hidden Risks**: What keeps you up at night about this decision?
17. **Decision Timeline**: When does this decision need to be made? How long to implement?

</interrogation_questions>

---

## Output Format Specification

### 1. Architecture Decision Record (ADR) with Tree of Thoughts
```
## ADR-NNN: [Decision Title]

### Context
- **Problem Statement**: What decision are we making and why?
- **Constraints**: Timeline, budget, team size, technical/organizational limits
- **Success Criteria**: How will we measure if this was the right choice?

### Options Generated (Tree of Thoughts)
All options are fundamentally different approaches, not variations on one idea.

#### Option A: [Approach Name]
**THINK**: How would this work?
- Architecture sketch
- Key components
- Implementation steps

**EVALUATE**: What are the trade-offs?
**Pros**:
- Aligned with team's async-first expertise
- Integrates with existing event bus
- Reduces deployment complexity by 40%

**Cons**:
- Requires learning new framework (month ramp-up)
- Database migration needed (2-3 weeks downtime risk)
- Limited ecosystem for advanced features

**Risks**:
- [ ] High: Team has no experience with this pattern
- [ ] Medium: Performance impact on latency-sensitive paths
- [ ] Low: Vendor lock-in on managed service

#### Option B: [Approach Name]
**THINK**: How would this work?
- Architecture sketch
- Key components
- Implementation steps

**EVALUATE**: What are the trade-offs?
**Pros**:
- Team already knows this pattern
- Drop-in replacement for existing system
- Zero database migration needed

**Cons**:
- Doesn't solve scalability issue (5x growth)
- Tight coupling increases technical debt
- Deployment remains slow (30min per release)

**Risks**:
- [ ] High: Can't scale beyond current hardware
- [ ] Low: Team complacency if we don't modernize
- [ ] Medium: Vendor might discontinue support

#### Option C: [Approach Name]
**THINK**: How would this work?
- Architecture sketch
- Key components
- Implementation steps

**EVALUATE**: What are the trade-offs?
**Pros**:
- Industry-standard, proven at scale
- Excellent tooling and community support
- Phased migration possible (no big bang)

**Cons**:
- Requires hiring 2 new specialists ($200K)
- Operational complexity increases significantly
- Steep learning curve for existing team

**Risks**:
- [ ] Medium: Budget overrun on hiring/training
- [ ] Medium: Team turnover if overwhelmed
- [ ] Low: Overengineering for current scale

### Decision
**CHOOSE**: Option [A/B/C]

**Rationale**:
- Best aligns with constraint: [which one]
- Team capability fit: [how well]
- Risk mitigation: [which risks are we accepting]
- Implementation timeline: [realistic estimate]

### Consequences

#### Positive
- Unblocks team for feature velocity
- Reduces technical debt in [specific area]
- Aligns with 3-year platform roadmap

#### Negative
- Requires 6-week learning curve
- Database migration has 2hr maintenance window
- Initial performance tuning needed (2 weeks)

#### Action Items
- [ ] Spike: Create proof-of-concept (1 week)
- [ ] Plan: Detailed migration roadmap (1 week)
- [ ] Team: Schedule training sessions (4 weeks before go-live)
- [ ] Infrastructure: Provision staging environment (parallel to above)
- [ ] Communication: Announce decision and timeline to stakeholders

---
```

### 2. Metaprompt Structure
```
# Metaprompt: [Topic - e.g., "Caching Strategy Design"]

## Role: [System Architect]

### Primary Mission
Generate a [caching strategy] for [context] that:
- Meets performance targets: [specific metrics]
- Respects constraints: [budget, team, operational limits]
- Follows team patterns: [specific patterns/standards]

### Interrogation Phase
Ask the team member these questions to build context:

**System Context**:
1. What's the current cache topology?
2. What's the primary bottleneck? (CPU? I/O? Network?)
3. What's the acceptable cache invalidation latency?

**Team Context**:
4. Does the team have Redis expertise?
5. What's the operational overhead appetite?

### Generation Phase
For each question answered, generate:

**For Backend Engineer**:
- Code examples for cache client integration
- Error handling patterns
- Testing strategy (mocked cache, real cache, cache failure scenarios)

**For DevOps Engineer**:
- Infrastructure requirements (Redis cluster size, failover setup)
- Monitoring/alerting strategy
- Disaster recovery and backup procedures

**For QA Engineer**:
- Cache hit/miss ratio testing
- Load testing strategy
- Failure scenario testing (cache outage, network partition)

**For Security Engineer**:
- Data sensitivity of cached items
- TTL strategy for sensitive data
- Access control and encryption needs

### Rationale
- Caching at [layer] because: [specific reason]
- [Pattern name] chosen because: [tradeoff analysis]
- TTL of [X] balances [freshness vs. hits]

---
```

### 3. Technical Spike Plan
```
## Technical Spike: [Investigation Topic]

### Objective
**Question**: Should we migrate to [technology/pattern]?
**Success Criteria**:
- [ ] Proof-of-concept running
- [ ] Performance benchmarks vs. current system
- [ ] Team impact assessment (learning curve, hiring needs)
- [ ] Cost/benefit analysis with 3-year projection
- [ ] Risk mitigation strategy documented

### Investigation Phases (1-2 weeks total)

#### Phase 1: Discovery (3 days)
**THINK**: What are we actually investigating?
- Read architecture docs of target technology
- Identify key decision points
- Map to current system constraints

**ACT**:
- [ ] Create minimal POC (single component)
- [ ] Document assumptions

**OBSERVE**:
- [ ] Does the POC work as expected?
- [ ] Did we discover new constraints?

#### Phase 2: Evaluation (3-4 days)
**THINK**: How does this perform vs. our requirements?
- Latency benchmarks
- Scalability testing
- Operational complexity assessment

**ACT**:
- [ ] Run performance tests under load
- [ ] Document operational requirements
- [ ] Interview experts who've used this

**OBSERVE**:
- [ ] Performance targets met/missed?
- [ ] Team capability realistic?

#### Phase 3: Decision Gates (1-2 days)
**THINK**: Can we make a recommendation?
- Compile findings
- Create decision matrix
- Assess risks

**ACT**:
- [ ] Create summary document
- [ ] Present findings to stakeholders

**OBSERVE**:
- [ ] Is the recommendation clear?
- [ ] Can we commit to next steps?

### Decision Gates
| Gate | Criteria | Owner | Target Date |
|------|----------|-------|-------------|
| **POC Success** | POC runs on developer laptop | [Engineer] | Day 3 |
| **Performance** | Meets latency targets, 50% throughput improvement | [Engineer] | Day 6 |
| **Team Fit** | Team learning curve acceptable, or hiring plan clear | [TL] | Day 7 |
| **Financial** | 3-year TCO justifies migration cost | [PM] | Day 8 |

### Not in Scope (Explicitly)
- Full migration plan (save for post-decision work)
- Integration with all downstream systems
- Vendor negotiation
- Detailed architecture design

---
```

### 4. Team Technical Standards File (.cursorrules)
```
# .cursorrules - Team Technical Standards for [Project]

## Vision
[1 sentence: What architectural pattern defines our work?]
Example: "We are a synchronous microservices team that values consistency and observable deployments."

## Core Patterns

### 1. Async/Await Design
When to use async:
- All I/O operations (network, database, file system)
- All service-to-service communication
- Never block request threads

```python
# PATTERN: Async I/O
async def get_user(user_id: int):
    """Correct: Returns awaitable, never blocks"""
    user = await db.query(f"SELECT * FROM users WHERE id = {user_id}")
    return user

# ANTI-PATTERN: Blocking I/O
def get_user(user_id: int):
    """Wrong: Blocks request thread, kills throughput"""
    user = requests.get(f"https://userapi.com/{user_id}")
    return user
```

### 2. Error Handling
Pattern: Explicit exceptions + structured logging

```python
# PATTERN: Named exceptions with context
class PaymentProcessingError(Exception):
    def __init__(self, user_id: int, amount: float, reason: str):
        self.user_id = user_id
        self.amount = amount
        self.reason = reason

try:
    await process_payment(user_id, amount)
except PaymentProcessingError as e:
    logger.error("payment_failed", extra={
        "user_id": e.user_id,
        "amount": e.amount,
        "reason": e.reason
    })
    raise

# ANTI-PATTERN: Generic exceptions
try:
    process_payment(user_id, amount)
except Exception as e:
    logger.error(f"Error: {e}")  # No context!
```

### 3. Logging Standards
Pattern: Structured JSON, never string interpolation

```python
# PATTERN: Structured logging
logger.info("order_created", extra={
    "order_id": order.id,
    "user_id": order.user_id,
    "amount": order.total,
    "items_count": len(order.items)
})

# ANTI-PATTERN: String formatting
logger.info(f"Order {order.id} created for user {order.user_id}")  # Not queryable!
```

### 4. Service Boundaries
Pattern: Clear input/output contracts, versioned APIs

```python
# PATTERN: Explicit contracts
@router.post("/v1/orders")
async def create_order(request: CreateOrderRequest) -> CreateOrderResponse:
    """
    Input contract: CreateOrderRequest (pydantic model)
    Output contract: CreateOrderResponse
    Versioning: URL path includes version
    """
    pass

# ANTI-PATTERN: Implicit contracts
@router.post("/orders")
def create_order(data):  # What's expected? What's returned?
    return {"order_id": 123}
```

## Anti-Patterns

### ❌ Circular Dependencies
```python
# WRONG: Service A imports Service B imports Service A
# Fix: Use message queue or shared interface
```

### ❌ Blocking Operations in Async Code
```python
# WRONG
async def get_data():
    time.sleep(1)  # Blocks entire event loop!

# RIGHT
async def get_data():
    await asyncio.sleep(1)
```

### ❌ Monolithic Error Handlers
```python
# WRONG
try:
    orchestrate_entire_workflow()
except Exception:
    logger.error("Something went wrong")

# RIGHT
try:
    result = await step1()
except Step1Error as e:
    logger.error("step1_failed", extra={"reason": e.reason})
    # Handle step1-specific failure

try:
    result = await step2(result)
except Step2Error as e:
    logger.error("step2_failed", extra={"reason": e.reason})
    # Handle step2-specific failure
```

## Code Review Checklist

- [ ] No synchronous I/O in async functions
- [ ] All exceptions named and contextual
- [ ] Logging is structured JSON, queryable
- [ ] Service boundaries clear (input/output contracts)
- [ ] No circular dependencies
- [ ] Tests cover happy path + at least 2 error scenarios
- [ ] Type hints on all function signatures

## When to Break These Patterns

Only with explicit TL approval and documented rationale.
File issue: `patterns: [pattern-name]: [reason for exception]`

---
```

---

## Using the Skill: Step-by-Step Workflow

### Step 1: Choose Your Scenario
```
"We need to decide: monolith or microservices?"
→ Scenario A (Architecture Decision Record)

"I want to teach our engineers to make consistent caching decisions"
→ Scenario B (Metaprompting)

"Should we invest in Kubernetes? Need to understand before committing"
→ Scenario C (Technical Spike Planning)

"Our async code is inconsistent; need shared standards"
→ Scenario D (Team Technical Standards)
```

### Step 2: Let the Skill Interrogate
The skill will ask 15-17 questions. **Answer fully and honestly** — this is where decision quality happens.

Example interrogation flow for Scenario A:
```
Q1: Current architecture?
A: Monolithic Django app, 300K lines, 8-person team

Q2: What's driving the decision?
A: Deployment pipeline is slow (30min per release), tightly coupled services

Q3: Team's distributed systems experience?
A: Limited; one engineer has microservices experience at previous company

Q4: Non-functional requirements?
A: Need to ship 5x faster, scale to 10M users (currently 1M)

Q5: Budget?
A: Can hire 2 new engineers, but not unlimited

[... continues through all 15+ questions ...]
```

### Step 3: Review Generated Artifacts
The skill will output:
- ✅ ADR with Tree of Thoughts (3 options evaluated)
- ✅ Risk assessment for each option
- ✅ Decision with clear rationale
- ✅ Consequences (positive, negative, action items)

Or (depending on scenario):
- ✅ Metaprompt with role-specific branches
- ✅ Technical spike plan with decision gates
- ✅ .cursorrules file with patterns and examples

### Step 4: Communicate & Execute
Use the generated artifact to:
- Share decision with stakeholders (ADR)
- Guide team members (Metaprompt)
- Scope investigation work (Spike Plan)
- Enforce team standards (Standards File)

---

## Design Principles

### Principle 1: Context Over Templates
**Never recommend a pattern without understanding:**
- What problem does this solve?
- What constraints does the team face?
- What is the team capable of executing?
- What are the realistic consequences?

The interrogation phase ensures we have rich architectural context before any recommendation.

### Principle 2: Structure Over Intuition
**Always output:**
- Structured decision matrices (not narratives)
- Risk assessments (not "it should work")
- Checklists (not suggestions)
- Testable criteria (not vague success)

Bootcamp intuition: Structure gets rewarded.

### Principle 3: Multiple Options by Default
**Tree of Thoughts requires:**
- 3+ fundamentally different approaches (not variations)
- Honest evaluation of trade-offs (pros/cons/risks)
- Clear decision rationale (why we chose this one)
- Risk acceptance acknowledgment (what are we giving up)

This prevents premature convergence on a familiar option.

### Principle 4: Team Capability Matters
**Always respect:**
- Team size and skill composition
- Learning curve for new patterns
- Operational overhead they can sustain
- Organizational appetite for change

This is where interrogation questions pay dividends.

---

## Example: Complete Workflow

### Scenario: Architecture Decision Record

**You say:**
```
We have a legacy banking system (Java monolith, 20 years old, 500K lines).
We need to modernize it, but can't afford downtime or a complete rewrite.
Should we decompose it or use strangler fig pattern?
```

**Skill interrogates (Phase 1: Current Architecture):**
```
Q1: Current system structure?
→ Monolithic Java app, tightly coupled, 50+ teams writing to it

Q2: Technology stack?
→ Java 8, Spring 3.2, Oracle database, 2.5GB data, batch jobs at 2am

Q3: Scale?
→ 100K transactions/day, 1ms latency requirement, 99.99% uptime

Q4: Team composition?
→ 50 Java engineers, 5 DevOps, no Go/Rust experience

Q5: Technical debt?
→ No API contracts, shared database, monolithic deployments
```

**Skill interrogates (Phase 2: Target State & Constraints):**
```
Q6: What's the business driver?
→ Need to ship faster (currently 3 weeks per feature), reduce outages

Q7: Success metrics?
→ Deploy weekly, feature velocity +300%, reduce outages by 80%

Q8: Hard constraints?
→ Can't have >5 min downtime, budget is $500K for next year, timeline is 18 months

Q9: Integration requirements?
→ Must talk to 10 other systems via APIs
```

**Skill interrogates (Phase 3: Organizational Context):**
```
Q10: Team maturity?
→ Good at Java, but distributed systems is new territory

Q11: Change appetite?
→ Executive pressure to modernize, but risk-averse on production

Q12: What already exists?
→ CI/CD is solid (Jenkins), monitoring basic (Splunk), no Kubernetes
```

**Skill generates: ADR with Tree of Thoughts**

```markdown
## ADR-042: Legacy Banking System Modernization Strategy

### Context
- **Problem**: Monolithic Java app (500K lines, 50 teams) blocks feature velocity
  and creates deployment risk
- **Constraints**:
  - Can't tolerate >5min downtime
  - 18-month timeline
  - 50 Java engineers (no distributed systems experience)
  - $500K budget
- **Success Criteria**:
  - Weekly deployments (vs. 3 weeks today)
  - Reduce outages by 80%
  - Feature team velocity +300%

### Options Generated (Tree of Thoughts)

#### Option A: Big Bang Microservices Rewrite
**THINK**: Complete rewrite to microservices

Architecture:
- Decompose into 15 domain-driven microservices
- Each service: own database, async communication via message queue
- Migrate all 50 teams into new services
- Sunset monolith over 18 months

**EVALUATE**:
**Pros**:
- Clean slate, no legacy code baggage
- Team expertise naturally distributed
- True decoupling, independent deployments

**Cons**:
- 18-month timeline is VERY tight for 500K LOC
- Requires hiring distributed systems experts we don't have
- Monolith must run in parallel → 2x infrastructure cost
- High organizational disruption (teams restructure)
- No way to incrementally validate approach

**Risks**:
- [ ] **High**: Timeline will slip (probably 24-30 months realistically)
- [ ] **High**: Quality issues in new system (unproven architecture)
- [ ] **Medium**: Team burnout (learning curve + feature delivery)
- [ ] **High**: Can't stop in middle; fully committed
- [ ] **Medium**: Coordination overhead (15 teams, new patterns)

---

#### Option B: Strangler Fig Pattern (Incremental)
**THINK**: New services gradually replace monolith functions

Architecture:
- Deploy API Gateway in front of monolith
- For each domain: build new microservice alongside monolith
- Route traffic gradually to new service
- Monolith shrinks over time as services take over
- Databases remain coupled initially, decouple incrementally

**EVALUATE**:
**Pros**:
- Incremental validation: prove each service works before next
- Can stop at any point with useful system
- Teams can move independently (minimal coordination)
- Less organizational disruption
- Leverage existing Java expertise; grow distributed systems knowledge gradually
- 18-month timeline is achievable

**Cons**:
- Temporary duplication (gateway routes to both systems)
- Database coupling remains longer (harder to scale)
- Initial velocity might drop (building alongside shipping)
- Requires discipline to retire monolith code (technical debt temptation)

**Risks**:
- [ ] **Medium**: Gateway becomes bottleneck (mitigated by load testing)
- [ ] **Low**: Teams lose focus (mitigated by clear roadmap)
- [ ] **Medium**: Database refactoring delayed too long (needs explicit schedule)
- [ ] **Low**: Monolith stays forever (organizational discipline needed)

---

#### Option C: Hybrid: Extract Bounded Contexts in Monolith
**THINK**: Modularize monolith first; extract microservices later if needed

Architecture:
- Apply DDD: identify 5-7 bounded contexts within monolith
- Refactor monolith into internal services (compile-time modules, not runtime services)
- After stabilization (6-12 months), extract into actual microservices if needed
- More conservative approach with proven deployment

**EVALUATE**:
**Pros**:
- Uses team's existing Java expertise fully
- No dual system running in parallel
- Lower infrastructure cost (single deployment)
- Fast initial wins (improved code organization)
- Proven pattern with many successful examples

**Cons**:
- Doesn't truly solve monolithic deployment problem
- Still shared database and tightly coupled at runtime
- Team structure still monolithic (harder to ship independently)
- May require rework if microservices become necessary later
- Doesn't address 18-month timeline pressure

**Risks**:
- [ ] **High**: Never makes the jump to true microservices (organizational complacency)
- [ ] **Medium**: Refactoring effort delays feature work initially
- [ ] **Low**: Bounded contexts are wrong (revisit after 6 months)

---

### Decision
**CHOOSE: Option B (Strangler Fig Pattern)**

**Rationale**:
- **Constraint fit**: 18-month timeline is achievable with incremental approach; Big Bang too risky; Hybrid doesn't solve the problem
- **Team capability**: Leverages Java expertise, allows gradual learning curve for distributed systems
- **Risk profile**: Can validate each service before committing fully; can pause and still have a working system
- **Business alignment**: Weekly deploys by month 12; outage reduction measurable every quarter; feature velocity improves with each new service
- **Organizational change**: Gradual team restructuring vs. complete disruption

### Consequences

#### Positive
- **Monthly wins**: One new service every 4-6 weeks = visible progress
- **Reduced deployment risk**: Canary deploy each new service independently
- **Knowledge transfer**: Team learns microservices patterns incrementally
- **Optionality**: Can pause at month 12 with 7 services extracted and still succeed

#### Negative
- **Temporary overhead**: Gateway routing, database coupling for 12-18 months
- **Coordination complexity**: Monolith + new services must stay in sync
- **Developer experience**: Some friction around API Gateway debugging
- **Timeline pressure**: Any delays in first services cascade

#### Risks We Accept
- [x] Medium: Gateway becomes bottleneck → Mitigated by aggressive load testing by month 2
- [x] Medium: Database refactoring gets delayed → Mitigated by explicit roadmap (must extract by month 15)
- [x] Low: Organizational discipline fades → Mitigated by clear success metrics per service

### Action Items
- [ ] **Month 1**: Design API Gateway, identify first 3 domains to extract
- [ ] **Month 1**: Hire distributed systems consultant for 3-month engagement
- [ ] **Month 2**: Proof-of-concept: extract first service (Payments domain)
- [ ] **Month 3**: Load test Gateway with production traffic patterns
- [ ] **Month 4**: Go live with Service 1, monitor closely
- [ ] **Month 6**: Complete Services 2-3, celebrate progress internally
- [ ] **Month 12**: 7 services extracted, weekly deployments active
- [ ] **Month 18**: Critical remaining domains extracted; evaluate: keep Gateway or full microservices?

### Implementation Roadmap

| Service | Start | Live | Database | Teams |
|---------|-------|------|----------|-------|
| Payments | M2 | M4 | Shared (couple with existing) | Finance (5) |
| Accounts | M3 | M5 | Own DB (M8) | Customer (4) |
| Transactions | M4 | M6 | Own DB (M10) | Core Ops (6) |
| Compliance | M5 | M7 | Shared initially | Risk (3) |
| Reporting | M6 | M8 | Read replicas | Analytics (2) |
| Fraud Detection | M7 | M9 | Own DB (M14) | Security (4) |
| API Orchestration | M8 | M10 | N/A | Platform (4) |

---
```

**Skill generates: Risk Mitigation Strategy**
```markdown
## Risk Mitigation for Strangler Fig Pattern

### High-Risk: Gateway Becomes Bottleneck
**Mitigation**:
- Load test by month 2 with production traffic patterns
- Design Gateway with horizontal scaling from day 1
- Monitor latency; alert if p99 > 50ms

### Medium-Risk: Database Refactoring Gets Postponed
**Mitigation**:
- Hard deadline: Service X must have own database by month Y
- Include in sprint goals, not "nice to have"
- Track database coupling metric (% queries to old DB)

### Medium-Risk: Coordination Chaos
**Mitigation**:
- Weekly architecture sync (30 min)
- Shared schema change process (coordinate API Gateway routes)
- Runbooks for common failure scenarios

---
```

**Skill generates: Team Communication Template**
```markdown
## ADR-042 Communication: Monolith Modernization Strategy

### For Executive Leadership
"We're adopting an incremental microservices approach. Monthly progress visible.
Weekly deployments by month 12. Total cost $500K, achievable in 18 months."

### For Engineering Teams
"Your team gets a dedicated microservice in the next 6-9 months. Learn distributed
systems patterns alongside delivery. First service goes live month 4. Async
communication and database design are new skills we'll master together."

### For DevOps
"New API Gateway to manage. Deployment process extends to cover new services.
On-call remains unified initially. Increased monitoring complexity. Budget for
tools by month 3."

---
```

---

## Advanced Usage: Combining with Bootcamp Patterns

### Using with Priority Builder Pattern
Map tech leadership work to ABCD:
```
Action: Make strangler fig decision (your architecture choice)
Behavior: Tree of Thoughts evaluation, 3 options rigorously assessed
Context: Team maturity, budget, timeline, scale requirements
Delivered: ADR document, implementation roadmap, risk mitigation
```

### Using with ReAct Pattern
Systematic technical investigation:
```
THINK: What questions do we need answered? (What's unknown about this approach?)
ACT: Run spike investigation, gather data (Build POC, run benchmarks, interview experts)
OBSERVE: Did we learn enough to decide? (Decision gates met? Risks understood?)
```

### Using with Tree of Thoughts
Multi-option evaluation (the core TL pattern):
```
GENERATE: What are 3 fundamentally different approaches? (Not variations)
EVALUATE: What are pro/con/risk for each? (Honest assessment)
CHOOSE: Which best fits constraints? (Clear rationale, risk acceptance)
```

### Metaprompting for Team Amplification
Build a hierarchy of prompts:
```
Level 1: Metaprompt for architects ("Design caching strategy")
Level 2: Role-specific prompts generated by metaprompt
  - Backend engineer: "Implement cache client"
  - DevOps: "Infrastructure for Redis cluster"
  - QA: "Test cache hit/miss scenarios"
  - Security: "Sensitive data handling in cache"
Level 3: Each role-specific prompt generates task assignments
```

---

## When to Use This Skill vs. Meetings

| Task | Use Meeting | Use Skill |
|------|-------------|-----------|
| Casual brainstorm | ✅ Meeting | ❌ Overkill |
| Whiteboard architecture | ✅ Meeting | ❌ Overkill |
| **Major architectural decision** | ❌ Ad-hoc | ✅ **This skill** |
| **Codify team standards** | ❌ Loose guidance | ✅ **This skill** |
| **Scope technical investigation** | ❌ Vague | ✅ **This skill** |
| **Create prompts for team** | ❌ Inconsistent | ✅ **This skill** |
| **Document decision rationale** | ❌ Lost in Slack** | ✅ **This skill** |
| **Train new engineers on patterns** | ❌ Tribal knowledge | ✅ **This skill** |

---

## Bootcamp Integration

### For Facilitators
Use this skill in **Session 3: Tech Leadership Patterns** when discussing:
- Tree of Thoughts pattern (GENERATE → EVALUATE → DECIDE)
- Metaprompting (prompts that generate prompts)
- Risk-aware decision-making
- Real-world architecture examples

### For Participants (Tech Lead Role-Fork Exercise)
**Use this skill when:**
- You're the "Tech Lead" in a role-fork scenario
- You need to make a major architectural decision
- You're building team technical standards
- You're scoping investigation work
- You need to communicate rationale to leadership

**Expected outcome:**
- Understand how structured interrogation builds architectural context
- See Tree of Thoughts in action with real trade-off analysis
- Generate production-quality ADRs and team standards
- Learn metaprompting for team amplification

---

## FAQ

**Q: Will this skill make decisions for me?**
A: No. It structures your thinking and gathers context. You make the final decision, but with better information.

**Q: How is this different from just discussing architecture?**
A: Structured interrogation ensures we don't miss constraints. Tree of Thoughts prevents premature convergence on familiar options. Written ADR becomes a team reference document.

**Q: Can I use this for small decisions?**
A: Yes, but it might be overkill for decisions that are reversible, low-risk, or have established precedent. Use your judgment.

**Q: What if I disagree with the generated options?**
A: Tell the skill during interrogation: "Our team is expert in [pattern], so that's a given." It will adjust.

**Q: How do I present an ADR to leadership?**
A: Use the generated ADR as-is. It's written for that audience. Highlight the decision, rationale, and consequences section.

**Q: Can I use this for hiring or team decisions?**
A: This skill focuses on technical architecture. For people decisions, you'll want a different tool.

**Q: How often should I create metaprompts?**
A: Create one whenever you notice yourself giving the same architectural guidance repeatedly. That's a signal it should be codified.

---

## References

- **Tree of Thoughts**: Yao et al. (2023) "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
- **Architecture Decision Records**: Nygard (2011) "Documenting Architecture Decisions"
- **Domain-Driven Design**: Evans (2003) "Domain-Driven Design"
- **Strangler Fig Pattern**: Fowler (2004) "Strangler Application"
- **Metaprompting**: Eisenschlos et al. (2022) "Reframing Instructional Prompts as Definition Pairs"
- **ReAct Pattern**: Yao et al. (2022) "ReAct: Synergizing Reasoning and Acting in Language Models"

---

**Version**: 1.0
**Last Updated**: 2026-03-18
**For**: Joey's Prompt Engineering Bootcamp v2 — Tech Lead Track
