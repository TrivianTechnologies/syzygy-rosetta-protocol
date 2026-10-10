# DR-0003: Evidence for substantive correction uptake

Status: **PROPOSED — founder review required**. Fixtures below are specifications,
not newly implemented tests or claims of current capability.
Date: 2026-10-10. Contract: [open-rosetta-contract/0.1.0-draft.1](../OPEN_ROSETTA_CONTRACT.md).

## Decision and evidence obligations

Substantive correction uptake means an observable, attributable change in a
relevant downstream state, next consumption or consequence. Acknowledgment,
corrected wording alone, an assessment, or a branch-selected boolean is not
sufficient. Immutable occurrences remain intact; correction changes supported
interpretation/use with provenance rather than overwriting history.

Every proposed fixture must retain:

- pre/post state with identities/digests and observation times;
- correction ID, target claim IDs and claim/dependency versions and identities;
- correction source, evidence provenance and relevant causal/dependency links;
- epistemic support plus distinct authorized acceptance and authorized
  application, with actor, scope, authority version and boundary observations;
- next-consumption trace showing whether the relevant corrected/contested state
  actually reached the consumer and what it did with that state;
- actual relevant consequence traces: attempts, receipts and effect observations,
  including unchanged/withheld effects and explicit missing observations;
- a comparison/control sufficient to distinguish content alignment from causal
  attribution, and an evidence level identifying simulation versus live evidence.

Temporal succession or aligned output does not by itself establish causation.
Controlled simulation can support a bounded causal account by varying the
correction while holding relevant inputs fixed; it does not become external
live evidence. A live causal claim requires its own adequate observations and
attribution design. A trace supplied by an unverified host is not automatically
authoritative merely because it is structurally well formed.

## Proposed fixture matrix

| Fixture ID | Required control and expected interpretation |
|---|---|
| U01 effective-uptake | Supported correction, valid authority and relevant dependency; observable authorized downstream change, next-consumption and consequence traces support scoped uptake |
| U02 acknowledgment-only | Acknowledgment recorded but relevant state/use/effect unchanged; no substantive uptake |
| U03 ignored-correction | Valid supported correction received in-window but not applied/consumed; fails the claimed uptake obligation |
| U04 unrelated-change | A different claim/effect changes; cannot count toward target correction uptake |
| U05 unsupported-correction | Unsupported content must not acquire authority or silently replace the claim; preserve rejection/uncertainty diagnostics |
| U06 wrong-authority | Content may align, but acceptance/application lacks correct authority; no authorized uptake or governed release |
| U07 before-boundary | Authorized correction before the boundary; require observable uptake, not merely eligibility |
| U08 at-boundary | Same obligation at the inclusive boundary; a branch-selected true is insufficient |
| U09 after-boundary | Disclose too late for the crossed effect; no cancellation inference; late first release is separately denied |
| U10 stale-dependency | A superseded/contested dependency cannot support a current clean claim; missing fresh resolution withholds governed release |
| U11 missing-observation | Missing pre/post, consumption or consequence evidence leaves claimed uptake UNRESOLVED, not success |

Apply before/at/after controls to the relevant fixtures, and keep assessment
status separate from the fixture's uptake finding. Deliberately unchanged
irrelevant claims are controls, not proof of ignored relevant correction.

## Unresolved compatibility gates

The audited public TRIA baseline includes correction assessment and governed
application surfaces, but green tests do not establish this proposed integration.
Specifically, **correction graph validation**, **next-context contestation
propagation**, and **mutation-wide authority/atomicity** remain UNRESOLVED gates.
Later authorized work must establish graph integrity and dependency semantics,
observable propagation into the next actual context, and authorization/atomicity
across the relevant mutation path before claiming compatibility. This decision
does not prescribe a fix, change witnesses, or certify those capabilities.

See pinned [correction assessment](https://github.com/TrivianTechnologies/tria-sdk/blob/19919d8c2562cc00381b30ac3a303a83ce6787fa/src/tria/correction.py)
and [local authority limits](https://github.com/TrivianTechnologies/tria-sdk/blob/19919d8c2562cc00381b30ac3a303a83ce6787fa/docs/agentic-alignment-contract.md).
F033 remains UNRESOLVED; no distributed-freshness solution is designed here.
