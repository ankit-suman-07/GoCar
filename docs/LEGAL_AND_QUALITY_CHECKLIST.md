# Legal, Provenance, and Quality Review Checklist

Version: 1.0 · Prepared: 24 October 2026 · Scope: standalone, extensible vehicle simulator

## Purpose and use

Use this checklist for human-authored and AI-assisted code, scenes, assets, configuration, documentation, dependencies, and releases. It reduces identifiable risks; it is not legal advice, a legal opinion, a patent search, or a guarantee of non-infringement, security, or accuracy. Legal requirements depend on jurisdiction and circumstances.

Review changed material before committing and review the complete distribution before publishing a release. Inspect actual files, dependency terms, and test evidence. Do not mark an item passed based only on an author's or AI's assurance. This file is guidance; it does not automatically execute checks or persist as an instruction in unrelated AI sessions. Provide it to those sessions or reference it through repository guidance.

## 1. Origin and ownership — every change

- [ ] Identify newly written, adapted, copied, downloaded, and generated material.
- [ ] For reused material, record its source, version, licence, modifications, and required notices. Public availability is not permission to redistribute.
- [ ] Do not copy protected code, prose, diagrams, screenshots, datasets, or assets without suitable permission.
- [ ] Confirm the contributor may publish the work. Check relevant employment, university, sponsor, confidentiality, and collaboration agreements when applicable.
- [ ] Review AI-assisted output for unexplained copied comments, names, code, assets, and dependencies. AI generation is not evidence of originality or rights clearance.
- [ ] Never invent provenance, licence permissions, copyright owners, or legal approval. Record uncertainty explicitly.

## 2. Licences and distribution — new dependencies and releases

- [ ] Select an explicit project licence before advertising the repository as open source. Do not assume all files share that licence.
- [ ] Check the actual licence for each dependency, plugin, font, model, texture, sound, map, dataset, and reused snippet.
- [ ] Check redistribution, modification, commercial-use, attribution, source-disclosure, and compatibility obligations as applicable. An optional adapter is not automatically exempt.
- [ ] Preserve required copyright statements, licence texts, attribution, and notices in source and applicable binary/web distributions.
- [ ] Check engine and transitive-dependency notices for the shipped build; do not assume the engine's licence covers every included component.
- [ ] Do not label third-party work as project-owned or remove notices to satisfy a branding preference.
- [ ] Record dependency names, exact versions, sources, licences, and notice locations in a dependency inventory. Review changes on upgrades.

## 3. Identity and claims — documentation and public releases

- [ ] Present the project using its own goals, design, examples, and branding. Avoid clone/replacement framing and unrelated product comparisons in project documents.
- [ ] Review the proposed name/logo for conflicts; do not imply another organisation's endorsement, affiliation, or certification.
- [ ] Preserve mandatory attribution even where an editorial naming preference would otherwise exclude it.
- [ ] Distinguish planned, implemented, and verified features. Publish performance and accuracy claims only with reproducible evidence and stated hardware/configuration.
- [ ] State model assumptions and limitations. Simulation success must not be presented as real-world vehicle safety certification or proof of physical sensor accuracy.
- [ ] Use the selected licence's warranty/liability wording accurately. Do not promise that a disclaimer removes all liability.

## 4. Privacy, confidentiality, and security — every change

- [ ] Exclude API keys, credentials, private URLs, personal records, proprietary code, and restricted research data from files, examples, logs, and commits.
- [ ] Use synthetic example data. Check permissions and applicable privacy obligations before accepting real recordings or personal information.
- [ ] Keep telemetry local by default unless a network connection is explicitly configured. Document any collection, destination, purpose, and retention.
- [ ] Validate external commands, vehicle IDs, schemas, numeric ranges, message sizes, and rates. Reject invalid input with useful errors.
- [ ] Bound queues, buffers, log growth, and scenario resource use. Avoid arbitrary command execution from incoming data.
- [ ] Check scenario paths and writes against traversal or unintended overwrite. Treat third-party scripts/plugins as executable code, not harmless data.
- [ ] Review network exposure and authentication before supporting remote connections. Check dependency vulnerabilities and document unresolved findings.

