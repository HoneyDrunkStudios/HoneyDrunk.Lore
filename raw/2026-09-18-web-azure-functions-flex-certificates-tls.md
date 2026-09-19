---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/ssltls-certificates-and-end-to-end-encryption-for-azure-functions-flex-consumpti/4556425"
title: "SSL/TLS certificates and end-to-end encryption for Azure Functions Flex Consumption"
author: "nzthiago"
date_published: "2026-09-14"
date_clipped: "2026-09-18"
category: "Azure & Cloud"
source_type: "web"
---

# SSL/TLS certificates and end-to-end encryption for Azure Functions Flex Consumption

Capture format: attributed summary of fetched public written content; not a full-text reproduction.

Microsoft announces site-scoped certificates and end-to-end TLS for Functions Flex Consumption. Custom-domain HTTPS, platform-front-end-to-worker encryption, outbound certificate use, and inbound client authentication protect separate boundaries.

Each app supports three private and three public certificates. Imports can use Key Vault and managed identity; renewed versions synchronize within 24 hours. Certificate access from code is granted individually instead of using WEBSITE_LOAD_CERTIFICATES. Linux runtime files replace Windows certificate-store assumptions, and thumbprint changes must be considered during rotation.

For inbound mTLS, Azure forwards the certificate through X-ARR-ClientCert; application code still validates trust, validity, usage, revocation policy, and authorization. Header presence alone is insufficient. Renegotiation-based configurations have TLS 1.3, HTTP/2, and large-request constraints.

The article includes Bicep settings for site-scoped certificates and internal-hop encryption. Dedicated Azure CLI certificate-management commands were unavailable at publication.

Lore relevance: deployment and migration guidance for securing serverless APIs without confusing transport encryption with caller authorization.

Source: [Original article](https://techcommunity.microsoft.com/blog/appsonazureblog/ssltls-certificates-and-end-to-end-encryption-for-azure-functions-flex-consumpti/4556425).
