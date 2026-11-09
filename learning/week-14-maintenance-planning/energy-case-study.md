# Applied Energy Case — Model sehat tetapi review burden naik

**Status:** materi ilustratif, belum dijalankan sebagai praktik mandiri atau asesmen BNSP.

## Masalah

HTTP endpoint selalu 200 tetapi kandidat anomali yang di-override operator meningkat dari 5% ke 20%.

## Worked reasoning

Availability bukan kualitas prediksi. Periksa label policy, sample sizes, per-meter drift, missing interval rate, model_version dan alert volume sebelum menyimpulkan model rusak. Buat quality gate dan rollback criteria.

## Latihan dengan bantuan bertahap

**Guided:** jelaskan langkah-langkah reasoning dan constraint tiap keputusan.  
**Faded:** ganti satu input/constraint dan isi satu langkah perhitungan/desain yang hilang.  
**Independent:** Buat empat SLI/SLO dengan numerator/denominator, owner, alert, runbook, dan RPO/RTO hipotesis.

## Negative case dan keamanan

Alert fatigue, data drift disangka kerusakan, log berisi lokasi sensitif, backup tanpa restore.

Saat implementasi, pisahkan **expected behavior** dari **actual test output** serta lampirkan environment, commit, log yang disanitasi, dan keterbatasan. Jangan mengklaim hasil yang belum dijalankan.

## Target bukti kompetensi

Maintenance plan, risk register, alert matrix dan backup/restore plan.

**Sumber kontrak:** [Canonical Energy Schema](../../docs/architecture/energy-data-contract.md) · [Threat Model](../../docs/architecture/threat-model.md) · [Gates](../../docs/architecture/energy-learning-gates.md).
