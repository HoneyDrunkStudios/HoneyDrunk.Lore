# Cloud Security Monitoring and SIEM

Cloud security monitoring covers detection surfaces, SIEM integrity, and telemetry governance for cloud-native and Azure security operations.

## 2026-07-07 compile additions: Microsoft Sentinel self-monitoring

### Source-backed claims
- The Sentinel self-monitoring source says SIEM workspaces should monitor their own control plane because attackers may first disable detections, feeds, retention, or incident visibility before performing louder actions. Source: `raw/2026-07-07-web-the-blind-spot-in-the-watchtower-detections-for-when-someone-attacks-y.md`; page: [[ai-coding-agent-security]]. confidence: 1 practitioner security source, last-confirmed 2026-07-07.
- The source identifies AzureActivity, SentinelAudit, and SentinelHealth as key places to detect changes to Sentinel rules, workspace/table settings, connectors, data collection rules, diagnostics, and rule execution health. Source: `raw/2026-07-07-web-the-blind-spot-in-the-watchtower-detections-for-when-someone-attacks-y.md`. confidence: 1 source, last-confirmed 2026-07-07.
- The source recommends an approved-admin or automation watchlist so edits by unexpected actors to analytic rules, access grants, playbooks, watchlists, incidents, and workbooks become high-signal alerts. Source: `raw/2026-07-07-web-the-blind-spot-in-the-watchtower-detections-for-when-someone-attacks-y.md`. confidence: 1 source, last-confirmed 2026-07-07.
- The source highlights catastrophic or stealthy Sentinel tamper paths: analytic rule deletion/disablement, retention shortening, connector disablement, diagnostic-setting deletion, unexpected portal sign-ins, automation/playbook/watchlist changes, incident tampering, workspace deletion, and resource-lock deletion. Source: `raw/2026-07-07-web-the-blind-spot-in-the-watchtower-detections-for-when-someone-attacks-y.md`. confidence: 1 source, last-confirmed 2026-07-07.

### Typed entities
- product: Microsoft Sentinel
- log/table: AzureActivity
- log/table: SentinelAudit
- log/table: SentinelHealth
- log/table: SigninLogs
- log/table: SecurityIncident
- function: `_SentinelAudit()`
- function: `_SentinelHealth()`
- control: approved-admin watchlist
- control: resource delete lock
- control: out-of-workspace alert export

### Explicit relationships
- SIEM self-monitoring complements ordinary threat detections by treating the detection platform as an asset attackers may tamper with.
- Approved-admin watchlists reduce noise by distinguishing expected SOC/configuration changes from unexpected actors.
- Diagnostic-setting deletion, data connector changes, and data collection rule changes can cause rule silence even when analytic rules remain enabled.
- Out-of-workspace alert export mitigates the limitation that an attacker with full workspace control can disable detections inside the same workspace.

### HoneyDrunk implications
- If HoneyDrunk uses Sentinel, maintain a small approved-admin/automation list for security-tool changes and alert when anyone else changes rules, feeds, roles, retention, incidents, or playbooks.
- Pair control-plane change detections with silence checks on high-volume tables where possible.
- Export critical SIEM-self-protection alerts outside the monitored workspace or tenant boundary when feasible.

### Privacy and quality notes
- Query patterns were summarized as detection categories rather than copied as operational runbooks. Adapt table names, watchlists, scope, and alert routing to the active tenant before use.

## 2026-08-21 compile additions: execution-path monitoring

### Source-backed claims
- "A Closed Network Path Is Not a Closed Execution Path" argues that defenders should correlate event-driven cloud execution from initiating message or event through queue/bus, function/workflow, service identity, workload, and privileged downstream action instead of relying only on network reachability diagrams. Source: `raw/2026-08-21-rss-tldr-infosec-a-closed-network-path-is-not-a-closed-execution-path-6-mi.md`; page: [[ai-coding-agent-security]]. confidence: 1 practitioner security source, last-confirmed 2026-08-21.
- The source says CloudTrail, application logs, mesh logs, flow logs, Lambda/function logs, event-bus rules, and original cross-account events may each record benign-looking pieces of a chain, while no single log source reconstructs the complete execution path for defenders. Source: `raw/2026-08-21-rss-tldr-infosec-a-closed-network-path-is-not-a-closed-execution-path-6-mi.md`. confidence: 1 source, last-confirmed 2026-08-21.

### Typed entities
- concept: execution-path monitoring
- log source: CloudTrail
- log source: application log
- log source: service mesh log
- log source: flow log
- resource: event bus rule
- resource: queue policy
- resource: function trigger

