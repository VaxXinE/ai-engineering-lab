# Data Sintetis — Catatan Kejadian Perangkat Energi

Skema CSV: `text,label`. Semua contoh ditulis untuk latihan; tidak berasal dari sensor fisik atau kejadian operasional.

| File | Jumlah | Distribusi |
| --- | --- | --- |
| train.csv | 54 | 18 normal, 18 warning, 18 fault |
| test.csv | 18 | 6 normal, 6 warning, 6 fault |

Kategori:
- **normal:** catatan sintetis tentang pengukuran stabil.
- **warning:** catatan perubahan konsumsi/arus/tegangan.
- **fault:** catatan gangguan perangkat dan telemetri.

Teks hanya merupakan **deskripsi status simulator**, bukan pengukuran angka kWh. Capstone energi akan memakai CSV numerik sendiri.

Split tetap dan jumlah sangat kecil: **tidak representatif untuk model produksi**. Jangan gunakan catatan perangkat yang memuat identitas lokasi/infrastruktur nyata tanpa hak.
