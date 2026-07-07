---
source: "https://www.cncf.io/blog/2026/07/03/how-data-sovereignty-is-changing-cloud-native-infrastructure-design"
title: "How data sovereignty is changing cloud native infrastructure design"
author: "CNCF"
date_published: "2026-07-03"
date_clipped: "2026-07-07"
category: "Azure & Cloud"
source_type: "web"
---

# How data sovereignty is changing cloud native infrastructure design

Source: https://www.cncf.io/blog/2026/07/03/how-data-sovereignty-is-changing-cloud-native-infrastructure-design

The core issue isn’t where your server sits. It’s who can be compelled to hand over what’s on it.

For years, cloud providers treated sovereignty as a geography problem. Pick a region. Choose a country. Keep your data local.

But laws such as the U.S. CLOUD Act changed the equation. Data access follows corporate control, not physical location. A hyperscaler operating infrastructure in Frankfurt remains subject to the laws governing its parent company. Region selection is a geographic control. Sovereignty is a jurisdictional one.

That distinction is increasingly shaping infrastructure decisions.

The EU’s Cloud and AI Development Act (CADA), proposed in June 2026, introduces a four-tier sovereignty framework for public sector cloud procurement. Canada’s federal government now scores cloud vendors on Canadian data residency and jurisdictional control. Many countries now maintain data localization, sovereignty, or residency requirements.t, and regulatory frameworks increasingly extend beyond data residency into questions of operational control, supply chain transparency, portability, and resilience.

The EU Data Act promotes interoperability and reduces barriers to switching providers. The AI Act introduces requirements around traceability, governance, and accountability for AI systems. NIS2 and DORA place greater emphasis on supply chain dependencies, operational resilience, and concentration risk. Similar conversations are emerging across jurisdictions worldwide.

Taken together, these developments point toward a future where infrastructure control is no longer merely a technical preference. It is increasingly becoming a regulatory expectation.

This shift is often framed as a privacy discussion. In reality, it is increasingly a resilience discussion. The same architecture that protects against foreign legal interference can also reduce exposure to sanctions, trade disputes, service suspensions, licensing changes, vendor exits, and other forms of external dependency.

For platform engineers, the challenge is straightforward: how do you meet sovereignty requirements without sacrificing the automation, portability, and operational efficiency that made cloud infrastructure attractive in the first place?

### The pattern emerging in production

Across Europe, regulated enterprises are increasingly assembling sovereign platforms from open-source components rather than buying sovereignty as a premium feature from hyperscalers.

The pattern is becoming familiar. Kubernetes provides the orchestration and policy layer. GitOps provides operational consistency across jurisdictions. OpenStack supplies the underlying infrastructure. Together, they allow organizations to enforce sovereignty requirements through architecture rather than contracts.

These are not proof of concept deployments. National rail operators, major banks, and European telecoms are already using Kubernetes, GitOps, and policy driven automation to operate regulated workloads at scale across sovereign environments.

The pattern is consistent: Kubernetes for governance and orchestration, OpenStack for sovereign infrastructure, policy as code for enforcement, and declarative operations for repeatability.

### Kubernetes as the sovereignty control plane

Building sovereign infrastructure is one challenge. Operating it consistently is another.

Most compliance programs still rely heavily on documentation, reviews, and manual processes. Those approaches work, but they don’t scale particularly well across hundreds or thousands of workloads. Kubernetes changes that by allowing sovereignty requirements to be enforced directly by the platform.

Admission controllers can enforce workload placement before a pod is ever scheduled. Node affinity rules ensure workloads only land on approved infrastructure within the correct jurisdiction. Namespace isolation creates clear boundaries between tenants, environments, or regions. Policy engines evaluate every API request against sovereignty requirements and reject non-compliant resources before they reach production.

Policy as code extends the same approach operationally. Sovereignty policies live in Git, are peer reviewed, tested through CI pipelines, and enforced automatically at deployment time. Tools such as OPA/Gatekeeper and Kyverno allow organizations to encode jurisdictional requirements directly into the cluster. The result is continuous enforcement rather than periodic verification. Every policy change is traceable. Every deployment decision is auditable.

At that point, sovereignty stops being a process and becomes a platform capability.

But Kubernetes still depends on an infrastructure layer underneath it. Compute, networking, storage, and identity all have to come from somewhere. If that foundation is tied to a platform operated by an organization outside your jurisdiction, some of the guarantees enforced at the Kubernetes layer become harder to maintain.

This is where OpenStack fits into the picture.

OpenStack provides the infrastructure services Kubernetes relies on while allowing organizations to operate those services within their own jurisdiction. Bare metal provisioning through Ironic removes the need for a proprietary hypervisor between workloads and hardware. Keystone keeps identity management self-hosted. Neutron provides network isolation under the operator’s control. Ceph delivers distributed storage on infrastructure you own and operate.

OpenStack can be deployed entirely within a controlled environment. No license servers. No mandatory telemetry services. No external dependencies required for day-to-day operations.

The combination is what makes the architecture work. Kubernetes provides the policy and enforcement layer. OpenStack provides the infrastructure foundation beneath it. Together they allow sovereignty requirements to be implemented in code, enforced automatically, and audited across the entire stack.

### The hard part: Operating it

Sovereignty often means separate environments for each jurisdiction. Every upgrade, certificate rotation, RBAC change, security patch, and capacity planning exercise now happens across multiple clusters instead of one.

GitOps is what makes this operationally manageable.

A Git repository contains shared configurations and jurisdiction specific overlays. GitOps controllers running inside each cluster continuously reconcile against that desired state. No centralized control plane is required. Each cluster pulls and applies its own configuration locally.

The operational benefits are obvious, but the compliance benefits are just as important. Every change is reviewed, version controlled, and auditable. When someone asks what was running in a cluster at a specific point in time, the answer is already in the commit history.

The same principle applies to the software supply chain. SBOMs, image signing, and admission policies help ensure that only verified workloads reach production.

For organizations pursuing higher levels of sovereignty, visibility cannot stop at the operating system. Firmware, management controllers, and hardware components sit below the software stack and often have broad access to the host itself. That is why Hardware Bills of Materials and firmware verification are becoming part of the sovereignty conversation as well.

### What comes next

The infrastructure buildout is already underway. CADA aims to significantly expand European data centre capacity over the coming years, but hardware alone does not create sovereignty. The platform layer matters just as much as the infrastructure underneath it.

AI is making that reality even more visible. As regulators place greater emphasis on how models are trained, governed, and audited, training infrastructure is increasingly being evaluated through the same sovereignty lens as the data itself.

Federated learning is one example of how this changes architecture. Instead of moving data to a central location, training happens where the data already resides. Sovereign Kubernetes clusters perform local training while only aggregated model updates move between jurisdictions. The same policies, namespace boundaries, and governance controls used for compliance become the foundation for distributed AI systems.

For platform teams, the question is no longer whether sovereignty requirements are arriving. They are already influencing procurement decisions, infrastructure design, and operational models.

The good news is that the building blocks already exist. Kubernetes provides the orchestration and policy framework. OpenStack provides the infrastructure foundation. GitOps, policy engines, software supply chain security, and identity complete the picture.

For years, cloud infrastructure optimized for centralization. Sovereignty is pushing in the opposite direction: more regional control, greater transparency, and stronger operational ownership.

The question is no longer whether sovereignty will shape infrastructure design.

The question is whether sovereignty remains something organizations document, or something their platforms can enforce.

Many of the technologies discussed in this article are developed and operated in the open. Explore VEXXHOST’s open-source work and contributions on GitHub: https://github.com/vexxhost.
