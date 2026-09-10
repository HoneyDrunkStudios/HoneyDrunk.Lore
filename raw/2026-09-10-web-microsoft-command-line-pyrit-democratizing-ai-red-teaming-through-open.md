---
source: "https://commandline.microsoft.com/pyrit-python-risk-identification-tool-ai-red-teaming-subject-matter-experts/"
title: "PyRIT: Democratizing AI red teaming through open-source tooling"
author: "Richard Lundeen, Roman Lutz"
date_published: "2026-09-10"
date_clipped: "2026-09-10"
category: "Security & Ethical Hacking"
source_type: "web"
---

# PyRIT: Democratizing AI red teaming through open-source tooling

Source: https://commandline.microsoft.com/pyrit-python-risk-identification-tool-ai-red-teaming-subject-matter-experts/

Open Source
Share
in
r
x
f
PyRIT: Democratizing AI red teaming through open-source tooling
PyRIT: Democratizing AI red teaming through open-source tooling
Learn how the Python Risk Identification Tool for generative AI evolved over time to open up AI red teaming to subject matter experts from virtually any domain.
By Richard Lundeen Principal Software Engineering Manager, Microsoft and Roman Lutz Responsible AI Engineering Lead, Microsoft
2026.09.10
A practical framework for identifying risks in generative AI systems,  PyRIT  (Python Risk Identification Tool) has matured since its launch in early 2024 through sustained use by AI red teams, developers, and domain experts working across a wide range of applications and threat models. That real-world pressure has shaped its evolution, clarifying where standardization was needed, where workflows needed to scale, and where access needed to expand. The result is a toolkit that is more complete, more structured, and more broadly usable, while remaining grounded in its original purpose.
Since its release, the creators and users of PyRIT have lived through many shifts in how organizations are approaching AI security. PyRIT is now a toolkit that supports repeatable, measurable, and collaborative red teaming. It enables teams to move from isolated, one-off exercises to structured assessments that can be run consistently over time. Just as importantly, it brings more contributors into the process, allowing the subject matter expertise required to evaluate risk to be applied more directly and at scale.
That evolution is detailed in a new white paper from our team, which demonstrates the framework’s progression from a research prototype into a production-grade platform used to red team hundreds of generative AI products and services. The paper also outlines the architectural principles behind PyRIT’s extensibility, multimodal support, and practitioner-focused design, offering a deeper look at how the project aims to make rigorous AI red teaming accessible to a broader community of security professionals, researchers, and domain experts.
How PyRIT has evolved
Instead of a single entry point, PyRIT now supports four:
A graphical user web-based interface ( CoPyRIT )
A scanner command line interface
The underlying Python framework
An agent test framework ( RAMPART )
CoPyrit GUI walkthrough.
Scanner CLI walkthrough.
Each of these reflects the same core capability—testing AI systems—but applied in different ways depending on the user. The GUI lets people interact directly with a system, branch conversations, and track findings without writing code. The scanner enables teams to run predefined batteries of tests in a single command, which is useful for repeatable assessments and integration into CI/CD pipelines. And the framework remains for engineers who want to build custom attacks or extend the system.
These additions were driven by how PyRIT was actually being used. Early adoption showed that one interface wasn’t enough, and we’ve seen that users often combine the available entry points. A team might run large-scale scans through the CLI while simultaneously exploring edge cases in the GUI. Security engineers needed automation and integration, while domain experts needed a way to participate without writing Python. Rather than forcing a single workflow, PyRIT evolved into a system where multiple entry points can be used together, depending on the task, while maintaining a shared foundation.
At the same time, the underlying system has become more structured and consistent. Testing is no longer centered on one-off scripts tied to individual objectives. Instead, PyRIT supports standardized, repeatable test runs that can be executed, compared, and reproduced over time. This matters in practice because repeatable measurement, not one-off detection, is what lets teams validate a risk and act on it with confidence.
Improvements since launch
As PyRIT has matured, several capabilities have become stronger and more reliable through iteration and use. One of the most visible improvements is accessibility. Domain experts who understand risk but don’t write code can now contribute directly through the GUI, which changes how teams approach testing and broadens the range of issues that surface. At the same time, engineers and platform teams can automate testing through the scanner and integrate it into their pipelines, allowing assessments to run continuously rather than as one-time exercises.
The PyRIT system also supports a broader range of targets. It can work with OpenAI-compatible endpoints, custom HTTP and WebSocket services, browser-based applications, and multimodal systems that include text, image, audio, and video inputs. This reflects how AI systems are actually built today, where interactions aren’t limited to a single modality or interface. Compatibility improvements reduce the overhead of getting started and allow teams to spend more time testing behavior instead of configuring connections.
Evaluation has also become more measurable since PyRIT’s launch. Rather than relying on assumptions about scoring quality, PyRIT enables comparison against human ground truth, which allows teams to assess how accurate automated judgments are. This is important for building confidence in results, especially when testing is scaled across many scenarios. In addition, PyRIT can adapt its techniques dynamically, selecting approaches that are more effective based on prior runs, which helps surface issues more efficiently without requiring users to tune every parameter.
What PyRIT enables
Case study: Building reproducible AI red teaming with PyRIT
Reproducibility can be difficult for modern AI red teaming, due to the probabilistic nature of generative AI models. Many assessments still rely on one-off prompts, screenshots, and manually documented findings, making it difficult to understand coverage, reproduce results, or demonstrate risk reduction over time.  Volkan Kutal , a Berlin-based AI red team engineer focused on regulated enterprise environments, has built his work around addressing that gap. Through his contributions to both PyRIT and the  OWASP GenAI Security Project , as well as his work with financial-sector clients, he focuses on making adversarial testing of LLMs and agentic systems repeatable, auditable, and tied to concrete security objectives rather than isolated findings.
For Kutal, PyRIT functions as the execution layer for AI red teaming engagements. It automates multi-turn attacks, scoring, and evidence collection while maintaining a detailed record of every conversation, scoring decision, and attack outcome. This allows findings to be traced back to exact interactions rather than screenshots or analyst notes. PyRIT has enabled him to scale testing without losing transparency, evaluate and compare scoring approaches against known ground truth, and continuously re-run assessments as models and applications change. As a result, more of this red teamer’s effort can be focused on threat modeling, attack design, and interpreting results rather than building and maintaining testing infrastructure.
The broader impact has been a shift from finding individual vulnerabilities to measuring security coverage. Kutal uses PyRIT’s data model to map objectives against frameworks like the OWASP Top 10 for Agentic Applications 2026 and regulatory requirements, allowing him to identify not only what risks were found but which threat classes were and were not tested. That coverage-based view has surfaced gaps that would have been easy to miss when focused solely on successful attack chains. In practice, this helps organizations treat AI red teaming as an ongoing security discipline tied to design reviews, release decisions, and risk governance rather than a one-time assessment performed immediately before deployment.
Case study: Advancing AI jailbreak testing with PyRIT-powered evaluation framework
Jailbreak testing faces a coverage problem. Security teams can measure a model against a handful of attack prompts, but demonstrating that those tests meaningfully represent the broader jailbreak landscape is far more difficult.  MLCommons , an independent AI engineering consortium known for its benchmarking work across industry and academia, is addressing this challenge through the development of a jailbreak benchmark designed to evaluate model resilience against a continuously evolving set of attacks drawn from published research, practitioner findings, and community contributions. Rather than inventing new attack techniques, MLCommons focuses on curating, classifying, and implementing representative attacks from the existing body of knowledge.
A key component of this effort is the MLCommons  Jailbreak Taxonomy , which organizes the attack space into a structured framework that can be used to evaluate coverage and compare results over time. To operationalize many of these attacks, MLCommons uses PyRIT’s attack libraries and prompt conversion capabilities as an implementation framework. This allows the benchmark to efficiently incorporate a wide range of jailbreak techniques while maintaining consistency in how attacks are executed and evaluated. The goal is not simply to collect prompts, but to create a repeatable methodology for assessing how models respond to distinct classes of adversarial behavior.
Today, the benchmark focuses primarily on single-turn attacks, providing a foundation for measuring model resilience across a broad spectrum of known jailbreak techniques. Looking ahead, MLCommons plans to extend that work into more sophisticated multi-turn and composite attack scenarios. PyRIT’s common architecture provides a path for implementing those more complex evaluations without creating an entirely new testing framework. The result is a benchmarking effort that emphasizes coverage, repeatability, and comparability, helping organizations understand not only whether a model can be jailbroken, but how thoroughly it has been tested against the attack techniques documented in the broader AI security community.
More about the “why”
Today, PyRIT is used by a broader set of practitioners than at launch, from security engineers and developers to domain experts. AI red teams and security engineers rely on it for both automated and human-led assessments. Developers use it to build and extend testing capabilities within their own systems. Domain experts, from legal to cybersecurity to policy, can now directly contribute to identifying risk without needing to translate their expertise into code.
What connects these groups is responsibility for the safety and security of AI systems. PyRIT’s evolution reflects the reality that effective red teaming depends on multiple perspectives. By supporting different workflows on top of a shared system, PyRIT allows those perspectives to be applied more consistently and at scale.
What’s next
As AI systems continue to evolve toward more complex, agentic behavior, the need for structured and repeatable testing increases. PyRIT is positioned as the testing layer within that ecosystem: a system designed to probe behavior, surface risk, and produce results that can be validated and reproduced. While other tools and systems can build on top of it, the focus remains on the mechanics of testing itself.
Rigorous AI red teaming shouldn’t depend on a single skill set. PyRIT allows anyone responsible for an AI application to run structured assessments, scale testing across scenarios, and generate results they can trust.
Download the white paper
Share
in
r
x
f
PyRIT: Democratizing AI red teaming through open-source tooling
Next Stop
Your agent’s guardrails have a bypass
Open Source
Agents are moving into production faster than the governance around them. Today’s controls are framework-specific, mostly observe-only, and fail open when they crash. To help address this, we created Agent Hooks: an open, framework-neutral governance contract with conformance testing on both sides. What follows is the contract and the story of proving “deny means deny” inside a real framework core.
[ read ]
August 27, 2026
How we built ThinkingBox to measure whether agents finish the job
Open Source
ThinkingBox separates the execution framework from the benchmark package. This split lets builders update the harness and benchmark independently.
[ read ]
August 19, 2026
