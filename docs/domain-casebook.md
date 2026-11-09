# Casebook — AI Smart Energy Monitoring

**Satu use case utama untuk seluruh 16 modul.** Ini adalah proyek software engineering dengan **data meter listrik sintetis**, bukan produk yang memantau instalasi gedung nyata.

## Problem framing

Dataset meter yang tidak terkontrol bisa memuat timestamp hilang/duplikat, nilai kWh tidak valid, serta lonjakan konsumsi yang tidak jelas apakah variasi normal atau perlu investigasi. Kita ingin menggabungkan **data quality + AI anomaly detection + dashboard review + AI operations**.

### Definisi teknis

- `energy_kwh` = energi digunakan **selama interval tertentu**; tidak sama dengan daya sesaat `kW`.
- `timestamp` = awal interval dalam UTC. Interval harus diketahui (misalnya 15 menit).
- `site_id` + `meter_id` = pembatas akses dan identitas meter sintetis.
- `source_event_id` = identitas sumber untuk mencegah duplicate ingest.
- `voltage_v` dan `current_a` adalah fitur simulasi, bukan verifikasi kualitas suplai listrik nyata.

### Contoh data input sintetis

```csv
site_id,meter_id,source_event_id,timestamp,energy_kwh,voltage_v,current_a
SITE-A,MTR-001,E-1001,2026-01-01T00:00:00Z,1.40,230.0,6.0
SITE-A,MTR-001,E-1002,2026-01-01T00:15:00Z,1.48,230.5,6.3
SITE-A,MTR-001,E-1003,2026-01-01T00:30:00Z,5.90,228.7,8.2
```

**Catatan:** Baris ketiga mempunyai nilai energi lebih tinggi, tetapi **belum bisa dipastikan sebagai anomali** tanpa baseline musiman/konteks serta ground truth. Jangan mencampur data interval 15 menit dengan 1 jam tanpa normalisasi.

## Pemetaan modul ke fitur nyata

| Minggu | Praktik domain | Evidensi yang direncanakan |
| --- | --- | --- |
| 01 | Klasifikasi catatan kejadian perangkat teks: normal/warning/fault | CLI, metrics, error analysis |
| 02 | Bandingkan heuristik statistik, Isolation Forest, dan opsi lain secara objektif | Decision matrix, ADR |
| 03 | Import CSV meter sintetis dengan stable source_event_id | Idempotent ingestion report |
| 04 | Validasi finite numeric values, unit, timestamp, duplikat, missing interval | Data quality checks dan test report |
| 05 | Aggregation per meter, sliding window, top-N energy intervals | Complexity analysis + tests |
| 06 | Rancang dashboard tren, anomaly review, filter site/meter | User journey + wireframe |
| 07 | Implementasi grafik dan event status empty/loading/error | UI components + accessibility tests |
| 08 | ERD site, meter, reading, model_version, anomaly_event, review_event | Migration + authorization tests |
| 09 | API/readings, anomaly service adapter, audit/observability | Architecture + API contracts |
| 10 | Query time-range, retention, batch inference dan load test | Scalability report |
| 11 | Baseline IQR/z-score vs model anomaly detection pada data sintetis | Evaluation report + model card |
| 12 | Integrasi anomaly scoring pada API, output validation, safe fallback | Integration/contract tests |
| 13 | Container API/DB/dashboard + reproducible setup | Install and smoke tests |
| 14 | Monitor data drift, false alerts, service latency, backup plan | Maintenance plan |
| 15 | Simulasi inference outage, rollback, dan DB restore isolated | Incident/restore report |
| 16 | Bukti mapping ke kompetensi dua skema LSP | Portofolio dan mock assessment |

### Dua teknik AI, dua tujuan

**Modul 1** adalah supervised *text classification* dari catatan simulator untuk memahami training/inference/F1. **Capstone Week 11–12** berfokus pada *numerical anomaly detection* dari data meter per interval. Kedua teknik **tidak boleh disamakan**, terutama cara evaluasi dan data yang dibutuhkan.

## AI risk boundary

- **Anomaly candidate** tidak berarti telah ditemukan kerusakan listrik atau pencurian energi.
- Tindakan terhadap perangkat listrik tidak boleh dijalankan otomatis dari keluaran model.
- Model tidak memutuskan siapa boleh melihat data suatu site.
- Data latih/test sintetis yang kecil tidak cukup untuk klaim generalisasi.
- Metrik seperti F1 hanya bermakna bila tersedia label ground truth yang jelas, walaupun sintetis.

**Status:** domain casebook siap; fitur numerik belum diimplementasikan. Semua tests harus dijalankan selama praktikum sebelum status berubah.
