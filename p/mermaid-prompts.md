---
title: "Diagrams as Prompts"
description: "Mermaid diagrams as structured reasoning inputs."
author: "Joey Lopez"
date: "2026-02-10"
tags: ["diagrams", "methodology", "theory"]
atom_id: 14
source_html: "mermaid-prompts.html"
url: "https://jrlopez.dev/p/mermaid-prompts.html"
generated: true
---

[jrlopez.dev ]()[Why Diagrams ]()[Specs ]()[Architecture ]()[Dependencies ]()[Flow ]()[The Pattern ]()[Examples ]()
# Diagrams as Prompts Mermaid diagrams aren't documentation. They're a reasoning tool. Feed yourself a diagram before you delegate work to AI. Joey Lopez [Why Diagrams ]()[Patterns ]()[Real Examples ]()Section 01
## The Problem With Prose Handoffs Prose feels clear when you write it. You're inside your own mental model. But when you hand it to an AI—or a teammate—all of a sudden the ambiguity surfaces. Dependencies weren't explicit. The sequence was wrong. Edge cases were invisible. Here's a prose spec for a simple page build: "Build a page with a nav, hero section, and three cards.
The nav should be sticky and have links to each card.
The cards should appear below the hero.
Make sure everything is responsive." Sounds reasonable, right? But look at what you didn't specify:
 - Does the nav need to be built before the cards?
 - Can the cards be built in parallel, or do they depend on shared tokens?
 - What if the hero depends on the nav's padding?
 - Is responsive a constraint or a suggestion? Now look at the same task as a diagram:
```
graph TD
   T[L0: Tokens] --> N[L1: Nav]
   T --> H[L1: Hero]
   T --> C[L1: Cards]
   N --> S[L2: Structure]
   H --> S
   C --> S
   S --> V[L3: Verify Responsive]
```
graph TD
   T[L0: Tokens] --> N[L1: Nav]
   T --> H[L1: Hero]
   T --> C[L1: Cards]
   N --> S[L2: Structure]
   H --> S
   C --> S
   S --> V[L3: Verify Responsive] The diagram forces you to answer every question *before *you delegate. You see the dependencies. You see the layers. You see the build order. And when you give it to the AI, there's no ambiguity. Core Insight Prose hides structural ambiguity. A diagram forces you to resolve dependencies, sequence, and scope BEFORE the AI starts working. The diagram becomes the specification. Section 02
## Diagrams as Specs A mermaid flowchart replaces a multi-paragraph spec. It's terse, visual, and executable. The AI can read it. You can verify it. And it's version-controlable. Example: A spec-driven workflow for feature development. Mermaid Source
```
graph LR
   K["📋 KNOWLEDGE.md"] --> S["📄 SPEC.md"]
   S --> P["📋 PLAN.md"]
   P --> O["⚙️ OUTPUT"]
   O --> E["✅ EXECUTION"]
   E -->|Iterate| S
```
graph LR
   K["📋 KNOWLEDGE.md"] --> S["📄 SPEC.md"]
   S --> P["📋 PLAN.md"]
   P --> O["⚙️ OUTPUT"]
   O --> E["✅ EXECUTION"]
   E -->|Iterate| S This diagram tells you:
 - Start with what you know (KNOWLEDGE.md)
 - Turn that into a spec (SPEC.md)
 - Turn the spec into a plan (PLAN.md)
 - Execute the plan and verify output
 - If output doesn't match spec, iterate on the spec, not the code Try It Take your next task. Before writing any prose, draw the flowchart first. Give ONLY the flowchart to the AI. No long instructions. Just the diagram. Section 03
## Architecture Handoffs When you need to coordinate multiple services or systems, a sequence diagram or architecture diagram replaces pages of documentation. Example: A three-service architecture with explicit message flow. Mermaid Source
```
sequenceDiagram
   Client->>API: POST /task
   API->>Queue: Enqueue task
   Queue->>Worker: Process task
   Worker->>Database: Save result
   Database->>Queue: Ack
   Queue->>API: Task complete
   API->>Client: Return result
```
sequenceDiagram
   Client->>API: POST /task
   API->>Queue: Enqueue task
   Queue->>Worker: Process task
   Worker->>Database: Save result
   Database->>Queue: Ack
   Queue->>API: Task complete
   API->>Client: Return result Now the AI—and any engineer reading this—knows:
 - The exact message passing order
 - Which services talk to which
 - Where synchronous vs. async boundaries are
 - What happens when a service fails Core Insight The diagram constrains the solution space. An AI given a sequence diagram can't invent new services or change the protocol. The diagram is the contract. Section 04
