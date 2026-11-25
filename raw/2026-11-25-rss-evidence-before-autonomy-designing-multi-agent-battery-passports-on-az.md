---
source: "https://techcommunity.microsoft.com/t5/azure-architecture-blog/evidence-before-autonomy-designing-multi-agent-battery-passports/ba-p/4575061"
title: "Evidence before autonomy: Designing multi-agent battery passports on Azure"
author: "Dominik Zemp"
date_published: "2026-11-23"
date_clipped: "2026-11-25"
category: "Software Architecture"
source_type: "rss"
canonical_url: "https://techcommunity.microsoft.com/blog/azurearchitectureblog/evidence-before-autonomy-designing-multi-agent-battery-passports-on-azure/4575061"
---

# Evidence before autonomy: Designing multi-agent battery passports on Azure

## How trusted battery evidence protects EU market access and opens new business options

**Author:** Dominik Zemp, Microsoft Switzerland, Enterprise Cloud Solution Architect

*About this article.* This article is written from the author's perspective as an Enterprise Cloud Solution Architect contributing to the wider Microsoft community, and the views expressed are the author's own. It is not official Microsoft documentation, product guidance or a product announcement. For official guidance, see [Microsoft Learn](https://learn.microsoft.com/) and the [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/). The scenario is fictional and uses synthetic data only. The article proposes a design; it does not describe a customer engagement, a production deployment or measured results. The article provides general information, not legal, regulatory, security or other professional advice.

The public GitHub repository [[dzemp/multi-agent-digital-battery-passport](https://github.com/dzemp/multi-agent-digital-battery-passport)] contains the companion prototype for this article, including the passport application and its AI agents, the Bicep templates and the command-line tool that deploy the Azure infrastructure, and documentation such as the architecture, scenario walkthrough and threat model.

## Executive summary

From February 18, 2027, a digital passport becomes a market-access requirement for in-scope batteries first placed on the EU market or first put into service there [1]. For manufacturers, this is not simply a documentation deadline. Missing mandatory data can block a release on day one. As due-diligence and forced-labor obligations phase in during 2027, disputed sourcing evidence can block a release too, while outdated approvals can allow unsupported claims to reach customers. The challenge is to keep evidence current and make accountable decisions when the facts change.

This article proposes an Azure reference architecture that connects supplier evidence, production records and review decisions to individual batteries. Microsoft Fabric prepares supplier and production data for analysis and reporting. Microsoft Foundry agents help interpret documents and prepare reviews. Accountable people resolve adverse findings and approve methods and policies. The passport application, not the AI, enforces publication controls and records decisions and passport versions in Azure SQL Database.

The central design principle is to bind every decision to the evidence it judged. The article follows a conflict between a supplier certificate and a transport record. Two batteries use material from the affected lot and need review; a third uses a different lot and can proceed if its own checks pass. When the evidence changes, the earlier review can no longer authorize publication, and the affected decision must be made again.

The immediate aim is dependable passport operations that support EU market access. This is a proposed design, not measured performance: its value must be demonstrated through reliable controls, reduced investigation effort and sustainable total operating cost.

## 1. Why battery passport evidence becomes a business issue

### The business problem behind the regulation

The EU battery passport makes battery data a condition of market access. From February 18, 2027, every in-scope battery needs a passport when it is first placed on the EU market or put into service there [1]. Batteries for electric vehicles and for light means of transport such as e-bikes are in scope, as are industrial batteries over 2 kWh. The passport is an electronic record linked to the battery by a unique identifier and a QR code, and access rights determine what each reader sees.

The rules take effect in phases, and the design must cover all of them:

- **Since July 20, 2026:** The EU registry for digital product passports is live, and battery passports are registered there [3], [32].
- **February 18, 2027:** The battery passport becomes mandatory. Carbon footprint, recycled content and due-diligence information are not yet required in the passport on this date [32].
- **August 18, 2027:** Battery due-diligence obligations apply [2].
- **December 14, 2027:** The Forced Labor Regulation prohibits products made with forced labor from being placed or made available on the EU market [35].

One company is accountable for each passport: the responsible economic operator. It must keep the passport accurate, complete and up to date, and it can delegate the work, but not the accountability [1], [32]. In this article, that is the battery manufacturer; Appendix C describes when an importer or a vehicle manufacturer holds the role instead [32].

Passports also have to work across company boundaries. They must align with the EU's common Digital Product Passport (DPP) system and follow the data models in the Commission's semantic repository [3, Arts. 11 and 12]. European standards for identifiers, data carriers, APIs and data exchange support that alignment [36].

Behind these rules lies the business problem that this article addresses: keeping evidence, battery genealogy and decisions aligned as facts change. Battery genealogy is the record of which material lots went into which battery. The regulation does not require AI or blockchain. The value lies in handling change in a controlled way and keeping a traceable account of each decision.

### One supplier conflict, three batteries

Consider a manufacturer preparing three batteries for release. Batteries 1 and 2 contain material from supplier lot A; battery 3 uses lot B. The certificate for lot A has a valid digital signature, but its origin claim conflicts with the transport records. For this illustrative example, the manufacturer's sourcing policy requires a review before affected batteries can be released. In February 2027, this check is a company control rather than a passport field.

The team needs to establish which batteries contain material from lot A, whether the conflict has a reasonable explanation and who is accountable for accepting that explanation.

Success is not simply publishing three passports. It is identifying the two affected batteries, avoiding an unnecessary hold on the third and ensuring that an earlier review cannot approve evidence that has since changed.

### Value beyond the first passport

Figure 1 shows how solving the lot A problem reaches beyond one release decision.

*Figure 1. The same evidence foundation supports passport obligations and potential customer value.*

**Horizon 1** is the business case this architecture is designed for: a correct passport for every battery in scope, without releasing batteries with unresolved issues or holding batteries that are unaffected.

**Horizon 2** is a credible extension: the same traceability could show vehicle manufacturers, often called original equipment manufacturers (OEMs), the carbon methods, sourcing evidence and review status behind a claim. Customer acceptance and commercial benefit remain unproven. **Horizon 3** is exploratory and outside the scope of this design: lifecycle history might later help qualified partners assess batteries for second-life uses such as stationary storage.

### What the leadership team needs to see

The Chief Sustainability Officer (CSO) needs to distinguish well-supported claims from claims that are incomplete, disputed or awaiting assurance. A single green compliance indicator would hide too much.

The Chief Technology Officer (CTO) needs that information to stay consistent across source systems, the passport application and reporting. That requires clear record ownership and controlled interfaces. Azure SQL holds current state and ledger history, Fabric prepares connected data for investigation and reporting, and Foundry supports bounded interpretation of documents. Other technologies could meet the same requirements; what matters is that the application remains the authority.

For the Chief Financial Officer (CFO), the case depends on the time needed to identify affected products, the duration of avoidable holds and the total cost of resolving an exception, including human review and correction of agent output. No savings or return are established here; section 5 outlines a cost model for testing the case.

## 2. Where AI agents help and where people decide

AI agents help prepare decisions. Qualified people remain responsible for safety, legal interpretation and decisions on adverse findings. The passport application enforces approved rules and required human approvals. Routine work can proceed automatically when those rules permit it, but no agent can bypass them.

### Helping people work through mixed evidence

Supplier evidence includes certificates, audit reports, transport documents and correspondence in different formats and languages. A data pipeline can move these files and check their structure, but it cannot always explain why two statements disagree. For lot A, an agent can identify the conflicting passages and explain which batteries may be affected. The reviewer receives a focused case rather than a folder of documents and still owns the decision.

Not everything needs AI. The application performs the tasks that require a repeatable result: it verifies signatures, validates data types, calculates approved formulas and enforces access rules.

### Five roles, described by what each may do

The architecture divides the work into five roles. Each role is described by what it is permitted to do, not by an autonomy score. Even the most automated role cannot override a failed check or a required human approval.

- **Regulatory watch: advisory.** The agent summarizes relevant legal changes and identifies potentially affected rules or records. Legal and compliance owners decide what those changes mean and whether a production policy should change.
- **Supplier due diligence: bounded action with mandatory escalation.** The agent gathers evidence, compares claims and prepares a cited review. It can request that the application place affected batteries on hold under an approved policy, but it cannot clear an adverse finding on its own. The same reviews later support the due-diligence report behind the passport's responsible-sourcing information [1, Annex XIII], [2], forced-labor inquiries and, where applicable, the Corporate Sustainability Due Diligence Directive [37].
- **Carbon footprint: automated workflow within a pinned method and verifier check.** The agent prepares per-batch calculation inputs and calls a deterministic calculator with pinned versions of the approved method and emission factors. A run completes only when an independent check reproduces the result exactly and every input traces to approved evidence. Missing inputs stop the run, and gaps stay visible rather than being filled with plausible model-generated values. The method owner remains accountable for the calculation approach.
- **Passport issuance: automated workflow within deterministic publication gates.** The agent assesses whether a candidate passport appears ready, requests publication and explains any gaps that block it. The application, not the agent, determines publication eligibility and commits the version. It does not write field values or access groups: a deterministic passport builder in the application maps the source records and applies the legal access groups and the rules for each battery category [1], [31]. No model-generated text appears in published passport fields. If every check passes, publication needs no separate manual step, but the agent has no write access to the passport database.
- **Lifecycle update: automated workflow within validation and duplicate checks.** The agent interprets authorized submissions from OEMs, repairers and recyclers and requests the corresponding updates. The application validates each event, checks whether it has already been processed and preserves the version history. Partner systems, including partners' own agents, submit signed messages through the intake route or a data-space connector; they never call the passport agents directly.

The passport application, not the agents, orchestrates the work. It runs Microsoft Agent Framework workflows inside the application itself [29]. Each run starts from a business event, such as changed evidence. Agents return typed proposals, and the application routes the next step by fixed rules, so agents never pass control to one another. Microsoft's orchestration guidance advises against agent-to-agent handoff when routing is deterministic and rule-based [30]; here, such a handoff could also bypass a required check or reviewer. Business state stays in Azure SQL Database, the system of record; Appendix C describes how runs start and resume [38].

### Bind decisions to evidence

The certificate for lot A can pass every technical check while the sourcing concern remains unresolved. A design that stores a single "approved" flag would merge those outcomes and keep the flag after the facts change. This architecture therefore records three outcomes separately:

1. **Evidence validity.** A verifier checks the signature, issuer, expiry and revocation status against the organization's trust policy. Cryptographic validity does not establish that the supplier's origin claim is true.
2. **Human judgment.** An accountable reviewer investigates the conflict and records a disposition: the decision, the reasons for it and the information considered. The disposition names a specific decision context, which the application calculates from the evidence versions, material relationships and the applicable method and policy versions.
3. **Publication eligibility.** Before it commits a passport version, the application checks that the disposition still names the current decision context.

When material evidence, a relationship, a method or a policy changes, the application calculates a new decision context. The earlier disposition still records what the reviewer judged, but it belongs to the old context and cannot authorize publication under the new one. Reassessment is required. Human approval also cannot waive a mandatory technical or legal requirement. Section 3 shows this sequence for lot A, where a corrected transport record turns context 7 into context 8.

### Choosing language models for each role

An agent role consists of instructions, tools, permitted data and controls; it does not need its own model. Pretrained Foundry models [14] can do this work when governed retrieval supplies current evidence and legal sources with each request. Fine-tuning cannot add evidence the manufacturer does not hold or replace retrieval and the application's controls [23]. Consider it only if a role keeps failing in the same way after its prompts, tools and retrieval improve, and expert-reviewed examples exist.

Supplier due diligence and regulatory watch reconcile ambiguous sources, so both are starting candidates for a more capable reasoning model. The carbon, issuance and lifecycle roles mainly prepare structured tool requests, so a smaller model may suffice.

### Earn autonomy through evaluation

Agent quality has to be judged against the work people actually need done. For supplier due diligence, a useful evaluation asks whether the agent identifies conflicting evidence, cites the right passages and explains the issue without inventing facts. It must include cases where no conflict exists. Otherwise, an agent that raises a hold on everything could appear reliable while creating unnecessary work.

Each candidate configuration, meaning a model version together with its prompts, tools and retrieval settings, runs against the same versioned cases. These include missing, contradictory, multilingual and maliciously instructed documents. Development and test cases come from different suppliers and document families. Deterministic checks score structured fields, tool calls and the resulting application state. Microsoft Foundry's built-in evaluators can add measures such as groundedness [22], which shows only that an answer agrees with its sources, not that those sources are true. Domain experts judge sourcing and legal quality, and an AI judge used to rate explanations should first be calibrated against human-scored examples.

Candidates must first meet the required safety and quality checks. Compare those that pass on task quality, reviewer effort, response time and cost per correctly completed case. A role takes on more of the work only where these cases show that it stays reliable within its control boundaries. A replacement model or configuration is adopted only after it passes the same checks.

## 3. Following lot A through the Azure reference architecture

The proposed architecture connects existing product and production systems to supplier evidence, agent-assisted work and a maintained passport record, without replacing the factory's systems of record or assuming one exchange technology for every supplier.

Figure 2 shows the pattern in one view. Evidence flows from sources and partners into evidence preparation. Inside the authority boundary, the passport API on Azure Container Apps applies deterministic publication controls and is the only writer of passport state in Azure SQL Database.

*Figure 2. Simplified view of the proposed architecture. In the lot A walkthrough, context N is context 7 and context N+1 is context 8. Figure B1 in Appendix B shows the full reference architecture with numbered workflow steps.*

The rest of this section follows the lot A certificate through these stages. It is an illustrative design walkthrough, not a recorded implementation result.

### Receiving the evidence and finding the affected batteries

Enterprise resource planning (ERP), manufacturing execution (MES) and quality management (QMS) systems supply the records that identify products, production activity and quality evidence. Fabric pipelines or supported mirroring bring permitted data into OneLake. Access controls must be configured for this analytical copy, because mirroring Azure SQL data does not transfer the source permissions or masking rules to Fabric [4].

In this design, MES owns the as-built lot-to-battery genealogy, reconciled with ERP supplier-lot identities; manufacturing data owners approve corrections. At commit, the passport API asks MES to confirm that the genealogy behind the candidate has not changed; if it has, or MES cannot confirm in time, the API refuses the commit. If the affected population is uncertain, operations must hold the potentially affected scope rather than assume that unlinked batteries are safe.

Partners submit evidence through a controlled file or API route or, where both organizations participate in Catena-X [24], through an agreed data-space connector (Appendix C). The regulation mandates neither route, and neither proves that a claim is true.

A deterministic verifier then checks a credential's issuer, proof, validity and status against the agreed profile. For an ordinary document, it records the authenticated sender and any signature check instead. The application records that technical result separately from authorization and the later compliance disposition. It stores the file in Blob Storage and records its reference, hash and status in SQL.

In Fabric, material genealogy links lot A to batteries 1 and 2, and the transport record is matched to the same lot. Battery 3 is linked to lot B, so the concern does not automatically apply to it.

The application then routes a short, lot-specific task to the supplier due-diligence agent in Microsoft Foundry Agent Service [7], [29]. Through role-scoped tools, the agent can read the pinned supplier claim and transport record; it has no database credentials or permission to browse unrelated evidence. It compares the sources, cites the passages that disagree and returns a typed result asking for review. A shipping route that differs from a claimed origin may have a legitimate explanation, so the agent reports a concern rather than accusing the supplier. The application applies its sourcing rules and places batteries 1 and 2 on hold. Because a database hold cannot stop a shipment, the application sends each hold to ERP, MES or QMS, which alone releases physical stock.

### Publishing the unaffected battery

While the compliance review of lot A continues, battery 3 moves toward publication. The carbon agent prepares inputs and requests the approved calculation, the passport builder assembles the candidate passport, and the issuance agent assesses its readiness and requests publication. The scoped hold contains the sourcing risk without turning one supplier investigation into a delay for unrelated products.

Publication authority belongs to the passport application on Azure Container Apps [8]. It rechecks battery 3's accepted evidence versions, genealogy assurance, dispositions and policies in the same SQL transaction as the write. That transaction does not span MES, Fabric or Blob, so later source corrections still trigger reassessment. The application then commits the passport version, an audit record and an outbox entry together in Azure SQL Database. The outbox records work to deliver to other systems; because it is saved in the same transaction, no delivery request is silently lost [9].

Two separate processes follow the commit. The passport's integrity status stays pending until ledger verification completes (section 4). A relay reads the outbox entry and passes the registration to the registry adapter, retrying if necessary; receiving systems must tolerate duplicates [9]. The adapter records the registry's answer as a separate status. A committed passport is not proof of registry acceptance, and a queued registration is not permission to release a product.

Registry access is a production dependency: only verified economic operators can register passports, and their verification must be renewed periodically [3, Art. 4], [32]. Appendix C summarizes these registry mechanics.

### Revisiting a decision when the facts change

Back on the lot A track, a compliance reviewer investigates the conflict:

1. The application calculates context 7 for batteries 1 and 2. It contains the certificate, the original transport record, the lot-to-battery links and the applicable sourcing policy.
2. The reviewer records a disposition against context 7.
3. Before publication, a corrected transport record arrives.
4. The application calculates context 8. Contexts 7 and 8 are versions of the decision basis, not passport versions.
5. When the issuance agent requests publication for batteries 1 and 2, the application sees that the recorded disposition names context 7, not context 8, and rejects the request. The earlier review cannot approve facts the reviewer did not see, even when reusing it would be faster.
6. The reviewer examines the corrected record and, in this example, records a new disposition against context 8. Publication can proceed only after the application reruns the remaining checks.

Had the new evidence failed to resolve the concern, the hold would remain. The workflow supports either outcome without letting an agent decide which result the business would prefer.

For readers who want every exchange, Figure 3 retraces the full lot A case from supplier submission to reporting; the steps above are its critical path.

*Figure 3. The full lot A sequence, read from top to bottom. Rows E1 to E26 are numbered separately from the workflow steps in Figure B1.*

### Maintaining the record after release

The evidence remains relevant after the batteries leave the plant. OEMs, repairers and recyclers send authorized updates through the partner intake route, and the application records them only after the checks described in section 2. Routine updates, such as a new state-of-health value, keep the same passport [32]. Much of that data reaches the battery manufacturer through the vehicle manufacturer, so the data-sharing agreement with each OEM is part of the design. Appendix C describes how the design handles ownership changes, repurposing, remanufacturing and recycling, and keeps private owners' personal data out of the passport [1, Art. 77(7)].

### Giving each reader the right view

Public QR readers receive the static public view; the authenticated API serves each access group its restricted view. An OEM using the restricted API can see the carbon method, supporting sources and sourcing-review status it is entitled to see. That entitlement rests on the regulation's legitimate-interest access [1, Art. 77(9)] or on a contract between the companies, and the application records the basis of each grant. This is the practical basis for Horizon 2: the OEM can inspect the basis of a claim instead of receiving an unexplained final number. Authorities and notified bodies receive the access that the regulation provides [1].

Because detailed access rights still await an implementing act [32], the roles shown in this architecture are illustrative, not a statement of legal entitlements. Legal and compliance owners translate the applicable rules into approved, versioned access policies.

For reporting, the application sends a minimized copy of committed status to OneLake, and Power BI combines it with evidence-readiness and supplier views. The CSO can see that the lot A concern affected two batteries, who reviewed it, whether it remains open and which passport versions reflect the outcome. Linking that view to retained evidence and decisions is intended to reduce the effort of reconstructing a case for a customer or auditor. Access to these reports remains governed: an executive dashboard does not justify copying all restricted evidence into an analytical dataset.

Report coverage as the number of in-scope batteries with a current, valid passport divided by all in-scope batteries in the release scope. Held batteries, and batteries whose passports the manufacturer maintains for an OEM, stay in the total. If only battery 3 has a valid passport, coverage is 1 of 3, not 100%. Show when the report was refreshed; if it differs from the passport application, the application is authoritative, and a dashboard never authorizes release.

## 4. Data and trust: Fabric, Azure SQL and the blockchain question

### Why preparation and publication remain separate

Throughout the lot A journey, Fabric prepared and reported information, but only the passport application recorded decisions and passports. That division reflects two different needs. Investigators compare supplier documents with production and logistics data; later, an auditor needs a controlled, versioned record of the evidence and decision behind a published passport.

Microsoft Fabric supports the first need by bringing information together, preparing reusable datasets and supporting reporting. Azure SQL Database supports the second by holding passport state, decisions and their relationships within transactions. A dashboard can tolerate a clearly disclosed refresh delay, but a publication decision cannot rely on a reporting copy that may be out of date. The product boundary matters too: SQL database in Fabric cannot create ledger tables under the documented limitations used for this design [6]. Azure SQL Database therefore holds the operational record, and Fabric remains valuable without becoming the authority for release.

### Preserving the route from source to battery

Fabric'smedallion pattern organizes data preparation into layers. Bronze retains what arrived, with its source and receipt time; Silver standardizes identifiers, units and relationships so that supplier lots match batteries; and Gold prepares candidate passport packages, evidence-readiness views and carbon inventories.

For lot A, this processing must preserve both the certificate and the conflicting transport information. A transformation should not silently select whichever value looks more complete. Each candidate package carries the relevant evidence references and source versions, so the information seen by the application can be reconstructed later.

Shared evidence requires careful treatment in analytics. If a production batch consumed 150 kg of a lithium compound and two batteries reference that batch, the material total remains 150 kg, not 300 kg. Battery counts use distinct identities, while per-battery values follow approved allocation rules.

### Making decisions and changes traceable

Azure SQL Database is the working record for battery status, evidence references, review decisions and passport versions. SQL Ledger adds tamper evidence to selected tables [10].

Evidence files, such as a supplier certificate, are kept in versioned Blob Storage [13]. SQL records each file's location, version and cryptographic hash, so the application can detect a changed file and retrieve the evidence behind a decision. SQL Ledger digests are retained in protected storage that database administrators cannot rewrite, and verification compares the database history with those digests [11], [12]. Because verification is asynchronous, the application reports whether it is pending, verified or failed. Appendix C covers the storage, digest and retention details.

Together, file hashes, retained versions and ledger verification can reveal certain changes to stored evidence or database history. They cannot establish that a supplier's claim is true, prove a battery's physical identity or confirm legal compliance.

### Why the baseline does not use a blockchain

A battery passport does not inherently require a blockchain; the regulation does not prescribe one [1]. This proposal has one accountable operator, so Azure SQL ledger tables and protected digests support its history without a jointly governed network.

A permissioned blockchain is relevant when independent organizations need shared control of a common history, but it would not resolve conflicting evidence. Consider Azure confidential ledger if the threat model in section 5 must cover collusion between database and storage administrators, or if partners need receipts they can verify independently [17]. Public hash anchoring adds privacy, cost and governance trade-offs.

## 5. Operating the architecture reliably

The lot A workflow must remain dependable when services fail or evidence changes. The following sections cover the qualities this workload depends on most and map them to the pillars of the Azure Well-Architected Framework (WAF) [20]. Its AI guidance makes ongoing evaluation part of operating the workload, rather than a one-time model-selection exercise [21].

### Reliability: keep records available and failures visible

Passports must outlive the system, and even the company that issued them. The regulation requires open, interoperable formats without vendor lock-in, and the passport must remain available even if the operator ceases to exist or ceases its activity in the EU [1, Arts. 77(5) and 78(e)]. Published passports should therefore remain readable when AI, Fabric or partner connections fail. Static public views served through Azure Front Door depend on neither SQL nor AI, and restricted views are precomputed for each access group. Keep a tested export in the Commission's data models [3, Arts. 11 and 12] and a backup copy with an independent operator authorized in writing [1, Arts. 77(4) and 78(c)].

Set separate recovery objectives for reading and publishing, because publishing can pause but reading should not. Run the restricted read API, the passport API and the workflow worker as separate container apps, so that each can fail, scale and recover on its own. Work awaiting evidence or verification must wait rather than bypass checks. Restores must reconcile SQL records, Blob evidence, protected digests and registry work, while retries must not create duplicate effects.

### Security: enforce authority outside the model

Managed identities, Key Vault and private data-service connectivity support the permission boundaries. Give each agent role its own least-privilege identity, scoped retrieval and allowlisted tools, so that a misled agent can reach only its role's data and cannot approve its own finding. APIs enforce field and action entitlements before returning data or calling tools. Supplier documents may contain prompt-injection instructions [15], so model warnings are insufficient. Turn on Prompt Shields document attack detection, which is off by default, for every model deployment or agent that reads partner content [39]. Scan uploads with Microsoft Defender for Storage on-upload malware scanning before an agent or reviewer opens them [40].

Public QR reads need an internet-reachable HTTPS entry point with abuse protection, such as Azure Front Door with Azure Web Application Firewall rate limiting and bot protection. Restricted partner and tool APIs require authenticated, scoped access. Choose processing regions for Fabric and models deliberately; private endpoints do not by themselves establish residency or partner entitlement. Use Microsoft Purview to classify restricted data and label the Fabric items that hold it.

The companion prototype publishes a STRIDE threat model with seven trust boundaries and fifteen threats [41]. Table C1 in Appendix C summarizes the threats that shape this architecture most. It covers a prototype with synthetic data, not a production assessment; a production threat model must also address registry credentials [3, Arts. 4 and 19], partner connectors and credential issuers, isolation between OEMs and tested disaster recovery.

### Cost optimization: count the whole process

Measure cloud consumption and human review together. A cheaper model may cost more overall if its output creates rework. A simple cost model separates three drivers: platform cost, which changes little with volume; per-battery cost, including public reads that must be free of charge [1, Art. 78(b)]; and per-exception cost for model tokens, reviewer time and rework. Divide the total by the number of correctly completed cases, not by the number of agent runs, and estimate each driver with the Azure pricing calculator [42]. Appendix C lists what each driver covers.

### Operational excellence and performance: make changes explainable and evidence timely

Version prompts, tools, methods and policies, and re-evaluate representative cases when they change. Azure Monitor and Application Insights should trace the submission through review, publication and registry response without unnecessarily logging confidential content. Named owners handle holds and failures; people, not agents, activate policy changes. Microsoft Agent 365 can optionally add agent inventory and governance, but not publication authority [33]; see Appendix A.

Legal owners must also assess applicable AI Act obligations for the intended uses, including transparency and AI literacy [34]. Human review and the authority descriptions used in this article do not establish compliance or determine a system's legal risk classification.

For performance, prepare evidence in batches unless freshness requirements justify streaming. Container Apps can scale with demand [8], but database, model and partner limits still matter. For lot A, the priority is getting corrected evidence to the release process in time.

## 6. Conclusion: three principles to carry forward

The lot A conflict began as a disagreement between two documents. It became a business issue because it affected the release of batteries 1 and 2. The architecture keeps that connection visible: it holds the two affected batteries, lets battery 3 proceed and refuses to let an outdated review authorize changed evidence.

Three principles carry beyond battery passports:

1. **Keep authority outside the model.** Agents interpret evidence and prepare actions; deterministic systems enforce release and publication.
2. **Bind decisions to evidence.** A decision applies only to the evidence, relationships, methods and policy against which it was made.
3. **Earn autonomy through evaluation.** Extend an agent's autonomy only where evaluation shows that it stays reliable within its control boundaries.

**Evidence before autonomy.**

## References

All links were last accessed on November 18, 2026. EU acts, harmonized standards, Commission guidance and Azure capabilities change, so confirm the current versions before you rely on them. Consolidated texts of EU law are documentation tools; only the texts published in the Official Journal of the European Union are authentic.

1. [Regulation (EU) 2023/1542 concerning batteries and waste batteries](https://eur-lex.europa.eu/eli/reg/2023/1542/2026-08-13/eng), consolidated version of August 13, 2026, particularly Articles 7, 13, 14, 47, 48, 77, 78 and 79 to 84. Also available as an [EU Publications Office consolidated text](https://publications.europa.eu/resource/cellar/d86c4599-ac88-11f1-b9e5-01aa75ed71a1.0007.02/DOC_1).
2. [Regulation (EU) 2025/1561 amending Regulation (EU) 2023/1542 as regards obligations of economic operators concerning battery due diligence policies](https://eur-lex.europa.eu/eli/reg/2025/1561/oj/eng), particularly Article 1. Also available as an [EU Publications Office text](https://publications.europa.eu/resource/cellar/fe1163e4-6cdd-11f0-bf4e-01aa75ed71a1.0006.03/DOC_1).
3. [Commission Implementing Regulation (EU) 2026/1778 laying down the implementation arrangements for the digital product passport registry set up under Regulation (EU) 2024/1781](https://eur-lex.europa.eu/eli/reg_impl/2026/1778/oj/eng), particularly Articles 4 to 12 and 19. Also available as an [EU Publications Office text](https://publications.europa.eu/resource/cellar/56aaf918-8178-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1).
4. Microsoft Learn. [*Limitations in Microsoft Fabric mirrored databases from Azure SQL Database*](https://learn.microsoft.com/en-us/fabric/mirroring/azure-sql-database-limitations).
5. Eclipse Tractus-X. [*Refactor of the Release Workflow*](https://github.com/eclipse-tractusx/tractusx-edc/blob/main/docs/development/decision-records/2024-10-07-azure-distribution/README.md), Azure distribution decision record, October 7, 2024.
6. Microsoft Learn. [*Limitations in SQL database in Microsoft Fabric*](https://learn.microsoft.com/en-us/fabric/database/sql/limitations).
7. Microsoft Learn. [*What is Microsoft Foundry Agent Service?*](https://learn.microsoft.com/en-us/azure/foundry/agents/overview?view=foundry)
8. Microsoft Learn. [*Azure Container Apps overview*](https://learn.microsoft.com/en-us/azure/container-apps/overview).
9. Microsoft Learn. [*Implement the Transactional Outbox Pattern by Using Azure Cosmos DB*](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos#solution) (Azure Architecture Center), particularly the general pattern and relational-database discussion under Solution; the worked implementation uses Cosmos DB, not the SQL-based design proposed here.
10. Microsoft Learn. [*Ledger overview*](https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview?view=azuresqldb-current).
11. Microsoft Learn. [*Digest management*](https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-digest-management?view=azuresqldb-current).
12. Microsoft Learn. [*Database verification*](https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-database-verification?view=azuresqldb-current).
13. Microsoft Learn. [*Store business-critical blob data with immutable storage in a write once, read many (WORM) state*](https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview).
14. Microsoft Learn. [*Foundry Models sold by Azure*](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure).
15. OWASP GenAI Security Project. [*LLM01:2025 Prompt Injection*](https://genai.owasp.org/llmrisk/llm01-prompt-injection/).
16. Microsoft Learn. [*Connect agents to Microsoft Fabric with Fabric IQ (preview)*](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/fabric-iq).
17. Microsoft Learn. [*About Azure confidential ledger*](https://learn.microsoft.com/en-us/azure/confidential-ledger/overview).
18. Eclipse Tractus-X. [*EcoPass KIT: adoption view*](https://eclipse-tractusx.github.io/docs-kits/kits/eco-pass-kit/adoption-view/), published documentation, not the /next/ development version.
19. Microsoft Learn. [*Microsoft Entra Verified ID architecture overview*](https://learn.microsoft.com/en-us/entra/verified-id/introduction-to-verifiable-credentials-architecture).
20. Microsoft Learn. [*Azure Well-Architected Framework pillars*](https://learn.microsoft.com/en-us/azure/well-architected/pillars).
21. Microsoft Learn. [*Test and evaluate AI workloads on Azure*](https://learn.microsoft.com/en-us/azure/well-architected/ai/test) (Azure Well-Architected Framework).
22. Microsoft Learn. [*Built-in evaluators reference*](https://learn.microsoft.com/en-us/azure/foundry/concepts/built-in-evaluators) (Microsoft Foundry).
23. Microsoft Learn. [*Training in Microsoft Foundry*](https://learn.microsoft.com/en-us/azure/foundry/fine-tuning/overview).
24. Catena-X Automotive Network. [*About us*](https://catena-x.net/about-us/).
25. Gaia-X European Association for Data and Cloud AISBL. [*Gaia-X: A Federated Secure Data Infrastructure*](https://gaia-x.eu/).
26. W3C. [*Verifiable Credentials Data Model v2.0*](https://www.w3.org/TR/vc-data-model-2.0/).
27. Eclipse Dataspace Decentralized Claims Protocol. [*DCP v1.0.1*](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/tree/v1.0.1).
28. Eclipse Dataspace Components (EDC). [*Adopters Manual*](https://eclipse-edc.github.io/documentation/for-adopters/).
29. Microsoft Learn. [*Microsoft Agent Framework overview*](https://learn.microsoft.com/en-us/agent-framework/overview/), particularly Workflows.
30. Microsoft Learn. [*AI agent orchestration patterns*](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) (Azure Architecture Center), particularly When to avoid handoff orchestration.
31. European Commission. [*Digital Product Passport for Batteries (Battery Passport)*](https://single-market-economy.ec.europa.eu/single-market/digital-product-passport/batteries_en), including the linked guidance on data points for each battery category, last updated on October 19, 2026.
32. European Commission. [*EU Digital Product Passport FAQ for Batteries*](https://single-market-economy.ec.europa.eu/single-market/digital-product-passport/eu-digital-product-passport-faq-batteries_en), September 2026, particularly sections 1, 2 and 5 to 10 on timelines, standards, responsibilities, the registry, verification, data requirements, dynamic data, repurposing and compliance.
33. Microsoft Learn. [*Microsoft Agent 365 overview*](https://learn.microsoft.com/en-us/microsoft-agent-365/overview) and [*Microsoft Agent 365 service description*](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365), including governance, observability, feature and licensing boundaries.
34. European Commission AI Act Service Desk. [*AI Act Explorer*](https://ai-act-service-desk.ec.europa.eu/en/ai-act-explorer), for applicability, risk classification, AI literacy and transparency provisions; consult its linked Official Journal texts for legal authority.
35. [Regulation (EU) 2024/3015 on prohibiting products made with forced labour on the Union market and amending Directive (EU) 2019/1937](https://eur-lex.europa.eu/eli/reg/2024/3015/oj/eng), particularly Articles 3 and 39.
36. [Commission Implementing Decision (EU) 2026/1736 on harmonised standards for digital product passports drafted in support of Regulation (EU) 2024/1781](https://eur-lex.europa.eu/eli/dec_impl/2026/1736/oj/eng), particularly the Annex.
37. [Directive (EU) 2024/1760 on corporate sustainability due diligence and amending Directive (EU) 2019/1937 and Regulation (EU) 2023/2859](https://eur-lex.europa.eu/eli/dir/2024/1760/oj/eng). Consult the current consolidated version for later amendments.
38. Microsoft Learn. [*Durable Task Scheduler*](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler) and [*Durable Task extension for Microsoft Agent Framework*](https://learn.microsoft.com/en-us/azure/durable-task/sdks/durable-agents-microsoft-agent-framework).
39. Microsoft Learn. [*Prompt Shields*](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) (Azure AI Content Safety), particularly document attack detection.
40. Microsoft Learn. [*On-upload malware scanning*](https://learn.microsoft.com/en-us/azure/defender-for-cloud/on-upload-malware-scanning) (Microsoft Defender for Storage).
41. Author. *Security and responsible-AI threat model*, companion prototype for this article, synthetic data only, released under the MIT License.  [[dzemp/multi-agent-digital-battery-passport](https://github.com/dzemp/multi-agent-digital-battery-passport)]
42. Microsoft Azure. [*Pricing calculator*](https://azure.microsoft.com/en-us/pricing/calculator/).

## Appendix A: Capability map

This map supplements Figure 2 and the full reference architecture in Appendix B with implementation boundaries and conditional services. It is not a deployment specification.

Table A1. Capabilities and Azure responsibilities.

| Capability | Proposed realization and boundary |
| --- | --- |
| Enterprise intake | Fabric Data Factory pipelines or supported mirroring read permitted ERP, MES, PLM and QMS data. Fabric access must be configured separately from source permissions [4]. MES owns as-built genealogy in this design; candidates retain source revision, completeness and freshness assurance for the application's gates. |
| Partner intake | Controlled file/API submission is a valid intake route; a maintained EDC/Tractus-X connector is optional where partners participate in Catena-X. Agree semantics, usage policy and credentials, and test conformance rather than infer it from the connector. Neither route replaces applicable EU DPP requirements. Earlier Azure-specific Tractus-X images are deprecated [5], [18], [24], [25], [27]. |
| Credential verification | A deterministic verifier checks the supported VC/VP proof, issuer, subject, validity and status. Separate participant identity/eligibility from product-evidence claims and technical verification from field/action authorization and compliance disposition [26], [27]. Other submissions retain sender attribution and applicable signature checks without being treated as VC/VPs. |
| Data preparation | OneLake holds governed bronze, silver and gold datasets. Power BI reports readiness and committed outcomes, but neither controls publication. |
| Optional analytical assistant | A Fabric data agent can support read-only questions through Fabric IQ (preview) [16]. Foundry connections use incoming Microsoft Entra user context or an OAuth session. Validate the selected connection and permissions; analytical answers never authorize publication. |
| Agent roles | Foundry Agent Service supports the five roles with scoped retrieval and allowlisted tools. Each role runs with its own least-privilege identity, and Prompt Shields screens partner documents for embedded instructions [39]. Choose pretrained models for the work each role performs; roles may share a model where it meets their needs (section 2). Agents cannot directly write passport records, clear adverse findings or activate policy changes. |
| Orchestration, review and publication | The Container Apps passport application runs Agent Framework workflows that route typed agent results by fixed rules; agents do not hand control to one another [29], [30]. Each run ends with a result or a hold for human review, and case, hold and review state stays in the same SQL database, which remains the system of record. The application records human dispositions and checks current decision context. It commits the version, audit and outbox in one SQL transaction. This protects accepted SQL context, not live upstream data; source-owned genealogy confirmation also gates physical release. |
| Operational history | Azure SQL Database ledger tables preserve authoritative state and audit history. Protected digest retention and separate verification are necessary to make tampering detectable [10], [11], [12]. Digest anchors must be protected from database writers; ledger history contains only retention-approved data. |
| Evidence storage | Versioned immutable Blob Storage retains files, while SQL holds references and hashes. Microsoft Defender for Storage scans each upload for malware before an agent or reviewer opens it [40]. The application reconciles partial failures without assuming a shared transaction or permission to delete retained files [13]. |
| Reader access | The public QR view is a static file in Blob Storage, served through Azure Front Door. Restricted views are precomputed for each access group and served through the authenticated API, which enforces field entitlements. Battery identity remains independent of the current hosting address. Use applicable DPP identifier/exchange standards and versioned legal access policies, including adopted rules for restricted data [31], [32]. |
| Registry exchange | The outbox-fed adapter uses a verified operator identity and records acknowledgments, failures, registration identifiers and proofs (Appendix C). The registry's automatic checks confirm structure, not compliance [3, Art. 8]. |
| Reporting | The application sends a minimized committed-status copy to OneLake. Power BI shows freshness and includes blocked batteries in the coverage denominator. |
| Shared operations | Microsoft Entra ID, managed identities, Key Vault, Azure Monitor and Application Insights support identity, secrets and traceability. Optional Microsoft Entra External ID manages partner identities, and Microsoft Purview classifies restricted data and labels the Fabric items that hold it. Recovery must include evidence, digests and registry reconciliation, not just database restore. |
| Optional agent governance | Microsoft Agent 365 adds organizational inventory, ownership, governance and observability for connected Foundry agents [33]. It is not the runtime, publication authority or a prerequisite for this architecture; validate integration, telemetry and licensing. Application Insights remains the workload-tracing service. |
| Conditional extensions | Azure Document Intelligence in Foundry Tools may help with complex document extraction; Foundry IQ (Azure AI Search) with governed retrieval; Azure API Management with external API policy; Azure Service Bus with asynchronous delivery; and Azure IoT Hub with device-event ingestion. Azure confidential ledger or a consortium ledger needs the justification discussed in section 4. Microsoft Entra Verified ID depends on partner credential fit [19]. These are not default deployments. |

## Appendix B: Full reference architecture

Figure 2 is a simplified view. Figure B1 shows the full proposed reference architecture behind it. It adds the official regulatory sources, the eleven numbered workflow steps that Figure 3 refers to, the workflow worker and Durable Task Scheduler, the ledger digest container and integrity status, the registry adapter, the Fabric data agent and the optional, trigger-based services. Each agent role carries a short label for the permitted authority described in section 2.

*Figure B1. Full proposed Azure reference architecture. Agents prepare typed, cited proposals; only the passport application writes passport versions. Role labels summarize the authority descriptions in section 2 and are not an industry or regulatory taxonomy. A Catena-X connector is conditional on partner participation and an agreed profile, not a legal prerequisite. EDC/Tractus-X does not itself establish interoperability, certification or deployment [5], [18], [24], [25], [27], [28]. The genealogy gate uses the source-version assurance described in section 3. Microsoft Agent 365 is optional governance and observability, not the agent runtime [33]. Long dashes mark external parties and systems; short dashes mark optional, conditional or recommended components. Azure Front Door is recommended for production public reads, with Azure Web Application Firewall as an option for rate limiting and bot protection. Foundry IQ (Azure AI Search), an optional retrieval service, is distinct from Fabric IQ. The Fabric data-agent box represents governed analytics through Fabric IQ (preview) [16]. Networking, regions and cost are not shown.*

Its numbered flow starts with enterprise and partner intake (steps 1 to 3), continues through data preparation (4), agent work (5) and human review (6) to publication (7), and ends with integrity verification (8), registry exchange (9), reader access (10) and reporting (11):

1. **Enterprise intake.** Data Factory pipelines or mirroring copy permitted ERP, MES, PLM and QMS data into OneLake bronze. MES owns the as-built genealogy, reconciled with ERP lot identities.
2. **Partner intake.** Suppliers and lifecycle partners submit through controlled file or API intake, with provenance, schema checks, malware scanning and quarantine, or through an optional Catena-X connector where both parties participate.
3. **Credential verification.** The verifier checks the VC/VP proof, issuer and status; authorization remains separate. Verified evidence and lifecycle events go to the passport API.
4. **Data preparation.** Fabric validates and joins data, builds versioned candidate packages and reports readiness in Power BI. Nothing is published here.
5. **Agent work.** Five Foundry roles, each with its own least-privilege identity, read permitted context and official sources and propose through typed tool endpoints. Prompt Shields screens partner documents. Agents hold no permission to write, publish, sign or approve.
6. **Human review.** Accountable reviewers record versioned dispositions that name the decision context they judged.
7. **Publication.** The passport API runs deterministic tools, including the passport builder; rechecks evidence validity, genealogy currency with MES, disposition currency and policy version; and commits version, audit and outbox in one SQL transaction.
8. **Integrity verification.** Ledger digests are stored asynchronously in a locked container, and integrity status moves from pending to verified or failed.
9. **Registry exchange and enterprise release.** The outbox relay sends each hold event to ERP, MES or QMS, which sets a blocking quality status and alone releases physical stock. It also passes registrations to the registry adapter, which uses a verified operator identity and stores the registration ID and proof for each version.
10. **Reader access.** Azure Front Door serves the static public view of each version from Blob Storage; partners and authorities use the authenticated restricted read API.
11. **Reporting.** The application sends a minimized committed-status copy to OneLake, and Power BI reports it with evidence readiness.

Agent Framework workflows in the application route typed agent results and hold work for reviewers; Durable Task Scheduler checkpoints run progress, while case and review state stays in SQL. Agent outputs remain proposals until the application and its controls accept them. Microsoft Entra ID, managed identities, Azure Key Vault, Azure Monitor and Application Insights provide identity, credential management and operational visibility across the whole flow. The cross-cutting band also shows Azure Front Door as the recommended public entry point, optional Microsoft Entra External ID for partner identities, Microsoft Defender for Storage, Microsoft Purview, optional Microsoft Agent 365 and the backup and exit controls described in section 5. Appendix A lists the service-level boundaries.

## Appendix C: Implementation considerations

This appendix keeps implementation detail that supports the main text but is not needed to follow the architecture. It is not a deployment specification.

### C1. Who acts as the responsible economic operator

In this article, the battery manufacturer is the responsible economic operator, because it places the finished batteries on the EU market. For batteries made outside the EU, the importer can hold the role, and a vehicle manufacturer that completes the battery, for example by adding the battery management system, becomes responsible [32]. The battery manufacturer can then maintain the passport on the vehicle manufacturer's behalf under a written authorization, without selling or reusing the data beyond that service [1, Arts. 77(4) and 78(d)].

### C2. Data spaces and verifiable credentials

Catena-X is an automotive data-space initiative, Gaia-X a related trust framework and Tractus-X EDC one connector implementation [5], [18], [24], [25], [28]. The Battery Regulation mandates none of them, nor verifiable credentials. Where partners use averifiable credential (VC), a digitally signed statement about an organization or product, packaged in a verifiable presentation (VP) for an exchange [26], [27], the verifier checks the issuer, proof, subject and status against the agreed profile. Passing those checks shows who made a claim, for example that Supplier A says lot A came from Mine North, not that the claim is true. A VP does not itself grant access to data; the passport application decides which organization may see or do what.

### C3. Workflow runs and checkpoints

Case status, holds, dispositions, passport versions and audit records stay in Azure SQL Database. The transactional outbox [9] starts each workflow run through Azure Durable Task Scheduler, which checkpoints run progress so that an interrupted run can resume [38]. A recorded disposition starts a new run that reloads current evidence, policy and decision context and reruns the publication gates.

### C4. Starting model hypotheses

Table C1 lists starting candidates from the Microsoft Foundry model catalog [14]. The same model can serve several roles if it meets their needs; compare candidates on the same cases before choosing.

Table C1. Starting model hypotheses for the five agent roles (not measured).

| Agent role and permitted authority | What the model contributes | Starting hypothesis | What stays outside the model | What evaluation measures |
| --- | --- | --- | --- | --- |
| Regulatory watch: advisory | Compares dated legal sources and drafts impact notes | More capable reasoning model; smaller challenger for simple summaries | Legal interpretation and policy activation | Correct source, status, scope and dates; no unsupported legal assertions |
| Supplier due diligence: bounded action with mandatory escalation | Reconciles conflicting documents, cites passages and prepares a review case | More capable reasoning model; smaller challenger for simple extraction | Credential verification; decisions on adverse findings | Accuracy of critical fields, correct citations, escalation of every known conflict, unnecessary holds |
| Carbon footprint: automated workflow within a pinned method and verifier check | Matches approved batch inputs to the pinned method and explains the result's provenance | Smaller tool-calling model | Method and factor versions, units, arithmetic and the verifier check | Correct inputs and method and factor versions, exact reproduction of the calculator's result, rejection of missing inputs |
| Passport issuance: automated workflow within deterministic publication gates | Assesses whether each candidate appears ready, then requests publication or explains blocking gaps | Smaller tool-calling model; shared capable model as challenger | Field values, access groups, applicability, authorization and the publication transaction | Correct readiness assessments, actionable gap explanations, no improper release |
| Lifecycle update: automated workflow within validation and duplicate checks | Interprets ambiguous partner submissions and explains conflicts | Smaller model; no model for well-structured events | Battery identity, event order, duplicate handling and state transitions | Correct battery and field mapping, duplicate and conflict handling, no unauthorized change |

### C5. Registry mechanics

Only verified economic operators can register passports, typically by using a qualified electronic seal or a qualified electronic attestation of attributes. Verification lapses when that seal or attestation expires, and after three years at the latest, so renewal belongs in the operating calendar [3, Art. 4], [32]. The operator must also protect its registry access credentials [3, Art. 19]. The registry's automatic checks confirm structure and granularity, not compliance [3, Art. 8]. Each proof of registration remains downloadable for only 90 days, so the adapter stores the registration identifier and a copy of the proof for each registered version [3, Arts. 8 and 9].

### C6. Lifecycle events after release

Dynamic data must be updated at least whenever the battery's status changes, not necessarily in real time [32]. A change of ownership keeps the same passport and is not recorded in it, but it can change who has a legitimate interest in restricted data, so the application applies any access change only under an approved policy. Preparation for reuse or repurposing, repurposing and remanufacturing each create a new passport linked to the original [1, Art. 77(7)]. After recycling, the passport ceases to exist [1]; any evidence kept after that point needs its own justification.

### C7. Evidence storage, ledger digests and retention

SQL and Blob Storage do not share a transaction, so the application uploads and verifies a file before recording its reference and hash, and reconciliation finds files left unreferenced by a failed write. Retention rules mean cleanup cannot assume that a stored file can be deleted. Ledger digests are kept in a container with a locked immutability policy, administered separately from database writers [11], [12]. Define retention by data class before enabling ledger or immutable storage: keep personal data and confidential narrative out of permanent ledger history, because deleting a current ledger row does not erase its history.

### C8. Threat model summary

Table C2. Threats that shape this architecture, summarized from the companion threat model [41].

| Threat (identifier in the threat model) | Controls in the prototype | Controls to add before production |
| --- | --- | --- |
| Instructions hidden in supplier documents steer an agent (T03) | A read-only tool scoped to each role's sections; a strict decision schema; agents hold no human decision rights | Prompt Shields document attack detection; AI red teaming |
| Forged, stale or replayed claims and approvals (T04, T07) | Ed25519 signatures checked against a party registry; expiry, revocation and replay checks; stale-task and version-conflict checks | Verifiable credentials through a standards-aligned partner connector; partner keys in Key Vault with rotation |
| A hold is bypassed, or evidence or history is altered (T08, T09) | Gates enforced in application code; separation of duties between the reviewer, compliance and policy-approver roles; ledger tables with digests in a separate storage account | Separation of duties for each person who holds several roles; a locked immutability policy with an approved retention period |
| Restricted data reaches the wrong reader (T02, T06) | Server-side field policy for each access group; telemetry that excludes evidence and prompts | Isolation between organizations; Microsoft Purview sensitivity labels |

### C9. Cost drivers

Platform cost changes little with volume and covers Fabric capacity, Azure SQL Database, Container Apps, the Durable Task Scheduler, Front Door, API Management where you use it, monitoring, the qualified electronic seal and partner connectivity. Per-battery cost covers passport versions, registry exchanges, evidence retention and public reads [1, Art. 78(b)]. Per-exception cost covers the model tokens of each agent run, reviewer minutes at a loaded hourly rate and rework. Integration, support, assurance and continuity also belong in the operating-cost view. Estimate each driver with the Azure pricing calculator [42].

Published Nov 23, 2026

Version 1.0

[advance analytics](https://techcommunity.microsoft.com/tag/advance%20analytics?nodeId=board%3AAzureArchitectureBlog)

[application](https://techcommunity.microsoft.com/tag/application?nodeId=board%3AAzureArchitectureBlog)

[apps & devops](https://techcommunity.microsoft.com/tag/apps%20%26%20devops?nodeId=board%3AAzureArchitectureBlog)

[artificial intelligence](https://techcommunity.microsoft.com/tag/artificial%20intelligence?nodeId=board%3AAzureArchitectureBlog)

[infrastructure](https://techcommunity.microsoft.com/tag/infrastructure?nodeId=board%3AAzureArchitectureBlog)

[well architected](https://techcommunity.microsoft.com/tag/well%20architected?nodeId=board%3AAzureArchitectureBlog)

[![Dominik Zemp's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/avatars/default/avatar-7.svg?image-dimensions=50x50)](https://techcommunity.microsoft.com/users/dominik%20zemp/187530)
