from channels.generic.websocket import AsyncWebsocketConsumer
import json

from asgiref.sync import sync_to_async

from .models import ConnectedUsers

@sync_to_async
def create_connected_user(user_id, user_channel):
    ConnectedUsers.objects.filter(user_id=user_id).delete()
    
    ConnectedUsers.objects.create(user_id=user_id, user_channel=user_channel)

@sync_to_async
def remove_connected_user(user_id, user_channel):
    ConnectedUsers.objects.filter(user_id=user_id, user_channel=user_channel).delete()

class NotficationHandler(AsyncWebsocketConsumer):   
    async def connect(self):
        await self.accept()

        user_id = self.scope["user"].id

        await create_connected_user(user_id, self.channel_name)

        print(self.channel_name)
        
    async def disconnect(self, close_code):
        user_id = self.scope["user"].id

        await remove_connected_user(user_id, self.channel_name)




    async def send_message(self, text_data):

        text_data_json = json.dumps(text_data)

        await self.send(text_data_json)
