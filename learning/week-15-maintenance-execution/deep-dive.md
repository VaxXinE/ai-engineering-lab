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

Gunakan request_id yang aman untuk menelusuri browser→API→inference→DB. Logs harus menyamarkan PII, prompt, tokens dan secrets. Catat error class dan retry count, bukan full telemetri. Root cause belum terbukti jika hanya ada correlation; bandingkan healthy versus failing requests, deploy diff dan resource trends.

### 3. Human fallback and containment

Ketika anomaly scorer tidak tersedia atau tidak tepercaya, hentikan penandaan otomatis dan gunakan `scoring_unavailable` dengan manual review. **Reading valid tetap tersimpan.** Jika model memberi skor tinggi, itu bukan alasan menjalankan perintah kelistrikan. Saat credential bocor, lakukan containment/revocation melalui prosedur yang tepat dan jangan membagikan token pada issue publik.

### 4. Restore di environment berbeda

Jalankan restore snapshot ke isolated DB, verifikasi schema, row count, sample records sintetis, referential integrity, permissions dan fungsi aplikasi. Ukur durasi aktual, bukan waktu yang diperkirakan. Jangan menimpa production DB saat latihan. Jika restore gagal, dokumentasikan penyebab dan perbaiki runbook.

### 5. Model rollback dan regression

Rollback memilih model artifact versi sebelumnya dengan schema/feature mapping yang kompatibel. Jalankan held-out numeric anomaly evaluation, smoke tests, dan cross-site access checks. Review history dan `energy_kwh` asli tidak dihapus. Kenaikan alert bukan otomatis bukti drift; diagnosis diperlukan.

### 6. Postmortem dan technical debt

Dokumentasikan timeline UTC/offset, impact, root cause yang terkonfirmasi, contributing factors, what went well, missed signals, corrective actions dan owners. Hindari menyalahkan engineer tertentu. Tambah automated test yang mereproduksi bug untuk mengurangi peluang terulang, lalu review efektivitas perubahan.

## Transfer lesson ke dunia kerja

Buat daftar tindakan yang aman dilakukan di environment test dan yang memerlukan izin perubahan produksi. Jelaskan risiko dan keterbatasan serta apa yang harus diverifikasi dengan data nyata. Jangan gunakan materi demo sebagai bukti hasil production.

## Bacaan primer

- https://sre.google/workbook/incident-response/
- https://www.postgresql.org/docs/current/backup.html
- https://www.nist.gov/itl/ai-risk-management-framework

[Contoh lengkap](worked-examples.md) · [Tes pemahaman](knowledge-check.md)
