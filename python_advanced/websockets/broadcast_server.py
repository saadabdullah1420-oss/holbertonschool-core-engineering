#!/usr/bin/env python3
"""Broadcast WebSocket messages to all connected clients."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Track clients and broadcast each message, including to its sender."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients.copy():
                try:
                    await client.send(f"B:{message}")
                except ConnectionClosed:
                    connected_clients.discard(client)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the broadcast server on IPv4 port 8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
