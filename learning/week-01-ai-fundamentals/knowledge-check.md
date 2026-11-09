# Knowledge Check & Feedback — Memahami AI sebagai komponen sistem, bukan kotak ajaib

**Petunjuk:** Jawab pertanyaan tanpa melihat `deep-dive.md` atau kode. Setelah itu baru baca kunci dan **alasan jawaban**. Ini latihan belajar mandiri, bukan soal resmi BNSP.

## Retrieval questions

1. Apakah sistem if/else termasuk supervised ML?
2. Jika support TP=6 FP=2 FN=4, bagaimana precision dan recall?
3. Mengapa 18 contoh test tidak cukup untuk SLA?
4. Apa fungsi abstain?
5. Bolehkah score Naive Bayes ditampilkan sebagai probabilitas kepastian?
6. Apa bedanya evaluation dan monitoring?

## Pembahasan / kunci untuk self-correction

**1. Apakah sistem if/else termasuk supervised ML?**

Tidak. Aturan ditulis developer, bukan parameter dipelajari dari pasangan data-label.

**2. Jika support TP=6 FP=2 FN=4, bagaimana precision dan recall?**

Precision=0.75 dan recall=0.60; jelaskan dampak empat komplain yang terlewat.

**3. Mengapa 18 contoh test tidak cukup untuk SLA?**

Sampelnya kecil, sintetis dan tidak mewakili variasi distribusi, bahasa, serta failure rate produksi.

**4. Apa fungsi abstain?**

Menahan prediksi saat evidence tidak cukup dan menyerahkan ke review; tidak otomatis menambah akurasi untuk semua request.

**5. Bolehkah score Naive Bayes ditampilkan sebagai probabilitas kepastian?**

Tidak tanpa calibration validation yang memadai.

**6. Apa bedanya evaluation dan monitoring?**

Evaluation mengukur model terhadap dataset acuan; monitoring mengamati kinerja dan perubahan setelah layanan digunakan.

## Diagnose misconceptions

- LLM selalu lebih pintar untuk semua tugas → salah; kualitas, biaya, kontrol, privasi dan ukuran masalah menentukan pilihan.
- Training accuracy bukan production accuracy → data bisa berbeda dan test leakage membuat angka terlalu optimistis.
- Confidence tinggi bukan kepastian → relatif score atau softmax bisa miscalibrated.
- Tidak ada error HTTP berarti model benar → valid JSON bisa memuat prediksi salah.
- Data sintetis tidak perlu diuji privasinya → tetap jangan mencampur potongan chat nyata.

## Spaced review (jadwal usulan)

| Waktu | Latihan |
| --- | --- |
| Hari 0 | Jawab 6 soal, analisis kesalahan, perbaiki catatan |
| Hari +1 | Ulangi 3 soal tersulit tanpa melihat jawaban |
| Hari +7 | Campurkan 3 soal modul ini dengan modul berikutnya |
| Hari +21 | Jelaskan konsep pada skenario baru di proyek capstone |

**Rubrik:** mampu menjawab benar saja belum cukup; peserta harus bisa menjelaskan alasan dan menunjukkan bukti praktik. Tandai materi **belum dikuasai** bila tidak mampu menalar kasus baru.

[Deep dive](deep-dive.md) · [Simulasi asesmen](assessment.md)
