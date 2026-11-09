# Modul 01 — AI Engineering Fundamentals

**Studi kasus domain energi:** [Applied Energy Case — worked reasoning, tantangan, negative tests](energy-case-study.md). Gunakan [canonical domain contract](../../docs/architecture/energy-data-contract.md); semua latihan domain ini masih **planned** sampai ada hasil implementasi teruji.

> **Materi v2:** [Deep Dive](deep-dive.md) → [Worked Examples](worked-examples.md) → [Knowledge Check](knowledge-check.md) → [Learning Contract](study-contract.md) → [Lab Guide](lab-guide.md).

**Domain praktik:** AI Smart Energy Monitoring (catatan kejadian perangkat sintetis)  
**Status:** Kode latihan tersedia; progres belajar peserta belum dinilai.  
**Estimasi:** 8–10 jam • **Kebutuhan:** Python 3.11+

## Tujuan

Pelajari AI vs ML vs DL vs GenAI, training vs inference, evaluasi, data leakage, dan keterbatasan confidence menggunakan **text classifier untuk catatan perangkat energi**. Ini aplikasi ML kecil yang tidak memerlukan API key atau instalasi package eksternal.

Kategori:
- `normal` — pembacaan stabil
- `warning` — perubahan penggunaan/tegangan yang perlu pemeriksaan
- `fault` — perangkat/sensor atau telemetri bermasalah
- `abstain` — input tak dikenal, dialihkan ke peninjauan manual

Bukan model yang mampu menganalisis keamanan instalasi listrik. Kategori diperoleh dari contoh berlabel sintetis untuk demonstrasi algoritma.

## Quick start

```bash
cd learning/week-01-ai-fundamentals
python -m week01 predict --text "meter melaporkan tegangan stabil normal"
python -m week01 predict --text "konsumsi energi meningkat mendekati ambang"
python -m week01 predict --text "sensor offline tidak mengirim data"
python -m week01 evaluate
python -m unittest discover -s tests -v
```

Training: **54** catatan sintetis, evaluation: **18** catatan sintetis. `relative_score` bukan probabilitas terkalibrasi. Semua kode memakai Python standard library.

## Navigasi

- [Teori singkat](theory.md)
- [Deep Dive](deep-dive.md)
- [Worked Examples](worked-examples.md)
- [Knowledge Check](knowledge-check.md)
- [Use-case dan kontrak](use-case-spec.md)
- [Panduan praktikum](lab-guide.md)
- [Latihan](exercises.md)
- [Simulasi asesmen](assessment.md)
- [Hasil dan batas verifikasi](results/verification.md)

## Kriteria penyelesaian peserta

- [ ] Bisa menjelaskan perbedaan rule-based dan model yang dilatih.
- [ ] Menjalankan tiga contoh inference dan evaluasi sendiri.
- [ ] Memahami precision/recall/F1 serta confusion matrix kelas.
- [ ] Mengidentifikasi kasus gagal atau abstain dan menjelaskan human fallback.
- [ ] Menghasilkan catatan latihan/commit yang dapat diverifikasi.

**Terkait capstone:** [AI Smart Energy Monitoring](../../projects/ai-energy-intelligence/README.md). Modul 11–12 nanti membahas **numerical energy anomaly detection**, bukan sekadar classifier teks modul ini.
