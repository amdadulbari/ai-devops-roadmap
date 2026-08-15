# Cost and choosing a model

AI is useful, but it is not free, and the cost can surprise you if you are not watching. This page explains how the cost works, gives a worked example, and shows how to keep it low.

Prices change often, so this page does not quote current prices. It shows you how to reason about cost, and points you to the pricing pages to plug in today's numbers.

## How pricing works

With hosted models you pay per token. A token is a chunk of text, roughly a few characters, so a word is often one or two tokens. You pay for two things:

- Input tokens: everything you send, including your prompt and any logs or diffs.
- Output tokens: everything the model writes back.

Output usually costs more per token than input. Providers quote a price per million tokens. Check the current numbers on the [OpenAI pricing page](https://openai.com/api/pricing/) and the [Anthropic pricing page](https://www.anthropic.com/pricing).

## A worked example

Say you summarize a batch of logs. A rough request might be:

- Input: about 4,000 tokens (the prompt plus a chunk of logs).
- Output: about 500 tokens (the summary).

To find the cost, plug in the current price per million tokens for your model:

```
input cost  = 4000  / 1,000,000  x  input price per million
output cost = 500   / 1,000,000  x  output price per million
total       = input cost + output cost
```

For a small model, a single summary like this is a fraction of a cent. That sounds tiny, and it is, until you run it on every alert, every minute, across every service. Then it adds up. The point is not that one call is expensive. It is that volume and loops are where cost hides.

## Where cost really comes from

- Volume. One call is cheap. A million calls are not. Do the math for your expected volume, not for one request.
- Big context. Sending a huge log file or a giant diff every time is the most common way to overspend. Send only what is needed.
- Agents in a loop. An agent that calls the model many times to complete a task can cost far more than a single call, and a buggy loop can run away. Put a hard limit on steps.
- Large models by default. The biggest models cost many times more than small ones. Most ops tasks do not need the biggest.

## How to keep it low

- Start with a small model. Try the smallest one that does the job well. Move up only for tasks where the small one clearly falls short.
- Trim the input. Send the relevant time window of logs, not the whole file. Summarize first, then ask follow-up questions.
- Cache. If you ask the same thing often, cache the answer.
- Set spending limits. Most providers let you set a hard cap. Use it.
- Cap agent steps. Never let an agent loop without a maximum number of calls.
- Watch it. Track spend the way you track any other resource. See [Langfuse](https://github.com/langfuse/langfuse) and [OpenTelemetry](https://opentelemetry.io) for tracing AI calls.

## Local models: a different cost shape

If you run models locally with a tool like [Ollama](https://ollama.com) or [vLLM](https://github.com/vllm-project/vllm), you do not pay per token. You pay for the hardware and the power to run it. This is a fixed cost rather than a per-use cost. It is a good fit when you have steady, high volume, or when your data cannot leave your machines. The trade-off is setup effort and, often, weaker results than the largest hosted models.

## The short version

Use the smallest model that works, send only the context you need, cap anything that loops, and set a spending limit. Do that, and cost stays small and predictable.

Back to [getting started](getting-started.md) or the [main roadmap](../README.md).
