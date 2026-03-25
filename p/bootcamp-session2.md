---
title: "Session 2 — Advanced"
description: "ReAct, Tree of Thoughts, spec-kit, interview prep."
author: "Joey Lopez"
date: "2026-01-22"
tags: ["workshop", "prompting", "teaching"]
atom_id: 10
source_html: "bootcamp-session2.html"
url: "https://jrlopez.dev/p/bootcamp-session2.html"
generated: true
---

[← home ]()[bootcamp ]()[recap ]()[advanced patterns ]()[spec-kit ]()[exercises ]()[java demo ]()[next steps ]()
# Session 2 Advanced Patterns & Complete Workflows — from simple templates to orchestrated systems Joey Lopez · Prompt Engineering Bootcamp · 60 minutes [ReAct ]()[Tree of Thoughts ]()[spec-kit ]()[exercises ]()[java demo ]()Overview
## Session Agenda

| Time  || Activity  || Type  |

| 0–5 min  || Session 1 Recap + Advanced Patterns Overview  || Lecture  |

| 5–10 min  || Spec-Kit Methodology  || Lecture  |

| 10–15 min  || ReAct + Tree of Thoughts  || Lecture  |

| 15–25 min  || Demo: Interview Prep Workflow  || Hands-on  |

| 25–40 min  || Your Turn: Build Interview Materials  || Hands-on  |

| 40–55 min  || Live Java Demo: Spring Migration  || Hands-on  |

| 55–60 min  || Integration + Next Steps  || Lecture  |

Foundation
## Session 1 Recap In Session 1 you built the foundation:
 - **Three Approaches Framework **— ADRs vs Structured Files vs Tool-assisted
 - **Tier Evaluation **— proven vs emerging vs experimental
 - **Four Foundational Patterns **— Persona, Few-shot, Template, Chain-of-Thought
 - **Real application **— Priority Builder with actual deliverables and CSV output Session 2 evolves each of those: simple patterns become orchestrated workflows, single-step tasks become multi-phase reasoning, and the same methodology scales from priorities to interviews to code. Patterns
## Advanced Patterns When a single prompt with four foundational patterns isn't enough for complex, multi-step tasks, two research-backed patterns handle the gap:
### ReAct Pattern From Yao et al. (2022). Designed for tasks that require validation checkpoints between steps — where you can't know the next action until you observe the result of the current one. THINK : Analyze the situation — what's actually being asked?
↓
ACT : Take a specific, concrete action
↓
OBSERVE : Check results — did it work? What changed?
↓
THINK : Next steps based on what you observed
↓
Repeat until task complete **When to use: **Multi-step tasks where each step depends on the previous result. Code migration, gap analysis, systematic positioning strategy.
### Tree of Thoughts From Yao et al. (2023). Designed for decision points where multiple valid approaches exist and the right choice requires explicit evaluation of tradeoffs.
```
1. Generate 3 genuinely different approaches to the problem
2. Evaluate pros/cons/risks of each approach explicitly
3. Choose the best approach with clear rationale
4. Proceed with that choice
```

**When to use: **Any decision point with real tradeoffs. Interview positioning strategy, architecture choices, migration approach selection.
### When Simple Patterns Are Enough
#### Use Foundational Patterns (Session 1)
 - Single-step tasks
 - Well-understood domains
 - Template-driven outputs
 - Quick iterations needed
#### Use Advanced Patterns (Session 2)
 - Multi-step reasoning required
 - Decision points with tradeoffs
 - Complex domain knowledge
 - Audit trail needed
 - Team scalability important **Decision rule: **Use the simplest approach that handles the complexity. Don't reach for ReAct when a good Persona + Template covers it. Methodology
## Spec-Kit 4-File Workflow The spec-kit pattern separates concerns across files so each piece can be reused, updated independently, and understood by teammates without context from your head. File 1 knowledge-base.md Domain expertise. Reusable across tasks. STAR method, positioning options, evaluation criteria. File 2 specification.md This task's specific requirements. Role details, candidate background, gaps and strengths. File 3 implementation-plan.md Execution strategy using ReAct + Tree of Thoughts. Reasoning documented. File 4 execution.md Generated materials — positioning statement, STAR examples, talking points. **Key advantage: **Separation of concerns. knowledge-base.md stays reusable; specification.md is the only file that changes per task; execution.md is throwaway. Exercises
## Exercise: Build Interview Strategy
### Phase 1 — Create specification.md (8 minutes)
 - Start with the provided knowledge-base.md(interview fundamentals, STAR method, positioning options)
 - Select a job from the participant materials (Senior Manager AI Strategy, Principal Consultant Banking, Director Digital Transformation)
 - Pick the same demo persona you used in Session 1 for continuity
 - Document: target role details, your persona's background, key gaps and key strengths
