from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import views


urlpatterns = [
    # Sign User
    path("", views.sign, name="sign"),
    path("signin/", views.sign_in, name="sign_in"),
    path("signup/", views.sign_up, name="sign_up"),
    path("signout/", views.sign_out, name="signout"),
    path("reset_password/", views.reset_password, name="reset_password"),
    # Chat
    path("create_room_chat/", views.create_room_chat, name="create_room_chat"),
    path(
        "choose_create_chat/<str:room_name>/",
        views.choose_create_chat,
        name="choose_create_chat",
    ),
    path("enter_key/<str:room_name>/", views.enter_key, name="enter_key"),
    path("chat/<str:room_name>/", views.room, name="room"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
