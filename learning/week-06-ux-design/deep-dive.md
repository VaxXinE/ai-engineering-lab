# Deep Dive — UX AI: mengurangi kesalahan keputusan manusia, bukan sekadar membuat dashboard rapi

**Target:** setelah modul, lo dapat mempertahankan pilihan desain melalui contoh dan kontra-contoh, bukan sekadar mengingat istilah.

## Learning outcomes

1. Memetakan task dan error flow dari meter reading hingga keputusan operator.
2. Mendesain human-in-the-loop agar prediksi dapat dikoreksi dan diaudit.
3. Menjelaskan tampilan ketidakpastian tanpa klaim confidence palsu.
4. Menyusun usability test berbasis tugas dan accessibility acceptance criteria.

## Pembahasan konsep dan trade-off

### 1. Mulai dari pekerjaan pengguna

Energy analyst perlu menemukan pola konsumsi, operator perlu memeriksa kandidat anomali, maintainer memeriksa ingestion dan scoring availability. Flow utama: pilih site/meter → lihat tren `energy_kwh` per 15 menit → lihat konteks missing data → review anomaly candidate → konfirmasi keputusan → lihat audit history. Kualitas UX diukur dari kesalahan membaca satuan, waktu menemukan interval, keberhasilan review dan apakah status model dapat dibedakan dari keputusan manusia.

### 2. AI output dan ketidakpastian

Numeric `anomaly_score` dalam rentang [0,1] adalah ranking yang didefinisikan model, **bukan** peluang kerusakan. Tampilkan candidate flag, model_version, pembanding historis dan quality flags. Jika `scoring_unavailable`, jangan tampilkan 'normal'. Jika interval hilang, tampilkan gap, bukan 0 kWh.

### 3. Human review sebagai control

Operator dapat memilih `confirmed_anomaly`, `expected_variation`, atau `needs_investigation`, dengan alasan. Simpan raw reading, anomaly score, dan review event secara terpisah. Jika dua operator mengedit event yang sama, tampilkan 409 conflict/reload sambil mempertahankan draft. Hindari tombol otomatis yang memutus listrik atau menyatakan kondisi berbahaya hanya dari skor.

### 4. UX states dan loss prevention

Loading, empty, error, unauthorized, stale data, konflik edit, dan network offline perlu desain. Menghilangkan draft ketika HTTP 500 meningkatkan biaya manusia. Tampilkan pesan error yang menolong tanpa membocorkan detail server, dan sediakan retry dengan idempotency key. Accessibility mencakup keyboard, focus management, label, status text, dan contrast; tidak cukup 'warna merah artinya error'.

### 5. Uji usability yang observable

Tugas uji: temukan meter MTR-001, jelaskan apakah titik 00.30 (5.9 kWh) berpotensi outlier, bedakan slot hilang dengan 0, lakukan review dan pulihkan draft setelah error. Ukur task success, salah baca unit, bantuan yang diperlukan, serta keyboard navigation. Sampel kecil memberi insight awal, bukan bukti usability universal.

## Aplikasi dalam AI Smart Energy Monitoring

Pikirkan perubahan berikut: traffic 10 kali lebih tinggi, perangkat memakai dua tenant, pengguna dapat memasukkan teks tidak tepercaya, dan AI service suatu saat mati. Desain mana yang tetap aman? Apa yang mesti diubah? Tuliskan konsekuensi pada kode, data, UX, keamanan, dan monitoring.

## Bacaan primer

- https://www.w3.org/WAI/WCAG22/quickref/
- https://www.nngroup.com/articles/ten-usability-heuristics/
- https://www.nist.gov/itl/ai-risk-management-framework

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md)
