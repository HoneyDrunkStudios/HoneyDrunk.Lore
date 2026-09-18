# Container Supply Chain and Compliance

## Purpose

This page tracks container-image supply-chain evidence, SBOM quality, provenance, and regulatory compliance obligations that affect build and release workflows.

## 2026-06-28 compile additions: CRA and SBOM generation

### Source-backed claims
- Docker's CRA overview says the EU Cyber Resilience Act applies a horizontal cybersecurity baseline to products with digital elements sold in the EU, with vulnerability and severe-incident reporting obligations starting on 2026-09-11 and full enforcement on 2027-12-11. Source: `raw/2026-06-28-rss-docker-blog-eu-cyber-resilience-act-cra-overview.md`. confidence: 1 vendor/legal overview source, last-confirmed 2026-06-28.
- The same Docker source says commercial container images and runtimes distributed into the EU can qualify as products with digital elements, making SBOMs, vulnerability handling, support periods, secure defaults, provenance, and integrity controls operational requirements rather than optional hygiene. Source: `raw/2026-06-28-rss-docker-blog-eu-cyber-resilience-act-cra-overview.md`. confidence: 1 source, last-confirmed 2026-06-28.
- Docker's SBOM workflow source argues that build-time SBOM generation is usually more complete than post-build scanning because the generator sees resolved dependency graphs, package-manager state, and build context before artifacts are flattened. Source: `raw/2026-06-28-rss-docker-blog-sbom-generation-for-container-workflows.md`. confidence: 1 vendor source, last-confirmed 2026-06-28.
- The SBOM source defines useful SBOM output by completeness, accuracy, freshness, verifiability, and format compliance; loose or stale SBOM files are weaker than attestations bound to a specific image digest. Source: `raw/2026-06-28-rss-docker-blog-sbom-generation-for-container-workflows.md`. confidence: 1 source, last-confirmed 2026-06-28.
- The SBOM generator itself is build attack surface because it can read source, dependency trees, and artifacts; generation tools should be pinned to immutable references, checksum-verified, monitored for advisories, and run in reproducible CI. Source: `raw/2026-06-28-rss-docker-blog-sbom-generation-for-container-workflows.md`. confidence: 1 source, last-confirmed 2026-06-28.

### Typed entities
- regulation: EU Cyber Resilience Act / CRA
- artifact: Software Bill of Materials / SBOM
- format: SPDX
- format: CycloneDX
- attestation: in-toto attestation
- standard/control: SLSA provenance
- artifact/control: OpenVEX
- product: Docker Hardened Images
- product: Docker Scout
- concept: build-time SBOM generation
- concept: post-build scanning
- date: 2026-09-11 CRA reporting obligations
- date: 2027-12-11 CRA full enforcement

### Explicit relationships
- CRA compliance depends-on vulnerability reporting, secure-by-design defaults, SBOM documentation, support periods, and conformity evidence.
- Build-time SBOM generation complements hardened base images by preserving resolved dependency and provenance evidence for application layers.
- Digest-bound attestations supersede detached SBOM files when consumers need to verify which artifact the SBOM describes.
- SBOM tooling depends-on the same supply-chain controls as other CI dependencies because compromised generators can falsify or leak build data.
- [[ai-coding-agent-security]] depends-on container supply-chain controls when agents create, modify, or publish deployable images.

### HoneyDrunk implications
- Inventory whether HoneyDrunk ships any container images, runtimes, or software products into the EU before 2026-09-11 so vulnerability-reporting clocks and support-period commitments are not discovered during an incident.
- Add build-time SBOM attestation and digest binding to the container pipeline backlog before treating SBOMs as compliance evidence.
- For high-impact images, prefer hardened, attestable base layers and verify OpenVEX/scanner behavior locally instead of assuming reduced CVE noise is correct.
- Pin SBOM generators and container-build actions to immutable references in release-capable workflows.

### Quality notes
- Docker is vendor-authored and promotes Docker products, but the compliance dates and SBOM-quality criteria are decision-useful for build-system planning.
- Legal applicability still needs counsel or compliance review before HoneyDrunk treats CRA obligations as confirmed for a specific product.
- Privacy filter: no secrets, customer data, internal hostnames, or exploit details were copied.

## 2026-07-05 compile additions: Argo CD source integrity and internal mTLS

