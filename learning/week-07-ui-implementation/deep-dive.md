# Deep Dive — Mengubah UX menjadi frontend state machine yang tepercaya

**Target:** setelah modul, lo dapat mempertahankan pilihan desain melalui contoh dan kontra-contoh, bukan sekadar mengingat istilah.

## Learning outcomes

1. Mendesain state loading/success/empty/error dengan discriminated unions.
2. Menangani submit, stale request, dan kesalahan AI tanpa kehilangan draft.
3. Menguji aksesibilitas keyboard dan kondisi abnormal.
4. Menjelaskan mengapa frontend tidak boleh menjadi satu-satunya otorisasi.

## Pembahasan konsep dan trade-off

### 1. Komponen berdasarkan tanggung jawab

Frontend membagi `EnergyOverview`, `MeterTrendChart`, `AnomalyTable`, `ReviewForm`, dan `StatusNotice`. Data fetching terpisah dari rendering; type safety membantu mencegah kecampuran measurement, scored candidate, dan human review. Gunakan caching per authorized site/meter/time-range dan component boundaries sesuai kebutuhan, bukan abstraction berlebihan.

### 2. Representasi asynchronous state

Gunakan TypeScript discriminated union (`idle`, `loading`, `success`, `empty`, `error`) sehingga state saling eksklusif. `success` dengan array kosong berbeda secara semantik dari `scoring_unavailable`. Review form yang gagal harus mempertahankan draft; invalid model output tidak ditampilkan sebagai angka valid.

### 3. Request race, idempotency dan cancellation

Saat filter berubah dari SITE-A ke SITE-B, request lama bisa selesai belakangan; AbortController atau sequence keys mencegah stale results. Cache harus terpartisi berdasarkan site yang terotorisasi, meter, dan window. Disabled submit bukan pengganti server-side idempotency/optimistic version checks.

### 4. Rendering aman dan data sensitif

React secara default meng-escape text nodes, tetapi raw HTML injection tetap berbahaya. Jangan memasukkan secret provider ke Next.js public env atau client bundle. Authorization perlu ditegakkan di backend untuk semua read/update by ID. UI route guard hanya memperbaiki pengalaman, bukan keamanan.

### 5. AI confidence dan human review di UI

Tampilkan `anomaly_score` sebagai skor/ranking model dan model_version, bukan 93% 'alat rusak'. Human decision disimpan terpisah dari anomaly flag. Jika AI belum memberi skor, readings tetap ada; UI menampilkan `pending_scoring` atau `scoring_unavailable` alih-alih label 'normal' palsu.

## Aplikasi dalam AI Smart Energy Monitoring

Pikirkan perubahan berikut: traffic 10 kali lebih tinggi, perangkat memakai dua tenant, pengguna dapat memasukkan teks tidak tepercaya, dan AI service suatu saat mati. Desain mana yang tetap aman? Apa yang mesti diubah? Tuliskan konsekuensi pada kode, data, UX, keamanan, dan monitoring.

## Bacaan primer

- https://react.dev/learn
- https://www.typescriptlang.org/docs/handbook/2/narrowing.html
- https://www.w3.org/WAI/WCAG22/quickref/

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md)
