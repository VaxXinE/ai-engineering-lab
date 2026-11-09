# Praktikum Terstruktur — Frontend trend meter + anomaly review

**Status:** tugas **direncanakan**; implementasi Week 03–12 belum dijalankan. Semua input, site, meter dan timeseries adalah sintetis.

## Problem dan konteks profesional

Build dashboard yang tetap benar ketika request filter site berubah, data terputus di interval tertentu, atau model scoring sedang unavailable.

**Single source of truth:** [kontrak domain](../../docs/architecture/energy-data-contract.md) · [threat model](../../docs/architecture/threat-model.md). Jangan mencampur kontrak klasifikasi log teks Week 01 dengan data anomaly scoring numerik Week 11–12.

## Langkah yang akan diimplementasikan saat sesi praktik

1. Definisikan TypeScript types MeterReading, AnomalyEvent, ReviewDecision dan RemoteState (loading/success/empty/error).

2. Bangun EnergyOverview dan MeterTrendChart dengan `energy_kwh` label per 15m dan timezone-aware timestamp.

3. Bangun AnomalyTable yang memisahkan anomaly_score (not calibrated probability) dari review status dan model_version.

4. Bangun ReviewForm dengan alasan, submit pending, error recovery dan optimistic concurrency pada event.

5. Simulasikan dua request filter yang resolve out of order; gunakan AbortController/request key agar response stale tidak menimpa site terbaru.

6. Uji accessibility (label, focus, keyboard, error announcements), invalid output guard, no site leakage dalam client cache.

## Acceptance criteria (belum dicentang)

- [ ] Graph gaps tidak diinterpolasi menjadi zero silently.
- [ ] Site filter tidak memperlihatkan data site lain; backend tetap wajib authZ.
- [ ] Invalid model score (NaN/inf/out-of-range) tidak ditampilkan sebagai valid.
- [ ] Review action tetap bisa diperbaiki saat API gagal.

## Evidence yang harus dibuat

React components (belum dibuat), TypeScript contracts, unit/UI tests, screenshot estados.

Saat praktik: catat input sintetis, expected behavior, actual output, command+versi runtime, error/negative tests, keamanan, dan link commit. Jangan mengarang skor model, latency, atau status passed.

## Pertanyaan transfer

Bagaimana memisahkan cache key berdasarkan authenticated site dan rentang waktu?

**Definition of done:** seluruh acceptance criteria diverifikasi dengan artefak sendiri, bukan sekadar dokumentasi ini; status BNSP tetap memerlukan asesmen resmi LSP.

[Latihan](exercises.md) · [Knowledge check](knowledge-check.md) · [Evidence matrix](../../certification/evidence-matrix.md)
