from enum import Enum
from fastapi import WebSocket
from firebase_admin import firestore
from pydantic import BaseModel

class WebSocketTypes(Enum):
    FRIEND_REQUEST_RECEIVED="FRIEND_REQUEST_RECEIVED"
    FRIEND_REQUEST_ANSWER="FRIEND_REQUEST_ANSWER"

class WebSocketResponse(BaseModel):
    type: WebSocketTypes
    data: dict

class WebSocketManager:
    email_to_id: dict[str, str] = {}
    connections: dict[str, WebSocket] = {}
    def __init__(self):
        self.connections = {}

    def connect(self, user_id: str, websocket: WebSocket):
        self.connections[user_id] = websocket

    def disconnect(self, user_id: str):
        if  user_id in self.connections:
            del self.connections[user_id]

    def get_id_from_email(self, email: str):
        if email in self.email_to_id:
            return self.email_to_id[email]
        try:
            client = firestore.client()
            doc = client.collection("users").where(filter=("email", "==", email)).limit(1).get()[0].to_dict()
            uid: str = doc["uid"]
            self.email_to_id[email] = uid
            return uid
        except:
            return None
        
    async def send_message_to_user_id(self, user_id: str, data: WebSocketResponse):
        if user_id in self.connections:
            web_socket = self.connections[user_id]
            await web_socket.send_json(data.model_dump())
    
    async def send_message(self, user_email: str, data: WebSocketResponse):
        uid = self.get_id_from_email(user_email)
        if uid:
            await self.send_message_to_user_id(uid, data)
        

websocket_manager = WebSocketManager()
