# Applied Energy Case — Skema audit untuk dua site

**Status:** worked case untuk belajar; bukan hasil implementasi atau asesmen formal. **Latar:** site dan meter sepenuhnya sintetis.

## Problem

SITE-A/MTR-001 dan SITE-B/MTR-001 mengirim E-1001 pada waktu sama. Operator Site-A ingin membaca Site-B.

## Worked reasoning — mengapa solusinya begitu?

Composite identity (site_id,meter_id,source_event_id) membedakan sumber. MeterReading → AnomalyEvent(ModelVersion) → ReviewEvent append-only; per-site authZ pada query. Optimistic lock menjaga review concurrent.

## Guided → Independent challenge

**Guided:** ulangi penalaran di atas dan jelaskan setiap asumsi.  
**Faded:** ubah satu angka/aturan lalu tulis ulang satu langkah yang diperlukan.  
**Independent:** Tulis migration berisi PK/FK/composite UNIQUE, index site+meter+UTC time; uji duplicate conflict dan cross-site IDOR.

## Negative case & security/reliability

Cross-site BOLA, lost update, orphan rows, serta rollback migration tanpa backup.

**Verifikasi yang disyaratkan saat praktik:** positif + negatif, expected vs actual, environment/runtime, test commands, kondisi gagal, dan catatan keterbatasan. Jangan tandai lulus hanya karena membaca contoh.

## Evidence target

ERD, migration, transaction tests, site authorization matrix.

**Kontrak:** [Energy Data Contract](../../docs/architecture/energy-data-contract.md) · [Threat model](../../docs/architecture/threat-model.md) · [Learning gates](../../docs/architecture/energy-learning-gates.md).
