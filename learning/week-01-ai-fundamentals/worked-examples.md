# Worked Examples — Memahami AI sebagai komponen sistem, bukan kotak ajaib

Contoh ini diselesaikan langkah demi langkah. Bacalah **sebelum** mengerjakan latihan, lalu tutup dokumen dan ulangi reasoning dari awal. Tidak ada klaim eksekusi kode/tes baru pada file ini.

## Contoh 1: Menghitung metrik dari 10 data support

**Masalah:** Ada 10 pesan yang sebenarnya support. Model menandai 8 pesan sebagai support; 6 di antaranya benar, 2 ternyata general. Empat pesan support lainnya salah label.

**Solusi dan reasoning:**

1. TP=6, FP=2, FN=4. Precision = 6/(6+2) = 0.75.
2. Recall = 6/(6+4) = 0.60. F1 = 2*(0.75*0.60)/(0.75+0.60) = 0.6667.
3. Kesimpulan: meski precision cukup tinggi, model gagal mengenali 40% komplain. Ini dapat lebih berbahaya daripada angka accuracy global terlihat.
4. Jika salah melewatkan keluhan lebih mahal daripada false alert, prioritaskan recall support dan human review untuk status ambigu.

**Counterexample / failure mode:** Kesalahan umum: memakai FN=2 karena keliru menganggap FP dan FN sama; atau menyimpulkan accuracy dari hanya metrik satu kelas.

**Self-explanation:** Mengapa langkah kedua diperlukan? Apa konsekuensi jika constraint-nya berubah?

## Contoh 2: Mendesain pipeline tanpa kebocoran data

**Masalah:** Ada 72 pesan sintetis: 54 train dan 18 test seperti Week 01. Developer ingin menyetel threshold abstain agar semua 18 test benar.

**Solusi dan reasoning:**

1. Tentukan terlebih dahulu aturan split. Train dipakai fitting, validation set untuk pemilihan hyperparameter; test tidak ikut tuning.
2. Buat baseline rule-based dan Naive Bayes. Bandingkan pada validation dan catat perubahan parameter serta alasannya.
3. Setelah desain dibekukan, jalankan held-out test satu kali dan tulis confusion matrix serta error cases.
4. Jika hasil test mengecewakan, jangan diam-diam mencampur test ke train. Catat limitation dan rancang evaluasi baru dengan sampel yang berbeda.

**Counterexample / failure mode:** Contoh buruk: menyusun daftar keyword dengan membaca setiap pesan test sampai semuanya berhasil, kemudian mengklaim generalization tinggi.

**Self-explanation:** Mengapa langkah kedua diperlukan? Apa konsekuensi jika constraint-nya berubah?


## Progressive practice

- **Guided:** ulangi kedua solusi dan cek nilai/langkah satu per satu.
- **Faded:** ubah satu input atau constraint sendiri, lalu hitung atau rancang ulang solusi.
- **Independent:** terapkan pola pada kasus baru dan catat alternatif serta risiko yang belum tertutup.
- **Verification:** untuk kode, jalankan test sendiri; untuk hitungan, cek ulang dengan perhitungan independen.

[Lanjut knowledge check](knowledge-check.md) · [Latihan utama](exercises.md)
