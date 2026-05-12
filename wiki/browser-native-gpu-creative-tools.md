# Browser-Native GPU Creative Tools

## Decision-useful summary
Browser-native creative tooling is credible for lightweight indie/artist workflows when GPU compute, local file handling, and real-time previews stay inside the browser. The NormalMap AI DEV.to case study describes a browser PBR texture generator using WebGL compute shaders, Three.js preview, no-plugin/no-upload workflow, and paid AI generation as the revenue layer. Treat it as a self-reported product build note, not a benchmark, but it is useful for HoneyDrunk when evaluating small, creator-facing tools that avoid heavyweight DCC installs. [source: raw/2026-05-12-rss-dev-to-gamedev-building-a-free-browser-based-pbr-texture-generator-no-.md]

## Claims
- NormalMap AI generates PBR texture sets from uploaded images in-browser, including Normal, Roughness, AO, Metallic, Height, and ORM maps. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-dev-to-gamedev-building-a-free-browser-based-pbr-texture-generator-no-.md]
- The reported technical pipeline uses WebGL compute shaders, Sobel-derived normal maps, local variance/high-frequency roughness, SSAO-style AO, multi-scale luminance height, and saturation/luminance metallic estimation. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-dev-to-gamedev-building-a-free-browser-based-pbr-texture-generator-no-.md]
- The real-time preview layer uses Three.js plus a custom HDRI loader and claims 60 fps rendering. confidence: 1 self-reported source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-dev-to-gamedev-building-a-free-browser-based-pbr-texture-generator-no-.md]
- The seamless texture workflow uses optimal offset search, min-cut seam repair, structural patch repair, low-frequency balance, and manual clone/healing brushes. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-dev-to-gamedev-building-a-free-browser-based-pbr-texture-generator-no-.md]
- The business model separates a broad free tier for non-AI PBR workflows from credit-based AI texture generation via Runware/Kie, with 5 free credits/day and paid plans from $19.90/month. confidence: 1 self-reported source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-dev-to-gamedev-building-a-free-browser-based-pbr-texture-generator-no-.md]

## Typed entities
- product/tool: NormalMap AI
- library/runtime: WebGL
- library/runtime: Three.js
- framework: Astro
- language: TypeScript
- backend/service: Supabase
- payments/service: Creem
- AI provider: Runware
- AI provider: Kie
- concept: PBR texture generation
- concept: normal map
- concept: roughness map
- concept: ambient occlusion map
- concept: metallic map
- concept: height map
- concept: ORM map
- algorithm: Sobel operator
- algorithm: min-cut seam repair
- algorithm: optimal offset search
- concept: browser-native GPU tooling

## Explicit relationships
- NormalMap AI uses WebGL and Three.js to provide browser-native texture generation and preview.
- Browser-native GPU tools depend-on client-side performance, privacy/no-upload posture, and compatibility across target browsers/devices.
- AI texture generation uses Runware/Kie and subsidizes the free non-AI PBR workflow.
- Seamless texture generation depends-on offset search, seam repair, patch repair, and manual touch-up.
- [[Unity 3D and Realtime VFX Patterns]] and technical-art workflows can use browser PBR generators as asset-prep/scouting tools, but production adoption depends-on quality and licensing validation.

## HoneyDrunk implications
- For quick art/VFX prototypes, browser-native PBR tools may reduce setup friction versus Substance/desktop workflows.
- Before using generated maps in production, validate tiling artifacts, color management, normal convention, export formats, license terms, and offline/privacy behavior.
- If HoneyDrunk builds creator tooling, keep the free/core workflow useful and monetize expensive AI generation or advanced workflows rather than gating basic utility.

## Confidence and quality notes
- Quality posture: useful as a product/architecture pattern; not enough to choose NormalMap AI or browser GPU tools without local quality/performance tests.
- Weak claims: performance, conversion, and “90% of use cases” are self-reported by the tool author.
- Privacy filter: no user-upload details copied; no credentials or unsafe PII present.
