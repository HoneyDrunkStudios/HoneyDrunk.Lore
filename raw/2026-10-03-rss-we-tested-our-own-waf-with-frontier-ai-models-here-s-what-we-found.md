---
"source": "https://blog.cloudflare.com/adaptive-ai-waf-testing"
"title": "We tested our own WAF with frontier AI models. Here's what we found"
"author": "unknown"
"date_published": "2026-09-29"
"date_clipped": "2026-10-03"
"category": "Security & Ethical Hacking"
"source_type": "rss"
"capture_method": "full-readable-extraction"
---

# We tested our own WAF with frontier AI models. Here's what we found

# We tested our own WAF with frontier AI models. Here’s what we found

“Is your WAF ready for frontier AI models?” We keep hearing this question from our customers, so we decided to find out.

When it comes to exploiting applications, what LLMs are really good at is iterating and mutating attack payloads faster than any human hacker could do. LLMs can use real-time responses to iterate and change their techniques by, for example, testing different encodings, sending the payload in a different part of the HTTP request, or moving to the next vulnerability to test.

Even before LLMs were around, security engineers used two common approaches to test applications: static and dynamic application security testing. The former analyzes code without executing it to identify vulnerabilities, while the latter probes running applications to find runtime flaws. There are plenty of works scanning code with frontier AI models, including details on __how to build your own harness.__

For the project described in this blog post, we took a dynamic approach: making the LLM act as if it was a hacker to evaluate whether a WAF is doing its job. The LLM had no visibility into source code, no view of the WAF's rules, and could only see selected HTTP response data.

We built a WAF tester that starts from known exploits and then iterates by changing how it is encoded or delivered, sends it again, and uses the response to choose the next variation. A request that was not blocked became a lead for human review, not a confirmed exploit.

We ran the tester against an authorized customer staging environment across six attack categories and recorded 1,107 attempts. After reviewing the non-blocked requests and removing malformed, benign, duplicate, and out-of-scope observations, the vast majority of the attacks were blocked by the Cloudflare WAF. The requests that got through helped us create new detections to harden our security to benefit all Cloudflare customers.

Here we will explain how we set up the system, the types of attacks we tested, which attack vectors bypassed the WAF more easily, and how we fixed it. Most importantly, we share what we learned from this process and how this exercise is becoming a foundational building block of our WAF development lifecycle.

Finally, we offer guidance to help you correctly deploy your WAF in front of your application and, most importantly, patch your software. A payload that bypasses the WAF still needs an exploitable application to succeed, so keeping your stack up-to-date remains one of the strongest defenses against attackers.

## How the adaptive loop works

To test our WAF with frontier models, we built a system that iterates over multiple scenarios. A scenario means choosing one attack category, placing the input in a specific part of the request, starting with a version the WAF already blocked, and giving the tester a fixed number of attempts to try other variations. The loop runs LLM models twice: the first is the proposal call, the second is the review call.

The first call receives the starting request, the context, a short history of earlier results, and suggests the next variation, then the code builds and sends the request. The review call receives the request context, response status, selected headers, and the response body. The loop stops when mutations stop producing useful variations or when a hard coded attempt limit has been reached.

Both model calls work without access to WAF internal information. Neither receives rule expressions, rule IDs, WAF Attack Score details, or the identity of the security layer that acted. We implemented the system in Python rather than wrapping an existing penetration-testing tool. It handles HTTP replay, scenario orchestration, state tracking, and result collection.

In the current implementation, the models do not send requests directly — code controls what happens at each step. Before each request, it checks the target hostname against an allowlist, disables redirects, records the attempt, and enforces the attempt limit. After each request, it records the response and uses the model's review to choose the next predefined step. Response text may appear in a later prompt, so the tester treats it as untrusted input. Neither model call can deploy a rule nor change enforcement.

The system records structured evidence for each attempt.

## Six attack categories against one WAF configuration

The main run targeted an authorized customer staging environment protected by Cloudflare’s WAF. We used an allowlisted test User-Agent so the customer’s automated-traffic controls would not stop the test before requests reached the WAF.

We ran 45 scenarios. For each, we looked for ways to deliver the same attack differently: different encoding, different part of the request, or the same destination written another way. Of these, 44 covered six attack categories: [ cross-site scripting (XSS)](https://www.cloudflare.com/learning/security/threats/cross-site-scripting/),

[,](https://www.cloudflare.com/learning/security/threats/sql-injection/)

__SQL injection (SQLi)__[,](https://community.owasp.org/attacks/Command_Injection)

__command injection (CMDi)__[, path traversal or local file inclusion (LFI), and Log4j. The remaining scenario covered log injection, reported separately.](https://en.wikipedia.org/wiki/Server-side_request_forgery)

__server-side request forgery (SSRF)__The WAF in the test zone was configured as follows: [ WAF Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/) blocking scores of 30 or below, all

[enabled, and](https://developers.cloudflare.com/waf/managed-rules/reference/cloudflare-managed-ruleset/)

__Cloudflare Managed Ruleset__[with Paranoia Level 3.](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/)

__OWASP Core Ruleset__For the headline measurement, we recorded whether the WAF blocked each request or not. The results describe the configured WAF boundary as a whole, not the performance of any individual rule or detection mechanism.

## What adaptation looked like in one recorded session

Here is an example of how the LLM adapts a Server-Side Request Forgery (SSRF) attack during the test.

Cloud metadata services can expose temporary credentials to workloads. An SSRF vulnerability can let an application fetch that data on an attacker's behalf. A WAF can help stop the malicious request before it reaches the application, but it is only one layer of protection.

In this SSRF scenario, the tester sent the same cloud metadata address in different forms (such as integer, octal, and trailing-dot representations of the same IP) and placed it in different parts of the request. The WAF blocked all of them except one. At attempt 18, the model kept the same request structure as the previous blocked attempt and switched to the trailing-dot form. The client encountered a redirect rather than a WAF block.

The table below shows selected moments from the session. The hypothesis column summarizes what the model said it was trying before each move. It is not a verbatim transcript, and it is not proof that the explanation was correct.

| Stage | Selected moment |
|---|---|
| BASELINE |
Observed: The WAF returned a 403 block page for the direct metadata address 169.254.169.254Hypothesis: The detector might recognize the literal dotted address or metadata path.Next move: Represent the same address as the decimal integer 2852039166.
|
| ATTEMPT 1 |
Observed: The decimal representation was blocked.Hypothesis: The metadata path or query placement might still trigger detection.Next move: Use the octal representation 0251.0376.0251.0376 and move the input from the query string to a form body.
|
| ATTEMPT 2 |
Observed: The octal representation in the form body was blocked.Hypothesis: The metadata path might still trigger detection regardless of host encoding.Next move: Try a hostname-based representation without that path.
|
| ATTEMPTS 3–16 |
Omitted from this excerpt. The tester continued exploring host, path, and request-shape combinations.
|
| ATTEMPT 17 |
Observed: The decimal integer host, now used with a later request shape, was blocked.Hypothesis: A trailing dot might change what the detector matched without changing the intended destination.Next move: Keep the method, input placement, content type, and path form the same; switch to the trailing-dot host form: 169.254.169.254.
|
| ATTEMPT 18 |
Observed: The client encountered a redirect rather than a Cloudflare block page. The run retained an edge-pass observation because the expected mitigation was absent.Limit: There was no successful origin response, response body, or evidence that the application fetched metadata.Next step: Preserve the request for triage and origin-side validation.
|

Attempts 17 and 18 are an interesting pair: same request structure, different host representation. One was blocked, one was not. That gave us a specific question: does the trailing dot change how the WAF reads the destination? It was a lead to investigate, but not proof that metadata was accessed.

This was one selected trajectory among 45 scenarios. The next section shows how we counted and triaged the full run.

## What we found

Our tester generated 1,107 attempts and the overall result was strong with XSS, LFI, SQLi, and Log4j having near full coverage. While the run produced useful findings, it also produced noise. After human review, we were left with 49 findings worth investigating, 48 of them belonging to CMDi and SSRF.

Here is how they break down:

|
|
|
|---|---|---|
Recorded mutation attempts | 1,107 | Model iterations across 45 active scenarios; not all produced a usable result |
Post-triage result set | 607 | The 558 blocked requests plus 49 documented WAF-relevant findings |
Blocked requests | 558 | The WAF stopped these before they reached the application |
WAF-relevant findings | 49 | Documented for remediation analysis after human review |

The rest did not produce a result worth counting as the model failed to generate a usable HTTP request, some failed before reaching the target, or the payload generated was benign.

When a request was not blocked, we worked through five questions before counting it as a finding:

|
|
|---|---|
Did the tester actually send a valid request? | If the model failed or the request never reached the target, the result tells us nothing about the WAF. |
Was the request clearly not blocked? | An ambiguous response is not enough to count. |
Was the request still malicious? | Changing a request to get it past the WAF can also make it harmless. |
Did the behavior belong to the WAF? | Some attacks only work through DNS or network paths the WAF cannot stop at request time. |
Could engineers reproduce it safely? | A fix needs a stable test case with a clear expected result. |

We removed anything that failed those checks and combined duplicate cases. What remained became the input for rule, normalization, and mitigation work.

## Findings became detections

Not every finding needed a new rule. Some pointed to gaps in existing [ Managed Rules](https://developers.cloudflare.com/waf/managed-rules/) coverage. Others pointed to how the WAF normalized the request or belonged to another security control. We replayed each case and decided where the change should happen.

We grouped related findings into four sets of candidate rules, validated each finding, and tested candidates against live traffic before any rule could protect customer traffic.

Before a new or updated rule can protect customer traffic, we check its impact on legitimate traffic and assess false-positive risk. Some of the issues we find when evaluating a new rule candidate include:

|
|
|---|---|
Missing or narrow detection | Review whether existing rules cover the finding |
Equivalent inputs interpreted differently | Engine or normalization review |
False-positive risk is too high | Revise or reject the candidate |

This work contributed to three changes in Cloudflare's Managed Ruleset: new detections for [ SSRF - Obfuscated Host](https://developers.cloudflare.com/waf/change-log/changelog/#2026-07-21) and

[in the July 21 release, and improvement of the existing](https://developers.cloudflare.com/waf/change-log/changelog/#2026-07-21)

__SSRF - Restricted Protocol__[rule. The SSRF - Obfuscated Host detection came directly from requests that encoded internal addresses in non-standard numeric forms.](https://developers.cloudflare.com/waf/change-log/changelog/#2026-08-04)

__SSRF - Cloud__## What we learned

The model was only one part of the test. We ran the same scenarios with two versions of the same model family. They produced different variations – and the same underlying issues appeared in both. Because request replay and evidence capture stayed consistent, we could compare the runs without treating either model's output as ground truth.

More attempts within one scenario did not always find more. Some scenarios started repeating earlier ideas near the end of the 25-attempt limit. We got broader coverage by testing more starting requests, attack categories, and input locations instead of extending one sequence.

The model generated requests. We decided which ones mattered. A request that was not blocked still needed replay and human review before it could become a finding, a mitigation, or a regression test. Without that review, there were no findings.

## What customers can do now

WAF is just one layer of detections you can deploy. When you deploy all available protections you increase the effectiveness of your overall stack.

First of all, check that Managed Rules, WAF Attack Score are [ set up correctly](https://developers.cloudflare.com/waf/get-started/) in front of your application. Other tools you can deploy include API Security, Bots and Fraud detection, and Threat Intelligence to strengthen your posture even further. For example,

[add a different layer: instead of looking only for known attack patterns, they define the request shapes an application expects and identify inputs outside that contract. This drastically reduces your attack surface area.](http://blog.cloudflare.com/application-profiles)

__positive security controls__Customers do not need to reproduce this experiment. To maximize the number of rules deployed in front of your application, we recommend running Managed Rules in log first, review matching requests in [ Security Events](https://developers.cloudflare.com/waf/analytics/security-events/), and confirm legitimate traffic is unaffected before moving a rule to Block. Alternatively, customers can reach out to their account team to get

[turned on, on their zones. This new feature simplifies how to review matched traffic and how to deploy signature detections. If you already perform application security testing, run those tests against a staging hostname protected by the same Cloudflare controls as production.](https://blog.cloudflare.com/attack-signature-detection/)

__Attack Signature Detection__## Next steps

By combining adaptive AI-driven testing with human triage and validation, we found detection gaps that fixed tests might miss and turned those findings into stronger WAF protections, improving our block rate. In a future post, we will share results from further testing using a white-box approach, where the model knows both the application’s vulnerabilities and the WAF rules protecting it.
