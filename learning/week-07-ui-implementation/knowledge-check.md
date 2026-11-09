# Knowledge Check & Umpan Balik — Mengubah UX menjadi frontend state machine yang tepercaya

Jawab tanpa melihat teori. Setelah itu bandingkan dengan pembahasan; jawab *mengapa*, bukan hanya mengingat terminologi.

## Pertanyaan

1. Apa keunggulan discriminated union?
2. Mengapa disabled button tidak cukup?
3. Apa itu stale response?
4. Bolehkah menyimpan API secret di public env Next.js?
5. Mengapa output AI harus terlihat sebagai saran?
6. Mengapa authorization tetap dibutuhkan di backend?

## Jawaban dan alasan

**1.** State mutually exclusive dan type narrowing mengurangi kombinasi error.

**2.** Retry, concurrency multi-tab dan permintaan langsung tetap bisa menduplikasi operasi; server perlu idempotency.

**3.** Response permintaan lama yang datang belakangan dan menimpa state untuk query terbaru.

**4.** Tidak; public env masuk client bundle dan dapat dibaca user.

**5.** Model bisa salah; human review menjadi keputusan yang tercatat.

**6.** Browser sepenuhnya dikendalikan user; UI hiding/route guard bukan enforcement.

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
