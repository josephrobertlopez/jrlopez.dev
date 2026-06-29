---
title: "Edge Dev on the Hardware You Already Own"
description: "A phone classifies images in 1.4 ms. Wrap any device's accelerator as an MCP tool an agent can call — local, sandboxed, on hardware you already own."
author: "Joey Lopez"
date: "2026-06-07"
tags: ["code", "methodology", "theory"]
atom_id: 29
source_html: "edge-node-mcp.html"
url: "https://jrlopez.dev/p/edge-node-mcp.html"
generated: true
---

[jrlopez.dev ]()[The Idea ]()[A Worked Example ]()[How to Start ]()[The Sandbox ]()[The Code ]()[Your Device Mesh ]()
# Edge Dev on the Hardware You Already Own The chips in your phone, laptop, and Raspberry Pi mostly sit idle. Edge development is just using them — and it's more reachable than it looks. Here's a worked example, how to start, and how one AI agent ties your devices together. Joey Lopez June 2026 [The Idea ]()[A Worked Example ]()[How to Start ]()[The Sandbox ]()[The Code ]()[Your Device Mesh ]()The Idea
## You Own Several Computers. You Use One. Count the computers around you. A laptop, a phone, maybe a Raspberry Pi or an old desktop. Each one has processors built for heavy math — a GPU, and on most recent phones and laptops a neural *accelerator *: a chip that runs the multiply-and-add inside machine-learning models very fast. Nearly all of it sits idle while your apps ship the work to a data center. Edge development is the opposite habit — do the work on the hardware you already have, next to where the data is. It used to mean special boards and a lot of patience. It still takes some patience, but the pieces are now small enough to wire up in an afternoon. The rest of this is one example, how to start your own, and the thing that makes it click: a single AI agent that can reach all your devices at once. A Worked Example
## A Phone That Classifies Images in 1.4 ms Here is one small enough to describe in full. A phone runs a little *server *— a few dozen lines of Python in Termux — that exposes its accelerator as a tool an AI agent can call. The standard for that is MCP: a tool is just a named function at a network address. The whole interesting part is one function:
```
# on the phone, inside the MCP server@mcp.tool()defclassify_image(path: str) -> dict:"""Classify an image on the phone's accelerator."""out = run(["./broker","--image", path])# the broker owns the chipreturnparse(out)# -> {label, ms}
```

The agent on my laptop sees classify_imagein its tool list and calls it by name. The phone does the work and answers in about 1.4 ms — roughly 20× its own CPU. (A small native *broker *program does the actual talking to the chip, because the chip's driver is locked to the operating system and ordinary code can't open it directly. The server just hands it the job.) Strip away the acronym and that *server *is a small program that sits at a network address and waits — concretely, a FastMCP streamable-HTTP app, a few dozen lines, bound to the phone's tailnet interface. It exposes a handful of named functions — classify this image, embed this text, run this prompt — and any agent that speaks the protocol can call them. The phone runs the function; the laptop just knows its name and where to knock. What that buys you is reach. The Pixel's accelerator was previously locked behind Android's own APIs, callable only by code running on the device. Wrap it in an MCP server and it becomes a function any agent can invoke from anywhere on your tailnet. The auth boundary is one bearer token, checked by a pure-ASGI gate before the request is ever handed to the app — refuse the header, refuse the call, no exceptions.
```
classBearerGate:# pure-ASGI: require Authorization: Bearer <EDGE_TOKEN>def__init__(self, app, token): self.app, self.token = app, tokenasync def__call__(self, scope, receive, send):ifscope.get("type") =="http":
           hdrs = dict(scope.get("headers")or[])ifhdrs.get(b"authorization", b"").decode() !=f"Bearer {self.token}":awaitsend({"type":"http.response.start","status":401, ...})returnawaitself.app(scope, receive, send)
```

The other half lives on the laptop — one block of config that names the tool and where to find it. That's the entire handshake.
```
"mcpServers": {"edge-node": {"type":"http","url":"http://pixel-10a:8765/mcp","headers": {"Authorization":"Bearer <EDGE_TOKEN>"}
 }
}
```

