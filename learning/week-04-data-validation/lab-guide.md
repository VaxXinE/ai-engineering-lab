# Praktikum Terstruktur — Validasi nilai energi dan timeline

**Status:** tugas **direncanakan**; implementasi Week 03–12 belum dijalankan. Semua input, site, meter dan timeseries adalah sintetis.

## Problem dan konteks profesional

Dalam file terdapat energy_kwh=NaN, 0, -1, interval_start tanpa Z, interval 60 menit, duplicate ID, dan gap 00:45. Kita harus membedakan error schema, nilai valid, dan data hilang.

**Single source of truth:** [kontrak domain](../../docs/architecture/energy-data-contract.md) · [threat model](../../docs/architecture/threat-model.md). Jangan mencampur kontrak klasifikasi log teks Week 01 dengan data anomaly scoring numerik Week 11–12.

## Langkah yang akan diimplementasikan saat sesi praktik

1. Definisikan indikator: kWh finite dan >=0, interval_minutes tepat 15, timestamp UTC/offset-aware dan align ke slot 15 menit; panjang ID serta known site/meter dibatasi.

2. Implementasikan schema validation; jangan melakukan silent coercion terhadap NaN, infinity, negatif atau timestamp tanpa timezone.

3. Pisahkan invalid row dari **missing slot**: gap 00:45 adalah quality anomaly, bukan measurement 0 kWh; catat expected vs observed slot.

4. Hitung completeness sebagai observed_unique_valid_intervals / expected_intervals, dan reject rate = invalid_rows / received_rows, dengan denominator tertulis.

5. Untuk evaluasi AI nanti, gunakan chronological train→validation→test; rolling feature untuk t hanya boleh memakai periode sebelum t.

6. Jalankan negative test dengan out-of-order, duplicate timestamp, wrong interval, future time yang melanggar policy, dan site mismatch.

## Acceptance criteria (belum dicentang)

- [ ] NaN/infinity/negatif ditolak; 0 kWh dapat valid bila sesuai aturan simulasi.
- [ ] Gap dilaporkan sebagai missing slot, tidak diisi nol tanpa penanda.
- [ ] Timestamp dinormalisasi UTC, interval diketahui dan konsisten.
- [ ] Data test tidak bocor ke fitting/scaler/rolling feature masa depan.

## Evidence yang harus dibuat

Validator, quality report dengan rumus, timestamp gap detector, test negative, data contract.

Saat praktik: catat input sintetis, expected behavior, actual output, command+versi runtime, error/negative tests, keamanan, dan link commit. Jangan mengarang skor model, latency, atau status passed.

## Pertanyaan transfer

Kenapa 0 kWh dan missing reading harus divisualisasikan berbeda?

**Definition of done:** seluruh acceptance criteria diverifikasi dengan artefak sendiri, bukan sekadar dokumentasi ini; status BNSP tetap memerlukan asesmen resmi LSP.

[Latihan](exercises.md) · [Knowledge check](knowledge-check.md) · [Evidence matrix](../../certification/evidence-matrix.md)
