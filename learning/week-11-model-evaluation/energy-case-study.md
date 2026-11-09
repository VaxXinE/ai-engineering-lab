# Applied Energy Case — Anomaly baseline versus ML numeric

**Status:** materi ilustratif, belum dijalankan sebagai praktik mandiri atau asesmen BNSP.

## Masalah

Dalam 1000 readings sintetis, 950 normal dan 50 diberi label injected anomaly oleh generator. Model naif selalu memberi 'normal'.

## Worked reasoning

Accuracy=950/1000=95%, tetapi recall anomaly=0/50=0%; kualitas detector buruk. Time split wajib dan skor Isolation Forest tidak otomatis menjadi probabilitas. Use case ini berbeda dari text classifier Week 01.

## Latihan dengan bantuan bertahap

**Guided:** jelaskan langkah-langkah reasoning dan constraint tiap keputusan.  
**Faded:** ganti satu input/constraint dan isi satu langkah perhitungan/desain yang hilang.  
**Independent:** Rancang rolling IQR dan Isolation Forest dengan fitting train, threshold validation, satu held-out test; jelaskan synthetic truth limitations.

## Negative case dan keamanan

Leakage masa depan, false detection pada meter berbeda, data missing dianggap nol, model artifact berbahaya.

Saat implementasi, pisahkan **expected behavior** dari **actual test output** serta lampirkan environment, commit, log yang disanitasi, dan keterbatasan. Jangan mengklaim hasil yang belum dijalankan.

## Target bukti kompetensi

Evaluation report, split manifest, per-class metrics jika label tersedia, model card.

**Sumber kontrak:** [Canonical Energy Schema](../../docs/architecture/energy-data-contract.md) · [Threat Model](../../docs/architecture/threat-model.md) · [Gates](../../docs/architecture/energy-learning-gates.md).
