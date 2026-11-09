# Week 15 — Eksekusi Maintenance, Troubleshooting dan Recovery

> **Materi v2:** [Deep Dive](deep-dive.md) → [Worked Examples](worked-examples.md) → [Knowledge Check + pembahasan](knowledge-check.md) → [Learning Contract](study-contract.md). Setelah itu baru praktik memakai [Lab Guide](lab-guide.md). Dokumentasi tersedia **bukan berarti latihan peserta sudah selesai**.


**Status materi:** siap dipelajari · **Status implementasi:** belum dikerjakan · **Estimasi:** 8–10 jam

**Acuan unit:** J.62AIN00.017.1 — Merawat Solusi AI. Kode unit dan KUK final memerlukan konfirmasi LSP.

**Tujuan:** Membuktikan proses diagnosis gangguan, perbaikan terkontrol, validasi regresi, dan restore di lingkungan uji.

## Cara pakai materi
1. Baca [teori](theory.md) dan jelaskan inti konsep dengan bahasa sendiri.
2. Ikuti [lab-guide](lab-guide.md) untuk implementasi (ketika pembelajaran dimulai).
3. Kerjakan [exercises](exercises.md) dan [simulasi asesmen](assessment.md).
4. Simpan artefak nyata di repo dan hubungkan ke [evidence matrix](../../certification/evidence-matrix.md).

**Skenario:** Simulasikan service inference offline sehingga klasifikasi gagal. Data inquiry tetap disimpan. Operator memverifikasi degraded mode, memulihkan service, menjalankan regression test, dan mendokumentasikan insiden.

**Indikator:** 
- Simulasi outage tidak kehilangan inquiry yang sudah diterima.
- Restore dijalankan pada environment uji dan diperiksa integritasnya.
- Setiap langkah pemulihan beserta hasil uji dicatat.
- Regression test menguji akar masalah, bukan hanya happy path.
- Tidak ada data customer asli atau secret dalam incident report.

Baca [roadmap](../../docs/learning-roadmap.md) dan [capstone](../../projects/ai-customer-intelligence/README.md). Keberadaan panduan tidak berarti kompetensi telah diverifikasi.