# DR-0002: Assessment precedence and consequential release

Status: **PROPOSED — founder review required**. No runtime change.
Date: 2026-10-10. Contract: [open-rosetta-contract/0.1.0-draft.1](../OPEN_ROSETTA_CONTRACT.md).

## Assessment decision

The versioned profile owns a nonempty required-check set. A caller supplies
evidence, not a replacement list or a reduced set of requirements. The draft
profiles require `authority_current`, `consent_current`, `scope_valid` and
`constraints_preserved`; domain-specific applicability and extensions require
profile review. A caller cannot mark a required check optional or inapplicable.

For a recognized profile and schema, aggregate all observations without early
return. Apply this proposed precedence, independent of check/observation order:

1. `FAILS`: any applicable required check has a valid, definitively false
   observation, even alongside unknown, missing or invalid evidence elsewhere.
2. `UNRESOLVED`: no such false observation exists, but required evidence is
   missing, invalid, unavailable or coverage is incomplete/ambiguous.
3. `SURVIVES`: every required check has complete, valid, unambiguous true
   evidence under the versioned profile. It describes only those checks.

Missing, empty or partial check coverage cannot yield a vacuous `SURVIVES`.
Duplicate/conflicting required-check coverage is ambiguous and non-authorizing:
retain all observations, do not silently deduplicate or use first/last-wins.
When a valid definite false is present it still yields `FAILS`; otherwise the
coverage defect yields `UNRESOLVED`. Invalid evidence is not coerced to false
or true. An absent/unrecognized profile or schema is `UNRESOLVED` and denies
release; retain observations diagnostically without inventing applicability.

Both `FAILS` and `UNRESOLVED` deny governed release. `SURVIVES` alone never
authorizes it. Preserve diagnostics for every supplied observation and every
missing requirement, including identities, provenance, validity, reasons and
errors; optional/advisory observations remain distinguishable. Do not erase
unknowns merely because a definite violation determines the aggregate status.

### Documentation/reference-code discrepancy

The pinned [remediation prose](https://github.com/TrivianTechnologies/syzygy-rosetta-protocol/blob/b4a3115da4fd9d9d46b2d87e9fa6556b24bc0b89/docs/FROZEN_REMEDIATION.md)
says any false check yields FAILS. Pinned [reference code](https://github.com/TrivianTechnologies/syzygy-rosetta-protocol/blob/b4a3115da4fd9d9d46b2d87e9fa6556b24bc0b89/core/reflex.py)
can return UNRESOLVED for missing, exceptional or nonboolean evidence before
aggregating a false result; early return can also omit later diagnostics.
This decision resolves the intended meaning **only at the proposed contract
level**, pending founder review. Existing behavior, tests and historical
evidence are unchanged; passing reference tests does not implement this rule.

## Release and effect decision

Keep five evidence categories separate: assessment; current permission;
execution attempt; completion receipt; independently observed external effects.
A reference ALLOW or INTERVENE is neither an execution attempt nor a receipt.
A receipt must not imply more external effect certainty than its evidence.

The host owns authentication, real-world authority/evidence, external effects,
transport, retries, cancellation and external observation. The proposed SDK
owns only its declared local mediation. Governed release requires a recognized
compatible tuple, pinned public TRIA backend, fresh authoritative resolution,
valid current scoped permission/consent, a satisfied assessment and a valid
boundary. Fail closed on backend loss, ambiguity, invalid or stale dependency
state, unknown versions or unresolved compatibility gates. No cached ALLOW,
alternate authority source or alternative-backend fallback is permitted.

The last-correctable boundary is **inclusive**: before and at the declared
boundary correction can still be attempted under fresh authority. A host must
justify that boundary against the actual effect path, not just a stage label.

- **Late first release:** first authorization/release resolution after that
  boundary is denied. A late ALLOW cannot retroactively authorize an effect.
- **Correction after an effect boundary:** disclose that correction is too
  late for that effect; do not imply the original effect was blocked, undone or
  cancelled. Any later remediation is a separately authorized action.

The pinned [queued reference](https://github.com/TrivianTechnologies/syzygy-rosetta-protocol/blob/b4a3115da4fd9d9d46b2d87e9fa6556b24bc0b89/evaluation/governability_harness.py)
already separates a late first release gate from its immediate correction
path. Branch-selected `consequence_changed` values are reference decisions,
not observations proving downstream change or cancellation.

Record attempts, action/correction identities, boundary observations and
receipts separately. Timeout, missing receipt or ambiguous transport outcome
requires explicit **unknown effect**, not success or no-effect. Do not blindly
retry on assumed nonexecution; host reconciliation and any retry require fresh
authority. Scope all initial guarantees to a declared local backend/store and
handoff; do not claim distributed atomicity, remote cancellation, freshness of
independent stores or global no-resurrection. F033 remains UNRESOLVED.
