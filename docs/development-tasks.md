# Development Tasks

**Status:** Planned; no checkbox implies completion. This expands the [roadmap](roadmap.md). Phase 2 delivers the connected 2D MVP. Complete each phase's gate before expanding scope, while allowing small feasibility checks for later features.

## Conventions

- **Output directory:** all experiment output goes under `runs/` (gitignored). Each run gets a unique subdirectory named `<run_id>/`, containing config, logs, measurements, commands, and metadata.
- **Contract freeze:** the sensor envelope and WebSocket schema are declared stable at a named version (e.g., `v0.1`) at the Phase 1 gate. Any change after that requires an explicit version bump and a compatibility note.
- **Commit hygiene:** each checkpoint runs relevant checks, inspects the diff, runs `git diff --check`, updates documentation, and commits related changes together.

## Phase 0a — Repository foundation

**Goal:** A clean, documented, testable repo that a fresh checkout can validate.

- [ ] Add the README, scope, roadmap, architecture, interfaces, and contribution guide in their agreed locations.
- [ ] Confirm ownership and add the chosen project licence; inventory existing icons, plugins, and other third-party material.
- [ ] Add AI instructions and the legal/quality checklist; preserve required engine notices.
- [ ] Pin a stable Godot version and initial renderer; document development prerequisites (`.godot-version` already added — reference it from README).
- [ ] Extend `.gitignore` to cover generated caches, build outputs, local credentials, and the `runs/` experiment-output directory; retain reproducible configuration.
- [ ] Establish the `runs/` output convention and document it in the contribution guide.
- [ ] Create initial folders for core logic, worlds/vehicles, sensors, scenarios, connections, UI, tests, and examples only as needed.
- [ ] Add a minimal headless test entry point and CI import/parse/smoke checks.
- [ ] Add a minimal Python script (`examples/python/probe.py`) that connects to a not-yet-implemented WebSocket endpoint, receives one `state` message, sends one `command`, and prints the `ack` — used later to validate the schema end-to-end.

**Gate:** A fresh checkout imports successfully on the documented development environment, the automated smoke check passes, CI is green, and foundational conventions (output dir, commit hygiene, version pin) are recorded. **Commit a foundation checkpoint and tag it.**

## Phase 0b — Architectural decisions

**Goal:** Settle the decisions that, if changed later, would ripple through every phase.

- [ ] Finalise SI units, canonical coordinates, mounting transforms, actor IDs, run IDs, frame numbering, and reset semantics.
- [ ] Define the fixed-step lifecycle and establish initial versioned scenario/message schemas (draft v0.1).
- [ ] Resolve command ordering, stale-command policy, controller ownership, watchdog behaviour, and error reporting before implementing networking.
- [ ] Decide the vehicle-collection architecture: world state holds a collection of vehicles even when length = 1, with per-vehicle IDs threaded through sensors, commands, and telemetry. Document the decision.
- [ ] Run a tiny browser-export feasibility check, including an outbound WebSocket connection; record limitations without promising browser support.
- [ ] Test an identity/routing stub with two vehicle IDs against the collection architecture; full multi-vehicle simulation remains later work.

**Gate:** Architectural decisions are recorded (in `docs/decisions/`), the vehicle-collection decision is documented, and the browser spike produces a written finding. **Decision point:** based on the browser spike, either (a) keep Phase 5 browser distribution as planned, (b) descope it to a documented stretch goal, or (c) commit to it with adjusted acceptance criteria. Record the decision. **Commit a decisions checkpoint.**

## Phase 1 — Offline 2D simulation

**Goal:** Demonstrate trustworthy movement and measurements without networking.

- [ ] Implement the simulation clock, fixed step, frame counter, and initial-state snapshot.
- [ ] Implement pause, one-step advancement, reset, and a new run ID after reset.
- [ ] Create a small straight-road scene with known dimensions and configurable static obstacles.
- [ ] Implement one vehicle's pose, dimensions, speed, acceleration, throttle, brake, and steering.
- [ ] Choose and document a simple kinematic motion model, limits, and integration method.
- [ ] Implement collision detection and events identifying involved actors; document collision response.
- [ ] Define a small sensor base interface now, avoiding tightly coupled one-off sensor code.
- [ ] Implement front range sensing, mounting transforms, self-exclusion, maximum range, and explicit no-detection results.
- [ ] Implement speed/odometry and collision measurements using documented units.
- [ ] Schedule sensors independently of display updates; support enable/disable and reset.
- [ ] Add a minimal viewer showing actor IDs, speed, distance, sensor status, and collision state.
- [ ] Keep keyboard/demo control separate from vehicle dynamics and identify it as a local controller.
- [ ] Verify known-distance cases, coordinate conversion, steering direction, speed limits, braking, collisions, sensor scheduling, and reset.
- [ ] Repeat an offline reference run and record tolerances; compare rendered and headless state where supported.
- [ ] **Freeze the sensor envelope and scenario schema at v0.1**: review the contracts drafted in 0b against real sensor output, declare them stable, and note that any future change requires a version bump.

