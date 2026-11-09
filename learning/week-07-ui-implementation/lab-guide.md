# Hands-on — Implementasi UI Dashboard AI

**Status:** panduan siap; langkah belum dieksekusi. Implementasi, metrik, dan bukti ditulis setelah praktikum.

## Target

Menerapkan wireframe Week 06 menjadi frontend yang responsif, aksesibel, dan aman menghadapi hasil AI yang tidak pasti.

## Skenario

Untuk meter reading yang masuk dengan label 'warning', operator melihat prediksi lalu memilih 'normal'. UI menampilkan konfirmasi, menyimpan action, serta mengembalikan hasil audit. Request gagal tidak menghilangkan perubahan yang belum tersimpan.

## Langkah implementasi

1. Review wireframe dari Week 06 dan definisikan type MeterReading, Prediction, ReviewStatus dengan union yang jelas.

2. Bangun halaman Inbox dengan filter kategori dan review state serta empty/error/loading states.

3. Bangun detail view dan form override dengan alasan wajib, inline validation dan pending submit.

4. Sediakan mocked API adapter lokal untuk latihan; dokumentasikan kontrak sebelum memakai backend nyata.

5. Uji keyboard navigation dan perbedaan state ketika AI mengeluarkan abstain atau timeout.

6. Buat component tests untuk label, invalid form, pending submit, dan error recovery; dokumentasikan hasil nyata.

## Acceptance criteria

- [ ] Semua state idle/loading/empty/success/error dapat direproduksi.
- [ ] Label AI dan keputusan manusia ditampilkan berbeda.
- [ ] Aksi double-submit tertahan di UI dan direncanakan juga dicegah di server.
- [ ] Komponen kritis dapat digunakan dengan keyboard.

## Rencana verifikasi

1. Buat skenario bukti untuk: Semua state idle/loading/empty/success/error dapat direproduksi.
2. Buat skenario bukti untuk: Label AI dan keputusan manusia ditampilkan berbeda.
3. Buat skenario bukti untuk: Aksi double-submit tertahan di UI dan direncanakan juga dicegah di server.
4. Buat skenario bukti untuk: Komponen kritis dapat digunakan dengan keyboard.

## Dokumentasi hasil

- Catat perintah, dependency/runtime, input sintetis, output aktual, dan edge case yang diuji.
- Catat source code atau desain beserta commit/PR.
- Tuliskan threat dan asumsi tersisa. Jangan menyatakan 'passed' sebelum menjalankan test.
- Kaitkan hasil dengan [evidence matrix](../../certification/evidence-matrix.md).

[Latihan](exercises.md) · [Simulasi](assessment.md)