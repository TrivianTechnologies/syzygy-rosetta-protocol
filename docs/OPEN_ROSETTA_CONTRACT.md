# Open Rosetta: proposed profiles and versioned contract

Contract ID: **open-rosetta-contract/0.1.0-draft.1**.
Status: **PROPOSED — founder review required**. Date: 2026-10-10.

This is PR 1, Decision Records and Versioned Contract Manifest. The architecture
direction is approved with conditions; every status rule and contract detail
here remains a draft documentation decision. No release version advances and
no runtime behavior changes. The [manifest](open-rosetta-contract.manifest.json)
describes this proposal for readers/tools; it is not runtime configuration or
an adopted wire schema.

## Decisions and profiles

| Record | Proposed obligation |
|---|---|
| [DR-0001](decisions/0001-open-rosetta-profiles-and-version-domains.md) | Canonical public protocol; separately distributed public Rosetta SDK; independent version domains; rights and compatibility gates |
| [DR-0002](decisions/0002-assessment-and-consequential-release.md) | Order-independent assessment precedence, profile-owned coverage, fresh governed release and explicit effect boundaries |
| [DR-0003](decisions/0003-substantive-correction-uptake.md) | Observable attributable uptake, proposed fixture matrix, unresolved TRIA compatibility gates |

`assessment-only` cannot authorize external actions. `governed-execution`
requires a version-pinned public TRIA backend, one authoritative backend per
deployment and fresh resolution at each consequential boundary. Missing or
incompatible backend denies release; no cached-ALLOW, assessment-only or
alternative-backend fallback. Separate assessment, permission, attempt,
completion receipt and observed external effects. Hosts retain responsibility
for real effects and evidence. Local guarantees do not imply remote atomicity
or cancellation. A first implementation may be local; HTTP is not required.

## Version domains and coverage

Protocol, package, schema, contract and compatibility versions are independent
as defined in DR-0001. Profile/check-set version `0.1.0-draft.1` is proposed
documentation only. Neither profile nor schema may be silently inferred or
upgraded. No supported integration tuple or new runtime schema is declared.

Both draft profiles own the nonempty required set: `authority_current`,
`consent_current`, `scope_valid`, `constraints_preserved`. Callers cannot reduce
it. Given recognized profile/schema, propose `FAILS` for any valid definite
false applicable required check; otherwise `UNRESOLVED` for unknown, missing,
invalid, unavailable or ambiguous coverage; `SURVIVES` only for complete valid
unambiguous true coverage. False dominates unknown, while all diagnostics are
retained. Missing/empty/partial/duplicate/conflicting coverage cannot yield
vacuous SURVIVES. Unknown profile/schema versions are non-authorizing and
UNRESOLVED. Both FAILS and UNRESOLVED deny governed release; SURVIVES remains
insufficient without current permission and all other gates.

DR-0002 records the current prose/code discrepancy. This is a proposed contract
resolution, not a runtime fix or a capability established by passing tests.

## Boundaries and correction evidence

The last-correctable boundary is inclusive. Deny late first release; distinguish
it from correction after an already-crossed effect boundary, which cannot imply
cancellation. Missing/ambiguous effect evidence stays unknown. Corrections need
attributable pre/post state, claim/dependency/correction identities, provenance,
authorized acceptance/application, next-consumption behavior and relevant
consequence traces. Content alignment alone does not prove causation. See all
eleven proposed fixtures in DR-0003; none are implemented by this PR.

## Tested baseline

These are separately observed public heads, not a validated integrated stack.
Links pin the audited source; this PR's documentation commit is recorded in PR
validation evidence separately, avoiding a self-referential manifest hash.

