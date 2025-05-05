

from typing import Dict
from fastapi import WebSocket, APIRouter, WebSocketDisconnect

web_socket_router = APIRouter(tags=["WebSocket"])

connected_users: Dict[str, WebSocket] = {}

@web_socket_router.websocket("/message/{user_id}")
async def message_socket(websocket: WebSocket, user_id: str):
    await websocket.accept()
    connected_users[user_id] = websocket

    try:
        while True:
            data = await websocket.receive_json()
            target_user = data.get("to")
            message = data.get("message")

            if target_user in connected_users:
                await connected_users[target_user].send_json({
                    "from": user_id,
                    "message": message
                })
            else:
                await websocket.send_json({
                    "error": f"User {target_user} is not connected."
                })
    except WebSocketDisconnect:
        del connected_users[user_id]
