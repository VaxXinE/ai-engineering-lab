# Week 03 — Data Ingestion & ETL

**Studi kasus domain energi:** [Applied Energy Case — worked reasoning, tantangan, negative tests](energy-case-study.md). Gunakan [canonical domain contract](../../docs/architecture/energy-data-contract.md); semua latihan domain ini masih **planned** sampai ada hasil implementasi teruji.

> **Materi v2:** [Deep Dive](deep-dive.md) → [Worked Examples](worked-examples.md) → [Knowledge Check + pembahasan](knowledge-check.md) → [Learning Contract](study-contract.md). Setelah itu baru praktik memakai [Lab Guide](lab-guide.md). Dokumentasi tersedia **bukan berarti latihan peserta sudah selesai**.


**Status materi: Siap dipelajari** · **Status praktik: Belum dikerjakan** · **Alokasi:** 8–10 jam

> **Ruang lingkup unit pada daftar LSP yang terpublikasi:** J.63OPR00.014.2 — Melakukan Pemasukan Data. Kode/skema final harus diverifikasi kembali pada dokumen LSP terkini.

**Tujuan:** Memindahkan dataset catatan kejadian perangkat sintetis ke storage secara konsisten, audit-able, dan aman diulang.

**Prasyarat:** Modul 1 dan 2; Python standard library CSV; dasar SQL.

## Urutan baca dan kerja

1. [Materi teori](theory.md) — konsep, alasan teknis, contoh dan risiko.
2. [Panduan hands-on](lab-guide.md) — langkah implementasi dan acceptance criteria.
3. [Latihan mandiri](exercises.md) — tugas wajib dan tantangan.
4. [Simulasi asesmen](assessment.md) — pertanyaan, demo, rubrik.

## Hasil yang direncanakan

- CSV valid dapat diproses dengan hasil terhitung.
- Input invalid ditolak dan dilaporkan tanpa menyimpan record corrupt.
- Menjalankan batch yang sama dua kali tidak menghasilkan duplikasi.
- Query parameterized dan transaction behavior teruji.

**Catatan:** seluruh latihan merujuk proyek [AI Smart Energy Monitoring](../../projects/ai-energy-intelligence/README.md), menggunakan data sintetis. Materi yang lengkap tidak berarti code, pengujian atau asesmen telah diselesaikan.

[Lihat roadmap](../../docs/learning-roadmap.md) · [Tracker](../../docs/progress-tracker.md) · [Evidence matrix](../../certification/evidence-matrix.md)
