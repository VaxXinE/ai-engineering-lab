# Latihan Mandiri — Modul 01

Kerjakan di branch belajar sendiri. Jangan memodifikasi test set untuk meningkatkan nilai metrik.

## A. Analisis metrik (wajib)
1. Berapa sampel train dan test setiap kategori?
2. Mengapa accuracy dan macro F1 berbeda?
3. Kelas mana yang paling sering salah dan mengapa?
4. Apa arti abstention_count?
5. Apakah hasil ini membuktikan model siap production?

**Bukti:** tulis notes/metrics-analysis.md dengan output yang benar-benar dijalankan.

## B. Tambah unit tests (wajib)
- Tambahkan tes input CSV dengan baris kosong / terlalu panjang.
- Tambahkan tes prediksi yang memeriksa label valid dan batas relative_score.

**Bukti:** file test dan log hasil menjalankan test suite.

## C. Error analysis
Pilih satu pesan test yang salah. Jelaskan token mana yang sudah/tidak dikenal, dugaan penyebabnya, dan cara melakukan eksperimen perbaikan tanpa membocorkan test ke data training.

## D. Rule-based vs ML
Ciptakan lima kalimat sintetis baru (typo/slang), lalu bandingkan prediksi manual dan model. Jelaskan kapan rule-based lebih aman/sederhana dan kapan ML lebih relevan.

## E. Human review UX (opsional)
Gambarkan langkah agent melihat prediksi, melakukan koreksi, dan memproses abstain. Jelaskan efeknya pada API/DB yang akan dibangun kemudian.

## Rubrik refleksi
- **Konsep:** bisa menjelaskan ML, training, inference, evaluation vs rules.
- **Praktik:** menjalankan dan menjelaskan kode, bukan hanya menyalin output.
- **Evaluasi:** membaca confusion matrix dan false positives/negatives.
- **Keamanan:** tidak ada data asli/secrets dan batas prototype dinyatakan.
- **Bukti:** menyimpan catatan keputusan, hasil uji, dan kekurangan.

Starter code yang sudah lolos test **bukan bukti bahwa latihan personal sudah dikerjakan**.
