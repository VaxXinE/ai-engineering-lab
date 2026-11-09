# Capstone Implementation Plan (Planned, Not Implemented)

## Tujuan

Satu aplikasi full-stack dengan **synthetic customer inquiries**, AI intent classification, review manusia, audit history, dan operational monitoring. Materi 16 minggu menjelaskan cara bertahap mencapainya. **Belum ada klaim deployment atau aplikasi production-ready**.

## Proposed future repository directories

~~~text
projects/ai-customer-intelligence/
  frontend/                 # Next.js/React/TypeScript
  backend/                  # FastAPI + domain services
  tests/                    # Integration and end-to-end tests
  ops/                      # docker compose, runbooks, monitoring
  docs/                     # Architecture, API, ERD, decisions
~~~

Dibuat hanya ketika implementasi nyata dimulai, bukan folder kosong tanpa isi. Pilihan tech stack didokumentasikan di Week 02.

## Delivery plan

| Gate | Module | Definition of done |
| --- | --- | --- |
| G1 | 03–04 | Ingestion idempotent, schema/quality tests dan reject report |
| G2 | 05–08 | Core algorithms, UX/UI, database schema, auth and object permissions |
| G3 | 09–10 | Architecture and API contracts, error handling, scalability test report |
| G4 | 11–12 | Evaluated model integrated with backend; validated output and human review |
| G5 | 13–15 | Reproducible installation, monitoring plan, incident and restore drill |
| G6 | 16 | Evidence pack, live demo, mock assessor Q&A and gap review |

## Architecture constraints

- No data from real CRM/trading customers; synthetic only.
- No model provider keys or credentials in repo.
- Do not train/tune against final held-out test set.
- Strong server-side object authorization; private data per tenant must be isolated.
- Keep AI predictions auditable with model version and human correction.
- Explicit fallback when model unavailable or uncertain.
- Security tests and recovery evidence recorded before calling any gate complete.

Related [requirements](requirements.md) and [architecture](architecture.md).
