# Deep Dive — Instalasi AI yang reproducible dan tidak menyebarkan secret

## Outcome terukur

1. Membedakan build artifacts, image, container, config, dan deployment state.
2. Merancang local Compose dengan health/readiness dan least privilege.
3. Menulis runbook clean install, smoke test, rollback dan restore.
4. Mengidentifikasi risiko unpinned dependencies, model artifacts, dan destructive migrations.

## Pembahasan engineering

### 1. Dari workstation ke environment terkontrol

Aplikasi yang berjalan di laptop belum tentu dapat direproduksi. Catat versi OS, Python/Node, dependency lock, model artifact hash, database schema/migration state dan environment variables. Build immutable artifact lebih mudah dilacak daripada setiap deploy menginstal package dengan versi terbaru. Hindari latest tags untuk image dan script installer yang belum diaudit.

### 2. Container boundary dan network

Pisahkan frontend, API, inference, dan database sesuai kebutuhan. Docker Compose memberi orkestrasi pengembangan lokal; production dapat memerlukan konfigurasi berbeda. DB service seharusnya tidak di-publish ke jaringan publik tanpa kebutuhan dan proteksi yang jelas. Gunakan non-root process bila memungkinkan, filesystem read-only untuk komponen yang tidak menulis data, volume khusus, dan resource limits proporsional.

### 3. Secret injection

File .env.example hanya berisi placeholder. Credential asli disimpan di secret manager atau mekanisme runtime yang punya permission sesuai environment; jangan menempelkan secret dalam Dockerfile ARG/ENV yang masuk image layer atau log. Saat local demo, .env yang di-ignore tetap bukan pengganti kebijakan perlindungan produksi. Rotasi kunci dan revocation plan perlu dirancang.

### 4. Migrations dan compatibility

Database migration bukan operasi yang otomatis reversible. Jika aplikasi v2 menambah kolom lalu segera menghapus kolom lama, rollback ke v1 bisa gagal. Expand → migrate → contract memungkinkan periode overlap bila diperlukan. Sebelum destructive step, siapkan backup dan uji restore isolated. Model artifact juga punya schema compatibility terhadap tokenizer/features.

### 5. Liveness, readiness dan smoke test

Liveness menjawab apakah proses masih hidup; readiness menjawab dapatkah service melayani request saat ini. Health endpoint tidak boleh membeberkan secret. Smoke test end-to-end dengan satu meter reading sintetis memastikan UI/API/DB/model terhubung. HTTP 200 pada /health saja tidak membuktikan model output benar; uji kontrak minimal juga.

### 6. Rollback dan pembuktian instalasi

Runbook harus menyebut preflight, command, expected result, abort condition, smoke test, backup state dan rollback target. Catat release commit/image digest/model version. Deployment dikatakan terverifikasi hanya bila dijalankan pada environment sesuai dan hasil dicatat. Diagram saja belum cukup untuk bukti kompetensi memasang solusi AI.

## Transfer lesson ke dunia kerja

Buat daftar tindakan yang aman dilakukan di environment test dan yang memerlukan izin perubahan produksi. Jelaskan risiko dan keterbatasan serta apa yang harus diverifikasi dengan data nyata. Jangan gunakan materi demo sebagai bukti hasil production.

## Bacaan primer

- https://docs.docker.com/compose/
- https://docs.docker.com/build/building/best-practices/
- https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html

[Contoh lengkap](worked-examples.md) · [Tes pemahaman](knowledge-check.md)
