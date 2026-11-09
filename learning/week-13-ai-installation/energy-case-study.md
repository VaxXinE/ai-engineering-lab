# Applied Energy Case — Clean install dengan secret dan rollback

**Status:** materi ilustratif, belum dijalankan sebagai praktik mandiri atau asesmen BNSP.

## Masalah

Aplikasi energy dashboard perlu dipasang dari checkout bersih ke test environment lokal tanpa API key dalam Git.

## Worked reasoning

Lock dependency/image digest, internal DB network, least-privileged users, migrations, model artifact provenance dan health readiness. Rollback app image tidak selalu membalik schema; migration perlu compatibility plan.

## Latihan dengan bantuan bertahap

**Guided:** jelaskan langkah-langkah reasoning dan constraint tiap keputusan.  
**Faded:** ganti satu input/constraint dan isi satu langkah perhitungan/desain yang hilang.  
**Independent:** Susun runbook berisi prerequisites, env placeholders, smoke test synthetic reading, abort/rollback, dan restore rehearsal.

## Negative case dan keamanan

Unpinned packages, leaked credentials, untrusted serialized model, exposed DB port.

Saat implementasi, pisahkan **expected behavior** dari **actual test output** serta lampirkan environment, commit, log yang disanitasi, dan keterbatasan. Jangan mengklaim hasil yang belum dijalankan.

## Target bukti kompetensi

Install/runbook yang dapat dieksekusi nanti, smoke-test log dan rollback validation.

**Sumber kontrak:** [Canonical Energy Schema](../../docs/architecture/energy-data-contract.md) · [Threat Model](../../docs/architecture/threat-model.md) · [Gates](../../docs/architecture/energy-learning-gates.md).
