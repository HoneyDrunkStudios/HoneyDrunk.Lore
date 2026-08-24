---
source: "https://www.endorlabs.com/learn/hacking-your-life-with-ai-can-get-you-hacked"
title: "Hacking Your Life With AI Can Get You Hacked"
author: "Endor Labs"
date_published: "2026-08-18"
date_clipped: "2026-08-24"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# Hacking Your Life With AI Can Get You Hacked

Source: https://www.endorlabs.com/learn/hacking-your-life-with-ai-can-get-you-hacked

## How AI orchestration platforms ship RCE by design

NocoBase, Flowise, Langflow, Dify, Activepieces, Kestra, and Apache Airflow have quietly become critical infrastructure as a result of the agentic AI buildout. They’re used by individuals and enterprises alike to hack personal productivity, build agents, and automate workflows. Langflow and Dify each carry more than 150,000 GitHub stars each, among the most-starred projects in the AI ecosystem. Even the smallest platform in this study, Activepieces, has more than 23,000 GitHub stars.

All seven have become critical infrastructure for developers building AI agents and workflows, but they also all All share the same dangerous assumption:

*"Anyone who can touch a workflow is trusted to run code on the host."*

I went hunting across those seven platforms and walked out with **fourteen critical and high vulnerabilities and multiple public CVEs/GHSAs (7 and growing)**. I collected an arsenal of vulnerabilities and primitives: shell injection, executing user supplied code on validation, prompt injecting LLMs to remote code execution, sandbox bypasses, and unauthenticated APIs that execute code.

The most serious chain needs almost no setup. An unauthenticated user can trigger a prompt injection, executing code and allowing them to exiltrate data, all without ever creating an account or credentials on the platform. With some configurations, Flowise, Kestra, and Langflow could all be exploited without an attacker ever signing in.

Some vendors closed the reports as working-as-designed, on the argument that executing code is the product and hardening the deployment is the developer's problem. That argument holds up until you notice the necessary defenses are either not present or any internet user can execute the code.

Every vulnerability is a variation on the same error. These are multi-tenant code-execution environments, shipped as single-user developer tools, and the threat model has not expanded alongside the products.

As a result, individuals and enterprises building agents with these platforms inherent the permissive threat models they ship by design. These vulnerabilities provide access to sensitive information meant to provide context to AI agents—credentials and access to personal email and calendars for individuals, or customer data for enterprises. Any connector implemented should be treated as a point of compromise.

I presented this research at DEF CON 34 and have published the full technical whitepaper here. I’ve summarized some of the technical findings below.

## The spectrum: from accidental to intentional

The findings from my research sit on a spectrum:

- Accidental: tried to build security but shipped it broken
- LLM as code: trusted LLM output as executable code
- Wrong phase: Built or applied a sandbox but to the wrong phases
- Intentional: Don’t apply a sandbox, leaving it to the builder.

## The accidental end

### NocoBase

On the accidental end, NocoBase built three defenses around its expression evaluator: a SES Compartment, a string preprocessor, and a Proxy guard.

All three had holes. The `lockdown()`

call that arms SES was commented out with a `TODO`

. The Proxy's `has()`

trap returns `true`

for a TypeScript `private`

field, because private is a compile-time fiction that compiles to an ordinary instance property. Every authenticated user could reach the sandbox through an ACL that read `loggedIn`

. One request escalated a member account to `COPY … TO PROGRAM`

on the database host. CVSS 9.9, no malice anywhere. Velocity outran review.

Further right, Flowise and Langflow trusted LLM output as executable code. It reduces to one simple equation:

**LLM output equals user input**

In security, we spent a decade learning not to `eval()`

untrusted user input. Then we wired a language model, which any user can steer through a prompt, directly into an `eval()`

.

### Flowise

Flowise's guard was a 38-pattern regex blocklist over a Pyodide runtime with pandas and numpy pre-imported by the executor, so the model never needed to write `import`

. The word-boundary bug in `\bimport\b `

meant it did not match `importlib`

either. Six independent bypasses passed the validator; one was blocked, `import os`

, the control case.

Here is the end-to-end chain against Flowise 3.1.2:

One `curl`

to `/api/v1/prediction/<uuid>`

, no credential, no account. The prompt tells the model to emit Python assembled from `chr()`

codes. The validator sees no banned identifier because the dangerous names arrive as data and only become text at evaluation. Pyodide runs the code. Pyodide's js bridge reaches Node's own scope, which means `process.mainModule.require('child_process')`

and `execSync`

. The CSV Agent's dataset leaves through the same bridge, straight into the query string of a `_js.fetch().`

### Langflow

Langflow's Smart Transform node made the guard shorter. The whole validator is `startswith("lambda") and ":" in lambda_text,`

followed by `eval(lambda_text).`

A syntactic shape check was promoted to a security boundary. That promotion, a correctness check quietly reclassified as a control, is one of the most common ways this class of bug reaches production.

