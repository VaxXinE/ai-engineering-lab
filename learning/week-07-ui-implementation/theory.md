# Teori — Implementasi UI Dashboard AI

**Hasil belajar:** Menerapkan wireframe Week 06 menjadi frontend yang responsif, aksesibel, dan aman menghadapi hasil AI yang tidak pasti.

## 1. Component architecture

Pisahkan container data dan presentational components. Page Inbox memuat filter dan data, InquiryDetail memuat informasi yang dapat ditinjau, ReviewAction memuat interaksi accept/override. Gunakan TypeScript discriminated union agar state loading, success, empty, dan error tidak tercampur. Komponen reusable yang berlebihan juga meningkatkan kompleksitas; abstraksikan ketika ada alasan jelas.

## 2. Reliable asynchronous UI

HTTP request dapat gagal, timeout, berulang, atau datang tidak berurutan. Tampilkan progress, tangani abort saat component unmount, batasi retry, dan hindari double submit. Pastikan tombol submit disabled saat operasi berlangsung, tetapi jangan menyandarkan pencegahan duplikasi hanya ke frontend: backend harus idempotent sesuai kontrak.

## 3. Aksesibilitas dan UX

Semantic HTML untuk tabel, form label, tombol, dialog, dan error event_note. Focus state dan keyboard warning wajib. Hindari penggunaan warna sebagai satu-satunya penanda status; gunakan teks seperti 'Perlu ditinjau' dan 'AI tidak tersedia'. Status perlu dapat dipahami screen reader via peringatan yang tepat.

## 4. Uncertain AI output

Jangan tampilkan relative_score sebagai 'tingkat keyakinan 99%'. Display label, model version dan status review secara terpisah. Jika model abstain atau output tidak valid, UI harus meminta pilihan manual daripada diam-diam memberi kategori otomatis. Menampilkan sumber/aspek data perlu memperhatikan privasi.

## 5. Frontend security boundaries

Escaping UI dari React membantu mencegah injection teks, tetapi bahaya masih ada bila menggunakan raw HTML. Jangan menyimpan API key rahasia di kode client, jangan percaya role yang dikirim browser, jangan bocorkan data antar-tenant lewat cache atau URL. Auth dan object-level authorization wajib enforced oleh backend.

## Skenario rekayasa perangkat lunak

Untuk meter reading yang masuk dengan label 'warning', operator melihat prediksi lalu memilih 'normal'. UI menampilkan konfirmasi, menyimpan action, serta mengembalikan hasil audit. Request gagal tidak menghilangkan perubahan yang belum tersimpan.

## Prinsip dan acceptance criteria

- Semua state idle/loading/empty/success/error dapat direproduksi.
- Label AI dan keputusan manusia ditampilkan berbeda.
- Aksi double-submit tertahan di UI dan direncanakan juga dicegah di server.
- Komponen kritis dapat digunakan dengan keyboard.

## Dokumentasi primer untuk pendalaman

- https://react.dev/learn
- https://www.w3.org/WAI/WCAG22/quickref/
- https://owasp.org/www-project-top-ten/

Penjelasan ini mengaitkan materi praktik dengan unit yang dipublikasikan LSP. Ini bukan reproduksi KUK resmi dan tidak menentukan hasil asesmen.

[Praktikum](lab-guide.md)