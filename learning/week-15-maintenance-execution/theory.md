# Teori — Eksekusi Maintenance, Troubleshooting dan Recovery

**Tujuan:** Membuktikan proses diagnosis gangguan, perbaikan terkontrol, validasi regresi, dan restore di lingkungan uji.

## 1. Incident lifecycle

Detect → triage → mitigate → recover → verify → postmortem. Mitigasi sementara (menonaktifkan inference dan mengarahkan ke human review) bisa tepat walau root cause belum selesai. Jangan membuat perubahan acak saat incident; simpan timestamp, aksi, dan result.

## 2. Root cause versus symptom

HTTP 500 hanya gejala. Bedakan timeout network, missing model artifact, invalid schema, expired credential, DB saturation, dan release incompatibility. Gunakan correlation ID dan bounded logs untuk menemukan komponen gagal. Redact customer content dan tidak menyalin token ke issue.

## 3. Change management and regression

Update dependency/model perlu compatibility assessment, unit/integration/regression tests, smoke test dan rollback. Model yang lebih akurat di satu test belum otomatis aman; evaluasi distribusi kelas dan kualitas error. Catat change ticket, versi sebelum/sesudah, dan approval owner.

## 4. Backup and restore drills

Restore harus diuji ke environment isolated agar tidak menimpa data aktif. Periksa schema, record count, checksums/consistency, permissions, dan business invariants. Ukur restore duration dan bandingkan dengan target RTO; jangan menyatakan RPO tercapai tanpa fakta backup interval serta replay.

## 5. Learning from incidents

Postmortem fokus pada kronologi, dampak, penyebab teknis, contributing factors, detection gaps, tindakan koreksi dan tindakan pencegahan yang terukur. Hindari menyalahkan individu. Regression tests terhadap root cause harus ditambahkan agar insiden tidak berulang.

## Studi kasus

Simulasikan service inference offline sehingga klasifikasi gagal. Data inquiry tetap disimpan. Operator memverifikasi degraded mode, memulihkan service, menjalankan regression test, dan mendokumentasikan insiden.

## Pertimbangan verifikasi

- Simulasi outage tidak kehilangan inquiry yang sudah diterima.
- Restore dijalankan pada environment uji dan diperiksa integritasnya.
- Setiap langkah pemulihan beserta hasil uji dicatat.
- Regression test menguji akar masalah, bukan hanya happy path.
- Tidak ada data customer asli atau secret dalam incident report.

## Bacaan primer

- https://sre.google/sre-book/monitoring-distributed-systems/
- https://www.postgresql.org/docs/current/backup.html
- https://docs.docker.com/engine/

Pelajari teori ini sebagai landasan praktik, bukan sebagai KUK atau pedoman asesmen resmi. [Lab](lab-guide.md).