# Explain a slow trace

Use this when a request is slow and you have a distributed trace but not the time to read every span.

Trust level: Assist. The AI reads the trace and explains. You confirm.

## Prompt

```
You are helping a DevOps engineer read a distributed trace.

Here is the trace (spans with service names, durations, and any attributes):
<paste the trace data>

Do the following:
1. Say where most of the time went, with the service and span named.
2. Explain the likely reason that span was slow.
3. Point out any span that waited on another service or a database.
4. Suggest what to look at next to confirm the cause. Read-only checks only.

If the trace does not clearly show the cause, say so and tell me what extra data would help.
```

## Tips

- Export the trace from your tool, such as Jaeger, Tempo, or an OpenTelemetry backend.
- Ask a follow-up if the slow span is a database call, such as which query to check.
- Confirm the finding against your metrics before you change anything.
