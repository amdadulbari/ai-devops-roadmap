# AI for DevOps: A Practical Roadmap

A hands-on guide to using AI in real DevOps and platform work, without losing control of your systems.

Most guides show you flashy AI demos. This one answers the question you actually care about at work: where can AI help, and how do you keep it safe near production? The short version is simple. Let AI do the reading, drafting, and explaining. Keep humans and policy in charge of the doing.

This is written from day-to-day platform engineering: Kubernetes, GitOps, policy as code, and observability. It is meant to be useful whether you are just starting with AI or already building tools with it.

## Who this is for

- DevOps, platform, and SRE engineers who want to use AI in their daily work.
- Team leads deciding where AI fits and where it does not belong.
- Engineers from an AI background who want to understand how ops teams actually run things.

## The one idea to remember

AI proposes. People and policy decide.

The quickest way to lose trust in AI at work is to let it change production without review. So we group every use of AI into three levels of trust:

| Level | What it means | Example |
|-------|---------------|---------|
| Assist | AI drafts, a person does everything | "Write me a Kyverno policy for this issue" |
| Gate | AI acts, but a review or policy check stands between it and production | AI opens a pull request that must pass checks and be merged by a person |
| Auto | AI acts on its own, only after it has proven itself on a narrow, well-tested task | Automatic rollback on a signal you fully trust |

Start at Assist. Move to Gate as you build confidence. Treat Auto as the rare exception that has to earn its place.

## Contents

