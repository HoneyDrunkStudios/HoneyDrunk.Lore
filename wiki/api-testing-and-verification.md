# API Testing and Verification

## Decision-useful summary

API test planning should name the risk class being tested instead of asking generally for "more tests." The 2026-09-08 and 2026-09-11 System Design Newsletter captures are partial/paywalled, but together they provide a useful taxonomy for layered API verification: fast smoke and contract checks, behavior and integration suites, performance/reliability tests, and security/compliance tests. For HoneyDrunk, this strengthens the rule that agent-authored API work needs explicit verification level, not only generated code.

## Source-backed claims

- The September 8 API-testing source enumerates common API test layers including smoke, functional, unit, integration, end-to-end, regression, acceptance, negative, boundary, validation, exploratory, contract, consumer-driven contract, load, stress, performance, spike, soak, scalability, latency, concurrency, security, authentication, and authorization testing. confidence: 1 newsletter source with paywalled tail, last-confirmed 2026-09-08. [source: raw/2026-09-08-rss-system-design-newsletter-i-struggled-with-api-testing-until-i-learned-.md]
- The September 11 continuation adds advanced and resilience/security-oriented categories including fuzz testing, penetration testing, injection attack testing, encryption/TLS testing, policy/compliance testing, reliability testing, chaos testing, circuit-breaker testing, backpressure testing, fault-injection testing, failover/recovery testing, idempotency testing, timeout/retry testing, caching testing, data-integrity/consistency testing, state-transition testing, UI-level API testing, developer-experience testing, documentation testing, rate-limiting testing, backward-compatibility testing, mutation testing, mock/stub testing, synthetic monitoring, scenario/workflow testing, and component testing. confidence: 1 partial newsletter source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-system-design-newsletter-api-testing-was-hard-until-i-learned-these-53.md]
- The visible September 11 sections explain that fuzz testing is machine-generated malformed input testing, penetration testing is context-aware simulated attack work, injection testing verifies that user input cannot escape into executable server behavior, TLS testing checks HTTPS/cert/protocol/cipher posture, compliance testing maps regulatory or organizational requirements to executable checks, reliability testing measures sustained error/availability behavior, and chaos testing injects bounded failures to verify graceful degradation. confidence: 1 partial newsletter source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-system-design-newsletter-api-testing-was-hard-until-i-learned-these-53.md]

## Typed entities

- concept: API testing
- test type: fuzz testing
- test type: penetration testing
- test type: injection attack testing
- test type: encryption/TLS testing
- test type: policy/compliance testing
- test type: reliability testing
- test type: chaos testing
- test type: idempotency testing
- test type: backward compatibility testing
- test type: synthetic monitoring

## Explicit relationships

- API verification depends-on matching test type to risk class; one broad "test" request can hide missing security, reliability, compatibility, or workflow coverage.
- Fuzz, injection, and penetration tests complement ordinary functional tests by exploring malformed input, hostile behavior, and chained attack paths.
- Reliability, chaos, failover, retry, backpressure, and circuit-breaker tests complement load/performance tests by validating behavior under failure, not only capacity.
- Compliance, documentation, developer-experience, and backward-compatibility tests depend-on explicit contracts outside implementation code.

## HoneyDrunk implications

- When asking agents to add API coverage, specify the verification layer and target risk: contract, auth, injection, concurrency, idempotency, performance, workflow, or compatibility.
- Treat security-oriented API tests as potentially high signal but expensive/noisy; triage findings with evidence and avoid promoting payload recipes into public wiki prose.
- Use this taxonomy as a checklist for API planning, not as proof that every API needs all 53 categories at release.

## Confidence and quality notes

- Quality posture: useful taxonomy from newsletter/practitioner material, but the capture is partial and paywalled after early sections. Use as planning vocabulary, not exhaustive implementation guidance.
- Privacy filter: no exploit payloads or offensive testing recipes were promoted.


## 2026-09-22: SDK generator continuity requires compatibility tests

### Typed entities

project: Google; project: Speakeasy; concept: OpenAPI compiler; concept: SDK compatibility; concept: generator supply dependency; concept: license scope.

### Claims and evidence

- Google describes replacing a proprietary generator after its provider announced closure, while preserving client interfaces, streaming, errors, and language-specific types. The replacement keeps formal OpenAPI compilation deterministic, with AI helping custom development around the compiler. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-22-rss-openapi-sdk-generator-supply-dependency.md)
- The post describes opening the Speakeasy generator suite under AGPLv3 and distinguishes generator licensing from generated-output ownership. Reported lower staffing needs remain a vendor account; intended generator use and modifications require checking the actual license. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-22-rss-openapi-sdk-generator-supply-dependency.md)

### Explicit relationships

Reproducible SDKs depend-on generator availability and build inputs as well as an open API specification. Generator replacement uses compatibility tests for generated clients.

### Decision and quality notes

Vendor migration account, not legal interpretation or independently measured productivity. Treat generator continuity as a supply dependency and verify interface, streaming, error, and type contracts. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent support. Open question: Which generated SDK contracts and pinned build inputs protect HoneyDrunk from generator-provider loss, and what generator-use license terms require review before a replacement? See [[indexes/gaps]].
