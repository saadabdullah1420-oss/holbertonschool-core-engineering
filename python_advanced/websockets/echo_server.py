#!/usr/bin/env python3
"""Run a WebSocket server that echoes received messages."""

import asyncio
import websockets


async def connection_handler(websocket):
    """Echo each message while keeping the connection open."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the server on IPv4 port 8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
