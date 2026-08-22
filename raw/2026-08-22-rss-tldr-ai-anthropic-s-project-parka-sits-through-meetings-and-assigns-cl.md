---
source: "https://runtimewire.com/article/anthropic-s-project-parka-sits-through-meetings-and-assigns-claude-agents-the-ho"
title: "Anthropic's Project Parka sits through meetings and assigns Claude agents the homework (11 minute read)"
author: "unknown"
date_published: "2026-08-21"
date_clipped: "2026-08-22"
category: "AI / LLM Research & Tooling"
source_type: "rss"
discovered_via: "https://tldr.tech/ai/2026-08-21"
source_role: "primary-via-tldr"
---

# Anthropic's Project Parka sits through meetings and assigns Claude agents the homework (11 minute read)

Source: https://runtimewire.com/article/anthropic-s-project-parka-sits-through-meetings-and-assigns-claude-agents-the-ho

Anthropic’s Project Parka sits through meetings and assigns Claude agents the homework
Internally codenamed Parka, the Mac-first feature can capture system and microphone audio, stream speaker-attributed transcripts and create runnable work for Claude's agents.
By Ryan Merket
· Published Aug 19, 2026, 3:00am CT
· Updated Aug 19, 2026, 3:19am CT
RUNTIMEWIRE INVESTIGATION — Scoop
Original reporting by RuntimeWire, based on reverse engineering.
Why it matters
Meeting summaries are already commodity software. Parka would let Anthropic own the spoken context that creates work and route it directly into Claude's coding and desktop agents.
Reporting record
Finding Anthropic has designed an unreleased, Mac-first meeting recorder inside Claude Desktop, codenamed Parka, that can turn meeting transcripts into Cowork, Claude Code, or manual follow-up actions; current public builds keep the feature disabled and ship without its working native implementation or user interface.
How we verified Methods: reverse engineering.
Claude Desktop 1.32885.1 contains an extensive Parka interface contract covering meeting creation and deletion, system and microphone audio capture, calendar metadata, transcription keyterms, live speaker-attributed transcript events, summaries, notes, granular editing, and error states.
The action schema assigns each follow-up a title, description, owner, full prompt, execution type, autoRunnable value, and optional Claude session URL. Its execution types are cowork, code, and manual.
Public packaged builds force parkaMeetings to an unavailable status. The native Parka loader included with both operating-system packages is an empty 551-byte stub. After RuntimeWire forced the renderer’s two Parka bootstrap values to report supported, Claude loaded normally but displayed no meeting interface or navigation item. The loaded renderer made no observable listParkaMeetings call and fetched no Parka-specific JavaScript chunk.
Separately identified Anthropic-controlled Titanium hosts use names resembling Deepgram’s Nova-3 and Flux speech models. Parka’s keyterms argument also resembles Deepgram’s Nova-3 Keyterm Prompting interface. The desktop package contains no Deepgram hostname, SDK, credential, or other direct vendor attribution, so that connection remains unconfirmed.
Tested versions: Claude Desktop 1.32885.1 — macOS universal DMG Claude Desktop 1.32885.1 — Windows x64 application archive Claude renderer asset shared-2-8TRRKqAc.js — retrieved August 19, 2026.
Reproduction RuntimeWire independently reproduced the core finding.
RuntimeWire obtained current Claude Desktop artifacts for macOS and Windows, calculated SHA-256 hashes, extracted the Electron application contents, and searched the packaged code for Parka identifiers. We traced the feature from its operating-system gate through the desktop IPC contract, native implementation loader, event definitions, meeting schema, action schema, permission text, and renderer bootstrap.
We compared the Mac and Windows packages to identify platform differences. In a signed-in Windows installation, we queried window.desktopBootFeatures.parkaMeetings and confirmed that the packaged application reported the feature as unavailable.
Using Chrome DevTools Local Overrides, we changed both Parka bootstrap values in the remotely delivered renderer asset to supported and reloaded Claude. We then inspected the interface, loaded sources, console, and network activity. Claude showed no Parka screen, navigation item, feature chunk, or meeting-list request.
We compared the recovered behavior with public documentation from Anthropic, Apple, Notion, Granola, and Deepgram. Claims about a possible Deepgram connection were kept separate from the confirmed desktop findings because the application artifacts contain no direct provider reference.
Reproduction instructions
Obtain Claude Desktop 1.32885.1 for macOS and the corresponding Windows application artifact.
Calculate and record the SHA-256 hash of each original file.
Extract the Electron app.asar contents using an ASAR-compatible extraction tool.
Search the extracted files for parkaMeetings, createParkaImpl, listParkaMeetings, hasVisionResolvedSpeakers, autoRunnable, and sessionUrl.
Trace the Parka contract and confirm the methods for listing, retrieving, starting, stopping, deleting, and editing meetings.
Inspect the Parka feature gate. Confirm that packaged builds return unavailable before reaching the macOS 13-or-later support check.
Inspect the native Parka loader and compare its contents across Mac and Windows.
Launch a signed-in Claude Desktop session with Developer Tools open and evaluate window.desktopBootFeatures.parkaMeetings.
Preserve the remotely loaded renderer asset. Use DevTools Local Overrides to change both Parka bootstrap values to {status:"supported"} without altering unrelated code.
Reload Claude and confirm that the runtime feature value reports supported.
Inspect the interface, Sources panel, console, and Network panel for a Parka screen, navigation item, feature chunk, or listParkaMeetings request.
Tie the result to the preserved renderer filename and hashes because Anthropic can replace remotely delivered assets without updating the desktop package.
File hashes sha256:78c392a9bb1b436cf2a4c03ab9b45cbeb5995bcd3a7021415dc7244da4830f53 Claude.dmg sha256:7f616a4a7ee9b095280f453d59a19fcc289a3322214583ad117da7d3d0ea9d1f app(4).asar sha256 shared-2-8TRRKqAc.js
Company response The company was not contacted before publication.
Anthropic is developing a meeting recorder inside Claude Desktop that can turn action items into tasks for Claude Cowork and Claude Code, according to application interfaces reviewed by RuntimeWire.
The project is internally codenamed Parka. A Claude Desktop macOS package carrying August 18th, 2026 filesystem timestamps contains a detailed contract for recording meetings, streaming speaker-attributed transcripts, generating notes and summaries, and extracting structured follow-up work. Public packaged builds still mark the feature as unavailable, and Parka may never be its public name.
The feature would extend Anthropic's expansion beyond chat into Claude Code , its coding agent, and Claude Cowork , a desktop agent that works across files, browsers and applications. Parka would give both products a new source of assignments: commitments made aloud in meetings.
From conversation to agent session
Parka's desktop contract exposes methods to list, retrieve, start, stop and delete meetings. A recording can capture system audio, microphone audio or a mix of both. It can also accept calendar-event metadata and transcription keyterms, which could help the speech system recognize company names, product terminology and technical language.
Live events deliver transcript segments with a speaker label, timestamp, text, optional utterance ID and a field distinguishing interim text from a finalized turn. Meeting records progress through recording , processing , ready and error states.
Once processed, a record can contain a title, timestamps, duration, capture source, speaker-attributed transcript, Markdown notes, a Markdown summary, calendar details and structured actions. Parka provides separate controls for editing notes, summaries, titles and actions. It can also remove an individual transcript turn.
The action schema reveals Anthropic's larger plan. Each action can carry a title, description, owner, full prompt, execution type and an autoRunnable flag. The available types are cowork , code and manual . An optional sessionUrl appears designed to link an action back to the Claude session created to complete it.
That structure could let a product meeting produce a Claude Code task with the relevant implementation prompt. An operations call could hand research, document preparation or browser work to Cowork. Commitments assigned to a person could remain manual tasks.
The interface does not establish whether Claude starts eligible actions automatically or waits for user approval. autoRunnable could power either behavior, so Parka's execution model remains unresolved.
A device-level recorder built first for Mac
Parka's feature gate requires macOS 13 or later. The same interface contract appears in the Windows package, where the feature is unsupported. The Mac package includes separate permission text for audio capture and Claude's existing microphone access, consistent with a recorder that needs both computer audio and the user's voice.
Apple introduced ScreenCaptureKit at WWDC22 as a framework for capturing screen content and application audio with user consent. It can capture audio associated with applications without requiring extra audio-routing software. Those capabilities would allow Claude to listen directly on the device across Zoom, Google Meet, Microsoft Teams and other meeting software without adding a participant bot to the call.
The exposed Parka interface includes a field named hasVisionResolvedSpeakers . The name suggests Anthropic has explored using visual cues from a meeting window, such as participant names or active-speaker indicators, to improve speaker identification. Calendar attendee names could supply another set of candidate identities. No visual payload appears in the renderer contract, so the exact mechanism cannot be established from the package.
Parka can delete a transcript turn using its timestamp, speaker, text prefix and optional utterance ID. That creates a more precise editing control than deleting an entire transcript. The interface does not reveal whether removing transcript text also deletes corresponding audio retained during processing.
No raw-audio path, media URL or recording object appears in the exposed meeting record. Anthropic could discard audio after transcription, retain it behind the native layer or store it remotely. The package does not answer that retention question.
A detailed contract with the product still withheld
The build uses an explicit production kill switch. Public packaged versions report Parka as unavailable before evaluating the operating-system requirement. Internal or unpackaged builds continue to the macOS 13 check.
RuntimeWire forced the parkaMeetings feature to report a supported status at both bootstrap points in a signed-in Claude app. Claude loaded normally, but no meeting screen, navigation item or Parka-related JavaScript chunk appeared. A search across the loaded renderer found no client call to listParkaMeetings , even though the two injected feature flags were present.
Claude Desktop loads most of its product interface remotely from Claude's web infrastructure. Anthropic can therefore add the missing Parka renderer later without shipping another desktop package.
The JavaScript module intended to load Parka's native implementation is currently an empty 551-byte stub in both the Mac and Windows packages. The surrounding contract is far more developed: it defines calendar alerts, live transcript events, granular editing, failure states, account resets and runnable action fields. The evidence shows substantial product design and integration work, with the operational implementation and user interface still held back.
Anthropic's public documentation currently describes voice conversations with Claude and Cowork's ability to analyze existing meeting notes or recordings. It does not document a native Claude meeting recorder.
Anthropic is entering an occupied category
Granola.ai homepage
Granola already records computer audio without a meeting bot, connects to calendars and produces notes, actions and follow-ups across macOS, Windows, iOS and Android. Its established capture experience and cross-meeting memory give it a considerable lead over an unreleased Claude feature.
Notion is the closest functional comparison. Notion AI Meeting Notes captures system and microphone audio in its desktop app, requires macOS 13 or later on Macs, associates recordings with calendar events, labels speakers, and generates summaries and action items.
On July 31st, 2026, Notion added a trigger that runs Custom Agents after a meeting note is summarized. Those agents can update project trackers, post recaps and create engineering tickets. Anthropic would enter with a major incumbent already connecting meeting capture to agent execution.
Otter, Fathom and Fireflies offer mature transcription, cross-meeting search and integrations with CRM and project-management systems. Google Meet, Microsoft Teams and Zoom have the advantage of controlling their own meeting platforms, participant identities and enterprise policies.
Parka's action types show the opening Anthropic intends to pursue. A first-class code action could route engineering commitments directly into Claude Code, while cowork could handle documents, analysis and operational work. Anthropic appears to be designing the recorder around its own agents instead of a broad catalog of CRM and task-management integrations.
That still leaves major unanswered competitive questions. The contract contains no evidence of mobile capture, Windows launch support, cross-meeting search, collaborative editing, clips, audio playback, summary templates, consent announcements, enterprise retention controls or external workflow integrations.
A possible Deepgram connection
Separate infrastructure findings point toward a possible speech provider. Anthropic-controlled hosts under titanium.api.anthropic.com use names including stt-nova3-s0 through stt-nova3-s8 and stt-flux-multi , with staging variants also provisioned. The Nova-3 hosts exposed a private 10.104.0.6 address through public DNS, suggesting an internal deployment accidentally made visible outside Anthropic's network.
Those labels closely match Deepgram's speech-recognition products. Deepgram describes Nova-3 as its general-purpose real-time transcription model and Flux as a conversational model with turn detection. Its multilingual Flux model is named flux-general-multi . Deepgram also directs Nova-3 users to Keyterm Prompting , matching the keyterms argument accepted when Parka starts a recording.
Anthropic has previously published a Claude cookbook example using Deepgram for transcription, but neither company has announced a Parka partnership. Deepgram's January 2026 Series C announcement does not list Anthropic among its investors.
The Claude Desktop package contains no Deepgram hostname, SDK or credential linking Parka directly to the Titanium endpoints. Anthropic could be proxying a speech provider through its own infrastructure, and those services could support other voice products. The matching model names and keyterm interface make Deepgram a strong working hypothesis rather than a confirmed vendor attribution.
Owning the work before it reaches the agent
Meeting transcription and AI summaries are established product features. The strategic value sits one step later: deciding which system receives the context, creates the assignment and carries out the work.
Granola can send meeting memory toward Claude, Cursor, Replit and other AI tools. Notion can preserve the meeting inside a company workspace and trigger its own agents. If either product owns the recording and action-extraction layer, Claude becomes one possible destination downstream.
Parka would give Anthropic control of the entire sequence inside Claude: capture the conversation, identify commitments, turn them into prompts and open the agent sessions that complete them.
That is a more specific proposition than another AI notetaker. Anthropic is preparing to turn meetings into an inbox for Claude's agents.
