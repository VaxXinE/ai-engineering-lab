# Deep Dive — Skalabilitas dari metrik, kapasitas, dan tail latency

## Apa yang dapat dibuktikan setelah mempelajari modul?

1. Membedakan throughput, concurrency, average dan p95 latency.
2. Melakukan estimasi awal in-flight work memakai Little's Law dengan asumsi eksplisit.
3. Merancang rate limit, timeout, dan retry aman.
4. Membaca hasil benchmark tanpa mengklaim SLA produksi.

## Prinsip desain, mekanisme dan konsekuensi

### 1. Workload model sebelum benchmark

Dengan slot 15 menit: 96 readings/meter/hari dan 96.000 readings/hari untuk 1000 meter. Ukur insert rows/sec, query p95 berdasarkan site/meter/rentang, bytes/reading, aggregation cost, scoring latency dan queue depth. Lebih banyak meter bukan otomatis lebih banyak browser RPS; pisahkan ingest workload dari dashboard read workload.

### 2. Latency, throughput, concurrency

Latency adalah durasi respons; throughput adalah laju requests selesai; concurrency adalah jumlah pekerjaan yang overlap. Perkiraan average in-flight = throughput * average duration (Little's Law) pada sistem yang relatif stabil. Ini bukan kapasitas maksimal; queue, bursts dan saturation harus diuji. P50 dapat membaik sementara P95 memburuk, sehingga pengguna tertentu tetap mengalami layanan lambat.

### 3. Scaling bottleneck end-to-end

Bottleneck bisa terjadi pada file parser, DB index, time-range query, aggregation, model scorer, atau browser chart. Horizontal scaling API tidak mengatasi DB contention. Cache key harus memasukkan authorized site/meter/time window/model version; hindari menyimpan readings site lain dalam client cache.

### 4. Backpressure dan cost safety

Batasi ukuran CSV/batch, concurrent scoring, queue depth, request timeouts dan retries. Untuk angka time-series, downsampling perlu menyimpan `sum(energy_kwh)` dan coverage; missing slot tidak boleh disamakan dengan energi nol. Stress test jangan diarahkan ke layanan eksternal tanpa izin.

### 5. Benchmark methodology

Catat data synthetic size, seed, request mix, client machine, server specs, test duration, warmup, concurrency, throughput, p50/p95/p99, error rate dan hasil logs. Run 3 kali jika mungkin dan laporkan variasi. Jangan mengukur provider eksternal dengan stress test tanpa izin. Load test untuk kode belum dijalankan harus diberi label test plan.

## Checklist penalaran

Ketika suatu solusi terlihat bekerja, tanyakan: (1) apakah hasil benar terhadap kontrak? (2) apakah tetap benar pada data berbeda? (3) apa yang terjadi bila dependency mati? (4) siapa yang berhak melihat/mengubah datanya? (5) bagaimana sistem membuktikan hasil pengujian? Jawab dengan contoh konkret, bukan sekadar kata "best practice".

## Sumber teknis primer

- https://sre.google/sre-book/monitoring-distributed-systems/
- https://www.postgresql.org/docs/current/indexes.html
- https://www.nist.gov/itl/ai-risk-management-framework

[Worked examples](worked-examples.md) · [Lab](lab-guide.md)
