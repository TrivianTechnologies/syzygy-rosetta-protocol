# Open Rosetta: proposed profiles and versioned contract

Contract ID: **open-rosetta-contract/0.1.0-draft.2**.
Status: **PROPOSED integration contract; not implemented or ratified**.
Date: 2026-10-10.

The public protocol defines scoped authority, behavioral assessment and
inclusive correction boundaries. Its reference implementation demonstrates
bounded local behavior through the existing test suite. This document proposes
how a separately distributed Rosetta SDK would compose those semantics with
public TRIA. The protocol and its reference behavior retain their own evidence status.

The [manifest](open-rosetta-contract.manifest.json) is a machine-readable
**documentation artifact**, not runtime configuration or an adopted wire schema.
Only this documentation contract revision changes; release versions and runtime
behavior remain unchanged.

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

## Conformance

**Current reference evidence:** scoped authority lifecycle and queued current
resolution are exercised by the reference suite; the declared correction window
is inclusive. Complete boolean behavioral checks have explicit pass/fail
results; missing/invalid/unavailable evidence yields uncertainty. The
[assessment discrepancy](decisions/0002-assessment-and-consequential-release.md#documentationreference-code-discrepancy)
limits claims about mixed evidence and complete diagnostics.

**Proposed integration requirements:** the following coverage and aggregation
rules specify the future SDK contract, not current implementation behavior.

Protocol, package, schema, contract and compatibility versions are independent
as defined in DR-0001. Profile/check-set version `0.1.0-draft.2` is proposed
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

## Security

The last-correctable boundary is inclusive. Deny late first release; distinguish
it from correction after an already-crossed effect boundary, which cannot imply
cancellation. Missing/ambiguous effect evidence stays unknown. Corrections need
attributable pre/post state, claim/dependency/correction identities, provenance,
authorized acceptance/application, next-consumption behavior and relevant
consequence traces. Content alignment alone does not prove causation. See all
eleven proposed fixtures in DR-0003; these remain integration requirements, not
capabilities established by the existing reference suite.

## Tested baseline

These are separately observed public heads, not a validated integrated stack.
Links pin the audited source. Documentation-head test runs and CI are recorded
separately in the change's execution records; they are not new integration evidence.

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
integration range.

## Compatibility

| ID | Review item / limitation |
|---|---|
| G01 | Correction graph validation — UNRESOLVED compatibility gate |
| G02 | Next-context contestation propagation — UNRESOLVED compatibility gate |
| G03 | Mutation-wide authority/atomicity — UNRESOLVED compatibility gate |
| F033 | Cross-store freshness/global no-resurrection — UNRESOLVED, outside initial guarantees; no distributed solution specified here |
| O01 | License files absent in SDK/Sandbox; establish applicable grants and notices before distribution/reuse |
| O02 | Supported interpreter/dependency ranges and exact compatible backend tuple require review; baseline pins are not adopted integration pins |
| O03 | Distribution/import names, profile naming and public API shape require review |
| O04 | Wire schema/transport and any HTTP service require review; local-first implementation is permitted as a future design choice |

## Release

No SDK integration release or supported compatibility tuple is established.
A release candidate needs explicit protocol/package/schema/contract/profile/
backend versions; demonstrated conformance, including the proposed coverage and
uptake controls; resolved compatibility gates for its claimed capabilities; an
exercised interpreter/dependency matrix; and documented licensing and transport
choices. A first local implementation need not add an HTTP service.

The candidate must retain raw execution records, failures and limitations
separately from historical evidence. Passing the current reference suite is
positive evidence for its encoded local behavior, not proof of the proposed
mixed-evidence rule, integrated correction propagation or external effects.
F033 remains outside the initial guarantee envelope.

## Licensing and attribution

Current protocol [software](../LICENSE) is MPL-2.0; its
[documentation](../LICENSE-DOCUMENTATION.md) is CC BY-SA 4.0 where applicable.
Follow controlling file-specific notices, preserve contributor attribution and
historical grants, and credit Sarasha Elion / Trivian Institute and current
engineering home Trivian Technologies. See [DR-0001](decisions/0001-open-rosetta-profiles-and-version-domains.md)
for the SDK/Sandbox licensing requirement. No license files change here.
