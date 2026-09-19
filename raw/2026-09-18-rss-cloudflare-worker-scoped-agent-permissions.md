---
source: "https://blog.cloudflare.com/workers-granular-authorization/"
title: "Give every teammate and agent the right level of access to your Workers"
author: "Dina Kozlov; Anthony Oreglia; Visal In"
date_published: "2026-09-15"
date_clipped: "2026-09-18"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# Give every teammate and agent the right level of access to your Workers

Capture format: attributed summary of fetched public written content; not a full-text reproduction.

Cloudflare introduces Worker-level permissions for users and API tokens. Four roles separate access to operational metadata, read-only product content, content/settings changes, and full administration. Editor can deploy changes but cannot create or delete resources; Admin includes destructive and access-management operations.

Resource scoping confines a CI token or agent to one Worker. Route and custom-domain changes additionally require Workers Routes permission for the zone. Existing deployments can continue without that zone permission if they do not alter the connection.

Durable Objects inherit permissions from their implementing Worker rather than receiving independent roles. Data Studio access requires Editor because it can modify stored data.

The article describes contextual authorization errors and availability through dashboard, API, and Terraform. Existing legacy assignments continue; granular access for other products is described as future work.

Lore relevance: a concrete least-privilege design for separating investigation, code review, deployment, and resource deletion in agent tooling.

Source: [Original article](https://blog.cloudflare.com/workers-granular-authorization/).
