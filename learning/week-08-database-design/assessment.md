# Simulasi Asesmen — Database Entities & Relational Integrity

Ini pertanyaan latihan nonresmi, **bukan bank soal BNSP**.

1. Apa beda PK dan unique index?

2. Mengapa FK menjaga integritas?

3. Apa masalah update anomaly?

4. Apa itu transaction isolation?

5. Bagaimana menghindari IDOR pada endpoint by-id?

6. Mengapa audit trail append-only berguna?

7. Kapan indeks memperlambat write?

8. Apa manfaat migrations pada proyek tim?

## Demonstrasi yang harus mampu dilakukan

- [ ] Setiap prediction memiliki model_version dan meter_reading_id yang valid.
- [ ] Foreign key menolak orphan record; rollback transaksi menjaga konsistensi.
- [ ] Akses tenant A tidak dapat membaca atau mengubah record tenant B.
- [ ] Re-running migration dan duplicate event ditangani sesuai rencana.

## Pengukuran kesiapan

1. **Konsep:** jelaskan tiap keputusan teknis dan trade-off.
2. **Praktik:** tunjukkan artefak yang dibuat sendiri beserta cara menjalankannya.
3. **Validasi:** tunjukkan hasil test aktual dan penanganan edge case.
4. **Risk:** jelaskan security, privacy, failure dan batasan pendekatan.
5. **Evidence:** dokumentasikan referensi commit/PR, diagram, logs, dan test.

Status 'kompeten' tetap ditetapkan melalui asesmen resmi LSP berlisensi, bukan penilaian diri.

[Portfolio](../../certification/evidence-matrix.md)