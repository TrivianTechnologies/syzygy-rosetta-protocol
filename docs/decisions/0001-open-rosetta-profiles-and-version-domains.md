# DR-0001: Open Rosetta profiles and version domains

Status: **PROPOSED — founder review required**. Architecture direction approved
with conditions; this documentation does not approve implementation or a release.
Date: 2026-10-10. Contract: [open-rosetta-contract/0.1.0-draft.1](../OPEN_ROSETTA_CONTRACT.md).

## Context and decision

Keep `TrivianTechnologies/syzygy-rosetta-protocol` canonical for the public
protocol, decisions and versioned contract. Propose a separately distributed
public Syzygy Rosetta SDK, with two explicit profiles:

- `assessment-only`: produces scoped observations and assessments. It cannot
  authorize external actions, including when an assessment says `SURVIVES`.
- `governed-execution`: requires a version-pinned public TRIA backend and fresh
  authoritative resolution at consequential boundaries. Missing, unavailable or
  incompatible backend means no governed release. There is no assessment-only,
  cached-ALLOW, or alternative-backend fallback.

One deployment has one authoritative governance backend. Rosetta must not
create a competing authority registry or silently select the most permissive
backend. A first local implementation need not add an HTTP service. SDK
distribution/import naming, API shape and wire transport remain review choices.
The public SDK scaffold's HTTP examples are plans, not an adopted wire contract.
Private `syzygy-rosetta-v1` and Faiyaz's proprietary financial-compliance Rosetta
are excluded: no inspection, dependency or implementation reuse.

## Independent version domains

| Domain | Meaning and baseline | Proposed change rule |
|---|---|---|
| Protocol | Public normative semantics; existing reference metadata is 2.1.0, with historical README/citation 2.0 labels retained | Semantic changes require separate protocol review; package or contract versions cannot silently redefine it |
| Package | Independently distributed artifacts: current protocol package `syzygy-rosetta` 2.1.0; public `tria-sdk` 0.1.0a7; new Rosetta SDK package version unset | Releases belong to their own distributions; no release advanced here |
| Schema | Each serialized format's identity and version; no new Rosetta wire schema adopted | Unknown/incompatible schema is non-authorizing; no guessing, aliasing or automatic migration |
| Contract | This proposed interoperability/evidence agreement: `open-rosetta-contract/0.1.0-draft.1` | Explicit reviewed revision, independent of runtime releases; draft identifier confers no support |
| Compatibility | Explicit mapping of exact protocol/package/schema/profile/backend versions and exercised guarantees | No supported integration tuple yet; candidate baseline is not a compatibility declaration |

The [JSON manifest](../open-rosetta-contract.manifest.json) is a machine-readable
**documentation artifact**, not runtime configuration, a runtime schema, or a
dependency resolver. Its `manifest_format_version` versions its documentation
layout only. Profile/check-set versions are part of the contract and cannot be
chosen ad hoc by callers. Unknown profile or schema versions cannot authorize.

Existing TRIA version domains remain distinct: operational spec 0.1.3,
diagnostic 0.2, truth-integrity 0.1, event schema 0.3, projection 0.6, replay
bundle 0.1, additive claim-release/correction protocol 0.2. These observations
are not interchangeable numbers or permission to migrate historical records.

## Evidence and compatibility gates

The [contract baseline](../OPEN_ROSETTA_CONTRACT.md#tested-baseline) records exact
public commits and scoped tests. Separate green suites do not validate future
Rosetta/TRIA composition. Required unresolved gates include TRIA correction
graph validation, next-context contestation propagation and mutation-wide
authority/atomicity. F033 remains UNRESOLVED and outside initial guarantees;
this PR designs no distributed-freshness mechanism.

Review must resolve licensing, supported interpreter/dependency ranges, naming
and wire transport before any corresponding implementation/release claim.
Existing metadata lower bounds and locally available interpreters do not
establish a supported integration matrix.

## Provenance and rights

Preserve Sarasha Elion's authorship, Trivian Institute research lineage, and
Trivian Technologies' current engineering home. Stewardship is not ownership
assignment. Contributor and third-party rights and notices remain applicable.
Current protocol software is MPL-2.0; documentation is CC BY-SA 4.0 where
applicable, with file-specific notices controlling. Earlier grants remain
valid; historical evidence and citations are retained. See the existing
[license record](../../LICENSE_METADATA.md), [software license](../../LICENSE)
and [documentation notice](../../LICENSE-DOCUMENTATION.md).

The public Rosetta SDK and Sandbox trees inspected at the recorded commits
have no repository license files. That absence is unresolved, not permission
to assume this repository's licenses apply there. No license selection,
relicensing, trademark grant or founder IP assignment is authorized by PR 1.

## Consequences

PR 1 changes only documentation and navigation. Runtime source, tests, frozen
witnesses, version pins, licenses and workflows remain unchanged. Later work
requires separate authorization under the [six-PR plan](../OPEN_ROSETTA_CONTRACT.md#six-pr-plan).
