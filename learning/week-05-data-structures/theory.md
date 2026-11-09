# Teori — Week 05: Data Structures, Algorithms & Complexity

**Tujuan:** Memilih struktur data agar pipeline dan API tidak berubah menjadi bottleneck saat record bertambah.

## Konsep dan keputusan engineering

### 1. Pemilihan struktur data

List mempertahankan urutan, cocok untuk sequential traversal; dict memberi lookup keyed rata-rata O(1) pada kasus lazim; set cocok untuk membership/dedup; deque untuk queue FIFO. Pemilihan harus mempertimbangkan memory, order, key uniqueness, dan kebutuhan concurrency.

### 2. Complexity analysis

Big O mengukur tingkat pertumbuhan resource terhadap input, bukan durasi absolut. Lookup berulang pada list menghasilkan O(n²) untuk nested scans; memindahkan lookup ke set sering memangkasnya mendekati O(n), dengan trade-off memori tambahan. Ukur juga data-skew dan worst cases.

### 3. Data aggregation

Untuk klasifikasi pesan, diperlukan grouping by category, penghitungan statistik, dan dedup per inquiry_id. Hindari mengubah collection saat iterasi, serta pikirkan stable ordering agar hasil deterministik dalam testing. Streaming/chunking mengurangi penggunaan memori untuk file besar.

### 4. Determinism dan testability

Pakai input/output yang jelas dan fungsi murni untuk logic pengolahan data. Test properti sederhana (unique IDs, counts konsisten) lebih kuat daripada hanya contoh happy path. Pertimbangkan Unicode normalization saat membandingkan teks untuk duplicate detection.

### 5. Security pada data structures

Resource exhaustion terjadi saat input tak dibatasi. Validasi ukuran batch, panjang teks, dan jumlah key; jangan menyimpan semua data besar dalam memori jika chunked processing cukup. Pilih struktur data berdasarkan karakteristik beban nyata.

## Studi kasus dalam capstone

100.000 ID: memeriksa setiap ID dengan 'id in list' berulang memiliki biaya yang tumbuh jauh lebih cepat daripada menyimpan ID yang sudah terlihat dalam set. Namun set memakai memori lebih dan tidak menyimpan frekuensi; Counter lebih tepat untuk kebutuhan agregasi.

## Kontrak kualitas dan keamanan

- Implementasi menyimpan satu item per unique ID dan punya aturan 'first wins' atau 'last wins' jelas.
- Semua input edge case diuji.
- Analisis Big O dan memory trade-off ditulis.
- Benchmark menyertakan lingkungan, jumlah record, dan metode.

**Inti pembelajaran:** kompetensi dinilai dari alasan dan bukti keputusan, bukan hafalan istilah. Materi ini merupakan penjelasan praktis untuk belajar mandiri, bukan salinan KUK resmi.

## Referensi primer

- https://docs.python.org/3/tutorial/datastructures.html
- https://docs.python.org/3/library/collections.html
- https://docs.python.org/3/library/time.html

[Mulai praktikum](lab-guide.md) · [Latihan](exercises.md)
