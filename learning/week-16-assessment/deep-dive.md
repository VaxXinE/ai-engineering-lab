# Deep Dive — Mengubah proyek menjadi bukti kompetensi yang dapat diuji

## Outcome terukur

1. Membuat evidence matrix per unit yang dikonfirmasi dari dokumen skema terkini.
2. Membedakan hasil kerja pribadi, hasil tim dan referensi dari pihak ketiga.
3. Merancang demonstrasi yang memuat success dan failure paths.
4. Melakukan gap analysis tanpa mengeklaim lulus asesmen BNSP.

## Pembahasan engineering

### 1. Unit, elemen dan KUK bukan daftar judul semata

Nama skema dan nama unit memberi arah, tetapi asesmen resmi juga menggunakan elemen dan kriteria unjuk kerja dari versi skema yang disetujui LSP. Saat ini LSP AI menampilkan 12 unit Aplikasi dan 6 unit Proses Data; direktori BNSP mencatat 13 unit untuk Aplikasi, sedangkan Kepmenaker 103/2026 telah mencabut 123/2021. Jangan menebak unit ke-13 atau menyamakan kode baru secara otomatis. Minta dokumen skema final ke LSP sebelum membuat mapping resmi.

### 2. Evidence yang relevan dan autentik

Satu repo besar belum otomatis membuktikan kompetensi. Asesor perlu menilai apakah setiap bukti relevan, autentik, cukup dan terkini sesuai prosedur. Simpan artefak seperti test output, ADR, ERD, diagram, code commit, laporan kualitas data, monitoring plan dan incident drill. Jelaskan kontribusi pribadi saat kerja kelompok, dan bedakan contoh pengajar dari tugas peserta.

### 3. Evidence traceability

Untuk setiap unit, catat judul/kode yang diverifikasi, elemen/KUK, artefak, commit SHA, tanggal pengujian, perintah reproduksi dan status. Satu test bisa mendukung beberapa kompetensi hanya bila benar-benar relevan. Hindari screenshot tanpa konteks, klaim '100% secure', hasil model tanpa dataset/split, atau file yang hanya berisi rencana.

### 4. Mock demonstration

Susun demo dari problem statement→dataset synthetic→validasi→storage→UI→classifier→review→failure injection→recovery. Tunjukkan minimal satu error case dan jelaskan dampak/security. Asesor mungkin menggunakan metode berbeda; demo 20 menit di repo ini hanyalah latihan untuk membangun komunikasi, bukan format BNSP yang dijanjikan.

### 5. Administrasi dan privasi

KTP, surat pengalaman kerja, FR.APL.01/02, detail identitas dan credential diserahkan lewat kanal resmi LSP; jangan simpan di GitHub public. Verifikasi syarat pengalaman, sertifikat pelatihan yang mungkin diwajibkan, biaya, jadwal, TUK dan aturan asesmen ulang. Bukti unit overlap tidak otomatis diakui lintas skema.

### 6. Competency gap and feedback loop

Jika unit 'Merawat solusi AI' belum didukung test restore aktual, tandai gap tersebut dan susun praktik. Materi selesai tidak sama dengan kompetensi terverifikasi. Setelah mock assessor memberi feedback, perbaiki artifact, jalankan test ulang dan simpan versioned evidence. Kejujuran pada keterbatasan menunjukkan praktik engineering yang dapat dipertanggungjawabkan.

## Transfer lesson ke dunia kerja

Buat daftar tindakan yang aman dilakukan di environment test dan yang memerlukan izin perubahan produksi. Jelaskan risiko dan keterbatasan serta apa yang harus diverifikasi dengan data nyata. Jangan gunakan materi demo sebagai bukti hasil production.

## Bacaan primer

- https://bnsp.go.id/
- https://lspartificialintelligence.id/penerapan-ai-untuk-aplikasi-perangkat-lunak/
- https://jdih.kemnaker.go.id/peraturan/detail/3020/keputusan-menteri-ketenagakerjaan-nomor-103-tahun-2026

[Contoh lengkap](worked-examples.md) · [Tes pemahaman](knowledge-check.md)
