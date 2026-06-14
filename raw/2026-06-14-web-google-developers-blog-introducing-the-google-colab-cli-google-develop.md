---
source: "https://developers.googleblog.com/introducing-the-google-colab-cli/"
title: "Introducing the Google Colab CLI- Google Developers Blog"
author: "Google Developers Blog"
date_published: "2026-06-05"
date_clipped: "2026-06-14"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Introducing the Google Colab CLI- Google Developers Blog

Source: https://developers.googleblog.com/introducing-the-google-colab-cli/

Today we are announcing the [Google Colab Command-Line Interface](https://github.com/googlecolab/google-colab-cli) (CLI), which bridges the gap between your local terminal and remote Colab runtimes, providing a zero-friction execution platform for both developers and AI agents. The Colab CLI offers:

`colab --gpu A100`

or `colab --gpu T4`

).`colab exec`

.`.ipynb`

logs via `colab download`

and `colab log`

.`colab repl`

or `colab console`

.Because the Colab CLI integrates seamlessly into standard terminal environments, it can be used by any agent with terminal access. To ensure your AI assistants can hit the ground running, the CLI includes a prepackaged Colab [skill file](https://github.com/googlecolab/google-colab-cli/blob/main/COLAB_SKILL.md) that provides agents with instant, built-in context on exactly how to leverage the CLI. Let's look at a real life example of something a user or agent might try with the Colab CLI.

*Note that while the example below highlights [Antigravity](https://antigravity.google/) agent using Colab CLI as a tool, Colab CLI can easily be used by Claude Code, Codex, and other agents.

Here is how an Agent can use the Colab CLI for a real-world ML workflow:

The CLI can be used to run a real QLoRA pipeline that runs end-to-end with just a handful of commands. Offload heavy computational lifting to a GPU without typing a single cloud provisioning command by Instructing Antigravity (or your agent of choice) to build a remote fine-tuning job. In this scenario, we ask our agent to use the Colab CLI to fine-tune [google/gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it) on a [Text-to-SQL dataset](https://huggingface.co/datasets/philschmid/gretel-synthetic-text-to-sql) to make the model better at writing SQL queries.

**The Antigravity prompt:**

Use the Colab CLI (https://github.com/googlecolab/google-colab-cli) to fine-tune Gemma 3 1B using QLoRA. Provision a Colab T4 GPU instance, install the necessary ML packages (transformers, datasets, peft, trl, etc.), run my local ~[finetune_run](https://github.com/googlecolab/google-colab-cli/blob/main/examples/finetune_run.py)[.py](https://gist.github.com/spencersgoogle/05be7d5b8a86785284a72032d11e7214) script remotely, download the resulting safetensors adapter, save the notebook log, and cleanup.

**Antigravity executes:**

```
$ colab new --gpu T4
$ colab install transformers datasets peft trl bitsandbytes accelerate
$ colab exec -f finetune_run.py
$ colab log --output gemma_finetune_log.ipynb
$ colab stop
```


Antigravity also uses the "colab download" command to download the adapter model, adapter config, tokenizer config, and tokenizer, which can be used to load and run your fine-tuned model locally. Now you have a remotely fine-tuned model ready to serve from your local device!

The Colab CLI makes powerful Colab compute accessible, programmable, and agent-ready. It is lightweight and easily accessible to any terminal-based AI agent. To start using the Colab CLI yourself, head over to the [Google Colab CLI GitHub repository](https://github.com/googlecolab/google-colab-cli) for setup instructions.

We are excited to see how this accelerates your development process and look forward to seeing what you and your agents build!