No API call and no code editor appears in the recording. A single chat message drives the node to emit `lambda x: __import__('os').system('id')`

. The validator confirms the string starts with `lambda`

and contains a colon. `eval`

runs it on the host. This is the shortest available path from a chat box to a shell.

### Dify and Activepieces

Further right, Dify and Activepieces built real sandboxes and applied them to the wrong phase. Dify's `prescript.py`

runs a server-supplied `{{preload}}`

string before `lib.DifySeccomp(...) `

is called. Chroot, no-new-privs, seccomp filter, uid drop, every control the sandbox has, in one call, after the attacker's string has already run. I confirmed `euid = 0, NoNewPrivs: 0`

, and a read of `/etc/shadow`

from the preload phase against `dify-sandbox:0.2.15.`

Activepieces makes the identical mistake one layer up, in the module-loading phase of a V8 isolate. `require() `

runs the module body in the host Node process before .`toString()`

on the exported function ever reaches the isolate.

## The intentional end: trust boundaries that describe a different product

Kestra and Airflow are the interesting cases, because both vendors initially closed the reports as working-as-designed. Their argument is coherent, and I want to state it before disagreeing with it. To summarize, executing scripts is the product. Hardening the deployment is the operator's job. I think most of that argument holds.

### Kestra

Kestra's maintainer points at least-privilege on workflow creation as the recommended control: "only trusted users have permission to create and execute workflows." But that is also the gap. Execution is not gated by that permission when a webhook trigger exists, and Kestra webhooks are unauthenticated by default.

A single flow uses `{{ trigger.body.command }}`

inside `beforeCommands`

. Pebble renders it, `ScriptService`

concatenates it into a single string, `/bin/sh -c`

executes it. The curl comes from outside any authentication boundary. `/tmp/pwned`

appears on the Kestra host.

### Airflow

Airflow's case turned on documentation. `BashOperator`

renders `bash_command`

through Jinja2 with `dag_run.conf`

values supplied at trigger time, then hands the string to `subprocess.run(["bash", "-c", ...])`

. The vulnerable pattern appears three times in Airflow's own docs, treated three different ways: the getting-started guide teaches it as the primary example with no warning, the provider docs carry a caution block, and the operator docstring says "DO NOT DO THIS".

Jarek Potiuk on the Airflow security team accepted the CVE once the internal inconsistency was specific. The fix in 3.2.0 is documentation-only. The sink is unchanged, which means every DAG already written against the old example is still vulnerable and needs auditing by hand.

## The patterns

I observed five patterns across all fourteen vulnerabilities. Most of these will sound familiar to any security researcher or software engineer working today:

- Velocity is outpacing code and security review
- LLM output is trusted as code
- Sandbox escape via execution ordering
- Trust boundary mismatch
- Documentation as attack surface

Every sandbox in this study failed for a reason unrelated to the sandbox's own strength. The primitives were sound, but they failed on composition: what runs before them, what leaks into them, whether they were switched on. Reviewing the primitive tells you little. Reviewing the wiring tells you a great deal.

## For operators

Treat every trigger endpoint like an exposed SSH port. Put authentication in front of `/api/v1/prediction/<uuid>`

(Flowise), `/api/v1/executions/webhook/...`

(Kestra), and `/api/v2/dags/{id}/dagRuns`

(Airflow). Configuring Flowise auth does not cover the prediction path, because that path is on the server's whitelist. Front it with a reverse proxy.

Scope permissions as code execution rather than "just a workflow." Trigger permission equals the author's code privilege, explicitly on Airflow and Kestra. Kill the dangerous default flags: `SANDBOX_ENABLE_NETWORK`

on Dify, `LANGFLOW_SKIP_AUTH_AUTO_LOGIN`

on Langflow, `enable_preload`

on Dify. Override `dify-sandbox`

as the default API key.

Upgrade where a patch exists: NocoBase 2.0.39, Langflow 1.10.3 or 1.11.0, Activepieces 0.80.0, Airflow 3.2.0 (documentation only, so existing DAGs still need auditing). Kestra and Dify have no patch for the findings above by vendor decision, so apply the compensating controls.

Flowise is the case where upgrading stops being the answer. Development ceased on 2026-07-29 and the repository was archived on 2026-08-10, so plan a migration and treat any running instance as unmaintained software with credentials attached.

## Results

Here is the full list, shown on the spectrum from accidental to intentional as explained above:

Three advisories were not public at the time of my presentation but followed our 90+30 disclosure timeline. For the NocoBase SES escape the code is fixed upstream and the advisory is pending. For the two Langflow advisories the fix status is undetermined, since I could not observe whether a fix has shipped.

## Takeaway

Until vendors admit these are code-execution platforms and secure them accordingly, these bugs will keep shipping, by design.

The full technical breakdown is in the whitepaper.

### What's next?

When you're ready to take the next step in securing your software supply chain, here are 3 ways Endor Labs can help:
