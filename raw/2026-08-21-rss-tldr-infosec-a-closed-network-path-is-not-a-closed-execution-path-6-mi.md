---
source: "https://thecorestrength.net/blog/a-closed-network-path-is-not-a-closed-execution-path"
title: "A Closed Network Path Is Not a Closed Execution Path (6 minute read)"
author: "unknown"
date_published: "2026-08-19"
date_clipped: "2026-08-21"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-08-19"
source_role: "primary-via-tldr"
---

# A Closed Network Path Is Not a Closed Execution Path (6 minute read)

Source: https://thecorestrength.net/blog/a-closed-network-path-is-not-a-closed-execution-path

A Closed Network Path Is Not a Closed Execution Path | The Core Strength Network
About Blog Podcast Events Join Join the Network A Closed Network Path Is Not a Closed Execution Path In the cloud, network isolation does not guarantee security. Even behind tight firewalls, privileged actions can be triggered across environments via legitimate event-driven architectures. Because security controls often operate independently, they fail to recognize how chained subscriptions and permissions create a continuous, unmonitored execution path. This post explores why defenders must shift from simply securing network boundaries to mapping and constraining complete execution flows from design to deployment.
Ramesh Ramani August 14, 2026 Imagine a sensitive cloud application with no Internet access, isolated behind tightly controlled firewalls and security groups.
Despite that, an event from lower-trust environments—or even from an Internet-connected external cloud account—can still cause the application to perform a privileged action without a direct network route, a code-level exploit, or the bypass of any configured IAM or network control.
The application is network-isolated. It is not execution-isolated.
Here is the difference: a network path is how something reaches your code. An execution path is how something causes your code to run. In the cloud, these two paths do not always align. A message arrives on a queue, so a function wakes up. The function calls a service. The service does its work using its own identity and permissions. Every link in that chain is a subscription, permission or service-to-service authorization rather than just a Layer 3 route, so these may not appear on a network diagram to reason about reachability — but the consequences can be the same.
When Isolation Does Not Prevent Execution Several years ago, I needed to pass some test data consistently from a development account to a staging-only internal service on AWS. The two environments had no direct Layer 3 route between them. The security engineer in me was pleased, but the developer was clearly not. What now?
Well, of course, the impatient developer voice won, and I reached for IAM to solve the problem. I sent the crafted information to an SQS queue in the Dev account, which triggered a Lambda function in the Staging account [1]. After processing the request, the Staging Lambda published the result to a response queue consumed by another Lambda in Dev. With the right queue policies, execution roles, and event source mappings, I had created a bidirectional workflow across environments that had no direct network route.
At the time, it felt like a clever event-driven shortcut. In retrospect, I had accidentally created something that looked a lot like event-driven command-and-control (C2): a path that allowed data to move from a lower-trust environment to a higher-trust one (and vice versa) without ever touching a customer-controlled cloud firewall.
In AWS, EventBridge can route events to Lambda or Step Functions, while a Lambda event source mapping can poll SQS and invoke a function. In Google Cloud, Pub/Sub or Eventarc can trigger Cloud Run or Workflows [2]. In Azure, Event Grid or Service Bus can initiate Functions or Logic Apps [3].
These are normal architectures. Many cloud applications depend on them.
The security problem appears when each trust relationship is reviewed separately. Connected together, however, those controls can create a path from an external or low-trust source to a privileged internal action.
A Legitimate Path Can Still Be Dangerous Once I realized that I could cross an account boundary without adding a network route, I pushed further.
I configured a cross-account EventBridge policy that allowed an external AWS account to send a crafted event into my internal account [4]. The event triggered a Lambda function inside the internal account, which then called an application running in an EKS cluster.
The application was protected by security groups, Kubernetes NetworkPolicies, and service-mesh authorization. But the request was allowed through each layer because every step was legitimate.
Once reached, the application used its own cloud identity to perform a privileged action. The application in question was used to clean up resources in dormant, lightly used environment accounts. The application received the input, assumed a role into the test account, and used that role’s broadly scoped permissions to perform an action I passed in. The message was to delete a particular security group.
Nothing was bypassed. Every control worked as configured.
The problem was that each control saw only one step. None of them understood that an external message could eventually trigger a privileged action inside the environment.
None of this tripped a detection signature.
This is the danger with evaluating cloud boundaries as just identities, policies, and isolation.
Why Detection Struggles I went looking for any detection signal I might have tripped along the way, but didn’t find any.
The only obviously destructive action was the deletion of the security group, and by then the original event was several steps removed. CloudTrail showed which identity made the call, but that identity belonged to the application in EKS—accurate attribution that explained nothing about why the application acted.
So I traced my own steps backward: application logs, mesh logs, flow logs, the Lambda request, the EventBridge rule, and finally the event sent from the external account. Each hop had left behind artifacts as evidence. It still took me most of an afternoon to piece together, and I knew exactly what I was looking for.
The artifacts existed. Each system recorded its own hop under its own identifier, so even a SIEM or automated hunt would have seen what I saw: a collection of benign audit records and network flows rather than a single execution path.
I knew the path. A defender wouldn’t.
And there is no single path to know. Every role and resource you add multiplies them. Signature-based alerting struggles against a set that grows with every deploy. Anomaly detection struggles as well because these paths are the baseline—the “approved” paths.
They were built on purpose.
Rethinking Ingress, Egress, and Service-to-Service Communication I come from a time when a firewall just meant iptables on a Linux server or an enterprise-level Layer 3/4 device with deep-packet inspection. Traditional network security meant ingress, egress, and east-west traffic; more recently, it has also encompassed service-to-service communication.
When I looked at these execution paths and how they eventually affected the data plane, they seemed to follow the same familiar patterns.
An event entering an account looked like ingress. A workflow moving across services looked like service-to-service communication. Data sent through a queue or event bus to an external account looked like egress.
Event routes, queues, workflow triggers, and service identities are not merely application plumbing. Together, they create execution paths that are also part of the security boundary.
The paths were familiar. Only the transport mechanism had changed.
What Should Change? By then, I was seeing this pattern everywhere; it had become impossible to ignore.
Instead of reviewing the queue policy, Lambda permissions, mesh authorization, and pod identity separately, I began following the execution path as one connected flow.
That also changed how I thought about detection. By the time such a path is reconstructed from logs, the action has already occurred. We were treating execution paths primarily as forensic trails rather than identifying and constraining them during system design.
We should start asking what execution paths a design could create, where they would cross trust boundaries, how they could be constrained, and what signals would be needed to detect their misuse. Path-aware detection begins at design time.
In practice, that meant:
Graphing service and execution relationships and maintaining baselines of expected paths. Treating cross-account event sources and targets as ingress or egress at the trust boundary—even when no direct network route exists. Evaluating workload identities in the context of both their upstream triggers and downstream privileges. Correlating initiating events with the identities, workloads, and privileged actions they ultimately trigger. While not easy, this approach can help build better guardrails, uncover attack paths that would otherwise be easy to miss, and make detection part of the design rather than something added afterward.
Follow the Execution Path The lesson was simple: a closed network path does not always mean a closed execution path.
We spend a lot of our time reviewing identities and scoping their permissions. Similarly, we invest a lot of time in constraining network access and isolating workloads. But we seldom think about what these controls enable when chained together.
The controls may all work as intended. The risk may still emerge from how they connect.
So when reviewing a cloud system, do not stop at isolation, policy, or identity.
Follow the execution path.
References [1] Amazon Web Services, “How Lambda processes records from stream and queue-based event sources,” AWS Lambda Developer Guide. [Online]. Available: https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html . [Accessed: Aug. 3, 2026].
[2] Google Cloud, “Create triggers from Pub/Sub events,” Google Cloud Documentation. [Online]. Available: https://cloud.google.com/run/docs/triggering/pubsub-triggers . [Accessed: Aug. 3, 2026].
[3] Microsoft, “Use a function as an event handler for Event Grid events,” Microsoft Learn. [Online]. Available: https://learn.microsoft.com/en-us/azure/event-grid/handler-functions . [Accessed: Aug. 3, 2026].
[4] R. Ramani, “Hijacking Amazon EventBridge for Launching Cross-Account Attacks,” Square Developer Blog, Jun. 25, 2025. [Online]. Available: https://developer.squareup.com/blog/hijacking-amazon-eventbridge-for-launching-cross-account-attacks/ .
Subscribe to our newsletter Get updates on events, resources, and insights from practitioners who are
shaping the future of network security.
Subscribe Thank you for subscribing to our newsletter. Something went wrong while subscribing to our newsletter. Please try again. No spam. Unsubscribe anytime. We respect your privacy. About Blog Podcasts Events Join Terms of Service Privacy Policy © 2026 All rights reserved. Powered By
