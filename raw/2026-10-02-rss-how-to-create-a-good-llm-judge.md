---
source: "https://newsletter.systemdesign.one/p/how-to-build-llm-judge"
title: "How to create a good LLM judge"
author: "Hamel Husain"
date_published: "2026-09-30"
date_clipped: "2026-10-02"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# How to create a good LLM judge

[We are in the middle of the agentic coding era, please take advantage of it (Partner)](https://blog.jetbrains.com/blog/2026/09/22/introducing-jetbrains-air/)

Coding agents are changing what it means to be a software engineer.

Typing code on a screen used to be a big part of the job. But now AI agents can handle more of that work.

The pattern of technological change is familiar:

*The mechanical part of work gets automated & human role moves up a layer.*

For software engineers, I think it means 3 things:

*You need to know what good looks like.*An agent can create a feature, fix a bug, and/or refactor code. But if you don’t know what good implementation looks like, you cannot tell whether the work should ship. The faster agents write code, the more your judgment matters.

*You need to learn how to manage multiple agents.*One developer can already give different tasks to different coding agents. That changes the job. You become responsible for:

giving context to agents,

directing their work,

checking results.


*You need a way to control this across the company.*Imagine all engineers in your company working this way…You need to know:

which “agents” people use,

what they’re doing & what they cost,

what happens when something goes wrong.



This is why I’m genuinely excited about JetBrains Air.

It gives you an environment for directing multiple coding agents & reviewing their work. So you can delegate more coding work without losing visibility/control.

Plus...

JetBrains Air Teams lets you coordinate software delivery workflows across engineers & agents. So engineering teams can manage agentic work across the development process.

JetBrains Air Governance gives organizations policies, visibility, auditability & cost management. So they can control how agents get used & maintain accountability for what ships.


And this works in a world where engineers use different agents & models.

i.e., you don’t have to bet everything on one provider.

**§**

Many AI outputs require subjective/domain-specific judgment.

A useful support response or a faithful summary is hard to grade with fixed rules in code[1](#footnote-1). People have to read & interpret these outputs. So repeating that review across many outputs takes time.

To reduce this review work, you can ask a large language model (**LLM**) to evaluate another model’s output. This use of a model is called *LLM-as-a-judge*. You give the judge the output & your evaluation criteria. It returns a decision, often with an explanation. This ability to automate subjective checks makes LLM-as-a-judge a “workhorse” in evals.

Onward.

**§**

I want to introduce ** Hamel Husain** as a guest author.

Hamel writes about AI evaluations and teaches the ** AI Evals course** with Shreya Shankar. In this newsletter, he explains how to build an LLM judge and check its decisions against human labels.

**§**

*Here’s what’s inside this newsletter:*

**A high judge score can still hide a broken evaluator.**Why a judge that looks accurate could completely miss the failures you actually care about.**Your human labels become the standard.**The decisions, critiques & rubrics that determine what your LLM judge should call Pass or Fail.**The examples your judge sees change its decisions.**Why some examples belong inside the prompt, while others must stay hidden until the final test.**One number won’t tell you whether your judge works.**The measurements that reveal how often it misses real failures & incorrectly flags good outputs.**Your judge gets stale as your AI product changes.**What happens to your evals when models, user behavior & evaluation criteria change over time.**A 6-step process takes you from real failures to a validated LLM judge.**The complete framework for choosing what to evaluate, defining the human standard, building the judge & checking whether you can trust its decisions.

[Share this letter](https://newsletter.systemdesign.one/p/how-to-build-llm-judge/?action=share)& I’ll send you some rewards for the referrals.

**§**

The judge can work alongside code-based checks:

Use code for checks with clear rules, such as whether an output follows the required format.

Use the judge for decisions that depend on meaning/context.


For example, code can check whether a support response contains the words *“I am sorry.”*

An LLM judge can assess whether the response addresses the customer’s frustration. Give the judge examples of acceptable responses so it can apply your support team’s standards.

Also code can check whether an answer includes a source link.

An LLM judge can compare the answer with the source to check whether the source supports the claim. Give the judge the source text so it has the evidence it needs.

For either task, the judge can make mistakes.

Before you rely on it, test whether its decisions match human judgments.

Even high agreement can hide these mistakes. If an error occurs in 5% of examples, a judge that always predicts Pass still has 95% agreement while detecting none of the errors.

To avoid this false confidence, measure whether the judge catches the failures that matter.

This newsletter starts with finding those failures and defining the human standard. It then shows how to build a judge prompt & test its decisions against that standard[2](#footnote-2).

**§**

**1. Choose a failure worth judging**

When you start building evals, it is tempting to use a metric[3](#footnote-3) someone else has already written.

Eval libraries offer ready-made scores for qualities such as helpfulness and coherence. You can run them on your outputs and get a score before deciding what a good result means for your product.

These metrics measure abstract qualities that may not matter for your use case.

Good scores on them do not mean your system works. For example, an answer might receive a high helpfulness score even though its sources do not support its claims[4](#footnote-4). You need a check for this specific failure.

Generic scores[5](#footnote-5) can still help you choose outputs to review…

For example, sort outputs by helpfulness & read some low-scoring examples. You may find a recurring problem worth checking. Read the outputs yourself to decide whether there is a failure and describe it. Keep some random examples in each review batch so you can find problems the generic score misses.

To decide which specific failures to check, review actual interactions and write notes about each problem. Then group similar problems into categories. This process is called **error analysis**[6](#footnote-6). Error analysis helps you decide what evals to write in the first place.

To understand an incorrect answer, you may need to see what happened before it.

Review the complete record of the user session, called a **trace**. It includes the user’s request & the model’s response, along with any tool calls and their results.

For example, several answers may include sources that do not support their claims. Group these cases under one failure category, such as “unsupported claims.” You can then decide whether that failure needs an automated check.

To find these patterns:

Gather about 100 traces that cover

*different*users & workflows.Then review at least 30 traces yourself.

As you read, write free-text notes about anything that seems “wrong” from the user’s perspective.


Do this initial review before reading an agent’s suggestions.

The agent may lack the product context you use to judge a good user experience. Its suggestions can direct your attention toward the problems it recognizes, causing you to miss failures it does not recognize.

After reviewing the first 30 traces, group similar failures and count the number in each category. Use your notes to ask the agent to search the remaining pool for similar examples. Review every suggestion yourself.

Continue until new traces stop revealing types of failure or changing your categories[7](#footnote-7).

The counts help you choose which failures to address first. For each failure, decide whether to fix it directly or build an automated check, often called an evaluator/eval.

Focus automated evaluators on failures that persist after fixing your prompts.

Teams sometimes discover their LLM doesn’t meet preferences they never specified, such as wanting short responses or a particular format.

Fix these obvious gaps first[8](#footnote-8).

Plus, choose the simplest check that can detect the failure.

For example, you can run generated code to check whether it produces the expected result. Use an LLM judge when the check requires human judgment.

An LLM judge needs labeled examples and ongoing maintenance[9](#footnote-9).

Before you can automate this judgment, you need a consistent human standard…

**§**

**2. Establish the human standard**

After choosing a failure to evaluate, you need to decide which outputs should “pass”.

People can disagree about whether the same output is acceptable. To establish a consistent standard, find the person who understands what a good result looks like for your product. A customer service director might be the right expert for a support assistant. An educational tool may need a teacher/curriculum developer.

For a small team, choose *one* domain expert to make final decisions about quality.

This reduces the work of coordinating several reviewers & resolving conflicting labels. The expert can incorporate input and feedback from others, but they drive the process. You then have a consistent standard to use when building and testing the judge.

The expert’s critiques also help uncover expectations people have not yet put into words. Use those critiques to define what the judge should check. If you are an independent developer with the relevant expertise, you can fill this role yourself.

Give the expert the information they need to evaluate each interaction.

That includes the user’s request & the model’s response. Depending on the task, they may also need results from tools or relevant information about the user. Present the relevant evidence together so they can review it without switching between several systems[10](#footnote-10).

**Use Pass and Fail, with a critique**

The expert needs a way to record each decision.

A 1-to-5 rating may seem useful for capturing degrees of quality. But the difference between adjacent points, like 3 versus 4, is often subjective and inconsistent across people labeling the outputs.

People can also default to middle values to avoid making a hard decision. Ask the expert to mark each example as `Pass`

or `Fail`

for the specific problem you are checking.

An evaluation with two possible labels is called *binary*.

Binary evaluations force clearer thinking & more consistent labeling. Besides the pass/fail decision, the domain expert should write a critique explaining their reasoning.

Use the same `Pass`

or `Fail`

outcomes for the judge. Each decision should answer one specific question about the output. A critique explains the decision; a middle score can leave it unclear whether the output is acceptable.

The critique identifies what caused the output to pass or fail and records the expectations the judge needs to follow.

You can still measure gradual improvement.

For example, you can track whether each expected fact appears in an answer. An answer that includes four of five expected facts passes four specific checks[11](#footnote-11).

**Expect your criteria to change**

Your evaluation criteria can change as you review outputs & discover expectations you hadn’t considered. (Shreya Shankar & her colleagues call this “criteria drift[12](#footnote-12).”)

Reviewing the judge’s critiques can help the expert notice inconsistencies in how they evaluate edge cases.

If several people label examples, check whether they apply the same standard…

Have these annotators label the same examples independently before they discuss them. Measure agreement and collect the cases where their labels differ. Discuss the rules for deciding Pass or Fail. These written rules are your rubric.

Update the rubric with a definition or example that covers the disputed case. Then relabel affected examples. If the annotators still disagree, assign a domain expert to make the final decision and record the reason[13](#footnote-13).

*Start with binary labels to understand what “bad” looks like.*

The expert’s labels & critiques give you the material for the judge’s prompt.

**§**

**§**

**3. Write a prompt from expert examples**

Use the expert’s critiques & evaluation rules to write the judge’s prompt.

Include labeled examples[14](#footnote-14) showing how to apply the rules to actual outputs.

Consider an assistant that turns a user’s request into a query for searching application data. The judge checks whether the generated query answers the request.

A user asks, *“show me slowest trace.”*

In this example, a trace records the steps an application takes to handle a request. The generated query found a maximum duration but didn’t group the data by each trace’s identifier.

It returned a duration without identifying the slowest trace[15](#footnote-15).

This shortened prompt includes the query & the expert’s critique.

Replace the placeholders with your application’s query-language information & evaluation guidelines[16](#footnote-16).

```
You are a query evaluator.
Evaluate whether the generated query answers the user’s request.
Here is information about the query language:
{{query_language_info}}
Here are the evaluation guidelines:
{{guidelines}}
Example evaluation:
<nlq>show me slowest trace</nlq>
<query>
{
“calculations”: [{”column”: “duration_ms”, “op”: “MAX”}],
“orders”: [{”column”: “duration_ms”, “op”: “MAX”,
“order”: “descending”}],
“limit”: 1
}
</query>
<critique>
{
“critique”: “While the query attempts to find the slowest trace
using MAX(duration_ms) and ordering correctly, it fails to group
by trace.trace_id. Without this grouping, the query only shows
the MAX(duration_ms) measurement over time, not the actual
slowest trace.”,
“outcome”: “Fail”
}
</critique>
For the following query, write a critique explaining your decision.
Then provide a Pass or Fail judgment in the same format as above.
<nlq>{{user_input}}</nlq>
<query>{{generated_query}}</query>
```


Include clear Pass examples alongside Fail examples to show the distinctions in your rubric.

Examples included in a prompt are often called “few-shot examples.”

Keep separate examples for testing the judge (described in the next section).

Keep each judge focused on one type of failure. Use separate judges for unrelated failures so you can see which behavior needs fixing[17](#footnote-17).

To check whether the prompt captures the expert’s judgment, compare their decisions on the same queries.

Put each user request and generated query in a spreadsheet with the judge’s critique and decision. Ask the expert to add their own critique and decision.

Use the disagreements to improve the prompt[18](#footnote-18).

**Give the judge the evidence it needs**

Some disagreements come from missing evidence.

To check a claim against a database, the judge needs the database result alongside the model’s answer. Your examples should contain the same information you use to evaluate.

Give each judge only the parts of the trace relevant to the failure it checks. Extra context can make its decisions *less* accurate.

Test your choices by comparing the judge’s decisions with human labels. Then, inspect disagreements to see whether the judge lacked necessary evidence or was distracted by irrelevant information.

Remove one piece of information at a time and check how the results change against human labels. If performance stays the same/improves, you may be able to leave it out.

Long-running agents can produce traces longer than the judge can read in one request. In those cases, consider giving the judge a tool to search for the parts it needs. Add this only when necessary, because it introduces more complexity & cost[19](#footnote-19).

You still need to check the judge on examples you did not use to develop its prompt.

**§**

**§**

**4. Check whether the judge catches failures**

A convincing critique can contain an incorrect decision.

Before relying on the judge, check how often its decisions match your domain expert. This check is called **validation**.

Run the judge on labeled examples you kept out of the prompt & inspect the mistakes[20](#footnote-20).

**Separate prompt development from the final test**

Repeated changes make a prompt work well on examples you use to develop it.

You also need to know how it performs on new examples… so keep a separate group for the final test.

The first 30 traces help you discover failures.

Yet testing the *judge* requires more labeled examples. Plan to label 100 to 200 examples for each type of failure. Reuse labeled traces from error discovery when they match that failure, then collect more until you reach that range. Include enough Pass & Fail examples to measure how well the judge recognizes each.

Split the labeled examples before you start revising the judge prompt[21](#footnote-21):

Training set contains examples you may put in the prompt. Here, “training” means choosing prompt examples. You do not change the model itself. Choose clear Pass and Fail examples with useful critiques.

The development set (dev set) is where you compare the judge with human labels while refining the prompt. Keep these examples out of the prompt.

Test set stays hidden until you finish revising the prompt. Freeze the prompt and run the judge on the test set once. Use the result as your final estimate of the judge’s performance.


Use 10 to 20 percent for train examples[22](#footnote-22) you may put in the prompt.

Use 40 to 45 percent for dev while refining the judge. Reserve the remaining 40 to 45 percent for one final test. The number of Pass and Fail examples is more useful than the percentage alone. Aim for 30 to 50 Pass examples and 30 to 50 Fail examples in both dev and test when possible.

A total of 100 examples cannot meet those targets for both dev & test. Collect more when you need better estimates, especially when failures are rare[23](#footnote-23).

On the dev set, read the disagreements. Check for missing rules or evidence. Clarify ambiguous examples and correct any mistaken human labels. Run the judge on the dev set again after each revision.

If you revise the prompt after seeing test results, those examples have become part of development. Reserve new examples for the next final check.

*The >90% target shown here is an example. Set targets based on the cost of missed failures and false alarms in your application.*

**Measure failures and passes separately**

The judge can miss a failure or incorrectly mark an acceptable output as Fail.

Measure these mistakes separately. Count Fail as a positive result because a failure is what you are trying to detect. Measure:

True positive rate (

**TPR**) is the fraction of human-labeled failures that the judge correctly marks Fail. This is also called*recall for failures*.True negative rate (

**TNR**) is the fraction of human-labeled passes that the judge correctly marks Pass.

Suppose your test set contains 50 human-labeled failures and 50 human-labeled passes. These numbers illustrate the calculation.

The judge catches 45 of 50 failures, so TPR is 90%.

It correctly passes 40 of 50 acceptable outputs, so TNR is 80%.

The judge from the opening, which always predicts Pass, has a TPR of 0% despite its 95% accuracy.

Report the counts alongside the rates.

A result based on a handful of failures gives you little evidence about performance on future failures. When using these rates to make decisions, include a range that accounts for uncertainty from testing only a sample.

If people review the outputs the judge flags, measure precision too. It answers, *“Of the examples flagged Fail, how many were failures according to the human?”* In the illustrative table, that is 45 out of 55, or about 82%. Precision also depends on how common failures are. A test set with equal numbers of passes and failures may produce a different precision from what you’ll see with real users[24](#footnote-24).

Your acceptable error rates depend on how you use the judge. Report TPR & TNR separately.

Use these same tests to compare the models you could use as your judge.

**§**

**5. Choose the model using human labels**

I like to use the most powerful model I can afford within my budget for cost & response time.

This budget might be different than my primary model, depending on the number of examples I need to score.

Using the same model is usually fine because the judge is doing a different task than your main LLM. The judges I recommend make specific Pass or Fail decisions.

Compare the judge with human labels[25](#footnote-25) to check whether it works[26](#footnote-26).

*Check the judge against human labels, even when it uses a different model.*

If the judge disagrees too often with human labels, inspect examples and prompt before trying another model.

You can optimize for cost later once you’ve established reliable evaluation criteria.

If prompt changes are not enough, you might consider further training the judge on labeled examples. This is called *fine-tuning*.

I prefer *not* to fine-tune LLM judges. I’d rather spend the effort fine-tuning the actual LLM instead[27](#footnote-27).

**What about TypeSafe’s Jev?**

[TypeSafe’s Jev](https://typesafe.ai/) has been very popular recently.

You may be wondering how it fits into this process. Jev returns decisions with probabilities, which makes it a useful example of how the same evaluation approach applies to different models.

An LLM judge is ultimately a “classifier”.

A classifier assigns an input to a category. In this newsletter, the input is an output you want to evaluate, and the categories are Pass and Fail. Choosing between two categories makes this a binary classifier.

You can use any approach you want to make those decisions, including Jev.

Validate the classifier against human labels so you know how well it works. Compare candidates on the same examples and measure TPR and TNR. You can then make a deliberate tradeoff between the mistakes each classifier makes and what it costs to run. For example, you might accept more missed failures for a lower cost, if those failures are inexpensive to fix.

Once the judge meets your requirements, keep checking it as your application changes.

**§**

**§**

**6. Keep the judge useful**

Changes to your application can produce outputs absent from the examples used to test the judge[28](#footnote-28).

So continue to check the judge against human labels as you use it to review new interactions. Read the failures it identifies to decide what to fix in your application.

I conduct this human review at regular intervals and whenever something material changes. For example, if I update a model, I’ll rerun the process. Your product’s criteria can also change as you see more outputs. Update the rubric and relabel affected examples when that happens.

Have the expert review a sample that reflects the interactions your users have. Give extra attention to cases where the judge is least reliable.

For example, if I find an error, I’ll search for more examples I think might trigger the same error. However, I also do a bit of random sampling. Use the random sample to estimate how often users encounter errors.

Eval datasets naturally get stale as your product and users change. Review new interactions to find problems and update your examples or reference answers[29](#footnote-29).

As your eval set changes, its scores may no longer be directly comparable with older scores. Track what changed before interpreting a higher or lower pass rate.

**§**

**Before you rely on the judge**

Check these points before using the judge’s scores to make product decisions:

Choose a specific failure you have observed in real outputs.

Have a domain expert label examples Pass or Fail and explain each decision.

Build the prompt from those rules and examples. Keep separate examples for the final test.

Measure how often the judge catches failures and accepts good outputs. Report the counts with the rates.

Repeat human review when your application or evaluation criteria change.


If the judge misses too many failures or flags too many acceptable outputs, review the disagreements before using its scores.

**§**

Thanks to ** Hamel** for writing this newsletter.

Read his [LLM judge guide](https://hamel.dev/blog/posts/llm-judge/) and [Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) for more examples. He teaches the [AI Evals course](https://maven.com/parlance-labs/evals?promoCode=SYSTEMDESIGNONE-C7) with Shreya Shankar.

If you find this newsletter valuable, share it with a friend, and subscribe if you haven’t already. There are [group discounts](http://newsletter.systemdesign.one/subscribe?group=true), [gift options](http://newsletter.systemdesign.one/subscribe?gift=true), and [referral rewards](https://newsletter.systemdesign.one/leaderboard) available.

Thank you for supporting this newsletter.

You are now 250,001+ readers strong, very close to 251k. Let’s try to get 251k readers by 7 October. Consider sharing this letter with your friends and get rewards.

Y’all are the best.

[1](#footnote-anchor-1)

**Code** means traditional software logic written with explicit rules.

[2](#footnote-anchor-2)

Hamel Husain, [Using LLM-as-a-Judge for Evaluation](https://hamel.dev/blog/posts/llm-judge/). The query prompt is shortened and generalized, with its outcome label changed to Fail.

[3](#footnote-anchor-3)

A** metric** measures some quality of an AI output and turns it into a **score/result**.

**Helpfulness:**How useful is the answer?**Coherence:**Does the answer make sense?**Faithfulness:**Does the answer stay supported by the provided source?**Relevance:**Does the answer address the question?

[4](#footnote-anchor-4)

Because **“helpfulness” and “source support” measure different properties**.

Imagine the user asks:


“Why did our database latency increase?”

AI answers:


“The latency increased because traffic doubled during the deployment. Adding read replicas would reduce the load.”

That answer could look clear, relevant, and actionable. A generic **helpfulness evaluator** could therefore give it a high score.

But provided source only says:


“Database latency increased from 50 ms to 120 ms.”

The source says nothing about traffic doubling or read replicas. AI invented the explanation.

So you could have:

```
Helpfulness check → Pass
The response appears useful.
Source-support check → Fail
The source does not support the response’s claims.
```


[5](#footnote-anchor-5)

Think of a generic score as a *filter that helps you decide what to inspect first.*

Say you have 1,000 AI responses. A helpfulness score marks 50 of them as low quality.

Read some of those 50 yourself. You could notice the same failure several times, such as answers that ignore part of the user’s question. Now you have found a specific problem worth checking with an eval.

But the helpfulness score could miss other problems. So also review some random responses to discover failures the score did not catch.

[6](#footnote-anchor-6)

Imagine you have an AI customer support agent. You review 100 real conversations and write down every problem you see:

8 responses gave the wrong refund policy.

5 responses ignored part of the customer’s question.

4 responses invented information.

3 responses were too long.


You then group similar problems into categories such as wrong policy, incomplete answer, and unsupported claims.

This process is **error analysis**.

It tells you which problems actually occur in your AI system. You then create **evals** to detect the important problems automatically.

So the flow is:

`Review real interactions → find problems → group similar problems → create evals for those failures.`


[7](#footnote-anchor-7)

Hamel Husain, [Why error analysis is important and how to perform it](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html).

[8](#footnote-anchor-8)

TLDR--Choose a failure worth judging (Personal notes from Neo):

Start with real failures, rather than generic metrics, such as helpfulness or coherence.

Review real traces & use error analysis to group recurring problems into failure categories.

Start with about 100 traces and manually review at least 30 before using an agent to help find similar failures.

Prioritize failures by how often they occur. Fix obvious prompt problems first.

Build an automated eval only for important failures that persist and require repeated checking.


[9](#footnote-anchor-9)

Hamel Husain, [Should I build automated evaluators for every failure mode?](https://hamel.dev/blog/posts/evals-faq/should-i-build-automated-evaluators-for-every-failure-mode-i-find.html).

[10](#footnote-anchor-10)

TLDR--Establish the human standard (Personal notes from Neo):

Choose one domain expert to define what good output looks like & make final quality decisions.

Use binary Pass/Fail labels for each specific failure, plus a critique explaining the decision.

Turn the expert’s decisions and critiques into a rubric the LLM judge should follow.

Expect criteria drift as you discover new cases. Update the rubric and relabel affected examples.

If annotators disagree, discuss the cases, refine the rubric, and let the domain expert make the final decision.


[11](#footnote-anchor-11)

Hamel Husain, [Why use binary evaluations instead of 1-to-5 ratings?](https://hamel.dev/blog/posts/evals-faq/why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales.html).

[12](#footnote-anchor-12)

Hamel Husain, [A field guide to rapidly improving AI products](https://hamel.dev/blog/posts/field-guide/), discussing Shreya Shankar and colleagues' research on criteria drift.

[13](#footnote-anchor-13)

Hamel Husain, [How many people should annotate outputs?](https://hamel.dev/blog/posts/evals-faq/how-many-people-should-annotate-my-llm-outputs.html).

[14](#footnote-anchor-14)

Think of the **judge’s prompt** as an instruction manual for the LLM judge.

**Evaluation rules:**The rules that define what counts as Pass or Fail.Example: “The generated query must answer the user’s full request.”

Example: “If the query misses required information, mark it Fail.”


**Labeled examples:**Real examples where a human expert has already decided the correct result.User asks: “Show me the slowest trace.”

Generated query fails to identify the trace.

Human label: Fail

Critique: “The query finds the maximum duration but does not identify which trace had it.”



The LLM judge learns from both:

```
Evaluation rules = what to look for
Labeled examples = what those rules look like in practice
```


[15](#footnote-anchor-15)

Imagine you have an AI assistant that converts plain English into database queries.

You ask:


“Show me the slowest trace.”

A **trace** is the record of everything an application did while handling one request. Each trace has an ID and a duration.

Suppose the data looks like this:

```
Trace A → 2 seconds
Trace B → 8 seconds
Trace C → 4 seconds
```



The correct answer should identify:

Trace B → 8 seconds


But the generated query only calculates:

Maximum duration → 8 seconds


It does not return Trace B.

So the query found the longest duration, but it failed to answer which trace was the slowest. The LLM judge should therefore mark the query Fail.

[16](#footnote-anchor-16)

Hamel Husain, [Using LLM-as-a-Judge for Evaluation](https://hamel.dev/blog/posts/llm-judge/). The query prompt is shortened and generalized, with its outcome label changed to Fail.

[17](#footnote-anchor-17)

It means giving each LLM judge one specific job.

Suppose your AI customer-support agent has three possible failures:

**Judge 1: Factual accuracy**→ Did the response contain incorrect information?**Judge 2: Completeness**→ Did it answer the user’s full question?**Judge 3: Source support**→ Does the provided source support the claims?

Instead of asking one judge:

“Is this response good overall?”


you run three focused judges. Then you could get:

```
Factual accuracy → Pass
Completeness → Fail
Source support → Pass
```



[18](#footnote-anchor-18)

TLDR--Write a prompt from expert examples (Personal notes from Neo):

Build the judge’s prompt from the expert’s evaluation rules, critiques & labeled examples.

Include clear Pass & Fail few-shot examples so the judge sees how to apply the rubric.

Keep each judge focused on one specific failure. Use separate judges for unrelated failures.

Compare the judge’s decisions with human labels & use disagreements to improve the prompt.

Give the judge only the evidence it needs. Remove irrelevant context that could hurt accuracy.

Test the final judge on new examples you did not use to develop its prompt.


[19](#footnote-anchor-19)

Hamel Husain, [How much context should I give an LLM judge?](https://hamel.dev/blog/posts/evals-faq/how-much-of-a-trace-should-i-give-an-llm-judge.html).

[20](#footnote-anchor-20)

TLDR--Check whether the judge catches failures (Personal notes from Neo):

Validate the judge by comparing its decisions with human-labeled examples.

Split labeled examples into training, dev & test sets before you start refining the prompt.

Use the training set for prompt examples, the dev set to improve the prompt & the hidden test set for the final evaluation.

Measure failures & passes separately with true positive rate (TPR) & true negative rate (TNR). Add precision when you care about how many flagged outputs are real failures.

Inspect disagreements on the dev set to find missing rules, missing evidence & incorrect human labels.

Keep the test set untouched. If you use its results to change the prompt, create a new test set for the next final evaluation.

Report sample counts alongside the metrics & choose acceptable error rates based on the cost of missed failures and false alarms.


[21](#footnote-anchor-21)

Think of it like studying for an exam. You split your labeled examples into three groups:

**Training set = examples you study from**Put some of these Pass/Fail examples directly in the judge’s prompt.

They teach the judge what good and bad outputs look like.

You are not training the LLM itself.


**Development set = practice exam**Run the judge on these examples.

Compare its answers with the correct human labels.

When it makes mistakes, improve the prompt and try again.

Never put these examples into the prompt.


**Test set = final exam**Keep these examples hidden while you improve the prompt.

Once you finish, freeze the prompt and run it on the test set.

This tells you how well the judge performs on unseen examples.



So the workflow is:

`Training set → build prompt → Dev set → improve prompt → Test set → measure final performance.`


[22](#footnote-anchor-22)

It means the percentage of your total collection of human-labeled examples for that specific failure.

For example, suppose you have 200 labeled examples:

**10–20% training set:**20–40 examples used to help build the judge prompt.**40–45% dev set:**80–90 examples used to test and improve the prompt.**40–45% test set:**80–90 examples kept hidden for the final evaluation.

So if you choose 10/45/45:

`200 total labeled examples → 20 train + 90 dev + 90 test`


[23](#footnote-anchor-23)

Hamel Husain, [How many examples do I need for an eval?](https://hamel.dev/blog/posts/evals-faq/how-many-examples-do-i-need-for-an-eval.html).

[24](#footnote-anchor-24)

Hamel Husain, [The revenge of the data scientist](https://hamel.dev/blog/posts/revenge/) and the validation section of his [LLM judge guide](https://hamel.dev/blog/posts/llm-judge/#how-do-you-validate-an-llm-judge-against-human-labels). The 100-example table is illustrative arithmetic.

[25](#footnote-anchor-25)

Hamel Husain, [Can I use the same model for the task and evaluation?](https://hamel.dev/blog/posts/evals-faq/can-i-use-the-same-model-for-both-the-main-task-and-evaluation.html).

[26](#footnote-anchor-26)

TLDR--Choose the model using human labels (Personal notes from Neo):

Start with the most powerful judge model your cost & response-time budget allows.

Validate every judge against the same human-labeled examples, even if you use a different model from your main LLM.

If the judge disagrees too often with humans, inspect the prompt & examples before switching models.

Compare judge models using TPR & TNR, then balance accuracy, cost & response time.

Avoid fine-tuning the judge unless prompt improvements fail. Prioritize improving the main LLM instead.

Treat the judge in this guide as a binary classifier: it classifies each output as Pass or Fail.

Jev fits the same process. Validate its decisions against human labels & compare its errors and cost with other judge models.


[27](#footnote-anchor-27)

Hamel Husain, [Using LLM-as-a-Judge for Evaluation](https://hamel.dev/blog/posts/llm-judge/). The query prompt is shortened and generalized, with its outcome label changed to Fail.

[28](#footnote-anchor-28)

TLDR--Keep the judge useful (Personal notes from Neo):

Keep validating the judge against human labels as your application changes.

Rerun human reviews after major changes, such as switching the model.

Update the rubric & relabel affected examples when your evaluation criteria change.

Review real user interactions, with extra attention to cases where the judge performs poorly.

Use targeted examples to investigate known errors & random samples to discover unexpected ones.

Refresh stale eval datasets with new interactions, examples & reference answers.

Track changes to your eval set because newer scores may not be directly comparable with older scores.


[29](#footnote-anchor-29)

Hamel Husain, [What should I do when my eval dataset becomes stale?](https://hamel.dev/blog/posts/evals-faq/what-should-i-do-when-my-gold-eval-dataset-becomes-stale.html)
