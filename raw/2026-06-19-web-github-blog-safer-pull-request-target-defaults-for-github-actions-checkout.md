---
source: "https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/"
title: "Safer pull_request_target defaults for GitHub Actions checkout"
author: "unknown"
date_published: "2026-06-18"
date_clipped: "2026-06-19"
category: "DevOps & CI/CD"
source_type: "web"
---
# Safer pull_request_target defaults for GitHub Actions checkout

The `pull_request_target`

event is one of the most commonly misused triggers in GitHub Actions, leading to vulnerabilities in workflows. Workflows triggered by `pull_request_target`

run with the base repository’s `GITHUB_TOKEN`

, secrets, and default-branch cache access. Checking out the head of an unreviewed pull request from a fork inside one of these workflows typically lets attacker-controlled code execute with the workflow’s full privileges. This pattern is known as a “pwn request,” and it has been the root cause of multiple supply-chain incidents across the ecosystem. For more information, see our blog posts about helping to prevent these requests.

Starting today, `actions/checkout`

v7 is generally available and refuses common pwn request patterns by default.

On July 16, 2026, we’ll backport the enforcement to all currently supported major versions. Workflows pinned to a floating major tag (e.g., `actions/checkout@v4`

) will automatically pick up the change. Workflows pinned to a specific SHA, minor, or patch version aren’t affected by the backport and will need to upgrade using Dependabot or through established upgrade processes.

Same-repository pull requests aren’t affected, and the `pull_request`

event is unchanged.

### What’s changing

`actions/checkout`

v7 refuses to fetch fork pull request code in `pull_request_target`

and `workflow_run`

workflows (the latter only when `workflow_run.event`

is a `pull_request*`

event). It refuses when the pull request is from a fork and any of the following apply:

`repository:`

resolves to the fork pull request’s repository.`ref:`

matches`refs/pull/number/head`

or`refs/pull/number/merge`

.`ref:`

resolves to a fork pull request’s head or merge commit SHA.

This change is focused on preventing the most common form of pwn requests in the Actions ecosystem. `actions/checkout`

will now fail for usage in `pull_request_target`

events from forks with insecure inputs such as:

`ref: refs/pull/${{ github.event.pull_request.number }}/merge`

`ref: ${{ github.event.pull_request.head.sha }}`

`repository: ${{ github.event.pull_request.head.repo.full_name }}`


### What’s not changing or covered

Pwn requests can be introduced in other ways outside of the scope of this change. For example, a `run`

block uses `git`

or the `gh`

CLI to pull a HEAD ref or other untrusted source that is subsequently executed. Additionally, pwn requests triggered in other event types besides `pull_request_target`

(such as `issue_comment`

) will not be blocked by this change. Further hardening of additional events may be explored in future releases.

This change only blocks checkouts of the fork pull request head and merge commits. It does not block checkouts of other untrusted repositories. For example, setting `repository:`

to an unrelated third-party repository is not blocked. Checking out and executing any untrusted code in a privileged event remains a pwn request risk that should be reviewed.

### Opting out of this protection

Some workflows need to check out fork pull request code with elevated trust, and this is why `pull_request_target`

was created in the first place. For example, generating coverage reports that require a private artifact registry or producing and running authenticated checks against the changes introduced from the pull request. We’re keeping an opt-out available so these workflows can continue to function, but you should treat opting out as a deliberate security decision.

Before you opt out, read our guidance for securely using `pull_request_target`

. After confirming the event is needed and safely used in your workflow, you can opt out of this protection by adding the `allow-unsafe-pr-checkout`

input on the `actions/checkout`

step. The flag is intentionally named to be easy to spot in code review and static analysis.

### Read more and give your feedback

For more details, see the `actions/checkout`

repository, the GitHub Actions documentation on `pull_request_target`

, and the security hardening guidance for GitHub Actions.
