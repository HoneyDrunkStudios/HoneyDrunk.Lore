# Gaps

Questions the wiki cannot currently answer. Populated by the Query operation when synthesis falls short, and by the Lint operation when entities are referenced but lack a backing page.

## Entry format

```
- <question or missing entity> - surfaced YYYY-MM-DD - context: <where it came up>
```

## Gaps

- How can OpenClaw's browser clipper reliably extract Discord announcement message bodies instead of UI/accessibility scaffolding? - surfaced 2026-05-05 - context: 20 Discord announcement snapshots across 2026-05-04 and 2026-05-05 were low-yield; reinforced 2026-05-06 by 18 additional low-yield Discord captures and 2026-05-07 by 10 more low-yield Discord captures.
- How can OpenClaw's X-list sourcing extract actual post text/URLs from the monitored list? - surfaced 2026-05-05 - context: X list snapshots for 2026-05-03 through 2026-05-05 mostly captured navigation/UI scaffolding; reinforced 2026-05-06 by two additional low-yield X captures and 2026-05-07 by another low-yield X capture.
- Why did the 2026-05-06 browser sourcing pass create duplicate Discord/X raw captures for several monitored surfaces, and should sourcing be made idempotent by source/date/channel? - surfaced 2026-05-06 - context: duplicate `-2` raw files for Anthropic/Claude, Aspire, Gemini, Hugging Face, Microsoft Community, Microsoft Foundry, .NET/C#, OpenAI Developer, and X list snapshots.
- Which HoneyDrunk services currently validate or store GitHub App installation tokens with fixed-length assumptions? - surfaced 2026-05-05 - context: GitHub App installation token format rollout to longer variable `ghs_APPID_JWT` tokens.
- What is the real cost impact of GitHub Copilot code review consuming Actions minutes after 2026-06-01 for HoneyDrunk repos? - surfaced 2026-05-05 - context: GitHub Copilot code review billing change.
- Should HoneyDrunk use Unity, Godot, WebXR/Babylon.js, or hybrid tooling for mobile/browser/interactive-3D prototypes? - surfaced 2026-05-05 - context: Godot mobile/4.7 updates, Unity Studio/VFX/rendering sources, and WebXR-vs-Unity-WebGL benchmark provide direction but not project-specific selection criteria.
- Can HoneyDrunk reproduce the WebXR/Babylon.js vs Unity WebGL vs Unreal HTML5 benchmark on its actual target devices and representative scenes? - surfaced 2026-05-06 - context: single-source DEV.to benchmark is useful but not procurement-grade evidence.
- Which AI scene-generation tools from the Genie-3-alternatives list are actually available, licensable, affordable, and workflow-compatible for HoneyDrunk prototypes? - surfaced 2026-05-06 - context: DEV.to list names many tools but does not validate HoneyDrunk-specific constraints.
- How can Lore RSS/forum ingestion strip Polycount forum JavaScript/theme scaffolding and retain only JSON-LD/schema discussion fields plus authored post text? - surfaced 2026-05-07 - context: three Polycount captures had usable schema snippets but large noisy forum scaffolding.
- Which automated gates should HoneyDrunk promote from recurring AI-code review findings into analyzers/lints/build checks? - surfaced 2026-05-07 - context: CivicSurvival case study reinforces that repeated AI mistakes should become enforced checks, not memory-only rules.
- Can HoneyDrunk validate AI-assisted animation pipelines (HY-Motion/Blender/UE5 retargeting or equivalents) on representative character rigs before relying on them for production iteration? - surfaced 2026-05-07 - context: MagicknessT dev log is useful but single-source/self-reported.
