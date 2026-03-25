---
name: make-skills
description: Meta-skill capstone — build your own interrogation-driven AI skill for any repeated task
version: 1.0
---

# Make-Skills Meta-Skill (Capstone)

## Overview

The **Make-Skills** skill is the capstone of Joey's Prompt Engineering Bootcamp v2. It's the moment when participants stop USING skills and start CREATING them.

This skill answers the fundamental question: **"How do you turn your repeated work into a skill that scales?"**

Using three interrogation phases, you'll discover the pattern hidden in your weekly tasks, extract it into a structured skill, and generate a production-ready skill file that you can save and use immediately.

The skill demonstrates all three bootcamp intuitions at the **meta level**:

1. **Context is everything** → The interrogation gathers rich context about YOUR task, YOUR constraints, YOUR audience
2. **Structure gets rewarded** → The output is a properly formatted skill file that an AI (or you) can read and execute
3. **You are the retrieval system** → The skill you build BECOMES a retrieval system for that task — it asks the right questions and assembles answers into structured context

---

## The Capstone Reveal

After you generate your first skill, the skill includes a **reflection section** that shows you what you just built:

> Look at what you just created:
>
> - It **ASKS questions** → that's retrieval (gathering relevant context)
> - It **ASSEMBLES your answers into structured context** → that's augmentation (organizing information)
> - It **FEEDS that context to the AI for generation** → that's generation (producing the output)
>
> **You just built a RAG system.** Every skill is a RAG system.
>
> The AI completing patterns from your context? That's what an LLM does. Why does structured input work better? The model was trained by humans who rewarded that — that's RLHF. You've been doing all three intuitions since the first exercise of the prereq.

---

## Key Capabilities

### 1. Task Discovery Phase
Finds the repeated, valuable work you do weekly and turns it into a skill-able task:

- **Identification**: What task do you repeat at least weekly?
- **Walkthrough**: How do you do it today, step by step?
- **Context Gathering**: What information do you need before you start?
- **Quality Criteria**: What does good output look like? Bad output?
- **Audience**: Who uses what you create?

### 2. Pattern Extraction Phase
Discovers the underlying pattern in your task and maps it to a skill framework:

- **Category Mapping**: Code generation? Document creation? Analysis? Communication? Planning?
- **Context Requirements**: What does this skill always need to know?
- **Question Design**: What should the skill ask the user before generating?
- **Output Structure**: What template ensures consistent, high-quality output?

### 3. Skill Generation Phase
Assembles your answers into a production-ready skill file:

- **SKILL.md Generation**: Properly formatted markdown with metadata, interrogation questions, output specifications
- **Example Interrogation**: A complete worked example showing the skill in action
- **Generated Example Output**: Sample output that participants can reference
- **Integration Notes**: How this skill connects to bootcamp patterns (RAG, ReAct, etc.)

---

## Usage Scenarios

### Scenario A: Repeatable Document Creation
*Sales decks, RFP responses, project briefs, technical specs*

**When to use**: "I create [documents] at least weekly. Each one is different, but the process is the same."

**What you'll get**: A skill that interviews you about the document's purpose, audience, and context — then generates a properly structured template with all sections filled in.

### Scenario B: Code Generation or Migration
*New microservice scaffolding, API contract implementation, database migration planning*

**When to use**: "I build [code structures] repeatedly, always following the same patterns."

**What you'll get**: A skill that asks about your codebase, conventions, and constraints — then generates implementation plans or code stubs with your team's exact patterns.

### Scenario C: Analysis or Decision Support
*Technical architecture reviews, competitive analysis, feasibility assessments, incident post-mortems*

**When to use**: "I analyze [situations] and always produce similar-structured recommendations."

**What you'll get**: A skill that gathers context about the situation — then generates structured analysis with evaluation frameworks and recommendation matrices.

### Scenario D: Communication or Planning
*Meeting agendas, status reports, project proposals, email templates*

**When to use**: "I create [communications] regularly and want them to be more consistent."

**What you'll get**: A skill that asks about the message, audience, and context — then generates well-structured communications with the right tone and completeness.

---

## 3-Phase Workflow

### Phase 1: Task Discovery (15 min)

The skill interrogates you to understand your repeated work:

