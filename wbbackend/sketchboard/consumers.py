from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync

class WhiteboardConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        print(event['text'])
        self.send({
            'type':'websocket.send',
            'message':'Hi from server'
        })
    
    def websocket_disconnect(self,event):
        pass
    
    
class ChatConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.send({
            'type':'websocket.accept'
        })
        self.room_name=self.scope['url_route']['kwargs']['roomName']
        print("room: ",self.room_name)
        print("channel: ",self.channel_name)
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)

    
    def websocket_receive(self,event):
        print(event['text'])
        self.room_name=self.scope['url_route']['kwargs']['roomName']
        async_to_sync(self.channel_layer.group_send)(self.room_name,{
            'type':'chat.message',
            'message':event['text']
        })
    def chat_message(self,event):
        print(event)
        self.send({
            'type':'websocket.send',
            'text':event['message']
                
        })
    
    def websocket_disconnect(self,event):
        pass