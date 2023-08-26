from rest_framework import serializers
from .models import Save, Post, Story


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image', 'location', 'description', 'created_date')

    def create(self, validated_data):
        request = self.context['request']
        user_id = request.user.id
        return Post.objects.create(user_id=user_id, **validated_data)


class SaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Save
        fields = ('id', 'user', 'post')


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ['id', 'content', 'description', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        user_id = request.user.id
        return Story.objects.create(user_id=user_id, **validated_data)
