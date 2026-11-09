# Worked Examples — UX AI: mengurangi kesalahan keputusan manusia, bukan sekadar membuat dashboard rapi

Contoh **ilustratif** untuk pemahaman dan code review. Cuplikan kode tidak otomatis sudah dieksekusi di repository; saat praktikum jalankan unit/integration tests sebelum memberi status passed.

## Contoh 1: Salah label dan audit state

**Masalah:** Pesan 'tidak bisa tarik laporan' diprediksi normal, operator mengubah menjadi warning.

**Solusi bertahap:**

1. Inbox menampilkan chip 'Prediksi: normal — belum ditinjau', bukan 'Device adalah normal'.

2. Detail view menampilkan pesan dan pilihan warning/fault/normal, tombol 'Simpan koreksi' dengan alasan.

3. Setelah API success, status menjadi 'Ditinjau: warning' sambil mempertahankan prediksi awal di riwayat.

4. Jika API error atau permission ditolak, draft alasan tidak hilang dan user mendapat feedback.

**Kesalahan yang harus dihindari:** Jika UI langsung mengganti predicted_label tanpa audit, data evaluasi model hilang.

**Teach-back:** jelaskan mengapa langkah 1→2→3 menghasilkan solusi dan bagaimana kegagalannya diuji.

## Contoh 2: Desain abstain dan kegagalan API

**Masalah:** Model tidak mengenali pesan berbahasa campuran, lalu hasil abstain; sesaat kemudian layanan inference timeout.

**Solusi bertahap:**

1. Untuk abstain, tampilkan 'Belum dapat diklasifikasikan' dan arahkan ke review queue manusia.

2. Untuk timeout, tampilkan 'Klasifikasi otomatis belum tersedia'; meter reading tetap bisa dibuka.

3. Jangan tampilkan tombol retry agresif yang menciptakan duplikasi; server tetap memvalidasi idempotency.

4. Uji dengan keyboard: tab ke field kategori, pilih nilai, kirim, periksa fokus dan pesan konfirmasi.

**Kesalahan yang harus dihindari:** Menyamakan abstain dengan fault akan merusak perhitungan kualitas model dan pengalaman warning.

**Teach-back:** jelaskan mengapa langkah 1→2→3 menghasilkan solusi dan bagaimana kegagalannya diuji.


## Latihan dengan scaffolding berkurang

1. **Worked:** baca contoh lengkap dan hitung/trace secara manual.
2. **Faded:** ulangi dengan satu langkah kosong dan isi reasoning sendiri.
3. **Independent:** ganti constraint (volume, concurrency, tenant, outage) dan susun solusi baru.
4. **Evidence:** rekam hasil test nyata dan dampak trade-off di dalam PR.

[Lihat latihan](exercises.md)
