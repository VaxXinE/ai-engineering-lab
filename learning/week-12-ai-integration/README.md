# Week 12 — Integrasi Komponen Solusi AI

> **Materi v2:** [Deep Dive](deep-dive.md) → [Worked Examples](worked-examples.md) → [Knowledge Check + pembahasan](knowledge-check.md) → [Learning Contract](study-contract.md). Setelah itu baru praktik memakai [Lab Guide](lab-guide.md). Dokumentasi tersedia **bukan berarti latihan peserta sudah selesai**.


**Status materi:** siap dipelajari · **Status implementasi:** belum dikerjakan · **Estimasi:** 8–10 jam

**Acuan unit:** J.62AIN00.014.1 — Mengintegrasikan Komponen Solusi AI. Kode unit dan KUK final memerlukan konfirmasi LSP.

**Tujuan:** Menyatukan model inference, service API, storage, review UI, dan pengujian end-to-end tanpa membuat AI menjadi single point of failure.

## Cara pakai materi
1. Baca [teori](theory.md) dan jelaskan inti konsep dengan bahasa sendiri.
2. Ikuti [lab-guide](lab-guide.md) untuk implementasi (ketika pembelajaran dimulai).
3. Kerjakan [exercises](exercises.md) dan [simulasi asesmen](assessment.md).
4. Simpan artefak nyata di repo dan hubungkan ke [evidence matrix](../../certification/evidence-matrix.md).

**Skenario:** Aplikasi dashboard energi menerima meter reading baru. Service memvalidasi input dan izin, menyimpan record, meminta prediksi melalui inference adapter, memvalidasi label hasil, lalu menampilkan status review. Inference dapat gagal atau memilih abstain.

**Indikator:** 
- Prediksi yang tersimpan selalu mempunyai model_version dan valid label.
- Data meter reading tidak hilang ketika AI gagal.
- Izin akses dites untuk resource berbeda dan tenant lain.
- UI dapat menerima hasil normal, abstain, timeout dan invalid model output.
- Ada bukti tests yang dijalankan, bukan screenshot tanpa reproduksi.

Baca [roadmap](../../docs/learning-roadmap.md) dan [capstone](../../projects/ai-energy-intelligence/README.md). Keberadaan panduan tidak berarti kompetensi telah diverifikasi.