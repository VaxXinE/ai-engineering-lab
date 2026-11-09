# AI Engineering Lab

A hands-on learning and portfolio repository for **AI Application Engineering** and **AI Data Processing**, aligned with the competency areas of two Indonesian BNSP schemes.

> Status: learning setup. This is a **self-study project**, not an official BNSP course, certificate or LSP endorsement. Always verify the latest scheme document and assessment requirements with the relevant licensed LSP.

## Goals

- Build a reliable data-ingestion and validation pipeline.
- Design and implement a full-stack application integrating AI inference.
- Evaluate model performance, software architecture, security, scalability and user experience.
- Practice installation, monitoring, maintenance, backup and recovery.
- Collect evidence for two separate BNSP assessments without duplicating overlapping work.

## Sixteen-week roadmap

| Phase | Weeks | Topics |
| --- | --- | --- |
| Foundation | 01–02 | AI fundamentals; tools and framework evaluation |
| Data processing | 03–04 | Data ingestion; data validation |
| Software engineering | 05–10 | Data structures, UX, UI, database, architecture, scalability |
| AI integration & operations | 11–15 | Model evaluation, integration, installation, maintenance |
| Certification preparation | 16 | Evidence mapping, demonstration and mock assessment |

**Start here:** [Complete materials index (16 modules)](docs/materials-index.md) · [Learning roadmap](docs/learning-roadmap.md) · [Progress tracker](docs/progress-tracker.md) · [Week 01 example](learning/week-01-ai-fundamentals/README.md)

## Capstone: AI Customer Intelligence Platform

One progressive project processes **synthetic** customer inquiries from ingestion to classification, human review and operational monitoring.

Proposed stack (not a BNSP requirement): **Next.js / React + TypeScript**, **Python + FastAPI**, **PostgreSQL**, **pandas / Pydantic / scikit-learn**, **Docker Compose**, and automated tests.

See [capstone requirements](projects/ai-customer-intelligence/README.md).

## Repository layout

```text
learning/                               Weekly lessons and exercises
projects/ai-customer-intelligence/      Capstone specification and future code
datasets/synthetic/                     Synthetic-only data policy
docs/learning-roadmap.md                16-week curriculum
docs/progress-tracker.md                Track each deliverable
docs/templates/                         Lesson and ADR templates
certification/ai-data-processing/       Data processing competency reference
certification/ai-software-application/  AI application competency reference
certification/evidence-matrix.md        Traceable assessment evidence
```

## Week 01 hands-on demo

Modul pertama sudah menyediakan **synthetic text classifier** menggunakan Multinomial Naive Bayes, rule-based baseline, evaluasi metrik, 23 unit tests, dan panduan belajar. Kode telah diverifikasi lokal, tetapi **hasil belajar peserta dan workflow CI belum otomatis dinyatakan lulus**.

~~~bash
cd learning/week-01-ai-fundamentals
python -m week01 evaluate
python -m week01 predict --text "saya ingin membeli paket langganan"
python -m unittest discover -s tests -v
~~~

Baca [materi Week 01](learning/week-01-ai-fundamentals/README.md) dan [hasil verifikasi](learning/week-01-ai-fundamentals/results/verification.md).

## Curriculum completion status

**All educational materials for Weeks 01–16 are authored**: each module has a theory lesson, a hands-on guide, exercises, and mock assessment. **Only Week 01 has implemented lab code and verified tests.** Weeks 02–16 are intentionally *learning-ready, not implementation-complete*, and learner progress is not marked passed. See [materials index](docs/materials-index.md) and [assessment readiness](docs/assessment-readiness.md).

Published LSP listing: 12 software application + 6 data processing units with 4 overlapping; BNSP currently lists 13 application units. [Regulation/sources and verification caveat](docs/references.md).

## Working agreement

1. Work in a dedicated branch: `learning/week-01-ai-fundamentals` or `feat/<feature>`.
2. For each module, record goals, key concepts, implementation, test evidence, and a retrospective.
3. Keep `main` usable; use pull requests to review changes.
4. Follow [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
5. Never commit secrets, real customer data, proprietary code, or private assessment records.

## Certification references

- [LSP Artificial Intelligence Indonesia: Penerapan AI untuk Aplikasi Perangkat Lunak](https://lspartificialintelligence.id/penerapan-ai-untuk-aplikasi-perangkat-lunak/)
- [BNSP](https://bnsp.go.id/)
- [Kemnaker SKKNI directory](https://jdih.kemnaker.go.id/)

**Scheme versions may change.** A previous LSP list showed 12 application units, whereas BNSP records may differ. Refer to the current official scheme and related SKKNI when preparing the final mapping.

## License

Original materials in this repository are MIT-licensed (see [LICENSE](LICENSE)). Third-party code, datasets and models retain their respective licenses.
