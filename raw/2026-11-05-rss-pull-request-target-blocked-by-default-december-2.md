---
source: "https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2"
title: "pull_request_target blocked by default December 2"
author: "Allison"
date_published: "2026-11-02"
date_clipped: "2026-11-05"
category: "Security & Ethical Hacking"
source_type: "rss"
canonical_url: "https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/"
source_last_modified: "2026-11-02"
---

# pull_request_target blocked by default December 2

![](https://github.blog/wp-content/themes/github-2021-child/assets/img/featured-v3-deprecations.svg)

Starting December 2, 2026, GitHub Actions will block `pull_request_target` events by default in all public repositories, unless an applicable Actions event policy explicitly allows them. Enforcement was previously scheduled for November 2, 2026.

GitHub introduced this default rule through workflow execution protections. The rule initially runs in evaluate mode, so you can see which workflow runs it would block before enforcement begins.

Private and internal repositories aren’t affected.

## [Why we’re making this change](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/#why-were-making-this-change)

`pull_request_target` runs in the context of the base repository and can access its secrets. If a workflow executes untrusted code from a fork, that code could compromise your pipeline or steal secrets. The default rule helps reduce this risk while letting you explicitly allow workflows that depend on the trigger.

## [Brownout schedule](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/#brownout-schedule)

Before permanent enforcement begins on December 2, 2026, we’ll temporarily enforce the default protection during two scheduled brownouts. These windows will help you identify affected workflows and update your policies before enforcement becomes permanent.

| Date | Time (UTC) |
| --- | --- |
| November 9, 2026 | 16:00–18:00 |
| November 16, 2026 | 16:00–18:00 |

During each window, `pull_request_target` workflow attempts blocked by the default rule in affected public repositories will create failed runs with an error annotation; the workflows won’t execute. After each window, the default rule will return to evaluate mode, allowing workflows to run with warnings. Private and internal repositories aren’t affected.

## [Prepare your workflows](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/#prepare-your-workflows)

Before the first brownout on November 9, use Insights to see which workflow runs the rule would block. From there, you have two options:

- Keep the default rule in place to block `pull_request_target`.
- Explicitly allow `pull_request_target` in an applicable Actions event policy if your workflows depend on it. Use workflow file targeting to allow specific workflows.

See [how to control workflow execution](https://docs.github.com/actions/how-tos/administer/control-workflow-execution) to configure your policies.

This change applies to public repositories on GitHub Free, GitHub Team, and GitHub Enterprise Cloud, not GitHub Enterprise Server.
