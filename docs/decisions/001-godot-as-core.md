# ADR-001: Godot + GDScript as the simulation core

**Status:** Accepted
**Date:** 2026-10-25
**Deciders:** Project maintainer
**Phase:** 0b

## Context

GoCar needs a simulation core that can:
- run headlessly for reproducible experiments,
- render optionally (2D now, low-poly 3D later),
- ship as a small, forkable project for students and researchers,
- avoid requiring a separate middleware stack (no mandatory ROS, etc.),
- expose a clean interface for external controllers over WebSocket.

Candidates considered included a from-scratch Python engine, a Unity-based
setup, and a Godot-based setup.

## Decision

Use **Godot 4.x (pinned via `.godot-version`) with GDScript** as the
simulation core, with the world/clock/sensors owned by plain GDScript
nodes/scripts, and rendering implemented as an optional viewer that
consumes simulation state. Headless execution must remain a first-class
run mode.

## Consequences

### Positive
- Single engine covers headless + 2D + future 3D with one toolchain.
- MIT licence matches the project's proposed licence.
- Low barrier for students (free, cross-platform, small download).
- Built-in WebSocket client/server support reduces custom transport work.
- GDScript is approachable; typed GDScript 2.0 is sufficient for a
  lightweight simulator.

### Negative / costs
- Web export has known constraints (threading, WASM size); browser
  feasibility must be verified early (see Phase 0b browser spike).
- Performance ceiling lower than a native C++ engine; benchmarks
  required to keep claims honest.
- Determinism depends on fixed timestep + seeded RNG discipline; the
  engine does not guarantee it for free.

### Neutral / follow-ups
- Pin the version and document it (`.godot-version`, README).
- Browser spike (Phase 0b) decides whether Phase 5 browser is
  committed, descoped, or a stretch goal.

## Alternatives considered

| Option | Why rejected |
|---|---|
| From-scratch Python engine | Would need to re-implement rendering, input, and packaging; slow for students; poor 3D path. |
| Unity + C# | Heavier install, licensing friction for classrooms, overkill for a lightweight 2D-first tool. |
| Custom C++/SDL | Too much low-level work before any experiment is runnable; hostile to forking by students. |

## References

- `README.md` — design principles and roadmap
- `docs/interfaces/sensor-contract.md`
- `docs/interfaces/websocket-schema.md`