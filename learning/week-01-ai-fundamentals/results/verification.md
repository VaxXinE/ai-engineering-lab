# Week 01 — Verifikasi Setelah Migrasi Use Case

**Tanggal verifikasi:** 9 November 2026  
**Sumber pengujian:** GitHub Actions pada commit `a05f6c5`  
**Konteks:** klasifikasi catatan kejadian perangkat energi **sintetis**, bukan anomaly scoring numerik atau sensor nyata.

## Perintah yang dijalankan CI

```bash
cd learning/week-01-ai-fundamentals
python -m unittest discover -s tests -v
python -m week01 evaluate
python -m compileall -q week01
```

## Hasil aktual

| Item | Nilai |
| --- | --- |
| Automated tests | **23 passed** pada Python 3.11 dan 3.13 |
| Training set | 54 contoh sintetis (18 per kelas) |
| Held-out test | 18 contoh sintetis (6 per kelas) |
| Naive Bayes accuracy | **0.8889** |
| Naive Bayes macro F1 | **0.8821** |
| Rule-based accuracy | **0.6111** |
| Rule-based macro F1 | **0.7556** |
| ML abstentions pada held-out test | **0** |
| Rule-based abstentions pada held-out test | **7** |

## Confusion matrix Naive Bayes

| Actual / predicted | normal | warning | fault | abstain |
| --- | ---: | ---: | ---: | ---: |
| normal | 4 | 1 | 1 | 0 |
| warning | 0 | 6 | 0 | 0 |
| fault | 0 | 0 | 6 | 0 |

**Catatan:** rule-based macro F1 lebih tinggi dari rule-based accuracy karena penghitungan abstain dan kelas seimbang; abstention dihitung sebagai prediksi yang tidak tepat untuk accuracy. Jangan memilih model hanya dari satu metrik.

## Bukti CI

- [Python checks — passed](https://github.com/VaxXinE/ai-engineering-lab/actions/runs/42571533170).

## Keterbatasan

- Data hanya 72 kalimat sintetis dan tidak merepresentasikan perilaku sensor/gedung nyata.
- Text classifier **tidak** mendeteksi anomali kWh.
- Tidak ada calibration atau pengujian pada data operasional.
- Belum ada frontend, backend API, model numerik, maupun deployment.
- Skor di atas tidak mendukung klaim keselamatan, keakuratan produksi, atau kelayakan untuk penanganan perangkat listrik.
