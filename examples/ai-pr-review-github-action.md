# AI pull request review with GitHub Actions

This example shows a safe way to add an AI review step to your pull requests. The workflow reads the diff, asks an AI for a plain-language summary and risk notes, and posts them as a comment. That is all it does. It does not approve, merge, or change any code. A human still reviews as normal.

Trust level: Assist. The AI gives a first pass. People still review and merge.

## How it works

1. When a pull request opens or updates, the workflow runs.
2. It collects the diff.
3. It sends the diff to an AI model with a review prompt.
4. It posts the model's response as a comment on the pull request.

The AI has no power to change anything. Its only output is a comment.

## The workflow

Save this as `.github/workflows/ai-review.yml` in your own repository. Read it fully and adjust it before use. You need to add your model provider's key as a repository secret named `AI_API_KEY` (Settings, then Secrets and variables, then Actions). The model call is included below and uses an OpenAI-compatible API with the Python that is already on the runner. To use a different provider, change the URL and model.

```yaml
name: AI PR review

on:
  pull_request:
    types: [opened, synchronize]

permissions:
  pull-requests: write   # only to post a comment
  contents: read         # only to read the diff

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - name: Check out the code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Get the diff
        id: diff
        run: |
          git diff origin/${{ github.base_ref }}...HEAD > pr.diff
          echo "created diff"

      - name: Ask the AI for a review
        env:
          AI_API_KEY: ${{ secrets.AI_API_KEY }}
          AI_MODEL: gpt-4o-mini
        run: |
          python3 - <<'PY'
          import json, os, urllib.request
          diff = open("pr.diff", encoding="utf-8").read()[:12000]  # keep the request small
          prompt = (
              "You are a careful senior engineer reviewing a pull request for "
              "infrastructure code.\n\nHere is the diff:\n" + diff + "\n\n"
              "Summarize what it does, rate the risk, list anything unsafe or "
              "missing, and ask any questions. Point to exact lines. Do not "
              "approve or merge."
          )
          body = json.dumps({
              "model": os.environ.get("AI_MODEL", "gpt-4o-mini"),
              "messages": [{"role": "user", "content": prompt}],
          }).encode()
          req = urllib.request.Request(
              "https://api.openai.com/v1/chat/completions",
              data=body,
              headers={
                  "Content-Type": "application/json",
                  "Authorization": "Bearer " + os.environ["AI_API_KEY"],
              },
          )
          with urllib.request.urlopen(req) as r:
              data = json.load(r)
          open("review.md", "w", encoding="utf-8").write(data["choices"][0]["message"]["content"])
          PY

      - name: Post the review as a comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const body = fs.readFileSync('review.md', 'utf8');
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: `AI review (first pass, a human still reviews):\n\n${body}`,
            });
```

## The review prompt

Use the [review a pull request](../prompts/review-a-pull-request.md) prompt in the AI step.

## Things to keep in mind

- Keep the permissions small. This workflow only needs to read the diff and write a comment.
- Do not let a workflow like this approve or merge. Keep the human review step.
- Be careful with secrets. The diff is sent to your model provider, so do not run this on repositories that contain secrets in the diff.
- Cost adds up. Large diffs cost more. You can skip the review for tiny changes.