On the same phone, classifying one image: 30.7 ms on its CPU, 14.3 ms on its GPU, 1.4 ms on the accelerator. Same device throughout — the only honest comparison. These are one model on one chip; another device will land somewhere else. CPU 30.7 ms GPU 14.3 ms chip 1.4 ms — ~20× faster than this phone's CPU MobileNet-v1 int8 · 50-run average · one Pixel 10a — chip ~1.4 ms (1.25–1.58), ~6.8× its 8-thread CPU build. The whole thing — the MCP server, the broker, the cross-compile recipe, and a runnable test client — is on GitHub: [github.com/josephrobertlopez/edge-node-mcp ](). How to Start
## See What's There, Test It, Then Build You can't tell what a device can really do from its spec sheet. The method is empirical, and it's the same three steps every time — the tool comes last, not first. See what chips are there Smoke-test each Build the tool — last Measure first; the tool wraps whatever won. **1. See what chips are there. **Ask the runtime what it can run on instead of guessing. On a phone, a TensorFlow Lite build will report the backends available to it — usually a CPU path, a GPU path, and a neural one (NNAPI, which routes to the NPU or TPU):
```
# what can this device actually run a model on?backends = list_delegates()# -> ['cpu', 'gpu', 'nnapi']
```

**2. Smoke-test each one. **Run a small, known model — MobileNet is the classic — through every backend and time it. This is where the spec sheet meets reality: some chips reject certain operations, and some *silently *fall back to the CPU while reporting success. So you measure, and you check what actually ran where. Those three numbers from the example are just this step on one phone.
```
# same model, every backend, 50 runs eachforbinbackends:
   print(b, benchmark(model, backend=b))# cpu 30.7 · gpu 14.3 · nnapi 1.4 ms
```

**3. Build the tool around the winner. **Only now do you write the tool, and you wrap the exact path that won — not a guess. Force it to fail loudly if the fast chip isn't really there, so you never ship a number that was secretly the CPU. Build last, around a measured result. That whole loop fits in an afternoon on one device. What costs time isn't the three steps — it's the mundane walls around them: a phone kills background processes, won't let your code read some files, forgets everything on reboot. Keep experiments small and reversible and you'll clear them. You don't need new hardware or a cloud account, just a device you already own. The Sandbox
## The Sandbox Is What Makes the Tinkering Fearless agent reaches in your phone — hardware you own proot sandbox files isolated shell isolated network isolated tinker nothing escapes the box Tailscale ACL → bearer gate → Termux proot → EDGE_FILE_ROOT jail. The agent only ever tinkers inside the innermost box. The agent never gets the whole phone. It runs inside a sandbox — Termux into a proot, its own throwaway Linux on hardware you own — and gets a fenced-off directory it can read and write inside, and nothing above. Every path the agent hands in gets resolved against a single root, and if the resolved path tries to climb out, the call is refused before anything touches disk. No .., no symlink trick, no quiet escape. The shell stays off by default, behind a destructive-command denylist, for the same reason.
```
def_safe_path(path: str) -> str:# resolve under EDGE_FILE_ROOT; raise if it escapes (.. or symlink)candidate = pathifos.path.isabs(path)elseos.path.join(EDGE_FILE_ROOT, path)
   rp = os.path.realpath(candidate)
   root = EDGE_FILE_ROOTifrp != rootand notrp.startswith(root + os.sep):raisePermissionError(f"path escapes sandbox EDGE_FILE_ROOT={root}")returnrp
```

