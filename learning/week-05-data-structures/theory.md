# Teori — Struktur Data untuk Telemetri Energi (Week 05)

**Outcome:** memilih struktur data sesuai operasi dan menguji agregasi time-series tanpa duplikasi atau future leakage.

## 1. Tentukan operasi

- `list`: preserve order, cocok untuk satu meter dengan interval berurutan.
- `dict[(site_id,meter_id)]`: kelompokkan meter, average dictionary lookup O(1) dalam kondisi lazim.
- `set[(site_id,meter_id,source_event_id)]`: membership/duplicate detection di satu proses; bukan pengganti UNIQUE database.
- `deque(maxlen=N)`: mempertahankan rolling window N **pembacaan sebelumnya**, efisien append/popleft.
- `Counter`: agregasi jumlah event per site / status quality.

## 2. Complexity

Nested scan duplikat lazimnya O(n²) untuk n rows. Scan dengan set memberi average O(n), tetapi memakai O(n) memory. Untuk file besar, pertimbangkan streaming dan dedup lewat DB constraint. Benchmark aktual memerlukan ukuran data, seed, hardware, runtime dan perintah, bukan angka perkiraan.

## 3. Aggregation yang menjaga satuan

`total_energy_kwh = sum(valid_interval.energy_kwh)`. Untuk slot 15 menit dan coverage lengkap, `average_power_kw = total_energy_kwh / (slot_count * 15/60)`. Jika sebagian slot hilang, jangan membuat kesimpulan total konsumsi seluruh rentang tanpa menjelaskan coverage. Menjumlah kW sesaat seolah energi adalah salah satuan.

## 4. Sliding window untuk anomaly baseline

Hitung median atau statistik dari interval **sebelum t**, baru skor interval t. Setelah scoring, masukkan nilai t ke window untuk interval berikutnya. Kalau memasukkan t dahulu, lonjakan bisa memengaruhi baseline dirinya sendiri.

## 5. Tests dan failure modes

- Empty input menghasilkan total 0 dan coverage 0 dengan pembagi aman.
- Duplicate input tidak terhitung dua kali.
- SITE-A/MTR-001 terpisah dari SITE-B/MTR-001.
- Out-of-order data diurutkan dengan kebijakan jelas, atau dibuffer/reject.
- Missing interval tidak otomatis dijadikan `0 kWh`.
- Batas N dan ukuran batch mencegah memory exhaustion.

[Lihat praktikum](lab-guide.md) · [Worked examples](worked-examples.md) · [Kontrak domain](../../docs/architecture/energy-data-contract.md).

Referensi: [Python collections](https://docs.python.org/3/library/collections.html), [Python data structures](https://docs.python.org/3/tutorial/datastructures.html).
