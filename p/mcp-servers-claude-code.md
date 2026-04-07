---
title: "MCP Servers: The Inference/Execution Boundary"
description: "When MCP is worth the token cost, when it's not, and why the separation between reasoning and action is the only argument that matters."
author: "Joey Lopez"
date: "2026-04-07"
tags: ["engineering", "methodology", "code"]
atom_id: 28
source_html: "mcp-servers-claude-code.html"
url: "https://jrlopez.dev/p/mcp-servers-claude-code.html"
generated: true
---

# MCP Servers: The Inference/Execution Boundary When MCP is worth the token cost, when it's not, and why the separation between reasoning and action is the only argument that matters. Joey Lopez · April 2026 · engineering opinion claude-code
## The One Diagram MCP's value is one thing: an explicit boundary between the model reasoning and the system acting. INFERENCE LAYER (LLM) decides what to do constructs params Reasoning only. No credentials. EXECUTION LAYER (MCP Server) validates · connects executes · returns result Action only. Logged as events. BOUNDARY params result Everything on the left is *thinking *. Everything on the right is *doing *. They're in separate processes with separate permissions, separate logs, separate failure modes. Without MCP, thinking and doing happen in the same undifferentiated stream.
## The Honest Token Math MCP is **not **inherently token-efficient. [One measured setup ](): 4 servers, 58 tools, 55,000 tokens consumed before a single prompt. That's half the context window gone. WITHOUT Tool Search 46K tokens half your context gone WITH Tool Search 2.9K tokens 85% reduction tokens consumed by tool schemas at session start tokens consumed by tool schemas at session start 85% reduction with Tool Search. [Source ]()
Tool Search helps. But the real token savings from MCP aren't at the schema layer — they're at the **result **layer. A tool returning pending: 142(5 tokens) vs psqldumping a formatted ASCII table (500+ tokens) for the same data. **Don't believe the "40x savings" claim. **Skills cost 30–50 tokens at rest (just a name, loaded on demand). MCP tools cost ~50 tokens at rest with Tool Search. They're roughly equal. MCP's advantage is *capabilities *, not token count. [The New Stack documented 10 strategies ]()to reduce MCP bloat — the fact that there are 10 tells you the problem is real.
## When MCP Is Worth It Does it need external systems? NO YES Change how Claude thinks? Audit trail? Credentials? Persistent state? YES Skill NO Bash ANY YES MCP ALL NO Bash MCP = you need the boundary. Skill = you need to shape reasoning. Bash = you need neither. Short version: **MCP is worth the cost when you need the boundary. **The boundary gives you auditability, credential isolation, and failure isolation. If you don't need those, a Bash command or a skill is simpler and cheaper.

| Scenario  || Right tool  || Why  |

| Query a production database  || MCP  || Credentials stay server-side. Every query logged.  |

| Explain your codebase conventions  || Skill / CLAUDE.md  || Needs to be IN context to affect reasoning.  |

| Run git status || Bash  || No credentials, no audit need, no state.  |

| Handle payment API keys  || MCP  || Structural security: model never sees sk_live_... |

| Format a markdown table  || Skill  || String manipulation doesn't need IPC.  |

| Search a 10K-doc knowledge base  || MCP  || Persistent index in server memory. Structured results.  |

| Deep multi-step research  || Agent  || Needs its own context window for extended reasoning.  |

## The Enterprise Argument: Separation as Governance In regulated environments, "what did the AI do?" needs to be answerable from structured logs, not by reading a conversation transcript. WITHOUT MCP 50K token transcript good luck finding the DB query WITH MCP Conversation (30K tokens) Audit Log (JSON) tool: db_query params: {table: orders} structured, queryable, replayable

| Compliance need  || MCP gives you  || Skills give you  |

| "What actions did the AI take?"  || Structured event log  || Parse a transcript  |

| "Did it access credentials?"  || Opaque handles — it never had them  || Hope the model didn't print them  |

| "Can we replay what happened?"  || Same params = same result  || Context-dependent, non-deterministic  |

| "Can we restrict what it can do?"  || Server-side permission checks  || Prompt-level "please don't"  |

## Attention Economics (AAF Lens) Four dimensions for evaluating whether a tool respects the model's limited attention budget: Precision (returns only what's needed) MCP Skill Entropy Gap (closes uncertainty per call) MCP Skill Identity (shapes how Claude thinks) MCP Skill wins Temporal (state persists across calls) MCP Skill MCP wins 3 of 4. Skills win on Identity — they shape reasoning, MCP can't.
## The Walk-Away Test If you stop using this tool tomorrow, what do you keep? ASSET PORTABLE? WALK-AWAY MCP servers Python/Node scripts. Run anywhere. HIGH Skills Markdown. Only useful in Claude Code. MEDIUM Data (good MCP) Plain files, JSON, YAML. cat it. HIGH Data (bad MCP) Proprietary binary, cloud-only. ZERO **The walk-away test for any MCP server: **Can you catthe data it produces? Can you open it in another app? If the answer is no, you haven't built a tool. You've built a dependency.
## Setup: The One Bug Everyone Hits Claude Code spawns MCP servers without sourcing your shell profile. python3resolves to system Python. npxisn't found. Every environment variable from .zshrcis missing.
```
# WRONG (will fail):
{ "command": "python3", "args": ["server.py"] }

# RIGHT:
{ "command": "/home/you/.conda/envs/myenv/bin/python3",
 "args": ["/absolute/path/to/server.py"],
 "env": { "PYTHONPATH": "/absolute/path/to/project" } }

# For npx — always add -y (no interactive prompt in stdio mode):
{ "command": "/home/you/.nvm/versions/node/v22/bin/npx",
 "args": ["-y", "@some/mcp-server@latest"] }
```
**The 30-second test: **Run env -i /absolute/path/to/python3 /absolute/path/to/server.py. If it works in a bare shell with zero environment, it works in Claude Code. If it doesn't, it won't.
## Summary USE MCP WHEN External systems (DB, API, FS) Credential isolation needed Audit trail required Persistent state across calls Structured, minimal results Team-shared tooling DON'T USE MCP WHEN String manipulation Domain knowledge / conventions One-off tasks Shaping Claude's behavior Needs conversation context Could be a 10-line skill MCP's value isn't token savings. It's the explicit boundary between reasoning and action. If you'd put a code review gate between "the AI decided to do X" and "X actually happened" — that gate is an MCP server. For everything else, there's a simpler option. Use it. Built with [FastMCP 3.x ]()and [Claude Code ](). References: [New Stack ](), [arXiv 2603.13417 ](), [Anthropic Engineering ](), [Versalence ]()
[jrlopez.dev ]()