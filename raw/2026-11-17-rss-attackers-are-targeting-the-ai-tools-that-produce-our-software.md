---
"source": "https://www.thoughtworks.com/insights/blog/generative-ai/attackers-are-targeting-the-ai-tools-that-produce-our-software"
"title": "Attackers are targeting the AI tools that produce our software"
"author": "Jim Gumbley, Gautam Koul"
"date_published": "2026-11-13"
"date_clipped": "2026-11-17"
"category": "Security & Ethical Hacking"
"source_type": "rss"
---

# Attackers are targeting the AI tools that produce our software

[Blogs
Back](https://www.thoughtworks.com/insights/blog)

- [Generative AI](https://www.thoughtworks.com/what-we-do/emerging-technology/genai)
- [Security](https://www.thoughtworks.com/security)
- [Blog](https://www.thoughtworks.com/insights/blog)

By 

[Jim Gumbley](https://www.thoughtworks.com/profiles/j/jimgumbley)
 and

[Gautam Koul](https://www.thoughtworks.com/profiles/g/gautam-Koul)

Published: November 13, 2026

*AI coding tools are now part of our software supply chain. We share six practical measures that can help address the risk.*

For around 11 hours on October 29, 2026 malicious versions of Anthropic’s Claude Code extension were available through Cursor’s marketplace, potentially affecting up to 5,000 users. The malicious code collected information about developers’ machines and attempted to install a backdoor for persistent remote access.

If those were your developers, which systems could an attacker reach? That’s the point leaders should take from this incident. Coding assistants, editors, MCP servers and their extensions are part of your software supply chain, and attackers have noticed. Today’s AI agents can execute shell commands, read local secrets and call external services autonomously, making a single compromised tool potentially very dangerous.

## Why developer tools are such an attractive target

A developer’s workstation holds source code, authenticated sessions, cloud credentials and connections to build and deployment systems. For some developers, those connections reach production systems containing sensitive data. Compromise one tool and you land somewhere very valuable.

The business model is simple. Attackers acquire access, work out what it unlocks and turn it into money through stolen code, extortion, ransomware partnerships or crypto mining.

Researchers from security firm Wiz tracked one such group of attackers, called TeamPCP. They found that they have hit development tools including Trivy, a software security scanner and LiteLLM, a gateway for AI coding use that helps with access to language models and limiting token costs. Each case saw stolen credentials exploited within hours, followed by exploration of victims’ cloud environments. A popular developer tool is an efficient way to reach many environments at once.

The strategy predates AI: in 2020, the enormous SolarWinds breach showed how a single trusted update could open the door to thousands of customers. What’s changed is that AI coding tools now sit in that strategic position, close to the developers, code, commands and services that deliver software. That makes them a juicy target for cyber attackers looking to make money quickly.

## Developer tools hold the keys, so lets treat them that way

That brings us to the central question for organizations: how should we establish trust in the AI tools on which software delivery increasingly depends?

Six practical measures help organizations establish that trust and prepare for a compromise.

## 

### 1. Apply zero trust to dependencies

At Thoughtworks, our sensible default approach is to apply zero trust thinking to build and delivery infrastructure. For developer tooling, that means zero trust for dependencies: establish confidence through evidence, grant only the access required and keep checking how the component behaves.

- **Trust is not all-or-nothing:** This doesn’t mean you can’t trust anything. A component maintained by a known team, with reviewed code and a controlled release process, gives you more reason for confidence than an unfamiliar package installed without scrutiny.
- **Verify everything:** The build process, marketplace and update mechanism all affect the integrity of what lands on your machine.

  ##

### 2. Own your software supply chain

Development teams should take primary responsibility for the supply chain of the software they build, including the AI assistants, editors, extensions and build tools used to produce it.

- **Treat tool adoption as an engineering decision:** Understand why a tool is needed, where it comes from, what access it requires and how it will be maintained before adopting it.
- **Keep ownership with the delivery team:** Guidance and approvals given by central security teams is important, but it does not transfer first-line responsibility; security specialists provide guardrails and shared standards, while engineering teams manage day-to-day risk.

  ##

### 3. Control updates

Treat updates to tools with access to code and credentials as changes to a sensitive environment.

- **Use pinning of dependencies where appropriate:** Use proven versions, staged deployments or a short review window before rolling out newly published packages.
- **Verify integrity:** Check package signatures and provenance wherever those mechanisms are supported.
- **Maintain a fast-track lane:** Ensure your update controls include an expedited path for urgent, verified security patches.

## 

### 4. Limit the blast radius

Assume that a tool or extension will eventually be compromised and focus on limiting what it can reach.

- **Eliminate overly broad privileges:** Run developer tools without unnecessary administrator rights, separate everyday dev access from production permissions and replace long-lived keys with narrowly scoped, short-lived credentials.
- **Enforce boundaries:** Use sandboxes and managed development environments with explicit controls around files, credentials and outbound network connections - covering both the editor and commands executed by an AI agent.

Do some threat modeling to explore the impact of a compromised component. Could it modify a local working copy of code? Push changes to a repository, alter a deployment pipeline or reach customer data? This should reveal opportunities to tighten over permissive setups.

## 

### 5. Be ready to respond

Bring developer tooling into your organization’s existing incident response playbooks before an incident forces you to improvise.

- **Rehearse the scenario:** Run tabletop exercises with engineering, platform and security teams to practice identifying affected machines, isolating endpoints, preserving evidence and revoking exposed tokens and sessions.
- **Plan for deep remediation:** Simply uninstalling a malicious extension often leaves persistence mechanisms behind as seen in the Cursor incident, so prepare workflows for full workstation wipes, reloads and repository/cloud audits.
- **Feed lessons back:** Use every incident or near miss to tighten tool approval processes, access boundaries and detection rules.

## 

### 6. Monitor the development environment

Establish security monitoring around developer machines and the services they access. Useful indicators might include unexpected SSH key changes, new startup mechanisms, unusual access to credentials and editor processes creating tunnels to unfamiliar destinations.

This becomes powerful for detection when endpoint signals are correlated with identity, repository and cloud activity. An unusual process on a laptop becomes more significant when it is followed by unfamiliar authentication, bulk repository access or changes to a delivery pipeline. Alerts need clear ownership and responders who understand normal engineering workflows. Establish security telemetry around developer machines and the downstream services they access.

- **Watch for workstation anomalies:** Alert on unexpected SSH key changes, new startup mechanisms, unusual credential file access and editor processes opening network tunnels to unfamiliar destinations.
- **Correlate across systems:** Combine endpoint signals with identity, repository and cloud logs: an unusual local process becomes high-priority when followed by unfamiliar authentication, bulk repo cloning or CI/CD pipeline changes.

## Preparing for the next supply-chain attack

The growing importance of AI coding tools makes the security of development environments a business concern. AI tools sit close to the code, credentials and connections through which organizations deliver change. Preparedness means understanding that position, containing the consequences of a failure and having the visibility to intervene before a compromised tool becomes a wider enterprise breach.

Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
