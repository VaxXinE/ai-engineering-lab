# Praktikum — Week 03: Data Ingestion & ETL

**Status:** rancangan latihan. Belum ada klaim bahwa langkah di bawah berhasil dijalankan.

## Konteks

CSV sintetis dengan kolom meter_reading_id, event_note, received_at, source. Dua baris punya meter_reading_id sama: loader menolak duplikasi atau melakukan upsert sesuai kebijakan yang terdokumentasi, tidak diam-diam menambah dua meter reading.

**Prasyarat:** Modul 1 dan 2; Python standard library CSV; dasar SQL.  
**Dataset:** data sintetis dari capstone; jangan memakai data perusahaan atau kredensial sungguhan.

## Langkah kerja

1. Buat docs/data-dictionary.md yang mendefinisikan meter_reading_id, event_note, received_at, source, schema version, contoh valid dan tidak valid.

2. Generate sedikitnya 100 pesan **sintetis**, tidak menggunakan data kantor atau device nyata; simpan generator/seed dan keterangan dataset.

3. Implementasikan parser CSV yang memvalidasi header, encoding, field wajib, jumlah kolom, dan panjang input.

4. Buat tabel staging atau database lokal (SQLite diperbolehkan sebagai langkah awal); gunakan parameterized insert dan unique constraint.

5. Jalankan import satu kali, ulangi import file yang sama, lalu verifikasi kebijakan idempotency.

6. Simpan import summary JSON (counts, batch id, error categories) tanpa menyimpan isi pesan pribadi di log.

## Test plan minimal

1. Satu row valid dan satu row missing required field.
2. Input duplicate meter_reading_id pada file sama dan import ulang.
3. File tidak ada, kolom berlebih, file terlalu besar dan interruption skenario.
4. Jumlah accepted + rejected + skipped sama dengan jumlah rows input.

## Acceptance criteria

- [ ] CSV valid dapat diproses dengan hasil terhitung.
- [ ] Input invalid ditolak dan dilaporkan tanpa menyimpan record corrupt.
- [ ] Menjalankan batch yang sama dua kali tidak menghasilkan duplikasi.
- [ ] Query parameterized dan transaction behavior teruji.

## Bukti yang disimpan setelah praktik

1. Source code / artefak desain serta alasan keputusan yang dibuat sendiri.
2. Cara menjalankan atau mereproduksi hasil (versi environment dan perintah aktual).
3. Test report: perintah, hasil sesungguhnya, sampel negatif dan edge cases.
4. Analisis risiko keamanan, privasi, performa, serta keterbatasan yang belum ditangani.
5. Link PR/commit ke [matriks bukti](../../certification/evidence-matrix.md).

## Syarat selesai

**Belum selesai** hanya dengan membaca dokumen ini. Tandai selesai setelah implementasi diverifikasi dan evidence tersimpan; uji kompetensi BNSP tetap dilakukan oleh LSP yang berwenang.

[Latihan tambahan](exercises.md) · [Simulasi asesmen](assessment.md)
