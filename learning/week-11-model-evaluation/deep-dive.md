# Deep Dive — Mengevaluasi Numeric Energy Anomaly Detection

**Unit pembelajaran pengayaan:** model selection dan evaluation untuk capstone AI Smart Energy Monitoring. Belum ada model numerik yang dijalankan.

## Learning outcomes

1. Mendefinisikan **apa itu kandidat anomali** pada kWh per interval tanpa menganggap nilai tinggi selalu salah.
2. Membandingkan baseline deterministik (misalnya rolling median + IQR) dengan kandidat ML seperti Isolation Forest.
3. Menghindari data leakage ketika data berupa time-series.
4. Menjelaskan perbedaan unsupervised score dan supervised ground truth, serta menulis model card.

## 1. Problem dan variabel

Pada site sintetis, setiap meter mengirim `energy_kwh` (konsumsi **per interval**) dan timestamp UTC. Model mencari interval yang tidak biasa dibanding pola pemakaian meter tersebut. Tetapi energi tinggi bisa mencerminkan aktivitas normal, sehingga **anomaly flag bukan bukti kerusakan**.

Sebelum modeling tetapkan frekuensi interval, holiday/workday simulation, missing data handling, dan apakah setiap meter punya baseline sendiri. Jika data berasal dari rentang interval berbeda, normalisasikan berdasarkan durasi sebelum membandingkan.

## 2. Baseline terlebih dahulu

Baseline sederhana: median consumption pada periode historis sesuai jam dan kondisi, lalu tentukan seberapa jauh pengamatan dari distribusi tersebut. IQR (Q3−Q1) atau robust z-score berguna untuk demonstrasi tetapi threshold harus diuji. Jangan sekadar memasang `kWh > 5` secara universal untuk semua meter tanpa konteks.

## 3. Kandidat ML

Isolation Forest dapat menjadi contoh unsupervised anomaly detection numerik, tetapi **skor anomali bukan probabilitas suatu meter rusak**. ML membutuhkan fitur yang benar, kontrol terhadap data hilang/NaN, serta split waktu yang tidak membocorkan masa depan. Feature engineering dapat mencakup jam, hari, rolling averages **berbasis data sebelumnya**, dan perubahan dibanding baseline.

## 4. Train/validation/test untuk time-series

Gunakan split kronologis train → validation → test. Jangan menghitung rolling statistic pada seluruh set sebelum split jika memanfaatkan periode masa depan. Hindari scaling yang di-fit pada test. Jika banyak meter memiliki profil berbeda, dokumentasikan apakah evaluasi per-meter, per-site, atau cross-site.

## 5. Bagaimana menilai model?

Jika dataset sintetis menyertakan label anomali yang disisipkan generator, boleh hitung precision/recall/F1 berdasarkan **label sintetis itu**. Namun angka tersebut mengukur kemampuan menemukan pola injeksi simulasi, bukan akurasi deteksi kerusakan nyata. Tanpa label, gunakan metrik unsupervised dan expert review yang relevan, serta hindari menyebut F1 secara sembarangan.

Metrik operasional mencakup alert volume, false review burden, data-quality rejection, P95 latency, dan model abstention/unavailable rate.

## 6. Model card dan security

Simpan:
- schema dan unit `energy_kwh` (interval),
- versi generator dan seed,
- split strategy,
- model/feature versions,
- hasil evaluasi per dataset,
- asumsi yang tidak diuji,
- batas penggunaan dan risiko false alerts.

Jangan mengunduh model artifacts yang tidak dipercaya kemudian membuka pickle/joblib tanpa evaluasi provenance—format deserialisasi dapat mengeksekusi kode.

## 7. Transfer ke keputusan engineering

Jika model memberikan skor anomali tinggi untuk satu periode, UI perlu menampilkan kWh, pembanding historis, kualitas data, dan tombol review, **bukan instruksi mengubah perangkat listrik**. Saat model offline, data meter tetap harus tersedia.

[Worked examples](worked-examples.md) · [Casebook](../../docs/domain-casebook.md).

Referensi: [scikit-learn anomaly detection](https://scikit-learn.org/stable/modules/outlier_detection.html), [time-series split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).
