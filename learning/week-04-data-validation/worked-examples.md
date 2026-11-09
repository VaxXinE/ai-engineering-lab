# Worked Examples — Time-series Data Validation

## 1. Missing interval ≠ zero consumption

Meter MTR-001 interval 15 menit: 00.00=1.40 kWh, 00.15=1.48 kWh, **00.30 hilang**, 00.45=0.00 kWh.

1. Expected slots=4; observed valid unique slots=3 → coverage `3/4=75%`.
2. `00.30` harus direpresentasikan sebagai **missing**, bukan nilai nol.
3. `00.45` memiliki pengukuran **0.00 kWh yang valid** bila field lainnya lulus validasi.
4. Total recorded energy = 1.40+1.48+0 = 2.88 kWh **untuk tiga interval yang terukur**, bukan taksiran konsumsi keempat interval.
5. Chart wajib menunjukkan gap dan label coverage.

## 2. Negative data quality tests

Input: `energy_kwh=NaN`, `Infinity`, `-1`, `interval_minutes=60`, `timestamp='2026-01-01 00:00'`, duplicate `source_event_id`.

- NaN/inf ditolak meskipun beberapa parser menerima format string-nya.
- Negatif ditolak, kecuali nanti skema baru memodelkan produksi/net export secara eksplisit.
- 60 menit ditolak dalam schema v1 15-menit; jangan membandingkan 1.5 kWh per 60m dengan 1.5 kWh per 15m sebagai daya sama.
- Timestamp tanpa offset di-reject supaya tidak menebak zona waktu.
- Duplicate identik di-skip; duplicate berubah payload adalah conflict yang harus diperiksa.

**Leakage counterexample:** rolling baseline untuk 00.30 tidak boleh menghitung data 00.45. Fitur untuk 00.30 hanya boleh memakai interval sebelum 00.30.

[Domain contract](../../docs/architecture/energy-data-contract.md) · [Lab](lab-guide.md).
