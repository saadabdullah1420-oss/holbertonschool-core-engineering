#!/usr/bin/env python3
"""Validate WebSocket messages while keeping connections open."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Reject empty messages and acknowledge the original valid text."""
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    """Start the validation server on IPv4 port 8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
