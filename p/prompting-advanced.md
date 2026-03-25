---
title: "Prompt Patterns (Advanced)"
description: "ReAct, Tree of Thoughts, self-consistency, constitutional AI."
author: "Joey Lopez"
date: "2025-11-05"
tags: ["prompting", "reference", "teaching"]
atom_id: 5
source_html: "prompting-advanced.html"
url: "https://jrlopez.dev/p/prompting-advanced.html"
generated: true
---

[jrlopez.dev ]()[ReAct ]()[Tree of Thoughts ]()[Spec-Kit ]()[When to Use ]()[Reference ]()
# Advanced Prompting Patterns When foundational patterns aren't enough. Multi-step reasoning, decision frameworks, and orchestrated workflows. Joey Lopez [ReAct ]()[Tree of Thoughts ]()[Spec-Kit ]()Pattern 1
## ReAct: Think → Act → Observe ReAct is a multi-phase reasoning pattern where you explicitly separate thinking from action. The key insight is that you don't just dump everything into one prompt—you pause at validation checkpoints between phases. I use this when each step builds on the previous one and I need confidence that we're not compounding errors. Before moving to the next phase, I check: Did the last step actually work? Core Idea ReAct (Reasoning + Acting) was formalized by Yao et al. (2022). The principle: explicit validation checkpoints between reasoning phases prevent hallucination chains from cascading.
### When to Use ReAct
 - Multi-step tasks where each step depends on previous results
 - You need to verify before continuing (database migrations, system changes, complex data pipelines)
 - Error recovery is critical—you want to catch issues immediately, not at the end
 - The task involves both planning and execution
### The Template ReAct Phase Structure
```
## Phase 1: [Name]
THINK: [What must be true before we act? What are we checking?]
ACT: [Specific, concrete tasks]
CHECK: [How do we verify this succeeded? What's the success criterion?]

## Phase 2: [Name]
THINK: [What did Phase 1 give us? What changed?]
ACT: [Next concrete tasks, informed by Phase 1 results]
CHECK: [Validation step]

[Repeat as needed]
```

### Real Example: Database Migration Database Migration via ReAct
```
## Phase 1: Schema Analysis
THINK: Do we understand the current schema? Are there constraints we'll break?
ACT:
- Inspect current table structure
- List all foreign keys and indexes
- Identify nullable vs non-nullable columns

CHECK: We have a complete picture of the schema. No surprises when we migrate.

## Phase 2: Migration Script Generation
THINK: Given what Phase 1 showed us, what migration script is safe?
ACT:
- Generate the migration using the constraints from Phase 1
- Include rollback statements

CHECK: Script is syntactically valid and includes rollback.

## Phase 3: Staging Deployment
THINK: Does this work in a realistic environment?
ACT:
- Run against staging database (copy of production)
- Verify data integrity post-migration
- Check query performance

CHECK: No errors on staging. Query performance acceptable.

## Phase 4: Production
THINK: We have evidence from staging. Are we ready?
ACT:
- Create production backup
- Run migration
- Verify against production data

CHECK: Migration succeeded. Data integrity confirmed. Rollback tested and works.
```
The Insight The CHECK step is what separates ReAct from just writing a longer prompt. You're forcing explicit validation. If the model says "check passed," you actually verify it independently. This is where the reliability comes from. Pattern 2
## Tree of Thoughts: Explore Before Committing Tree of Thoughts is about generating multiple approaches to a decision, evaluating their tradeoffs, then choosing one with documented reasoning. You're not just picking the first reasonable option—you're deliberately exploring the decision space. I use this when a decision has real tradeoffs. The output isn't just the choice; it's the reasoning that justifies it. That reasoning becomes reusable for future similar decisions. Core Idea Tree of Thoughts (Yao et al., 2023) formalizes decision-making as a multi-branch search. You generate candidate approaches, evaluate each against criteria, then select the best with explicit justification.
### When to Use Tree of Thoughts
 - Multiple valid approaches exist with different tradeoffs
 - You need to document WHY you chose one over others (for future reference or stakeholders)
 - The decision affects downstream work or architecture
 - Risk tolerance matters—some options are safer than others
### The Template Tree of Thoughts Decision Structure
```
## Decision: [What's being decided?]
[Context: Why are we deciding? What's at stake?]

### Option A: [Name]
- Pros: [Benefits, what goes right]
- Cons: [Drawbacks, what goes wrong]
- Effort: [Implementation cost, e.g., 2 days]
- Risk: [Low / Med / High, and why]

### Option B: [Name]
- Pros: [...]
- Cons: [...]
- Effort: [...]
- Risk: [...]

### Option C: [Name]
[Same structure]

### Recommendation
Choose [X] because [explicit reasoning given constraints].
Key tradeoff we're accepting: [What are we giving up?]
```

