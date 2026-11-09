# Deep Dive — Integrasi inference dengan typed contracts, idempotency, dan failure containment

## Apa yang dapat dibuktikan setelah mempelajari modul?

1. Merancang strict input/output schema untuk inferensi dan status review.
2. Mengimplementasikan secara konseptual AI adapter yang bisa diganti.
3. Membedakan success, abstain, timeout, invalid output dan unauthorized.
4. Menyusun pengujian kontrak serta negative integration tests.

## Prinsip desain, mekanisme dan konsekuensi

### 1. Tentukan dua kontrak berbeda

Numerical scoring menerima verified meter reading features + history, mengembalikan finite normalized `anomaly_score` [0,1], `flagged`, `model_version`, dan reason codes. Review API menerima keputusan operator atas AnomalyEvent. Auth context/site membership berasal dari backend; AI **tidak** boleh mengembalikan user/site permissions. Week 01 `normal/warning/fault` adalah text-lab terpisah.

### 2. Model API sebagai dependency yang bisa gagal

Provider bisa timeout, 429, 5xx, response berubah, version deprecated, atau token rate limit. Rancang failure taxonomy dan fungsi adapter yang menerjemahkan provider-specific errors menjadi domain errors. Jaga total request deadline; recovery state jelas untuk operator. Hindari retry tak terbatas karena biaya dan latency.

### 3. Simpan input dahulu, prediksi kemudian

Ingestion menyimpan valid `MeterReading` dengan `pending_scoring`. Scoring berhasil menambah `AnomalyEvent` append-only; timeout atau invalid response menghasilkan `scoring_unavailable` tanpa menghapus sumber. Bounded retry/queue didesain idempotent; human review tetap tersedia.

### 4. Boundary security dan injection

CSV dan model output dianggap untrusted. Validasi NaN/infinity, allowed score range, model_version, source identity dan role/site authorization; jangan memberi skor kemampuan mengubah izin atau mengendalikan listrik. Jika suatu saat memakai LLM untuk merangkum analisis, prompt injection ditangani sebagai risiko tambahan tanpa menukar authorization dengan system prompt.

### 5. Testing contracts dan observed behavior

Contract tests: valid finite score, NaN/inf, <0/>1, missing model_version, malformed structure, timeout/429/5xx. Integration tests juga memverifikasi object-scoped authorization, accepted reading tetap tersimpan, review audit append-only, dan tidak ada duplikat pada retry.

## Checklist penalaran

Ketika suatu solusi terlihat bekerja, tanyakan: (1) apakah hasil benar terhadap kontrak? (2) apakah tetap benar pada data berbeda? (3) apa yang terjadi bila dependency mati? (4) siapa yang berhak melihat/mengubah datanya? (5) bagaimana sistem membuktikan hasil pengujian? Jawab dengan contoh konkret, bukan sekadar kata "best practice".

## Sumber teknis primer

- https://fastapi.tiangolo.com/tutorial/handling-errors/
- https://docs.pydantic.dev/latest/concepts/models/
- https://genai.owasp.org/llm-top-10/

[Worked examples](worked-examples.md) · [Lab](lab-guide.md)
