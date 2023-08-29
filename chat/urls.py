from django.urls import path
from chat import views

urlpatterns = [
    # room
    path('room/', views.RoomListCreateAPIView.as_view()),
    path('room/<int:pk>/', views.RoomRUDAPIView.as_view()),
    # message
    path('message/', views.MessageListCreateAPIView.as_view()),
    path('message/<int:pk>/', views.MessageRUDAPIView.as_view()),
]
