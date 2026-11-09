# Worked Examples — Evaluasi Model Anomali Energi

Semua perhitungan berikut merupakan **contoh numerik**, bukan hasil pelatihan model pada dataset nyata.

## Contoh 1 — Accuracy 95% yang menyesatkan

**Dataset simulasi:** 1.000 pembacaan meter, 950 diberi label normal dan 50 disisipkan sebagai anomali sintetis.

Model yang **selalu menjawab normal**:
1. Accuracy = 950/1000 = **95%**.
2. Recall anomali = 0/50 = **0%**, karena tidak satu pun anomali terdeteksi.
3. Precision anomali = 0 (konvensi ketika tidak ada prediksi positif).
4. F1 untuk kelas normal = 2×0.95×1/(0.95+1) ≈ **0.9744**.
5. Macro F1 biner ≈ (0.9744 + 0)/2 = **0.4872**.

**Kesimpulan:** sistem tidak berguna untuk menemukan anomali meski accuracy terlihat tinggi. Gunakan recall anomali, precision, false-alert burden, dan konteks biaya kesalahan.

## Contoh 2 — Evaluasi IQR vs Isolation Forest

1. Buat dataset **sintetis dengan seed**, interval 15 menit, pola hari kerja dan injected spikes.
2. Split **berdasarkan waktu**, bukan random shuffle yang dapat membocorkan data masa depan.
3. Fit scaler, IQR baseline dan model ML pada **train**; tuning pada validation.
4. Evaluasi sekali pada held-out test dan bandingkan precision, recall, F1 anomali dan volume alert.
5. Buat model card yang menyatakan data simulasi, metode injeksi anomali, fitur, hyperparameters, dan limitasi.
6. Ketika tidak memiliki ground truth yang jelas, jangan mengklaim F1 dari skor unsupervised saja.

**Anti-pattern:** memilih threshold setelah melihat setiap label test hingga semua kasus benar, lalu mengklaim generalisasi.

## Tugas transfer

Bagaimana jika sebuah meter hanya aktif pada jam kerja dan meter lain aktif 24 jam? Jelaskan kenapa global threshold bisa menghasilkan banyak false positives.
