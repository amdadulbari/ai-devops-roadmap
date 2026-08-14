# Explain an alert in plain words

Use this at 3 a.m. when an alert fires and you need to understand it fast.

Trust level: Assist. The AI explains and suggests. You decide and act.

## Prompt

```
You are helping an on-call engineer understand an alert.

Here is the alert:
<paste the alert name, description, labels, and current value>

Here is some context if I have it:
<recent deploys, related services, links to runbooks, anything useful>

Do the following:
1. Explain in plain words what this alert means and why it might fire.
2. Rate how urgent it looks and why.
3. List the most likely causes, most likely first, with the reason for each.
4. Give an ordered checklist of things to look at. Read-only checks only.
5. Note anything that would make this a false alarm.

Do not suggest changing anything in production. I will decide what to do.
```

## Tips

- Paste the alert labels. They usually name the service and severity.
- If you have a runbook, include the link so the model can point you to the right steps.
- The model may be confident and wrong. Verify each claim against the real system.
