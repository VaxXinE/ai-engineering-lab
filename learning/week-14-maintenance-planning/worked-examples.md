# Worked Examples — Mengukur kesehatan layanan dan AI secara terpisah

Semua langkah berikut adalah **contoh pembelajaran**, bukan laporan pelaksanaan. Uji ulang dengan alat yang tersedia saat fase praktik.

## Contoh 1: Error budget contoh 99.5%

**Problem:** Tujuan reliability internal: 99.5% request valid sukses selama periode 100.000 request.

1. Target sukses 0.995 * 100000 = 99500 request.

2. Error budget 0.005 * 100000 = 500 failed valid requests.

3. Jika observasi 650 failed requests, target SLO tidak tercapai, kecuali ada definisi exclusion yang memang sudah didokumentasikan.

4. Keputusan: prioritaskan stabilitas dan root cause, bukan langsung menyimpulkan perlu menambah kapasitas.

**Common failure:** SLO numerator/denominator tanpa definisi 'valid requests' dapat dimanipulasi, terutama saat sengaja mengecualikan error yang tidak nyaman.

**Why-question:** kenapa langkah sebelumnya mencegah risiko tersebut dan test apa yang membuktikannya?

## Contoh 2: Quality degradation tanpa downtime

**Problem:** API tetap 200, tetapi support override agent naik dari 5% ke 20% setelah model update.

1. Pastikan perbedaan jumlah sampel dan label policy tidak berubah; bandingkan per tenant/channel/language.

2. Ambil sampel review terverifikasi dan hitung per-class precision/recall, bukan menganggap override rate = error rate.

3. Jika kenaikan terkonfirmasi dan konsekuensinya tinggi, nonaktifkan auto-route atau rollback model sesuai kriteria.

4. Jalankan regression evaluation pada data waktu terbaru yang dibekukan; audit model version dan log keputusan.

**Common failure:** Melakukan retraining otomatis dari seluruh override tanpa menyaring label noise/abuse dapat memperburuk prediksi.

**Why-question:** kenapa langkah sebelumnya mencegah risiko tersebut dan test apa yang membuktikannya?

## Latihan bertahap

- **Fully worked:** ulas reasoning semua langkah.
- **Faded:** ulang tanpa melihat langkah kedua.
- **Independent:** pindahkan solusi ke studi kasus baru dan buat test plan.
- **Reflection:** catat apa yang belum bisa dijamin dari evidence yang tersedia.

[Latihan mandiri](exercises.md)
