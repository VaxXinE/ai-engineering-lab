# Applied Energy Case — Memilih baseline anomali untuk meter 15 menit

**Status:** worked case untuk belajar; bukan hasil implementasi atau asesmen formal. **Latar:** site dan meter sepenuhnya sintetis.

## Problem

Bandingkan rolling median/IQR, Isolation Forest dan hosted language model untuk angka kWh per interval. Constraints: offline lab, interpretability, biaya dan kemudahan monitoring.

## Worked reasoning — mengapa solusinya begitu?

IQR cocok baseline pertama karena transparan, tetapi bermasalah pada distribusi musiman. Isolation Forest memerlukan fitur numerik dan threshold selection. LLM bukan scorer utama time-series. Pilih baseline secara sementara; lakukan evaluasi held-out berbasis waktu untuk keputusan final.

## Guided → Independent challenge

**Guided:** ulangi penalaran di atas dan jelaskan setiap asumsi.  
**Faded:** ubah satu angka/aturan lalu tulis ulang satu langkah yang diperlukan.  
**Independent:** Tulis ADR dengan bobot interpretability 35%, quality 30%, cost 20%, ops 15%. Ubah satu bobot dan jelaskan perubahan keputusan.

## Negative case & security/reliability

Model dan dependency supply chain; jangan menjalankan package tak dipercaya atau mengirim data meter asli ke provider luar.

**Verifikasi yang disyaratkan saat praktik:** positif + negatif, expected vs actual, environment/runtime, test commands, kondisi gagal, dan catatan keterbatasan. Jangan tandai lulus hanya karena membaca contoh.

## Evidence target

ADR, tool comparison matrix, model comparison plan dan provenance checklist.

**Kontrak:** [Energy Data Contract](../../docs/architecture/energy-data-contract.md) · [Threat model](../../docs/architecture/threat-model.md) · [Learning gates](../../docs/architecture/energy-learning-gates.md).
