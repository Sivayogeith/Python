import asyncio
import websockets

async def test(mes):
    async with websockets.connect('ws://192.168.43.28:4554') as websocket:
        await websocket.send(mes)
        response = await websocket.recv()
        print(response)

while True:
    asyncio.get_event_loop().run_until_complete(test(input('what to send? ')))
