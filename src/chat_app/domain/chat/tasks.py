from datetime import datetime, timedelta
from dateutil.relativedelta import *
from django.utils import timezone
import math


from chat_app.data.chat.models import Room, Message


def time_check(room):

    last_message = Message.objects.filter(room=room).order_by("-timestamp").first()

    # if empty no need to delete chat
    if not last_message:
        last_use = room.created

    else:
        last_use = last_message.timestamp

    all_messages = Message.objects.filter(room=room)

    # last message timestamp + 10 days
    time_passed = str(last_use + relativedelta(days=+5))

    time_now = str(timezone.now())

    # check if is passed more than 10 days from last message
    if time_passed < time_now:
        for message in all_messages:
            message.delete()
        room.delete()
        return True

    else:
        return False
