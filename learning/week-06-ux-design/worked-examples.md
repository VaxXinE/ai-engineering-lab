# Worked Examples — UX untuk Dashboard Anomali Energi

Semua skenario ini **ilustratif**; UI belum diimplementasikan.

## Contoh 1 — Pengukuran kWh tidak biasa

**Masalah:** pembacaan MTR-001 pada interval 00.30 menunjukkan 5.9 kWh, sedangkan dua interval sebelumnya 1.40 dan 1.48 kWh. Sistem menandai kandidat anomali, tetapi belum mengetahui apakah hal itu benar-benar kesalahan.

1. Tabel menampilkan meter, timestamp, kWh interval, status **candidate anomaly**, dan versi model.
2. Operator memilih meter dan melihat grafik interval sebelum/sesudah serta catatan kualitas data.
3. Operator boleh memilih `confirmed`, `expected_variation`, atau `needs_investigation`, dengan alasan.
4. Sistem menyimpan review event **tanpa menimpa** nilai pembacaan asli atau prediksi awal.
5. Jika API menolak perubahan, alasan dan pilihan di form tetap ada sehingga operator dapat memperbaiki kesalahan.

**Anti-pattern:** menampilkan 'Sensor rusak' hanya karena satu interval melampaui angka threshold. Nilai tinggi dapat mencerminkan perubahan beban yang valid.

## Contoh 2 — Missing interval dan model timeout

**Masalah:** tidak ada pembacaan 00.45 dan service anomaly scoring tidak tersedia.

1. Grafik membedakan **missing data** dari nilai energi **0 kWh**. Jangan otomatis menggambar garis nol untuk interval hilang.
2. Dashboard menampilkan badge `Scoring unavailable` dan riwayat meter tetap bisa dilihat.
3. Review queue manual tetap dapat digunakan untuk pembacaan yang sudah diterima.
4. Retry dibatasi dan tidak membuat event duplikat; pending action memiliki feedback jelas.
5. Uji keyboard navigation, focus, label, empty/error states dan alur pembatalan.

**Anti-pattern:** mengubah missing interval menjadi nol bisa membuat agregasi konsumsi energi dan model anomali menghasilkan kesimpulan palsu.

## Faded example

Ganti interval 15 menit menjadi satu jam. Jelaskan perubahan pada unit data, agregasi, tooltip, dan perbandingan baseline—tanpa langsung mengganti kWh menjadi kW.

## Independent exercise

Rancang tiga layar: tren site, detail meter, dan review kandidat anomali. Sertakan status loading, missing data, API outage, unauthorized access dan review conflict.

[Deep dive](deep-dive.md) · [Latihan UX](exercises.md).
