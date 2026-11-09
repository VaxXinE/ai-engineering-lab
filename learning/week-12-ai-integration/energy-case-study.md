# Applied Energy Case — Output model numerik harus divalidasi

**Status:** materi ilustratif, belum dijalankan sebagai praktik mandiri atau asesmen BNSP.

## Masalah

Model mengembalikan anomaly_score=NaN atau timeout setelah reading valid tersimpan.

## Worked reasoning

Tolak NaN/inf/out-of-range, model_version kosong, dan reason code tidak dikenal. Jangan mengubahnya menjadi skor 0. Reading tetap ada dan status scoring_unavailable; review manusia tidak bergantung pada suksesnya model.

## Latihan dengan bantuan bertahap

**Guided:** jelaskan langkah-langkah reasoning dan constraint tiap keputusan.  
**Faded:** ganti satu input/constraint dan isi satu langkah perhitungan/desain yang hilang.  
**Independent:** Buat fake adapter untuk valid score, timeout, 429, invalid JSON dan cross-site access, beserta expected statuses.

## Negative case dan keamanan

BOLA, unchecked AI output, raw inference scores disalahartikan sebagai probability, dan actuators otomatis.

Saat implementasi, pisahkan **expected behavior** dari **actual test output** serta lampirkan environment, commit, log yang disanitasi, dan keterbatasan. Jangan mengklaim hasil yang belum dijalankan.

## Target bukti kompetensi

Typed contract, unit/integration tests, error taxonomy, audit & review traces.

**Sumber kontrak:** [Canonical Energy Schema](../../docs/architecture/energy-data-contract.md) · [Threat Model](../../docs/architecture/threat-model.md) · [Gates](../../docs/architecture/energy-learning-gates.md).
