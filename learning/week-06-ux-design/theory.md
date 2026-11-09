# Teori — UX Dashboard Analitik Energi (Week 06)

**Outcome:** mendesain alur Energy Overview → Meter Detail → Anomaly Review → Audit History yang dapat dipahami operator dan aman ketika data/model gagal.

## 1. Alur tugas dan persona

**Energy analyst** menilai tren pemakaian. **Facility operator** memeriksa kandidat anomali; **system maintainer** mengurus error ingestion/inference. Jangan menggabungkan seluruh kebutuhan itu dalam satu layar padat. Tetapkan task terukur: menemukan periode konsumsi tinggi, memeriksa kualitas pembacaan, dan menyimpan review tanpa kehilangan draft.

## 2. Kebenaran satuan dan visualisasi

Grafik memakai `energy_kwh` **per 15 menit**, sumbu dan tooltip mencantumkan durasi dan zona waktu. Untuk grafik kekosongan data, tampilkan **gap**, bukan titik `0 kWh`. Konversi ke average kW hanya ketika durasinya jelas. Hindari menyebut satu titik energi tinggi sebagai 'sensor rusak'.

## 3. AI assistive, bukan autonomous

Tampilkan `anomaly_score` sebagai skor internal/ranking dengan model_version dan indikator `candidate anomaly`. Jangan menampilkan skor 0.93 sebagai peluang 93% kerusakan. Review human mempunyai decision `confirmed_anomaly`, `expected_variation` atau `needs_investigation`. Simpan keputusan manusia terpisah dari skor asli.

## 4. Error/empty/conflict flows

Empty: meter belum memiliki readings. Missing: ada slot waktu kosong. Offline/scoring_unavailable: readings tetap terlihat. Unauthorized: tidak membuka site lain. Conflict: dua operator mengedit review version lama → tampilkan konflik sambil mempertahankan draft. Semua kondisi perlu copywriting yang jelas, keyboard access dan fokus yang dapat diprediksi.

## 5. Pengujian usability

Task contoh: temukan MTR-001, bandingkan tiga interval, review satu kandidat anomali. Ukur task success, kesalahan interpretasi satuan, waktu, dan kebutuhan bantuan. Jumlah partisipan sedikit hanya memberikan insight awal, bukan bukti universal.

**Anti-pattern:** menampilkan alert 'Bahaya listrik' atau perintah pemadaman berdasarkan anomali model. Sistem pembelajaran ini tidak memproses keputusan keselamatan.

[Praktikum UX](lab-guide.md) · [Worked examples](worked-examples.md) · [WCAG 2.2 Quick Ref](https://www.w3.org/WAI/WCAG22/quickref/).
