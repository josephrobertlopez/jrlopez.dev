---
name: dev-second-brain
description: Developer second brain — interrogation-driven code assistance using systematic patterns (ReAct, spec-kit)
version: 1.0
---

# Developer Second Brain Skill

## Overview

The **Developer Second Brain** is an expert assistant that guides developers through complex code challenges using three bootcamp intuitions:

1. **Context is everything** — Gathers rich context about your codebase before suggesting changes
2. **Structure gets rewarded** — Uses structured output (plans, diffs, tests) instead of loose prose
3. **You are the retrieval system** — Acts as an automated knowledge retrieval system for your codebase and team conventions

This skill enables developers to tackle:
- ✅ Code migrations (framework upgrades, language version bumps)
- ✅ Refactoring (extract service, decompose monolith)  
- ✅ New feature implementation with existing conventions
- ✅ Systematic debugging approaches

---

## Key Capabilities

### 1. Interrogation-Driven Workflow
Gathers structured context before generating code using a **20-question style interview** adapted for developers:

- **Codebase Context**: Framework, language version, architecture pattern
- **Target State**: Migration target, acceptance criteria, success metrics
- **Dependencies**: External libraries, team integrations, data pipelines
- **Test Coverage**: Existing test patterns, testing conventions
- **Team Conventions**: Naming, error handling, logging standards

### 2. ReAct Pattern Implementation
Generates migration plans with **THINK → ACT → OBSERVE** annotations:

```
THINK: What's the constraint here? (Analysis phase)
ACT: Here's the code change (Implementation)
OBSERVE: How do we verify? (Testing/validation)
```

### 3. Structured Output Formats
- **Implementation Plan**: Step-by-step with ReAct annotations
- **Code Diffs**: Side-by-side before/after with reasoning
- **Test Strategy**: Unit, integration, regression test cases
- **Checklist**: Verification steps before merge

---

## Usage Scenarios

Choose the scenario matching your current task:

### **Scenario A: Code Migration**
*Framework upgrade, language version bump, major dependency migration*

**When to use**: "I need to migrate from Framework A to B"  
**What you'll get**: Migration plan, code diffs, test strategy, rollback plan

### **Scenario B: Refactoring**  
*Extract service, decompose monolith, improve testability*

**When to use**: "I need to refactor this component"  
**What you'll get**: Refactoring goals, dependency map, extraction plan, test approach

### **Scenario C: Feature Implementation**
*New feature using existing codebase conventions*

**When to use**: "I need to implement a new feature following our patterns"  
**What you'll get**: Feature spec, code stubs with TODOs, test outline, integration points

### **Scenario D: Systematic Debugging**
*Track down root cause of production issue*

**When to use**: "I need to debug this systematic issue"  
**What you'll get**: Hypothesis, investigation steps, diagnostic queries, solution options

---

## Structured Interrogation Framework

The skill will ask you these questions to build context:

<interrogation_questions>

### Phase 1: Current State Analysis (5-7 questions)
1. **Language & Framework**: What language/framework + version? (e.g., Python 3.11 + Django 4.2)
2. **Architecture Pattern**: What's the overall pattern? (Monolith, microservices, event-driven, layered?)
3. **Current Problem**: What specifically needs to change? (One sentence)
4. **Scope**: Is this one file, one module, or multiple services?
5. **Team Size**: How many developers? What's your role? (Individual contributor, tech lead, etc.)

### Phase 2: Target State Definition (3-4 questions)
6. **Success Criteria**: How will you know it's working? (Metrics, tests, deployment success?)
7. **Constraints**: Any hard constraints? (No downtime, budget limits, timeline?)
8. **Dependencies**: What other systems does this touch?

### Phase 3: Implementation Context (3-4 questions)
9. **Test Coverage**: Do you have existing tests? What's the pattern? (Unit, integration, e2e?)
10. **Team Conventions**: What's the naming convention? Error handling pattern? Logging standard?
11. **Review Process**: What does code review look like? (Automated checks, approval gates?)
12. **Rollback Plan**: What's your safety net if something goes wrong?

### Phase 4: Knowledge Gathering (2-3 questions)
13. **Similar Changes**: Have you done something like this before?
14. **Tribal Knowledge**: What does every developer wish they knew about this codebase?
15. **Decision Log**: Are there decisions that limit how you can change this?

</interrogation_questions>

---

## Output Format Specification

