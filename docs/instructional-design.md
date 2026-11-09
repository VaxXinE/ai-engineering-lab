# Instructional Design System v2 — AI Engineering Lab

**Status:** editorial design standard for self-study; not an approved BNSP teaching package.  
**Audience:** developer full-stack 2–3 tahun; dapat coding, baru mempelajari engineering of AI.  
**Goal:** belajar bukan sekadar 'mengenal istilah', melainkan mampu menjelaskan, mempraktikkan, menguji, dan mentransfer keterampilan ke kasus baru.

## Mengapa v1 belum memadai?

Audit editorial 2026-11-09:
- Konten utama rata-rata berupa paragraf singkat, bukan pembahasan bertahap/teks ajar.
- Langkah lab sering berbentuk instruksi tinggi tanpa contoh solusi dan reasoning lengkap.
- Pertanyaan asesmen belum memberi model jawaban/rubrik; sulit digunakan untuk self-assessment.
- Tidak ada retrieval schedule/spacing, diagnosis miskonsepsi, atau scaffolding yang berkurang.
- Bukti unit sertifikasi belum dipetakan sampai elemen/KUK yang diverifikasi dengan dokumen skema LSP aktual.

**Jangan meratakan semua masalah menjadi jumlah kata**: detail harus menambah pemahaman dan kemampuan demonstrasi, bukan mengulang daftar istilah.

## Kerangka riset pembelajaran

### 1. Backward Design — outcome → evidence → instruction

Mulai dari pertanyaan: "Di akhir modul, tugas profesional apa yang dapat dikerjakan?" Lalu tentukan bukti yang bisa dinilai (kode, diagram, test, ADR, data-quality report) sebelum menentukan urutan bacaan. Setiap modul menyatakan:
- **Outcome observable**: kata kerja seperti analisis, implementasi, evaluasi, merancang, atau mempertahankan keputusan.
- **Evidence**: output pekerjaan sendiri dan test method.
- **Learning activities**: teori → worked example → guided practice → independent application.

