# Teori — Database Entities & Relational Integrity

**Hasil belajar:** Merancang struktur data untuk pesan, prediksi AI, versi model, review, dan audit trail dengan integritas kuat.

## 1. Conceptual, logical dan physical modeling

Mulai dari entity dan business rules, turunkan menjadi kolom dan relasi lalu implementasi tabel, index dan constraints. Jangan menduplikasi informasi seperti nama customer pada setiap prediction jika relasi customer_id sudah ada; normalisasi mencegah update anomaly. Denormalisasi hanya dilakukan setelah kebutuhan performa terukur.

## 2. Keys dan cardinality

Customer memiliki banyak Inquiry; satu Inquiry dapat memiliki beberapa Prediction per model version, lalu review berbeda. Gunakan primary key, foreign key, uniqueness untuk idempotent event, dan check constraints untuk enum/rentang sah. Tentukan perilaku ON DELETE secara eksplisit, tidak hanya mengandalkan default.

## 3. Auditability

Prediksi AI dan hasil review sebaiknya menjadi event yang dipertahankan, bukan satu kolom yang ditimpa. Dengan itu engineer bisa menilai kualitas model, waktu perubahan dan siapa reviewer. Hindari menyimpan metadata sensitif yang tidak perlu. Catat model_version agar prediksi lama bisa dijelaskan.

## 4. Transactions dan concurrency

Dua agent dapat memperbarui inquiry yang sama. Gunakan optimistic concurrency (version column), unique event keys, dan transaction boundary. Race condition tetap mungkin walau frontend sudah men-disable tombol, sehingga integritas perlu ditegakkan oleh database dan backend.

## 5. Authorization dan tenancy

ID bukan bukti hak akses. Semua query untuk data privat harus dibatasi scope user/org dan diuji dengan setidaknya dua tenant sintetis. Gunakan indexing untuk query yang sering dipakai tanpa mengindeks semua kolom secara membabi buta; indeks mempercepat read namun memperlambat write dan memakan storage.

## Skenario rekayasa perangkat lunak

Inquiry dibuat pada 09.00 dengan model v1, lalu direview ulang oleh agent. Model v2 dipasang minggu berikutnya. Riwayat harus tetap bisa menunjukkan prediksi v1 dan tindakan agent tanpa menghapus data historis.

## Prinsip dan acceptance criteria

- Setiap prediction memiliki model_version dan inquiry_id yang valid.
- Foreign key menolak orphan record; rollback transaksi menjaga konsistensi.
- Akses tenant A tidak dapat membaca atau mengubah record tenant B.
- Re-running migration dan duplicate event ditangani sesuai rencana.

## Dokumentasi primer untuk pendalaman

- https://www.postgresql.org/docs/current/ddl-constraints.html
- https://www.postgresql.org/docs/current/tutorial-transactions.html
- https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/

Penjelasan ini mengaitkan materi praktik dengan unit yang dipublikasikan LSP. Ini bukan reproduksi KUK resmi dan tidak menentukan hasil asesmen.

[Praktikum](lab-guide.md)