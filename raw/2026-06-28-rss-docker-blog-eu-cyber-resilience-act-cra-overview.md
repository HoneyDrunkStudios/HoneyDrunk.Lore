---
source: "https://www.docker.com/blog/eu-cyber-resilience-act-overview/"
title: "EU Cyber Resilience Act (CRA): Overview"
author: "Dan Stelzer and Monique Altman"
date_published: "2026-06-25"
date_clipped: "2026-06-28"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# EU Cyber Resilience Act (CRA): Overview

Source: https://www.docker.com/blog/eu-cyber-resilience-act-overview/

EU Cyber Resilience Act: Overview, Requirements, and Timelines
Posted Jun 25, 2026
Dan Stelzer 
and
Monique Altman 
The EU Cyber Resilience Act (CRA) was officially introduced on December 10th 2024, to protect foundational EU values in the face of rising cyberattack threats. As cyberattacks targeting products with digital elements have grown more frequent and costly, the regulation establishes the first horizontal cybersecurity baseline for all hardware and software products sold in Europe. The urgency is real given that in Omdia’s 2026 software supply chain security report , 77% of organizations reported experiencing a supply chain incident in the last year.
The regulation will take full effect on December 11, 2027, but mandatory vulnerability reporting obligations take effect on September 11, 2026 . For teams building and shipping containerized software , the CRA turns practices like SBOM generation, vulnerability disclosure, and image hardening from voluntary best practices into legal requirements.
This guide covers what the EU CRA requires, who it applies to, how its SBOM mandate connects to container build workflows, and what teams need to do before the compliance deadlines arrive.
Key takeaways
The CRA requires all products with digital elements sold in the EU to meet cybersecurity standards by December 2027. 
Manufacturers must include a machine-readable SBOM in technical documentation for every product. 
Actively exploited vulnerabilities and severe incidents having an impact on the security of a product with digital elements must be reported to authorities within 24 hours starting September 2026. 
Container runtimes distributed commercially into the EU qualify as products with digital elements under the CRA. 
What is the EU Cyber Resilience Act (CRA)? 
Before the CRA , the EU had no single, cross-sector regulation setting cybersecurity baselines for  products with digital elements. A smart thermostat, an enterprise database, and a container runtime were all subject to different (or no) cybersecurity obligations. There was no general obligation to patch vulnerabilities, disclose security incidents, or document the software of products with digital elements launched in the EU market. The CRA closes that gap with a horizontal regulation that applies across several industries, placing the primary burden on manufacturers.
The regulation defines a product with digital elements as any software or hardware product, including its remote data processing solutions and any components placed on the market separately. That scope is intentionally broad: it covers everything from consumer IoT devices to enterprise software platforms to container images distributed through registries. Manufacturers must design products securely, handle vulnerabilities throughout the product lifecycle, and provide transparency about software composition.
How the CRA relates to NIS2 
The CRA is one part of the broader EU cybersecurity strategy that includes other regulatory frameworks, like NIS2 and DORA. Since the CRA and NIS2 both deal with cybersecurity obligations, they’re easy to conflate, but they target different things. The CRA applies to cybersecurity of products with digital elements, while NIS2 applies to the cybersecurity of essential and important entities .
Recital 12 of CRA even affirms that SaaS, PaaS, or IaaS solutions are subject to NIS2, in principle carving them out of its own scope. However, the line is blurry for products depending on cloud infrastructure.
The European Commission’s March 2026 draft guidance introduced a three-part test for determining when a cloud component falls under CRA scope: 
Does the processing happen remotely? 
Would the product lose a core function without it? 
Did the manufacturer design, develop, or is control of that remote component under its responsibility? 
If the answer to all three is yes, the cloud component is part of the product for CRA purposes. Where that test pulls a cloud component into scope and the component processes personal data, the GDPR applies on top of the CRA rather than in place of it, so you still need to assign controller and processor roles and confirm a lawful basis.
Who the CRA applies to 
The CRA assigns obligations based on your role in bringing a product to market.
Role 
Obligations 
Manufacturers 
The heaviest set of obligations. 
The manufacturer has assessment obligations before placing the product on the market, in order to ensure compliance with the cybersecurity requirements set out in the CRA. 
After this process, the manufacturer can affix the CE marking and attach a declaration of conformity to its products. After placement on the market, the manufacturer is required to handle vulnerabilities in the products throughout their lifetime and to report actively exploited vulnerabilities and severe incidents.
Importers and distributors 
Fewer obligations. 
Both must ensure that the manufacturer complied with a set of obligations, but also retain documentation and act upon becoming aware of non-conformity of the product with the CRA or a vulnerability.
Open-source software stewards 
A new CRA category. 
Mainly for micro-enterprises and small and medium-sized enterprises, including start-ups, individuals, non-profit organizations and academic research organizations, that systematically support open-source used in commercial activity. 
Scaled-down obligations covering, in particular, putting in place a cybersecurity policy and vulnerability handling, but also cooperation with market surveillance authorities and certain reporting obligations.
Key requirements for the EU CRA 
The CRA organizes its requirements into two main areas, both defined in Annex I of the regulation: essential cybersecurity requirements for product properties, and vulnerability handling obligations for the product lifecycle.
Security by design 
Products must be designed, developed, and produced to ensure an appropriate level of cybersecurity based on a risk assessment. In practice, this means shipping with secure default configurations, minimizing the attack surface by removing unnecessary components, protecting the confidentiality and integrity of stored and transmitted data, and providing mechanisms for secure updates. 
For container images, the security-by-design requirement maps directly to image hardening:
minimal base layers 
no unnecessary shells or package managers 
secure defaults out of the box. 
The essential requirements also include data minimization: a product should process only personal or other data that is adequate, relevant, and limited to what is necessary for its intended purpose.
Vulnerability handling 
Manufacturers must maintain processes for identifying, documenting, and remediating vulnerabilities throughout the support period they define for each product. This includes coordinated vulnerability disclosure policies, timely security updates, and public disclosure of fixed vulnerabilities with enough detail for users to assess impact and apply remediation. 
Security updates must be provided free of charge for the duration of the support period. Public disclosures should be limited to the technical detail users need and must not expose personal data, such as the identity of a reporter or of affected users, consistent with the CRA’s expectation that disclosures avoid increasing risk and with GDPR limits on publishing personal data.
Transparency and SBOMs 
The CRA also requires manufacturers to include a software bill of materials in the technical documentation for every product with digital elements. The SBOM must be in a commonly used, machine-readable format and must include, at minimum, the top-level dependencies of the product. However, the regulation does not mandate a specific format, but in practice that typically means SPDX or CycloneDX.  Scope the generated SBOM to package and dependency metadata and keep embedded secrets and personal data out of the artifact.
An important nuance: The CRA does not require manufacturers to publish SBOMs publicly. SBOMs must be included in technical documentation and provided to market surveillance authorities on request. Also, the documentation must be retained for ten years after the product is placed on the market, or for the duration of the support period, whichever is longer.
Incident and vulnerability reporting 
Manufacturers must report actively exploited vulnerabilities and severe security incidents to the relevant national Computer Security Incident Response Team (CSIRT) and to ENISA through a single reporting platform. The reporting timelines are:
Reporting timelines:
– 24 hours : early warning notification
– 72 hours : full notification with technical details
– 14 days : final report after a corrective measure is available (for actively exploited vulnerabilities)
– 1 month : final report from the 72-hour submission (for severe incidents)
Note for Privacy: These reports can contain personal data, such as a reporter’s identity or affected-user details, so limit each report to the technical information the CSIRT and ENISA actually need and handle any personal data in line with the GDPR.  Notifications should also avoid disclosing information that would increase risk to users.
Conformity assessment 
Before placing a product on the EU market, manufacturers must complete a conformity assessment to verify compliance with the essential cybersecurity requirements. The type of assessment depends on how the product is classified under the CRA.
Product categories and conformity assessment 
The CRA classifies products into three tiers based on their cybersecurity risk, with each tier subject to increasingly rigorous conformity assessment procedures.
If you’re shipping container runtimes, you likely fall into the Important Class II category and will need a third-party assessment. Products that pass their conformity assessment receive the CE marking, which indicates compliance with the CRA and allows them to be sold on the EU market. Products that fail, or that are found to be non-compliant after placement, can be ordered withdrawn or recalled by national market surveillance authorities.
CRA timeline: 3 Deadlines that matter 
The CRA entered into force on December 10, 2024, but its obligations phase in over three years . Each milestone introduces a distinct set of requirements.
Date 
Milestone 
What takes effect 
June 11, 2026 
Conformity assessment bodies 
Member states must designate notifying authorities. Conformity assessment bodies begin formal notification and can start conducting assessments. 
September 11, 2026 
Reporting obligations 
Manufacturers must report actively exploited vulnerabilities and severe security incidents to CSIRTs and ENISA. This retroactively applies to all products already on the EU market, not just new ones. 
December 11, 2027 
Full enforcement 
All essential cybersecurity requirements take effect: security by design, SBOM in technical documentation, vulnerability handling, conformity assessment, CE marking. Non-compliance triggers fines. 
The key detail most teams miss: the September 2026 reporting obligation is applicable to products that are already in the market. It retroactively applies to products already on the EU market, not just new releases. If you are selling container images to EU customers today, your 24-hour reporting clock starts in months, not years.
Penalties for non-compliance 
Article 64 of the CRA establishes three penalty tiers for non-compliance, with fines set at the member-state level but capped by the regulation:
Up to €15 million or 2.5% of global annual turnover (whichever is higher) for failure to comply with essential cybersecurity requirements and other core obligations (Art. 64 (2))  
Up to €10 million or 2% of global annual turnover (whichever is higher) or failure to comply with other CRA obligations (Art. 64 (3)) 
Up to €5 million or 1% of global annual turnover (whichever is higher) for supplying incorrect, incomplete, or misleading information to authorities (Art. 64 (4)) 
Beyond fines, market surveillance authorities can order product withdrawals, recalls, or outright bans from the EU market. For organizations selling software products into the EU, losing market access is often a more significant consequence than the fine itself.
Microenterprises and small enterprises are generally exempt from fines for missing the 24-hour early warning deadline on vulnerability and incident reporting. Open-source software stewards are not subject to fines for any CRA infringement.
Open-source software and the CRA 
The CRA’s treatment of open source was one of the most debated aspects during the legislative process. The final text draws a clear line based on commercial activity.
Free and open-source software that’s not used in the course of a commercial activity, either directly or through support, is outside the CRA’s scope. Individual developers and volunteer maintainers are not classified as manufacturers under the regulation, as long as they operate outside a commercial activity. And the CRA explicitly does not apply to open-source software supplied for distribution outside the scope of a commercial activity.
However, the regulation introduces a new role: the open-source software steward . 
A “steward” is a legal person (a company or foundation, not an individual) that systematically supports the development of open source software intended for commercial activities. The CRA applies a light-touch regime for stewards with limited obligations. They must mainly:
Maintain a cybersecurity policy. 
Report actively exploited vulnerabilities. 
Cooperate with market surveillance authorities.  
Critically, stewards are not subject to financial penalties for CRA infringements.
Organizations that distribute open-source software under a commercial model, whether through paid support or commercial container image registries, are classified as manufacturers, not stewards. The distinction matters because manufacturers carry the full weight of CRA obligations, including conformity assessment and CE marking.
What the CRA means for container teams 
Everything above applies to the full universe of digital products. Here’s where it gets specific. Container images and runtimes distributed commercially into the EU qualify as products with digital elements under the CRA. If your organization publishes container images in a registry that EU customers can pull from, and those images are part of a commercial offering, the CRA applies and you may be considered a manufacturer. This is true regardless of where your organization is headquartered.
The practical implications span the entire container lifecycle:
Image composition transparency: Every image needs a machine-readable SBOM that documents at least the top-level dependencies. Image-layer SBOMs generated at build time, which capture OS packages, runtime libraries, and transitive dependencies, go further than the CRA’s minimum. 
Vulnerability management: Organizations must have processes to track, remediate, and report vulnerabilities in the components their images contain. Starting September 2026, all vulnerability and incident reporting obligations listed in Article 14 come into effect. 
Security by design: Images should ship with minimal attack surfaces, secure default configurations, and no unnecessary components. Hardened base images with shells, package managers, and debug tools removed satisfy this requirement more directly than standard community images. 
Provenance and integrity: The CRA’s essential requirements include protecting the integrity of the product and verifying that components have not been tampered with. Cryptographic signatures and provenance attestations address this directly. 
Support periods: Manufacturers must define and communicate a support period during which they will handle vulnerabilities. For container images, that means committing to a patch and rebuild cadence for the lifecycle of each supported image tag. 
Compliance starts at the image layer 
The CRA raises the bar for every organization that ships software into the EU. For container teams, the requirements map directly to practices the industry has been moving toward: hardened images, build-time SBOMs, provenance attestations, vulnerability monitoring, and defined support lifecycles. The difference is that these practices are no longer optional.
Thankfully, Docker Hardened Images ship with the artifacts the CRA demands: complete SBOMs, SLSA Build Level 3 provenance with non-falsifiable attestations, OpenVEX exploitability data, and cryptographic signatures. The images are minimal by default, continuously rebuilt against upstream fixes, and backed by defined support periods. Pair that with continuous vulnerability monitoring against SBOM data limited to package and component metadata and excluding personal data and embedded secrets, and the CRA’s 24-hour reporting clock starts with a known blast radius rather than a manual triage.
Get started with Docker Hardened Images → 
Explore vulnerability monitoring with Docker Scout → 
Frequently asked questions 
Does the CRA apply to container images?
Yes, generally. Container images distributed commercially into the EU qualify as products with digital elements under the CRA. This applies whether the images are distributed as part of a software product, sold as managed services, or published in a commercial registry. The regulation applies based on commercial availability in the EU market, not on where the manufacturer is headquartered.
What SBOM format does the CRA require?
The CRA requires a commonly used, machine-readable format but does not name a specific standard. In practice, that usually means SPDX or CycloneDX . For container workflows, SPDX is the format BuildKit generates natively as an image attestation. Whichever format you use, scope the SBOM to package and dependency metadata and exclude embedded secrets and personal data from the generated artifact.
Do I have to publish my SBOM publicly?
No. The CRA requires SBOMs to be included in technical documentation and provided to market surveillance authorities upon request. There is no obligation to make them publicly available. However, organizations that do publish SBOMs as attestations attached to their images make it easier for downstream consumers to verify compliance and assess risk. If you do publish, scrub the SBOM and attestations of secrets, internal hostnames, and any personal data first, because a published artifact is difficult to retract.
Are open-source projects exempt?
Open-source software is outside the CRA’s scope as far as they are not made available on the market, and therefore supplied for distribution or use in the course of a commercial activity. Individual volunteer maintainers are not classified as manufacturers as far as they operate outside a commercial activity. However, organizations that distribute open-source software commercially (through paid support, managed services, or commercial registries) may be classified as manufacturers and subject to the full set of CRA obligations.
When do the CRA’s SBOM requirements take effect?
The SBOM requirement is part of the essential cybersecurity requirements in Annex I, which take full effect on December 11, 2027 . However, the vulnerability reporting obligations that begin on September 11, 2026 are operationally much harder to meet without SBOM data, so the practical imperative to have SBOMs in place arrives well before the formal deadline.
Source 
Omdia,  Securing the Software Supply Chain: Strategic Approaches to Support Scaling Development with AI Adoption , May 2026.
Concepts 
Docker Hardened Images 
Docker Scout 
security 
software supply chain security 
Products 
Table of contents 
Related Posts
May 12, 2026 
Docker AI Governance: Unlock Agent Autonomy, Safely
Introducing Docker AI Governance: centralized control over how agents execute, what they can reach on the network, which credentials they can use, and which MCP tools they can call, so every developer in your company can run AI agents safely, wherever they work. Your laptop is the new prod Agents are the biggest productivity unlock…
Srini Sekaran 
Read now 
Jun 26, 2026 
What Does EU AI Act Compliance Require?
Learn what EU AI Act compliance requires at each risk tier, key deadlines through 2027, and how engineering teams can operationalize AI governance.
Dan Stelzer 
and
Monique Altman 
Read now 
Jun 25, 2026 
How to Generate an SBOM for Container Workflows
Learn when, where, and how to generate SBOMs for container images. Covers build-time vs. post-build approaches, quality criteria, and CI/CD integration.
Aditya Tripathi 
Read now 
Jun 25, 2026 
EU Cyber Resilience Act: Overview, Requirements, and Timelines
Learn what the EU Cyber Resilience Act requires, including SBOM mandates, vulnerability reporting, and compliance deadlines for container teams.
Dan Stelzer 
and
Monique Altman 
Read now
