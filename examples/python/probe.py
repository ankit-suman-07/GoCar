#!/usr/bin/env python3
"""
GoCar Python probe.

Minimal client that connects to the GoCar WebSocket endpoint, receives one
`state` message, sends one `command`, and prints the `ack`/`error` reply.

This is a schema-validation stub for Phase 0a. Until the simulator's
WebSocket server exists (Phase 2), running it will fail to connect —
that is expected and useful (it proves the client-side contract shape).

Usage:
    python probe.py [--url ws://127.0.0.1:9090/sim] [--vehicle ego_0] [--timeout 5]

Requirements:
    pip install websockets>=12
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import uuid
from typing import Any

try:
    import websockets
except ImportError:  # pragma: no cover
    print(
        "error: the 'websockets' package is required.\n"
        "       install it with: pip install websockets>=12",
        file=sys.stderr,
    )
    sys.exit(2)

SCHEMA_VERSION = "0.1"


def envelope(
    msg_type: str,
    payload: dict[str, Any],
    *,
    correlation_id: str | None = None,
    step: int = 0,
    sim_time_s: float = 0.0,
) -> dict[str, Any]:
    """Build a message conforming to docs/interfaces/websocket-schema.md."""
    return {
        "schema_version": SCHEMA_VERSION,
        "msg_type": msg_type,
        "msg_id": str(uuid.uuid4()),
        "correlation_id": correlation_id,
        "sim_time_s": sim_time_s,
        "step": step,
        "payload": payload,
    }


async def run(url: str, vehicle_id: str, timeout: float) -> int:
    print(f"connecting to {url} ...")
    try:
        async with websockets.connect(url, open_timeout=timeout) as ws:
            # 1. Wait for one 'state' message.
            state_msg = await asyncio.wait_for(
                _recv_until(ws, "state"), timeout=timeout
            )
            if state_msg is None:
                print("error: no 'state' message received", file=sys.stderr)
                return 1
            vehicles = state_msg.get("payload", {}).get("vehicles", [])
            print(f"received state: {len(vehicles)} vehicle(s)")
            for v in vehicles:
                print(f"  - {v.get('id')}: speed={v.get('speed_mps')} m/s")

            # 2. Send one zero command with a short TTL.
            cmd_id = f"cmd-{uuid.uuid4().hex[:8]}"
            command = envelope(
                "command",
                {
                    "vehicle_id": vehicle_id,
                    "accel_mps2": 0.0,
                    "brake": 0.0,
                    "steer_rad": 0.0,
                    "ttl_ms": 200,
                },
                correlation_id=cmd_id,
                step=state_msg.get("step", 0),
                sim_time_s=state_msg.get("sim_time_s", 0.0),
            )
            await ws.send(json.dumps(command))
            print(f"sent command {cmd_id} for vehicle '{vehicle_id}'")

            # 3. Wait for the ack/error tied to that command.
            reply = await asyncio.wait_for(
                _recv_until(ws, "ack", correlation_id=cmd_id, alt_type="error"),
                timeout=timeout,
            )
            if reply is None:
                print("error: no ack/error received", file=sys.stderr)
                return 1
            if reply["msg_type"] == "error":
                print(f"error reply: {reply['payload']}", file=sys.stderr)
                return 1
            print(f"ack received: {reply['payload']}")
            return 0
    except (OSError, asyncio.TimeoutError, websockets.WebSocketException) as exc:
        # Expected until Phase 2 implements the server.
        print(f"probe could not complete: {exc}", file=sys.stderr)
        print(
            "note: the simulator's WebSocket server is not implemented yet "
            "(planned for Phase 2). This probe validates the client-side "
            "contract shape in the meantime.",
            file=sys.stderr,
        )
        return 1


async def _recv_until(
    ws: Any,
    want_type: str,
    *,
    correlation_id: str | None = None,
    alt_type: str | None = None,
    max_messages: int = 100,
) -> dict[str, Any] | None:
    """Read messages until one matches want_type (or alt_type), or give up."""
    for _ in range(max_messages):
        raw = await ws.recv()
        try:
            msg = json.loads(raw)
        except json.JSONDecodeError:
            print(f"warning: non-JSON frame ignored: {raw!r}", file=sys.stderr)
            continue
        mtype = msg.get("msg_type")
        if mtype == want_type or (alt_type and mtype == alt_type):
            if correlation_id is not None and msg.get("correlation_id") != correlation_id:
                continue
            return msg
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="GoCar WebSocket probe")
    parser.add_argument("--url", default="ws://127.0.0.1:9090/sim")
    parser.add_argument("--vehicle", default="ego_0")
    parser.add_argument("--timeout", type=float, default=5.0)
    args = parser.parse_args()
    try:
        return asyncio.run(run(args.url, args.vehicle, args.timeout))
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())