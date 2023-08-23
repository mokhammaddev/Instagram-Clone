from django.db import models
from account.models import Account
from main.models import Location


def file_path(instance, filename):
    return f"post/{filename}"


class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=file_path)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Save(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ManyToManyField(Post)




