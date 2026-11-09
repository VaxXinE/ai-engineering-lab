# Rubrik Kualitas Materi — Editorial Review

Gunakan untuk menilai kekurangan konten sebelum diajarkan.

| Aspek | 0 (tidak ada) | 1 (dasar) | 2 (memadai) | 3 (mendalam) |
| --- | --- | --- | --- | --- |
| Learning outcome | Tidak ada | Umum: 'paham' | Terukur | Terukur + evidence + transfer |
| Konsep | Daftar jargon | Definisi singkat | Penjelasan mekanisme | Mekanisme, trade-off, failure modes |
| Worked example | Tidak ada | Hasil tanpa proses | Langkah dan alasan | Dua contoh, counterexample, analisis |
| Guided practice | Tidak ada | Tugas abstrak | Task + acceptance | Scaffolding + variasi dan transfer |
| Assessment | Pertanyaan tanpa feedback | Pertanyaan umum | Jawaban beralasan | Miskonsepsi + feedback + rubrik |
| Security/reliability | Diabaikan | Generic warning | Risiko sesuai konteks | Kontrol, prioritas dan negative test |
| Evidence BNSP | Tak terkait | Klaim umum | Unit published dipetakan | Elemen/KUK terverifikasi LSP + bukti sendiri |
| Source/traceability | Tanpa sumber | Blog tak jelas | Dokumentasi primer | Sumber terbaru dan tanggal verifikasi |

**Target editorial v2:** minimum skor 2 pada outcome, konsep, worked example, guided practice, assessment dan security; skor 3 hanya jika bukti benar-benar mendukung. Jangan membuat skor fiktif untuk modul.

## Audit gap

- Week 01: sudah punya runnable example; tetap perlu teach-back, retrieval quiz, dan penjelasan lebih mendalam.
- Week 02–16: kode capstone belum diimplementasikan; materi harus membedakan worked example **illustrative** dari executed lab.
- Setiap unit: Elemen/KUK resmi belum dipetakan 1:1; tidak mengklaim siap dinilai.

## Mandatory review after Phase 3

- Every Week 01–16 includes a **distinct `energy-case-study.md`** with measurable task, worked reasoning, negative/security case and expected evidence.
- All numerically focused lessons comply with [canonical energy contract](architecture/energy-data-contract.md): site/meter/source identity, explicit interval, UTC, finite nonnegative kWh, gap ≠ zero.
- Week 01 is a text ML exercise, not an energy anomaly detector; Week 11–12 evaluate numerical time-series.
- Only real test output may be called verified. Documentation coverage does not mean code coverage.