**Gate:** One offline scenario produces verified measurements and repeatable motion in the tested environment. Pause/step/reset work, and rendering does not determine simulation time. The sensor envelope and scenario schema are frozen at v0.1. **Commit a working example and tag the contract freeze.**

## Phase 2 — Connected 2D MVP

**Goal:** Complete a configurable sensor-to-controller-to-vehicle experiment.

### Configuration and extensions

- [ ] Implement validated scenario loading: world, initial actors, sensors, seed, timestep, duration, and events.
- [ ] Reject duplicate IDs, invalid values, unavailable sensor types, and unsupported schema versions before starting.
- [ ] Complete sensor registration, configuration, lifecycle, and payload contracts.
- [ ] Implement runtime enable/disable with logged lifecycle changes; sampling must stop while disabled.
- [ ] Add a custom example sensor and prove it needs no core-loop, movement, or transport changes.
- [ ] Add one scripted NPC with reproducible movement, slowing/stopping, and valid collision geometry.
- [ ] Implement scheduled sensor failure and clearing; reset must clear faults and pending events.

### External control

- [ ] Implement the native WebSocket server with configurable address/port and local-only binding by default.
- [ ] Publish versioned sensor envelopes and JSON schemas with IDs, frames, sequences, validity, and units (frozen at v0.1 from Phase 1).
- [ ] Implement controller assignment, command validation, bounded queues, and accepted/rejected acknowledgements.
- [ ] Apply commands only at simulation boundaries and report application frames separately from acceptance.
- [ ] Implement duplicate/out-of-order/stale/wrong-run rejection and reset queue invalidation.
- [ ] Implement documented disconnect, timeout, pause/resume, and watchdog policies; test stale-throttle handling.
- [ ] Add minimal scenario-control messages without mixing them with vehicle actuator commands.
- [ ] Provide a Python example client/controller (extend the Phase 0a probe), dependency instructions, and reconnect/error handling.

### Results and verification

- [ ] Export run configuration, sensor/events, received/applied commands, outcomes, and timing metadata to files under `runs/<run_id>/`.
- [ ] Add headless arguments for scenario, seed, duration, and output; avoid conflicts with engine arguments.
- [ ] Return meaningful success/failure exit codes and flush output on completion or failure.
- [ ] Automate clear-road travel, obstacle braking, failure response, and recovery scenarios.
- [ ] Test malformed messages, unknown targets, oversized input, overload, and controller disconnect.
- [ ] Add an observable connection/status panel and useful validation errors.
- [ ] Record initial CPU, memory, startup, and step-timing baselines with hardware and configuration.
- [ ] Publish one exact quick-start procedure; update CI and run the full pre-release review.

**Gate:** A fresh-checkout user can run the documented external-controller experiment interactively and headlessly, inspect its results, and add the example sensor. All MVP acceptance criteria are evidenced. **Tag the first MVP release.**

## Phase 3a — Sensor realism (2D)

**Goal:** Add richer sensor models without expanding experiment infrastructure.

- [ ] Add a configurable multi-ray scanner: angular coverage, ray count, range, mounting, and output format.
- [ ] Add GNSS and IMU models with documented derivation, reference frames, and simplifications.
- [ ] Add seeded noise/bias and supported drift/dropout models with boundary tests.
- [ ] Add curves and intersections to the 2D world.
- [ ] Verify new sensors against known-value cases and record tolerances.

**Gate:** Multi-ray, GNSS, and IMU sensors produce measurements that match documented reference values within recorded tolerances. **Commit and document model assumptions.**

## Phase 3b — Experiment infrastructure (2D)

**Goal:** Support extensible, measurable experiments with reproducible evidence.

