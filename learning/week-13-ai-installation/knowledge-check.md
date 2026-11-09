# Retrieval dan Feedback — Instalasi AI yang reproducible dan tidak menyebarkan secret

Tutup teori. Jawab soal berikut tanpa bantuan, lalu evaluasi dengan alasan di bawahnya.

## Pertanyaan

1. Apa bedanya image dan container?
2. Kenapa `latest` kurang cocok untuk reproducibility?
3. Apa beda liveness dan readiness?
4. Mengapa DB internal tidak perlu dipublish?
5. Apakah Compose fragment berarti sistem sudah deploy?
6. Mengapa rollback image saja bisa gagal?

## Pembahasan

**1.** Image adalah blueprint immutable/read-only layers; container adalah instance runtime.

**2.** Tag mengarah ke content yang bisa berubah sehingga build/deploy tidak deterministik.

**3.** Liveness hidup; readiness siap melayani request dengan dependensi yang diperlukan.

**4.** Aplikasi berbicara melalui network internal; port publish memperluas attack surface.

**5.** Tidak; perlu file lengkap, konfigurasi, jalankan dan verifikasi pada environment nyata.

**6.** Database schema/model artifact berubah tidak kompatibel dengan aplikasi sebelumnya.

## Latihan transfer

Ambil satu masalah dari [capstone](../../projects/ai-energy-intelligence/README.md), ubah satu constraint utama, dan jelaskan akibatnya pada solution design. Catat miskonsepsi yang sudah diperbaiki.

## Jadwal recall

Hari 0 → Hari +1 → Hari +7 → Hari +21. Review aktif dapat berupa menuliskan ulang kontrak, menggambar diagram dari ingatan, atau menjelaskan failure mode tanpa melihat jawaban.

[Deep dive](deep-dive.md)
