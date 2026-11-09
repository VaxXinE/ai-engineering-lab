# Hands-on — Database Entities & Relational Integrity

**Status:** panduan siap; langkah belum dieksekusi. Implementasi, metrik, dan bukti ditulis setelah praktikum.

## Target

Merancang struktur data untuk pesan, prediksi AI, versi model, review, dan audit trail dengan integritas kuat.

## Skenario

Inquiry dibuat pada 09.00 dengan model v1, lalu direview ulang oleh agent. Model v2 dipasang minggu berikutnya. Riwayat harus tetap bisa menunjukkan prediksi v1 dan tindakan agent tanpa menghapus data historis.

## Langkah implementasi

1. Definisikan entity diagram untuk organization, user, inquiry, model_version, prediction, review_event, ingestion_batch.

2. Tentukan data dictionary berisi tipe, nullable rules, uniqueness, retention dan relasi.

3. Buat migration SQL dengan foreign key dan check constraints, bukan tabel di-create manual tanpa versi.

4. Implementasikan parameterized SQL pada repository layer dan filter organisasi dalam setiap read/update.

5. Tambah optimistic concurrency atau unique version supaya simultaneous edits terdeteksi.

6. Buat integration tests untuk duplicate event, foreign key, rollback dan cross-tenant IDOR.

## Acceptance criteria

- [ ] Setiap prediction memiliki model_version dan inquiry_id yang valid.
- [ ] Foreign key menolak orphan record; rollback transaksi menjaga konsistensi.
- [ ] Akses tenant A tidak dapat membaca atau mengubah record tenant B.
- [ ] Re-running migration dan duplicate event ditangani sesuai rencana.

## Rencana verifikasi

1. Buat skenario bukti untuk: Setiap prediction memiliki model_version dan inquiry_id yang valid.
2. Buat skenario bukti untuk: Foreign key menolak orphan record; rollback transaksi menjaga konsistensi.
3. Buat skenario bukti untuk: Akses tenant A tidak dapat membaca atau mengubah record tenant B.
4. Buat skenario bukti untuk: Re-running migration dan duplicate event ditangani sesuai rencana.

## Dokumentasi hasil

- Catat perintah, dependency/runtime, input sintetis, output aktual, dan edge case yang diuji.
- Catat source code atau desain beserta commit/PR.
- Tuliskan threat dan asumsi tersisa. Jangan menyatakan 'passed' sebelum menjalankan test.
- Kaitkan hasil dengan [evidence matrix](../../certification/evidence-matrix.md).

[Latihan](exercises.md) · [Simulasi](assessment.md)