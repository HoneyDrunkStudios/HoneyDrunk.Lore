---
source: "https://github.com/vitali87/code-graph-rag"
title: "Code-Graph-RAG (GitHub Repo)"
author: "TLDR DevOps"
date_published: "2026-08-12"
date_clipped: "2026-08-14"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-08-12"
source_role: "primary-via-tldr"
---

# Code-Graph-RAG (GitHub Repo)

Source: https://github.com/vitali87/code-graph-rag

Code-Graph-RAG
Code-Graph-RAG parses a multi-language codebase with Tree-sitter, builds a knowledge graph of its structure in Memgraph, and lets you query, edit, and optimise that code in plain English. It works across a monorepo of mixed languages under one unified graph schema.
Latest News 🔥
Ruby Support : Ruby joins the graph through a new pluggable ast-grep tier that adds a language from a single YAML pattern file, emitting Module , Function , and Class nodes plus import edges without a hand-written parser.
Structural Search & Replace : Find and rewrite code by AST pattern with ast-grep, exposed as agent tools so you can match and transform structure across the whole codebase instead of relying on text or regex.
Data-Flow Tracing : New FLOWS_TO taint edges follow values through assignments, function calls, and I/O sinks. This release adds C#, Java, C, and Go, bringing tracing to 10 languages (Python, JavaScript, TypeScript/TSX, Go, Java, Rust, C++, C, and C#).
See NEWS.md for the full history.
What It Does
Point Code-Graph-RAG at a repository and it reads every source file, extracts functions, classes, methods, modules, and the relationships between them, and stores the result as an interconnected graph. Once the graph exists you can:
Ask questions about the codebase in natural language and get answers grounded in the real structure.
Retrieve the actual source of any function, class, or method by name or by intent.
Edit code through the agent with AST-based surgical patching and a diff preview before anything changes.
Optimise code against language best practices or your own coding standards.
Find dead code by walking call and reference edges from entry points.
Search and rewrite structurally by AST pattern with ast-grep.
How It Works
The system has two components:
Multi-language parser. A Tree-sitter based parser reads the codebase and ingests functions, classes, methods, modules, and their relationships into Memgraph under a single language-agnostic schema.
RAG system ( codebase_rag/ ). An interactive CLI that turns natural language into Cypher queries, retrieves matching code, and drives AI-powered editing and optimisation.
Source Code -> Tree-sitter Parser -> AST Analysis -> Memgraph Knowledge Graph
|
User Query -> AI Model (Cypher Gen) -> Cypher Query -> Graph Results -> Response
See the Architecture Overview and Graph Schema for the full picture.
Supported Languages
Python, TypeScript, TSX, JavaScript, Rust, Go, Java, C, C++, C#, PHP, Lua, and Dart are fully supported. Scala is in development, and Ruby has structural support (modules, functions, classes, and imports) through the pluggable ast-grep tier. See the Language Support matrix for per-language capabilities.
Installation
cgr is published to PyPI. Install it system-wide with the treesitter-full (all languages) and semantic (vector search) extras:
# with uv (recommended)
uv tool install " code-graph-rag[treesitter-full,semantic] "
# or with pipx
pipx install " code-graph-rag[treesitter-full,semantic] "
You also need Docker (for Memgraph), cmake , and ripgrep . Full prerequisites, source installs, and environment setup are in the Installation guide.
Quick Start
# Start the packaged Memgraph + Qdrant stack (no compose file needed)
cgr daemon up
# Parse a repository into the graph, then query it
cgr start --repo-path /path/to/repo --update-graph
cgr start --repo-path /path/to/repo
Repeat the first command for each repository you want indexed; the graph is
shared, and syncing one project leaves the others alone. To start over from an
empty graph, add --clean — it deletes every project in the shared graph,
not just this one, and asks for confirmation first when other
projects would be destroyed.
The Quick Start guide walks through parsing, querying, and exporting in five minutes.
MCP Server
Code-Graph-RAG runs as an MCP server so Claude Code and other MCP clients can query and edit your codebase directly. See the MCP Server guide for setup.
Documentation
Getting Started
Installation
Quick Start
Configuration
User Guide
CLI Reference
Interactive Querying
Code Optimisation
Dead Code Detection
Graph Export
Real-Time Updates
MCP Server
Architecture
Overview
Graph Schema
Language Support
Data-Flow Edges
Python SDK
Overview
Graph Loader
Cypher Generator
Semantic Search
Advanced
Adding Languages
Ignore Patterns
Building Binaries
Troubleshooting
Enterprise Services
Code-Graph-RAG is open source and free to use. For organisations that need more, we offer fully managed cloud-hosted solutions and on-premise deployments :
Cloud-Hosted Deployment : Managed cloud infrastructure for both the graph database and the AI agent connection. Zero infrastructure overhead, so we handle scaling, updates, and availability while your team focuses on building.
On-Premise & Air-Gapped Deployment : Deploy Code-Graph-RAG entirely within your own environment, including air-gapped networks. Full data sovereignty for regulated industries and security-sensitive organisations.
We also offer custom development, integration consulting, technical support contracts, and team training.
View plans & pricing at code-graph-rag.com
Contributing
Please see CONTRIBUTING.md for contribution guidelines. Good first PRs come from the TODO issues.
Support
For issues or questions, check the Troubleshooting guide first, then open an issue.
License
MIT. See LICENSE .
