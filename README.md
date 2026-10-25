# Go-Car

A lightweight, extensible vehicle simulator with modular sensors for student and research projects.

> **Status: planning and initial project setup.** The capabilities below describe the intended product. A working simulator, performance benchmarks, and platform compatibility have not yet been verified.

## Purpose

Go-Car aims to make vehicle-software experiments accessible on everyday computers. Users will configure vehicles, attach simulated sensors, introduce obstacles or faults, connect an external application, and inspect the resulting behaviour and measurements.

The project is intended for students, researchers, and developers exploring sensor interfaces, software-defined vehicle (SDV) integration, basic planning and control, and fault handling. It is being developed as a standalone Godot project that others can fork and extend.

## Design principles

- **Lightweight by design:** small environments, simple visuals, configurable workloads, and optional components. Resource savings will be measured rather than assumed.
- **Independent integration:** no required vehicle middleware or vendor stack. External applications connect through documented interfaces or optional adapters.
- **Extensible sensors:** built-in and custom sensors follow a common lifecycle and output contract.
- **Observable experiments:** explicit units, timestamps, vehicle identities, event logs, and test outcomes.
- **Repeatable execution:** fixed simulation steps, recorded configuration, seeded randomness, and documented tolerances.
- **Optional rendering:** separate simulation logic from presentation so experiments can also run headlessly.

## Planned MVP

The first MVP will provide a complete 2D experiment with:

- One instrumented ego vehicle with basic acceleration, braking, steering, and collisions.
- Simple roads, obstacles, and lightweight scripted NPC traffic.
- Front range sensing, speed/odometry, and collision measurements.
- Configurable sensor sampling and a documented interface for adding sensors.
- Scenario files, pause, step, reset, and sensor-failure injection.
- Bidirectional WebSocket telemetry and vehicle commands, with a Python example controller.
- Headless execution, event logs, basic metrics, and automated scenario assertions.

An example milestone is an external controller receiving obstacle measurements, returning a braking command, and producing a recorded pass/fail result. The simulator generates measurements and applies commands; the connected application owns its decision logic.

## Development roadmap

| Phase | Focus | Intended outcome |
|---|---|---|
| 0 | Foundation | Documentation, conventions, project setup, and initial automated checks |
| 1 | Offline 2D simulation | Vehicle movement, obstacles, range sensing, and local controls |
| 2 | Connected 2D MVP | External controller, faults, logs, and an automated end-to-end experiment |
| 3 | Research-ready 2D | More sensor models, experiment automation, replay, benchmarks, and extension guides |
| 4 | Low-poly 3D | Height-aware geometry, sensing, collisions, and a simple 3D viewer |
| 5 | Broader platform | Multiple instrumented vehicles, optional adapters, richer scenarios, and browser distribution |

Browser feasibility and multi-vehicle routing should be checked early. Full browser delivery and multi-vehicle experiments remain later milestones. Genuine 3D sensing requires additional world and sensor implementations, beyond changing the viewer.

## Planned structure and technology

The core will own the clock, world state, vehicles, and component scheduling. Sensor modules will measure that state. Scenarios will define initial conditions and events. A connection layer will exchange measurements and commands, while the viewer and results recorder observe the simulation.

Godot and GDScript are the proposed core tools. JSON will describe scenarios and message contracts. Python will support an optional client SDK and experiment tooling. Additional integrations will remain optional; standalone experiments should not require a separate middleware stack or database server.

## Getting started

Implementation instructions are pending. At this stage, start with the project scope and roadmap below. A pinned Godot version, supported-platform matrix, runnable example, and exact launch commands will be published as they are verified. Opening the initial Godot project does not yet imply that an experiment is available.

## Documentation

The following is the intended documentation set. Links to planning documents may become available as those files are added.

| Document | What to read it for |
|---|---|
| [Scope and requirements](docs/scope-and-requirements.md) | Features, exclusions, and acceptance criteria |
| [Roadmap](docs/roadmap.md) | Detailed phase deliverables and milestones |
| [Architecture](docs/architecture.md) | Module boundaries and data flow |
| [Interfaces](docs/interfaces.md) | Sensor extension and external communication contracts |
| [Contributing](CONTRIBUTING.md) | Development setup, testing, and contribution workflow |
| [AI instructions](AGENTS.md) | Repository guidance for coding assistants |
| [Legal and quality checklist](docs/LEGAL_AND_QUALITY_CHECKLIST.md) | Provenance, licensing, security, and correctness reviews |
| [Third-party notices](THIRD_PARTY_NOTICES.md) | Applicable dependency and asset notices |

## Extending Go-Car

The intended workflow for a new sensor is to implement the common sensor contract, define its configuration and measurements, register the module, and add a small scenario with tests. Core movement, networking, and the simulation loop should not need modification for a typical sensor extension. Templates and a worked example are planned.

## Model limitations

Go-Car will use simplified geometry and vehicle/sensor models. It will initially target software interfaces and controlled behaviour, without photorealistic perception, detailed vehicle dynamics, or physically validated sensor reproduction. Any supported research claim must match the model and its validation evidence. Simulation results do not establish real-world vehicle safety or certification. Cross-platform determinism and performance targets remain to be measured.

## Licence and acknowledgements

The proposed project licence is MIT. The repository's `LICENSE` file, once added, will provide the actual terms; this README does not grant a substitute licence. Third-party components retain their own terms and required notices.

Go-Car is being developed with [Godot Engine](https://godotengine.org/). See [Godot's licence information](https://godotengine.org/license/) for the engine's MIT licence and third-party notices.
