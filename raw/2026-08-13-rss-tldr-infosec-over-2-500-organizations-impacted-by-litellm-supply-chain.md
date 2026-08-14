---
source: "https://www.securityweek.com/over-2500-organizations-impacted-by-litellm-supply-chain-attack"
title: "Over 2,500 Organizations Impacted by LiteLLM Supply Chain Attack (2 minute read)"
author: "TLDR InfoSec"
date_published: "2026-08-13"
date_clipped: "2026-08-13"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-08-13"
source_role: "primary-via-tldr"
---

# Over 2,500 Organizations Impacted by LiteLLM Supply Chain Attack (2 minute read)

Source: https://www.securityweek.com/over-2500-organizations-impacted-by-litellm-supply-chain-attack

Supply Chain Security
Over 2,500 Organizations Impacted by LiteLLM Supply Chain Attack
LiteLLM was compromised through the Trivy hack and abused to distribute information-stealing malware to its users.
By
Ionut Arghire
|
August 12, 2026 (5:55 AM ET)
Flipboard
Reddit
Whatsapp
Whatsapp
Email
More than 2,500 organizations and over 430,000 CI/CD pipelines were affected by the LiteLLM supply chain attack earlier this year, CloudSEK reports.
The LiteLLM compromise was disclosed shortly after the supply chain attack on Aqua Security’s Trivy open source vulnerability scanner and was a direct result of it.
According to CloudSEK, TeamPCP , the threat actor behind multiple high-profile open source software (OSS) compromises, never targeted LiteLLM directly.
The open source Python library and proxy server was compromised after its CI pipeline installed the compromised Trivy version automatically. Two LiteLLM versions, namely 1.82.7 and 1.82.8, were pushed to PyPI, providing the hackers with access to all the information LiteLLM touched.
“Trivy, then the [LiteLLM] build system, then the LiteLLM release: one unrevoked token, three tools deep. That chain is what turns a single credential leak into ecosystem-wide exposure,” CloudSEK notes .
“Automated build systems compress time. Once a malicious artifact reaches a registry, scheduled jobs, dependency resolvers, ephemeral runners, developer laptops, and cached layers can copy it rapidly. The forensic and credential-rotation window therefore extends beyond package removal,” the company continues. Advertisement. Scroll to continue reading.
The modified LiteLLM versions contained malicious code executed on every Python invocation, with no explicit import. The payload ran on all systems where the package was installed.
According to CloudSEK, while the affected packages were live for only 40 minutes, the window was long enough for the malicious code to propagate, ultimately exposing 434,000 CI/CD pipelines and impacting over 2,500 organizations.
Nvidia, AWS, Samsung, Salesforce, Cisco, ServiceNow, Accenture Federal Services, Siemens, Regeneron Pharmaceuticals, London Stock Exchange Group, FedEx, Volkswagen, Orange, HP, Deutsche Bahn, NGINX, and Zscaler are only some of the names on CloudSEK’s list .
“The 2,500+ company and 434,000 pipeline figures describe reconstructed exposure. They should not be read as proof that every listed organization was successfully compromised or that every credential was stolen,” CloudSEK says, noting that compromise should be independently verified in each case.
The LiteLLM supply chain attack led to broad sensitive information compromise : package publishing credentials, cloud keys, SSH keys, tokens, environment variables, runtime data, and AI provider keys, among others.
Hackers could use these secrets to take over accounts, steal data, inject malicious commits, achieve persistence, move laterally, disrupt services, deploy malware, and mount various other types of attacks.
Organizations should consider any secret accessible to the LiteLLM library as compromised, including those “present in process memory, injected into the job, stored on disk, or retrievable through an instance metadata service”.
Potentially compromised secrets should be validated, then rotated alongside service accounts and sessions, and logs should be reviewed to determine the exposure scope and timeframe.
According to CloudSEK, the next major supply chain attack will likely target AI infrastructure, as these systems have become “high-value junctions between data, identity, compute, and autonomous action”.
“The incident was not only a software supply chain breach that happened to involve an AI product. It demonstrated that compromising an AI control point can expose the identities and systems around it. Future attacks are likely to target the AI layer precisely because it is connected to everything else,” CloudSEK notes.
Related: Over 400 NPM Packages Infected in ChainDrop Supply Chain Attack
Related: New GitHub, PyPI Policies Boost Supply Chain Security
Related: Multiple Jscrambler Packages Impacted by Supply Chain Attack
Related: More Klue Breach Victims Identified as Hackers Get Hacked
Written By
Ionut Arghire
Ionut Arghire is an international correspondent for SecurityWeek.
Daily Briefing Newsletter
Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert
insights.
More from Ionut Arghire
Mindgard Raises $30 Million to Protect AI Systems Ceva Logistics Operations Disrupted by Cyberattack Fresh Windows Zero-Day Exploited in North Korean Cyberattacks Ivanti EPM Update Patches Remotely Exploitable Flaws SonicWall Patches Critical Vulnerabilities in Discontinued GMS Platform August 2026 Patch Tuesday: Microsoft Fixes 421 CVEs, One Exploited Zero-Day Adobe Urges Immediate Patching of Critical ColdFusion, Campaign Classic Flaws Zoom Patches Zero-Click Code Execution Vulnerability
Latest News
Cybersecurity M&A Roundup: 21 Deals Announced in July 2026 Adobe Commerce Bug Targeted Immediately After Disclosure WordPress 7.0.4 Patches Remote Code Execution Vulnerability Venture Firm Team8 Secures Additional $365 Million Fortinet Patches Authentication Flaws in FortiWeb and FortiManager White House Mobilizes Security Firms for Operations Against Foreign Cybercrime Gangs Critical VMware vCenter Vulnerability in Attackers’ Crosshairs Nightmare Eclipse Drops Windows Zero-Day Exploit ‘ShieldBreak’
Trending
Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts.
Webinar: Rethinking Cyber Defense for AI-Speed Attacks
August 18, 2026
Join this live webinar as we explore if detection-first security operations can keep pace with AI, or if it’s time to rethink prevention as the strongest default.
Register
Virtual Event: CodeSecCon 2026
August 19, 2026
CodeSecCon bridges the gap between dev and security. Discover best practices for secure coding, innovative risk-reduction tools, and safe AI integration to cultivate a true DevSecOps culture. Safely secure your apps!
Register
People on the Move Erika Dean has been appointed Chief Information Security Officer at Tricentis.
C1 has named Jeff St. Clair Chief Revenue Officer.
John Opala has joined Ralph Lauren as Chief Information Security Officer.
More People On The Move Expert Insights
The AI Governance Gap Is a Leadership Problem: Waiting Won’t Close It
Organizations are rushing to implement AI without fully grasping where its legal protections begin and end.
(Steve Durbin)
