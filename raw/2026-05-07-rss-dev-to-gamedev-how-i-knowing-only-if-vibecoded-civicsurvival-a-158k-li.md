---
source: "https://dev.to/valentyn_kurchenkohai_7f/how-i-knowing-only-if-vibecoded-civicsurvival-a-158k-line-mod-a-rag-server-and-300-analyzers-375c"
title: "How I, knowing only IF, vibecoded CivicSurvival: a 158K-line mod for Cities: Skylines II, a RAG server, and 300 analyzers in 3 months"
author: "DEV.to Gamedev"
date_published: "Wed, 06 May 2026 18:35:38 +0000"
date_clipped: "2026-05-07"
category: "Game Development / Unity"
source_type: "rss"
---

# How I, knowing only IF, vibecoded CivicSurvival: a 158K-line mod for Cities: Skylines II, a RAG server, and 300 analyzers in 3 months

Source: https://dev.to/valentyn_kurchenkohai_7f/how-i-knowing-only-if-vibecoded-civicsurvival-a-158k-line-mod-a-rag-server-and-300-analyzers-375c

try {
if(localStorage) {
let currentUser = localStorage.getItem('current_user');
if (currentUser) {
currentUser = JSON.parse(currentUser);
if (currentUser.id === 3355218) {
document.getElementById('article-show-container').classList.add('current-user-is-article-author');
}
}
}
} catch (e) {
console.error(e);
}
Valentyn Kurchenko-Hai 
Posted on May 6 
How I, knowing only IF, vibecoded CivicSurvival: a 158K-line mod for Cities: Skylines II, a RAG server, and 300 analyzers in 3 months
# ai 
# gamedev 
# unity3d 
# csharp 
Where I started
My name is Valentyn Kurchenko-Hai. I currently teach English; coding is a hobby. My programmer background fits in one sentence: I don't know syntax, but writing a mod for Cities: Skylines II is not my first AI project. A year ago I started "vibecoding" with no IT background. Before CivicSurvival there was a large Python/FastAPI server (a personal AI assistant with a LiveKit integration), and that's where I learned the main thing: don't let AI break the architecture . This matters for the context of this article — I didn't start from zero. I started with about six months of working with AI as my primary tool.
But DOTS, ECS, Burst, ComponentLookup, sync point, EntityCommandBuffer, Harmony postfix patch, Coherent UI, Roslyn analyzer — these were just words to me, none of which I could define without Google. DOTS (Data-Oriented Technology Stack) is Unity's architecture for very fast code, but it's specific and far less forgiving of mistakes than classic OOP. I had never touched C# before. I still don't know the syntax.
CivicSurvival started December 26, 2025. On the calendar — 4.5 months to beta. But I lost almost all of April to a pause for another project — so it's really about ~3 months of net development time . In those three months we shipped:
Metric 
Value 
C# code 
158,583 lines out of 700,000 generated 
TypeScript/React 
31,219 lines 
C# systems (ECS) 
542 
UI components 
369 
Custom Roslyn analyzers 
300+ 
Git commits 
2,503 
Custom MCP server for codebase navigation 
CivicRAG (custom-built) 
Separate diagnostics mod 
VanillaProfiler 
Record month 
March 2026, 895 commits 
Calendar time 
4.5 months 
Net development time 
~3 months (April was a pause for another project) 
Spoiler: the mod is currently in closed beta. If you like breaking complex systems in Cities: Skylines II, at the end of this article I'll explain exactly who I'm looking for to test it.
The stack ended up not small. The mod itself is C# on top of Unity DOTS/ECS, Burst, Harmony patches, and the stock Cities: Skylines II systems. The interface is TypeScript/React and Coherent UI. Around the mod lives a Python layer: CivicRAG, an MCP server, codebase indexing, SQLite with vector and full-text search, model export scripts, report generators, and helper tools for audits. Plus a VPS for RAG, Roslyn analyzers for C#, ESLint for the frontend, Git as a journal of the entire history. So it's not one mod file, it's a small ecosystem around the game.
I remember very clearly where I started: a person who can articulate "if this — do that," but who can't write proper ECS code from scratch and doesn't know enough syntax to honestly call it manual programming. I started without Git, with the classic "Final," "working" folders.
This article is about something else: what pure vibecoding looks like when you don't romanticize it but instead surround the AI with constraints, checks, and planning . What works, what doesn't, and why this process is currently running into a wall without live beta testers.
In short: AI didn't replace a programmer for me. It became a very fast executor, and my role is to hold the intent, the context, the rules, the verification, and the actual behavior of the game. I don't write code in the classical sense. I rather hold the process so the system doesn't lose meaning and fall apart.
What is CivicSurvival?
CivicSurvival is a total conversion mod for Cities: Skylines II (CS2 from here on). In short: into a peaceful city-building simulator I wanted to add things that don't need much explanation — blackouts, generators, corruption, panic, the Telemarathon, drones, shelters, exhausted people, and the constant choice between "the right thing" and "just survive the night."
In terms of genre it's a mix of city simulator, survival strategy, and social satire. Reference points: Frostpunk, This War of Mine, Papers Please, Beholder. But importantly: I didn't want to make another game where war is just explosions. I was interested in the other side: how a city lives when war becomes the background, and the main gameplay isn't shooting but deciding who gets electricity tonight, who'll believe the propaganda, where the bureaucrat will steal the budget, and how many moral compromises the system can take.
The context is familiar to a Ukrainian: DTEK (Ukraine's main electricity provider) appears in the English locale as Power Company , the bomb shelter is Resilience Point (a real Ukrainian term for civilian heating/charging hubs during blackouts), the inbound drone is Shahed — but only in the Ukrainian locale. This isn't a "war game" in the literal sense. It's a simulation of civilian life when war is background noise, and the decisions you make are about which district to leave without power tonight and whether to install an air defense battery.
Project tagline: "Corruption is the cause. Blackout is the consequence." 
The gameplay triangle:
Survival type 
Domain 
Question to the player 
Physical 
Power Grid 
"Will there be light tonight?" 
Mental 
Cognitive Warfare 
"What is the truth?" 
Moral 
Corruption 
"Everyone steals. Why shouldn't I?" 
A typical moment in the game looks roughly like this. In the evening the grid is overloaded, part of the city is already running on generators, panic is rising in Chirper, and intel is warning about an inbound Shahed . You can reroute power to the hospital, but then a residential district goes dark. You can buy cheap equipment through a shady tender, but it'll come back as accidents later. You can paper over the problem with a nice Telemarathon broadcast, but public trust isn't infinite. I wanted the player to not just optimize numbers, but to constantly feel that any decision has a political, technical, and human price.
At the system level the mod consists of 15 domains. Power Grid handles electricity, blackouts, repairs, and grid overload. Air Defense — aerial threats, AD batteries, Shahed attacks, and the consequences of impacts. Cognitive Warfare — the information noise, Telemarathon, trust, panic, and how people react to what they're told. Corruption — kickbacks, schemes, tenders, and situations where a bad decision looks short-term very profitable.
Around all this there are scenarios, tutorials, UI, localization, balance tables, diagnostics, profilers, a separate mod for performance measurement, and a pile of small things the player doesn't see directly but without which everything falls apart. For example, 469 sarcastic Chirper messages — these aren't just jokes for jokes' sake. It's a way to show how the city comments on your decisions: sometimes funny, sometimes angry, sometimes so bad you want to reload the save.
What a working day with AI looks like
The toolset is simple: Claude Code as the main interface, plus a few specialized tools around it.
A plan almost always comes before code. But it's not a deterministic ritual of five steps and not a document in the style of "here's the architecture for the next month." The scale of planning depends on the task. A small fix might go through one short round. A new mechanic, a domain refactor, or a bug at the system boundary may need several passes over the same document.
The main thing is to fully immerse the model in context . Not just say "build a feature," but force it to read the existing systems, find similar patterns, understand who writes the state, who reads it, what events already exist, what analyzers might fire, where the domain boundaries are, and what cannot be broken. Very often the first plan after such a read turns out to be naive. And that's normal: its job is not to be final, it's to extract the hidden constraints.
Then comes the discussion about the pattern. The model can offer three options: a quick hack, a local fix, or a proper integration into the existing architecture. My job is not to write C# instead of it, but to choose the right form of the solution: should this be a new component, an extension to an existing system, a separate event, a change in execution order, a UI binding, a save migration, or a flat-out refusal because the change breaks an invariant.
After this the plan gets rewritten. Sometimes once, sometimes three times. On big tasks I can run the same document up to five passes: each time adding a new layer of context, removing unnecessary improvisation, clarifying risks, breaking the work into phases, and forcing the model to explain why exactly this pattern fits the existing codebase.
A separate important thing: it almost never works to write a plan "for everything" on the first try. This is very similar to how people program without AI. First you sketch the functionality: buttons, states, events, reactions, the first working connections. Then comes architectural discipline: where is the responsibility, where are the dependencies, where are the boundaries, where are SOLID principles or their DOTS analog. And only after this comes targeted refactoring: in Python it was separate classes and services, in CivicSurvival — separate ECS systems, components, and seams between domains.
So planning with AI is not an attempt to guess the perfect architecture in one go. It's a controlled movement from "it has to work somehow" to "it works in the right place, with the right pattern, and doesn't break the neighbors."
The final plan usually no longer looks like the general idea. It can be several phases: first the components and data, then the systems, then the UI, then localization, then an analyzer or test log, then a save check. The plan must contain specific files, forbidden actions, expected behavior, risks, and the criterion by which I'll know the AI actually did what was needed.
Only after this does the AI edit files. And after implementation a reconciliation is mandatory: what we planned, what was actually done, what wasn't, which tests or builds passed, which risks remain. I don't accept "done" as a result. The result is a diff, a build log, and a short list of deviations from the plan that I can evaluate at the level of system behavior, not at the level of "I personally understand every syntactic nuance."
This sounds slow, but in practice it's faster than digging out the chaos that follows a single broad prompt. Most AI mistakes are born not in the code but in the moment when you allow it to fill in too much.
1. Claude Code — my IDE replacement
I don't write code by hand. I describe intent, constraints, and expected behavior . The AI reads files via Read, searches patterns via Grep, edits via Edit. I don't reread every diff before applying, but I can refuse, I can ask the AI to redo it. And this doesn't mean I'm sitting there programming C# in the classical sense.
Key thing: I try not to delegate responsibility for meaning . I very rarely write "read this and fix it." Often it's a specific issue that we previously, together with the AI, extracted from logs, grep, decompilation, or a previous failed fix.
2. Global rules in CLAUDE.md 
CLAUDE.md is a local file with rules that the AI reads at session start. But importantly: it's not a magical contract the model always follows. It's more like a set of fences that reduce the number of dumb decisions.
You can add as many rules there as you want. For example: don't create a new sync point if it could hurt FPS. No domain → domain imports. Don't delete "dead code" without separate confirmation. Don't use git restore / git checkout , you might accidentally wipe another agent's work. Don't fix 50 warnings in one swing. Don't rewrite the architecture if the task was about one method.
This really helps, but it doesn't replace control. The model often doesn't break a rule directly. It approaches it from the side. For example, it's forbidden to make a new sync point — and it doesn't write EntityManager.ToEntityArray() outright, but offers a "convenient helper" that internally does the same thing. Formally, the rule isn't broken. In practice — a future FPS bug.
So part of my job is to read not just the code but the direction of the model's thinking . If I see it starting to justify an unnecessary refactor, creating a new abstraction layer without need, wanting to "temporarily" bypass an analyzer, or using a Git command that's better left alone — I try to stop it before implementation. This is very similar to pair programming with someone who writes fast and often well, but didn't read the neighboring system.
And there's a difference between tools here. Claude Code usually shows me intent and the chain of thought readably enough: I see where it's headed and can stop the model in time. With Codex it's worse for me: it often dumps changes in big chunks, and physically I can't review the 2,000-5,000 lines a day an AI can produce. There's no point in that: I'm still a person who only knows if . My role isn't to manually re-read every line, it's to hold the frame of the task, notice when the model starts going the wrong way, and have automated checks where human attention runs out.
3. Custom MCP server: CivicRAG
A regular grep doesn't show connections . If I ask "who reads BlackoutState ?" — I have to read dozens of files because ComponentLookup<BlackoutState> hides in class fields.
So I asked the AI to build an MCP server on Python + SQLite. Metadata for 542 systems, 369 UI components, and 1427 cross-domain links is indexed once and accessible through tools:
rag_query("blackout permanence") — semantic search. 
rag_styk("AirDefense", "Threats") — analysis of the seam between two domains: data flow, code fragment, sync points, risks. 
rag_component("BlackoutState") — component map: who writes, who reads, execution order. 
rag_system("AirDefenseOrchestrator") — full system profile. 
4. 300+ custom Roslyn analyzers
This is where it gets most important.
DOTS code is easy to break. This isn't knowledge I came into the project with, it's something I had to absorb through AI, logs, bugs, and analyzers. If the AI did EntityManager.SetComponentData inside OnUpdate — you silently get a potential 20 ms sync point. If ComponentLookup<T> wasn't refreshed via .Update(this) — runtime error. If an EntityQuery was created in OnUpdate instead of OnCreate — leak. None of this is caught by the C# compiler.
So I asked the AI to generate 300+ custom Roslyn analyzers , which it found from examples of its own analysis. This isn't a style linter — this is forced enforcement of architectural rules at compile time:
CIVIC051 — write operations through EntityManager are forbidden in OnUpdate . Only ComponentLookup or ECB . 
CIVIC310 — magic numbers (only via GameRate.SECONDS_PER_HOUR , not 3600f ). 
CIVIC324 — singleton naming convention. 
CIVIC361 — no domain → domain imports. 
CIVIC382-385 — new rules from audits. 
Every build with --no-incremental runs all the analyzers. If the AI generated code that violates the architecture — it just won't compile. I see the error, tell the AI "this violates CIVIC051," and the AI rewrites it. I don't have to remember the entire analyzer API syntax. I just have to understand which project rule was violated.
This is the most powerful coercive prompt in the project. AI can be wrong about plans or logic, but a portion of dangerous changes the compiler and analyzers simply won't let through. A code review can forget a rule. An analyzer cannot.
Where AI didn't pull through: two weeks with drone rendering
So it doesn't sound like AI is a magic button, I have to separately tell you about the most painful part of the project. Drone rendering.
It was a nearly two-week saga at the intersection of several things at once: Unity ECS, DOTS, the stock CS2 render pipeline, BatchRendererGroup, HDRP, motion vectors, temporal smoothing, Coherent UI for diagnostic panels, custom .cok models, undocumented engine code, and visual eyeball verification. And this was where AI was at its weakest.
Because the problem wasn't in one interface or one file. The code could be formally correct, the logs could show clean data, ECS components could match the stock game objects, and on screen the drone still pulsed at 2x/3x speed. This is the class of bug where AI confidently explains five plausible causes to you, and none of them is the actual root cause.
If you open the Git history of this section, you see not "one bug and one fix" but a proper funnel of pain. First AttackDrone.cok appears in the repo — the first real drone model. Then almost immediately documents about the render pipeline start, because it becomes clear: just drawing a mesh isn't enough. The drone has to live in the same stock pipeline as cars, planes, and helicopters in CS2.
Then the story branches. One direction — backward jitter: the drone seems to move forward, but the camera or render sometimes shows it with a snap backward. In the Git records you see dozens of attempts: TransformFrame , UpdateFrame , ObjectInterpolateSystem , diagnostic systems, log writes, comparisons with stock objects. At some point this was closed by writing render components directly in TMS.
But after this another symptom remained — jitter on acceleration and motion blur pulsation. And it was worse, because the code already looked correct. In the repo this is visible in the investigation documents: attempts 25-32 (meaning 32 different rendering variants were written), comparative testing against the stock helicopter prefab, comparison with the stock car, OTW delta measurements at the BRG group level, checks for PreviousM , change tags, and memory reallocations. So we didn't just "tweak a parameter." We tried to walk the entire path from ECS component to GPU matrix and figure out where the stock game behaves differently.
In parallel, Model/ moved into the main repo. Before this the models lived separately in D:\Model , but it became obvious that without the FBX files, textures, export scripts, and notes about CS2 resources, you can't properly investigate rendering bugs. AttackDrone, Bofors, LADS — these are no longer "pictures off to the side" but part of the project's technical picture.
The final fix turned out to be not heroic but pragmatic. We stopped fighting motion vector flags in individual render groups, because in CS2 1.5.5 the path through GetMotionVectorsEnabled() effectively didn't give the control we needed. Instead the AI generated a patch that, at speeds above 1x, disables motion blur via a forced HDRP Volume override ( MotionBlur.intensity = 0 ) and restores the normal state when returning to 1x. Not academically elegant, but the drone stopped pulsing.
Another important thing visible in the repo: we built ourselves a local reference folder with the decompiled Game.dll ( _decompiled\Game\ ). This wasn't "let's steal code." It was "without a map of the stock pipeline we don't even know where to look." From this grew an entire Rendering folder: VANILLA_RENDER_PIPELINE.md , VANILLA_RENDER_MESH.md , VANILLA_RENDER_ENTITIES.md , VANILLA_VFX_PIPELINE.md . I spent 100 million tokens on creating these documents. They describe what ObjectInterpolateSystem , UpdateGroupSystem , PreCullingSystem , BatchInstanceSystem , BatchDataSystem do, how Created/Updated/Applied live, how the TransformFrame ring buffer works, CullingInfo , motion vectors, and the material resolution chain.
Without this reference folder we'd have just been groping in the dark. There's no official documentation for this. In CS2 modding the answer often looks like: open the decompiled code, find the stock path, replicate it as closely as the mod allows.
The funniest part: at some point the CPU-side data was identical between our drone and stock objects. In the investigation documents there are tables where OTW delta for the drone and the stock car have identical coordinates. No change tags, memory reallocations explain nothing, OIS reads the same slots, InterpolatedTransform is fine. So everything we could measure from C# looked correct. But on screen the drone was pulsing.
This is where the AI's limit became very visible. The AI was good at generating diagnostic systems, quickly making Harmony patches, helping decompile and structure knowledge. But it didn't see the screen. It couldn't say: "this isn't math jitter, this is exactly motion blur pulsation." It confused similar symptoms: backward motion, camera lag, render clock jitter, temporal smoothing artifact, motion vectors. A human looks at the drone in-game and says in a second: "that's not it." AI without visual control trusts only logs, and the logs here didn't show the root cause.
The final conclusion was pragmatic: we don't fix the GPU/HDRP path of the game itself from a mod. We proved our CPU-side data is clean, found that the artifact lives below the level of accessible C# code, and made a working workaround: disable motion blur on accelerated speeds. It's not a beautiful academic root cause. But it works.
This episode was sobering. AI is brilliant when the task is textual, structural, or statically analyzable. But at the intersection of undocumented engine code, rendering, shader behavior, and the human eye, it becomes not an autopilot but a very fast assistant who still needs a pilot. (By the way, the original game has the same problem.)
What an AI audit looks like — the paradox of free search
DOTS code is hard to cover with unit tests. Building a test ECS World, populating archetypes, mocking EntityManager — all of this often costs more than it gives. So we went a different route: AI agents as an army of static testers .
Scale
Scale matters. This isn't "I ran 10 agents and wrote a conclusion." AUDIT_HISTORY.md currently records about 9,700+ claimed findings and 5,500+ fixed across all audit methods. And that's only what made it into reports. Roughly the same volume burned earlier: at the level of compilation, Roslyn analyzers, ESLint, builds after refactors, and small fixes that nobody filed as a separate audit. So it's more honest to talk not about "ten thousand checks" but about tens of thousands of signals — the documents preserve only the lower bound.
The Free report for March alone is ~1,500 debugger-agent reports , ~2,600 unique findings . If you count all agent checks of various types across the project — that's not hundreds but thousands of agent runs, and even that number doesn't include everything the compiler and analyzers caught during normal work.
In other words, this is no longer "AI sometimes helps find a bug." It's a separate production line: an agent finds a suspicion, another agent verifies it, the fix passes the build, and a recurring class of error eventually turns into an analyzer.
Evolution
At first the known categories worked. Manual audits in the style of "check serialization," "check time," "check Entity.Index," "check dead code" gave good signal when the category was concrete. Then came theoretical pattern lists: hundreds of hypotheses in the style of "what if there's a class of error like this somewhere." That was exhausted quickly. The documents show the ceiling: after 760 theoretical patterns , the last focused pass found 0 confirmed bugs . The model invented plausible risks, but the code no longer contained them. 
Then we moved to system seams. STM — semantic threat modeling — gives the agent not just a list of files but the seam context: who writes, who reads, execution order, where the events are, where the state is, where saves are. This opened up a new class of bugs: races between systems, frame N/N+1 ordering, events that arrive before initialization, switch without a new case . This isn't caught by a linter. But STM also has a limit: after a few passes it starts chewing on the same contracts. 
And then came the paradox of free search. The most effective approach turned out to be not the smartest checklist but an almost free prompt: "here's a narrow set of files, find any runtime bugs that could realistically break the game; prove every finding with code." No category list. No "check only serialization." No "look only for sync points." This is paradoxical, because it seems the more specific the prompt, the better. But an overly specific prompt creates a flashlight effect: the agent only sees what it was asked to look for. 
The right formula turned out to be: free prompt + narrow scope + correct context . When the agent was given a whole domain at 4-6K lines, it skimmed the surface. When given a pair of interacting systems and shared components at ~2K lines, it started modeling execution: "what if A fires before B? what if after? what if save and load happen between them?" In W13-cross this approach gave 2.8 findings per agent — the highest yield in the audit history. The same narrow scope with a checklist gave around 0.9 findings per agent .
CODE and RAG
CODE and RAG turned out to be different eyes. In the free method each session was often launched as a pair: one agent reads local code directly, another first takes context from the RAG server plus code. They don't split the work — they independently check the same file list. The CODE agent is better at local arithmetic, edge cases, dead code, serialization minutiae. The RAG agent is better at execution order, system links, post-load hydration, who overwrites whom.
The numbers backed this up. In the basic FREE, CODE produced more findings by volume — about 60%. But RAG more often brought higher criticality: in CRIT2 RAG found all 4 CRITICAL issues that CODE didn't see. The conclusion isn't "RAG is better than code" or "code is better than RAG." The conclusion is: RAG isn't a replacement for reading code, it's navigation and link highlighting. The best results come from a pair: RAG suggests where to look, code confirms or refutes.
Model debates
For complex fixes I made models argue. When it was unclear how to fix a tricky bug, I sometimes ran not "one wise agent" but a debate: GPT proposes a fix, Claude critiques, another agent searches for regressions, yet another defends the minimal variant. Then I look not at who sounds more confident, but at where there's concrete proof: file, line, execution order, log, risk to the neighboring system. This is useful specifically for fixes, because the agent that found the bug very often proposes too broad or dangerous a fix.
The method's limit
The method's limit is noise and exhaustion. Repeat waves inevitably degrade: the false-positive share can climb from 15% to 90%, especially when the code is already cleaned. Agents start inventing thread-safety problems where the entire code runs on the main thread, or exaggerating one-frame state staleness in throttled systems. So the law is simple: a single method is exhausted in 3-4 passes. If there are no new HIGH findings — change the method or the area, don't run another 100 agents with the same query.
And even 826 agents don't replace gameplay testing. They can find Random(0) , a forgotten clamp , a state overwrite, wrong system order, a NativeContainer leak, missing cleanup. But they won't tell you if the game is fun, if the tutorial is clear, if the scenario has dramaturgy, if Telemarathon makes you doubt rather than just press a button. That's no longer a code audit. That's live people.
Five things I learned in a year of vibecoding and three months of CivicSurvival
1. AI without guardrails is a tech-debt generator
I learned this on the Python server a year ago — the codebase turned into a mishmash of three different patterns in two weeks because AI only remembers the context of one session. I came into CivicSurvival already with that conclusion: external memory is needed. Axioms in CLAUDE.md , analyzers, the RAG server — these are formalized memory of the rules that forces the AI to be consistent between sessions.
2. Specificity > abstraction
"Fix the bug" — bad. "Here's the symptom, here's the log, here's the file we suspect, here's the rule that can't be broken, here's the expected behavior" — good. Sometimes after several rounds of diagnosis it gets to the level of "in file X on line Y replace API W with API V," but not because I suddenly became a C# developer. It's because the AI, the logs, and grep helped narrow the search space to one place. The more precise I formulate, the less the AI improvises. AI improvisation is a source of bugs.
3. Real behavior + logs
Project Axiom 1 was born from a 30-hour investigation of a February bug. I spent half a day convincing the AI that "the fix doesn't work, I see the bug."
Since then any theory is verified by two things: the actual behavior of the system in-game and a log that explains why it behaves that way . A log alone isn't truth. If a district went dark in-game, people disappeared, or the UI shows the wrong thing — that's also a fact. But for the AI this fact alone isn't enough: it doesn't see the screen, doesn't feel the game's tempo, and can't itself understand what happened between two frames.
So our logging is often maximally detailed, sometimes almost at method level: who was called, with what data, in which frame, what was before, what came after — it's a way to give the AI eyes. When the model only sees the code, it guesses behavior. When there's actual behavior plus a detailed log, it can finally reconstruct how the code actually works.
4. Custom analyzers > one-shot code review
I don't throw away AI code review. On the contrary, I often take it as the first analysis layer: the model quickly spots suspicious places, unusual patterns, repetitions, and potential regressions. But a single AI pass isn't truth. I force checking conclusions multiple times, comparing them with the actual code, logs, in-game behavior, and Git history: when the file appeared, what was changed nearby, which fix was already tried, which commits could've spawned the symptom. Git here works not as an archive but as a causality map.
An analyzer is the next level after such a review. If a bug or architectural rule recurs, you have to not just "remember" it but formalize it. An analyzer works without human fatigue or inattention, and it catches the same class of bug every build.
Every time I or the AI catches a bug during testing or audit that should've been caught automatically, I ask the AI to formulate a new analyzer rule. The AI generates the analyzer code, then we run it against the real codebase, scrub false positives, and bring it to a state where it catches that bug class permanently. In 4.5 months — 300+.
5. I don't know syntax, but I try to understand behavior
I probably can't write IJobChunk from scratch without AI. I don't know the syntax, don't know the API, and wouldn't pass an interview for a junior Unity DOTS developer. But I try to understand how my project should behave: which domains shouldn't directly depend on each other, which states should persist in saves, where you can't create a sync point, what game effect a system should produce.
So I don't read 5,000 lines of AI code as a C# engineer. I read the plan, the logs, the analyzer errors, and the in-game behavior. If a system should turn off a district but turns off half the city — I notice it. If the AI wants to make a workaround through a different domain — I try to stop it at the plan level. If the build fails on CIVIC051 — I don't write the analyzer API from memory, but I understand: the model is again trying to write where it shouldn't.
This is a separately interesting question — am I a programmer in the classical sense? No, more likely no. I'm a pure vibecoder who holds the product, the rules, the verification, and the feedback loop.
Why statistical analysis exhausted itself
This is the most interesting part. Why 4.5 months it worked — and why right now it doesn't.
In stages 1-3 (December-February) — AI agents found real bugs by the dozen. Each audit wave gave 30-50 findings, of which 10-20 were genuine.
In stage 4 (March) — the signal started weakening. Waves repeated previous findings. We caught small things — naming, dead code, a missing [Persist] on a field nobody uses. Real gameplay bugs — zero. This coincides with the record 895 commits in March — a lot of work, but already polish, not the search for fundamental problems.
April — pause for another project. Came back at the end of the month.
Now (May): AI statistical analysis has technically exhausted itself . I'd like to believe all sync points are removed and serialization gaps closed. The analyzers catch regressions automatically.
What's left is the integrity of the gameplay experience . Whether the game is fun. Whether the tutorial is clear. Whether the balance numbers, whether the "First Shahed" modal appears at the right moment. Which bugs still remain (I think 50% the AI just couldn't find). Whether the Telemarathon mechanic makes you hesitate rather than just press a button.
This is no longer caught well by agents. This needs live people who play for hours. 
What I'm looking for now
Beta testers for the closed phase. 
People ready to play 5-10 hours on a single save — some mechanics open up only on long distance (mobilization, Telemarathon, corruption schemes). Ready to give feedback in a structured form. The platform for the beta is Discord.
Why here. Because this audience has already seen some AI-driven development. If this article landed for you — you're probably the type of person who'll understand that a mod built in 3 net months by one person + AI is not vibecoding in the bad sense . Yes, a year ago that's exactly where I started. But unguarded vibecoding breaks at 5,000 lines of code. At 158,000 lines you only survive with a process — 300 analyzers, a RAG server, axioms, and audits. Your feedback I'll be able to process correctly.
P. S. — a technical note
An episode that nicely shows the limits of the process:
One Shahed destroyed the city in 80 seconds. In the February bug the city was literally dying in 30-80 seconds: residential buildings broke en masse, people disappeared from the normal life cycle, and the AI patched system after system, because the symptom looked like a cascading game failure. In the wrong investigation branch the AI replaced entity references in 11 components and checked 15 systems for separate mod entities; if you count all affected system, service, and UI files in the migration commits — 32 files. And the cause was in one line with CopyFromComponentDataArray : the method name sounds like it "copies components into an array," and the AI read it that way several times. In reality the method was writing zero Transform s back into residential buildings. Thirty hours of investigation, two days of searching in Game.dll , and the bug was in AI-generated code. 
Top comments (0) 
Subscribe 
Personal 
Trusted User 
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit 
Preview 
Dismiss 
Code of Conduct 
• 
Report abuse 
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink .
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
