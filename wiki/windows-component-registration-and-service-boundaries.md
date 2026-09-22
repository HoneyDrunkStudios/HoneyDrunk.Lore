# Windows Component Registration and Service Boundaries

## Decision-useful summary

The captured disclosure below links component registration, module-path permissions, and privileged activation. Use it to scope installer/service review; it does not determine a machine's vulnerability or patch status.


## 2026-09-22: Stale COM registrations need path and activation analysis

### Typed entities

person: James Forshaw; project: Windows; concept: COM registration; concept: module path permissions; concept: custom marshaling; concept: privileged activation.

### Claims and evidence

- Forshaw describes a missing registered DLL at a user-writable location and a reachable privileged custom-marshaling path. Repairing one activation route had left the underlying registration issue available through another; object-selected code could load before the target method executed. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-22-rss-windows-dangling-com-registration-defense.md)
- The report recommends stale-registration cleanup, registered-path permission checks, and marshaling-policy review. It identifies CVE-2026-66804 as recently fixed; a missing DLL alone does not prove exploitability, and the capture does not establish any studio machine's patch state. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-22-rss-windows-dangling-com-registration-defense.md)

### Explicit relationships

Privileged component loading depends-on registration, path resolution, write access, and activation reachability. A partial activation fix can leave the registration boundary exposed. See [[ai-coding-agent-security]].

### Decision and quality notes

Researcher disclosure summarized defensively without payloads. Review installer cleanup and service trust boundaries; verify applicable remediation and host inventory before making exposure claims. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent support. Open question: Do Windows installer cleanup and privileged COM services leave missing registered modules on writable paths, and what activation-policy and patch evidence establishes actual exposure or remediation? See [[indexes/gaps]].
