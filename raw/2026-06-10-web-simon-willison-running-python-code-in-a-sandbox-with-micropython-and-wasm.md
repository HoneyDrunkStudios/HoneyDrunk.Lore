---
source: "https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/"
title: "Running Python code in a sandbox with MicroPython and WASM"
author: "Simon Willison"
date_published: "2026-06-06"
date_clipped: "2026-06-10"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Running Python code in a sandbox with MicroPython and WASM

Source: https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/

# [Simon Willison’s Weblog](/)

[Subscribe](/about/#subscribe)

**Sponsored by:** AWS — If you're building with AI, AWS Summit NYC on June 17 is the room you want to be in. 200+ sessions. Totally free. [Register here](https://bit.ly/4a9sUYg)

## Running Python code in a sandbox with MicroPython and WASM

6th June 2026

I’ve been experimenting with different approaches to running code in a sandbox for several years now, but my latest attempt feels like it might finally have all of the characteristics I’ve been looking for. I’ve released it as an alpha package called [micropython-wasm](https://github.com/simonw/micropython-wasm), and I’m using it for a code execution sandbox plugin for [Datasette Agent](https://github.com/datasette/datasette-agent) called [datasette-agent-micropython](https://github.com/datasette/datasette-agent-micropython).

- [Why do I want a sandbox?](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#why-do-i-want-a-sandbox-)
- [What I want from a sandbox](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#what-i-want-from-a-sandbox)
- [WebAssembly looks really promising here](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#webassembly-looks-really-promising-here)
- [MicroPython in WebAssembly](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#micropython-in-webassembly)
- [Building the first version](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#building-the-first-version)
- [Try it yourself](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#try-it-yourself)
- [Should you trust my vibe-coded sandbox?](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#should-you-trust-my-vibe-coded-sandbox-)

#### Why do I want a sandbox?

My key open source projects—[Datasette](https://datasette.io/), [LLM](https://llm.datasette.io/), even [sqlite-utils](https://sqlite-utils.datasette.io/)—all support plugins.

I absolutely love plugins as a mechanism for extending software. A carefully designed plugin system reduces the risk involved in trying new things to almost nothing—even the wildest ideas won’t leave a lasting influence on the core application itself. My software can grow a new feature overnight and I don’t even have to review a pull request!

There’s one major drawback: my plugin systems all use Python and [Pluggy](https://pluggy.readthedocs.io/en/latest/), and plugin code executes with full privileges within my applications. A buggy or malicious plugin could break everything or leak private data.

I’d love to be able to run plugin-style code in an environment where it is unable to read unapproved files, connect to a network, or generally operate in a way that’s risky or harmful to the rest of the application or the user’s computer.

My interest covers more than just plugins. For Datasette in particular there are many features I’d like to support where arbitrary code execution would be useful. I’ve already experimented with this for [Datasette Enrichments](https://enrichments.datasette.io/), where code can be used to transform values stored in a table. I’d love to build a mechanism where you can run code on a schedule that fetches JSON from an approved location, runs a tiny bit of code to reformat it into a list of dictionaries, then inserts those as rows in a SQLite database table.

#### What I want from a sandbox

My goal is to execute code safely within my own Python applications. Here’s what I need:

- Dependencies that **cleanly install from PyPI**, including binary wheels across multiple platforms if necessary. I don’t want people using my software to have to take any extra steps beyond directly installing my Python package.
- Executed code must be subject to both **memory** and **CPU** limits. I don’t want `while True: s += "longer string"` to crash my application or the user’s computer.
- **File access must be strictly controlled**. Either no filesystem access at all or I get to define exactly which files can be read and which files can be written to.
- **Network access is controlled as well**. Sandboxed code should not be able to communicate with anything without going through a layer I fully control.
- Support for interaction with **host functions**. A sandbox isn’t much use if I can’t carefully expose selected platform features to the code that it’s running.
- It has to be **robust, supported, and clearly documented**. I’ve lost count of the number of sandbox projects I’ve seen in repos with warnings that they aren’t actively maintained!

#### WebAssembly looks really promising here

Web browsers operate in the most hostile environment imaginable when it comes to malicious code. Their job is to download *and execute* untrusted code from the web on almost every page load.

Given this, JavaScript engines should be excellent candidates for sandboxes. Sadly those engines are also extremely complicated, and are not designed for easy embedding in other projects. Most of the V8-in-Python projects I’ve seen are infrequently maintained and come with warnings not to use them with completely untrusted code.

WebAssembly is a *much better* candidate. It was designed from the start to support all of the characteristics I care about and has been tested in browsers for nearly a decade. The [wasmtime](https://pypi.org/project/wasmtime) Python library brings WASM to Python, is actively maintained, and has binary wheels.

#### MicroPython in WebAssembly

WebAssembly engines like wasmtime run WebAssembly binaries. Some programming languages like Rust are easy to compile directly to WebAssembly. Dynamic languages like JavaScript and Python are harder—they support language primitives like `eval()`, which means they need a full interpreter available at runtime.

To run Python we need a full Python interpreter compiled to WebAssembly, wired up in a way that makes it easy to feed it code, hook up host functions and access the results.

Pyodide offers an outstanding package for running Python using WebAssembly in the browser, but using Pyodide in server-side Python isn’t supported. The most recent advice I could find was [from October 2024](https://github.com/pyodide/pyodide/discussions/5145) stating “Pyodide is built by the Emscripten toolchain and can only run in a browser or Node.js”.

The other day I decided to take a look at [MicroPython](https://micropython.org) as an option for this. The MicroPython site says:

> MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.

WebAssembly sure feels like a constrained environment to me!

#### Building the first version

I had GPT-5.5 Pro [do some research for me](https://chatgpt.com/share/6a1e2a5c-58b8-8328-ba1c-0e6aadb0a051), which turned up [this PR against MicroPython](https://github.com/micropython/micropython/pull/13676) by [Yamamoto Takahashi](https://github.com/yamt) titled “Experimental WASI support for ports/unix”.

It then produced this [research.md document](https://github.com/simonw/micropython-wasm/blob/c08fbd2276b15dc8c9bdff82845f750971f45647/research.md), so I let Codex Desktop and GPT-5.5 high [loose on it](https://gist.github.com/simonw/27461a16d76f28f8619c609444d544fe) to see what would happen:

> `read the research.md document and build this. You will probably need to write a script that compiles a custom WASM version of MicroPython as part of this project - fetch the MicroPython code to a /tmp directory for this as part of that script.`

It worked. I now had a prototype Python library that could execute Python code inside a WebAssembly sandbox!

The trickiest piece to solve was persistent interpreter state. The WASM build we are using here exposes a single entry point which starts the interpreter, runs the code and then stops the interpreter at the end.

This works fine for one-off scripts, but for Datasette Agent I want variables and functions to stay resident in memory so I can reuse them across multiple code execution calls.

A neat thing about working with coding agents is that you can get from an idea to a proof of concept quickly. I prompted:

> `For keeping variables resident: what if we ran code inside micropython itself which called a host function get_next_python_code() and then passed that to eval() - and that host function blocked until new code was available, maybe by running in a thread with a queue? Could that or a similar idea help here?`

After some iteration we got to a version of this that works! In Python code you can now do this:

```
from micropython_wasm import MicroPythonSession

with MicroPythonSession() as session:
    print(session.run("x = 10\nprint(x)").stdout)
    print(session.run("x += 5\nprint(x)").stdout)
    print(session.run("print(x * 2)").stdout)
```

Under the hood this starts a thread, sets up a request queue and then sends messages to that queue for the `session.run()` command, each time waiting on a reply queue for the result of that execution. Inside WASM the MicroPython interpreter blocks waiting for a `__session_next__()` host function to return the next line of code, which it runs `eval()` on before calling `__session_result__({"id": request_id, "ok": True})` when each block has been successfully executed.

The other piece of complexity was supporting host functions, so my Python library could selectively expose functions that could then be called by code running in MicroPython.

Codex ended up solving this with [78 lines of C](https://github.com/simonw/micropython-wasm/blob/0.1a1/micropython_wasm/usercmodule/host/hostmodule.c), which ends up compiled into the [362KB WebAssembly blob](https://github.com/simonw/micropython-wasm/blob/0.1a1/micropython_wasm/artifacts/micropython-wasi.wasm) I’m distributing with the package.

I am by no means a C programmer, but I’ve read the C and had two different models explain it to me (here’s [Claude’s explanation](https://claude.ai/share/62f74371-cc3c-44f2-b406-33d03513de9e)) and I’ve subjected it to a barrage of tests.

The great thing about working with WebAssembly is that if the C turns out to be fatally flawed the worst that can happen is the WebAssembly execution will fail with an exception. I can live with that risk.

Memory limits are directly supported by wasmtime. CPU limits are a little harder: wasmtime offers a “fuel” concept to limit how many operations a WebAssembly call can execute, and that’s the correct fit for this problem, but the units are hard to reason about. I’m experimenting with a 20 million default “fuel” setting now but I’m not confident that it’s the most appropriate value.

#### Try it yourself

The `micropython-wasm` alpha is now [live on PyPI](https://pypi.org/project/micropython-wasm).

You can try it from your own Python code as [described in the README](https://github.com/simonw/micropython-wasm). I’ve also added a simple CLI mode in [version 0.1a2](https://github.com/simonw/micropython-wasm/releases/tag/0.1a2) which means you can try it using `uvx` without first installing it like so:

```
uvx micropython-wasm -c 'print("Hello world")'
# To see it run out of fuel:
uvx micropython-wasm -c 's = ""; while True: s += "longer"'
# Outputs: micropython-wasm: guest exited with code 1
```

You can also try it in [Datasette Agent](https://agent.datasette.io/) like this:

```
uvx llm keys set openai
# Paste in an OpenAI key, then:
uvx --with datasette-agent \
  --with datasette-agent-micropython \
  --prerelease allow \
  datasette --internal internal.db \
    -s plugins.datasette-llm.default_model gpt-5.5 \
    --root -o
```

Then navigate to <http://127.0.0.1:8001/-/agent> and run the prompt:

> `show me some micropython`

![Screenshot of a chat application interface with a dark blue-grey header reading "home" on the left and "root" with a hamburger menu icon on the right. Below is a navigation row with "← Back" and "Chat" on the left and an "EXPORT" button on the right. A blue user message bubble reads "show me some micropython". Below it a collapsed thinking section reads "▸Thinking: … to show the result clearly. After that, I can wrap up with a brief explanation!" followed by a "▶ Tool: execute_micropython" label. A code block follows: "# A tiny MicroPython example: blink-style logic + Fibonacci" / "def fib(n):" / "    a, b = 0, 1" / "    out = []" / "    for _ in range(n):" / "        out.append(a)" / "        a, b = b, a + b" / "    return out" / 'print("Hello from MicroPython!")' / 'print("First 10 Fibonacci numbers:", fib(10))' / "# MicroPython often runs on microcontrollers, e.g.:" / "# from machine import Pin" / "# led = Pin(2, Pin.OUT)" / "# led.value(1)  # turn LED on" / "# led.value(0)  # turn LED off". Below a horizontal divider is the output: "Hello from MicroPython!" / "First 10 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]", followed by a "▶ Result: execute_micropython" label. At the bottom is a text input field with placeholder "Type a message..." and a blue "Send" button.](https://static.simonwillison.net/static/2026/micropython-in-datasette-agent.jpg)

You can try a live demo of that plugin running in Datasette Agent by signing into [agent.datasette.io](https://agent.datasette.io) with your GitHub account.

#### Should you trust my vibe-coded sandbox?

Having complained about immature, loosely-maintained sandboxing libraries, it’s deeply ironic that I’ve now built my own!

I deliberately slapped an alpha release version on it, and I’m not ready to recommend it to anyone who isn’t willing to take a significant risk.

I’ve put it through enough testing that I’m OK using it myself. I’ve shipped my first plugin that uses it, [datasette-agent-micropython](https://github.com/datasette/datasette-agent-micropython). I’ve also locked GPT-5.5 xhigh in that Datasette Agent plugin and [challenged it to break out of the sandbox](https://gist.github.com/simonw/5de497c44d25f9fd459c8aa2c959fe4a) and so far it has not managed to.

I’m hoping this implementation can convince some companies with professional security teams and high-stakes problems to commit to using Python in WebAssembly as a sandboxing approach and open source their own solutions.

Posted [6th June 2026](/2026/Jun/6/) at 3:53 am · Follow me on [Mastodon](https://fedi.simonwillison.net/@simon), [Bluesky](https://bsky.app/profile/simonwillison.net), [Twitter](https://twitter.com/simonw) or [subscribe to my newsletter](https://simonwillison.net/about/#subscribe)

## More recent articles

- [Initial impressions of Claude Fable 5](/2026/Jun/9/claude-fable-5/) - 9th June 2026
- [Claude Opus 4.8: "a modest but tangible improvement"](/2026/May/28/claude-opus-4-8/) - 28th May 2026

This is **Running Python code in a sandbox with MicroPython and WASM** by Simon Willison, posted on [6th June 2026](/2026/Jun/6/).

[python
1,257](/tags/python/)
[sandboxing
45](/tags/sandboxing/)
[ai
2,063](/tags/ai/)
[datasette
1,507](/tags/datasette/)
[webassembly
124](/tags/webassembly/)
[generative-ai
1,821](/tags/generative-ai/)
[llms
1,789](/tags/llms/)
[ai-assisted-programming
385](/tags/ai-assisted-programming/)
[codex
51](/tags/codex/)
[datasette-agent
15](/tags/datasette-agent/)
[micropython
9](/tags/micropython/)

**Next:** [Initial impressions of Claude Fable 5](/2026/Jun/9/claude-fable-5/)

**Previous:** [Claude Opus 4.8: "a modest but tangible improvement"](/2026/May/28/claude-opus-4-8/)

### Monthly briefing

Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

[Sponsor & subscribe](https://github.com/sponsors/simonw/)

- [Disclosures](/about/#disclosures)
- [Colophon](/about/#about-site)
- ©
- [2002](/2002/)
- [2003](/2003/)
- [2004](/2004/)
- [2005](/2005/)
- [2006](/2006/)
- [2007](/2007/)
- [2008](/2008/)
- [2009](/2009/)
- [2010](/2010/)
- [2011](/2011/)
- [2012](/2012/)
- [2013](/2013/)
- [2014](/2014/)
- [2015](/2015/)
- [2016](/2016/)
- [2017](/2017/)
- [2018](/2018/)
- [2019](/2019/)
- [2020](/2020/)
- [2021](/2021/)
- [2022](/2022/)
- [2023](/2023/)
- [2024](/2024/)
- [2025](/2025/)
- [2026](/2026/)
