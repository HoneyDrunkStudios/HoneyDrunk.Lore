---
source: "https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic"
title: "The text in Claude Code's “Extended Thinking” output is not authentic (3 minute read)"
author: "TLDR AI"
date_published: "Tue, 23 Jun 2026 00:00:00 GMT"
date_clipped: "2026-06-23"
category: "AI / LLM Research & Tooling"
source_type: "rss"
discovered_via: "https://tldr.tech/ai/2026-06-23"
source_role: "primary-via-tldr"
---

# The text in Claude Code's “Extended Thinking” output is not authentic (3 minute read)

Source: https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic

Posted on June 22, 2026 June 23, 2026 by patrick The text in Claude Code’s “Extended Thinking” output is not authentic. 
Claude Code records each session to disk. Those logs include “thinking blocks” — the model’s own reasoning as it works.
I went to inspect that reasoning this weekend and found a signature (600 characters long) and no text.
So I read the docs: https://platform.claude.com/docs/en/build-with-claude/extended-thinking 
Some details worth being aware of:
Claude encrypts its reasoning into that signature. 
Anthropic holds the key. Your machine doesn’t receive it. 
The API hands back a SUMMARY of reasoning, NOT the reasoning itself. 
Getting the full thinking output requires an enterprise agreement. 
Matt Green looked into this and has some more detailed observations on the signature blocks. 
This is worth knowing before you promise anyone an audit trail. Also- BEWARE: T he “extended-thinking” output from ctrl+o is a summary of Fable/Opus’ thinking. It isn’t the actual thinking that drove the model’s actions in a session- but a summary of the thinking logic. This is like saving a bmp as a .jpeg and then editing the .jpeg and saving it back as a .bmp. The conversion produces data loss. [edit: I originally had the order inverted, which triggered some HN readers. Apologies!]
I’m underwhelmed by how Anthropic is presenting the behavior of their application. If you ever need a record of the logic a used by YOUR AGENT during a session:
you can’t produce the logic using the local files. The reasoning logs on your system are not accessible to you. 
You can log the inputs, the outputs, and the actions of a running Claude code with some scrappy scraping- but even then- it’s not the actual reasoning that drove the agent’s behavior. 
And the language in the docs is awfully indirect. If you haven’t had your coffee, you might miss that “extended thinking returns a summary of Claude’s full thinking process”
Screenshot 
Performance improvements in Open Source models need to come faster. 
Related 
Categories Uncategorized Tags LLMs
