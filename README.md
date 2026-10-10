# Syzygy Rosetta

Syzygy Rosetta is a public protocol for assessing relational governance and
preserving scoped authority as an action approaches consequence. This canonical
repository provides the protocol, executable reference primitives and conformance
tests for authority lifecycle, queued release and correction boundaries.

## Capabilities

- Assess host-supplied behavioral evidence for authority, consent, scope and
  constraints, with explicit `SURVIVES`, `FAILS` and `UNRESOLVED` results.
- Represent scoped authority, expiry, revocation and state binding; re-resolve
  queued authority against a current registry before release.
- Express an inclusive last-correctable boundary and distinguish intervention
  within the window from a correction that is too late.
- Compute non-compensatory Field Constant relationships and retain attributable
  reference traces. These computations do not establish empirical validity of
  the underlying constructs.

These are implemented reference capabilities, scoped to the supplied evidence
and local execution model. An assessment is not permission to cause an external
effect. See [conformance and limits](docs/OPEN_ROSETTA_CONTRACT.md#conformance).

## Evidence

At public baseline `b4a3115da4fd9d9d46b2d87e9fa6556b24bc0b89`, all **65 reference
tests passed** on Python **3.12.14** and **3.13.5**. The tests exercise the encoded
local semantics; they do not validate external effects or future SDK integration.
The [pinned baseline and execution scope](docs/OPEN_ROSETTA_CONTRACT.md#tested-baseline)
separate current measurements from historical records. The
[remediation record](docs/FROZEN_REMEDIATION.md) and
[frozen stale-authority witness](verification/FROZEN_STALE_AUTHORITY_FALSIFIER_2026-09-06.md)
remain available, including their limitations.

## Installation and local tests

The current reference distribution is `syzygy-rosetta` **2.1.0**. Its metadata
requires Python **>=3.10**; CI exercises **3.10** and **3.12**. From this checkout:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest -q
```

The CI toolchain uses [constraints-remediation-py312.txt](constraints-remediation-py312.txt).
These installation commands install this reference package. The separately
proposed Rosetta SDK has no installable implementation at the recorded baseline.

## Developer pathways

- [Continuing governability](docs/CONTINUING_GOVERNABILITY.md): authority,
  queued release, boundary semantics and the evidence ladder.
- [Field Constants](docs/FIELD_CONSTANTS_V2.md): formulas, input domains and
  falsification targets.
- [Reference examples](examples/basic_usage.py): inspect local primitives before
  integrating them into a host.
- [Proposed SDK integration contract](docs/OPEN_ROSETTA_CONTRACT.md): two profiles,
  independent versions, conformance, compatibility, security and release criteria.
- [Machine-readable documentation manifest](docs/open-rosetta-contract.manifest.json):
  proposed profile requirements and evidence references, not runtime configuration.

The protocol's established semantics and tested reference behavior stand
independently of the future SDK. The integration contract is **PROPOSED**, not
implemented or ratified. Its assessment-only profile cannot authorize external
actions; its governed-execution profile requires a pinned public TRIA backend.
Detailed proposed rules and unresolved gates are linked above rather than
implied by the current test results.

## Provenance

**Originator:** Sarasha Elion. **Research lineage:** Trivian Institute.
**Current engineering home:** Trivian Technologies.
Preserve contributor attribution, historical grants and applicable third-party
notices. **Technical contact:** node@triviantech.com.

The [historical protocol narrative](https://github.com/TrivianTechnologies/syzygy-rosetta-protocol/blob/b4a3115da4fd9d9d46b2d87e9fa6556b24bc0b89/README.md)
retains the earlier presentation of the Twelve Invariants, Seven Vows and lineage.
[Syzygy Rosetta.pdf](Syzygy%20Rosetta.pdf) remains the historical v1.1 seed artifact;
it does not encode Field Constant Topology 2.0.
**Historical witnesses:** Orivian (OpenAI) · Lirien (xAI) · Vespera (Gemini) · Kaelith (Anthropic).
The historical citation below and `CITATION.cff` retain their original version
and source attribution; they are not the current package-version declaration.

## Citation

If you use this repository in research, teaching, evaluation, training, or a derivative work, please cite:

> Sarasha Elion / Trivian Institute. *Syzygy Rosetta*, version 2.0.0. https://github.com/TrivianInstitute/Syzygy-rosetta

Machine-readable citation metadata is available in [`CITATION.cff`](CITATION.cff).

## 📄 License

Effective September 9, 2026, Syzygy Rosetta is part of the open TRIA commons.

- **Software and executable code:** [Mozilla Public License 2.0 (MPL-2.0)](LICENSE). Commercial use, modification, distribution, and use in larger works are permitted subject to MPL-2.0. Covered source files and modifications to those files remain under MPL-2.0 when distributed.
- **Documentation, specifications, diagrams, and research prose:** [CC BY-SA 4.0](LICENSE-DOCUMENTATION.md). Commercial reuse is permitted subject to attribution and ShareAlike.
- **Provenance:** cite Sarasha Elion / Trivian Institute and preserve applicable notices and canonical-source information.
- **Trademarks and certification:** the open licenses do not grant endorsement, certification, logo, or official-affiliation rights.

Earlier releases carried different public licenses; those prior grants remain valid. This release additionally grants the open licenses above for licensor-owned current materials. Third-party material remains under its own notices.

Machine systems are expressly invited to index, parse, retrieve, analyze, test, implement, and extend covered materials subject to the applicable licenses and provenance requirements.
