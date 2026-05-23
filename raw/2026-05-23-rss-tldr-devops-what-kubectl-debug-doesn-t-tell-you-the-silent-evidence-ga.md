---
source: "https://www.cncf.io/blog/2026/05/18/what-kubectl-debug-doesnt-tell-you-the-silent-evidence-gap/"
title: "What kubectl debug doesn't tell you: The silent evidence gap (5 minute read)"
author: "TLDR DevOps"
date_published: "Fri, 22 May 2026 00:00:00 GMT"
date_clipped: "2026-05-23"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-05-22"
source_role: "primary-via-tldr"
---

# What kubectl debug doesn't tell you: The silent evidence gap (5 minute read)

Source: https://www.cncf.io/blog/2026/05/18/what-kubectl-debug-doesnt-tell-you-the-silent-evidence-gap/

Posted on May 18, 2026
by Shamsher Khan, CNCF Community Member 
CNCF projects highlighted in this post
The session that left no record 
A kubectl debug session can contain the only direct observation of a failing system state. However, once the session ends, Kubernetes does not retain the termination context of that session in its API. This is not a kubectl bug — it follows directly from the Kubernetes API design for ephemeral containers.
Once the pod state changes, the Kubernetes API no longer exposes the termination context of that debug session. The exit code that encoded your finding, the duration of the session, which container you targeted — is not retained by the Kubernetes API after subsequent pod updates.
Here is what that looks like, and what it means for your incident response workflow.
Reproduce it in three commands 
You do not need a special cluster to see this. Any Kubernetes 1.25+ cluster works. Three commands confirm the gap.
Step 1 — Deploy a stable target pod: 
kubectl run debug-target --image=nginx:alpine -n default
kubectl wait --for=condition=Ready pod/debug-target -n default
Step 2 — Attach a debug session, run for 10 seconds, exit with a distinctive code: 
kubectl debug debug-target -n default \
--image=busybox:1.36 \
--target=nginx \
-it -- sh -c "echo 'finding: connection pool exhausted'; sleep 10; exit 42"
Note: –target is a kubectl CLI feature that routes the debug container into the target container’s process namespace. The target container name is not stored as an API field on the pod object.
Step 3 — Immediately after exit, inspect the ephemeral container status: 
kubectl get pod debug-target -n default \
-o jsonpath='{.status.ephemeralContainerStatuses[*]}' | jq .
What you get: 
{
"containerID": "containerd://...",
"image": "busybox:1.36",
"name": "debugger-xxxxx",
"ready": false,
"state": {
"terminated": {
"exitCode": 42,
"finishedAt": "2026-04-17T16:43:56Z"
}
}
}
The exit code is visible here — but only while this State.Terminated entry is still present. The moment any other event modifies the pod — another container restarts, a second debug session is attached, the pod is rescheduled — this termination context is replaced and the prior session’s exit code is no longer observable. Check logs after the session ends:
kubectl logs debug-target -c debugger-xxxxx -n default
Error from server (NotFound): container "debugger-xxxxx" not found
There is no lastState to fall back on. Once the current state changes, the termination context is no longer accessible through the Kubernetes API. 
Why this happens: The API specification decision 
This is not a bug or missing feature — it is an explicit API design decision. The EphemeralContainerStatus type in the Kubernetes API (v1.32) does not include a lastState field:
EphemeralContainerStatus:
containerID string
image string
name string
ready boolean
state ContainerState
# lastState: absent by design
# restartCount: absent by design
Compare with ContainerStatus for a regular container:
ContainerStatus:
containerID string
image string
lastState ContainerState ← preserves prior termination
name string
ready boolean
restartCount integer ← counts restarts
state ContainerState
The key distinction: ContainerStatus.lastState preserves the prior termination record — exit code, start time, finish time, reason — and survives across restarts. EphemeralContainerStatus has no equivalent field.
Ephemeral containers were introduced to support debugging without affecting pod lifecycle guarantees. Their design explicitly avoids restart semantics, which influences how their state is exposed in the Kubernetes API. The Kubernetes specification defines ephemeral containers as
“not restarted on failure.” As a result, the restart tracking and last-state preservation mechanisms that apply to regular containers are excluded by design. See the Kubernetes Ephemeral Containers documentation and the kubectl debug reference for the upstream specification.
MAGE: ContainerStatus vs EphemeralContainerStatus side-by-side comparison showing lastState present/absent 
What gets lost in practice 
Investigation Signal Visible After Pod State Changes? Exit code Only while current State.Terminated is present Session duration Not available Target container (–target) Not recorded as an API field Debug container logs Not accessible after termination 
These signals exist only transiently and are not preserved across pod state transitions.
The exit code convention is particularly common in SRE workflows — exit 42 for “connection pool exhausted,” exit 1 for “config file missing.” Once the pod state changes, these signals are no longer observable through the Kubernetes API.
Partial workaround: Pipe findings to a file on a shared volume before exiting, or use kubectl logs -f in a parallel terminal to capture stdout in real time. Note that kubectl logs -f requires the session to be actively writing to stdout and the user to be capturing before exit — not always possible during a live incident. 
The incident response impact 
Consider a realistic handoff sequence:
On-call engineer attaches kubectl debug to a struggling pod 
Spends 12 minutes investigating inside the container 
Identifies the issue, exits with code 42 
Writes incident notes: “found connection pool exhaustion, exit 42” 
Hands off to the next engineer 
The next engineer tries to verify:
# How long was the debug session?
kubectl get pod my-pod -o jsonpath='{.status.ephemeralContainerStatuses[*]}' | jq .
# Duration: not available
# What container did they target?
# --target is a kubectl CLI flag — not stored in the API
# Can I see what they ran?
kubectl logs my-pod -c debugger-xxxxx
# Error: container not found
The handoff depends entirely on the first engineer’s notes. If those notes are incomplete — which happens during a live incident — the diagnostic context may no longer be observable through the Kubernetes API. The second engineer starts from scratch.
In some regulated environments, this has compliance implications. Frameworks that require traceability of operational actions — such as PCI-DSS requirement 10.3 on audit logging, or SOC 2 access activity requirements — have no mechanism to satisfy that requirement for ephemeral container sessions through the Kubernetes API alone.
Because the Kubernetes API does not record the –target container name or session duration as API fields, it is currently impossible to answer “who looked at what container, and for how long” using standard Kubernetes audit logs alone for ephemeral container sessions. 
What can be done today 
Application-level logging: Establish a team convention to log findings to a shared volume or external system before exiting. Simple but requires discipline under incident pressure.
Real-time capture via the watch API: Event-driven capture at the Terminated transition can preserve the State.Terminated block before any subsequent pod modification replaces it. An event-driven capture approach can preserve ephemeral container termination state at the moment it occurs, before it is replaced by subsequent pod updates. This requires a watch on pod modifications and assumes no other controller updates the pod before capture.
External observability systems: Route debug session findings to an external audit log or SIEM at the application level before exiting.
An example implementation demonstrating this approach is available at github.com/opscart/k8s-causal-memory , with a reproducible scenario under scenarios/05-ephemeral-exit/ . The captured record for a 10-second session exiting with code 42:
container_name: debugger-1776446626
target_container: nginx
exit_code: 42
exit_class: ERROR
duration_seconds: 10.0
node_name: opscart-m02
Everything the Kubernetes API no longer exposes after pod state changes — preserved at the moment of exit.
Is this worth a KEP? 
This raises a potential area for enhancement in Kubernetes. One option would be introducing a minimal termination history — similar to lastState in ContainerStatus — for ephemeral containers. The lastState field could be added to EphemeralContainerStatus with minimal breaking changes, since ephemeral containers are never restarted. It would store only the most recent termination record.
The design decision to exclude lastState made sense when ephemeral containers were introduced in alpha (Kubernetes v1.16). As kubectl debug becomes a standard incident response tool across the ecosystem, the absence of a termination record has real operational consequences.
As ephemeral containers become a standard debugging mechanism, the absence of even minimal termination history raises broader questions about observability and auditability in Kubernetes itself.
The natural owners of such a proposal would be SIG Node — which owns the kubelet and container lifecycle — or SIG Instrumentation — which owns observability primitives.
Reproduce the scenario: github.com/opscart/k8s-causal-memory/scenarios/05-ephemeral-exit 
Share
