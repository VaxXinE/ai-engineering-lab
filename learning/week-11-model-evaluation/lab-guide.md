# Hands-on — Model Evaluation, Error Analysis & AI Quality Gates

**Status:** panduan siap; langkah belum dieksekusi. Implementasi, metrik, dan bukti ditulis setelah praktikum.

## Target

Mengembangkan baseline text classifier dan mengukur kualitas hasil secara disiplin sebelum mengintegrasikannya ke API.

## Skenario

Model Week 01 menghasilkan 77.78% accuracy pada hanya 18 sampel sintetis. Evaluasi lanjutan perlu memperluas data dan memisahkan validation dari test, bukan mengulang banyak perubahan sampai 18 sampel tersebut cocok.

## Langkah implementasi

1. Review Week 01 verification.md dan identifikasi kesalahan label pada confusion matrix.

2. Susun dataset tambahan yang sepenuhnya sintetis untuk eksperimen baru dan dokumentasikan sumber/seed/label policy.

3. Buat tiga split train/validation/test atau cross-validation yang sesuai, periksa duplicate dan potential group leakage.

4. Bandingkan aturan, Naive Bayes, dan satu model alternatif yang memiliki alasan teknis jelas (opsional scikit-learn).

5. Catat per-class metrics, confusion matrix, error examples sintetis, stability terhadap typo/slang dan abstention policy.

6. Buat model card dan quality gate eksplisit sebelum Week 12 integration.

## Acceptance criteria

- [ ] Model dievaluasi pada set yang tidak digunakan untuk train/tuning.
- [ ] Metrik yang dipilih berhubungan dengan dampak bisnis salah klasifikasi.
- [ ] Semua hasil yang dilaporkan benar-benar diukur dan dapat direproduksi.
- [ ] Model card menyebut limitasi data sintetis dan risiko domain shift.

## Rencana verifikasi

1. Buat skenario bukti untuk: Model dievaluasi pada set yang tidak digunakan untuk train/tuning.
2. Buat skenario bukti untuk: Metrik yang dipilih berhubungan dengan dampak bisnis salah klasifikasi.
3. Buat skenario bukti untuk: Semua hasil yang dilaporkan benar-benar diukur dan dapat direproduksi.
4. Buat skenario bukti untuk: Model card menyebut limitasi data sintetis dan risiko domain shift.

## Dokumentasi hasil

- Catat perintah, dependency/runtime, input sintetis, output aktual, dan edge case yang diuji.
- Catat source code atau desain beserta commit/PR.
- Tuliskan threat dan asumsi tersisa. Jangan menyatakan 'passed' sebelum menjalankan test.
- Kaitkan hasil dengan [evidence matrix](../../certification/evidence-matrix.md).

[Latihan](exercises.md) · [Simulasi](assessment.md)