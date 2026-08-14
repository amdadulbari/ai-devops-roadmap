# Turn noisy logs into a short summary

Use this when you have a wall of log output and need to know what actually went wrong.

Trust level: Assist. The AI summarizes. You confirm before acting.

## Prompt

```
You are helping a DevOps engineer read logs.

Here are the logs:
<paste your logs here>

Do the following:
1. Summarize what happened in three sentences or fewer.
2. List the distinct errors you see, grouped by root cause, most important first.
3. For each group, give the number of times it appears and one example line.
4. Point out anything that looks like the first sign of trouble (the earliest related error).
5. Suggest what to check next. Do not suggest running any command that changes state.

If the logs are not enough to be sure, say what extra information you would need.
```

## Tips

- Paste a time window around the problem, not the whole file.
- If the logs are very large, ask for the summary first, then ask follow-up questions.
- Always open the real log lines the model points to and confirm them yourself.
