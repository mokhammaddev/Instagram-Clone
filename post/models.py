from django.db import models
from account.models import Account
from main.models import Location


def file_path(instance, filename):
    return f"post/{filename}"


def content_path(instance, filename):
    return f"story/{filename}"


class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=file_path)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Save(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ManyToManyField(Post)


class Like(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Story(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.FileField(upload_to=content_path)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


