# Further reading

A short, hand-picked list of resources to go deeper. These are chosen for being clear and practical, not for hype. Each link was checked at the time of writing. Links move, so if you find a dead one, please open an issue or a pull request.

## How LLMs and AI apps work

- [Building LLM applications for production](https://huyenchip.com/2023/04/11/llm-engineering.html) by Chip Huyen. A clear look at what changes when you take LLM features to production.
- [Emerging Architectures for LLM Applications](https://a16z.com/emerging-architectures-for-llm-applications/) by a16z. A reference architecture for LLM apps, including RAG and tool use.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) (Lewis et al., 2020). The paper that introduced RAG.
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) (Wei et al., 2022). Why asking a model to show its reasoning improves results.
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (Yao et al., 2022). A foundation for how agents reason and use tools.

## Prompting

- [Anthropic prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview). Practical patterns for writing prompts that work.

## Connecting tools to models

- [Model Context Protocol](https://modelcontextprotocol.io). A common way to expose tools and data to models. Start with read-only tools.

## Security and governance

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). The common security risks for AI apps, including prompt injection.
- [Simon Willison on prompt injection](https://simonwillison.net/tags/prompt-injection/). An ongoing, practical archive of how prompt injection works and why it is hard to fully solve.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). A framework for managing the risks of AI systems.

## SRE and DevOps foundations

The ops side of the house. AI sits on top of these practices, it does not replace them.

- [Google SRE books](https://sre.google/books/). Free to read online. Start with Site Reliability Engineering and the SRE Workbook.
- [DORA research](https://dora.dev/research/). Long-running, evidence-based research on what makes software delivery work well, including how AI is affecting teams.

## Observability for AI (LLMOps)

- [OpenTelemetry Semantic Conventions for GenAI](https://github.com/open-telemetry/semantic-conventions-genai). Standard ways to trace and measure AI calls, so you can watch your AI features the same way you watch services.

## Talks and conferences to browse

- [CNCF on YouTube](https://www.youtube.com/@cncf). Talks from KubeCon and CloudNativeCon, including a growing set on AI in cloud native.
- [USENIX SREcon](https://www.usenix.org/srecon). Talks from practitioners on running reliable systems.

## Suggest a resource

Know something that belongs here? Open an issue or a pull request. Add the link, say what it is in one line, and keep it practical. See the [contributing guide](../CONTRIBUTING.md).

Back to the [main roadmap](../README.md).
