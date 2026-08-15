# Tools catalog

A curated list of tools for using AI in DevOps, grouped by what they do. Each entry has a one-line description and a trust level, so you know how much control you keep.

These are starting points, not endorsements. Check each one against your own needs, and read its own docs, since features change over time.

Trust levels: Assist means it drafts or explains. Gate means it acts behind a review or check. Auto means it can act on its own, which you should approach with care.

## Kubernetes diagnosis

| Tool | What it does | Trust |
|------|--------------|-------|
| k8sgpt | Scans a cluster and explains problems in plain language. Read-only by default. | Assist |

See the [k8sgpt quickstart](../examples/k8sgpt-quickstart.md).

## Incident investigation

| Tool | What it does | Trust |
|------|--------------|-------|
| HolmesGPT (Robusta) | Helps investigate alerts and incidents by gathering context and suggesting causes. | Assist to Gate |

## Alerting and AIOps

| Tool | What it does | Trust |
|------|--------------|-------|
| Keep | Open-source alert management with some AI features for grouping and enrichment. | Assist to Gate |

## Running models

| Tool | What it does | Trust |
|------|--------------|-------|
| Ollama | Run open models on your own machine. Good when data cannot leave. | Learn |
| vLLM | Serve open models with good performance for heavier local use. | Learn |

## Building your own helpers

| Tool | What it does | Trust |
|------|--------------|-------|
| LangChain | A framework for building apps that use models, tools, and memory. | Build |
| LlamaIndex | A framework focused on connecting your data to models, useful for RAG. | Build |
| MCP (Model Context Protocol) | A common way to expose tools and data to models. Start with read-only tools. | Build |

## Watching your AI in production (LLMOps)

| Tool | What it does | Trust |
|------|--------------|-------|
| OpenTelemetry | Trace and measure AI calls the same way you trace services. | Learn |

## How to read this list

- Start with Assist tools. They explain and draft, and cannot change your systems.
- Move to Gate tools once you trust the Assist ones and have a review step in place.
- Be slow and careful with anything that can act on its own.

## Suggest a tool

Know a good one that is missing? Open an issue or a pull request. Say what it does in one line and give it a trust level. See the [contributing guide](../CONTRIBUTING.md).

Back to the [main roadmap](../README.md).
