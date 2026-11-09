# Week 09 — Software Architecture for AI-Enabled Applications

**Materi:** siap dibaca · **Praktik:** belum diimplementasikan/dijalankan · **Alokasi:** 8–10 jam

**Unit acuan:** J.620100.008.01 — Merancang Arsitektur Aplikasi (verifikasi dokumen LSP terbaru sebelum asesmen).

**Tujuan:** Merancang batas komponen, contract API, alur data, failure handling dan desain yang tetap fleksibel saat model AI berubah.

**Prasyarat:** Week 02 technology ADR, Week 07 UI, Week 08 database.

## Materi dan tugas
1. [Teori terstruktur](theory.md)
2. [Panduan praktik dan test plan](lab-guide.md)
3. [Latihan mandiri](exercises.md)
4. [Latihan tanya jawab asesmen](assessment.md)

**Indikator hasil:**
- Diagram konsisten dengan requirement dan relasi data.
- Semua endpoint kritis memiliki kontrak validasi dan error codes.
- AI inference failure tidak menghilangkan data yang sudah diterima.
- Authorization dan secret handling ditempatkan pada trust boundary yang benar.

Semua latihan memakai data sintetis dan mengembangkan [capstone](../../projects/ai-customer-intelligence/README.md). Materi siap bukan bukti implementasi/kelulusan.

[Roadmap](../../docs/learning-roadmap.md) · [Progress](../../docs/progress-tracker.md) · [Evidence mapping](../../certification/evidence-matrix.md)