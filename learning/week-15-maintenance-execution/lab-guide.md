# Panduan Hands-on — Eksekusi Maintenance, Troubleshooting dan Recovery

**Praktik:** belum dieksekusi. Jangan menulis angka kinerja atau status passed tanpa pengujian.

## Masalah yang dikerjakan

Simulasikan service inference offline sehingga klasifikasi gagal. Data inquiry tetap disimpan. Operator memverifikasi degraded mode, memulihkan service, menjalankan regression test, dan mendokumentasikan insiden.

## Langkah terurut

1. Buat test environment terpisah dengan dataset sintetis dan snapshot/backup awal; catat keadaan awal.

2. Simulasikan inference timeout dengan fake adapter atau service dihentikan, tanpa mengganggu production apapun.

3. Periksa error logs dan status health, tetapkan tingkat insiden, dan aktifkan fallback manual review.

4. Lakukan rollback/restart/update terkontrol sesuai runbook, lalu uji request awal dan failure path.

5. Uji database backup restore pada environment terpisah; bandingkan count/checksums dan ukur durasi.

6. Tulis incident report (timeline, root cause, impact, corrective action), change log dan bukti regression tests.

## Acceptance criteria

- [ ] Simulasi outage tidak kehilangan inquiry yang sudah diterima.
- [ ] Restore dijalankan pada environment uji dan diperiksa integritasnya.
- [ ] Setiap langkah pemulihan beserta hasil uji dicatat.
- [ ] Regression test menguji akar masalah, bukan hanya happy path.
- [ ] Tidak ada data customer asli atau secret dalam incident report.

## Test & evidence protocol

1. Catat environment serta versi runtime dan tools yang benar-benar digunakan.
2. Rekam command/aksi, input sintetis, output, error path dan test results aktual.
3. Jangan menggunakan production data, kredensial atau system perusahaan.
4. Tautkan diagram, source code, logs teredaksi, commits dan evaluasi ke [evidence matrix](../../certification/evidence-matrix.md).
5. Tulis residual risk dan pekerjaan yang belum teruji sebagai catatan eksplisit.

[Latihan tambahan](exercises.md) · [Asesmen simulasi](assessment.md).