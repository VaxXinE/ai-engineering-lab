# Knowledge Check & Umpan Balik — UX AI: mengurangi kesalahan keputusan manusia, bukan sekadar membuat dashboard rapi

Jawab tanpa melihat teori. Setelah itu bandingkan dengan pembahasan; jawab *mengapa*, bukan hanya mengingat terminologi.

## Pertanyaan

1. Mengapa harus membedakan prediction dan review?
2. Apa default terbaik saat model abstain?
3. Apa risiko hanya memakai warna sebagai status?
4. Apa yang harus terjadi jika save gagal?
5. Mengapa override perlu audit?
6. Bagaimana menguji UX secara terukur?

## Jawaban dan alasan

**1.** Agar agent mengetahui asal keputusan dan evaluasi model punya ground truth review.

**2.** Tampilkan perlu review dan jalur manual, bukan memilih label secara diam-diam.

**3.** Pengguna dengan keterbatasan penglihatan warna atau screen reader bisa kehilangan makna.

**4.** Draft dipertahankan, penyebab ditampilkan aman, retry tersedia tanpa duplikasi.

**5.** Mendukung transparansi, troubleshooting, dan evaluasi kualitas model.

**6.** Berikan task, ukur keberhasilan dan jenis kesalahan, dokumentasikan keterbatasan sampel.

## Refleksi

- Mana kesalahan yang berpotensi menyebabkan **data loss** atau **access bypass**?
- Mana kesalahan yang hanya membuat metrik/kinerja tidak optimal?
- Bukti apa yang akan membedakan keduanya pada aplikasi yang nyata?

## Spaced review

- Hari 0: jawab semua soal dan catat alasan yang masih ragu.
- Hari +1: ulangi pertanyaan yang salah tanpa membaca catatan.
- Hari +7: jelaskan konsep ke contoh lain, bukan mengulang kalimat.
- Hari +21: campurkan dengan soal sistem data + AI dari modul lain.

Jadwal di atas adalah *learning plan*, bukan klaim interval optimal untuk semua orang.

[Deep dive](deep-dive.md) · [Mock assessment](assessment.md)
