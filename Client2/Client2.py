import asyncio
import websockets

async def hello():
    uri = "ws://25.20.18.47:8080"
    async with websockets.connect(uri) as websocket:
        await websocket.send("0")
        mes = input()
        await websocket.send(mes)
        await websocket.recv()

asyncio.get_event_loop().run_until_complete(hello())
