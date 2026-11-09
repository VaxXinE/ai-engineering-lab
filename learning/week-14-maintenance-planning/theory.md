# Teori — Rencana Pemeliharaan Solusi AI

**Tujuan:** Menghasilkan maintenance plan yang memisahkan reliability aplikasi, kualitas prediksi, keamanan dependency dan pemulihan insiden.

## 1. Operational vs model quality

Service availability 99.9% bukan bukti prediksi baik. Pantau error rate, P95 inference latency, queue backlog, failed review operations serta kualitas label dari hasil human review. Jangan mengandalkan accuracy training yang statis sebagai metrik model berjalan.

## 2. Observability and signal quality

Log untuk incident diagnosis, metric untuk trend/alert, trace untuk request flow. Log harus memakai request ID dan menyamarkan PII; hindari menulis teks device, token dan headers sensitif. Alert harus actionable, bukan noisy; threshold dibuat berdasarkan baseline lalu dievaluasi.

## 3. Data/model drift

Data drift adalah perubahan input, concept drift perubahan hubungan input-target. Keduanya tidak otomatis membutuhkan retraining. Lakukan investigasi kualitas label, perubahan channel/bahasa, dan latency; retrain hanya setelah dataset dan evaluasi memadai serta proses approval.

## 4. Maintenance calendar

Susun schedule harian untuk health/error, mingguan untuk failed predictions dan quality review, bulanan untuk patch dependency dan restore drill. Ini contoh cadence yang dapat diubah sesuai SLO dan tingkat risiko. Catat pemilik tindakan, severity, eskalasi dan bukti selesai.

## 5. Incident response and recovery planning

Buat severity matrix, escalation path, keputusan disable AI, fallback manual, backup/restore schedule, dan model rollback criteria. Untuk fitur device-critical, service manual harus jelas. Lakukan tabletop exercise sebelum production. Rencana saja belum membuktikan pemulihan.

## Studi kasus

Setelah sistem terpasang, kualitas klasifikasi bisa turun walau service tetap online. Kita merencanakan pengukuran outcome, inspeksi, update, backup, dan incident response sebelum gangguan nyata terjadi.

## Pertimbangan verifikasi

- Setiap metrik memiliki definisi yang tidak ambigu dan sumber data.
- Tersedia severity, owner, tindakan, escalation dan jadwal review.
- Tersedia backup/restore plan, rollback dan kebijakan model update.
- Privasi log dan akses observability diperhitungkan.
- Tidak ada klaim 'drift terdeteksi' tanpa data pengamatan.

## Bacaan primer

- https://sre.google/sre-book/monitoring-distributed-systems/
- https://www.nist.gov/itl/ai-risk-management-framework
- https://owasp.org/www-project-top-ten/

Pelajari teori ini sebagai landasan praktik, bukan sebagai KUK atau pedoman asesmen resmi. [Lab](lab-guide.md).