# Deep Dive — Arsitektur AI yang isolasi kegagalan dan tanggung jawabnya jelas

## Apa yang dapat dibuktikan setelah mempelajari modul?

1. Membedakan domain service, API adapter, repository, dan inference port.
2. Merancang data flow dan trust boundaries untuk AI service.
3. Menjelaskan kapan modular monolith lebih masuk akal daripada microservices.
4. Mendemonstrasikan rencana graceful degradation saat inference gagal.

## Prinsip desain, mekanisme dan konsekuensi

### 1. Tentukan boundary dari kebutuhan, bukan nama framework

Aktor: energy analyst, facility operator, maintainer; komponen: browser, authenticated API, ingestion/validation, site-scoped database, anomaly scorer, review audit, observability. Browser dan CSV tidak dipercaya; output model juga tidak dipercaya. C4 context/container/component dan sequence diagrams perlu menampilkan trust boundaries serta jalur fallback saat scorer gagal.

### 2. Modular monolith adalah pilihan sadar

Monolith modular memiliki deployment sederhana, transaksi DB lebih mudah, latency antar modul rendah dan dapat ditest end-to-end lebih cepat. Microservices berguna jika kapasitas, kepemilikan, kebutuhan deploy dan isolasi menuntutnya; tetapi menambah network failures, tracing, service identity dan consistency complexity. Tidak ada aturan bahwa aplikasi AI harus microservice. Mulai dengan modul jelas agar ekstraksi service kelak tidak memerlukan rewrite total.

### 3. Ports and adapters untuk vendor-independent AI

Domain energy scoring bergantung pada `score(reading_features)->AnomalyResult`, bukan `classify(event_note)`. Adapter dapat menjalankan IQR baseline atau numeric anomaly model. Return harus finite normalized score, flagged, reason_codes, model_version. Raw scores tidak otomatis probability. Perubahan provider/model tidak mengubah route atau permission policy.

### 4. Consistency dan asynchronous workflows

Simpan valid `MeterReading` lebih dahulu, kemudian kirim job scoring yang idempotent. Jika queue gagal setelah DB commit, status pending dan reconciler atau transactional outbox dapat memulihkan. Pada timeout, buat `scoring_unavailable`, jangan menghapus pembacaan atau menandainya normal. Retry dibatasi agar tidak menciptakan duplicate AnomalyEvent.

### 5. Security dan abuse controls

AuthN dan site-scoped AuthZ dilakukan server; SQL parameterized, object access pada site+meter, strict CSV and model output schemas, encrypted secrets dan bounded resource usage. Model tidak memiliki akses mengendalikan perangkat listrik. Lakukan negative tests cross-site IDOR dan malformed AI response.

## Checklist penalaran

Ketika suatu solusi terlihat bekerja, tanyakan: (1) apakah hasil benar terhadap kontrak? (2) apakah tetap benar pada data berbeda? (3) apa yang terjadi bila dependency mati? (4) siapa yang berhak melihat/mengubah datanya? (5) bagaimana sistem membuktikan hasil pengujian? Jawab dengan contoh konkret, bukan sekadar kata "best practice".

## Sumber teknis primer

- https://c4model.com/
- https://fastapi.tiangolo.com/
- https://owasp.org/www-project-api-security/

[Worked examples](worked-examples.md) · [Lab](lab-guide.md)
