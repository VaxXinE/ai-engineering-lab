# Teori — Week 03: Data Ingestion & ETL

**Tujuan:** Memindahkan dataset pesan pelanggan sintetis ke storage secara konsisten, audit-able, dan aman diulang.

## Konsep dan keputusan engineering

### 1. Data contract dan lineage

Sebelum mengimpor data, definisikan sumber, pemilik, timestamp, tipe kolom, allowed values, unique identifier, dan aturan retensi. Kontrak input merupakan batas kompatibilitas. Data lineage menjawab dari file mana record berasal, siapa/apa yang memproses, dan transformasi apa yang diterapkan.

### 2. ETL versus ELT

ETL membersihkan dan mentransformasikan sebelum load; ELT memuat data ke staging terkontrol lalu mentransformasikan. Untuk CRM kecil, ETL sederhana cukup; untuk volume lebih besar, staging membantu audit dan reprocessing. Hindari menyimpan data invalid ke tabel produksi tanpa status dan guard.

### 3. Idempotency dan batch processing

Import yang sama dijalankan dua kali seharusnya menghasilkan kondisi data sama atau kegagalan yang jelas, bukan duplikasi. Pakai stable ID atau checksum, uniqueness constraint, dan conflict strategy yang ditentukan. Satu transaksi per batch menjaga konsistensi, tetapi batch besar mungkin perlu chunking dan checkpoint.

### 4. CSV safety dan database transaction

Validasi header, encoding UTF-8, file size, row length, dan karakter tak terduga. Saat hasil diekspor ke spreadsheet, awasi formula injection pada field yang dimulai =, +, -, @. Query harus memakai parameter binding. Jangan membangun SQL dengan concatenation input. Pada kegagalan batch, definisikan all-or-nothing atau partial-accept dengan log penerimaan.

### 5. Operational feedback

Hasil import harus melaporkan accepted, rejected, skipped/duplicate, durasi, batch ID, alasan reject yang tidak membocorkan data sensitif, dan langkah pemulihan. Pengguna harus bisa memeriksa jumlah total input = accepted + rejected + skipped.

## Studi kasus dalam capstone

CSV sintetis dengan kolom inquiry_id, message, received_at, source. Dua baris punya inquiry_id sama: loader menolak duplikasi atau melakukan upsert sesuai kebijakan yang terdokumentasi, tidak diam-diam menambah dua inquiry.

## Kontrak kualitas dan keamanan

- CSV valid dapat diproses dengan hasil terhitung.
- Input invalid ditolak dan dilaporkan tanpa menyimpan record corrupt.
- Menjalankan batch yang sama dua kali tidak menghasilkan duplikasi.
- Query parameterized dan transaction behavior teruji.

**Inti pembelajaran:** kompetensi dinilai dari alasan dan bukti keputusan, bukan hafalan istilah. Materi ini merupakan penjelasan praktis untuk belajar mandiri, bukan salinan KUK resmi.

## Referensi primer

- https://docs.python.org/3/library/csv.html
- https://www.postgresql.org/docs/current/ddl-constraints.html
- https://cheatsheetseries.owasp.org/cheatsheets/CSV_Injection_Prevention_Cheat_Sheet.html

[Mulai praktikum](lab-guide.md) · [Latihan](exercises.md)
