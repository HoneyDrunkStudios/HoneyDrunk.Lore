---
source: "https://github.blog/changelog/2026-11-17-secret-scanning-on-demand-for-developers-and-agents/"
title: "Secret scanning on demand for developers and agents"
author: "Allison"
date_published: "2026-11-17"
date_clipped: "2026-11-20"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Secret scanning on demand for developers and agents

Secret scanning should keep pace with the way you build software, whether you write code yourself or work with an AI agent. Copilot’s security review specialist now runs GitHub secret scanning, so developers and agents can catch secrets in code changes before they’re merged.

You can use the public preview in Copilot CLI and Copilot app sessions, through Copilot SDK integrations, and in Copilot code review.

### [What’s new](https://github.blog/changelog/2026-11-17-secret-scanning-on-demand-for-developers-and-agents/#whats-new)

Copilot security review already looks for exposed secrets as part of its LLM-based review. Once you opt in, it also runs GitHub’s secret scanning detectors alongside that analysis.

- **Provider patterns:** Detect more than 500 secret types from GitHub’s growing catalog, built with [150+ industry partners](https://github.com/security/advanced-security/secret-protection?utm_source=secret-scanning-changelog-secret-protection-docs&utm_medium=changelog&utm_campaign=ignite-nov-2026) through the [secret scanning partner program](https://docs.github.com/code-security/secret-scanning/secret-scanning-partnership-program/secret-scanning-partner-program?utm_source=secret-scanning-changelog-partner-program-docs&utm_medium=changelog&utm_campaign=ignite-nov-2026).
- **GitHub’s fine-tuned model for secret detection:** Not every credential has a recognizable format. The model reads surrounding code to identify likely secrets, including passwords and credentials in connection strings.

The review checks your changes for secrets. It doesn’t search repository history.

### [Secret scanning in your workflow](https://github.blog/changelog/2026-11-17-secret-scanning-on-demand-for-developers-and-agents/#secret-scanning-in-your-workflow)

- **Review changes as you work.** In Copilot CLI and the Copilot app, ask your coding agent to run the `security-review` specialist. Use its findings to make fixes and request another review, or run `/security-review` yourself on your changes or an agent’s work.
- **Build checks into your own agents.** With the Copilot SDK, your agent can request a security review before returning its changes, without maintaining separate secret detectors.
- **Catch secrets during pull request review.** Copilot code review can flag secrets on added lines, including changes that weren’t checked during development, so authors and reviewers can address them before merge.

### [Enable secret scanning](https://github.blog/changelog/2026-11-17-secret-scanning-on-demand-for-developers-and-agents/#enable-secret-scanning)

Secret scanning is off by default. Until you opt in, security review uses its existing LLM-based detection only.

Enable secret scanning for your tool, then request a review:

| Tool | Enable secret scanning | Run a scan |
| --- | --- | --- |
| Copilot CLI | In an interactive session, run `/settings aiSecretDetection on`. | Delegate to `security-review` through the `task` tool (`agent_type: "security-review"`), or run `/security-review` manually. |
| Copilot app | In **Settings > Experimental**, turn on **AI secret detection**. | Delegate to `security-review` through `task`, or run `/security-review` manually. |
| Copilot SDK integrations\* | When you create a session, set the `SECURITY_REVIEW_FINE_TUNED_MODEL` feature flag to `true`. Configure GitHub authentication on the SDK client, such as with a token obtained through GitHub CLI sign-in. | Delegate from the session agent, or call `session.rpc.tasks.startAgent` with `agentType: "security-review"`. |
| Copilot code review | In the repository’s **Settings > Copilot > Code review**, turn on **Secret scanning** under **Security**. | Request a review from **Copilot** on the pull request, or set up automatic reviews. |

\*For SDK integrations: A model-provider API key alone is not sufficient. Tokens issued by your integration’s own OAuth app are not currently supported for secret scanning. VS Code support is not included in this release.

*Editor’s note (November 18, 2026): This post was updated to clarify authentication requirements for Copilot SDK integrations.*

### [Availability and billing](https://github.blog/changelog/2026-11-17-secret-scanning-on-demand-for-developers-and-agents/#availability-and-billing)

No additional plan is required for the Copilot experiences listed above. SDK integrations must meet the authentication requirements described above. Scans consume AI credits under the Secret Protection AI Credit SKU.

### [Learn more and share feedback](https://github.blog/changelog/2026-11-17-secret-scanning-on-demand-for-developers-and-agents/#learn-more-and-share-feedback)

Learn more about [secret scanning](https://docs.github.com/code-security/concepts/secret-security/secret-scanning?utm_source=secret-scanning-changelog-learn-more-docs-link-1&utm_medium=changelog&utm_campaign=ignite-nov-2026) and [supported secret scanning patterns](https://docs.github.com/code-security/reference/secret-security/supported-secret-scanning-patterns?utm_source=secret-scanning-changelog-learn-more-link-2&utm_medium=changelog&utm_campaign=ignite-nov-2026).

For Copilot, see how to [run a security review in the app](https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions?utm_source=secret-scanning-changelog-learn-more-docs-link-4&utm_medium=changelog&utm_campaign=ignite-nov-2026#using-security-review-in-app-sessions) or [request a code review](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-code-review?utm_source=secret-scanning-changelog-learn-more-docs-link-5&utm_medium=changelog&utm_campaign=ignite-nov-2026).

Share your feedback in the [community discussion](https://gh.io/community-secret-scanning).
