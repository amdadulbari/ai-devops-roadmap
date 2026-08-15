# Kyverno policy: require a team label (real, testable)

A working [Kyverno](https://kyverno.io) policy that requires every Deployment to have a non-empty `team` label. This is a real artifact you can test, not a sketch. It also shows the kind of policy an AI can draft for you, which you then test and own.

Trust level: Gate. A policy is a gate. It decides what is allowed, including what an AI is allowed to propose.

## Why this matters here

Two reasons this example is in an AI roadmap:

1. AI is good at drafting policies from a plain description. See the [Kyverno prompt](../../prompts/write-a-kyverno-policy.md). But a drafted policy is only useful once you test it, which is what this example teaches.
2. Policies are how you keep AI-proposed changes safe. In [topic 5](../../topics/05-cicd-and-gitops/README.md), any change an AI proposes has to pass policies like this one before it becomes a pull request. The AI passes the same gate a human does.

## Files

- `policy.yaml`: the policy. It starts in Audit mode, so it reports violations without blocking them.
- `good-deployment.yaml`: a Deployment with a `team` label. Should pass.
- `bad-deployment.yaml`: a Deployment with no `team` label. Should fail.

## Test it offline, no cluster needed

The Kyverno CLI can check a policy against resource files without a cluster. Install it from the [Kyverno docs](https://kyverno.io/docs/kyverno-cli/), then run:

```
kyverno apply policy.yaml --resource good-deployment.yaml --resource bad-deployment.yaml
```

You should see the `checkout` Deployment pass and the `reports` Deployment fail with the message "The label 'team' is required on all Deployments."

## Try it on a cluster

If you have a cluster with Kyverno installed:

```
kubectl apply -f policy.yaml
kubectl apply -f good-deployment.yaml     # applies, and passes the policy
kubectl apply -f bad-deployment.yaml      # applies, but is reported as a violation in Audit mode
```

Because the policy is in Audit mode, the bad Deployment is not blocked, only reported. Check the report:

```
kubectl get policyreport -A
```

## From Audit to Enforce

Audit mode is how you roll out a policy safely. You watch the reports, fix the workloads that violate the rule, and only then switch to Enforce, which blocks new violations. To enforce, change `validationFailureAction` in `policy.yaml` from `Audit` to `Enforce` and apply again. On Kyverno 1.11 and newer you can set `failureAction` under the rule instead.

## The pattern, in plain words

The rule matches every Deployment. The `validate.pattern` says `metadata.labels.team` must match `?*`, which means one character followed by any characters, so the label must exist and not be empty. If it does not match, the resource fails with the message shown.

Back to [examples](../README.md).
