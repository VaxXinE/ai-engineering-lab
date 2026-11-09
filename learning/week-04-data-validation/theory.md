# Teori — Week 04: Data Quality, Validation & Leakage Prevention

**Tujuan:** Menetapkan aturan mutu data dan membuat pemeriksaan otomatis yang bisa dibuktikan.

## Konsep dan keputusan engineering

### 1. Dimensi data quality

Completeness: data wajib tersedia; validity: sesuai format/rentang; uniqueness: identitas tidak berulang; consistency: data lintas sumber tidak saling bertentangan; timeliness: cukup segar; accuracy: sesuai fakta dunia nyata. Validity tidak menjamin accuracy. Kualitas data harus terkait keputusan yang akan dibuat, bukan sekadar persen field terisi.

### 2. Schema versus business validation

Schema memeriksa tipe/struktur; business rule memeriksa semantik, misal received_at tidak jauh di masa depan, panjang pesan aman, label berada dalam enum sah, dan status review sesuai alur. Pisahkan error yang bisa diperbaiki otomatis dari yang butuh human intervention.

### 3. Data profiling dan anomaly detection

Buat summary jumlah null, duplikasi, distribusi kelas, panjang teks, nilai tidak dikenal, dan timestamp outlier. Threshold berubah mengikuti kebutuhan bisnis; contoh reject lebih dari 2% perlu ditinjau, tetapi jangan menganggap angka latihan ini benchmark industri.

### 4. Data leakage dan split

Data test tak boleh memengaruhi training, pemilihan fitur, atau threshold melalui trial yang terus-menerus. Periksa overlap ID, normalized text, dan entity. Lebih kuat lagi gunakan group split per device/tenant serta time-based split sesuai use case. Catat batasan pemeriksaan duplicate sederhana.

### 5. Privasi dan klasifikasi sensitivitas

Minimalkan data yang dikumpulkan, mask PII untuk debugging, batasi akses dataset dan waktu retensi. Anonimisasi semu bisa gagal jika dataset dikombinasikan dengan informasi lain. Data sintetis adalah pilihan aman untuk latihan.

## Studi kasus dalam capstone

EventNote '  ' invalid secara bisnis walau bertipe string. Timestamp di masa depan bisa valid secara format ISO namun tidak semestinya diterima. Train/test dengan teks identik tapi ejaan berbeda juga bisa membocorkan informasi semantik.

## Kontrak kualitas dan keamanan

- Minimal lima aturan tervalidasi otomatis dan punya pesan kesalahan terkontrol.
- Tersedia ringkasan data quality dengan jumlah dan formula metrik.
- Data test tidak tercampur dalam training; kebocoran eksplisit ditolak.
- Tidak ada PII/kredensial dalam dataset dan laporan.

**Inti pembelajaran:** kompetensi dinilai dari alasan dan bukti keputusan, bukan hafalan istilah. Materi ini merupakan penjelasan praktis untuk belajar mandiri, bukan salinan KUK resmi.

## Referensi primer

- https://docs.pydantic.dev/latest/concepts/validators/
- https://scikit-learn.org/stable/common_pitfalls.html
- https://www.nist.gov/itl/ai-risk-management-framework

[Mulai praktikum](lab-guide.md) · [Latihan](exercises.md)