### Source-backed claims
- InfoQ reports that Argo CD 3.5 release-candidate work adds repo-server internal mTLS, Git commit signature/source integrity validation before sync, and native ApplicationSet UI list/filter/detail/preview support. Source: `raw/2026-07-05-rss-tldr-devops-argo-cd-3-5-tightens-supply-chain-security-with-internal-m.md`. confidence: 1 trade/news source, last-confirmed 2026-07-05.
- The source says Argo CD Source Integrity can require valid Git signatures through Application spec or CLI configuration, closing a gap where tampered or unsigned manifests could otherwise be deployed if a repository was compromised. Source: `raw/2026-07-05-rss-tldr-devops-argo-cd-3-5-tightens-supply-chain-security-with-internal-m.md`. confidence: 1 source, last-confirmed 2026-07-05.
- The same source says impersonation and Source Hydrator moved to beta, improving audit trails for server operations and supporting dry-source/rendered-manifest separation in multi-repository GitOps patterns. Source: `raw/2026-07-05-rss-tldr-devops-argo-cd-3-5-tightens-supply-chain-security-with-internal-m.md`. confidence: 1 source, last-confirmed 2026-07-05.

### Typed entities
- product: Argo CD
- feature: repo-server mTLS
- feature: Source Integrity
- feature: ApplicationSet UI
- feature: impersonation
- feature: Source Hydrator
- concept: Git commit signature verification
- concept: GitOps supply chain

### Explicit relationships
- GitOps deployment security depends-on both transport security between controller components and source integrity for manifests.
- Source Integrity complements SBOM/provenance controls by verifying the Git source that drives cluster state before sync.
- Source Hydrator supports separation between unhydrated source templates and rendered manifests with different repository access controls.

### HoneyDrunk implications
- If HoneyDrunk adopts Argo CD, require source-signature policy, internal component trust model, ApplicationSet preview/review flow, and impersonation audit mapping before production use.
- For any GitOps-style agent deployment, keep dry source, rendered output, signer identity, and sync authority distinct in run receipts.

### Quality notes
- InfoQ is secondary trade reporting. Verify exact Argo CD version, API fields, and release status against primary Argo CD docs before implementation.

## 2026-08-26 compile additions: Docker Verified Publisher as agent-era provenance signal

### Source-backed claims
- Docker says Docker Verified Publisher applications are now self-serve through Docker Hub, while Docker still manually reviews each accepted publisher identity. Source: `raw/2026-08-26-rss-tldr-devops-docker-verified-publisher-apps-are-now-self-serve-3-minute.md`. confidence: 1 Docker vendor source, last-confirmed 2026-08-26.
- The Docker source frames publisher verification as a trust signal for machine-speed software selection across images, MCP servers, models, sandboxes, agents, and other Docker Hub content, but warns that consumers still need artifact review, digest pinning, provenance/signature checks, and CVE review. Source: `raw/2026-08-26-rss-tldr-devops-docker-verified-publisher-apps-are-now-self-serve-3-minute.md`; page: [[ai-coding-agent-security]]. confidence: 1 source, last-confirmed 2026-08-26.
- Docker Verified Publisher analytics can expose which repositories and versions get adoption and which company domains pull them, making trusted distribution both a supply-chain and commercial-discovery surface. Source: `raw/2026-08-26-rss-tldr-devops-docker-verified-publisher-apps-are-now-self-serve-3-minute.md`. confidence: 1 vendor source, last-confirmed 2026-08-26.

### Typed entities
- program: Docker Verified Publisher / DVP
- registry: Docker Hub
- content type: container image
- content type: MCP server
- content type: model
- content type: sandbox
- content type: agent
- control: digest pinning
- control: provenance/signature verification
- artifact: publisher analytics report

### Explicit relationships
- Publisher verification complements artifact-level provenance, signatures, digest pinning, and vulnerability review; it does not supersede them.
- Agent-era software selection depends-on publisher identity because agents can choose dependencies, containers, MCP servers, and models faster than humans can manually inspect every option.
- Docker Hub distribution overlaps-with go-to-market analytics when pull domains and version trends are exposed to verified publishers.

### HoneyDrunk implications
- For container or MCP consumption, prefer verified publishers only as one input; still pin digests, inspect artifacts, review licenses, and scan vulnerabilities.
- If HoneyDrunk publishes Docker Hub content, evaluate DVP for trust/discoverability, but account for analytics privacy and commercial exposure before relying on pull-domain reports.

