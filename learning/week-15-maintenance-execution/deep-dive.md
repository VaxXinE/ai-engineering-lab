# Deep Dive — Melakukan incident response dan recovery berbasis bukti

## Outcome terukur

1. Memisahkan gejala, hipotesis, root cause dan mitigasi.
2. Menjalankan secara konseptual recovery drill terisolasi tanpa menyentuh production.
3. Mengukur hasil restore dan regression test dengan evidence.
4. Membuat postmortem yang berfokus pada sistem dan tindak lanjut.

## Pembahasan engineering

### 1. Incident bukan sekadar restart

Saat inference timeout meningkat, lihat sejak kapan, perubahan terakhir, p95, queue backlog, DB health, network dan model artifact. Restart mungkin memulihkan sementara tetapi menyembunyikan akar masalah. Urutan detect→triage→mitigate→recover→verify→learn membuat respons lebih akurat. Wajib batasi efek samping dan melibatkan owner sebelum perubahan production.

### 2. Fault isolation dengan correlation ID

Gunakan request_id yang aman untuk menelusuri browser→API→inference→DB. Logs harus menyamarkan PII, prompt, tokens dan secrets. Catat error class dan retry count, bukan full chat. Root cause belum terbukti jika hanya ada correlation; bandingkan healthy versus failing requests, deploy diff dan resource trends.

### 3. Human fallback and containment

Jika model hasilnya tidak tepercaya, hentikan auto-route dan tampilkan manual review untuk pesan baru. Jangan menghapus inquiries yang sedang menunggu. Untuk kemungkinan credential leak, containment mencakup revoke/rotate dengan prosedur yang benar, audit access dan komunikasi; jangan mem-push contoh token ke issue publik.

### 4. Restore di environment berbeda

Jalankan restore snapshot ke isolated DB, verifikasi schema, row count, sample records sintetis, referential integrity, permissions dan fungsi aplikasi. Ukur durasi aktual, bukan waktu yang diperkirakan. Jangan menimpa production DB saat latihan. Jika restore gagal, dokumentasikan penyebab dan perbaiki runbook.

### 5. Model rollback dan regression

Pilih model release sebelumnya dengan fingerprint dan feature schema kompatibel. Jalankan held-out test untuk correctness dan smoke test untuk connectivity. Perbedaan score/label bisa berasal data drift bukan binary deployment, sehingga catat semuanya. Pastikan rollback tidak menghapus audit history hasil model baru.

### 6. Postmortem dan technical debt

Dokumentasikan timeline UTC/offset, impact, root cause yang terkonfirmasi, contributing factors, what went well, missed signals, corrective actions dan owners. Hindari menyalahkan engineer tertentu. Tambah automated test yang mereproduksi bug untuk mengurangi peluang terulang, lalu review efektivitas perubahan.

## Transfer lesson ke dunia kerja

Buat daftar tindakan yang aman dilakukan di environment test dan yang memerlukan izin perubahan produksi. Jelaskan risiko dan keterbatasan serta apa yang harus diverifikasi dengan data nyata. Jangan gunakan materi demo sebagai bukti hasil production.

## Bacaan primer

- https://sre.google/workbook/incident-response/
- https://www.postgresql.org/docs/current/backup.html
- https://www.nist.gov/itl/ai-risk-management-framework

[Contoh lengkap](worked-examples.md) · [Tes pemahaman](knowledge-check.md)
