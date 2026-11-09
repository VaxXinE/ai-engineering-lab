# Deep Dive — Data quality sebagai penghalang sebelum AI, bukan cleanup kosmetik

> Materi lanjutan untuk pembaca yang sudah memahami software engineering dasar. **Contoh hitungan adalah ilustrasi**, bukan hasil pengujian sistem production.

## Learning outcomes yang harus bisa dibuktikan

1. Membedakan completeness, validity, accuracy, consistency, uniqueness dan timeliness.
2. Menyusun schema, business rules, serta data-quality report yang menggunakan denominator jelas.
3. Menganalisis train/test leakage dan quality gates.
4. Mendesain error response yang berguna tanpa mengekspos PII.

## Penjelasan konsep secara mendalam

### 1. Dimensi kualitas data dan pengukuran

Completeness untuk data meter adalah proporsi slot 15 menit yang benar-benar memiliki reading valid; validity memeriksa numerik finite, nonnegatif, timestamp timezone-aware serta durasi; consistency memeriksa meter/site dan satuan; uniqueness menolak kunci event ganda; timeliness memeriksa latency dari interval ke ingestion; accuracy memerlukan pembandingan dengan referensi yang dipercaya. **0 kWh valid berbeda dari missing interval**. Format yang dapat diparse bukan jaminan nilainya benar secara fisik.

### 2. Schema, semantic rules dan normalization

Schema v1 memerlukan site_id,meter_id,source_event_id,interval_start_utc,interval_minutes,energy_kwh,voltage_v,current_a. Validasi semantik memastikan interval 15 menit, timestamp UTC/offset-aware dan aligned, nilai finite/nonnegatif serta meter terdaftar di site. Jangan menyamakan API authorization dengan validasi struktur; site membership tetap diverifikasi server-side.

### 3. Validation boundary dan fail-safe defaults

Pisahkan parser CSV, schema validator, business rule dan database constraint. `NaN` dan `Infinity` harus ditolak secara eksplisit; nilai negatif bukan kWh konsumsi pada definisi v1. Jangan mengganti timestamp gagal parse dengan jam sekarang. Error report cukup row number dan error code; jangan mem-publish lokasi atau data asli.

### 4. Profiling dan quality gate

Profile expected vs observed time slots, invalid numeric count, duplikat source_event_id, konflik payload, data arrival lateness dan missing intervals per meter. Quality gate memiliki threshold hipotesis, owner, dan tindakan reject/quarantine; bukan klaim benchmark resmi. Missing reading adalah data-quality issue, bukan anomali konsumsi `0`.

### 5. Data leakage dalam machine learning

Karena meter menghasilkan deret waktu, evaluasi perlu split kronologis (train→validation→test). Fit scaler/threshold pada train/validation saja, dan rolling feature untuk interval t hanya boleh memakai interval sebelum t. Jangan memakai pola label anomali masa depan untuk memutuskan fitur saat training.

### 6. Privasi, anonymization dan retention

PII dalam telemetri dapat berupa nomor telepon, rekening, alamat, atau konteks kombinasi yang memungkinkan re-identification. Untuk pembelajaran buat data sintetis dari nol; tidak cukup mengganti nama pada telemetri sungguhan. Batasi retention, access policy, encryption dan audit. Output error dan model cards tidak perlu menyimpan pesan mentah jika statistik agregat sudah cukup.

## Miskonsepsi yang perlu diwaspadai

- Valid format berarti benar secara faktual → salah.
- Menghapus outlier selalu memperbaiki AI → bisa menghapus kasus penting.
- Data test boleh dipakai untuk fit scaler/vectorizer karena bukan label → tetap leakage.
- Semua missing values bisa diisi default → silent coercion bisa merusak audit.
- Anonimisasi dengan mengganti nama cukup untuk publik → konteks lain bisa mengidentifikasi individu.

## Transfer ke profesi full-stack

Ambil satu kebutuhan dari capstone [AI Smart Energy Monitoring](../../projects/ai-energy-intelligence/README.md). Jelaskan **data apa yang tepercaya, aturan bisnis mana yang harus deterministik, apa yang bisa diprediksi AI, bagaimana failure ditangani, dan bagaimana keputusan diuji**. Jangan menyatakan modul selesai hanya dengan menyalin contoh.

## Bacaan lanjutan (dokumentasi dan pembelajaran primer)

- https://docs.pydantic.dev/latest/concepts/validators/
- https://scikit-learn.org/stable/common_pitfalls.html
- https://www.nist.gov/itl/ai-risk-management-framework

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md) · [Lab](lab-guide.md)
