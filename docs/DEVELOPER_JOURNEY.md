# From protocol to a working local integration

Open Rosetta makes assessment, authority and observed outcomes separately inspectable.
Use this path to evaluate it with a small synthetic example before integrating a
consequential operation.

1. **Understand the contract.** Read the [implemented reference capabilities](../README.md),
   [relational architecture](RELATIONAL_ARCHITECTURE.md), and
   [integration contract](OPEN_ROSETTA_CONTRACT.md). The contract's draft status is
   explicit; implementation evidence does not silently ratify normative changes.
2. **Install the SDK.** Use the [SDK developer guide](https://github.com/TrivianTechnologies/syzygy-rosetta-sdk/blob/f54813a5fc90fbcf3c5aaa49b1f974a02766bf93/docs/GETTING_STARTED.md).
   This guide is a review candidate. It names exact merged SDK/TRIA source revisions,
   Python requirements and clean-environment commands; no PyPI release is assumed.
3. **Observe a boundary.** Run the SDK quickstart: one authorized mock action, consent
   revocation, then a blocked attempt. Assessment alone never authorizes.
4. **Reproduce the controls.** The [Sandbox repository](https://github.com/TrivianTechnologies/syzygy-rosetta-sandbox)
   retains its existing default branch while the new offline candidate awaits review
   and deployment-trigger clearance. Use its supplied candidate artifact for local
   reproduction; do not run legacy service-connection tests as offline checks.
5. **Discuss an implementation.** Contact [node@triviantech.com](mailto:node@triviantech.com)
   with source revisions, the boundary you need, and a synthetic example. Investment
   inquiries go to [invest@triviantech.com](mailto:invest@triviantech.com).

Assessment and governed execution are distinct profiles. Correction-dependent SDK
execution remains gated. Fixed local correction controls demonstrate encoded
behavior, not verified host truth or live external effects. F033 remains unresolved:
no distributed revocation freshness, independent-store convergence or global
no-resurrection guarantees. Architecture and normative contracts remain unchanged.

## Obtain the documented SDK example

```bash
git clone https://github.com/TrivianTechnologies/syzygy-rosetta-sdk.git
cd syzygy-rosetta-sdk
git checkout f54813a5fc90fbcf3c5aaa49b1f974a02766bf93
```

This pins the onboarding candidate, including `examples/quickstart.py`. Follow its
Getting started guide to create a fresh environment and install the separately
pinned merged runtime sources. A documentation candidate is not a package release.
