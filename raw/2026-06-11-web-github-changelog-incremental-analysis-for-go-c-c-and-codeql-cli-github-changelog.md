---
source: "https://github.blog/changelog/2026-06-10-incremental-analysis-for-go-c-c-and-codeql-cli/"
title: "Incremental analysis for Go, C/C++, and CodeQL CLI - GitHub Changelog"
author: "Allison"
date_published: "2026-06-10"
date_clipped: "2026-06-11"
category: "DevOps & CI/CD"
source_type: "web"
---

# Incremental analysis for Go, C/C++, and CodeQL CLI - GitHub Changelog

Source: https://github.blog/changelog/2026-06-10-incremental-analysis-for-go-c-c-and-codeql-cli/

CodeQL scans on pull requests for C/C++ and Go now run incrementally, making them faster. Earlier this year, [we released improved incremental analysis](https://github.blog/changelog/2026-03-24-faster-incremental-analysis-with-codeql-in-pull-requests/) for CodeQL analysis of C#, Java, JavaScript/TypeScript, Python, and Ruby. We are now shipping the same improvements for C/C++ and Go, and are also adding [incremental analysis to the CodeQL CLI](https://docs.github.com/code-security/how-tos/find-and-fix-code-vulnerabilities/scan-from-the-command-line/incremental-analysis).

Across more than 15,000 repositories, we classified repositories into three groups based on how long it takes to run a non-incremental scan:

- Three minutes or less
- Between three and seven minutes
- Seven minutes or more

For these repositories, we measured the change in analysis time for incremental scans compared to traditional scans over a seven-day period. In each case, incremental scans showed a significant speed up.

This latest improvement to incremental analysis applies to repositories using code scanning with the default CodeQL query suite.

Incremental CodeQL analysis is enabled by default for all projects that are using the `build mode none`

extraction mechanism in both default setup and advanced setup on github.com.

Beginning with version 2.25.5, CodeQL CLI also supports [incremental analysis](https://docs.github.com/code-security/how-tos/find-and-fix-code-vulnerabilities/scan-from-the-command-line/incremental-analysis) in third-party CI systems.
