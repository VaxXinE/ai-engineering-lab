# Worked Examples — Arsitektur AI yang isolasi kegagalan dan tanggung jawabnya jelas

**Semua cuplikan/angka adalah demonstrasi edukatif**, bukan bukti sudah diimplementasikan atau dideploy pada capstone. Jalankan dan catat hasil sebenarnya ketika masuk sesi praktikum.

## Solusi 1: Alur error AI pada modular monolith

**Masalah:** Create meter reading sukses menyimpan data, tetapi inference timeout.

**Tahapan pemecahan:**

1. Browser mengirim POST /meter readings dengan autentikasi; backend memvalidasi tenant dan payload.

2. Database menyimpan meter reading status=pending_inference dan commit. Model dipanggil lewat interface dengan timeout.

3. Saat timeout, backend tidak menghapus meter reading; status pending_manual_review atau pending_retry sesuai kebijakan.

4. Operator dashboard tetap menampilkan pesan dan memungkinkan review manual. Correlation ID membantu tracing.

5. Skenario diuji dengan fake adapter yang selalu timeout, bukan mematikan provider produksi.

**Anti-pattern:** Buruk: transaksi DB dibuka selama menunggu model remote lama, lalu timeout mengunci resource atau menghilangkan pesan.

**Explain-back:** bagaimana cara membuat negative test untuk membuktikan anti-pattern tersebut?

## Solusi 2: Merancang port aplikasi dengan code contract

**Masalah:** Model lokal akan diganti model API, tetapi UI dan domain business rules tak boleh berubah.

**Tahapan pemecahan:**

1. Contoh Python interface ilustratif:

```python
from typing import Protocol, Literal
from dataclasses import dataclass

Label = Literal['normal','warning','fault','abstain']

@dataclass(frozen=True)
class Prediction:
    label: Label
    model_version: str

class Classifier(Protocol):
    def predict(self, text: str) -> Prediction: ...
```

2. Domain memanggil Classifier, bukan sdk.telemetri.completions.create secara langsung.

3. Adapter baru wajib lulus contract test label enum, model_version, input limits dan timeout behavior.

4. UX tidak perlu tahu provider model; output tetap kontrak domain yang sama.

**Anti-pattern:** Jika provider-specific JSON tersebar di controller dan frontend, migrasi provider menyebabkan breaking change luas.

**Explain-back:** bagaimana cara membuat negative test untuk membuktikan anti-pattern tersebut?

## Progressive practice

- **Demonstrate:** trace contoh dengan input dan output yang diketahui.
- **Faded:** ganti satu parameter dan isi satu langkah yang sengaja dihilangkan sendiri.
- **Independent:** rancang kasus lain yang menuntut trade-off berbeda.
- **Verify:** jalankan test, simpan version/command/output aktual; jangan mengarang benchmark.

[Quiz dengan feedback](knowledge-check.md)
