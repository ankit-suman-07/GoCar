# Scope and Requirements

**Status:** Planning baseline. Requirements below are targets, not verified capabilities.

## Purpose

Go-Car is a lightweight, extensible vehicle simulator for students and researchers testing sensor interfaces, external controllers, fault handling, and vehicle-software integration. It must run independently of any particular middleware or vendor stack.

## MVP: connected 2D simulation

| Area | Required capability |
|---|---|
| World | Small configurable road scene, static obstacles, and at least one scripted NPC vehicle |
| Ego vehicle | One instrumented vehicle with acceleration, braking, steering, and collision handling |
| Sensors | Front range, speed/odometry, and collision measurements; configurable mounting and sampling where applicable |
| Extensions | Common sensor lifecycle, registration mechanism, and a minimal custom-sensor example |
| Scenarios | File-based initial conditions, scheduled events, sensor-failure injection, pause, step, and reset |
| Integration | Versioned WebSocket telemetry and vehicle commands; a Python example controller |
| Results | Timestamped event logs, basic latency measurements, and automated pass/fail assertions |
| Execution | Interactive and headless operation using the same simulation rules |

The simulator generates measurements and applies commands. External applications own their decision logic. Disabled sensors must perform no normal sampling work.

## Quality requirements

- **Correctness:** explicit units, coordinate conventions, simulation timestamps, and vehicle/sensor IDs; validate incoming commands and reject unknown targets.
- **Repeatability:** fixed simulation steps, recorded configuration and seed, and documented comparison tolerances. Cross-platform equivalence must be tested before being claimed.
- **Efficiency:** instantiate only selected modules; separate sensor, rendering, and telemetry rates; bound queues and log buffering.
- **Accessibility:** document installation and provide one runnable experiment. Publish supported platforms only after verification.
- **Maintainability:** keep sensors, transport, scenarios, and presentation separate; include proportionate automated tests and extension documentation.
- **Provenance:** follow the legal and quality checklist; preserve applicable licences and notices.

## MVP acceptance criteria

1. A configured vehicle moves and a front range sensor reports obstacle distances within a declared tolerance against known geometry.
2. An external Python controller receives measurements and returns a braking command; the addressed vehicle decelerates and stops before collision in the documented braking scenario.
3. Injecting and clearing a sensor failure produces the documented invalid/healthy measurements; the example controller performs its specified response and recovery.
4. A disabled sensor emits no samples and performs no sampling calls. Reset restores the documented initial state.
5. A custom example sensor can be added through the extension mechanism without changing the core loop, vehicle movement, or transport implementation.
6. Headless execution runs the example experiment, exports results, and exits with code 0 on success and non-zero on assertion failure or runtime error.
7. Repeated runs of the same offline reference scenario match within declared tolerances on the tested environment. Live external-loop timing is measured separately.
8. A baseline report records hardware, software versions, configuration, startup time, memory, CPU use, and simulation-step timing. Hardware and performance targets are set from measured evidence.

## Later scope

Multi-ray scanning, GNSS and IMU models; configurable noise and communication faults; batch experiments and record/replay; low-poly 3D with genuine height-aware sensing; multiple instrumented vehicles; optional integration adapters; a scenario editor and browser distribution.

## Boundaries

The initial release excludes photorealistic perception, full physical sensor reproduction, detailed tire/suspension dynamics, large city environments, and safety certification. Simplified geometry can affect sensing and collision outcomes. Results support only the tested model and assumptions; they do not establish real-world vehicle safety.

See [roadmap](roadmap.md), [architecture](architecture.md), [interfaces](interfaces.md), and the [legal and quality checklist](LEGAL_AND_QUALITY_CHECKLIST.md). Supporting documents will be linked as they are added.
