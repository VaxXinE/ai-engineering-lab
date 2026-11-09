# Worked Examples — Melakukan incident response dan recovery berbasis bukti

Semua langkah berikut adalah **contoh pembelajaran**, bukan laporan pelaksanaan. Uji ulang dengan alat yang tersedia saat fase praktik.

## Contoh 1: Fault injection timeout tanpa merusak data

**Problem:** Untuk satu meter reading sintetis, fake AI adapter selalu melempar TimeoutError.

1. Sebelum uji, snapshot state test DB dan catat meter reading count.

2. Buat 1 meter reading; API harus menyimpannya, lalu AI adapter gagal dengan timeout yang disengaja.

3. Periksa bahwa status berubah ke pending_manual_review dan data tetap ada; log hanya menyimpan request ID serta error class.

4. Pulihkan adapter normal dan jalankan regression test. Bandingkan counts dan audit history terhadap baseline.

**Common failure:** Menghapus meter reading saat AI error berarti coupling salah antara data ingestion dan inference; test harus gagal.

**Why-question:** kenapa langkah sebelumnya mencegah risiko tersebut dan test apa yang membuktikannya?

## Contoh 2: Checklist verifikasi restore

**Problem:** Restore berhasil mengembalikan database test berisi 1200 meter reading dan 1300 prediction, tetapi UI menunjukkan 0 meter reading.

1. Periksa schema dan tenant filter; bisa jadi restored database memakai tenant_id berbeda dari test user.

2. Periksa referential integrity, counts dan accepted credentials tanpa menuliskan password di logs.

3. Jalankan satu read API dengan test tenant yang benar dan satu negative cross-tenant test.

4. Tandai restore sukses hanya jika database **dan** aplikasi memenuhi business invariants yang ditetapkan.

**Common failure:** pg_restore exit code 0 saja belum membuktikan aplikasi dapat beroperasi.

**Why-question:** kenapa langkah sebelumnya mencegah risiko tersebut dan test apa yang membuktikannya?

## Latihan bertahap

- **Fully worked:** ulas reasoning semua langkah.
- **Faded:** ulang tanpa melihat langkah kedua.
- **Independent:** pindahkan solusi ke studi kasus baru dan buat test plan.
- **Reflection:** catat apa yang belum bisa dijamin dari evidence yang tersedia.

[Latihan mandiri](exercises.md)
