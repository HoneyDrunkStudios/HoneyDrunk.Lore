---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/operating-model-enterprise-ai-agent-reliability"
title: "An operating model for enterprise AI agent reliability"
author: "unknown"
date_published: "2026-08-14"
date_clipped: "2026-08-21"
category: "Software Architecture"
source_type: "rss"
---

# An operating model for enterprise AI agent reliability

Source: https://www.thoughtworks.com/insights/blog/generative-ai/operating-model-enterprise-ai-agent-reliability

An operating model for enterprise AI agent reliability
Blogs
Back
Blogs
Back
Close
Generative AI
Blog
By
Arun Srinivasan
and
Zichuan Xiong
Published: August 14, 2026
Agentic AI is becoming the leading use case in enterprise AI adoption, and their reliability now decides whether that adoption succeeds. But these agents don't always fail in obvious ways: an agent can generate valid SQL, complete a query successfully and return figures that appear reasonable while still misinterpreting the original request.
Because enterprise AI agents cannot rely on evaluation alone, we propose a comprehensive operating model that guardrails reliability at every layer.
An agent failure that looked like success
We have a good example of the challenge of agents. A healthcare analytics platform we were working with allowed insurance analysts to query provider performance and claims data using natural language. One clinical reviewer asked the agent:
"Show me readmission rates for Medicare Advantage members with CHF (congestive heart failure) diagnoses since January 2024."
The agent returned a number that looked reasonable. However, the reviewer was able to flag three mistakes:
It included both Medicare Advantage and Original Medicare members.
It used an outdated ICD-10 grouping that omitted newly added CHF codes.
It interpreted the date range as starting one year earlier than requested.
Our end-to-end evaluation missed all three, because the query ran and the output looked plausible.
Tracing the request, we found failures across two layers owned by different teams. The semantic layer held stale clinical definitions and lacked the metadata to separate Medicare Advantage from fee-for-service plans.
Each error was plausible taken on their own; no final-output check caught their combined effect. This wasn't a model hallucination, it was a system governance failure. An end-to-end evaluation that checks only execution success or final-answer plausibility can miss semantic failures introduced earlier in the pipeline. That is why the query passed evaluation and still produced a wrong answer. A final answer can be correct for the wrong reasons, or wrong even when every stage reports success.
Reliability has to be tested at the same level where failures occur, not just at the finish line. This is why there's such a clear case for an operating model that's focused on agent reliability.
The operating model: How the components fit together
Reliability is a systemic engineering problem. It requires a layered approach, tested at the level where failures occur. The approach has a few core components, as the image below illustrates.
Reliability ladder: The reliability ladder defines the layers where truth can break down: terminology, routing, agent intent, semantic context, execution, result. Each layer is a separate governance boundary and can fail independently. Truth contracts: Each layer hosts one or more of what we call truth contracts. A truth contract states what must be true at that point, defining the requirement, measurement, tolerance, owner and enforcement action. Contract tests: These verify truth contracts. A contract that cannot be verified is only documentation, so every contract needs executable tests covering positive cases, ambiguity, boundaries and regressions. Failure taxonomy: Truth contracts map to a failure taxonomy. A failure code, assigned during design, classifies each violation by layer, owner, severity and expected response. The taxonomy is the shared registry of these codes. Contract triggers: They activate truth contracts. They sit outside any single contract and determine when to rerun tests, review contracts or add regression coverage, on a system change, a definition change or a production failure.
The reliability ladder
The reliability ladder is the structural model mitigating reliability risks at each level. It breaks the path from a natural-language request to a business result into independently governable layers, so each risk can be guarded against where it actually occurs.
For the CHF readmission request, the ladder looks like this:
Layer
Reliability risk
Guardrail in the case of CHF use case
Terminology
Definitions go stale or incomplete.
The CHF grouper must reference the approved CMS revision and include every applicable ICD-10-CM code..
Routing
The request reaches the wrong domain.
The request must route to the Medicare readmission semantic view or ask the user for clarification.
Agent intent
The interpretation drops or misreads a constraint.
“Medicare Advantage” must resolve to plan_type = 'MA', while 'since January 2024' must resolve to the correct start date.
Semantic context
Metadata fails to distinguish key business concepts.
The plan type dimension must define Medicare Advantage and fee-for-service as distinct values.
Execution
Generated SQL drops a constraint.
The generated SQL must preserve the requested population, diagnosis and date constraints.
Result
Output looks plausible but is wrong.
The query must return the expected result across representative data and important boundary cases.
Expand table
Collapse table
Each layer is a separate governance boundary that can fail independently, often under a different owner, which is exactly what happened in the CHF example: the terminology layer held a stale grouper, and the semantic context layer lacked the metadata to separate plan types.
The ladder does not define every guardrail or response, it tells us where risks live. Once teams know where truth can fail, they can define what each layer must preserve.
Truth contracts
As the reliability ladder names risks, a truth contract details the mitigation: an explicit, testable statement of expected truth at one layer of the system.
Every material contract should define the following. For the CHF terminology layer, the contract could state:
Field
Definition
In the case of CHF
Requirement
What condition must remain true.
The CHF grouper must match the approved CMS revision.
Measurement
How the team will measure deviation.
Compare the grouper version and included codes with the governed clinical glossary.
Tolerance
What level of deviation, if any, the system can accept.
No missing or retired codes are allowed in a customer-facing view.
Owner
Which team owns the condition and its remediation.
The clinical data team.
Enforcement
Whether a failure causes a warning, clarification, escalation or complete stop.
Block the affected view and notify the owner.
Failure code
Which predefined classification applies when the condition fails.
VIEW_TERM_STALE.
Dependencies
Which definitions, systems or upstream contracts the requirement depends on.
The approved CMS grouper revision as the upstream source of truth.
Expand table
Collapse table
A truth contract is operational, not just descriptive. Operating a truth contract requires teams to store it in a version-controlled YAML or JSON manifest, or a dedicated contract registry, binding the requirement to its tests, owner, failure code, dependencies, tolerance and enforcement action.
Once a truth contract is set, we still need three more components to operate it in practice: contract tests, the failure taxonomy and contract triggers.
Contract tests
Contract tests make a truth contract executable, not merely a written statement. To execute it right, each truth contract should be expressed through one or more tests, covering positive cases, ambiguity cases, boundary conditions and regression cases.
Contract tests have a few types.
Test type
Verifies
Terminology
The semantic view uses the approved business or regulatory definition.
Routing
The system directs the request to the intended semantic view.
Semantic metadata
Business concepts are explicit in the semantic layer, not inferred.
Intent
The structured interpretation preserves every material part of the request.
Execution
The generated SQL faithfully implements the approved intent, not just a passing syntax check.
Result
The business outcome holds against representative test data, not just one dataset.
Expand table
Collapse table
To operate at scale, the team runs the applicable terminology, routing, semantic and intent checks before the agent executes an action, then validates the generated SQL and its output with execution and result tests.
Failure taxonomy
The failure taxonomy shares an operational vocabulary for contract test failures. Instead of labeling every issue as a hallucination or model error, the taxonomy gives each failure an identity that routes it to the right remediation path.
Those failure classifications may include the below attributes:
Attribute
Description
Affected layer
Where in the system the failure occurred.
Known failure class
The category of failure this violation belongs to.
Accountable owner
The team responsible for remediation.
Severity
How serious the failure is.
Expected response
What the system or team should do when this failure occurs.
Expand table
Collapse table
The AI architect or evaluation lead defines these codes during system design, in collaboration with each layer's owner, so the code is set before any failure happens, not invented at runtime. When a contract fails, the harness simply looks up the code from the registry and routes the incident to its owner.
If production exposes a failure that doesn't fit the taxonomy, the team defines a new class and updates the corresponding contract and regression tests. This keeps the taxonomy governed and versioned, not an ad hoc list of errors.
Contract triggers
Truth contracts define what to test, while triggers define when those tests run. They sit outside the reliability ladder, since one change event may affect multiple layers. These triggers map to three types of change, each suggesting which contract tests should run.
They are:
Trigger
Source of change
Example
Response
System change
A change to a prompt, model, router, semantic view, source system or orchestration rule.
A new plan_type dimension gets added to the semantic view.
Run only the contract tests tied to that component, in this case, metadata and terminology tests.
Truth-definition change
A change to a regulation, clinical code, business definition or reporting policy.
The CMS grouper revision updates to add new CHF codes.
Identify every dependent contract, rerun its tests and block any component that no longer satisfies the requirement.
Production failure
A real request exposes a gap the test suite didn't cover.
The clinical reviewer catches a wrong date range that no test had checked for.
Turn the failure into a regression test, then audit related dependencies for the same weakness.
Expand table
Collapse table
To scale, teams use dependency metadata to select the affected tests, rather than rerunning the full suite or relying on manual judgment. A regression test prevents the observed problem from returning, a dependency audit checks whether the same weakness exists elsewhere.
Together, the three triggers turn every change and every unexpected incident into durable system knowledge. Together, these mechanisms form a continuous control loop.
The control loop
This is the ultimate goal for anyone operating AI agents: a system that gets stronger every time it fails.
A trigger runs the relevant contract tests. A failure routes to its owner for a fix. The fix is itself a change, so it re-triggers the loop and the observed failure becomes regression coverage, making the same failure mode much less likely to recur unnoticed, as illustrated below.
Summary
The CHF example showed why evaluation is not good enough for managing AI agents. Stale clinical terminology, incomplete semantic metadata and an incorrect interpretation of the request combined into valid SQL that carried every error into the final answer. Nothing crashed. Each error looked plausible enough to pass unnoticed and evaluation confirmed the pipeline ran, not that it preserved the truth of the request.
That is why we propose an operating model built from a few core components. The reliability ladder establishes where governance belongs. Truth contracts state what each layer must preserve. Contract tests provide executable evidence. The failure taxonomy makes ownership and response explicit. Triggers keep the controls current as systems and definitions change.
These components do not work as a checklist. They work as a loop. A trigger runs the tests, a failure routes to its owner, and the fix becomes a permanent test. The same pattern never slips through twice, so the system gets stronger every time it fails.
Agent reliability is a systems engineering problem. Solving it is what will makes AI agents trustworthy enough to unlock real adoption. That, for us, is the difference between evaluating a model and engineering AI that works.
Data strategy
Semantic drift and semantic integrity: Stewarding meaning in the age of AI
Learn more
Generative AI
Navigating today’s AI token crisis
Learn more
Programming languages
Is a codeless future an illusion?
Learn more
View more
View less
Explore a snapshot of today's tech landscape
Read Technology Radar
