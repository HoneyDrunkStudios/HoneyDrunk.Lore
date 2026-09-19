---
source: "https://detect.fyi/threat-hunting-with-ja4-ja4s-practical-kql-queries-ef673fc5fcc0"
title: "Threat Hunting with JA4/JA4S (+ Practical KQL Queries)"
author: "Sergio Albea"
date_published: "2026-09-14"
date_clipped: "2026-09-18"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# Threat Hunting with JA4/JA4S (+ Practical KQL Queries)

Capture format: attributed summary of fetched public written content; not a full-text reproduction.

Sergio Albea demonstrates defensive TLS-fingerprint analysis using KQL. JA4 describes client handshake characteristics, while JA4S provides server-side context. Splitting structured components supports investigation beyond exact fingerprint matches.

Examples analyze GatewayJA4 in EntraIdSignInEvents and extract ja4/ja4s from AdditionalFields in DeviceNetworkEvents where telemetry contains them. Queries decode transport, TLS version, SNI, cipher/extension counts, and ALPN, then group activity by users, addresses, and geography.

The author enriches fingerprints with FoxIO's public mapping dataset but reports low match coverage in the tested environment. Unmatched fingerprints remain useful for baselining and clustering; mapping absence is not evidence of compromise.

Rare fingerprints, missing SNI, unusual ALPN, or differing cipher counts require contextual investigation rather than automatic malicious classification. Compare related applications and expected clients before escalating.

Lore relevance: reusable hunting logic for Entra and endpoint telemetry. Field availability and the author's observed mapping coverage are environment-specific, and these queries were not run against HoneyDrunk telemetry.

Source: [Original article](https://detect.fyi/threat-hunting-with-ja4-ja4s-practical-kql-queries-ef673fc5fcc0).
