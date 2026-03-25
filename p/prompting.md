---
title: "Prompt Patterns (Foundational)"
description: "Zero-shot, few-shot, chain-of-thought, persona, template."
author: "Joey Lopez"
date: "2025-10-20"
tags: ["prompting", "reference", "teaching", "template"]
atom_id: 4
source_html: "prompting.html"
url: "https://jrlopez.dev/p/prompting.html"
generated: true
---

[jrlopez.dev ]()[The gap ]()[Approaches ]()[Patterns ]()[Second brain ]()[Reference ]()
# Prompt Engineering Notes Workshop notes cleaned up. Patterns, anti-patterns, and exercises from real sessions. Take what's useful. Joey Lopez [the gap ]()[approaches ]()[patterns ]()Section 01 I didn't invent any of this. Chain of Thought is from Wei et al., Tree of Thoughts is from Yao et al., the Persona and Template patterns are catalogued in White et al. I just organized them in the order I wish someone had shown me.
## The gap The fastest way to understand prompt engineering is to feel the difference. Here's a quick exercise I use in workshops. Try this **Open whatever AI tool you use. **Type this and save the output:
```
Write a Python function that validates email addresses.
```

Then try this one. Same task:
```
You are a senior Python developer building a user registration API.

Write an email validation function with these requirements:
- Must handle edge cases: plus-addressing (user+tag@domain),
 international domains, and subdomains
- Return a typed result (valid/invalid) with specific error reasons
- Include type hints and follow PEP 8

Example input/output:
 validate_email("user@example.com") -> ValidationResult(valid=True)
 validate_email("user@") -> ValidationResult(valid=False, error="Missing domain")
 validate_email("user+tag@sub.example.co.uk") -> ValidationResult(valid=True)

Constraints:
- Do NOT use the 're' module for the core logic
- Must handle at least 5 explicit edge cases
- Include docstring with usage examples
```

Same AI. Same model. Same task. The second output is more specific, more tested, more usable. The difference isn't what the AI knows -- it's what you gave it to work with. That's basically the whole idea. Everything below -- every pattern, every template -- is just a different way of getting the right context in front of the model faster.
### Three intuitions These explain most of what happens in AI interactions:

| Intuition  || What it means  || Analog  |

| **Context is everything ** || The model completes patterns from what you give it. More relevant context = better output.  || A vague Jira ticket produces vague work.  |

| **Structure gets rewarded ** || Organized input produces organized output. The model was trained to respect structure.  || A well-formatted code review gets better responses than a wall of text.  |

| **You are the retrieval system ** || Every AI interaction is: retrieve context, assemble it, generate. The question is who's doing the retrieval.  || Re-explaining your project every conversation = doing retrieval by hand.  |

These three ideas explain RAG, prompt engineering, context windows, and most of what enterprise AI platforms do. The terminology doesn't matter yet. The intuitions do. Section 02
## Three approaches Not every task needs the same level of effort. Using a four-file spec-driven workflow to fix a typo is overkill. I think about it as: what are the stakes? **Simple, one-off task? **
Yes → Freestyle. Just type and send.
No ↓

**Will you repeat this? Does quality matter? **
Yes → Systematic prompt. Add patterns.
No ↓

**Complex, multi-step, or high-stakes? **
Yes → Spec-driven. Multiple files, structured workflow.

### Freestyle Just talk to the AI. No structure, no patterns. This is how most people use AI most of the time, and for quick questions and throwaway tasks, it's fine. **Use it for: **Quick questions, brainstorming, anything you'd delete in an hour. **Stop using it when: **You find yourself re-explaining context, correcting output, or doing the same task twice.
### Systematic prompts Apply named patterns -- persona, few-shot, chain-of-thought, output format -- to a single prompt. This is the workhorse. Freestyle
```
Help me review this pull request.
```

Generic feedback. Misses project conventions. Systematic
```
You are a senior code reviewer
focused on maintainability.

Review this PR against these criteria:
- Error handling completeness
- Test coverage for edge cases
- Naming conventions (camelCase)

Flag severity: MUST FIX / SHOULD FIX / NIT

Example:
MUST FIX: Missing null check on line 42.
 userService.getUser() can return null
 but is used without guard.

PR diff:
[paste diff]
```

Specific, actionable, consistently formatted.
### Spec-driven For complex multi-step work: separate your knowledge, requirements, and execution plan into distinct files. Feed them to the AI in order. **The three files: **

