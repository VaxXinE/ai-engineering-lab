# Latihan Asesmen — Eksekusi Maintenance, Troubleshooting dan Recovery

**Simulasi nonresmi, bukan soal BNSP.**

## Pertanyaan teknis

1. Apa beda mitigation dan permanent fix?

2. Apa itu root cause?

3. Kenapa restore jangan dilakukan di database live saat latihan?

4. Bagaimana membuktikan rollback berhasil?

5. Apa isi postmortem?

6. Apa hubungan monitoring dengan incident detection?

7. Bagaimana menghindari PII leak dalam incident report?

8. Kapan harus rollback model walau semua HTTP endpoints masih 200?

## Bukti demonstrasi

- [ ] Simulasi outage tidak kehilangan meter reading yang sudah diterima.
- [ ] Restore dijalankan pada environment uji dan diperiksa integritasnya.
- [ ] Setiap langkah pemulihan beserta hasil uji dicatat.
- [ ] Regression test menguji akar masalah, bukan hanya happy path.
- [ ] Tidak ada data device asli atau secret dalam incident report.

## Rubrik penilaian diri

- **Konsep:** menjelaskan tujuan, konsep dan alasan pilihan.
- **Praktik:** menunjukkan artefak yang dibuat sendiri dan reproducible.
- **Kualitas:** menyertakan test negatif dan outcome yang aktual.
- **Keamanan:** privasi, authorization, data handling, dan risks jelas.
- **Komunikasi:** dapat menjawab apa yang belum berhasil, risiko sisa dan langkah perbaikan.

Self-assessment hanya latihan. Hasil kompeten ditetapkan oleh LSP melalui asesmen resmi. [Portfolio](../../certification/evidence-matrix.md).