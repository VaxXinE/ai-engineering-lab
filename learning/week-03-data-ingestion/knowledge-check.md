# Knowledge Check & Feedback — Data ingestion sebagai kontrak sistem yang idempotent

**Petunjuk:** Jawab pertanyaan tanpa melihat `deep-dive.md` atau kode. Setelah itu baru baca kunci dan **alasan jawaban**. Ini latihan belajar mandiri, bukan soal resmi BNSP.

## Retrieval questions

1. Mengapa menggunakan unique constraint di DB?
2. Apa bedanya upsert dan insert biasa?
3. Kapan partial accept lebih tepat?
4. Jika 91 accepted, 6 rejected, 3 skipped dari 100, apa acceptance rate?
5. Apa bahayanya interpolasi raw CSV ke SQL?
6. Kenapa source event ID dan batch ID berbeda?

## Pembahasan / kunci untuk self-correction

**1. Mengapa menggunakan unique constraint di DB?**

Melindungi integritas dari race, retry, dan bug proses selain validasi aplikasi.

**2. Apa bedanya upsert dan insert biasa?**

Upsert menangani konflik row sesuai kebijakan update/ignore yang eksplisit.

**3. Kapan partial accept lebih tepat?**

Ketika tiap record independen dan laporan reject bisa ditindaklanjuti, bukan saat batch harus atomik.

**4. Jika 91 accepted, 6 rejected, 3 skipped dari 100, apa acceptance rate?**

91%; denominator semua input 100, status mutually exclusive.

**5. Apa bahayanya interpolasi raw CSV ke SQL?**

SQL injection; parameterized statements memisahkan struktur query dan nilainya.

**6. Kenapa source event ID dan batch ID berbeda?**

Event ID mengidentifikasi record untuk dedup; batch ID mengidentifikasi proses import untuk lineage dan audit.

## Diagnose misconceptions

- Idempotency sama dengan exactly-once delivery → tidak; delivery bisa diulang, efek proses dibuat konsisten.
- Validator di Python cukup untuk mencegah duplikat → DB constraint tetap diperlukan untuk race.
- Semua error sebaiknya membuat seluruh batch gagal → tergantung kontrak operasi.
- CSV itu hanya teks, pasti aman → data berbahaya saat dipakai pada sistem lain termasuk spreadsheet.
- Menyimpan semua raw data memperbaiki audit → dapat memperbesar exposure PII.

## Spaced review (jadwal usulan)

| Waktu | Latihan |
| --- | --- |
| Hari 0 | Jawab 6 soal, analisis kesalahan, perbaiki catatan |
| Hari +1 | Ulangi 3 soal tersulit tanpa melihat jawaban |
| Hari +7 | Campurkan 3 soal modul ini dengan modul berikutnya |
| Hari +21 | Jelaskan konsep pada skenario baru di proyek capstone |

**Rubrik:** mampu menjawab benar saja belum cukup; peserta harus bisa menjelaskan alasan dan menunjukkan bukti praktik. Tandai materi **belum dikuasai** bila tidak mampu menalar kasus baru.

[Deep dive](deep-dive.md) · [Simulasi asesmen](assessment.md)
