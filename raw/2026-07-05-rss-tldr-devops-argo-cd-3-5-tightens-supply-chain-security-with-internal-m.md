---
source: "https://www.infoq.com/news/2026/06/argocd-supply-chain-security"
title: "Argo CD 3.5 Tightens Supply Chain Security with Internal mTLS and Source Integrity (3 minute read)"
author: "TLDR DevOps"
date_published: "2026-07-03"
date_clipped: "2026-07-05"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-07-03"
source_role: "primary-via-tldr"
---

# Argo CD 3.5 Tightens Supply Chain Security with Internal mTLS and Source Integrity (3 minute read)

Source: https://www.infoq.com/news/2026/06/argocd-supply-chain-security

InfoQ Homepage 

News 

Argo CD 3.5 Tightens Supply Chain Security with Internal mTLS and Source Integrity 

DevOps
Argo CD 3.5 Tightens Supply Chain Security with Internal mTLS and Source Integrity
Jun 26, 2026 
3
min read
by
Claudio Masolo 
Follow us on 
Youtube 232K Followers 
Linkedin 26K Followers 
Instagram New 
RSS 19K Readers 
X 57.1k Followers 
Facebook 21K Likes 
Bluesky New 
Listen to this article -  0:00 
Audio ready to play 
Your browser does not support the audio element.
0:00 
0:00 
Normal 1.25x 1.5x 
Like 
Reading list 
The Argo CD project released a v3.5 release candidate in June 2026. This version adds mutual TLS enforcement for internal components. It also includes Git commit signature verification for supply chain security and native ApplicationSet management in the UI. The release also graduates two significant features: impersonation and Source Hydrator, from alpha to beta.
Large-scale Argo CD deployments have long faced gaps in internal security posture and operational visibility. Communication between the repo-server and other components, like the API server and controllers, was unencrypted before. This left internal traffic outside the usual mTLS protection that teams apply at the ingress layer. On the supply chain side, nothing in Argo CD prevented a compromised Git repository from silently deploying unsigned or tampered manifests. ApplicationSet resources create applications at scale, but they lacked native UI support. Operators had to check YAML or use kubectl to see what an ApplicationSet would produce.
The repo-server now supports mTLS , requiring client certificates from each connecting component. For environments without custom certificates, the repo-server creates self-signed certs in memory. This helps with internal health checks and avoids relying on the filesystem. Source Integrity validation lets operators ensure Git sources have valid signatures before syncing. This can be set up through the Application spec with sourceIntegrity.required: true or by using the CLI flag argocd app set --source-integrity-required . The ApplicationSet UI, created by engineers from Intuit, Red Hat, GoTo, and Octopus Deploy, includes list, filter, and detail views. It also has a Preview Apps tab, which shows the applications an ApplicationSet template will create before deployment.
Argo CD can now take on a specific user identity for server-side tasks. This includes log streaming, resource deletion, and sync. It has moved to beta. When you set up impersonation through AppProject or RBAC policy , it now applies automatically to all server operations. This is important for audit trails in multi-tenant clusters. The Source Hydrator, which separates dry (unhydrated) manifests from their hydrated output, also reaches beta. Teams can now set different drySource.repoURL and syncSource.repoURL values. This enables multi-repository GitOps patterns. Here, source templates and rendered manifests are in different repositories. Each can have its own access controls.
The release also adds Helm 4 support alongside backward compatibility with Helm 3 deployments. ApplicationSets can now be deployed in any namespace, not just the Argo CD namespace. This change brings stable status and meets a long-requested need for teams managing GitOps by namespace. ApplicationSet concurrency controls help operators limit the number of applications processed at the same time. This reduces the risk of overwhelming the cluster or upstream Git APIs. Azure AD users hitting group claims overflow can now route group resolution through the Microsoft Graph API, bypassing OIDC token size limits. Azure DevOps repositories gain Service Principal authentication support, eliminating the PAT dependency.
Among Argo CD's main competitors, the three v3.5 headline features: internal mTLS, Source Integrity, and ApplicationSet UI, vary greatly based on each tool's architecture. Flux (v2.8, March 2026) avoids the internal mTLS issue by design. Its controllers use Kubernetes API objects to communicate instead of direct gRPC. This means there’s no internal traffic that needs securing. Flux supports mTLS for external connections. You can use certSecretRef with GitRepository , HelmRepository , and OCIRepository resources. On commit signature verification, Flux has offered native GPG support in the GitRepository API via spec.verify.mode: head longer than Argo CD, so Argo CD is catching up here. Flux 2.8 added a web dashboard to the UI via the separate Flux Operator. This includes views for Kustomization and HelmRelease. However, it lacks an ApplicationSet Preview equivalent. Instead, Flux's ArtifactGenerator API manages template-driven generation without a visual preview step. On UI, Flux 2.8 introduced a web dashboard through the separately-installed Flux Operator , covering Kustomization and HelmRelease views, but there is no ApplicationSet Preview equivalent.
Rancher Fleet uses a websocket-based agent system instead of gRPC. This means internal mTLS isn't needed. TLS is handled at the Rancher ingress and agent trust levels. Fleet lacks a built-in Source Integrity mechanism. To enforce commit signatures, you'll need a policy from your Git provider or an admission webhook. Its UI is part of the Rancher dashboard's Continuous Delivery section, not a separate app.
Jenkins X uses Tekton to enforce supply chain controls at the pipeline layer. This includes Tekton Chains and GPG-signed releases. It does not provide a first-party dashboard and lacks a preview capability like ApplicationSet. Multi-cluster promotion occurs through pull request–based environment flows, not by generating templates.
About the Author 
Claudio Masolo 
Show more Show less 
Rate this Article 
Adoption 
Style 
Author Contacted 
This content is in the DevOps topic
Related Topics: 
DevOps 
GitOps 
Argo CD 
Security 
Related Editorial 
Related Sponsors 
Popular across InfoQ 
Google Releases A2UI v0.9: Portable, Framework-Agnostic Generative UI
Scaling Java-Based Real-Time Systems: The Hidden Tradeoffs of Event-Driven Design
Million PDFs: Building a Modern Document Infrastructure with Rust and Typst
Agentic AI Architecture
Architectural Patterns: Moving Beyond Cloud-Native to Local-First - Insights from Adam Wiggins
AWS Launches Lambda MicroVMs for Isolated Agent and User Code Execution
Related Content 
The InfoQ Newsletter 

A round-up of last week’s content on InfoQ sent out every Tuesday. Join a community of over 250,000 senior developers.

View an example 

Enter your e-mail address 

Select your country 

Select a country 

I consent to InfoQ.com handling my data as explained in this Privacy Notice . 

We protect your privacy.
