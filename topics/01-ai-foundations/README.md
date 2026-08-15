# Topic 1: AI foundations

You do not need to be a machine learning expert to use AI well in DevOps. You do need a working understanding of what these tools are, what they are good at, and where they fail. This page gives you that, aimed at operators, not researchers.

Trust level: Learn. Nothing here changes your systems. It builds the base for everything that follows.

## What a large language model is, in plain words

A large language model, or LLM, is a program that predicts the next piece of text based on the text it has seen. It has read a huge amount of writing and learned the patterns. When you ask it something, it produces the most likely helpful continuation.

That simple idea has two big consequences:

- It is very good at working with language: summarizing, explaining, rewriting, and drafting.
- It does not "know" facts the way a database does. It produces text that sounds right, which is usually right, but not always.

Keep both in mind. The strength and the weakness come from the same place.

## The words you will hear

- Token: a chunk of text, roughly a few characters. Models read and write in tokens. You often pay per token.
- Context window: how much text the model can look at in one go. Bigger windows cost more and can still miss details in the middle.
- Prompt: the text you give the model. Better prompts get better results.
- Temperature: a setting for how creative or random the output is. Low for factual work, higher for brainstorming.
- Hallucination: when the model states something false with confidence. This is the main risk to plan around.

See the [glossary](../../glossary/README.md) for more terms in plain language.

## Prompting that works for ops

You do not need tricks. A few habits get most of the value:

- Be specific about the task and the output you want.
- Give the model the real context: the log, the config, the error, the metric names.
- Ask it to show its reasoning or list its assumptions, so you can check them.
- Tell it what not to do, such as "do not suggest anything that changes production".

The [prompt library](../../prompts/README.md) has ready-made prompts built this way.

## RAG: grounding the model in your own knowledge

RAG stands for retrieval-augmented generation. The idea is simple. Before the model answers, you fetch the relevant parts of your own documents, runbooks, or past incidents, and hand them to the model along with the question. Now the answer is based on your reality, not just its training.

RAG is the single most useful pattern for making AI reliable in a specific environment. When you build your own helpers, this is usually where you start. See [topic 6](../06-build-your-own/README.md).

## Tool calling and agents

- Tool calling means the model can use functions you define, like "get the pods in this namespace". You control what tools exist and what they can do.
- An agent is a model that plans a series of steps and uses tools to carry them out.

This is powerful and also where risk enters, because now the model can do things, not just talk. The whole rest of this roadmap is about doing that safely, one trust level at a time.

## MCP, in one paragraph

MCP, the Model Context Protocol, is a common way to connect tools and data to models. Instead of writing custom glue for every tool, you expose it through MCP and many AI apps can use it. When you build helpers, start by exposing read-only tools through MCP before you expose anything that changes state.

## Hosted or local models

- Hosted: an API from a provider. Easy to start, strong results, but your input leaves your machine. Never send secrets or customer data.
- Local: runs on your own hardware, for example with Ollama. Your data stays with you. More setup, and results can be weaker for hard tasks.

A common pattern: local for sensitive data, hosted for general help where the input is safe.

## The failure modes to plan around

- Confident and wrong. Always verify before you act.
- Stale or missing context. The model only knows what you show it and what it was trained on.
- Non-deterministic. The same prompt can give different answers.
- Prompt injection. Hostile text in the input can try to change the model's behavior. Treat model input like untrusted user input.

If you design for these from the start, everything else in this roadmap gets safer.

## Next

Go to [topic 2: everyday ops](../02-everyday-ops/README.md), or back to [all topics](../README.md).
