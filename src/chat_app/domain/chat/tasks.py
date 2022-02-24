from datetime import datetime, timedelta
from dateutil.relativedelta import *
from django.utils import timezone


from chat_app.data.chat.models import Room, Message


def time_check(room):

    last_message = Message.objects.filter(room=room).order_by('timestamp')[0]
    all_messages = Message.objects.filter(room=room)

    time_passed = str(last_message.timestamp+relativedelta(months=+1))
    time_now = str(timezone.now())

    if time_passed < time_now:
        for message in all_messages:
            message.delete()
        room.delete()
        return True

    else:
        return False