```
Q1: "What task do you repeat at least weekly at work?"
→ Example: "I create test plans for new features"

Q2: "Walk me through how you do it today, step by step."
→ Step 1: Review feature specification
→ Step 2: Identify test scenarios (happy path, edge cases, error cases)
→ Step 3: Write test cases for each scenario
→ Step 4: Document expected outcomes
→ Step 5: Review with development team

Q3: "What information do you need to gather before you start?"
→ Feature spec, API contracts, existing test data,
→ Known limitations, browser/OS requirements,
→ Performance requirements, security considerations

Q4: "What does GOOD output look like? Bad output?"
→ GOOD: Clear test cases, comprehensive scenarios,
→        prioritized by risk, reproducible steps
→ BAD: Vague scenarios, missing edge cases,
→      unclear expected outcomes, untestable

Q5: "Who is the audience for your output?"
→ Development team reads it to understand testing
→ QA team executes it
→ Project manager uses it to track testing progress
```

### Phase 2: Pattern Extraction (10 min)

The skill identifies the underlying pattern and asks how to structure it:

```
Q6: "Which category best describes your task?
     • Code generation (scaffolding, migrations, implementations)
     • Document creation (decks, specs, proposals, briefs)
     • Analysis/decision (reviews, assessments, comparisons)
     • Communication (emails, reports, announcements)
     • Planning (agendas, roadmaps, schedules)"
→ Category: "Document creation"
   (test plan is a structured document with specific sections)

Q7: "What context does the skill always need to know?
     List 5-7 pieces of information that change every time but are always needed."
→ Feature specification, testing scope,
→ Team's testing standards, environment constraints,
→ Performance/security requirements, timeline,
→ Success criteria for testing

Q8: "What questions should the skill ask the user
     before generating the output?
     (Think: what do you always ask when someone
     hands you a feature to test?)"
→ What's the feature being tested?
→ What are the main user flows?
→ What edge cases matter most?
→ What's the timeline for testing?
→ What environments are available?

Q9: "What structure should the output follow?
     Describe section headings, ordering, format details."
→ ## Test Objectives
→ ## Scope (in-scope, out-of-scope)
→ ## Test Scenarios (matrix: happy path, edge cases, errors)
→ ## Test Cases (step-by-step for each scenario)
→ ## Success Criteria
→ ## Known Limitations
```

### Phase 3: Skill Generation (automatic)

The skill assembles your answers into a complete, formatted skill file:

```markdown
---
name: [generated from your task]
description: [generated from your answers]
version: 1.0
---

# [Your Skill Name]

## Overview
[Generated explanation of what this skill does]

## Key Capabilities
[Generated from Phase 2 answers]

## Usage Scenarios
[Generated categories where this skill applies]

## Structured Interrogation Framework

### Phase 1: [Context gathering]
[Your questions, adapted and refined]

### Phase 2: [Structure definition]
[Your output structure requirements]

## Output Format Specification
[Your template with examples]

## Example: Complete Workflow
[Worked example showing interrogation → output]

## Reflection: What You Just Built
[The RAG explanation]
```

---

## Structured Interrogation Framework

### Phase 1: Task Discovery (5-7 questions)

1. **Weekly Task**: What task do you repeat at least weekly?
2. **Current Process**: Walk me through your steps today (step-by-step)
3. **Input Requirements**: What information do you need before starting?
4. **Quality Definition**: What's GOOD output? What's BAD?
5. **Audience**: Who uses your output? How?

### Phase 2: Pattern Extraction (3-4 questions)

6. **Task Category**: Code generation, document creation, analysis, communication, or planning?
7. **Context Requirements**: What 5-7 pieces of information always change but are always needed?
8. **Question Design**: What questions should the skill ask to gather that context?
9. **Output Structure**: What sections, ordering, and format for the output?

### Phase 3: Skill Assembly (automatic)

10. **Formatting**: Converts your answers into proper skill YAML/markdown
11. **Example Generation**: Creates a worked example showing interrogation → output
12. **Integration Notes**: Explains how the skill connects to RAG, ReAct, bootcamp patterns

---

## Output Format Specification

### Generated Skill Structure

```yaml
---
name: [Your-Task-Name]
description: [Your task interrogation-driven skill]
version: 1.0
---

# [Your Skill Name]

## Overview
[Purpose, target audience, core value]

## Key Capabilities
[What this skill does, derived from Phase 2 answers]

## Structured Interrogation Framework

### Context Assembly Questions
[Your questions, formatted as phase blocks]

## Output Format Specification
[Your output template with sections]

## Example: Complete Workflow

### Interrogation Phase
[Worked example of Q&A]

### Generated Output
[Sample output your skill would produce]

## Reflection: What You Built
[Explanation of RAG system structure]
```

