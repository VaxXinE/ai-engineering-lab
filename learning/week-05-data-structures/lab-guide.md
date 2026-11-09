# Praktikum — Week 05: Data Structures, Algorithms & Complexity

**Status:** rancangan latihan. Belum ada klaim bahwa langkah di bawah berhasil dijalankan.

## Konteks

100.000 ID: memeriksa setiap ID dengan 'id in list' berulang memiliki biaya yang tumbuh jauh lebih cepat daripada menyimpan ID yang sudah terlihat dalam set. Namun set memakai memori lebih dan tidak menyimpan frekuensi; Counter lebih tepat untuk kebutuhan agregasi.

**Prasyarat:** Modul 3–4; Python collection types dan dasar fungsi.  
**Dataset:** data sintetis dari capstone; jangan memakai data perusahaan atau kredensial sungguhan.

## Langkah kerja

1. Definisikan kontrak fungsi deduplicate(records), group_by_label(records), dan summarize(records).

2. Implementasikan versi naif list-based dan versi yang menggunakan set/dict; jangan gunakan dataset pribadi.

3. Buat generator pesan sintetis dengan seed tetap untuk 100, 1000, dan 10000 record.

4. Jalankan benchmark menggunakan time.perf_counter di mesin yang sama dan catat spesifikasi serta variasi run.

5. Tambahkan tests untuk empty list, duplicate ID, unknown class, dan stable output ordering.

6. Analisis trade-off memory dan complexity tanpa menyebut benchmark lokal sebagai jaminan performa produksi.

## Test plan minimal

1. Empty collection menghasilkan output valid.
2. Duplikasi deterministik tanpa kehilangan ID berbeda.
3. Group count per label sama dengan total record diterima.
4. Output yang sama untuk input yang sama.

## Acceptance criteria

- [ ] Implementasi menyimpan satu item per unique ID dan punya aturan 'first wins' atau 'last wins' jelas.
- [ ] Semua input edge case diuji.
- [ ] Analisis Big O dan memory trade-off ditulis.
- [ ] Benchmark menyertakan lingkungan, jumlah record, dan metode.

## Bukti yang disimpan setelah praktik

1. Source code / artefak desain serta alasan keputusan yang dibuat sendiri.
2. Cara menjalankan atau mereproduksi hasil (versi environment dan perintah aktual).
3. Test report: perintah, hasil sesungguhnya, sampel negatif dan edge cases.
4. Analisis risiko keamanan, privasi, performa, serta keterbatasan yang belum ditangani.
5. Link PR/commit ke [matriks bukti](../../certification/evidence-matrix.md).

## Syarat selesai

**Belum selesai** hanya dengan membaca dokumen ini. Tandai selesai setelah implementasi diverifikasi dan evidence tersimpan; uji kompetensi BNSP tetap dilakukan oleh LSP yang berwenang.

[Latihan tambahan](exercises.md) · [Simulasi asesmen](assessment.md)
