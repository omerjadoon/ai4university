import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import time

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        message = "dummy msg"

        while(1):
             # Send message to WebSocket
            self.send(text_data=json.dumps({
                'message': message
            }))
            time.sleep(5)
        

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = "dummy msg"

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))