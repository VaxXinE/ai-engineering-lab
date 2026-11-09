# Deep Dive — Integrasi inference dengan typed contracts, idempotency, dan failure containment

## Apa yang dapat dibuktikan setelah mempelajari modul?

1. Merancang strict input/output schema untuk inferensi dan status review.
2. Mengimplementasikan secara konseptual AI adapter yang bisa diganti.
3. Membedakan success, abstain, timeout, invalid output dan unauthorized.
4. Menyusun pengujian kontrak serta negative integration tests.

## Prinsip desain, mekanisme dan konsekuensi

### 1. Tentukan dua kontrak berbeda

Kontrak inference menerima validated message dan menghasilkan PredictedLabel + model_version + diagnostic metadata. Kontrak review menerima keputusan agent untuk object tertentu dengan identity/permission. Jangan membiarkan model menghasilkan user_id, tenant_id, atau access control decision. Output LLM ataupun model lokal harus divalidasi terhadap enum, batas panjang dan tipe; invalid output bukan kesalahan user.

### 2. Model API sebagai dependency yang bisa gagal

Provider bisa timeout, 429, 5xx, response berubah, version deprecated, atau token rate limit. Rancang failure taxonomy dan fungsi adapter yang menerjemahkan provider-specific errors menjadi domain errors. Jaga total request deadline; recovery state jelas untuk agent. Hindari retry tak terbatas karena biaya dan latency.

### 3. Simpan input dahulu, prediksi kemudian

Jika pesan diterima sebelum inference, persist inquiry dengan status pending. Setelah hasil valid, tambahkan prediction event dan status review. Saat inference gagal, inquiry tetap ditampilkan di manual review. Jika background worker digunakan, idempotency dan outbox atau reconciliation menjadi isu penting agar tidak ada double event setelah retry.

### 4. Boundary security dan injection

Teks customer adalah untrusted data; jika dimasukkan sebagai prompt LLM, ia dapat mengandung instruksi malicious yang meminta model mengabaikan aturan. Jangan menjadikan system prompt sebagai authorization; tools hanya boleh memiliki izin minimal dan tidak boleh mengambil data tenant lain. Secrets tetap di server. Sebelum menyimpan keluaran, lakukan output parsing, business validation dan escaping di UI.

### 5. Testing contracts dan observed behavior

Lakukan contract tests untuk normal label, abstain, invalid enum, unexpected nesting, missing model_version, timeout dan rate limit. Gunakan fake adapter agar tests deterministik dan tidak bergantung biaya/provider. API tests juga harus memverifikasi akses tenant cross-user dan tidak kehilangan inquiry saat model outage.

## Checklist penalaran

Ketika suatu solusi terlihat bekerja, tanyakan: (1) apakah hasil benar terhadap kontrak? (2) apakah tetap benar pada data berbeda? (3) apa yang terjadi bila dependency mati? (4) siapa yang berhak melihat/mengubah datanya? (5) bagaimana sistem membuktikan hasil pengujian? Jawab dengan contoh konkret, bukan sekadar kata "best practice".

## Sumber teknis primer

- https://fastapi.tiangolo.com/tutorial/handling-errors/
- https://docs.pydantic.dev/latest/concepts/models/
- https://genai.owasp.org/llm-top-10/

[Worked examples](worked-examples.md) · [Lab](lab-guide.md)
