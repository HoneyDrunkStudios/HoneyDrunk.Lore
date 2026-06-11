---
source: "https://github.blog/changelog/2026-06-10-dedicated-security-review-command-now-available-in-copilot-cli/"
title: "Dedicated security review command now available in Copilot CLI - GitHub Changelog"
author: "Allison"
date_published: "2026-06-10"
date_clipped: "2026-06-11"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Dedicated security review command now available in Copilot CLI - GitHub Changelog

Source: https://github.blog/changelog/2026-06-10-dedicated-security-review-command-now-available-in-copilot-cli/

You can now run a security review on your code changes directly from GitHub Copilot CLI. The new `/security-review`

slash command is shipping as an experimental feature in public preview, giving you a fast, AI-driven way to catch security vulnerabilities before they reach production code.

`/security-review`

analyzes your local code changes and returns:

- High-confidence security findings, scored by severity and confidence.
- Actionable suggestions you can apply without leaving the terminal.
- A focused review that lives in your existing workflow.

The scan is tuned to flag common, high-impact vulnerability classes such as injection flaws, cross-site scripting, insecure data handling, path traversal, and weak cryptography.

This is a Copilot-driven scan that doesn’t rely on GitHub code scanning, Dependabot, or GitHub secret scanning. It complements those tools by giving you a lightweight, on-demand way to review your changes before you commit.

This is an experimental command. To try it, turn on [experimental mode in Copilot CLI](https://github.com/github/copilot-cli#experimental-mode), then run `/security-review`

in any project to scan your current changes.

Join the discussion and share your feedback within the [GitHub Community](https://github.com/orgs/community/discussions/196523).
