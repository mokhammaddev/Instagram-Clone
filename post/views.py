from rest_framework import generics
from .models import Post, Save
from .serializers import PostSerializer, SaveSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class SaveListCreateAPIView(generics.ListCreateAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer


class SaveRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer



