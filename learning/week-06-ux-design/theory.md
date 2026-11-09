# Teori — Week 06: User Experience for AI-Assisted Workflows

**Tujuan:** Mendesain alur operator dashboard energi yang dapat mengerti, memeriksa, memperbaiki dan menolak rekomendasi AI.

## Konsep dan keputusan engineering

### 1. User journey dan task analysis

Pisahkan kebutuhan operator, supervisor, dan operator teknis. Rancang task dari pesan baru sampai resolved state dengan jumlah langkah rendah tetapi status yang jelas. Catat moment of uncertainty saat AI salah atau tidak tersedia; di sinilah desain memiliki dampak terbesar pada trust.

### 2. Human-in-the-loop

AI tidak boleh menjadi pemutus akhir untuk tindakan konsekuensial tanpa mekanisme review. Operator harus melihat prediksi dan alasan/konteks yang aman, lalu dapat accept/override/abstain. Simpan alasan perubahan dan identitas reviewer secara audit-able.

### 3. Information architecture

Pertahankan navigasi konsisten: Inbox, Detail, Review Queue, History. Bedakan kategori pesan dengan status progres (misalnya normal vs pending). Progressive disclosure menyembunyikan detail teknis sampai dibutuhkan tanpa menyembunyikan tindakan penting.

### 4. Designing uncertainty

Jangan menampilkan relative_score dari model sederhana sebagai probabilitas pasti. Gunakan status 'perlu tinjauan' untuk abstain/low quality input. Berikan feedback ketika prediksi berubah dan informasikan asal prediksi (versi model).

### 5. Accessibility dan failure state

Gunakan hierarki heading, keyboard focus, labels untuk form, error text yang actionable, dan contrast yang memadai. Skeleton/loading bukan pengganti penjelasan status; pada kegagalan API, lindungi draft dan sediakan retry manual dengan kebijakan idempotency.

## Studi kasus dalam capstone

Jika prediksi 'warning' salah dan operator memilih 'normal', tampilkan 'Label diperbarui' plus riwayat audit. Jangan diam-diam menghilangkan prediksi awal: itu merusak ability to evaluate model.

## Kontrak kualitas dan keamanan

- Journey memuat alur sukses, error, dan manual override.
- Prediksi AI dibedakan dari keputusan manusia.
- Wireframe mencakup loading/empty/error state dan aksesibilitas.
- Ada minimal tiga task usability dengan success criteria.

**Inti pembelajaran:** kompetensi dinilai dari alasan dan bukti keputusan, bukan hafalan istilah. Materi ini merupakan penjelasan praktis untuk belajar mandiri, bukan salinan KUK resmi.

## Referensi primer

- https://www.w3.org/WAI/WCAG22/quickref/
- https://www.nngroup.com/articles/ten-usability-heuristics/
- https://www.nist.gov/itl/ai-risk-management-framework

[Mulai praktikum](lab-guide.md) · [Latihan](exercises.md)
