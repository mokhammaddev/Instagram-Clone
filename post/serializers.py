from rest_framework import serializers
from .models import Save, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'image', 'location', 'description', 'created_date')


class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = ('id', 'user', 'post')
