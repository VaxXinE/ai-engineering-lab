# Deep Dive — Model data yang mencegah kehilangan historis prediksi dan celah akses

**Target:** setelah modul, lo dapat mempertahankan pilihan desain melalui contoh dan kontra-contoh, bukan sekadar mengingat istilah.

## Learning outcomes

1. Membuat ERD dengan cardinality dan constraint yang masuk akal.
2. Menjelaskan transaksi, concurrency, dan foreign-key correctness.
3. Mendesain audit append-only dengan model_version.
4. Menguji object-level authorization lintas tenant.

## Pembahasan konsep dan trade-off

### 1. Model konseptual → fisik

Entitas utama: Site, Meter, MeterReading, IngestionBatch, ModelVersion, AnomalyEvent, ReviewEvent, dan ReviewerMembership. Site→Meter; Meter→MeterReading; MeterReading→AnomalyEvent; AnomalyEvent→ReviewEvent. ModelVersion melekat pada AnomalyEvent agar skor tetap dapat diaudit saat model berubah. Review tidak boleh mengubah `energy_kwh` asli.

### 2. Constraints sebagai kontrak bisnis

Kunci unik ingestion: `UNIQUE(site_id,meter_id,source_event_id)`; meter_id boleh berulang antar-site. Foreign key perlu memastikan meter berada pada site yang dirujuk, `energy_kwh>=0`, `interval_minutes=15` serta waktu UTC pada layer parsing. DB tidak menggantikan pemeriksaan `NaN`/infinity secara eksplisit. Gunakan migration untuk schema evolution dan FK constraints sebagai garis pertahanan race.

### 3. Isolation dan lost update

Dua operator mungkin review AnomalyEvent yang sama, bukan mengedit reading mentah. Gunakan optimistic version pada review state dan insert ReviewEvent dalam transaksi atomik. Jika UPDATE WHERE version=? tidak mengubah baris, balas conflict dan pertahankan draft operator.

### 4. Object-level authorization dan multi-tenancy

Route `/api/v1/sites/{site_id}/meters/{meter_id}/readings` memerlukan authenticated site membership dan verifikasi meter dalam site. Query by-ID juga harus scope by site; UUID tidak menggantikan authorization. Uji SITE-A tidak dapat membaca atau mengubah anomali SITE-B.

### 5. Query performance dan indexing

Untuk time-series, index komposit `(site_id,meter_id,interval_start_utc)` mendukung query rentang waktu per meter; EXPLAIN dan benchmark diperlukan dengan data sintetis representatif. Jangan mengindeks semua kolom tanpa alasan; setiap index meningkatkan biaya storage dan write.

### 6. Backup dan migration evolution

Expand/migrate/contract mengurangi risiko deployment aplikasi v1/v2 bersamaan. Backup restore diuji di instance isolated, khususnya sebelum migration destruktif. Model_version harus survive rollback karena inference lama bisa dipakai untuk menjelaskan keputusan historis.

## Aplikasi dalam AI Smart Energy Monitoring

Pikirkan perubahan berikut: traffic 10 kali lebih tinggi, perangkat memakai dua tenant, pengguna dapat memasukkan teks tidak tepercaya, dan AI service suatu saat mati. Desain mana yang tetap aman? Apa yang mesti diubah? Tuliskan konsekuensi pada kode, data, UX, keamanan, dan monitoring.

## Bacaan primer

- https://www.postgresql.org/docs/current/ddl-constraints.html
- https://www.postgresql.org/docs/current/transaction-iso.html
- https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md)
