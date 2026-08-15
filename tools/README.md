# Tools catalog

A curated list of tools for using AI in DevOps, grouped by what they do. Each entry has a link, a one-line description, and a trust level, so you know how much control you keep.

These are starting points, not endorsements. Check each one against your own needs, and read its own docs, since features change over time.

Trust levels: Assist means it drafts or explains. Gate means it acts behind a review or check. Auto means it can act on its own, which you should approach with care.

## Kubernetes diagnosis

| Tool | What it does | Trust |
|------|--------------|-------|
| [k8sgpt](https://github.com/k8sgpt-ai/k8sgpt) | Scans a cluster and explains problems in plain language. Read-only by default. | Assist |

See the [k8sgpt quickstart](../examples/k8sgpt-quickstart.md).

## Incident investigation

| Tool | What it does | Trust |
|------|--------------|-------|
| [HolmesGPT](https://github.com/robusta-dev/holmesgpt) | Investigates alerts and incidents by gathering context and suggesting causes. | Assist to Gate |
| [Robusta](https://github.com/robusta-dev/robusta) | Kubernetes monitoring and automation, with enrichment for alerts. | Assist to Gate |

## Alerting and AIOps

| Tool | What it does | Trust |
|------|--------------|-------|
| [Keep](https://github.com/keephq/keep) | Open-source alert management with grouping and enrichment features. | Assist to Gate |

## Workflow and automation

These let you wire AI into your ops workflows, and most support a human-approval step, which fits the Gate level well.

| Tool | What it does | Trust |
|------|--------------|-------|
| [n8n](https://github.com/n8n-io/n8n) | Visual workflow automation. Build flows like alert to AI enrichment to Slack, with a human-approval step in the middle. | Gate |
| [Flowise](https://github.com/FlowiseAI/Flowise) | Visual builder for AI apps and agents, useful for prototyping a helper before you code it. | Build |
| [Dify](https://github.com/langgenius/dify) | Platform for building and running AI apps, with tools and workflows. | Build |

## Agent and app frameworks

For when you build your own helpers. See [topic 6](../topics/06-build-your-own/README.md).

| Tool | What it does | Trust |
|------|--------------|-------|
| [LangChain](https://github.com/langchain-ai/langchain) | A framework for building apps that use models, tools, and memory. | Build |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Build agent workflows as graphs, which makes approval steps explicit. | Build |
| [LlamaIndex](https://github.com/run-llama/llama_index) | Focused on connecting your data to models, useful for RAG. | Build |
| [CrewAI](https://github.com/crewAIInc/crewAI) | A framework for coordinating multiple agents on a task. | Build |

## Running models

| Tool | What it does | Trust |
|------|--------------|-------|
| [Ollama](https://ollama.com) | Run open models on your own machine. Good when data cannot leave. | Learn |
| [vLLM](https://github.com/vllm-project/vllm) | Serve open models with good performance for heavier local use. | Learn |

## Connecting tools to models

| Tool | What it does | Trust |
|------|--------------|-------|
| [Model Context Protocol (MCP)](https://modelcontextprotocol.io) | A common way to expose tools and data to models. Start with read-only tools. | Build |

## Watching your AI in production (LLMOps)

| Tool | What it does | Trust |
|------|--------------|-------|
| [Langfuse](https://github.com/langfuse/langfuse) | Open-source tracing, evaluation, and cost tracking for AI features. | Learn |
| [OpenTelemetry](https://opentelemetry.io) | Trace and measure AI calls the same way you trace services. | Learn |

## Policy and security, to gate AI actions

These are not AI tools, but they are how you keep AI changes safe. See [topic 5](../topics/05-cicd-and-gitops/README.md) and [topic 7](../topics/07-production-safety/README.md).

| Tool | What it does | Trust |
|------|--------------|-------|
| [Kyverno](https://kyverno.io) | Kubernetes policy engine. Put it in front of any change an AI proposes. | Gate |
| [Open Policy Agent (OPA)](https://www.openpolicyagent.org) | General policy engine for validating changes against your rules. | Gate |
| [Trivy](https://github.com/aquasecurity/trivy) | Scans for vulnerabilities and misconfigurations. Pairs well with AI triage. | Assist |

## How to read this list

- Start with Assist tools. They explain and draft, and cannot change your systems.
- Move to Gate tools once you trust the Assist ones and have a review step in place.
- Be slow and careful with anything that can act on its own.

## Suggest a tool

Know a good one that is missing? Open an issue or a pull request. Add the link, say what it does in one line, and give it a trust level. See the [contributing guide](../CONTRIBUTING.md).

Back to the [main roadmap](../README.md).
