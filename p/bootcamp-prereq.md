---
title: "Bootcamp Prereq"
description: "15-minute self-study before the live session."
author: "Joey Lopez"
date: "2026-01-10"
tags: ["prompting", "teaching", "reference"]
atom_id: 8
source_html: "bootcamp-prereq.html"
url: "https://jrlopez.dev/p/bootcamp-prereq.html"
generated: true
---

[← home ]()[bootcamp ]()[decision matrix ]()[personas ]()[templates ]()[checklist ]()
# Participant Materials Reference cards, demo personas, and workflow templates for the Prompt Engineering Bootcamp Joey Lopez · Prompt Engineering Bootcamp [decision matrix ]()[personas ]()[templates ]()[research ]()[checklist ]()Frameworks
## Three Approaches Decision Matrix

| When to Use  || ADRs + Config  || Structured Files  || Tool-Assisted  |

| **Team Size ** || Any size  || 5–15 people  || Committed to one tool  |

| **Task Type ** || Simple–Medium  || Complex, repeated  || IDE-integrated work  |

| **Maturity ** || Proven (Tier 1)  || Experimental (Tier 3)  || Varies (Tier 2–3)  |

| **Maintenance ** || Low  || Medium  || Low (tool manages)  |

| **Examples ** || .github/copilot-instructions.md || Priority Builder (325 lines)  || Windsurf workflows  |

| **Time to Setup ** || 15 minutes  || 1–2 hours  || 30 minutes  |

| **Best For ** || Most teams  || Learning, complex tasks  || Platform-specific teams  |

## Foundational Patterns Reference

| Pattern  || Template  || When to Use  |

| **Persona ** || "You are an expert [role] with [expertise]..."  || Need specialized knowledge  |

| **Few-shot ** || "Example 1: Input → Output"  || Want consistent format  |

| **Template ** || "Respond in this format: [structure]"  || Need structured output  |

| **Chain-of-Thought ** || "Show your reasoning step by step"  || Complex problem solving  |

## Advanced Patterns Reference

| Pattern  || Structure  || When to Use  |

| **ReAct ** || Think → Act → Observe → Think...  || Multi-step tasks with validation  |

| **Tree of Thoughts ** || Generate options → Evaluate → Choose  || Decision points with tradeoffs  |

| **Spec-Kit ** || knowledge-base → specification → implementation  || Complex, repeated tasks  |

Practice Material
## Demo Personas for Safe Practice Use these fictional profiles during exercises to avoid putting real client or personal information into AI tools.
#### Persona A — Delivery Lead, Financial Services
 - **Experience: **8 years, manages 12-person team
 - **Current Project: **Digital transformation for regional bank ($2.3M, 18 months)
 - **Accomplishments: **Delivered 3 weeks early, NPS 6.5→8.2, team engagement 4.1/5.0
 - **Skills: **Agile/Scrum Master, AWS Cloud Practitioner, stakeholder management Best for: Client Value Creation or Great Place to Work priority exercises
#### Persona B — Tech Lead, Banking Automation
 - **Experience: **5 years, AI/ML specialist
 - **Current Project: **Banking automation (1,500 datasets processed, 6x speed improvement)
 - **Accomplishments: **4 POC demos to Senior Managers, 1 advanced to $800K pitch
 - **Skills: **Python, AI tools (Copilot, Windsurf), spec-driven development Best for: AI Enablement or Client Value Creation exercises
#### Persona C — Associate Manager, Digital Strategy
 - **Experience: **6 years, MBA hire, manages 5 people
 - **Current Project: **Organizational redesign ($12M savings, 85% adoption rate)
 - **Accomplishments: **Client satisfaction 9.1/10, innovation award, board presentation
 - **Skills: **Change management, AI workforce planning, thought leadership Best for: Great Place to Work or Community exercises Sample Job Descriptions
## Jobs for Interview Prep Exercises
#### Job A — Senior Manager, AI Strategy
 - **Company: **Fortune 500 Financial Services
 - **Role: **Develop enterprise AI strategy and lead client-facing transformations
 - **Requirements: **8+ years consulting, 3+ in AI/digital, $2M+ engagement leadership
 - **Team: **6 direct reports, 20+ indirect
#### Job B — Principal Consultant, Banking Technology
 - **Company: **Big 4 Consulting Firm
 - **Role: **Lead core banking modernization and cloud-native architecture projects
 - **Requirements: **7+ years banking technology, cloud expertise, CTO/CIO relationships
 - **Team: **Lead 10–15 person engagement teams
