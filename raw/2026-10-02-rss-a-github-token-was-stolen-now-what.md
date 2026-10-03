---
source: "https://www.invictus-ir.com/news/a-github-token-was-stolen-now-what"
title: "A GitHub token was stolen. Now what?"
author: "unknown"
date_published: "2026-09-30"
date_clipped: "2026-10-02"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-10-01"
---

# A GitHub token was stolen. Now what?

# A GitHub token was stolen. Now what?

## One compromised Personal Access Token can reach every repository an identity can touch. How to scope the damage, trace the theft, and harden against the next one.

### TL;DR

A single compromised GitHub Personal Access Token (PAT) can expose every repository an identity can reach, and the real damage is the secrets and credentials inside those repositories. Scoping what the token could reach, investigating how it was stolen, and hardening against the next one is where the incident is actually won or lost.

- Classic PATs create the largest blast radius because they inherit the identity's full repository access, so start by identifying which token type was compromised.
- Scope to what your telemetry proves was touched, but where logging is missing, treat the blast radius as everything the token could reach.
- Reduce future risk by migrating off classic PATs to fine-grained tokens or GitHub Apps and enforcing organization wide lifetime and access policies.

### Introduction

Invictus has been busy handling incidents throughout 2026, and the heart of these cases are GitHub PATs. The scenario is fairly straightforward with a threat actor gaining access to a single token with enough permissions to clone every repository the user has access to. Within a short period of time, large amounts of source code is exfiltrated.

As bad as this sounds, theft of the source code is only the beginning of the issue, since secrets, API keys, cloud credentials and other tokens live in those repositories. Each working credential can give the threat actor access to another system, which may contain even more data and credentials. What started with one stolen token quickly snowballs into something much more serious.

INVICTUS · INCIDENT RESPONSE

How one stolen token becomes *a larger incident*

The token is only the way in. The credentials inside the repositories carry the threat actor further.

- Token stolen
- Repositories mapped
- Targets chosen
- Repos cloned, secrets hunted
- Other systems reached, persistence established

And this raises an uncomfortable question most organizations struggle to answer, which is what would happen if all the secrets or keys in your repositories were compromised today? Invictus has seen in recent cases, organizations struggle with the reality that they don’t know which secrets are valid, their ownership, their usage, and the massive effort required to rotate all of them, while trying not to break production systems.

One detail ties many of these cases together. The compromised token is almost always a classic PAT rather than a fine-grained one. If you know the difference, you probably already know why that matters. If not, it's worth understanding how a PAT compromise actually unfolds.

### The anatomy of a PAT compromise

Tokens end up wherever credentials get left behind, including browsers, configuration files, environment variables, credential stores, and endpoints themselves. Threat actors obtain them with info-stealer malware via compromised workstations, through malicious browser extensions, or by running secret discovery tools like TruffleHog against repositories and Git history.

Invictus has observed that developer endpoints receive the most attention and the logic is simple. One workstation can hold source code, development tooling, and stored credentials at once, which makes a single compromise highly valuable.

With a working token in hand, the threat actor needs to know what the compromised identity can actually reach. In recent cases that reconnaissance has looked like automated repository enumeration against the GitHub API. The threat actor queries repository endpoints at scale, including */repositories/{id}/readme, which can generate thousands of api.request events in a short window. That sweep maps every repository the identity can see, surfaces the valuable ones, and lets the threat actor prioritize targets before cloning and secret hunting.

INVICTUS · INCIDENT RESPONSE

What enumeration looks like *in the audit stream*

Enumeration is loud. One token accessing every repository leaves thousands of api.request events in minutes, if they are being streamed.

02:14:07 api.request GET /repositories/10231/readme 200

02:14:07 api.request GET /repositories/10232/readme 200

02:14:07 api.request GET /repositories/10233/readme 404

02:14:08 api.request GET /repositories/10234/readme 200

02:14:08 api.request GET /repositories/10235/readme 200

⋮ thousands of these in minutes, one per repository

