# Deep Dive — Skalabilitas dari metrik, kapasitas, dan tail latency

## Apa yang dapat dibuktikan setelah mempelajari modul?

1. Membedakan throughput, concurrency, average dan p95 latency.
2. Melakukan estimasi awal in-flight work memakai Little's Law dengan asumsi eksplisit.
3. Merancang rate limit, timeout, dan retry aman.
4. Membaca hasil benchmark tanpa mengklaim SLA produksi.

## Prinsip desain, mekanisme dan konsekuensi

### 1. Workload model sebelum benchmark

Tulis volume pesan per menit, peak bursts, ukuran pesan, persentase inference lokal vs remote, read/write ratio, dan kebutuhan tenant. Beban 100 req/s dengan 2 KB payload berbeda total biaya dari 100 req/s dengan 100 KB payload. Query latency tergantung data cardinality dan indexing; model inference cost tergantung token atau artifact CPU. Spesifikasi hasil harus mencantumkan environment.

### 2. Latency, throughput, concurrency

Latency adalah durasi respons; throughput adalah laju requests selesai; concurrency adalah jumlah pekerjaan yang overlap. Perkiraan average in-flight = throughput * average duration (Little's Law) pada sistem yang relatif stabil. Ini bukan kapasitas maksimal; queue, bursts dan saturation harus diuji. P50 dapat membaik sementara P95 memburuk, sehingga pengguna tertentu tetap mengalami layanan lambat.

### 3. Scaling bottleneck end-to-end

Cek komponen yang melambat: browser rendering, API CPU, DB connections, index, inference serialization, provider network atau rate limit. Horizontal scaling API tak membantu jika DB satu-satunya bottleneck. Caching dapat membantu read tetapi risiko cross-tenant leak dan stale model outputs; cache key perlu tenant, input hash dan model version saat relevan.

### 4. Backpressure dan cost safety

Rate limit, concurrency semaphore, bounded queue, timeout dan circuit breaker mencegah satu dependency menghabiskan sumber daya. Retry exponential backoff + jitter hanya untuk idempotent operations; unbounded retry dapat menciptakan retry storm dan biaya tinggi. Dalam LLM usage, batas token, request quotas dan cost monitoring sama penting dengan latency.

### 5. Benchmark methodology

Catat data synthetic size, seed, request mix, client machine, server specs, test duration, warmup, concurrency, throughput, p50/p95/p99, error rate dan hasil logs. Run 3 kali jika mungkin dan laporkan variasi. Jangan mengukur provider eksternal dengan stress test tanpa izin. Load test untuk kode belum dijalankan harus diberi label test plan.

## Checklist penalaran

Ketika suatu solusi terlihat bekerja, tanyakan: (1) apakah hasil benar terhadap kontrak? (2) apakah tetap benar pada data berbeda? (3) apa yang terjadi bila dependency mati? (4) siapa yang berhak melihat/mengubah datanya? (5) bagaimana sistem membuktikan hasil pengujian? Jawab dengan contoh konkret, bukan sekadar kata "best practice".

## Sumber teknis primer

- https://sre.google/sre-book/monitoring-distributed-systems/
- https://www.postgresql.org/docs/current/indexes.html
- https://www.nist.gov/itl/ai-risk-management-framework

[Worked examples](worked-examples.md) · [Lab](lab-guide.md)
