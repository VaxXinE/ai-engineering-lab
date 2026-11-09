# Retrieval dan Feedback — Mengukur kesehatan layanan dan AI secara terpisah

Tutup teori. Jawab soal berikut tanpa bantuan, lalu evaluasi dengan alasan di bawahnya.

## Pertanyaan

1. Apa bedanya SLI dan SLO?
2. Berapa error budget dari 100000 request dengan SLO 99.5%?
3. Apakah override rate = error rate model?
4. Apa yang membedakan data drift dan concept drift?
5. Kenapa backup success tidak cukup?
6. Apa yang harus ada dalam alert?

## Pembahasan

**1.** SLI ukuran yang diobservasi; SLO target terhadap ukuran tersebut.

**2.** 500 request failed (dengan definisi denominator jelas).

**3.** Tidak selalu; review bisa bias atau alasan koreksi tidak terkait kebenaran label.

**4.** Perubahan input distribution vs hubungan input dengan label.

**5.** Restore harus terbukti mampu menghasilkan data/konsistensi yang diperlukan.

**6.** Metric, threshold/window, severity, owner, actionable runbook, dan eskalasi.

## Latihan transfer

Ambil satu masalah dari [capstone](../../projects/ai-customer-intelligence/README.md), ubah satu constraint utama, dan jelaskan akibatnya pada solution design. Catat miskonsepsi yang sudah diperbaiki.

## Jadwal recall

Hari 0 → Hari +1 → Hari +7 → Hari +21. Review aktif dapat berupa menuliskan ulang kontrak, menggambar diagram dari ingatan, atau menjelaskan failure mode tanpa melihat jawaban.

[Deep dive](deep-dive.md)
