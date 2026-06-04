---
source: "https://www.bleepingcomputer.com/news/security/red-hat-npm-packages-compromised-to-steal-developer-credentials/"
title: "Red Hat npm packages compromised to steal developer credentials"
author: "Lawrence Abrams"
date_published: "2026-06-01"
date_clipped: "2026-06-04"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Red Hat npm packages compromised to steal developer credentials

Source: https://www.bleepingcomputer.com/news/security/red-hat-npm-packages-compromised-to-steal-developer-credentials/

Red Hat npm packages compromised to steal developer credentials 
By Lawrence Abrams 
June 1, 2026 
05:38 PM 
0 
More than 30 npm packages under Red Hat's '@redhat-cloud-services' namespace were compromised in a supply-chain attack that distributed a new variant of the Shai-Hulud credential-stealing malware, dubbed "Miasma."
The incident was discovered by security firms Aikido and OX Security , which found dozens of package versions backdoored with malware designed to steal developer credentials, cloud secrets, SSH keys, CI/CD tokens, and other sensitive information.
According to Aikido, the compromised packages receive roughly 117,000 weekly downloads.
In a statement shared with BleepingComputer, Red Hat said it removed the affected packages after becoming aware of the incident and that the compromise was limited to internal development tooling.
"Red Hat is aware of security reports regarding certain npm packages within our development tooling ecosystem. We immediately initiated an investigation and removed the packages from the npm registry," Red Hat told BleepingComputer.
"The packages are strictly limited to internal development, and the malicious code was never published for customer consumption via the console.redhat.com system. While our investigation is ongoing, we have not identified any impact to customer or partner environments or Red Hat production systems."
The company says it is continuing to investigate the incident, but did not answer our questions about how the account was compromised.
Red Hat packages backdoored through GitHub compromise 
According to Aikido, the attackers allegedly compromised a Red Hat employee's GitHub account and used it to push malicious commits directly to multiple repositories.
Those commits added a GitHub Actions workflow and a script that abused npm's publishing mechanism to release backdoored packages.
"When the workflow runs, it installs Bun and executes  _index.js , passing it a list of target packages via the OIDC_PACKAGES environment variable," explains Aikido.
"The script uses the id-token: write permission to request a short-lived OIDC token from GitHub, then uses that token to authenticate directly with npm's trusted publishing endpoint and publish backdoored versions of every package in the list."
These compromised packages contained a malicious 'preinstall script that automatically executed a heavily obfuscated malicious index.js file when developers installed the packages.
"scripts": {
"preinstall": "node index.js"
} 
According to Aikido, the 'index.js' payload was approximately 4.2 MB in size, and is used to steal GitHub Actions secrets, AWS credentials, Google Cloud credentials, Azure service principal credentials, HashiCorp Vault tokens, Kubernetes service account tokens, npm and PyPI publishing tokens, SSH keys, Docker credentials, GPG keys, and `.env` files.
Aikido says 32 packages and 96 package versions were affected by the compromise, including numerous client libraries maintained under the `@redhat-cloud-services` namespace.
Organizations that installed any affected versions are advised to rotate all credentials, secrets, and tokens utilized by code on the infected device immediately.
Miasma appears to be a new Shai-Hulud variant 
Over the past couple of months, there have been numerous supply chain attacks utilizing a Shai-Hulud malware to steal credentials and spread to other projects.
These attacks have impacted well-known projects, including Bitwarden , SAP ,  Mistral , TanStack , OpenAI , and GitHub .
In May, the TeamPCP threat group publicly released the source code for its Mini Shai-Hulud malware framework, making the malware available to other threat actors.
Researchers say the malware used in the Red Hat compromise shares many similarities with Mini Shai-Hulud, but now utilizes the "Miasma: The Spreading Blight" string as comments in compromised GitHub repositories .
Miasma-compromised repositories on GitHub 
While the malware resembles TeamPCP's Mini Shai-Hulud, it is unclear whether the campaign was conducted by that threat actor or by another threat actor that modified the leaked malware source code.
OX Security says the malware retains the same credential-stealing functionality as Mini Shai-Hulud but adds additional obfuscation layers, multi-stage payload delivery mechanisms, and enhanced data theft and credential-harvesting features.
At the time of this writing, 309 GitHub repositories have been compromised by the Miasma malware campaign.
Test every layer before attackers do 
Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.
The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.
Get the whitepaper 
Related Articles: 
Bitwarden CLI npm package compromised to steal developer credentials 
New Shai-Hulud malware wave compromises 600 npm packages 
Shai Hulud attack ships signed malicious TanStack, Mistral npm packages 
TeamPCP hackers advertise Mistral AI code repos for sale 
OpenAI confirms security breach in TanStack supply chain attack
