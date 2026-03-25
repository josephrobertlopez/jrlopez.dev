---
title: "Session 1 — Patterns"
description: "Three Approaches, foundational patterns, priority builder."
author: "Joey Lopez"
date: "2026-01-15"
tags: ["prompting", "teaching"]
atom_id: 9
source_html: "bootcamp-session1.html"
url: "https://jrlopez.dev/p/bootcamp-session1.html"
generated: true
---

[← home ]()[bootcamp ]()[the problem ]()[three approaches ]()[patterns ]()[exercises ]()[wrap-up ]()
# Session 1 Industry Standards & Real-World Application — from ad-hoc prompting to systematic approaches Joey Lopez · Prompt Engineering Bootcamp · 60 minutes [the problem ]()[three approaches ]()[patterns ]()[exercises ]()Overview
## Session Agenda

| Time  || Activity  || Type  |

| 0–5 min  || Problem & Solution Overview  || Lecture  |

| 5–15 min  || Three Approaches Framework  || Lecture  |

| 15–20 min  || Foundational Patterns  || Lecture  |

| 20–25 min  || Demo: Priority Builder  || Hands-on  |

| 25–45 min  || Your Turn: Build Priorities  || Hands-on  |

| 45–55 min  || Compare: Three Approaches  || Hands-on  |

| 55–60 min  || Wrap & Session 2 Preview  || Lecture  |

The Problem
## Ad-Hoc AI Prompting Doesn't Scale Most professionals use AI tools the same way they'd use a search engine — one-off questions, generic context, inconsistent results. Here's what that looks like:
```
Professional: "Hey AI, help me write my annual priorities"
AI: [generates generic priorities]
Professional: "These don't capture my impact... try again"
AI: [generates different generic priorities]
Professional: "Still missing key metrics..."
```

The problems with ad-hoc prompting:
 - Every prompt starts from scratch — no accumulated knowledge
 - No team knowledge captured — can't share what works
 - Inconsistent results across attempts and team members
 - Successful approaches can't be reused or improved **Key insight: **Patterns matter more than format. Choose based on team needs, not dogma. Framework
## Three Valid Approaches There is no single "right" way to do systematic prompting. Three approaches have emerged in industry practice, each suited to different team contexts:
#### ADRs + Config Architecture Decision Records plus configuration files. Example: .github/copilot-instructions.mdthat any AI tool reads automatically. Best for most teams. Low setup overhead.
#### Structured Files Multi-file workflows: knowledge-base → specification → implementation-plan. Each file has a specific purpose and builds on the previous. Best for complex, repeated tasks and learning.
#### Tool-Assisted Platform-native workflows like Windsurf's cascade system (290 lines). The tool manages context and sequencing automatically. Best for teams committed to one IDE or platform.
### Tier Framework for Evaluation Use this to assess any prompt engineering approach you encounter:
#### Tier 1 — Proven (10+ years) Architecture Decision Records, Few-shot prompting, Chain-of-Thought. Used at scale by Microsoft, AWS, Google, Netflix. These patterns have survived real production use.
#### Tier 2 — Production Ready (1–3 years) .github/copilot-instructions.md, ReAct pattern. Growing enterprise adoption. Reasonably safe to build on.
#### Tier 3 — Experimental (<2 years) Spec-kit workflows, structured prompt files, tool-specific approaches. Interesting and useful, but unproven at scale. Use deliberately. Patterns
## Four Foundational Patterns These patterns are research-backed and appear in all serious prompt engineering work. A well-constructed prompt uses all four. Persona "You are an expert [role] with [specific expertise]..." Establishes the lens the AI uses for all responses. Few-shot Provide 2–3 example input/output pairs before your actual request. Shows the desired format and quality level. Template "Respond in this format: [structure]" Constrains output shape for reuse and consistency. Chain-of-Thought "Show your reasoning step by step before giving the answer." Forces deliberate reasoning, catches errors earlier.
### The 325-Line Priority Builder The Priority Builder Agent prompt uses all four patterns together. It demonstrates what a production-grade prompt looks like vs a quick one-off request:
 - **Persona: **"You are an expert career coach specializing in professional priorities..."
 - **Few-shot: **Built-in priority examples with ABCD reflections showing expected quality
 - **Template: **Structured CSV output plus formatted summaries for direct submission
 - **Chain-of-Thought: **The 20-question ABCD reflection framework that guides analysis The result: persona-driven specificity, structured questioning that ensures completeness, and consistent output format — versus the ad-hoc alternative that generates something generic every time. Exercises
## Hands-On: Build Priorities
### Exercise 1 — Freestyle First (10 minutes) Before using any systematic approach, attempt to create one priority for a demo persona using your normal prompting style.
#### Choose a demo persona
 - **Option A: **Delivery Lead, Financial Services (8 years, team management)
 - **Option B: **Tech Lead, Banking Automation (5 years, AI/ML specialist)
 - **Option C: **Associate Manager, Digital Strategy (6 years, transformation) **Goal: **1 priority in any category with basic reflection. Use your AI tool however you normally would. Notice what's hard: specificity, metrics, avoiding generic language that could apply to anyone.
### Exercise 2 — Priority Builder Template (15 minutes) Now use the complete Priority Builder Agent with a different persona than Exercise 1.
 - Load the 325-line Priority Builder prompt into your AI tool
 - Choose a different persona than the freestyle round
 - Let the agent guide you through its 20-question process — answer as your persona
 - Select a version: Conservative, Balanced, or Aspirational
 - Export the CSV output (ready for submission format) **Success criteria: **Complete ABCD reflections with specific metrics, CSV output ready.
### Exercise 3 — Compare Three Approaches (10 minutes) Same Spring Boot 2→3 migration task, three different approaches. Observe the difference in structure and maintenance overhead — not the result.
#### Approach A — ADRs + Config
```
"Following .github/copilot-instructions.md,
migrate UserController to Spring Boot 3"
```

#### Approach B — Structured Files Load: knowledge-base.md→ specification.md→ implementation-plan.md
#### Approach C — Tool-Assisted Windsurf cascade workflow (290-line systematic methodology with built-in validation steps). Same result, different maintenance overhead. Which fits your team? Wrap-Up
## What You Accomplished
 - Learned the Three Approaches evaluation framework and when each applies
 - Recognized all four foundational patterns in a real 325-line production prompt
 - Generated priorities using a systematic approach vs freestyle
 - Compared structured vs unstructured methodology on the same task
### Cross-Domain Application The patterns you practiced in this session work across domains:
#### Business Applications
 - Strategic planning documents
 - Performance reviews and goal setting
 - Client presentations and proposals
 - Training material development
#### Technical Applications
 - Code migration and refactoring
 - Architecture documentation
 - Troubleshooting workflows
 - System design patterns Same systematic thinking, different domain. Session 2 demonstrates this across the full range.
#### Session 2 Preview
 - **ReAct pattern **(Think → Act → Observe) for multi-step reasoning
 - **Tree of Thoughts **for decision points with real tradeoffs
 - **Interview prep workflow **— 4-file systematic approach
 - **Live technical demo **— Spring Boot migration using same patterns Bring a job description you're interested in, or use the samples in the participant materials. Joey Lopez · 2026 · [jrlopez.dev ]()
[← home ]()· [bootcamp overview ]()· [participant materials ]()· [session 2 → ]()· [quick reference ]()· [facilitator guide ]()[.md ]()