Reconnaissance as described is loud, but only for defenders who have the telemetry and detections to see it. We'll come back to that in the next section. From there the incident rarely stays inside GitHub. Source code, configuration files, and Git history routinely expose more credentials, for cloud platforms, SaaS applications, CI/CD pipelines, databases, and internal systems. A single stolen PAT becomes the way into all of it.

The impact can also reach well beyond the compromised organization. In a public repository, a threat actor could submit a malicious pull request from a threat actor controlled account, then use the compromised developer identity to approve and merge it wherever repository rules allow. If that change later makes it into a release, what began as a stolen PAT can turn into a software supply chain attack affecting every organization or user that consumes the compromised software.

This is what makes these cases so hard to scope. What you can see in GitHub is usually just the first layer, and knowing which repositories were touched is only the start. The question that actually sets the size of the incident is what else that token could reach, and how much of it the threat actor got to before anyone noticed.

### Before you investigate, know your GitHub telemetry

What GitHub can tell you about a PAT compromise is mostly decided before the compromise happens. Evidence is scattered across different logs, and which of those logs exist depends on the organization's configuration and licensing. Some of the most useful activity is only available with Enterprise features or with logging that was set up in advance. So the practical quality of a PAT investigation is largely fixed before responders are ever called, which is why the first step is knowing exactly what your telemetry does and does not capture.

INVICTUS · INCIDENT RESPONSE

What each GitHub plan can tell you *during a PAT compromise*

Only Enterprise records repository cloning, and api.request events only arrive if streaming was switched on before the incident.

| Capability | Free | Team | Enterprise |
|---|---|---|---|
| Personal security log User-level security events for the affected account | ✓ | ✓ | ✓ |
| Organization audit events Admin and security activity in the organization | — | ✓ | ✓ |
`git.clone` / `git.fetch` / `git.push` Shows repository cloning, fetching and pushing. Kept 7 days | — | — | ✓ |
| Audit Log API Collect and query audit and Git events programmatically | — | — | ✓ |
| Enterprise audit log Correlate activity across organizations | — | — | ✓ |
| Audit-log streaming Send telemetry to a SIEM or storage for longer retention | — | — | ✓ |
`api.request` events*Shows API enumeration and other API activity | — | — | ✓* |

*`api.request`

events are only available through audit log streaming and must be explicitly enabled. This is the telemetry used to identify API reconnaissance such as requests to `/repositories/{id}/readme`

.

Two retention facts decide how much of the investigation survives:

- Git events, as shown in the third row of the table above, are kept by GitHub for only seven days. So, if they weren't streamed or otherwise collected, evidence of repository cloning may already be gone before the incident is even discovered.
[The organization audit log runs longer, 180 days,](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization)but by default the GUI shows only the last three months by default.

INVICTUS · INCIDENT RESPONSE

GitHub keeps Git events for 7 days. *Stream them yourself.*

By the time most compromises are detected, the day-0 clone record is gone and API requests were never kept. Only your own log stream still has them.

### Investigating a PAT Compromise

#### Scope: Token Types

Start by determining whether the compromised token is a classic or fine-grained PAT. The distinction matters because it can completely change the potential blast radius.

Invictus most commonly encounters classic PATs during these investigations, and they tend to create the largest blast radius. Classic PATs use broad scopes and inherit the repository permissions of the compromised identity. A classic PAT with the repo scope, for example, can reach any private repository that identity is authorized to open. One stolen token can therefore turn into access across a significant number of repositories.

Fine-grained PATs offer much tighter control. They can be restricted to a specific resource owner, limited to selected repositories, assigned individual permissions, and given an expiration date. If one is compromised, the exposure is usually far smaller.

There's also a third tangential case, which is a GitHub App. Here the compromised artifact is usually the App's private key rather than a token, and that key mints installation tokens on demand. Identify it early, because its blast radius tracks the App's installations, not one user's access.

INVICTUS · INCIDENT RESPONSE

Know what kind of credential *you found*

The credential type sets the ceiling. Identify it before you scope anything.

