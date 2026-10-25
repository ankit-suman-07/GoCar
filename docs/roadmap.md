# Development Roadmap

**Status:** Planned. Phases describe intended work, not completed capabilities. The connected 2D MVP is delivered at the end of Phase 2.

| Phase | Include | Complete when |
|---|---|---|
| **0 — Foundation** | Concise project documents, licence and notices, pinned Godot version, unit/coordinate conventions, repository setup, and initial CI | The project imports and a minimal headless check passes; planning documents establish scope and interfaces |
| **1 — Offline 2D** | One ego vehicle, small road, static obstacles, acceleration/braking/steering, collision handling, front range and speed measurements, pause/step/reset | A local scenario runs; measurements match known geometry within declared tolerances and reset restores initial state |
| **2 — Connected 2D MVP** | Sensor extension contract, configurable sampling, scripted NPC, scenario files, sensor-failure injection, WebSocket telemetry/commands, Python example controller, logs, metrics, and headless assertions | An automated external-controller experiment demonstrates braking, fault response, and recovery; a custom example sensor works without core changes |
| **3 — Research-ready 2D** | Multi-ray scanning, GNSS/IMU models, configurable noise and communication faults, batch runs, record/replay, benchmarks, and extension guides | A documented experiment can be reproduced in the tested environment; reference-output checks and resource measurements are published |
| **4 — Low-poly 3D** | Simple 3D environments and actors, height-aware sensor queries, slopes, collision handling, and optional 3D presentation | Flat-road reference cases agree with 2D within justified tolerances, and height-dependent sensing cases pass |
| **5 — Broader platform** | Multiple instrumented vehicles, richer NPC scenarios, optional adapters, scenario editor, and browser distribution | Supported workflows have examples and tests; multi-vehicle isolation and browser compatibility are verified |

## Rules across phases

- Keep the core independent of any middleware stack; integrations remain optional.
- Separate simulation, sensing, rendering, and communication. Disabled sensors do no normal sampling work.
- Check browser feasibility and vehicle-addressed routing early, before architecture choices make them costly to change.
- Use relevant automated checks and the [legal and quality checklist](LEGAL_AND_QUALITY_CHECKLIST.md) at each checkpoint; run the complete review before public releases.
- Preserve a working example, update documentation, and commit each verified milestone. Label unverified capabilities clearly.
- Measure performance before optimising. Record configurations and limitations; do not trade away required correctness to improve speed.

Later phases are expandable milestones, not prerequisites for using the 2D MVP. Prioritise them using user feedback and demonstrated research needs. Detailed acceptance criteria belong in [scope and requirements](scope-and-requirements.md).
