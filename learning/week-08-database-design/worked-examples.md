# Worked Examples — Database Energi, Integritas dan Izin Akses

> Potongan SQL berikut ilustratif, belum migration yang dijalankan.

## Contoh 1 — Meter readings dengan constraint dan idempotency

```sql
CREATE TABLE meter_readings (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  site_id TEXT NOT NULL,
  meter_id TEXT NOT NULL,
  source_event_id TEXT NOT NULL,
  measured_at TIMESTAMPTZ NOT NULL,
  energy_kwh NUMERIC(12, 4) NOT NULL CHECK (energy_kwh >= 0),
  voltage_v NUMERIC(8, 2),
  current_a NUMERIC(8, 2),
  UNIQUE (meter_id, source_event_id)
);
```

1. `energy_kwh` adalah konsumsi **per interval**, bukan kW sesaat.
2. `source_event_id` mencegah import berulang menciptakan rows baru untuk meter yang sama.
3. `site_id` mendukung query scoping. **Tabel ini belum memuat FK site/meter**; pada implementasi final, tambahkan referential constraints sesuai model master.
4. Pencarian readings harus memverifikasi `site_id` dari context pengguna di API, bukan menggunakan parameter site bebas dari browser.

**Kesalahan:** hanya memakai uuid acak dan menganggap user tidak bisa menebak ID—itu bukan object-level authorization.

## Contoh 2 — Review kandidat anomali secara aman

1. Operator A dan B membaca anomaly_event dengan `version=3`.
2. A membuat review event dan update status menggunakan kondisi `WHERE version=3`; transaksi commit menaikkan version=4.
3. B mengirim update lama dengan version=3; affected rows=0. Backend mengembalikan conflict (misalnya HTTP 409).
4. UI mempertahankan draft komentar B dan meminta reload, bukan mengganti keputusan A diam-diam.
5. Audit menyimpan model_version, anomaly_score, label review manusia, waktu dan actor.

**Anti-pattern:** mengganti raw `energy_kwh` atau menghapus skor lama setiap kali reviewer menekan simpan. Data sumber dan keputusan manusia harus dibedakan.

## Latihan

Rancang FK site/meter, index pada `(site_id,meter_id,measured_at)`, skema `anomaly_events` dan `review_events`, lalu uji integritas dan cross-site IDOR dalam environment test.
