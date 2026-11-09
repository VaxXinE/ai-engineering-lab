# Deep Dive — Mengubah UX menjadi frontend state machine yang tepercaya

**Target:** setelah modul, lo dapat mempertahankan pilihan desain melalui contoh dan kontra-contoh, bukan sekadar mengingat istilah.

## Learning outcomes

1. Mendesain state loading/success/empty/error dengan discriminated unions.
2. Menangani submit, stale request, dan kesalahan AI tanpa kehilangan draft.
3. Menguji aksesibilitas keyboard dan kondisi abnormal.
4. Menjelaskan mengapa frontend tidak boleh menjadi satu-satunya otorisasi.

## Pembahasan konsep dan trade-off

### 1. Komponen berdasarkan tanggung jawab

Pecah layar menjadi InquiryList, InquiryDetail, PredictionBadge, ReviewForm, dan ErrorNotice. Hindari satu component yang memiliki fetching, transformasi, business logic, dan styling sekaligus. React hooks perlu dependency yang benar agar tidak memakai stale state; api client dan domain types berada pada modul terpisah. Tidak semua state butuh global store.

### 2. Representasi asynchronous state

Boolean isLoading + error + data dapat memunculkan kombinasi mustahil (misal loading true tetapi data error). Discriminated union menjamin state eksklusif dengan union TypeScript: idle, loading, success(data), error(event_note). Ini membantu rendering dan pengujian. Untuk optimistic update, simpan snapshot sebelum request dan rollback jika API menolak; hindari menyembunyikan konflik.

### 3. Request race, idempotency dan cancellation

Jika user memilih filter A lalu B cepat, response A bisa datang belakangan dan menimpa B. Gunakan AbortController atau request sequence guard dan cache keys yang memasukkan tenant/filter. Disabled submit mengurangi klik ganda tetapi network retry maupun double tab tetap memerlukan server-side idempotency key.

### 4. Rendering aman dan data sensitif

React secara default meng-escape text nodes, tetapi raw HTML injection tetap berbahaya. Jangan memasukkan secret provider ke Next.js public env atau client bundle. Authorization perlu ditegakkan di backend untuk semua read/update by ID. UI route guard hanya memperbaiki pengalaman, bukan keamanan.

### 5. AI confidence dan human review di UI

Prediksi perlu status, label, model_version, action history. Relative score pada Week 01 bukan probabilitas yang dapat dipahami user; jika menampilkan angka, beri konteks dan hindari angka palsu. Tombol override perlu reason dan submit confirmation; error server harus menjaga draft. Review by user hanya berhasil jika API mengonfirmasi.

## Aplikasi dalam AI Smart Energy Monitoring

Pikirkan perubahan berikut: traffic 10 kali lebih tinggi, perangkat memakai dua tenant, pengguna dapat memasukkan teks tidak tepercaya, dan AI service suatu saat mati. Desain mana yang tetap aman? Apa yang mesti diubah? Tuliskan konsekuensi pada kode, data, UX, keamanan, dan monitoring.

## Bacaan primer

- https://react.dev/learn
- https://www.typescriptlang.org/docs/handbook/2/narrowing.html
- https://www.w3.org/WAI/WCAG22/quickref/

[Worked examples](worked-examples.md) · [Knowledge check](knowledge-check.md)
