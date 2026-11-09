# Teori — Data Quality dan Time-series Validation (Week 04)

**Outcome:** menetapkan serta menguji aturan untuk data meter sintetis, dengan definisi data valid, gap, duplikasi, dan leakage yang terukur.

## 1. Enam dimensi kualitas

**Completeness**: interval yang diharapkan tersedia. **Validity**: struktur, numerik, durasi, timestamp tepat. **Uniqueness**: identity event tidak berulang. **Consistency**: relasi meter/site dan satuan konsisten. **Timeliness**: keterlambatan data terhadap target. **Accuracy**: kesesuaian dengan fakta referensi—**tidak** dapat dibuktikan hanya melalui parsing.

## 2. Schema vs business rules

`energy_kwh` wajib finite dan nonnegatif. Nilai **0** bisa valid, berbeda dengan **missing interval**. `interval_minutes` harus 15 dalam versi latihan; data 60 menit tidak boleh diperlakukan sebagai 15 menit. `interval_start_utc` harus offset-aware, UTC, dan align ke slot waktu yang disepakati. `site_id` dan `meter_id` harus terdaftar; authorization dilakukan terpisah ketika API memproses permintaan user.

## 3. Time-series profiling

Per meter/site, hitung expected slots = rentang durasi / interval minutes; observed slots adalah jumlah pengukuran valid dan unik. Contoh: 4 slot diharapkan, 3 tersedia ⇒ coverage 75%, bukan 100% walau tiga row valid. Missing **tidak boleh diisi nol** tanpa aturan imputasi yang terdokumentasi. Jangan mencampur kWh per 15 menit dengan per jam saat membuat histogram.

## 4. Validation pipeline dan quality gate

Parser memeriksa struktur CSV, schema validator memeriksa tipe/range, business validator memeriksa timestamp/relasi, quality reporter mencatat distribusi. Error perlu memiliki kode dan row number, bukan raw sensor payload yang berpotensi sensitif. Quality gate punya threshold yang beralasan dan tindakan reject/quarantine/review—bukan angka 2% yang diklaim standar universal.

## 5. Leakage dan AI

Untuk numeric time-series, split kronologis. Rolling window saat scoring `t` tidak boleh membaca `t+1` atau statistik agregat yang di-fit dari seluruh data. Normalization/scaler perlu di-fit pada training period. Nilai spike sintetis tidak boleh dilabel dari informasi test ketika memilih threshold.

## 6. Security

Batasi file size, row count, max cells, timestamp parsing work, serta hak baca berdasarkan site. Jika data nyata kelak digunakan, metadata meter bisa sensitif sehingga dataset latihan harus tetap fiktif.

**Contoh gagal:** `NaN` dapat lolos beberapa operasi Python floating point meski bukan nilai energi yang sah. Gunakan `math.isfinite` atau finite-number validator yang sesuai.

[Deep Dive](deep-dive.md) · [Praktikum](lab-guide.md) · [Domain contract](../../docs/architecture/energy-data-contract.md).

Referensi: [Pydantic validators](https://docs.pydantic.dev/latest/concepts/validators/), [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html).
