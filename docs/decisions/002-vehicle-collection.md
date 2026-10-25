# ADR-002: World state holds a collection of vehicles from day one

**Status:** Accepted
**Date:** 2026-10-25
**Deciders:** Project maintainer
**Phase:** 0b

## Context

The MVP (Phase 2) features exactly one instrumented ego vehicle, plus a
scripted NPC in Phase 2 and richer NPC interactions later. Full
multi-vehicle experiments are a Phase 5 milestone. The naive design is
to model "the vehicle" as a singleton in world state and introduce a
collection later.

That approach has a known failure mode: sensor IDs, command routing,
telemetry envelopes, reset semantics, and the WebSocket schema all end
up implicitly assuming one vehicle. Refactoring them in Phase 5 ripples
through the sensor contract, the message schema, the Python client, and
every recorded experiment.

## Decision

World state holds a **collection of vehicles** from Phase 1 onward, even
when the collection length is 1. Every vehicle has a stable `vehicle_id`
threaded through:
- sensor measurement envelopes (`owner_id`),
- command routing (`payload.vehicle_id`),
- telemetry (`payload.vehicle_id`, per-vehicle state entries),
- scenario definitions and reset semantics,
- run metadata and logs.

The MVP still runs one ego vehicle; the collection is an architectural
commitment, not a feature commitment.

## Consequences

### Positive
- Phase 5 multi-vehicle becomes additive rather than a rewrite.
- Schema and contract are stable across the MVP → multi-vehicle
  transition; no v0.2 breaking change forced by vehicle count.
- Forces per-vehicle IDs into logs and experiments early, improving
  observability and reproducibility.
- NPCs can be modeled as (non-instrumented) vehicles from the start,
  unifying collision and sensing code paths.

### Negative / costs
- Slightly more verbose code in Phase 1–2 (iteration over a list,
  per-vehicle lookup) than a singleton would require.
- Requires discipline: no API may assume "the vehicle"; reviewers must
  catch accidental singleton assumptions.
- Slight overhead in the single-vehicle case (negligible at MVP scale).

### Neutral / follow-ups
- Sensor contract and WebSocket schema already include `owner_id` /
  `vehicle_id`; keep them mandatory, never optional.
- Phase 0b identity/routing stub with two vehicle IDs validates the
  collection plumbing before Phase 1 implements motion.
- Phase 5 tasks build on this; no schema change expected.

## Alternatives considered

| Option | Why rejected |
|---|---|
| Singleton vehicle, collection introduced in Phase 5 | Forces a late, cross-cutting refactor of contracts, schemas, clients, and recorded experiments. |
| Collection only for instrumented vehicles, NPCs separate | Splits collision/sensing code paths; duplicates logic; makes NPC instrumentation awkward later. |
| Collection with optional vehicle_id | Erodes the contract; clients could omit IDs and silently break multi-vehicle routing. |

## References

- `docs/interfaces/sensor-contract.md` — `owner_id` field
- `docs/interfaces/websocket-schema.md` — `vehicle_id` routing
- `development-tasks.md` — Phase 0b decision task, Phase 1 implementation