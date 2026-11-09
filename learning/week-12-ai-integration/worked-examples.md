# Worked Examples — Integrasi Anomaly Scoring dengan API

**Status:** contoh kode edukatif, bukan implementasi capstone yang telah dijalankan.

## Contoh 1 — Validasi output model numerik

**Masalah:** AI anomaly scorer mengirim `NaN`, skor negatif, atau `model_version` kosong.

Contoh kontrak Pydantic v2:

```python
from pydantic import BaseModel, ConfigDict, Field

class AnomalyResult(BaseModel):
    model_config = ConfigDict(extra="forbid")
    anomaly_score: float = Field(ge=0.0, le=1.0, allow_inf_nan=False)
    flagged: bool
    model_version: str = Field(min_length=1, max_length=64)
```

1. Adapter menghitung skor yang berada dalam kontrak 0–1; **skor ini tidak otomatis probabilitas kerusakan**.
2. Backend memvalidasi hasil sebelum menyimpan anomaly_event.
3. Output tidak valid masuk error taxonomy `invalid_model_output` dan **tidak** dipaksa menjadi skor nol.
4. Versi model disimpan untuk audit.

**Anti-pattern:** menganggap JSON dengan status HTTP 200 pasti aman dan langsung memicu perubahan pada perangkat listrik.

## Contoh 2 — Gagal inference tanpa kehilangan pengukuran

1. API menerima pembacaan meter yang valid dengan `meter_id, measured_at, energy_kwh`.
2. Simpan reading secara transaksional dan tetapkan state `pending_scoring`.
3. Adapter gagal karena timeout; reading **tidak dihapus**.
4. UI menampilkan pembacaan dan pesan `Scoring unavailable`, lalu menyediakan jalur review manusia.
5. Test fake adapter timeout harus memverifikasi reading count tetap, audit tertulis, dan tidak ada duplicate event.
6. Saat inference pulih, skor baru hanya disimpan jika output dan permission valid.

**Anti-pattern:** menimpa pembacaan energi dengan estimasi AI atau memalsukan status `normal` saat scoring gagal.

## Transfer challenge

Tambahkan aturan invalid numeric payload (`NaN`, `Infinity`, `energy_kwh < 0`), cross-site authorization, dan idempotency key. Jalankan negative tests ketika implementasi tersedia.
