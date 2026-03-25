---
title: "Prompts Are Programs"
description: "Composition cheat sheet. Load/Chain/Compose operators."
author: "Joey Lopez"
date: "2025-11-20"
tags: ["methodology", "reference", "template"]
atom_id: 13
source_html: "prompt-cheatsheet.html"
url: "https://jrlopez.dev/p/prompt-cheatsheet.html"
generated: true
---

[jrlopez.dev ]()[Formula ]()[Attention ]()[Density ]()[Operations ]()[Structure ]()[Patterns ]()[Persistence ]()[Reference ]()[Mistakes ]()
# Prompts Are Programs A composition cheat sheet. Attention positioning, token density, core operations, and every pattern with citations. Joey Lopez [Attention ]()[Operations ]()[Patterns ]()Section 01
## The Formula Every prompt you've ever written follows this structure. Template defines *how *to think. Context defines *what *to think about. Output is the novel result. Template (static)  + Context (dynamic) = Output (novel)
  ↓                    ↓                   ↓
How to think      What to think about   Result for THIS context This isn't metaphorical. It's literal. The template is reusable—you can apply it to any context. The context is unique to this instance. The output is only possible because both exist together. Core Insight Every prompt you've ever written is an instance of this formula. Template + Context = Output. Reuse templates across contexts. Never mix them. Section 02
## Where Attention Falls Language models don't distribute attention equally. Transformer architectures have positional bias: top and bottom get more focus. Middle content—even if critical—gets statistically less attention. ┌─────────────────────────────────┐
│ TOP: Critical instructions      │ ← HIGH attention (primacy)
│ - Role, constraints, "never X"  │
├─────────────────────────────────┤
│ MIDDLE: Reference material      │ ← LOWER attention
│ - Code, data, examples          │
├─────────────────────────────────┤
│ BOTTOM: Task + output format    │ ← HIGH attention (recency)
│ - Specific ask, reminders       │
└─────────────────────────────────┘ **Sandwich technique: **Put critical constraints at TOP and BOTTOM. Never bury your most important instruction in the middle, no matter how well you explain it. Warning If your critical instruction is in the middle, the model is statistically less likely to follow it. This isn't a design choice—it's an artifact of positional encoding in transformers. **Citation: **Liu et al. (2023) *Lost in the Middle: How Language Models Use Long Contexts *arXiv:2307.03172 Section 03
## Token Density Whitespace, prose, and formatting all cost tokens. The same idea expressed densely uses 3-5x fewer tokens. Denser tokens = more context available for the model to use.

| Format  || Density  || Best For  |

| Pseudocode  || Highest  || Technical specs  |

| Collapsed JSON  || Very High  || Tabular data to LLM  |

| XML  || High  || Structured instructions  |

| YAML  || Medium  || Human-readable config  |

| Prose  || Low  || Explanations  |

| Formatted JSON  || Lower  || Pretty-printed output  |

**Example: **Dense (15 tokens)
```
def get_user(id: int) -> User:
   """Cache 5min, raise NotFound"""
```
Sparse (45 tokens)
```
The get_user function accepts an integer ID parameter
and returns a User object. Results are cached for 5
minutes. Raises NotFound if the user doesn't exist.
```
Try It Take your last prompt. Rewrite the specification section as pseudocode instead of prose. Count how many tokens you save. Share the ratio with a colleague. Section 04
## Load, Chain, Compose There are only three things you can do with a prompt. Everything else is a combination of these three operations.
### 1. Load Bring artifacts into context—files, git status, command output, external data.
```
<context>
 <file path="./src/auth.py"/>
 <command>!`git status --short`</command>
</context>
```

### 2. Chain Output of step A becomes input to step B. Preserve state across steps.
```
Step 1: Analyze requirements → requirements.md
Step 2: Load requirements.md → Generate plan → plan.md
Step 3: Load plan.md → Implement with full context
```

