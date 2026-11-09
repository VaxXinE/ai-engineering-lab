# Deep Dive — Mengukur kesehatan layanan dan AI secara terpisah

## Outcome terukur

1. Menentukan SLI dan SLO dari dampak pengguna, bukan angka acak.
2. Membedakan drift, quality degradation dan outage infra.
3. Menyusun maintenance plan lengkap dengan owner, threshold, backup dan incident class.
4. Mendesain release model quality gate dan rollback criteria.

## Pembahasan engineering

### 1. Service health bukan model quality

HTTP availability 99.9% hanya berarti endpoint banyak berhasil melayani request, bukan kategorinya benar. Untuk AI customer triage, ukur API error, p95 latency, queue backlog, abstention, disagreement dari human review dan per-class misrouting setelah label diverifikasi. Jangan memakai unverified review sebagai ground truth tanpa aturan; perubahan perilaku reviewer dapat menipu quality signal.

### 2. SLI, SLO dan SLA

SLI adalah metrik operasional, misalnya jumlah request valid yang sukses / request valid total. SLO adalah target internal beserta window seperti 99.5% 30 hari; SLA adalah komitmen formal dengan konsekuensi bila tidak tercapai. Target tutorial dipakai sebagai contoh pemikiran, bukan rekomendasi universal. Tentukan error budget untuk menimbang perubahan fitur vs reliability.

### 3. Drift dan feedback loop

Data drift adalah perubahan distribusi input; concept drift adalah perubahan hubungan fitur dengan target. Kata baru dalam pesan customer adalah potensi drift, tetapi belum membuktikan penurunan kualitas model. Teliti label policy, per-class metrics dan sampel baru yang representatif sebelum memutuskan retrain. Retraining otomatis dapat memperburuk model dan memasukkan feedback bias.

### 4. Risk-oriented maintenance calendar

Jadwalkan health review harian, quality review mingguan, dependency patch periodik, backup verification dan restore drill. Interval disesuaikan volume/risiko; yang penting mencantumkan owner, triggering events, rollback conditions dan evidence. Versi model, database schema dan dependencies perlu dicatat terpisah. Gunakan change approval saat risiko tinggi.

### 5. Backup retention, RPO/RTO

RPO adalah usia data maksimal yang rela hilang; RTO adalah durasi maksimal pemulihan yang ditargetkan. Backup frequency saja tidak membuktikan RPO; restore exercise pada test DB dan monitoring backup success diperlukan. Akses backup sering lebih sensitif daripada akses aplikasi biasa, perlu encryption dan least privilege.

### 6. Alert quality dan incident ownership

Alert harus actionable: siapa menerima, apa gejala, langkah diagnosis pertama, dan kapan eskalasi. Alert berlebihan meningkatkan alert fatigue. Incident plan mencakup model outage, invalid output, provider cost spike, DB outage, dan suspected PII leak. Perbaikan tidak boleh langsung menyuruh mematikan security controls demi kembali online.

## Transfer lesson ke dunia kerja

Buat daftar tindakan yang aman dilakukan di environment test dan yang memerlukan izin perubahan produksi. Jelaskan risiko dan keterbatasan serta apa yang harus diverifikasi dengan data nyata. Jangan gunakan materi demo sebagai bukti hasil production.

## Bacaan primer

- https://sre.google/sre-book/service-level-objectives/
- https://www.nist.gov/itl/ai-risk-management-framework
- https://www.postgresql.org/docs/current/backup.html

[Contoh lengkap](worked-examples.md) · [Tes pemahaman](knowledge-check.md)
