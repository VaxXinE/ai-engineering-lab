# Applied Energy Case — Confusion matrix klasifikasi log perangkat

**Status:** worked case untuk belajar; bukan hasil implementasi atau asesmen formal. **Latar:** site dan meter sepenuhnya sintetis.

## Problem

Test Naive Bayes pada 18 catatan sintetis: 6 normal, 6 warning, 6 fault. Matrix contoh yang sudah tercatat: normal diprediksi [4 normal,1 warning,1 fault]; warning 6 benar; fault 6 benar.

## Worked reasoning — mengapa solusinya begitu?

Prediksi benar=4+6+6=16 dari 18 → accuracy 16/18=88.89%. Recall normal 4/6=66.67%; warning 100%; fault 100%. Angka ini hanya cocok untuk data latihan tersebut.

## Guided → Independent challenge

**Guided:** ulangi penalaran di atas dan jelaskan setiap asumsi.  
**Faded:** ubah satu angka/aturan lalu tulis ulang satu langkah yang diperlukan.  
**Independent:** Tunjukkan dua salah prediksi, jelaskan false normal/false fault dan mengapa hasil teks tidak berlaku untuk anomali kWh.

## Negative case & security/reliability

Data leakage, kegagalan mengenali catatan tidak dikenal, dan false confidence. Gunakan abstain dan human review.

**Verifikasi yang disyaratkan saat praktik:** positif + negatif, expected vs actual, environment/runtime, test commands, kondisi gagal, dan catatan keterbatasan. Jangan tandai lulus hanya karena membaca contoh.

## Evidence target

Hasil CLI pada dataset sintetis, confusion matrix, per-class metrics dan analisis kesalahan.

**Kontrak:** [Energy Data Contract](../../docs/architecture/energy-data-contract.md) · [Threat model](../../docs/architecture/threat-model.md) · [Learning gates](../../docs/architecture/energy-learning-gates.md).