| Prefix | What it is | Ceiling if stolen |
|---|---|---|
`ghp_` | Classic PAT | Every repository the user can reach, within its scopes |
`github_pat_` | Fine-grained PAT | Only the repositories and permissions it was issued for, until it expires |
`gho_` | OAuth App access token | Every repository the user can reach, within the scopes they granted the OAuth App, until revoked |
`ghu_` | GitHub App user access token | Only where the user's access and the App's installation overlap, for eight hours |
`ghr_` | GitHub App refresh token | New `ghu_` tokens for six months, if the App's client secret is also stolen |
`ghs_` | GitHub App installation token | That installation's repositories, for one hour |
| none | GitHub App private key | Every installation of the App, until the key is rotated |

#### Assess: Blast Radius

The blast radius is assessed based on what the token could reach relative to what the threat actor can be proven to have touched. The ceiling comes from the token. A classic PAT with repo scope could reach every repository the compromised identity can access, private ones included. However, a fine-grained token is bound by the repositories and permissions it was issued for.

A GitHub App changes the shape of the blast radius, not just its size. If the stolen credential is the App's private key, the ceiling is every repository and permission across all of its installations, because the key can generate fresh tokens for every repository the App is installed on, indefinitely. Revoking a token does nothing. Containment means rotating the key and reviewing installations. Invictus has seen exactly this, an App key stolen and used to authenticate directly, and a widely installed App can be a bigger prize than any single PAT.

INVICTUS · INCIDENT RESPONSE

Define the *floor and ceiling* of your evidence

Anything the logs cannot clear stays in scope, so the incident is sized at the ceiling.

The floor comes from telemetry. Events such as git.clone and git.fetch show which repositories were pulled, and api.request events expose the reconnaissance before it. The evidence can be thin, but on [Enterprise Cloud, Git events](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/audit-log-events-for-your-organization) are available through the REST API only, with seven-day retention, and a clone never appears in the web interface. Unless they were streamed somewhere, the record of what was cloned is usually gone before the investigation begins.[ ](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/audit-log-events-for-your-organization)

So the scoping rule is simple. Where you have the telemetry, scope to what it shows. Where you don't, the blast radius is the ceiling, not zero, because a missing git.clone event is proof the logging wasn't there, not proof the repository was untouched.

From there it becomes a secret discovery problem. For every repository in scope, assume the full contents and Git history are in the threat actor’s hands, then answer three things:

- What credentials were in the code?
- Are they still valid?
- What does each one unlock?

That is what turns one stolen PAT into cloud, SaaS, and CI/CD exposure, and what sizes the incident.

#### Investigate: Initial Access

One of the hardest questions to answer is often not what the threat actor did with the PAT, but how they obtained it in the first place. GitHub can show you activity after a credential is used, but it cannot tell you how that credential was stolen. This is where endpoint and external threat intelligence become important.

If you have access to EDR telemetry, investigate the affected endpoint around the first known malicious GitHub activity. Look for info-stealer execution, suspicious browser or credential store access, malicious extensions, unusual shell activity, archive creation, or processes interacting with developer tooling and configuration files.Furthermore, info-stealer or credential exposure intelligence has proven valuable in Invictus investigations. Check whether the affected user, hostname, or corporate domain appears in known stealer log datasets.

The token may not have come from an endpoint at all. Check whether it was exposed via public repositories, Git history, code snippets, build artifacts, config files, and other places where developers may have inadvertently committed or published it. Tools such as TruffleHog can search repositories and their history for exposed credentials, and for GitHub tokens you can also review GitHub's secret scanning detections and any available alerts to see whether the token was flagged in a repository before.

Finally, look at where the token itself may have been stored. For example, Git credential helpers, GitHub CLI authentication, environment variables, configuration files, CI/CD tooling, or plaintext scripts. The goal is not only to explain how the PAT was lost, but to determine what else the threat actor could have taken from the same endpoint.

#### Recover: Follow the Secrets

