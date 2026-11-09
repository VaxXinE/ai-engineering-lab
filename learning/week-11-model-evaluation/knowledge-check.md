# Retrieval Quiz — Eksperimen AI yang menolak angka bagus tanpa bukti generalisasi

**Petunjuk:** jawab dari ingatan, bukan sekadar mencari keyword di dokumen. Pembahasan berada setelah pertanyaan agar bisa membandingkan reasoning.

## Pertanyaan

1. Kenapa memakai train/validation/test?
2. 95 fault dari 100, selalu memprediksi fault: accuracy?
3. Macro F1 memberi bobot berdasarkan sample count?
4. Kenapa softmax score belum tentu confidence?
5. Bolehkah membuka file joblib random dari internet?
6. Apa isi model card minimum?

## Pembahasan

**1.** Memisahkan fitting, tuning, dan final evaluation agar hasil tidak bias.

**2.** 95%, tetapi dua kelas minoritas recall-nya nol.

**3.** Tidak; setiap kelas dibobot sama, berbeda weighted F1.

**4.** Model dapat miscalibrated; perlu empirical validation dan calibration.

**5.** Tidak aman: format pickle-based dapat mengeksekusi kode saat deserialize.

**6.** Intended use, data/split, metrics, version/provenance, limitations, risks.

## Koreksi aktif

Tandai jawaban yang keliru dan tulis satu contoh baru yang bisa membedakan konsep salah dengan konsep benar. Jika semua soal benar tetapi tidak mampu menyelesaikan variasi baru, statusnya belum dikuasai.

## Review bertahap

- Hari 0: semua pertanyaan.
- Hari +1: ulangi topik sulit tanpa buku.
- Hari +7: campur dengan modul sebelumnya.
- Hari +21: teach-back dan praktik pada skenario capstone baru.

[Teori mendalam](deep-dive.md)
