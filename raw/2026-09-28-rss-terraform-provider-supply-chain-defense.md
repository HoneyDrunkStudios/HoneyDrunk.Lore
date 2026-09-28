---
source: "https://www.aikido.dev/blog/graphalgo-terraform-go-modules"
title: "Graphalgo campaign spreads to Terraform providers and Go Modules"
author: "Oliver Smith"
date_published: "2026-09-22"
date_clipped: "2026-09-28"
category: "Security & Ethical Hacking"
source_type: "rss"
capture_format: "attributed-summary"
discovered_via: "https://tldr.tech/infosec/2026-09-25"
---

# Source capture

Aikido reports a malware campaign extending into Terraform providers and Go modules. Look-alike package identities and fabricated ecosystem sites supported social engineering. Some payloads activated only for specific runtime inputs, making ordinary smoke tests insufficient evidence of safety.

The report also describes manipulated commit dates that made a package appear older in downstream tooling. Apparent age and a plausible package name therefore did not establish trustworthy provenance.

HoneyDrunk application: verify provider namespaces and repository ownership, review dependency changes, and isolate infrastructure execution from broad credentials. These are defensive implications of the reported case.

For affected systems, the researchers recommend host isolation, credential rotation, investigation of activity performed with those credentials, and rebuilding the environment. Removing the dependency alone may leave a separately launched payload active.

This capture preserves defensive lessons without reproducing payload code, secrets, or personal identifiers. Campaign scope and attribution remain the researchers' findings.

Source: [Original article](https://www.aikido.dev/blog/graphalgo-terraform-go-modules).

Capture note: Original attributed summary after fetching readable written content; not a full-text reproduction.
