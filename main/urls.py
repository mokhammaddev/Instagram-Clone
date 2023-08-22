from django.urls import path
from .views import LocationListCreateAPIView, LocationRUDAPIView

urlpatterns = [
    path('locatoin/', LocationListCreateAPIView.as_view()),
    path('location/<int:pk>/', LocationRUDAPIView.as_view()),
]