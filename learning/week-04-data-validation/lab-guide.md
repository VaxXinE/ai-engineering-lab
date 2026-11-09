# Praktikum — Week 04: Data Quality, Validation & Leakage Prevention

**Status:** rancangan latihan. Belum ada klaim bahwa langkah di bawah berhasil dijalankan.

## Konteks

EventNote '  ' invalid secara bisnis walau bertipe string. Timestamp di masa depan bisa valid secara format ISO namun tidak semestinya diterima. Train/test dengan teks identik tapi ejaan berbeda juga bisa membocorkan informasi semantik.

**Prasyarat:** Modul 3; Python, skema data, data ingestion report.  
**Dataset:** data sintetis dari capstone; jangan memakai data perusahaan atau kredensial sungguhan.

## Langkah kerja

1. Susun tabel aturan validasi untuk ID, timestamp, channel, event_note, source, dan label (bila ada).

2. Gunakan schema validator (Pydantic atau standard-library validator) terpisah dari parser ingestion.

3. Buat fixture sintetis berisi valid row, blank event_note, unsupported source, duplicate ID, future timestamp, dan pesan berlebihan.

4. Hitung quality metrics sebelum dan sesudah validasi, disertai denominator dan definisi metrik.

5. Tambahkan pemeriksaan train/test exact overlap serta dokumentasikan keterbatasan semantic overlap.

6. Tulis rekomendasi quality gate untuk menolak dataset sebelum model training.

## Test plan minimal

1. Null dan whitespace-only string ditolak.
2. Unsupported enum/channel dan timestamp out-of-policy ditolak.
3. Input terlalu panjang ditolak dengan sebab yang aman.
4. Replikasi data train ke test memicu leakage guard.

## Acceptance criteria

- [ ] Minimal lima aturan tervalidasi otomatis dan punya pesan kesalahan terkontrol.
- [ ] Tersedia ringkasan data quality dengan jumlah dan formula metrik.
- [ ] Data test tidak tercampur dalam training; kebocoran eksplisit ditolak.
- [ ] Tidak ada PII/kredensial dalam dataset dan laporan.

## Bukti yang disimpan setelah praktik

1. Source code / artefak desain serta alasan keputusan yang dibuat sendiri.
2. Cara menjalankan atau mereproduksi hasil (versi environment dan perintah aktual).
3. Test report: perintah, hasil sesungguhnya, sampel negatif dan edge cases.
4. Analisis risiko keamanan, privasi, performa, serta keterbatasan yang belum ditangani.
5. Link PR/commit ke [matriks bukti](../../certification/evidence-matrix.md).

## Syarat selesai

**Belum selesai** hanya dengan membaca dokumen ini. Tandai selesai setelah implementasi diverifikasi dan evidence tersimpan; uji kompetensi BNSP tetap dilakukan oleh LSP yang berwenang.

[Latihan tambahan](exercises.md) · [Simulasi asesmen](assessment.md)
