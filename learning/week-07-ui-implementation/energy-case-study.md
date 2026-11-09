# Applied Energy Case — State machine grafik dan request filter race

**Status:** worked case untuk belajar; bukan hasil implementasi atau asesmen formal. **Latar:** site dan meter sepenuhnya sintetis.

## Problem

User membuka SITE-A kemudian SITE-B. Response dari A datang setelah B; query dashboard juga mengandung gap time-series.

## Worked reasoning — mengapa solusinya begitu?

Gunakan remote state union idle/loading/success/empty/error, request key site+meter+window, AbortController, dan render missing slots sebagai gap. Backend tetap enforce site permission.

## Guided → Independent challenge

**Guided:** ulangi penalaran di atas dan jelaskan setiap asumsi.  
**Faded:** ubah satu angka/aturan lalu tulis ulang satu langkah yang diperlukan.  
**Independent:** Uji dua deferred fetch yang selesai terbalik, retry 5xx, dan input anomaly_score=NaN.

## Negative case & security/reliability

Cross-site cache leak, XSS raw text, secret client bundle, double submit dan interpretasi skor sebagai probabilitas.

**Verifikasi yang disyaratkan saat praktik:** positif + negatif, expected vs actual, environment/runtime, test commands, kondisi gagal, dan catatan keterbatasan. Jangan tandai lulus hanya karena membaca contoh.

## Evidence target

Typed React components, UI tests, screenshot states, dan access-control tests server-side.

**Kontrak:** [Energy Data Contract](../../docs/architecture/energy-data-contract.md) · [Threat model](../../docs/architecture/threat-model.md) · [Learning gates](../../docs/architecture/energy-learning-gates.md).
