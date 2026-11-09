# Teori — AI Engineering Fundamentals

## 1. Apa itu AI, ML, DL, dan GenAI?

| Konsep | Makna | Contoh software |
| --- | --- | --- |
| AI | Istilah payung untuk sistem yang menunjukkan kemampuan menyelesaikan tugas cerdas | Pengelompokan pertanyaan customer |
| ML | Subbidang AI yang mempelajari pola dari contoh data | Text classifier yang dilatih dari contoh berlabel |
| Deep Learning | Subbidang ML dengan jaringan saraf berlapis | Model text/image modern |
| Generative AI | Model yang dapat menghasilkan konten baru | Ringkasan chat |
| LLM | Model bahasa skala besar untuk memproses/menghasilkan teks | Chatbot, summarization, extraction |
| Rule-based | Logika eksplisit buatan developer, tidak otomatis merupakan ML | Jika ada kata harga, arahkan ke sales |

**Tidak semua solusi AI butuh LLM.** Untuk tugas yang sederhana dan terstruktur, aturan eksplisit atau model klasifikasi kecil dapat lebih murah, cepat, dapat diaudit, dan mudah dipelihara.

## 2. Training, inference, dan evaluation

- **Training**: algoritma membaca 54 pesan berlabel dan mempelajari distribusi kata setiap kelas.
- **Inference**: model menerima pesan baru lalu memperkirakan label berdasarkan parameter yang sudah dipelajari.
- **Evaluation**: membandingkan prediksi dengan label sebenarnya pada **18 pesan terpisah**, bukan data yang dilatih.
- **Deployment**: menjalankan model sebagai bagian dari aplikasi. Belum dilakukan pada modul ini.

~~~mermaid
flowchart TD
    A[Pesan berlabel] --> B[Train dataset]
    A --> C[Held-out test dataset]
    B --> D[Latih model]
    D --> E[Model terlatih]
    E --> F[Prediksi test]
    C --> G[Label asli]
    F --> H[Hitung metrik]
    G --> H
~~~

**Data leakage** terjadi ketika informasi dari data evaluasi ikut memengaruhi training atau keputusan pemilihan model. Contoh kita memeriksa overlap teks yang sama setelah normalisasi, tetapi **belum** mampu mendeteksi kalimat yang berbeda namun semantik hampir sama.

## 3. Cara kerja Naive Bayes

Input teks diubah menjadi **bag-of-words**, sehingga urutan kata diabaikan. Model menghitung jumlah dokumen per kelas dan frekuensi kata pada setiap kelas.

Untuk setiap kata w dan kelas c, dipakai Laplace smoothing agar kata yang frekuensinya nol tidak mematikan seluruh skor:

~~~text
P(w | c) = (count(w,c) + 1) / (total_kata_di_c + ukuran_vocab)
~~~

Skor setiap kelas dihitung dengan log-probabilities supaya lebih stabil daripada mengalikan bilangan kecil. Label dengan skor tertinggi dipilih, kecuali semua token input tidak dikenal, yang menghasilkan **abstain**.

Skor relatif bukan confidence yang terkalibrasi. Label dan skor bisa tampak meyakinkan tetapi tetap salah, terutama pada data yang berbeda dari data latihan.

## 4. Rule-based vs Machine Learning

Contoh: "berapa harga paket tahunan?"

- **Rule-based**: developer mendefinisikan daftar kata seperti harga, paket, biaya. Tidak ada proses training.
- **ML**: model mencari pola kata dalam data berlabel, lalu mengklasifikasikan contoh baru.
- **LLM**: aplikasi dapat meminta model bahasa memahami intent lalu mengeluarkan label terstruktur, tetapi ada konsekuensi biaya, latency, privasi, dan validasi output.

Minggu ini hanya menerapkan dua pendekatan pertama. Tidak ada API AI eksternal atau model deep learning.

## 5. Accuracy, Precision, Recall, F1

- **TP:** support yang diprediksi sebagai support.
- **FP:** bukan support tetapi diprediksi support.
- **FN:** support tetapi diprediksi kategori lain, termasuk abstain.

~~~text
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
F1        = 2 * Precision * Recall / (Precision + Recall)
Accuracy  = Semua prediksi benar / Semua contoh uji
Macro F1  = Rata-rata F1 dari tiga kelas
~~~

Confusion matrix membantu kita melihat kelas mana yang sering tertukar. Data berimbang dalam latihan ini **tidak mewakili** traffic aplikasi sungguhan. Accuracy tinggi pada data kecil tidak berarti model layak produksi.

**Trade-off bisnis:** salah mengirim keluhan ke sales dapat memperlambat support; salah mengirim lead ke general dapat menunda follow-up. Karena itu hasil AI memerlukan evaluasi berdasarkan dampak kesalahan dan jalur pemeriksaan manusia.

## 6. Posisi AI dalam software full-stack

~~~mermaid
flowchart LR
    U[Operator dashboard] --> B[Backend API]
    B --> V[Validasi input + authorization]
    V --> M[AI inference]
    M --> O[Validasi output]
    O --> D[(Database)]
    O --> H[Human review]
~~~

Diagram di atas merupakan **target rancangan** untuk modul berikutnya, bukan komponen yang sudah dibuat. Pada aplikasi nyata, API key dan logika authorization berada di server, bukan frontend.

## 7. Batasan keamanan dan kualitas

1. Pakai **data sintetis**; jangan kirim percakapan/customer records asli.
2. Jangan membocorkan rahasia, API key, atau data pribadi melalui prompt/log.
3. Validasi input dan output; perlakukan model sebagai komponen yang dapat salah.
4. Pantau kemungkinan data leakage, typo, slang, bahasa campuran, dan perubahan distribusi data.
5. Jangan percaya relative_score sebagai tingkat keyakinan yang akurat.
6. Gunakan human review untuk tindakan berisiko dan jangan pakai model pembelajaran untuk routing production.

Bacaan: [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) · [scikit-learn evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) · [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).
