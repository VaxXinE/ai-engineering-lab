# Simulasi Asesmen — Scalability, Performance & Reliability

Ini pertanyaan latihan nonresmi, **bukan bank soal BNSP**.

1. Apa beda latency, throughput dan concurrency?

2. Kenapa P95 penting?

3. Apa arti saturation?

4. Bagaimana memilih sync vs async job?

5. Mengapa retry dapat memperparah outage?

6. Bagaimana mengestimasi biaya token eksternal tanpa angka palsu?

7. Kapan caching memberi masalah correctness?

8. Apa syarat benchmark dapat direproduksi?

## Demonstrasi yang harus mampu dilakukan

- [ ] Setiap hasil uji mencantumkan alat, mesin, durasi, concurrency, dan ukuran data.
- [ ] Rekomendasi perubahan diturunkan dari bottleneck yang diobservasi.
- [ ] Sistem menghindari retry tak berbatas dan uncontrolled external API consumption.
- [ ] Terdapat error case dan timeout scenario dalam pengujian.

## Pengukuran kesiapan

1. **Konsep:** jelaskan tiap keputusan teknis dan trade-off.
2. **Praktik:** tunjukkan artefak yang dibuat sendiri beserta cara menjalankannya.
3. **Validasi:** tunjukkan hasil test aktual dan penanganan edge case.
4. **Risk:** jelaskan security, privacy, failure dan batasan pendekatan.
5. **Evidence:** dokumentasikan referensi commit/PR, diagram, logs, dan test.

Status 'kompeten' tetap ditetapkan melalui asesmen resmi LSP berlisensi, bukan penilaian diri.

[Portfolio](../../certification/evidence-matrix.md)