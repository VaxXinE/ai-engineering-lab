# Praktikum Terstruktur — Time-series query, ingestion rate dan inference latency

**Status:** tugas **direncanakan**; implementasi Week 03–12 belum dijalankan. Semua input, site, meter dan timeseries adalah sintetis.

## Problem dan konteks profesional

Jumlah meter bertambah dari 10 menjadi 1000, interval 15 menit, dan permintaan grafik periode 30 hari meningkat.

**Single source of truth:** [kontrak domain](../../docs/architecture/energy-data-contract.md) · [threat model](../../docs/architecture/threat-model.md). Jangan mencampur kontrak klasifikasi log teks Week 01 dengan data anomaly scoring numerik Week 11–12.

## Langkah yang akan diimplementasikan saat sesi praktik

1. Hitung volume harian: satu meter menghasilkan 96 readings/hari; 1000 meter menghasilkan 96.000 readings/hari tanpa gap.

2. Rancang query terbatasi site_id, meter_id, start/end UTC dan pagination/aggregation; index komposit sesuai EXPLAIN.

3. Tentukan metrik insert throughput, query P50/P95, scoring latency, memory, CPU, error rate, dan queue depth.

4. Uji secara lokal load 10/100/1000 meter sintetis; simpan command, hardware, sample size, versions dan hasil aktual.

5. Atur bounded queue, timeouts, backpressure dan idempotent retry; hindari langsung load-test provider eksternal tanpa izin.

6. Rancang retention/downsampling dengan menjaga arti per-interval kWh dan data gaps.

## Acceptance criteria (belum dicentang)

- [ ] Perhitungan jumlah readings/hari benar.
- [ ] Benchmark terukur dan reproducible tanpa angka karangan.
- [ ] Tidak ada cross-site cache leakage.
- [ ] Retry dan queue memiliki batas yang jelas.

## Evidence yang harus dibuat

Capacity worksheet, SQL EXPLAIN, load tests, p95 report, scaling ADR.

Saat praktik: catat input sintetis, expected behavior, actual output, command+versi runtime, error/negative tests, keamanan, dan link commit. Jangan mengarang skor model, latency, atau status passed.

## Pertanyaan transfer

Kenapa membaca seluruh readings mentah untuk grafik satu tahun bisa buruk untuk UX maupun DB?

**Definition of done:** seluruh acceptance criteria diverifikasi dengan artefak sendiri, bukan sekadar dokumentasi ini; status BNSP tetap memerlukan asesmen resmi LSP.

[Latihan](exercises.md) · [Knowledge check](knowledge-check.md) · [Evidence matrix](../../certification/evidence-matrix.md)