### Real Example: Security Config Modernization Migration Strategy via Tree of Thoughts
```
## Decision: Modernize API authentication to OAuth 2.0

Context: Current system uses API keys in headers. It's insecure and hard to audit.
We need to move but must maintain backward compatibility for 90 days (Q2 migration window).

### Option A: Keep Current System
- Pros: Zero effort, zero risk, no breaking changes
- Cons: Security risk remains, audit trail weak, tech debt grows
- Effort: 0 days
- Risk: Low (no change = no breakage)

### Option B: Parallel Systems (Recommended)
- Pros: Gradual migration path, clients can transition at own pace, rollback is safe
- Cons: Two auth systems to maintain for 90 days, testing burden is higher
- Effort: 5 days (OAuth implementation + migration logic)
- Risk: Medium (complexity of dual-system, but reversible)

### Option C: Full Cutover
- Pros: Clean break, one auth system, audit trail complete
- Cons: Breaking change, forces all clients to migrate immediately, 24h downtime expected
- Effort: 3 days (faster because no parallel logic)
- Risk: High (client outages, support burden)

### Recommendation
Choose Option B (Parallel Systems) because:
- We have a 90-day window; gradual migration is safer
- Client ecosystem is fragmented; not everyone can upgrade in parallel
- Tradeoff we're accepting: 5 days of dev vs. 30 days of operational complexity (worth it)
- Rollback path is clear if OAuth implementation has issues
```
The Insight You'll do this decision again. By documenting your reasoning upfront—why you rejected Option C, what tradeoff made Option B worth the effort—you save yourself from re-litigating the same choice six months from now. Pattern 3
## Spec-Kit: Separation of Concerns for Complex Tasks Spec-Kit is a file structure pattern. Instead of dumping everything into one massive prompt, you split complex work into 3-4 files that build on each other. Each file has a clear job. This scales to much larger problems than a single prompt can handle. I use this when context is too large or the task is repeatable. The knowledge base becomes write-once, use-forever. Every future task in that domain inherits it. Core Idea Spec-Kit is named after the specification kits used in aerospace and manufacturing. One document describes the system forever (knowledge base). Each project applies it to solve a specific instance (specification + plan). Context grows with complexity, not with each new task.
### The Three Files
#### 1. knowledge-base.md (Write Once) Domain context, architectural decisions, constraints, terminology. Answers questions like:
 - What is this system's architecture?
 - What constraints do we always operate under?
 - What terminology does this domain use?
 - What decisions have we already made and why? You write this once. Every future task in this domain reads it. It pays dividends over time.
#### 2. specification.md (Task-Specific) This task's requirements, acceptance criteria, edge cases. It reads the knowledge base and says "given all that, here's what we need to do right now."
 - What is the goal?
 - What's in scope? What's out?
 - How do we know when we're done?
 - What edge cases matter?
#### 3. implementation-plan.md (Task-Specific) Phased execution with dependencies and validation checkpoints. This is where you apply ReAct and Tree of Thoughts to the specific task.
 - Phase 1: [What goes first? Why?]
 - Phase 2: [What depends on Phase 1?]
 - Validation: [How do we know each phase succeeded?]
 - Rollback: [How do we undo if something fails?]
### When to Use Spec-Kit
 - Complex, multi-step work that's hard to fit in a single prompt
 - The task is repeatable or similar tasks will follow (migrations, architecture decisions, configurations)
 - You need to collaborate with others (specs serve as shared references)
 - High-stakes decisions where getting it right matters more than speed
 - Across technical and non-technical domains (works for business tasks too—interview prep, priority documents, fundraising pitch)
### Template: knowledge-base.md Reusable Domain Context
```
# Knowledge Base: [Domain Name]

## System Architecture
[How is this system organized? What are the main components?]

## Constraints
[What's always true? What can never change?]
- [Constraint 1]
- [Constraint 2]

## Terminology
| Term | Definition |
| --- | --- |
| [Term] | [Definition] |

## Key Decisions Made
- [Decision 1]: [Why we chose this]
- [Decision 2]: [Why we chose this]

## Common Patterns
[How do we usually solve problems in this domain?]
```

### Template: specification.md Task-Specific Requirements
```
# Specification: [Task Name]

## Goal
[What are we trying to achieve?]

## Context
[Why are we doing this? What's the business reason?]

## Scope
### In Scope
- [Requirement 1]
- [Requirement 2]

### Out of Scope
- [What we're explicitly not doing and why]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Edge Cases
[What could go wrong? What's unusual about this task?]
```

