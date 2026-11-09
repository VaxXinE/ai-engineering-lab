# Teori — Integrasi Komponen Solusi AI

**Tujuan:** Menyatukan model inference, service API, storage, review UI, dan pengujian end-to-end tanpa membuat AI menjadi single point of failure.

## 1. Contract-first integration

Rancang request/response schema yang ketat sebelum menghubungkan UI, API dan model. Untuk capstone numerik, output harus memuat finite anomaly_score dalam kontrak 0–1, boolean flagged, dan model_version; label normal/warning/fault hanya digunakan pada latihan teks Modul 1. Status aplikasi seperti pending_scoring/reviewed bukan hasil model. Pisahkan status agar proses bisnis tidak mengira prediksi sebagai keputusan final.

## 2. Ports and adapters

Definisikan antarmuka scoring dengan method score(reading_features)->AnomalyResult; implementasi lokal/hosted berada di adapter tersendiri. Ini memudahkan unit testing memakai fake adapter tanpa biaya provider, dan memungkinkan penggantian model setelah evaluasi. Jangan menaruh provider-specific behavior dalam domain service.

## 3. Transaction and failure handling

Simpan meter reading secara konsisten, lalu lakukan inference dengan timeouts terkendali; jika provider gagal, jangan hilangkan pesan. Untuk pemrosesan asynchronous gunakan queue dan idempotency key. Status pending_manual_review lebih aman daripada menciptakan prediksi tebakan baru saat service tidak tersedia.

## 4. Security boundary

Authentication dan server-side object-level authorization wajib untuk endpoint review. Validasi payload panjang, label output model, dan safe logging; catatan kejadian perangkat tidak boleh dikirim ke eksternal tanpa otorisasi kebijakan dan data minimization. Prompt injection relevan bila nanti menggunakan LLM dengan tool atau retrieval.

## 5. Test pyramid

Unit test inference adapter dan domain service, integration test API + database, contract tests untuk model response, serta end-to-end scenario UI. Test error 400/401/403/429/5xx dan timeout. Mock model behavior dalam test, bukan mengetes production API berulang.

## Studi kasus

Aplikasi dashboard energi menerima meter reading baru. Service memvalidasi input dan izin, menyimpan record, meminta prediksi melalui inference adapter, memvalidasi label hasil, lalu menampilkan status review. Inference dapat gagal atau memilih abstain.

## Pertimbangan verifikasi

- Prediksi yang tersimpan selalu mempunyai model_version dan valid label.
- Data meter reading tidak hilang ketika AI gagal.
- Izin akses dites untuk resource berbeda dan tenant lain.
- UI dapat menerima hasil normal, abstain, timeout dan invalid model output.
- Ada bukti tests yang dijalankan, bukan screenshot tanpa reproduksi.

## Bacaan primer

- https://fastapi.tiangolo.com/tutorial/
- https://docs.pydantic.dev/latest/
- https://owasp.org/www-project-api-security/

Pelajari teori ini sebagai landasan praktik, bukan sebagai KUK atau pedoman asesmen resmi. [Lab](lab-guide.md).