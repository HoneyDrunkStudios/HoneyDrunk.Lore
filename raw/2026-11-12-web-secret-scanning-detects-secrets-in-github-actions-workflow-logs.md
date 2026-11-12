---
source: "https://github.blog/changelog/2026-11-09-secret-scanning-detects-secrets-in-github-actions-workflow-logs"
title: "Secret scanning detects secrets in GitHub Actions workflow logs"
author: "unknown"
date_published: "2026-11-09"
date_clipped: "2026-11-12"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Secret scanning detects secrets in GitHub Actions workflow logs

![](https://github.blog/wp-content/themes/github-2021-child/assets/img/featured-v3-improvements.svg)

GitHub secret scanning now detects secrets in GitHub Actions workflow logs, in addition to [issues, wikis, discussions, and pull requests](https://github.blog/changelog/2024-08-16-secret-scanning-for-non-code-github-surfaces-is-now-generally-available/). Actions workflow log scanning is available in public preview.

### [How does Actions workflow log scanning work?](https://github.blog/changelog/2026-11-09-secret-scanning-detects-secrets-in-github-actions-workflow-logs/#how-does-actions-workflow-log-scanning-work)

When a workflow run completes, GitHub scans its logs for provider patterns. Findings appear in your repository’s secret scanning alert list, alongside alerts from code and other content, with a link back to the Actions workflow log. Validity checks run for supported secret types, and alerts remain available even after the logs are deleted.

### [How do I enable it?](https://github.blog/changelog/2026-11-09-secret-scanning-detects-secrets-in-github-actions-workflow-logs/#how-do-i-enable-it)

The preview is available to enterprises on GitHub Enterprise Cloud with GitHub Secret Protection or GitHub Advanced Security, including those with data residency on GHE.com.

Enterprise owners can enable **Secret scanning for Actions workflow logs** by opening their enterprise settings and selecting **Policies**, then **Advanced Security**. Select **Enabled** in the **All repositories** dropdown. The policy is disabled by default and applies only to repositories with secret scanning enabled under those licenses.

### [What should I know about the preview?](https://github.blog/changelog/2026-11-09-secret-scanning-detects-secrets-in-github-actions-workflow-logs/#what-should-i-know-about-the-preview)

Only workflow runs that complete after you enable the feature are scanned; existing logs aren’t backfilled. Generic patterns, custom patterns, AI-detected secrets, and secrets already masked by Actions aren’t detected.

Alerts from Actions workflow logs don’t generate notifications during the preview, so check your repository’s secret scanning alert list directly.

### [Learn more](https://github.blog/changelog/2026-11-09-secret-scanning-detects-secrets-in-github-actions-workflow-logs/#learn-more)

Learn more about [secret scanning](https://docs.github.com/en/enterprise-cloud@latest/code-security/concepts/secret-security/secret-scanning#secrets-detected-in-github-actions-workflow-logs) in our product documentation. Have feedback? Let us know by [joining the discussion](https://gh.io/community-secret-scanning). We’re listening.
