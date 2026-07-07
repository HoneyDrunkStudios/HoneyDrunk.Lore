# Cloud Sovereignty and Platform Governance

Cloud sovereignty captures jurisdictional, operational, supply-chain, portability, and resilience controls for cloud-native systems. This page tracks platform patterns that make sovereignty enforceable rather than only documented.

## 2026-07-07 compile additions: sovereign cloud-native platform pattern

### Source-backed claims
- CNCF's data-sovereignty source distinguishes geographic region controls from jurisdictional sovereignty: a hyperscaler region can keep data in-country while corporate control and parent-company law may still affect access obligations. Source: `raw/2026-07-07-web-how-data-sovereignty-is-changing-cloud-native-infrastructure-design.md`; page: [[edge-ai-and-ai-infrastructure-2026]]. confidence: 1 CNCF blog/practice source, last-confirmed 2026-07-07.
- The source says European and Canadian public-sector procurement and regulatory expectations are expanding from data residency into operational control, supply-chain transparency, portability, resilience, and concentration-risk concerns. Source: `raw/2026-07-07-web-how-data-sovereignty-is-changing-cloud-native-infrastructure-design.md`. confidence: 1 source, last-confirmed 2026-07-07.
- The source presents a production pattern built from Kubernetes as policy/orchestration layer, OpenStack as operator-controlled infrastructure, GitOps as auditable desired-state management, and policy engines such as OPA/Gatekeeper or Kyverno as continuous enforcement. Source: `raw/2026-07-07-web-how-data-sovereignty-is-changing-cloud-native-infrastructure-design.md`. confidence: 1 source, last-confirmed 2026-07-07.
- The source says software supply-chain evidence such as SBOMs, image signing, admission policies, hardware bills of materials, and firmware verification are becoming part of higher-sovereignty platform discussions. Source: `raw/2026-07-07-web-how-data-sovereignty-is-changing-cloud-native-infrastructure-design.md`. confidence: 1 source, last-confirmed 2026-07-07.

### Typed entities
- concept: cloud sovereignty
- concept: data residency
- law/framework: U.S. CLOUD Act
- proposed framework: EU Cloud and AI Development Act / CADA
- regulation: EU Data Act
- regulation: EU AI Act
- regulation: NIS2
- regulation: DORA
- platform: Kubernetes
- platform: OpenStack
- practice: GitOps
- policy engine: OPA/Gatekeeper
- policy engine: Kyverno
- evidence artifact: SBOM
- evidence artifact: Hardware Bill of Materials / HBOM

### Explicit relationships
- Data residency is a geographic control; sovereignty depends-on jurisdictional control and operational authority.
- Kubernetes policy-as-code complements sovereign infrastructure by enforcing placement, namespace, RBAC, and admission decisions before workloads run.
- OpenStack complements Kubernetes where operator-controlled compute, identity, networking, storage, and bare-metal provisioning are sovereignty requirements.
- GitOps enables auditable per-jurisdiction operations because each cluster can reconcile desired state locally from reviewed commits.
- SBOM, image signing, HBOM, and firmware verification complement runtime policy when supply-chain transparency is part of the sovereignty requirement.

### HoneyDrunk implications
- For regulated deployments, ask what legal entity can be compelled to disclose data or operate infrastructure, not only where the servers are.
- If HoneyDrunk offers AI or cloud features to sovereignty-sensitive customers, preserve evidence for placement policy, operator access, supply-chain inputs, portability, and local recovery.
- Treat sovereignty as a platform requirement when customer contracts, public-sector procurement, or training-data governance depend on it.

### Quality notes
- CNCF blog is practice guidance with legal/regulatory interpretation. Use it as architecture framing and verify obligations with current primary legal sources before commitments.
