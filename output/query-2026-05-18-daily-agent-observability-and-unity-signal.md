# Daily agent observability and Unity architecture signal — 2026-05-18

## Durable facts crystallized
- OpenTelemetry GenAI semantic conventions provide a provider-neutral way to trace model calls, token usage, finish reasons, tool calls, and optionally prompt/tool content. Content capture is privacy-sensitive and should be opt-in. [source: raw/2026-05-18-rss-opentelemetry-blog-inside-the-llm-call-genai-observability-with-opente.md; wiki: [[opentelemetry-genai-observability-and-ecosystem]]]
- Code quality in the LLM era increasingly means explicit domain vocabulary, bounded contexts, tests, types, and invariants that humans and LLMs can share; otherwise teams accumulate cognitive debt. [source: raw/2026-05-18-rss-martin-fowler-what-is-code.md; wiki: [[ai-assisted-software-practice]]]
- Albion Online's cross-platform Unity MMO architecture depends on a single project, platform-specific UI/input profiles, simulation/visualization separation, CI validation, local full-stack dev loops, and weakest-device performance baselines. [source: raw/2026-05-18-rss-unity-blog-architecting-albion-online-how-sandbox-interactive-built-a-.md; wiki: [[unity-3d-and-realtime-vfx-patterns]]]
- The Rundown AI 2026-05-18 captures were not promoted as AI-platform facts because raw body content was missing/noisy and public client config had to be privacy-filtered. [sources: raw/2026-05-18-web-the-rundown-ai-android-enters-its-gemini-intelligence-era.md; raw/2026-05-18-web-the-rundown-ai-the-enterprise-shift-openai-saw-coming.md; wiki: [[browser-snapshot-source-quality]]]

## Decision implications
- Put OTel/GenAI telemetry on the HoneyDrunk agent-harness roadmap, but separate metadata telemetry from prompt/tool content capture.
- Prefer deterministic workflow code with bounded LLM calls over autonomous runtime agents when orchestration is known.
- If Unity enters a multiplayer/cross-platform HoneyDrunk prototype, define simulation authority and visualization ownership early.

## Confidence
Decision-usable for architecture scouting; implementation still requires local validation against current tool versions and HoneyDrunk privacy constraints.
