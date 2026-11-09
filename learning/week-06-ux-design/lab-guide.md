# Praktikum — Week 06: User Experience for AI-Assisted Workflows

**Status:** rancangan latihan. Belum ada klaim bahwa langkah di bawah berhasil dijalankan.

## Konteks

Jika prediksi 'support' salah dan agent memilih 'sales', tampilkan 'Label diperbarui' plus riwayat audit. Jangan diam-diam menghilangkan prediksi awal: itu merusak ability to evaluate model.

**Prasyarat:** Use-case Week 01 dan acceptance criteria capstone.  
**Dataset:** data sintetis dari capstone; jangan memakai data perusahaan atau kredensial sungguhan.

## Langkah kerja

1. Buat dua persona singkat: agent dan supervisor, termasuk pain points dan hak akses.

2. Petakan journey dari incoming inquiry, AI prediction, review, override, submit, dan audit trail.

3. Gambar wireframe Inbox, Detail, Review Queue, dan Empty/Error state memakai alat pilihan.

4. Prototipe alur ketika prediksi abstain dan ketika inference service timeout.

5. Buat kriteria usability (dapat menemukan unread inquiries, review tanpa kehilangan draft, melihat status model) dan tiga task test.

6. Evaluasi minimum keyboard navigation, label controls, semantic alerts, dan keterbacaan.

## Test plan minimal

1. Agent bisa menemukan 1 inquiry tanpa tersesat.
2. Pada timeout AI, data pesan tetap terlihat dan aksi manual tersedia.
3. Semua input punya label yang jelas dan fokus keyboard terurut.
4. Status 'abstain' tidak keliru ditampilkan sebagai kepastian.

## Acceptance criteria

- [ ] Journey memuat alur sukses, error, dan manual override.
- [ ] Prediksi AI dibedakan dari keputusan manusia.
- [ ] Wireframe mencakup loading/empty/error state dan aksesibilitas.
- [ ] Ada minimal tiga task usability dengan success criteria.

## Bukti yang disimpan setelah praktik

1. Source code / artefak desain serta alasan keputusan yang dibuat sendiri.
2. Cara menjalankan atau mereproduksi hasil (versi environment dan perintah aktual).
3. Test report: perintah, hasil sesungguhnya, sampel negatif dan edge cases.
4. Analisis risiko keamanan, privasi, performa, serta keterbatasan yang belum ditangani.
5. Link PR/commit ke [matriks bukti](../../certification/evidence-matrix.md).

## Syarat selesai

**Belum selesai** hanya dengan membaca dokumen ini. Tandai selesai setelah implementasi diverifikasi dan evidence tersimpan; uji kompetensi BNSP tetap dilakukan oleh LSP yang berwenang.

[Latihan tambahan](exercises.md) · [Simulasi asesmen](assessment.md)
