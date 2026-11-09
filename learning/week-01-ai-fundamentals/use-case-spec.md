# Use Case — Synthetic Customer Inquiry Classification

**Tanggal:** 9 November 2026  
**Versi:** 0.1 (proof-of-concept, belum production)

## Masalah dan tujuan

Pesan customer website/live chat perlu dipilah ke sales, support, atau general inquiry. Modul ini mempraktikkan cara mendefinisikan tugas AI dan mengevaluasinya; **belum ada penghematan biaya atau perbaikan KPI yang dibuktikan**.

## Persona
- Agent: memeriksa dan dapat mengoreksi label.
- Sales: menerima prospek yang relevan.
- Developer/QA: menguji data, output, dan risiko.

## Kontrak input/output

- **Input:** pesan sintetis 1–500 karakter dengan kata yang dapat dibaca.
- **Output:** kelas sales/support/general, atau abstain jika tidak satu pun token dikenali.
- **Format:** JSON pada CLI; relative_score bukan confidence terkalibrasi.
- **Storage:** tidak ada penyimpanan pesan yang dimasukkan pada CLI.

## Acceptance criteria

1. File data wajib CSV text,label dengan kategori yang sah.
2. Data kosong, duplikat, invalid, atau berukuran berlebihan ditolak.
3. Model dilatih menggunakan train, dievaluasi dengan test terpisah, overlap terdeteksi.
4. Output evaluasi memuat accuracy, macro F1, precision/recall/F1 per kelas, matrix, abstention.
5. Perbandingan model ML dan rule-based memakai dataset uji yang sama.
6. Unit tests menilai happy path, failure path, dan kasus khusus.

## Quality dan security constraints

- Tidak memerlukan jaringan maupun API key.
- Data seluruhnya sintetis; jangan memasukkan data klien sungguhan.
- Skor hasil adalah performa pada dataset uji kecil, bukan prediksi performa dunia nyata.
- Tidak melakukan proses bisnis otomatis; human review direncanakan di capstone.

## Risiko dan kontrol

| Risiko | Dampak | Kontrol awal |
| --- | --- | --- |
| PII bocor lewat dataset | Pelanggaran privasi | Dataset sintetis |
| Input tidak valid | Training/output rusak | Validasi schema, label, panjang |
| Test leakage | Metrik menyesatkan | Pemisahan file + duplicate check |
| Kata asing tidak dikenali | Salah route | Explicit abstain |
| Relative score dianggap kepastian | Overtrust | Disclaimer output |
| Deploy terlalu dini | Salah keputusan operasional | POC lokal, tidak ada integrasi production |

## Di luar cakupan

Frontend, backend service, authentication, database, cloud deployment, LLM, vector database, fine tuning, serta pengolahan data asli.

Lanjutkan pada [capstone project](../../projects/ai-customer-intelligence/README.md).
