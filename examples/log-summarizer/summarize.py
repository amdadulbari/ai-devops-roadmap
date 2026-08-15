#!/usr/bin/env python3
"""
Summarize noisy logs with a model.

Reads log text from a file or from stdin, sends it to a model with a summary
prompt, and prints the summary. No third-party packages needed, just Python 3.

Two ways to run it:

1. Local model with Ollama (default, no API key, your data stays on your machine):
     ollama pull llama3          # once, to download the model
     python3 summarize.py sample.log

2. A hosted OpenAI-compatible API:
     export AI_API_KEY=your-key
     export AI_MODEL=gpt-4o-mini      # optional
     python3 summarize.py sample.log

Safety note: with the default local model nothing leaves your machine. With a
hosted API your logs are sent to the provider, so do not send secrets.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

PROMPT = """You are helping a DevOps engineer read logs.

Here are the logs:
{logs}

Do the following:
1. Summarize what happened in three sentences or fewer.
2. List the distinct errors, grouped by root cause, most important first.
3. For each group, give the count and one example line.
4. Point out the earliest line that looks related to the problem.
5. Suggest what to check next. Do not suggest anything that changes state.
"""


def build_messages(logs):
    return [{"role": "user", "content": PROMPT.format(logs=logs)}]


def call_ollama(base, model, messages):
    url = base.rstrip("/") + "/api/chat"
    body = json.dumps({"model": model, "messages": messages, "stream": False}).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as response:
        data = json.load(response)
    return data["message"]["content"]


def call_openai(base, key, model, messages):
    url = base.rstrip("/") + "/chat/completions"
    body = json.dumps({"model": model, "messages": messages}).encode()
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + key}
    req = urllib.request.Request(url, data=body, headers=headers)
    with urllib.request.urlopen(req) as response:
        data = json.load(response)
    return data["choices"][0]["message"]["content"]


def main():
    parser = argparse.ArgumentParser(description="Summarize logs with a model.")
    parser.add_argument("logfile", nargs="?", help="Path to a log file. If omitted, reads stdin.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the request that would be sent, without calling the model.",
    )
    args = parser.parse_args()

    logs = open(args.logfile, encoding="utf-8").read() if args.logfile else sys.stdin.read()
    if not logs.strip():
        print("No log input. Pass a file path or pipe logs on stdin.", file=sys.stderr)
        sys.exit(1)

    messages = build_messages(logs)

    key = os.environ.get("AI_API_KEY")
    model = os.environ.get("AI_MODEL")
    if key:
        provider = "openai-compatible"
        base = os.environ.get("AI_BASE_URL", "https://api.openai.com/v1")
        model = model or "gpt-4o-mini"
    else:
        provider = "ollama"
        base = os.environ.get("OLLAMA_URL", "http://localhost:11434")
        model = model or "llama3"

    if args.dry_run:
        print(f"provider: {provider}")
        print(f"base: {base}")
        print(f"model: {model}")
        print("\nrequest messages:")
        print(json.dumps(messages, indent=2))
        return

    try:
        if provider == "openai-compatible":
            output = call_openai(base, key, model, messages)
        else:
            output = call_ollama(base, model, messages)
    except urllib.error.URLError as error:
        print(f"Could not reach the model at {base}: {error}", file=sys.stderr)
        if provider == "ollama":
            print("Is Ollama running? Try: ollama serve  (and: ollama pull llama3)", file=sys.stderr)
        sys.exit(2)

    print(output)


if __name__ == "__main__":
    main()
