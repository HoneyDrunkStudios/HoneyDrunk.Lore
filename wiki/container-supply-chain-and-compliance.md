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
