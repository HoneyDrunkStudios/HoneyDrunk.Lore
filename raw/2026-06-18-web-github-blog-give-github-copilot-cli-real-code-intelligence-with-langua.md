---
source: "https://github.blog/ai-and-ml/github-copilot/give-github-copilot-cli-real-code-intelligence-with-language-servers"
title: "Give GitHub Copilot CLI real code intelligence with language servers"
author: "GitHub Blog"
date_published: "2026-06-10"
date_clipped: "2026-06-18"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Give GitHub Copilot CLI real code intelligence with language servers

Source: https://github.blog/ai-and-ml/github-copilot/give-github-copilot-cli-real-code-intelligence-with-language-servers

Give GitHub Copilot CLI real code intelligence with language servers - The GitHub Blog
/
Blog
Changelog
Docs
Customer stories
AI & ML Learn about artificial intelligence and machine learning across the GitHub ecosystem and the wider industry.
Generative AI Learn how to build with generative AI.
GitHub Copilot Change how you work with GitHub Copilot.
LLMs Everything developers need to know about LLMs.
Machine learning Machine learning tips, tricks, and best practices.
How AI code generation works Explore the capabilities and benefits of AI code generation and how it can improve your developer experience.
Learn more
Developer skills
Developer skills Resources for developers to grow in their skills and careers.
Application development Insights and best practices for building apps.
Career growth Tips & tricks to grow as a professional developer.
GitHub Improve how you use GitHub at work.
GitHub Education Learn how to move into your first professional role.
Programming languages & frameworks Stay current on what’s new (or new again).
Get started with GitHub documentation Learn how to start building, shipping, and maintaining software with GitHub.
Learn more
Engineering
Engineering Get an inside look at how we’re building the home for all developers.
Architecture & optimization Discover how we deliver a performant and highly available experience across the GitHub platform.
Engineering principles Explore best practices for building software at scale with a majority remote team.
Infrastructure Get a glimpse at the technology underlying the world’s leading AI-powered developer platform.
Platform security Learn how we build security into everything we do across the developer lifecycle.
User experience Find out what goes into making GitHub the home for all developers.
How we use GitHub to be more productive, collaborative, and secure Our engineering and security teams do some incredible work. Let’s take a look at how we use GitHub to be more productive, build collaboratively, and shift security left.
Learn more
Enterprise software
Enterprise software Explore how to write, build, and deploy enterprise software at scale.
Automation Automating your way to faster and more secure ships.
CI/CD Guides on continuous integration and delivery.
Collaboration Tips, tools, and tricks to improve developer collaboration.
DevOps DevOps resources for enterprise engineering teams.
DevSecOps How to integrate security into the SDLC.
Governance & compliance Ensuring your builds stay clean.
GitHub recognized as a Leader in the Gartner® Magic Quadrant™ for AI Code Assistants Learn why Gartner positioned GitHub as a Leader for the second year in a row.
Learn more
News & insights
News & insights Keep up with what’s new and notable from inside GitHub.
Company news An inside look at news and product updates from GitHub.
Product The latest on GitHub’s platform, products, and tools.
Octoverse Insights into the state of open source on GitHub.
Policy The latest policy and regulatory changes in software.
Research Data-driven insights around the developer ecosystem.
The library Older news and updates from GitHub.
Unlocking the power of unstructured data with RAG Learn how to use retrieval-augmented generation (RAG) to capture more insights.
Learn more
Open Source
Open Source Everything open source on GitHub.
Git The latest Git updates.
Maintainers Spotlighting open source maintainers.
Social impact How open source is driving positive change.
Gaming Explore open source games on GitHub.
An introduction to innersource Organizations worldwide are incorporating open source methodologies into the way they build and ship their own software.
Learn more
Security Stay up to date on everything security.
Application security Application security, explained.
Supply chain security Demystifying supply chain security.
Vulnerability research Updates from the GitHub Security Lab.
Web application security Helpful tips on securing web applications.
The enterprise guide to AI-powered DevSecOps Learn about core challenges in DevSecOps, and how you can start addressing them with AI and automation.
Learn more
Search
Categories
Back AI & ML Learn about artificial intelligence and machine learning across the GitHub ecosystem and the wider industry.
Generative AI Learn how to build with generative AI.
GitHub Copilot Change how you work with GitHub Copilot.
LLMs Everything developers need to know about LLMs.
Machine learning Machine learning tips, tricks, and best practices.
How AI code generation works Explore the capabilities and benefits of AI code generation and how it can improve your developer experience.
Learn more
Developer skills
Back Developer skills Resources for developers to grow in their skills and careers.
Application development Insights and best practices for building apps.
Career growth Tips & tricks to grow as a professional developer.
GitHub Improve how you use GitHub at work.
GitHub Education Learn how to move into your first professional role.
Programming languages & frameworks Stay current on what’s new (or new again).
Get started with GitHub documentation Learn how to start building, shipping, and maintaining software with GitHub.
Learn more
Engineering
Back Engineering Get an inside look at how we’re building the home for all developers.
Architecture & optimization Discover how we deliver a performant and highly available experience across the GitHub platform.
Engineering principles Explore best practices for building software at scale with a majority remote team.
Infrastructure Get a glimpse at the technology underlying the world’s leading AI-powered developer platform.
Platform security Learn how we build security into everything we do across the developer lifecycle.
User experience Find out what goes into making GitHub the home for all developers.
How we use GitHub to be more productive, collaborative, and secure Our engineering and security teams do some incredible work. Let’s take a look at how we use GitHub to be more productive, build collaboratively, and shift security left.
Learn more
Enterprise software
Back Enterprise software Explore how to write, build, and deploy enterprise software at scale.
Automation Automating your way to faster and more secure ships.
CI/CD Guides on continuous integration and delivery.
Collaboration Tips, tools, and tricks to improve developer collaboration.
DevOps DevOps resources for enterprise engineering teams.
DevSecOps How to integrate security into the SDLC.
Governance & compliance Ensuring your builds stay clean.
GitHub recognized as a Leader in the Gartner® Magic Quadrant™ for AI Code Assistants Learn why Gartner positioned GitHub as a Leader for the second year in a row.
Learn more
News & insights
Back News & insights Keep up with what’s new and notable from inside GitHub.
Company news An inside look at news and product updates from GitHub.
Product The latest on GitHub’s platform, products, and tools.
Octoverse Insights into the state of open source on GitHub.
Policy The latest policy and regulatory changes in software.
Research Data-driven insights around the developer ecosystem.
The library Older news and updates from GitHub.
Unlocking the power of unstructured data with RAG Learn how to use retrieval-augmented generation (RAG) to capture more insights.
Learn more
Open Source
Back Open Source Everything open source on GitHub.
Git The latest Git updates.
Maintainers Spotlighting open source maintainers.
Social impact How open source is driving positive change.
Gaming Explore open source games on GitHub.
An introduction to innersource Organizations worldwide are incorporating open source methodologies into the way they build and ship their own software.
Learn more
Back Security Stay up to date on everything security.
Application security Application security, explained.
Supply chain security Demystifying supply chain security.
Vulnerability research Updates from the GitHub Security Lab.
Web application security Helpful tips on securing web applications.
The enterprise guide to AI-powered DevSecOps Learn about core challenges in DevSecOps, and how you can start addressing them with AI and automation.
Learn more
Changelog
Docs
Customer stories
Install and configure LSP servers for GitHub Copilot CLI, replacing brute-force grep/decompile with real code intelligence.
Bruno Borges · @brunoborges
June 10, 2026
|
5 minutes
Share:
Ever watched GitHub Copilot CLI extract a JAR file to a temporary directory, grep through .class files, and piece together an API signature from raw bytecode? The agent is resourceful, but without a language server, that’s the best it can do.
The Language Server Protocol (LSP) is the standard that powers go to definition, find references, and type resolution in editors like VS Code. It works just as well in the terminal. The LSP Setup skill automates the installation and configuration of LSP servers for Copilot CLI, so the agent gets precise, structured answers about your code instead of relying on text search heuristics.
In this post, you’ll learn how the skill works under the hood, see the configuration format it generates, and get set up for any of the 14 languages it supports today.
The problem: heuristic code understanding
Without an LSP server, the agent in GitHub Copilot CLI reverse-engineers API information through text search and binary extraction. For a Java project, that might look like:
# Find the dependency JAR
find ~/.m2/repository -name "*httpclient*.jar"
# Extract it to a temp directory
mkdir /tmp/httpclient && cd /tmp/httpclient
jar xf ~/.m2/repository/org/apache/httpcomponents/httpclient/4.5.14/httpclient-4.5.14.jar
# Search extracted class files for a method
grep -r "execute" --include="*.class" .
For Python, the agent might cat files inside site-packages . For TypeScript, it walks node_modules . These text-based approaches work for simple cases, but they’re doing pattern-matching over raw text rather than true semantic analysis, so they miss generics, overloads, and transitive types, and can’t see compiled bytecode at all. That’s exactly the gap a language server close.
An LSP server solves this structurally. When the agent sends a textDocument/definition request for a symbol, the language server returns the exact source location, fully resolved type, and signature.
What is an agent skill?
Agent skill is a reusable instruction set that extends what an AI coding agent can do. Skills are defined in Markdown files with YAML frontmatter and follow a standard structure: trigger descriptions, step-by-step workflows, reference data, and behavioral constraints.
The LSP Setup skill uses this structure to guide the agent through a multi-step installation process, detecting the operating system, choosing the right package manager, writing valid configuration, and verifying the result.
How the LSP Setup skill works
When triggered, the skill executes a seven-step workflow:
1. Language selection
The agent uses ask_user with a set of choices to determine which language the user needs LSP support for. This drives all subsequent steps.
2. Operating system detection
The agent runs uname -s (or checks $env:OS / %OS% on Windows) to determine the target platform. Install commands vary by operating system. For example, brew install jdtls on macOS versus downloading from eclipse.org on Linux.
3. LSP server lookup
The skill includes a reference file ( references/lsp-servers.md ) with curated data for 14 languages: install commands per operating system, binary names, and ready-to-use config snippets. The agent reads this file and selects the matching entry.
4. Configuration scope
The agent asks whether the config should be:
User-level : ~/.copilot/lsp-config.json —applies to all repositories
Repository-level : lsp.json at the repository root or .github/lsp.json —scoped to a single project
Repository-level configuration takes precedence when both exist.
5. Installation
The agent runs the appropriate install command. For example:
# TypeScript on any OS
npm install -g typescript typescript-language-server
# Java on macOS
brew install jdtls
# Rust on any OS
rustup component add rust-analyzer
6. Configuration
The agent writes or merges an entry into the chosen config file. The format uses a lspServers object where each key is a server identifier:
{
"lspServers": {
"java": {
"command": "jdtls",
"args": [],
"fileExtensions": {
".java": "java"
}
}
}
}
Key rules the skill enforces:
command must be on $PATH or an absolute path
args typically includes "--stdio" for standard I/O transport (some servers like jdtls handle this internally)
fileExtensions maps each extension (with leading dot) to a language identifier
Existing entries in the config file are preserved — the agent merges, never overwrites
7. Verification
The agent runs which <binary> (or where.exe on Windows) to confirm the server is accessible, then validates the config file is well-formed JSON.
Supported languages
The skill comes with a set of predefined language servers for several programming languages. If the coding agent faces one that it is not mapped out already, it will search for an appropriate server and walk you through manual configuration.
What changes after setup
Once an LSP server is configured, the CLI agent can:
Resolve types across dependencies — no more grepping through JAR files or node_modules
Jump to definitions in third-party libraries, even when source isn’t checked into the repository
Find all references to a symbol across the project
Read hover documentation for any function, class, or type
This means the agent spends less time on tool calls and produces more accurate code on the first pass. For you, that’s less time waiting while the agent decompiles a JAR file or greps through node_modules to answer a question your IDE already knows, and fewer wrong turns built on a misread signature. The agent reasons about your code with the same structured understanding you get from go-to-definition in your editor, so you can hand it bigger, gnarlier tasks and trust the result.
Get started
Download the skill : visit the Awesome Copilot LSP Setup skill page and click the Download button to get a ZIP file.
Extract the ZIP to ~/.copilot/skills/ by running:
unzip lsp-setup.zip -d ~/.copilot/skills/
Restart GitHub Copilot CLI : if Copilot CLI is already running, type /exit first. Then relaunch copilot so it picks up the new skill.
Ask the agent to set up a language server: for example, “set up LSP for Java” or “enable code intelligence for Python” .
Verify : after the skill installs and configures the LSP server, restart Copilot CLI one more time ( /exit , then relaunch), run /lsp to check the server status, and try go-to-definition on a symbol from one of your dependencies.
The skill is part of the Awesome Copilot project. It’s open source, so contributions and feedback are welcome!
Tags:
GitHub Copilot
GitHub Copilot CLI
Written by
Bruno Borges
@brunoborges
Principal Product Manager
GitHub Copilot
GitHub Copilot CLI
Table of Contents
The problem: heuristic code understanding
What is an agent skill?
How the LSP Setup skill works
Supported languages
What changes after setup
Get started
More on GitHub Copilot Getting more from each token: How Copilot improves context handling and model routing How GitHub Copilot is making more of each session go toward useful work, so your credits go further.
Joe Binder
What are git worktrees, and why should I use them? Git worktrees have been around since 2015, but it wasn’t until recently they became popular. Learn what they are, how to use them, and why you might.
Cassidy Williams
Related posts
Getting more from each token: How Copilot improves context handling and model routing
How GitHub Copilot is making more of each session go toward useful work, so your credits go further.
Joe Binder
What are git worktrees, and why should I use them?
Git worktrees have been around since 2015, but it wasn’t until recently they became popular. Learn what they are, how to use them, and why you might.
Cassidy Williams
GitHub Copilot CLI for Beginners: Overview of common slash commands
GitHub Copilot CLI for Beginners: Learn how to use slash commands to control your terminal AI agent.
Kayla Cinnamon
Explore more from GitHub
Docs
Everything you need to master GitHub, all in one place.
Go to Docs
GitHub
Build what’s next on GitHub, the place for anyone from anywhere to build anything.
Start building
Customer stories
Meet the companies and engineering teams that build with GitHub.
Learn more
GitHub Universe 2026
Join us October 28-29 in San Francisco or online for GitHub Universe, our flagship developer event uniting people, agents, and the world’s code.
Register now
We do newsletters, too Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.
Your email address
*
Your email address
Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the GitHub Privacy Statement for more details.
Site-wide Links
Product Features Security Enterprise Customer Stories Pricing Resources Platform Developer API Partners Atom Electron GitHub Desktop Support Docs Community Forum Training Status Contact Company About Blog Careers Press Shop
© 2026 GitHub, Inc.
Terms
Privacy
Do not share my personal information
LinkedIn icon
GitHub on LinkedIn
Instagram icon
GitHub on Instagram
YouTube icon
GitHub on YouTube
X icon
GitHub on X
TikTok icon
GitHub on TikTok
Twitch icon
GitHub on Twitch
GitHub icon
GitHub’s organization on GitHub
