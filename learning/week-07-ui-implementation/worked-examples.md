# Worked Examples — Type-Safe Energy Monitoring UI

## 1. State machine untuk grafik

Dalam TypeScript, jangan mengandalkan beberapa boolean yang bisa saling bertentangan:

```ts
type Reading = { meterId: string; intervalStartUtc: string; energyKwh: number };
type RemoteState =
  | { kind: 'idle' }
  | { kind: 'loading' }
  | { kind: 'success'; readings: Reading[] }
  | { kind: 'empty' }
  | { kind: 'error'; message: string };

function summary(state: RemoteState): string {
  switch (state.kind) {
    case 'idle': return 'Siap';
    case 'loading': return 'Memuat';
    case 'success': return state.readings.length + ' readings';
    case 'empty': return 'Tidak ada pembacaan';
    case 'error': return state.message;
  }
}
```

Saat `success`, data diurutkan berdasarkan timestamp UTC; buat **gap** untuk missing interval, bukan menampilkan `energyKwh=0`.

## 2. Response race saat filter site berubah

1. Operator memilih SITE-A; request A dimulai.
2. Operator beralih ke SITE-B; request B dimulai.
3. B selesai dahulu. UI mengaktifkan hasil SITE-B.
4. A selesai belakangan; AbortController/request version mencegah hasil lama mengganti SITE-B.
5. Server tetap membatasi data dengan auth membership site; cache key mencakup authorized site dan meter.

**Security pitfall:** menyembunyikan filter site di UI tidak mencegah IDOR. API harus memverifikasi hak akses ke site/meter sebelum mengembalikan data.

## 3. Uncertain scores and review

Jika `anomaly_score=0.93`, tampilkan 'skor anomali (ranking model)' **bukan** '93% alat rusak'. Saat timeout, tampilkan `scoring_unavailable` dan data tetap terlihat. Form review mempertahankan pilihan saat 409 atau 5xx.

[Theoretical contract](../../docs/architecture/energy-data-contract.md) · [UX case](../week-06-ux-design/worked-examples.md).
