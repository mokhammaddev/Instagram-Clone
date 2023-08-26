from django.contrib import admin
from post.models import Post, Save, Like, Story


admin.site.register(Save)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Story)
