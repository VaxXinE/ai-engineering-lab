# Retrieval dan Feedback — Melakukan incident response dan recovery berbasis bukti

Tutup teori. Jawab soal berikut tanpa bantuan, lalu evaluasi dengan alasan di bawahnya.

## Pertanyaan

1. Apa beda mitigation dan root-cause fix?
2. Mengapa restart berulang tanpa diagnosis buruk?
3. Kenapa restore test harus isolated?
4. Apa yang perlu diverifikasi selain exit code restore?
5. Apa isi postmortem minimum?
6. Mengapa cross-tenant test penting setelah restore?

## Pembahasan

**1.** Mitigation mengurangi dampak segera, fix menyelesaikan penyebab yang terkonfirmasi.

**2.** Bisa menyembunyikan bukti, menambah downtime, atau mengulang kegagalan yang sama.

**3.** Menghindari menimpa data hidup dan memungkinkan pemeriksaan secara aman.

**4.** Schema, counts, integrity, permissions dan fungsi aplikasi.

**5.** Timeline, impact, root cause/status hipotesis, mitigasi, recovery, preventive actions dan owners.

**6.** Restore/config/migration bisa mengubah permission/filter; data antarorganisasi tetap harus terisolasi.

## Latihan transfer

Ambil satu masalah dari [capstone](../../projects/ai-energy-intelligence/README.md), ubah satu constraint utama, dan jelaskan akibatnya pada solution design. Catat miskonsepsi yang sudah diperbaiki.

## Jadwal recall

Hari 0 → Hari +1 → Hari +7 → Hari +21. Review aktif dapat berupa menuliskan ulang kontrak, menggambar diagram dari ingatan, atau menjelaskan failure mode tanpa melihat jawaban.

[Deep dive](deep-dive.md)
