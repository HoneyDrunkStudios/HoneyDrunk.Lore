---
source: "https://commandline.microsoft.com/agent-hooks-framework-neutral-ai-governance-contract/"
title: "Your agent's guardrails have a bypass"
author: "Mohammad Abuomar, Caitie McCaffrey, Sarah Bird, Responsible AI at Microsoft"
date_published: "2026-08-27"
date_clipped: "2026-09-10"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Your agent's guardrails have a bypass

Source: https://commandline.microsoft.com/agent-hooks-framework-neutral-ai-governance-contract/

Open Source
Share
in
r
x
f
Your agent’s guardrails have a bypass
Your agent’s guardrails have a bypass
Agents are moving into production faster than the governance around them. Today’s controls are framework-specific, mostly observe-only, and fail open when they crash. To help address this, we created Agent Hooks: an open, framework-neutral governance contract with conformance testing on both sides. What follows is the contract and the story of proving “deny means deny” inside a real framework core.
By Mohammad Abuomar Principal Architect, Responsible AI, Microsoft , Caitie McCaffrey Member of Technical Staff, CoreAI, Microsoft , Sarah Bird Chief Product Officer of Responsible AI, Microsoft , and Responsible AI at Microsoft Microsoft’s Responsible AI team
2026.08.27
The deployments are real now: agents with tools, credentials, and the autonomy to act on an organization’s behalf. Every agent carries the same requirement: policies must be enforced, approvals must actually gate actions, and there must be evidence of what happened. And every framework answers that requirement differently, with mechanisms that were designed for observability, not governance. As agents grow more capable, their execution paths multiply: subagents, retries, batch entry points, background tasks. The governance question moves from “did we write a guardrail?” to “is it enforced on every path, and can we prove it?”
Here is an example of this gap in practice.
A team builds a customer support agent. It can look up accounts, draft replies, and issue refunds. Compliance sets two rules: refunds above a threshold need human approval, and account data never reaches the reply channel unredacted. The team does what their framework documentation suggests, adding a guardrail callback on tool calls and tool outputs.
While performing quarter-end financial closing, it was discovered that there is a large gap exceeding the discretionary customer refund budget. The system has been issuing refunds erroneously. The incident review finds three things. The approval guard threw an exception on a malformed refund request; the framework dispatcher caught the error, logged a warning, and executed the refund anyway, which is its documented default. The output scanner never saw one egress path, because a batch entry point emitted no callback at all: the guard was attached to the interactive path, and the batch path simply never fired it. And nobody could produce evidence of what either guard actually evaluated, because callbacks observed values without recording anything that binds them to what executed.
Nothing here is exotic. The team followed the instructions. The instructions were the problem.
The failure class: enforcement attached to one path, while the runtime grows paths. The fix is structural, not more callbacks.
The hooks you have are not a governance surface
We catalogued the interception surfaces of the mainstream agent frameworks from their primary documentation and source. LangChain’s BaseCallbackHandler defines 20 lifecycle events, and the dispatcher discards handler return values, so a callback cannot block or rewrite anything; a handler exception is caught and swallowed unless the author opts into raise_error, which defaults to false. CrewAI’s event bus registers 78 typed event kinds, all observe-only. LlamaIndex’s instrumentation module is telemetry by design: no return value, exception, or mutation reaches the underlying action. The OpenAI Agents SDK exposes lifecycle hooks that observe and guardrails that can block, but its input guardrails race the first model call unless you set a flag. Semantic Kernel’s filters genuinely block; but when registered through dependency injection, execution order is documented as not guaranteed and ordering decides whether redaction runs before egress.
Count the lifecycle surfaces alone: LangChain exposes 20 callback events, CrewAI 78, the OpenAI Agents SDK seven, and Semantic Kernel three, while LlamaIndex ships two coexisting observability surfaces. Payloads range from untyped dictionaries to typed contexts. Control semantics range from none to full block-and-modify. Failure behavior ranges from silently swallowed to propagated. And not one of these frameworks ships a conformance suite that a controls author can run to verify that a deny stops the action. Every guarantee your control depends on is framework-specific folklore.
Why builders should care
If you run agents in production, you inherit two problems: controls behave differently across frameworks, and you cannot reliably prove that they ran.
Control builders must create and maintain a separate adapter for each framework. Worse, each framework answers the most important question differently: when a control denies an action, does the action always stop?
Framework builders face the other side of the same problem. Enterprise customers need approvals, policy checks, audit records, and data controls, so each framework must build and maintain these features itself. A shared contract changes the practical outcomes for all three: write controls once and reuse them across frameworks, verify enforcement instead of assuming it, get audit evidence by construction, and stop paying the per-framework integration tax on every governance requirement.
Agent Hooks: One governance contract for the ecosystem, testable on both sides
Today we’re publishing Agent Hooks , specified as AGENT-HOOKS-0.1: an open, framework-neutral governance contract for AI agents, and a common interoperability layer that any framework can implement and any control can target. It ships with SDKs in Python, TypeScript, .NET, Rust, and Go, a 47-scenario conformance kit that makes “supported” a testable claim, and a first-class implementation merged into Microsoft Agent Framework ’s core. The contract is deliberately small: eight interception points that bracket the agent loop, one context payload, three verdicts, and normative obligations on the host. Controls integrate against it once. Frameworks implement it once. The M×N adapter matrix becomes M+N.
Twenty bespoke adapters, or one contract with a conformance kit on each side of it.
What it looks like
An interceptor is a few lines. This one enforces the refund rule from the opening incident:
Copy
from agent_hooks import Interceptor, Verdict
class RefundGuard(Interceptor):
def intercept(self, context) -> Verdict:
if context["interception_point"] != "pre_tool_call":
return Verdict.allow()
call = context["tool_call"]
if call["name"] == "issue_refund" and call["args"]["amount"] > 500:
return Verdict.escalate(reason="refund_over_limit",
message="requires human approval")
return Verdict.allow()
And installing the full contract in Microsoft Agent Framework is one factory call:
Copy
pip install agent-framework-core[agent-hooks]
agent = Agent(client=client, tools=[issue_refund],
middleware=[create_agent_hooks_middleware([RefundGuard()])])
That single call installs enforcement at every point of the loop: it is deliberately impossible to install part of the contract and believe you have all of it.
How it works: Emitting and enforcing
The eight points bracket the loop: agent_startup, input, pre_model_call, post_model_call, pre_tool_call, post_tool_call, output, agent_shutdown. At each, the host builds an AgentContext, a tiered JSON payload with a small required core (agent, session, sequence, timestamp, and the target under evaluation), per-point required fields, and namespaced extensions. The target is the one value a transform may rewrite, pinned per point.
Interceptors return a verdict with one of three decisions; allow, deny, transform. On the wire, an escalation looks like this:
Copy
{
"decision": "deny",
"reason": "refund_over_limit",
"message": "requires human approval",
"approval": {
"resolver": "host",
"context_identity": "sha256:11f8bab5…"
}
}
In earlier iterations, we also had warn and escalate verdicts. Warn verdict was removed since a warning is an allow carrying warnings, because warning is metadata, not control flow. An escalation is now modeled as a deny carrying an approval block, denied as-is unless the approval seam lifts it. That construction removes a failure mode outright. An unresolved escalation used to be a state the host had to remember not to proceed on; now it is simply a deny. Fail-closed is a property of the type system, not a code path someone has to maintain.
Host obligations are the half that frameworks usually leave undefined, and they are normative here. A deny at pre_tool_call means the tool is not invoked. A deny at post_tool_call means the result is discarded and never enters agent state. A host that cannot build a valid context, cannot reach an interceptor, times one out, or receives a malformed verdict must synthesize a deny with a reserved machine-readable reason. The opening incident cannot occur on a conformant host: the crashing guard becomes a deny, and the record says so.
Every emission also produces an InterceptionRecord, which is payload-free by design. It carries the verdict projection, which interceptor decided, the composition profile, the sequence number, and content identities computed before and after enforcement. It never carries customer content. You can export the full audit trail of an agent’s decisions without exporting a single prompt.
The approval that can’t be replayed
The approval block above carries a context_identity: a SHA-256 over the canonical JSON of exactly what the approver was shown. The resolution must echo that identity byte-for-byte. This is the difference between approving an action and approving a session.
Approval binds to content, not to a session. Change the content, and the approval does not transfer.
In our demo suite, a support agent tries to refund $840 against a $500 cap. The guard escalates; a human sees the exact call (tool, arguments, identity) and approves. The refund executes, and the record binds the approval to that identity. Then the demo replays the approval against a mutated call: issue_refund for $8,400, claiming the earlier authorization. Different content, different identity, and the deny stands. We run this same scenario across eight frameworks: LangGraph, the OpenAI Agents SDK, Microsoft Agent Framework, Semantic Kernel, LlamaIndex, CrewAI, the Claude Agent SDK, and a bare reference host. Every one of them produces the identical 20-row decision stream, with the identity probe byte-identical across the Python, .NET, and TypeScript SDKs. One contract, one behavior, provable.
Doesn’t a hook layer slow everything down?
The enforcement seam itself is cheap. During the Microsoft Agent Framework integration review, the per-run overhead of the contract’s machinery (identity allocation, gate consultation, scope management) was measured at roughly a microsecond per run and a microsecond per streamed update on commodity hardware: noise against any model call. The honest cost lives elsewhere, and we will name it: fully fail-closed streaming means buffering. A host that guarantees no token egress before the output verdict cannot also give you first-token latency during enforcement. The spec supports a declared bounded-exposure incremental mode for hosts that need streaming, with the exposure bound stated in the conformance claim; buffered is the default, because it is the only mode with zero exposure.
Policy evaluation is also cheap when it is in-process. The first policy runtime built on the contract originally shelled out to an external policy engine per decision: 26.8 milliseconds per evaluation, dominated by process spawn. Moving Rego evaluation in-process brought a warm evaluation to 0.32 milliseconds, measured as best-of-five over the same policy pack on the same hardware, with activation amortized after roughly twenty decisions. Your policy engine shouldn’t be the slow part of your agent, and it doesn’t have to be.
What Agent Hooks doesn’t protect against
Agent Hooks is a cooperative contract, not a security boundary. The host framework is fully trusted: interceptors run in-process with full data access, and registering an interceptor is equivalent to granting it write access to every action the agent takes. A hostile or buggy host can skip points or ignore verdicts, and the conformance kit can’t detect that. There’s no complete-mediation claim: a framework may expose direct tool execution or background paths that never reach pre_tool_call, so the contract makes coverage testable, not automatic. Server-side tool execution (hosted code interpreters, service-managed tools) can’t be intercepted at the tool seam at all; it surfaces at post_model_call, and conformant hosts document exactly that. The threat model in the spec says all of this in normative language. A hook layer governs what a cooperating framework does; containing hostile or untrusted code is a sandbox’s job, and Agent Hooks isn’t a sandbox. If someone tells you otherwise, they are selling something.
Proof it survives contact
A contract is worth what its enforcement survives. The Microsoft Agent Framework integration went through five maintainer review rounds, and the maintainers didn’t take our claims on faith: they reproduced real fail-open paths, including a retrying middleware that defeated persistence ownership and a drained-and-discarded attempt that persisted before any verdict existed. Every finding was fixed with a regression test that fails when the fix is reverted. We’ll be honest: the hardest part of this project wasn’t writing the spec; it was watching skilled reviewers falsify our own “this is fail-closed” claims, twice, and rebuilding until they couldn’t.
That discipline is what the conformance kit packages. Forty-seven scripted scenarios drive a host through the contract: denies that must stop actions, transforms that must be applied, crashes that must become denies, approvals that must bind to content. A conformance claim is a declared surface plus the report. There is no certification theater, just results you can re-run. Two hosts hold certified claims today: the Agent Control Specification policy runtime and Microsoft Agent Framework’s core implementation, which passes 47 of 47 applicable scenarios and discloses its one non-default behavior (terminating the run on enforcement-layer failure) as a declared posture rather than papering it over. The .NET implementation is in review with the same test discipline: 84 tests, every enforcement property pinned.
Try it
Copy
pip install agent-hooks-sdk # Python
npm install @responsibleai/agent-hooks # TypeScript (napi, prebuilt)
cargo add agent-hooks-sdk # Rust
dotnet add package ResponsibleAI.AgentHooks # .NET
go get github.com/responsibleai/agent-hooks/sdk/go/agenthooks
The spec, the conformance kit, the documentation, and all five SDKs live in the agent-hooks repository at github.com/responsibleai/agent-hooks . If you’re on Microsoft Agent Framework, the feature is in core behind the agent-hooks extra today. The eight-framework demo suite, including the replay scenario above, ships with runnable, deterministic scripts that need no API keys.
An open contract needs more than one author
AGENT-HOOKS-0.1 is versioned, the schemas are published, changes go through public proposals, and the conformance kit is the arbiter of what “supported” means. We built reference implementations in five languages so that no single runtime defines the contract, and we encourage other implementations. If you maintain a framework and want the conformance report with your name on it, the harness interface is four methods, and we’ll do the integration work with you. If you build controls and the contract is missing a seam you need, the proposal process is open. We’d love to hear from both sides.
FAQs
Why not just use each framework’s middleware?
Because middleware answers “where can code run,” not “what must happen when it says no.” The contract’s value is the normative half: deny stops the action, crashes become denies, approvals bind to content, records are payload-free. Middleware is how hosts implement it; the contract is what makes the result verifiable.
Three verdicts seems small. Where are warn and escalate?
They’re encoded, deliberately: warn is allow plus warnings; escalate is deny plus a liftable approval. Five verdicts means five states hosts can mishandle; three with fail-closed composition means an unresolved anything is a deny.
What happens under streaming?
By default, everything buffers until the output verdict: zero exposure, at an honest latency cost. Hosts that need incremental release declare a bounded-exposure mode in their conformance surface, with the bound stated. What no conformant host may do is stream first and enforce later while claiming otherwise.
Can a malicious host just lie?
Yes. See the threat model section: the host is trusted, and this is a contract, not a sandbox. What the contract changes is that a cooperative host’s claims become testable, and a gap becomes a conformance finding instead of an incident.
Is this Microsoft only?
No. The spec and SDKs are MIT-licensed under an open organization; the first certified consumer is an independent policy runtime, and the same scenario suite runs on eight frameworks from six vendors. Microsoft Agent Framework is the first framework to ship it in core; the contract is written, so it will not be the last.
Share
in
r
x
f
Your agent’s guardrails have a bypass
Next Stop
PyRIT: Democratizing AI red teaming through open-source tooling
Open Source
Learn how the Python Risk Identification Tool for generative AI evolved over time to open up AI red teaming to subject matter experts from virtually any domain.
[ read ]
September 10, 2026
How we built ThinkingBox to measure whether agents finish the job
Open Source
ThinkingBox separates the execution framework from the benchmark package. This split lets builders update the harness and benchmark independently.
[ read ]
August 19, 2026
