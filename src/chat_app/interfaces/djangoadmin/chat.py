from django.contrib import admin


from chat_app.data.chat.models import Room, Message


class MessageAdmin(admin.TabularInline):
    model = Message


class RoomAdmin(admin.ModelAdmin):
    inlines = [MessageAdmin]


admin.site.register(Room, RoomAdmin)