Sumber: [Vanderbilt Center for Teaching](https://www.vanderbilt.edu/cdr/module-3/principles-and-frameworks/), [Vermont State — Backward Design](https://ctli.vermontstate.edu/teaching-effectiveness-framework/curricular-alignment/backward-design/).

### 2. Bloom — tujuan dapat diukur

Tujuan buruk: "Memahami REST API dan AI." Tujuan lebih baik: "Mengidentifikasi minimal empat failure mode inference API, membuat error contract dan menguji setidaknya satu unauthorized request."

Gunakan progression: remember/understand → apply → analyze → evaluate → create; tidak semua topik harus pada tingkatan tertinggi. Pilih verb yang sesuai artefak dan durasi. Sumber: [Cornell — Defining Learning Outcomes](https://teaching.cornell.edu/teaching-resources/preparing-teach/designing-your-course/defining-learning-outcomes).

### 3. Merrill — authentic problem first

Setiap modul memakai **satu proyek konsisten** (AI Smart Energy Monitoring), lalu lima tahap:
- **Problem:** tunjukkan problem profesional dan batasannya.
- **Activation:** kaitkan pengetahuan full-stack yang sudah dimiliki.
- **Demonstration:** guru menunjukkan solusi yang sudah dikerjakan, termasuk reasoning dan failure cases.
- **Application:** pelajar mengulang dengan bimbingan lalu mengubah constraint.
- **Integration:** pelajar menjelaskan dan menggunakan kembali pada proyek/kompetensi berikutnya.

Sumber: [MIT Open Learning — First Principles](https://openlearning.mit.edu/mit-faculty/research-based-learning-findings/first-principles-instruction), [Merrill 2002](https://doi.org/10.1007/BF02505024).

### 4. Worked → faded → independent

Untuk topik baru, berikan **worked example lengkap**: problem, input, solusi, alasan tiap langkah, output/expected result (ditandai ilustrasi apabila belum diuji), pitfall, dan counterexample. Latihan pertama mengisi bagian solusi; latihan kedua mengubah kasus; tugas ketiga merancang solusi sendiri. Ini membantu menekan cognitive load tanpa menghilangkan kompleksitas nyata. Sumber: [MIT Worked and Faded Examples](https://openlearning.mit.edu/mit-faculty/research-based-learning-findings/worked-and-faded-examples).

### 5. Retrieval + spaced practice + feedback

Jangan menjadikan rereading satu-satunya strategi belajar. Tutup dokumen, jawab 4–8 soal tanpa melihat teori, lalu cek pembahasan dan tuliskan kesalahan. Review setelah **1 hari, 7 hari, dan 21 hari** sebagai jadwal usulan, bukan kewajiban pedagogis universal. Campurkan soal lama dengan topik modul baru (interleaving) dan lakukan koreksi aktif. Sumber: [IES What Works Clearinghouse](https://ies.ed.gov/ncee/wwc/practiceguide/1), [Weinstein et al. 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5780548/).

## Paket materi v2 per modul

| File | Tujuan |
| --- | --- |
| README.md | Orientasi, outcome dan status |
| theory.md | Ringkasan awal yang tetap mudah dipindai |
| **deep-dive.md** | Buku ajar mendalam: conceptual model, trade-offs, troubleshooting, risk |
| **worked-examples.md** | Contoh diselesaikan: hitungan, kode/pseudocode, reasoning, failure path |
| lab-guide.md | Tugas praktik saat pembelajaran dimulai |
| exercises.md | Guided → faded → independent practice |
| **knowledge-check.md** | Diagnostic/retrieval quiz, pembahasan, miskonsepsi |
| assessment.md | Mock interview/demonstration, bukan soal resmi |
| **study-contract.md** | Learning outcomes observable, evidence, review 1/7/21 hari |

Konten tambahan adalah materi ajar, bukan bukti bahwa capstone Week 02–16 telah dikodekan atau diuji.

## Ritme belajar 8–10 jam per modul (usulan)

- **Pra-belajar 15 menit:** diagnostic questions tanpa melihat solusi.
- **Teori 2 jam:** deep dive dalam dua sesi, catat "apa, kapan, mengapa, gagal karena apa".
- **Worked examples 1.5 jam:** jalankan/cek solusi dan jelaskan alasan langkah.
- **Guided lab 2.5 jam:** tiru dengan dataset sintetis dan catat error.
- **Transfer practice 1 jam:** ubah constraint (tenant, latency, auth, invalid data).
- **Testing & evidence 1 jam:** catat command, test, output aktual, bukan angka dugaan.
- **Recall 30 menit:** retrieval quiz, koreksi, jadwalkan review ulang.

## Content QA checklist

- [ ] Tujuan terukur cocok dengan evidence dan praktik.
- [ ] Ada dua contoh spesifik, salah satunya menangani kegagalan.
- [ ] Minimal satu counterexample atau miskonsepsi dijelaskan.
- [ ] Ada alasan trade-off, security dan privacy sesuai topik.
- [ ] Jawaban quiz bisa dievaluasi dan memberi penjelasan *why*.
- [ ] Label **illustration/expected** bukan **verified run** jika belum dieksekusi.
- [ ] Referensi primer dapat ditelusuri (dokumen resmi untuk SDK, DB, OWASP, pendidikan).
- [ ] Tidak ada API key, PII nyata atau asumsi kelulusan BNSP.
- [ ] Link internal dan struktur dokumen diperiksa dengan checker.
- [ ] Alur belajar cocok dengan pengalaman 2–3 tahun full-stack.

## Batasan asesmen resmi

Tujuan pembelajaran v2 diselaraskan dengan **nama unit yang terpublikasi**, belum dapat diakui sebagai ketercapaian semua Elemen/KUK karena dokumen skema final belum diberikan LSP. Kepmenaker 103/2026 berlaku dan mencabut 123/2021; kode AI yang terpublikasi LSP mungkin masih mengacu standar terdahulu. Simpan mismatch dalam [standards watch](standards-watch.md).

## Maintainer review workflow

Review 16 modul berdasarkan [content quality rubric](content-quality-rubric.md). Koreksi kesalahan teknis atau evidensial lewat PR dengan tests. Quality of content harus diperiksa manusia, tidak hanya dengan checker menghitung file.
