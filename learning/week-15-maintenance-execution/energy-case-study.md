# Applied Energy Case — Incident drill tanpa menyentuh data hidup

**Status:** materi ilustratif, belum dijalankan sebagai praktik mandiri atau asesmen BNSP.

## Masalah

Scorer sengaja dibuat timeout saat satu measurement SITE-A valid masuk; backup DB test tersedia.

## Worked reasoning

Catat baseline counts → fault inject → pastikan reading tersimpan → status scoring_unavailable → rollback model → restore database ke isolated test instance → check referential integrity dan UI read path.

## Latihan dengan bantuan bertahap

**Guided:** jelaskan langkah-langkah reasoning dan constraint tiap keputusan.  
**Faded:** ganti satu input/constraint dan isi satu langkah perhitungan/desain yang hilang.  
**Independent:** Buat postmortem dengan timeline, impact, hypothesis vs confirmed root cause, regression tests dan actual restore duration.

## Negative case dan keamanan

Jangan mengganggu production, jangan log secrets, jangan mengklaim restore berhasil hanya dari exit code.

Saat implementasi, pisahkan **expected behavior** dari **actual test output** serta lampirkan environment, commit, log yang disanitasi, dan keterbatasan. Jangan mengklaim hasil yang belum dijalankan.

## Target bukti kompetensi

Incident report, restore verification, regression tests dan changelog.

**Sumber kontrak:** [Canonical Energy Schema](../../docs/architecture/energy-data-contract.md) · [Threat Model](../../docs/architecture/threat-model.md) · [Gates](../../docs/architecture/energy-learning-gates.md).
