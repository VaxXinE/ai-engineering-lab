# Worked Examples — Bukti untuk Asesmen Dua Skema

**Ini latihan nonresmi, bukan metode penilaian atau soal resmi BNSP.**

## 1. Mengumpulkan bukti unit AI Integration

**Konteks:** capstone AI Smart Energy Monitoring mempunyai anomaly scoring API dengan input numeric dan output terverifikasi.

1. **Klaim kemampuan:** mampu mengintegrasikan komponen AI secara aman ke aplikasi, termasuk fallback.
2. **Evidence utama:** kontrak API dan code adapter yang telah diimplementasikan; link commit dan penjelasan kontribusi sendiri.
3. **Evidence pengujian:** negative tests NaN/inf score, inference timeout, cross-site IDOR, dan idempotent retry, jika benar-benar telah dieksekusi.
4. **Gap saat ini:** backend capstone belum dibuat, jadi bukti di atas adalah **rencana**, bukan evidence yang telah dimiliki.
5. **Asesmen:** setelah memperoleh unit/elemen/KUK final dari LSP, petakan bukti aktual ke tiap tuntutan. Jangan mengklaim unit selesai berdasarkan dokumen ini.

## 2. Draft presentasi demonstrasi internal

- Menit 0–3: problem dan measurement units (kWh per 15 menit).
- 3–6: synthetic CSV, data dictionary, ingestion/validation dan missing-slot report.
- 6–10: data model, site-scoped API dan dashboard.
- 10–14: baseline IQR vs anomaly model, output score validation, human review.
- 14–18: fault injection scoring timeout dan restore drill (hanya jika sudah diimplementasikan dan diuji).
- 18–20: mapping evidence, trade-offs, security risks dan pekerjaan yang masih belum selesai.

Waktu hanya target latihan pribadi, **bukan aturan BNSP**. Bila demo belum berjalan, sebut status sebenarnya dan gunakan gap register.

[Kontrak domain](../../docs/architecture/energy-data-contract.md) · [Evidence matrix](../../certification/evidence-matrix.md) · [Standards watch](../../docs/standards-watch.md).
