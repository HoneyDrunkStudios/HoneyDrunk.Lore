---
source: "https://github.blog/changelog/2026-05-19-expanded-oidc-support-for-dependabot-and-code-scanning"
title: "Expanded OIDC support for Dependabot and code scanning"
author: "GitHub Changelog"
date_published: "2026-05-19"
date_clipped: "2026-05-30"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Expanded OIDC support for Dependabot and code scanning

Source: https://github.blog/changelog/2026-05-19-expanded-oidc-support-for-dependabot-and-code-scanning

Back to changelog 
Improvement 
May 19, 2026 •
1 minute read 
Expanded OIDC support for Dependabot and code scanning 
Dependabot and code scanning now support OpenID Connect (OIDC) authentication for private registries configured at the organization level for two additional registries: Cloudsmith and Google Artifact Registry .
What’s new 
Organization administrators can configure OIDC-based credentials for private registries across their organization. With OIDC-based authentication, you can dynamically obtain short-lived credentials from your cloud identity provider, just like GitHub Actions workflows using OIDC federation . This builds on earlier support for OIDC authentication at the org level and extends it to support two new registries.
Supported registries 
AWS CodeArtifact 
Azure DevOps Artifacts 
JFrog Artifactory 
Cloudsmith 
Google Artifact Registry 
This feature is now generally available on github.com and will ship in GitHub Enterprise Server 3.22.
Learn more about configuring OIDC for Dependabot and code scanning at the organization level. You can also join the community discussion .
application security 
supply chain security 
Share 
Copied 
Shared 
Back to changelog
