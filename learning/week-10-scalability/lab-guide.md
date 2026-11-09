# Hands-on — Scalability, Performance & Reliability

**Status:** panduan siap; langkah belum dieksekusi. Implementasi, metrik, dan bukti ditulis setelah praktikum.

## Target

Mengukur bottleneck frontend/backend/DB/inference dan merancang scaling serta failure protection berdasarkan data.

## Skenario

Traffic naik dari 5 menjadi 100 pesan/detik pada jam ramai. Inference eksternal punya rate limit dan lonjakan P95. Evaluasi queue dan fallback manual dibanding menaikkan CPU secara membabi buta.

## Langkah implementasi

1. Rancang scenario baseline 1, 10, 50 concurrent clients pada dataset sintetis.

2. Pilih metrik requests/sec, P50, P95, P99, 5xx, retry count, inference latency dan DB query latency.

3. Bangun sederhana reproducible load test script; tetapkan timeouts dan pembatas agar tidak membebani sistem pihak lain.

4. Catat hasil sebenarnya, buat grafik tabel per skenario dan cari bottleneck dominan.

5. Simulasikan model outage/slowdown dengan test double lokal (bukan stress-test API provider tanpa izin).

6. Tulis capacity recommendations dan cost estimate dengan asumsi eksplisit.

## Acceptance criteria

- [ ] Setiap hasil uji mencantumkan alat, mesin, durasi, concurrency, dan ukuran data.
- [ ] Rekomendasi perubahan diturunkan dari bottleneck yang diobservasi.
- [ ] Sistem menghindari retry tak berbatas dan uncontrolled external API consumption.
- [ ] Terdapat error case dan timeout scenario dalam pengujian.

## Rencana verifikasi

1. Buat skenario bukti untuk: Setiap hasil uji mencantumkan alat, mesin, durasi, concurrency, dan ukuran data.
2. Buat skenario bukti untuk: Rekomendasi perubahan diturunkan dari bottleneck yang diobservasi.
3. Buat skenario bukti untuk: Sistem menghindari retry tak berbatas dan uncontrolled external API consumption.
4. Buat skenario bukti untuk: Terdapat error case dan timeout scenario dalam pengujian.

## Dokumentasi hasil

- Catat perintah, dependency/runtime, input sintetis, output aktual, dan edge case yang diuji.
- Catat source code atau desain beserta commit/PR.
- Tuliskan threat dan asumsi tersisa. Jangan menyatakan 'passed' sebelum menjalankan test.
- Kaitkan hasil dengan [evidence matrix](../../certification/evidence-matrix.md).

[Latihan](exercises.md) · [Simulasi](assessment.md)