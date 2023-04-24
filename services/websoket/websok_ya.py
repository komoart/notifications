import asyncio

import websockets


peoples = {}


async def welcome(websoket: websockets.WebSocketServerProtocol) -> str:
    await websoket.send('Представьтесь!')
    name = await websoket.recv()
    await websoket.send('Чтобы поговорить, напишите "<имя>: <сообщение>". Например: Ира: купи хлеб.')
    await websoket.send('Посмотреть список участников можно командой "?"')
    await websoket.send('Для добавления пользователя в блок лист воспользуйтесь командой "!"')
    peoples[name.strip()] = [websoket, []]
    return name


async def receiver(websoket: websockets.WebSocketServerProtocol, path: str) -> None:
    MAX_MESSAGE = 5
    MESSAGE_INTERVAL = 2
    
    message_count = 0
    name  = await welcome(websoket)

    try:
        while True:

            message = (await websoket.recv()).strip()
            message_count += 1

            def decrease_message_count():
                nonlocal message_count
                message_count -= 1

            if message_count > MAX_MESSAGE:
                await websoket.send('Слишком много сообщений')
                continue
            else:
                loop.call_later(MESSAGE_INTERVAL, decrease_message_count) 

            if message == '?':
                await websoket.send(', '.join(peoples.keys()))
                continue

            if message == '!':
                await websoket.send('Укажите имя для добавления в блок лист')
                block_user = await websoket.recv()
                peoples[name.strip()][1].append(block_user.strip())
                continue

            if ':' not in message:
                await websoket.send('Неверный формат сообщения')
                await websoket.send('Чтобы поговорить, напишите "<имя>: <сообщение>". Например: Ира: купи хлеб.')
                await websoket.send('Посмотреть список участников можно командой "?"')
                continue

            to, text = message.split(':', 1)
            if (to in peoples) and (name.strip() not in peoples[to][1]):
                await peoples[to][0].send(f'Сообщение от {name}: {text}')
            elif name.strip() in peoples[to][1]:
                await websoket.send(f'Пользователь {to} вас заблокировал')
            else:
                await websoket.send(f'Пользователь {to} не зарегистрирован')
                
    except websockets.ConnectionClosed:
        del peoples[name.strip()]


ws_server = websockets.serve(receiver, 'localhost', 8765)

loop = asyncio.get_event_loop()
loop.run_until_complete(ws_server)
loop.run_forever() 
