---
title: "AI Learning Hub"
description: "Guided path: why AI → tools → patterns → pick your track."
author: "Joey Lopez"
date: "2026-03-22"
tags: ["prompting", "workshop", "teaching"]
atom_id: 6
source_html: "ai-learning-hub.html"
url: "https://jrlopez.dev/p/ai-learning-hub.html"
generated: true
---

[← home ]()[start here ]()[tracks ]()[tools ]()[sessions ]()[workshop ]()Prompt Engineering & Tooling
# AI Learning Hub Context is everything. Structure gets rewarded. You are the retrieval system. Joey Lopez · Sr. Data Engineer [start here ]()[why AI? ]()[tool landscape ]()[pick your track ]()[sessions ]()4 tracks 5 skills 90 min live + self-paced maintained 2026 Start Here
## Four steps, then you're off Whether you're brand new or have been prompting for a year, this path covers the foundation before branching into role-specific work. 01
#### Why AI? What it actually does well, what changes for your role, and why prompting is closer to programming than talking. [read it here ]()02
#### Pick Your Tool Chat assistant, code completion, AI-native editor, or agentic IDE — don't overthink it, but know the difference. [tool landscape ]()03
#### Learn the Patterns Zero-shot, few-shot, chain-of-thought, ReAct, Tree of Thoughts — foundations and advanced patterns, with a second brain framework. [prompting patterns ]()04
#### Pick Your Role Track Dev, PO/PM, Delivery Lead, Tech Lead, or capstone. Role-specific workflows built on the same underlying patterns. [choose a track ]()Why AI? Why Should I Care?
## Before you learn the patterns, orient yourself Three things worth internalizing before you touch a prompt library or install a tool. What AI actually does well
#### The tasks where it earns its keep
 - Drafting first passes on anything text-shaped (emails, docs, PRDs, summaries)
 - Transforming content — reformatting, translating register, restructuring arguments
 - Recognizing patterns in messy inputs (logs, feedback, transcripts)
 - Writing boilerplate and scaffolding you'd otherwise copy-paste
 - Rubber-ducking your own thinking — externalizing and stress-testing ideas What changes for your role
#### The same tool, different leverage points Developer Specs and test cases arrive faster than code. The bottleneck shifts to review and integration, not generation. PO / PM User stories with Given/When/Then, sprint backlogs, and roadmap rationales in seconds instead of hours. Delivery Lead Risk matrices, status reports, and onboarding plans generated from your notes — you edit, not author. Tech Lead Run parallel architecture evaluations, generate ADRs via Tree of Thoughts, and build metaprompts that amplify your whole team. The mental model shift
#### Prompting is programming A prompt isn't a request. It's a program. The same engineering principles that make code maintainable make prompts effective. In code Database In a prompt *Context *Why it matters What you include determines what the model can retrieve In code Schema In a prompt *Structure *Why it matters Format and constraints shape the output space In code Query / retrieval In a prompt *You *Why it matters You decide what enters the context — that is the skill Tool Landscape
## Four categories of AI tooling Most people start with whatever's available and upgrade when they hit a ceiling. That's the right move. Here's what the categories actually mean.

|  || Chat Assistant  || Code Completion  || AI-Native Editor  || Agentic IDE  |

| What it is  || Conversational interface for open-ended prompting e.g. ChatGPT, Claude.ai, Copilot Chat  || Inline suggestions as you type, trained on code e.g. GitHub Copilot, Tabnine, Codeium  || Editor with deep AI integration — inline editing, codebase awareness e.g. Cursor, Windsurf  || Agent that reads, edits, and runs code autonomously across files e.g. Claude Code, Devin, Copilot Workspace  |

| Best for  || Drafting, explaining, brainstorming, non-code tasks  || Speeding up typing in familiar codebases; boilerplate  || Refactoring, multi-file edits, test generation, codebase Q&A  || Large refactors, new features with specs, automated review loops highest leverage  |

| Primary users  || Everyone — all roles benefit  || Developers (and technically-minded POs/TLs)  || Developers who want more than autocomplete  || Senior devs and tech leads comfortable giving AI significant scope  |

