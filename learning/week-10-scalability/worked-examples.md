# Worked Examples — Skalabilitas dari metrik, kapasitas, dan tail latency

**Semua cuplikan/angka adalah demonstrasi edukatif**, bukan bukti sudah diimplementasikan atau dideploy pada capstone. Jalankan dan catat hasil sebenarnya ketika masuk sesi praktikum.

## Solusi 1: Estimasi concurrency dengan Little's Law

**Masalah:** Sebuah service menerima rata-rata 40 req/s, average response time 250 ms saat steady-state.

**Tahapan pemecahan:**

1. Laju lambda = 40 request/detik.

2. Average W = 0.250 detik.

3. Perkiraan L = lambda * W = 40 * 0.250 = 10 requests in flight.

4. Jika latency naik jadi 1 detik pada throughput sama, rata-rata in-flight naik ke 40; jika resource tak cukup, antrean dan error akan bertambah.

**Anti-pattern:** 10 in-flight tidak berarti cukup 10 worker untuk seluruh peak; distribusi latency dan burst load harus diperhitungkan.

**Explain-back:** bagaimana cara membuat negative test untuk membuktikan anti-pattern tersebut?

## Solusi 2: Retry storm dari model provider

**Masalah:** 100 request menunggu inference; provider 429 untuk 30%. Client/backend retry 5 kali tanpa backoff.

**Tahapan pemecahan:**

1. Tanpa batas, setiap failure menambah requests baru yang dapat memperparah 429.

2. Tetapkan retry max (misal satu retry untuk operasi inferensi yang idempotent), exponential backoff+jitter, dan model deadline total.

3. Jika threshold error tinggi, buka circuit breaker dan arahkan ke manual review sementara.

4. Catat attempted vs successful requests dan biaya aktual; jangan menghitung hanya request dari UI.

**Anti-pattern:** Retry POST create meter reading tanpa idempotency bisa menghasilkan duplikat bahkan jika provider hanya timeout setelah berhasil memproses.

**Explain-back:** bagaimana cara membuat negative test untuk membuktikan anti-pattern tersebut?

## Progressive practice

- **Demonstrate:** trace contoh dengan input dan output yang diketahui.
- **Faded:** ganti satu parameter dan isi satu langkah yang sengaja dihilangkan sendiri.
- **Independent:** rancang kasus lain yang menuntut trade-off berbeda.
- **Verify:** jalankan test, simpan version/command/output aktual; jangan mengarang benchmark.

[Quiz dengan feedback](knowledge-check.md)