### Quality notes
- Docker is vendor-authored and commercial. The durable Lore claim is that publisher identity is a useful but incomplete supply-chain control.

## 2026-09-04 compile additions: registry worm controls and provenance limits

### Source-backed claims
- The Shai-Hulud pipeline-security source argues that package registries and infrastructure registries share a dangerous execution assumption: resolving and installing a package means running publisher-provided code with the privileges of the requesting developer machine or CI runner. Source: `raw/2026-09-04-rss-tldr-infosec-shai-hulud-whoever-controls-your-package-registry-control.md`; page: [[ai-coding-agent-security]]. confidence: 1 sponsored/security-practice source, last-confirmed 2026-09-04.
- The source says a later registry-worm variant used a legitimate signed release pipeline, creating valid provenance attestations for poisoned versions and demonstrating that attestation proves origin/build path but not whether the release should have happened. Source: `raw/2026-09-04-rss-tldr-infosec-shai-hulud-whoever-controls-your-package-registry-control.md`. confidence: 1 source, last-confirmed 2026-09-04.
- Recommended defensive posture includes pinning provider/module/package dependencies to immutable references, routing resolution through curated private registries, replacing standing CI/developer secrets with short-lived deployment credentials, and constraining runner egress to required registries/state backends/cloud APIs. Source: `raw/2026-09-04-rss-tldr-infosec-shai-hulud-whoever-controls-your-package-registry-control.md`. confidence: 1 source, last-confirmed 2026-09-04.

### Typed entities
- incident family: Shai-Hulud
- variant: ChainDrop
- registry: npm registry
- registry class: Terraform provider/module registry
- control: immutable reference pinning
- control: private allowlisted registry
- control: short-lived deployment credential
- control: runner egress allowlist
- standard/control: SLSA provenance

### Explicit relationships
- SLSA provenance complements source integrity but does not supersede release authorization review when an attacker controls legitimate publishing credentials.
- Registry consumption depends-on publisher trust, dependency immutability, credential scope, and runner egress together.
- CI runners and developer laptops overlap-with production security boundaries when they hold publish, registry, or cloud credentials.

### HoneyDrunk implications
- For release-capable workflows, require immutable pins for Terraform modules/providers, GitHub Actions, container bases, MCP packages, and npm dependencies where possible.
- Treat public registries as untrusted input unless HoneyDrunk controls an allowlisted mirror or review gate for the dependency class.
- Remove long-lived publishing/cloud credentials from CI runners before assuming package signatures or attestations are enough.

### Quality notes
- The source is sponsored and includes historical/incident narrative. Lore retained defensive controls and provenance-limit lessons, not malware mechanics.

## 2026-09-18: Build history can retain credentials beyond filesystem cleanup

### Typed entities

project: Baseten; project: GitHub; concept: container build history; concept: credential revocation; concept: least-privilege build identity.

### Claims and evidence

- Strix reports a broadly privileged GitHub token in the build history of an anonymously downloadable container image. The authors say the token originated in a 2023 build and retained repository administration and push access in July 2026; deleting a secret-bearing file would not remove its separate metadata copy. confidence: 1 source, last-confirmed 2026-09-18 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-16-rss-strix-container-history-secret-exposure.md)
- The report says Baseten restricted registry access and rotated the credential after disclosure. Its defensive guidance covers old tags, anonymous access, layers and configuration/history, secret mounts that do not persist consumed credentials, and narrow expiring build identities. confidence: 1 source, last-confirmed 2026-09-18 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-16-rss-strix-container-history-secret-exposure.md)

### Explicit relationships

Credential exposure can be caused by build-command expansion into image history. Recovery depends-on revocation as well as artifact cleanup; rebuilding an image cannot revoke previously copied credentials. See [[ai-coding-agent-security]].

### Decision and quality notes

Researcher-reported incident and remediation, not an independent assessment of current Baseten exposure. No credential material, exploit payload, or unnecessary infrastructure identifiers are included. Source-specific claims remain provisional single-source evidence; related sources and derived summaries are not independent confirmation of these details. Open question: Which old images, public registry paths, layers, and build-history records need secret scanning, and can exposed build identities be promptly revoked with narrow replacement permissions? See [[indexes/gaps]].