### 1. Implementation Plan with ReAct
```
## Migration Plan: [Component] from [Old] to [New]

### Phase 1: Preparation
**THINK**: What needs to be true before we start?
- [ ] Dependencies installed
- [ ] Tests passing  
- [ ] Backup created
- [ ] Team notified

**ACT**: Run these commands:
\`\`\`bash
# Setup steps with exact commands
\`\`\`

**OBSERVE**: Verify with:
\`\`\`bash
# Verification commands
\`\`\`

### Phase 2: Core Change
**THINK**: What's changing and why?
- Breaking change X affects Y consumers
- New API requires Z configuration
- Database migration needed for schema

**ACT**: Apply these changes:
\`\`\`diff
- old_code()
+ new_code()
\`\`\`

**OBSERVE**: Test coverage:
- [ ] Unit test for new_code()
- [ ] Integration test for X→Y flow
- [ ] No regression in unchanged code

### Phase 3: Verification
**THINK**: How do we know this is safe?

**ACT**: Run full test suite

**OBSERVE**: Success criteria met
```

### 2. Code Diff with Annotations
```python
# THINK: Why are we changing this class?
# - Needs to support async operations
# - Current implementation blocks on I/O
# - Caller expects non-blocking behavior

# ACT: Before
class DataFetcher:
    def get_data(self, url):
        return requests.get(url).json()

# ACT: After  
class DataFetcher:
    async def get_data(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

# OBSERVE: Test this change:
# - Unit test: mock async response, verify await
# - Integration test: real async flow, verify non-blocking
# - Regression: old caller code still works (adapter if needed)
```

### 3. Test Strategy Matrix
```
| Component | Test Type | Approach | Coverage |
|-----------|-----------|----------|----------|
| DataFetcher | Unit | Mock async response | get_data returns parsed JSON |
| UserService | Integration | Real async client | User creation flow with I/O |
| API Handler | E2E | Load test | 100 concurrent requests |
| Rollback | Regression | Before/after comparison | No breaking changes |
```

### 4. Verification Checklist
```
## Pre-Deployment Checklist

### Code Quality
- [ ] Tests pass (unit + integration + e2e)
- [ ] Code review approved by [person/team]
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

---

## Using the Skill: Step-by-Step Workflow

### Step 1: Choose Your Scenario
```
"I need to migrate from Python 3.9 to 3.12"
→ Scenario A (Code Migration)

"Our monolith is 50K lines, time to extract services"  
→ Scenario B (Refactoring)

"Build user authentication module following our patterns"
→ Scenario C (Feature Implementation)

"Production is slow, need to find root cause"
→ Scenario D (Systematic Debugging)
```

### Step 2: Let the Skill Interrogate
The skill will ask 12-15 questions. **Answer fully** — this is where context richness happens.

Example interrogation flow:
```
Q1: What language/framework?
A: Python 3.9 with Django 3.2

Q2: What's the architecture pattern?
A: Monolithic Django app with background workers via Celery

Q3: What needs to change?
A: Move to Python 3.12 and Django 5.0, async views

Q4: Scope?
A: All 47 views in main app, plus celery tasks

Q5: How many developers?
A: Team of 5, I'm tech lead

[... continues through all 15 questions ...]
```

### Step 3: Review Generated Plan
The skill will output:
- ✅ Implementation plan with phases
- ✅ Code diffs with THINK/ACT/OBSERVE annotations
- ✅ Test strategy matrix
- ✅ Verification checklist

### Step 4: Execute with Confidence
Follow the plan step-by-step, using the checklist to verify each phase.

---

## Design Principles

### Principle 1: Context Over Guessing
**Never generate code without understanding:**
- What problem does this solve?
- What constraints exist?
- What conventions must be followed?
- What could break?

The interrogation phase ensures we have rich context before any code.

### Principle 2: Structure Over Prose
**Always output:**
- Structured plans (not narratives)
- Checklists (not suggestions)
- Diffs (not rewrites)
- Test cases (not "should work")

Bootcamp intuition: Structure gets rewarded.

### Principle 3: Verification by Default
**Every change includes:**
- Why we're making it (THINK)
- The actual change (ACT)
- How to verify it works (OBSERVE)

ReAct pattern enforces safety.

### Principle 4: Team Conventions Matter
**Always respect:**
- Naming conventions
- Error handling patterns
- Logging standards
- Code review process

This is where interrogation questions pay dividends.

---

## Example: Complete Workflow

### Scenario: Feature Implementation

**You say:**
```
I need to add a new Payment Processing module to our existing system.
It should accept credit card and PayPal payments.
I want to follow our team's conventions.
```

**Skill interrogates (Phase 1: Current State):**
```
Q1: Language/framework?
→ "Python 3.11 + FastAPI"

Q2: Architecture?
→ "Microservices, async-first design"