| File  || Contains  || Reusable?  |

| knowledge-base.md || Domain context, architecture decisions, constraints, terminology  || Yes -- project-level  |

| specification.md || This feature's requirements, acceptance criteria, edge cases  || No -- feature-level  |

| implementation-plan.md || Phased execution, dependencies, validation checkpoints  || No -- task-level  |

The knowledge base is write-once, use-forever. You build it on day one and every future spec inherits it.
### Where these come from These aren't categories I made up. They map to existing industry practices:

| Approach  || Industry equivalent  || Maturity  |

| Freestyle  || Ad-hoc ChatGPT/Copilot usage  || Universal  |

| Systematic  || ADRs + .github/copilot-instructions.md || 10+ years  |

| Spec-driven  || GitHub spec-kit, Kiro, structured file workflows  || Experimental  |

Honest assessment Systematic prompts (ADRs + config files) are **proven at scale **across Microsoft, AWS, Google, Netflix, and Spotify. Spec-driven workflows are newer and less battle-tested. Both work. The difference is maintenance overhead vs. task complexity. Use the simplest approach that handles your complexity. Escalate when you need to, not before. Section 03
## Patterns Every effective prompt is built from a small set of composable patterns. I think of them like tools in a toolbox -- a hammer isn't better than a screwdriver, but using a hammer on a screw will ruin your day.
### Foundational patterns These four cover roughly 80% of daily prompt engineering. I'd get comfortable with these before reaching for the advanced ones. Persona Proven I use this when I need domain expertise, consistent tone, or a specific frame of reference. **Template: **
```
You are [role] with [specific expertise].
Your focus areas include [domains].
[Task]
```
Without persona
```
Explain this database schema.
```
With persona
```
You are a database architect
specializing in high-throughput
transactional systems.

Explain this schema, focusing on:
- Indexing strategy
- Query performance implications
- Normalization tradeoffs
```
Why it works The persona biases the model toward responses that people with that expertise would produce in the training data. The more specific the persona, the more targeted the activation. **Source: **White et al. (2023), "A Prompt Pattern Catalog" -- arXiv 2302.11382 Few-Shot Proven I use this when showing is faster than explaining -- when I have a transformation or format that's hard to describe but easy to demonstrate. **Template: **
```
Transform inputs using these examples:

Example 1:
 Input: [example input]
 Output: [example output]

Example 2:
 Input: [example input]
 Output: [example output]

Now transform:
 Input: [your actual input]
```
Without examples
```
Convert these Java imports
to the new namespace.
```
With examples
```
Convert imports using these rules:

Example:
 Before: import javax.validation.Valid;
 After:  import jakarta.validation.Valid;

Example:
 Before: import javax.servlet.http.*;
 After:  import jakarta.servlet.http.*;

Now convert:
 import javax.persistence.Entity;
```
Why it works Two to three examples establish a pattern more reliably than a paragraph of instructions. The model extracts the transformation rule and applies it. More than three examples rarely helps -- diminishing returns set in fast. **Source: **Brown et al. (2020), "Language Models are Few-Shot Learners" -- the GPT-3 paper Chain-of-Thought Proven I use this when the task requires multi-step reasoning or debugging, and I need to see (and verify) the logic. **Template: **
```
Solve this step by step:

1. First, analyze [aspect]
2. Then, evaluate [aspect]
3. Next, consider [aspect]
4. Finally, recommend [action]

Show your reasoning for each step.
```
Without CoT
```
Why is this API slow?
```
With CoT
```
Debug this API latency issue
step by step:

1. Check the query execution plan
2. Identify N+1 query patterns
3. Evaluate connection pool config
4. Check for missing indexes
5. Review payload size

Show reasoning for each step.

Endpoint: GET /api/users
Avg response: 2.3s
Expected:<200ms
```
Why it works Step-by-step reasoning reduces errors on complex tasks by 10-30% in benchmarks. More importantly, it makes errors visible. When you can see the reasoning chain, you can catch where it went wrong instead of getting a confidently wrong final answer. **Source: **Wei et al. (2022), "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" -- arXiv 2201.11903 Output Format (Template) Proven I use this when I need consistent, parseable, or copy-paste-ready output -- when the format matters as much as the content. **Template: **
```
Respond in this exact format:

## Summary
[2-3 sentences]

## Changes Required
- [ ] Change 1: [description]
- [ ] Change 2: [description]

## Risk Assessment
| Risk | Severity | Mitigation |
|------|----------|------------|
| ...  | ...      | ...        |
```
Why it works The model was trained on millions of interactions where structured requests got structured responses. When you provide a template, the output almost always mirrors it.
### Advanced patterns I reach for these when the foundational patterns aren't enough -- when there are dependencies between steps, multiple valid approaches, or several concerns to orchestrate. ReAct Research-backed I use this for multi-phase work where each phase depends on the previous one and I need validation checkpoints between steps. **Template: **
```
## Phase 1: [Name]
THINK: [What must be true before we act?]
ACT:   [Specific tasks]
CHECK: [How to verify this phase succeeded]

## Phase 2: [Name]
THINK: [What did Phase 1 give us?]
ACT:   [Next tasks]
CHECK: [Validation]
```
Example: database migration
```
## Phase 1: Schema Backup
THINK: Must have rollback before any DDL changes
ACT:   pg_dump --schema-only > backup_schema.sql
CHECK: Backup file exists and is non-empty

## Phase 2: Add New Columns
THINK: Schema backup confirmed, safe to alter
ACT:   ALTER TABLE users ADD COLUMN email_verified BOOLEAN DEFAULT FALSE;
CHECK: \d users shows new column, existing data intact

## Phase 3: Backfill Data
THINK: Column exists, now populate from legacy flag
ACT:   UPDATE users SET email_verified = (status = 'verified');
CHECK: SELECT COUNT(*) WHERE email_verified IS NULL = 0
```