### Phase 2 — Execute implementation-plan.md (7 minutes)
#### ReAct Analysis
```
THINK: What is the biggest gap between my background and this role?
ACT: Map my specific experience to each key requirement
OBSERVE: What positioning angle emerges from this mapping?
THINK: How do I turn gaps into learning narratives?
ACT: Develop core connecting story: past experience → role requirements
```

#### Tree of Thoughts Strategy
```
Option A: Technical Expert
 Pros: Deep credibility, clear differentiation
 Cons: May undersell business acumen, narrow appeal
 Risk: Medium

Option B: Strategic Leader
 Pros: Broad appeal, executive positioning
 Cons: May lack specificity, needs strong evidence
 Risk: Medium

Option C: Balanced Bridge
 Pros: Technical depth + business growth story
 Cons: Harder to articulate concisely
 Risk: Low

Selected: [Your choice with rationale]
```

**Success criteria: **Clear positioning strategy with documented rationale, not just a chosen answer. Technical Demo
## Live Java Demo: Spring Boot Migration Same patterns, technical domain. Spring Boot 2→3 migration involves three types of changes: namespace updates ( javax→ jakarta), annotation modernization, and security configuration updates. The three approaches from Session 1 apply directly:
#### Approach A — ADRs + Config A .github/copilot-instructions.mdthat documents migration standards. Single prompt referencing that document handles most cases.
```
"Following .github/copilot-instructions.md migration standards,
migrate UserController to Spring Boot 3"
```

#### Approach B — Structured Files (with ReAct) A spec/ folder workflow. ReAct pattern in the implementation plan:
```
THINK: Dependencies must be updated before annotations
ACT: Update javax → jakarta imports first
OBSERVE: mvn compile — success, proceed to annotations
THINK: Security config needs modernization next
ACT: Migrate to SecurityFilterChain pattern
```

#### Approach C — Tool-Assisted (Windsurf) 290-line cascade workflow. Built-in validation gates at each step. Tree of Thoughts for security config decision:
 - Option A: Keep current security config (low risk, technical debt remains)
 - Option B: Modernize to SecurityFilterChain (balanced)
 - Option C: Full OAuth2 rewrite (high risk, high reward)
 - **Decision: **Option B — balanced modernization
### Cross-Domain Pattern Recognition The same cognitive patterns appear across all three domains in this workshop:
#### Universal pattern: ReAct
 - **Priorities: **Think what category fits → Act on metrics → Observe quality → Refine
 - **Interview: **Think about gap → Act on positioning → Observe fit → Select strategy
 - **Code: **Think dependencies → Act on imports → Observe compilation → Continue The domain changes. The systematic thinking doesn't. Toolkit
## What You Now Have
#### Evaluation Framework
 - Three Approaches — ADRs vs Structured vs Tool-assisted
 - Tier Assessment — proven vs emerging vs experimental
#### Pattern Library
 - **Foundational: **Persona, Few-shot, Template, Chain-of-Thought
 - **Advanced: **ReAct, Tree of Thoughts, Spec-Kit
### This Week
 - Apply ReAct pattern to one complex work decision
 - Use Tree of Thoughts for your next strategic choice — write out the three options explicitly
 - Create a spec-kit workflow for one task you do repeatedly
### Longer Term
 - Evaluate new AI tools using the Three Approaches and Tier frameworks before adopting
 - Build team templates using proven foundational patterns — document what works
 - Apply systematic thinking across your domain — same patterns, different problems
#### Research Papers
 - White et al. (2023) — Prompt Pattern Catalog · arXiv 2302.11382
 - Yao et al. (2022) — ReAct Pattern · arXiv 2210.03629
 - Yao et al. (2023) — Tree of Thoughts · arXiv 2305.10601 Joey Lopez · 2026 · [jrlopez.dev ]()
[← home ]()· [bootcamp overview ]()· [← session 1 ]()· [participant materials ]()· [quick reference ]()· [facilitator guide ]()