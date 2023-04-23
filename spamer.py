import asyncio
import websockets

uri = "ws://localhost:8765"

async def spammer(users_name: list) -> None:
    # Используйте менеджер контекста, чтобы соединение автоматически закрылось при выходе из блока
    async with websockets.connect(uri) as websocket:
        await websocket.recv()
        await websocket.send('Продам гараж')
        await websocket.recv()
        await websocket.recv()
        while True:
            for user_name in users_name:
                for _ in range(10):
                    await websocket.send(f'{user_name}: продам гараж')
                await asyncio.sleep(10)

loop = asyncio.get_event_loop()
loop.run_until_complete(spammer(['Алексей'])) 