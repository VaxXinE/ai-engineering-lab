# Capstone — AI Customer Intelligence Platform

**Status:** specification only. Application code, runtime dependencies, tests and deployment are **not implemented yet**.

## Problem

Incoming synthetic customer inquiries need to be validated, stored, classified into support/sales/general categories and reviewed by an authorized human operator.

## Personas

- **Agent:** reviews classified inquiries and corrects labels.
- **Supervisor:** sees quality trends and audit history.
- **Developer / operator:** deploys, monitors and maintains the service.

## Functional scope (planned)

1. Ingest synthetic CSV or API input with a repeatable pipeline.
2. Validate types, completeness, duplicate identifiers and length.
3. Store customers, inquiries, predictions, model versions, and reviews.
4. Provide role- and object-authorized REST endpoints.
5. Display responsive dashboard and accessible empty/loading/error states.
6. Classify inquiry text with a baseline model, storing confidence and review state.
7. Allow manual override and capture reasons in an audit trail.
8. Return controlled errors and degrade gracefully if inference fails.
9. Provide tests, logging, backup/restore exercises and installation instructions.

## Nonfunctional scope

- **Privacy:** synthetic data only; minimize stored text and redact sensitive logs.
- **Security:** authentication, server-side authorization, input constraints, rate limiting and safe model loading.
- **Reliability:** bounded timeouts, error handling and non-destructive retries.
- **Maintainability:** modular design, documented API contracts, migration strategy, tests.
- **Evaluation:** accuracy is insufficient alone; measure per-class precision, recall, F1 and review errors.

## Proposed architecture

```text
Browser (Next.js / TypeScript)
  -> API (FastAPI)
     -> PostgreSQL (data, reviews, audit trail)
     -> AI inference module (validated model artifact)
     -> observability (structured logs / metrics)
```

**Technology selection remains open** until the Week 02 assessment. See [requirements](docs/requirements.md) and [architecture](docs/architecture.md).

## Delivery gates

- **Week 04:** ingestion and validation proof.
- **Week 10:** documented UI, backend, database and architecture.
- **Week 13:** AI integration and reproducible installation.
- **Week 15:** operational monitoring and recovery evidence.
- **Week 16:** demonstration and traceable certification portfolio.

Do not claim the gates passed without evidence.