### Template: implementation-plan.md Phased Execution Plan
```
# Implementation Plan: [Task Name]

## Phase 1: [Name]
Depends on: [Nothing / Phase 0]
Duration: [Estimate]

THINK: [What do we need to verify before acting?]
ACT: [Concrete tasks]
CHECK: [Validation step]

## Phase 2: [Name]
Depends on: [Phase 1]
Duration: [Estimate]

THINK: [...]
ACT: [...]
CHECK: [...]

## Rollback
[How do we undo this if something goes wrong?]
```

### Cross-Domain Example Spec-Kit works everywhere. Here's how you'd apply it to interview prep (business, not technical): Business Task: Interview Prep
```
## knowledge-base.md
### Company Context
- Founded 2015, 800 people, Series C
- Fundraising in Q3 targeting $50M
- Product: Developer tools for monitoring

### Common Questions We See
- "How do you handle scale?" → Technical depth needed
- "What's your vision?" → CEO alignment matters
- "Why join now?" → Understanding their fundraising matters

## specification.md
### Goal
Prepare for interviews at TechCorp for Staff Engineer role

### Acceptance Criteria
- [ ] Can answer 15 technical depth questions
- [ ] Can articulate how my background aligns with their problems
- [ ] Can explain why this role at this stage

## implementation-plan.md
### Phase 1: Deep Dive on Technical Stack
- Spend 4 hours on their architecture docs
- Run their demo, break it, understand failure modes

### Phase 2: Study Their Problems
- What are 3 things they're probably struggling with at scale?
- How does my experience address those?

### Phase 3: Interview Dry Run
- Friend asks random interview questions
- Get feedback on clarity and depth
```
Important Don't over-engineer. If the task is "rename a variable," you don't need Spec-Kit. Use it when complexity is real, when context is large, or when you're solving the same problem more than once. Pattern Selection
## Choosing the Right Pattern These patterns aren't mutually exclusive. The question isn't "which one should I use?" It's "which combination solves this task cleanly?"
### Decision Table

| Task Type  || Pattern  || Why This Works  |

| Simple, well-understood  || Foundational (Persona + Few-Shot)  || Don't add complexity where it doesn't belong  |

| Multi-step with dependencies  || ReAct  || Validation checkpoints prevent error cascades  |

| Decision with real tradeoffs  || Tree of Thoughts  || Documented reasoning is reusable  |

| Complex, high-stakes, repeatable  || Spec-Kit  || Separation of concerns scales to large contexts  |

| Large task combining all of above  || Combine them  || ReAct phases + ToT decisions + Spec-Kit files  |

### Practical Combinations **Scenario 1: Database Migration **
 - Use Spec-Kit: knowledge-base describes the system, specification says which tables, plan says which phases
 - Use ReAct: Each phase has THINK/ACT/CHECK steps
 - Result: Highly structured, low-risk execution **Scenario 2: Architecture Decision **
 - Use Tree of Thoughts: Explore monolith vs. microservices vs. serverless
 - Use Spec-Kit knowledge-base: Document constraints (team size, latency requirements, budget)
 - Result: Justified decision that stakeholders understand **Scenario 3: Feature Implementation **
 - Use Spec-Kit: knowledge-base for domain context, specification for requirements
 - Use ReAct: Implementation plan with phases
 - Result: Clear scope, execution discipline, testable outcomes Anti-Pattern **Over-engineering simple tasks. **If you're adding ReAct phases to rename a variable or using Spec-Kit for a 10-minute task, you've lost the plot. These patterns have cognitive overhead. They pay off when complexity is real. Rule of Thumb Start simple. If you find yourself confused about state, unsure where you are in the task, or making the same decision repeatedly, that's when you upgrade to a more complex pattern. References
## Quick Reference
### Papers & Sources

| Pattern  || Citation  || Key Insight  |

| ReAct  || Yao et al. (2022) "ReAct: Synergizing Reasoning and Acting in Language Models"  || Validation checkpoints between reasoning phases  |

| Tree of Thoughts  || Yao et al. (2023) "Tree of Thoughts: Deliberate Problem Solving with Language Models"  || Multi-branch exploration before committing  |

| Prompt Patterns  || White et al. (2023) "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT"  || 16+ catalogued patterns (foundational and advanced)  |

### Related Resources [Foundational Prompting Patterns ]()covers Persona, Few-Shot, Chain-of-Thought, and Output Format. Those are your building blocks. The patterns here are what you build when the foundational ones aren't enough.
### When You're Stuck
 - **Task feels too large to fit in one prompt: **Use Spec-Kit
 - **You keep making the same decision over again: **Use Tree of Thoughts (document your reasoning)
 - **Each step depends on the previous one: **Use ReAct with CHECK steps
 - **You're not sure if it worked: **Add validation checkpoints
 - **You're over-engineering: **Strip it back. Start simple. Upgrade when complexity demands it. Joey Lopez · 2026 · [jrlopez.dev ]()
[← jrlopez.dev ]()· [← foundational patterns ]()· [guardrails → ]()