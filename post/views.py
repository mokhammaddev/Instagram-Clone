from rest_framework import generics
from .models import Post, Save, Story
from .serializers import PostSerializer, SaveSerializer, StorySerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class SaveListCreateAPIView(generics.ListCreateAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer


class SaveDeleteAPIView(generics.DestroyAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer


class StoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer



