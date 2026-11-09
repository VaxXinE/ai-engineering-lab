# Week 05 — Data Structures, Algorithms & Complexity

**Studi kasus domain energi:** [Applied Energy Case — worked reasoning, tantangan, negative tests](energy-case-study.md). Gunakan [canonical domain contract](../../docs/architecture/energy-data-contract.md); semua latihan domain ini masih **planned** sampai ada hasil implementasi teruji.

> **Materi v2:** [Deep Dive](deep-dive.md) → [Worked Examples](worked-examples.md) → [Knowledge Check + pembahasan](knowledge-check.md) → [Learning Contract](study-contract.md). Setelah itu baru praktik memakai [Lab Guide](lab-guide.md). Dokumentasi tersedia **bukan berarti latihan peserta sudah selesai**.


**Status materi: Siap dipelajari** · **Status praktik: Belum dikerjakan** · **Alokasi:** 8–10 jam

> **Ruang lingkup unit pada daftar LSP yang terpublikasi:** J.620100.004.02 — Menggunakan Struktur Data. Kode/skema final harus diverifikasi kembali pada dokumen LSP terkini.

**Tujuan:** Memilih struktur data agar pipeline dan API tidak berubah menjadi bottleneck saat record bertambah.

**Prasyarat:** Modul 3–4; Python collection types dan dasar fungsi.

## Urutan baca dan kerja

1. [Materi teori](theory.md) — konsep, alasan teknis, contoh dan risiko.
2. [Panduan hands-on](lab-guide.md) — langkah implementasi dan acceptance criteria.
3. [Latihan mandiri](exercises.md) — tugas wajib dan tantangan.
4. [Simulasi asesmen](assessment.md) — pertanyaan, demo, rubrik.

## Hasil yang direncanakan

- Implementasi menyimpan satu item per unique ID dan punya aturan 'first wins' atau 'last wins' jelas.
- Semua input edge case diuji.
- Analisis Big O dan memory trade-off ditulis.
- Benchmark menyertakan lingkungan, jumlah record, dan metode.

**Catatan:** seluruh latihan merujuk proyek [AI Smart Energy Monitoring](../../projects/ai-energy-intelligence/README.md), menggunakan data sintetis. Materi yang lengkap tidak berarti code, pengujian atau asesmen telah diselesaikan.

[Lihat roadmap](../../docs/learning-roadmap.md) · [Tracker](../../docs/progress-tracker.md) · [Evidence matrix](../../certification/evidence-matrix.md)
