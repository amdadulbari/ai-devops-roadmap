# Triage an incident

Use this in the first few minutes of an incident to get organized.

Trust level: Gate. The AI helps you think and draft. A human runs the incident.

## Prompt

```
You are helping run an incident. Stay calm and structured.

What we know so far:
<what is broken, when it started, what users see, any alerts, any recent changes>

Do the following:
1. Write a one-line summary of the current impact.
2. Suggest a severity level and explain why.
3. List the top hypotheses for the cause, with the evidence for and against each.
4. Give an ordered list of next actions. Mark each as either "safe to check" or "changes production".
5. Draft a short status update I can post to the team channel.

For anything that changes production, remind me to get review before doing it.
```

## Tips

- Update the "what we know" section as you learn more and ask again.
- Keep the status update short and honest. Say what you know and what you are still checking.
- The model should never tell you to make a risky change without review. If it does, ignore that part.
