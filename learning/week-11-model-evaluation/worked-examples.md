# Worked Examples — Eksperimen AI yang menolak angka bagus tanpa bukti generalisasi

**Semua cuplikan/angka adalah demonstrasi edukatif**, bukan bukti sudah diimplementasikan atau dideploy pada capstone. Jalankan dan catat hasil sebenarnya ketika masuk sesi praktikum.

## Solusi 1: Accuracy 95% yang menyesatkan

**Masalah:** Dalam 100 contoh, 95 general, 3 support, 2 sales. Model selalu memprediksi general.

**Tahapan pemecahan:**

1. Benar=95/100 → accuracy=95%.

2. Recall untuk support=0/3=0; recall sales=0/2=0.

3. General precision=95/100=.95; recall general=95/95=1; F1 general=2*.95*1/(1.95)=0.97436.

4. Macro F1=(0.97436+0+0)/3 ≈ 0.32479, jauh lebih rendah dari accuracy.

5. Kesimpulan: model berisiko gagal tugas routing penting walau 95% accuracy.

**Anti-pattern:** Jika hanya memantau accuracy, stakeholder dapat menyetujui model yang tidak pernah mengenali keluhan customer.

**Explain-back:** bagaimana cara membuat negative test untuk membuktikan anti-pattern tersebut?

## Solusi 2: Membuat model-card yang bisa diaudit

**Masalah:** Developer ingin mempromosikan model v2 setelah menaikkan F1 di data sintetis.

**Tahapan pemecahan:**

1. Buat dokumentasi intended uses, inappropriate uses, data-source synthetic, label policy dan split strategy.

2. Tulis hasil per-class metrics pada validation dan held-out test yang belum dipakai tuning.

3. Cantumkan model version, code commit, training parameters, dependency versions, provenance artifact.

4. Catat failure cases seperti message multilingual, mixed intent, dan domain shift; jangan klaim production readiness.

5. Tentukan pemicu rollback seperti naiknya support false negative dari feedback terverifikasi.

**Anti-pattern:** Menghapus kasus sulit dari test agar F1 meningkat termasuk manipulasi evaluasi, bukan perbaikan model.

**Explain-back:** bagaimana cara membuat negative test untuk membuktikan anti-pattern tersebut?

## Progressive practice

- **Demonstrate:** trace contoh dengan input dan output yang diketahui.
- **Faded:** ganti satu parameter dan isi satu langkah yang sengaja dihilangkan sendiri.
- **Independent:** rancang kasus lain yang menuntut trade-off berbeda.
- **Verify:** jalankan test, simpan version/command/output aktual; jangan mengarang benchmark.

[Quiz dengan feedback](knowledge-check.md)
