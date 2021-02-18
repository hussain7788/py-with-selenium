from django.urls import path
from .views import  RoomView, JoinRoom

urlpatterns = [
    path('', RoomView.as_view()),
    path('join-room', JoinRoom.as_view()),
]