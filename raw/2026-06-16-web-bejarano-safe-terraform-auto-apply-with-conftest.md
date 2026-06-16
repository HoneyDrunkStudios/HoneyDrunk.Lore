---
source: "https://www.bejarano.io/terraform-autoapply/"
title: "Safe Terraform auto-apply with conftest"
author: "Ricard Bejarano"
date_published: "2026-06-06"
date_clipped: "2026-06-16"
category: "DevOps & CI/CD"
source_type: "web"
---

# Safe Terraform auto-apply with conftest

Source: https://www.bejarano.io/terraform-autoapply/

Safe
Terraform

auto-apply
with
conftest

Published Jun 6, 2026 by
Ricard Bejarano

You know the ritual: a change is made, Terraform plans, someone reviews it,
approves it, and it gets applied. At low enough velocity, this works. The
reviewer catches the odd mistakes, and everyone sleeps well.

Past a certain point,
the reviewer becomes the bottleneck
. Plans pile
up, engineers either rush through them or let them sit, and you start losing
either velocity or review quality. Often both.

Our immediate next thought is to
delegate review to AI
.
And while you can
complement
your plan review with AI—the most interesting
solution I’ve found in this space is
Overmind↗
—you
cannot fully delegate plan review to it, not for production infrastructure:

it’s
non-deterministic
: the same plan may pass today and fail tomorrow;

it often
violates audit/compliance requirements
that mandate human
sign-off with clear accountability; and critically

it
removes responsibility from the feedback loop
, no one owns the
decision, which is exactly what you don’t want when something breaks.

There’s a third option:
evaluating Terraform plans programmatically and
deterministically using policy-as-code
. That’s what we do, with

conftest↗
.

conftest

conftest↗
is a policy-as-code tool built on

Open Policy Agent↗
. You write policies in

Rego↗
, feed it
JSON data, and it tells you whether your data satisfies your policy.

The key insight is that
Terraform can export its plan as JSON
:

terraform plan -out=plan.tfplan
terraform show -json plan.tfplan > plan.json

That JSON file contains
every resource change
Terraform intends to make:
what’s being created, updated, deleted, and the before/after values of each
attribute. It’s the same information a human reviewer would look at, in a
structured format a policy engine—like conftest—can evaluate:

conftest test plan.json

If the plan satisfies your policy, it passes. If it doesn’t, it fails with an
explicit reason.
The decision is auditable, testable, and reproducible.

An example policy

Here’s a Rego policy that only allows plans where every change is a no-op, a
resource create, or a data source read. Any update or delete fails the policy:

package main

import rego.v1

safe_actions := {"no-op", "create", "read"}

deny contains msg if {
some resource_change in input.resource_changes
some action in resource_change.change.actions
not action in safe_actions
msg := sprintf(
"resource %q has action %q, which is not in the safe set %v",
[resource_change.address, action, safe_actions],
)
}

This policy iterates over every
resource_changes
entry in the JSON-formatted
Terraform plan. For each one, it checks whether all of its actions are in the

safe_actions
set. If any action falls outside that set (an
update
or a

delete
), the policy emits a denial with the offending resource and action.

That’s it.
If this policy passes, the plan only creates new resources,
reads data sources, or does nothing
, so it’s safe to auto-apply. If it
fails, the pipeline stops and a human reviews.

Note:
depending on what Terraform providers you use,
new resource creation may not be completely harmless. Point here is that you
create your own policy to suit your organization’s definition of what a “safe to
auto-apply” plan means, as we will see below.

Wiring it into your pipeline

The CI/CD integration is straightforward. After Terraform plans, export the plan
to JSON, run
conftest
, and branch on the result:

terraform plan -out=plan.tfplan
terraform show -json plan.tfplan > plan.json

if conftest test plan.json; then
terraform apply plan.tfplan
else
# gate on human approval
fi

What makes this work well is that the decision boundary is
explicit
. You’re
not asking someone (or something) to judge whether a plan “looks safe”. You’re
checking whether it satisfies a set of rules you defined, tested, and versioned
alongside your infrastructure code.

Extending the policy

The example above is deliberately minimal: it only allows creates, data source
reads, and no-ops. In practice, you’ll want a richer policy, and the JSON
Terraform plan gives you plenty to work with:

Resource types.
Not all resources carry the same risk. You might auto-apply
changes to CloudWatch alarms, but always gate on RDS instances or IAM policies.
The
type
field on each
resource_changes
entry gives you this:

safe_resource_types := {"aws_cloudwatch_metric_alarm"}

deny contains msg if {
some resource_change in input.resource_changes
not resource_change.type in safe_resource_types
some action in resource_change.change.actions
action not in {"no-op", "read"}
msg := sprintf("resource %q has type %q, which is not in the auto-apply safe set", [resource_change.address, resource_change.type])
}

Resource fields.
Sometimes the resource type isn’t enough—you want to
auto-apply changes that only touch certain attributes. The
change
object in
the JSON plan let you diff individual fields. This policy denies any update that
modifies fields beyond
tags
:

deny contains msg if {
some resource_change in input.resource_changes
some action in resource_change.change.actions
action == "update"
changed_keys := {key |
some key in object.keys(resource_change.change.after)
resource_change.change.before[key] != resource_change.change.after[key]
}
changed_keys != {"tags", "tags_all"}
msg := sprintf("resource %q changes fields other than tags: %v", [resource_change.address, changed_keys])
}

Blast radius.
A plan that touches 2 resources is different from one that
touches 200. You can count the resources with actual changes and gate when the
number exceeds a given threshold:

max_auto_apply_changes := 10

deny contains msg if {
changed := {resource_change.address |
some resource_change in input.resource_changes
some action in resource_change.change.actions
action not in {"no-op", "read"}
}
count(changed) > max_auto_apply_changes
msg := sprintf("plan affects %d resources, which exceeds the auto-apply limit of %d", [count(changed), max_auto_apply_changes])
}

Environment.
Auto-apply in staging, gate in production. If your resources
are tagged with their environment, you can read that from the plan. This policy
denies any non-trivial change to a resource whose
Environment
tag is not

staging
:

deny contains msg if {
some resource_change in input.resource_changes
some action in resource_change.change.actions
action not in {"no-op", "read"}
resource_change.change.after.tags.Environment != "staging"
msg := sprintf("resource %q is not in staging, requires human review", [resource_change.address])
}

These rules compose. You can combine them in the same policy file, and
conftest

will evaluate all of them. A plan must pass
every
rule to auto-apply, and
any single denial is enough to fail the policy. The policy grows with your
confidence, and because it’s code, you can version it and test it like you do
with any other code.

A mechanism like this becomes ever
more important as you introduce AI
agents to your SDLC
, and let them propose and execute changes to your
live infrastructure. Without a deterministic way of attesting plan safety,
you
either compromise on confidence, velocity, or both
.

Thanks
for dropping by!

Did you find what you were looking for?

Let me know if you didn't.

Have a great day!
