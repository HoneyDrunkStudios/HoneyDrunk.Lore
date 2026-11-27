---
source: "https://www.docker.com/blog/prove-your-ai-agent-guardrails-work/"
title: "Prove your AI agent guardrails work"
author: "Hrittik Roy; Saloni Narang"
date_published: "2026-11-25"
date_clipped: "2026-11-27"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# Prove your AI agent guardrails work

You ask a coding agent to clean up one repository. If it has broad permissions, it may also reach your home directory, use your development credentials, and send requests to services you never approved. That gap between the task and the access you grant can turn a routine coding session into a data leak or lost work.

In [Sandboxing Claude and MCP](https://hrittikhere.com/posts/sandbox-claude-code-mcp-docker-sbx), Hrittik walked through running Claude Code and an MCP server inside Docker Sandboxes using its command-line interface, `sbx`. That walkthrough started with outbound access blocked, allowed the endpoints needed for the task, and inspected requests to other destinations, including telemetry. The useful part was seeing an actual request fail at the network boundary.

Now extend that workflow to a team. Models and providers will change, but the access rules still need to hold. A sandbox limits what an agent can reach on one machine. Organization governance adds shared rules, a managed way to run agents, and records of policy decisions. In this post, we’ll look at how one laptop can affect the whole organization, review two reported incidents, and connect them to four Docker controls: network policy, filesystem policy, managed credentials, and MCP access. Then we’ll test the network and filesystem controls with a simple bank administrator demo.

## How one laptop can affect the whole organization

If an agent exposes a developer’s SSH key or cloud token, every system that accepts that credential may need investigation. The security team must work out what left the machine, replace or revoke exposed credentials, and check whether anyone used them. Deleted work can also halt development. Keep backups of work that has not yet reached the repository.

The compliance consequences depend on the data and the organization. A personal data breach can trigger [GDPR notification duties](https://www.edpb.europa.eu/sme/assess-the-risks/data-breaches_en), subject to the applicable risk thresholds. HIPAA has [separate requirements](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html) for covered entities and business associates following breaches of unsecured protected health information. India’s DPDP framework also includes breach duties, but those provisions are [scheduled to take effect in May 2027](https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf). For a [SOC 2 examination](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2/), the question is whether the relevant controls operate as described. SOC 2 is not a breach-notification law.

Data sovereignty adds another question: where does the data go, and who controls it? Before approving a model API endpoint, establish where prompts and outputs are processed and stored, who can access them, and which contracts and laws apply. A provider’s nationality alone does not answer those questions. Network policy can restrict the destination, but it cannot prove how the provider handles data after receiving it.

This gets harder when developers choose and configure agents independently. A rule on one laptop may be missing on the next. An ignore file may stop one component from reading a file while another component includes it in an upload. Written policy needs matching controls in the software that runs the agent.

## Two real incidents of agents with too much access

In July 2026, developers reported two incidents where a coding agent went far beyond its task. In one, data left the machine. In the other, files were deleted from it.

### A background upload beyond the visible task

In an X post that has since been deleted, a user said Grok had uploaded their entire user directory, including SSH keys, a password manager database, and personal files. A [Hacker News discussion](https://news.ycombinator.com/item?id=48892468) brought wider attention to the claim. The home-directory claim remains the user’s account. The separate investigation below tested repository uploads.

Researcher Cereblab [intercepted Grok Build CLI traffic](https://web.archive.org/web/20261105135607/https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) and found a background upload running alongside the coding task. In a test with a 12 GB repository, about 5.1 GiB had left the machine before the capture stopped, and the upload was still running. The data went to Google Cloud Storage. Fake secrets planted in the repository also appeared in the traffic without being hidden. At the time, turning off “Improve the model” did not stop the repository uploads.

In a [reproducible follow-up](https://web.archive.org/web/20260906103014/https://github.com/cereblab/grok-build-exfil-repro), the researcher rebuilt the repository from a captured Git bundle, an archive of tracked files and Git history. The bundle included files the agent had been told not to read. Telling the model not to read a file didn’t stop the CLI from packaging and uploading it in the background.

There was a subsequent change. The researcher’s [updated timeline](https://cereblab.com/) says whole-repository uploading was disabled server-side on July 13 and remained off when retested on July 22.

The fix does not change the lesson. A coding agent is more than the model. It includes the CLI and any background processes, and those can act without the model asking. Give the whole application only the access its task needs. This is the principle of least privilege.

### A cleanup task that deleted a home directory

On July 10, Matt Shumer wrote: “[GPT-5.6-Sol just accidentally deleted almost ALL of my Mac’s files](https://x.com/mattshumer_/status/2075657271401390161).” He shared the agent’s acknowledgment and [confirmed that Full Access was enabled](https://x.com/mattshumer_/status/2075665244500677120). His [follow-up](https://x.com/mattshumer_/status/2076794038456385546) described the loss of his home directory.

A separate experiment shows why blocking one command is a fragile response. Developer [LinearUncle reported](https://x.com/LinearUncle/status/2075755010156302487) that, after a plugin blocked rm, the agent tried unlink, find -delete, and apply\_patch. A later attempt to move files to Trash through the GUI failed on permissions; a call to Node’s fs.unlink succeeded. The [plugin’s own documentation](https://github.com/linearuncle/codex-agentguard/blob/main/README.md) describes it as an additional guardrail and recommends sandboxing and backups.

The common issue is excessive access. A model can choose a different tool, and a background process can run outside the model’s visible workflow. Filesystem and network boundaries need to constrain both.

## What a sandbox gives you locally

Docker Sandboxes runs each agent in a microVM, a lightweight virtual machine with its own Linux kernel and Docker Engine. A workspace mount shares a host directory with the sandbox. A proxy on the host checks outgoing connections against network policy. The [isolation documentation](https://docs.docker.com/ai/sandboxes/security/isolation/) explains these boundaries.

That gives a developer a useful starting point. Share the project needed for the task, restrict outbound access, and inspect failures before adding permissions. Unnecessary telemetry endpoints can remain blocked while the required model and package services are allowed.

Choose mounts carefully. A writable mount shares real host files, so changes and deletions inside it affect your machine. Check additional mounts too, including shared agent skills where enabled. Docker’s [clone mode](https://docs.docker.com/ai/sandboxes/security/isolation/#clone-mode) gives the agent a private copy of a Git repository so you can review its commits before bringing them back. Isolation limits access, but files in a writable host mount still need backups. Clone mode still exposes the host repository for reading, including ignored files. Keep secrets outside it.

Local settings leave a rollout problem. A teammate can choose different rules or run an agent directly on the host. The organization needs a managed way to run agents, a way to require its use, and visibility into which sessions it covers.

*The diagram below shows how organization and team policies reach managed sandbox sessions, where access checks occur, and how policy decisions feed audit records.*

*Figure 1. Organization and team policies govern access for enrolled, licensed sandbox sessions.*

## How Docker AI Governance extends those controls

[Docker AI Governance](https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/) lets administrators manage sandbox rules and MCP access centrally. MCP, short for Model Context Protocol, connects agents to tools and data sources. Administrators define policies in Docker Home. On developer machines, sandbox mount checks, the host proxy, and Docker’s MCP gateway enforce the relevant rules. This gives teams shared access rules and records they can review when something goes wrong.

### Control outbound access and host mounts

[Network policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/) allow or deny destinations such as domain names, IP addresses, and IP ranges written in CIDR notation. For a restricted workflow, start with access denied and allow only the destinations the task needs. Under organization governance, local allow rules cannot grant extra access. Deny rules win, and developers can add local network restrictions.

This can block a background upload to an unapproved destination. But an approved hostname may still handle several kinds of traffic. In the Grok investigation, model requests and storage uploads used different URL paths on the same hostname, so a hostname-only allow rule would not distinguish them. Docker AI Governance now supports more granular network policies: on an allowed host, rules can match the HTTP method, URL path, and query parameters. For example, a policy can permit an agent to open a GitHub pull request while blocking requests to merge it. These finer-grained rules complement filesystem restrictions, which limit the data an application can collect and send.

[Filesystem policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem/) control which host paths may be mounted. A writable mount needs both read and write permission; a read-only mount needs read. If a filesystem deny rule and an allow rule match the same request, the deny wins. The decision happens when the sandbox is created. Once a writable mount exists, the agent can modify or delete files within it, regardless of whether it uses rm, a patch tool, or a programming language API.

### Keep managed credentials outside the agent environment

For [proxy-managed credentials](https://docs.docker.com/ai/sandboxes/configuration/credentials/), the host proxy adds authentication to outbound requests. The agent can authenticate to an approved service without receiving the raw secret inside the microVM. Credentials can also be scoped to a named sandbox.

This reduces the need to paste API tokens into prompts or store them in the workspace. The protection applies to proxy-managed credentials. A real token placed in an environment variable, a mounted file, or a passthrough login response may still be visible inside the sandbox. Limit what each credential can access and how long it stays valid. Storing a token through the proxy does not change its permissions or expiry.

### Govern MCP access through the gateway

[MCP access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/) govern server registration and subsequent requests through Docker’s MCP gateway. With MCP enforcement active, access requires an explicit permit, and a forbid rule overrides it. Administrators can control tool calls, resource reads, and prompt retrieval, rather than treating an approved server as permission to do everything it offers.

Registration and use are separate decisions. Blocking new registrations does not stop access to a server that is already registered. Rules checked on each request handle that case. Direct connections to remote MCP servers also need network controls because they bypass Docker’s gateway. Check where each server runs too: [local stdio servers run on the host](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/#restrict-host-run-servers), outside the sandbox VM. Their host access needs separate review.

*The next diagram summarizes the four controls to review together: network access, host mounts, managed credentials, and MCP tools.*

*Figure 2. Network, filesystem, credentials, and MCP controls apply to the whole agent application.*

### Make enrollment part of the rollout

Administrators manage [organization and team policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/) in Docker Home. Group mapping can keep Docker teams in sync with the organization’s identity provider. Policy updates take up to five minutes to reach developer machines. Network changes then apply to new requests. Filesystem changes require removing and recreating affected sandboxes because existing mounts keep their original access.

[Sign-in enforcement](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/sign-in-enforcement/) is also part of deployment. IT distributes it through endpoint management so developers must authenticate as members of an approved organization. This prevents personal-account bypass within sbx. Your endpoint controls also need to cover agents launched outside that managed workflow.

## A simple demo: protect a bank’s logs

Suppose you are a bank administrator. Developers want to use coding agents, and you need to enforce the bank’s access rules. Let’s keep the demo to two simple requirements:

- The sandbox can reach [hrittikhere.com](https://hrittikhere.com) (standing in for the bank’s website) over HTTPS. Other destinations stay blocked.
- The sandbox can use its project workspace, but it cannot read bank logs stored in your host home directory.

We’ll use fictional logs and a shell sandbox to check both boundaries without needing a model API. The results below describe what to expect when you run the demo.

### 1. Prepare the workspace and bank logs

[Install sbx](https://docs.docker.com/ai/sandboxes/get-started/) on macOS or Linux and sign in with an AI Governance licensed test user. You’ll also need permission to manage policies and audit delivery in a test organization:

```
sbx version
sbx login
sbx ls
```

Run these commands in your host terminal to create a workspace and a separate directory containing a fictional bank log:

```
mkdir -p \
  "$HOME/sbx-bank-demo/workspace" \
  "$HOME/sbx-bank-demo/bank-logs"

printf 'Fictional bank audit log: demo only\n' > \
  "$HOME/sbx-bank-demo/bank-logs/demo.log"
```

Next, enable AI Governance for your organization. In Docker Home, open **AI Platform → Manage and turn on AI Governance:**

*Figure 3. Enable AI Governance in Docker Home before configuring organization policies.*

### 2. Set the bank’s access rules

Next, create the bank’s network and filesystem access rules.

**Network policy**

First, let’s look at network access. In a bank, you don’t want employees’ coding agents connecting to just any website. For this demo, we’ll allow the sandbox to reach only [hrittikhere.com](https://hrittikhere.com) (standing in for the bank’s website) over HTTPS.

Once AI Governance is enabled, open AI Platform → Network access → Create policy and enter the following values:

| Field | Value |
| --- | --- |
| **Policy name** | `bank-demo-network` |
| **Scope** | Organization |
| **Decision** | Allow |
| **Destinations** | `hrittikhere.com:443` |
| **Protocol** | TCP |
| **Rule name (optional)** | `bank-demo-website` |

**With this as the only applicable network allow rule, all other destinations remain blocked by default.**

The curl checks below request headers without following redirects, so they need only hrittikhere.com:443. If you later add -L to follow a redirect to www.hrittikhere.com, allow that exact hostname on port 443 as well.

**Filesystem policy**

Next, let’s protect the bank’s logs. Employees may need a coding agent to work on a project, but that agent should not be able to read or modify sensitive logs in the home directory. We’ll allow access to the demo workspace and block access to bank-logs.

Open AI Platform → Filesystem access → Create policy.

***Note:*** *Use ~ in policy paths, not $HOME;* [*environment variables are not expanded*](https://docs.docker.com/ai/governance/reference/filesystem-rules/#home-directory) *by the policy engine.*

First, allow the project workspace with the values below. A writable workspace needs [both Read and Write permissions](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem/) for sandbox creation to succeed:

| Field | Value |
| --- | --- |
| **Policy name** | `bank-demo-filesystem` |
| **Scope** | Organization |
| **Rule Action** | Allow |
| **Filesystem path** | `~/sbx-bank-demo/workspace ~/sbx-bank-demo/workspace/**` |
| **Permissions** | Read and Write |
| **Rule name (optional)** | `bank-demo-workspace` |

In the same bank-demo-filesystem policy, add a second rule named bank-demo-logs to deny access to the protected logs:

| Field | Value |
| --- | --- |
| **Policy name** | `bank-demo-filesystem` |
| **Scope** | Organization |
| **Rule Action** | Deny |
| **Filesystem path** | `~/sbx-bank-demo/bank-logs ~/sbx-bank-demo/bank-logs/**` |
| **Permissions** | Read and Write |
| **Rule name (optional)** | `bank-demo-logs` |

**The workspace allow rule covers workspace and its descendants; it does not include the sibling bank-logs directory. The logs are protected by the explicit deny rule.**

Save the policies. You can also check their rules and scope in the Platform UI. Allow up to five minutes for [policy sync](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/), then inspect the active rules:

```
sbx policy ls --wide
```

*Figure 6. Active organization rules allow hrittikhere.com:443 and the workspace, and deny bank-logs mounts.*

### **3. Check website access**

Create a fresh sandbox with only the approved workspace:

```
sbx create --name bank-demo shell "$HOME/sbx-bank-demo/workspace"
```

From the host terminal, run the following requests inside the sandbox. The –max-time 15 option caps each request at 15 seconds, so a stalled request times out instead of hanging:

```
sbx exec bank-demo curl -fI --max-time 15 https://hrittikhere.com
```

The first request should return HTTP headers from the approved site:

*Figure 7. The approved HTTPS request to hrittikhere.com returns HTTP 200.*

```
sbx exec bank-demo curl -fI --max-time 15 https://example.com
```

The second should be blocked:

*Figure 8. The request to example.com returns HTTP 403; the network log confirms the policy decision.*

You can also check the [network log](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring/) to confirm that the failure came from policy enforcement:

```
sbx policy log bank-demo
```

The network log distinguishes allowed traffic from requests blocked by policy:

*Figure 9. The network log records hrittikhere.com:443 as allowed and example.com:443 as blocked.*

### 4. Check that bank logs stay private

Run both commands below from your host terminal so $HOME expands to the same host path. First read the fictional log on the host, then request that path inside the sandbox:

```
cat "$HOME/sbx-bank-demo/bank-logs/demo.log"
```

*Figure 10. The host can read the fictional bank log.*

```
sbx exec bank-demo cat "$HOME/sbx-bank-demo/bank-logs/demo.log"
```

The sandbox command should fail with “No such file or directory” because bank-logs is not mounted. This checks filesystem isolation; the next command tests mount-policy enforcement:

*Figure 11. The unmounted bank-logs path returns “No such file or directory” inside the sandbox.*

Now check whether a developer could add the logs as a read-only mount:

```
sbx create --name bank-demo-denied shell \  "$HOME/sbx-bank-demo/workspace" \  "$HOME/sbx-bank-demo/bank-logs:ro"
```

Creation should fail with a mount policy denied error:

*Figure 12. The bank-demo-logs rule rejects the read-only mount with a Read policy denial.*

A read-only mount still requires Read permission. The bank-demo-logs rule denies Read, so :ro does not bypass the policy.

### 5. Review the evidence in Docker Home

You can also review the policy decisions in the Docker Home UI under AI Platform → Audit logs → [Audit events](https://docs.docker.com/ai/sandboxes/governance/audit/view-export/). Filter by the test user and time, then inspect the denied mount request for bank-logs. Look for [filesystem\_mount](https://docs.docker.com/ai/sandboxes/governance/audit/record-reference/), the deny decision, the resource path, and the user. If Cloud delivery was disabled during the test, enable it and repeat the mount request.

*Figure 13. Audit events record the denied bank-logs mount and allowed workspace mounts.*

These audit records capture governance decisions, not every file operation or the agent’s prompts and output. sbx policy log shows network traffic; use the audit view for the mount decision. Docker also supports local JSONL audit files and Cloud delivery for hosted search, CSV export, and [SIEM forwarding](https://docs.docker.com/ai/sandboxes/governance/audit/siem/).

The bank now has a simple access-control check: the approved site is reachable, an unapproved site is blocked, and protected logs cannot be read or mounted. This supports the bank’s compliance work; it does not establish compliance on its own.

### 6. Clean up

After reviewing the results, remove the sandbox:

```
sbx rm bank-demo
```

Output:

```
❯ sbx rm bank-demo
Remove sandbox 'bank-demo'? This cannot be undone. (y/N): y
Deleting sandbox bank-demo...
Sandbox 'bank-demo' removed
```

You can then remove the fictional demo files and the test policies.

## Best practices for Docker AI Governance

Putting AI governance policies in place is only the first step. The real challenge is making sure those policies are practical, consistently enforced, and easy to verify as more developers start using coding agents. A few good practices can help teams reduce unnecessary access, apply the right restrictions to different workloads, and maintain visibility into what agents are doing. Here are five recommendations to keep in mind when rolling out Docker AI Governance across your organization:

1. **Use specific hostnames, not wildcards.** For example, allow `api.github.com:443` rather than `**.github.com`. A broad wildcard lets agents reach services you never meant to approve. Also avoid the Open preset, which allows every destination.
2. **Test a rule before you roll it out.** Check what a policy would do without running an agent. For example, `sbx policy check network blocked.example.com` shows whether that destination would be allowed or blocked.
3. **Use read-only mounts for reference data.** If an agent only needs to read docs or sample data, mount that folder with `:ro`. The agent can use the files but can’t change or delete them.
4. **Use team policies for different risk levels.** Set a policy’s scope to Teams instead of Organization. For example, the payments team can get a stricter network list than an internal tools team. Map Docker teams to your identity provider groups so access follows people as they move teams.
5. **Send audit records where your security team already looks.** Turn on SIEM forwarding, which requires cloud delivery. Use CSV export when an auditor asks for proof that a rule was enforced over a given period.

### Repeat the checks in other environments

The same questions apply when agents run in continuous integration (CI) jobs or other environments: which host files can they access, which services can they reach, and which credentials can they use? Check which controls each environment supports and repeat the tests there. A policy on a developer’s laptop does not automatically protect an unrelated container or production cluster.

For security teams, useful evidence connects a licensed, signed-in user to an active policy, a blocked action, and a record they can find. Check sign-in enforcement and license coverage alongside policy. An empty audit dashboard may mean some sessions were never covered.

## Start with a boundary you can verify

Sandboxing limits an agent’s access on one machine. Governance applies shared rules to managed sessions across the organization. Providers will fix individual failures, but the next failure may look different. Limit which files, services, and credentials it can affect, then test those limits and check the records.

Start with [the local sandboxing walkthrough](https://hrittikhere.com/posts/sandbox-claude-code-mcp-docker-sbx), inspect your rules with `sbx policy ls`, and run the bank demo with your platform or security team. Use the [Docker AI Governance documentation](https://docs.docker.com/ai/sandboxes/governance/) and [announcement](https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/) to plan a small rollout. Expand it after you have checked both the blocked actions and the audit records.
