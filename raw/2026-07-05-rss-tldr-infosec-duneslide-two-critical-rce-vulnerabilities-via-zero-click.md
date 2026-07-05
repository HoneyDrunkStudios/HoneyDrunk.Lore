---
source: "https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities"
title: "DuneSlide: Two Critical RCE vulnerabilities via Zero-Click Prompt Injection in Cursor IDE (6 minute read)"
author: "TLDR InfoSec"
date_published: "2026-07-03"
date_clipped: "2026-07-05"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-07-03"
source_role: "primary-via-tldr"
---

# DuneSlide: Two Critical RCE vulnerabilities via Zero-Click Prompt Injection in Cursor IDE (6 minute read)

Source: https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities

Cato AI Labs uncovered two 9.8 CVSS remote code execution flaws in Cursor IDE, tracked as CVE-2026-50548 and CVE-2026-50549, that let zero-click prompt injection delivered through an untrusted MCP server or poisoned web result escape the terminal sandbox and achieve full system compromise. The flaws stemmed from two independent architectural gaps, working directory parameter manipulation and a symlink canonicalization fallback, that let an LLM agent be steered into overwriting the cursorsandbox binary, showing how prompt injection reached beyond the LLM layer into classical vulnerability classes not previously treated as part of the coding agent attack surface. Cursor initially rejected the report on the grounds that its threat model excluded MCP server misuse, then reopened it on escalation and shipped fixes in the Cursor 3.0 client, with Cato framing the case as evidence that autonomous command execution in coding agents needs systemic rather than one-off protection.
