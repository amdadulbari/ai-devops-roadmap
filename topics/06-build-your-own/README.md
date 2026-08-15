# Topic 6: Build your own helpers

At some point you will want to build your own AI tools, not just use other people's. This page covers what you need to know to do that well and safely.

Trust level: Build carefully and test hard.

## Start with the smallest useful thing

Do not start by building an agent that can do everything. Start with one small, read-only helper that does one job, such as summarizing an alert with context from your runbooks. Get that reliable. Then grow.

## The building blocks

### Tool calling

Tool calling lets the model use functions you define, like "get the pods in a namespace" or "fetch the last five deploys". You write the functions. You decide what they can do. Start with read-only tools. Add tools that change state only later, and put a gate in front of them.

### RAG over your own knowledge

RAG, retrieval-augmented generation, means fetching your relevant docs, runbooks, and past incidents and giving them to the model with the question. This is what makes a helper reliable in your environment instead of generic. For most ops helpers, RAG over your runbooks is the highest-value thing you can build.

### MCP for connecting tools

MCP, the Model Context Protocol, is a common way to expose tools and data to models. If you expose your tools through MCP, many AI apps can use them. Expose read-only tools first. Be very careful before you expose anything that changes state.

## Design the gate first, not last

The most important design choice is where a human says yes. Decide it before you write the fun parts. Good gates:

- The helper proposes a change as a pull request, and a person merges it.
- The helper posts a suggested action to Slack, and a person clicks approve.
- The helper explains and recommends, and a person does the action.

If you cannot describe where the human approves, you are not ready to let the helper act.

## LLMOps: running AI like production software

Once your helper matters, treat it like real software:

- Evaluate it. Build a set of test cases and check the quality of the output when you change a prompt or a model.
- Test prompts like code. A prompt change can quietly break things. Catch it with tests.
- Trace and log. Record inputs, outputs, and actions. OpenTelemetry can trace AI calls the same way it traces services.
- Watch cost and latency. Try a small, cheap model first. Use a big one only when you need it. Cache where you can.
- Version your prompts and models, so you know what produced a given result.

## Guardrails

- Validate the model's output before you use it. If it should be YAML, parse it. If it should be one of three choices, check that it is.
- Limit what tools can do. A read tool cannot cause much harm. A write tool needs a gate.
- Handle the case where the model is wrong or the tool fails. Do not assume success.

## Next

Go to [topic 7: production safety](../07-production-safety/README.md), or back to [all topics](../README.md).
