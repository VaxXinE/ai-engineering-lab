# Worked Examples — Data Structures untuk Meter Readings

## 1. Deduplikasi composite event identity

Input: `[('A','M1','E1'),('A','M1','E2'),('A','M1','E1'),('B','M1','E1')]`.

```python
rows = [('A','M1','E1'), ('A','M1','E2'), ('A','M1','E1'), ('B','M1','E1')]
seen, output = set(), []
for row in rows:
    if row not in seen:
        seen.add(row)
        output.append(row)
assert output == [('A','M1','E1'), ('A','M1','E2'), ('B','M1','E1')]
```

Dengan set, average runtime O(n) dengan tambahan memory O(n). Tanpa `site_id`, event SITE-B akan tertolak keliru. Kode ini **hanya untuk pembelajaran**; database UNIQUE tetap dibutuhkan pada sistem multi-worker.

## 2. Rolling window tanpa membaca masa depan

Data M1: kWh interval `[1.0, 1.1, 5.9, 1.2]`. Saat memberi skor untuk nilai 5.9 pada slot ketiga, gunakan history `[1.0,1.1]`; nilai 5.9 **jangan dimasukkan terlebih dahulu** ke window. Setelah memberi skor, window dapat diperbarui untuk interval berikutnya.

Contoh pseudocode:

```python
from collections import deque
history = deque(maxlen=2)
for kwh in [1.0, 1.1, 5.9, 1.2]:
    baseline = sum(history) / len(history) if history else None
    print(kwh, baseline)  # illustrative; not a deployed detector
    history.append(kwh)
```

**Batas:** jumlah slot, bukan waktu jika ada gap. Untuk rolling berbasis waktu, validasi kontinuitas timestamp; data terlambat dan out-of-order harus ditangani.

[Data contract](../../docs/architecture/energy-data-contract.md) · [Latihan](exercises.md).
