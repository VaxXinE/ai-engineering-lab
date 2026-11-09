# Worked Examples — Reliable Energy CSV Ingestion

**Status:** worked reasoning, bukan bukti kode importer sudah dijalankan.

## 1. Conflict-safe idempotent import

**Data:** SITE-A/MTR-001 mengirim E-1001 pada 00.00 dengan `energy_kwh=1.40`.

1. Impor pertama: accepted 1, `UNIQUE(site_id,meter_id,source_event_id)` mencegah duplicate identity.
2. Impor ulang **identik**: skipped 1, accepted 0, seluruh nilai asli tidak berubah.
3. Impor ulang dengan E-1001 tetapi `energy_kwh=9.99`: **conflicting duplicate**, rejected/quarantined; jangan menimpa pembacaan asli.
4. SITE-B/MTR-001/E-1001: identity lain, dapat diterima karena site berbeda.
5. Database uniqueness harus ditegakkan dalam transaksi. Check-before-insert saja masih rentan race antara dua worker.

Contoh SQL ilustratif setelah skema dibuat:

```sql
INSERT INTO meter_readings (site_id,meter_id,source_event_id,interval_start_utc,interval_minutes,energy_kwh)
VALUES ($1,$2,$3,$4,15,$5)
ON CONFLICT (site_id,meter_id,source_event_id) DO NOTHING;
```

**Catatan penting:** `DO NOTHING` sendiri **tidak** membedakan payload duplicate identik vs konflik; aplikasi harus membandingkan payload atau hash saat konflik dan melaporkan sesuai kebijakan.

## 2. Rekonsiliasi batch

100 events: 91 accepted, 6 schema-invalid dan 3 exact duplicates ⇒ `91+6+3=100`. Acceptance 91%, reject 6%, skipped 3%. Bila row yang sama ditandai invalid **dan** duplicate, tentukan satu status final supaya total tidak dihitung ganda. Jika batch diulang, hasil accepted akan berubah meski total input tetap 100.

**Negative test:** NaN/inf/negative kWh dan timestamp tanpa timezone ditolak; string yang dikirim ke SQL tidak boleh di-concatenate.

[Canonical CSV](../../docs/architecture/energy-data-contract.md) · [Praktikum](lab-guide.md).
