# Praktikum Terstruktur — Scoring API dan review tanpa kehilangan data

**Status:** tugas **direncanakan**; implementasi Week 03–12 belum dijalankan. Semua input, site, meter dan timeseries adalah sintetis.

## Problem dan konteks profesional

Backend menerima reading valid, tetapi model mengeluarkan NaN atau timeout. Sistem harus tetap menyimpan reading dan menandai scoring unavailable.

**Single source of truth:** [kontrak domain](../../docs/architecture/energy-data-contract.md) · [threat model](../../docs/architecture/threat-model.md). Jangan mencampur kontrak klasifikasi log teks Week 01 dengan data anomaly scoring numerik Week 11–12.

## Langkah yang akan diimplementasikan saat sesi praktik

1. Definisikan contract `AnomalyResult`: finite score [0,1], bool flagged, model_version nonempty, reason_codes dan scoring_status.

2. Implementasikan adapter `score(reading_features)` di boundary AI; model output tidak menentukan site_id, user_id atau permissions.

3. Buat ingestion→persist reading→score as a separate step, dengan status pending_scoring/scored/scoring_unavailable.

4. Tolak NaN, infinity, skor negatif atau >1 dan model_version kosong; jangan coerce skor invalid menjadi normal.

5. Wire UI human review dengan decisions confirmed_anomaly/expected_variation/needs_investigation; simpan audit history.

6. Test fake adapter (success/timeout/malformed), retry idempotent, cross-site review IDOR, resource limits dan logs redacted.

## Acceptance criteria (belum dicentang)

- [ ] Sensor readings tetap tersimpan pada timeout.
- [ ] Anomaly score harus valid/finite dan terbatas.
- [ ] Cross-site unauthorized review ditolak.
- [ ] Model tidak dapat mengaktifkan/menonaktifkan peralatan listrik.

## Evidence yang harus dibuat

Typed API adapter and contract tests, error taxonomy, mock integration trace, audit samples.

Saat praktik: catat input sintetis, expected behavior, actual output, command+versi runtime, error/negative tests, keamanan, dan link commit. Jangan mengarang skor model, latency, atau status passed.

## Pertanyaan transfer

Kenapa HTTP 200 dari model tidak cukup untuk menjamin output valid?

**Definition of done:** seluruh acceptance criteria diverifikasi dengan artefak sendiri, bukan sekadar dokumentasi ini; status BNSP tetap memerlukan asesmen resmi LSP.

[Latihan](exercises.md) · [Knowledge check](knowledge-check.md) · [Evidence matrix](../../certification/evidence-matrix.md)