### Explicit relationships
- Execution-path monitoring complements SIEM self-monitoring by treating event subscriptions and workload identities as part of the security boundary.
- Individual benign audit records can contradict the real attack path when no correlation joins the initiating event to the final privileged action.

### HoneyDrunk implications
- For cloud agents and event-driven services, preserve correlation IDs across event source, queue/bus, function/workflow, workload identity, and privileged API call.
- Review detection coverage during design; post-incident log stitching is weaker than predeclared execution-path baselines.

### Quality notes
- Source is practitioner security guidance. The wiki retained architecture and monitoring implications, not copy-pastable exploit steps.


## 2026-09-19: TLS fingerprints support contextual investigation

### Typed entities

person: Sergio Albea; concept: JA4; concept: JA4S; concept: KQL; project: FoxIO; concept: TLS fingerprint baseline.

### Claims and evidence

- Albea’s defensive examples use JA4 client-handshake characteristics and JA4S server context, including GatewayJA4 in EntraIdSignInEvents and ja4/ja4s in DeviceNetworkEvents AdditionalFields where those fields are present. Structured components support investigation beyond exact matches. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-rss-ja4-ja4s-kql-threat-hunting.md)
- The author reports low coverage from FoxIO’s mapping dataset in the tested environment. Unmatched or rare fingerprints, missing SNI, unusual ALPN, or cipher-count differences need application/client context; neither rarity nor mapping absence establishes compromise. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-rss-ja4-ja4s-kql-threat-hunting.md)

### Explicit relationships

TLS fingerprint hunting uses structured telemetry and contextual baselines; useful detection depends-on field availability and expected client behavior.

### Decision and quality notes

Practitioner hunting summary, not a validated HoneyDrunk detection. No individual user/address data or executable query payloads were promoted. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Do HoneyDrunk telemetry sources contain JA4/JA4S fields, and what expected-client baselines and contextual checks distinguish useful anomalies from benign rarity or missing mappings? See [[indexes/gaps]].


## 2026-10-18: OCSF normalization needs semantic tests as well as typed representations

### Typed entities

project: Atlassian; project: Databricks; project: OCSF; library: TypeGo; concept: security-event normalization; concept: canary promotion.

### Claims and evidence

- The Atlassian/Databricks account describes transforming heterogeneous security logs into OCSF before lakehouse storage, representing the schema in Go types, and correlating standardized entities across event sources. Query and cost improvements are reported for its own workloads. confidence: 1 source, last-confirmed 2026-10-18 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-18-rss-reducing-the-noise-how-atlassian-built-an-ocsf-security-lakehouse-on-d.md)
- Its self-service mapping workflow still generates tests, submits reviewed changes, validates canaries at scale, and waits through a soak before production promotion. Schema versions, unmapped fields, and entity meaning remain substantive validation concerns; planned agent hunts and context graphs are roadmap items. confidence: 1 source, last-confirmed 2026-10-18 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-18-rss-reducing-the-noise-how-atlassian-built-an-ocsf-security-lakehouse-on-d.md)

### Explicit relationships

Security correlation uses normalized OCSF entities; safe mapping promotion depends-on tests, review, and canary evidence. See [[opentelemetry-genai-observability-and-ecosystem]].

### Decision and quality notes

Source-interpretation flag: the assertion that typed schemas make invalid mappings impossible overstates what compilation proves. Types constrain representation; the account itself retains regression and canary gates. No schema adoption, measured HoneyDrunk performance, or commercial comparison is established. Source-specific claims remain provisional; derived queries add no independent support. Open question: Which HoneyDrunk telemetry mappings validate timestamp and identity semantics, unmapped-field retention, schema upgrades, privacy, and canary rollback beyond type checking? See [[indexes/gaps]].

### Source interpretation resolution

The account says embedding OCSF in Go types guarantees correctness and prevents invalid mappings. An interpretation that compile success guarantees semantically correct event transformations is retained here as rejected framing. superseded-by: [bounded interpretation](#ocsf-mapping-interpretation-2026-10-18), 2026-10-18T10:05:47-04:00; reasoning: The same account requires local regression tests, review, canary validation, and soak. Typed representation is the supported narrow claim; correct timestamps, identity mapping, and event meaning still need validation.

<a id="ocsf-mapping-interpretation-2026-10-18"></a>

Selected interpretation: The same account requires local regression tests, review, canary validation, and soak. Typed representation is the supported narrow claim; correct timestamps, identity mapping, and event meaning still need validation. confidence: 1 source, last-confirmed 2026-10-18. [captured source](../raw/2026-10-18-rss-reducing-the-noise-how-atlassian-built-an-ocsf-security-lakehouse-on-d.md)
