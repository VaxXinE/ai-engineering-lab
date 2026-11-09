# Teori — Data Ingestion Meter Listrik (Week 03)

**Outcome:** mampu merancang ingestion idempotent untuk pembacaan kWh per 15 menit, lengkap dengan schema, transaction boundaries, dan rekonsiliasi batch. Baca [kontrak domain](../../docs/architecture/energy-data-contract.md) sebelum melihat contoh SQL.

## 1. Kontrak input

Setiap row adalah **satu pengukuran satu meter dalam satu interval**, bukan pesan teks. Delapan kolom: `site_id,meter_id,source_event_id,interval_start_utc,interval_minutes,energy_kwh,voltage_v,current_a`. Tipe, satuan, durasi dan UTC wajib dipastikan saat import. Versi skema yang berubah harus dicatat.

## 2. ETL vs ELT

ETL: validasi dan transform sebelum masuk tabel target. ELT: simpan dulu ke staging dengan akses dan retensi terkendali lalu transform. Untuk latihan, ETL dengan ringkasan reject cukup. Staging bermanfaat untuk forensic/replay tetapi memperbesar permukaan penyimpanan data yang belum tervalidasi.

## 3. Event identity vs measurement time

Kunci idempotency: **(site_id,meter_id,source_event_id)**. Dua site boleh memakai nama meter sama. File import dua kali seharusnya tidak menggandakan row. Payload duplikat dengan hash sama ⇒ skipped; payload berbeda pada key sama ⇒ **conflicting duplicate** yang perlu quarantine. Timestamp interval yang sama dengan source ID berbeda juga butuh kebijakan konflik (misalnya satu accepted reading per slot dengan history koreksi).

## 4. Transactions dan concurrency

Gunakan parameterized SQL dan database constraint, bukan sekadar cek sebelum insert yang rentan race. Batch atomic lebih sederhana untuk dataset kecil; partial accept memerlukan log per-record dan rekonsiliasi `received = accepted + rejected + skipped`. Ketika worker crash setelah commit tetapi sebelum ack, retry harus konsisten.

## 5. Security dan operasional

Batasi ukuran berkas, jumlah row dan panjang cell; tolak kolom tak dikenal, nilai NaN/inf/negatif, encoding salah, atau path traversal pada upload. Ekspor CSV perlu mitigasi formula injection jika data berupa teks yang dapat dikontrol user. Catat batch ID, checksum, jumlah status dan alasan error **tanpa menuliskan kredensial**.

## Worked reasoning

Jika ada 100 rows, 90 diterima, 7 ditolak dan 3 skipped, acceptance rate = 90/100 = 90%. Saat file sama dimasukkan ulang, row existing tetap; exact duplicates menjadi skipped. Jangan menebak 90 rows accepted pada percobaan kedua.

[Worked examples](worked-examples.md) · [Praktikum](lab-guide.md) · [Kontrak energi](../../docs/architecture/energy-data-contract.md).

Referensi: [Python CSV](https://docs.python.org/3/library/csv.html), [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html), [OWASP SQL injection](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
