from django.db import models
from django.contrib.auth.models import User
import uuid


class UserChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Chat(models.Model):
    user_chat = models.ForeignKey(
        UserChat, on_delete=models.CASCADE, blank=True, null=True
    )
    user_receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    chat_n = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class ChatSenderMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=True, null=True)
    sender_message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)


class ChatReceiverMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=True, null=True)
    receiver_message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
