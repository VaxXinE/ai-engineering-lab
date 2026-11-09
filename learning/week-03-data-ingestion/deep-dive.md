# Deep Dive — Data ingestion sebagai kontrak sistem yang idempotent

> Materi lanjutan untuk pembaca yang sudah memahami software engineering dasar. **Contoh hitungan adalah ilustrasi**, bukan hasil pengujian sistem production.

## Learning outcomes yang harus bisa dibuktikan

1. Merancang CSV ingestion dengan schema, source lineage, dan transaksi.
2. Membedakan ETL, ELT, upsert, strict reject, dan partial accept.
3. Menguji idempotency dengan import batch sama dua kali.
4. Menjelaskan risiko CSV formula injection dan penggunaan prepared statements.

## Penjelasan konsep secara mendalam

### 1. Definisikan sumber dan data contract sebelum coding

Dataset telemetri numerik memiliki site_id, meter_id, source_event_id, timestamp UTC, energy_kwh per interval, voltage_v, dan current_a. Data dictionary harus menjelaskan satuan, frekuensi, serta rentang simulasi. Tentukan field wajib, tipe, encoding, range panjang, dan pemilik data. Source lineage menyimpan asal input, schema_version dan timestamp import agar kesalahan bisa diusut. Tanpa kontrak, perubahan kolom mendadak dapat diam-diam memindahkan data yang salah ke tabel yang tampak valid.

### 2. ETL versus ELT dan staging

ETL mentransformasi record sebelum dimuat ke storage target. ELT memuat raw data yang diizinkan ke staging lalu mentransformasi, cocok untuk kebutuhan traceability besar. Untuk demo gunakan ETL kecil yang memvalidasi sebelum insert; untuk scale, staging perlu retention dan access controls karena raw record mungkin sensitif. Jangan menyimpan raw PII tanpa dasar legal; pada lab gunakan data sintetis.

### 3. Atomic import versus partial accept

All-or-nothing transaction menggagalkan seluruh batch jika satu record invalid, memberi konsistensi kuat namun dapat menghambat batch besar. Partial accept memproses record valid dan menyimpan statistik penolakan sehingga operasional lebih fleksibel, tetapi membutuhkan rekonsiliasi. Tentukan kebijakan per batch dan error contract sebelum menulis kode. Untuk DB gunakan transaction dengan rollback pada kondisi yang tidak bisa dipulihkan.

### 4. Idempotency dan at-least-once delivery

Saat ingestion worker mengalami timeout setelah database commit, event dapat dikirim ulang. Unique key yang benar adalah **(site_id,meter_id,source_event_id)**. Exact repeat dapat di-skip, tetapi ID sama dengan payload berbeda harus di-reject/quarantine agar pembacaan historis tidak diam-diam ditimpa. Concurrent writers tetap memerlukan UNIQUE constraint; check-before-insert saja tidak aman.

### 5. Parsing, encoding dan ancaman injection

Hindari membuat SQL dari string CSV. Prepared statements memisahkan query structure dari data. Pastikan delimiter, quoting, encoding, BOM, extra columns, null bytes, file size dan row count ditangani. CSV formula injection relevan ketika data diekspor lalu dibuka spreadsheet: nilai yang diawali karakter formula bisa diproses sebagai rumus. Selalu gunakan strategi output sesuai target export; jangan menganggap CSV string aman di semua konteks.

### 6. Observability dan kualitas hasil

Setiap batch harus melaporkan received, accepted, rejected, skipped serta alasan kategori error tanpa menuliskan data pribadi. Rekonsiliasi: received = accepted + rejected + skipped (untuk kebijakan mutually exclusive). Simpan batch ID, source checksum, versi skema dan durasi aktual. Beri cara replay dan rollback yang jelas, tidak sekadar mencatat 'import success'.

## Miskonsepsi yang perlu diwaspadai

- Idempotency sama dengan exactly-once delivery → tidak; delivery bisa diulang, efek proses dibuat konsisten.
- Validator di Python cukup untuk mencegah duplikat → DB constraint tetap diperlukan untuk race.
- Semua error sebaiknya membuat seluruh batch gagal → tergantung kontrak operasi.
- CSV itu hanya teks, pasti aman → data berbahaya saat dipakai pada sistem lain termasuk spreadsheet.
- Menyimpan semua raw data memperbaiki audit → dapat memperbesar exposure PII.

## Transfer ke profesi full-stack

Ambil satu kebutuhan dari capstone [AI Smart Energy Monitoring](../../projects/ai-energy-intelligence/README.md). Jelaskan **data apa yang tepercaya, aturan bisnis mana yang harus deterministik, apa yang bisa diprediksi AI, bagaimana failure ditangani, dan bagaimana keputusan diuji**. Jangan menyatakan modul selesai hanya dengan menyalin contoh.

## Bacaan lanjutan (dokumentasi dan pembelajaran primer)

- https://docs.python.org/3/library/csv.html
- https://www.postgresql.org/docs/current/ddl-constraints.html
- https://cheatsheetseries.owasp.org/cheatsheets/CSV_Injection_Prevention_Cheat_Sheet.html

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md) · [Lab](lab-guide.md)
