---
source: "https://novee.security/blog/cordyceps"
title: "Cordyceps: The Silent Parasite Consuming Your Supply Chain (12 minute read)"
author: "TLDR InfoSec"
date_published: "2026-06-25"
date_clipped: "2026-06-29"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-06-25"
source_role: "primary-via-tldr"
---

# Cordyceps: The Silent Parasite Consuming Your Supply Chain (12 minute read)

Source: https://novee.security/blog/cordyceps

Cordyceps: The Silent Parasite Consuming Your Supply Chain 
The silent parasite consuming your supply chain doesn't get a CVE. 
The silent parasite consuming your supply chain doesn't get a CVE. 
Back 
Platform 
Company 
Resources 
Customers 
Contact 
Careers 
Book a demo 
Book a demo 
PLATFORM 
AI Pentesting Platform 
Web App Testing 
Mobile App Testing 
AI Red Teaming 
Agentic Remediation 
SOLUTIONS 
Scale manual pentesting 
Replace DAST 
Rethink Bug Bounties 
Meet Compliance 
About 
Careers 
News 
Blog 
Labs 
News 
Exploit Registry 
Buyer's Guide 
Blog 
Cordyceps 🍄‍🟫: The Silent Parasite Consuming Your Supply Chain 
Novee's research team discovered Cordyceps, a critical supply chain flaw hiding in plain sight, impacting code repositories at thousands of organizations, including Microsoft, Google, Apache, and Cloudflare. 
Elad Meged, Founding Engineer & Security Researcher 
June 23, 2026 
12 mins 
Explore Article
+ 
Request a Demo
Novee identified a systemic class of exploitable CI/CD vulnerabilities across the open-source supply chain – command injection, broken authentication logic, artifact poisoning chains, and privilege escalation in GitHub Actions workflows.  
Our team scanned roughly 30,000 high-impact repositories, validated hundreds of fully exploitable attack chains, and received confirmation of fixes at dozens of organizations, including Microsoft, Google, Apache, Cloudflare, and the Python Software Foundation. There are millions of repositories that are potentially affected by this same pattern. 
The nature of agentic coding means these CI/CD vulnerabilities are reproduced persistently, at scale, “infecting” repositories at an exponential rate. Because anonymous users can use them to gain control over the software supply chain, we like to think of it as “puppeteering” the repositories of some of the world’s biggest companies, silently manipulating their workflows.  
We’re calling it Cordyceps, after the infamous parasitic fungus, best known for body-snatching its hosts.
Key Takeaways 
Novee found a critical exploitable pattern in the software supply chain –  which we’re calling Cordyceps – allowing for workflow hijack and full attacker control of repositories at dozens of the world’s largest companies. 
The flaw is exploitable by any unauthenticated user. No org membership or special privileges; a free account is enough to forge approvals, push code, or steal credentials. 
This is a CI/CD vulnerability pattern that the biggest, best-resourced engineering teams in the world keep making – including on the build tooling behind Microsoft, Google, Cloudflare, Python, and Apache .  
Once the exploit pattern was identified, 654 repositories were flagged in a single scan, and more than 300 were confirmed fully exploitable – attacker-controlled code execution, credential theft, or outright supply chain compromise. The downstream reach spans thousands of organizations that depend on this infrastructure.  
AI coding agents are scaling the problem. They generate CI/CD configuration fast and reproduce the same insecure patterns over and over, so the same mistakes can compound across millions of repositories. 
Detecting it requires reasoning and validation . Inventory-based attack-surface tools miss it; Novee’s Continuous External Attack Validation finds and proves this class of risk, then verifies the fix. 
How a CI/CD Vulnerability Can “Body-Snatch” Fortune 100 Infrastructure 
Our research discovered exploitable vulnerabilities in CI/CD workflow code – the same classes security teams already track in application code, living in GitHub Actions YAML instead. Workflow code is code. A bug in that code is a vulnerability.
The most dangerous findings in our research were multi-step exploit chains, i.e. an untrusted PR triggers a low-privilege workflow, whose output flows into a high-privilege workflow, whose token authenticates to GCP with roles/owner. No single step looks dangerous. Vulnerabilities only existed in the composition; untrusted data crossing a trust boundary that no one audited.
Modern software gets built atop the backs of thousands of open-source projects, and many operations are being automated, e.g. tests and CI/CD deployment using GitHub Actions. These workflows run shell commands, authenticate to cloud providers, hold signing keys, and publish releases, yet they are treated as “configuration,” not as security-critical code. The result: command injection, privilege escalation, and supply-chain compromise hiding in plain sight in .yml files that no traditional security scanner audits.
For some context, GitHub draws more than 14 million daily visitors and 90% of Fortune 100 companies use GitHub in their development workflows , and tens of thousands of GitHub Actions are in use . 
It’s important to note this flaw does not live in GitHub ; any workflow management system is susceptible, but GitHub is the path of least resistance for attackers given its combination of ubiquity and openness. 
A workflow fires because someone opened a pull request or left a comment. It treats that input as if it came from a maintainer, and acts on it with the maintainer’s permissions. Meaning, an outsider with a free GitHub account can borrow a project’s authority for a few minutes and use it to forge approvals, push malicious code, or steal credentials.  
When that same software is then installed by thousands of organizations, one compromised workflow in one repository can ripple outward into banks, cloud accounts, AI labs, and end-user devices. 
The Impact: Example Findings at Microsoft, Google, Apache, and Cloudflare 
Example findings below, across some of the most widely used open-source projects in the world.
1. Microsoft > Azure Sentinel (Microsoft’s SIEM, which ships detection rules, hunting queries, and automated playbooks to customers’ security environments):
Found: A comment on a pull request runs anonymous attacker code on Microsoft’s CI and steals a non-expiring GitHub App key.
At stake: Persistent write access to the security content Microsoft ships to customers, meaning they could be silently weakened or implanted with malicious infrastructure templates.
Credit: Behavior confirmed by MSRC.
Blast Radius and Effects: 
Microsoft Sentinel Content Hub supply chain: Content from this repository deploys directly into customer Sentinel workspaces via Azure Marketplace. The Content Hub is the centralized location for all out-of-the-box detection content. 
2. Google > AI Agent Development Kit (adk-samples, the official sample repository for Google’s AI Agent Development Kit):
Found: A single pull request runs attacker code in Google’s CI and gains authenticated control over the associated Google Cloud project.
At stake: The highest-possible Google Cloud role (roles/owner). Anyone who runs code from this repository’s pipeline gets full control over the associated Google Cloud project. One PR converts to permanent cloud access.
Credit: Issue and impact confirmed by Google.
Blast Radius and Effects: 
Google’s official ADK sample repository, with 9,200+ stars, is the primary reference for developers building AI agents on Google Cloud. A compromised CI pipeline could poison sample code and cloud infrastructure that developers depend on. 
3. Apache > Doris (Apache’s high-performance analytics database):
Found: Two independent zero-click attacks:
Path 1 – A single comment on any pull request runs attacker code and exfiltrates hardcoded CI credentials. 
Path 2 – A fork PR runs attacker code and steals a token with full write permissions across actions, contents, packages, pages and more.
At stake: Direct code modification of an Apache enterprise database repository; used as a data analytics bedrock tens of thousands of companies. The two paths can be changed to produce malicious artifacts through Apache’s own build infrastructure.
Credit: Issue and impact confirmed and fixed by the Apache Security Team, and then verified by Novee with a fix-bypass attempt.
Blast Radius and Effects: 
10,000+ global enterprises powered by Apache Doris. 
4. Cloudflare > Workers SDK (Cloudflare’s official developer toolkit (Wrangler CLI) for building on Cloudflare Workers)
Found: A pull request with a crafted branch name executed arbitrary commands on Cloudflare’s CI runners.
At stake: We confirmed code execution on their CI; no production secrets were reachable from this specific entry point. Cloudflare credited Novee and applied broad hardening across their workflows in response.
Credit: Credited as a reporter of the issue, comprehensive hardening applied.
Blast Radius and Effects: 
Developer-facing toolchain compromise: Confirmed code execution on Cloudflare CI, albeit without access to production secrets (no route to escalation). But the pattern persisted until hardening. 
5. Python Software Foundation – Black (the de-facto standard code formatter for Python)
Found: A single pull request from anyone could run attacker code on Black’s build systems and steal the automation token, which can post, approve, and manipulate pull requests as the project’s own bot.
At stake: The stolen bot token can approve pull requests as the project’s own bot, opening a path from code injection to the main branch. This could theoretically lead to a downstream consequence of exposing official Black images.
Blast Radius and Effects: 
Reach of 130 million installs per month: The stolen bot token can approve pull requests as the project’s own bot, opening a path from code injection to the main branch. From there, the project’s Docker image release would expose Docker Hub credentials, putting the official Black images that developers pull automatically at risk. 
Finding A Supply Chain Flaw at Scale  
Our research started wide and let AI narrow it down. We collected roughly 30,000 repositories across the npm, PyPI, crates, and Go ecosystems, narrowed to the thousands with attacker-triggerable CI/CD workflows, and then turned AI agents loose to confirm which were actually exploitable. 654 repositories were flagged in this single scan. More than 300 were confirmed fully exploitable – attacker-controlled code execution, credential theft, or outright supply chain compromise – at companies including Microsoft, Google, and Apache.
There are millions of repositories that are potentially affected by this same pattern.
Across the repositories Novee examined, the proven impact covered the full build-and-release pipeline: 
Supply chain compromise – publishing malicious packages to npm, PyPI, crates.io, Docker/GHCR, and Helm 
Pushing code directly to protected branches 
Forging CI checks and bypassing merge gates 
Stealing cloud credentials across AWS, GCP, and Netlify 
Persistent compromise of self-hosted runners 
Bot impersonation and social engineering 
Similar patterns turned up at LLVM, OpenHands, and dozens more . Here are just a handful more examples of the level of impact:
Vulnerability Class Finding App-Code Equivalent Command Injection Attacker-controlled input (branch names, PR titles, comment bodies) interpolated directly into shell commands and executed Unsanitized user input passed to os.system(), exec(), or SQL queries Code Injection Attacker-controlled input interpolated into JavaScript code (actions/github-script) and evaluated at runtime Server-side template injection (SSTI), eval() of user input Broken Authorization Authorization logic that existsbut fails silently. Not a missing check, but a logic bug in the check itself (e.g., checking a property that doesn’t exist on the triggering event type). Broken access control where isAdmin() returns true due to a null-check bug Cross-Workflow Privilege Escalation Untrusted data from a low-privilege workflow crosses into a high-privilege workflow via artifacts, outputs, or env files. Neither workflow is vulnerable alone, but the exploit exists in the composition. Deserialization chains, confused-deputy attacks, TOCTOU race conditions: each component correct, but the interplay exploitable. 
Why This Class of Flaw Is Invisible to Legacy Security Tools 
This supply chain vulnerability lies in the foundational open-source plumbing the entire industry runs on, and the kind of issue that hides from scanners because, technically, every individual piece is working as designed. The workflow does what it was told. The vulnerability exists only in the composition – untrusted data crossing a trust boundary that no one audited.
SAST and DAST – any tool across an AST suite – won’t be able to reason about a cross-workflow finding. Existing tools do pattern-matching on single files, but the most dangerous vulnerabilities we found are multi-step exploit chains.
A deterministic scanner checking one workflow file sees valid YAML. An attacker sees a 4-step chain to permanent credentials. Finding chains like these requires:
Understanding what a workflow is supposed to do and, crucially, what should never happen. “An anonymous outsider can act with maintainer privileges” is only a finding if you understand the intended trust model in the first place. 
Reasoning across boundaries. The findings are multi-step chains: a comment runs code that steals a non-expiring key; a pull request poisons the package that every downstream user installs. Each step in isolation looks benign. The risk only appears when you can see how they connect. 
Proof . A theoretical “this might be exploitable” is just noise. What matters is whether the chain works, end to end, with evidence behind it. 
How Novee Finds It 
Finding these chains requires attacker reasoning across multiple workflows, privilege boundaries, and time. That’s what Novee’s AI agents do, and that’s what no scanner, no linter, and no manual review caught at the organizations where we validated vulnerabilities. This is the core Novee capability – proactive CI/CD and supply chain exposure discovery that identifies exploitable attack paths before they become incidents .
The same engine that found these issues across Microsoft, Google, and Apache can run against any organization’s external attack surface, delivered through Novee’s Continuous External Attack Validation . Starting from your domain, Novee continuously discovers your entire internet-facing environment, including the assets you’ve forgotten, groups them into named business applications, validates which risks are genuinely exploitable with reproduction steps and a working PoC, and delivers stack-specific remediation that’s automatically retested to confirm the fix held.
The same properties that make this class of flaw hard to catch are the ones Novee is designed around:
It reasons about what each application and workflow does, and what should never happen. 
It finds and proves chained attack paths, not isolated, low-context findings. 
Every result is independently validated by separate agents, so what reaches your team is real exploitable risk – no false positives to triage. 
It runs continuously and on change, which is exactly how CI/CD configurations drift into danger in the first place. 
Your software supply chain is part of your attack surface, whether or not anyone is testing it the way an attacker would. Novee already does. 
Are You Exposed? What CISOs and Security Leaders Need to Do Now 
The next Shai-Hulud isn’t just a code bug. It’s a systemic exploitable pattern in the software backbone of the modern enterprise, and it’s exploitable by anyone with a free account.
If your organization runs software on GitHub or any workflow management system, or depends on open-source developer projects that do, you should assume this is relevant to you and proactively check whether you’re impacted. The good news: even if you are, the fix is straightforward, once you know where to look.
Contact us: Novee’s team can guide you into learning whether or not you’re exposed.
How Novee AI Pentesting Can Help You Stay Ahead of Cordyceps — and the Next Supply Chain Threat  
Novee is a continuous AI pentesting platform that combines the capabilities of an AI hacker and an AI defender, continuously learning how your environment behaves to uncover real exploitable risk, prove exploitability, and close the loop with verified remediation at scale. 
Novee’s offensive AI agents map, reason, exploit, and validate attack paths the way real attackers do, including the chained attack paths, CI/CD misconfigurations, and supply chain exposures that scanners miss and point-in-time pentests can’t keep pace with. We work with organizations across technology, financial services, manufacturing, and more. 
Get a demo to see how Novee can protect your organization from Cordyceps and the supply chain threats that come after it.
You might also like
Top 8 Briefings to Attend at Black Hat 2026 
Novee Marketing 
June 27, 2026 
A CISO's guide to the must-attend Black Hat 2026 briefings on AI red teaming, agent exploitation, and offensive security — from prompt injection to pre-auth RCE. 
6 mins 
Read more
What a Penetration Testing Report Should Include (And What Red Flags to Watch For) 
Novee Marketing 
June 24, 2026 
A penetration testing report should reveal real business risk, exploit paths, and clear remediation steps that drive action. 
10 mins 
Read more
How AI-Powered Attacks Are Outpacing Traditional Security Defenses 
Novee Marketing 
June 24, 2026 
AI-powered attacks now reach data exfiltration in under 72 minutes. Discover how attackers exploit AI to compress the kill chain — and what security teams must do to keep up. 
11 mins 
Read more
Stay updated
Get the latest insights on AI, cybersecurity, and continuous pentesting
delivered to
your
inbox
Your browser does not support the video tag.
Follow the path real attackers take 
Book a demo 
Company 
About 
News 
Careers 
Resources 
Blog 
Novee Labs 
Glossary 
Security Guides 
Compare 
Novee vs DAST 
Novee v. DIY Generic LLMs 
Stay Connected
Privacy Policy 
Terms of Service 
© Novee. All Rights reserved.

