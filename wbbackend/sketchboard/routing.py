from django.urls import path
from . import consumers

websocket_pattern=[
    path('whiteboard/<str:boardName>',consumers.WhiteboardConsumer.as_asgi()),
    path('chat/<str:roomName>',consumers.ChatConsumer.as_asgi()),
]