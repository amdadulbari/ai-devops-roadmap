# Draft a blameless postmortem

Use this after an incident to get a first draft you can edit, instead of staring at a blank page.

Trust level: Assist. The AI drafts. A human owns the final document.

## Prompt

```
You are helping write a blameless postmortem. Focus on systems and process, not blame.

Here is what happened:
<timeline of events, what broke, how it was found, how it was fixed, the impact>

Write a postmortem with these sections:
1. Summary: what happened and the impact, in a few sentences.
2. Timeline: the key events with times.
3. What went well.
4. What went wrong or was harder than it should have been.
5. Root cause, as best we understand it.
6. Action items: concrete follow-ups, each with a clear owner-shaped description.

Keep the tone factual and blameless. Do not name individuals as the cause.
```

## Tips

- Give it the raw timeline from your chat, alerts, and deploy history. It shapes it into prose.
- Edit the action items to be specific and assign real owners.
- A postmortem is a human document. Use the draft as a starting point, not the final word.
