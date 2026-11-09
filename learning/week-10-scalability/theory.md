# Teori — Scalability for Meter Time-Series and AI Scoring (Week 10)

**Outcome:** dapat mengestimasi volume, menganalisis bottleneck, merencanakan load test reproducible, dan membedakan latency dari throughput.

## 1. Dimensi volume

Dengan interval 15 menit, satu meter menghasilkan `24*4=96` readings per hari jika tidak ada gap. Seribu meter menghasilkan `96.000` readings/hari, sekitar `2.88 juta` dalam 30 hari, sebelum retention dan corrections. Nilai tersebut hanyalah perhitungan kapasitas, bukan benchmark database.

## 2. SLI untuk pipeline

Ukur ingest rows/sec, rejected/duplicate rates, P50/P95/P99 API latency, query time-range, scoring latency, queue backlog, CPU/memory dan disk usage. Grafik satu bulan memerlukan pagination/aggregation; query seluruh raw readings untuk setiap user bisa mahal. Index pada `(site_id,meter_id,interval_start_utc)` membantu pola query spesifik tetapi harus diuji EXPLAIN pada dataset yang sesuai.

## 3. Average concurrency

Little's Law memperkirakan average in-flight = throughput × average response time dalam kondisi steady-state. Contoh 40 req/s × 0.25s = 10 in-flight, **bukan** bukti cukup 10 workers saat peak. P95 latency penting karena queueing dan resource saturation memengaruhi ekor distribusi.

## 4. Safe load test

Load testing hanya pada environment test yang dimiliki/diizinkan. Gunakan dataset sintetis dengan seed dan ukuran jelas, mencatat mesin, versi, concurrency, duration, response mix, error rate, P95, dan metode perhitungan. Jangan mengarang hasil sampai benchmark dijalankan.

## 5. Backpressure, cost dan cache

Batasi ukuran request/batch, connection pools, retries/backoff+jitter, queue depth, per-site rate limits dan timeouts. Caching perlu key site+meter+range+model_version, kalau tidak ada risiko cross-site disclosure atau stale results. Retry pada import harus idempotent dengan composite event key.

## 6. Timeseries correctness under scale

Aggregasi harus mempertahankan jumlah kWh dan coverage; missing interval bukan nol, dan perubahan interval duration harus ditangani eksplisit. Downsampling dapat menyimpan `sum(kWh)` dan `observed/expected slot count` agar grafik tidak menyamarkan kekosongan data.

[Perencanaan benchmark](lab-guide.md) · [Domain contract](../../docs/architecture/energy-data-contract.md).

Referensi: [Google SRE Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/), [PostgreSQL indexes](https://www.postgresql.org/docs/current/indexes.html).
