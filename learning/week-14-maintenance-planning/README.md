# Week 14 — Rencana Pemeliharaan Solusi AI

> **Materi v2:** [Deep Dive](deep-dive.md) → [Worked Examples](worked-examples.md) → [Knowledge Check + pembahasan](knowledge-check.md) → [Learning Contract](study-contract.md). Setelah itu baru praktik memakai [Lab Guide](lab-guide.md). Dokumentasi tersedia **bukan berarti latihan peserta sudah selesai**.


**Status materi:** siap dipelajari · **Status implementasi:** belum dikerjakan · **Estimasi:** 8–10 jam

**Acuan unit:** J.62AIN00.016.1 — Merencanakan Perawatan Solusi AI. Kode unit dan KUK final memerlukan konfirmasi LSP.

**Tujuan:** Menghasilkan maintenance plan yang memisahkan reliability aplikasi, kualitas prediksi, keamanan dependency dan pemulihan insiden.

## Cara pakai materi
1. Baca [teori](theory.md) dan jelaskan inti konsep dengan bahasa sendiri.
2. Ikuti [lab-guide](lab-guide.md) untuk implementasi (ketika pembelajaran dimulai).
3. Kerjakan [exercises](exercises.md) dan [simulasi asesmen](assessment.md).
4. Simpan artefak nyata di repo dan hubungkan ke [evidence matrix](../../certification/evidence-matrix.md).

**Skenario:** Setelah sistem terpasang, kualitas klasifikasi bisa turun walau service tetap online. Kita merencanakan pengukuran outcome, inspeksi, update, backup, dan incident response sebelum gangguan nyata terjadi.

**Indikator:** 
- Setiap metrik memiliki definisi yang tidak ambigu dan sumber data.
- Tersedia severity, owner, tindakan, escalation dan jadwal review.
- Tersedia backup/restore plan, rollback dan kebijakan model update.
- Privasi log dan akses observability diperhitungkan.
- Tidak ada klaim 'drift terdeteksi' tanpa data pengamatan.

Baca [roadmap](../../docs/learning-roadmap.md) dan [capstone](../../projects/ai-energy-intelligence/README.md). Keberadaan panduan tidak berarti kompetensi telah diverifikasi.