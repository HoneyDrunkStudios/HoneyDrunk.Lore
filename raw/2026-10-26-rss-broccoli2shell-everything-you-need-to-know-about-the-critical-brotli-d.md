---
source: "https://www.wiz.io/blog/cve-2026-111497-brotli-rce-node-js"
title: "Broccoli2shell: Everything You Need To Know About The Critical Brotli Decoder Vulnerability"
author: "Merav Bar"
date_published: "2026-10-25"
category: "Security & Ethical Hacking"
source_type: "rss"
date_clipped: "2026-10-26"
discovered_via: "https://tldr.tech/devops/2026-10-26"
---

# Broccoli2shell: Everything You Need To Know About The Critical Brotli Decoder Vulnerability

A critical vulnerability, tracked as CVE-2026-111497 and referred to as Broccoli2Shell, has been identified in the Brotli decompression library. The vulnerability affects multiple widely used technologies, including Node.js, Bun, Envoy Proxy, and more. Successful exploitation could allow an unauthenticated remote attacker to trigger memory corruption, disclose sensitive information, crash affected processes, or potentially achieve remote code execution (RCE).

Organizations using affected components to decompress untrusted Brotli-compressed data are advised to prioritize remediation.

CVE-2026-111497 was discovered and reported by Khai Tran and Sylvie Mayer (OpenAI Codex Security), with fixes implemented by Matteo Collina and Antoine du Hamel (Node.js). Ron Masas (Imperva Red Team) demonstrated its exploitability, while OpenSourceMalware and Aikido analyzed its impact on the Python ecosystem.

# What is CVE-2026-111497?

Broccoli2Shell (a.k.a Node2Shell and HTTP2Shell) originates from an out-of-bounds write vulnerability in the Brotli decoder, a widely adopted compression component used to reduce the size of HTTP traffic and other data. The flaw occurs when the decoder improperly handles specially crafted compressed data during block-processing operations, potentially writing beyond allocated memory boundaries. An attacker can exploit this behavior by supplying malicious Brotli-compressed input to a vulnerable application, potentially resulting in memory disclosure, application crashes, or arbitrary code execution with the privileges of the affected process. Researchers have demonstrated successful exploitation against unpatched Node.js environments.

Although initially associated with Node.js, the vulnerability originates in the upstream Brotli C decoder and extends to multiple downstream technologies that incorporate the affected component. Exploitation requires an application or dependency to decompress attacker-controlled Brotli data, either through incoming HTTP requests, externally fetched responses, or other untrusted compressed content. Certain HTTP clients and application frameworks may perform decompression automatically when Brotli support is enabled, potentially exposing applications even when Brotli is not explicitly referenced in application code.

# Wiz Research data: what’s the risk to cloud environments?

Cloud environments are particularly exposed due to the widespread use of Brotli-enabled components across containerized applications, Kubernetes clusters, API gateways, reverse proxies, serverless workloads, and cloud-hosted web services. Internet-facing applications that process attacker-controlled requests, as well as internal services that retrieve compressed responses from untrusted external sources, may provide exploitation paths. Successful exploitation could enable attackers to compromise application workloads, access sensitive information, disrupt service availability, or execute malicious code within affected containers or runtime environments.

According to Wiz data 91% of cloud environments have resources vulnerable to CVE-2026-111497, and 82% of cloud environments have publicly exposed Node.js instances.

# Which products are affected?

Additional products that bundle or link against vulnerable versions of the Brotli C decoder may also be affected. Organizations should consult vendor-specific security advisories, particularly for statically linked libraries and embedded dependencies. End-of-life runtime branches should be migrated to supported versions.

| Product | Affected Versions | Patched Versions |
| --- | --- | --- |
| Google Brotli / libbrotli | 1.0.3–1.2.0, excluding patched backports | 1.0.10, 1.1.1, 1.2.1 |
| Python Brotli | 1.0.3–1.2.0 | 1.2.1 |
| Python brotlicffi | 1.0.3–1.2.0.x | 1.2.1.0 |
| Node.js | Unpatched 22.x, 24.x, 26.x releases | 22.23.4, 24.22.1, 26.12.1 |
| Bun | 1.0.21–1.4.3 | 1.4.4 |
| Envoy Proxy | 1.36.11, 1.37.7, 1.38.5, 1.39.2 | 1.36.12, 1.37.8, 1.38.6, 1.39.3, 1.40.0 |
| Istio | 1.29.0–1.29.8, 1.30.0–1.30.5, 1.31.0–1.31.1 | 1.29.9, 1.30.6, 1.31.2 |
| andybalholm/brotli (Go) | Versions before v1.2.7 | v1.2.7 |

# Which actions should security teams take?

Organizations should prioritize the following mitigation and remediation measures:

1. Apply security updates: Upgrade affected Brotli libraries, Node.js runtimes, Python packages, Bun, Envoy Proxy, and Istio deployments to their respective patched versions or later supported releases.
2. Identify vulnerable cloud workloads: Inventory virtual machines, Kubernetes clusters, containers, serverless functions, API gateways, and application dependencies for vulnerable Brotli components. Prioritize internet-facing services and workloads processing untrusted compressed data.
3. Review application exposure: Identify applications that decompress Brotli-compressed HTTP requests, external HTTP responses, uploaded files, or other attacker-controlled content. Include indirect and transitive dependencies in the assessment.
4. Rebuild and redeploy affected workloads: Update container base images, dependency lockfiles, and bundled libraries. Rebuild and redeploy affected container images, restart running processes, and verify that patched components are loaded.
5. Implement temporary mitigations: Where immediate patching is not possible, consider disabling Brotli decompression or rejecting Brotli-encoded requests before they reach vulnerable components. Restrict untrusted compressed responses where feasible. These controls may reduce exposure but do not replace patching.
6. Strengthen monitoring and detection: Review WAF, application, and network logs for suspicious Brotli-compressed traffic, unexpected application crashes, and anomalous process behavior. Monitor affected workloads for indicators of exploitation.

Wiz customers can use the pre-built query and advisory in the [Wiz Threat Center](https://app.wiz.io/boards/threat-center/wiz-adv-2026-191) to search for vulnerable instances in their environment.

![](https://www.datocms-assets.com/75231/1792939224-screenshot-2026-10-25-at-16-40-09.png?fm=webp)

# References

- [Node.js advisory](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)
- [Vercel advisory](https://vercel.com/kb/bulletin/node-js-security-advisory)
- [Imperva writeup](https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/)
- [Patch the Planet advisory](https://patchtheplanet.org/brotli)
- [Broccoli2Shell website](https://broccoli2shell.com/)
- [Istio advisory](https://istio.io/latest/news/security/istio-security-2026-007/)
- [Envoy Proxy advisory](https://github.com/envoyproxy/envoy/security/advisories/GHSA-3wvj-j6qm-62mr)
- [Brotli advisory](https://github.com/advisories/GHSA-9v8h-qqgm-4m35)
- [oss-security post](https://www.openwall.com/lists/oss-security/2026/10/23/25)
- [Bun advisory](https://github.com/oven-sh/bun/security/advisories/GHSA-663w-cv8g-jj2p)
- [Aikido blogpost](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497)
- [OpenSourceMalware blogpost](https://opensourcemalware.com/blog/brotlipocalypse)
