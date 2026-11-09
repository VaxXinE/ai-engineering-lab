# Panduan Hands-on — Instalasi, Konfigurasi dan Deployment AI

**Praktik:** belum dieksekusi. Jangan menulis angka kinerja atau status passed tanpa pengujian.

## Masalah yang dikerjakan

Aplikasi yang berjalan pada laptop developer perlu bisa dipasang ulang di lingkungan test tanpa hidden manual setup. Gunakan container untuk UI, API, dan database serta model artifact tervalidasi.

## Langkah terurut

1. Tetapkan versi runtime/dependency dari hasil Week 02 dan pilih image base tepercaya; tulis alasan versi.

2. Siapkan Dockerfile/Compose untuk local test, jaringan internal, volumes dan env placeholders; jangan publish DB ke internet.

3. Definisikan health endpoints; periksa status database migration dan model artifact yang di-load dari sumber tepercaya.

4. Jalankan setup pada environment bersih dengan perintah yang terdokumentasi (bukan asumsi 'works on my machine').

5. Eksekusi smoke test normal dan kondisi model artifact missing; catat status nyata.

6. Latih proses rollback versi aplikasi dan periksa integritas database setelah rollback pada test environment.

## Acceptance criteria

- [ ] Satu runbook cukup untuk instalasi pada environment bersih.
- [ ] Tidak ada credential asli, privileged container yang tidak perlu, atau secret di image.
- [ ] Health/status endpoints memberi sinyal operasional yang tepat.
- [ ] Smoke test dan rollback diuji serta hasilnya dicatat.
- [ ] Model artifact punya provenance/version/hash atau kontrol setara.

## Test & evidence protocol

1. Catat environment serta versi runtime dan tools yang benar-benar digunakan.
2. Rekam command/aksi, input sintetis, output, error path dan test results aktual.
3. Jangan menggunakan production data, kredensial atau system perusahaan.
4. Tautkan diagram, source code, logs teredaksi, commits dan evaluasi ke [evidence matrix](../../certification/evidence-matrix.md).
5. Tulis residual risk dan pekerjaan yang belum teruji sebagai catatan eksplisit.

[Latihan tambahan](exercises.md) · [Asesmen simulasi](assessment.md).