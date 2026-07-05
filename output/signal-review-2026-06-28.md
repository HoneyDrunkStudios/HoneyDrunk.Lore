# Lore Daily News Blast - 2026-06-28

## Blast summary

- Send to Discord: yes
- Theme: Today's useful cluster is agent and MCP hardening, CI/runtime control, and container compliance evidence for the HoneyHub and NovOutbox lanes.
- Coverage: 15 saved public web sources and 0 fresh X posts reviewed

## Top stories

1. Simon Willison reports a large prompt-injection challenge failed to leak an AI assistant secret
   - Main points: A public challenge drew roughly 2,000 participants and about 6,000 attempts against an email-fed assistant without leaking the target secret. The useful point is encouraging model-side resistance, but the source is explicit that this does not make prompt-only defenses safe for irreversible production actions.
   - Source: Simon Willison
   - Source URL: https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/
   - HoneyDrunk angle: Good confidence boost for HoneyHub-style agent workflows, but deletes, deployments, credential use, payments, and external messaging still need execution-layer gates.

2. Docker lays out the next MCP security boundary
   - Main points: Docker frames MCP adoption as moving from direct host execution toward containerized servers, managed catalogs, and gateway mediation. The concrete risk list is useful: rug pulls from changed tool descriptions, tool shadowing, poisoned tool metadata, loose secrets, and uncontrolled egress.
   - Source: Docker Blog
   - Source URL: https://www.docker.com/blog/whats-next-for-mcp-security/
   - HoneyDrunk angle: Directly relevant to HoneyHub tool profiles: record server provenance, image digest, tool descriptions, network reach, and secret scope before trusting an MCP surface.

3. GitHub Actions now has first-class parallel steps
   - Main points: GitHub Actions added `background`, `wait`, `wait-all`, `cancel`, and `parallel` so independent work can run concurrently inside one job while keeping separate logs. This replaces fragile shell backgrounding for patterns like parallel builds, temporary services, and non-blocking telemetry uploads.
   - Source: GitHub Changelog
   - Source URL: https://github.blog/changelog/2026-06-25-actions-steps-can-now-be-run-in-parallel
   - HoneyDrunk angle: Useful for speeding CI, but only where build outputs, caches, ports, and environment state cannot race.

4. GitHub adds stronger hosted-runner controls
   - Main points: Organizations can now disable standard hosted-runner labels such as `ubuntu-latest`, and can put macOS runners into runner groups with access and concurrency limits. The release makes runner selection more governable, especially for costly or sensitive runner classes.
   - Source: GitHub Changelog
   - Source URL: https://github.blog/changelog/2026-06-25-more-control-over-your-github-hosted-runners
   - HoneyDrunk angle: Watch for HoneyDrunk CI policy: default labels are convenient, but named runner groups make cost and access intent explicit.

5. Docker explains why build-time SBOMs beat checkbox SBOMs
   - Main points: Docker argues that SBOM quality depends on completeness, accuracy, freshness, verifiability, and format compliance. The strongest recommendation is to generate SBOMs at build time and bind them to the image digest as attestations, while treating the SBOM generator itself as privileged build attack surface.
   - Source: Docker Blog
   - Source URL: https://www.docker.com/blog/sbom-generation-for-container-workflows/
   - HoneyDrunk angle: NovOutbox and any containerized beta surface should treat digest-bound SBOMs as release evidence, not loose files saved after the fact.

6. Docker summarizes the EU Cyber Resilience Act timeline for container teams
   - Main points: The source highlights 2026-09-11 for vulnerability and severe-incident reporting obligations and 2027-12-11 for full CRA enforcement. It also says commercial container images and runtimes distributed into the EU can fall under product-with-digital-elements obligations.
   - Source: Docker Blog
   - Source URL: https://www.docker.com/blog/eu-cyber-resilience-act-overview/
   - HoneyDrunk angle: Watch only until applicability is confirmed, but NovOutbox commercial packaging should not discover support-period, SBOM, or reporting expectations during an incident.

