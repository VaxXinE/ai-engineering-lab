# Worked Examples — Struktur Data: memilih berdasarkan operasi dan beban

Contoh **ilustratif** untuk pemahaman dan code review. Cuplikan kode tidak otomatis sudah dieksekusi di repository; saat praktikum jalankan unit/integration tests sebelum memberi status passed.

## Contoh 1: Deduplikasi list vs set

**Masalah:** Input sintetis IDs ['a','b','a','c','b']. Kebutuhan: 'first event wins' dan output tetap sesuai urutan pertama.

**Solusi bertahap:**

1. Solusi naïf: untuk setiap row, cari ID di daftar output; semakin besar n, worst case mendekati O(n²).

2. Solusi terarah: siapkan seen=set() dan result=[]; jika id not in seen, tambahkan ke keduanya.

3. Jalankan manual: 'a' masuk; 'b' masuk; 'a' skip; 'c' masuk; 'b' skip. Hasil ['a','b','c'].

4. Kode ilustratif Python:

```python
rows = ['a', 'b', 'a', 'c', 'b']
seen, unique = set(), []
for key in rows:
    if key not in seen:
        seen.add(key)
        unique.append(key)
assert unique == ['a', 'b', 'c']
```

**Kesalahan yang harus dihindari:** Mengubah seen menjadi penyimpanan nama device saja dapat menyatukan dua perangkat dengan nama sama; gunakan stable event ID.

**Teach-back:** jelaskan mengapa langkah 1→2→3 menghasilkan solusi dan bagaimana kegagalannya diuji.

## Contoh 2: Batch 1 juta event — memory versus streaming

**Masalah:** Dataset input 1.000.000 event_note, dengan batas memory kecil dan hanya perlu count per label.

**Solusi bertahap:**

1. Tidak perlu menyimpan semua row: iterasi satu record, validasi lalu perbarui Counter[label].

2. Bila ada tiga label, memory aggregation mendekati konstan terhadap jumlah pesan (selain streaming buffers).

3. Tetap terapkan batas ukuran satu field dan rate, karena satu record sangat besar dapat menghabiskan memory.

4. Untuk dedup global per event ID, seen set O(n) memory; jika terlalu besar pindahkan uniqueness ke database dengan index.

**Kesalahan yang harus dihindari:** Streaming tidak menghapus seluruh kebutuhan memory: parsing, buffering, dan ID set bisa tetap besar.

**Teach-back:** jelaskan mengapa langkah 1→2→3 menghasilkan solusi dan bagaimana kegagalannya diuji.


## Latihan dengan scaffolding berkurang

1. **Worked:** baca contoh lengkap dan hitung/trace secara manual.
2. **Faded:** ulangi dengan satu langkah kosong dan isi reasoning sendiri.
3. **Independent:** ganti constraint (volume, concurrency, tenant, outage) dan susun solusi baru.
4. **Evidence:** rekam hasil test nyata dan dampak trade-off di dalam PR.

[Lihat latihan](exercises.md)
