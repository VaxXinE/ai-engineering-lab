# Praktikum Terstruktur — Relasi site, meter, reading, scoring, dan review

**Status:** tugas **direncanakan**; implementasi Week 03–12 belum dijalankan. Semua input, site, meter dan timeseries adalah sintetis.

## Problem dan konteks profesional

Pembacaan dari beberapa site memakai ID meter yang mungkin sama; inference dapat dijalankan ulang dengan model baru dan keputusan review harus dapat ditelusuri.

**Single source of truth:** [kontrak domain](../../docs/architecture/energy-data-contract.md) · [threat model](../../docs/architecture/threat-model.md). Jangan mencampur kontrak klasifikasi log teks Week 01 dengan data anomaly scoring numerik Week 11–12.

## Langkah yang akan diimplementasikan saat sesi praktik

1. Rancang ERD Site, Meter, MeterReading, IngestionBatch, ModelVersion, AnomalyEvent, ReviewEvent, dan ReviewerMembership.

2. Definisikan FK (site_id,meter_id) pada MeterReading ke Meter, UNIQUE(site_id,meter_id,source_event_id) dan aturan konflik payload.

3. Simpan measured_at UTC, interval_minutes, energy_kwh numeric >=0 serta metadata versi input. Jangan menimpa bacaan untuk 'memperbaiki' hasil AI.

4. AnomalyEvent menyimpan score/version/time, dan ReviewEvent append-only dengan actor, decision, reason, timestamp.

5. Review optimistic locking memakai version expected, update atomik serta conflict response bila affected rows=0.

6. Uji cross-site IDOR untuk GET dan POST review, duplicate ingest, FK orphan dan rollback transaction.

## Acceptance criteria (belum dicentang)

- [ ] Meter SITE-A/MTR-001 dan SITE-B/MTR-001 tidak tercampur.
- [ ] AnomalyEvent mengacu reading dan model_version yang valid.
- [ ] Audit review tidak menghapus prediksi lama.
- [ ] IDOR ditolak berdasarkan authenticated site membership, bukan keacakan ID.

## Evidence yang harus dibuat

ERD, migration SQL, index design, transaction/integrity tests, authorization test matrix.

Saat praktik: catat input sintetis, expected behavior, actual output, command+versi runtime, error/negative tests, keamanan, dan link commit. Jangan mengarang skor model, latency, atau status passed.

## Pertanyaan transfer

Apa yang terjadi jika sebuah site mengirim source_event_id sama dengan site lain?

**Definition of done:** seluruh acceptance criteria diverifikasi dengan artefak sendiri, bukan sekadar dokumentasi ini; status BNSP tetap memerlukan asesmen resmi LSP.

[Latihan](exercises.md) · [Knowledge check](knowledge-check.md) · [Evidence matrix](../../certification/evidence-matrix.md)
