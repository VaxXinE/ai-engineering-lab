# Teori — Arsitektur AI Smart Energy Monitoring (Week 09)

**Outcome:** merancang API, domain service, inference adapter dan storage yang mempertahankan data meter saat model gagal, dengan trust boundaries jelas.

## 1. Modular monolith first

Untuk capstone, frontend Next.js + backend FastAPI + PostgreSQL bisa menjadi modular monolith yang mudah diuji. Backend memisahkan import/validation, site authorization, readings service, scoring adapter, review/audit, dan metrics. Microservices baru dipertimbangkan jika isolation, ownership dan independent scaling dibuktikan, bukan karena AI harus microservices.

## 2. API boundaries yang konsisten

Gunakan route acuan: `POST /api/v1/import-batches`, `GET /api/v1/sites/{site_id}/meters/{meter_id}/readings`, `GET /api/v1/sites/{site_id}/anomaly-events`, dan endpoint review. Field `site_id` harus berasal dari resource dan dikonfirmasi authorized membership, bukan dari output model. Kode HTTP 400/401/403/404/409/422/429/5xx dipilih sesuai failure semantics dan security posture.

## 3. Adapter bukan domain logic

Antarmuka `score(features)->AnomalyResult` menerima fitur numerik valid (kWh interval, history, time features), menghasilkan finite `anomaly_score` [0,1], `flagged`, `model_version` dan alasan. Raw IsolationForest score tidak otomatis [0,1]; adapter bertanggung jawab mapping yang terdokumentasi. Text classifier Week 01 menggunakan interface berbeda.

## 4. Failure containment

Persistence membaca/import meter harus terpisah dari scoring. Ketika inference timeout, pembacaan valid tetap tersimpan dan ditampilkan, status `scoring_unavailable` / pending manual review; jangan memalsukan label normal atau menghapus sumber. Retry dibatasi dan idempotent. Pilihan synchronous vs queue perlu dilandaskan ke latency dan kualitas UX yang diukur.

## 5. Trust boundaries

CSV untrusted → validation/size limits. Browser untrusted → auth/session/object scope. AI output untrusted → strict output schema. DB → parameterized SQL, FK, atomic audit. Metrics → redaction. Model artifacts → provenance dan deserialization safety. Tidak ada actuator elektrik, billing atau keputusan safety otomatis.

## 6. Arsitektur sebagai bukti

C4 component diagram + sequence diagram untuk success dan timeout; ADR memilih modular monolith; API contract dengan success/errors. Bedakan planned vs implemented. Negative tests harus menguji cross-site IDOR, invalid score dan data retention ketika outage.

[Canonical contract](../../docs/architecture/energy-data-contract.md) · [Threat model](../../docs/architecture/threat-model.md) · [Lab](lab-guide.md).

Referensi: [C4](https://c4model.com/), [FastAPI](https://fastapi.tiangolo.com/), [OWASP API security](https://owasp.org/www-project-api-security/).
