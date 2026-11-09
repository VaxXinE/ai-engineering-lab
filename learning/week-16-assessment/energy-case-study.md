# Applied Energy Case — Portofolio yang bisa ditelusuri per unit

**Status:** materi ilustratif, belum dijalankan sebagai praktik mandiri atau asesmen BNSP.

## Masalah

Repository memiliki 16 modul materi, tetapi baru Week 01 mempunyai runnable code dan hasil tests; capstone numerik belum berjalan.

## Worked reasoning

Petakan unit berdasarkan skema LSP terbaru ke bukti aktual. Status 'planned' tidak boleh menjadi 'verified' karena README tersedia. Empat unit AI yang overlap dapat memakai artefak belajar sama, bukan pengakuan asesmen otomatis.

## Latihan dengan bantuan bertahap

**Guided:** jelaskan langkah-langkah reasoning dan constraint tiap keputusan.  
**Faded:** ganti satu input/constraint dan isi satu langkah perhitungan/desain yang hilang.  
**Independent:** Latih demo skenario import → data quality → anomaly scoring → human review → timeout → restore hanya setelah fitur benar-benar diimplementasi dan diverifikasi.

## Negative case dan keamanan

Jangan upload KTP/berkas privat ke repo publik atau memalsukan hasil uji; cek perbedaan unit LSP/BNSP sebelum mendaftar.

Saat implementasi, pisahkan **expected behavior** dari **actual test output** serta lampirkan environment, commit, log yang disanitasi, dan keterbatasan. Jangan mengklaim hasil yang belum dijalankan.

## Target bukti kompetensi

Evidence matrix, assessment gap register, mock interview record, update dokumen skema.

**Sumber kontrak:** [Canonical Energy Schema](../../docs/architecture/energy-data-contract.md) · [Threat Model](../../docs/architecture/threat-model.md) · [Gates](../../docs/architecture/energy-learning-gates.md).
