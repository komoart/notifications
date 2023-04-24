import asyncio

import websockets


peoples = {}


async def welcome(websoket: websockets.WebSocketServerProtocol) -> str:
    await websoket.send('Представьтесь!')
    name = await websoket.recv()
    await websoket.send('Чтобы поговорить, напишите "<имя>: <сообщение>". Например: Ира: купи хлеб.')
    await websoket.send('Посмотреть список участников можно командой "?"')
    peoples[name.strip()] = websoket
    return name


async def receiver(websoket: websockets.WebSocketServerProtocol, path: str) -> None:
    name  = await welcome(websoket)
    try:
        while True:
            message = (await websoket.recv()).strip()
            if message == '?':
                await websoket.send(', '.join(peoples.keys()))
                continue
            if ':' not in message:
                await websoket.send('Неверный формат сообщения')
                await websoket.send('Чтобы поговорить, напишите "<имя>: <сообщение>". Например: Ира: купи хлеб.')
                await websoket.send('Посмотреть список участников можно командой "?"')
                continue
            to, text = message.split(':', 1)
            if to in peoples:
                await peoples[to].send(f'Сообщение от {name}: {text}')
            else:
                await websoket.send(f'Пользователь {to} не зарегистрирован')
    except websockets.ConnectionClosed:
        del peoples[name]


ws_server = websockets.serve(receiver, 'localhost', 8765)

loop = asyncio.get_event_loop()
loop.run_until_complete(ws_server)
loop.run_forever() 