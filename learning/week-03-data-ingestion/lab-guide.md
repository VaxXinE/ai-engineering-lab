# Praktikum Terstruktur — Ingestion CSV pembacaan meter 15 menit

**Status:** tugas **direncanakan**; implementasi Week 03–12 belum dijalankan. Semua input, site, meter dan timeseries adalah sintetis.

## Problem dan konteks profesional

Generator menghasilkan 100 rekaman sintetis SITE-A/MTR-001. File mungkin diproses ulang setelah worker timeout, mungkin berisi dua source_event_id yang sama tetapi payload berbeda.

**Single source of truth:** [kontrak domain](../../docs/architecture/energy-data-contract.md) · [threat model](../../docs/architecture/threat-model.md). Jangan mencampur kontrak klasifikasi log teks Week 01 dengan data anomaly scoring numerik Week 11–12.

## Langkah yang akan diimplementasikan saat sesi praktik

1. Definisikan schema CSV **8 kolom** sesuai [domain contract](../../docs/architecture/energy-data-contract.md): site_id,meter_id,source_event_id,interval_start_utc,interval_minutes,energy_kwh,voltage_v,current_a.

2. Buat generator deterministik dengan seed; gunakan meter/site fiktif dan timeline UTC 15 menit. Jangan mengubah kWh menjadi kW tanpa durasi.

3. Parser membatasi bytes/rows, memvalidasi header/encoding dan menolak kolom tambahan, empty ID, atau payload tidak valid. Gunakan test fixtures kecil dahulu.

4. Design transaction dan constraint UNIQUE(site_id,meter_id,source_event_id); identitas sama dengan payload sama ⇒ skipped; identitas sama dengan payload berbeda ⇒ conflicting duplicate yang ditolak.

5. Uji import ulang tiga kali, sekaligus error partial row dan rollback; rekonsiliasi received=accepted+rejected+skipped.

6. Catat counts, batch_id, schema_version, checksum dan error categories tanpa membocorkan token/metadata sensitif.

## Acceptance criteria (belum dicentang)

- [ ] Re-import batch identik tidak menambah record.
- [ ] Duplikat dengan payload berbeda ditolak, bukan overwrite.
- [ ] Site-A dan Site-B tetap terpisah meski source_event_id mirip.
- [ ] Parameterized query mencegah SQL injection; file size/rows terbatas.

## Evidence yang harus dibuat

Data dictionary, generator, parser/importer, migration constraint, retry tests, import summary JSON.

Saat praktik: catat input sintetis, expected behavior, actual output, command+versi runtime, error/negative tests, keamanan, dan link commit. Jangan mengarang skor model, latency, atau status passed.

## Pertanyaan transfer

Apa yang berubah jika interval data datang tidak berurutan atau sebagian event hilang?

**Definition of done:** seluruh acceptance criteria diverifikasi dengan artefak sendiri, bukan sekadar dokumentasi ini; status BNSP tetap memerlukan asesmen resmi LSP.

[Latihan](exercises.md) · [Knowledge check](knowledge-check.md) · [Evidence matrix](../../certification/evidence-matrix.md)
