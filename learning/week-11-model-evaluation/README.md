# Week 11 — Model Evaluation, Error Analysis & AI Quality Gates

**Studi kasus domain energi:** [Applied Energy Case — worked reasoning, tantangan, negative tests](energy-case-study.md). Gunakan [canonical domain contract](../../docs/architecture/energy-data-contract.md); semua latihan domain ini masih **planned** sampai ada hasil implementasi teruji.

> **Materi v2:** [Deep Dive](deep-dive.md) → [Worked Examples](worked-examples.md) → [Knowledge Check + pembahasan](knowledge-check.md) → [Learning Contract](study-contract.md). Setelah itu baru praktik memakai [Lab Guide](lab-guide.md). Dokumentasi tersedia **bukan berarti latihan peserta sudah selesai**.


**Materi:** siap dibaca · **Praktik:** belum diimplementasikan/dijalankan · **Alokasi:** 8–10 jam

**Unit acuan:** Pengayaan dan persiapan unit integrasi AI; bukan unit mandiri pada daftar LSP 12 unit. (verifikasi dokumen LSP terbaru sebelum asesmen).

**Tujuan:** Mengembangkan baseline text classifier dan mengukur kualitas hasil secara disiplin sebelum mengintegrasikannya ke API.

**Prasyarat:** Week 01 Naive Bayes baseline, Week 03–04 data quality, Week 05 algoritma.

## Materi dan tugas
1. [Teori terstruktur](theory.md)
2. [Panduan praktik dan test plan](lab-guide.md)
3. [Latihan mandiri](exercises.md)
4. [Latihan tanya jawab asesmen](assessment.md)

**Indikator hasil:**
- Model dievaluasi pada set yang tidak digunakan untuk train/tuning.
- Metrik yang dipilih berhubungan dengan dampak bisnis salah klasifikasi.
- Semua hasil yang dilaporkan benar-benar diukur dan dapat direproduksi.
- Model card menyebut limitasi data sintetis dan risiko domain shift.

Semua latihan memakai data sintetis dan mengembangkan [capstone](../../projects/ai-energy-intelligence/README.md). Materi siap bukan bukti implementasi/kelulusan.

[Roadmap](../../docs/learning-roadmap.md) · [Progress](../../docs/progress-tracker.md) · [Evidence mapping](../../certification/evidence-matrix.md)