# Requirements — AI Smart Energy Monitoring

**Status:** Draft SRS untuk pembelajaran; belum diimplementasikan.

## User stories

1. Sebagai energy analyst, gue bisa mengimpor data meter sintetis dan melihat jumlah valid, rejected, skipped serta alasan penolakan.
2. Sebagai facility operator, gue bisa melihat grafik kWh per meter/time range dan mengetahui saat ada missing interval.
3. Sebagai analyst, gue bisa melihat kandidat anomali dari model beserta versi dan metode baseline pembanding.
4. Sebagai reviewer, gue bisa menandai anomaly sebagai `confirmed_anomaly`, `expected_variation` atau `needs_investigation` dengan alasan yang tercatat.
5. Sebagai maintainer, gue bisa melihat latency/error/status pipeline tanpa mengekspos data pengukuran detail ke log publik.

## Functional requirements

- **FR-01:** CSV dataset dengan field `site_id,meter_id,source_event_id,interval_start_utc,interval_minutes,energy_kwh,voltage_v,current_a`.
- **FR-02:** reject baris invalid sesuai schema dan pencatatan ingestion summary.
- **FR-03:** repeated import yang sama tidak menggandakan pembacaan.
- **FR-04:** dashboard responsive + accessible untuk tren dan tabel anomali.
- **FR-05:** baseline rule-based dan model scoring dengan audit `model_version`.
- **FR-06:** review manual dan audit event append-only.
- **FR-07:** fallback saat inference gagal; data measurement tetap dapat diakses.
- **FR-08:** hanya pengguna dalam site yang diizinkan dapat membaca/mengubah review pada site tersebut.

## NFR dan acceptance tests (direncanakan)

| ID | Kriteria penerimaan | Bukti saat praktik |
| --- | --- | --- |
| AC-01 | Header/units/schema invalid ditolak tanpa mengubah rows existing | Negative import tests |
| AC-02 | Re-import tidak membuat duplicate rows untuk `(site_id,meter_id,source_event_id)` | Integration test |
| AC-03 | `kWh` diperlakukan sebagai interval, bukan counter cumulative | Data dictionary + tests |
| AC-04 | Alert tidak bisa tersimpan dengan model output invalid | Contract tests |
| AC-05 | Site-A tidak dapat membaca Site-B walau tahu ID | IDOR/BOLA tests |
| AC-06 | Saat model timeout, measurement tersimpan dan berstatus scoring_unavailable (reading tetap tersedia) | Failure test |
| AC-07 | Reviewer action tercatat dan tidak menimpa raw prediction | Audit test |
| AC-08 | Restore menghasilkan jumlah data dan relasi yang benar | Restore drill |
| AC-09 | Tidak ada API key, PII, lokasi gedung asli, atau data sensitif di repo | Privacy/code review |

## Out of scope

Meter fisik, smart-grid control, billing, pengendalian kelistrikan, rekomendasi keselamatan, dashboard produksi gedung nyata, dan integrasi sensor tanpa persetujuan.

**Kontrak API, satuan, dan identity:** [Domain Contract](../../../docs/architecture/energy-data-contract.md). Tidak ada endpoint atau fitur dari dokumen ini yang sudah diimplementasikan.
