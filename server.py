import asyncio

import websockets

# create handler for each connection

async def handler(websocket, path):
    data = await websocket.recv()
    print(f"Data recieved as:  {data}!")

    await websocket.send(input("reply: "))



start_server = websockets.serve(handler, "localhost", 4554)


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()