**Source: **Yao et al. (2022), "ReAct: Synergizing Reasoning and Acting in Language Models" Tree of Thoughts Research-backed I use this when multiple valid approaches exist and the tradeoffs depend on my specific context -- when I need to document why I chose option A over B. **Template: **
```
## Decision: [What needs deciding]

### Option A: [Name]
- Pros: [benefits]
- Cons: [drawbacks]
- Effort: [estimate]
- Risk: [Low/Med/High]

### Option B: [Name]
[same structure]

### Option C: [Name]
[same structure]

### Recommendation
Choose [X] because [rationale given constraints].
```
When not to use this Don't force this when only one reasonable approach exists. Manufacturing fake alternatives wastes time. If the answer is obvious, just do it. **Source: **Yao et al. (2023), "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" Meta-Prompting (Orchestration) Production-ready I use this when I need to combine multiple patterns, synthesize context from several sources, or create a reproducible workflow. **Template: **
```
# Task: [What we're building]

## Context Synthesis
From knowledge-base.md:
 - Domain rules: [extracted]
 - Constraints: [extracted]

From specification.md:
 - Requirements: [extracted]
 - Success criteria: [extracted]

## Execution
Using ReAct phases from implementation-plan.md:
 Phase 1: [action] -> Validate: [check]
 Phase 2: [action] -> Validate: [check]

Using Tree of Thoughts decisions:
 Decision 1: Chose [X] because [reason]

## Generate
[Final output instructions]
```

### Combining patterns These are composable. I start with one and add others only when they earn their place:

| Task complexity  || Patterns I typically use  |

| Simple (5-15 min)  || Persona + Few-shot  |

| Medium (30-60 min)  || Persona + Few-shot + Output format + Chain-of-Thought  |

| Complex (hours+)  || All foundational + ReAct + Tree of Thoughts + Meta-prompting  |

Common mistake Over-engineering simple tasks. If you're adding ReAct phases to rename a variable, you've lost the plot. Use the simplest approach that handles your complexity. Section 04
## Second brain Every conversation, you re-explain your project, your role, your constraints. You're doing context retrieval by hand, every time. The fix is writing it down once.
### Start with 10 questions Don't try to capture everything. Answer these in a single file. That file is your second brain v1. The first 10 questions
 - What project are you working on right now?
 - In one sentence, what does it do and who is it for?
 - What's the tech stack?
 - What are the 3 biggest constraints you work within?
 - What does "done" look like for your typical work items?
 - What mistakes do people make repeatedly on your project?
 - What do you wish the AI already knew about your work?
 - What output format do you prefer? (bullet points, tables, prose, code?)
 - What should the AI *never *assume about your work?
 - What's the one thing you re-explain in every AI conversation? Try this Create a file called my-context.md. Answer questions 1, 2, 3, and 10. Four answers, five minutes. Start a new AI conversation, paste that file at the top, and ask it to do something you'd normally do. Notice how much less explaining you need.
