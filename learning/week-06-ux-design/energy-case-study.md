# Applied Energy Case — Tampilan anomali kandidat, bukan alarm keselamatan

**Status:** worked case untuk belajar; bukan hasil implementasi atau asesmen formal. **Latar:** site dan meter sepenuhnya sintetis.

## Problem

MTR-001 mencatat 5.90 kWh pada 00.30. Operator melihat dua interval sebelumnya 1.40 dan 1.48 kWh tetapi belum tahu sebab perubahan.

## Worked reasoning — mengapa solusinya begitu?

Dashboard menampilkan angka per interval, baseline, data-quality flag dan model version. Human review memutuskan confirmed_anomaly/expected_variation/needs_investigation. Missing slot ditampilkan sebagai gap.

## Guided → Independent challenge

**Guided:** ulangi penalaran di atas dan jelaskan setiap asumsi.  
**Faded:** ubah satu angka/aturan lalu tulis ulang satu langkah yang diperlukan.  
**Independent:** Buat wireframe Energy Overview → Meter Detail → Anomaly Review → History, termasuk model outage dan HTTP 409 review conflict.

## Negative case & security/reliability

Tidak boleh menyebut listrik berbahaya atau mengontrol daya berdasarkan output AI; perhatikan akses site.

**Verifikasi yang disyaratkan saat praktik:** positif + negatif, expected vs actual, environment/runtime, test commands, kondisi gagal, dan catatan keterbatasan. Jangan tandai lulus hanya karena membaca contoh.

## Evidence target

Persona, user journey, task tests, wireframe dan accessibility criteria.

**Kontrak:** [Energy Data Contract](../../docs/architecture/energy-data-contract.md) · [Threat model](../../docs/architecture/threat-model.md) · [Learning gates](../../docs/architecture/energy-learning-gates.md).
