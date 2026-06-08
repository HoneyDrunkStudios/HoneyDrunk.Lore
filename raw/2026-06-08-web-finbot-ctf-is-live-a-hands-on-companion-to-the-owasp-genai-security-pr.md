---
source: "https://genai.owasp.org/2026/04/14/finbot-ctf-is-live-a-hands-on-companion-to-the-owasp-genai-security-project/"
title: "FinBot CTF Is Live: A Hands-On Companion to the OWASP GenAI Security Project"
author: "OWASP Gen AI Security Project"
date_published: "2026-04-14"
date_clipped: "2026-06-08"
category: "Security & Ethical Hacking"
source_type: "web"
---

# FinBot CTF Is Live: A Hands-On Companion to the OWASP GenAI Security Project

Source: https://genai.owasp.org/2026/04/14/finbot-ctf-is-live-a-hands-on-companion-to-the-owasp-genai-security-project/

At RSAC 2026, the community got an early look at FinBot through the OWASP GenAI Security Summit and Open Workshop, including the session **“FinBot: An Agentic AI Capture-The-Flag Deep Dive.”** FinBot was also showcased at AppSec Village in **“AI Risks Through the OWASP GenAI Security Project & FinBot CTF,”** where it was used to demonstrate how agentic AI systems can fail in practice through a live walkthrough and audience participation.

Now that the platform is live, it is a good time to formally describe what FinBot is and how it fits into the broader OWASP effort. FinBot is part of the **OWASP GenAI Security Project’s Agentic Security Initiative** and is designed to help builders and defenders better understand and mitigate agentic AI risks through a hands-on environment. The OWASP GenAI project describes it as an interactive Agentic Security CTF built around a simulated financial-services-focused application and designed as the **“Juice Shop for Agentic AI.”**

That role is best understood as complementary to the parent project. The **OWASP Top 10 for Agentic Applications for 2026** is a globally peer-reviewed framework developed with contributions from more than 100 experts, researchers, and practitioners, and it provides practical guidance for securing AI agents that plan, act, and make decisions across complex workflows. FinBot complements that guidance by giving practitioners a place to interact with agentic risk directly and see how those patterns emerge in a live system.

FinBot simulates a multi-agent vendor management platform with autonomous onboarding, fraud detection, invoice processing, and communications, all powered by LLMs with real tool access. Its challenges cover prompt injection, tool misuse, policy bypass, data exfiltration, privilege escalation, and remote code execution, with mappings to the OWASP Top 10 for LLM Applications, the OWASP Top 10 for Agentic Applications, CWE, and MITRE ATLAS.

The platform also reflects an important reality about agentic AI security: the risk is not limited to a single chatbot interaction. In FinBot, malicious vendor data can flow upstream into administrative AI workflows and laterally into other tenants through shared context. On the administrative side, participants configure MCP tool servers (to simulate supply chain attacks) that agents rely on and can observe how tampered MCP tool descriptions or compromised external tool servers can influence trusted agents – threats can come from other vendors, the supply chain, and the tools themselves.

FinBot is therefore best viewed as a hands-on companion to the OWASP GenAI Security Project and the Agentic Security Initiative. The parent project provides the shared guidance, taxonomy, and direction. The Agentic Top 10 provides the framework. FinBot helps bring those ideas to life in a way that is practical, interactive, and grounded in how agentic systems actually operate.

Finally, FinBot would not exist without the energy and contributions of the broader community. We want to thank the contributors, workstream leads, and OWASP GenAI Security Project leadership who have helped shape the platform, strengthen its quality, and move the work forward. FinBot is very much a community-built effort, and we are excited to continue growing it with practitioners, builders, and defenders across the ecosystem. To meet the people behind the project, visit the [About page](https://owasp-finbot-ctf.org/about).

**Explore the platform:** [OWASP FinBot CTF
](https://owasp-finbot-ctf.org/)

**Learn the framework:**

[OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)


**Learn more about the platform:**

[How FinBot Works](https://owasp-finbot-ctf.org/how-it-works)


**Get involved:**Contribute ideas, feedback, and future challenges through the OWASP GenAI community

[here](https://github.com/GenAI-Security-Project/finbot-ctf).
