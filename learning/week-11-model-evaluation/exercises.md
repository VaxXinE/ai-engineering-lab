# Latihan Mandiri — Numeric Energy Anomaly Evaluation

**Status:** belum dikerjakan. Gunakan synthetic meter dataset untuk Week 11, bukan hasil text classifier Week 01.

1. **A — Baseline:** rancang rolling median/IQR untuk satu meter dengan interval 15 menit; jelaskan input historis dan bagaimana menghindari future leakage.
2. **B — Evaluasi:** dari 1000 readings sintetis dengan 50 injected anomalies, hitung precision/recall model yang selalu menjawab normal. Mengapa accuracy 95% berbahaya?
3. **C — Time split:** buat rencana train/validation/test kronologis, termasuk bagaimana threshold dipilih tanpa melihat held-out test.
4. **D — Model card:** tulis fitur, durasi interval, seed generator, ground truth sintetis, per-meter limitations, model_version dan rencana rollback.

## Review checklist

- [ ] Threshold dan preprocessing tidak memanfaatkan data test.
- [ ] Missing timestamp dipisahkan dari measurement 0 kWh.
- [ ] Score tidak diklaim sebagai probabilitas kerusakan.
- [ ] Perbandingan rule/IQR vs ML menyimpan hasil nyata ketika sudah diuji.
- [ ] Keputusan review manusia tidak dipakai diam-diam sebagai label sempurna.

[Teori](theory.md) · [Contoh evaluasi](worked-examples.md) · [Canonical data contract](../../docs/architecture/energy-data-contract.md).
