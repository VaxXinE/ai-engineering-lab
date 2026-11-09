# Week 10 — Scalability, Performance & Reliability

**Materi:** siap dibaca · **Praktik:** belum diimplementasikan/dijalankan · **Alokasi:** 8–10 jam

**Unit acuan:** J.620100.002.01 — Menganalisis Skalabilitas Perangkat Lunak (verifikasi dokumen LSP terbaru sebelum asesmen).

**Tujuan:** Mengukur bottleneck frontend/backend/DB/inference dan merancang scaling serta failure protection berdasarkan data.

**Prasyarat:** Week 08–09 architecture dan API plan.

## Materi dan tugas
1. [Teori terstruktur](theory.md)
2. [Panduan praktik dan test plan](lab-guide.md)
3. [Latihan mandiri](exercises.md)
4. [Latihan tanya jawab asesmen](assessment.md)

**Indikator hasil:**
- Setiap hasil uji mencantumkan alat, mesin, durasi, concurrency, dan ukuran data.
- Rekomendasi perubahan diturunkan dari bottleneck yang diobservasi.
- Sistem menghindari retry tak berbatas dan uncontrolled external API consumption.
- Terdapat error case dan timeout scenario dalam pengujian.

Semua latihan memakai data sintetis dan mengembangkan [capstone](../../projects/ai-customer-intelligence/README.md). Materi siap bukan bukti implementasi/kelulusan.

[Roadmap](../../docs/learning-roadmap.md) · [Progress](../../docs/progress-tracker.md) · [Evidence mapping](../../certification/evidence-matrix.md)