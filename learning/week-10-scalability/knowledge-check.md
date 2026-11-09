# Retrieval Quiz — Skalabilitas dari metrik, kapasitas, dan tail latency

**Petunjuk:** jawab dari ingatan, bukan sekadar mencari keyword di dokumen. Pembahasan berada setelah pertanyaan agar bisa membandingkan reasoning.

## Pertanyaan

1. Apa bedanya P95 dan rata-rata?
2. 40 req/s * 0.25 s menghasilkan berapa in-flight average?
3. Mengapa scaling API tak selalu membantu?
4. Apa risiko cache inference?
5. Mengapa jitter membantu retry?
6. Apa minimum laporan benchmark?

## Pembahasan

**1.** P95 berarti 95% pengamatan berada pada atau di bawah angka tersebut; average menyamarkan ekor lambat.

**2.** Sekitar 10 jika steady-state dan asumsi Little's Law terpenuhi.

**3.** DB atau inference provider bisa menjadi bottleneck dominan.

**4.** Data leak antar tenant, stale model version, replay informasi sensitif, dan invalidation kompleks.

**5.** Menyebarkan retry sehingga banyak client tidak menyerang provider pada waktu sama.

**6.** Environment, workload, tool, version, duration, metrics, errors, method dan limitations.

## Koreksi aktif

Tandai jawaban yang keliru dan tulis satu contoh baru yang bisa membedakan konsep salah dengan konsep benar. Jika semua soal benar tetapi tidak mampu menyelesaikan variasi baru, statusnya belum dikuasai.

## Review bertahap

- Hari 0: semua pertanyaan.
- Hari +1: ulangi topik sulit tanpa buku.
- Hari +7: campur dengan modul sebelumnya.
- Hari +21: teach-back dan praktik pada skenario capstone baru.

[Teori mendalam](deep-dive.md)