## Dependency Maps If you can't draw the dependency graph, you don't understand the build order. And if you don't understand the build order, you're gambling that the AI does. Example: A real build dependency graph. Mermaid Source
```
graph TD
   CSS["CSS Tokens"] --> Nav["Nav Component"]
   CSS --> Hero["Hero Component"]
   CSS --> Card["Card Component"]
   Nav --> Page["Page Layout"]
   Hero --> Page
   Card --> Page
   Page --> Test["Integration Tests"]
   JS["JavaScript"] --> Test
   Test --> Build["Production Build"]
```
graph TD
   CSS["CSS Tokens"] --> Nav["Nav Component"]
   CSS --> Hero["Hero Component"]
   CSS --> Card["Card Component"]
   Nav --> Page["Page Layout"]
   Hero --> Page
   Card --> Page
   Page --> Test["Integration Tests"]
   JS["JavaScript"] --> Test
   Test --> Build["Production Build"] This diagram answers:
 - What can be built in parallel? (Nav, Hero, Card all depend only on CSS)
 - What's the critical path? (CSS → Page → Test → Build)
 - What breaks if I skip a step? (You'll see it immediately) Warning If you can't draw the dependency graph, you don't understand the build order. And if you don't understand the build order, you're hoping the AI does. That's not a strategy. Section 05
## Flow Analysis Mermaid flows work for user journeys, data flows, and state machines. They make invisible paths visible. Example: A visitor flow through a teaching site. Mermaid Source
```
graph TD
   L["Landing Page"]
   L --> B["Browse Items"]
   B --> T1["Teaching Page"]
   B --> P["Paper PDF"]
   T1 --> T2["Other Teaching Pages"]
   T1 --> L
   P --> L
   T2 --> L
```
graph TD
   L["Landing Page"]
   L --> B["Browse Items"]
   B --> T1["Teaching Page"]
   B --> P["Paper PDF"]
   T1 --> T2["Other Teaching Pages"]
   T1 --> L
   P --> L
   T2 --> L And a state machine for a task processor: Mermaid Source
```
stateDiagram-v2
   [*] --> Idle
   Idle --> Running: task_enqueued
   Running --> Complete: success
   Running --> Failed: error
   Complete --> [*]
   Failed --> Idle: retry
   Failed --> [*]: max_retries
```
stateDiagram-v2
   [*] --> Idle
   Idle --> Running: task_enqueued
   Running --> Complete: success
   Running --> Failed: error
   Complete --> [*]
   Failed --> Idle: retry
   Failed --> [*]: max_retries Flows expose edge cases you didn't think about. Where can the system get stuck? What transitions are missing? The diagram is the test suite. Section 06
## The Universal Pattern Every time you delegate work to an AI, follow this pattern:
 - **Think. **Don't write prose. Draw a diagram.
 - **Audit. **Does the diagram match your intent? Are there missing edges? Circular dependencies?
 - **Delegate. **Give ONLY the diagram to the AI. No long instructions.
 - **Verify. **Does the output match the diagram? If not, the AI either misread it or the diagram was wrong. This is the contract. The diagram is the spec. Prose is optional. Code is the execution. Core Insight The diagram is the contract between you and the AI. Prose is a suggestion. A diagram is a specification. It has no ambiguity. This pattern works for:
 - Feature specs
 - Build pipelines
 - API contracts
 - Data transformations
 - System architecture
 - User journeys Section 07
## Real Examples Here are three real diagrams I use in practice. Each one replaced pages of documentation.
### Example 1: Site Build Lattice This is a teaching site build. It shows layers of dependencies and which components can be built in parallel. Mermaid Source
```
graph TD
   T["L0: Tokens"] --> N["L1: Nav"]
   T --> H["L1: Hero"]
   T --> C["L1: Cards"]
   N --> S["L2: Structure"]
   H --> S
   C --> S
   S --> V["L3: Verify"]
```
graph TD
   T["L0: Tokens"] --> N["L1: Nav"]
   T --> H["L1: Hero"]
   T --> C["L1: Cards"]
   N --> S["L2: Structure"]
   H --> S
   C --> S
   S --> V["L3: Verify"] **Used for: **Handed this to an AI agent to build the site. The layers made the build order crystal clear. No ambiguity about what blocks what.
### Example 2: Spec-Driven Workflow This is the workflow I follow for every feature: Knowledge → Spec → Plan → Output → Execution. Mermaid Source
```
graph LR
   K["KNOWLEDGE.md"] --> S["SPEC.md"]
   S --> P["PLAN.md"]
   P --> O["OUTPUT"]
   O --> E["EXECUTION"]
```
graph LR
   K["KNOWLEDGE.md"] --> S["SPEC.md"]
   S --> P["PLAN.md"]
   P --> O["OUTPUT"]
   O --> E["EXECUTION"] **Used for: **Pinning this above my terminal. When I'm tempted to jump to code without writing a spec, I see it and stop. The diagram is the guardrail.
### Example 3: Visitor Flow This is a teaching site's user journey. It shows how visitors move through the content and where they can return to the landing page. Mermaid Source
```
graph TD
   L["Landing"]
   L --> B["Browse items"]
   B --> T1["Teaching page"]
   B --> P["Paper PDF"]
   T1 --> T2["Other teaching"]
   T1 --> L
   P --> L
   T2 --> L
```
graph TD
   L["Landing"]
   L --> B["Browse items"]
   B --> T1["Teaching page"]
   B --> P["Paper PDF"]
   T1 --> T2["Other teaching"]
   T1 --> L
   P --> L
   T2 --> L **Used for: **Shared with a designer. They could see exactly how users move through the site without reading a single paragraph of documentation. Joey Lopez · 2026 · [jrlopez.dev ]()
[← jrlopez.dev ]()· [← cheat sheet ]()· [lattice development → ]()