# Log summarizer (runnable example)

A small, real command-line tool that reads logs and asks a model to summarize them. It needs no third-party packages, just Python 3. This is the "hello world" of using AI in ops: read-only, safe, and useful.

Trust level: Assist. It reads and summarizes. It never changes anything.

## What it does

It takes log text, sends it to a model with the [logs to summary prompt](../../prompts/logs-to-summary.md), and prints:

1. A short summary of what happened.
2. The distinct errors, grouped by root cause.
3. A count and example for each.
4. The earliest line that looks related.
5. What to check next.

## Run it with a local model (no API key, data stays local)

This is the recommended way, because your logs never leave your machine. You need [Ollama](https://ollama.com) installed.

```
ollama pull llama3
python3 summarize.py sample.log
```

That is it. It reads the included `sample.log` and prints a summary.

## Run it with a hosted API

If you would rather use a hosted OpenAI-compatible API:

```
export AI_API_KEY=your-key
export AI_MODEL=gpt-4o-mini        # optional, this is the default
python3 summarize.py sample.log
```

Do not do this with logs that contain secrets or customer data. Use the local model for anything sensitive.

## Other ways to run it

Pipe logs in from another command:

```
kubectl logs deploy/checkout --tail=200 | python3 summarize.py
```

See exactly what would be sent, without calling a model:

```
python3 summarize.py --dry-run sample.log
```

## The sample log

`sample.log` is a made-up but realistic story: a service cannot reach its database, falls back to a degraded mode, then hits a nil pointer and runs out of memory. A good summary should spot that the database timeout is the root cause and that the crash came after.

## Settings

The tool reads these environment variables:

| Variable | What it does | Default |
|----------|--------------|---------|
| `AI_API_KEY` | If set, use a hosted OpenAI-compatible API instead of Ollama | not set |
| `AI_MODEL` | The model name | `llama3` for Ollama, `gpt-4o-mini` for the API |
| `AI_BASE_URL` | Base URL for the hosted API | `https://api.openai.com/v1` |
| `OLLAMA_URL` | Base URL for Ollama | `http://localhost:11434` |

## Where the human stays in control

The tool only reads and summarizes. It suggests what to check next, but it never runs those checks. You decide what to do.

Back to [examples](../README.md).
