---
source: "https://projectzero.google/2026/09/windows-dangling-com.html"
title: "Windows Exploitation Techniques: Dangling COM Object Registrations"
author: "James Forshaw"
date_published: "2026-09-21"
date_clipped: "2026-09-22"
category: "Security & Ethical Hacking"
source_type: "rss"
capture_format: "attributed-summary"
discovered_via: "https://tldr.tech/infosec/2026-09-22"
---

# Windows Exploitation Techniques: Dangling COM Object Registrations

Source: [Windows Exploitation Techniques: Dangling COM Object Registrations](https://projectzero.google/2026/09/windows-dangling-com.html)

Attributed summary of the fetched written article; not a full reproduction. Source claims have not been independently reproduced.

James Forshaw analyzes a Windows privilege-escalation issue involving a machine-wide COM registration whose referenced DLL was absent from a location writable by ordinary users. Repairing one way of reaching the object had left the underlying registration problem available to another activation path.

The post explains how custom COM marshaling can cause an object-selected component to load inside a privileged process before the target method executes. The demonstrated path depended on finding a privileged server that did not enable the relevant custom-marshaling restrictions.

Defensive implications include removing stale registrations, checking write access along registered module paths, and reviewing marshaling policy in privileged COM services. Missing files alone do not prove exploitability; path resolution, writable placement, and reachable privileged activation must be established together.

The author identifies the issue as CVE-2026-66804 and describes it as recently fixed. HoneyDrunk relevance: use the case to review Windows installer cleanup and service trust boundaries. This capture does not establish whether any studio machine is affected or patched.
