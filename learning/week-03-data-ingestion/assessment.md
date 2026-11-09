# Simulasi Asesmen — Week 03

**Ini latihan pribadi, bukan soal, asesmen, atau panduan resmi BNSP.**

## Tanya jawab teknis

1. Apa beda ETL dan ELT?

2. Kenapa uniqueness constraint tetap diperlukan walau kode mengecek duplikat?

3. Apa arti idempotent?

4. Bagaimana menangani file malformed tanpa kehilangan semua data?

5. Kenapa prepared statements penting?

6. Apa itu source lineage?

7. Apa konsekuensi impor multi-batch dan transaksi?

8. Bagaimana mengaudit hasil import tanpa mencatat isi data sensitif?

## Demo praktis yang perlu disiapkan

- [ ] Tunjukkan bukti: CSV valid dapat diproses dengan hasil terhitung.
- [ ] Tunjukkan bukti: Input invalid ditolak dan dilaporkan tanpa menyimpan record corrupt.
- [ ] Tunjukkan bukti: Menjalankan batch yang sama dua kali tidak menghasilkan duplikasi.
- [ ] Tunjukkan bukti: Query parameterized dan transaction behavior teruji.

## Penilaian diri

- **Belum bisa:** belum dapat menjelaskan atau mendemonstrasikan.
- **Perlu latihan:** bisa dengan bantuan tetapi belum konsisten.
- **Mandiri:** bisa menjelaskan dan mendemonstrasikan sendiri, beserta error path.
- **Siap dievaluasi:** bukti direproduksi dan risiko tersisa dijelaskan.

Jangan menganggap skor ini menentukan status **Kompeten** BNSP. Keputusan resmi memerlukan prosedur dan asesor LSP.

## Bukti untuk portfolio

Gunakan [template evidence](../../docs/templates/evidence-template.md) dan tautkan bukti ke [matriks sertifikasi](../../certification/evidence-matrix.md).
