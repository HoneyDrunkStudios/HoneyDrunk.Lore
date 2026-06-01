# Mobile AI and React Native 2026

## Decision-useful summary
React Native AI coding support is becoming specialized. Callstack's Apex source argues that React Native work has enough framework, native-module, library, and cross-platform nuance that a domain-specialized model can be useful even when general coding models improve. Treat Apex as a scout signal for model specialization and local evals, not as proof that HoneyDrunk should switch mobile model defaults. [source: raw/2026-06-01-web-introducing-apex-a-fast-specialized-model-for-react-native.md]

## Claims
- Apex is a focused React Native coding model based on Gemma 4, trained with supervised fine-tuning and GRPO after proof-of-concept experiments on other bases such as Devstral and Qwen. confidence: 1 vendor/source-author source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-introducing-apex-a-fast-specialized-model-for-react-native.md]
- Callstack says Apex is evaluated against React Native Evals and is meant to improve the React Native performance-to-cost ratio relative to larger general models within that narrow domain. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-introducing-apex-a-fast-specialized-model-for-react-native.md]
- The training data is described as curated from recent GitHub repositories and React Native ecosystem work rather than a random broad web scrape. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-introducing-apex-a-fast-specialized-model-for-react-native.md]

## Typed entities
- model: Apex
- company: Callstack
- framework: React Native
- benchmark: React Native Evals
- base model: Gemma 4
- model family: Devstral
- model family: Qwen
- training method: supervised fine-tuning / SFT
- training method: Group Relative Policy Optimization / GRPO

## Explicit relationships
- Apex depends-on React Native-specific training data and evaluation rather than broad coding benchmarks alone.
- Domain specialization complements [[edge-ai-and-ai-infrastructure-2026]] model-routing decisions.
- React Native agent workflows depend-on native module, platform constraint, and ecosystem-library knowledge.

## HoneyDrunk implications
- If HoneyDrunk starts React Native work, create a small React Native eval set before adopting Apex or any routing default.
- Track domain-specialized models as cost-control candidates, especially for repetitive framework-specific tasks.

## Confidence and quality notes
- Quality posture: useful scouting signal, but vendor-authored and requires local benchmark validation.
- Privacy filter: no private repository data copied; public model/company/framework names retained.
