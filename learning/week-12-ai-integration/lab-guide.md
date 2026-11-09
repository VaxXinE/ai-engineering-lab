# Panduan Hands-on — Integrasi Komponen Solusi AI

**Praktik:** belum dieksekusi. Jangan menulis angka kinerja atau status passed tanpa pengujian.

## Masalah yang dikerjakan

Aplikasi CRM menerima inquiry baru. Service memvalidasi input dan izin, menyimpan record, meminta prediksi melalui inference adapter, memvalidasi label hasil, lalu menampilkan status review. Inference dapat gagal atau memilih abstain.

## Langkah terurut

1. Definisikan Pydantic/TypeScript schema untuk InquiryCreate, PredictionResult dan ReviewAction, lengkap dengan batas field.

2. Buat adapter lokal yang memanggil model baseline dari Week 11 di backend; tandai model version pada respons.

3. Implementasikan endpoint create inquiry dan classify dengan authorization dan idempotency policy yang jelas.

4. Pastikan hasil classifier divalidasi against label enum, bukan ditulis mentah ke database.

5. Sambungkan UI: hasil normal, abstain, invalid output, timeout, dan human override harus memiliki state berbeda.

6. Jalankan unit, integration dan negative tests; catat response status, latency baseline dan failure-path evidence.

## Acceptance criteria

- [ ] Prediksi yang tersimpan selalu mempunyai model_version dan valid label.
- [ ] Data inquiry tidak hilang ketika AI gagal.
- [ ] Izin akses dites untuk resource berbeda dan tenant lain.
- [ ] UI dapat menerima hasil normal, abstain, timeout dan invalid model output.
- [ ] Ada bukti tests yang dijalankan, bukan screenshot tanpa reproduksi.

## Test & evidence protocol

1. Catat environment serta versi runtime dan tools yang benar-benar digunakan.
2. Rekam command/aksi, input sintetis, output, error path dan test results aktual.
3. Jangan menggunakan production data, kredensial atau system perusahaan.
4. Tautkan diagram, source code, logs teredaksi, commits dan evaluasi ke [evidence matrix](../../certification/evidence-matrix.md).
5. Tulis residual risk dan pekerjaan yang belum teruji sebagai catatan eksplisit.

[Latihan tambahan](exercises.md) · [Asesmen simulasi](assessment.md).