| Context window  || Single conversation; loses context across sessions  || Current file + a few nearby files  || Whole codebase via embeddings or selection significant upgrade  || Repo-wide; can run commands, read logs, write tests maximum scope  |

| Learning curve  || Low — natural language interface start here  || Low-medium — mostly passive until you learn to steer it start here  || Medium — new prompting patterns, composer mode, rules files  || High — requires spec discipline and trust calibration graduate when ready  |

| When to start  || Day one — use it for anything you'd Google  || Week one if you write code regularly  || When you're writing AI-assisted features or doing large refactors  || When you can write a spec that an agent can execute without babysitting  |

Don't overthink tool choice. Start with what's available, graduate when you hit limits. Pick Your Track
## Five role-specific skill files Each track is a complete, production-relevant workflow — not a tutorial. You get a skill file you can actually run. [Developer 💻
#### Developer Second Brain ReAct-driven migrations, refactoring, feature implementation, and systematic debugging with annotated diffs. ]()[PO / PM 📊
#### PO/PM Second Brain User stories with Given/When/Then, sprint backlogs, roadmap prioritization, and executive reporting. ]()[Delivery Lead 📋
#### Delivery Lead Second Brain ABCD priority building, risk matrices, client status reports, and phased onboarding — all system-ready. ]()[Tech Lead 🏗️
#### Tech Lead Second Brain ADRs via Tree of Thoughts, metaprompts for team amplification, spike plans, and .cursorrules generation. ]()[Capstone 🔨
#### Make Skills Turn any repeated weekly task into a structured skill file. Discover, extract the pattern, generate. Every skill is a RAG system. ]()Sessions & Reference
## Materials for the live workshop Self-study first, then the live sessions, then keep the reference cards close. 📋
#### Common Knowledge 15-minute self-study. Complete before the live session to align on foundational concepts and vocabulary. [Prereq materials ]()🎤
#### Session 1 — Patterns & Priority Builder 60 min. Three Approaches Framework, foundational patterns, and a hands-on priority builder exercise. [Session 1 ]()🎯
#### Session 2 — Advanced Patterns & Interview Prep 60 min. ReAct, Tree of Thoughts, and a complete interview preparation workflow using spec-kit methodology. [Session 2 ]()⚡
#### Quick Reference Cards Pattern recognition guide and decision tree for rapid lookup during practice. Printable and screen-friendly. [Quick reference ]()Go Deeper
## When you want more than the workshop covers
#### Advanced Patterns Self-consistency, constitutional AI, chain-of-density, structured generation, and evaluation loops. [prompting-advanced ]()
#### Prompt Cheat Sheet Composition patterns, operator reference, and the scaffolding primitives behind every skill file. [cheat sheet ]()
#### Diagrams as Prompts Using Mermaid diagrams as structured reasoning inputs. Why pictures beat paragraphs for complex specs. [mermaid prompts ]()
#### Lattice-Driven Dev Dependency-ordered development methodology. Build L1 before L2, verify before shipping each layer. [lattice dev ]()Workshop Delivery
## For facilitators Session structure, timing, and materials for running the live workshop. Session flow & facilitator notes ▼
### Session flow — 105 min total 15 min Prereq Self-study before the call 15 min Activation Framing & three intuitions 40 min Role Fork Role-specific deep dive with skill file 20 min Capstone Build your own skill 10 min Close Synthesis & next steps 📚
#### Facilitator Guide v2 Minute-by-minute script, timing notes, failure modes, and contingency plans for delivery. [Facilitator guide ]()👥
#### Participant Materials Decision matrices, demo personas, spec-kit templates, and workshop completion checklist. [Participant materials ]()
### v2 improvements
 - **Faster **— 90 min instead of 120 (still covers more ground)
 - **Role-specific **— four parallel tracks instead of one generic path
 - **Agency **— participants build their own skill file in the capstone
 - **Lower entry friction **— 15-min prereq removes baseline alignment overhead from live time
 - **Production-grounded **— examples drawn from real project patterns, not textbook exercises Joey Lopez · 2026 · [jrlopez.dev ]()· [← home ]()· [guardrails → ]()