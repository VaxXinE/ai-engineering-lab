# Teori — Model Evaluation, Error Analysis & AI Quality Gates

**Hasil belajar:** Mengembangkan baseline text classifier dan mengukur kualitas hasil secara disiplin sebelum mengintegrasikannya ke API.

## 1. Model lifecycle dan baseline

Mulai dari rule-based dan Naive Bayes Week 01 sebagai baseline. Model baru dinilai lebih baik jika melampaui baseline pada metrik yang relevan dan biaya yang dapat diterima. Jangan memperumit dengan deep learning atau LLM tanpa evidence; evaluasi penggunaan pretrained model versus training ulang berdasarkan data yang tersedia.

## 2. Data splitting dan experimental discipline

Pisahkan train/validation/test: train untuk fitting, validation untuk hyperparameter selection, test sebagai evaluasi final. Data kecil mudah overfit dan noisy; gunakan cross-validation pada train/validation, lalu satu held-out evaluation. Group split diperlukan bila pesan dari customer yang sama berkorelasi; time split bila perilaku berubah dari waktu ke waktu.

## 3. Metrics beyond accuracy

Pada tiga kelas, lihat precision dan recall per class, macro F1, confusion matrix serta abstention/rejection rate. Cost-sensitive decisions bisa memprioritaskan support recall jika salah menyalurkan komplain mahal. Calibration dibutuhkan bila skor akan ditampilkan sebagai probabilitas; jangan mengubah softmax score menjadi jaminan.

## 4. Error taxonomy dan model card

Kelompokkan kesalahan menjadi keyword ambiguity, typos, novel vocabulary, mixed intent, label noise, dan drift. Simpan model version, data source, split method, metric, limitations dan intended use. Hindari menyimpan example text sensitif dalam artifact publik.

## 5. Safety dan model artifact provenance

Data poisoning dapat muncul dari data tidak tepercaya. Jangan deserialize pickle/joblib dari sumber asing di production tanpa trust; format ini dapat menjalankan kode. Validasi provenance model artifact, dependency version, file hash dan permission storage. Benchmark kualitas tanpa threat model belum cukup untuk deploy.

## Skenario rekayasa perangkat lunak

Model Week 01 menghasilkan 77.78% accuracy pada hanya 18 sampel sintetis. Evaluasi lanjutan perlu memperluas data dan memisahkan validation dari test, bukan mengulang banyak perubahan sampai 18 sampel tersebut cocok.

## Prinsip dan acceptance criteria

- Model dievaluasi pada set yang tidak digunakan untuk train/tuning.
- Metrik yang dipilih berhubungan dengan dampak bisnis salah klasifikasi.
- Semua hasil yang dilaporkan benar-benar diukur dan dapat direproduksi.
- Model card menyebut limitasi data sintetis dan risiko domain shift.

## Dokumentasi primer untuk pendalaman

- https://scikit-learn.org/stable/modules/cross_validation.html
- https://scikit-learn.org/stable/modules/model_evaluation.html
- https://scikit-learn.org/stable/common_pitfalls.html

Penjelasan ini mengaitkan materi praktik dengan unit yang dipublikasikan LSP. Ini bukan reproduksi KUK resmi dan tidak menentukan hasil asesmen.

[Praktikum](lab-guide.md)