# Kubernetes Platform Governance and CI/CD

This page tracks Kubernetes governance, policy-as-code, GitOps, CI/CD, image promotion, and cluster release controls across AKS/EKS-style environments.

## 2026-08-17 compile additions: AKS/EKS governance and microservice delivery

### Source-backed claims
- Microsoft Learn frames Kubernetes governance around targets, scopes, and policy directives across cloud environment, cluster deployment infrastructure, clusters, and applications; automation is required because manual policy checks are inefficient and inconsistent. Source: `raw/2026-08-17-web-governance-options-for-a-kubernetes-cluster-eks-to-aks.md`; page: [[cloud-sovereignty-and-platform-governance]]. confidence: 1 Microsoft Learn architecture source, last-confirmed 2026-08-17.
- Kubernetes policy enforcement can use built-in admission controllers, ValidatingAdmissionPolicy, admission webhooks, OPA/Gatekeeper, Kyverno, Kubewarden, and GitOps tooling; Gatekeeper adds OPA-backed admission/audit, Kyverno adds Kubernetes-native validate/mutate/generate/cleanup and image verification, and Kubewarden runs Wasm policies in multiple languages. Source: `raw/2026-08-17-web-governance-options-for-a-kubernetes-cluster-eks-to-aks.md`. confidence: 1 source, last-confirmed 2026-08-17.
- The AKS/EKS comparison says EKS governance commonly combines policy-as-code admission controllers, AWS validation/configuration controls, customer-managed IAM least privilege, and AWS Config conformance packs; AKS can combine Kyverno/Gatekeeper with Azure Policy for Kubernetes, Azure Policy initiatives, AKS Deployment Safeguards, and Azure Kubernetes Fleet Manager. Source: `raw/2026-08-17-web-governance-options-for-a-kubernetes-cluster-eks-to-aks.md`. confidence: 1 source, last-confirmed 2026-08-17.
- Microsoft Learn's microservices CI/CD article recommends independent per-service build/deploy pipelines, trunk-based development with release branches per microservice, PR-stage full checks, production-like deployment after passing CI, quality gates at each stage, and side-by-side deployment of service versions where needed. Source: `raw/2026-08-17-web-microservices-ci-cd-pipeline-on-kubernetes-with-azure-devops-and-helm.md`; page: [[github-actions-platform-operations]]. confidence: 1 Microsoft Learn architecture source, last-confirmed 2026-08-17.
- The CI/CD source recommends secretless authentication where possible, including workload identity federation for Azure Pipelines or GitHub Actions and Microsoft Entra Workload ID for deployed workloads; long-lived pipeline variables, Kubernetes secrets, client secrets, and certificates should be avoided where managed identity or federated credentials fit. Source: `raw/2026-08-17-web-microservices-ci-cd-pipeline-on-kubernetes-with-azure-devops-and-helm.md`; page: [[ai-coding-agent-security]]. confidence: 1 source, last-confirmed 2026-08-17.
- The CI/CD source contrasts push deployments with GitOps pull deployments: push offers direct deterministic pipeline control, while GitOps reduces direct cluster access and adds consistency, auditability, self-healing, and drift detection. Source: `raw/2026-08-17-web-microservices-ci-cd-pipeline-on-kubernetes-with-azure-devops-and-helm.md`. confidence: 1 source, last-confirmed 2026-08-17.
- The source recommends production cluster isolation from dev/test clusters, namespace-level logical isolation in non-production clusters, network policies, resource quotas, Entra/RBAC, non-root containers, restricted Pod Security admission for production workloads, minimal/distroless images, SBOM generation, vulnerability scanning, image signing by immutable digest, and Ratify/Azure Policy admission validation. Source: `raw/2026-08-17-web-microservices-ci-cd-pipeline-on-kubernetes-with-azure-devops-and-helm.md`; page: [[container-supply-chain-and-compliance]]. confidence: 1 source, last-confirmed 2026-08-17.

### Typed entities
- platform: Kubernetes
- managed service: Azure Kubernetes Service / AKS
- managed service: Amazon Elastic Kubernetes Service / EKS
- policy engine: Open Policy Agent / OPA
- policy engine: Gatekeeper
- policy engine: Kyverno
- policy engine: Kubewarden
- policy language: Rego
- policy language/runtime: WebAssembly / Wasm
- tool: gator CLI
- governance control: Azure Policy for Kubernetes add-on
- governance control: Azure Policy initiative
- governance control: AWS Config conformance pack
- governance control: AKS Deployment Safeguards
- service: Azure Kubernetes Fleet Manager
- deployment practice: GitOps
- tool: Flux
- tool: Argo CD
- package manager: Helm
- config tool: Kustomize
- identity: Microsoft Entra Workload ID
- control: workload identity federation
- control: Ratify image-signature admission
- artifact: SBOM

### Explicit relationships
- Kubernetes governance depends-on targets, scopes, and policy directives being enforced by cluster and cloud controls.
- Gatekeeper uses OPA/Rego for Kubernetes admission validation and audit, while Kyverno uses Kubernetes resources to validate, mutate, generate, clean up, and verify resources.
- Azure Policy for AKS extends Gatekeeper and reports cluster compliance back into Azure Policy; Kyverno and Kubewarden remain separate policy-engine options.
- GitOps complements Kubernetes governance by making Git the desired-state source and reconciling cluster state through an in-cluster operator.
- Push deployment depends-on pipeline-to-cluster access; GitOps supersedes that direct access when pull-based reconciliation, drift detection, and reduced attack surface are more important.
- Secretless CI/CD uses workload identity federation and managed workload identity to reduce long-lived credential exposure.
- Container promotion depends-on immutable version tags, registry namespace isolation, scanning, SBOMs, signing, and admission validation.

### HoneyDrunk implications
- If HoneyDrunk runs AKS/EKS workloads, choose one primary policy engine per cluster family and define exception workflows before teams build ad hoc webhook stacks.
- For microservice delivery, scope CI triggers, images, Helm charts, release branches, and approvals per service so one team's release does not widen another team's blast radius.
- Prefer GitOps for clusters where direct pipeline access is too broad; prefer push only when deterministic deployment control and pipeline audit are stronger requirements.
- Require OIDC/workload identity for build and runtime cloud access before exposing Kubernetes deployment paths to agents or scheduled automation.

### Quality notes
- Microsoft Learn sources are architecture guidance and include access-warning scaffolding in the raw captures. Promoted claims came from article body content only. Validate current AKS/EKS feature availability, policy syntax, and pricing before implementation.