1. [Everyday help](#1-everyday-help)
2. [Watching your systems: metrics, logs, and traces](#2-watching-your-systems-metrics-logs-and-traces)
3. [Alerts and incidents](#3-alerts-and-incidents)
4. [AI in CI/CD and GitOps](#4-ai-in-cicd-and-gitops)
5. [Building your own AI helpers](#5-building-your-own-ai-helpers)
6. [Keeping it safe in production](#6-keeping-it-safe-in-production)
7. [Tools worth knowing](#7-tools-worth-knowing)
8. [Things to avoid](#8-things-to-avoid)

## 1. Everyday help

This is where almost everyone should start. It is low risk because you review everything before it runs. Trust level: Assist.

- Write and clean up Terraform, Helm charts, Kustomize, and Kubernetes manifests.
- Turn a requirement or a security finding into a draft policy (Kyverno, OPA, conftest).
- Explain a confusing log line, stack trace, or error message in plain language.
- Write and improve runbooks and internal docs.
- Summarize a pull request or draft a clear commit message.
- Answer read-only questions in Slack, like "which services are on version 1.4".

One rule: never paste secrets, tokens, or customer data into a hosted model. Redact first, or use a model that runs locally.

## 2. Watching your systems: metrics, logs, and traces

This is where AI saves the most time day to day. You are drowning in signals, and AI is good at reading a lot of text fast and explaining it in words. You stay in charge of what to do next. Trust level: Assist to Gate.

### Metrics

- Ask questions in plain language and get a PromQL query back, then check it before running.
- Get a spike or a drop explained: what went up, when, and what changed around that time.
- Summarize a busy dashboard into a few sentences for a status update.
- Line up a metric change with recent deploys or config changes to point at a likely cause.

### Logs

- Turn thousands of noisy log lines into a short summary of what actually went wrong.
- Group similar errors together so you see three real problems instead of three thousand lines.
- Search logs by describing what you want, instead of memorizing query syntax.
- Pull the useful fields out of messy, unstructured logs.

### Traces

- Point to the slow span in a distributed trace and explain why the request was slow.
- Follow a request across services and summarize where the time went.
- Connect a slow trace to the metric or log that explains it.

### Putting it together

The real win is an assistant that reads metrics, logs, and traces at the same time and gives you one plain summary during an incident. Think of it as a fast junior engineer who reads everything and hands you a clear briefing. You still make the call.

A safe way to start: keep it read-only. Let the AI look at your observability data and explain it. Do not give it permission to change anything yet.

## 3. Alerts and incidents

Trust level: Gate. AI helps the on-call person; the on-call person stays in control.

- Enrich an alert with context: recent deploys, past similar incidents, and the matching runbook.
- Suggest a first set of things to check, in priority order.
- Offer possible causes with the evidence behind them, not a single confident guess.
- Draft a blameless incident timeline and postmortem for a person to edit and finish.

The goal is a calmer 3 a.m. The AI does the gathering and drafting. The human decides and acts.

## 4. AI in CI/CD and GitOps

Trust level: Gate. This is the sweet spot, because a pull request is a natural place to keep a human in the loop.

- Add AI review to pull requests: a plain-language summary of the change and its risks.
- Generate tests and test data for new code.
- Turn a pile of vulnerability findings into a short, ranked, explained list.
- Let AI fix things through Git, not through direct access. Instead of running commands on the cluster, it opens a pull request to your GitOps repo. Argo CD or Flux applies the change after a person merges it.
- Run every AI-proposed change through your normal policy checks (Kyverno, OPA, conftest) before the pull request is even opened. The AI has to pass the same gates a human does.

The rule that keeps this safe: the AI's only tools are Git and a pull request. It gets no direct write access to the cluster or the cloud.

## 5. Building your own AI helpers

When you are ready to build tools instead of just using them. Trust level: build carefully, test hard.

- Learn tool calling: how a model actually does things through functions you define.
- Learn RAG (retrieval-augmented generation): grounding the model in your own runbooks, docs, and past incidents so it stops guessing.
- Look at MCP (Model Context Protocol), a common way to connect tools to models. Start with read-only tools.
- Design the approval step first, not last. Decide up front where a human says yes.
- Track quality over time: test your prompts like code, watch for regressions, and log what the model did.
- Watch cost and speed. Try a small, cheap model first and only reach for a big one when you need it.

## 6. Keeping it safe in production

The part most guides skip. This is where your security and platform experience matters most.

- Give AI agents the least access they need. No standing production credentials. Use short-lived, scoped tokens.
- Put policy in front of anything an agent proposes (Kyverno or OPA), so it cannot suggest something that breaks your rules.
- Log every AI decision: the input, the reasoning, and the action taken. You want a clear audit trail.
- Watch for prompt injection, where hostile input tries to make the model do something it should not. Treat model input like untrusted user input.
- Keep a kill switch and limit the blast radius. If something goes wrong, you want to stop it fast and keep the damage small.
- Be honest about when not to use AI at all.

## 7. Tools worth knowing

A short, honest list. These are starting points, not endorsements. Check each one against your own needs.

- k8sgpt: scans a Kubernetes cluster and explains what is wrong in plain language.
- HolmesGPT (Robusta): helps investigate alerts and incidents.
- Keep: open-source alert management with some AI features.
- Ollama and vLLM: run models locally when you cannot send data to a hosted API.
- LangChain and LlamaIndex: frameworks for building your own AI tools.

## 8. Things to avoid

- Letting an agent run apply commands against production with no review step.
- Pasting secrets or customer data into a hosted model.
- Trusting a confident answer that has no grounding and no sources.
- Automating a fix based on a noisy or unproven signal.
- Running an agent with broad, standing credentials.
- Having no record of what the AI did and why.

## How to use this roadmap

1. Find your level. Already shipping infrastructure code every day? Start at section 4. Building tools? Jump to section 5.
2. Move up one trust level at a time. Earn it with reliability.
3. Pick one item, try it for real, then show a teammate how it worked.
4. Use the safety notes as a checklist before anything touches production.

## Contributing

Contributions are very welcome. You can:

- Add a tool, resource, or short guide under the right section.
- Tag any tool with a trust level (Assist, Gate, or Auto) and one line on where the human stays in control.
- Keep it practical. Real, tested advice beats hype.

See CONTRIBUTING.md for details.

## License

Content is licensed under CC BY 4.0. Any code samples are MIT licensed. See LICENSE.

## Maintainer

Maintained by Amdadul Bari Imad, a DevOps and platform engineer. Site: https://amdadulbari.com

If this helped you use AI at work without losing sleep, a star helps other people find it.
