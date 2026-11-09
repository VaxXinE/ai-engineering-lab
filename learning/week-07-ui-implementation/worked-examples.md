# Worked Examples — Mengubah UX menjadi frontend state machine yang tepercaya

Contoh **ilustratif** untuk pemahaman dan code review. Cuplikan kode tidak otomatis sudah dieksekusi di repository; saat praktikum jalankan unit/integration tests sebelum memberi status passed.

## Contoh 1: TypeScript discriminated union

**Masalah:** Dashboard bisa idle/loading/success/error. Hindari kombinasi state tidak valid.

**Solusi bertahap:**

1. Definisikan satu field status untuk membedakan setiap variant.

2. Contoh TypeScript ilustratif:

```ts
type Inquiry = { id: string; message: string };
type Result =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; inquiries: Inquiry[] }
  | { status: 'error'; message: string };
function renderSummary(result: Result): string {
  switch (result.status) {
    case 'idle': return 'Siap';
    case 'loading': return 'Memuat';
    case 'success': return `${result.inquiries.length} data`;
    case 'error': return result.message;
  }
}
```

3. Pada branch success, compiler tahu inquiries tersedia; branch error tidak bisa keliru mengaksesnya.

4. Test setiap variant dan empty array (success tetapi tidak ada hasil).

**Kesalahan yang harus dihindari:** Menggunakan dua boolean isLoading dan hasError memungkinkan state kontradiktif yang sulit direproduksi.

**Teach-back:** jelaskan mengapa langkah 1→2→3 menghasilkan solusi dan bagaimana kegagalannya diuji.

## Contoh 2: Dua request filter datang tak berurutan

**Masalah:** User mengaktifkan filter support, kemudian sales. Response support datang setelah response sales.

**Solusi bertahap:**

1. Simpan AbortController untuk request aktif; ketika filter berubah, abort request lama.

2. Gunakan request key / sequence id dan hanya update UI jika response cocok filter terbaru.

3. Test dengan deferred promises: request kedua resolve lebih dulu; data pertama tidak boleh menimpa state sales.

4. Backend tetap wajib membatasi hasil berdasarkan tenant; filter frontend tidak cukup untuk authorization.

**Kesalahan yang harus dihindari:** Mengandalkan response order dari network adalah race condition, bukan asumsi yang aman.

**Teach-back:** jelaskan mengapa langkah 1→2→3 menghasilkan solusi dan bagaimana kegagalannya diuji.


## Latihan dengan scaffolding berkurang

1. **Worked:** baca contoh lengkap dan hitung/trace secara manual.
2. **Faded:** ulangi dengan satu langkah kosong dan isi reasoning sendiri.
3. **Independent:** ganti constraint (volume, concurrency, tenant, outage) dan susun solusi baru.
4. **Evidence:** rekam hasil test nyata dan dampak trade-off di dalam PR.

[Lihat latihan](exercises.md)
