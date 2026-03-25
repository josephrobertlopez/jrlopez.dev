---
title: "Quick Reference Cards"
description: "6-card one-pager of all frameworks."
author: "Joey Lopez"
date: "2026-01-20"
tags: ["reference", "prompting", "template"]
atom_id: 11
source_html: "bootcamp-reference.html"
url: "https://jrlopez.dev/p/bootcamp-reference.html"
generated: true
---

[← home ]()[bootcamp ]()[decision matrix ]()[foundational patterns ]()[advanced patterns ]()[taking it forward ]()
# Quick Reference One-page reference for all frameworks, patterns, and workflows from the Prompt Engineering Bootcamp Joey Lopez · Prompt Engineering Bootcamp [decision matrix ]()[foundational patterns ]()[advanced patterns ]()[action plan ]()Card 1
## Three Approaches Decision Matrix

| When your task is...  || Choose this approach  || Example  |

| Simple–Medium complexity  || **ADRs + Config ** || .github/copilot-instructions.md |

| Team uses multiple AI tools  || **ADRs + Config ** || Reference standards document  |

| Complex, repeated tasks  || **Structured Files ** || Priority Builder (325 lines)  |

| Learning prompt engineering  || **Structured Files ** || 4-file interview workflow  |

| Team committed to one IDE  || **Tool-Assisted ** || Windsurf workflows  |

| Want automated guidance  || **Tool-Assisted ** || Platform-integrated prompts  |

Decision Rule Use the simplest approach that handles your complexity level. Card 2
## Foundational Patterns Checklist Before writing any prompt, check for all four patterns:
 - **Persona **— "You are an expert [role] with [specific expertise]..."
 - **Few-shot **— Provide 2–3 example input/output pairs
 - **Template **— "Respond in this format: [structure]"
 - **Chain-of-Thought **— "Show your reasoning step by step" **Quality check: **Does your prompt use all 4 patterns? If not, which one would help most? Card 3
## Advanced Patterns Quick Guide
### ReAct Pattern — multi-step tasks
```
THINK:   Analyze the situation — what is actually needed?
ACT:     Take a specific, concrete action
OBSERVE: Check results — did it work? What changed?
THINK:   Next steps based on what you observed
        (repeat until complete)
```

### Tree of Thoughts — decision points
```
1. Generate 3 genuinely different approaches
2. Evaluate pros/cons/risks of each
3. Choose best approach with explicit rationale
```

### Spec-Kit Workflow — complex tasks
```
knowledge-base.md      Domain expertise (reusable across tasks)
specification.md       This task's specific requirements
implementation-plan.md Execution strategy (ReAct + Tree of Thoughts)
execution.md           Generated output materials
```
Card 4
## Pattern Recognition Quick Test When you see any prompt, identify:
 - What **persona **is established?
 - What **examples **are provided?
 - What **format **is requested?
 - Is **reasoning **required?
#### Good prompt = all 4 patterns visible If you can't find one of the four, the prompt has a gap. Fill it before you run it. Card 5
## Taking This Forward
### This Week
 - Apply ReAct pattern to one complex work decision
 - Use Tree of Thoughts for your next strategic choice
 - Create a spec-kit workflow for a task you do repeatedly
### Longer Term
 - Evaluate new AI tools using the Three Approaches framework
 - Build team templates using foundational patterns
 - Scale systematic thinking across your domain The Core Principle Patterns beat formats. Choose your approach based on team context and task complexity. Card 6
## Research Backing
 - **White et al. (2023) **— Prompt Pattern Catalog · arXiv 2302.11382
Foundational patterns: Persona, Few-shot, Template, Chain-of-Thought
 - **Yao et al. (2022) **— ReAct Pattern · arXiv 2210.03629
Think → Act → Observe for complex reasoning
 - **Yao et al. (2023) **— Tree of Thoughts · arXiv 2305.10601
Generate → Evaluate → Choose for decision making Joey Lopez · 2026 · [jrlopez.dev ]()
[← home ]()· [bootcamp overview ]()· [session 1 ]()· [session 2 ]()· [participant materials ]()· [facilitator guide ]()