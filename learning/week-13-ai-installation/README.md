# Week 13 — Instalasi, Konfigurasi dan Deployment AI

**Status materi:** siap dipelajari · **Status implementasi:** belum dikerjakan · **Estimasi:** 8–10 jam

**Acuan unit:** J.62AIN00.015.1 — Memasang Solusi AI. Kode unit dan KUK final memerlukan konfirmasi LSP.

**Tujuan:** Menyiapkan runtime yang reproducible, rahasia yang terlindungi, health checks, release metadata, dan proses rollback.

## Cara pakai materi
1. Baca [teori](theory.md) dan jelaskan inti konsep dengan bahasa sendiri.
2. Ikuti [lab-guide](lab-guide.md) untuk implementasi (ketika pembelajaran dimulai).
3. Kerjakan [exercises](exercises.md) dan [simulasi asesmen](assessment.md).
4. Simpan artefak nyata di repo dan hubungkan ke [evidence matrix](../../certification/evidence-matrix.md).

**Skenario:** Aplikasi yang berjalan pada laptop developer perlu bisa dipasang ulang di lingkungan test tanpa hidden manual setup. Gunakan container untuk UI, API, dan database serta model artifact tervalidasi.

**Indikator:** 
- Satu runbook cukup untuk instalasi pada environment bersih.
- Tidak ada credential asli, privileged container yang tidak perlu, atau secret di image.
- Health/status endpoints memberi sinyal operasional yang tepat.
- Smoke test dan rollback diuji serta hasilnya dicatat.
- Model artifact punya provenance/version/hash atau kontrol setara.

Baca [roadmap](../../docs/learning-roadmap.md) dan [capstone](../../projects/ai-customer-intelligence/README.md). Keberadaan panduan tidak berarti kompetensi telah diverifikasi.