Q3: Current structure?
→ "Other modules are in /services/, each with models.py, routes.py, tests/"

Q4: Scope?
→ "New module only, but touches Order service"
```

**Skill interrogates (Phase 2: Target State):**
```
Q5: Success criteria?
→ "Process payments, return confirmation, handle failures gracefully"

Q6: Constraints?
→ "No external payment service downtime allowed, must be testable"

Q7: Dependencies?
→ "Order service, Customer service, audit log service"
```

**Skill interrogates (Phase 3: Implementation Context):**
```
Q8: Test pattern?
→ "Pytest, mock external APIs, use fixtures for common objects"

Q9: Team conventions?
→ "Snake_case functions, async/await required, error logging with structured JSON"

Q10: Code review?
→ "PR requires approval + CI tests passing"
```

**Skill generates: Implementation Plan**
```markdown
## Payment Processing Module Implementation

### Phase 1: Setup
**THINK**: What's the minimal skeleton?
- FastAPI router
- Database models
- External API clients

**ACT**:
\`\`\`python
# services/payment_processing/models.py
from sqlalchemy import Column, String, Float, DateTime
from datetime import datetime

class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    amount = Column(Float)
    provider = Column(String)  # credit_card, paypal
    status = Column(String)  # pending, completed, failed
    created_at = Column(DateTime, default=datetime.utcnow)

# services/payment_processing/routes.py
from fastapi import APIRouter, HTTPException
import logging

router = APIRouter(prefix="/payments")
logger = logging.getLogger(__name__)

@router.post("/process")
async def process_payment(order_id: int, provider: str, amount: float):
    """Process payment through specified provider"""
    # TODO: Validate input
    # TODO: Call provider API
    # TODO: Update Payment record
    # TODO: Notify Order service
    # TODO: Log with structured JSON
    pass

# services/payment_processing/tests/test_routes.py
import pytest
from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
async def test_process_payment_success():
    # TODO: Mock payment provider
    # TODO: Assert payment recorded
    # TODO: Assert order service notified
    pass

@pytest.mark.asyncio  
async def test_process_payment_provider_failure():
    # TODO: Mock provider error
    # TODO: Assert graceful failure
    # TODO: Assert retry logic
    pass
\`\`\`

**OBSERVE**: Verify structure exists:
\`\`\`bash
ls -la services/payment_processing/
# Should show: models.py, routes.py, tests/, __init__.py
pytest services/payment_processing/tests/ -v
# All tests should run (though skip actual implementations)
\`\`\`
```

**Skill generates: Code Diffs with Annotations**
```python
# THINK: Why do we need payment provider abstraction?
# - Support multiple providers (credit card, paypal, etc.)
# - Swap providers without changing business logic
# - Easy to test with mocks
# - Follows team's dependency injection pattern

# ACT: Before (monolithic payment)
def process_payment(order_id, card_number, cvv, amount):
    response = requests.post("https://api.stripe.com/...", ...)
    if response.status == 200:
        update_order(order_id, "paid")
    return response

# ACT: After (provider abstraction)
class PaymentProvider:
    async def charge(self, amount: float) -> PaymentResult:
        raise NotImplementedError

class StripeProvider(PaymentProvider):
    async def charge(self, amount: float) -> PaymentResult:
        result = await self.client.create_charge(amount=amount)
        return PaymentResult(success=result.status == "succeeded", ...)

class PayPalProvider(PaymentProvider):
    async def charge(self, amount: float) -> PaymentResult:
        result = await self.client.create_payment(amount=amount)
        return PaymentResult(success=result.state == "approved", ...)

async def process_payment(order_id: int, provider: PaymentProvider, amount: float):
    """Route payment through appropriate provider"""
    result = await provider.charge(amount)
    
    if result.success:
        logger.info("payment_processed", extra={
            "order_id": order_id,
            "amount": amount,
            "provider": provider.__class__.__name__
        })
        await order_service.mark_paid(order_id)
    else:
        logger.error("payment_failed", extra={
            "order_id": order_id,
            "reason": result.error
        })
        raise PaymentException(result.error)
    
    return result

# OBSERVE: This design enables:
# - Unit test: mock PaymentProvider, verify logic
# - Integration test: real Stripe test account
# - Easy to add new provider: just implement interface
# - Follows team's dependency injection convention
```

**Skill generates: Test Strategy**
```
| Component | Test Type | Approach | Coverage |
|-----------|-----------|----------|----------|
| PaymentProvider (abstract) | Unit | Mock all implementations | Interface contract |
| StripeProvider | Unit | Mock Stripe API | charge() returns correct result |
| PayPalProvider | Unit | Mock PayPal API | charge() returns correct result |
| process_payment() | Unit | Mock providers | Success path, failure path |
| process_payment() + Order svc | Integration | Real test database, mock payment APIs | Full workflow |
| /process endpoint | E2E | Load test against test environment | 1000 concurrent requests |
```

