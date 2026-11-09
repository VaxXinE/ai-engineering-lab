# Latihan Asesmen — Integrasi Komponen Solusi AI

**Simulasi nonresmi, bukan soal BNSP.**

## Pertanyaan teknis

1. Apa gunanya AI adapter terpisah?

2. Mengapa model output perlu divalidasi lagi?

3. Bagaimana memastikan semua request review authorized?

4. Apa yang terjadi saat model timeout?

5. Apa perbedaan retry aman dan unsafe?

6. Bagaimana mencegah logging data sensitif?

7. Kenapa model_version harus disimpan?

8. Bagaimana desain contract test?

## Bukti demonstrasi

- [ ] Prediksi yang tersimpan selalu mempunyai model_version dan valid label.
- [ ] Data meter reading tidak hilang ketika AI gagal.
- [ ] Izin akses dites untuk resource berbeda dan tenant lain.
- [ ] UI dapat menerima hasil normal, abstain, timeout dan invalid model output.
- [ ] Ada bukti tests yang dijalankan, bukan screenshot tanpa reproduksi.

## Rubrik penilaian diri

- **Konsep:** menjelaskan tujuan, konsep dan alasan pilihan.
- **Praktik:** menunjukkan artefak yang dibuat sendiri dan reproducible.
- **Kualitas:** menyertakan test negatif dan outcome yang aktual.
- **Keamanan:** privasi, authorization, data handling, dan risks jelas.
- **Komunikasi:** dapat menjawab apa yang belum berhasil, risiko sisa dan langkah perbaikan.

Self-assessment hanya latihan. Hasil kompeten ditetapkan oleh LSP melalui asesmen resmi. [Portfolio](../../certification/evidence-matrix.md).