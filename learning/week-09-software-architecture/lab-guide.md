# Praktikum Terstruktur — API dan scorer yang terpisah

**Status:** tugas **direncanakan**; implementasi Week 03–12 belum dijalankan. Semua input, site, meter dan timeseries adalah sintetis.

## Problem dan konteks profesional

Kegagalan numerical anomaly model tidak boleh menghapus pembacaan meter valid atau memicu perintah pada instalasi listrik.

**Single source of truth:** [kontrak domain](../../docs/architecture/energy-data-contract.md) · [threat model](../../docs/architecture/threat-model.md). Jangan mencampur kontrak klasifikasi log teks Week 01 dengan data anomaly scoring numerik Week 11–12.

## Langkah yang akan diimplementasikan saat sesi praktik

1. Gunakan [canonical routes](../../docs/architecture/energy-data-contract.md) alih-alih endpoint dengan spasi: POST /api/v1/import-batches; GET /api/v1/sites/{site_id}/meters/{meter_id}/readings.

2. Rancang komponen ingestion, validation, storage, anomaly scoring port, model adapter, review service dan observability.

3. Definisikan `score(features)->AnomalyResult` dengan output finite normalized score, flagged, reason codes, model_version; status aplikasi terpisah.

4. Gambar sequence diagram: persist reading→async score→review; fault injection timeout→scoring_unavailable tanpa data loss.

5. Petakan trust boundaries browser/API, CSV importer, model outputs, DB, logs; site authorization di setiap read/review endpoint.

6. Tulis ADR modular monolith vs split-service serta reasoned scaling trigger.

## Acceptance criteria (belum dicentang)

- [ ] API methods/path valid dan scope otorisasi jelas.
- [ ] Model output tidak boleh memutuskan site permissions.
- [ ] Gagal scoring tidak menghapus accepted readings.
- [ ] Kontrak adapter berbeda dari Week 01 text classifier.

## Evidence yang harus dibuat

C4 component diagram, sequence success/error, API schema draft, threat model, ADR.

Saat praktik: catat input sintetis, expected behavior, actual output, command+versi runtime, error/negative tests, keamanan, dan link commit. Jangan mengarang skor model, latency, atau status passed.

## Pertanyaan transfer

Bagaimana mencegah user yang login Site-A meminta reading ID milik Site-B?

**Definition of done:** seluruh acceptance criteria diverifikasi dengan artefak sendiri, bukan sekadar dokumentasi ini; status BNSP tetap memerlukan asesmen resmi LSP.

[Latihan](exercises.md) · [Knowledge check](knowledge-check.md) · [Evidence matrix](../../certification/evidence-matrix.md)