**Skill generates: Verification Checklist**
```
## Pre-Merge Checklist

### Code Quality
- [ ] All tests pass: pytest services/payment_processing/
- [ ] Type checking passes: mypy services/payment_processing/
- [ ] Code review approved by [peer]
- [ ] No security issues (no hardcoded credentials, etc.)
- [ ] README added to explain module

### Functionality
- [ ] Happy path works: successful payment
- [ ] Error path works: provider failure handled
- [ ] Retry logic works: transient failures retry
- [ ] Audit logging works: all transactions logged with JSON
- [ ] Order service integration: payment status reflected

### Safety  
- [ ] Rollback plan: Can disable module with feature flag
- [ ] No database migration needed (using base SQLAlchemy)
- [ ] Monitoring added: alert on payment failures
- [ ] Can run alongside old payment system
```

---

## Advanced Usage: Combining with Bootcamp Patterns

### Using with Priority Builder Pattern
Map your development work to ABCD:
```
Action: Implement payment processing module (your feature)
Behavior: 100% test coverage, follows team conventions
Context: Supports multiple payment providers
Delivered: Rollback-safe, production-ready code
```

### Using with ReAct Pattern  
Systematically debug production issues:
```
THINK: What could cause this error? (Hypothesis generation)
ACT: Add logging here, check this metric (Investigation)
OBSERVE: Does hypothesis hold? (Verification)
```

### Using with Tree of Thoughts
Complex architecture decisions:
```
Generate: Multiple refactoring approaches (extract service A, B, or C?)
Evaluate: Which respects team conventions best?
Choose: Option B because it aligns with event-driven pattern
```

---

## When to Use This Skill vs. IDE

| Task | Use IDE | Use Skill |
|------|---------|-----------|
| Syntax autocomplete | ✅ IDE | ❌ Overkill |
| Quick bug fix | ✅ IDE | ❌ Overkill |
| Variable rename across file | ✅ IDE refactoring | ❌ Use IDE |
| **Migrate framework** | ❌ Too complex | ✅ **This skill** |
| **Refactor large component** | ❌ Too many decisions | ✅ **This skill** |
| **New feature matching patterns** | ❌ Need context | ✅ **This skill** |
| **Root cause debugging** | ❌ Too many unknowns | ✅ **This skill** |
| **Code review for architecture** | ❌ Just guidance | ✅ **This skill** |

---

## Bootcamp Integration

### For Facilitators
Use this skill in **Session 2: Advanced Patterns** when discussing:
- ReAct pattern (THINK→ACT→OBSERVE)
- Real-world code examples  
- Systematic problem-solving in technical domain

### For Participants (Role-Fork Exercise)
**Use this skill when:**
- You're the "Developer" in a role-fork scenario
- You need to implement a feature quickly
- You're new to a codebase and need guidance
- You're debugging a systematic issue

**Expected outcome:**
- Understand how structured interrogation builds context
- See ReAct pattern in action with real code
- Generate production-ready code following team conventions

---

## FAQ

**Q: Will this skill generate all my code for me?**  
A: No. It generates structure, plans, and guidance. You write the actual code, guided by the plan and diffs.

**Q: What if I don't know the answers to all 15 interrogation questions?**  
A: That's fine! The skill will ask follow-up questions to clarify. The goal is to gather context, not quiz you.

**Q: How is this different from just asking an LLM to write code?**  
A: The interrogation phase ensures the code respects your team's conventions, matches your architecture, and solves the actual problem — not a generic version.

**Q: Can I use this for legacy code with no tests?**  
A: Yes. The interrogation will help you understand what's there and create a safe refactoring plan.

**Q: What if the skill suggests something that violates my team's standards?**  
A: Tell it during interrogation: "Our error handling uses exceptions, not result types." It will adjust.

---

## References

- **ReAct Pattern**: Yao et al. (2022) "ReAct: Synergizing Reasoning and Acting in Language Models"
- **Chain of Thought**: Wei et al. (2022) "Chain-of-Thought Prompting"
- **Few-shot Learning**: Brown et al. (2020) "Language Models are Few-Shot Learners"
- **Prompt Patterns**: White et al. (2023) "A Prompt Pattern Catalog to Enhance Prompt Engineering"

---

**Version**: 1.0  
**Last Updated**: 2026-03-18  
**For**: Joey's Prompt Engineering Bootcamp v2
