# Post-Quantum Security and Cryptography

## Purpose

Track post-quantum cryptography adoption signals that affect HoneyDrunk infrastructure, developer machines, SSH/TLS/VPN choices, and agent-runner security posture.

## 2026-06-22 compile additions: SSH, TLS, and VPN readiness

### Source-backed claims
- Brandon Rozek's post frames post-quantum adoption around harvest-now/decrypt-later risk: encrypted traffic captured today may be decrypted later if classical key exchange remains vulnerable to future quantum computers. Source: `raw/2026-06-22-rss-brandonrozek-com-on-post-quantum-security-adoption.md`. confidence: 1 practitioner source, last-confirmed 2026-06-22.
- The source identifies hybrid SSH key exchange `mlkem768x25519-sha256` in OpenSSH as an adoption path, and notes that newer OpenSSH clients warn when a server does not offer post-quantum key exchange. Source: `raw/2026-06-22-rss-brandonrozek-com-on-post-quantum-security-adoption.md`. confidence: 1 practitioner source, last-confirmed 2026-06-22.
- The source identifies hybrid TLS key exchange `X25519MLKEM768` and says Firefox/Chrome support has existed since 2024; current browser/server support and Cloudflare traffic percentages should be rechecked before operational decisions. Source: `raw/2026-06-22-rss-brandonrozek-com-on-post-quantum-security-adoption.md`. confidence: 1 practitioner source, last-confirmed 2026-06-22.
- WireGuard is not post-quantum by default in this source. A static `PresharedKey` can add a post-quantum-ish layer if generated out of band, while Rosenpass is presented as a way to rotate WireGuard pre-shared keys more frequently. Source: `raw/2026-06-22-rss-brandonrozek-com-on-post-quantum-security-adoption.md`. confidence: 1 practitioner source, last-confirmed 2026-06-22.

### Typed entities
- concept: post-quantum cryptography / PQC
- threat: harvest-now/decrypt-later
- protocol/tool: OpenSSH
- key exchange: `mlkem768x25519-sha256`
- protocol: TLS
- key exchange: `X25519MLKEM768`
- protocol/tool: WireGuard
- field: `PresharedKey`
- tool: Rosenpass

### Explicit relationships
- Harvest-now/decrypt-later risk depends-on the confidentiality lifetime of captured traffic.
- Hybrid SSH and TLS key exchange combine classical and post-quantum components to reduce migration risk while preserving compatibility.
- WireGuard pre-shared keys complement classical WireGuard handshakes but static keys do not provide the same forward-secrecy posture as regularly rotated keys.
- PQC adoption does not supersede ordinary certificate, key-management, patching, and endpoint controls.

### HoneyDrunk implications
- Inventory SSH servers/clients, TLS endpoints, and WireGuard/VPN usage before treating PQC as done or irrelevant.
- Prioritize systems where captured traffic has long confidentiality lifetime: private repos, credentials, legal/business documents, and source snapshots.
- Verify current OpenSSH, browser, server, CDN, and VPN support before changing defaults; PQC support is moving quickly.

### Quality notes
- Practitioner source. Decision-useful as a readiness checklist, but operational dates, browser/CDN percentages, and software behavior should be refreshed from primary docs before implementation.

## 2026-07-04 compile additions: threat-model framing for pure and hybrid PQ

### Source-backed claims
- Soatok's threat-model guide argues that hybrid post-quantum plus classical key exchange is mainly a hedge against post-quantum algorithm breaks before a cryptography-relevant quantum computer exists; once Q-Day occurs, classical ECDH no longer contributes meaningful long-term confidentiality against harvest-now/decrypt-later attacks. Source: `raw/2026-07-04-web-soatok-s-informal-guide-to-threat-models-dhole-moments.md`. confidence: 1 practitioner cryptography source, last-confirmed 2026-07-04.
- The same source says objecting to non-hybrid ML-KEM RFC publication does not by itself improve security for users already configured to prefer hybrid KEMs, while it can block organizations that need stable IETF/FIPS/CNSA-aligned references for compliance. Source: `raw/2026-07-04-web-soatok-s-informal-guide-to-threat-models-dhole-moments.md`. confidence: 1 source, last-confirmed 2026-07-04.
- The source frames PQ+PQ hybrids, optionally with ECDH, as the more intellectually consistent diversity hedge for teams worried about future algorithm breaks in one PQ family. Source: `raw/2026-07-04-web-soatok-s-informal-guide-to-threat-models-dhole-moments.md`. confidence: 1 practitioner source, last-confirmed 2026-07-04.

### Typed entities
- algorithm: ML-KEM
- algorithm: HQC
- primitive: ECDH
- concept: Q-Day
- concept: hybrid PQ+ECDH
- concept: PQ+PQ hybrid
- standard context: IETF RFC
- standard context: CNSA 2.0
- standard context: FIPS 140-3

### Explicit relationships
- Hybrid PQ+ECDH mitigates migration and pre-Q-Day algorithm-break risk but does not supersede pure PQ once classical key exchange is quantum-broken.
- PQ+PQ hybrids complement ECDH hybrids when algorithm diversity after Q-Day is the threat model.
- Compliance publication needs can affect security adoption even when the technical security delta is small for already-hybrid deployments.

### HoneyDrunk implications
- When tracking PQ readiness, separate three threat models: migration compatibility, pre-Q-Day PQ algorithm failure, and harvest-now/decrypt-later after Q-Day.
- Do not treat "hybrid" as a single security property; record which primitives are combined and what failure each component is intended to hedge.

### Quality notes
- Practitioner source with strong opinions. Use as threat-model vocabulary, not as the sole basis for cryptographic standard selection.
