# Week 08 — Database Entities & Relational Integrity

> **Materi v2:** [Deep Dive](deep-dive.md) → [Worked Examples](worked-examples.md) → [Knowledge Check + pembahasan](knowledge-check.md) → [Learning Contract](study-contract.md). Setelah itu baru praktik memakai [Lab Guide](lab-guide.md). Dokumentasi tersedia **bukan berarti latihan peserta sudah selesai**.


**Materi:** siap dibaca · **Praktik:** belum diimplementasikan/dijalankan · **Alokasi:** 8–10 jam

**Unit acuan:** J.620100.007.01 — Mengimplementasikan Rancangan Entitas dan Keterkaitan Antar Entitas (verifikasi dokumen LSP terbaru sebelum asesmen).

**Tujuan:** Merancang struktur data untuk pesan, prediksi AI, versi model, review, dan audit trail dengan integritas kuat.

**Prasyarat:** Week 03–04; SQL, relational keys, transactions.

## Materi dan tugas
1. [Teori terstruktur](theory.md)
2. [Panduan praktik dan test plan](lab-guide.md)
3. [Latihan mandiri](exercises.md)
4. [Latihan tanya jawab asesmen](assessment.md)

**Indikator hasil:**
- Setiap prediction memiliki model_version dan inquiry_id yang valid.
- Foreign key menolak orphan record; rollback transaksi menjaga konsistensi.
- Akses tenant A tidak dapat membaca atau mengubah record tenant B.
- Re-running migration dan duplicate event ditangani sesuai rencana.

Semua latihan memakai data sintetis dan mengembangkan [capstone](../../projects/ai-customer-intelligence/README.md). Materi siap bukan bukti implementasi/kelulusan.

[Roadmap](../../docs/learning-roadmap.md) · [Progress](../../docs/progress-tracker.md) · [Evidence mapping](../../certification/evidence-matrix.md)