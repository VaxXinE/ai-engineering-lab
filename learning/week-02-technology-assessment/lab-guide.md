# Praktikum — Week 02: Technology Assessment & Dependency Selection

**Status:** rancangan latihan. Belum ada klaim bahwa langkah di bawah berhasil dijalankan.

## Konteks

Contoh keputusan: membandingkan classifier lokal Naive Bayes, hosted LLM, dan aturan keyword. Saat data sensitif, biaya rendah, dan bahasa domain sempit, baseline lokal bisa dipilih untuk MVP; dampak accuracy dan false routing tetap diuji.

**Prasyarat:** Modul 1, pemahaman aplikasi web/API, dan kemampuan membaca dokumentasi library.  
**Dataset:** data sintetis dari capstone; jangan memakai data perusahaan atau kredensial sungguhan.

## Langkah kerja

1. Salin persyaratan dari projects/ai-energy-intelligence/docs/requirements.md; identifikasi requirement must-have dan constraint.

2. Buat docs/decisions/0001-ai-strategy.md dengan tiga opsi: rule-based, model ML lokal, dan hosted LLM.

3. Buat decision-matrix.md (minimal 5 kriteria dengan bobot berjumlah 100%) dan beri bukti/link setiap skor.

4. Bandingkan dua opsi backend dan dua pilihan UI berdasarkan kemampuan implementasi dan operasional tim.

5. Catat threat model awal: data perangkat, kredensial provider, abuse rate, dependency berbahaya, vendor outage.

6. Pilih arsitektur baseline sementara, tulis rollback/exit strategy dan cara memverifikasinya pada Week 11.

## Test plan minimal

1. Jumlah bobot decision matrix tepat 100%.
2. Setiap alternatif dievaluasi dengan kriteria yang sama.
3. Keputusan mempertimbangkan minimal satu risiko privacy, satu risiko supply-chain, dan satu risiko operasional.

## Acceptance criteria

- [ ] Tiga strategi AI dibandingkan dengan bobot eksplisit dan rasional penilaian.
- [ ] ADR memuat alternatif yang ditolak beserta konsekuensinya.
- [ ] Dependency dan lisensi utama dicatat tanpa hardcoded API key.
- [ ] Ada rencana validasi berbasis pengukuran, bukan hanya opini.

## Bukti yang disimpan setelah praktik

1. Source code / artefak desain serta alasan keputusan yang dibuat sendiri.
2. Cara menjalankan atau mereproduksi hasil (versi environment dan perintah aktual).
3. Test report: perintah, hasil sesungguhnya, sampel negatif dan edge cases.
4. Analisis risiko keamanan, privasi, performa, serta keterbatasan yang belum ditangani.
5. Link PR/commit ke [matriks bukti](../../certification/evidence-matrix.md).

## Syarat selesai

**Belum selesai** hanya dengan membaca dokumen ini. Tandai selesai setelah implementasi diverifikasi dan evidence tersimpan; uji kompetensi BNSP tetap dilakukan oleh LSP yang berwenang.

[Latihan tambahan](exercises.md) · [Simulasi asesmen](assessment.md)