---

## Example: Complete Workflow

### Scenario: QA Lead Building a "Test Plan Generation" Skill

**You say:**
```
I'm a QA Lead and I create test plans every week.
I want a skill that helps me generate them faster
and more consistently.
```

---

### Phase 1: Task Discovery

**Skill interrogates:**

```
Q1: What task do you repeat at least weekly?
→ "Creating test plans for new features.
   I do this every sprint, sometimes 2-3 plans per week."

Q2: Walk me through how you do it today, step by step.
→ "Step 1: Read the feature specification
   Step 2: Identify main user flows and happy paths
   Step 3: List edge cases and error scenarios
   Step 4: Define test cases (pre-conditions, steps, expected results)
   Step 5: Estimate effort for each test case
   Step 6: Create test data requirements
   Step 7: Review with dev team to confirm scope
   Step 8: Document known limitations
   Step 9: Get stakeholder sign-off on scope"

Q3: What information do you need to gather before you start?
→ "Feature specification document
   API contracts (if applicable)
   User personas and use cases
   Browser/platform requirements
   Performance or load requirements
   Security requirements
   Existing test data and test environments
   Team's testing standards (what counts as 'thorough')"

Q4: What does GOOD output look like? Bad output?
→ "GOOD:
    - Clear objectives aligned to feature goals
    - Comprehensive scenarios (happy path + edge cases + errors)
    - Test cases with reproducible steps
    - Clear expected outcomes
    - Test cases prioritized by risk
    - Known limitations documented
    - Can be executed by any QA person

   BAD:
    - Vague test scenarios ('test the feature')
    - Missing edge cases
    - Unclear expected outcomes
    - No priority or risk indication
    - Can't be executed without asking author
    - Covers only happy path"

Q5: Who is the audience for your output?
→ "Primary: My QA team (5 people) who execute the tests
   Secondary: Development team (needs to understand test scope)
   Tertiary: Project manager (tracks testing progress)"
```

---

### Phase 2: Pattern Extraction

**Skill interrogates:**

```
Q6: Which category best describes your task?
→ "Document creation — test plans are structured
   technical documents with specific sections"

Q7: What context does the skill always need to know?
→ "1. Feature specification (what are we testing?)
    2. Testing scope boundaries (in/out of scope)
    3. User flows and personas
    4. Platform/environment constraints
    5. Performance or security requirements
    6. Available test data and test environments
    7. Team's testing standards"

Q8: What questions should the skill ask the user?
→ "When I get a feature to test, I always ask:
    - What's the core feature we're testing?
    - What are the main user flows?
    - What edge cases are most important?
    - What error scenarios matter?
    - What's the timeline for testing?
    - What environments do we have?
    - What's known about performance/security needs?
    - Are there similar features we can reference?"

Q9: What structure should the output follow?
→ "## Test Plan: [Feature Name]

   ### Test Objectives
   - What we're validating

   ### Scope
   - In-scope test areas
   - Out-of-scope (explicitly)

   ### Test Scenarios
   (Matrix table: Feature area | Happy Path | Edge Cases | Error Cases)

   ### Test Cases
   For each scenario:
   - Pre-conditions
   - Step 1, 2, 3... (reproducible)
   - Expected outcome
   - Priority (P0, P1, P2)

   ### Test Data Requirements
   - What data do we need?

   ### Success Criteria
   - What does passing look like?

   ### Known Limitations
   - What can't we test?

   ### Sign-Off
   - Stakeholders agree to scope"
```

---

### Phase 3: Skill Generation

**The skill generates a complete SKILL.md file:**

