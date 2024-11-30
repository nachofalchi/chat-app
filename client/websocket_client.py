import asyncio
import websockets

class WebSocketClient:
    def __init__(self, url):
        self.url = url
        self.websocket = None

    async def connect(self):
        """Conectar al servidor WebSocket"""
        self.websocket = await websockets.connect(self.url)

    async def send_message(self, message):
        """Enviar un mensaje al servidor"""
        if self.websocket:
            await self.websocket.send(message)

    async def receive_message(self):
        """Recibir un mensaje del servidor"""
        if self.websocket:
            message = await self.websocket.recv()
            return message

    async def close(self):
        """Cerrar la conexión WebSocket"""
        if self.websocket:
            await self.websocket.close()
