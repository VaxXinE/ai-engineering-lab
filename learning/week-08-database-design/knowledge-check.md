# Knowledge Check & Umpan Balik — Model data yang mencegah kehilangan historis prediksi dan celah akses

Jawab tanpa melihat teori. Setelah itu bandingkan dengan pembahasan; jawab *mengapa*, bukan hanya mengingat terminologi.

## Pertanyaan

1. Mengapa prediction perlu model_version?
2. Apa fungsi UNIQUE(site_id,meter_id,source_event_id)?
3. Apa yang terjadi jika optimistic lock UPDATE affected 0?
4. Mengapa FK tidak bisa diganti sekadar validasi frontend?
5. Bagaimana mencegah IDOR?
6. Kenapa audit event tidak sebaiknya ditimpa?

## Jawaban dan alasan

**1.** Agar hasil dapat dijelaskan dan direproduksi menurut model yang dipakai saat itu.

**2.** Mencegah duplikat event per site dan meter; ID meter boleh berulang antar-site, sedangkan payload konflik pada identity sama perlu ditolak.

**3.** Konflik atau row tidak ada; backend harus membedakan authorization/not found/conflict secara aman.

**4.** Frontend bisa dilewati dan concurrent writer dapat melanggar integritas.

**5.** Server memeriksa izin object dan site pada query serta menguji cross-tenant access.

**6.** Untuk menjaga historical traceability, review quality dan investigasi incident.

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
