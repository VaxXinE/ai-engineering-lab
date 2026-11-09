# Applied Energy Case — Volume 1000 meter dan query time range

**Status:** materi ilustratif, belum dijalankan sebagai praktik mandiri atau asesmen BNSP.

## Masalah

Satu meter mengirim setiap 15 menit, selama 30 hari, dan ada 1000 meter sintetis.

## Worked reasoning

96 readings/meter/hari × 1000 = 96,000 readings/hari dan 2,880,000 dalam 30 hari (asumsi tidak ada gap). Gunakan index site+meter+UTC, bounded range, aggregation dan coverage-aware downsampling.

## Latihan dengan bantuan bertahap

**Guided:** jelaskan langkah-langkah reasoning dan constraint tiap keputusan.  
**Faded:** ganti satu input/constraint dan isi satu langkah perhitungan/desain yang hilang.  
**Independent:** Hitung storage dengan asumsi ukuran bytes/row eksplisit, rancang pengukuran P95 dan negative overload tests.

## Negative case dan keamanan

Jangan stress-test sistem eksternal tanpa izin. Hindari cache yang membocorkan hasil antar-site, retry storm.

Saat implementasi, pisahkan **expected behavior** dari **actual test output** serta lampirkan environment, commit, log yang disanitasi, dan keterbatasan. Jangan mengklaim hasil yang belum dijalankan.

## Target bukti kompetensi

Capacity worksheet, index EXPLAIN, reproducible load test dan hasil aktual saat praktik.

**Sumber kontrak:** [Canonical Energy Schema](../../docs/architecture/energy-data-contract.md) · [Threat Model](../../docs/architecture/threat-model.md) · [Gates](../../docs/architecture/energy-learning-gates.md).
