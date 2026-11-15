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
    """Send the demo message and print without a final newline."""
    response = await connect_and_send("ws://127.0.0.1:8765", "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
