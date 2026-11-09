# Week 07 — Implementasi UI Dashboard AI

**Studi kasus domain energi:** [Applied Energy Case — worked reasoning, tantangan, negative tests](energy-case-study.md). Gunakan [canonical domain contract](../../docs/architecture/energy-data-contract.md); semua latihan domain ini masih **planned** sampai ada hasil implementasi teruji.

> **Materi v2:** [Deep Dive](deep-dive.md) → [Worked Examples](worked-examples.md) → [Knowledge Check + pembahasan](knowledge-check.md) → [Learning Contract](study-contract.md). Setelah itu baru praktik memakai [Lab Guide](lab-guide.md). Dokumentasi tersedia **bukan berarti latihan peserta sudah selesai**.


**Materi:** siap dibaca · **Praktik:** belum diimplementasikan/dijalankan · **Alokasi:** 8–10 jam

**Unit acuan:** J.620100.005.02 — Mengimplementasikan User Interface (verifikasi dokumen LSP terbaru sebelum asesmen).

**Tujuan:** Menerapkan wireframe Week 06 menjadi frontend yang responsif, aksesibel, dan aman menghadapi hasil AI yang tidak pasti.

**Prasyarat:** Week 06; TypeScript, React dan HTTP API dasar.

## Materi dan tugas
1. [Teori terstruktur](theory.md)
2. [Panduan praktik dan test plan](lab-guide.md)
3. [Latihan mandiri](exercises.md)
4. [Latihan tanya jawab asesmen](assessment.md)

**Indikator hasil:**
- Semua state idle/loading/empty/success/error dapat direproduksi.
- Label AI dan keputusan manusia ditampilkan berbeda.
- Aksi double-submit tertahan di UI dan direncanakan juga dicegah di server.
- Komponen kritis dapat digunakan dengan keyboard.

Semua latihan memakai data sintetis dan mengembangkan [capstone](../../projects/ai-energy-intelligence/README.md). Materi siap bukan bukti implementasi/kelulusan.

[Roadmap](../../docs/learning-roadmap.md) · [Progress](../../docs/progress-tracker.md) · [Evidence mapping](../../certification/evidence-matrix.md)