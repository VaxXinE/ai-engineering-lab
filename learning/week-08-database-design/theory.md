# Teori — Database Time-Series, Anomaly dan Audit (Week 08)

**Outcome:** membuat model data per site dan meter yang konsisten, idempotent, audit-friendly, dan aman terhadap IDOR/BOLA.

## 1. Logical entities

`Site` memiliki banyak `Meter`; setiap `Meter` menghasilkan `MeterReading`; setiap reading dapat dinilai beberapa kali sehingga mempunyai banyak `AnomalyEvent` berdasarkan `ModelVersion`. `ReviewEvent` menyimpan keputusan manusia atas kandidat anomali. `IngestionBatch` melacak proses import. Keputusan review **bukan** atribut yang mengganti nilai energi.

## 2. Key dan constraints

Kunci pembacaan: `(site_id,meter_id,source_event_id)`. Jika meter_id hanya unik dalam site, FK perlu komposit `(site_id,meter_id)`. Data `energy_kwh` adalah finite dan >=0, `interval_minutes=15` untuk v1, UTC dan aligned; parsers harus menolak NaN/inf sebelum persist. `UNIQUE` mencegah concurrency race; application validation memberikan error feedback yang lebih jelas.

## 3. Query scoping

`GET /api/v1/sites/{site_id}/meters/{meter_id}/readings` wajib memeriksa bahwa authenticated principal punya membership pada site, dan meter memang berada dalam site tersebut. Jangan membangun authorization dari `site_id` yang dikirim client tanpa verifikasi. Negative test: user Site-A mengetahui meter ID Site-B tetap tidak boleh melihat data.

## 4. Transactions dan audit

Simpan perubahan status review dan `ReviewEvent` dalam satu transaction. Pakai optimistic locking jika dua operator menyunting review bersamaan: `WHERE version=?`, dan saat affected_rows=0 tampilkan conflict. Audit harus append-only untuk mempertahankan skor, model_version, siapa dan kapan keputusan dibuat.

## 5. Index dan performance

Query grafik sering memakai filter site,meter,interval_start_utc. Pertimbangkan index `(site_id,meter_id,interval_start_utc)` dan uji via EXPLAIN pada data sintetis, bukan indeks semua kolom. Retention dan downsampling perlu menjaga arti kWh per interval dan tidak menghilangkan audit penting.

## 6. Safe migration

Migration harus versioned, diuji di database isolated, dan menjaga backward compatibility saat rollback. Backup dan restore memerlukan uji integritas data, bukan sekadar status proses selesai.

[ERD contract](../../docs/architecture/energy-data-contract.md) · [SQL worked example](worked-examples.md) · [Lab](lab-guide.md).

Referensi: [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html), [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html), [OWASP BOLA](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/).
