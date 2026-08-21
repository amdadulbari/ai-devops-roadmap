# Examples

Small, concrete examples you can learn from and adapt. Each one keeps a human in control.

These are teaching examples. Read them, understand them, and adjust them to your own setup before you use them. Do not copy an example into production without review.

## Available examples

- [Redact before you send](redact/README.md): a small, runnable tool that strips secrets, tokens, and emails out of text before you paste it into a hosted model. Follows the one rule this roadmap repeats most. No packages to install.
- [Log summarizer](log-summarizer/README.md): a small, runnable command-line tool that reads logs and asks a model to summarize them. Works with a local model or a hosted API. No packages to install.
- [Kyverno policy: require a team label](kyverno-require-team-label/README.md): a real, testable policy you can validate offline with the Kyverno CLI. Shows the kind of policy AI can draft and how a policy gates AI-proposed changes.
- [Prompt injection walkthrough](prompt-injection-walkthrough.md): a concrete attack and the design that prevents it. Read this before you let AI act.
- [AI pull request review with GitHub Actions](ai-pr-review-github-action.md): a workflow that asks an AI to comment on a pull request. It only comments. It never merges or changes code.
- [k8sgpt quickstart](k8sgpt-quickstart.md): use an open-source tool to scan a Kubernetes cluster and explain problems in plain language.

## Want to add one?

Good examples are welcome. Keep them small, keep them safe, and explain what they do and where the human stays in control. See the main CONTRIBUTING guide.