### The full framework: 100 questions Once the first 10 click, here's the expanded version. It's organized in two tiers:

| Tier  || Goal  || Questions  || Time  |

| **Tier 1: Knowledge Extraction ** || Get what's in your head into notes  || 50 questions across domain, requirements, tech, patterns, people  || 3-4 hours  |

| **Tier 2: Knowledge Composition ** || Compose those notes into a reusable AI context file  || 50 questions across AI usage, role, output standards, task patterns, composition  || 2-3 hours  |

Tier 1: Knowledge Extraction (50 questions)
#### Section A: Domain Context
 - What project/product are you working on right now?
 - In one sentence, what does it do and who is it for?
 - What's the business problem it solves?
 - Who are the main stakeholders and what do they care about?
 - What's the current state vs. the desired state?
 - What are the 3 biggest constraints you work within?
 - What decisions have already been made that you can't change?
 - What's the history? Why does it look the way it does?
 - What would a new team member need to understand in their first week?
 - What do people outside your team consistently misunderstand about your domain?
#### Section B: Requirements and Standards
 - What does "done" look like for typical work items?
 - What's the definition of quality in your context?
 - What are the non-negotiable requirements?
 - What are the "nice to haves" vs "must haves"?
 - What approval processes exist and who's involved?
 - What documentation standards do you follow?
 - What testing/validation is required before shipping?
 - What are the common acceptance criteria patterns?
 - What gets work items rejected or sent back?
 - What does your QA/review process actually check?
#### Section C: Technical Context
 - What's the tech stack?
 - What integrations or dependencies exist?
 - What are the known technical constraints?
 - What's fragile or risky to change?
 - What environments exist?
 - What data is involved and where does it live?
 - What are the common technical gotchas?
 - What's the deployment/release process?
 - What monitoring or observability exists?
 - What technical debt are you carrying?
#### Section D: Patterns and Anti-Patterns
 - What's a well-written work item in your context? (give an example)
 - What's a badly-written one? Why did it fail?
 - What patterns keep recurring?
 - What mistakes do people make repeatedly?
 - What shortcuts exist that people should know about?
 - What "obvious" solutions don't actually work and why?
 - What tribal knowledge exists that isn't documented?
 - What questions do new people always ask?
 - What do you wish someone had told you when you started?
 - What's the "right way" vs. what actually happens?
#### Section E: People and Process
 - Who needs to be involved in what types of decisions?
 - Who has context that others lack?
 - What communication norms exist?
 - What meetings matter and what do they accomplish?
 - What's the escalation path when things go wrong?
 - Who are the bottlenecks and why?
 - What politics or sensitivities should people be aware of?
 - What's the feedback loop for completed work?
 - How do priorities get set and changed?
 - What do you personally know that your team doesn't? Tier 2: Knowledge Composition (50 questions)
#### Section F: Current AI Usage
 - What AI tools do you currently use?
 - What do you use them for?
 - What works well? What outputs do you actually use?
 - What doesn't work? What do you always have to fix?
 - What context do you repeatedly explain to AI?
 - What do you copy-paste into prompts frequently?
 - What prompts do you reuse vs. write fresh?
 - How much back-and-forth does it take to get useful output?
 - What would "AI understands my context" look like?
 - What's the highest-value task AI could help with if it had full context?
#### Section G: Role and Identity
 - What's your role? What are you responsible for?
 - What decisions do you make vs. defer?
 - What's your deep expertise?
 - What's your perspective on how things should be done?
 - What standards do you hold yourself to?
 - What tone/style do you communicate in?
 - What are your non-negotiables?
 - What do you want AI to assume about you?
 - What should AI never assume about you?
 - If AI were your assistant, what would a good one know?
#### Section H: Output Standards
 - What does good output look like? (give an example)
 - What format do you prefer?
 - What level of detail is right?
 - What terminology should AI use or avoid?
 - What common AI outputs do you always fix?
 - What would make AI output copy-paste ready?
 - What's the review process for AI-generated content?
 - What gets rejected and why?
 - What style guides apply?
 - How do you measure whether AI output was useful?
