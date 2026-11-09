# Retrieval Quiz — Arsitektur AI yang isolasi kegagalan dan tanggung jawabnya jelas

**Petunjuk:** jawab dari ingatan, bukan sekadar mencari keyword di dokumen. Pembahasan berada setelah pertanyaan agar bisa membandingkan reasoning.

## Pertanyaan

1. Apa trust boundary utama browser → backend?
2. Kapan microservices layak?
3. Mengapa AI adapter membantu maintainability?
4. Apa risiko DB transaction terbuka selama remote inference?
5. Apa gunanya outbox?
6. Apa yang dilakukan jika model outage?

## Pembahasan

**1.** Input dan identitas dari browser tidak tepercaya, semua permission dan schema harus divalidasi server-side.

**2.** Jika ada kebutuhan scaling, ownership, release isolation yang nyata dan tim mampu mengelola kompleksitas operasional.

**3.** Model/provider dapat diganti dan diuji tanpa mengubah domain/API contract.

**4.** Lock duration dan resource contention meningkat, rollback bisa membuang inquiry.

**5.** Membantu menyelaraskan state database dengan penerbitan event asynchronous saat ada crash.

**6.** Simpan inquiry, tandai fallback/retry state, berikan manual review dan monitoring.

## Koreksi aktif

Tandai jawaban yang keliru dan tulis satu contoh baru yang bisa membedakan konsep salah dengan konsep benar. Jika semua soal benar tetapi tidak mampu menyelesaikan variasi baru, statusnya belum dikuasai.

## Review bertahap

- Hari 0: semua pertanyaan.
- Hari +1: ulangi topik sulit tanpa buku.
- Hari +7: campur dengan modul sebelumnya.
- Hari +21: teach-back dan praktik pada skenario capstone baru.

[Teori mendalam](deep-dive.md)