Assume every secret in a cloned repository is compromised until proven otherwise. Revoking the original PAT prevents further use of that credential, but it does not undo the access the threat actor already had. In one recent incident, a compromised token resulted in the cloning of approximately 300+ repositories. Invictus identified more than 1,100 potential secrets across the affected repositories and their Git history, including credentials associated with AWS, Azure, GCP, GitHub, Slack, and Snowflake.

INVICTUS · INCIDENT RESPONSE

What one compromised GitHub token *exposed*

One token exposed more than 1,100 potential secrets, and working through them took more than 30 people over a week.

Finding the secrets was the easy part. Validating and rotating them became the real work. Each one had to be checked to determine whether it was still valid, what it unlocked, where it was used, who owned it, and whether revocation would break a production system.

For an incident of this size, that is not a task for the security team alone. More than 30 people across security, IT, and engineering spent over a week working through the exposed credentials. Some could be revoked immediately; others required owners to be identified, dependencies mapped, replacements deployed, and applications monitored before the old credential could safely be disabled.

The risk also changes as the process continues. A valid AWS credential may expose further secrets in Secrets Manager, and a CI/CD credential may open up deployment environments. Each working credential can therefore expand the scope of the incident and create another investigation and rotation task. Revoking the stolen PAT takes seconds. Recovering from everything it exposed can take weeks.

#### Harden: Reduce the Risk

Start with inventory. Identify the classic PATs still in use, put the broad scoped ones first (repo, admin:org, workflow), and for each one decide whether it can move to a fine-grained PAT scoped to named repositories and permissions, or to a mechanism that isn't a long lived user credential at all; or a GitHub App or OIDC for automation, where the tooling supports it. Fine-grained tokens also expire by default, with the organization maximum lifetime set[ to 366 days by default](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization), so the migration buys an expiry that does not exist today.[ ](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization)

For automation, the better destinations aren't tokens at all. A GitHub App authenticates as its own identity, not a person, using installation tokens that expire after 1 hour, scoped to only the permissions it needs. Nothing breaks at offboarding, and a leaked token dies in an hour. For cloud access from workflows, OIDC removes the stored credential entirely. The workflow pulls a short lived token straight from the cloud provider, valid for a single job and then automatically expires, with no static key in a secret store to be cloned with the repo. This only covers cloud provider authentication, so third party keys like Slack or Snowflake still live as secrets.

INVICTUS · INCIDENT RESPONSE

What a threat actor gets, from weakest to *strongest setup*

Each step down shrinks what a stolen credential is worth.

| Setup | Acts as | Lifetime | If stolen |
|---|---|---|---|
| Classic PAT | A person | May never expire | Every repository the person can reach |
| Fine-grained PAT | A person | Expires. Org maximum 366 days by default | Only the named repositories and permissions |
| GitHub App | Its own identity | Installation tokens last 1 hour | Its installations. A stolen private key mints new tokens |
| OIDC | The workflow | One job | No stored cloud credential. Third-party keys still live as secrets |

Moving off classic PATs is rarely a clean swap. Legacy tooling and automation may depend on them, and replacing a token without understanding those dependencies breaks production. Treat it as a migration, not a rotation. Find the owner, map where the credential is actually used, cut its permissions to the minimum, give it an expiration, and remove it once nothing depends on it. The objective is not to make token theft impossible, as much as everyone would like that. It is to make sure the next stolen token cannot expose half the company.

### Conclusion

A stolen PAT is rarely the whole incident. Get ahead of it now by inventorying your classic PATs, migrate the broadly scoped ones, and set organization controls before a threat actor forces the issue. If you are working through a suspected PAT compromise and need help, Invictus is here.

We are an incident response company and we ❤️ the cloud. We specialize in supporting organizations in preparing for and responding to cyber attacks across AWS, Azure, Google Cloud, and beyond. We help our clients stay undefeated.

🆘 For incident response support reach out to cert@invictus-ir.com or go to[ https://www.invictus-ir.com/24-7](https://www.invictus-ir.com/24-7)
