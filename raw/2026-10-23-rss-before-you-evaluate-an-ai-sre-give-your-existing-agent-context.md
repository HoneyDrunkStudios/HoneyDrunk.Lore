---
source: "https://www.cncf.io/blog/2026/10/21/before-you-evaluate-an-ai-sre-give-your-existing-agent-context"
title: "Before you evaluate an AI SRE, give your existing agent context"
author: "Roy Libman, CPO, Radar (Skyhook.io)"
date_published: "2026-10-21"
date_clipped: "2026-10-23"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-10-23"
---

# Before you evaluate an AI SRE, give your existing agent context

Source: https://www.cncf.io/blog/2026/10/21/before-you-evaluate-an-ai-sre-give-your-existing-agent-context

Posted on October 21, 2026
by Roy Libman, CPO, Radar (Skyhook.io)

CNCF projects highlighted in this post

[![Kubernetes logo](https://landscape.cncf.io/logos/e0303fdc381c96c1b4461ad1a2437c8f050cfb856fcb8710c9104367ca60f316.svg)](https://www.cncf.io/projects/kubernetes "Go to Kubernetes")

If you’re evaluating AI SRE products, you probably own most of one already. The coding agent your engineers use, whether that’s Claude Code, Codex or Cursor, can already investigate a Kubernetes cluster. What it usually lacks is context: what’s failing right now, and what changed before it broke.

We measured how much that gap matters. The same agent and model worked through 50 broken clusters twice, once with a shell and raw kubectl, and once with read-only MCP tools that return that context:

|  |  |  |
| --- | --- | --- |
| **Claude Code, same model, same 50 faults** | **Shell + kubectl** | **Read-only cluster context** |
| Correct | 45 | 46 |
| Mean judge score (0 to 1) | 0.905 | 0.936 |
| Correct within 2 minutes | 60% | 86% |
| Correct within 5 minutes | 78% | 90% |
| Mean time to submit a diagnosis, right or wrong | 191 s | 64 s |
| Median | 87 s | 44 s |
| 90th percentile | 632 s | 94 s |
| Mean tool calls per fault | 16.3 | 9.8 |

With context the agent was slightly more accurate: 46 correct against 45, and a mean judge score of 0.936 against 0.905. Both arms were right on 44 of the same faults.

The bigger difference was time, which is what counts during an active outage: nobody wants to wait fifteen minutes for an AI investigation while users are getting errors. With context, the agent had a correct diagnosis within two minutes on 86% of faults, against 60% with a shell. With a shell, one fault in ten took more than ten minutes. The gap was widest on the 14 faults where every pod reported Ready but the application was broken: 326 seconds on average with a shell, 79 with context. Fewer tool calls also means fewer model turns, which usually means lower token spend.

So before you evaluate an AI SRE, give the agent you already have that context, and measure it. That gives you a baseline for what the product adds.

## **How we ran it**

We ran 50 faults from [SREGym](https://github.com/SREGym/SREGym), the open Kubernetes fault benchmark from Microsoft and UIUC, on a live 3-node Amazon EKS cluster. Both arms used Claude Code on Claude Sonnet 5 through Amazon Bedrock. One had a shell and raw kubectl. The other had read-only MCP tools from Radar, an open-source Kubernetes UI and MCP server that we maintain, with kubectl blocked so it couldn’t fall back to a shell. SREGym’s judge, Claude Opus 5 at temperature 0, graded the first diagnosis each run submitted.

Context didn’t fix the model’s judgment. Both arms missed the same three faults. In one, a mutating webhook rewrote the pod’s memory limits at admission. In another, a PriorityClass mis-scoped as the global default changed the priority of newly created pods and set off preemption. Neither agent named the object responsible in either case. In the third, both found a real but unrelated misconfiguration and reported that instead of the DNS fault. Same model, same mistakes.

The two arms also differed in permissions, since only the shell could write, so this run doesn’t say which kind of context did the work. Every tool call from both arms is published in a per-fault [replay](https://radarhq.io/benchmark/mcp-vs-kubectl).

## **What we mean by context**

Radar’s read-only MCP tools add four things on top of what kubectl returns:

- **Current failures, already detected.** A ranked list of what’s broken right now, so the first call starts from what’s failing instead of a full inventory.
- **A change timeline.** Spec changes and Helm release history, kept after Kubernetes events expire. Events last an hour by default (the API server’s –event-ttl flag), and many changes never produce one.
- **Resources joined to their relationships.** Owners, topology and related issues come back with the object, so the agent doesn’t fetch them one by one.
- **Logs filtered to the errors.** Diagnostic lines first, with secrets redacted.

Since we maintain Radar, read the results with that in mind. None of the four depends on Radar specifically: any MCP server that returns the same context can be tested the same way.

## **What the agent asked for**

One fault shows the difference. In the OpenTelemetry Astronomy Shop demo, the frontend Deployment had lost its CART\_ADDR environment variable. Every pod reported Ready and nothing restarted. Both arms got the right answer:

```
Shell + kubectl: 58 tool calls, 701.6 s (excerpt)
  2.1s  kubectl get pods -n astronomy-shop -o wide
  2.2s  kubectl get events -n astronomy-shop --sort-by=.lastTimestamp
 10.3s  kubectl logs -n astronomy-shop product-catalog-77497fdc44-f5nx9 --previous
   ...
423.6s  kubectl run catsrc ...; kubectl cp astronomy-shop/email...
665.8s  helm get values astronomy-shop -n astronomy-shop
674.6s  kubectl get secret sh.helm.release.v1.astronomy-shop.v1 ... | base64 -d | base64 -d | gunzip
701.6s  submitted: "The frontend Deployment in astronomy-shop is missing the
        CART_ADDR environment variable..."
```

```
Read-only cluster context: 7 tool calls, 34.8 s
  1.0s  ToolSearch         (loads the MCP tool definitions)
  4.6s  issues             namespace=astronomy-shop
  4.9s  get_changes        namespace=astronomy-shop
 11.8s  get_resource       deployment/frontend
 12.3s  get_workload_logs  frontend
 19.8s  get_workload_logs  frontend
 20.4s  diagnose           deployment/product-catalog
 34.8s  submitted: "The frontend Deployment in astronomy-shop is missing its
        CART_ADDR environment variable, which was removed from the container spec..."
```

With a shell, the agent spent nearly twelve minutes on it, and ended by decoding Helm’s release Secret to diff the deployed manifest by hand. With the cluster’s recent changes one call away, it had the answer in 35 seconds.

Across all 50 faults the transcripts show the same thing. Without context, the agent opened every fault with `kubectl get pods` and `kubectl get events`. On 24 of them it then went looking for history, in ReplicaSets, rollout history or Helm release values, because nothing it could read told it what had changed.

With context, the agent asked for the same two things first, nearly every time. Current failures were its first call on all 50 faults, and the change timeline was its second on 35. Those are the two things the shell agent had to piece together from get pods, get events and rollout history. Much of the shell agent’s time went into rebuilding that context before it could start on the diagnosis.

## **What you’re actually buying**

An AI SRE is several products sold as one:

|  |  |  |
| --- | --- | --- |
| **Part** | **What it does** | **What most teams already have** |
| Trigger | Starts an investigation when an alert fires | Alerting, but nothing that starts an agent |
| Context | What the agent can read: live state, recent changes, current failures | kubectl and RBAC. Change history is the usual gap |
| Reasoning loop | The model, plus the harness that picks the next call | Claude Code, Codex, Cursor |
| Delivery | Puts the answer in Slack, the ticket or the incident channel | Partly |
| Governance | Whose identity it uses, what it may change, what gets recorded | Kubernetes RBAC, and API audit logs if you’ve configured an audit policy |

If your team pays for a coding agent, it already has a reasoning loop, and the results above measure the context row on its own. When you evaluate a product’s context, check whether it:

- keeps change history after Kubernetes events expire
- starts from what’s already failing

Context also isn’t tied to one agent. An MCP server can give the same read-only context to your coding agent or to an SRE agent: [HolmesGPT](https://github.com/HolmesGPT/holmesgpt), a CNCF Sandbox project, accepts remote MCP servers as toolsets. So you can test the context and the agent separately.

If your coding agent with good context diagnoses as well as the AI SRE you’re trialling, judge the product on the other rows of that table, starting with the trigger. A coding agent investigates when someone asks it to. An AI SRE can start when the alert fires, while you’re asleep, and have an answer waiting by the time you open Slack. That’s a real advantage, and worth weighing on its own.

## **What it runs as**

The shell transcripts also show why the governance row matters. The agent launched its own pods on 13 faults and ran exec, cp, port-forward or debug on 21. On 4 it pulled Secret data into its context, decoding it on 3. Read-only access doesn’t prevent that: the built-in view role excludes Secrets, but many “read-only” roles don’t. On one fault in the Social Network app it launched a pod that ran drop() on two of the application’s MongoDB collections to test a theory, then submitted a wrong diagnosis. SREGym’s prompt allowed all of this: it tells the agent a fix stage follows, says its kubectl can “inspect and modify resources”, and tells it not to ask for confirmation. An agent given write access and told to fix things will use that access while it’s still investigating.

So check what an AI SRE runs as. It should:

- work with a read-only identity, with no exec and no access to Secrets
- record every call it made, so you can see what it read

## **Test it yourself**

**Give every contender the same model and the same read-only identity.** Kubernetes’ built-in view role leaves out Secrets and grants no exec. This writes a kubeconfig that holds only a service account bound to it, so no contender can fall back to your admin credentials:

```
kubectl create serviceaccount ai-eval -n default
kubectl create clusterrolebinding ai-eval-view --clusterrole=view --serviceaccount=default:ai-eval
TOKEN=$(kubectl create token ai-eval -n default --duration=8h)
ADMIN_USER=$(kubectl config view --minify -o jsonpath='{.users[0].name}')
kubectl config view --minify --flatten > ai-eval.kubeconfig
export KUBECONFIG=$PWD/ai-eval.kubeconfig
kubectl config set-credentials ai-eval --token="$TOKEN"
kubectl config set-context --current --user=ai-eval
kubectl config delete-user "$ADMIN_USER"
kubectl auth can-i get secrets   # should print "no"
```

**Run the same faults.** SREGym has drivers for Claude Code, Codex, Copilot, Cursor, Gemini CLI and OpenCode, and its Lite suite of 17 problems runs on kind with 8 vCPU and 16 GB of memory ([setup](https://github.com/SREGym/SREGym#readme)):

```
uv run main.py --suite sregym-lite --agent claudecode --model claude-sonnet-5 \
  --judge-model <a model none of your contenders use> --stages diagnosis --n-attempts 3
```

For an AI SRE product SREGym has no driver for, `--use-external-harness --problem <id>` injects the fault and leaves the cluster broken for you to point the product at.

**Score at a fixed time limit, and repeat.** Use a limit that matches your response target; we report two and five minutes. Run each fault more than once, because a gap of two or three faults in a single run can be noise. Record token spend per fault too.

**Then replay two or three of your own incidents** on staging, with the same identity. Benchmarks inject faults into a freshly deployed app, and your incidents won’t look like that.

## **What this doesn’t show**

- We maintain Radar, and the context arm used Radar’s MCP server. The per-fault data is public so you can check our reading of it.
- Each arm ran each fault once.
- SREGym injects each fault minutes after deploying the app. That favours anything that tracks recent changes, Radar included.
- We measured diagnosis, not remediation.

## **Start with context**

Give the agent you already have read-only access to the cluster’s current failures and recent changes, and measure it at a fixed time limit. Use that as the baseline for anything you trial: compare diagnosis first, then what the product adds around it. Before you replace the agent, measure what happens when you improve what the agent knows.

*Radar is an open-source (Apache-2.0) Kubernetes UI with a read-only MCP endpoint. The source and install instructions are at* [*github.com/skyhook-io/radar*](https://github.com/skyhook-io/radar)*.*
