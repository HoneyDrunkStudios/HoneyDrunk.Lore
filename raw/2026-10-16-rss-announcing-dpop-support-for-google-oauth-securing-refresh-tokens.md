---
source: "https://developers.googleblog.com/announcing-dpop-support-for-google-oauth-securing-refresh-tokens"
title: "Announcing DPoP Support for Google OAuth: Securing Refresh Tokens"
author: "Sergei Akulich; Brian Daugherty"
date_published: "2026-10-15"
date_clipped: "2026-10-16"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# Announcing DPoP Support for Google OAuth: Securing Refresh Tokens

![banner-usability-safety-updates-google-auth-pla.original](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/banner-usability-safety-updates-google-auth-pla.original_kKZ094I.png)

Traditional OAuth bearer tokens operate on a "finders-keepers" model, making them vulnerable to Infostealer malware (e.g. RedLine, NodeStealer) and Adversary-in-the-Middle (AiTM) attacks.

DPoP (Demonstrating Proof-of-Possession) is an application-layer OAuth 2.0 security profile ([RFC 9449](https://datatracker.ietf.org/doc/html/rfc9449)) that neutralizes token theft and replay attacks by cryptographically binding tokens to a client-generated asymmetric keypair at the application layer, ensuring that even if a token is stolen, it cannot be replayed without the corresponding private key.

This article is meant to inform you on where and how to [adopt DPoP](https://developers.google.com/identity/protocols/oauth2/resources/dpop-adoption) and describes Google's specific DPoP implementation. A DPoP adoption [SKILL.md](https://github.com/google/skills/blob/main/skills/identity/dpop-adoption/SKILL.md) is also available to help implement DPoP.

Some optional features and implementation decisions in RFC 9449 are delegated to Google as an authorization provider. [Google Identity](https://developers.google.com/identity), and its [OAuth Platform](https://developers.google.com/identity/protocols/oauth2), function as a developer-facing service where engineers implement OAuth 2.0 and cryptographic security controls like DPoP to protect API integrations. Separately, Google Workspace [Context-Aware Access](https://cloud.google.com/access-context-manager/docs/caa-agent-security) (CAA) leverages DPoP to secure enterprise AI workloads on the Gemini Enterprise Agent Platform by cryptographically validating agent identities at the Agent Gateway.

Google's OAuth Platform supports DPoP binding specifically for refresh tokens. This design choice reflects a pragmatic engineering tradeoff: by sender-constraining the long-lived refresh token, we neutralize the primary vector for persistent offline impersonation. Meanwhile, short-lived access tokens remain standard Bearer tokens, ensuring that high-QPS resource APIs do not incur the per-request asymmetric cryptographic verification overhead of DPoP. This approach delivers robust protection for your most sensitive credentials while maintaining the high performance and low latency of Google API integrations.

Unlike standard Bearer token flows, DPoP requires client-side cryptographic key generation, strict timestamp and nonce handling, specific claim computation (htm, htu, iat, jti), exact header construction, and DPoP proof JWT construction. These changes may introduce additional system constraints to support secure computation, handling, and storage.

### **Architectural considerations**

The IETF’s Best Current Practice for OAuth 2.0 Security ([RFC 9700](https://datatracker.ietf.org/doc/html/rfc9700)) discusses sender-constrained refresh tokens. Additionally, the [OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps#name-application-architecture-pa) IETF draft discusses three models: Backend-for-Frontend (BFF), Token-Mediating Backend, and Browser-based OAuth Client.

Following this guidance, Google recommends using DPoP to sender-contrain refresh tokens in these models.

Unlike transport-layer token binding (e.g., mTLS/RFC 8705) which often breaks or terminates at modern cloud proxies and load balancers, DPoP operates at the HTTP header level. This makes it highly resilient for complex, multi-hop environments, including emerging **Model Context Protocol (MCP)** and autonomous agent architectures.

### **Architectural Deep-Dive: The Performance-vs-Security Tradeoff**

A common question from security architects is: If DPoP is designed to sender-constrain tokens, why are Google's access tokens still standard Bearer tokens?

The answer lies in operational scaling and performance at Google's scale. Verifying asymmetric cryptographic signatures (such as ES256) requires significant CPU cycles. If every API call to high-throughput Google resource servers (like Gmail, Calendar, or Drive APIs) required verifying a DPoP proof, the compute overhead at the API Gateway layer would be massive, introducing measurable latency and scaling costs.

By constraining DPoP binding strictly to the refresh token, Google's architecture achieves a balance:

**Long-Lived Credentials Protected:** The highly sensitive, long-lived refresh token (which can be used to obtain new access tokens indefinitely) is cryptographically bound to the client's key pair. If exfiltrated, it is useless to an attacker.

**High-Performance Serving:** Short-lived access tokens (typically valid for 1 hour or less) remain standard Bearer tokens. This ensures that the vast majority of API requests incur zero cryptographic verification overhead, maintaining the high performance and low latency developers expect from Google APIs.

### **Complementary Protections: DPoP and DBSC**

DPoP is a powerful tool for securing OAuth 2.0 tokens, but it is important to understand its boundaries.

DPoP does not protect standard web application session cookies, which remain a primary target for Infostealer malware. To address cookie theft, Google and the Web Incubator Community Group (WICG) are actively developing **Device Bound Session Credentials (DBSC)**. While DPoP operates at the application layer to secure API tokens for public and confidential clients, DBSC operates at the browser and network layer to cryptographically bind browser session cookies to the device's hardware (such as TPM). Together, DPoP and DBSC form a comprehensive defense-in-depth strategy against credential theft across both API and web-based user sessions.

### **Multi-Agent Delegation & Model Context Protocol (MCP)**

As autonomous AI agents and **Model Context Protocol (MCP)** architectures emerge, securing tool-use tokens becomes critical. While DPoP is highly resilient in single-hop client-to-server connections, multi-agent workflows (where Agent A delegates a task to Agent B, which calls Resource C) introduce delegation challenges.

In a multi-agent chain, Agent B cannot sign a DPoP proof on behalf of Agent A without access to Agent A's private key—and sharing private keys violates the core security principles of DPoP. Because Google's core consumer OAuth endpoint (oauth2.googleapis.com) does not support [OAuth 2.0 Token Exchange (RFC 8693)](https://datatracker.ietf.org/doc/html/rfc8693), developers building multi-agent or federated cloud workloads should consider [Google Cloud Secure Token Service (STS)](https://cloud.google.com/iam/docs/reference/sts/rest). By routing delegation through STS, the intermediate agent can exchange the upstream token for a new, short-lived federated token cryptographically bound to its own local key pair, preserving the sender-constrained security model across the entire agent chain without key exposure.

See our [DPoP Adoption Guide](https://developers.google.com/identity/protocols/oauth2/resources/dpop-adoption), our DPoP adoption [SKILL.md](https://github.com/google/skills/blob/main/skills/identity/dpop-adoption/SKILL.md), and improve your platform security today.
