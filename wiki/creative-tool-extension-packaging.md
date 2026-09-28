# Creative Tool Extension Packaging

## Decision-useful summary

Creative-tool extensions need explicit package manifests that describe files, install destinations, and host compatibility. The Adobe CEP/MXI article is old but still useful as a packaging-pattern reference: package structure and manifest instructions must agree, and ordinary assets should be installed through declared destinations rather than ad hoc copying.

## Source-backed claims

- Adobe's 2019 Creative Cloud extension packaging article says custom package contents and install locations are configured through an `.mxi` XML manifest. confidence: 1 old Adobe developer source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-adobe-developer-blog-how-to-customize-your-adobe-creative-cloud-extens.md]
- The article says the actual package folder structure must match the `.mxi` file, which can declare author, description, UI access, license text, product compatibility, and file-install instructions. confidence: 1 source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-adobe-developer-blog-how-to-customize-your-adobe-creative-cloud-extens.md]
- The example distinguishes CEP extension packages (`csxs`) from native plugins and ordinary files, with ordinary files able to use destination path tokens such as a downloads folder. confidence: 1 source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-adobe-developer-blog-how-to-customize-your-adobe-creative-cloud-extens.md]

## Typed entities

- platform: Adobe Creative Cloud
- extension runtime: CEP
- package format: ZXP
- manifest format: MXI
- file type: `csxs`
- file type: `plugin`
- file type: `ordinary`

## Explicit relationships

- Extension installation depends-on manifest/package-structure agreement.
- Host compatibility depends-on declared products and minimum versions.
- Ordinary asset installation complements panel/plugin installation but should be represented as manifest-controlled file entries.

## HoneyDrunk implications

- If HoneyDrunk packages Adobe/creator-tool extensions, capture install destinations, product compatibility, license display, and bundled assets in a manifest-reviewed checklist.
- Before adopting CEP/MXI guidance, verify whether the target Adobe host now prefers UXP or another current extension model.

## Confidence and quality notes

- Quality posture: low-to-medium. The source is official but from 2019, so it is a packaging-pattern reference rather than current Adobe platform guidance.
- Privacy filter: no secrets or private install paths were promoted.


## 2026-09-28: Plugin scaffolds need packaged-install and host-compatibility verification

### Typed entities

person: Justin Taylor; project: Bolt UXP; project: Bolt Express; project: Adobe Premiere; library: Vite; concept: typed sandbox messaging; concept: packaged installation.

### Claims and evidence

- Taylor describes Bolt UXP 1.3 adding asynchronous command execution, source-level debugging, centralized error handling, Premiere helpers, and packaged-install test scripts. External tools can execute without blocking the plugin interface. confidence: 1 source, last-confirmed 2026-09-28 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-28-web-adobe-bolt-plugin-development-workflow.md)
- Bolt Express 1.2 adds sandbox reload improvements and typed messaging in both directions between frontend and sandbox. Both frameworks retain access to underlying platform APIs and Vite configuration rather than making those extension points inaccessible. confidence: 1 source, last-confirmed 2026-09-28 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-28-web-adobe-bolt-plugin-development-workflow.md)

### Explicit relationships

Plugin delivery uses packaging tests and debug visibility; compatibility depends-on host APIs and versions. Typed messaging connects the frontend and sandbox.

### Decision and quality notes

August 18 author report, not compatibility certification. Flagged future-host claims: an unresolved editorial timeline note leaves additional integrations unconfirmed. The old CEP/MXI page content remains historical guidance for a different extension model, not a contradictory UXP contract. Source-specific claims remain provisional single-source evidence; related accounts and derived queries add no independent confirmation. Open question: Which Adobe host versions, external-command failure paths, typed messages, debug workflows, and packaged-install tests qualify a Bolt scaffold for HoneyDrunk creator-tool automation? See [[indexes/gaps]].


## 2026-09-28: Premiere UXP lint rules expose lock and transaction scope errors

### Typed entities

person: Cameron Legleiter; project: Adobe Premiere UXP; project: ESLint; concept: lock callback; concept: transaction scope; concept: undo label.

### Claims and evidence

- Adobe describes an initial ESLint rule set checking action construction and transaction operations within the expected lock/transaction callbacks, including asynchronous work and action objects escaping synchronous bounded scopes. confidence: 1 source, last-confirmed 2026-09-28 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-28-web-premiere-uxp-transaction-linting.md)
- Additional warnings encourage meaningful undo labels and the recommended lock wrapper. The article associates these mistakes with broken undo, corrupted state, or intermittent crashes; configurable severity and limited rule scope leave both false positives and missed patterns to review. confidence: 1 source, last-confirmed 2026-09-28 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-28-web-premiere-uxp-transaction-linting.md)

### Explicit relationships

Domain-specific linting uses API scope contracts; plugin correctness depends-on host execution and undo tests as well as static checks. See [[api-testing-and-verification]].

### Decision and quality notes

August 19 vendor description of an initial rule set. A clean lint run is not proof of correct transactions or all plugin behavior. Asynchronous external commands in Bolt and synchronous Premiere transaction callbacks concern different scopes and do not contradict each other. Source-specific claims remain provisional single-source evidence; related accounts and derived queries add no independent confirmation. Open question: Which Premiere lock, transaction, escaping-action, async-callback, and undo tests complement configurable lint rules for a HoneyDrunk plugin? See [[indexes/gaps]].