#### Job C — Director, Digital Transformation
 - **Company: **Fortune 100 Retail Company
 - **Role: **Internal transformation leader for AI-enabled operations
 - **Requirements: **10+ years transformation experience, P&L responsibility, executive presence
 - **Team: **Multiple cross-functional teams (50+ people) Templates
## Spec-Kit Workflow Templates
### knowledge-base.md
```
# Interview Knowledge Base

## STAR Method Framework
- **Situation**: Context and background
- **Task**: What needed to be accomplished
- **Action**: Steps you took (focus on YOUR actions)
- **Result**: Outcome and impact (quantified when possible)

## Common Senior Manager Questions
1. "Tell me about a time you led a complex project"
2. "How do you handle competing stakeholder priorities?"
3. "Describe your approach to building teams"
4. "Give an example of driving strategic change"
5. "What's your experience with digital/AI transformation?"

## Positioning Strategy Options
- **Technical Expert**: Emphasize deep functional skills
- **Strategic Leader**: Focus on business impact and vision
- **Balanced Bridge**: Demonstrate both technical depth and business acumen
```

### specification.md
```
# Interview Specification

## Target Role Details
- **Position**: [Role title]
- **Company**: [Company name and industry]
- **Key Requirements**: [Must-have qualifications]
- **Team/Scope**: [Management responsibilities]

## Candidate Background
- **Current Role**: [Your position and experience]
- **Key Projects**: [2-3 most relevant projects]
- **Notable Achievements**: [Quantified results]
- **Skills Gap Analysis**: [What you're missing vs what you have]

## Success Criteria
- [What good positioning looks like for this role]
- [Key messages to convey]
- [Questions to ask that show strategic thinking]
```

### implementation-plan.md
```
# Interview Implementation Plan

## Phase 1: ReAct Analysis
**THINK**: What positioning strategy best fits this role + my background?
**ACT**: Map my experience to role requirements systematically
**OBSERVE**: What gaps/strengths emerge from this analysis?
**THINK**: How can I position gaps as learning opportunities?
**ACT**: Develop core narrative connecting past experience → role requirements

## Phase 2: Tree of Thoughts Strategy
**Option A**: [First positioning approach]
- Pros: [What works well]
- Cons: [Potential weaknesses]
- Risk Level: [High/Medium/Low]

**Option B**: [Second positioning approach]
- Pros: [What works well]
- Cons: [Potential weaknesses]
- Risk Level: [High/Medium/Low]

**Option C**: [Third positioning approach]
- Pros: [What works well]
- Cons: [Potential weaknesses]
- Risk Level: [High/Medium/Low]

**Selected Strategy**: [Chosen approach with rationale]

## Phase 3: Materials Generation
- One-page positioning summary
- 5 prepared STAR examples
- Strategic questions to ask
- Practice plan for delivery
```
Research
## Research References
 - **White et al. (2023) **— "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT" · arXiv 2302.11382
Foundational patterns: Persona, Few-shot, Template, Chain-of-Thought
 - **Yao et al. (2022) **— "ReAct: Synergizing Reasoning and Acting in Language Models" · arXiv 2210.03629
Think → Act → Observe pattern for complex reasoning
 - **Yao et al. (2023) **— "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" · arXiv 2305.10601
Generate → Evaluate → Choose pattern for decision making Completion
## Workshop Completion Checklist
### Session 1 Objectives
 - I can explain when to use ADRs vs Structured Files vs Tool-Assisted approaches
 - I can identify Persona, Few-shot, Template, Chain-of-Thought patterns in prompts
 - I generated realistic priorities using the Priority Builder methodology
 - I understand the difference between systematic and ad-hoc prompting
### Session 2 Objectives
 - I can execute ReAct analysis (Think → Act → Observe) for complex problems
 - I can use Tree of Thoughts to evaluate multiple strategies
 - I built complete interview preparation materials using the 4-file workflow
 - I see how the same patterns scale across business and technical domains
### Action Items
 - Apply ReAct pattern to one complex work decision this week
 - Create a spec-kit workflow for a task I do repeatedly
 - Evaluate new AI tools using the Tier Framework
 - Share the Three Approaches framework with my team Joey Lopez · 2026 · [jrlopez.dev ]()
[← home ]()· [bootcamp overview ]()· [session 1 → ]()· [session 2 → ]()· [quick reference → ]()· [facilitator guide → ]()[.md ]()