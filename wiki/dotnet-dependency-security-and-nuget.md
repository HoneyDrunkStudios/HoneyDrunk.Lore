# .NET Dependency Security and NuGet

## Decision-useful summary
.NET 10 makes NuGet dependency/audit output more actionable by enabling transitive auditing (`NuGetAuditMode=all`) and package pruning by default for `net10.0+` projects. Package pruning removes redundant platform-provided packages from the restore graph when the target framework's runtime libraries already supply them, reducing false-positive vulnerability reports and restore noise. For HoneyDrunk, this is directly relevant to SDK/service upgrades and agent-generated dependency changes: audit fewer phantom transitive CVEs, but still validate multi-targeting and direct references before deleting packages. [source: raw/2026-05-19-rss-net-blog-nuget-package-pruning-cleaner-dependencies-and-actionable-vul.md]

## Claims
- In .NET 10, `NuGetAuditMode` defaults to `all`, so NuGet audits transitive dependencies by default; package pruning is enabled by default for projects targeting .NET 10 or later. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-net-blog-nuget-package-pruning-cleaner-dependencies-and-actionable-vul.md]
- Package pruning removes transitive packages from the restore graph when the .NET Runtime Libraries already provide the package/version range for the target framework; pruned packages are not downloaded, do not appear in restore outputs, and are not reported as transitive audit dependencies. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-net-blog-nuget-package-pruning-cleaner-dependencies-and-actionable-vul.md]
- Direct `PackageReference` items in the pruning range are not silently deleted; NuGet applies `PrivateAssets='all'` and `IncludeAssets='none'`, and raises `NU1510` when a direct reference can be removed for every target framework. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-net-blog-nuget-package-pruning-cleaner-dependencies-and-actionable-vul.md]
- Microsoft reports telemetry where .NET 10 defaults produce 70% fewer transitive vulnerability reports, measurably higher restore success, and up to 50% per-project restore-time reduction where pruning applies; these are vendor telemetry claims and should be verified locally. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-net-blog-nuget-package-pruning-cleaner-dependencies-and-actionable-vul.md]
- If any target framework in a multi-targeted project is `net10.0` or later, package pruning applies to all target frameworks in that project, so multi-targeted libraries need extra restore/audit review. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-net-blog-nuget-package-pruning-cleaner-dependencies-and-actionable-vul.md]

## Typed entities
- ecosystem: .NET
- tool: NuGet
- feature: NuGet Package Pruning
- property: `RestoreEnablePackagePruning`
- property: `NuGetAuditMode`
- warning: `NU1510`
- target framework: `net10.0`
- concept: transitive dependency audit
- concept: false-positive vulnerability report
- package: `System.Text.Json`
- package: `System.Text.Encodings.Web`
- package: `System.Formats.Asn1`
- file: raw/2026-05-19-rss-net-blog-nuget-package-pruning-cleaner-dependencies-and-actionable-vul.md

## Explicit relationships
- NuGet Package Pruning uses .NET Runtime Libraries package lists to decide which dependencies are platform-provided.
- `NuGetAuditMode=all` depends-on pruning to keep expanded transitive audit output actionable instead of noisy.
- `NU1510` identifies direct package references that can be removed, but deletion depends-on target-framework review.
- Multi-targeted projects can be affected across all TFMs when any TFM is `net10.0+`.
- [[microsoft-dotnet-ai-stack]] and [[dotnet-runtime-and-mobile-2026]] depend-on cleaner NuGet restore/audit behavior when adopting .NET 10/11-era platform packages.

## HoneyDrunk implications
- For .NET 10+ projects, treat a newly quieter NuGet audit as “less graph noise,” not proof that dependency risk disappeared; inspect remaining transitive warnings as higher-signal.
- Add a dependency-cleanup pass after net10 upgrades: remove direct packages flagged by `NU1510` only after confirming every TFM/runtime path is covered.
- Watch agent-generated package edits: agents may add redundant platform packages that pruning later hides; keep dependency policy explicit in repo docs/analyzers.

