# Review a pull request

Use this to get a second pair of eyes on a change before a human review.

Trust level: Assist. The AI gives a first pass. A human still reviews and approves.

## Prompt

```
You are a careful senior engineer reviewing a pull request for infrastructure code.

Here is the diff:
<paste the diff>

Here is the context:
<what the change is meant to do, and which systems it touches>

Do the following:
1. Summarize what the change does in a few sentences.
2. Rate the risk of this change and explain why.
3. List anything that looks wrong, unsafe, or easy to break, most important first.
4. Point out anything missing, such as tests, docs, or a rollback plan.
5. Ask any questions you would ask the author.

Be direct and specific. Point to the exact lines. Do not approve or merge anything.
```

## Tips

- This is a first pass, not a replacement for human review.
- It is most useful for large diffs where you want a quick map before you read closely.
- For infrastructure changes, ask it to focus on blast radius and rollback.
