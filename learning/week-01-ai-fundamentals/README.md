# Modul 01 — AI Engineering Fundamentals

**Jalur belajar:** AI Aplikasi Perangkat Lunak + AI Proses Data  
**Status:** Starter materi dan kode tersedia; kemampuan peserta belum dinilai.  
**Estimasi belajar:** 8–10 jam  
**Prasyarat:** Python 3.11+, terminal dasar

## Apa yang akan dipelajari?

Sebagai full-stack software engineer, kita tidak cukup hanya memanggil API AI. Modul ini mengenalkan konsep **AI vs ML vs DL vs Generative AI**, **training vs inference**, **evaluasi model**, dan **risiko penggunaan AI** melalui klasifikasi pesan pelanggan **sintetis**.

Studi kasus: mengategorikan pesan menjadi **sales**, **support**, atau **general** menggunakan dua pendekatan:
- **Rule-based:** aturan keyword yang ditulis developer, tanpa training ML.
- **Multinomial Naive Bayes:** model statistik sederhana yang mempelajari frekuensi kata dari data berlabel.

Ini adalah proof-of-concept lokal, **bukan layanan AI production** dan **bukan LLM**.

## Hasil belajar

Setelah mengerjakan modul ini, peserta diharapkan bisa:
1. Menjelaskan AI, ML, DL, GenAI, dan penggunaan LLM dalam software.
2. Memisahkan data latih, inferensi, dan data uji tanpa kebocoran data.
3. Membaca accuracy, precision, recall, F1, confusion matrix dan abstentions.
4. Membandingkan rule-based dengan ML berdasarkan hasil pengujian.
5. Menjelaskan keterbatasan model dan alasan human review diperlukan.

## Alur sistem

~~~mermaid
flowchart LR
    A[72 pesan sintetis] --> B[54 data train]
    A --> C[18 data test]
    B --> D[Training Naive Bayes]
    D --> E[Inference]
    C --> E
    E --> F[Accuracy, Precision, Recall, F1]
    C --> G[Rule-based baseline]
    G --> H[Evaluasi pembanding]
~~~

## Quick start

Dari root repo:

~~~bash
cd learning/week-01-ai-fundamentals
python -m week01 evaluate
python -m week01 predict --text "saya ingin membeli paket langganan"
python -m week01 predict --text "aplikasi saya gagal login"
python -m week01 predict --text "zzzzzzqqq"
python -m unittest discover -s tests -v
~~~

Tidak perlu pip install; semua kode memakai **Python standard library**. Gunakan python3 atau py -3 jika alias python tidak tersedia.

Contoh custom dataset:

~~~bash
python -m week01 --train data/train.csv evaluate --test data/test.csv
~~~

**Penting:** relative_score adalah bobot relatif model, **bukan probabilitas yang sudah terkalibrasi**. Jika tidak ada token yang dikenali, model mengeluarkan **abstain**. Data test tidak digunakan saat pelatihan.

## Struktur modul

| File / Folder | Fungsi |
| --- | --- |
| week01/dataset.py | Validasi dan pembacaan CSV; cek overlap train/test |
| week01/model.py | Tokenizer dan Multinomial Naive Bayes |
| week01/rules.py | Baseline aturan keyword |
| week01/metrics.py | Accuracy, precision, recall, F1, confusion matrix |
| week01/cli.py | Command predict dan evaluate |
| data/train.csv | 54 pesan sintetis berlabel |
| data/test.csv | 18 pesan sintetis untuk evaluasi |
| tests/ | 23 automated tests |
| results/verification.md | Hasil eksekusi yang telah diuji |

## Urutan belajar

1. [Teori AI Engineering](theory.md)
2. [Use-case specification](use-case-spec.md)
3. [Praktikum dan troubleshooting](lab-guide.md)
4. [Latihan mandiri](exercises.md)
5. [Simulasi pertanyaan asesmen](assessment.md)
6. [Bukti verifikasi teknis](results/verification.md)

## Checklist belajar personal

- [ ] Bisa menjelaskan AI, ML, DL, GenAI, training dan inference.
- [ ] Berhasil menjalankan predict, evaluate dan test suite sendiri.
- [ ] Bisa menjelaskan setidaknya satu kesalahan prediksi dan alasan terjadinya.
- [ ] Menyelesaikan latihan A dan B dan mencatat hasil aktual.
- [ ] Memahami risiko data leakage, privasi, misrouting, dan overtrust.
- [ ] Membuat catatan/refleksi di branch latihan sendiri.

**Checklist tidak otomatis tercentang saat file di-push.** Kesiapan sertifikasi tetap menunggu bukti kompetensi dan asesmen LSP.

## Referensi pembelajaran

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [scikit-learn — Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)
- [Python — unittest](https://docs.python.org/3/library/unittest.html)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

[Roadmap lengkap](../../docs/learning-roadmap.md) | [Tracker](../../docs/progress-tracker.md) | [Portfolio BNSP](../../certification/evidence-matrix.md)

> Week 01 adalah fondasi lintas unit, bukan bukti bahwa unit kompetensi BNSP tertentu telah dipenuhi.
