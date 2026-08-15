# Topic 2: Everyday ops

This is where almost everyone should start using AI at work. The tasks here are low risk because you review everything before it runs. The AI drafts and explains. You decide and apply.

Trust level: Assist.

## Where AI helps every day

### Writing and cleaning up config

- Draft Terraform, Helm charts, Kustomize, and Kubernetes manifests from a description.
- Refactor a messy config into something readable.
- Convert between formats, for example a plain list of requirements into a values file.

Always read the result and test it in a safe environment before you apply it. The model can produce config that looks right and is subtly wrong.

### Drafting policies

Turn a rule you want into a first draft of a policy for Kyverno, OPA, or conftest. Describe the rule in plain words and let the model write the YAML, then test it in audit mode before you enforce it. See the [Kyverno prompt](../../prompts/write-a-kyverno-policy.md).

### Explaining errors and unfamiliar output

Paste a stack trace, a cryptic error, or a chunk of output you do not recognize, and ask for a plain-language explanation and likely causes. This turns a 20-minute search into a 20-second read, as long as you confirm what it tells you.

### Writing docs and runbooks

- Draft a runbook from a description of a task.
- Turn rough notes into clear documentation.
- Improve a page that is hard to read.

Docs are a great first use because the risk is low and the time saved is real.

### Pull requests and commits

- Summarize what a pull request does. See the [PR review prompt](../../prompts/review-a-pull-request.md).
- Draft a clear commit message from a diff.
- Draft a changelog entry.

### ChatOps, read-only

A chat assistant that answers questions about your systems is useful and safe when it can only read. For example, "which services are on version 1.4" or "show the recent deploys for checkout". Keep it read-only at this stage.

## The one rule that matters here

Never paste secrets, tokens, or customer data into a hosted model. Redact first, or use a model that runs locally. This one habit prevents the most common and most serious mistake.

## How to build the habit

Pick one task from this page that you do often. Use AI for it every time for a week. Compare the result to what you would have done. You will quickly learn where it helps and where it does not, with no risk to production.

## Related prompts

- [Turn noisy logs into a summary](../../prompts/logs-to-summary.md)
- [Draft a Kyverno policy](../../prompts/write-a-kyverno-policy.md)
- [Review a pull request](../../prompts/review-a-pull-request.md)

## Next

Go to [topic 3: monitoring](../03-monitoring/README.md), or back to [all topics](../README.md).
