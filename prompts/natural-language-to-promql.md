# Write a PromQL query from plain language

Use this when you know what you want to measure but do not want to hand-write the query.

Trust level: Assist. Always check the query before you run it or put it on a dashboard.

## Prompt

```
You are a Prometheus and PromQL expert helping a DevOps engineer.

I want to measure:
<describe what you want, for example: the 95th percentile request latency for the checkout service over the last 5 minutes>

Some of my metric names and labels:
<paste a few relevant metric names and labels, or say you are not sure>

Do the following:
1. Write the PromQL query.
2. Explain in plain words what each part of the query does.
3. Note any assumptions you made about metric or label names.
4. Warn me about common mistakes for this kind of query, such as rate windows or label matching.

Keep the query simple and readable.
```

## Tips

- Give the model a few of your real metric names. It guesses labels otherwise.
- Run the query in Prometheus or Grafana and check the result makes sense before trusting it.
- Ask it to explain the difference between `rate`, `irate`, and `increase` if you are unsure which to use.
