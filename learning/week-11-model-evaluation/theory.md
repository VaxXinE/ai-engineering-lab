# Teori — Evaluation of Numeric Energy Anomaly Detectors (Week 11)

**Outcome:** mengevaluasi baseline robust statistik dan kandidat anomaly model numerik secara time-aware, tanpa mencampurnya dengan text classifier.

## 1. Definisikan anomali secara operasional

Anomali adalah interval yang **tidak biasa relatif terhadap pola pembanding**, bukan bukti pencurian, kerusakan atau bahaya listrik. Contoh 5.90 kWh pada 00:30 bisa wajar jika mesin tertentu mulai bekerja. Kriteria harus didasarkan distribusi historis per meter, weekday/hour patterns dan data quality.

## 2. Baseline vs model

Bandingkan rolling median/IQR yang mudah dijelaskan dengan Isolation Forest, yang menghasilkan ranking berdasarkan isolation-path. **Raw `decision_function` bukan probabilitas**, dan tidak otomatis bisa disamakan dengan skor [0,1]. Adapter harus mendokumentasikan mapping atau gunakan raw score terpisah. LLM teks bukan default scorer untuk angka kWh time-series.

## 3. Time-aware split

Split chronologically train→validation→held-out test. Fitur rolling pada waktu `t` hanya boleh memakai pengamatan sebelumnya; scaler/model fit di train, threshold dipilih validation, test hanya evaluasi final. Bila meter/situs memiliki perilaku berbeda, evaluasi per-meter dan per-site serta coverage—jangan membiarkan satu kelompok dominan menyamarkan kesalahan.

## 4. Metrik sesuai tugas

Jika generator menyisipkan spike dan memberikan label sintetis secara jelas, evaluasi binary anomaly precision, recall, F1, confusion matrix dan alert rate. Tanpa labels, jangan klaim supervised accuracy atau F1 dari ranking unsupervised. Hasil numerik pada simulasi hanya mengukur kemampuan menemukan pola injeksi generator, bukan generalisasi ke sensor lapangan.

## 5. Feature integrity

Validasi `energy_kwh`, `interval_minutes`, UTC, missing slots, outliers, dan duplicate IDs. Jangan imputasi missing menjadi 0 tanpa alasan: bisa membuat model mendeteksi anomali palsu. `voltage_v` dan `current_a` juga contoh simulasi; jangan menyimpulkan keselamatan dengan rumus V×A sederhana.

## 6. Model card dan keamanan

Catat generator seed/version, schema, train/validation/test periods, fitur, baseline, hyperparameter, thresholds, quality metrics, failure cases, artifact hash dan dependency versions. Jangan memuat pickle/joblib yang tidak dipercaya. Kualitas model perlu re-evaluasi ketika data distribution berubah.

**Pemisahan:** Week 01 = supervised klasifikasi catatan teks `normal/warning/fault`; Week 11 = numerical time-series anomaly detection. Keduanya hanya berbagi prinsip evaluasi, bukan label/output model yang sama.

[Numeric deep dive](deep-dive.md) · [Worked examples](worked-examples.md) · [Lab](lab-guide.md).

Referensi: [scikit-learn outlier detection](https://scikit-learn.org/stable/modules/outlier_detection.html), [time-series split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html).