### 3. Compose Combine a template with context to produce a specialized output.
```
Template: "Review code for $CRITERIA"
Context:  CRITERIA=security, FILE=auth.py
Output:   Security review of auth.py
```
Core Insight These are the only three things you can do with a prompt. Everything else—chaining, few-shot, meta-prompting—is a combination of Load, Chain, and Compose. Section 05
## XML Structure XML tags create clear boundaries between objective, context, requirements, constraints, output, and verification. The model respects structured boundaries more reliably than prose.
### 6-Tag Pattern
```
<objective>What and why</objective>
<context>Background, files to load</context>
<requirements>Specific instructions</requirements>
<constraints>What to avoid and WHY</constraints>
<output>Where to save, format</output>
<verification>How to confirm success</verification>
```

### Tag Selection by Complexity

| Task Type  || Include Tags  |

| Simple  || objective, output, verification  |

| Complex  || Add context, constraints  |

| Pattern demo  || Add examples, before/after  |

| Security risk  || Add security_checklist  |

### Full Template
```
<objective>
Refactor the authentication module to use industry-standard bcrypt
instead of custom hashing, improving security and maintainability.
</objective>

<context>
<file path="./src/auth.py"/>
<file path="./tests/test_auth.py"/>
<current_password_hash>custom_sha256 with salt rotation every 30 days</current_password_hash>
</context>

<requirements>
1. Replace custom hash with bcrypt
2. Maintain backward compatibility for existing hashes
3. All existing tests must pass
4. New tests for bcrypt edge cases
</requirements>

<constraints>
- No new external dependencies (bcrypt must already be in requirements)
- Cost factor must be ≥12
- Never log passwords, hashes, or salt
- Migration path for existing users
</constraints>

<output>
Refactored auth.py with clear comments at hash/verify boundaries.
Updated test_auth.py with new test cases. Provide migration guide.
</output>

<verification>
All tests pass, including new bcrypt tests.
Manual check: old hashes still verify, new hashes use bcrypt.
No new secrets in logs.
</verification>
```
Section 06
## The Pattern Catalog These are the patterns that work. Not because they're trendy—because they're grounded in how transformers process language.
### Foundational Patterns

| Pattern  || Template  || When  |

| **Persona ** || "You are an expert [role] with [skills]..."  || Every prompt. Anchors behavior.  |

| **Few-Shot ** || 2-3 input → output examples  || Complex output format or rare patterns.  |

| **Template ** || "Respond in this format: [structure]"  || When output structure is critical.  |

| **Chain-of-Thought ** || "Think step by step before answering"  || Multi-step reasoning, math, logic.  |

### Advanced Patterns
#### ReAct (Reasoning + Action)
```
THINK: What should I do?
ACT: Do specific action
OBSERVE: Check result
→ Repeat until done
```

**Citation: **Yao et al. (2022) *ReAct: Synergizing Reasoning and Acting in Language Models *arXiv:2210.03629
#### Tree of Thoughts
```
1. Generate 3 approaches
2. Evaluate pros/cons each
3. Choose best, execute
```

**Citation: **Yao et al. (2023) *Tree of Thoughts: Deliberate Problem Solving with Large Language Models *arXiv:2305.10601
#### Meta-Prompting Use AI to generate prompts for other AI to execute. Separates analysis from execution—one model does clarification, another does the work with fresh context.
```
You (vague idea) → AI #1 (generates detailed prompt) → AI #2 (executes with full attention)
```

**Why it works: **AI #1 asks clarifying questions, adds structure, defines success criteria. AI #2 gets clean, specific instructions with full attention. No context wasted on negotiation. Pattern Insight Persona + Few-Shot should be in every prompt. Use Chain-of-Thought for reasoning. Use ReAct for iteration. Use Meta-Prompting when one model can't hold both the goal and the execution strategy.
### Citations
 - Wei et al. (2022) *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models *arXiv:2201.11903
 - White et al. (2023) *A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT *arXiv:2302.11382 Section 07
## Making Context Survive Context windows fill up. Conversations end. Projects span weeks. These three files are how you maintain coherence across boundaries.
### Spec Folder Pattern
```
spec/
├── KNOWLEDGE.md   # WHY - Decisions, constraints, patterns
├── SPEC.md        # WHAT - Requirements, acceptance criteria
└── PLAN.md        # HOW - Phases, tasks, verification
```

