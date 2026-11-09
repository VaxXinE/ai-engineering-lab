# Deep Dive — Model data yang mencegah kehilangan historis prediksi dan celah akses

**Target:** setelah modul, lo dapat mempertahankan pilihan desain melalui contoh dan kontra-contoh, bukan sekadar mengingat istilah.

## Learning outcomes

1. Membuat ERD dengan cardinality dan constraint yang masuk akal.
2. Menjelaskan transaksi, concurrency, dan foreign-key correctness.
3. Mendesain audit append-only dengan model_version.
4. Menguji object-level authorization lintas tenant.

## Pembahasan konsep dan trade-off

### 1. Model konseptual → fisik

Entitas inti: Tenant, User, Inquiry, Prediction, ModelVersion, ReviewEvent dan IngestionBatch. One-to-many: Tenant→Inquiry, Inquiry→Prediction, Inquiry→ReviewEvent. Prediction mengacu ModelVersion supaya hasil historis dapat ditelusuri setelah upgrade. Tentukan arti status dan owned_by. Jangan menggabungkan semua entitas ke satu tabel dengan banyak nullable columns karena mempersulit integrity.

### 2. Constraints sebagai kontrak bisnis

Primary key mengidentifikasi baris; foreign key memastikan relasi sah; UNIQUE(tenant_id, source_event_id) melindungi idempotency; CHECK dapat memvalidasi status dan rentang; NOT NULL menjaga field wajib. Validasi aplikasi memberi feedback cepat, sedangkan DB constraint melindungi dari bug/race dan jalur import lain. Gunakan migration version supaya perubahan schema repeatable.

### 3. Isolation dan lost update

Dua agent dapat mengambil inquiry yang sama. Tanpa version checking, penyimpanan kedua menimpa perubahan pertama. Optimistic lock menambah row version dan update WHERE id=? AND version=?; jika affected_rows=0, return conflict dan tawarkan reload/merge. Transaction memastikan review event dan perubahan status terjadi atomik.

### 4. Object-level authorization dan multi-tenancy

Endpoint /inquiries/{id} harus membatasi WHERE id = ? AND tenant_id = authorized_tenant, bukan hanya memeriksa user login. Gunakan least-privilege DB credentials dan separate permission untuk worker versus agent. Test silang tenant dengan dua organisasi sintetis; jangan menganggap UUID acak sebagai security control.

### 5. Query performance dan indexing

Index tenant_id + created_at mempercepat inbox filter per tenant; indeks semua kolom justru menambah write cost. EXPLAIN dan benchmark perlu data representatif; untuk lab ukur pada sintetis dengan keterbatasan. Simpan query plan dan catat cardinality.

### 6. Backup dan migration evolution

Expand/migrate/contract mengurangi risiko deployment aplikasi v1/v2 bersamaan. Backup restore diuji di instance isolated, khususnya sebelum migration destruktif. Model_version harus survive rollback karena inference lama bisa dipakai untuk menjelaskan keputusan historis.

## Aplikasi dalam AI Customer Intelligence

Pikirkan perubahan berikut: traffic 10 kali lebih tinggi, pelanggan memakai dua tenant, pengguna dapat memasukkan teks tidak tepercaya, dan AI service suatu saat mati. Desain mana yang tetap aman? Apa yang mesti diubah? Tuliskan konsekuensi pada kode, data, UX, keamanan, dan monitoring.

## Bacaan primer

- https://www.postgresql.org/docs/current/ddl-constraints.html
- https://www.postgresql.org/docs/current/transaction-iso.html
- https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md)
