from django.db import models
from django.contrib.auth.models import AbstractUser


# Расширение модели User
class User(AbstractUser):
    photo = models.ImageField(upload_to='chat/%Y/%m/%d/', blank=True, null=True)


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added', )

