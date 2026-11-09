# Applied Energy Case — Rolling baseline tanpa memengaruhi diri sendiri

**Status:** worked case untuk belajar; bukan hasil implementasi atau asesmen formal. **Latar:** site dan meter sepenuhnya sintetis.

## Problem

Input per-meter berturut-turut [1.0,1.1,5.9,1.2] kWh. Window N=2.

## Worked reasoning — mengapa solusinya begitu?

Untuk interval ketiga, window history adalah [1.0,1.1]; baseline mean 1.05 kWh. Hitung skor 5.9 **sebelum** memasukkan 5.9 ke window. Sliding window berbasis slot memerlukan aturan missing slots.

## Guided → Independent challenge

**Guided:** ulangi penalaran di atas dan jelaskan setiap asumsi.  
**Faded:** ubah satu angka/aturan lalu tulis ulang satu langkah yang diperlukan.  
**Independent:** Implementasikan fungsi pure yang mengelompokkan berdasarkan (site_id,meter_id), mengurutkan UTC, dan mengelola out-of-order.

## Negative case & security/reliability

Future leakage, unlimited memory, dan duplikat antar-worker; gunakan DB constraints.

**Verifikasi yang disyaratkan saat praktik:** positif + negatif, expected vs actual, environment/runtime, test commands, kondisi gagal, dan catatan keterbatasan. Jangan tandai lulus hanya karena membaca contoh.

## Evidence target

Algorithm invariants, complexity analysis, unit tests dan benchmark yang benar-benar dijalankan.

**Kontrak:** [Energy Data Contract](../../docs/architecture/energy-data-contract.md) · [Threat model](../../docs/architecture/threat-model.md) · [Learning gates](../../docs/architecture/energy-learning-gates.md).
