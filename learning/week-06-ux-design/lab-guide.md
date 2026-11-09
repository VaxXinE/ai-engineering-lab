# Praktikum Terstruktur — UX analis energi dan review kandidat anomali

**Status:** tugas **direncanakan**; implementasi Week 03–12 belum dijalankan. Semua input, site, meter dan timeseries adalah sintetis.

## Problem dan konteks profesional

Pada 00:30 meter MTR-001 mencatat 5.90 kWh, jauh lebih tinggi dari dua interval sebelumnya, tetapi belum ada bukti kerusakan. Operator perlu konteks dan jalur review.

**Single source of truth:** [kontrak domain](../../docs/architecture/energy-data-contract.md) · [threat model](../../docs/architecture/threat-model.md). Jangan mencampur kontrak klasifikasi log teks Week 01 dengan data anomaly scoring numerik Week 11–12.

## Langkah yang akan diimplementasikan saat sesi praktik

1. Petakan persona energy analyst/operator dan tugas: melihat tren, memilih site/meter, membaca kandidat anomali, memeriksa data quality, membuat keputusan review.

2. Gambar empat layar: Overview Energy, Meter Detail Chart, Anomaly Review Queue, dan Review History; bukan inbox pesan.

3. Pada chart, visualisasikan data kWh per 15 menit; tooltips berisi satuan, rentang waktu, source quality, dan versi model.

4. Bedakan status missing interval (gap) dari 0 kWh; bedakan anomaly candidate dari confirmed anomaly.

5. Rancang review decisions confirmed_anomaly/expected_variation/needs_investigation dan display audit append-only.

6. Uji task flow menggunakan keyboard; desain state loading, empty, scoring_unavailable, conflict/403 dan error retry tanpa hilang draft.

## Acceptance criteria (belum dicentang)

- [ ] Analis dapat menemukan meter dan anomali tanpa salah membaca satuan.
- [ ] Prediksi model tidak diperlakukan sebagai fakta listrik atau instruksi pengendalian.
- [ ] Missing slot dan zero-value jelas berbeda.
- [ ] UI dapat dipakai tanpa mouse untuk task inti.

## Evidence yang harus dibuat

Persona, user journey, wireframes, task-based UX checklist, accessibility review.

Saat praktik: catat input sintetis, expected behavior, actual output, command+versi runtime, error/negative tests, keamanan, dan link commit. Jangan mengarang skor model, latency, atau status passed.

## Pertanyaan transfer

Kenapa status kandidat anomali tidak boleh langsung ditampilkan sebagai 'meter rusak'?

**Definition of done:** seluruh acceptance criteria diverifikasi dengan artefak sendiri, bukan sekadar dokumentasi ini; status BNSP tetap memerlukan asesmen resmi LSP.

[Latihan](exercises.md) · [Knowledge check](knowledge-check.md) · [Evidence matrix](../../certification/evidence-matrix.md)
