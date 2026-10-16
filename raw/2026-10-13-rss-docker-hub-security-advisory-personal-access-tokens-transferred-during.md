---
source: "https://www.docker.com/blog/docker-hub-security-advisory-cve-2026-105445"
title: "Docker Hub security advisory: personal access tokens transferred during account-to-organization conversions"
author: "Mark Lechner"
date_published: "2026-10-12"
date_clipped: "2026-10-13"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# Docker Hub security advisory: personal access tokens transferred during account-to-organization conversions

On September 30, 2026, security researchers reported a vulnerability in Docker Hub’s identity and access management through our Vulnerability Disclosure Program. We confirmed the report and deployed a fix to production the same afternoon, less than four hours after receiving it. We then reviewed every account conversion back to the date the flaw was introduced, and on October 2, notified every user and organization owner whose account could have been impacted by this vulnerability. This post explains what the vulnerability was, what it could and could not do, what we found, and what we have changed.

We want to thank Peter Molnar and Krisztian Hozak of mptrdev.com for finding the issue, reporting it responsibly, and coordinating disclosure with us. Their technical write-up is available at [ghostpat.com](https://ghostpat.com). This issue is tracked as CVE-2026-105445.

## Was I or any member of my organization exposed to the vulnerability?

On October 2 at 5:30PM EST, we sent out an email with the subject line “Docker Hub Vulnerability Identified & Resolved” to the limited number of users exposed to this vulnerability. If you did not receive an email, you and any members of the organizations you administer were not exposed and there are no actions for you to take.

## What the vulnerability was

Docker Hub lets you convert a personal account into an organization. People do this because Hub has no way to move a repository from one account to another: conversion is how alice/app becomes an organization-owned alice/app without breaking every Docker pull that references it. During conversion, the user names an existing Docker Hub account as the new organization’s owner.

Beginning  August 26, 2024, conversion also re-assigned the converted account’s personal access tokens (PATs) to that new owner. It did this by changing the token’s owner record, without rotating or revoking the token secret. The named owner was not asked to confirm and was not notified. Together, those two gaps made the following possible:

1. An attacker creates an account and generates a PAT on it.
2. The attacker converts that account to an organization and names a target user as the owner.
3. The attacker’s PAT is re-assigned to the target user. The attacker still holds the secret and the PAT remains active now with the target user’s scope.
4. The token now authenticates to the registry as the target user.

## What an attacker could and could not do

Within the scope of the token, a re-assigned PAT acted as the target user at the registry level, meaning an attacker could potentially pull, push, and/or delete images in the target’s repositories and in organizations where the target had access. Because that includes publishing images under a legitimate name, we treated this as a software supply chain risk and rated it critical.

The vulnerability did not give access to the Docker Hub web interface, and it could not be used to change the target’s password, email address, or two-factor settings, or to take over the account.

The exposure window ran from August 26, 2024, 20:33 UTC, until the fix was deployed on September 30, 2026, at approximately [19:10] UTC.

## Timeline (all times U.S. Eastern)

* **Sept 30, 11:40 AM:** Report received at security@docker.com.
* **Sept 30, ~1:30 PM:** We independently reproduced the issue with internal test accounts.
* **Sept 30, ~3:10 PM:** Fix deployed to production and verified against the original proof of concept. Conversion no longer transfers PATs.
* **Sept 30, ~3:23 PM:** Documentation updated to state that PATs do not transfer and must be recreated by the new owner, with organization access tokens recommended.
* **Sept 30, 4:59 PM:** Researchers informed of the fix. Both parties agreed to coordinate disclosure.
* **Oct 2, 5:30 PM:** Exposed users and their organization owners notified by email.
* **Oct 8, 3:45 PM:** Forced deactivation of all PATs transferred through conversion, except where the account holder opted out.

## What we investigated and found

We enumerated every account conversion performed since August 26, 2024 and correlated them with registry authentication logs, Docker Hub usage data, and IAM token records. We looked for any token used under more than one identity, and we examined every push made with a transferred token, about 304,000 in all.

**We found no evidence that the vulnerability was exploited.**

* Every push made with a transferred token landed either in the converted organization’s own repositories or in the new owner’s own repositories. None went into an unrelated user’s or organization’s account. In the large majority of cases, the account converted and the account named as owner belonged to the same person or team, which is the normal, legitimate use of this feature.

* We statically analyzed the highest-risk public images without executing them: images pushed after a conversion where we could not establish that the same person controlled both accounts. We found no malware, cryptominers, command-and-control activity, credential harvesting, persistence, or tampering.
* We found no evidence that Docker’s own infrastructure or services were affected.

We also want to be clear about the limits of that finding:registry logs show when a token is used, not that it exists, so a transferred token that was never used leaves no trace. For that reason, we did not rely on detection to decide who was exposed. We treated every PAT that moved through conversion during the window as potentially affected, whether or not we saw it used.

## What we did for affected users

On October 2, we emailed the limited number of users whose accounts received transferred PATs. Each email listed the in-scope tokens by description and creation date so users could find them in Docker Hub. We separately notified the associated organization owners. On October 8th at 3:45 PM EST, we deactivated the identified transferred PATs. Tokens that their owners asked to keep before the deadline were excluded.

Once again, if you did not receive the above email, no PAT on your account was transferred through this flow. Your account was therefore not exposed to this vulnerability and there is no action for you to take.

## What we are changing

The immediate fix removed PAT transfer from conversion entirely. Beyond that, we are now:

* requiring consent from a user before they are named as an organization owner, and notifying them when it happens;
* recording an auditable history of every token ownership change, so questions like this can be answered from records rather than inference;
* reviewing other flows that change credential ownership for the same pattern.

## What you can do

Review the personal access tokens on your account in Docker Hub under Account settings, Personal access tokens, and revoke any you don’t recognize or no longer use. For automation that belongs to an organization, use organization access tokens rather than a person’s PAT. If you have questions about this notice, contact Docker Support at [app.docker.com/support/contact](https://app.docker.com/support/contact).

Responsible disclosure works when researchers and vendors treat each other as partners. Peter and Krisztian did that here, and our users are safer for it. If you find a security issue in a Docker product, please report it to [security@docker.com](mailto:security@docker.com).
