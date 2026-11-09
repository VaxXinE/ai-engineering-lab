# Implementation Plan — AI Smart Energy Monitoring

**Status:** planned, bukan aplikasi yang sudah berjalan.

## Rencana struktur

```text
projects/ai-energy-intelligence/
  frontend/            # Next.js, TypeScript dashboard (akan dibuat)
  backend/             # FastAPI, database, model adapter (akan dibuat)
  tests/               # unit/integration/e2e (akan dibuat)
  ops/                 # Docker, logging, restore runbooks (akan dibuat)
  docs/                # requirements, architecture, model card, ADR
```

## Roadmap bertahap

| Minggu | Rencana implementasi | Penilaian |
| --- | --- | --- |
| 01 | Klasifikasi catatan kejadian perangkat sintetis untuk AI fundamentals | CLI, train/test, metrics, tests |
| 02 | Pilihan stack dan strategi deteksi anomali: heuristik vs ML | Decision matrix + ADR |
| 03 | Generator meter sintetis, CSV import, stable event ID | Ingestion summary + idempotency tests |
| 04 | Interval start UTC, explicit 15-minute duration, finite-range validation, data quality | Quality report + negative tests |
| 05 | Time-series grouping, dedup, aggregations, streaming | Complexity and test evidence |
| 06–07 | Dashboard penggunaan energi dan status review | UX walkthrough, accessibility, UI tests |
| 08–09 | ERD meter/site/reading/anomaly/review, API boundaries | Migrations + IDOR tests |
| 10 | Query scale, interval aggregation, inference latency | Performance tests |
| 11 | Baseline threshold vs anomaly detection ML on synthetic data | Evaluation report + model card |
| 12 | Strict anomaly API + human review + fallback | Integration & contract tests |
| 13 | Reproducible install | Smoke test + rollback plan |
| 14–15 | Monitoring, model drift, maintenance, backup/restore | Risk register + incident drill |
| 16 | Evidence mapping dua skema BNSP | Demo dan gap analysis |

## Non-negotiables

- Tidak menghubungkan meter listrik nyata atau perangkat pengendali.
- Data dan lokasi sepenuhnya sintetis; tanpa data penghuni/gedung asli.
- Keputusan keamanan dan otorisasi tidak diberikan ke AI.
- Tindakan manusia tidak boleh diotomatisasi dari alert model tanpa review.
- Validasi sumber data, hasil prediksi, permission dan batas ukuran input.
- Selalu bedakan planned, implemented, tested dan verified.
- Jangan klaim sertifikasi BNSP otomatis dari project.
