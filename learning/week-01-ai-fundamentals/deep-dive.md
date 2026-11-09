# Deep Dive — Memahami AI sebagai komponen sistem, bukan kotak ajaib

> Materi lanjutan untuk pembaca yang sudah memahami software engineering dasar. **Contoh hitungan adalah ilustrasi**, bukan hasil pengujian sistem production.

## Learning outcomes yang harus bisa dibuktikan

1. Membedakan rule-based, supervised ML, deep learning, dan LLM melalui contoh yang tidak ambigu.
2. Menjelaskan tiap tahap dataset → training → inference → evaluation tanpa memakai data test untuk tuning.
3. Menghitung precision, recall, F1 dari confusion matrix kecil dan menyimpulkan failure cost.
4. Memilih fallback human review ketika input di luar cakupan model.

## Penjelasan konsep secara mendalam

### 1. Mulai dari keputusan bisnis, bukan pemilihan model

Bayangkan 100 pesan masuk lewat live chat tiap jam. Tujuan bisnisnya bukan 'memakai AI', melainkan menekan waktu triase tanpa mengorbankan customer yang butuh support. Identifikasi input (teks pesan), output (sales/support/general atau abstain), aktor (agent), biaya kesalahan, dan cara membandingkan dengan proses manual. Klasifikasi otomatis bisa saja tidak layak jika volume terlalu kecil atau kelas ambigu. Jika masalah selesai dengan tiga aturan yang stabil dan mudah diaudit, AI/ML bukan kewajiban teknis. Sebelum memilih model, tulis baseline business KPI dan error budget yang bisa diterima.

### 2. AI, ML, Deep Learning, LLM dan relasinya

AI adalah payung metode untuk menyelesaikan tugas seperti klasifikasi dan perencanaan. ML belajar parameter dari contoh berlabel atau tak berlabel. Supervised classification menggunakan input dan label target; unsupervised clustering tidak punya label kebenaran yang sama. Deep Learning menggunakan jaringan neural bertingkat, berguna untuk pola kompleks tetapi memerlukan lebih banyak resource dan evaluasi. LLM adalah model bahasa besar yang sering digunakan untuk menghasilkan atau mengekstrak teks; LLM tidak wajib untuk klasifikasi intent. Rule-based memakai keputusan eksplisit developer; hasilnya deterministik untuk input yang sama, tetapi rapuh terhadap variasi bahasa.

### 3. Training versus inference versus evaluasi versus deployment

Training mengestimasi parameter model dari data pelatihan; inference memakai model tetap untuk input baru; evaluation menghitung performa pada contoh yang tidak digunakan selama training; deployment menjalankan model dalam sistem dan mengelola kegagalannya. Keempat tahap memiliki risiko berbeda. Contoh: training berhasil bukan bukti inference cepat; inference menghasilkan JSON valid bukan bukti kategori benar; accuracy tinggi pada dataset sintetis bukan bukti performa pada chat produksi. Pada integrasi API, model inference tidak boleh memutuskan izin akses ke resource.

### 4. Representasi teks dan asumsi Naive Bayes

Model Week 01 mengubah teks menjadi token kata dan frekuensi per label. Multinomial Naive Bayes mengasumsikan kontribusi token bersifat kondisional independen terhadap kelas; asumsi ini sering tidak benar secara linguistik, tetapi algoritmanya cepat dan berguna sebagai baseline. Laplace smoothing memberi kemungkinan non-nol untuk token yang belum pernah muncul pada suatu kelas. Token di luar vocabulary tidak memberi informasi dalam implementasi dasar; semua token baru menghasilkan abstain. Konsekuensinya, istilah slang, ejaan typo atau code switching perlu diukur sebagai domain shift.

### 5. Memahami matriks kesalahan secara bisnis

Precision menjawab 'dari yang diprediksi support, berapa benar support?', recall menjawab 'dari seluruh support asli, berapa berhasil ditemukan?'. F1 menggabungkan keduanya dengan harmonic mean. Confusion matrix penting karena kesalahan support→general beda dampaknya dari general→sales. Bila input sering ambigu, sistem harus menyediakan abstention/manual review. Relative score keluaran Naive Bayes merupakan normalisasi skor model, bukan confidence yang terkalibrasi; jangan menyatakan '99% pasti benar'.

### 6. Menjaga kualitas eksperimen

Pisahkan data train dan held-out test; test sebaiknya hanya untuk evaluasi akhir. Jika setelah melihat hasil test kita berkali-kali mengubah stopwords, fitur dan threshold agar angka meningkat, test secara tidak langsung menjadi validation set. Gunakan validation data atau cross-validation saat tuning, lalu satu evaluasi final. Lakukan pemeriksaan duplikat teks dan, untuk data nyata, mempertimbangkan group split berdasarkan customer agar pesan mirip dari orang yang sama tidak menipu metrik. Data sintetis kecil hanya cocok untuk membuktikan alur, bukan mengukur generalisasi.

## Miskonsepsi yang perlu diwaspadai

- LLM selalu lebih pintar untuk semua tugas → salah; kualitas, biaya, kontrol, privasi dan ukuran masalah menentukan pilihan.
- Training accuracy bukan production accuracy → data bisa berbeda dan test leakage membuat angka terlalu optimistis.
- Confidence tinggi bukan kepastian → relatif score atau softmax bisa miscalibrated.
- Tidak ada error HTTP berarti model benar → valid JSON bisa memuat prediksi salah.
- Data sintetis tidak perlu diuji privasinya → tetap jangan mencampur potongan chat nyata.

## Transfer ke profesi full-stack

Ambil satu kebutuhan dari capstone [AI Customer Intelligence](../../projects/ai-customer-intelligence/README.md). Jelaskan **data apa yang tepercaya, aturan bisnis mana yang harus deterministik, apa yang bisa diprediksi AI, bagaimana failure ditangani, dan bagaimana keputusan diuji**. Jangan menyatakan modul selesai hanya dengan menyalin contoh.

## Bacaan lanjutan (dokumentasi dan pembelajaran primer)

- https://developers.google.com/machine-learning/crash-course
- https://scikit-learn.org/stable/modules/naive_bayes.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md) · [Lab](lab-guide.md)