#### Section I: Task Patterns
 - What types of tasks do you repeat weekly?
 - For each: what's the input? What's the expected output?
 - What context does each task type require?
 - What are the common variations?
 - What's the workflow from request to completion?
 - What templates or structures do you use?
 - What checklists or validation steps exist?
 - What's the 80/20? (20% of tasks that are 80% of work)
 - What tasks could be automated vs. need judgment?
 - What's the handoff to the next step?
#### Section J: Context Composition
 - Which Tier 1 notes are essential for AI?
 - Which are "always relevant" vs "sometimes relevant"?
 - What's the hierarchy?
 - What should be included by default?
 - What's the right chunk size?
 - How should notes be ordered for comprehension?
 - What links reveal critical related context?
 - What's the minimal viable context?
 - What's the maximal context?
 - How do you know when the context file is "done enough"?
### The context file template Once you've answered the questions, compose them into this format. This is the file you paste into every AI conversation:
```
# [Your Name]'s Context File

## Who I Am
[Role, expertise, standards -- from Section G]

## My Domain
[Project context, constraints, stakeholders -- from Tier 1]

## How I Work
[Task patterns, workflows, output standards -- from Sections H/I]

## What Good Looks Like
[Examples, format preferences, terminology -- from Section H]

## AI Instructions
[What to assume, what to avoid, communication style -- from Section G]
```
How to test it Use your context file on three real tasks. After each one, note: how much correction was needed? What context was missing? What was noise? Update the file. By the third iteration, you should need less than 20% correction -- down from 50%+ without the file.
### Why links matter If you use a linked note system (Obsidian, Roam, Notion with links), the connections between notes become useful:

| Tags (flat search)  || Links (graph traversal)  |

| "Show me notes tagged #requirements"  || "Show me requirements AND everything connected to them"  |

| You get what you asked for  || You get what you asked for + related context you forgot  |

| Good for known queries  || Good for discovery  |

The link structure is the advantage. When your notes eventually feed a retrieval system, links let it pull in connected context that keyword search would miss. Section 05
## Reference
### Pre-prompt checklist I run through this before writing any non-trivial prompt:

| Check  || Pattern  || Add if...  |

| Would a role help?  || Persona  || Task needs domain expertise  |

| Can I show examples?  || Few-shot  || Easier to show than explain  |

| Does format matter?  || Output format  || Need consistent/parseable output  |

| Is reasoning complex?  || Chain-of-Thought  || Multi-step analysis or debugging  |

| Multiple phases with dependencies?  || ReAct  || Need validation between steps  |

| Real tradeoff to evaluate?  || Tree of Thoughts  || Multiple valid approaches  |

### Copy-paste templates Debug code
```
You are a senior [language] developer.

Debug this error step by step:
1. Identify the root cause
2. Explain why it happens
3. Suggest the fix
4. Explain why the fix works

Error message:
[paste error]

Relevant code:
[paste code]

Environment: [language version, framework, OS]
```
Code review
```
You are a senior code reviewer focused on [maintainability/security/performance].

Review this code against:
- Error handling completeness
- Test coverage gaps
- Naming and style conventions
- Security concerns

Severity levels: MUST FIX / SHOULD FIX / NIT

Example:
 MUST FIX (line 42): Missing null check.
 userService.getUser() can return null but is
 dereferenced without guard.

Code to review:
[paste code]
```
Write tests
```
You are a test engineer specializing in [framework].

Write tests for this code following these patterns:

Example test structure:
test('should [expected behavior]', () => {
 // Arrange: [setup]
 // Act: [execution]
 // Assert: [verification]
});

Requirements:
- Cover happy path and at least 3 edge cases
- Include error scenarios
- Use descriptive test names

Code to test:
[paste code]
```
Architecture decision
```
You are a solutions architect.

I need to decide between [option A] and [option B]
for [specific use case].

Evaluate each option:

## Option A: [name]
- Pros: [list]
- Cons: [list]
- Effort: [hours/days]
- Risk: [Low/Medium/High]
- Maintenance burden: [description]

## Option B: [name]
[same structure]

Context:
- Team size: [N]
- Timeline: [deadline]
- Existing stack: [tech]
- Scale requirements: [metrics]

Recommend the best option with specific rationale
given my constraints.
```
Migration task
```
You are an expert [technology] migration engineer.

Migrate this code using these transformation rules:

Example:
 Before: [old pattern]
 After:  [new pattern]

Example:
 Before: [old pattern]
 After:  [new pattern]

Execute in phases:

Phase 1: [what to change first]
 Validate: [how to verify]

Phase 2: [what to change next]
 Validate: [how to verify]

Constraints:
- Preserve all existing behavior
- Do NOT change [specific things to protect]
- Must pass [existing tests/checks]

Code to migrate:
[paste code]
```
Spec-driven workflow (3 files) **File 1: knowledge-base.md **
```
# Project Knowledge Base

## Domain Concepts
- [Term]: [Definition]
- [Term]: [Definition]

## Architectural Principles
- [Pattern]: [Rationale]
- Anti-patterns: [What to avoid]

## Constraints
- Technical: [list]
- Regulatory: [list]
- Organizational: [list]

## Past Decisions
- [Decision]: [Rationale] (Date: [when])
```

