# Worked Examples — Model data yang mencegah kehilangan historis prediksi dan celah akses

Contoh **ilustratif** untuk pemahaman dan code review. Cuplikan kode tidak otomatis sudah dieksekusi di repository; saat praktikum jalankan unit/integration tests sebelum memberi status passed.

## Contoh 1: Skema SQL minimal dengan constraint

**Masalah:** Satu tenant tidak boleh punya dua event dengan source_event_id sama.

**Solusi bertahap:**

1. Contoh SQL ilustratif (bukan migration yang sudah dijalankan):

```sql
CREATE TABLE inquiries (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  tenant_id uuid NOT NULL,
  source_event_id text NOT NULL,
  message text NOT NULL CHECK (char_length(message) BETWEEN 1 AND 500),
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (tenant_id, source_event_id)
);
```

2. Buat dua row dengan source_event_id sama dalam tenant sama → database menolak yang kedua.

3. Buat source_event_id sama dengan tenant berbeda → unik gabungan masih terpenuhi.

4. Jika tenant_id harus valid secara relasional, tambahkan FK yang mengarah tenants(id), bukan mengandalkan UUID.

**Kesalahan yang harus dihindari:** Unique(source_event_id) tanpa tenant_id bisa salah menolak event antarorganisasi yang ID sumbernya sama.

**Teach-back:** jelaskan mengapa langkah 1→2→3 menghasilkan solusi dan bagaimana kegagalannya diuji.

## Contoh 2: Optimistic lock saat dua agent mengedit

**Masalah:** Agent A dan B membaca row version=3; A menyimpan dahulu, B menyimpan dengan data lama.

**Solusi bertahap:**

1. Saat A update: UPDATE inquiries SET status='reviewed', version=4 WHERE id=? AND version=3; affected 1.

2. B mencoba WHERE version=3 setelah A commit; affected 0, artinya konflik, bukan sukses.

3. Backend mengirim HTTP 409 dan UI menawarkan refresh serta mempertahankan alasan review yang belum disimpan.

4. Simpan ReviewEvent dalam transaksi yang sama dengan status update supaya audit history tidak hilang.

**Kesalahan yang harus dihindari:** Last-write-wins diam-diam menghilangkan keputusan A atau B dan membuat audit tidak akurat.

**Teach-back:** jelaskan mengapa langkah 1→2→3 menghasilkan solusi dan bagaimana kegagalannya diuji.


## Latihan dengan scaffolding berkurang

1. **Worked:** baca contoh lengkap dan hitung/trace secara manual.
2. **Faded:** ulangi dengan satu langkah kosong dan isi reasoning sendiri.
3. **Independent:** ganti constraint (volume, concurrency, tenant, outage) dan susun solusi baru.
4. **Evidence:** rekam hasil test nyata dan dampak trade-off di dalam PR.

[Lihat latihan](exercises.md)
