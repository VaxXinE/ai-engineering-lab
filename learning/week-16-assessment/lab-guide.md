# Panduan Hands-on — Portofolio dan Simulasi Asesmen BNSP

**Praktik:** belum dieksekusi. Jangan menulis angka kinerja atau status passed tanpa pengujian.

## Masalah yang dikerjakan

Punya repo berisi kode tidak otomatis memenuhi unit kompetensi. Untuk setiap unit harus ada klaim kemampuan spesifik, tindakan yang dilakukan peserta, artefak, hasil verifikasi aktual, dan batas kontribusinya.

## Langkah terurut

1. Konfirmasi ke LSP dokumen skema terbaru, unit ke-13 yang tercatat di BNSP, KUK, persyaratan administrasi dan aturan bukti.

2. Salin evidence-matrix.md sebagai matriks kerja, lengkapi link commit/PR/test output untuk setiap unit yang benar-benar telah dilakukan.

3. Jalankan sistem pada clean environment dengan data sintetis dan dokumentasikan setup serta outcome sesungguhnya.

4. Susun demo 20 menit: problem, data validation, ML evaluation, UI/API, AI failure, recovery dan security controls.

5. Latihan sesi tanya jawab: teori, opsi keputusan, false positive/negative, scaling, auth, backup, dan perubahan model.

6. Isi gap analysis; jangan tandai lulus atau eligible tanpa verifikasi LSP. Persiapkan berkas administrasi sesuai prosedur.

## Acceptance criteria

- [ ] Matriks unit sesuai dokumen LSP final yang dikonfirmasi.
- [ ] Setiap klaim kompetensi mempunyai bukti kontribusi sendiri dan dapat direproduksi.
- [ ] Tes dan demo hasil nyata, tidak ada klaim palsu.
- [ ] Data/credential/proprietary work aman sebelum dibagikan.
- [ ] Kekurangan bukti dan rencana remediasi tercatat jelas.

## Test & evidence protocol

1. Catat environment serta versi runtime dan tools yang benar-benar digunakan.
2. Rekam command/aksi, input sintetis, output, error path dan test results aktual.
3. Jangan menggunakan production data, kredensial atau system perusahaan.
4. Tautkan diagram, source code, logs teredaksi, commits dan evaluasi ke [evidence matrix](../../certification/evidence-matrix.md).
5. Tulis residual risk dan pekerjaan yang belum teruji sebagai catatan eksplisit.

[Latihan tambahan](exercises.md) · [Asesmen simulasi](assessment.md).