# Applied Energy Case — Graceful degradation scoring

**Status:** materi ilustratif, belum dijalankan sebagai praktik mandiri atau asesmen BNSP.

## Masalah

Valid meter reading masuk melalui POST /api/v1/import-batches saat numerical anomaly scorer timeout.

## Worked reasoning

Backend validate/authorize → commit reading → scoring port times out → state scoring_unavailable; data tetap ada. Model score bukan permission. Route ditetapkan canonical contract; tidak ada '/meter readings' dengan spasi.

## Latihan dengan bantuan bertahap

**Guided:** jelaskan langkah-langkah reasoning dan constraint tiap keputusan.  
**Faded:** ganti satu input/constraint dan isi satu langkah perhitungan/desain yang hilang.  
**Independent:** Gambar sequence success, timeout, invalid score; buat interface score(features)->AnomalyResult dan ADR modular monolith.

## Negative case dan keamanan

IDOR per site, malformed model output, data-loss pada retry, unbounded job queue.

Saat implementasi, pisahkan **expected behavior** dari **actual test output** serta lampirkan environment, commit, log yang disanitasi, dan keterbatasan. Jangan mengklaim hasil yang belum dijalankan.

## Target bukti kompetensi

API contract, C4/sequence diagrams, timeout integration-test plan, ADR.

**Sumber kontrak:** [Canonical Energy Schema](../../docs/architecture/energy-data-contract.md) · [Threat Model](../../docs/architecture/threat-model.md) · [Gates](../../docs/architecture/energy-learning-gates.md).
