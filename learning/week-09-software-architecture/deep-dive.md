# Deep Dive — Arsitektur AI yang isolasi kegagalan dan tanggung jawabnya jelas

## Apa yang dapat dibuktikan setelah mempelajari modul?

1. Membedakan domain service, API adapter, repository, dan inference port.
2. Merancang data flow dan trust boundaries untuk AI service.
3. Menjelaskan kapan modular monolith lebih masuk akal daripada microservices.
4. Mendemonstrasikan rencana graceful degradation saat inference gagal.

## Prinsip desain, mekanisme dan konsekuensi

### 1. Tentukan boundary dari kebutuhan, bukan nama framework

Uraikan aktor agent, tenant, supervisor, browser, backend, database dan AI inference. Trust boundary memisahkan browser yang tidak dipercaya dari backend, dan komponen AI dari business logic. Data chat user harus divalidasi pada batas masuk; respons AI juga dianggap tidak dipercaya. Diagram C4 Context menjelaskan aktor dan hubungan; Container menjelaskan deployment-level units; Component menjelaskan modul internal. Gunakan kedalaman yang membantu pengambilan keputusan.

### 2. Modular monolith adalah pilihan sadar

Monolith modular memiliki deployment sederhana, transaksi DB lebih mudah, latency antar modul rendah dan dapat ditest end-to-end lebih cepat. Microservices berguna jika kapasitas, kepemilikan, kebutuhan deploy dan isolasi menuntutnya; tetapi menambah network failures, tracing, service identity dan consistency complexity. Tidak ada aturan bahwa aplikasi AI harus microservice. Mulai dengan modul jelas agar ekstraksi service kelak tidak memerlukan rewrite total.

### 3. Ports and adapters untuk vendor-independent AI

Domain service bergantung pada port interface: classify(message)->Prediction. Adapter lokal bisa Naive Bayes, remote adapter bisa hosted LLM; keduanya harus validasi output yang sama. Jangan meletakkan prompt, SDK, API key, atau aturan retry provider di controller bisnis. Tujuannya bukan overengineering, melainkan memisahkan risiko perubahan model/provider dari proses review customer.

### 4. Consistency dan asynchronous workflows

Synchronous inference dapat menambah latency endpoint create; asynchronous pattern menyimpan inquiry dahulu dan memproses inference kemudian. Jika database commit berhasil tetapi queue publish gagal, outbox pattern bisa membantu konsistensi; di skala kecil, status pending dan retry reconciler mungkin cukup. Rancang idempotency agar pesan tidak duplikat saat retry. Setiap strategi punya operational cost.

### 5. Security dan abuse controls

AuthN memverifikasi identitas; AuthZ menentukan akses per tenant/inquiry; input validation memastikan bentuk data; output encoding mencegah XSS; secrets tidak boleh masuk frontend atau logs. Model tidak punya hak memutuskan kepemilikan object. Gunakan least privilege untuk worker, DB dan provider, serta rate limiting untuk penggunaan mahal. Threat model menyebut asset, entry point, trust boundaries, possible attacker dan mitigasi.

## Checklist penalaran

Ketika suatu solusi terlihat bekerja, tanyakan: (1) apakah hasil benar terhadap kontrak? (2) apakah tetap benar pada data berbeda? (3) apa yang terjadi bila dependency mati? (4) siapa yang berhak melihat/mengubah datanya? (5) bagaimana sistem membuktikan hasil pengujian? Jawab dengan contoh konkret, bukan sekadar kata "best practice".

## Sumber teknis primer

- https://c4model.com/
- https://fastapi.tiangolo.com/
- https://owasp.org/www-project-api-security/

[Worked examples](worked-examples.md) · [Lab](lab-guide.md)
