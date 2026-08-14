# Draft a Kyverno policy

Use this to turn a rule you want into a first draft of a Kyverno policy.

Trust level: Gate. The AI drafts. You test it and review it before it guards a cluster.

## Prompt

```
You are a Kubernetes policy expert who writes Kyverno policies.

I want a policy that does this:
<describe the rule, for example: block any pod that runs as root, or require a team label on all deployments>

Do the following:
1. Write the Kyverno policy as YAML.
2. Explain what each part does in plain words.
3. Say whether it should be an audit or an enforce policy, and why.
4. Give one example that the policy should block and one it should allow.
5. Note any edge cases where this policy might be too strict or too loose.
```

## Tips

- Test the policy in audit mode first. See what it would block before you enforce it.
- Run it against real manifests with the Kyverno CLI before you apply it.
- The same prompt works for OPA or conftest. Just change the tool name and language.
