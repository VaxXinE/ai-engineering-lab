# Deep Dive — Eksperimen AI yang menolak angka bagus tanpa bukti generalisasi

## Apa yang dapat dibuktikan setelah mempelajari modul?

1. Membedakan train, validation, test dan cross-validation.
2. Menghitung macro F1 dan memahami efek class imbalance.
3. Membuat error taxonomy serta model card.
4. Mendesain quality gate sebelum model diintegrasikan ke API.

## Prinsip desain, mekanisme dan konsekuensi

### 1. Evaluation loop yang disiplin

Definisikan target use case dan risk cost dulu. Train untuk fitting; validation untuk tuning parameter; test untuk evaluasi final. Jangan mencoba banyak model pada test sampai memilih yang paling tinggi, karena test menjadi validation tersembunyi. Gunakan cross-validation jika dataset train kecil, dengan group/time split bila ada hubungan antar device atau urutan waktu.

### 2. Label policy dan inter-annotator quality

Ground truth tidak otomatis benar. Pesan 'Saya mau beli tapi login gagal' mengandung multi-intent; tentukan aturan label: satu priority label atau multi-label output. Dokumentasikan label definitions, contoh borderline, disagreement resolution dan missing context. Data sintetis dapat terlalu bersih dibanding real-world slang dan code switching. Buat taxonomy kesalahan sebelum mencoba fitur tambahan.

### 3. Precision, recall, F1, macro vs weighted

Accuracy tertipu class imbalance. Pada 95% fault messages, model yang selalu menjawab fault tampak 95% akurat namun gagal menemukan normal/warning. Macro F1 memberi bobot sama ke setiap kelas, weighted F1 memberi bobot berdasarkan warning. Ukur per-class recall, precision, confusion matrix dan abstain. Pilih metrik berdasarkan dampak false negative/positive di operasi.

### 4. Probability calibration dan threshold

Normalized scores dari classifier atau softmax tidak selalu menyatakan peluang kebenaran empiris. Perlu calibration curve/reliability diagram dan data validation terpisah. Threshold untuk auto-route/human review harus dievaluasi sebagai coverage vs selective risk, bukan ditentukan dari angka intuitif 0.8 saja.

### 5. Artifact safety dan provenance

Model version, data version, feature schema, code commit, dependency lock serta hash artifact harus dapat ditelusuri. Jangan load pickle/joblib dari sumber tidak dipercaya karena deserialization dapat menjalankan kode. Data poisoning dari contoh berlabel salah perlu diwaspadai; review dataset, protected pipeline, dan evaluation monitoring membantu.

## Checklist penalaran

Ketika suatu solusi terlihat bekerja, tanyakan: (1) apakah hasil benar terhadap kontrak? (2) apakah tetap benar pada data berbeda? (3) apa yang terjadi bila dependency mati? (4) siapa yang berhak melihat/mengubah datanya? (5) bagaimana sistem membuktikan hasil pengujian? Jawab dengan contoh konkret, bukan sekadar kata "best practice".

## Sumber teknis primer

- https://scikit-learn.org/stable/modules/model_evaluation.html
- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/calibration.html

[Worked examples](worked-examples.md) · [Lab](lab-guide.md)
