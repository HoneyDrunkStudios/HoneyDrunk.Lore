# Cloud Vector Storage Security

## Decision-useful summary
Cloud vector storage should be treated as untrusted data storage for RAG systems, not as an instruction authority. The August 2026 S3 Vectors analysis did not find intrinsic server-side input-validation flaws in S3 Vectors itself, but it showed that permissive write access, cross-account bucket policies, predictable chunk keys, mutable metadata, weak retrieval trust boundaries, and incomplete telemetry can make RAG systems vulnerable to poisoning and hard to reconstruct after an incident. [source: raw/2026-08-12-rss-tldr-infosec-a-security-analysis-of-amazon-s3-vectors-and-its-use-in-l.md]

## 2026-08-12 compile additions: S3 Vectors and RAG poisoning controls

### Source-backed claims
- OFFENSAI/TUCN's S3 Vectors analysis says the service did not show intrinsic server-side input-validation vulnerabilities in their tests; the risks they demonstrated came from how applications authorize writes, trust metadata, and consume retrieved context. Source: `raw/2026-08-12-rss-tldr-infosec-a-security-analysis-of-amazon-s3-vectors-and-its-use-in-l.md`. confidence: 1 security research source, last-confirmed 2026-08-12.
- The analysis says permission to set a vector bucket policy can grant cross-account data-plane access to a vector bucket, while owner-only control-plane boundaries remain separate. Source: `raw/2026-08-12-rss-tldr-infosec-a-security-analysis-of-amazon-s3-vectors-and-its-use-in-l.md`. confidence: 1 source, last-confirmed 2026-08-12.
- The source says principals with vector-write access can poison RAG behavior by changing metadata, source labels, citations, chunk text, vector coordinates, ranking behavior, or predictable chunk keys. Source: `raw/2026-08-12-rss-tldr-infosec-a-security-analysis-of-amazon-s3-vectors-and-its-use-in-l.md`. confidence: 1 source, last-confirmed 2026-08-12.
- The analysis ties poisoned retrieval context to misinformation, prompt injection, tool hijacking, frontend exfiltration through rendered content, and developer code-suggestion poisoning; an RCE example in the source involved a third-party sandbox rather than S3 Vectors itself. Source: `raw/2026-08-12-rss-tldr-infosec-a-security-analysis-of-amazon-s3-vectors-and-its-use-in-l.md`; page: [[ai-coding-agent-security]]. confidence: 1 source, last-confirmed 2026-08-12.
- CloudTrail data events are off by default for this surface in the captured analysis, and even enabled events may omit vector keys, embeddings, metadata, deleted keys, query vectors, and filter expressions; reconstruction may require index scanning or re-ingestion. Source: `raw/2026-08-12-rss-tldr-infosec-a-security-analysis-of-amazon-s3-vectors-and-its-use-in-l.md`. confidence: 1 source, last-confirmed 2026-08-12.

### Typed entities
- service: Amazon S3 Vectors
- concept: vector bucket
- permission: `s3vectors:PutVectorBucketPolicy`
- operation: vector write
- system pattern: retrieval-augmented generation / RAG
- threat class: RAG poisoning
- threat class: prompt injection
- threat class: tool hijacking
- telemetry source: CloudTrail data events
- control: isolated ingester role
- control: nonpredictable chunk key
- control: retrieved-content trust boundary

### Explicit relationships
- Vector bucket policies can create cross-account data-plane access that depends-on exact resource ARNs and identity policy.
- RAG poisoning is caused by treating writable vector metadata or retrieved chunks as trusted instructions or verified source facts.
- Nonpredictable chunk keys and isolated ingester roles complement least privilege by reducing overwrite and unauthorized-write paths.
- CloudTrail data events complement access logs, but do not supersede application-level write receipts, source provenance, and index consistency checks.
- Retrieved content should be data-to-evaluate; it should not supersede system/developer instructions or execute tool calls without confirmation.

### HoneyDrunk implications
- If Lore/Knowledge ever uses managed vector storage, keep raw/wiki citations authoritative and treat vector retrieval as a candidate evidence path, not final truth.
- Separate vector ingestion roles from query/runtime roles; keep humans, shared CI identities, and broad automation out of write paths unless explicitly justified.
- Use UUID/HMAC-like nonpredictable chunk keys, write quotas, unauthorized-write alerts, sweeper checks for unverified/orphaned data, and re-ingestion plans.
- Require manual confirmation or strong policy gates before retrieved content can influence mutating tools, code changes, or frontend-rendered output.
- Enable telemetry deliberately, but do not assume default cloud logs can reconstruct poisoned index state.

### Confidence and quality notes
- Quality posture: decision-useful for threat modeling RAG storage and vector-index governance. Privacy filter: no exploit payloads, suspicious domains, phone numbers, exact malicious text, or reusable operational snippets were copied from the source.
