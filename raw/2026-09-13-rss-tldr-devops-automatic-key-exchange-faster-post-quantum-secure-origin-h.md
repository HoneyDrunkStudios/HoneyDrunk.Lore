---
source: "https://blog.cloudflare.com/automatic-key-exchange-for-origins"
title: "Automatic Key Exchange: faster, post-quantum secure origin handshakes for 45 billion daily connections (and counting)"
author: "Suleman Ahmad; Yawar Jamal; Alex Krivit"
date_published: "2026-09-08"
date_clipped: "2026-09-13"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-09-11"
capture_mode: "attributed-summary"
full_text_fetched: "true"
---

# Automatic Key Exchange: faster, post-quantum secure origin handshakes for 45 billion daily connections (and counting)

Original source: [Automatic Key Exchange: faster, post-quantum secure origin handshakes for 45 billion daily connections (and counting)](https://blog.cloudflare.com/automatic-key-exchange-for-origins)

## Source-content summary

Cloudflare describes measuring origin-server key-agreement support before selecting a TLS 1.3 client keyshare. A static first choice can trigger HelloRetryRequest and add a round trip; the new origin-specific selection prefers the X25519MLKEM768 hybrid where supported.

The company reports that, during rollout, retry requests decreased from roughly 52% to 3.7%, with more than 150 milliseconds removed from p90 handshake latency. These are Cloudflare deployment measurements, not universal estimates.

The article separates browser-to-edge and edge-to-origin connections and discusses compatibility constraints around larger keyshares, fallback, and future post-quantum authentication. HoneyDrunk relevance: assess origin TLS separately from edge TLS, use observed endpoint capabilities to guide migration, and monitor retry rates. Post-quantum key agreement alone does not establish post-quantum certificate authentication or eliminate every downgrade concern.

Capture note: This is an attributed summary of the fetched article, not a verbatim full-text archive. The original source retains the complete examples and discussion.
