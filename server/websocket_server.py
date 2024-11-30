# websockets.py

from fastapi import WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from typing import Dict

router = APIRouter()

# Diccionario para almacenar las conexiones WebSocket por user_id
active_connections: Dict[str, WebSocket] = {}

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    # Aceptar la conexión WebSocket
    await websocket.accept()

    # Verificar si el user_id es válido (esto depende de cómo gestionas tus usuarios)
    # Por ejemplo, hacer una consulta a la base de datos para validar el usuario.
    if not await validate_user(user_id):
        await websocket.send_text("Invalid user ID")
        await websocket.close()
        return

    # Registrar la conexión en el diccionario
    active_connections[user_id] = websocket

    try:
        while True:
            # Esperar un mensaje del cliente
            data = await websocket.receive_text()
            # Puedes agregar la lógica para manejar el mensaje aquí
            # Por ejemplo, enviar el mensaje a un usuario específico
            await send_message_to_user(user_id, data)
    except WebSocketDisconnect:
        # Cuando el usuario se desconecta, eliminar la conexión
        active_connections.pop(user_id, None)
        await websocket.close()

async def send_message_to_user(user_id: str, message: str):
    """Enviar un mensaje a un usuario específico"""
    if user_id in active_connections:
        await active_connections[user_id].send_text(message)

async def validate_user(user_id: str) -> bool:
    """Verificar si el user_id es válido (conectarse a la base de datos o validación del token)"""
    # Aquí puedes consultar tu base de datos o verificar el hash del usuario
    # Ejemplo de validación sencilla:
    return True  # Por ahora, solo retornamos True
