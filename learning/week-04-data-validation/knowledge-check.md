# Knowledge Check & Feedback — Data quality sebagai penghalang sebelum AI, bukan cleanup kosmetik

**Petunjuk:** Jawab pertanyaan tanpa melihat `deep-dive.md` atau kode. Setelah itu baru baca kunci dan **alasan jawaban**. Ini latihan belajar mandiri, bukan soal resmi BNSP.

## Retrieval questions

1. Apa beda validity dan accuracy?
2. Mengapa interval coverage 75% tidak berarti data konsumsi 100% lengkap?
3. Kapan pipeline harus quarantine record?
4. Mengapa fit scaler sebelum split salah?
5. Apakah identitas site yang sudah diganti otomatis aman dipublikasikan?
6. Apa bukti quality gate efektif?

## Pembahasan / kunci untuk self-correction

**1. Apa beda validity dan accuracy?**

Validity adalah kesesuaian aturan; accuracy kesesuaian dengan keadaan benar yang perlu diverifikasi.

**2. Mengapa interval coverage 75% tidak berarti data konsumsi 100% lengkap?**

Coverage 75% berarti 3 dari 4 interval diharapkan memiliki reading valid. Baris yang ada bisa 100% valid namun satu interval tetap hilang; missing bukan 0 kWh.

**3. Kapan pipeline harus quarantine record?**

Ketika record tidak memenuhi kualitas tetapi dibutuhkan untuk audit/perbaikan dan ada storage serta akses yang tepat.

**4. Mengapa fit scaler sebelum split salah?**

Statistik data test memengaruhi pelatihan sehingga evaluasi bias.

**5. Apakah pesan PII-redacted otomatis aman dipublikasikan?**

Tidak. Residual identifiers dan konteks tetap perlu diperiksa; gunakan sintetis untuk lab.

**6. Apa bukti quality gate efektif?**

Test negative/positive yang dijalankan, pengukuran reject yang dapat diulang, dan proses owner meninjau kegagalan.

## Diagnose misconceptions

- Valid format berarti benar secara faktual → salah.
- Menghapus outlier selalu memperbaiki AI → bisa menghapus kasus penting.
- Data test boleh dipakai untuk fit scaler/vectorizer karena bukan label → tetap leakage.
- Semua missing values bisa diisi default → silent coercion bisa merusak audit.
- Anonimisasi dengan mengganti nama cukup untuk publik → konteks lain bisa mengidentifikasi individu.

## Spaced review (jadwal usulan)

| Waktu | Latihan |
| --- | --- |
| Hari 0 | Jawab 6 soal, analisis kesalahan, perbaiki catatan |
| Hari +1 | Ulangi 3 soal tersulit tanpa melihat jawaban |
| Hari +7 | Campurkan 3 soal modul ini dengan modul berikutnya |
| Hari +21 | Jelaskan konsep pada skenario baru di proyek capstone |

**Rubrik:** mampu menjawab benar saja belum cukup; peserta harus bisa menjelaskan alasan dan menunjukkan bukti praktik. Tandai materi **belum dikuasai** bila tidak mampu menalar kasus baru.

[Deep dive](deep-dive.md) · [Simulasi asesmen](assessment.md)
