# Teori — Scalability, Performance & Reliability

**Hasil belajar:** Mengukur bottleneck frontend/backend/DB/inference dan merancang scaling serta failure protection berdasarkan data.

## 1. Latency, throughput, utilization

Latency ialah durasi per request; throughput ialah jumlah pekerjaan per detik; concurrency ialah pekerjaan yang berlangsung bersamaan. P50 tidak cukup: P95/P99 menunjukkan tail latency pengguna. Throughput dan latency bisa memburuk cepat saat resource mendekati saturation.

## 2. Capacity planning

Mulai dari workload: ukuran request, jumlah active users, arrivals/second, ratio read/write, kebutuhan CPU/memori, external API quota. Perhitungan konservatif contoh: 20 req/s * 250 ms service time ~ 5 concurrent in-flight requests pada kondisi stabil, belum termasuk bursts dan overhead. Jangan menganggap kapasitas = angka teoritis saja.

## 3. Reliability controls

Timeout harus lebih pendek dari total request deadline; retry exponential backoff dengan jitter hanya untuk operasi aman/idempotent; circuit breaker membatasi chain failure; rate limiting mencegah abuse dan biaya tak terkendali. Bila model mahal, job queue dan bulkheads bisa memisahkan beban.

## 4. Caching, indexes, batching

Caching hasil inference punya risiko privasi dan stale model; key harus mempertimbangkan tenant, versi model, input normalized, expiry. Index mempercepat lookup tetapi overhead storage/write. Batching mengurangi per-item overhead tetapi memperpanjang antrian dan menambah kompleksitas error handling.

## 5. Load testing dan interpretasi

Simulasikan pola realistis, warmup, bounded duration, request mix, error rate, dan latencies. Catat hardware, network, versi aplikasi, concurrency, dan ukuran data. Uji failure path, bukan hanya success throughput. Hasil lokal tidak boleh dipromosikan sebagai SLA production.

## Skenario rekayasa perangkat lunak

Traffic naik dari 5 menjadi 100 pesan/detik pada jam ramai. Inference eksternal punya rate limit dan lonjakan P95. Evaluasi queue dan fallback manual dibanding menaikkan CPU secara membabi buta.

## Prinsip dan acceptance criteria

- Setiap hasil uji mencantumkan alat, mesin, durasi, concurrency, dan ukuran data.
- Rekomendasi perubahan diturunkan dari bottleneck yang diobservasi.
- Sistem menghindari retry tak berbatas dan uncontrolled external API consumption.
- Terdapat error case dan timeout scenario dalam pengujian.

## Dokumentasi primer untuk pendalaman

- https://sre.google/sre-book/monitoring-distributed-systems/
- https://www.postgresql.org/docs/current/indexes.html
- https://docs.python.org/3/library/statistics.html

Penjelasan ini mengaitkan materi praktik dengan unit yang dipublikasikan LSP. Ini bukan reproduksi KUK resmi dan tidak menentukan hasil asesmen.

[Praktikum](lab-guide.md)