# Getting started

This page helps you take the first step, even if you have never used AI in your work before. It is short on purpose.

## Pick where to start

Match your situation to a starting point:

- New to using AI at work: start with the [prompt library](../prompts/README.md). Try the logs summary or the PromQL prompt on a real task today.
- Already using AI to read logs and write config: read the [monitoring guide](../topics/03-monitoring/README.md), then look at Stage 3 in the main roadmap (AI in CI/CD and GitOps).
- Ready to build your own tools: jump to Stage 5 and Stage 6 in the main [README](../README.md).

## Choose how you will run models

You have two main choices, and the right one depends on your data.

- Hosted models (an API from a provider). Easy to start, strong results. The catch: your input leaves your machine, so never send secrets or customer data.
- Local models (run on your own hardware, for example with Ollama). Your data stays with you. Good for sensitive work. The catch: setup takes more effort and results can be weaker for hard tasks.

A common pattern: use a local model for anything with sensitive data, and a hosted model for general help where the input is safe to share.

## Your first three tasks

Try these on real work this week. Each one is low risk.

1. Paste a confusing block of logs and ask for a summary. Compare it to what you already know.
2. Describe a metric you want and ask for the PromQL. Check the query before you run it.
3. Take a pull request and ask for a plain-language summary and a risk rating. Review it yourself as usual.

If AI helps on these three, you have found where it fits. Grow from there, one trust level at a time.

## The habit that keeps you safe

Before you paste anything, ask one question: is there a secret or customer detail in here? If yes, redact it or use a local model.

Before you act on any answer, ask one more: have I confirmed this against the real system? If no, check first.

Those two habits cover most of the risk.
