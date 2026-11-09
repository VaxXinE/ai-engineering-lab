# Pedoman Belajar Mandiri & Pendampingan

## Tujuan

Menjaga proses pembelajaran terukur, bertahap, dan benar-benar menghasilkan keterampilan. Materi dituntaskan terlebih dahulu untuk 16 modul, tetapi progress praktik ditentukan dari pekerjaan yang dilakukan sendiri.

## Penerapan v2

Gunakan metode **outcome → bukti → materi**, lalu kerja nyata dengan contoh yang sudah diselesaikan (*worked example*) dan bimbingan berkurang (*faded example*). Lakukan retrieval quiz tanpa melihat jawaban, beri feedback alasan, dan ulangi topik pada hari +1/+7/+21 sebagai usulan interval belajar.

[Instructional design & sumber riset](instructional-design.md).

## Alur sesi per modul

1. **Pre-check:** jelaskan konsep prasyarat tanpa membaca catatan, tentukan target pribadi.
2. **Theory walkthrough:** baca theory.md; terjemahkan istilah ke contoh full-stack dan arsitektur nyata.
3. **Mini demo:** lihat data/API/diagram kecil, jelaskan input dan output sebelum running.
4. **Hands-on:** ikuti lab-guide, ubah kode sendiri dan catat apa yang terjadi.
5. **Tests:** jalankan happy + failure cases; simpan command, output, runtime, environment.
6. **Engineering review:** audit kualitas, akses, privacy, failure handling, maintainability, complexity.
7. **Self assessment:** jawab pertanyaan di assessment.md tanpa melihat teori dan sebutkan trade-off.
8. **Evidence:** tautkan file, PR, log teredaksi dan dokumentasi ke matrix; baru kemudian tandai progress.

## Kriteria peserta boleh lanjut

- **Pengetahuan:** setidaknya dapat menjelaskan tujuan, konsep, alasan teknik, dan batasan.
- **Keterampilan:** artefak dapat dijalankan ulang dari README pada lingkungan bersih.
- **Testing:** minimal 1 happy path, 1 invalid input dan 1 failure path relevan terdokumentasi, dengan hasil aktual.
- **Security:** tidak mengandung secrets/PII asli dan akses/data validation dipertimbangkan proporsional.
- **Portfolio:** bukti pekerjaan sendiri dapat dirujuk ke commit atau dokumen.

Jika sebuah modul hanya murni desain (contoh Week 06), pengganti executable test adalah task-based usability review dan artefak desain yang bisa dievaluasi, bukan sekadar klaim 'sudah bagus'.

## Review praktik bersama AI pendamping

AI pendamping boleh menjelaskan dan mengulas, tetapi **jangan** menganggap jawaban yang diberikan sebagai bukti pemahaman peserta. Tanyakan alasan teknis, minta peserta memodifikasi/menjelaskan baris kode, lalu evaluasi hasil dari tests yang dijalankan.

## Kebijakan kelulusan

- Materi repo ini **tidak resmi** dan tidak menjamin hasil BNSP.
- Status "kompeten" hanya dihasilkan dari asesmen LSP yang berwenang.
- Wajib meminta skema/KUK/aturan bukti terkini pada LSP sebelum asesmen final.
