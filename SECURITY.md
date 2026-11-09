# Security Policy

## Scope and principles

This is a **public learning repository**, not a production system. Treat any future AI-integrated application as potentially security-sensitive.

- **No secrets**: Do not commit tokens, API keys, passwords, service credentials, `.env` or cloud keys.
- **No private records**: Use generated/synthetic device data only. Do not push client or employer data, device chats, unpublished business logic, or private assessment documents.
- **Least privilege**: Apply authorization at API and object level; do not rely on hidden frontend controls.
- **Validate boundaries**: Validate input types, file sizes and AI output schemas; encode UI output; use parameterized SQL.
- **AI safety**: Treat prompts, retrieval context, model output and model files as untrusted. Mitigate prompt injection, data disclosure and unbounded usage.
- **Supply chain**: Review license, provenance and dependencies before use; pin versions in lock files when implementations are introduced.
- **Observability**: Mask PII/secrets in logs; retain only necessary information.

## Reporting

Please **do not open public issues with exploitable vulnerabilities or sensitive data**. Contact the maintainer privately through the GitHub profile until a private reporting channel is configured.

## Local checks

Before pushing a feature, inspect `git diff --cached`, run relevant tests and review any added dataset and configuration file for secrets.