- [ ] Add controlled delay, loss, and reordering at an explicit communication boundary; distinguish injected from accidental loss.
- [ ] Add reusable following, crossing, sudden-obstacle, and cut-in scenarios on the Phase 3a world.
- [ ] Add configurable scenario assertions for transitions, collisions, stopping, timing, and recovery.
- [ ] Implement batch execution, parameter sweeps, unique output directories under `runs/`, and failure summaries.
- [ ] Separate recorded-data playback from re-simulation using recorded commands; document replay guarantees.
- [ ] Record command application frames, versions, configuration, seeds, and checksums needed for comparisons.
- [ ] Report latency distributions and resource measurements across repeated runs, with declared clock assumptions.
- [ ] Benchmark actor count, sensor count, ray count, and sampling frequency; report deadline misses and logging overhead.
- [ ] Profile measured bottlenecks and verify optimisations against reference outputs.
- [ ] Add golden/reference scenario regression checks and a bounded long-run memory test.
- [ ] Publish sensor/adapter templates and complete "add a sensor" and "run an experiment" guides.
- [ ] Ask a fresh-checkout tester to reproduce an experiment and record setup problems.

**Gate:** Another person can reproduce the published reference experiment within documented tolerances and extend a sensor using the guide. **Publish measured limits, known failures, and model assumptions.**

## Phase 4 — Low-poly 3D

**Goal:** Add real 3D geometry and sensing while retaining a small default workload.

- [ ] Define shared state/configuration boundaries and distinct 2D/3D world-query implementations.
- [ ] Build a small low-poly road world with configurable dimensions, slopes, and height-dependent obstacles.
- [ ] Add simple vehicles, buildings, and pedestrian representations with reviewed asset provenance.
- [ ] Implement/document the 3D motion model, ground contact, and slope behaviour; avoid implying detailed dynamics.
- [ ] Implement 3D collision handling and sensor mounting transforms using canonical coordinates.
- [ ] Add 3D range/scanner implementations and explicit world occlusion; do not treat this as merely a viewer change.
- [ ] Separate visual meshes from sensor/collision geometry where useful, preserving scenario-relevant shapes.
- [ ] Add an optional viewer with labels and sensor overlays; keep decorative effects off by default.
- [ ] Support 3D headless scenarios without constructing unnecessary viewer elements.
- [ ] Verify flat-road 2D/3D cases within justified tolerances and test overhead obstacles, slopes, and vertical occlusion separately.
- [ ] Benchmark rendered/headless 3D and document additional hardware requirements.
- [ ] Update extension instructions for dimension-specific sensor capabilities.

**Gate:** Reference flat-road comparisons and genuine height-dependent tests pass; the 2D workflow remains usable and 3D resource costs are documented.

## Phase 5 — Broader platform

**Goal:** Expand supported workflows based on user demand. Deliver these as separate milestones rather than one large release.

### Multiple instrumented vehicles

- [ ] Spawn/remove vehicles with independent controllers, sensors, faults, and state (architecture already committed in Phase 0b and threaded through Phases 1–3).
- [ ] Route telemetry, commands, and scenario actions by run/vehicle/sensor identity.
- [ ] Test targeted faults and commands, lifecycle cleanup, reset, and cross-vehicle isolation.
- [ ] Add interactions between ego vehicles and NPCs; measure sustainable scale.

### Optional integrations and usability

- [ ] Prioritise adapters from actual user needs; implement each with examples, licence checks, and integration tests.
- [ ] Add capability discovery so clients can inspect available actors, sensors, commands, and schema versions.
- [ ] Extend NPC behaviours and traffic rules with explicit assumptions and deterministic scenario options.
- [ ] Build a minimal scenario editor that saves the same validated format used by headless runs.
- [ ] Keep imported scenarios/configuration as data; require explicit trust for third-party executable plugins.

### Browser and distribution

- [ ] Implement outbound browser WebSocket transport using an external endpoint; retain native server mode.
- [ ] Test browser security requirements, connection failures, resource limits, and tab/background timing behaviour.
- [ ] Provide browser-compatible configuration import and results download; document unsupported workflows.
- [ ] Compare browser/native outputs within declared tolerances; do not promise equivalent real-time timing.
- [ ] Publish tested platform support, versioned releases, required notices, migration notes, and compatibility policies.

**Gate:** Each advertised workflow has a working example and verification evidence. Required adapters remain optional, and fresh users can run the base simulator independently.

## Checkpoint rules

- Complete tasks in small vertical slices; preserve the last working example.
- At each meaningful checkpoint: run relevant checks, inspect the diff, run `git diff --check`, update documentation, and commit related changes together.
- Link completion claims to tests, logs, or a reproducible manual procedure. Record skipped checks and limitations.
- Use the full legal/quality review before public releases. Reassess later-phase priorities without silently expanding the MVP.
- Respect the v0.1 contract freeze from Phase 1: any change to the sensor envelope or WebSocket schema after the freeze requires an explicit version bump and a compatibility note in the changelog.