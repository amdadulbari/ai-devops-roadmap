#!/usr/bin/env python3
"""
Redact secrets and personal data from text before you paste it into a model.

Reads text from a file or from stdin, removes things that should never leave
your machine (keys, tokens, passwords, private keys, emails), and prints the
cleaned text to stdout. No third-party packages needed, just Python 3.

This tool never calls the network. It only edits text on your own machine.

Typical use, piping logs straight into a summarizer:

    kubectl logs deploy/checkout --tail=200 | python3 redact.py | \
        python3 ../log-summarizer/summarize.py

See what would be removed, with counts, without changing the output you read:

    python3 redact.py --report sample.txt

Important: redaction lowers risk, it does not remove it. This tool errs on the
side of removing too much, and it will still miss secrets it does not
recognize. For anything truly sensitive, use a model that runs locally so the
data never leaves your machine at all.
"""

import argparse
import re
import sys

# Each rule is (name, compiled pattern, replacement). Order matters: broad,
# structural patterns (private keys) run before narrower ones, and the generic
# "key = value" rule runs after the specific token shapes so it does not fight
# them. Every replacement makes the text safer, never less safe, so when a rule
# is unsure it over-redacts on purpose.
RULES = [
    (
        "private key",
        re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.DOTALL),
        "[REDACTED-PRIVATE-KEY]",
    ),
    (
        "JWT",
        re.compile(r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"),
        "[REDACTED-JWT]",
    ),
    (
        "AWS access key id",
        re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
        "[REDACTED-AWS-KEY]",
    ),
    (
        "GitHub token",
        re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
        "[REDACTED-TOKEN]",
    ),
    (
        "Slack token",
        re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
        "[REDACTED-TOKEN]",
    ),
    (
        "bearer token",
        re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/\-]+=*"),
        "Bearer [REDACTED-TOKEN]",
    ),
    (
        "url password",
        re.compile(r"(?i)([a-z][a-z0-9+.\-]*://[^:/\s@]+):[^@/\s]+@"),
        r"\1:[REDACTED-PASSWORD]@",
    ),
    (
        "secret assignment",
        re.compile(
            r"(?i)"
            r"([A-Za-z0-9_.\-]*"
            r"(?:password|passwd|pwd|secret|token|apikey|api[_-]?key|access[_-]?key|auth|credential)"
            r"[A-Za-z0-9_.\-]*)"
            r'(["\']?\s*[:=]\s*)'
            r"(['\"]?)"
            r"([^\s\"',;]+)"
        ),
        r"\1\2\3[REDACTED-SECRET]",
    ),
    (
        "email",
        re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
        "[REDACTED-EMAIL]",
    ),
]

IP_RULE = (
    "ip address",
    re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "[REDACTED-IP]",
)


def redact(text, redact_ips=False):
    """Return (cleaned_text, counts) where counts maps rule name to hits."""
    rules = list(RULES)
    if redact_ips:
        rules.append(IP_RULE)

    counts = {}
    for name, pattern, replacement in rules:
        text, hits = pattern.subn(replacement, text)
        if hits:
            counts[name] = hits
    return text, counts


def main():
    parser = argparse.ArgumentParser(
        description="Redact secrets and personal data from text before sending it to a model."
    )
    parser.add_argument("file", nargs="?", help="Path to a text file. If omitted, reads stdin.")
    parser.add_argument(
        "--ips",
        action="store_true",
        help="Also redact IPv4 addresses. Off by default, since logs often need them.",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print a count of what was redacted, to stderr, in addition to the output.",
    )
    args = parser.parse_args()

    text = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()

    cleaned, counts = redact(text, redact_ips=args.ips)

    sys.stdout.write(cleaned)

    if args.report:
        total = sum(counts.values())
        if total:
            print(f"\nredacted {total} item(s):", file=sys.stderr)
            for name in sorted(counts):
                print(f"  {counts[name]:>3}  {name}", file=sys.stderr)
        else:
            print("\nnothing matched. review the text yourself before sending it.", file=sys.stderr)


if __name__ == "__main__":
    main()
