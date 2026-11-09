# Teori — Week 02: Technology Assessment & Dependency Selection

**Tujuan:** Memilih teknologi yang aman, relevan, terukur, dan bisa dipelihara untuk capstone AI Smart Energy Monitoring.

## Konsep dan keputusan engineering

### 1. Requirement-first technology selection

Mulai dari constraint produk, bukan popularitas library. Tentukan fungsi wajib, nonfungsional (latency, privacy, compliance, budget, dukungan tim) dan lingkup MVP. Tools terbaik bukan yang paling banyak fitur, tetapi yang memenuhi kebutuhan dengan total risiko dan biaya terkendali. Pisahkan hard requirement, preferensi, dan asumsi yang perlu diuji.

### 2. Decision matrix dan pembobotan

Nilai alternatif dengan kriteria yang dapat diamati. Contoh bobot: kesesuaian produk 30%, keamanan 25%, maintainability 20%, biaya 15%, performa 10%. Skor 1–5 tidak ilmiah jika tidak disertai bukti; jelaskan sumber dan kondisi pengukuran. Perubahan bobot dapat mengubah pemenang, sehingga lakukan sensitivity analysis.

### 3. Library selection dan supply-chain

Evaluasi lisensi (termasuk kewajiban distribusi), maintainer, cadence rilis, issue keamanan, dependencies transitive, dukungan runtimes, dokumentasi, dan migration path. Gunakan versi yang kompatibel dan lockfile. Hindari menjalankan installation script yang tidak dipahami serta jangan menonaktifkan audit security agar instalasi berhasil.

### 4. AI deployment decision

Bandingkan rule-based, ML lokal, dan hosted LLM: kualitas keluaran, data residency, biaya per-request, cold start, latency P95, rate limits, outage dependency, dan kontrol model. Pilihan awal dapat berupa baseline ML lokal; LLM boleh menyusul ketika baseline tidak memadai dan evaluasi membuktikan peningkatan.

### 5. Architecture Decision Record (ADR)

ADR mencatat konteks keputusan, alternatif, keputusan, konsekuensi, validasi, dan trigger review. ADR harus dapat dibantah lewat pengujian: misalnya pilih FastAPI jika integration overhead dan kemampuan tim lebih sesuai; validasi dengan prototype dan dokumentasi open-source, bukan dengan asumsi.

## Studi kasus dalam capstone

Contoh keputusan: membandingkan classifier lokal Naive Bayes, hosted LLM, dan aturan keyword. Saat data sensitif, biaya rendah, dan bahasa domain sempit, baseline lokal bisa dipilih untuk MVP; dampak accuracy dan false routing tetap diuji.

## Kontrak kualitas dan keamanan

- Tiga strategi AI dibandingkan dengan bobot eksplisit dan rasional penilaian.
- ADR memuat alternatif yang ditolak beserta konsekuensinya.
- Dependency dan lisensi utama dicatat tanpa hardcoded API key.
- Ada rencana validasi berbasis pengukuran, bukan hanya opini.

**Inti pembelajaran:** kompetensi dinilai dari alasan dan bukti keputusan, bukan hafalan istilah. Materi ini merupakan penjelasan praktis untuk belajar mandiri, bukan salinan KUK resmi.

## Referensi primer

- https://docs.github.com/en/code-security/supply-chain-security
- https://fastapi.tiangolo.com/
- https://docs.python.org/3/library/venv.html

[Mulai praktikum](lab-guide.md) · [Latihan](exercises.md)