### Surgical Loading Load based on what you're doing, not everything at once:

| Task  || Load This  || Why  |

| Understanding constraints  || KNOWLEDGE.md only  || Focus on why, not what or how  |

| Checking requirements  || SPEC.md only  || Verify acceptance criteria  |

| Executing next step  || PLAN.md only  || Get unblocked, don't re-design  |

| Planning a phase  || SPEC.md + KNOWLEDGE.md  || Requirements + constraints  |

Warning Never load all three at once. It wastes context on irrelevant information. You're optimizing for attention—load only what this step needs.
### Context Handoff Template
```
<original_task>
What was requested at the start
</original_task>

<work_completed>
Files created/modified, decisions made, blockers resolved
</work_completed>

<work_remaining>
Specific next tasks with file paths
</work_remaining>

<attempted_approaches>
What failed and why - avoid repeating mistakes
</attempted_approaches>

<critical_context>
Gotchas, assumptions, constraints discovered in the work
</critical_context>

<current_state>
What's finalized vs still draft. Which files are safe to change.
</current_state>
```

Save this as HANDOFF.mdor CONTEXT.md. Load it at the start of your next session. Forward Link This folder structure isn't arbitrary. It's a dependency lattice. Knowledge informs Spec. Spec informs Plan. Plan refers back to both. This is Lattice-Driven Development. Section 08
## Quick Reference Bookmark this section. Use these tables every time you write a prompt.
### Attention Positioning

| Position  || Put Here  || Why  |

| Top  || Role, constraints, "never X"  || Primacy bias  |

| Middle  || Code, data, examples  || Reference material  |

| Bottom  || Task, output format, reminders  || Recency bias  |

### Core Operations

| Operation  || What  || Example  |

| Load  || Bring into context  || <file path="./auth.py"/>  |

| Chain  || Output → Input  || plan.md → implementation  |

| Compose  || Template + Context  || "Review $FILE for $CRITERIA"  |

### Token Optimization

| Do  || Don't  |

| Pseudocode  || Verbose prose  |

| Collapsed JSON  || Formatted JSON  |

| XML tags  || Markdown headings  |

| TOON for arrays  || Nested JSON  |

### Patterns to Use

| Pattern  || When  |

| Persona + Few-shot  || Every prompt  |

| Chain-of-Thought  || Complex reasoning  |

| ReAct  || Multi-step with validation  |

| Tree of Thoughts  || Trade-off decisions  |

| Meta-Prompting  || AI generates prompts  |

| Sandwich  || Critical constraints  |

### Persistence Files

| File  || Contains  |

| KNOWLEDGE.md  || Why (decisions, constraints)  |

| SPEC.md  || What (requirements, criteria)  |

| PLAN.md  || How (tasks, phases)  |

| CONTEXT.md  || State (handoff, current progress)  |

Section 09
## Common Mistakes These happen in almost every project. Learn to spot them early.

| Wrong  || Right  || Why  |

| Load entire repo into prompt  || Load only what this step needs  || Wastes context, dilutes attention on relevant code  |

| "Make it better"  || "Refactor X to use Y pattern"  || Vague instructions breed vague outputs  |

| Analyze + fix in one prompt  || Analyze → report → fresh context → fix  || Separate concerns let model focus on one thing  |

| Bury critical instruction in middle  || Put at top AND bottom (sandwich)  || Positional attention bias; recency + primacy  |

| Prose for specs  || Pseudocode or XML  || Dense is better; whitespace costs tokens  |

| Load KNOWLEDGE + SPEC + PLAN together  || Surgical load: pick one or two per step  || Irrelevant files waste context window  |

Try It Pick your last 3 prompts. Check each against this table. Did you make any of these mistakes? Rewrite one to fix it. Share the before/after with a colleague. Joey Lopez · 2026 · [jrlopez.dev ]()
[← jrlopez.dev ]()· [← guardrails ]()· [foundational patterns → ]()