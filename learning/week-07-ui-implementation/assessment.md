# Simulasi Asesmen — Implementasi UI Dashboard AI

Ini pertanyaan latihan nonresmi, **bukan bank soal BNSP**.

1. Mengapa state asynchronous harus eksplisit?

2. Apa beda UI validation dan server-side validation?

3. Bagaimana menangani race condition dua request?

4. Mengapa confidence tidak boleh ditampilkan tanpa kalibrasi?

5. Apa itu accessible form error?

6. Apa risiko dangerouslySetInnerHTML?

7. Mengapa disabled button saja tidak mencegah double submission?

8. Bagaimana menjaga pemisahan tenant pada UI data cache?

## Demonstrasi yang harus mampu dilakukan

- [ ] Semua state idle/loading/empty/success/error dapat direproduksi.
- [ ] Label AI dan keputusan manusia ditampilkan berbeda.
- [ ] Aksi double-submit tertahan di UI dan direncanakan juga dicegah di server.
- [ ] Komponen kritis dapat digunakan dengan keyboard.

## Pengukuran kesiapan

1. **Konsep:** jelaskan tiap keputusan teknis dan trade-off.
2. **Praktik:** tunjukkan artefak yang dibuat sendiri beserta cara menjalankannya.
3. **Validasi:** tunjukkan hasil test aktual dan penanganan edge case.
4. **Risk:** jelaskan security, privacy, failure dan batasan pendekatan.
5. **Evidence:** dokumentasikan referensi commit/PR, diagram, logs, dan test.

Status 'kompeten' tetap ditetapkan melalui asesmen resmi LSP berlisensi, bukan penilaian diri.

[Portfolio](../../certification/evidence-matrix.md)