# Deep Dive — UX AI: mengurangi kesalahan keputusan manusia, bukan sekadar membuat dashboard rapi

**Target:** setelah modul, lo dapat mempertahankan pilihan desain melalui contoh dan kontra-contoh, bukan sekadar mengingat istilah.

## Learning outcomes

1. Memetakan task dan error flow dari inquiry hingga keputusan agent.
2. Mendesain human-in-the-loop agar prediksi dapat dikoreksi dan diaudit.
3. Menjelaskan tampilan ketidakpastian tanpa klaim confidence palsu.
4. Menyusun usability test berbasis tugas dan accessibility acceptance criteria.

## Pembahasan konsep dan trade-off

### 1. Mulai dari pekerjaan pengguna

Agent ingin memproses pesan cepat tetapi tak ingin salah route. Supervisor ingin tahu mana pesan salah dan apakah koreksi diikuti. Developer butuh observability, bukan menambahkan segala grafik pada layar agent. Buat task decomposition: buka inbox → pahami konteks → lihat usulan AI → terima/tolak → konfirmasi perubahan → lanjut. Aksi paling penting harus jelas, sedangkan model version dan confidence teknis dapat masuk detail yang dapat dibuka (progressive disclosure).

### 2. AI output dan ketidakpastian

Label 'support' dari classifier adalah saran, bukan fakta. Tampilkan sumbernya seperti 'Prediksi otomatis' serta status 'Belum ditinjau'. Jika abstain, gunakan 'Perlu klasifikasi manual', bukan 'Tidak ada masalah'. Hindari progress bar 98% karena relative_score bisa tidak terkalibrasi. Jika organisasi memakai confidence empiris, jelaskan metrik kalibrasi dan threshold decision yang didasarkan validasi.

### 3. Human review sebagai control

Human-in-the-loop efektif jika reviewer punya konteks dan waktu cukup. Jangan merancang tombol override tersembunyi atau hanya dapat diakses supervisor jika agen punya kewajiban mengecek prediksi. Saat override, catat label awal, label baru, alasan, actor, timestamp dan model_version; izin akses ditentukan server. Jika dua agen mengubah record bersamaan, berikan conflict resolution UX.

### 4. UX states dan loss prevention

Loading, empty, error, unauthorized, stale data, konflik edit, dan network offline perlu desain. Menghilangkan draft ketika HTTP 500 meningkatkan biaya manusia. Tampilkan pesan error yang menolong tanpa membocorkan detail server, dan sediakan retry dengan idempotency key. Accessibility mencakup keyboard, focus management, label, status text, dan contrast; tidak cukup 'warna merah artinya error'.

### 5. Uji usability yang observable

Definisikan task test: menemukan inquiry tidak terbaca, memperbaiki label salah, memulihkan pekerjaan setelah AI timeout. Catat success/assistance/error count, bukan hanya 'UI terasa nyaman'. Empat partisipan latihan tidak membuktikan general usability; catat keterbatasan sampel. Uji screen reader dengan alat nyata ketika implementasi tersedia.

## Aplikasi dalam AI Customer Intelligence

Pikirkan perubahan berikut: traffic 10 kali lebih tinggi, pelanggan memakai dua tenant, pengguna dapat memasukkan teks tidak tepercaya, dan AI service suatu saat mati. Desain mana yang tetap aman? Apa yang mesti diubah? Tuliskan konsekuensi pada kode, data, UX, keamanan, dan monitoring.

## Bacaan primer

- https://www.w3.org/WAI/WCAG22/quickref/
- https://www.nngroup.com/articles/ten-usability-heuristics/
- https://www.nist.gov/itl/ai-risk-management-framework

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md)
