---
source: "https://commandline.microsoft.com/azure-sre-agent-restricting-environment-ai-safety/"
title: "Stop restricting the agent. Start restricting its environment."
author: "Sanchit Mehta, Vishesh Agarwal"
date_published: "2026-08-21"
date_clipped: "2026-09-10"
category: "Azure & Cloud"
source_type: "web"
---

# Stop restricting the agent. Start restricting its environment.

Source: https://commandline.microsoft.com/azure-sre-agent-restricting-environment-ai-safety/

Deep Dive
Share
in
r
x
f
Stop restricting the agent. Start restricting its environment.
Stop restricting the agent. Start restricting its environment.
Human review improves safety but limits autonomy. Standing credentials preserve autonomy but increase risk. With Azure SRE Agent, we found a safer middle by moving control out of the model and into the runtime around it.
By Sanchit Mehta Principal Software Engineering Manager, CoreAI, Microsoft and Vishesh Agarwal Senior Software Engineer, CoreAI, Microsoft
2026.08.21
Azure SRE Agent gives an LLM tools, a code execution environment, and access to production resources. The first question most people ask is: “How is that safe?”
The instinctive answer is to restrict the agent. Least-privileged scopes. Short-lived credentials. A human approval gate in front of anything that mutates state. All of that helps, and we do all of it.
But after a year in production, we learned that restriction is only half the answer. A useful agent needs the capability to reason, the authority to act, and the agency to carry work through to completion. It must gather evidence, choose between tools, and act on what it finds. The same authority that makes an agent useful is also what makes it risky.
Human review is the obvious mitigation, and it remains the right boundary for irreversible, high-consequence actions. But if every meaningful action requires approval, the human is still operating the system one click at a time. The agent hasn’t removed the operational burden; it has only changed the interface. Rather than simply restricting the agent, the design problem is figuring out how to make a much larger class of actions safe enough to execute autonomously.
So, we start from a harder assumption: the agent will eventually do the wrong thing—whether it’s talked into it by a poisoned log line or simply going wrong on its own. A prompt can tell the agent what it should do, but it can’t guarantee what the agent will do. The same is true of controls implemented inside the environment the agent can inspect or influence. To the agent, a control within reach is just one tool call away from being bypassed.
The enterprise version of this problem is harder, because a shared agent serves readers, operators, and admins at once. “Can the agent do this?” splits into multiple questions: Who is asking? What authority do they carry? What can the execution environment reach? Where do the credentials live while it runs?
But the safer platform isn’t the one with the most approval gates. To maximize safety, you need to move the controls outside the agent’s reach. Inside its execution environment, the agent stays fully capable. Outside it, the enforcement layer decides what the environment can reach, what authority each operation carries, and when a human enters the loop. Authority is issued per task and expires with it. Prohibited behavior isn’t discouraged; it fails to execute.
We rebuilt Azure SRE Agent around this model. What follows traces each boundary we introduced, the gap it exposed, and how moving enforcement out of the agent let us increase autonomy without treating safety as a matter of trust.
Right intentions, unsafe outcomes
Let’s start with where we got it wrong. The failures that changed our architecture weren’t clever attacks. They were normal agent behavior pointed at an environment that allowed the wrong outcome.
The agent issued itself a credential, bypassing its harness. During an early test of PR-creation flow, the agent’s short-lived GitHub token expired. It inspected its own source, reconstructed the OAuth device-code flow, and prompted a researcher to complete the login, then wrote the new access and refresh tokens to its filesystem for reuse. The harness was supposed to fetch credentials and determine what authority the agent received. Instead, the agent rebuilt that machinery from inside its runtime and replaced the system-provided credential with one it had acquired itself.
It exfiltrated an image by trying to read it. Asked to interpret a screenshot in an alert payload, and lacking a vision tool, the agent found a free OCR service on the public internet, POSTed our test image to it, and read back the text. That’s a perfectly reasonable chain of thought—and it showed the possibility for customer data could be shipped to an unvetted third party and logged onto someone else’s server.
It found a customer’s secret and memorized it. A credential was committed in a customer repo. The agent found it during an investigation, quoted it in its findings, and saved it to memory with a note never to use it. This was well-intentioned, but now the secret lived in an investigation summary and a memory store, neither of which is in anyone’s rotation playbook.
It deallocated a VM on a pattern match. The agent was instructed to deallocate VMs after five safety checks. During one run, the logging service became unavailable after the third check. Instead of stopping, the agent matched the situation to a past memory where deallocation had been safe and deallocated anyway. Right authority, wrong action.
None of these needed an adversary—that’s the point. An adversary just makes it all worse for free: every channel the agent reads can be written to by someone you don’t trust, and at the execution layer, a hallucinated command and an injected one are the same command. The recent public disclosure of a coding agent steered into reading `/proc/self/environ` and finding a live API key is just the OCR story with malice added.
If you strip away the good intentions, there are three classes of attacks:
Bypassing the harness itself
Exfiltrating sensitive information or secrets
Taking disruptive actions against production resources
Underneath all four incidents is the same interaction pattern: the agent sits between things it reads and things it can act on. Every inbound channel can carry untrusted instructions. Every outbound channel can leak sensitive data or change production.
That forced the shift: If the environment permits it, the agent will eventually do it—intentionally, maliciously, or by accident. The environment is the policy.
>
If the environment permits it, the agent will eventually do it—intentionally, maliciously, or by accident. The environment is the policy.
So we moved the policy boundary outside the agent’s reach, converging on four enforcement layers that close the gaps.
1. Sandboxing: Get execution out of the trust boundary
Like many agents, our first design ran the harness itself, model-authored code, tools, and credentials together on the same machine—a pattern inherited from coding assistants. The harness is the control plane: it drives the loop, enforces policy, registers tools, and fetches credentials. Every path from the agent to the rest of the platform runs through it. That works better when there’s a human in the loop. Autonomous agents keep the layout but lose that immediate oversight, leaving model-authored code with the host’s network, filesystem, and identity.
The GitHub incident was possible because the harness sat on a filesystem the agent could read: when the agent’s token expired, it pulled the OAuth flow out of the harness’s own source and ran it itself. Better in-process checks wouldn’t have closed the gap: a policy hook can inspect a command before it runs, but the agent can inspect the hook right back – modify it, kill it, route around it. The code being governed can interfere with the machinery governing it.
Co-residency cut the other way, too: model-authored code had the host’s network. The OCR incident was possible because nothing stood between the agent deciding to send customer data and the request leaving the machine. The prompt said not to. The network still allowed it. The same co-residency also puts platform secrets within reach, often one file read away in places like /proc/self/environ from model-authored code, injected or not.
So we split the system into two. Agent reasoning and orchestration stay in a trusted runtime. Model-authored code and tools run in a per-agent microVM, connected back to the runtime over a narrow API surface. Inside the VM, the agent keeps full control: inspect files, launch processes, install packages. The agent can’t touch the machinery governing it—provisioning, tool mounting, policy, credential flows—none of which shares its filesystem. Platform secrets stay outside it, and egress is default-deny at a boundary the model can’t modify. The agent may still attempt the OCR call; it simply can’t leave.
We chose microVMs—built on ACA Sandboxes —over containers because containers share the host kernel. For arbitrary model-authored code, we wanted each agent to have its own kernel behind a hardware-virtualized boundary without sacrificing interactive startup times.
But isolation leaves a gap: tools still need to authenticate. Put credentials inside a microVM, and they become accessible to everything running there, including model-authored code, dependencies, and local MCP servers.
The sandbox needs to use credentials without possessing them.
2. Nothing worth stealing
Isolation moved platform secrets out of the runtime into the tool execution sandbox. But tools still need to authenticate. az needs an Azure token. git needs repository access. kubectl, MCP servers, and package registries need credentials of their own.
Put those credentials inside the microVM, and it’s still a credential-bearing environment. Every tool, generated script, dependency, and local MCP server runs beside the agent’s working identity.
Egress allowlists aren’t enough. The destinations a stolen credential would be sent to are often the same ones the agent must reach. GitHub, Azure, Kubernetes, and registries must all remain accessible.
So we adopted a stronger rule: The sandbox can use credentials, but it can’t possess them.
>
The sandbox can use credentials, but it can’t possess them.
We did not rewrite git , az , kubectl , or existing SDKs. They still request authentication through their normal paths but receive an opaque handle instead of a real credential. The handle is useless outside the egress proxy that transforms it.
The proxy does the real exchange at the boundary. Each handle is valid for exactly one tool call, one destination, one operation, and one use:
Call-bound: Valid only for the active tool call—the git push that requested it, not the rest of the session.
Destination-locked: Usable only for the endpoint authorized for that call. A handle for github.com/organizationA/repoB does not get filled for repoC, a public gist, or any other GitHub path.
Scope-limited: Restricted to the approved operation. A handle for pushing one branch is not repo-admin auth.
Single use: Dead once the request is completed. Replay doesn’t produce another credential.
Only after those checks pass does the proxy inject a short-lived credential into the outbound request. The credential never enters the VM’s filesystem, environment, process memory, tool output, model context, logs, or memory.
This closes the failure mode from our GitHub incident. An expired token no longer gives the agent an opportunity to reconstruct OAuth, capture refresh credentials, and turn its sandbox into a credential store. Credential issuance and refresh terminate outside the VM.
But authentication credentials are only one class of sensitive data. A legitimate tool call can return secrets as data: az command can retrieve a key or connection string, just as a repository, configuration file, or log can contain passwords, tokens, or keys as ordinary text. In those cases, the secret can still enter the sandbox as part of the requested operation.
That was our memorized secret incident. The agent found a customer credential during an investigation, quoted it in its findings, and saved it to memory with a note never to use it. But the ordering was already wrong: once the value had entered model context, a note not to use it couldn’t undo the exposure. The secret had already propagated into memory, sub-agents, and investigation notes.
This requires a second boundary, which we are piloting internally: inspecting and scrubbing sensitive tool output before it enters model context.
The rules are simple:  Real credentials never enter the sandbox. Raw secrets never enter the model.
>
Real credentials never enter the sandbox. Raw secrets never enter the model.
At this point, the agent can authenticate without acquiring durable credentials and investigate without ingesting recognized secrets. But neither guarantee prevents an authorized action from being wrong.
3. Authority without blanket approval
Secretless authentication determines how the agent reaches production systems—but not which production effects may proceed unattended.
The VM incident exposed that gap. The agent didn’t steal a token, bypass egress, or leak data. It used a valid path to take a production action, but the action was wrong. When its safety checks became unavailable mid-run, it should have stopped and escalated. Instead, it matched the situation to a past trajectory and deallocated the VM—through a path the approval policy never intercepted.
That’s the other half of agent safety: not whether the agent can perform an operation, but whether it should perform this operation, now, against this target, given this evidence.
Our current production boundary is simple: every mutation requires human approval. Reads stay autonomous, writes wait for approval, deletes are blocked. It’s safe, but it treats every change alike. The hard cases sit in between – restart this instance, scale this service, drain this node, deallocate this VM. No policy can classify these from the command alone. The same operation is routine or catastrophic depending on three inputs:
The operation: Restart vs. deallocate
The target: A disposable test VM vs. a critical production dependency
The evidence: A proven-unresponsive host vs. a missing or hallucinated check
Anthropic’s Claude Code auto mode and Meta’s agent guardrails point in the same direction: classify each action before letting it run unattended. So, we treat approval as a risk-classification problem rather than a permission check. Before execution, an independent guard – outside the agent’s reasoning loop – scores the proposed action against all three inputs: what it does, what it touches, and whether the evidence behind it is current and corroborated. Low-risk actions with current evidence proceed. Critical targets, or actions with insufficient evidence, stop for review.
We’re still building this layer out, and it’s where our design is least settled. But it already unlocks event-driven operation: an incident, a failed deployment, or a scheduled task can start an investigation with no human in the chat. The agent gathers evidence, takes the actions classified as low-risk, and pauses exactly where the remaining authority requires a person.  The unit of approval is not the command. It’s the operation, its target, and its evidence.
>
The unit of approval is not the command. It’s the operation, its target, and its evidence.
Everything above assumes the agent is acting autonomously. But when a human enters the loop, it acts on behalf of that person—and with the agent being a shared team resource, the question shifts from, “Is this action safe?” to, “Is this user allowed to cause this action?” That’s the next boundary.
4. Nothing to borrow
The previous layer decides whether an action is safe enough for the agent to perform unattended. A shared agent can’t answer that question with one sandbox, one tool set, one memory, and one identity for everyone. Doing so creates a confused deputy: a low-privilege user can borrow capabilities they don’t hold directly or modify shared state that influences a more privileged session later.
Shared memory makes the problem concrete. A user can teach the agent behavior that persists beyond that user’s authority. The same path exists through connectors, skills, hooks, and other shared configurations. The agent can’t be expected to remember which parts each user may influence.
The caller’s role must shape the environment before reasoning begins. Readers can observe but not drive the agent. Users can chat without modifying shared behavior. Operators can manage shared surfaces without approving high-privilege actions. Administrators can explicitly approve or delegate that authority.
These roles aren’t prompt instructions. They determine which tools and MCP servers are mounted, which resources the sandbox can reach, which memory is visible or writable, which credentials may be injected, and which actions require approval.
The rule is monotonic: the caller’s authority may be narrowed by the environment, but it must never be widened by the agent. A low-privilege request can’t be laundered through shared memory, a shared connector, an alternate tool path, or a high-privilege service identity.
The agent has nothing to borrow because there is no ambient authority outside the caller’s delegation chain. Rather than something the model remembers, policy is the environment instant for that user.
Autonomy through constraint
Model guardrails matter, but production safety can’t depend on them working every time. We already accept this with people: no one hands an operator root and promises to be careful. We give them scoped identities, just-in-time access, network boundaries, change control, and audit trails. Judgment is the first line of defense—never the only one.
Agents need the same backstops at a different cadence. An agent can make hundreds of tools calls in a single incident, replan between any two of them, and reach the same effect through three different tools. Approve every step and autonomy disappears; approve only the plan and everything after it runs unchecked. So, the question was never whether to keep policy gates. Instead, the question was where to put them: at runtime, as close as possible to each production effect, with human review reserved for the consequences the system can’t bound on its own.
That’s what the four layers are: one move, repeated. We opened with the questions a shared agent forces: Who is asking? What authority do they carry? What can the environment reach? Where do the credentials live? Each layer answers one of those questions in the runtime instead of the prompt.
Across the four layers, the design principles are the same:
Enforce constraints outside the agent’s access
Prefer deterministic enforcement over model judgment
Define invariants that hold even as architecture evolves
Where it still breaks
The system isn’t complete, and we still discover gaps in our enforcement layers. Examples of gaps we closed recently: an action blocked through one tool could still be reached through a different execution channel that bypassed hooks. In another case, an MCP server could silently widen its contract after onboarding, and the protocol had no mechanism to detect the change.
As these gaps surface, we improve our implementation. But our security principles stay invariant:
Better models will make mistakes rarer. They won’t shrink the blast radius when a mistake still happens. A smarter model shifts where the line falls between autonomous action and human review—more actions cleared as low-risk, more investigations that run start to finish without a human in the chat. But that line is drawn by the controls, not by the model. What microVM can reach, where credentials live, whose authority a session carries.
Five questions for agent platform builders
The four incidents ultimately changed the questions we asked in review:
Can the agent inspect, modify, or bypass the machinery that provisions its tools, identity, policy, or credentials?
Can the same effect be reached through another tool or execution path that avoids the intended control?
Through which paths can sensitive data enter the agent-controlled environment or leave the system?
For every consequential effect, can the platform identify who asked, what it did, what it touched, what data it carried, what evidence supported it, and whose authority it ran under?
When evidence is missing, stale, or ambiguous, does the operation reliably leave the autonomous path?
If the answer to any of those questions was “no,” we weren’t running a guarded agent. These are questions worth asking of any agent platform, including our own.
That’s what we mean when we say: The environment is the policy.
We also thank Zhenquan Xu, Hong Wang, Yefu Wang, and Eben Carek for their contributions to this work.
Share
in
r
x
f
Stop restricting the agent. Start restricting its environment.
Next Stop
One requirement, many failure paths: Evaluate, control, and optimize with ASSERT and ACS
Deep Dive
A safety requirement might appear simple while the runtime failure surface is complex. ASSERT helps identify coverage bugs; ACS fixes the policy.
[ read ]
August 24, 2026
Tool search: Finding the right tool at the right time
Deep Dive
As you add more tools to AI agents, the advantage comes from making the right tools discoverable at the right moment without paying the full cost of exposing everything upfront.
[ read ]
July 29, 2026
