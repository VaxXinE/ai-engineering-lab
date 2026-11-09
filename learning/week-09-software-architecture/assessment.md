# Simulasi Asesmen — Software Architecture for AI-Enabled Applications

Ini pertanyaan latihan nonresmi, **bukan bank soal BNSP**.

1. Apa tanggung jawab domain service?

2. Apa perbedaan modular monolith dan microservices?

3. Apa itu trust boundary?

4. Bagaimana API menjaga provider independence?

5. Bagaimana memastikan PII tidak muncul di logs?

6. Kapan queue lebih baik dibanding synchronous inference?

7. Apa contoh graceful degradation?

8. Apa kegunaan ADR dan sequence diagram?

## Demonstrasi yang harus mampu dilakukan

- [ ] Diagram konsisten dengan requirement dan relasi data.
- [ ] Semua endpoint kritis memiliki kontrak validasi dan error codes.
- [ ] AI inference failure tidak menghilangkan data yang sudah diterima.
- [ ] Authorization dan secret handling ditempatkan pada trust boundary yang benar.

## Pengukuran kesiapan

1. **Konsep:** jelaskan tiap keputusan teknis dan trade-off.
2. **Praktik:** tunjukkan artefak yang dibuat sendiri beserta cara menjalankannya.
3. **Validasi:** tunjukkan hasil test aktual dan penanganan edge case.
4. **Risk:** jelaskan security, privacy, failure dan batasan pendekatan.
5. **Evidence:** dokumentasikan referensi commit/PR, diagram, logs, dan test.

Status 'kompeten' tetap ditetapkan melalui asesmen resmi LSP berlisensi, bukan penilaian diri.

[Portfolio](../../certification/evidence-matrix.md)