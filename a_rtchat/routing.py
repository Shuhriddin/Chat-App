from django.urls import path
from .consumers import ChatroomConsumer as ChatroomConsumer

websocket_urlpatterns = [
    path('ws/chatroom/<chatroom_name>', ChatroomConsumer.as_asgi())
]