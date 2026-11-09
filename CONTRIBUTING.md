# Contributing and Learning Workflow

This repo prioritizes **clarity, reproducibility, security, traceable evidence, and maintainability**.

## Branches and pull requests

1. Create a branch named `learning/week-XX-topic`, `feat/short-name`, `fix/short-name`, or `docs/short-name`.
2. Keep changes focused and reviewable.
3. Document why a design was chosen and note trade-offs.
4. Run relevant tests and provide their output in the PR summary. Do not claim unexecuted tests passed.
5. Open a PR and include links to evidence in `certification/evidence-matrix.md`.

## Commit examples

- `docs: define week 01 AI use case`
- `feat: add synthetic data ingestion pipeline`
- `test: cover invalid customer message payloads`
- `fix: enforce ownership checks on prediction lookup`

## Definition of done

- [ ] Goal and acceptance criteria are documented.
- [ ] Implementation is small, readable and runnable.
- [ ] Relevant unit/integration/security tests are executed and recorded.
- [ ] Error, loading and permission states are considered as applicable.
- [ ] Documentation and evidence links are updated.
- [ ] No secrets, company code or real customer data are committed.

See [lesson template](docs/templates/module-template.md) and [evidence template](docs/templates/evidence-template.md).
