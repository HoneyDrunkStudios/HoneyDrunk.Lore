---
source: "https://aws.amazon.com/blogs/security/governing-infrastructure-as-code-using-pattern-based-policy-as-code/"
title: "Governing infrastructure as code using pattern-based policy as code"
author: "Guptaji Teegela, Paul Keastead"
date_published: "2026-05-19"
date_clipped: "2026-06-01"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Governing infrastructure as code using pattern-based policy as code

Source: https://aws.amazon.com/blogs/security/governing-infrastructure-as-code-using-pattern-based-policy-as-code/

Governing infrastructure as code using pattern-based policy as code 
by Guptaji Teegela and Paul Keastead on 19 MAY 2026 in Advanced (300) , Best Practices , Security, Identity, & Compliance Permalink Comments Share 
Organizations often struggle to enforce security and compliance requirements consistently across their cloud infrastructure. In one environment, a workload might be deployed in an AWS Region that was never approved for that class of data. In another, a security group might allow broader access than intended. Required tags might be missing. Encryption might be assumed but not configured. These gaps create risk, increase review effort, and make audits harder than they need to be.
Many organizations already have standards that describe what good infrastructure looks like. The more difficult problem is making sure those expectations are checked the same way across repositories, environments, and teams before infrastructure is deployed. Manual review helps, but it doesn’t scale when delivery moves faster and more teams provision infrastructure directly.
Policy as code helps address this problem. It turns control intent into preventive checks that run in delivery workflow.
A pattern-based policy model makes those checks more straightforward to review, maintain, and explain. Teams can organize policy checks around recurring control patterns such as required metadata, allowed configuration, exposure restriction, protection enforcement, and privilege constraint, as shown in Figure 1. This structure simplifies policy coverage across security, governance, risk, and compliance (GRC), and engineering teams.
This post shows you how to use Open Policy Agent (OPA) in continuous integration and continuous delivery (CI/CD) pipelines to validate Amazon Web Services (AWS) infrastructure changes before deployment. You will learn how to structure policy checks around recurring control patterns, fit those checks into a gated delivery workflow, and retain validation artifacts that support both release decisions and later audit review.
The Compliance Engineering and Automation team from AWS Security Assurance Services (AWS SAS) frequently helps customers implement policy as code as part of broader control design and compliance automation efforts. This post focuses on the pre-deployment layer. Runtime monitoring and post-deployment controls still matter, but they are outside the scope of this article.
Figure 1: Pattern-based policy as code in a gated delivery workflow
Organize policies around recurring patterns 
Teams sometimes build rules one service at a time, which can make policy as code libraries difficult to review and extend as the library grows. Similar control requirements can be expressed differently across repositories, and teams lose a common way to discuss what the policies are enforcing.
A pattern-based approach organizes policies around recurring control intent rather than service-specific checks, as shown in Figure 2. This makes coverage more straightforward to review, explain, and evolve as infrastructure changes.
A practical set of patterns includes:
Required metadata – for tags and other fields used for ownership, support, cost allocation, and automation. 
Allowed configuration – for approved Regions, accepted deployment boundaries, and other approved settings. 
Exposure restriction – for configurations that make infrastructure more reachable than intended, such as public ingress or internet-facing resources in the wrong environment. 
Protection enforcement – for baseline safeguards such as encryption, logging, or deletion protection. 
Privilege constraint – for AWS Identity and Access Management (IAM) definitions and access patterns that need tighter validation. 
Figure 2: Recurring control patterns used to organize policy as code checks
Where OPA fits in a layered governance model 
This post focuses on the preventive layer. You still need runtime controls, drift monitoring, remediation workflows, and compliance reporting. On AWS, AWS Organizations , AWS Control Tower , AWS Config , and AWS Security Hub remain important after resources exist.
OPA fits earlier in the process and validates that infrastructure changes align with expectations. OPA evaluates structured input ( HashiCorp Terraform plan JSON) against policy logic. It doesn’t replace AWS governance services that provide organizational guardrails, continuous monitoring, and resource level enforcement after resources exist.
As shown in Figure 3:
OPA – Checks proposed changes before deployment 
AWS Organizations and Control Tower – Establish organizational guardrails 
AWS Config and Security Hub – Provide visibility and monitoring after resources exist 
Service-level protections – Enforce settings at the resource boundary 
Figure 3: OPA validates changes pre-deployment; AWS services enforce guardrails, monitoring, and controls post-deployment
How to implement policy validation in your CI/CD pipeline 
Use the following steps to integrate OPA policy evaluation into your delivery workflow:
Submit a change through a pull request or merge request.
Run early validation checks such as formatting, syntax validation, and dependency checks. 
Generate a Terraform plan and convert it to JSON format. 
Evaluate the plan (JSON format) against the shared OPA policy library. 
Publish the validation report as an artifact. 
Run additional automated quality checks as needed. 
Use the validation artifact during approval decisions for higher-risk environments. 
Deploy approved changes. 
Continue post-deployment monitoring through AWS-native governance services. 
Quality gates provide automated pass or fail results based on defined criteria. Approval gates control whether a change moves into a protected environment. This separation matters—manual approval isn’t the first place where anyone notices missing tags, a disallowed AWS Region, or public ingress. Automated checks identify those issues earlier. OPA belongs in the automated gate layer. Its output also feeds the approval process.
Structure your policy library by control domain and intent 
A pattern-based library structure, as shown in the following sample, keeps the policy model closer to how teams talk about controls.
opa-policies/
├── patterns/
│ ├── baseline/ # Foundational security
│ ├── tagging/ # Required tags
│ ├── networking/ # Network controls
│ ├── logging/ # Logging enablement
│ ├── encryption/ # Encryption at rest and transit
│ └── iam/ # IAM best practices
├── shared/
│ ├── helpers.rego
│ └── messages.rego
├── tests/
├── fixtures/
└── docs/ 
A compliance engineer might describe a requirement as mandatory metadata. A cloud engineer might describe the same requirement as a tagging standard. The pattern structure helps both teams talk about the same thing.
Example 1: Enforce secure transport for Amazon S3 
This example demonstrates the protection enforcement pattern for Amazon Simple Storage Service (Amazon S3) . The goal is to verify that S3 bucket access is protected in transit by requiring a bucket policy that denies requests when aws:SecureTransport is set to false .
The policy checks two things: whether an S3 bucket policy includes a deny statement that blocks non-encrypted requests, and whether an S3 bucket has any corresponding bucket policy at all. The rule evaluates both create and update actions in the Terraform plan JSON.
This example uses an explicit deny rather than an allow statement for secure transport. An explicit deny overrides allow statements that might exist elsewhere in the policy set, making it the stronger enforcement pattern.
package compliance.amazon_s3.ssl
import future.keywords.in
import future.keywords.contains
import future.keywords.if
# Deny: S3 bucket policy missing SecureTransport deny statement
deny contains msg if {
resource := input.resource_changes[_]
resource.type == "aws_s3_bucket_policy"
is_create_or_update(resource.change.actions)
policy_value := resource.change.after.policy
policy := json.unmarshal(policy_value)
not has_secure_transport_deny(policy)
msg := sprintf(
"[S3-OPA-1] Resource '%s' does not enforce SSL/TLS. Bucket policy must include a Deny statement with Condition Bool aws:SecureTransport set to \"false\".",
[resource.address]
)
}
# Deny: S3 bucket created without any corresponding bucket policy
deny contains msg if {
resource := input.resource_changes[_]
resource.type == "aws_s3_bucket"
is_create_or_update(resource.change.actions)
bucket_name := resource.change.after.bucket
not has_bucket_policy(bucket_name)
msg := sprintf(
"[S3-OPA-1] Resource '%s' (bucket '%s') has no bucket policy. A bucket policy with a Deny statement for aws:SecureTransport \"false\" is required.",
[resource.address, bucket_name]
)
}
is_create_or_update(actions) if { actions[_] == "create" }
is_create_or_update(actions) if { actions[_] == "update" }
has_bucket_policy(bucket_name) if {
bp := input.resource_changes[_]
bp.type == "aws_s3_bucket_policy"
is_create_or_update(bp.change.actions)
bp.change.after.bucket == bucket_name
}
has_secure_transport_deny(policy) if {
stmt := policy.Statement[_]
stmt.Effect == "Deny"
stmt.Condition.Bool["aws:SecureTransport"] == "false"
stmt.Principal == "*"
action := stmt.Action
action == "s3:*"
}
When you adapt this example, decide whether you want to require one exact policy shape or support several equivalent forms of enforcement. A strict rule is more straightforward to reason about, but it might create false positives if teams already use alternate policy structures that achieve the same outcome.
Example 2: Restrict public ingress on sensitive ports 
This example implements the exposure restriction pattern. The goal is to identify Amazon Virtual Private Cloud (Amazon VPC) security group configurations that allow public ingress on sensitive ports before those rules are deployed.
The policy evaluates both inline aws_security_group ingress rules and standalone aws_security_group_rule resources, because customer repositories often use both modeling styles.
This example checks directly for public ingress on sensitive ports rather than trying to infer whether later controls might reduce actual exposure. Security group rules are a direct expression of intended network reachability, making them the right place to enforce this pattern early.
package compliance.amazon_vpc.ingress
import future.keywords.in
import future.keywords.contains
import future.keywords.if
# Sensitive ports that must not be open to the internet
sensitive_ports := {22, 3389, 5432}
# Deny: aws_security_group with inline ingress open to 0.0.0.0/0 on sensitive ports
deny contains msg if {
resource := input.resource_changes[_]
resource.type == "aws_security_group"
is_create_or_update(resource.change.actions)
ingress := resource.change.after.ingress[_]
ingress.cidr_blocks[_] == "0.0.0.0/0"
port := sensitive_ports[_]
ingress.from_port <= port
ingress.to_port >= port
msg := sprintf(
"[VPC-OPA-1] Resource '%s' allows ingress from 0.0.0.0/0 on port %d. Restrict access to specific CIDR ranges.",
[resource.address, port]
)
}
# Deny: aws_security_group_rule with type "ingress" open to 0.0.0.0/0 on sensitive ports
deny contains msg if {
resource := input.resource_changes[_]
resource.type == "aws_security_group_rule"
is_create_or_update(resource.change.actions)
resource.change.after.type == "ingress"
resource.change.after.cidr_blocks[_] == "0.0.0.0/0"
port := sensitive_ports[_]
resource.change.after.from_port <= port
resource.change.after.to_port >= port
msg := sprintf(
"[VPC-OPA-1] Resource '%s' allows ingress from 0.0.0.0/0 on port %d. Restrict access to specific CIDR ranges.",
[resource.address, port]
)
}
is_create_or_update(actions) if { actions[_] == "create" }
is_create_or_update(actions) if { actions[_] == "update" }
When you adapt this example, review which ports to treat as sensitive, whether both IPv4 and IPv6 exposure need checking, and how to handle approved exceptions.
Example 3: Enforce least privilege trust policy for IAM roles 
This example implements the privilege constraint pattern for IAM role trust policies. The goal is to identify trust relationships that allow overly broad principals to assume a role. The policy inspects the assume_role_policy document for aws_iam_role resources and looks for wildcard principals in three valid representations: Principal is "*" , Principal.AWS is "*" , and Principal.AWS is an array containing "*" . A wildcard principal allows a broader set of callers than most environments intend to permit. By treating wildcard principals as the prohibited pattern, the rule enforces a safer default and returns a clear result that reviewers can understand quickly.
package compliance.amazon_iam.trust
import future.keywords.in
import future.keywords.contains
import future.keywords.if
# Deny: IAM role with wildcard principal in trust policy
deny contains msg if {
resource := input.resource_changes[_]
resource.type == "aws_iam_role"
is_create_or_update(resource.change.actions)
policy_value := resource.change.after.assume_role_policy
policy := json.unmarshal(policy_value)
stmt := policy.Statement[_]
stmt.Effect == "Allow"
has_wildcard_principal(stmt)
msg := sprintf(
"[IAM-OPA-2] Resource '%s' has a wildcard principal in its trust policy. Specify explicit account ARNs, service principals, or federated providers instead of \"*\".",
[resource.address]
)
}
# Principal is directly "*"
has_wildcard_principal(stmt) if {
stmt.Principal == "*"
}
# Principal.AWS is "*"
has_wildcard_principal(stmt) if {
stmt.Principal.AWS == "*"
}
# Principal.AWS is an array containing "*"
has_wildcard_principal(stmt) if {
stmt.Principal.AWS[_] == "*"
}
is_create_or_update(actions) if { actions[_] == "create" }
is_create_or_update(actions) if { actions[_] == "update" }
When you adapt this example, decide what least privilege means for your IAM trust model. The key design choice is whether your policy checks for a single prohibited pattern or validates trust relationships against an approved set of trusted principals and conditions.
AWS Labs provides IAM Policy Autopilot , an open-source Model Context Protocol (MCP) server and command-line tool that helps generate baseline identity-based IAM policies from application code. That is adjacent to the pattern shown here —IAM Policy Autopilot helps with policy generation, while this example focuses on validating whether IAM role trust policies are scoped appropriately in infrastructure changes.
CI/CD implementation examples 
The following examples show the same operating model in two common CI/CD systems. The syntax changes, but the sequence stays the same: validate, plan, evaluate policy, retain the artifact, and use the result during promotion and approval. These examples assume OPA is installed in your CI/CD environment, the opa-policies directory contains your policy library, and Terraform is configured with appropriate credentials.
GitLab CI 
stages:
- validate
- plan
- policy_check
variables:
TF_IN_AUTOMATION: "true"
terraform_validate:
stage: validate
script:
- terraform fmt -check
- terraform init
- terraform validate
terraform_plan:
stage: plan
script:
- terraform plan -out=tfplan
- terraform show -json tfplan > tfplan.json
artifacts:
paths:
- tfplan.json
opa_policy_check:
stage: policy_check
script:
- opa eval --format pretty --data opa-policies --input tfplan.json "data.terraform.deny"
- opa eval --format json --data opa-policies --input tfplan.json "data.terraform.deny" > policy-report.json
artifacts:
paths:
- policy-report.json
GitHub Actions 
name: Terraform Policy Check
on:
pull_request:
jobs:
policy-check:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
- uses: hashicorp/setup-terraform@v3
- name: Terraform Format Check
run: terraform fmt -check
- name: Terraform Init
run: terraform init
- name: Terraform Validate
run: terraform validate
- name: Terraform Plan
run: terraform plan -out=tfplan
- name: Convert Plan to JSON
run: terraform show -json tfplan > tfplan.json
- name: Run OPA Policy Check
run: |
opa eval --format pretty --data opa-policies --input tfplan.json "data.terraform.deny"
opa eval --format json --data opa-policies --input tfplan.json "data.terraform.deny" > policy-report.json
- name: Upload Validation Artifact
uses: actions/upload-artifact@v4
with:
name: policy-report
path: policy-report.json
Retain validation artifacts for review and audit support 
In mature delivery workflows, policy results don’t disappear into pipeline logs but are retained as validation artifacts. Those artifacts help reviewers decide whether a change is ready for approval, supports exception handling by showing which controls failed and why, and can stay with the change record for later audit discussions. At a minimum, the artifact identifies the change or pipeline run, the evaluated scope, the policy package or version, the checks that ran, and the pass or fail results.
Test the policy model like software 
The first few rules are usually straightforward.The real work starts when the library grows and multiple teams depend on it. Testing includes:
Positive and negative test cases – Each policy has cases that show valid input and cases that show expected failures. 
Regression coverage – Shared helpers need regression coverage. 
Realistic fixtures – Terraform plan fixtures look like real changes rather than tiny made-up samples. 
Impact analysis – When a rule changes, teams can tell quickly what else might be affected. 
If developers stop trusting the results, they stop treating policy as a useful mechanism.
A phased approach to rolling out policy checks 
You don’t need broad coverage on day one. A phased rollout works better than an all at once enforcement approach.
Phase 1: Assess and pilot 
Start in advisory mode so teams can see results without being blocked. 
Identify two or three high-confidence patterns such as required metadata, approved Regions, or public exposure restrictions. 
Run OPA against existing pipelines and review the output for accuracy. 
Phase 2: Begin enforcement 
Enforce the small set of high-confidence patterns after the output is stable and the failures are useful. 
Integrate validation artifacts into your approval workflow. 
Establish ownership and exception handling processes for shared packages. 
Phase 3: Operationalize and expand 
Formalize versioning for shared policy packages. 
Expand pattern coverage based on team feedback and organizational priorities. 
Connect pre-deployment validation with post-deployment monitoring through AWS Config , AWS Security Hub , and AWS Organizations . 
Conclusion 
Policy as code helps narrow the distance between what an organization says it expects and what its delivery system checks. By implementing these OPA patterns in your CI/CD pipelines, you can build a preventive layer that evaluates infrastructure changes before deployment. With a pattern-based library, validation artifacts, and clear ownership, policy as code becomes a repeatable way to help translate control intent into day-to-day delivery, while AWS governance services continue to provide visibility and monitoring after resources exist.
To learn more about policy as code and AWS governance capabilities, see:
Contact AWS Security Assurance Services – Get help with your compliance engineering journey 
Open Policy Agent Documentation – Read the official OPA documentation and policy language reference 
AWS Security Hub User Guide – Learn how to aggregate and prioritize security findings 
AWS Well-Architected Framework: Security pillar – Review security best practices for your workloads 
AWS Config Developer Guide – Learn how to monitor and record resource configurations 
IAM Policy Autopilot – An open source command line interface (CLI) and MCP server from AWS Labs that helps generate IAM policies 
If you have feedback about this post, submit comments in the Comments section below.
Guptaji Teegela 
Guptaji is a Cloud Infrastructure Architect with AWS Security Assurance Services, where he focuses on compliance automation and policy-as-code for regulated workloads. He brings over 15 years of hands-on experience across site reliability engineering, platform engineering, and cloud architecture, with deep expertise in both AWS and Azure environments. Backed by a broad portfolio of industry certifications spanning cloud and security domains, Guptaji is driven by a passion for helping customers design and deliver reliable, secure, and highly automated cloud platforms.
Paul Keastead 
Paul is a Senior Security Engineer with AWS Global Professional Services Security, specializing in compliance automation, policy as code, and security engineering for regulated workloads. A CISSP-ISSEP, Lead CMMC Certified Assessor, and former FedRAMP Assessor, he builds automated validation pipelines that translate control requirements into preventive, testable checks in delivery workflows. He brings over a decade of experience in national security and public sector technology compliance.
TAGS: governance , Security Blog 
Loading comments…
