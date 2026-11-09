# Deep Dive — Membuat keputusan teknologi yang bisa diuji dan dipertanggungjawabkan

> Materi lanjutan untuk pembaca yang sudah memahami software engineering dasar. **Contoh hitungan adalah ilustrasi**, bukan hasil pengujian sistem production.

## Learning outcomes yang harus bisa dibuktikan

1. Menerjemahkan kebutuhan menjadi hard constraints dan weighted criteria.
2. Membandingkan tiga arsitektur AI menggunakan angka contoh dan sensitivitas bobot.
3. Menyusun ADR dengan asumsi, opsi ditolak, risiko, dan trigger review.
4. Mengevaluasi risiko supply-chain sebelum menambah dependency.

## Penjelasan konsep secara mendalam

### 1. Pahami kebutuhan sebagai constraint yang terukur

Sebelum membandingkan FastAPI, NestJS, model lokal, atau hosted LLM, definisikan use-case. Hard constraints adalah hal yang tidak boleh dilanggar: misalnya tidak boleh mengirim PII ke provider eksternal. Soft constraints adalah preferensi yang dapat diperdagangkan: developer familiarity, speed of development, monthly budget dan p95 latency. Hard constraints harus menjadi filter sebelum scoring; opsi dengan skor terbaik tetap tidak layak jika melanggar privasi.

### 2. Decision matrix bukan objektivitas palsu

Weighted scoring memberi struktur pada diskusi, bukan membuktikan teknologi A secara ilmiah unggul. Tentukan kriteria dan bobot dari kebutuhan bisnis serta bukti untuk setiap skor. Pastikan skala konsisten: keamanan 5 = pengelolaan data memenuhi kebijakan, bukan karena library terkenal. Uji sensitivity: jika biaya lebih penting saat perusahaan kecil, pilihan bisa berbalik. Catat sumber skor, tanggal, dan asumsi agar keputusan bisa direview.

### 3. Build versus buy untuk AI

Rule-based menawarkan prediktabilitas tinggi namun kesulitan menangani variasi bahasa. Model ML lokal perlu data label, monitoring kualitas dan artifact management; tetapi inference dapat tetap dalam jaringan sendiri. Hosted LLM memudahkan integrasi tugas bahasa umum, tetapi membawa data residency, biaya token, rate-limit, latency provider, dan vendor lock-in. Hybrid pipeline dapat menggabungkan aturan prioritas dengan AI untuk pesan ambigu, namun lebih banyak cabang mempersulit evaluasi.

### 4. Dependency and license diligence

Periksa paket resmi, komunitas maintainer, security advisories, CVEs, dukungan platform, release cadence, dan lisensi termasuk transitive dependencies. Package dengan nama mirip bisa typosquatting. Jangan menjalankan script setup tak diketahui; gunakan lockfile, hashes bila tepat, security scanning, dan review perubahan lockfile. Semakin kritis komponennya, semakin tinggi tuntutan provenance dan update strategy.

### 5. API version, runtime version dan maintenance

Jangan memilih versi hanya dari blog lama. Dokumentasi resmi menentukan compatibility matrix; buktikan dengan small spike yang menjalankan endpoint, serialisasi, dan error. Upgrade library utama perlu test, bukan sekadar npm install latest. ADR harus mencatat exit strategy agar perubahan kontrak provider tidak merusak seluruh aplikasi.

### 6. Kapan keputusan ditinjau kembali

Rencana validasi memerlukan acceptance threshold: misalnya review cost per 1000 messages, p95 inference untuk ukuran pesan tertentu, error rate provider dan kualitas klasifikasi. Pilihan bersifat reversible jika interface adapter stabil. Jangan menyamakan benchmark localhost dengan throughput cloud production; catat lingkungan dan limitasi.

## Miskonsepsi yang perlu diwaspadai

- Skor total tertinggi berarti pilihan paling benar → skor bergantung asumsi dan bobot.
- Library populer pasti aman → dependencies tetap bisa rentan dan maintenance bisa berhenti.
- Lebih banyak microservices berarti lebih skalabel → overhead jaringan dan operasional bisa tidak proporsional.
- Tag latest mempermudah maintenance → menyebabkan build tidak reproducible.
- Framework pilihan harus tetap selamanya → ADR menyimpan kondisi perubahan.

## Transfer ke profesi full-stack

Ambil satu kebutuhan dari capstone [AI Smart Energy Monitoring](../../projects/ai-energy-intelligence/README.md). Jelaskan **data apa yang tepercaya, aturan bisnis mana yang harus deterministik, apa yang bisa diprediksi AI, bagaimana failure ditangani, dan bagaimana keputusan diuji**. Jangan menyatakan modul selesai hanya dengan menyalin contoh.

## Bacaan lanjutan (dokumentasi dan pembelajaran primer)

- https://docs.github.com/en/code-security/supply-chain-security
- https://fastapi.tiangolo.com/
- https://docs.python.org/3/library/venv.html

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md) · [Lab](lab-guide.md)