That single function is the whole reason you can tinker without flinching. The hardware is yours, the directory is throwaway, and there's no cloud account to bill you for a mistake — delete the folder and the experiment never happened. It's reproducible because the boundary is one line of code, not a *trust me *: its own pip venv, imports that degrade instead of dying, a fence you can read in a sitting. Knock it down and rebuild it; nothing of yours is on the other side. The mesh of your devices is one tinkerer's sandbox — isolated, reversible, reproducible. The Code
## The Code, Top to Bottom It's all in one repo — [github.com/josephrobertlopez/edge-node-mcp ]()— and it's short enough to read in a sitting. Three pieces do the work: edge_node.py, the MCP server that holds the twelve tools behind the bearer gate and binds uvicorn to the tailnet; the launcher that keeps the server alive on a device that would rather kill it; and the test client that proves the fast chip is actually the chip that ran. Start with the server. The tools are honest about themselves — classify_imagedoesn't claim the accelerator ran just because it was asked to. It reports the delegate that *actually *executed, and if the accelerator library fails to load it says so in the return value instead of silently falling back and lying about it.
```
delegate_used ="cpu-xnnpack"ifEDGETPU_DELEGATE_LIBandos.path.exists(EDGETPU_DELEGATE_LIB):try:
       delegates = [load_delegate(EDGETPU_DELEGATE_LIB)]
       delegate_used =f"delegate:{os.path.basename(EDGETPU_DELEGATE_LIB)}"exceptExceptionase:
       delegate_used =f"cpu-xnnpack (delegate load failed: {repr(e)[:80]})"# ... returns {"results": res, "delegate": delegate_used}  <- which chip really ran
```

The same server degrades instead of dying. If the heavy dependencies aren't installed, the RAG tools return a clear error and the rest of the server keeps serving — a missing library shouldn't take the whole phone offline.
```
try:importnumpyasnpimportrag_cli# embedder, retrieve, build_prompt, run_llm, IDX_*exceptExceptionase:# deps missing -> RAG tools degrade, server still servesRAG_OK, RAG_ERR =False, repr(e)def_need_rag():if notRAG_OK:return{"error":f"RAG deps unavailable: {RAG_ERR}. Install fastembed+numpy."}returnNone
```

The file tools sit behind the _safe_pathjail from the last section, so the same server that serves the chip can't be talked into reading something it shouldn't. Then the launcher — the mundane-walls answer in one loop. A phone kills background processes and forgets them on reboot, so the launcher grabs a wake-lock to survive the screen going dark and supervises the server so a crash or an OOM just restarts it. Not clever. Just stubborn.
```
"$WAKELOCK"&& echo"[edge-node] wake-lock acquired"# survive screen-offtrap cleanup INT TERMwhiletrue;do"$PY""$SRV"echo"[edge-node] exited (code $?) — restarting in 2s">&2
 sleep 2done
```

The last piece is the desktop side: test_edge_client.pyas the smoke-test, and mcp.client.jsonplus a short CONNECT.mdas the handshake you copy into your own agent. Clone it, point the config at your own device's name, and call a tool. The loop only closes when the laptop knocks and the phone answers. Your Device Mesh
## One Agent, All Your Devices Here's the part that makes it more than a trick. Run Claude Code — or any tool that speaks MCP — on your laptop, and point it at the tools running on your other devices. Claude Code is happy to hold several of these connections at once, so a single agent can reach all your hardware: the phone's camera and accelerator, the desktop's GPU, the Pi's sensors. Each is just a tool at an address on your private mesh. Your scattered gadgets stop being separate things and become one system you operate by asking. *Classify what the phone camera sees. Run this on the desktop GPU. Read the greenhouse sensor and tell me if it's dry. *Same agent, different hardware, nothing leaving your network. A camera that thinks, a GPU shared between machines, a house of sensors with one brain — built from devices you already own. A first project Take the oldest phone in your drawer. Put one tool on it — classify whatever its camera sees — and wire it to Claude Code on your laptop. That's a working edge node and your first device on the mesh. The second one is the same recipe with the address changed. The hardware is already yours, and already idle. The only missing piece is deciding to wire one thing up. Whatever is beside you right now has been waiting for exactly that. Why bother, when there's a cloud for this Because the cloud has the math backwards. Tokens are cheap and effectively infinite — what's scarce is your attention, and the trust of the people whose attention you spend. So the tool wraps the delegate that *measured *as the winner, never a guess; it reports which chip really ran instead of confident bullshit; and it keeps the boundary one line of code so a mistake is cheap to undo — isolation and reproducibility as respect for finite attention. And it's all public on GitHub, reproducible by a stranger on hardware they already own — because shared, reproducible tinkering is the one thing that actually compounds. Pick up the phone you already own and ask it to do something. See what it says back. Joey Lopez · 2026 · [jrlopez.dev ]()
[← jrlopez.dev ]()· [agent-first design → ]()· [guardrails deep dive → ]()