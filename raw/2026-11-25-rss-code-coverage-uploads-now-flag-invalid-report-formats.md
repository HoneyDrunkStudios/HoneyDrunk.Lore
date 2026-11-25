---
source: "https://github.blog/changelog/2026-11-23-code-coverage-uploads-now-flag-invalid-report-formats"
title: "Code coverage uploads now flag invalid report formats"
author: "Allison"
date_published: "2026-11-23"
date_clipped: "2026-11-25"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Code coverage uploads now flag invalid report formats

The GitHub Code Quality `upload-code-coverage` action now checks that your coverage report is in Cobertura XML format. If it isn’t in a supported format, the upload step fails and the Actions log shows this error:

> This file is not a Cobertura XML report. Upload a Cobertura XML report.

Previously, these uploads appeared to succeed, but no coverage showed up on your pull requests. Now you’ll find out about the problem in the workflow run, with a clear next step.

If your workflow begins failing with this error, configure your test framework to output Cobertura XML, or convert your report to Cobertura XML before the upload step.

We’ve also made processing more forgiving for valid Cobertura reports. We no longer reject a report because of minor structural issues, and we skip individual lines that don’t have a usable line number or hit count instead of discarding the whole report.

To use code coverage, you need GitHub Code Quality enabled for your repository. This change is available now on GitHub Enterprise Cloud and GitHub Team, including GitHub Enterprise Cloud with data residency. It isn’t available on GitHub Enterprise Server. Learn more about [setting up code coverage for your repository on GitHub Enterprise Cloud](https://docs.github.com/enterprise-cloud@latest/code-security/how-tos/maintain-quality-code/set-up-code-coverage).

[application security](https://github.blog/changelog/2026/?label=application-security)

Share
Copied
Shared
[Back to changelog](https://github.blog/changelog/)
