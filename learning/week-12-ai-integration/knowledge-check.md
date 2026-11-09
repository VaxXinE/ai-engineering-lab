# Retrieval Quiz — Integrasi inference dengan typed contracts, idempotency, dan failure containment

**Petunjuk:** jawab dari ingatan, bukan sekadar mencari keyword di dokumen. Pembahasan berada setelah pertanyaan agar bisa membandingkan reasoning.

## Pertanyaan

1. Mengapa response AI perlu schema validation?
2. Bolehkah anomaly scorer menentukan site_id atau permissions?
3. Apa fallback aman ketika inference gagal?
4. Bagaimana menguji provider tanpa biaya jaringan?
5. Apa itu prompt injection pada kasus telemetri?
6. Mengapa idempotency penting pada worker?

## Pembahasan

**1.** Model output bisa salah bentuk atau nilai meski HTTP 200; kontrak mencegah corrupt data.

**2.** Tidak. Server harus menggunakan authorization context, bukan output model.

**3.** Pertahankan meter reading dan tampilkan manual review atau bounded retry.

**4.** Fake adapter deterministik plus contract/negative tests; provider integration test terpisah opsional.

**5.** Jika suatu saat AI generatif memproses catatan perangkat, teks input yang mengandung instruksi berbahaya bisa membelokkan model; pada anomaly scorer numerik Week 12 risiko utama adalah output tidak valid, data leakage, dan penyalahgunaan API.

**6.** Retry setelah timeout dapat memproses event yang sama berkali-kali tanpa key/constraint.

## Koreksi aktif

Tandai jawaban yang keliru dan tulis satu contoh baru yang bisa membedakan konsep salah dengan konsep benar. Jika semua soal benar tetapi tidak mampu menyelesaikan variasi baru, statusnya belum dikuasai.

## Review bertahap

- Hari 0: semua pertanyaan.
- Hari +1: ulangi topik sulit tanpa buku.
- Hari +7: campur dengan modul sebelumnya.
- Hari +21: teach-back dan praktik pada skenario capstone baru.

[Teori mendalam](deep-dive.md)
