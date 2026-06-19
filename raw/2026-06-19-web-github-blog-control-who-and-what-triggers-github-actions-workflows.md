---
source: "https://github.blog/changelog/2026-06-18-control-who-and-what-triggers-github-actions-workflows/"
title: "Control who and what triggers GitHub Actions workflows"
author: "unknown"
date_published: "2026-06-18"
date_clipped: "2026-06-19"
category: "DevOps & CI/CD"
source_type: "web"
---
# Control who and what triggers GitHub Actions workflows

Workflow execution protections are now in public preview for GitHub Enterprise, organizations, and repositories. This new capability lets enterprise administrators define an allow list that controls who can trigger GitHub Actions workflows and which events are permitted to run them, giving you predictable, secure workflow execution.

Previously, a workflow ran based on the workflow file in the commit that triggered it. An attacker with repository access could modify that file to run malicious code. Workflow execution protections close that gap. Administrators define the rules and GitHub Actions evaluates them before a run, so an unauthorized actor or event can never trigger an unwanted workflow execution.

## One policy, every repository

Workflow execution protections are built on the GitHub rulesets framework, so the targeting you already know from rulesets works here too. You can apply protections across your enterprise with organization-wide rulesets and scope them to specific repositories using repository custom properties. That means you stop reasoning about security one YAML file at a time and instead make broad protections visible and enforceable in one place. You can also use evaluate mode to run your rules in shadow, so you can see exactly what a rule would block before you enforce it and roll out policies. This helps prevent you from breaking existing workflows.

## Two rule types to start

Event and actor are the first two rule types, and we’ll add more over time.

**Actor rules**control who can trigger workflows, including individual users, repository roles (e.g.,`Read`

,`Maintain`

, and`Admin`

), GitHub Apps, Copilot, and Dependabot.**Event rules**control which events are permitted, such as`push`

,`pull_request`

,`pull_request_target`

, and`workflow_dispatch`

.

By default, every user with write access to a repository can trigger workflows. Actor rules let you separate who contributes code from who runs your CI, so you can grant a contributor write access without granting them the ability to execute workflows.

## Stop common attacker techniques

Workflow execution protections disrupt several real-world attack patterns:

**Poisoned pipeline execution from pull requests:**Restrict or prohibit`pull_request_target`

across your organization, including in public repositories where it’s most often exploited.**Manual-trigger abuse:**Limit`workflow_dispatch`

to maintainers so untrusted identities can’t kick off workflows.**Untrusted-actor execution:**Block low-trust identities from triggering workflows entirely.**Misconfiguration exploitation:**Apply central policy that short-circuits any single misconfigured workflow file.

## Getting started

You’ll find workflow execution protections in your organization and repository settings under “Actions”, in the new “Policies” section. This “Policies” section is new and separate from your existing “General” Actions settings.

To learn more, read about workflow execution protections in the GitHub Actions documentation.

Join the discussion within GitHub Community.
