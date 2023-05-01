import json

import aiohttp
import uvicorn
from fastapi import FastAPI, WebSocket, Depends, Request, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

from config import settings

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

class Settings(BaseModel):
    authjwt_secret_key: str = settings.authjwt_secret_key

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Authorize</title>
    </head>
    <body>
        <h1>WebSocket Authorize</h1>
        <p>Token:</p>
        <textarea id="token" rows="4" cols="50"></textarea><br><br>
        <button onclick="websocketfun()">Send</button>
        <ul id='messages'>
        </ul>
        <script>
            const websocketfun = () => {
                let token = document.getElementById("token").value
                let ws = new WebSocket(`ws://localhost/ws?token=${token}`)
                ws.onmessage = (event) => {
                    let messages = document.getElementById('messages')
                    let message = document.createElement('li')
                    let content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                }
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket('/ws')
async def websocket(websocket: WebSocket, token: str = Query(...), Authorize: AuthJWT = Depends()):
    await websocket.accept()
    try:
        Authorize.jwt_required("websocket",token=token)
        await websocket.send_text("Successfully Login!")
        while True:
            message = await websocket.receive()
            if message.type == websocket.Text:
                data = json.loads(message.data)
                # отправляем данные на сервер
                async with aiohttp.ClientSession() as session:
                    async with session.post(settings.NOTIFICATION_API_REGISTRATION_EVENT_URL, data=data) as response:
                        response_text = await response.text()
                # отправляем ответ на запрос
                await websocket.send(response_text)
    except AuthJWTException as err:
        await websocket.send_text(err.message)
        await websocket.close()
    finally:
        await session.close()

@app.post('/login')
def login(user: User, Authorize: AuthJWT = Depends()):
    #идет проверка через auth_jwt микросервис, возвращает токен
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401,detail="Bad username or password")

    access_token = Authorize.create_access_token(subject=user.username,fresh=True)
    refresh_token = Authorize.create_refresh_token(subject=user.username)
    return {"access_token": access_token, "refresh_token": refresh_token}


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000
    )