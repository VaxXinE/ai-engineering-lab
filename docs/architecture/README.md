# Architecture & Security References — AI Smart Energy Monitoring

Kontrak dan diagram di bawah adalah **rancangan untuk pembelajaran**, belum diterapkan/deploy.

1. [Canonical Energy Data & API Contract](energy-data-contract.md) — satuan kWh, interval 15 menit UTC, identity, API, model score dan review.
2. [Threat Model](threat-model.md) — upload risks, cross-site IDOR, AI output, model provenance, rate limits dan failure.
3. [Cross-module Quality Gates](energy-learning-gates.md) — acceptance/failure cases 16 modul.
4. [Capstone Architecture](../../projects/ai-energy-intelligence/docs/architecture.md).

Hindari penulisan schema/endpoint baru yang bertentangan dengan kontrak canonical. Semua real implementation, test metrics dan deployment harus diverifikasi terpisah.
