# Worked Examples — Memilih Pendekatan Anomaly Detection Energi

## Contoh 1 — Weighted decision matrix

**Masalah:** data meter interval 15 menit harus dianalisis, dataset masih sintetis, belum punya banyak label anomali.

Bandingkan:
- **A: IQR/rolling baseline** — mudah dijelaskan, rendah kompleksitas, threshold perlu dijaga.
- **B: Isolation Forest** — dapat belajar kombinasi fitur, butuh data training dan evaluasi lebih hati-hati.
- **C: Hosted LLM** — tidak cocok sebagai scorer utama angka timeseries dalam problem ini; latency, privacy, dan biaya tambahan.

Bobot ilustratif: interpretabilitas 35%, kualitas potensial 30%, biaya 20%, kemudahan operasi 15%. Skor asumsi 1–5:

| Kriteria | Bobot | A | B | C |
| --- | ---: | ---: | ---: | ---: |
| Interpretabilitas | 35% | 5 | 3 | 2 |
| Kualitas potensial | 30% | 3 | 4 | 2 |
| Biaya | 20% | 5 | 4 | 2 |
| Operasional | 15% | 5 | 3 | 2 |

Hitung:
- A = 0.35×5 + 0.30×3 + 0.20×5 + 0.15×5 = **4.40**.
- B = 0.35×3 + 0.30×4 + 0.20×4 + 0.15×3 = **3.50**.
- C = 0.35×2 + 0.30×2 + 0.20×2 + 0.15×2 = **2.00**.

**Keputusan sementara:** baseline IQR untuk MVP, lalu bandingkan dengan model ML. Ini **simulasi skor**, bukan hasil benchmark nyata.

## Contoh 2 — ADR local-first

**Context:** semua data sintetis; ingin mengurangi dependency eksternal, menjelaskan keputusan model dan memudahkan evaluasi offline.

**Options:** heuristik statistik, Isolation Forest, hosted model.

**Decision:** bangun heuristik statistik sebagai baseline awal, lalu uji ML bila data memadai.

**Validation plan:** held-out time split, precision/recall pada injected labels sintetis, alert rate, latency, dan cost. Simpan keputusan revisi jika model baru menunjukkan peningkatan yang valid.

**Anti-pattern:** memilih deep learning karena populer tanpa dataset, metric, atau kebutuhan yang mendukung.

## Transfer exercise

Jika meter berubah dari interval 15 menit ke 60 menit, revisi kriteria perbandingan dan jelaskan mengapa energy_kwh dan kW tidak dapat langsung disamakan.
