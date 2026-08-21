# Redact before you send (runnable example)

The one rule this whole roadmap repeats is: never paste secrets, tokens, or
customer data into a hosted model. This is a small tool that helps you follow
it. It reads text, removes the obvious sensitive things, and prints the cleaned
version. No third-party packages, just Python 3.

Trust level: it is a safety helper. It never calls the network and never changes
your systems. It only edits text on your own machine.

## What it removes

- Private key blocks (`-----BEGIN ... PRIVATE KEY-----`).
- JWTs and bearer tokens.
- AWS access key ids, GitHub tokens, and Slack tokens.
- Passwords inside connection strings, like `postgres://user:pass@host`.
- Anything that looks like a `secret`, `password`, `token`, `api_key`, or
  `access_key` assignment.
- Email addresses, and optionally IP addresses (`--ips`).

Each match is replaced with a clear marker like `[REDACTED-SECRET]`, so the
model still sees the shape of your data without the sensitive value.

## Run it

Clean a file and read the result:

```
python3 redact.py sample.txt
```

See what it removed, with counts, while still getting the cleaned output:

```
python3 redact.py --report sample.txt
```

The real point is to put it in front of a model. Pipe your logs through it
first, then into the [log summarizer](../log-summarizer/README.md):

```
kubectl logs deploy/checkout --tail=200 | python3 redact.py | \
    python3 ../log-summarizer/summarize.py
```

## The sample

`sample.txt` is a made-up log full of things that should never leave your
machine: a database password, AWS keys, a JWT, a webhook secret, a GitHub
token, an email, and an IP. Run the tool on it and watch them all disappear.

## Read this before you rely on it

Redaction lowers risk. It does not remove it.

- It errs on the side of removing too much. If it is unsure, it redacts. You may
  see a normal word or a hostname get replaced, and that is the safe direction
  to fail in.
- It will still miss secrets it does not recognize. A new token format, a secret
  with no obvious name, or data that is sensitive only in context will slip
  through. Always read the output before you send it.
- It is not a substitute for a local model. For anything truly sensitive, run
  the model on your own machine with something like Ollama or vLLM, so the data
  never leaves at all. See [cost and model selection](../../docs/cost-and-model-selection.md).

## Where the human stays in control

The tool only suggests what to remove. You read the cleaned text and decide
whether it is safe to send. It never sends anything itself.

Back to [examples](../README.md).
