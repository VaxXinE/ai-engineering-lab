# Week 01 — Hasil Verifikasi Lokal

**Tanggal:** 9 November 2026  
**Lingkungan:** Python 3.13 di container lokal  
**Status:** Starter code telah diuji secara lokal; kompetensi peserta belum dinilai.

Perintah yang dijalankan:

~~~bash
cd learning/week-01-ai-fundamentals
python -m unittest discover -s tests -v
python -m week01 evaluate
python -m week01 predict --text "saya ingin membeli paket langganan"
python -m compileall -q week01
~~~

## Hasil aktual

| Item | Nilai |
| --- | --- |
| Automated tests | **23 passed, 0 failed** |
| Data latih | **54** contoh sintetis |
| Data uji held-out | **18** contoh sintetis |
| Naive Bayes accuracy | **0.7778** |
| Naive Bayes macro F1 | **0.7948** |
| Rule-based accuracy | **0.7222** |
| Rule-based macro F1 | **0.7242** |
| ML abstentions | **1 dari 18** |
| Demo prediksi | "saya ingin membeli paket langganan" → sales; relative_score 0.9914 |

## ML Confusion Matrix

| Label asli / prediksi | sales | support | general | abstain |
| --- | ---: | ---: | ---: | ---: |
| sales | 6 | 0 | 0 | 0 |
| support | 1 | 4 | 1 | 0 |
| general | 1 | 0 | 4 | 1 |

## Batasan penting

- **72 teks buatan tangan** terlalu sedikit untuk memperkirakan performa pada chat customer nyata.
- Tidak ada cross-validation, pembuktian semantic leakage, pengujian fairness atau calibration.
- Relative_score **bukan** probabilitas terkalibrasi.
- Belum ada API, frontend, authorization, storage, observability atau deployment.
- CI GitHub Actions dirancang, tetapi **hasil workflow cloud belum diverifikasi** di catatan ini.
- Jangan pakai contoh ini sebagai sistem routing customer production.

Angka ini hanya menunjukkan kemampuan demonstrasi teknis pada set uji kecil. Hasil bisa berubah bila kode/data diperbarui.
