# Deep Dive — Data quality sebagai penghalang sebelum AI, bukan cleanup kosmetik

> Materi lanjutan untuk pembaca yang sudah memahami software engineering dasar. **Contoh hitungan adalah ilustrasi**, bukan hasil pengujian sistem production.

## Learning outcomes yang harus bisa dibuktikan

1. Membedakan completeness, validity, accuracy, consistency, uniqueness dan timeliness.
2. Menyusun schema, business rules, serta data-quality report yang menggunakan denominator jelas.
3. Menganalisis train/test leakage dan quality gates.
4. Mendesain error response yang berguna tanpa mengekspos PII.

## Penjelasan konsep secara mendalam

### 1. Dimensi kualitas data dan pengukuran

Completeness menghitung kehadiran nilai wajib; validity memeriksa kesesuaian format/rentang; accuracy memerlukan pembandingan dengan fakta eksternal; consistency memastikan tidak bertentangan antar-field/sumber; uniqueness mengukur duplikat; timeliness mengukur kesegaran terhadap kebutuhan. Field email 'abc@example.test' mungkin valid sintaks tetapi belum tentu alamat nyata. Jangan menyimpulkan semua data berkualitas hanya dari valid rows yang lulus schema.

### 2. Schema, semantic rules dan normalization

Schema memeriksa tipe dan struktur; semantic rule menghubungkan data dengan konteks bisnis. received_at di masa depan bisa lolos parser ISO 8601 tetapi melanggar kebijakan platform. Tenant ID bisa berupa UUID valid namun tidak sah di organisasi tersebut; validasi authorization terpisah wajib. Normalisasi whitespace/case bermanfaat untuk dedup tetapi jangan mengubah raw text tanpa alasan karena bisa menghapus makna bahasa.

### 3. Validation boundary dan fail-safe defaults

Validasi paling awal dilakukan saat data masuk; aturan kritis juga ditegakkan di database dan pada output model. Return error yang dapat ditindaklanjuti per field, tetapi jangan membocorkan full message atau detail internal ke log. Untuk pipeline dengan data sebagian invalid, kebijakan quarantine atau reject dapat lebih aman daripada silent coercion (misalnya mengubah tanggal yang tak dapat diparse menjadi hari ini).

### 4. Profiling dan quality gate

Data profiling menghitung null, distribution per channel/label, panjang teks, jumlah duplikat, dan outliers. Gunakan per-metric numerator/denominator serta baseline. Reject rate 2% bukan selalu buruk dan 0% bukan selalu baik; mungkin filter terlalu permisif. Quality gate menggabungkan threshold, konsekuensi, exception workflow dan owner; hasilnya harus bisa direproduksi.

### 5. Data leakage dalam machine learning

Leakage bukan hanya duplikat teks persis. Dataset bisa bocor jika preprocessing belajar statistik dari seluruh data sebelum split, data dari customer yang sama tersebar di train dan test, atau fitur mengandung informasi tentang label masa depan. Split berdasarkan group atau waktu ketika relevan. Jangan terus tuning menggunakan test set karena ia berubah menjadi sumber keputusan model.

### 6. Privasi, anonymization dan retention

PII dalam chat dapat berupa nomor telepon, rekening, alamat, atau konteks kombinasi yang memungkinkan re-identification. Untuk pembelajaran buat data sintetis dari nol; tidak cukup mengganti nama pada chat sungguhan. Batasi retention, access policy, encryption dan audit. Output error dan model cards tidak perlu menyimpan pesan mentah jika statistik agregat sudah cukup.

## Miskonsepsi yang perlu diwaspadai

- Valid format berarti benar secara faktual → salah.
- Menghapus outlier selalu memperbaiki AI → bisa menghapus kasus penting.
- Data test boleh dipakai untuk fit scaler/vectorizer karena bukan label → tetap leakage.
- Semua missing values bisa diisi default → silent coercion bisa merusak audit.
- Anonimisasi dengan mengganti nama cukup untuk publik → konteks lain bisa mengidentifikasi individu.

## Transfer ke profesi full-stack

Ambil satu kebutuhan dari capstone [AI Customer Intelligence](../../projects/ai-customer-intelligence/README.md). Jelaskan **data apa yang tepercaya, aturan bisnis mana yang harus deterministik, apa yang bisa diprediksi AI, bagaimana failure ditangani, dan bagaimana keputusan diuji**. Jangan menyatakan modul selesai hanya dengan menyalin contoh.

## Bacaan lanjutan (dokumentasi dan pembelajaran primer)

- https://docs.pydantic.dev/latest/concepts/validators/
- https://scikit-learn.org/stable/common_pitfalls.html
- https://www.nist.gov/itl/ai-risk-management-framework

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md) · [Lab](lab-guide.md)