```markdown
---
name: test-plan-generator
description: Create comprehensive test plans for new features using interrogation-driven scope definition
version: 1.0
---

# Test Plan Generator Skill

## Overview

The **Test Plan Generator** helps QA leads and testers create comprehensive,
well-scoped test plans for new features. Instead of starting from a blank page,
the skill interrogates you about the feature, generates a structured test plan,
and ensures nothing is missed.

This skill demonstrates all three bootcamp intuitions:

1. **Context is everything** — Before generating a test plan, it asks about
   the feature, constraints, audience, and testing standards
2. **Structure gets rewarded** — Output is a properly formatted test plan with
   clear sections, test scenarios, and success criteria
3. **You are the retrieval system** — The skill asks the questions YOUR team
   always asks, capturing your testing expertise

## Key Capabilities

- **Feature Context Gathering**: Understand feature specifications, user flows, edge cases
- **Scope Definition**: Explicit in-scope and out-of-scope boundaries
- **Test Scenario Generation**: Happy path, edge cases, error scenarios in a matrix
- **Test Case Creation**: Step-by-step reproducible test cases with expected outcomes
- **Effort Estimation**: Risk-based prioritization (P0, P1, P2)
- **Stakeholder Alignment**: Built-in sign-off and known limitations

## Structured Interrogation Framework

### Phase 1: Feature Context (5 questions)

1. **Feature Name & Purpose**: What feature are you testing?
2. **User Flows**: What are the main user journeys through this feature?
3. **Edge Cases**: What edge cases matter most for this feature?
4. **Constraints**: What environment, platform, or performance constraints exist?
5. **Scope Boundaries**: What's explicitly OUT of scope?

### Phase 2: Test Strategy (4 questions)

6. **Test Objectives**: What are you validating? (Functionality? Performance? Security?)
7. **Test Scenarios**: What scenarios do you need to cover?
   - [ ] Happy path
   - [ ] Edge cases
   - [ ] Error handling
   - [ ] Performance/load
   - [ ] Security (if applicable)

8. **Test Data**: What test data do you need?
9. **Success Criteria**: How will you know the feature works?

## Output Format Specification

```markdown
# Test Plan: [Feature Name]

## Test Objectives
- Validate [core functionality]
- Ensure [user flow] works correctly
- Confirm [error handling] behavior

## Scope

### In-Scope
- [ ] User registration flow
- [ ] Login functionality
- [ ] Password reset
- [ ] User profile updates

### Out-of-Scope
- [ ] Advanced analytics
- [ ] Historical data migration
- [ ] Internationalization (phase 2)

## Test Scenarios

| Feature Area | Happy Path | Edge Cases | Error Cases |
|--------------|-----------|-----------|-------------|
| Registration | Valid email, new user | Existing email, special chars | Invalid email format |
| Login | Valid credentials | Case sensitivity, spaces | Wrong password, locked account |
| Reset Password | Email exists | Email case variations | Email not found |

## Test Cases

### Scenario: User Registration (Happy Path)

**Test Case 1.1: Register with valid email**
- Pre-condition: User has never registered
- Steps:
  1. Navigate to registration page
  2. Enter email: test@example.com
  3. Enter password: ValidPass123!
  4. Click "Register"
- Expected: Account created, redirected to dashboard

**Test Case 1.2: Validate email format**
- Pre-condition: Registration page open
- Steps:
  1. Enter email: not-an-email
  2. Click "Register"
- Expected: Error message: "Please enter a valid email"

### Scenario: Login (Happy Path)

**Test Case 2.1: Login with correct credentials**
- Pre-condition: Account exists with email test@example.com, password ValidPass123!
- Steps:
  1. Navigate to login page
  2. Enter email: test@example.com
  3. Enter password: ValidPass123!
  4. Click "Login"
- Expected: Redirected to dashboard, session created, name displayed

**Test Case 2.2: Login with wrong password**
- Pre-condition: Account exists, user not logged in
- Steps:
  1. Enter email: test@example.com
  2. Enter password: WrongPass123!
  3. Click "Login"
- Expected: Error message: "Invalid email or password"
- Priority: P1

## Test Data Requirements

- Email account: test@example.com / ValidPass123!
- Email account: second@example.com / TestPass456!
- Test database with 100 sample users
- Staging environment with current feature code

## Success Criteria

- [ ] All P0 test cases pass
- [ ] All P1 test cases pass
- [ ] Error messages clear and actionable
- [ ] Login/logout flow works end-to-end
- [ ] No console errors or warnings

## Known Limitations

- **Out of scope for this test plan**: Load testing (separate performance testing)
- **Assumption**: Email service is working (not testing email delivery)
- **Browser coverage**: Chrome/Firefox only (Safari tested separately)
- **Not covered**: 3rd-party authentication (OAuth tested in integration suite)

## Sign-Off

| Role | Name | Date | Approved |
|------|------|------|----------|
| Dev Lead | [Dev Lead Name] | | ☐ |
| Product Manager | [PM Name] | | ☐ |
| QA Lead | [Your Name] | | ☐ |

---

## The Reflection: What You Just Built

Look at what you just created:

