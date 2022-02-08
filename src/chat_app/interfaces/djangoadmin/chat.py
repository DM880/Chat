from django.contrib import admin


from chat_app.data.chat.models import UserChat, Chat, ChatSenderMessage, ChatReceiverMessage


class ChatSenderMessageAdmin(admin.TabularInline):
    model = ChatSenderMessage


class ChatReceiverMessageAdmin(admin.TabularInline):
    model = ChatReceiverMessage


class ChatAdmin(admin.ModelAdmin):
    inlines = [ChatSenderMessageAdmin, ChatReceiverMessageAdmin]


admin.site.register(UserChat)
admin.site.register(Chat, ChatAdmin)
