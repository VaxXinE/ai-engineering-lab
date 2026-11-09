# Latihan Asesmen — Instalasi, Konfigurasi dan Deployment AI

**Simulasi nonresmi, bukan soal BNSP.**

## Pertanyaan teknis

1. Apa beda Docker image dengan container?

2. Mengapa tag latest bukan strategi reproducible?

3. Apa beda liveness dan readiness?

4. Mengapa DB tidak semestinya diekspos ke internet?

5. Apa itu secret injection?

6. Mengapa restore test wajib?

7. Bagaimana perubahan database bisa menggagalkan rollback?

8. Apa arti RPO dan RTO?

## Bukti demonstrasi

- [ ] Satu runbook cukup untuk instalasi pada environment bersih.
- [ ] Tidak ada credential asli, privileged container yang tidak perlu, atau secret di image.
- [ ] Health/status endpoints memberi sinyal operasional yang tepat.
- [ ] Smoke test dan rollback diuji serta hasilnya dicatat.
- [ ] Model artifact punya provenance/version/hash atau kontrol setara.

## Rubrik penilaian diri

- **Konsep:** menjelaskan tujuan, konsep dan alasan pilihan.
- **Praktik:** menunjukkan artefak yang dibuat sendiri dan reproducible.
- **Kualitas:** menyertakan test negatif dan outcome yang aktual.
- **Keamanan:** privasi, authorization, data handling, dan risks jelas.
- **Komunikasi:** dapat menjawab apa yang belum berhasil, risiko sisa dan langkah perbaikan.

Self-assessment hanya latihan. Hasil kompeten ditetapkan oleh LSP melalui asesmen resmi. [Portfolio](../../certification/evidence-matrix.md).