# Contributing to Go-Car

Go-Car is in planning and initial setup. Contributions to documentation, implementation, tests, and examples are welcome. Discuss substantial features or architectural changes in an issue before implementing them.

## Before you start

1. Read the [README](README.md), [scope](docs/scope-and-requirements.md), and [architecture](docs/architecture.md).
2. Read [AGENTS.md](AGENTS.md) and apply the relevant parts of the [legal and quality checklist](docs/LEGAL_AND_QUALITY_CHECKLIST.md).
3. Check the repository's `LICENSE` and any applicable third-party terms. Submit only work you have permission to contribute under the project's licence; clarify unclear ownership or terms before submission.

## Development workflow

- Fork and clone the repository, then create a focused branch such as `feat/front-range-sensor`, `fix/scenario-reset`, or `docs/setup-guide`.
- Use the Godot version pinned by the project once available. Import `project.godot`; runnable scenarios and exact test commands will be documented as implemented.
- Keep changes small and related. Follow existing naming and formatting; avoid unrelated rewrites or new dependencies without a clear need.
- Keep the core independent of external middleware. Make integrations optional and follow the [interface contracts](docs/interfaces.md).
- Update relevant documentation and examples when behaviour or configuration changes. Clearly distinguish planned, implemented, and verified capabilities.

## Verification

Run the documented checks relevant to your change and `git diff --check`. For behavioural changes, add or update tests that verify meaningful outcomes. Check headless operation when changing simulation logic and interactive behaviour when changing the viewer.

Sensor contributions should include configuration/output definitions, a minimal scenario, and checks for sampling, reset, disabled behaviour, and vehicle identity. Optimisations should include measurements and reference-output comparisons within documented tolerances.

Do not claim checks passed if they were not run. State unavailable tooling, skipped checks, and remaining limitations.

## Pull requests

Explain:

- What problem the change solves and the resulting behaviour.
- How it was verified, with relevant results.
- Any new dependencies, third-party material, compatibility changes, or limitations.

Use clear commit messages such as `feat: add front range sensor` or `docs: clarify scenario configuration`. Keep discussion respectful and address review feedback before merging.

## Rights and responsible reporting

Preserve required licences, attribution, and notices. Identify adapted or third-party material and its source; review AI-assisted output to the same standard as other contributions. Never commit credentials, personal data, or confidential material.

For suspected vulnerabilities or exposed secrets, avoid posting exploit details or sensitive values in public issues. Use the private reporting route in `SECURITY.md` or the repository's Security tab when available. If neither exists, request a private contact without disclosing details.
