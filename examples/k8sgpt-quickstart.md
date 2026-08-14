# k8sgpt quickstart

k8sgpt is an open-source tool that scans a Kubernetes cluster, finds problems, and explains them in plain language. It is a good first taste of AI in ops, because it is read-only by default. It looks and explains. It does not change your cluster.

Trust level: Assist. It reports problems. You decide what to fix.

## What it does

k8sgpt looks at your cluster for common problems, such as pods that will not start, failing probes, or misconfigured resources. It then uses an AI model to explain each problem in words a human can act on, often with a suggested fix.

## Try it

You need access to a cluster (a local one like kind or minikube is fine) and the k8sgpt tool installed. Check the project's own docs for install steps, since they change over time.

A typical first run looks like this:

```
# Point k8sgpt at a model provider (follow the tool's auth docs)
k8sgpt auth add

# Scan the cluster and explain what is wrong
k8sgpt analyze --explain
```

You get a list of problems, each with a plain-language explanation.

## A safe way to learn with it

1. Break something on purpose in a test cluster. For example, set a pod image to a name that does not exist.
2. Run the scan and read how the tool explains the problem.
3. Compare its explanation to what you already know is wrong.
4. This builds your sense of when the tool is helpful and when it is off.

## Where the human stays in control

k8sgpt tells you what looks wrong and suggests fixes. You decide what to change and you make the change yourself, ideally through your normal GitOps flow. Do not wire a tool like this to change the cluster on its own while you are still learning to trust it.

## Learn more

See the k8sgpt project on GitHub for install steps, supported model providers, and current features.
