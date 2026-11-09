# Deep Dive — Struktur Data: memilih berdasarkan operasi dan beban

**Target:** setelah modul, lo dapat mempertahankan pilihan desain melalui contoh dan kontra-contoh, bukan sekadar mengingat istilah.

## Learning outcomes

1. Memilih list/set/dict/deque untuk workload yang konkret dan menjelaskan kompleksitasnya.
2. Menganalisis solusi O(n²) dibanding O(n) pada deduplikasi.
3. Membangun invariant untuk pengelompokan dan status record.
4. Menentukan batas ukuran batch untuk mencegah memory exhaustion.

## Pembahasan konsep dan trade-off

### 1. Operasi dahulu, struktur belakangan

Pertanyaan pertama bukan 'pakai dict atau list?' tetapi operasi apa yang paling sering terjadi. Untuk antrean FIFO, collections.deque memudahkan popleft dibanding list.pop(0) yang menggeser elemen. Untuk membership ID, set biasanya lookup O(1) average tetapi memakai memori ekstra. Untuk mempertahankan urutan asli dan duplikat, list lebih cocok. Untuk mapping ID → record atau aggregation count, dict / Counter dapat memberi kode jelas. Evaluasi data skew, bukan hanya ukuran nominal.

### 2. Time complexity dan invariants

Big-O berbicara tentang pertumbuhan, bukan benchmark detik. Deduplikasi nested-loop membandingkan tiap record dengan semua record sebelumnya, biaya O(n²). Dengan set seen_ids, satu scan O(n) average; trade-off memori O(n). Tulis invariant: setelah memproses k input, setiap ID yang sudah terlihat disimpan tepat satu kali. Invariant ini memberi dasar unit test untuk empty, duplicate, dan collision scenario.

### 3. Aggregation tanpa memori berlebih

Record bisa diproses streaming menggunakan iterator ketika file besar. Untuk ringkasan count per kelas, gunakan Counter tanpa menyimpan semua message. Namun jika perlu audit full row, catat storage persisten yang sesuai dan retention, bukan memori proses. Chunk processing harus menjaga consistency boundary dan checksum serta mampu resume dari checkpoint.

### 4. Unicode dan normalization

Casefold lebih kuat daripada lower untuk beberapa teks, tetapi normalisasi tidak boleh diam-diam membuang makna. Misal 'refund' dan 'refund?' dapat dianggap setara untuk dedup tertentu, tetapi angka transaksi mungkin penting. Selalu bedakan identitas record (event_id) dari kemiripan isi pesan; dua pelanggan mengirim teks yang sama bukan berarti event yang sama.

### 5. Concurrency dan security

Set/dict dalam satu proses tidak menjamin konsistensi dua worker. Saat concurrency meningkat, uniqueness DB constraint tetap diperlukan. Input attacker dapat memaksa memory exhaustion dengan batch terlalu besar; enforce limit di API, parser, dan queue. Hindari menyimpan seluruh file ketika streaming cukup. Pengujian memuat batas input dan timeout.

## Aplikasi dalam AI Customer Intelligence

Pikirkan perubahan berikut: traffic 10 kali lebih tinggi, pelanggan memakai dua tenant, pengguna dapat memasukkan teks tidak tepercaya, dan AI service suatu saat mati. Desain mana yang tetap aman? Apa yang mesti diubah? Tuliskan konsekuensi pada kode, data, UX, keamanan, dan monitoring.

## Bacaan primer

- https://docs.python.org/3/tutorial/datastructures.html
- https://docs.python.org/3/library/collections.html

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md)