## 5. Correctness and reproducibility — relevant implementation changes

- [ ] State units, coordinate axes, reference frames, timestamps, and schema versions explicitly.
- [ ] Preserve vehicle/sensor identity and isolation; ensure commands affect only their target.
- [ ] Keep simulation, sensor sampling, display, and telemetry schedules explicit. Do not silently alter experiment timing to improve FPS.
- [ ] Verify disabled sensors do not sample; reset restores documented state; seeded noise behaves as specified.
- [ ] Verify geometry and collision simplifications preserve the properties needed by the scenario. Separate visual detail from sensor and collision representations.
- [ ] Run proportionate functional tests and headless checks. Record failures, skipped checks, and untested platforms honestly.
- [ ] For optimisations, compare reference outputs within documented tolerances and measure resource use. Fixed seeds alone do not prove cross-platform determinism.
- [ ] Record software versions, scenario configuration, seed, timestep, and relevant environment information with experiment results.

## 6. Release decision

Use four outcomes: PASS (evidence inspected), FAIL (requirement unmet), UNKNOWN (evidence insufficient), or N/A (reason recorded). A pass means this review found no unresolved issue in scope; it is not legal clearance.

- Fix or exclude material with unclear redistribution rights, missing mandatory notices, exposed secrets, or unresolved critical security findings before release. Continue independent work on unaffected material.
- Seek the rights holder's clarification or qualified advice for disputed ownership, incompatible/unclear licences, material trademark or patent concerns, or consequential liability questions. Do not ask for routine approval when evidence already resolves the issue.
- Escalate university/sponsor ownership questions before publishing affected work. General ideas may be reused, but patents, contracts, and protected expression require separate consideration.
- Before release, verify the exact source archive, binary, or web package—not only the development checkout—and include required notices and applicable source materials.

## Review record template

```text
Change / PR / release:
Commit and reviewed files:
Reviewer and date:
Origin / ownership: PASS | FAIL | UNKNOWN | N/A — evidence:
Licences / notices: PASS | FAIL | UNKNOWN | N/A — evidence:
Branding / claims: PASS | FAIL | UNKNOWN | N/A — evidence:
Privacy / security: PASS | FAIL | UNKNOWN | N/A — evidence:
Correctness / tests: PASS | FAIL | UNKNOWN | N/A — evidence:
Checks not performed and limits:
Open issues, affected files, and owner:
Decision: ready within reviewed scope | revise | specialist review needed
```

## Minimal supporting repository files

Maintain `LICENSE`, `THIRD_PARTY_NOTICES.md`, a dependency/asset inventory, `CONTRIBUTING.md`, model limitations, and a private vulnerability-reporting route when accepting public users. Add per-file licences where required. A source inventory may use:

| Path/package | Origin/version | Rights holder | Licence/permission | Changes | Required notices |
|---|---|---|---|---|---|
| To be completed | | | | | |

## Reference sources

Consult current terms when adding material or changing distribution; these references do not clear this project's particular files.

- Canadian Intellectual Property Office, [About copyright](https://www.ised-isde.canada.ca/site/ised/en/about-copyright): expression versus ideas.
- CIPO, [Intellectual property rights in software in Canada](https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/intellectual-property-rights-software-canada): distinct IP rights.
- GitHub, [Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).
- Godot, [Engine licence](https://godotengine.org/license/): engine attribution and licence information.
- Apache Software Foundation, [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0): example terms covering redistribution, patents, trademarks, warranty, and liability; not a licence selection for this project.
- Office of the Privacy Commissioner of Canada, [Meaningful consent guidance](https://www.priv.gc.ca/en/privacy-topics/privacy-for-businesses/appropriate-handling-of-personal-information/collecting-personal-information-and-consent/consent/gl_omc_201805/): relevant where applicable personal-information laws apply.
- Ontario Tech, [Intellectual property](https://research.ontariotechu.ca/faculty/intellectual-property/index.php): consult current policy and applicable agreements if university-related work is involved.

Review this checklist when dependencies, contributors, data collection, distribution models, or legal circumstances change.
