# Praktikum Terstruktur — Evaluasi anomali pada angka energi

**Status:** tugas **direncanakan**; implementasi Week 03–12 belum dijalankan. Semua input, site, meter dan timeseries adalah sintetis.

## Problem dan konteks profesional

Kita memerlukan algoritma yang menandai interval konsumsi tidak biasa, bukan classifier kata dari Week 01. Dataset sintetis menyisipkan spike dengan label ground truth yang jelas.

**Single source of truth:** [kontrak domain](../../docs/architecture/energy-data-contract.md) · [threat model](../../docs/architecture/threat-model.md). Jangan mencampur kontrak klasifikasi log teks Week 01 dengan data anomaly scoring numerik Week 11–12.

## Langkah yang akan diimplementasikan saat sesi praktik

1. Generate seri 15-menit per meter dengan pola harian/mingguan dan seed; sisipkan spike serta missing data secara terkontrol dan dokumentasikan generator.

2. Split train→validation→test **kronologis**, fit scaler/rolling baseline hanya dengan masa lalu, threshold dipilih di validation.

3. Bandingkan baseline robust median/IQR dan kandidat ML numerik (mis. Isolation Forest) yang sesuai data.

4. Jelaskan raw IsolationForest decision_function bukan probability; normalisasi anomaly_score ke [0,1] hanya lewat transform yang didokumentasikan.

5. Hitung precision/recall/F1 hanya terhadap label injeksi sintetis; ukur juga alert volume, false-alert rate dan per-meter effect.

6. Catat model card: intended use, data schema, seed, split, metrics, limitations, fairness/coverage, data drift, artifact provenance.

## Acceptance criteria (belum dicentang)

- [ ] Tidak ada leakage dari masa depan atau held-out test saat threshold fitting.
- [ ] Model mengevaluasi numeric readings, bukan event_note teks.
- [ ] Metrik berlabel sintetis tidak dipromosikan sebagai validasi kerusakan listrik nyata.
- [ ] Missing intervals diperlakukan sebagai kualitas data, bukan nol.

## Evidence yang harus dibuat

Generator numeric series, evaluation scripts, confusion report, model card, split manifest.

Saat praktik: catat input sintetis, expected behavior, actual output, command+versi runtime, error/negative tests, keamanan, dan link commit. Jangan mengarang skor model, latency, atau status passed.

## Pertanyaan transfer

Apa alasan menggunakan time-split dibanding random split untuk data meter berurutan?

**Definition of done:** seluruh acceptance criteria diverifikasi dengan artefak sendiri, bukan sekadar dokumentasi ini; status BNSP tetap memerlukan asesmen resmi LSP.

[Latihan](exercises.md) · [Knowledge check](knowledge-check.md) · [Evidence matrix](../../certification/evidence-matrix.md)
