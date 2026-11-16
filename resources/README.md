# Further reading

A short, hand-picked list of resources to go deeper. These are chosen for being clear and practical, not for hype. Every link here was checked in November 2026. Links move, so if you find a dead one, please open an issue or a pull request.

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
- [The MCP specification](https://modelcontextprotocol.io/specification). Worth reading once if you are going to expose your own tools. Revisions are named by date, the current one is 2026-07-28, and pinning a revision saves you surprises.

## Security and governance

- [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/). The common security risks for AI apps. Prompt injection is still number one, and excessive agency, giving a model more power than the job needs, moved up to number three. That is this roadmap's whole argument, written as a security list.
- [OWASP Agentic AI Security Initiative](https://genai.owasp.org/initiatives/agentic-security-initiative/). The companion work on agents that use tools and act across systems, including the Top 10 for Agentic Applications and [Securing Agentic Applications](https://genai.owasp.org/resource/securing-agentic-applications-v2/). Read this one before you let an agent act, not after.
- [Simon Willison on prompt injection](https://simonwillison.net/tags/prompt-injection/). An ongoing, practical archive of how prompt injection works and why it is hard to fully solve.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). A framework for managing the risks of AI systems.

## SRE and DevOps foundations

The ops side of the house. AI sits on top of these practices, it does not replace them.

- [Google SRE books](https://sre.google/books/). Free to read online. Start with Site Reliability Engineering and the SRE Workbook.
- [DORA research](https://dora.dev/research/). Long-running, evidence-based research on what makes software delivery work well.
- [DORA on AI](https://dora.dev/ai/). Their dedicated work on AI-assisted development, including the [ROI report](https://dora.dev/ai/roi/report/). The finding worth carrying around: AI amplifies whatever your engineering foundations already are, good or bad.

## Observability for AI (LLMOps)

- [OpenTelemetry Semantic Conventions for GenAI](https://github.com/open-telemetry/semantic-conventions-genai). Standard ways to trace and measure AI calls, so you can watch your AI features the same way you watch services.

## Talks and conferences to browse

- [CNCF on YouTube](https://www.youtube.com/@cncf). Talks from KubeCon and CloudNativeCon, including a growing set on AI in cloud native.
- [USENIX SREcon](https://www.usenix.org/srecon). Talks from practitioners on running reliable systems.

## Suggest a resource

Know something that belongs here? Open an issue or a pull request. Add the link, say what it is in one line, and keep it practical. See the [contributing guide](../CONTRIBUTING.md).

Back to the [main roadmap](../README.md).
