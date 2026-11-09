# Worked Examples — Failure Containment dan Scoring Port

## 1. Score-independent reading persistence

**Skenario:** `POST /api/v1/import-batches` menerima reading valid, tetapi anomaly scorer timeout.

1. Authenticated import checks site membership and schema.
2. DB commits `MeterReading` with `pending_scoring`, including UTC interval and kWh.
3. Scorer adapter times out; system marks `scoring_unavailable` and retains the accepted reading.
4. Operator sees time-series with reading present; review queue can handle missing scoring.
5. Test fake scorer timeout and assert reading count unchanged; verify no false `normal` label was fabricated.

**Anti-pattern:** holding a DB transaction open during a long external inference call or deleting readings when the model fails.

## 2. Stable port for model substitution

```python
from typing import Protocol
from dataclasses import dataclass

@dataclass(frozen=True)
class AnomalyResult:
    anomaly_score: float  # finite, normalized [0,1]; validate at adapter boundary
    flagged: bool
    model_version: str

class AnomalyScorer(Protocol):
    def score(self, history: list[float], current_kwh: float) -> AnomalyResult: ...
```

Pilih rule baseline atau ML adapter tanpa mengubah review API. Sebelum menyimpan output, enforce finite score, model version, dan site-scoped authorization di backend.

## 3. Trust boundary checklist

Browser cannot authorize itself. CSV is untrusted. Model output is untrusted. DB is source of record for site/meter permissions. No model output can trigger electrical actuation. Draw success and timeout sequence diagrams and attach actual test outcomes after implementation.

[Domain contract](../../docs/architecture/energy-data-contract.md) · [Threat model](../../docs/architecture/threat-model.md).
