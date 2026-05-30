# GitHub Actions Platform Operations

## Decision-useful summary
GitHub Actions has two May 2026 operational changes that matter for CI/CD reliability: concurrency groups can now queue multiple pending runs instead of replacing the single pending run, and hosted runner images are entering migration windows for Arm64 maintenance ownership, Windows 2025/Visual Studio 2026, and `macos-latest` moving to macOS 26. For HoneyDrunk, the concurrency queue is useful for ordered deploys against shared environments, while the runner-image migrations should be pinned/tested before default labels move. [sources: raw/2026-05-16-rss-github-changelog-actions-github-actions-concurrency-groups-now-allow-l.md; raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md]

## Claims
- GitHub Actions concurrency groups can now allow multiple jobs or workflow runs to wait in the same concurrency group, with up to 100 queued jobs or workflow runs per group. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-github-changelog-actions-github-actions-concurrency-groups-now-allow-l.md]
- Larger concurrency queues are enabled with `queue: max` in the workflow `concurrency` block when `cancel-in-progress` is false or unset, making ordered deployment workflows easier to preserve. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-github-changelog-actions-github-actions-concurrency-groups-now-allow-l.md]
- GitHub now owns and maintains Arm64 hosted runner images; `windows-11-arm` has transitioned, and Ubuntu Arm64 images are migrating to GitHub internal pipelines with no expected compatibility/package change. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md]
- The `windows-latest` and `windows-2025` hosted-runner labels migrate to Visual Studio 2026 between 2026-06-08 and 2026-06-15; workflows that must stay on Visual Studio 2022 should pin `windows-2022`. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md]
- The `macos-latest` label begins a 30-day migration on 2026-06-15 from macOS 15 to macOS 26; workflows requiring macOS 15 should pin `macos-15`. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md]

## Typed entities
- platform: GitHub Actions
- feature: concurrency groups
- feature: concurrency `queue: max`
- runner label: `windows-latest`
- runner label: `windows-2025`
- runner label: `windows-2025-vs2026`
- runner label: `windows-2022`
- runner label: `macos-latest`
- runner label: `macos-15`
- runner image: `ubuntu-24.04-arm`
- runner image: `ubuntu-22.04-arm`
- runner image: `windows-11-arm`
- date/decision: 2026-06-08 Windows 2025 Visual Studio 2026 migration begins
- date/decision: 2026-06-15 macos-latest migration begins
- file: raw/2026-05-16-rss-github-changelog-actions-github-actions-concurrency-groups-now-allow-l.md
- file: raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md

## Explicit relationships
- GitHub Actions concurrency groups use `queue: max` to supersede the previous one-pending-run replacement behavior for ordered workflows.
- Ordered deployment workflows depend-on serialized access to shared resources/environments.
- `windows-latest` and `windows-2025` labels will point to Visual Studio 2026 after the migration, superseding implicit Visual Studio 2022 assumptions.
- `macos-latest` will point to macOS 26 after migration, superseding implicit macOS 15 assumptions.
- [[github-copilot-and-app-token-changes]] depends-on GitHub Actions runner capacity/cost for agentic Copilot code review workloads.

## HoneyDrunk implications
- Use `queue: max` for deploy pipelines where canceling pending runs is wrong and sequential delivery matters.
- Pin runner labels for production release workflows before June 2026 migrations; use default labels only after smoke tests pass on the new images.
- Add a CI audit for workflows that assume macOS 15, Visual Studio 2022, or specific Arm64 image package versions.

## Confidence and quality notes
- Quality posture: decision-usable for CI/CD scheduling and runner-image migration planning.
- Weak spots: vendor changelog source; verify exact YAML syntax against GitHub docs before bulk migration.
- Privacy filter: no private repository or runner details copied.

## 2026-05-24 compile additions

### Claims
- GitHub's Issues navigation modernization used a local-first architecture with IndexedDB caching, preheating, in-memory layers, and service workers to reduce perceived latency and make repeated issue views feel instant. confidence: 1 GitHub engineering source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-devops-from-latency-to-instant-modernizing-github-issues-navigati.md]
- The GitHub source reports many React navigation paths loading under 200 ms after the modernization, while remaining hard navigation bottlenecks are tied to JavaScript boot and server rendering. confidence: 1 GitHub engineering source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-devops-from-latency-to-instant-modernizing-github-issues-navigati.md]

### Typed entities
- product: GitHub Issues
- browser storage: IndexedDB
- browser feature: service worker
- architecture pattern: local-first navigation
- concept: preheating
- concept: perceived latency
- framework: React

### Explicit relationships
- Local-first navigation uses IndexedDB, memory caches, preheating, and service workers to reduce repeated-view latency.
- JavaScript boot and server rendering remain bottlenecks even after client-side cache layers improve navigation.

### HoneyDrunk implications
- For issue/task-heavy internal tools, cache issue/task shells and recently visited data locally before optimizing server endpoints.
- Measure perceived navigation latency separately from backend latency; users feel route transitions, boot cost, and hydration, not only API timings.

## 2026-05-30 compile additions

### Claims
- GitHub Code Quality Repository Enablement API is in public preview on github.com, adding `PATCH /repos/{owner}/{repo}/code-quality/setup` to enable/disable default setup, configure languages, and choose runner type, plus `GET /repos/{owner}/{repo}/code-quality/setup` to retrieve state, languages, runner type, and analysis schedule. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-github-code-quality-repository-enablement-api.md]
- The repository enablement API supports `csharp`, `go`, `java-kotlin`, `javascript-typescript`, `python`, and `ruby`, and is not available on GitHub Enterprise Server during this preview. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-github-code-quality-repository-enablement-api.md]
- GitHub code coverage metrics on pull requests are in public preview for GitHub Code Quality users on github.com; teams upload Cobertura reports from CI using `upload-code-coverage`, and GitHub Apps/Actions need the new fine-grained `code-quality:write` permission. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-code-coverage-on-pull-requests-is-now-in-public-previ.md]
- GitHub Code Quality is available for GitHub Enterprise Cloud and Team and free during preview, but not yet available on GitHub Enterprise Server. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-code-coverage-on-pull-requests-is-now-in-public-previ.md]

### Typed entities
- product: GitHub Code Quality
- API: `PATCH /repos/{owner}/{repo}/code-quality/setup`
- API: `GET /repos/{owner}/{repo}/code-quality/setup`
- feature: pull request code coverage
- report format: Cobertura
- action: `upload-code-coverage`
- permission: `code-quality:write`
- languages: C#, Go, Java/Kotlin, JavaScript/TypeScript, Python, Ruby

### Explicit relationships
- GitHub Code Quality Repository Enablement API uses repository-level configuration to automate static analysis rollout.
- Pull request coverage depends-on CI-generated Cobertura reports and `code-quality:write` upload permission.
- Code Quality preview features complement existing CI checks but do not supersede local test and coverage gates until preview behavior is validated.

### HoneyDrunk implications
- Audit which HoneyDrunk repos could enable Code Quality centrally, especially C# and TypeScript repos.
- If coverage is adopted, upload least-privilege Cobertura reports from existing CI and avoid broad permissions where `code-quality:write` is enough.
