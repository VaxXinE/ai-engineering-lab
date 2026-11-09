# Worked Examples — Data ingestion sebagai kontrak sistem yang idempotent

Contoh ini diselesaikan langkah demi langkah. Bacalah **sebelum** mengerjakan latihan, lalu tutup dokumen dan ulangi reasoning dari awal. Tidak ada klaim eksekusi kode/tes baru pada file ini.

## Contoh 1: Idempotent import di PostgreSQL

**Masalah:** Ada dua event dengan ID sama dari source yang sama. Saat import ulang, row tidak boleh bertambah.

**Solusi dan reasoning:**

1. Rancang UNIQUE(tenant_id, source_event_id) untuk mencegah duplikasi lintas worker.
2. Contoh SQL ilustratif: INSERT INTO meter readings(tenant_id,source_event_id,event_note) VALUES ($1,$2,$3) ON CONFLICT (tenant_id,source_event_id) DO NOTHING;
3. Jika hasil import pertama menerima 3 record berbeda dan kedua input sama, import kedua membuat 0 row baru; laporkan tiga skipped berdasarkan conflict handling yang benar-benar diukur.
4. Negative test: dua tenant boleh memiliki source_event_id sama jika constraint mengikutkan tenant_id, tetapi satu tenant tak boleh duplikat.

**Counterexample / failure mode:** Cek eksistensi lalu insert tanpa constraint tidak aman terhadap race condition dan dapat menghasilkan dua row.

**Self-explanation:** Mengapa langkah kedua diperlukan? Apa konsekuensi jika constraint-nya berubah?

## Contoh 2: Rekonsiliasi partial-accept

**Masalah:** File berisi 100 event sintetis: 91 valid unik, 6 invalid, 3 duplicate.

**Solusi dan reasoning:**

1. Klasifikasikan tiap record tepat satu status: accepted, rejected atau skipped.
2. Total = 91 + 6 + 3 = 100; simpan summary dengan denominator 100.
3. Hitung acceptance rate 91/100 = 91%; rejection rate 6/100 = 6%; skipped rate 3/100 = 3%.
4. Kebijakan kualitas contoh: jika reject rate di atas toleransi proyek, tandai batch perlu review. Threshold bukan standar universal.

**Counterexample / failure mode:** Kesalahan umum: menghitung duplikat sekaligus rejected sehingga jumlah status melebihi row yang benar-benar diterima.

**Self-explanation:** Mengapa langkah kedua diperlukan? Apa konsekuensi jika constraint-nya berubah?


## Progressive practice

- **Guided:** ulangi kedua solusi dan cek nilai/langkah satu per satu.
- **Faded:** ubah satu input atau constraint sendiri, lalu hitung atau rancang ulang solusi.
- **Independent:** terapkan pola pada kasus baru dan catat alternatif serta risiko yang belum tertutup.
- **Verification:** untuk kode, jalankan test sendiri; untuk hitungan, cek ulang dengan perhitungan independen.

[Lanjut knowledge check](knowledge-check.md) · [Latihan utama](exercises.md)
