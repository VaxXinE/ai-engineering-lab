# Knowledge Check & Feedback — Membuat keputusan teknologi yang bisa diuji dan dipertanggungjawabkan

**Petunjuk:** Jawab pertanyaan tanpa melihat `deep-dive.md` atau kode. Setelah itu baru baca kunci dan **alasan jawaban**. Ini latihan belajar mandiri, bukan soal resmi BNSP.

## Retrieval questions

1. Apa beda hard constraint dan weighted preference?
2. Bagaimana mendeteksi bias pada decision matrix?
3. Kenapa security advisory harus dicek sebelum install?
4. Kapan hosted LLM ditolak walau kualitas bahasa bagus?
5. Apa isi minimal ADR?
6. Apa bentuk spike paling kecil untuk memilih backend?

## Pembahasan / kunci untuk self-correction

**1. Apa beda hard constraint dan weighted preference?**

Hard constraint membatalkan opsi meski skor tinggi; preference dapat diperdagangkan sesuai bobot.

**2. Bagaimana mendeteksi bias pada decision matrix?**

Catat definisi skala, bukti skor, pemilik asumsi dan sensitivity terhadap perubahan bobot.

**3. Kenapa security advisory harus dicek sebelum install?**

Nama package, reputasi dan lockfile tidak menjamin tak ada vulnerability atau script berbahaya.

**4. Kapan hosted LLM ditolak walau kualitas bahasa bagus?**

Ketika melanggar data policy, biaya tak terkendali, latency/SLO, atau izin data belum tersedia.

**5. Apa isi minimal ADR?**

Context, options, decision, consequences, verification/rollback criteria.

**6. Apa bentuk spike paling kecil untuk memilih backend?**

Satu endpoint tervalidasi, test async/error, dependency lock dan hasil profiling yang dilabelkan sesuai environment.

## Diagnose misconceptions

- Skor total tertinggi berarti pilihan paling benar → skor bergantung asumsi dan bobot.
- Library populer pasti aman → dependencies tetap bisa rentan dan maintenance bisa berhenti.
- Lebih banyak microservices berarti lebih skalabel → overhead jaringan dan operasional bisa tidak proporsional.
- Tag latest mempermudah maintenance → menyebabkan build tidak reproducible.
- Framework pilihan harus tetap selamanya → ADR menyimpan kondisi perubahan.

## Spaced review (jadwal usulan)

| Waktu | Latihan |
| --- | --- |
| Hari 0 | Jawab 6 soal, analisis kesalahan, perbaiki catatan |
| Hari +1 | Ulangi 3 soal tersulit tanpa melihat jawaban |
| Hari +7 | Campurkan 3 soal modul ini dengan modul berikutnya |
| Hari +21 | Jelaskan konsep pada skenario baru di proyek capstone |

**Rubrik:** mampu menjawab benar saja belum cukup; peserta harus bisa menjelaskan alasan dan menunjukkan bukti praktik. Tandai materi **belum dikuasai** bila tidak mampu menalar kasus baru.

[Deep dive](deep-dive.md) · [Simulasi asesmen](assessment.md)
