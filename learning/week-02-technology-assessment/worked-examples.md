# Worked Examples — Membuat keputusan teknologi yang bisa diuji dan dipertanggungjawabkan

Contoh ini diselesaikan langkah demi langkah. Bacalah **sebelum** mengerjakan latihan, lalu tutup dokumen dan ulangi reasoning dari awal. Tidak ada klaim eksekusi kode/tes baru pada file ini.

## Contoh 1: Contoh weighted decision matrix yang transparan

**Masalah:** Tiga opsi: A rule-based, B ML lokal, C hosted LLM. Bobot: privacy 30, quality 30, cost 20, ease 20 (jumlah 100). Skor asumsi 1–5: A=[5,2,5,5], B=[5,4,4,3], C=[2,5,2,4].

**Solusi dan reasoning:**

1. A = 0.30*5 + 0.30*2 + 0.20*5 + 0.20*5 = 4.10.
2. B = 0.30*5 + 0.30*4 + 0.20*4 + 0.20*3 = 4.10.
3. C = 0.30*2 + 0.30*5 + 0.20*2 + 0.20*4 = 3.30.
4. A dan B seri berdasarkan asumsi; pilih eksperimen terukur untuk memisahkan keduanya. Jika privacy adalah hard constraint yang melarang transfer data, opsi C gugur sebelum scoring.

**Counterexample / failure mode:** Jangan mencatat skor sebagai fakta pasar. Angka di atas adalah simulasi metode evaluasi dan perlu bukti teknis.

**Self-explanation:** Mengapa langkah kedua diperlukan? Apa konsekuensi jika constraint-nya berubah?

## Contoh 2: ADR pendek untuk model local-first

**Masalah:** Sebuah dashboard energi perlu energy anomaly scoring, tanpa mengirim data telemetri ke pihak luar. Tentukan keputusan yang masuk akal.

**Solusi dan reasoning:**

1. Context: data policy melarang data raw keluar; 30–50 req/menit; tiga kategori dan budget rendah.
2. Options: rules, local ML, hosted LLM. Hosted LLM tidak memenuhi hard constraint, sehingga tidak layak.
3. Decision: mulai model lokal sebagai baseline; rule-based tetap jadi comparator; bukan klaim final paling akurat.
4. Verification: held-out macro F1, warning recall, p95 latency, monitoring drift dan ability to rollback; if thresholds fail, evaluasi opsi lain yang memenuhi privacy.

**Counterexample / failure mode:** ADR buruk hanya menulis 'pakai FastAPI karena cepat dan populer' tanpa constraint, trade-off, atau bukti.

**Self-explanation:** Mengapa langkah kedua diperlukan? Apa konsekuensi jika constraint-nya berubah?


## Progressive practice

- **Guided:** ulangi kedua solusi dan cek nilai/langkah satu per satu.
- **Faded:** ubah satu input atau constraint sendiri, lalu hitung atau rancang ulang solusi.
- **Independent:** terapkan pola pada kasus baru dan catat alternatif serta risiko yang belum tertutup.
- **Verification:** untuk kode, jalankan test sendiri; untuk hitungan, cek ulang dengan perhitungan independen.

[Lanjut knowledge check](knowledge-check.md) · [Latihan utama](exercises.md)
