# Worked Examples — Mengubah proyek menjadi bukti kompetensi yang dapat diuji

Semua langkah berikut adalah **contoh pembelajaran**, bukan laporan pelaksanaan. Uji ulang dengan alat yang tersedia saat fase praktik.

## Contoh 1: Evidence mapping untuk unit AI integration

**Problem:** Peserta punya FastAPI endpoint yang memanggil classifier, tetapi tak ada tes timeout maupun izin akses.

1. Catat unit Published: Mengintegrasikan Komponen Solusi AI (kode sementara berdasarkan halaman LSP).

2. Evidence awal: link ke implementation commit dan API schema; status implemented, not verified.

3. Gap: missing timeout path, invalid model output, cross-tenant authorization tests.

4. Rencana: tambah negative integration tests dan simpan output aktual; kemudian review dengan elemen/KUK yang diberikan LSP.

5. Jangan menandai kompeten hanya karena endpoint mengembalikan 200 pada satu contoh.

**Common failure:** Mengubah status unit menjadi verified berdasarkan README saja menghilangkan nilai matriks bukti.

**Why-question:** kenapa langkah sebelumnya mencegah risiko tersebut dan test apa yang membuktikannya?

## Contoh 2: Draft demo 20 menit nonresmi

**Problem:** Mempresentasikan capstone dengan fokus dua skema, bukan menampilkan semua file repo.

1. Menit 0–3: use case dan requirement; Menit 3–6: ingestion, validation, data quality.

2. Menit 6–10: UI/API/DB architecture, authorization dan model selection.

3. Menit 10–14: inferensi dan human review; tunjukkan satu false prediction atau abstain.

4. Menit 14–18: test outage/rollback atau maintenance drill yang sudah dijalankan; Menit 18–20: bukti commit/tests, risiko dan hal belum siap.

5. Waktu di atas sekadar latihan komunikasi; ikuti metode penilaian resmi yang diminta asesor.

**Common failure:** Demo yang hanya menunjukkan UI cantik tanpa testing/maintenance kurang membuktikan dua skema.

**Why-question:** kenapa langkah sebelumnya mencegah risiko tersebut dan test apa yang membuktikannya?

## Latihan bertahap

- **Fully worked:** ulas reasoning semua langkah.
- **Faded:** ulang tanpa melihat langkah kedua.
- **Independent:** pindahkan solusi ke studi kasus baru dan buat test plan.
- **Reflection:** catat apa yang belum bisa dijamin dari evidence yang tersedia.

[Latihan mandiri](exercises.md)
