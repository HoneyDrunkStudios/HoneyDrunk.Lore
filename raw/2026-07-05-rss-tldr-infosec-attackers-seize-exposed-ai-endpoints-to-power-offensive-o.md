---
source: "https://www.darkreading.com/cloud-security/attackers-hijack-exposed-ai-endpoints-power-offensive-ops"
title: "Attackers Seize Exposed AI Endpoints to Power Offensive Ops (3 minute read)"
author: "TLDR InfoSec"
date_published: "2026-07-02"
date_clipped: "2026-07-05"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-07-02"
source_role: "primary-via-tldr"
---

# Attackers Seize Exposed AI Endpoints to Power Offensive Ops (3 minute read)

Source: https://www.darkreading.com/cloud-security/attackers-hijack-exposed-ai-endpoints-power-offensive-ops

Informa TechTarget | SearchSecurity Cybersecurity Dive InformationWeek Channel Dive Explore our brands An Informa TechTarget Publication Dark Reading Resource Library Black Hat News Omdia Cybersecurity Advertise Newsletter Sign-Up Newsletter Sign-Up Cybersecurity Topics Related Topics Application Security Cybersecurity Careers Cloud Security Cyber Risk Cyberattacks & Data Breaches Cybersecurity Analytics Cybersecurity Operations Data Privacy Endpoint Security ICS/OT Security Identity & Access Mgmt Security Insider Threats IoT Mobile Security Perimeter Physical Security Remote Workforce Threat Intelligence Vulnerabilities & Threats Recent in  Cybersecurity Topics Cyber Risk Chinese LLMs Broaden the Gap Between Attackers & Defenders Chinese LLMs Broaden the Gap Between Attackers & Defenders by Robert Lemos Jul 3, 2026 4 Min Read Vulnerabilities & Threats Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them. Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them. by Jeffrey Schwartz Jul 2, 2026 8 Min Read World Related Topics DR Global Middle East & Africa Asia Pacific Latin America See All The Edge DR Technology Events Related Topics Upcoming Events Podcasts Webinars SEE ALL Resources Related Topics Resource Library White Papers Reports Webinars Newsletters Podcasts Heard It From a CISO Reporters' Notebook Dark Reading's 20th Videos Dark Reading Polls Partner Perspectives Meet the Editors Advertise With Us About Us Dark Reading Resource Library Сloud Security Application Security Cyber Risk Endpoint Security News Attackers Seize Exposed AI Endpoints to Power Offensive Ops Threat actors don't need any special authentication to reach a target endpoint — they just need to know where it is.
Alexander Culafi , Senior News Writer , Dark Reading June 30, 2026
4 Min Read Source: PhonlamaiPhoto via Getty Images Threat actors are trying to leverage organization-owned AI agents to power complex threat activity. 
Between March and May, Zenity researchers observed three distinct campaigns leveraging its honeypots' large language model (LLM) infrastructure as resourcing for offensive AI operations , exposing Ollama and LiteLLM endpoints. What's most fascinating about this attack vector is that it doesn't require a full-scale compromise, just knowledge of an exposed endpoint.  
More specifically, Zenity's blog post notes that attackers exploit "the inference endpoints that self-hosted AI software exposes for applications to call." The attacker doesn't need any special authentication to reach them; they just need to know where the endpoint is. Examples of such endpoints include the Ollama "/api/generate" and "/api/chat" endpoints on port 11434, and LiteLLM's "/v1/responses" endpoint on port 4000. 
Three Attackers Leveraging AI Infrastructure The three operators used the tooling for different use cases. Two were autonomous penetration testing frameworks (Strix and HexStrike AI) and one was "an OpenAI Codex agent carrying a persona built to suppress safety refusals and assisting in web reverse-engineering work." 
Related: Amazon Q VS Extension Flaw Leads to Cloud Credential Theft 
"The approach needs no software exploit. The attacker simply configures an agent or client (e.g., a LiteLLM client, the CherryStudio desktop app, or the Codex CLI) to use the exposed endpoint as its model backend," Zenity researchers said . "The agent's entire 'brain' then rides in the request body: its system-prompt persona and its tool definitions, which is exactly what our sensors captured. Operators typically send a small 'hello' probe first to confirm the endpoint answers, then submit the full payload." 
For the Strix operator, a single IP source used a LiteLLM client to send a 140,000-character prompt to leverage the client to weaponize Strix against an unidentified French auction house. Notably, the prompt instructed the agent to never ask for permission, run non-stop, never identify "Strix" or any identifiable names/markers in the agent's actions, and to "GO SUPER HARD on all targets." Zenity's sensors caught and thwarted the effort, though the presence of persistent "retry" commands suggested a potential live operator.  
For HexStrike AI, the attacker pointed the desktop LLM client at the honeypot's Ollama instance and sent it the penetration testing orchestration servicer's 150-plus offensive tool toolset. There was never a target identified in this attempt, suggesting the operator may have been in the staging process for an attack.  
Related: Name That Toon: Mark of (Cybersecurity) Progress 
A third IP source pointed an OpenAI Codex agent at a honeypot's LiteLLM proxy and, under the persona of a security auditor, directed the agent to conduct Web reverse-engineering work. 
Part of what enables these attacks is how Ollama and LiteLLM handle authentication. According to Zenity, Ollama ships with no built-in authentication on its default port (the aforementioned 11434) and LiteLLM authentication is opt-in, dependent on whether a user sets a master key. There is also a common placeholder key (sk-1234) attackers have been known to target. 
Then there's the exposure element. Ollama defaults to a local host but is commonly misconfigured to be exposed to all interfaces, and LiteLLM's proxy is Internet-facing on a public host by default. 
Don't Expose Your AI Infrastructure or Else Michael Bargury, chief technology officer (CTO) and co-founder of Zenity, tells Dark Reading that, for the most part, customers own their AI footprint when it comes to a question of who is responsible. That said, it's not cut and dried. 
"A customer's use of an AI platform, cloud infrastructure, third-party and homegrown agents results in a new attack surface. As a customer, you own what you build and deploy," he says. "However, vendors are accountable for the securability and inspectability of their platforms. They should provide secure defaults and allow customers to own their security outcomes by providing ways for customers to inspect and hook their runtimes." 
Related: LatAm Vibe Hackers Generate Custom Hacking Tools on the Fly 
For organizations that want to protect themselves from these kinds of attacks, Zenity recommends watching for requests from commonly abused endpoints, particularly those carrying full-agent payloads rather than a standard prompt; to block common request body indicators such as prompts that include a full suite of tooling or requests involving models you don't host; to block requests associated with penetration testing tools or unsafe personas; and to block IP addresses used by the operators.  
Broader recommendations include: don't expose model back ends to the Internet wherever possible; require real authentication and reject default or placeholder keys; inspect the request body from outside sources; and monitor the traffic coming through to your AI infrastructure. 
For CISOs, Bargury says a big takeaway is that attackers are showing increasing AI agentic literacy and are finding new ways to target organizations. 
"Attackers are actively looking to discover and hijack AI infrastructure and use your tokens to achieve their goals," he says. "Assume any AI system you put on the Internet will be targeted by AI literate malicious actors within hours." 
About the Author Alexander Culafi
Senior News Writer, Dark Reading
Alex is an award-winning writer, journalist, and podcast host based in Boston. After cutting his teeth writing for independent gaming publications as a teenager, he graduated from Emerson College in 2016 with a Bachelor of Science in journalism. He has previously been published on VentureFizz, Search Security, Nintendo World Report, and elsewhere.  
At Dark Reading, he covers a variety of cybersecurity topics, including the cybercrime ecosystem, open source security, and the intersection between AI and threat actors. In his spare time, Alex hosts the weekly Nintendo podcast, "Talk Nintendo Podcast," and works on personal writing projects, including two previously self-published science fiction novels. 
He has received numerous awards, including TechTarget's Writer of the Year in 2022 as well as more than 10 Azbee awards for his reporting between 2022 and today.  
See more from Alexander Culafi Want more Dark Reading stories in your Google search results? Add Us Now More Insights Industry Reports The State of Cloud Security: The Latest Challenges
The total economic impact™ of Snyk
How Organizations Are Managing Incident Response
How Enterprises Are Developing Secure Applications
Inside RSAC 2026: security leaders reveal the risks redefining your defense strategy
Access More Research Webinars Securing the AI Era: Shadow AI, AI Agents, and Why AI Detection and Response Changes Everything
Practical Zero Trust Implementation on a Budget in the Age of Mythos
Building a Risk Based Vulnerability Management Program
Threat Hunting That Gets Big Results Despite Small Budgets
Say Yes to AI: Securing Innovation Without Compromise
More Webinars Editor's Choice Cybersecurity Operations Why Identity Security Is Your Cyber Career Entry Point Why Identity Security Is Your Cyber Career Entry Point by Kristina Beek Jun 30, 2026 Cyberattacks & Data Breaches EdTech Attackers Shift From Schools to Their Software Suppliers EdTech Attackers Shift From Schools to Their Software Suppliers by Arielle Waldman Jun 25, 2026 Want more Dark Reading stories in your Google search results?
Keep up with the latest cybersecurity threats, newly discovered vulnerabilities, data breach information, and emerging trends. Delivered daily or weekly right to your email inbox. Subscribe Aug 1-6 | Mandalay Bay, Las Vegas Use code: DARKREADING & save $200 on a Briefings pass or $100 on a Business pass
The premier cybersecurity event returns. GET YOUR PASS Discover More Black Hat Omdia Working With Us About Us Meet the Editors Advertise Reprints Join Us Newsletter Sign-Up Follow Us Copyright © 2026 TechTarget, Inc. d/b/a Informa TechTarget. This website is owned and operated by Informa TechTarget, part of a global network that informs, influences and connects the world’s technology buyers and sellers. All copyright resides with them. Informa PLC’s registered office is 5 Howick Place, London SW1P 1WG. Registered in England and Wales. TechTarget, Inc.’s registered office is 275 Grove St. Newton, MA 02466.
Home | Cookie Policy | Privacy | Terms of Use Your Privacy Choices
