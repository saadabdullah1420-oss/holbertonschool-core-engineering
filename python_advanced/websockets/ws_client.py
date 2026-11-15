#!/usr/bin/env python3
"""Send one WebSocket message and receive one response."""

import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Send a message, return the response, and close cleanly."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    """Send the required message and print the server response."""
    response = await connect_and_send(
        "ws://localhost:8765", "Hello WebSocket"
    )
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
