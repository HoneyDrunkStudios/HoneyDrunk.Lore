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
