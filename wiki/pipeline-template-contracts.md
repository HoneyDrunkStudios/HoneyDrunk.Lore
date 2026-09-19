# Pipeline Template Contracts

## Decision-useful scope

Research on separating consumer intent, template expansion, and runtime deployment values. The source-backed case below is Azure DevOps-specific; it does not establish equivalent behavior in other CI systems.


## 2026-09-19: Compile-time manifests and runtime values have different roles

### Typed entities

project: Azure DevOps Pipelines; concept: manifest facade; concept: template expansion; concept: versioned schema; concept: leaf deployment template.

### Claims and evidence

- The case study puts a thin builder in each consumer repository and a shared orchestrator in the platform repository. The builder constructs an object manifest during template expansion; the orchestrator expands it into stages/jobs while leaf templates implement deployment. Configuration read after checkout cannot reshape an already expanded pipeline. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-azure-pipeline-manifest-facade.md)
- The author proposes a versioned JSON Schema, unsupported-version rejection, and validation before deployment. Secrets and execution-discovered values remain runtime concerns. Release-tag pinning and pipeline preview make shared-template versions and expanded YAML reviewable. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-azure-pipeline-manifest-facade.md)

### Explicit relationships

Pipeline structure depends-on template-time inputs; orchestration uses a versioned manifest and leaf templates. See [[github-actions-platform-operations]] for separate GitHub-specific runtime evidence.

### Decision and quality notes

Single Azure DevOps architecture case, not a GitHub Actions implementation or a tested HoneyDrunk pipeline. Additional per-repository builders and template-expression limits remain tradeoffs. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which pipeline inputs must be known during template expansion, and which schema-version, preview, runtime-secret, and leaf-template tests qualify a manifest facade for HoneyDrunk? See [[indexes/gaps]].
