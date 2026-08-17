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

## 2026-08-17 compile additions: Kubernetes governance as enforceable platform control

### Source-backed claims
- Microsoft Learn's AKS/EKS governance comparison reinforces that Kubernetes governance should be automated across clusters and applications through policy-as-code, admission controls, GitOps, cloud governance scopes, and multicluster reporting rather than manual review. Source: `raw/2026-08-17-web-governance-options-for-a-kubernetes-cluster-eks-to-aks.md`; page: [[kubernetes-platform-governance-and-cicd]]. confidence: 1 Microsoft Learn architecture source, last-confirmed 2026-08-17.

### Typed entities
- page: [[kubernetes-platform-governance-and-cicd]]
- platform: Kubernetes
- policy engine: OPA/Gatekeeper
- policy engine: Kyverno
- policy engine: Kubewarden
- practice: GitOps
- control: Azure Policy initiative
- control: AWS Config conformance pack

### Explicit relationships
- Kubernetes governance complements cloud sovereignty by turning residency, access, supply-chain, and runtime rules into admission, audit, and reconciliation controls.
- Multicloud governance depends-on mapping provider scopes such as AWS Organizations/accounts and Azure management groups/subscriptions to Kubernetes cluster/namespace/application policy scopes.

### HoneyDrunk implications
- Treat Kubernetes policy-as-code as a sovereignty-adjacent control whenever customer commitments involve tenant isolation, region control, supply-chain proof, or operator-access limits.

### Quality notes
- Microsoft Learn is platform-authored guidance. Verify legal and customer-specific sovereignty requirements separately.
