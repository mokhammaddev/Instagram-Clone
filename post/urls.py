from django.urls import path
from .views import PostListCreateAPIView, PostRUDAPIView, SaveListCreateAPIView, SaveRUDAPIView


urlpatterns = [
    path('post/', PostListCreateAPIView.as_view()),
    path('post/<int:pk>/', PostRUDAPIView.as_view()),
    path('save/', SaveListCreateAPIView.as_view()),
    path('save/<int:pk>/', SaveRUDAPIView.as_view()),
]
