# Applied Energy Case — Gap dalam seri energi: kosong bukan nol

**Status:** worked case untuk belajar; bukan hasil implementasi atau asesmen formal. **Latar:** site dan meter sepenuhnya sintetis.

## Problem

Empat slot 15 menit: 00:00=1.40, 00:15=1.48, 00:30 missing, 00:45=0.00 kWh.

## Worked reasoning — mengapa solusinya begitu?

Coverage observed_unique_valid/expected=3/4=75%. Total **terukur** 2.88 kWh; jangan mengklaim total untuk seluruh jam karena ada gap. 0 kWh valid di slot terakhir.

## Guided → Independent challenge

**Guided:** ulangi penalaran di atas dan jelaskan setiap asumsi.  
**Faded:** ubah satu angka/aturan lalu tulis ulang satu langkah yang diperlukan.  
**Independent:** Tambahkan input NaN, infinity, -1 kWh, timestamp tanpa zona, dan interval 60; tentukan reject/quality status.

## Negative case & security/reliability

Time leakage dari rolling window ke test, malformed timezones dan silent coercion.

**Verifikasi yang disyaratkan saat praktik:** positif + negatif, expected vs actual, environment/runtime, test commands, kondisi gagal, dan catatan keterbatasan. Jangan tandai lulus hanya karena membaca contoh.

## Evidence target

Validation matrix, coverage quality report, negative tests dan leakage analysis.

**Kontrak:** [Energy Data Contract](../../docs/architecture/energy-data-contract.md) · [Threat model](../../docs/architecture/threat-model.md) · [Learning gates](../../docs/architecture/energy-learning-gates.md).