- It **ASKS questions** → Questions 1-9 are retrieval. They gather the specific context about YOUR feature, YOUR constraints, YOUR team
- It **ASSEMBLES your answers into structured context** → The interrogation responses get organized into a structured format (scenarios, test cases, data requirements)
- It **FEEDS that context to generation** → A test plan engine could take those structured answers and produce the test plan

**You just built a RAG system.**

Every skill is a RAG system:
- **Retrieval**: The interrogation questions fetch relevant context from your knowledge
- **Augmentation**: Your answers get organized into structured format
- **Generation**: The structured format becomes a test plan any team member can execute

The AI completing patterns? That's what an LLM does. Why does this structured approach work so much better than "write me a test plan"? The LLM was trained by humans who rewarded clear, structured, specific inputs — that's RLHF. You've been doing all three (retrieval, augmentation, generation) since the first bootcamp exercise.
```

---

### What The Participant Now Has

A complete, formatted skill file they can save to their Claude Code skills library and use immediately:

```bash
# They save it as:
~/.claude-code/skills/test-plan-generator/SKILL.md

# Or reference it in a Claude Code project
# And use it like any other skill in the bootcamp
```

---

## Design Principles

### Principle 1: Task Discovery is Non-Negotiable
Never skip Phase 1. The quality of Phase 3 (generated skill) depends entirely on how well you understand your own task. A vague skill leads to vague prompts.

### Principle 2: Your Expertise is the Content
The skill isn't generic — it captures YOUR process, YOUR team's standards, YOUR audience. Generic skills fail because they don't match your reality.

### Principle 3: Pattern Extraction Reveals Structure
Many people don't realize the patterns in their work until interrogated. The questions force you to articulate what's implicit.

### Principle 4: The Generated Skill is Just the Beginning
The skill file you generate is your starting point. You'll refine it as you use it, add examples, adjust questions based on what you learn.

---

## Integration with Bootcamp Patterns

### How Make-Skills Ties Everything Together

**Priority Builder Pattern** (ABCD):
- **Action**: Your weekly task (the skill you're building)
- **Behavior**: The questions you ask (structured interrogation)
- **Context**: The information you always need (assembled by Phase 2)
- **Delivered**: The skill file (production-ready artifact)

**ReAct Pattern** (THINK → ACT → OBSERVE):
The skill itself uses ReAct:
- **THINK**: What questions do I need to ask? (Phase 1-2)
- **ACT**: Ask them and gather answers (interaction)
- **OBSERVE**: Generate the skill file and verify it makes sense (Phase 3)

**RAG System** (Retrieval, Augmentation, Generation):
The culmination of everything:
- **Retrieval**: Questions fetch context (what you know about your task)
- **Augmentation**: Answers get structured (organized into sections)
- **Generation**: Structure becomes artifact (skill file or output)

**Context is Everything Intuition**:
The entire workflow is about context — discovering it, mapping it, and encoding it into a skill that can access it later.

**Structure Gets Rewarded Intuition**:
The output is never prose — it's always formatted skill files, interrogation frameworks, matrices. That structure is why it works.

**You Are the Retrieval System Intuition**:
The skill you build IS a retrieval system. It retrieves your expertise about your task, augments it into structure, and generates outputs your team can use.

---

## Advanced Usage: Skill Composition

Once you have a few skills, you can **compose them**:

```
Skill A: "Generate technical specification"
Skill B: "Create implementation plan"
Skill C: "Design test strategy"