7. Azure Functions MCP extension is becoming a fuller remote tool surface
   - Main points: The extension now covers tools, resources, prompts, MCP Apps, structured content, rich content, explicit schemas, built-in auth, and On-Behalf-Of examples. Microsoft is signaling that serverless Functions can host production-shaped MCP servers rather than just demo tools.
   - Source: Azure SDK Blog
   - Source URL: https://devblogs.microsoft.com/azure-sdk/functions-mcp-updates-build-2026/
   - HoneyDrunk angle: Candidate for HoneyHub remote tools, but only with documented Entra/OBO scopes, schemas, observability, and per-tool capability review.

8. Azure Developer CLI adds stronger agent-operable deployment primitives
   - Main points: The May/June release train adds `azd tool` for prerequisite management and `azd exec` for command execution with the full `azd` environment, including Key Vault resolution. The notes also include important parallel-deploy fixes around ACR image contamination, correlation IDs, and build artifact races.
   - Source: Azure SDK Blog
   - Source URL: https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/
   - HoneyDrunk angle: Helpful for agent-run Azure workflows, but inherited secret context must be intentional, logged, and scoped.

9. Hugging Face shows one-command private vLLM endpoints on Jobs
   - Main points: Hugging Face Jobs can expose an OpenAI-compatible vLLM server with one command, token-gated access, per-second billing, and quick cleanup. The post positions Jobs for experiments, evals, and batch generation, while Inference Endpoints remain the production-oriented choice.
   - Source: Hugging Face Blog
   - Source URL: https://huggingface.co/blog/vllm-jobs
   - HoneyDrunk angle: Useful for HoneyHub eval experiments or model trials before committing to durable hosting, with budget and token handling called out up front.

10. A2A is framed as the agent-to-agent layer next to MCP
   - Main points: The A2A explainer positions MCP as agent-to-tool communication and A2A as agent-to-agent delegation, discovery, task lifecycle, streaming, artifacts, and push notifications. It is most useful as a vocabulary and boundary-setting piece, not as an implementation decision by itself.
   - Source: System Design Newsletter
   - Source URL: https://newsletter.systemdesign.one/p/agent-to-agent-protocol
   - HoneyDrunk angle: Keep HoneyHub diagrams clear: MCP tool servers and A2A-facing agents have different trust, auth, and audit requirements.

## Top X posts

- No fresh X posts available today. The X refresh did not produce new captured posts, so no stale or fabricated posts were included.

## Worth watching

- Thoughtworks' AI knowledge fabric article maps closely to the existing Lore direction: concise Markdown/JSON/YAML, ownership, freshness, and explicit "don'ts" for agents. https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/build-AI-knowledge-fabric-for-your-organization
- Miris' WebXR car configurator is a strong watch item for Curiosities-style interactive 3D: high-fidelity cross-device 3D without one cloud GPU per viewer is commercially interesting if the claims hold. https://80.lv/articles/miris-built-a-car-configurator-without-pixel-streaming-here-s-what-they-found/
- Crema's Temtem: Pioneers interview is useful game-production signal around genre blending, co-op/solo transitions, and community-backed alpha development. https://80.lv/articles/temtem-developing-massively-multiplayer-creature-collection-adventure/
- The alien-island vegetation breakdown is good technical-art reference for procedural variation, PCG scattering, SpeedTree/Substance workflows, and readable biome composition. https://80.lv/articles/setting-up-vegetation-for-alien-island-in-3d/

## Parked / low signal

- OWASP's agentic AI security landscape page is a useful pointer, but this capture is too thin to rank individual tools or make procurement decisions. https://genai.owasp.org/resource/ai-security-solutions-landscape-for-agentic-ai-q2-2026/
- The Azure `azd` release post is very broad; only the agent/deployment/security parts are worth carrying forward today. https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/
- The 80 Level vegetation article is craft-useful, but not urgent against HoneyHub, NovOutbox, or Curiosities unless an art pipeline spike is active. https://80.lv/articles/setting-up-vegetation-for-alien-island-in-3d/

## Review notes

- Files reviewed: latest saved web-source summary, latest X status, latest source-reflection summary, 15 fresh saved public sources, current focus, charter, and relevant context pages for security, MCP, CI, Azure, and container compliance.
- Blockers: Fresh X refresh failed because the local X command was unavailable; no posts were exported, so the X section is intentionally empty.
