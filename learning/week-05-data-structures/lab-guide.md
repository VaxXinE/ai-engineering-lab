# Praktikum Terstruktur — Sliding window dan agregasi per meter

**Status:** tugas **direncanakan**; implementasi Week 03–12 belum dijalankan. Semua input, site, meter dan timeseries adalah sintetis.

## Problem dan konteks profesional

1.000 interval 15 menit dari beberapa meter harus dikelompokkan per site/meter, dihitung total kWh, dan dinilai kandidat outlier tanpa membaca masa depan.

**Single source of truth:** [kontrak domain](../../docs/architecture/energy-data-contract.md) · [threat model](../../docs/architecture/threat-model.md). Jangan mencampur kontrak klasifikasi log teks Week 01 dengan data anomaly scoring numerik Week 11–12.

## Langkah yang akan diimplementasikan saat sesi praktik

1. Pilih struktur data: dict[(site_id,meter_id)] → list/iterator readings terurut waktu; set keys untuk dedup; deque untuk rolling window.

2. Definisikan invariant bahwa setiap record valid masuk satu kelompok dan semua timestamps dalam kelompok urut naik; gunakan deterministic tie policy.

3. Buat moving baseline dari **N pembacaan sebelumnya**, bukan termasuk target saat scoring bila itu berpotensi leakage.

4. Tulis fungsi agregasi total_energy_kwh=sum(energy_kwh). Bila butuh daya rata-rata, bagi total energi dengan durasi jam yang benar; jangan campur slot missing tanpa coverage.

5. Bandingkan memory O(n) untuk seluruh readings vs streaming O(window) per meter, catat trade-off urutan data dan buffering.

6. Test empty input, duplicate ID, out-of-order timestamp, missing interval, all-zero valid input, dan boundary N pertama.

## Acceptance criteria (belum dicentang)

- [ ] Total energi pada grup sesuai manual sum.
- [ ] Rolling feature tidak menggunakan timestamp > target.
- [ ] Missing interval tidak otomatis menjadi 0.
- [ ] ID grup site+meter tidak tercampur.

## Evidence yang harus dibuat

Algorithm spec, unit tests, complexity analysis, sample aggregation output.

Saat praktik: catat input sintetis, expected behavior, actual output, command+versi runtime, error/negative tests, keamanan, dan link commit. Jangan mengarang skor model, latency, atau status passed.

## Pertanyaan transfer

Bagaimana desain streaming berubah jika reading dari beberapa meter datang tak berurutan?

**Definition of done:** seluruh acceptance criteria diverifikasi dengan artefak sendiri, bukan sekadar dokumentasi ini; status BNSP tetap memerlukan asesmen resmi LSP.

[Latihan](exercises.md) · [Knowledge check](knowledge-check.md) · [Evidence matrix](../../certification/evidence-matrix.md)
