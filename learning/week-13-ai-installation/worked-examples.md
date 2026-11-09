# Worked Examples — Instalasi AI yang reproducible dan tidak menyebarkan secret

Semua langkah berikut adalah **contoh pembelajaran**, bukan laporan pelaksanaan. Uji ulang dengan alat yang tersedia saat fase praktik.

## Contoh 1: Compose service boundaries (potongan konfigurasi)

**Problem:** Backend harus bisa berbicara dengan PostgreSQL tanpa mengekspose DB ke internet.

1. Contoh YAML ilustratif:

```yaml
services:
  api:
    build: ./backend
    environment:
      DATABASE_HOST: db
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:17
    environment:
      POSTGRES_DB: app
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U postgres -d app']
      interval: 5s
      retries: 5
```

Catatan: ini **fragmen**, bukan compose lengkap atau production-safe. Image/DB users/secrets harus dikonfigurasi dan dikunci saat implementasi.

2. Tanpa `ports:` pada db, port DB tidak dipublish ke host secara default; service tetap bisa bicara di jaringan compose.

3. Tambahkan secret injection, volume, non-root policy, resource controls, migrations, dan health tests ketika membuat aplikasi.

4. Cek actual service health dan koneksi menggunakan test sintetis; jangan menganggap depends_on sudah menjamin semua migration selesai.

**Common failure:** Menaruh password root Postgres dalam repository atau membuka 5432 ke 0.0.0.0 tanpa kebutuhan menciptakan risiko data exposure.

**Why-question:** kenapa langkah sebelumnya mencegah risiko tersebut dan test apa yang membuktikannya?

## Contoh 2: Rollback aplikasi vs database

**Problem:** Aplikasi v2 memakai field baru, migration sudah dijalankan, lalu bug mendesak rollback ke v1.

1. Sebelum deploy, pastikan v1 bisa tetap membaca schema setelah migrasi tambahan (expand phase).

2. Jalankan schema migration yang backward-compatible dulu, kemudian deploy aplikasi baru.

3. Jika bug, kembalikan image v1 (dengan versi jelas) dan verifikasi endpoint serta data tetap terbaca.

4. Jika migration destruktif telah dilakukan, rollback image saja mungkin tidak cukup; pemulihan dari backup/tested migration path dibutuhkan.

**Common failure:** Membuat DROP COLUMN pada migration v2 sebelum memastikan v1 tidak membutuhkannya dapat menjadikan rollback darurat gagal.

**Why-question:** kenapa langkah sebelumnya mencegah risiko tersebut dan test apa yang membuktikannya?

## Latihan bertahap

- **Fully worked:** ulas reasoning semua langkah.
- **Faded:** ulang tanpa melihat langkah kedua.
- **Independent:** pindahkan solusi ke studi kasus baru dan buat test plan.
- **Reflection:** catat apa yang belum bisa dijamin dari evidence yang tersedia.

[Latihan mandiri](exercises.md)
