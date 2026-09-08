---
source: "https://newsletter.systemdesign.one/p/api-testing-types"
title: "I struggled with “API testing” until I learned these 53 techniques"
author: "Neo Kim"
date_published: "2026-08-31"
date_clipped: "2026-09-08"
category: "Software Architecture"
source_type: "rss"
---

# I struggled with “API testing” until I learned these 53 techniques

Source: https://newsletter.systemdesign.one/p/api-testing-types

I struggled with “API testing” until I learned these 53 techniques #173: Part 1 - smoke testing, functional testing, unit testing, and 22 others. Neo Kim Aug 31, 2026 ∙ Paid 70 15 Share
Get my system design playbook for FREE on newsletter signup:
Subscribe Share this letter & I’ll send you some rewards for the referrals.
Some of these are foundational, and some are quite advanced. ALL of them are super useful to engineers building production-ready systems.
Curious to know how many were new to you:
Smoke Testing
Functional Testing
Unit Testing
Integration Testing
End-to-end testing
Regression Testing
Acceptance Testing
Negative Testing
Boundary Testing
Validation Testing
Exploratory Testing
Contract Testing
Consumer-Driven Contract Testing
API Contract Mocking
Load Testing
Stress Testing
Performance Testing
Spike Testing
Soak/Endurance Testing
Scalability Testing
Latency Testing
Concurrency Testing
Security Testing
Authentication Testing
Authorization Testing
For each, I’ll share:
What it is & how it works in simple words
A real-world analogy
Tradeoffs
Why it matters
Let’s go!
§ Make your agents realtime (Partner) Agents are killing your apps with compounding latency across workflows.
Your customers want their agent workflows to be efficient, so you’re losing deals if you don’t make them event-driven. Webhooks solve this issue, but implementing them is harder than it looks.
If you homebrewed your webhooks and are getting pinged at 4 in the morning for failed deliveries, this is for you.
Svix handles everything: retries, idempotency, security, and compliance. Qualified startups get $12,000 in free credits.
Get started for free
(Thanks to Svix for partnering on this newsletter.)
§ 1. Smoke Testing Smoke testing is the first sanity check you run after a new build/deployment. You pick the most critical endpoints: a health check, a login, a basic read, and confirm the API responds at all.
It runs first in your CI pipeline.
If it fails, everything else stops. No point running 500 detailed tests on a broken build. A passing smoke test only means the API responded, NOT that it responded correctly.
So you cannot rely on smoke tests alone & call it safe.
Analogy Before a surgeon begins a 6-hour operation, they confirm the patient’s vitals are stable…Not a full diagnosis, but is the patient ready to proceed?
Smoke testing is that vital check before you invest deeper.
Tradeoff Smoke tests are lightning fast and simple. They give instant feedback on failures before they ripple through a QA pipeline.
But simplicity is also their limitation. They are a first gate, not a full safety net.
Why it matters Every minute a broken build spends in a QA pipeline wastes someone’s time.
Smoke testing is the cheapest guard you can put at the gate.
Run them first in every CI pipeline. If they fail, stop everything else immediately!
2. Functional Testing Functional testing holds the API accountable to its specification. For every endpoint, you define what valid input looks like, what the response must contain, and what status code should come back. Then you verify if the API delivers it.
This includes happy paths and unhappy paths.
What happens when required fields are missing?
…When the auth token is invalid?
…When the payload is structurally wrong?
Analogy Imagine a vending machine:
Functional testing is inserting the right coins, pressing the right button, and confirming the right snack drops.
Then inserting too few coins, pressing a sold-out item, and confirming the machine rejects it cleanly without eating your money.
Tradeoff Functional tests give you direct, verifiable confidence in your API’s behavior.
They’re the key safety net for catching broken contracts before a consumer sees them. Yet the catch is the maintenance costs. Poorly written functional tests become a tax: fragile, brittle, and constantly breaking on harmless changes.
Why it matters Consumers build products on top of your API, trusting it behaves as documented.
Functional tests enforce trust internally every time code changes. Assert what truly matters to clients, not every incidental implementation detail.
3. Unit Testing Unit testing isolates the pieces of your API logic: single handler, validation function, data transformer, and verifies them independently.
No real database, no real network… Just the logic, tested in a controlled environment with mocked dependencies.
Analogy Before assembling a watch, a craftsman tests each gear wheel individually on a flat surface.
You cannot judge the full watch until you trust the components individually.
Tradeoff Unit tests are the fastest tests you will ever write.
They run in milliseconds and give instant feedback during development, enabling fearless refactoring. Yet the risk is over-reliance.
Mocks do not always reflect reality, and a codebase with 100% unit test coverage can still fail catastrophically when components interact.
Why it matters Unit tests form the foundation of the testing pyramid.
They catch logic bugs before they compound into harder-to-debug integration failures.
Use them for all pure logic: validators, transformers, calculators, and business rules.
4. Integration Testing Integration testing verifies if different parts of the system work correctly “together”.
Instead of testing a single endpoint in isolation, you chain a sequence of API calls that reflect a real workflow: create a resource, read it back, update it, and delete it .
Then you confirm the entire sequence produces correct state. These tests touch realistic versions of your databases, queues, and dependent services.
Analogy A chef does not just taste each ingredient separately…
Before serving a dish, they cook the full recipe, taste the result, and confirm the combined flavors work together.
Integration testing is that final cook-and-taste step before the plate leaves the kitchen.
Tradeoff Integration tests catch an entire class of bugs that unit tests are structurally incapable of finding: serialization mismatches, transaction failures, auth token propagation errors.
But they are slower, need more infrastructure, and sensitive to environmental issues. One “flaky” dependency can make the entire suite unreliable.
Why it matters In distributed systems, the bugs that cause the worst incidents rarely live inside a single function.
They live in the seams between systems. So keep a small, critical integration suite per workflow and run heavier scenarios on a nightly schedule.
5. End-to-End (E2E) Testing End-to-end testing validates a complete user journey through the entire system, exactly as a real user would experience it.
Unlike integration tests, you hit the “real” API, which calls real services, writes to a real database, and returns a real response.
Analogy A car manufacturer does not just test the engine on a stand and/or the brakes on a rig.
Before shipping a vehicle, a test driver takes it on the road, through traffic, over speed bumps, at highway speed, to confirm the whole car behaves as designed in the real world.
Tradeoff E2E tests are the most realistic tests you can run, which makes them the most trustworthy signal before a release.
But they are the most expensive to maintain. Flaky environments, test data management & slow execution times make large E2E suites painful.
Why it matters Individual services can all pass their own tests while the complete user journey still fails.
E2E tests are the last line of defense before users become your testers. Keep the suite small and focused on the most critical business journeys only.
6. Regression Testing Regression testing reruns a set of existing tests every time new code gets merged. This confirm nothing previously working has been broken .
It’s less about testing new functionality & more about protecting what already works.
Analogy A musician who mastered a repertoire runs through it before every performance.
This is not to learn the pieces, but to catch any drift/forgotten fingering that crept in during recent practice of new material.
Tradeoff Regression tests are the institutional memory of your API.
They compound in value over time, catching the “should not have touched that” changes.
Without discipline, a regression suite becomes slow & unmaintainable.
Why it matters The most common source of production bugs is not new features…but unintended side effects of changes to existing code.
Run regression tests automatically on every merge request & block merges on failures.
7. Acceptance Testing Acceptance testing is the final verification the API delivers what was agreed upon before development began.
It tests against business criteria & user requirements, not just technical specifications.
The question is not “does it work?” but “does it do what we promised?”
Analogy A tailor finishing a bespoke suit does not just check the stitching.
They have the client try it on against the original measurements & requirements.
The technical craft could be perfect, but if the suit does not fit the client’s needs,,, the job is not done.
Tradeoff Acceptance tests provide the highest level of business confidence of any testing type.
They close the gap between a technical specification & a business requirement.
But they require close collaboration between technical & non-technical stakeholders. Plus, they are too slow and coarse to run on every commit.
Why it matters Teams can spend weeks building an API that works perfectly from a technical standpoint but completely misses the actual business need…
Use acceptance tests as the final sign-off before a feature ships to production.
§ Reminder: this is a teaser of the subscriber-only newsletter, exclusive to my golden members.
When you upgrade, you’ll get:
High-level architecture of real-world systems.
Deep dive into how popular real-world systems work.
How real-world systems handle scale, reliability, and performance.
Unlock Full Access
(If this newsletter has helped you become a better software engineer, consider subscribing to support my work.)
§ 8. Negative Testing Keep reading with a 7-day free trial Subscribe to The System Design Newsletter to keep reading this post and get 7 days of free access to the full post archives.
Start trial Already a paid subscriber? Sign in Previous Next
