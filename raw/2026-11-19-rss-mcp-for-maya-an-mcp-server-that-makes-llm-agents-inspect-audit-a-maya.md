---
source: "https://www.tech-artists.org/t/mcp-for-maya-an-mcp-server-that-makes-llm-agents-inspect-audit-a-maya-scene-instead-of-editing-blind/18659"
title: "mcp-for-maya: an MCP server that makes LLM agents inspect + audit a Maya scene instead of editing blind"
author: "xxx91n"
date_published: "2026-11-18"
date_clipped: "2026-11-19"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# mcp-for-maya: an MCP server that makes LLM agents inspect + audit a Maya scene instead of editing blind

Source: https://www.tech-artists.org/t/mcp-for-maya-an-mcp-server-that-makes-llm-agents-inspect-audit-a-maya-scene-instead-of-editing-blind/18659

[xxx91n](https://www.tech-artists.org/u/xxx91n)

November 18, 2026, 3:28pm

1

Hi all, first post here. I’ve been building an open-source MCP server for Maya and figured this is the crowd most likely to tell me where it’s wrong.

The idea: an agent (Claude, Codex, whatever) shouldn’t touch a scene it can’t see. So every edit goes Inspect → Compute → Execute → Verify. Inspect is one batched call returning names / types / world bboxes / hierarchy, Verify is a registry of 11 deterministic validators (naming against GRP\_/GEO\_/MAT\_/LGT\_ prefixes, overlaps, floating geo, light rig roles…) giving a 0-100 score. One validator throwing gets logged as check\_error and the rest of the round still runs.

A few decisions that might interest TAs:

- Two capture paths on purpose. scene\_viewport\_snapshot uses M3dView.readColorBuffer (cheap, in memory, WYSIWYG), scene\_render\_preview is a single-frame playblast with a chosen camera and no HUD. Gotcha I hit: on VP2 the MImage has to be created as kFloat and read with readRGBA=True or you get a black frame. QWidget.grab() also gives black on the GL surface, which matches what maya-capture and others found.
- No silent headless fallback. In batch there’s no viewport, so the tools return a structured gui\_session\_required error instead of quietly using cmds.render. A model looking at a renderer image and treating it as the viewport is worse than no image.
- The preview switches the panel camera and restores it in a finally. Hijacking the artist’s viewport is the fastest way to lose trust.
- Dirty-scene guard: before anything that would open a new scene it checks the modified flag. file(new, force=True) on a dirty scene silently throws away work, without force it pops a modal and hangs the UI thread. So it stops and hands the decision back.
- Checkpoints are exportAll snapshots in memory state (references flattened), rollback reopens and rebinds the original path explicitly.

All the README images were produced by the tool through these same calls (playblast for the orbit, scene\_review before/after for the audit pair). Scripts to reproduce are in the repo.

Limits: it executes arbitrary Python in Maya, the validation is a safety net for accidents not a sandbox. Started as a fork of chadrik/maya-mcp-server.

[GitHub - Xxx91n/mcp-for-maya: Maya MCP Server with spatial awareness, camera planning, aesthetic analysis, and scene auditing · GitHub](https://github.com/Xxx91n/mcp-for-maya) (MIT, pip install mcp-for-maya)

Curious what you’d add to the validator list, or what in this design would break in a studio pipeline.
