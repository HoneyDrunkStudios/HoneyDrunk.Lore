# Creative Automation and Firefly Services

## Decision-useful summary
Adobe Photoshop API v2 in Firefly Services is now a production-oriented creative automation surface for server-side Photoshop/Lightroom-style workflows. It matters to HoneyDrunk as a possible high-volume content pipeline option, not as a substitute for local art direction: v2 adds linked smart objects, larger files, UXP scripting, richer document metadata, action workflows, and flexible storage. [source: raw/2026-06-02-web-adobe-developer-adobe-photoshop-api-firefly-services.md]

## Claims
- Photoshop API v2 is generally available in Firefly Services and is positioned as the unified next-generation API surface for Photoshop and Lightroom-style workflows. confidence: 1 Adobe documentation source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-adobe-developer-adobe-photoshop-api-firefly-services.md]
- Photoshop API v2 raises the maximum file size from 2GB to 5GB and adds linked smart-object support so assets can be referenced instead of embedded, reducing PSD size growth and centralizing shared asset governance. confidence: 1 Adobe documentation source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-adobe-developer-adobe-photoshop-api-firefly-services.md]
- Photoshop API v2 supports UXP JavaScript scripting inside workflows, enabling custom logic such as copy fitting, dynamic text adjustments, automated recoloring/localization, print-specific adjustments, and brand/compliance rule enforcement. confidence: 1 Adobe documentation source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-adobe-developer-adobe-photoshop-api-firefly-services.md]
- Photoshop API v2 includes action workflows for Generative Fill, Generative Expand, customizable Adobe action files, runtime-generated outputs, artboard metadata, embedded smart-object extraction, richer layer/text/blend/layout metadata, ICC profile support, SVG/linked asset workflows, and improved error handling. confidence: 1 Adobe documentation source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-adobe-developer-adobe-photoshop-api-firefly-services.md]
- Photoshop API v1 reaches end of life on 2026-07-31; new integrations should target v2 and existing v1 workflows need migration planning. confidence: 1 Adobe documentation source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-adobe-developer-adobe-photoshop-api-firefly-services.md]

## Typed entities
- product/API: Adobe Photoshop API v2
- platform: Adobe Firefly Services
- deprecated API: Photoshop API v1
- date/decision: 2026-07-31 Photoshop API v1 end of life
- concept: linked smart object
- scripting runtime: UXP JavaScript
- action: Generative Fill
- action: Generative Expand
- metadata object: artboard
- metadata object: layer/text/blend/layout metadata
- color management: ICC profile

## Explicit relationships
- Photoshop API v2 supersedes Photoshop API v1 for new production integrations.
- Linked smart objects reduce file-size duplication and depend-on shared asset governance.
- UXP scripting complements fixed API endpoints by embedding business and brand logic into content workflows.
- Firefly Services uses REST-style APIs and Adobe I/O Events to support chained and event-driven creative automation.

## HoneyDrunk implications
- Consider Photoshop API v2 for templated asset variants, localized promotional images, cutouts, and repeatable brand-safe creative operations.
- Do not plan new work on Photoshop API v1 after this source; any inherited v1 automation needs migration before 2026-07-31.
- Treat generated/automated outputs as reviewable creative artifacts; API scalability does not remove art direction, licensing, or brand QA.

## Confidence and quality notes
- Quality posture: high for API capability and migration-date claims because the source is Adobe documentation; local feasibility still depends on Adobe account terms, costs, storage model, and pipeline needs.
- Privacy filter: no credentials or private project data were present in the source.

## 2026-06-20 compile additions: event-driven Photoshop API workflows

### Source-backed claims
- Adobe's workflow article demonstrates Photoshop/Lightroom-style API automation as an event-driven pipeline: a Dropbox folder trigger in Pipedream gets an input link, creates a temporary Dropbox upload URL, obtains an Adobe access token, calls the Lightroom AutoTone API, and writes the corrected output to a separate Dropbox folder. Source: `raw/2026-06-20-web-adobe-developer-blog-automating-image-workflows-with-the-photoshop-api.md`. confidence: 1 Adobe developer blog source, last-confirmed 2026-06-20.
- The source reinforces that production creative automation needs job submission, polling/status handling, output routing, error handling, and human QA decisions rather than blindly overwriting source assets. Source: `raw/2026-06-20-web-adobe-developer-blog-automating-image-workflows-with-the-photoshop-api.md`. confidence: 1 source, last-confirmed 2026-06-20.

### Typed entities
- API: Photoshop API
- API: Lightroom AutoTone API
- platform: Pipedream
- platform: Dropbox
- concept: event-driven creative workflow
- auth flow: Adobe access token / JWT exchange
- artifact: temporary upload URL

### Explicit relationships
- Pipedream uses Dropbox triggers to start Photoshop API workflows.
- Photoshop/Lightroom API jobs depend-on input and output URLs, token exchange, asynchronous job status, and post-processing policy.
- Automated image correction complements, but does not supersede, human visual review and source-asset retention.

### HoneyDrunk implications
- For marketing or screenshot pipelines, preserve originals and write generated variants to separate folders with review status.
- Treat storage links and Adobe credentials as sensitive workflow infrastructure; agents should receive scoped handles, not durable secrets.

### Quality notes
- Adobe source is an older developer example clipped on 2026-06-20. Use it as workflow-shape evidence, while checking current Photoshop/Firefly Services docs before implementation.
