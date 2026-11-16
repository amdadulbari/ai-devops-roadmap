# Glossary

Plain-language definitions of the AI terms you will meet in this roadmap. No jargon, no math. If a term here is unclear, open an issue and we will improve it.

### Agent

A model that plans a series of steps and uses tools to carry them out, instead of just answering in text. Powerful, and the point where you need gates and least privilege.

### AI gateway

One endpoint that sits between your teams and the model providers. It is where you put per-team keys, spend caps, rate limits, and logging, so you are not chasing API keys around a dozen repos.

### Context window

How much text a model can look at in one request, measured in tokens. Bigger windows cost more and can still miss details buried in the middle.

### Embedding

A way to turn text into numbers so a computer can find similar text. It is what powers search in a RAG system.

### Eval

A test suite for AI output. A set of inputs with known-good answers that you run after changing a prompt or a model, so a quiet regression shows up before your users find it. The AI version of a unit test, and just as worth having.

### Excessive agency

Giving a model or agent more power than its job needs: broader credentials, more tools, or the ability to act without review. One of the top risks on OWASP's 2026 list for LLM applications, and the thing trust levels exist to prevent.

### Fine-tuning

Training a base model further on your own examples so it behaves a certain way. Often not needed. RAG solves many problems more simply.

### Guardrail

A check that limits what a model or agent can do. For example, validating the output format, or requiring human approval before an action.

### Hallucination

When a model states something false with confidence. The main risk to plan around. The fix is grounding (RAG), verification, and human review.

### Human in the loop

A design where a person reviews or approves what the AI does before it takes effect. The core idea of this whole roadmap.

### Inference

Running a model to get an answer. When you send a prompt and get a response, that is inference. It costs money and time.

### LLM (large language model)

A program that predicts the next piece of text based on patterns it learned from a huge amount of writing. Great with language, not a source of hard facts.

### LLMOps

Running AI features like production software: testing prompts, evaluating quality, tracing calls, watching cost, and versioning prompts and models.

### MCP (Model Context Protocol)

A common way to connect tools and data to models, so many AI apps can use the same tools. Expose read-only tools first.

### MCP server

A process that exposes a set of tools or data to models over MCP. Worth remembering that it is code running with whatever access you gave it, so treat one you did not write like any other dependency near production.

### Model

The AI itself. Different models have different sizes, costs, and strengths. Try a small one first and reach for a big one only when needed.

### Prompt

The text you give a model. Clear, specific prompts with real context get better results.

### Prompt injection

An attack where hostile text in the input tries to change the model's behavior, for example "ignore your instructions". Treat model input like untrusted user input.

### RAG (retrieval-augmented generation)

Fetching your own relevant documents and giving them to the model with the question, so the answer is based on your reality. The most useful pattern for reliable AI in a specific environment.

### Temperature

A setting for how random the output is. Low for factual and repeatable work. Higher for brainstorming.

### Token

A chunk of text, roughly a few characters. Models read and write in tokens, and you usually pay per token.

### Tool calling

Letting a model use functions you define, such as "get the pods in a namespace". You control which tools exist and what they can do.

### Vector database

A store built to find similar embeddings quickly. It is the memory behind a RAG system.

Back to the [main roadmap](../README.md).
