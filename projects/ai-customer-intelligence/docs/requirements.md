# Capstone Requirements (Draft)

**Scope:** teaching project with synthetic customer inquiries.

## User stories

- As an **agent**, I can upload a synthetic inquiry file and see which rows were accepted/rejected, so I know which records require correction.
- As an **agent**, I can view a predicted category and model version, so I can decide whether to accept or override it.
- As a **supervisor**, I can review changes and aggregate quality indicators without needing access to secret settings.
- As an **operator**, I can see service health, errors and model latency while avoiding exposure of inquiry content in logs.

## Acceptance criteria (to implement and test)

1. Invalid rows are rejected with actionable, non-sensitive reasons.
2. Re-importing the same source does not silently duplicate records.
3. Users cannot read/modify data outside their authorized scope.
4. Model results conform to a documented response schema; invalid outputs cannot be persisted.
5. An unavailable AI service does not erase accepted inquiries and is reported clearly.
6. Corrections retain original prediction, editor and timestamp in an audit record.
7. Health, installation and recovery procedures are documented and demonstrated.

## Out of scope initially

Real customer data, automatic trading or financial advice, autonomous outbound messaging, model fine-tuning at scale, billing, real production integrations.
