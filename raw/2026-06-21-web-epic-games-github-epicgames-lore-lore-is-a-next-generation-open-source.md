---
source: "https://github.com/EpicGames/lore"
title: "GitHub - EpicGames/lore: Lore is a next-generation, open source version control system"
author: "Epic Games"
date_published: "unknown"
date_clipped: "2026-06-21"
category: "Game Development / Unity"
source_type: "web"
---

# GitHub - EpicGames/lore: Lore is a next-generation, open source version control system

Source: https://github.com/EpicGames/lore

Skip to content
Navigation Menu
Toggle navigation
Sign in
Appearance settings
Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing
Search or jump to...
Search code, repositories, users, issues, pull requests...
Search
Clear
Search syntax tips
Provide feedback
We read every piece of feedback, and take your input very seriously.
Include my email address so I can be contacted
Cancel
Submit feedback
Saved searches
Use saved searches to filter your results more quickly
Name
Query
To see all available qualifiers, see our documentation .
Cancel
Create saved search
Sign in
Appearance settings
Resetting focus
You signed in with another tab or window. Reload to refresh your session.
You signed out in another tab or window. Reload to refresh your session.
You switched accounts on another tab or window. Reload to refresh your session.
Dismiss alert
{{ message }}
EpicGames
lore
Public
Notifications
You must be signed in to change notification settings
Fork
Star
5.3k
Code
Issues
Pull requests
Actions
Security and quality
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Security and quality
Insights
EpicGames/lore
main Branches Tags Go to file Code Open more actions menu Folders and files Name Name Last commit message Last commit date Latest commit   History 136 Commits 136 Commits .cargo .cargo     .github/ workflows .github/ workflows     docs docs     lore-aws lore-aws     lore-base lore-base     lore-capi lore-capi     lore-chaos-client lore-chaos-client     lore-client lore-client     lore-credential lore-credential     lore-error-set-macro lore-error-set-macro     lore-error-set lore-error-set     lore-hashicorp lore-hashicorp     lore-integration-tests lore-integration-tests     lore-macro lore-macro     lore-notification lore-notification     lore-proto lore-proto     lore-revision lore-revision     lore-server lore-server     lore-storage lore-storage     lore-telemetry lore-telemetry     lore-transport lore-transport     lore lore     notices notices     scripts scripts     vendor/ quinn-proto vendor/ quinn-proto     .dockerignore .dockerignore     .gitignore .gitignore     .loreignore .loreignore     .markdownlint-cli2.jsonc .markdownlint-cli2.jsonc     .pre-commit-clippy.py .pre-commit-clippy.py     .pre-commit-config.yaml .pre-commit-config.yaml     .rustfmt.toml .rustfmt.toml     .vale.ini .vale.ini     CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md     CONTRIBUTING.md CONTRIBUTING.md     Cargo.lock Cargo.lock     Cargo.toml Cargo.toml     DCO DCO     GOVERNANCE.md GOVERNANCE.md     LICENSE LICENSE     MAINTAINERS.md MAINTAINERS.md     README.md README.md     SECURITY.md SECURITY.md     about.toml about.toml     build-helper.rs build-helper.rs     clippy.toml clippy.toml     deny.toml deny.toml     mkdocs.yml mkdocs.yml     pyproject.toml pyproject.toml     pyrightconfig.json pyrightconfig.json     uv.lock uv.lock     View all files Repository files navigation README Code of conduct Contributing MIT license Security
Lore
Next-generation open source version control
Download Lore
Quickstart
Read the docs
Join the conversation
Table of contents
About Lore
Get started with Lore
Overview
Lore's architecture
Lore's repositories
Fully open source
Contributing
License
Contact and community
About Lore
Lore is an open source version control system designed for unprecedented scalability of both data and teams. It is optimized for projects that combine code with large binary assets, including games and entertainment, and caters for the needs of developers and artists alike.
Note
Lore is pre-1.0 and under active development. Interfaces, on-disk formats, and APIs may change between releases.
(back to top)
Get started with Lore
Quickstart — install Lore and make your first commit by following the quickstart guide .
Read the docs — delve into Lore's ethos and architecture in the Lore documentation .
Have questions? — the FAQ covers licensing, supported platforms, production readiness, and how Lore compares to other version control systems.
See where Lore is headed — the roadmap lays out the big-rock features by time horizon, from scalable locking to an open source desktop client.
Join the conversation — chat with us and our community on Discord .
Or try it right now — install Lore and start a local server in demo mode:
macOS / Linux
curl -fsSL https://raw.githubusercontent.com/EpicGames/lore/main/scripts/install.sh | bash -s -- --demo
Windows (PowerShell)
$ env: LORE_DEMO = 1 ; irm https: // raw.githubusercontent.com / EpicGames / lore / main / scripts / install.ps1 | iex
(back to top)
Overview
Easy setup, on-demand scalability — Get started in local mode in minutes. Then, scale up as far and as fast as you need.
Fast and efficient processes — Scale without slowdowns, thanks to shared, reusable data and as-needed downloads.
Free branching — Quickly and easily create, manage, and sync branches to freely experiment, iterate, and release.
History you can trust — Confidently track and manage revisions with Lore's verifiable tamper-evident source of truth.
Intuitive interface — Enjoy complete one-to-one access to the full Lore functionality via the CLI.
Full-surface API — Extend, customize, and integrate Lore via C/C++, C#, Rust, Go, Python, or JavaScript.
Note
Lore is the built-in version control system for UEFN (Unreal Editor for Fortnite), but today's open source tooling can't yet talk to it: the UEFN build uses a proprietary compression format that can't ship with the open source project. We're actively moving UEFN onto an open compression format — the same one this open source project uses — to eliminate the gap between the two.
(back to top)
Lore's architecture
Lore is a centralized, content-addressed version control system that represents repository state as Merkle trees and an immutable revision chain, optimized for binary-first storage, deduplication, and sparse/on-demand data hydration at scale. For the full model—on-disk formats, chunking internals, and the mechanics of the Merkle tree—read the system design doc .
Highlights
Content-addressed storage — Repository data is stored and referenced by content hash in a Merkle tree, enabling fast comparisons, integrity checks, and reuse across history and branches.
Immutable revision chain — A revision's hash signature is derived from its revision state, including parent revision hashes and contained data hashes, forming an immutable chain with cryptographic integrity.
Chunked storage for large files — Files are stored as reusable chunks with indexed lookup, reducing duplication and enabling efficient updates and transfer for large binary assets.
On-demand hydration and sparse workspaces — Workspaces can stay lightweight by fetching file data only when needed, so you don't have to download everything up front.
Centralized service with caching — A service-backed architecture uses caching in front of durable storage to scale throughput for large teams and repositories.
Lightweight branches and fast switching — Branches are lightweight mutable references, so creating and switching branches is low-overhead without duplication of underlying data.
(back to top)
Lore's repositories
Lore spans a family of repositories: the core library, server, and CLI in this repository, plus a software development kit (SDK) for each supported language.
Repository
Description
Link
Lore Library, Server & CLI
The core Lore library, the Lore Server, and the Lore CLI. You are here.
View on GitHub
JavaScript SDK
The JavaScript binding for the Lore API.
View on GitHub
Python SDK
The Python binding for the Lore API.
View on GitHub
C# SDK
The C# binding for the Lore API.
View on GitHub
Go SDK
The Go binding for the Lore API.
View on GitHub
(back to top)
Fully open source
We believe a truly open ecosystem is built collectively using open standards. Lore is fully open source under an MIT license , and we invite you to build the version control system of the future in the open. See CONTRIBUTING.md to get involved.
(back to top)
Contributing
Contributions of every kind are welcome — code, documentation, bug reports, and reviews. Start with CONTRIBUTING.md for the development workflow, then read the Code of Conduct and the project governance model . New to the codebase? The good-first-issue label is a good place to start.
(back to top)
License
Lore is released under the MIT License. See LICENSE for the full text. Copyright (c) 2026 Epic Games, Inc.
(back to top)
Contact and community
Discord — chat with the team and community on Discord .
GitHub Issues — report bugs and request features through GitHub Issues .
(back to top)
About
Lore is a next-generation, open source version control system
lore.org
Topics
open-source
Resources
Readme
License
MIT license
Code of conduct
Code of conduct
Contributing
Contributing
Security policy
Security policy
Uh oh!
There was an error while loading. Please reload this page .
Activity
Custom properties
Stars
5.3k
stars
Watchers
watching
Forks
forks
Report repository
Releases
v0.8.3
Latest
Jun 17, 2026
Packages
Uh oh!
There was an error while loading. Please reload this page .
Contributors
Uh oh!
There was an error while loading. Please reload this page .
Languages
Rust
81.5%
Python
14.3%
3.9%
Shell
0.2%
PowerShell
0.1%
Dockerfile
0.0%
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
You can’t perform that action at this time.
