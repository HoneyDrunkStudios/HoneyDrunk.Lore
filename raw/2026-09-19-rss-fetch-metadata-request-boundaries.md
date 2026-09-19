---
source: "https://andrewlock.net/understanding-the-fetch-metadata-http-headers-sec-fetch-site-and-friends"
title: "Understanding the Fetch Metadata HTTP headers: Sec-Fetch-Site and friends"
author: "Andrew Lock"
date_published: "2026-07-29"
date_clipped: "2026-09-19"
category: "Security & Ethical Hacking"
source_type: "rss"
capture_format: "attributed-summary"
---

# Understanding the Fetch Metadata HTTP headers: Sec-Fetch-Site and friends

Source: [Understanding the Fetch Metadata HTTP headers: Sec-Fetch-Site and friends](https://andrewlock.net/understanding-the-fetch-metadata-http-headers-sec-fetch-site-and-friends)

*Attributed summary of the fetched written article; not a verbatim reproduction.*

Andrew Lock explains the browser-provided Fetch Metadata headers and how servers can use request context when designing cross-origin protections.

Sec-Fetch-Site describes the relationship between initiating and destination sites. Same-site is broader than same-origin, so subdomains and ports require deliberate treatment. Sec-Fetch-Dest identifies the intended resource use, such as a document or image. Sec-Fetch-Mode describes navigation, CORS, and related modes. Sec-Fetch-User signals user activation when present.

The article separates sending cross-origin requests from JavaScript access to their responses. A no-CORS request can still reach a server even when its response is opaque to script; CORS alone should not be mistaken for complete CSRF protection.

HoneyDrunk implication: use this as background for reviewing browser-facing API request policies and the newer ASP.NET Core CSRF work. Evaluate legitimate navigation, embedded resources, and cross-site integrations before adopting rejection rules. This source explains the headers; it is not a complete production middleware configuration.
