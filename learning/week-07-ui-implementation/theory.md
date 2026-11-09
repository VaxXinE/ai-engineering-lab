# Teori — Frontend Dashboard Energy Anomaly (Week 07)

**Outcome:** menerapkan dashboard timeseries dengan TypeScript state yang aman terhadap race, invalid model score, dan site-scoping.

## 1. Component boundaries

Rancang `EnergyOverview`, `MeterTrendChart`, `AnomalyTable`, `ReviewForm` dan `StatusNotice`. Pisahkan data-fetching dari presentasi. Gunakan discriminated union untuk request state `idle|loading|success|empty|error`, dan jangan gabungkan score status dengan review status.

## 2. Unit dan data gaps

Chart menunjukkan `energy_kwh` per 15 menit, bukan kW instan. `null` / missing time slot bukan `0`; jangan membiarkan chart library melakukan interpolation sebagai pembacaan nyata. Timestamp disimpan UTC; format untuk display mengikuti zona waktu user.

## 3. Async UI and concurrency

Filter Site-A lalu Site-B bisa menghasilkan response tak berurutan. Gunakan AbortController atau request-sequence key dan cache partition berdasarkan site+meter+time window. Saat submit review, cegah double click **di UI**, tetapi backend tetap membutuhkan idempotency/versioning. Pada HTTP 409, pertahankan draft dan tawarkan refresh/merge.

## 4. Validasi dan keamanan

Output AI harus finite score [0,1], flagged boolean, model_version string. Validasi schema di API dan UI; jangan menjadikan skor sebagai probabilitas kegagalan. React secara default escape text nodes, tetapi raw HTML injection tetap berisiko. Authorization **selalu server-side**; client-side filtering dan menyembunyikan tombol tidak menghalangi IDOR.

## 5. Accessibility

Gunakan native HTML elements, labels dan aria-live messages yang tepat untuk perubahan status. Loading, empty, error dan scoring_unavailable masing-masing perlu pesan berbeda. Seluruh review flow dapat dipakai melalui keyboard, label grafik tersedia dalam alternatif tabel.

## Worked scenario

MTR-001 mencatat 5.90 kWh pada 00:30. Model memberi `flagged=true`; operator memilih `expected_variation`. UI menyimpan review via API dan menampilkan riwayat. Jika API gagal, alasan review tetap ada di form. Jangan menulis ulang measurement sumber saat keputusan diubah.

[Praktikum](lab-guide.md) · [Typed state example](worked-examples.md) · [Threat model](../../docs/architecture/threat-model.md).

Referensi: [React](https://react.dev/learn), [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html), [WCAG](https://www.w3.org/WAI/WCAG22/quickref/).
