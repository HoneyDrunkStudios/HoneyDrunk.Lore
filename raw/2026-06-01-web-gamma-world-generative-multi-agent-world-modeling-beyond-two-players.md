---
source: "https://research.nvidia.com/labs/sil/projects/gamma-world/"
title: "Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players"
author: "Fangfu Liu et al."
date_published: "2026-05-29"
date_clipped: "2026-06-01"
category: "AI / LLM Research & Tooling"
source_type: "web"
---

# Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

Source: https://research.nvidia.com/labs/sil/projects/gamma-world/

Gamma-World: 
Generative Multi-Agent World Modeling
Beyond Two Players 
Fangfu Liu 1,2* 
Kai He 1,3,4* 
Tianchang Shen 1 
Tianshi Cao 1 
Sanja Fidler 1,3,4 
Yueqi Duan 2 
Jun Gao 1 
Igor Gilitschenski 3,4† 
Zian Wang 1† 
Xuanchi Ren 1† 
1 NVIDIA 
2 Tsinghua University 
3 University of Toronto 
4 Vector Institute 
* Equal contribution. 
† Joint advising. 
Paper
Code
Citation 
TL;DR: γ-World is a generative multi-agent world model that supports independently controllable, permutation-symmetric agents via Simplex Rotary Agent Encoding and Sparse Hub Attention , achieving real-time 24 FPS rollouts and zero-shot generalization from two to four players.
γ-World 
γ-World interactively generates coherent future frames from multi-agent actions while preserving shared-world consistency, scaling from virtual games to real-world environments.
Gallery 
Overview 
Two-Agent Interaction 
Four-Agent Generalization 
Real-World Robotics 
γ-World Overview 
A comprehensive overview of γ-World: interactive multi-agent world generation across diverse scenes and configurations.
Two-Agent Interaction 
Qualitative results of two-agent interaction. Each agent is independently controllable while sharing the same evolving world.
Four-Agent Generalization 
Benefiting from the permutation-symmetric simplex agent encoding, γ-World generalizes from two to four players without additional training .
Real-World Robotics Coordination 
γ-World extends to real-world multi-robot coordination scenarios, demonstrating practical applicability beyond virtual environments.
Abstract 
World models for interactive video generation have largely focused on single-agent settings, where future observations are rolled out from a single action stream, user input, or controllable viewpoint. However, many simulated worlds are inherently populated: multiple players, robots, or embodied agents act simultaneously within a shared, evolving environment. Scaling world models to such settings requires a principled multi-agent design: agents should remain independently controllable, permutation-symmetric, and support efficient inference while maintaining consistency across time and perspectives.
In this paper, we present γ-World , a generative multi-agent world model for interactive simulation. γ-World introduces Simplex Rotary Agent Encoding , a parameter-free extension of 3D RoPE that represents agents as vertices of a regular simplex in rotary angle space. This gives each agent a distinct phase while making all agents permutation-equivalent, enabling scalable agent identity without learned per-slot identities or a fixed agent ordering.
To support efficient cross-agent interaction, we further propose Sparse Hub Attention , where learnable hub tokens mediate communication across agents, reducing cross-agent attention cost from quadratic to linear in the number of agents. Finally, we use a bidirectional multi-agent teacher to guide a block-causal student with distillation, after which the final causal model can use KV caching for streaming, achieving real-time action-responsive rollouts at 24 FPS .
Experiments in multiplayer virtual environments show that γ-World improves video fidelity, action controllability, and inter-agent consistency over slot-based and dense-attention baselines, while generalizing from two to four players without additional training.
Method 
Architecture overview. γ-World takes per-agent action streams and produces a shared, multi-view rollout. Two key designs make it scalable to many agents:
Simplex Rotary Agent Encoding 
A parameter-free extension of 3D RoPE that represents agents as vertices of a regular simplex in rotary angle space. Each agent receives a distinct phase while remaining permutation-equivalent , eliminating the need for learned per-slot identities or a fixed agent ordering.
Sparse Hub Attention 
Learnable hub tokens mediate communication across agents, reducing cross-agent attention cost from quadratic to linear in the number of agents — enabling efficient scaling to four or more agents.
Efficiency: Sparse Hub Attention 
Sparse Hub Attention scales linearly with the number of agents, while dense attention scales quadratically.
