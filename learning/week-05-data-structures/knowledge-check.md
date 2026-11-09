# Knowledge Check & Umpan Balik — Struktur Data: memilih berdasarkan operasi dan beban

Jawab tanpa melihat teori. Setelah itu bandingkan dengan pembahasan; jawab *mengapa*, bukan hanya mengingat terminologi.

## Pertanyaan

1. Apa invariant utama dedup?
2. Mengapa nested list search bisa O(n²)?
3. Apa yang paling cocok untuk queue FIFO?
4. Bolehkah dua pesan teks sama dianggap event sama?
5. Kenapa set bukan solusi dedup global lintas worker?
6. Apa trade-off set dibanding list?

## Jawaban dan alasan

**1.** Setiap ID unik hanya muncul sekali; urutan disesuaikan kebijakan first/last wins.

**2.** Untuk setiap dari n item, pencarian dapat memeriksa hingga n item lainnya.

**3.** deque (atau queue service untuk multi-worker), karena popleft efisien.

**4.** Tidak otomatis; event identity bergantung stable event ID dan tenant.

**5.** State in-memory tidak konsisten antarprocess; DB constraint lebih andal.

**6.** Lookup average cepat tetapi perlu memory tambahan dan tidak menyimpan seluruh urutan/double entries.

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