**File 2: specification.md **
```
# Feature Specification: [Name]

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2

## Acceptance Criteria
- [ ] Criterion 1 (testable)
- [ ] Criterion 2 (testable)

## Edge Cases
- [Case 1]: [How to handle]
- [Case 2]: [How to handle]

## Out of Scope
- [What we're NOT doing]
```

**File 3: implementation-plan.md **
```
# Implementation Plan

## Phase 1: [Name]
THINK: [What must be true before we start?]
ACT:   [Tasks]
CHECK: [Validation]
Effort: [Estimate]

## Phase 2: [Name]
THINK: [What did Phase 1 give us?]
ACT:   [Tasks]
CHECK: [Validation]
Depends on: Phase 1

## Rollback Plan
If any phase fails: [recovery steps]
```

**Usage: **Load files 1, 2, 3 into the AI in that order. Then say: "Execute the implementation plan, following the knowledge base constraints and specification requirements."
### Tool evaluation New AI tools show up constantly. These are the questions I ask:

| Question  || Why it matters  |

| How old is it?  || Longer track record = more failure learning  |

| Who uses it beyond the creators?  || Multi-company adoption is a stronger signal than star counts  |

| Does it work across platforms?  || Vendor lock-in is expensive to undo  |

| What problem does it actually solve?  || Distinguish genuinely new capability from repackaging  |

| What's the exit cost?  || Time to learn, data portability, switching pain  |

| Maturity  || Track Record  || Action  || Examples  |

| Tier 1  || 10+ years, multi-company  || Adopt  || ADRs, few-shot, chain-of-thought, persona  |

| Tier 2  || 1-3 years, growing adoption  || Adopt with monitoring  || .github/copilot-instructions.md, ReAct, Cursor  |

| Tier 3  || Months, limited evidence  || Experiment cautiously  || GitHub spec-kit, Kiro, Tessl  |

### Common mistakes Mistake
```
Fix this code
```

No context, no constraints, no format. The AI guesses at everything. Fix
```
You are a Python expert.
This code throws a KeyError
on line 10 when the user dict
is missing the 'email' field.
Explain the root cause and
suggest a fix that handles
missing keys gracefully.
```
Mistake Over-specifying a persona with a paragraph of background. "You are an expert who has worked for 20 years in enterprise systems across multiple Fortune 500 companies and has deep knowledge of..." Fix
```
You are a senior database
performance engineer.
```

One line. The model doesn't need a resume. Mistake Providing 10 few-shot examples when 2-3 would establish the pattern. Fix 2-3 representative examples. Cover the main case and one edge case. Diminishing returns hit fast.
### Sources

| Paper  || Pattern  || Citation  |

| Prompt Pattern Catalog  || Persona, Few-shot, Template, 16+ patterns  || White et al. (2023) -- arXiv 2302.11382  |

| Few-Shot Learners  || Few-shot prompting  || Brown et al. (2020) -- arXiv 2005.14165  |

| Chain-of-Thought  || Step-by-step reasoning  || Wei et al. (2022) -- arXiv 2201.11903  |

| ReAct  || Reasoning + Acting loops  || Yao et al. (2022)  |

| Tree of Thoughts  || Multi-branch evaluation  || Yao et al. (2023)  |

| Architecture Decision Records  || Systematic prompt organization  || Nygard (2011)  |

Joey Lopez · 2026 · [jrlopez.dev ]()
[← jrlopez.dev ]()· [advanced patterns → ]()· [guardrails → ]()