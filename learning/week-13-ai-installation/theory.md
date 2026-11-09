# Teori — Instalasi, Konfigurasi dan Deployment AI

**Tujuan:** Menyiapkan runtime yang reproducible, rahasia yang terlindungi, health checks, release metadata, dan proses rollback.

## 1. Environment reproducibility

Pisahkan development/test/production configuration. Lock dependency, kontrol versi runtime dan catat OS/arsitektur. Docker image bukan jaminan reproducible jika tag floating, install tak pinned atau model artifact berubah; dokumentasikan lockfile dan checksum untuk model/release.

## 2. Secrets and permissions

Tidak pernah menaruh .env dengan nilai sesungguhnya dalam Git atau image. Gunakan secret injection yang tepat untuk target deployment; least privilege untuk DB user, container dan file. Docker Compose lokal bukan otomatis konfigurasi aman untuk internet terbuka.

## 3. Startup and health probes

Liveness memeriksa proses tidak stuck; readiness memeriksa service dapat melayani request; model readiness memeriksa artifact valid/tersedia. Backend harus bisa melaporkan health tanpa mengekspos nama/isi secret atau data privat. Migration version perlu dicek sebelum API menerima traffic.

## 4. Release and rollout

Buat preflight check, migrate database, start services, smoke test, lalu traffic. Gunakan runbook dengan preconditions, expected outcomes, rollback, dan troubleshooting. Perubahan database yang tidak backward compatible dapat membuat rollback aplikasi gagal; rancang expand/migrate/contract.

## 5. Recovery strategy

Backup terenkripsi dan restore teruji dibedakan dari sekadar restart container. Backup hanya berguna jika bisa dipulihkan. RPO adalah toleransi kehilangan data, RTO adalah target waktu pulih; keduanya harus punya asumsi dan bukti uji.

## Studi kasus

Aplikasi yang berjalan pada laptop developer perlu bisa dipasang ulang di lingkungan test tanpa hidden manual setup. Gunakan container untuk UI, API, dan database serta model artifact tervalidasi.

## Pertimbangan verifikasi

- Satu runbook cukup untuk instalasi pada environment bersih.
- Tidak ada credential asli, privileged container yang tidak perlu, atau secret di image.
- Health/status endpoints memberi sinyal operasional yang tepat.
- Smoke test dan rollback diuji serta hasilnya dicatat.
- Model artifact punya provenance/version/hash atau kontrol setara.

## Bacaan primer

- https://docs.docker.com/compose/
- https://docs.docker.com/build/building/best-practices/
- https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html

Pelajari teori ini sebagai landasan praktik, bukan sebagai KUK atau pedoman asesmen resmi. [Lab](lab-guide.md).