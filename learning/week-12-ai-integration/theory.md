# Teori — Numerical Anomaly Scoring Integration (Week 12)

**Outcome:** menghubungkan hasil scoring numerik ke API/dashboard dengan output validation, idempotency dan human review; tidak kehilangan data ketika dependency AI gagal.

## 1. Scoring versus text classification

Model numerik menerima `energy_kwh`, metadata meter/time yang valid, dan historical features. Kontrak output: finite `anomaly_score` [0,1] **setelah mapping yang didokumentasikan**, `flagged: bool`, `model_version`, `reason_codes`. Model classification `normal/warning/fault/abstain` Week 01 berbeda dan tidak menjadi schema endpoint numeric.

## 2. Data lifecycle

Import → validate → persist `MeterReading` → score → add append-only `AnomalyEvent` → human review. Status `pending_scoring/scored/scoring_unavailable/needs_review/reviewed` adalah state aplikasi, bukan class ML. Kegagalan inference tidak menghapus reading dan tidak boleh otomatis dipetakan menjadi 'normal'.

## 3. Ports/adapters

Backend memanggil interface `score(features)->AnomalyResult`. Adapter memegang detail library/provider, timeouts, retry policy, model provenance, dan normalisasi skor. Input/output model tidak mengandung keputusan site permission, sehingga server tetap mengotorisasi setiap resource.

## 4. Output verification

Tolak `NaN`, `inf`, nilai negatif atau lebih dari 1, versi kosong, unknown reason codes dan payload tak terduga. `HTTP 200` dari model tidak menjamin hasil valid. Jika score invalid, simpan failure state untuk review dan log error secara redacted.

## 5. Reliability dan security

Gunakan rate/size limits, deadlines, bounded idempotent retries, fake adapters untuk tests success/timeout/malformed/unauthorized. Review endpoint memverifikasi site membership dan optimistic locking. Tidak ada actuator/pemadaman/perintah fisik dari anomaly score.

## 6. Verification

Unit: adapter parser dan score mapping; integration: persistence saat timeout, audit, valid review; E2E: UI displays missing vs scored; security: cross-site IDOR dan malicious input. Keberhasilan kode baru boleh dicatat setelah test benar-benar dijalankan.

[Canonical contract](../../docs/architecture/energy-data-contract.md) · [Worked example](worked-examples.md) · [Lab](lab-guide.md).

Referensi: [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/), [FastAPI errors](https://fastapi.tiangolo.com/tutorial/handling-errors/), [OWASP GenAI](https://genai.owasp.org/llm-top-10/).
