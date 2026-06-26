---
title: Quantitative Analytics Engineering Intern
company: BlackRock
location: Mumbai, Maharashtra

start: 2026-01
end: 2026-06

skills:
  - Python
  - RAG
  - FastAPI
  - LangChain
  - Google ADK
  - Qdrant
  - Vector Search
  - Streamlit
  - WebSockets
  - Tree-sitter
  - SSE
  - Sybase
  - XML parsing
  - REST APIs

tags:
  - ai
  - agents
  - retrieval
  - backend
  - orchestration
  - harness
---

# AI Engineering

Built multiple RAG-based agents for natural-language querying over internal codebases and documentation — starting with test codebases, then expanding to production engines.

Designed ingestion pipelines to convert codebases and wiki/documentation into structured JSONL and Markdown formats, generate AI summaries per chunk, embed them, and store and search them through vector databases.

Worked on summary engine report workflows: generating reports from server-side processes, parsing XML/report outputs, extracting formulas from Excel tie-outs, embedding report context, and adding agent tools to retrieve and explain report information.

Explored retrieval strategies for explaining derived and calculated columns — including reading full files instead of just chunks, adjusting chunking granularity, and adapting retrieval approach based on feedback from domain experts.

Worked on mono-W knowledge tooling: embedded the W codebase, extracted workflow queries, integrated dependency-graph documentation, and extended the existing agent toolset with W-specific analysis capabilities.

Integrated internal AI model access through RockAI and BlackRock-approved chat-completions APIs, handling API-key setup, authentication flows (bearer tokens, basic auth, client-credentials), and reducing manual token refreshes by moving to client-credentials.

Set up Qdrant as a hosted vector database so the agent could share and query embeddings across teammates without relying on local vector-store files.

# AI Orchestration

Evaluated and compared multiple AI orchestration frameworks across prototype iterations: LangChain, Google ADK, raw tool-calling agents, and graph-based reasoning.

Experimented with hybrid workflows combining embeddings, file-level context injection, LLM reasoning, and metadata retrieval — iterating on which combination gave the most coherent answers for codebase understanding tasks.

Designed multi-tool agent workflows where the agent could dynamically select between tools (vector search, file read, database query, SSH) depending on the nature of the question.

Designed and prototyped specialized sub-agents for Sybase/ASE database connectivity, SSH host access, and Confluence/wiki retrieval — extending the core RAG agent with domain-specific tool-calling for downstream analysis workflows.

# Harness Engineering

Packaged the codebase-to-embeddings workflow first as a standalone executable, then refactored it into a FastAPI service with REST endpoints, branch support, bearer-token authentication, and distributed it to teammates for use in related projects.

Deployed a Streamlit-based demo interface for the AI agent on an internal compute session — debugged environment and configuration issues, fixed feedback and logging functionality for easier iterative testing.

Scaffolded a new backend for a regression-viewer agent: integrated internal database/connectivity libraries (Sybase, blkdbi/blkcore), implemented tool-calling interfaces, and added real-time communication — experimenting with SSE before settling on WebSockets.

Set up Sybase/ASE database connectivity from scratch for the regression-viewer project: handled credential setup, ASE driver configuration, and initial integration of database-backed tools into the agent workflow.

Parallelized the embedding ingestion pipeline, reducing processing time from ~7,000s to ~1,200s for a 3,000-line JSONL workload by implementing concurrent batching driven by API response cadence.