| Public repository / immutable source | SHA | Evidence scope |
|---|---|---|
| [Protocol](https://github.com/TrivianTechnologies/syzygy-rosetta-protocol/blob/b4a3115da4fd9d9d46b2d87e9fa6556b24bc0b89/README.md) | `b4a3115da4fd9d9d46b2d87e9fa6556b24bc0b89` | Existing offline suite: 65 passed on Python 3.12.14 and 3.13.5 |
| [TRIA SDK](https://github.com/TrivianTechnologies/tria-sdk/blob/19919d8c2562cc00381b30ac3a303a83ce6787fa/pyproject.toml) | `19919d8c2562cc00381b30ac3a303a83ce6787fa` | 408 passed on each interpreter; wheel/sdist builds and four isolated clean-install checks passed |
| [Rosetta SDK scaffold](https://github.com/TrivianTechnologies/syzygy-rosetta-sdk/blob/c2907575de1ce4d79d36041c95d5ac03a38f4633/README.md) | `c2907575de1ce4d79d36041c95d5ac03a38f4633` | Documentation-only inspection; no installable SDK or tested integration |
| [Sandbox](https://github.com/TrivianTechnologies/syzygy-rosetta-sandbox/blob/2136b84a0bf8996c9a2b0a7ff13d020f9fc4a4ee/README.md) | `2136b84a0bf8996c9a2b0a7ff13d020f9fc4a4ee` | No assertion-based safe offline suite; service/credential checks not executed or collected |

The isolated sandbox `drift_tests/without_rosetta/run.py` produced six static
fixture records per interpreter without service calls; that is fixture
generation, not a test pass or empirical governance evidence. Current results
are separate from historical saved artifacts. Protocol CI lists Python 3.10
and 3.12; TRIA CI lists 3.11 and 3.12. Python 3.10/3.11 were unavailable locally;
3.13 was an additional metadata-permitted check, not proof of a supported
integration range. No private MVP or proprietary financial-compliance code was
inspected or reused.

## Open gates and choices

| ID | Review item / limitation |
|---|---|
| G01 | Correction graph validation — UNRESOLVED compatibility gate |
| G02 | Next-context contestation propagation — UNRESOLVED compatibility gate |
| G03 | Mutation-wide authority/atomicity — UNRESOLVED compatibility gate |
| F033 | Cross-store freshness/global no-resurrection — UNRESOLVED, outside initial guarantees; no distributed solution in this PR |
| O01 | License files absent in SDK/Sandbox; no license choice or rights assignment here |
| O02 | Supported interpreter/dependency ranges and exact compatible backend tuple require review; baseline pins are not adopted integration pins |
| O03 | Distribution/import names, profile naming and public API shape require review |
| O04 | Wire schema/transport and any HTTP service require review; local-first implementation is permitted as a future design choice |

## Six-PR plan

| PR | Scope | Authorization |
|---|---|---|
| 1 | Decision Records and Versioned Contract Manifest | PR 1 documentation and draft review only |
| 2 | Public types and non-authorizing reference profile | NOT AUTHORIZED — new approval required |
| 3 | TRIA adapter and guarded execution profile | NOT AUTHORIZED — new approval required |
| 4 | Correction contract and bounded uptake work | NOT AUTHORIZED — new approval required |
| 5 | Local mock conformance Sandbox and migration documentation | NOT AUTHORIZED — new approval required |
| 6 | Packaging and release-candidate evidence | NOT AUTHORIZED — new approval required |

This is the current agreed sequence. Architecture approval does not authorize
PRs 2–6. Each requires new approval; license changes, merge, publication and
deployment also require separate approval. Listing follow-on work does not
implement it or satisfy its unresolved compatibility gates.

## Provenance and review boundary

Preserve Sarasha Elion / Trivian Institute provenance, contributor and third-party
rights, historical grants and notices, and current engineering stewardship by
Trivian Technologies. Current protocol software MPL-2.0 and documentation
CC BY-SA 4.0 notices apply as described in DR-0001; no new license or ownership
assignment is made. Missing SDK/Sandbox licenses remain unresolved.

PR 1 must remain documentation-only. No source, assertions, frozen witnesses,
runtime schemas, package versions, dependency pins, workflows or license files
change. PRs 2–6, merge, publication and deployment require further authorization.
