# Applied Energy Case — Batch import dengan retry dan konflik payload

**Status:** worked case untuk belajar; bukan hasil implementasi atau asesmen formal. **Latar:** site dan meter sepenuhnya sintetis.

## Problem

SITE-A/MTR-001/E-1001 mencatat 1.40 kWh. Event yang sama datang lagi persis identik, lalu datang E-1001 dengan nilai berbeda.

## Worked reasoning — mengapa solusinya begitu?

Gunakan composite UNIQUE(site_id,meter_id,source_event_id). Duplikat identik di-skip, duplikat berbeda payload di-reject/quarantine; jangan silently overwrite. Rekonsiliasi accepted+rejected+skipped=received.

## Guided → Independent challenge

**Guided:** ulangi penalaran di atas dan jelaskan setiap asumsi.  
**Faded:** ubah satu angka/aturan lalu tulis ulang satu langkah yang diperlukan.  
**Independent:** Susun dua run input 100 rows dan hitung accepted, rejected, skipped dari status yang mutually exclusive.

## Negative case & security/reliability

SQL injection, oversized CSV, duplicate race dan cross-site confusion.

**Verifikasi yang disyaratkan saat praktik:** positif + negatif, expected vs actual, environment/runtime, test commands, kondisi gagal, dan catatan keterbatasan. Jangan tandai lulus hanya karena membaca contoh.

## Evidence target

Sample batch, SQL migration, test re-import dan summary logs yang disanitasi.

**Kontrak:** [Energy Data Contract](../../docs/architecture/energy-data-contract.md) · [Threat model](../../docs/architecture/threat-model.md) · [Learning gates](../../docs/architecture/energy-learning-gates.md).
