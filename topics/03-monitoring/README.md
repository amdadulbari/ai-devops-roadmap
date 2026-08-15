# Topic 3: Monitoring

This is the part of DevOps where AI saves the most time day to day. You are buried in signals from Prometheus, your logs, and your traces. AI is good at reading a lot of that fast and explaining it in plain words. You stay in charge of what to do next.

Trust level: Assist to Gate.

The golden rule for monitoring: start read-only. Let the AI look at your data and explain it. Do not give it permission to change anything until you trust it on the reading job first.

## Contents

- [Metrics](#metrics)
- [Logs](#logs)
- [Traces](#traces)
- [Bringing it together during an incident](#bringing-it-together-during-an-incident)
- [What AI is good at, and what it is not](#what-ai-is-good-at-and-what-it-is-not)
- [A safe setup to start with](#a-safe-setup-to-start-with)

## Metrics

Metrics tell you the shape of your system over time: request rates, error rates, latency, saturation. The hard part is often writing the right query and reading the result quickly.

Ways AI helps:

- Write a PromQL query from a plain description, so you do not have to remember the syntax. Always check the query before you run it. See the [prompt](../../prompts/natural-language-to-promql.md).
- Explain a spike or a drop. Paste the metric and a short description of the time window, and ask what changed and when.
- Summarize a busy dashboard into a few sentences for a status update.
- Line up a metric change with recent deploys or config changes to point at a likely cause. You still confirm the link.

Example: explain a latency spike.

```
Here is the p95 latency for the checkout service over the last hour:
<paste the values or a description of the shape>

We deployed checkout at 14:32.

Explain what the graph shows, whether the deploy lines up with the change,
and what I should check next. Read-only checks only.
```

Limit to remember: the model does not see your live system. It only sees what you paste. It can guess a cause, but you have to confirm it against the real metrics.

## Logs

Logs are where the detail lives, and also where the noise lives. A single problem can produce thousands of lines.

Ways AI helps:

- Turn a wall of logs into a short summary of what went wrong. See the [prompt](../../prompts/logs-to-summary.md).
- Group similar errors by root cause, so three real problems do not look like three thousand lines.
- Search logs by describing what you want, instead of memorizing query syntax for your log tool.
- Pull structured fields out of messy, unstructured log lines.

Example: find the first sign of trouble.

```
Here are the logs from 14:30 to 14:45:
<paste the logs>

Summarize what happened, group the errors by cause, and tell me the earliest
line that looks related to the problem. Give me the real line, not a paraphrase.
```

Two limits to remember:

- Do not paste secrets or customer data into a hosted model. Redact first, or use a local model.
- The model can miss the one line that matters, or invent a pattern that is not there. Open the real lines it points to and confirm them.

## Traces

Traces show the path of a single request across services. They are the best tool for "why was this slow", and often the hardest to read quickly.

Ways AI helps:

- Point to the slow span and explain why the request was slow. See the [prompt](../../prompts/explain-a-trace.md).
- Follow a request across services and summarize where the time went.
- Connect a slow trace to the metric or log that explains it.

Example: find the bottleneck.

```
Here is a trace for a slow checkout request:
<paste the spans with service names and durations>

Tell me which span took most of the time, why it was likely slow, and whether
it was waiting on a database or another service. Suggest what to check next.
```

Limit to remember: a trace shows where time went, not always why. The model can suggest a reason, but you confirm it with the service logs or a database query.

## Bringing it together during an incident

The real win is an assistant that reads metrics, logs, and traces at the same time and gives you one plain summary. Think of it as a fast junior engineer who reads everything and hands you a clear briefing. You still make the call.

A simple flow that works:

1. Paste the alert and the metric that fired.
2. Add the related logs from the same time window.
3. Add a trace of a slow or failed request if you have one.
4. Ask for one summary: what is happening, the most likely cause, and what to check next. Read-only checks only.

You get a fast, plain-language starting point. You keep control of every action. For the incident side of this, see [topic 4](../04-alerts-and-incidents/README.md).

## What AI is good at, and what it is not

Good at:

- Reading a lot of text fast and summarizing it.
- Explaining unfamiliar errors, queries, and syntax.
- Spotting patterns across many lines.
- Turning a plain description into a query or a draft.

Not good at, or not safe for:

- Being the source of truth. It only sees what you show it.
- Being certain. It can be confident and wrong. Verify before you act.
- Handling secrets. Never paste them into a hosted model.
- Taking action on its own in this stage. Keep it read-only while you build trust.

## A safe setup to start with

1. Pick one service you know well.
2. Give the AI read-only access to its metrics, logs, and traces, or just paste the data by hand at first.
3. Use it during a real but low-pressure investigation.
4. Check every claim it makes against the real system.
5. Once it reliably helps you read faster, then think about the next step, which is the Gate level.

The point is simple. Let AI help you read and understand your systems first. Earn trust there before you let it do anything else.

## Next

Go to [topic 4: alerts and incidents](../04-alerts-and-incidents/README.md), or back to [all topics](../README.md).
