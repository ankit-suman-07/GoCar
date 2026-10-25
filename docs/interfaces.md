# Interfaces

**Status:** Proposed v0.1 contract. Names and examples are design targets, not an implemented API. Version incompatible changes explicitly.

## Shared conventions

| Item | Convention |
|---|---|
| Units | Metres, seconds, radians, m/s, and m/s²; name units in measurement fields |
| Coordinates | Canonical right-handed frame: X forward, Y left, Z up; heading is counterclockwise from +X about +Z. 2D uses Z = 0. Convert Godot coordinates at the boundary |
| Mounting | Sensor position and orientation are relative to the parent vehicle frame |
| Identity | Unique vehicle IDs per world; unique sensor IDs per vehicle; a new run ID on reset |
| Time | Frame 0 is initial state; integer frames and simulation time identify causality. Monotonic local clocks measure durations; wall clocks alone do not establish latency across machines |
| Validity | Distinguish valid data, no detection, failure, and disabled state. Do not encode failure as zero distance |

## Sensor extension contract

Each sensor module implements the following conceptual operations:

| Operation | Responsibility |
|---|---|
| `configure(config)` | Validate IDs, mounting, sampling frequency, and sensor-specific settings |
| `sample(context)` | Read documented vehicle/world queries and return a measurement when scheduled |
| `set_fault(fault)` | Apply a supported fault; reject unknown fault types |
| `reset(seed)` | Restore initial configuration, counters, and seeded noise state |
| `set_enabled(enabled)` | Suspend/resume sampling; disabled sensors produce no measurements |

Register modules by sensor type. The scheduler owns sampling times; sensors do not advance the clock or modify vehicle motion. Samples identify their vehicle, sensor, frame, and sequence. Document each sensor's payload, units, valid ranges, and limitations. A new module must include a small example and relevant verification tests.

## External connection

The native MVP will expose a WebSocket server for external clients. No middleware is required. An optional browser build will act as a WebSocket client to a separately running relay/controller endpoint; browsers cannot host this server interface. Both use the same message contracts. Exact addresses and port configuration will be documented with implementation.

### Example measurement

```json
{
  "schemaVersion": "0.1",
  "type": "sensor.sample",
  "runId": "run-001",
  "vehicleId": "vehicle-001",
  "sensorId": "front-range",
  "frame": 120,
  "simulationTimeSeconds": 2.0,
  "sequence": 20,
  "status": "valid",
  "data": {"distanceMeters": 8.2}
}
```

For this range model, `status` is `valid`, `no_detection`, or `failed`. The latter two use `distanceMeters: null`; the configured maximum range remains available in sensor configuration. Disabled sensors emit no samples; lifecycle events record enable/disable changes. Other sensors define their own payloads without changing the envelope.

### Example control command

```json
{
  "schemaVersion": "0.1",
  "type": "vehicle.control",
  "runId": "run-001",
  "commandId": "cmd-001",
  "vehicleId": "vehicle-001",
  "sourceFrame": 120,
  "throttle": 0.0,
  "brake": 1.0,
  "steeringRadians": 0.0
}
```

Throttle and brake range from 0 to 1. Positive steering turns left; vehicle configuration defines steering limits. Commands set actuator inputs, not instantaneous speed. Scenario start/pause/step/reset controls are separate from vehicle commands; their message definitions will be added before implementation.

## Routing, timing, and errors

- Validate schema version, message type, IDs, finite numbers, ranges, and configured size/rate limits. Never execute code supplied in messages.
- Accept commands only from the assigned controller for that vehicle. Reject wrong-run, duplicate, out-of-order, and stale commands using documented sequence/frame policies; final thresholds belong in configuration.
- Queue accepted commands and apply them at the next simulation boundary. Return an acknowledgement with command ID, accepted/rejected status, and error code; report the actual application frame separately. Acceptance is not proof of application.
- Hold the latest applied inputs until replaced or the configured watchdog expires. Timeout, pause/resume, and disconnect behaviour must be explicitly configured, tested, and logged; do not silently resume stale throttle.
- Bound queues and report drops/overflow. Log command receipt/application and measurement sequences for traceability. Cross-machine latency requires a documented clock strategy.

Publish machine-readable JSON schemas and exact error codes alongside implementation. See [architecture](architecture.md) and [scope and requirements](scope-and-requirements.md).
