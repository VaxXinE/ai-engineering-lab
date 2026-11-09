# Worked Examples — Data quality sebagai penghalang sebelum AI, bukan cleanup kosmetik

Contoh ini diselesaikan langkah demi langkah. Bacalah **sebelum** mengerjakan latihan, lalu tutup dokumen dan ulangi reasoning dari awal. Tidak ada klaim eksekusi kode/tes baru pada file ini.

## Contoh 1: Menghitung data quality per tahap

**Masalah:** Dari 200 pesan sintetis, 16 event_note kosong, 4 duplikat event ID, 10 timestamp di luar rentang. Anggap ketiga kelompok tidak overlap.

**Solusi dan reasoning:**

1. Completeness event_note = (200-16)/200 = 92%.
2. Jika validitas mensyaratkan ketiga aturan sekaligus, jumlah lolos = 200-16-4-10 = 170 = 85%.
3. Jika kelompok ternyata overlap, jumlah lolos tidak bisa dihitung hanya dari penjumlahan; butuh pemeriksaan record-level.
4. Laporan harus menyebut asumsi non-overlap, schema_version, dan denominator 200.

**Counterexample / failure mode:** Tidak benar mengatakan 92% completeness sama dengan 92% overall data quality.

**Self-explanation:** Mengapa langkah kedua diperlukan? Apa konsekuensi jika constraint-nya berubah?

## Contoh 2: Leakage akibat preprocessing sebelum split

**Masalah:** Developer menghitung vocabulary dan IDF dari seluruh 1000 pesan, baru membagi 80% train/20% test.

**Solusi dan reasoning:**

1. Karena IDF bergantung frekuensi seluruh teks, statistik test ikut memengaruhi transformasi train.
2. Perbaiki: split terlebih dahulu, fit tokenizer/vectorizer pada train saja, lalu transform validation/test tanpa refit.
3. Jika device mengirim banyak pesan mirip, lakukan group split berdasarkan device agar semantic correlation tidak bocor.
4. Catat limitation: pemeriksaan exact normalized overlap tidak menjamin bebas semantic leakage.

**Counterexample / failure mode:** Menghapus teks yang sama persis saja tidak mencegah semua leakage; perlu mempertimbangkan fitur yang 'melihat masa depan'.

**Self-explanation:** Mengapa langkah kedua diperlukan? Apa konsekuensi jika constraint-nya berubah?


## Progressive practice

- **Guided:** ulangi kedua solusi dan cek nilai/langkah satu per satu.
- **Faded:** ubah satu input atau constraint sendiri, lalu hitung atau rancang ulang solusi.
- **Independent:** terapkan pola pada kasus baru dan catat alternatif serta risiko yang belum tertutup.
- **Verification:** untuk kode, jalankan test sendiri; untuk hitungan, cek ulang dengan perhitungan independen.

[Lanjut knowledge check](knowledge-check.md) · [Latihan utama](exercises.md)
