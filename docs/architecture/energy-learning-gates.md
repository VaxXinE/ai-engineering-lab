# Cross-Module Engineering Gates — Energy Capstone

This document defines a **planned verification contract**, not proof that Week 02–16 code exists. Each gate is satisfied only when actual evidence is linked from an implemented branch.

| Weeks | Quality gate | Negative case / security gate | Planned artifact |
| --- | --- | --- | --- |
| 01–02 | Distinguish text classification from numeric anomaly scoring; justify model/stack | No calibration or accuracy overclaim; dependency provenance | Model comparison + ADR |
| 03 | Synthetic CSV ingestion with composite event identity | Duplicate payload conflict and SQL injection-safe parameters | Data generator, importer, batch summary |
| 04 | Finite numerics, UTC 15-min interval and data-quality reporting | NaN/inf, wrong interval, gaps, invalid timestamps | Validation tests & quality report |
| 05 | Sliding window and per-meter aggregations are deterministic | Future leakage and unbounded memory/batch | Complexity and invariant tests |
| 06 | Analyst can find an outlier and see context | Missing data ≠ zero; inaccessible controls | UX wireframes + task review |
| 07 | Dashboard handles loading/empty/error/review states | Cross-site cache bleed and malformed AI output | UI tests + accessibility report |
| 08 | Site/meter/readings/anomaly/review constraints | Composite uniqueness, lost update and IDOR | ERD, migrations, SQL integration tests |
| 09 | Ports/adapters and API contract support outage fallback | Site authorization server-side, no silent data deletion | Component/sequence diagrams + contract tests |
| 10 | Capacity and tail-latency test reproducible | Bounded retries and no unauthorized stress testing | Load-test plan and measurements |
| 11 | Time-split, per-meter baseline, labeled synthetic evaluation | Future data excluded; held-out test not tuned on | Model card and metrics |
| 12 | Score schema, audit and human override | Invalid score/NaN, timeout, cross-site review | Integration/contract tests |
| 13 | Clean install with locked versions and health probes | Secret leak, unsafe exposed DB and incompatible migrations | Runbook + smoke tests |
| 14 | Monitoring plans align to SLI/SLO and review burden | No fabricated drift/availability claims | Maintenance/alert/backup plan |
| 15 | Isolated restore and inference-outage recovery | No real production changes or data overwrite | Incident report with actual tests |
| 16 | Map authentic artifacts to approved LSP KUK | Do not publish identity docs or claim automatic credit | Evidence matrix + gap register |

A clear distinction between **planned**, **implemented**, **tested**, and **LSP-assessed** must remain visible across every module.
