# Week 01 — Verifikasi Setelah Migrasi Use Case

**Diperbarui:** 9 November 2026

## Perubahan besar

Model dan aturan pengolahan teks kini memakai `normal`, `warning`, `fault` untuk **synthetic energy-device event notes**, bukan kategori domain lain.

- Training examples: 54 sintetis, 18 per kelas.
- Held-out evaluation examples: 18 sintetis, 6 per kelas.
- API/model eksternal: tidak digunakan.
- Tes unit dan evaluasi hasil: **jalankan ulang setelah perubahan data/label**.
- Skor accuracy/F1 sebelumnya **tidak boleh dipakai sebagai hasil benchmark untuk dataset baru**.

## Perintah verifikasi

```bash
cd learning/week-01-ai-fundamentals
python -m unittest discover -s tests -v
python -m week01 evaluate
python -m week01 predict --text "meter melaporkan tegangan stabil normal"
python -m compileall -q week01
```

**Status:** pendokumentasian disiapkan; hasil aktual untuk dataset baru perlu direkam dari CI atau local run yang selesai. Setelah itu masukkan accuracy/F1, confusion matrix dan test outcomes yang benar-benar diamati. Jangan menyebutnya siap produksi.

### Batasan

- Text classifier ini bukan model mendeteksi anomali numerik.
- 72 contoh sintetis tidak mencerminkan situasi lapangan.
- Tidak ada aksi otomatis yang mengendalikan perangkat listrik.
- Relative_score tidak terkalibrasi.
