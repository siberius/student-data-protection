# 1. Reading the requirements and the assistant's workflow

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 1.

## 1. Reading the requirements and the assistant's workflow

- **[Z] Legal requirement:** applies when the stated conditions are met. The cited regulation takes precedence over technical advice.
- **[P] Security profile:** a concrete implementation choice of this skill. MUST and MUST NOT in the technical sections define this profile, not a literal GDPR command. Document any deviation with the threat, the compensating control, a test, and the decision of the school's responsible person.
- **[D] Recommendation:** a useful extension depending on risk and operation.
- **[O] Verify:** a question that depends on actual use, current law, or unconfirmed configuration. Do not present it as satisfied.

1. Determine the requested mode from the task: design, implementation, audit or incident. An audit produces findings and recommendations without changing the application. An incident review does not authorise disabling live services, revoking accounts or notifying people. Execute such actions only within actual authorisation.
2. Reuse known context and identify the affected purpose, data flows, roles and change in risk. Ask only for missing information that changes the decision. For a narrow fix, assess the affected boundary and regressions instead of restarting the entire application assessment. Flag a serious adjacent issue with evidence; do not silently expand implementation.
3. Map only the relevant data, recipients, identity, permissions, retention and threats. Preserve an existing secure architecture and working controls. Use synthetic data while purpose, lawful basis or deployment decisions remain unresolved.
4. For design, propose proportionate controls and acceptance criteria. For authorised implementation, apply the selected controls and record their code/configuration locations. For audit, report severity, evidence, impact, proposed action and the verification needed. Classify suspected issues separately from observed failures.
5. Select acceptance scenarios for the affected features and risk. Report passed, failed, not performed and not applicable with a reason; a full redesign is not required for every correction. Do not claim execution from a proposed test plan.
6. Before real-data deployment, verify the applicable legal basis, required assessment and current legal text. The controller makes deployment decisions with timely DPO advice and appropriate expert review. If a required basis or assessment is missing, do not recommend the affected processing; continue authorised unaffected work.

Do not put real student data, production logs, keys, or databases into an ordinary AI chat or a public repository. Generate synthetic data for debugging. Using real data in an AI service requires a separate assessment of purpose, necessity, contract, recipients, retention, and transfers; disabling training alone is not enough.

### 1.1 Select controls by data flow and risk

Legal duties apply when their conditions are met. Baseline outcomes are purpose limitation, minimisation, trustworthy access boundaries, integrity, recoverability and an accountable handling of incidents and rights, proportionate to actual processing. An activity with no personal processing does not need accounts, a database, KMS or a personal audit merely because this guide describes them. Check hosting and operational metadata before calling it anonymous.

The detailed [P] settings below form a strict reference profile for new systems with persistent school records or where the project explicitly adopts it. Named algorithms, timeouts and operational targets are profile choices. For an existing system, first assess its actual controls and equivalent protections against the relevant threats; a different maintained technology is not automatically a vulnerability. Do not weaken authorisation or invent an exemption from law. Document a material departure from an adopted profile with the threat, compensating control, verification and the responsible controller's decision. A review may propose that decision; it must not fabricate approval or require a new approval for every routine in-scope edit.

Choose the architecture before applying implementation-specific recipes. Encryption-library internals and nonce management belong to the component doing that encryption, not automatically to the application if a verified storage service handles it. Explain key access, backup protection, metadata exposure and residual risk for the actual solution. Any change to hosting, identity provider, paid service or data recipients needs the corresponding authorisation.

### 1.2 Controller and DPO

The controller is accountable for purposes, lawful processing and deployment decisions. The DPO informs, advises and monitors independently and is consulted in good time, including on a DPIA. This guide does not assign general operational approval or controller responsibility to the DPO. Record advice and the responsible decision; resolve disagreements through the appropriate governance process. See [EDPB: DPO](https://www.edpb.europa.eu/sme/be-compliant/data-protection-officer_en).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
