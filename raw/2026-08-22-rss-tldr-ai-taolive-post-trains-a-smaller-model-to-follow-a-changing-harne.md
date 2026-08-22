---
source: "https://arxiv.org/abs/2608.15763"
title: "TaoLive post-trains a smaller model to follow a changing harness (11 minute read)"
author: "unknown"
date_published: "2026-08-21"
date_clipped: "2026-08-22"
category: "AI / LLM Research & Tooling"
source_type: "rss"
discovered_via: "https://tldr.tech/ai/2026-08-21"
source_role: "primary-via-tldr"
---

# TaoLive post-trains a smaller model to follow a changing harness (11 minute read)

Source: https://arxiv.org/abs/2608.15763

-->
Computer Science > Computation and Language
arXiv:2608.15763 (cs)
[Submitted on 16 Aug 2026]
Title: TaoLive Digital Avatar Agent Technical Report: Training Agents to Evolve with Their Harness
Authors: TaoLive AIGC LLM Team : Yuhan Sun , Wenhao Lin , Yongdong Luo , Yibo Hu , Meiguang Jin , Junfeng Ma , Weihang Pan , Jiaxin Zhao , Zulong Chen View a PDF of the paper titled TaoLive Digital Avatar Agent Technical Report: Training Agents to Evolve with Their Harness, by TaoLive AIGC LLM Team: Yuhan Sun and 8 other authors
View PDF
HTML (experimental)
Abstract: AI-powered digital-avatar streamers in live e-commerce must answer product questions, engage viewers, and execute changing business strategies in real time. This requires low latency, factual and effective replies, and rapid adaptation to updated campaign, compliance, and style requirements. We develop an evolvable Harness that decouples Skills, Hooks, system prompts, and tools from model weights, allowing runtime behavior to change without retraining. However, Harness evolution creates a moving execution environment: compact models fine-tuned on one configuration may memorize names, schemas, and prompt templates rather than follow the Harness currently provided, while stronger zero-shot models are too slow for real-time use. We address this tension with Harness-Aware Training (HAT), which makes Harness states part of the training distribution. HAT applies task-preserving Harness-State Augmentation (HSA) to Skills, tool schemas, prompt structures, and interaction constraints, and comprises three stages: HSA-based supervised fine-tuning, general on-policy distillation to recover general capabilities, and HSA-based agentic reinforcement learning in a production-informed live-room simulator. Across four evaluation sets with more than 4,500 cases, our compact 35B model scores 94.8 on real-world Live-Stream QA, versus 80.3 for the base model and 93.0 for the strongest evaluated general LLM, while scoring 94.6 on Harness-Variant QA and retaining 83.5 on IFEval. By contrast, fixed-Harness SFT reduces IFEval by 7.7 points. In a controlled complete-agent replay on one NVIDIA H20 GPU with MTP enabled, the system achieves 3.407 s P50 and 8.114 s P95 latency. These results show that HAT produces a latency-feasible compact agent that remains effective under evaluated Harness changes without sacrificing general instruction following.
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2608.15763 [cs.CL]
(or
arXiv:2608.15763v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2608.15763
Focus to learn more
arXiv-issued DOI via DataCite (pending registration)
Submission history From: Yuhan Sun [ view email ]
[v1]
Sun, 16 Aug 2026 14:32:56 UTC (1,218 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled TaoLive Digital Avatar Agent Technical Report: Training Agents to Evolve with Their Harness, by TaoLive AIGC LLM Team: Yuhan Sun and 8 other authors View PDF HTML (experimental) TeX Source
view license
Current browse context:
cs.CL
< prev
|
next >
new
|
recent
| 2026-08
Change to browse by:
cs
References & Citations
NASA ADS Google Scholar
Semantic Scholar
export BibTeX citation
Loading...
BibTeX formatted citation
×
loading...
Data provided by:
Bookmark
Bibliographic Tools
Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer ( What is the Explorer? )
Connected Papers Toggle
Connected Papers ( What is Connected Papers? )
Litmaps Toggle
Litmaps ( What is Litmaps? )
scite.ai Toggle
scite Smart Citations ( What are Smart Citations? )
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv ( What is alphaXiv? )
Links to Code Toggle
CatalyzeX Code Finder for Papers ( What is CatalyzeX? )
DagsHub Toggle
DagsHub ( What is DagsHub? )
GotitPub Toggle
Gotit.pub ( What is GotitPub? )
Huggingface Toggle
Hugging Face ( What is Huggingface? )
ScienceCast Toggle
ScienceCast ( What is ScienceCast? )
Demos
Demos
Replicate Toggle
Replicate ( What is Replicate? )
Spaces Toggle
Hugging Face Spaces ( What is Spaces? )
Spaces Toggle
TXYZ.AI ( What is TXYZ.AI? )
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower ( What are Influence Flowers? )
Core recommender toggle
CORE Recommender ( What is CORE? )
Author
Venue
Institution
Topic
About arXivLabs
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .
Which authors of this paper are endorsers? |
Disable MathJax ( What is MathJax? )