## Confidence and quality notes
- Quality posture: decision-usable for upgrade planning and dependency-audit policy. Vendor telemetry claims need local measurement.
- Privacy filter: no private project/package inventory copied.

## 2026-05-26 cross-ecosystem note

- npm 11.15.0 staged publishing and install-source allowlist flags are not NuGet features, but they reinforce the same dependency-security posture: package publication should use short-lived trusted identity plus human approval for release, and package installation should restrict nonregistry sources by default where possible. confidence: 1 GitHub changelog source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-infosec-staged-publishing-and-new-install-time-controls-for-npm-2.md; page: [[ai-coding-agent-security]]]

Typed entities added: ecosystem: npm; control: staged publishing; control: install source allowlist.

Relationship added: npm staged publishing complements OIDC trusted publishing; install-source allowlists complement package cooldown/proxy and NuGet audit/pruning by reducing dependency-source ambiguity.

## 2026-08-12 cross-reference note

- Microsoft August 2026 servicing updates include security fixes for .NET 10.0.11, 9.0.19, and 8.0.30 across information disclosure, security feature bypass, denial of service, elevation of privilege, and remote code execution classes. confidence: 1 Microsoft servicing source, last-confirmed 2026-08-12. [source: raw/2026-08-12-web-dotnet-framework-august-2026-servicing-updates.md; page: [[dotnet-runtime-and-mobile-2026]]]

Typed entities added: runtime: .NET 10.0.11; runtime: .NET 9.0.19; runtime: .NET 8.0.30; concept: runtime servicing inventory.

Relationship added: runtime servicing complements NuGet audit because project security posture depends on both package graph and installed/shared runtime patch level.

## 2026-08-13 compile additions: NuGet API key lifetime reduction

### Source-backed claims
- Microsoft says new NuGet.org API keys will be limited to a 30-day maximum duration starting 2026-08-17, and new 365-day API keys will no longer be available. Source: `raw/2026-08-13-web-strengthening-nuget-supply-chain-security-reducing-api-key-lifetime-ne.md`. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-08-13.
- Microsoft says NuGet.org API keys created before 2026-08-17 will expire on 2026-11-01, so existing package-publishing automation needs inventory and rotation or migration before that date. Source: `raw/2026-08-13-web-strengthening-nuget-supply-chain-security-reducing-api-key-lifetime-ne.md`. confidence: 1 source, last-confirmed 2026-08-13.
- The source recommends NuGet Trusted Publishing, where CI authenticates to NuGet.org with OIDC and NuGet issues short-lived publishing credentials for the operation rather than relying on long-lived repository secrets. Source: `raw/2026-08-13-web-strengthening-nuget-supply-chain-security-reducing-api-key-lifetime-ne.md`; page: [[ai-coding-agent-security]]. confidence: 1 source, last-confirmed 2026-08-13.

### Typed entities
- ecosystem: NuGet.org
- credential: NuGet API key
- control: NuGet Trusted Publishing
- protocol: OpenID Connect / OIDC
- date: 2026-08-17 new API key lifetime change
- date: 2026-11-01 pre-change key expiration

### Explicit relationships
- NuGet Trusted Publishing supersedes long-lived NuGet API keys for supported CI publishing workflows.
- Shorter API key lifetime reduces disclosure blast radius but depends-on automation that can rotate keys safely when OIDC is not available.
- Package publishing credentials complement package-graph auditing because compromised publishing can create malicious versions even when dependencies are otherwise clean.

### HoneyDrunk implications
- Inventory any HoneyDrunk NuGet publishing workflows before 2026-08-17 and migrate GitHub Actions/GitLab workflows to Trusted Publishing where possible.
- If an API key remains necessary, scope it narrowly, rotate within 30 days, keep it out of logs, and confirm expiration alerts reach an actively monitored account.

### Quality notes
- Microsoft source is authoritative for NuGet.org policy direction. Verify current Trusted Publishing provider support before changing release pipelines.
