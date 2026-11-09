# Hands-on — Software Architecture for AI-Enabled Applications

**Status:** panduan siap; langkah belum dieksekusi. Implementasi, metrik, dan bukti ditulis setelah praktikum.

## Target

Merancang batas komponen, contract API, alur data, failure handling dan desain yang tetap fleksibel saat model AI berubah.

## Skenario

Jika AI inference timeout, simpan inquiry lebih dahulu, catat status 'pending_manual_review', jangan mengulang submit sampai menciptakan dua inquiry. Agent tetap dapat bekerja.

## Langkah implementasi

1. Tuliskan konteks sistem: actor, frontend, backend, storage, inference, observability dan sistem eksternal.

2. Gambar component/container diagram; tandai trust boundaries dan data flow PII.

3. Buat sequence diagram untuk create inquiry, run inference, review, dan timeout fallback.

4. Definisikan kontrak POST /inquiries serta endpoint review (request, response, validation, errors).

5. Pisahkan inference adapter dari domain handler; jelaskan opsi sync versus background queue melalui ADR.

6. Lakukan threat-model ringan untuk injection, IDOR, provider outage, dan data exfiltration; tentukan tests.

## Acceptance criteria

- [ ] Diagram konsisten dengan requirement dan relasi data.
- [ ] Semua endpoint kritis memiliki kontrak validasi dan error codes.
- [ ] AI inference failure tidak menghilangkan data yang sudah diterima.
- [ ] Authorization dan secret handling ditempatkan pada trust boundary yang benar.

## Rencana verifikasi

1. Buat skenario bukti untuk: Diagram konsisten dengan requirement dan relasi data.
2. Buat skenario bukti untuk: Semua endpoint kritis memiliki kontrak validasi dan error codes.
3. Buat skenario bukti untuk: AI inference failure tidak menghilangkan data yang sudah diterima.
4. Buat skenario bukti untuk: Authorization dan secret handling ditempatkan pada trust boundary yang benar.

## Dokumentasi hasil

- Catat perintah, dependency/runtime, input sintetis, output aktual, dan edge case yang diuji.
- Catat source code atau desain beserta commit/PR.
- Tuliskan threat dan asumsi tersisa. Jangan menyatakan 'passed' sebelum menjalankan test.
- Kaitkan hasil dengan [evidence matrix](../../certification/evidence-matrix.md).

[Latihan](exercises.md) · [Simulasi](assessment.md)