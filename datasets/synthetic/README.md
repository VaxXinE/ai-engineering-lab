# Synthetic Energy Data

Semua data dalam project harus **sintetis dan bisa direproduksi**. Jangan memakai dataset meter gedung nyata, alamat site asli, atau identitas penghuni.

## Dataset yang direncanakan

- `meter_readings.csv`: `site_id,meter_id,source_event_id,interval_start_utc,interval_minutes,energy_kwh,voltage_v,current_a`.
- `anomaly_labels.csv` (opsional): ground-truth sintetis untuk evaluasi model.
- `device_events.csv`: catatan kejadian simulasi (untuk latihan text classifier Modul 1).

Generator dataset nanti perlu mencatat seed, interval pengukuran, asumsi pola musiman, injeksi outlier, field missing, dan licensing. Jangan mengklaim anomali injeksi sama dengan kejadian listrik nyata.

**Belum ada dataset numerik yang dihasilkan.** Dataset teks Module 01 ada di folder modul tersebut.

## Data hygiene

- Finite non-negative kWh per interval, interval_start_utc dengan UTC serta interval_minutes=15 dan composite key unik (site_id,meter_id,source_event_id).
- Input malformed atau duplikat harus diproses sesuai reject/quarantine policy.
- Jangan mengisi missing interval dengan angka acak tanpa aturan yang terdokumentasi.
- Train/test numerical anomaly split harus mempertimbangkan time leakage.

Lihat [data dictionary dan unit](../../docs/architecture/energy-data-contract.md). Belum ada generator numerik yang dieksekusi.
