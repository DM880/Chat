from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Room(models.Model):
    name = models.CharField(max_length=50)
    private = models.BooleanField(default=False)
    key = models.CharField(null=True,blank=True,max_length=50)

    def __str__(self):
        return f"{self.name}"


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    handler = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