Composed Workflow:
1. Use Skill A to generate spec for new feature
2. Feed that spec's output to Skill B
3. Feed that plan's output to Skill C
4. Now you have spec + plan + tests, all coherent
```

The more skills you build, the more you can chain them for complex workflows.

---

## When to Build a Skill

### Build a Skill If:
- ✅ You do this task at least weekly
- ✅ The output matters (affects others)
- ✅ It takes 30+ minutes
- ✅ You always gather the same information
- ✅ You want it more consistent
- ✅ Others could use it too

### Skip Skills If:
- ❌ You do it once per quarter (too infrequent)
- ❌ The output is just for you (lower ROI)
- ❌ It takes 2 minutes (IDE/templates work fine)
- ❌ The process changes dramatically each time
- ❌ It's already fully automated

---

## FAQ for Capstone Learners

**Q: Will the generated skill be perfect?**
A: No. It's your starting point. You'll refine it as you use it, adjust questions, improve output templates. That's normal.

**Q: Can I build a skill for something non-work?**
A: Absolutely! Recipe generation, travel planning, gift recommendation — anything with a repeatable process.

**Q: What if I can't articulate my process clearly?**
A: That's what the interrogation does. The skill will help you think through it step-by-step.

**Q: Can I combine two tasks into one skill?**
A: Only if they're truly the same process with different contexts. Otherwise, split them — two focused skills beat one bloated one.

**Q: How long until I'm confident building skills?**
A: After your first 2-3 skills, the pattern becomes obvious. By skill 5-6, you'll be able to design them in your head.

**Q: Can I share my skills with my team?**
A: Yes! If your skill captures team expertise, your team can use it. Over time, you'll have a library of organizational skills.

**Q: What if my skill doesn't work as expected?**
A: Debug it like code: Test with different inputs, check the interrogation questions, refine the output template. Iteration is normal.

**Q: Is there a format for advanced use cases (like multi-stage pipelines)?**
A: Yes, but start with the basic 3-phase format. Once you're comfortable, you can extend it.

---

## Bootcamp Integration

### For Participants

**This skill is:**
- ✅ The capstone exercise of the bootcamp
- ✅ A meta-demonstration of interrogation at the skill-level
- ✅ The moment you become a skill creator, not just a user
- ✅ Your first tool for scaling your expertise

**Use this skill when:**
- You finish all prerequisite skills and patterns
- You've seen 3-4 example skills (dev-second-brain, etc.)
- You want to automate your own repeated work
- You're ready to build organizational capability

**Expected outcome:**
- Generate a complete, usable skill file
- Understand RAG at a deep level (you built one)
- Start thinking about your work as "patterns to automate"
- Join the community of skill creators

### For Facilitators

**Introduce in:**
- Final session of bootcamp (Session 3 or later)
- Post-bootcamp office hours (perfect for 1-on-1 coaching)
- Advanced track materials

**Teaching approach:**
1. **Show the framework** (3 phases, interrogation questions)
2. **Walk through the example** (QA Lead building test-plan-generator)
3. **Have participants do Phase 1** (find their task, walk through it)
4. **Guide Phase 2** (help them extract patterns)
5. **Generate Phase 3** (show them their skill file)
6. **The reflection** (explain what they just built)

**Expected time:**
- Simple skill (document template): 30 minutes
- Moderate skill (test planning, code generation): 45 minutes
- Complex skill (architecture analysis, multi-stage workflow): 60+ minutes

---

## Example Skills Participants Have Built

### From Past Bootcamp Cohorts:

- **Sales Deck Generator** (Sales team) — interrogates about product, audience, pricing, differentiators → generates sales deck outline
- **Technical Specification Writer** (Engineering team) — interrogates about feature, stakeholders, constraints → generates spec template
- **Meeting Facilitator** (Management) — interrogates about meeting goal, attendees, outcomes → generates agenda + discussion guide
- **Code Review Checklist Generator** (QA/Dev team) — interrogates about codebase, tech stack, risks → generates custom review checklist
- **Customer Interview Template** (Product) — interrogates about research goals, user segment, hypotheses → generates interview guide
- **Incident Post-Mortem Facilitator** (DevOps) — interrogates about incident severity, systems affected, timeline → generates post-mortem structure

---

## Files in This Skill

- `SKILL.md` — Complete skill definition and usage guide (this file)
- `README.md` — Quick-start guide for bootcamp participants

---

## References

### Bootcamp Patterns Used
- **Priority Builder**: ABCD framework for structured thinking
- **ReAct**: Reasoning + Acting pattern
- **RAG System**: Retrieval, Augmentation, Generation paradigm
- **Interrogation Workflow**: Questions before answers

### Academic References
- Yao et al. (2022) "ReAct: Synergizing Reasoning and Acting in Language Models"
- Lewis et al. (2020) "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
- Brown et al. (2020) "Language Models are Few-Shot Learners"

---

**Version**: 1.0
**Status**: Production-ready for bootcamp capstone
**Last Updated**: 2026-03-18
**For**: Joey's Prompt Engineering Bootcamp v2 — Capstone Track

---

## Quick Start

1. **Choose a task** you repeat weekly
2. **Answer the Phase 1 discovery questions** (5 min)
3. **Extract the pattern** in Phase 2 (5 min)
4. **Get your generated skill file** (automatic)
5. **Read the reflection** section to understand what you built
6. **Save and use it** with your Claude Code or share with your team
