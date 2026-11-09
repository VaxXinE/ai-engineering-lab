# Worked Examples — Integrasi inference dengan typed contracts, idempotency, dan failure containment

**Semua cuplikan/angka adalah demonstrasi edukatif**, bukan bukti sudah diimplementasikan atau dideploy pada capstone. Jalankan dan catat hasil sebenarnya ketika masuk sesi praktikum.

## Solusi 1: Typed Pydantic response untuk AI classifier

**Masalah:** Model menghasilkan JSON dengan kategori tidak sah seperti 'admin', model_version hilang atau confidence sebagai string.

**Tahapan pemecahan:**

1. Definisikan enum label dan field versi model required; hindari silent coercion.

2. Cuplikan ilustratif Pydantic v2:

```python
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

class AIResult(BaseModel):
    model_config = ConfigDict(extra='forbid')
    label: Literal['sales','support','general','abstain']
    model_version: str = Field(min_length=1, max_length=64)

# AIResult.model_validate({'label':'admin','model_version':'v1'})
# raises a ValidationError
```

3. Provider adapter menangkap validation error dan menandainya invalid_model_output; jangan me-retry input tidak valid tanpa alasan.

4. Simpan valid result dengan model_version dan request id; kategori yang tidak dikenal tidak boleh diteruskan ke workflow.

**Anti-pattern:** Menggunakan parse JSON lalu memasukkan kategori mentah ke DB dapat membuat role/admin logic salah mengartikan output.

**Explain-back:** bagaimana cara membuat negative test untuk membuktikan anti-pattern tersebut?

## Solusi 2: Sequence error untuk inference timeout

**Masalah:** Inquiry tersimpan namun AI model tidak merespons dalam deadline yang disepakati.

**Tahapan pemecahan:**

1. POST inquiry valid → commit record dengan status pending_inference.

2. Adapter memanggil AI dengan timeout; request gagal sehingga status berubah ke pending_manual_review dengan audit event.

3. UI menampilkan inquiry dan memberi action review agent; tidak memalsukan prediction 'general'.

4. Integration test memakai fake adapter timeout dan assert record tetap ada serta review action authorized.

**Anti-pattern:** Menyimpan transaction lock selama remote request lama dapat mengurangi throughput dan meningkatkan deadlock/resourcing risk.

**Explain-back:** bagaimana cara membuat negative test untuk membuktikan anti-pattern tersebut?

## Progressive practice

- **Demonstrate:** trace contoh dengan input dan output yang diketahui.
- **Faded:** ganti satu parameter dan isi satu langkah yang sengaja dihilangkan sendiri.
- **Independent:** rancang kasus lain yang menuntut trade-off berbeda.
- **Verify:** jalankan test, simpan version/command/output aktual; jangan mengarang benchmark.

[Quiz dengan feedback](knowledge-check.md)
