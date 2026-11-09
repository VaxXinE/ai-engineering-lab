# Hands-on Lab — Week 01

## Persiapan

Butuh Python 3.11+. Dari direktori root repo:

~~~bash
cd learning/week-01-ai-fundamentals
python --version
~~~

Library pihak ketiga **tidak diperlukan**. Kode standard library sengaja dipilih supaya konsep training dan evaluasi terlihat jelas.

## Praktik 1: mengenali data

Buka data/train.csv dan data/test.csv. Ada **54 train** dan **18 test** (masing-masing tiga kelas). Semua contoh disusun secara sintetis.

Tinjau week01/dataset.py:
- read_examples memvalidasi header, label, panjang teks dan duplikasi.
- check_train_test_leakage menolak teks yang sama muncul di kedua set.

**Pertanyaan:** mengapa data evaluasi tidak boleh dipakai saat training?

## Praktik 2: memahami model

Buka week01/model.py:
1. tokenize mengubah teks menjadi kata.
2. word_counts menghitung frekuensi tiap kata pada tiap kelas.
3. vocabulary memuat kata dari train saja.
4. predict menghitung log-score dan kelas terbaik.
5. Jika tidak ada satu pun kata dikenali, model mengeluarkan abstain.

Model ini adalah implementasi **Multinomial Naive Bayes sederhana**; tidak memakai LLM atau model pretrained.

## Praktik 3: menjalankan inference

~~~bash
python -m week01 predict --text "saya ingin membeli paket langganan"
python -m week01 predict --text "aplikasi saya gagal login"
python -m week01 predict --text "alamat kantor perusahaan di mana"
python -m week01 predict --text "zzzzzzqqq"
~~~

Output JSON berisi label, relative_score dan peringatan bahwa skor **bukan** confidence terkalibrasi. Bandingkan hasil tiap contoh.

## Praktik 4: evaluasi ML dan baseline aturan

~~~bash
python -m week01 evaluate
~~~

Output mencakup accuracy, macro F1, precision, recall, F1 setiap kelas, confusion matrix, dan abstention_count. Properti rule_based_baseline berisi metrik dari aturan keyword pada **18 test yang sama**.

**Pertanyaan:** Apa makna warning recall 0.6667? Mengapa akurasi tidak otomatis mewakili kemampuan generalisasi model?

## Praktik 5: automated testing

~~~bash
python -m unittest discover -s tests -v
python -m compileall -q week01
~~~

Jangan hanya melihat hijau. Baca test invalid CSV, leakage, metrik, prediksi, dan abstain; pahami mengapa semuanya penting.

## Troubleshooting

| Gejala | Kemungkinan penyebab | Solusi |
| --- | --- | --- |
| No module named week01 | Berada di folder yang salah | Masuk ke learning/week-01-ai-fundamentals |
| CSV columns must be exactly | Header tidak text,label | Perbaiki nama/urutan kolom |
| Training/test leakage | Ada record yang sama | Periksa dan pisahkan dataset |
| Prediksi abstain | Seluruh kata tidak ada di vocab | Perlu data latih yang lebih representatif |
| python not found | Python belum di PATH | Gunakan python3 atau py -3 |

## Tugas lanjutan

Kerjakan [exercises.md](exercises.md), lalu uji pemahaman melalui [assessment.md](assessment.md). Simpan hasil aktual, bukan angka yang diduga.
