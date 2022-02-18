import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        username = self.scope["user"].username
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        message_user = username + ": " + message

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message_user}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = self.scope["user"].username

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps({"message": message, "username": username})
        )

    # @database_sync_to_async
    # def create_mess_instance(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     room = text_data_json

    #     json_model_data = {
    #         'user':self.scope['user'],
    #         'room': room,
    #         'message': message,
    #     }

    #     mess_instance = Message.objects.create(**json_model_data)

    #     return mess_instance
