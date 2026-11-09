# Teori — Software Architecture for AI-Enabled Applications

**Hasil belajar:** Merancang batas komponen, contract API, alur data, failure handling dan desain yang tetap fleksibel saat model AI berubah.

## 1. Modular monolith as baseline

Arsitektur tidak selalu harus microservices. Modular monolith bisa cukup untuk lab dan MVP: pisahkan API endpoints, domain service, repository, dan inference adapter. Kurangi distributed failure dan kompleksitas deployment; tetap dokumentasikan kriteria pemisahan service jika load atau ownership berkembang.

## 2. Contracts and separation of concerns

Frontend mengenali REST/JSON contract, backend mengenali domain service, inference adapter mengenali model input/output. Jangan menyisipkan HTTP provider calls ke domain business logic. Dengan interface infer(text)->Prediction, model lokal dan hosted provider dapat berganti tanpa merombak API.

## 3. Trust boundaries dan data flow

Klasifikasi AI dan input pengguna sama-sama tidak tepercaya. Sebelum model: auth, object permission, validation dan redaction. Sesudah model: output schema validation, allowed labels, bounded score range, fallback. Diagram harus menunjukkan jalur secret/config dan privacy-safe logs.

## 4. Failure design

Rancang graceful degradation: message tetap tersimpan ketika inference gagal, lalu status pending_review atau pending_retry. Pemanggilan synchronous lebih sederhana tetapi menambah latency; async worker perlu queue, retry dedup dan idempotency. Pilih berdasarkan SLO nyata.

## 5. Architecture documentation

Gunakan C4 context/container/component atau diagram lain secukupnya, plus sequence diagram untuk alur review dan failure. Diagram yang berbeda harus konsisten dengan kode; beri label Planned/Implemented/Verified. ADR melacak trade-off, bukan daftar tools saja.

## Skenario rekayasa perangkat lunak

Jika AI inference timeout, simpan inquiry lebih dahulu, catat status 'pending_manual_review', jangan mengulang submit sampai menciptakan dua inquiry. Agent tetap dapat bekerja.

## Prinsip dan acceptance criteria

- Diagram konsisten dengan requirement dan relasi data.
- Semua endpoint kritis memiliki kontrak validasi dan error codes.
- AI inference failure tidak menghilangkan data yang sudah diterima.
- Authorization dan secret handling ditempatkan pada trust boundary yang benar.

## Dokumentasi primer untuk pendalaman

- https://c4model.com/
- https://fastapi.tiangolo.com/tutorial/
- https://owasp.org/www-project-api-security/

Penjelasan ini mengaitkan materi praktik dengan unit yang dipublikasikan LSP. Ini bukan reproduksi KUK resmi dan tidak menentukan hasil asesmen.

[Praktikum](lab-guide.md)