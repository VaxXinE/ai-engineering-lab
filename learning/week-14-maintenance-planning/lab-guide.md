# Panduan Hands-on — Rencana Pemeliharaan Solusi AI

**Praktik:** belum dieksekusi. Jangan menulis angka kinerja atau status passed tanpa pengujian.

## Masalah yang dikerjakan

Setelah sistem terpasang, kualitas klasifikasi bisa turun walau service tetap online. Kita merencanakan pengukuran outcome, inspeksi, update, backup, dan incident response sebelum gangguan nyata terjadi.

## Langkah terurut

1. Tetapkan SLI/SLO awal: availability, P95 latency, prediction-error rate, review disagreement rate dan data-quality rejection; tandai sebagai target hipotesis.

2. Untuk tiap metrik tentukan definisi numerator/denominator, sumber log/metric, agregasi dan owner.

3. Susun playbook untuk model outage, drift, model artifact corrupt, kredensial bocor dan DB outage.

4. Tentukan patch schedule, dependency audit, model re-evaluation, serta backup, restore dan retensi.

5. Buat escalation matrix dan human fallback; tentukan kapan AI boleh dinonaktifkan sementara.

6. Lakukan review rencana dengan contoh risiko dan sesuaikan threshold berdasarkan baseline nyata dari pengujian sebelumnya.

## Acceptance criteria

- [ ] Setiap metrik memiliki definisi yang tidak ambigu dan sumber data.
- [ ] Tersedia severity, owner, tindakan, escalation dan jadwal review.
- [ ] Tersedia backup/restore plan, rollback dan kebijakan model update.
- [ ] Privasi log dan akses observability diperhitungkan.
- [ ] Tidak ada klaim 'drift terdeteksi' tanpa data pengamatan.

## Test & evidence protocol

1. Catat environment serta versi runtime dan tools yang benar-benar digunakan.
2. Rekam command/aksi, input sintetis, output, error path dan test results aktual.
3. Jangan menggunakan production data, kredensial atau system perusahaan.
4. Tautkan diagram, source code, logs teredaksi, commits dan evaluasi ke [evidence matrix](../../certification/evidence-matrix.md).
5. Tulis residual risk dan pekerjaan yang belum teruji sebagai catatan eksplisit.

[Latihan tambahan](exercises.md) · [Asesmen simulasi](assessment.md).